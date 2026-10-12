"""Prepare EPUB volumes locally; source text stays out of the manifest and Git."""

import argparse
from collections import Counter
from copy import deepcopy
import hashlib
from html.entities import html5
import json
from pathlib import Path
import posixpath
import re
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
import zipfile

from lxml import etree as LET
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
EXCLUDED_EPUB_TYPES = {
    "cover", "toc", "list", "copyright-page", "frontmatter", "backmatter",
    "appendix", "colophon", "landmarks",
}
EXCLUDED_PATH = re.compile(
    r"(?:^|/)(?:cover|titlepage|nav|toc|copyright|copyrightpage|newsletter\w*|"
    r"afterword|appendix|colophon)(?:[_ .-]|\.|$)", re.I
)
NOTE_PATH = re.compile(r"(?:footnotes?|endnotes?|_split_\d{3})(?:[_ .-]|\.|$)", re.I)
VOLUME_FILENAME = re.compile(r"\bLN[ _-]*0*(\d{1,2})\b", re.I)
HTML_ENTITY = re.compile(rb"&([A-Za-z][A-Za-z0-9]+);")


def tag(element):
    return element.tag.rsplit("}", 1)[-1]


def epub_type_tokens(element):
    value = element.attrib.get(EPUB_TYPE) or element.attrib.get("epub:type") or ""
    return set(value.split())


def parse_xhtml(data):
    """Parse XML XHTML, tolerating common named HTML entities without touching the EPUB."""
    names = {key[:-1]: value for key, value in html5.items() if key.endswith(";")}

    def entity(match):
        value = names.get(match.group(1).decode("ascii"))
        if value is None:
            return match.group(0)
        return b"".join(f"&#{ord(char)};".encode("ascii") for char in value)

    normalized = HTML_ENTITY.sub(entity, data)
    try:
        return ET.fromstring(normalized)
    except ET.ParseError:
        parser = LET.HTMLParser(recover=True, no_network=True)
        root = LET.fromstring(normalized, parser=parser)
        if root is None:
            raise ValueError("XHTML document could not be parsed")
        return root


def serialize_element(element):
    if element.__class__.__module__.startswith("lxml"):
        return LET.tostring(element, encoding="unicode", method="html")
    return ET.tostring(element, encoding="unicode")


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
    types = epub_type_tokens(element)
    if types:
        result["epub_type"] = " ".join(sorted(types))
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


def toc_entries(archive, package, base):
    """Return top-level EPUB navigation entries without persisting their labels."""
    manifest = {item.attrib["id"]: item.attrib
                for item in package.find(OPF + "manifest")}
    nav_items = [item for item in manifest.values()
                 if "nav" in item.get("properties", "").split()]
    for item in nav_items:
        nav_path = posixpath.normpath(posixpath.join(base, item["href"]))
        nav_tree = ET.fromstring(archive.read(nav_path))
        for nav in nav_tree.iter():
            if tag(nav) != "nav" or "toc" not in epub_type_tokens(nav):
                continue
            ordered = []
            ol = next((child for child in nav if tag(child) == "ol"), None)
            if ol is None:
                continue
            for li in (child for child in ol if tag(child) == "li"):
                anchor = next((element for element in li.iter()
                               if element is not li and tag(element) == "a"
                               and element.get("href")), None)
                if anchor is None:
                    continue
                label = " ".join("".join(anchor.itertext()).split())
                target, fragment = resolve_link(nav_path, anchor.get("href"))
                ordered.append((target, fragment, label))
            if ordered:
                return ordered
    spine = package.find(OPF + "spine")
    ncx_id = spine.get("toc")
    ncx_item = manifest.get(ncx_id) if ncx_id else None
    if ncx_item:
        ncx_path = posixpath.normpath(posixpath.join(base, ncx_item["href"]))
        ncx_tree = ET.fromstring(archive.read(ncx_path))
        nav_map = next((node for node in ncx_tree.iter() if tag(node) == "navMap"), None)
        if nav_map is not None:
            ordered = []
            for point in (child for child in nav_map if tag(child) == "navPoint"):
                content = next((child for child in point if tag(child) == "content"), None)
                label_node = next((child for child in point if tag(child) == "navLabel"), None)
                source = content.get("src") if content is not None else None
                if not source:
                    continue
                label = " ".join("".join(label_node.itertext()).split()) if label_node is not None else ""
                target, fragment = resolve_link(ncx_path, source)
                ordered.append((target, fragment, label))
            if ordered:
                return ordered
    return []


