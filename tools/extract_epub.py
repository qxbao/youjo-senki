"""Prepare audited LN 01 locally; never persist source text in the manifest."""

import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import posixpath
import re
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
import zipfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
EPUB_TYPE = "{http://www.idpf.org/2007/ops}type"
OPF = "{http://www.idpf.org/2007/opf}"
CHAPTER_FILES = {
    0: ("Prologue.xhtml", "chapter001.xhtml"),
    1: ("chapter002.xhtml", "chapter003.xhtml", "chapter003a.xhtml",
        "chapter003b.xhtml", "chapter003c.xhtml", "chapter003d.xhtml"),
    2: ("chapter004.xhtml", "chapter005.xhtml", "chapter005a.xhtml", "chapter005b.xhtml"),
    3: ("chapter006.xhtml", "chapter007.xhtml", "chapter007a.xhtml", "chapter007b.xhtml"),
    4: ("chapter008.xhtml", "chapter009.xhtml", "chapter009a.xhtml", "chapter009b.xhtml"),
    5: ("chapter010.xhtml", "chapter011.xhtml", "chapter011a.xhtml", "chapter011b.xhtml"),
}
SCOPE = {f"Text/{name}": chapter for chapter, names in CHAPTER_FILES.items() for name in names}
SCOPE["Text/footnote.xhtml"] = None
EXPECTED_CHAPTER_COUNTS = {0: 154, 1: 364, 2: 436, 3: 813, 4: 524, 5: 828}


def tag(element):
    return element.tag.rsplit("}", 1)[-1]


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def metadata_attributes(element):
    # Explicit allowlist: title/alt/aria-label and arbitrary attributes may contain prose.
    result = {key: element.attrib[key] for key in ("id", "class", "href", "src")
              if key in element.attrib}
    if EPUB_TYPE in element.attrib:
        result["epub_type"] = element.attrib[EPUB_TYPE]
    return result


def walk(element, path=None):
    """Preorder traversal with sibling-indexed DOM paths."""
    path = path or f"/{tag(element)}[1]"
    yield element, path
    counts = Counter()
    for child in element:
        counts[tag(child)] += 1
        yield from walk(child, f"{path}/{tag(child)}[{counts[tag(child)]}]")


def resolve_link(document, href):
    link = urlsplit(href)
    if link.scheme or link.netloc:
        raise ValueError("Unexpected external link in an extracted unit")
    target = posixpath.normpath(posixpath.join(posixpath.dirname(document), unquote(link.path))) if link.path else document
    return target, unquote(link.fragment)


def extract(epub):
    fingerprint = sha256(epub)
    units, records, documents, events = [], [], [], []
    seen = set()
    with zipfile.ZipFile(epub, "r") as archive:
        container = ET.fromstring(archive.read("META-INF/container.xml"))
        opf_path = next(e.attrib["full-path"] for e in container.iter() if tag(e) == "rootfile")
        package = ET.fromstring(archive.read(opf_path))
        base = posixpath.dirname(opf_path)
        items = {e.attrib["id"]: e.attrib for e in package.find(OPF + "manifest")}
        for spine_index, reference in enumerate(package.find(OPF + "spine"), 1):
            item = items[reference.attrib["idref"]]
            relative = posixpath.normpath(item["href"])
            if relative not in SCOPE:
                continue
            if relative in seen or item["media-type"] != "application/xhtml+xml":
                raise ValueError("Unexpected duplicate or non-XHTML scope document")
            seen.add(relative)
            document = posixpath.normpath(posixpath.join(base, relative))
            tree = ET.fromstring(archive.read(document))
            chapter = SCOPE[relative]
            kind = "note" if chapter is None else "story"
            p_ordinal = count = 0
            for element, dom_path in walk(tree):
                if "/body[1]/" not in dom_path:
                    continue
                locator = {"xhtml": document, "spine_index": spine_index, "dom_path": dom_path}
                classes = element.get("class", "").split()
                event_types = []
                if tag(element) == "img":
                    event_types.append("image")
                if "pagebreak" in element.get(EPUB_TYPE, "").split():
                    event_types.append("pagebreak")
                if any(c.startswith("space-break") for c in classes):
                    event_types.append("space_break")
                for event_type in event_types:
                    event = {"type": event_type, "locator": locator,
                             "attributes": metadata_attributes(element)}
                    if event_type == "image":
                        target, _ = resolve_link(document, element.attrib["src"])
                        if target not in archive.namelist():
                            raise ValueError("Missing image resource")
                        event["resource"] = target
                    events.append(event)
                if tag(element) != "p":
                    continue
                p_ordinal += 1  # Count empty p too: IDs are independent of text filtering.
                text = "".join(element.itertext())
                if not text.strip():
                    continue
                locator = {**locator, "p_ordinal": p_ordinal}
                if kind == "note":
                    note_id = element.get("id", "")
                    if not re.fullmatch(r"fn\d{4}fn", note_id):
                        raise ValueError("Unexpected note ID")
                    unit_id = f"YS-LN01/Note/{note_id}"
                else:
                    unit_id = f"YS-LN01/{relative}/p{p_ordinal:06d}"
                inline = []
                links = []
                for child, child_path in walk(element, dom_path):
                    if child is not element:
                        inline.append({"tag": tag(child), "dom_path": child_path,
                                       "attributes": metadata_attributes(child)})
                    if tag(child) == "a" and child.get("href"):
                        target, fragment = resolve_link(document, child.attrib["href"])
                        links.append({"dom_path": child_path, "href": child.attrib["href"],
                                      "target_xhtml": target, "target_id": fragment})
                unit = {"id": unit_id, "kind": kind, "chapter": chapter,
                        "locator": locator, "attributes": metadata_attributes(element),
                        "inline_markup": inline, "links": links}
                units.append(unit)
                local_element = deepcopy(element)
                local_element.tail = None
                records.append({"id": unit_id, "kind": kind, "locator": locator,
                                "source_sha256": fingerprint, "text": text,
                                "xhtml": ET.tostring(local_element, encoding="unicode")})
                count += 1
            documents.append({"xhtml": document, "spine_index": spine_index,
                              "linear": reference.get("linear", "yes"),
                              "kind": kind, "chapter": chapter, "unit_count": count})
    if seen != set(SCOPE):
        raise ValueError("Audited LN 01 scope documents are missing")
    chapter_counts = Counter(u["chapter"] for u in units if u["kind"] == "story")
    notes = [u for u in units if u["kind"] == "note"]
    if dict(chapter_counts) != EXPECTED_CHAPTER_COUNTS or len(notes) != 20:
        raise ValueError("Unit counts differ from the LN 01 audit")
    # Map note destinations and inline call anchors to containing units.
    anchors = {}
    for unit in units:
        nodes = [{"attributes": unit["attributes"]}, *unit["inline_markup"]]
        for node in nodes:
            if "id" in node["attributes"]:
                key = (unit["locator"]["xhtml"], node["attributes"]["id"])
                if key in anchors:
                    raise ValueError("Duplicate anchor in extracted scope")
                anchors[key] = unit["id"]
    for unit in units:
        for link in unit["links"]:
            target = anchors.get((link["target_xhtml"], link["target_id"]))
            if target is None:
                raise ValueError("Link target outside the extracted units")
            link["target_unit"] = target
    if sha256(epub) != fingerprint:
        raise ValueError("EPUB changed while reading")
    manifest = {"schema_version": 1, "volume": "vol-01",
                "source": {"filename": epub.name, "sha256": fingerprint, "opf": opf_path},
                "counts": {"story": 3119, "note": 20, "total": len(units)},
                "documents": documents, "units": units, "events": events}
    return manifest, records


