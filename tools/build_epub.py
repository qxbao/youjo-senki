#!/usr/bin/env python3
"""Build Vietnamese EPUB 3 files from Git-tracked manifest and translation JSONL files.

Never reads or bundles copyrighted source EPUB files or work/ files.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import sys
import zipfile

import yaml

ROOT = Path(__file__).resolve().parents[1]

VOLUME_TITLES_VI = {
    "vol-01": "Tập 01 — Deus lo vult",
    "vol-02": "Tập 02 — Plus Ultra",
    "vol-03": "Tập 03 — The Finest Hour",
    "vol-04": "Tập 04 — Dabit deus his quoque finem",
    "vol-05": "Tập 05 — Abyssus abyssum invocat",
    "vol-06": "Tập 06 — Nil admirari",
    "vol-07": "Tập 07 — Ut sementem feceris, ita metes",
    "vol-08": "Tập 08 — In omnia paratus",
    "vol-09": "Tập 09 — Omnes una manet nox",
    "vol-10": "Tập 10 — Viribus unitis",
    "vol-11": "Tập 11 — Alea iacta est",
    "vol-12": "Tập 12 — Mundus vult decipi, ergo decipiatur",
    "vol-13": "Tập 13 — Dum spiro, spero",
    "vol-14": "Tập 14 — Audaces fortuna iuvat",
}

BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)")


def render_inline_markdown(text: str) -> str:
    """Escape XML entities and convert **bold** / *italic* Markdown to XHTML tags."""
    escaped = html.escape(text, quote=False)
    escaped = BOLD_RE.sub(r"<strong>\1</strong>", escaped)
    escaped = ITALIC_RE.sub(r"<em>\1</em>", escaped)
    return escaped


def load_volume_translations(vol: str) -> dict[str, dict]:
    trans_dir = ROOT / "translations" / vol
    if not trans_dir.is_dir():
        return {}
    by_id: dict[str, dict] = {}
    for path in sorted(trans_dir.glob("*.jsonl")):
        for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line:
                continue
            row = json.loads(line)
            seg_id = row.get("segment_id")
            if not seg_id:
                raise ValueError(f"{path}:{line_no} missing segment_id")
            by_id[seg_id] = row
    return by_id


def check_volume_status(vol: str) -> dict:
    manifest_path = ROOT / "segments" / vol / "manifest.yml"
    if not manifest_path.is_file():
        return {"volume": vol, "exists": False}
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    story_units = [u for u in manifest.get("units", []) if u.get("kind") == "story"]
    translations = load_volume_translations(vol)

    translated_count = 0
    reviewed_count = 0
    for u in story_units:
        row = translations.get(u["id"])
        if row and isinstance(row.get("translation"), str) and row["translation"].strip():
            translated_count += 1
            if row.get("status") in ("reviewed", "approved"):
                reviewed_count += 1

    total = len(story_units)
    return {
        "volume": vol,
        "exists": True,
        "story_units": total,
        "translated_units": translated_count,
        "reviewed_units": reviewed_count,
        "is_complete": total > 0 and translated_count == total,
        "is_fully_reviewed": total > 0 and reviewed_count == total,
    }


def build_css() -> str:
    return """@charset "UTF-8";