def chapter_number(label, fallback):
    normalized = label.casefold()
    if re.search(r"\b(prologue|preface|prelude)\b", normalized):
        return 0
    match = re.search(r"\bchapter\s+([0-9]+|[ivxlcdm]+)\b", normalized)
    if not match:
        return fallback
    value = match.group(1)
    if value.isdecimal():
        return int(value)
    values = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
    total = previous = 0
    for char in reversed(value):
        current = values[char]
        total += -current if current < previous else current
        previous = max(previous, current)
    return total


def fragment_paragraph_ordinal(entry, fragment):
    """Map a navigation fragment to its containing/next paragraph boundary."""
    nodes = list(walk(entry["tree"]))
    target_index = next((i for i, (element, _) in enumerate(nodes)
                         if element.get("id") == fragment), None)
    if target_index is None:
        raise ValueError("Navigation fragment is missing from its XHTML document")
    target_path = nodes[target_index][1]
    paragraphs = []
    ordinal = 0
    for i, (element, path) in enumerate(nodes):
        if "/body[1]/" not in path or tag(element) != "p":
            continue
        ordinal += 1
        paragraphs.append((i, path, ordinal))
    if not paragraphs:
        return 0
    containing = [value for value in paragraphs
                  if target_path == value[1] or target_path.startswith(value[1] + "/")]
    if containing:
        return containing[-1][2]
    following = next((value[2] for value in paragraphs if value[0] > target_index), None)
    if following is None:
        return 0
    return following