def ensure_local_source(root):
    relative = "work/vol-01/source.jsonl"
    tracked = subprocess.run(["git", "ls-files", "--", "work/"], cwd=root,
                             check=True, capture_output=True, text=True)
    if tracked.stdout:
        raise ValueError("work/ contains Git-tracked files; refusing to write source")
    ignored = subprocess.run(["git", "check-ignore", "-q", "--", relative], cwd=root)
    if ignored.returncode != 0:
        raise ValueError("Local source path must be ignored by Git")
    for path in (root / "work", root / "work/vol-01", root / relative,
                 root / "segments", root / "segments/vol-01",
                 root / "segments/vol-01/manifest.yml"):
        if path.is_symlink():
            raise ValueError("Refusing symlink output paths")


def check_fingerprint(manifest_path, fingerprint, force):
    if manifest_path.exists():
        previous = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        if previous["source"]["sha256"] != fingerprint and not force:
            raise ValueError("EPUB SHA-256 changed; use --force only after reviewing the new source")


def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(content)
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("volume", choices=["vol-01"])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true", help="Allow a reviewed source fingerprint change")
    args = parser.parse_args()
    try:
        config = yaml.safe_load((ROOT / "project.local.yml").read_text(encoding="utf-8"))
        source_dir = (ROOT / config["source_dir"]).resolve()
        if source_dir.is_relative_to(ROOT):
            raise ValueError("EPUB sources must remain outside this repository")
        candidates = [p for p in source_dir.iterdir() if p.is_file()
                      and p.suffix.lower() == ".epub" and re.search(r"\bLN[ _-]*0?1\b", p.name, re.I)]
        if len(candidates) != 1:
            raise ValueError("Expected exactly one LN 01 EPUB in source_dir")
        ensure_local_source(ROOT)
        manifest_path = ROOT / "segments/vol-01/manifest.yml"
        check_fingerprint(manifest_path, sha256(candidates[0]), args.force)
        manifest, records = extract(candidates[0])
        check_fingerprint(manifest_path, manifest["source"]["sha256"], args.force)
        if not args.dry_run:
            ensure_local_source(ROOT)
            atomic_write(ROOT / "work/vol-01/source.jsonl",
                         "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))
            atomic_write(manifest_path, yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False))
        print(f"{'DRY RUN (no writes)' if args.dry_run else 'EXTRACTED'}: story=3119 notes=20 total=3139")
        print(f"Metadata: documents={len(manifest['documents'])} events={len(manifest['events'])}")
    except (ValueError, OSError, KeyError, TypeError, ET.ParseError, zipfile.BadZipFile,
            yaml.YAMLError, subprocess.CalledProcessError):
        # Parser errors and offending values may contain source prose: do not print them.
        parser.exit(1, "Extraction refused: check local config, scope/counts, SHA-256 and Git ignore rules.\n")


if __name__ == "__main__":
    main()