body {
  font-family: "Noto Serif", "Literata", "Georgia", serif;
  line-height: 1.65;
  margin: 1.2em;
  color: #111111;
}
h1, h2 {
  font-family: "Noto Sans", "Helvetica Neue", sans-serif;
  text-align: center;
  margin: 1.5em 0 1em 0;
  line-height: 1.3;
}
p {
  margin: 0.35em 0;
  text-indent: 1.5em;
  text-align: justify;
}
p.noindent, p.sect {
  text-indent: 0;
}
p.sect {
  font-weight: bold;
  margin-top: 1.2em;
  margin-bottom: 0.5em;
}
p.space-break, p.space-break1, p.space-break2 {
  margin-top: 1.6em;
  text-indent: 0;
}
div.scene-break {
  text-align: center;
  margin: 1.2em 0;
  letter-spacing: 0.4em;
  color: #555555;
}
.title-box {
  text-align: center;
  margin-top: 18%;
}
.title-main {
  font-size: 1.8em;
  font-weight: bold;
  margin-bottom: 0.4em;
}
.title-sub {
  font-size: 1.25em;
  margin-bottom: 1.5em;
}
.title-meta {
  font-size: 0.95em;
  color: #444444;
  text-indent: 0;
  text-align: center;
}
"""


def build_epub(vol: str, output_path: Path | None = None, require_reviewed: bool = False) -> Path:
    manifest_path = ROOT / "segments" / vol / "manifest.yml"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")

    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    story_units = [u for u in manifest.get("units", []) if u.get("kind") == "story"]
    if not story_units:
        raise ValueError(f"No story units in {manifest_path}")

    translations = load_volume_translations(vol)
    missing = [u["id"] for u in story_units if u["id"] not in translations]
    if missing:
        raise ValueError(
            f"{vol} is incomplete: missing {len(missing)}/{len(story_units)} story units "
            f"(first missing: {missing[0]})"
        )

    if require_reviewed:
        unreviewed = [
            u["id"]
            for u in story_units
            if translations[u["id"]].get("status") not in ("reviewed", "approved")
        ]
        if unreviewed:
            raise ValueError(
                f"{vol} has {len(unreviewed)} unreviewed units (first: {unreviewed[0]})"
            )

    # Collect space_break events keyed by (xhtml, dom_path)
    space_breaks = set()
    for ev in manifest.get("events", []):
        if ev.get("type") == "space_break":
            loc = ev.get("locator", {})
            if loc.get("xhtml") and loc.get("dom_path"):
                space_breaks.add((loc["xhtml"], loc["dom_path"]))

    # Group units by chapter number in spine order
    chapters: dict[int, list[dict]] = defaultdict(list)
    chapter_order: list[int] = []
    for u in story_units:
        ch = int(u.get("chapter", 0))
        if ch not in chapters:
            chapter_order.append(ch)
        chapters[ch].append(u)

    vol_title = VOLUME_TITLES_VI.get(vol, f"Tập {vol.split('-')[-1]}")
    book_title = f"Tanya Chiến Ký (Youjo Senki) — {vol_title}"
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    book_uuid = f"urn:uuid:{hashlib.sha256(f'youjo-senki-vi-{vol}'.encode()).hexdigest()[:32]}"

    if output_path is None:
        output_path = ROOT / "output" / f"youjo-senki-vi-{vol}.epub"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    chapter_files: list[tuple[str, str, str]] = []
    for ch_num in chapter_order:
        ch_units = chapters[ch_num]
        ch_label = "Mở đầu (Prologue)" if ch_num == 0 else f"Chương {ch_num:02d}"
        first_text = translations[ch_units[0]["id"]]["translation"].strip()
        if len(first_text) <= 90 and not first_text.endswith("."):
            ch_heading = f"{ch_label}: {first_text}"
        else:
            ch_heading = ch_label

        body_lines = [f"  <h1>{html.escape(ch_label)}</h1>"]
        prev_xhtml = None
        for u in ch_units:
            loc = u.get("locator", {})
            xhtml_doc = loc.get("xhtml")
            dom_path = loc.get("dom_path")
            attrs = u.get("attributes") or {}
            css_class = attrs.get("class", "")

            if prev_xhtml is not None and xhtml_doc != prev_xhtml:
                body_lines.append('  <div class="scene-break">* * *</div>')
            elif (xhtml_doc, dom_path) in space_breaks or "space-break" in css_class:
                body_lines.append('  <div class="scene-break">* * *</div>')
            prev_xhtml = xhtml_doc

            text_html = render_inline_markdown(translations[u["id"]]["translation"].strip())
            class_attr = f' class="{html.escape(css_class, quote=True)}"' if css_class else ""
            id_attr = f' id="{html.escape(u["id"].replace("/", "_"), quote=True)}"'
            body_lines.append(f"  <p{id_attr}{class_attr}>{text_html}</p>")

        fname = f"chapter-{ch_num:02d}.xhtml"
        xhtml_content = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="vi" lang="vi">
<head>
  <meta charset="utf-8" />
  <title>{html.escape(ch_heading)}</title>
  <link rel="stylesheet" type="text/css" href="../style/main.css" />
</head>
<body>
{chr(10).join(body_lines)}
</body>
</html>
"""
        chapter_files.append((fname, ch_heading, xhtml_content))

    titlepage_xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="vi" lang="vi">
<head>
  <meta charset="utf-8" />
  <title>{html.escape(book_title)}</title>
  <link rel="stylesheet" type="text/css" href="../style/main.css" />
</head>
<body>
  <div class="title-box">
    <div class="title-main">TANYA CHIẾN KÝ (YOUJO SENKI)</div>
    <div class="title-sub">{html.escape(vol_title)}</div>
    <p class="title-meta">Nguyên tác: Carlo Zen</p>
    <p class="title-meta">Bản dịch tiếng Việt: Youjo Senki VI Translation Pipeline</p>
    <p class="title-meta">Số đoạn dịch: {len(story_units)}</p>
  </div>