def extract_generic(epub, volume):
    """Extract story chapters using spine order, EPUB type markers, and TOC/NCX boundaries."""
    fingerprint = sha256(epub)
    volume_number = int(volume.removeprefix("vol-"))
    prefix = f"YS-LN{volume_number:02d}"
    units, records, documents, events = [], [], [], []
    with zipfile.ZipFile(epub, "r") as archive:
        container = ET.fromstring(archive.read("META-INF/container.xml"))
        opf_path = next(e.attrib["full-path"] for e in container.iter() if tag(e) == "rootfile")
        package = ET.fromstring(archive.read(opf_path))
        base = posixpath.dirname(opf_path)
        manifest = {item.attrib["id"]: item.attrib
                    for item in package.find(OPF + "manifest")}
        spine = package.find(OPF + "spine")
        toc = toc_entries(archive, package, base)
        spine_docs = []
        for spine_index, reference in enumerate(spine, 1):
            item = manifest[reference.attrib["idref"]]
            if item.get("media-type") != "application/xhtml+xml":
                continue
            relative = posixpath.normpath(item["href"])
            document = posixpath.normpath(posixpath.join(base, relative))
            tree = parse_xhtml(archive.read(document))
            all_types = set().union(*(epub_type_tokens(element) for element in tree.iter()))
            body = next((element for element in tree.iter() if tag(element) == "body"), tree)
            body_types = epub_type_tokens(body)
            path_excluded = bool(EXCLUDED_PATH.search(relative))
            note_doc = bool({"footnote", "endnote"} & all_types) or bool(NOTE_PATH.search(relative))
            excluded = path_excluded or bool(EXCLUDED_EPUB_TYPES & all_types)
            spine_docs.append({
                "spine_index": spine_index, "reference": reference, "item": item,
                "relative": relative, "document": document, "tree": tree,
                "body": body, "body_types": body_types, "all_types": all_types,
                "note": note_doc, "excluded": excluded,
            })

        by_document = {entry["document"]: entry for entry in spine_docs}
        boundaries = []
        fallback = 1
        for target, fragment, label in toc:
            entry = by_document.get(target)
            if entry is None:
                continue
            if entry["excluded"] or entry["note"]:
                boundaries.append((entry["spine_index"], 0, None, target, fragment))
                continue
            chapter = chapter_number(label, fallback)
            if chapter:
                fallback = max(fallback, chapter + 1)
            paragraph = fragment_paragraph_ordinal(entry, fragment) if fragment else 0
            boundaries.append((entry["spine_index"], paragraph, chapter, target, fragment))
        boundaries.sort(key=lambda value: (value[0], value[1]))
        if not any(chapter is not None for _, _, chapter, _, _ in boundaries):
            # NCX-less books can still be prepared when the EPUB marks chapter documents.
            for entry in spine_docs:
                if (not entry["excluded"] and not entry["note"]
                        and "chapter" in entry["all_types"]):
                    boundaries.append((entry["spine_index"], 1, fallback,
                                       entry["document"], ""))
                    fallback += 1
            boundaries.sort(key=lambda value: (value[0], value[1]))
        if not any(chapter is not None for _, _, chapter, _, _ in boundaries):
            raise ValueError("No unambiguous chapter markers in EPUB navigation or spine")

        active_chapter = None
        boundary_by_doc = {}
        for value in boundaries:
            boundary_by_doc.setdefault(value[0], []).append(value)
        for entry in spine_docs:
            spine_index = entry["spine_index"]
            doc_boundaries = sorted(boundary_by_doc.get(spine_index, []), key=lambda value: value[1])
            for _, paragraph, chapter, _, _ in doc_boundaries:
                if paragraph == 0:
                    active_chapter = chapter
            count = 0
            paragraph_chapters = set()
            p_ordinal = 0
            for element, dom_path in walk(entry["tree"]):
                if "/body[1]/" not in dom_path or tag(element) != "p":
                    continue
                p_ordinal += 1
                for _, boundary_ordinal, chapter, _, _ in doc_boundaries:
                    if boundary_ordinal == p_ordinal:
                        active_chapter = chapter
                kind = "note" if entry["note"] else "story" if active_chapter is not None and not entry["excluded"] else None
                text = "".join(element.itertext())
                if kind is None or not text.strip():
                    continue
                locator = {"xhtml": entry["document"], "spine_index": spine_index,
                           "dom_path": dom_path, "p_ordinal": p_ordinal}
                if kind == "note":
                    unit_id = f"{prefix}/Note/{entry['relative']}/p{p_ordinal:06d}"
                    unit_chapter = None
                else:
                    unit_id = f"{prefix}/{entry['relative']}/p{p_ordinal:06d}"
                    unit_chapter = active_chapter
                    paragraph_chapters.add(active_chapter)
                unit = {"id": unit_id, "kind": kind, "chapter": unit_chapter,
                        "locator": locator, "attributes": metadata_attributes(element),
                        "inline_markup": [], "links": []}
                for child, child_path in walk(element, dom_path):
                    if child is element:
                        continue
                    unit["inline_markup"].append({"tag": tag(child), "dom_path": child_path,
                                                  "attributes": metadata_attributes(child)})
                    if tag(child) == "a" and child.get("href"):
                        href = child.get("href")
                        link = urlsplit(href)
                        if link.scheme or link.netloc:
                            continue
                        target_path, target_id = resolve_link(entry["document"], href)
                        unit["links"].append({"dom_path": child_path, "href": child.get("href"),
                                              "target_xhtml": target_path, "target_id": target_id})
                local_element = deepcopy(element)
                local_element.tail = None
                records.append({"id": unit_id, "kind": kind, "locator": locator,
                                "source_sha256": fingerprint, "text": text,
                                "xhtml": serialize_element(local_element)})
                units.append(unit)
                count += 1
            if not entry["excluded"] and (entry["note"] or active_chapter is not None
                                           or paragraph_chapters):
                for element, dom_path in walk(entry["body"]):
                    locator = {"xhtml": entry["document"], "spine_index": spine_index,
                               "dom_path": dom_path}
                    classes = element.get("class", "").split()
                    event_types = []
                    if tag(element) == "img":
                        event_types.append("image")
                    if "pagebreak" in epub_type_tokens(element):
                        event_types.append("pagebreak")
                    if any(value.startswith("space-break") for value in classes):
                        event_types.append("space_break")
                    for event_type in event_types:
                        event = {"type": event_type, "locator": locator,
                                 "attributes": metadata_attributes(element)}
                        if event_type == "image":
                            target, _ = resolve_link(entry["document"], element.attrib["src"])
                            if target not in archive.namelist():
                                raise ValueError("Missing image resource")
                            event["resource"] = target
                        events.append(event)
            documents.append({"xhtml": entry["document"], "spine_index": spine_index,
                              "linear": entry["reference"].get("linear", "yes"),
                              "kind": "note" if entry["note"] else "story" if paragraph_chapters else "excluded",
                              "chapter": next(iter(paragraph_chapters)) if len(paragraph_chapters) == 1 else None,
                              "unit_count": count,
                              "epub_type": sorted(entry["all_types"])})
        # Resolve only links whose local target corresponds to an extracted paragraph.
        anchors = {}
        for unit in units:
            nodes = [{"attributes": unit["attributes"]}, *unit["inline_markup"]]
            for node in nodes:
                anchor_id = node["attributes"].get("id")
                if anchor_id:
                    anchors[(unit["locator"]["xhtml"], anchor_id)] = unit["id"]
        for unit in units:
            for link in unit["links"]:
                target = anchors.get((link["target_xhtml"], link["target_id"]))
                if target is not None:
                    link["target_unit"] = target
        if sha256(epub) != fingerprint:
            raise ValueError("EPUB changed while reading")
    story_count = sum(unit["kind"] == "story" for unit in units)
    note_count = sum(unit["kind"] == "note" for unit in units)
    chapter_counts = Counter(unit["chapter"] for unit in units if unit["kind"] == "story")
    manifest = {"schema_version": 1, "volume": volume,
                "source": {"filename": epub.name, "sha256": fingerprint, "opf": opf_path},
                "counts": {"story": story_count, "note": note_count,
                           "total": len(units)},
                "chapter_counts": dict(sorted(chapter_counts.items())),
                "scope_method": "epub3_toc_or_ncx_and_spine_types_fail_closed",
                "documents": documents, "units": units, "events": events}
    if story_count == 0:
        raise ValueError("No story paragraphs found in selected EPUB scope")
    return manifest, records