</body>
</html>
"""

    nav_items = "\n".join(
        f'        <li><a href="Text/{fname}">{html.escape(heading)}</a></li>'
        for fname, heading, _ in chapter_files
    )
    nav_xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="vi" lang="vi">
<head>
  <meta charset="utf-8" />
  <title>Mục lục — {html.escape(book_title)}</title>
  <link rel="stylesheet" type="text/css" href="style/main.css" />
</head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Mục lục</h1>
    <ol>
      <li><a href="Text/titlepage.xhtml">Trang tiêu đề</a></li>
{nav_items}
    </ol>
  </nav>
</body>
</html>
"""

    ncx_points = []
    for idx, (fname, heading, _) in enumerate(chapter_files, 2):
        ncx_points.append(
            f"""    <navPoint id="navPoint-{idx}" playOrder="{idx}">
      <navLabel><text>{html.escape(heading)}</text></navLabel>
      <content src="Text/{fname}"/>
    </navPoint>"""
        )
    toc_ncx = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{book_uuid}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>{html.escape(book_title)}</text></docTitle>
  <navMap>
    <navPoint id="navPoint-1" playOrder="1">
      <navLabel><text>Trang tiêu đề</text></navLabel>
      <content src="Text/titlepage.xhtml"/>
    </navPoint>
{chr(10).join(ncx_points)}
  </navMap>
</ncx>
"""

    manifest_items = [
        '    <item id="css" href="style/main.css" media-type="text/css"/>',
        '    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '    <item id="titlepage" href="Text/titlepage.xhtml" media-type="application/xhtml+xml"/>',
    ]
    spine_items = [
        '    <itemref idref="titlepage"/>',
        '    <itemref idref="nav"/>',
    ]
    for idx, (fname, _, _) in enumerate(chapter_files, 1):
        item_id = f"ch{idx:02d}"
        manifest_items.append(
            f'    <item id="{item_id}" href="Text/{fname}" media-type="application/xhtml+xml"/>'
        )
        spine_items.append(f'    <itemref idref="{item_id}"/>')

    content_opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId" xml:lang="vi">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">{book_uuid}</dc:identifier>
    <dc:title>{html.escape(book_title)}</dc:title>
    <dc:creator>Carlo Zen</dc:creator>
    <dc:language>vi</dc:language>
    <meta property="dcterms:modified">{now_iso}</meta>
  </metadata>
  <manifest>
{chr(10).join(manifest_items)}
  </manifest>
  <spine toc="ncx">
{chr(10).join(spine_items)}
  </spine>
</package>
"""

    container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/epub+zip"/>
  </rootfiles>
</container>
"""

    with zipfile.ZipFile(output_path, "w") as zf:
        zf.writestr("mimetype", b"application/epub+zip", compress_type=zipfile.ZIP_STORED)
        zf.writestr("META-INF/container.xml", container_xml.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/style/main.css", build_css().encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/Text/titlepage.xhtml", titlepage_xhtml.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/toc.ncx", toc_ncx.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/content.opf", content_opf.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        for fname, _, content in chapter_files:
            zf.writestr(f"OEBPS/Text/{fname}", content.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)

    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Vietnamese EPUB from translated JSONL batches.")
    parser.add_argument("volumes", nargs="*", help="Volume IDs (e.g. vol-02 vol-03) or omit with --all-completed")
    parser.add_argument("--all-completed", action="store_true", help="Build all volumes with 100%% story unit coverage")
    parser.add_argument("--require-reviewed", action="store_true", help="Only build volumes where 100%% of story units are reviewed/approved")
    parser.add_argument("--list-status", action="store_true", help="List completion status of all volumes in segments/")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "output", help="Output directory for built EPUBs")
    args = parser.parse_args()

    seg_dirs = sorted(p.name for p in (ROOT / "segments").glob("vol-*") if (p / "manifest.yml").is_file())

    if args.list_status:
        statuses = [check_volume_status(v) for v in seg_dirs]
        print(json.dumps(statuses, indent=2, ensure_ascii=False))
        return 0

    targets = list(args.volumes)
    if args.all_completed:
        for v in seg_dirs:
            st = check_volume_status(v)
            if st.get("is_complete") and (not args.require_reviewed or st.get("is_fully_reviewed")):
                if v not in targets:
                    targets.append(v)

    if not targets:
        print("No volumes specified or matched --all-completed.", file=sys.stderr)
        return 1

    built = []
    for vol in targets:
        out_file = args.output_dir / f"youjo-senki-vi-{vol}.epub"
        built_path = build_epub(vol, output_path=out_file, require_reviewed=args.require_reviewed)
        st = check_volume_status(vol)
        built.append({
            "volume": vol,
            "output": str(built_path.relative_to(ROOT) if built_path.is_relative_to(ROOT) else built_path),
            "size_bytes": built_path.stat().st_size,
            "story_units": st["story_units"],
            "reviewed_units": st["reviewed_units"],
        })
        print(f"BUILT: {built_path} ({built_path.stat().st_size} bytes, units={st['story_units']}, reviewed={st['reviewed_units']}/{st['story_units']})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