def ensure_local_source(root, volume="vol-01"):
    relative = f"work/{volume}/source.jsonl"
    tracked = subprocess.run(["git", "ls-files", "--", "work/"], cwd=root,
                             check=True, capture_output=True, text=True)
    if tracked.stdout:
        raise ValueError("work/ contains Git-tracked files; refusing to write source")
    ignored = subprocess.run(["git", "check-ignore", "-q", "--", relative], cwd=root)
    if ignored.returncode != 0:
        raise ValueError("Local source path must be ignored by Git")
    for path in (root / "work", root / f"work/{volume}", root / relative,
                 root / "segments", root / f"segments/{volume}",
                 root / f"segments/{volume}/manifest.yml"):
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
    parser.add_argument("volume", help="Volume key such as vol-02")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true", help="Allow a reviewed source fingerprint change")
    args = parser.parse_args()
    try:
        if not re.fullmatch(r"vol-\d{2}", args.volume):
            raise ValueError("Volume must use the vol-NN format")
        config = yaml.safe_load((ROOT / "project.local.yml").read_text(encoding="utf-8"))
        source_dir = (ROOT / config["source_dir"]).resolve()
        if source_dir.is_relative_to(ROOT):
            raise ValueError("EPUB sources must remain outside this repository")
        volume_number = int(args.volume.removeprefix("vol-"))
        candidates = [p for p in source_dir.iterdir() if p.is_file()
                      and p.suffix.lower() == ".epub"
                      and (match := VOLUME_FILENAME.search(p.name))
                      and int(match.group(1)) == volume_number]
        if len(candidates) != 1:
            raise ValueError("Expected exactly one matching volume EPUB in source_dir")
        ensure_local_source(ROOT, args.volume)
        manifest_path = ROOT / f"segments/{args.volume}/manifest.yml"
        check_fingerprint(manifest_path, sha256(candidates[0]), args.force)
        if args.volume == "vol-01":
            manifest, records = extract(candidates[0])
        else:
            manifest, records = extract_generic(candidates[0], args.volume)
        check_fingerprint(manifest_path, manifest["source"]["sha256"], args.force)
        if not args.dry_run:
            ensure_local_source(ROOT, args.volume)
            atomic_write(ROOT / f"work/{args.volume}/source.jsonl",
                         "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))
            atomic_write(manifest_path, yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False))
        print(f"{'DRY RUN (no writes)' if args.dry_run else 'EXTRACTED'}: "
              f"{args.volume}: story={manifest['counts']['story']} "
              f"notes={manifest['counts']['note']} total={manifest['counts']['total']}")
        print(f"Metadata: documents={len(manifest['documents'])} events={len(manifest['events'])}")
    except (ValueError, OSError, KeyError, TypeError, ET.ParseError, zipfile.BadZipFile,
            yaml.YAMLError, subprocess.CalledProcessError):
        # Parser errors and offending values may contain source prose: do not print them.
        parser.exit(1, "Extraction refused: check local config, scope/counts, SHA-256 and Git ignore rules.\n")


if __name__ == "__main__":
    main()
