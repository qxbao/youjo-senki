"""Plan Chapter 0 batches locally; emit source only under Git-ignored work/."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

import yaml

from extract_epub import ROOT, atomic_write, ensure_local_source, sha256
from validate_segments import validate

MIN_WORDS = 600
MAX_WORDS = 900
TARGET_WORDS = 750
# Match the pilot convention: contractions/hyphenated words count once.
WORD_PATTERN = r"[A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*"
CANON_PATHS = (
    "canon/glossary.yml", "canon/style-guide.md", "canon/characters.yml",
    "canon/decisions.md", "canon/glossary-pending.yml",
)
CHECKPOINTS = {
    "meaning": "Giữ nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic và thời gian của giả định.",
    "pronouns": "Theo DEC-P01-001; phân biệt trần thuật và nội tâm, không suy diễn quan hệ khi thiếu ngữ cảnh.",
    "emphasis": "Theo DEC-P01-002; dùng *...* trong translation chỉ khi nguồn có nhấn mạnh tương ứng.",
    "pending_terms": "Tra canon/glossary-pending.yml; ghi nghi vấn theo mã đoạn, không tự chốt thuật ngữ.",
}


def word_count(record):
    return len(re.findall(WORD_PATTERN, record["text"]))


def marker_at_start(record, target_path):
    """An inline pagebreak is a cut before its unit only if no text precedes it."""
    prefix = []
    found = False

    def visit(element, path):
        nonlocal found
        if path == target_path:
            found = True
            return
        prefix.append(element.text or "")
        counts = Counter()
        for child in element:
            name = child.tag.rsplit("}", 1)[-1]
            counts[name] += 1
            visit(child, f"{path}/{name}[{counts[name]}]")
            if found:
                return
            prefix.append(child.tail or "")

    visit(ET.fromstring(record["xhtml"]), record["locator"]["dom_path"])
    return found and not "".join(prefix).strip()


def boundary_points(units, records, events, scene_starts):
    """Map structural markers to cuts before whole units, never inside them."""
    boundaries = {}
    priority = {"space_break": 1, "pagebreak": 2, "scene_boundary": 3}

    def add(index, kind):
        if index > 0 and priority[kind] > priority.get(boundaries.get(index), 0):
            boundaries[index] = kind

    for i in range(1, len(units)):
        if units[i]["locator"]["xhtml"] != units[i - 1]["locator"]["xhtml"]:
            add(i, "scene_boundary")
    for event in events:
        kind = event["type"]
        if kind not in ("space_break", "pagebreak"):
            continue
        locator = event["locator"]
        path = locator["dom_path"]
        for i, unit in enumerate(units):
            unit_locator = unit["locator"]
            if unit_locator["xhtml"] != locator["xhtml"]:
                continue
            unit_path = unit_locator["dom_path"]
            if path == unit_path or path.startswith(unit_path + "/"):
                if kind == "space_break" or marker_at_start(records[i], path):
                    add(i, kind)
                break
        else:
            # Empty p markers have no source unit; use the following sibling p.
            marker = re.fullmatch(r"(.+)/p\[(\d+)\]", path)
            if marker:
                parent, ordinal = marker.group(1), int(marker.group(2))
                for i, unit in enumerate(units):
                    candidate = re.fullmatch(r"(.+)/p\[(\d+)\]", unit["locator"]["dom_path"])
                    if (unit["locator"]["xhtml"] == locator["xhtml"] and candidate
                            and candidate.group(1) == parent and int(candidate.group(2)) > ordinal):
                        add(i, kind)
                        break
    indices = {unit["id"]: i for i, unit in enumerate(units)}
    for segment_id in scene_starts:
        if segment_id not in indices:
            raise ValueError("Scene boundary is outside the assigned chapter")
        add(indices[segment_id], "scene_boundary")
    return boundaries


def plan_ranges(units, records, boundaries, pilot):
    """Choose a complete partition, preferring in-range batches and useful cuts."""
    ids = [unit["id"] for unit in units]
    pilot_start = ids.index(pilot["segment_id_start"])
    pilot_end = ids.index(pilot["segment_id_end"])
    if pilot_start > pilot_end:
        raise ValueError("Invalid pilot context range")
    prefix = [0]
    for record in records:
        prefix.append(prefix[-1] + word_count(record))
    # Protect pilot context: within that span, only a page/scene transition
    # permits a cut. A space-break alone does not establish a scene change.
    allowed = [i for i in range(1, len(units) + 1)
               if not (pilot_start < i <= pilot_end)
               or boundaries.get(i) in ("pagebreak", "scene_boundary")]
    best = {0: ((0, 0, 0, 0), [])}
    for end in allowed:
        for start, (cost, spans) in list(best.items()):
            if start >= end:
                continue
            count = prefix[end] - prefix[start]
            outside = not MIN_WORDS <= count <= MAX_WORDS
            if (outside and end != len(units) and end not in boundaries
                    and not (end - start == 1 and count > MAX_WORDS)):
                continue
            kind = boundaries.get(end, "unit_boundary") if end < len(units) else "chapter_end"
            penalty = {"scene_boundary": 0, "pagebreak": 0,
                       "space_break": 200, "chapter_end": 0, "unit_boundary": 400}[kind]
            deviation = max(MIN_WORDS - count, count - MAX_WORDS, 0)
            candidate = (cost[0] + int(outside), cost[1] + deviation,
                         cost[2] + penalty, cost[3] + abs(count - TARGET_WORDS))
            if end not in best or candidate < best[end][0]:
                best[end] = (candidate, spans + [(start, end, count, kind)])
    if len(units) not in best:
        raise ValueError("No complete partition")
    return best[len(units)][1]


def assert_safe_output(root, relative, source):
    path = root / relative
    for component in (path, *path.parents):
        if component == root:
            break
        if component.is_symlink():
            raise ValueError("Symlink output is forbidden")
    ignored = subprocess.run(["git", "check-ignore", "-q", "--", relative], cwd=root)
    if ignored.returncode not in (0, 1) or (ignored.returncode == 0) != source:
        raise ValueError("Output ignore rules do not match source/metadata roles")


def prepare_outputs(manifest, units, records, ranges, pilot, versions):
    outputs, handoffs = [], []
    editor = pilot["translation_editor"]
    if not re.fullmatch(r"[A-Za-z0-9_-]+", editor):
        raise ValueError("Invalid editor metadata")
    for number, (start, end, count, kind) in enumerate(ranges, 1):
        batch_id = f"ch-00-b{number:02d}"
        source_path = f"work/vol-01/batches/{batch_id}-source.jsonl"
        source = "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records[start:end])
        handoff = {
            "task_id": f"vol-01-{batch_id}", "volume": "vol-01", "chapter": 0,
            "segment_id_start": units[start]["id"], "segment_id_end": units[end - 1]["id"],
            "unit_count": end - start, "source_word_count": count,
            "word_count_method": {"type": "regex_matches_per_unit", "pattern": WORD_PATTERN,
                                  "includes_numbers": True, "includes_date_location_units": True},
            "source_sha256": manifest["source"]["sha256"],
            "glossary_version": "sha256:" + versions["canon/glossary.yml"],
            "style_guide_version": "sha256:" + versions["canon/style-guide.md"],
            "canon_references": [{"path": path, "sha256": value} for path, value in versions.items()],
            "source_manifest": "segments/vol-01/manifest.yml",
            "source_package": source_path,
            "source_package_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
            "translation_editor": editor, "status": "ready",
            "checkpoints": CHECKPOINTS.copy(),
            "planning": {"min_source_words": MIN_WORDS, "max_source_words": MAX_WORDS,
                         "boundary_after": kind},
        }
        if end < len(units):
            handoff["planning"]["next_segment_id"] = units[end]["id"]
        if not MIN_WORDS <= count <= MAX_WORDS:
            if end - start == 1 and count > MAX_WORDS:
                reason = "Một đơn vị nguồn vượt ngưỡng; không được chia nhỏ đơn vị."
            else:
                reason = "Giữ ranh giới cấu trúc hoặc kết thúc chương khi không có cách chia toàn chương đạt ngưỡng mà vẫn giữ ngữ cảnh pilot."
            handoff["planning"]["word_count_exception"] = reason
        # Only explicitly constructed metadata reaches a tracked handoff.
        handoffs.append(handoff)
        outputs.extend([(source_path, source, True),
                        (f"handoffs/vol-01/{batch_id}.yml",
                         yaml.safe_dump(handoff, allow_unicode=True, sort_keys=False), False)])
    return outputs, handoffs


def verify_plan(units, records, ranges):
    cursor = 0
    for start, end, count, _ in ranges:
        if start != cursor or end <= start:
            raise ValueError("Batch coverage is not consecutive")
        selected = records[start:end]
        if [record["id"] for record in selected] != [unit["id"] for unit in units[start:end]]:
            raise ValueError("Batch IDs/order differ")
        if any(record["kind"] != "story" for record in selected):
            raise ValueError("Note found in story batch")
        if sum(word_count(record) for record in selected) != count:
            raise ValueError("Batch word count differs")
        cursor = end
    if cursor != len(units):
        raise ValueError("Incomplete chapter coverage")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("volume", choices=["vol-01"])
    parser.add_argument("chapter", choices=["chapter-00"])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Plan and verify without writing")
    mode.add_argument("--check", action="store_true", help="Verify existing output against the current inputs")
    parser.add_argument("--scene-start", action="append", default=[], metavar="SEGMENT_ID",
                        help="Explicit scene boundary before a whole source unit; repeatable")
    args = parser.parse_args()
    try:
        ensure_local_source(ROOT)
        manifest = yaml.safe_load((ROOT / "segments/vol-01/manifest.yml").read_text(encoding="utf-8"))
        with (ROOT / "work/vol-01/source.jsonl").open(encoding="utf-8") as stream:
            all_records = [json.loads(line) for line in stream]
        validate(manifest, all_records)
        if manifest["volume"] != args.volume or not re.fullmatch(r"[a-f0-9]{64}", manifest["source"]["sha256"]):
            raise ValueError("Invalid volume/fingerprint")
        pilot = yaml.safe_load((ROOT / "handoffs/pilot-01.yml").read_text(encoding="utf-8"))
        if pilot["source_sha256"] != manifest["source"]["sha256"]:
            raise ValueError("Pilot and source fingerprints differ")
        if pilot["word_count_method"]["pattern"] != WORD_PATTERN:
            raise ValueError("Pilot word-count convention differs")
        pairs = [(unit, record) for unit, record in zip(manifest["units"], all_records)
                 if unit["kind"] == "story" and unit["chapter"] == 0]
        units = [unit for unit, _ in pairs]
        records = [record for _, record in pairs]
        boundaries = boundary_points(units, records, manifest["events"], args.scene_start)
        ranges = plan_ranges(units, records, boundaries, pilot)
        verify_plan(units, records, ranges)
        versions = {path: sha256(ROOT / path) for path in CANON_PATHS}
        outputs, handoffs = prepare_outputs(manifest, units, records, ranges, pilot, versions)
        # Preflight every output before the first write. Reruns are idempotent;
        # never reset an existing handoff's owner, status or pinned canon.
        for relative, content, source in outputs:
            assert_safe_output(ROOT, relative, source)
            path = ROOT / relative
            if path.exists() and path.read_text(encoding="utf-8") != content:
                raise ValueError("Existing output differs; refusing to overwrite")
            if args.check and not path.is_file():
                raise ValueError("Expected output is missing")
        if not args.dry_run and not args.check:
            for relative, content, _ in outputs:
                if not (ROOT / relative).exists():
                    atomic_write(ROOT / relative, content)
        label = "DRY RUN" if args.dry_run else "PASS" if args.check else "PLANNED"
        print(f"{label}: Chapter 0; {len(units)} story units; {len(handoffs)} batches; no notes")
        for handoff in handoffs:
            print(f"{handoff['task_id']}: {handoff['segment_id_start']} .. {handoff['segment_id_end']}; "
                  f"units={handoff['unit_count']} words={handoff['source_word_count']}; "
                  f"cut={handoff['planning']['boundary_after']}")
            if "word_count_exception" in handoff["planning"]:
                print(handoff["planning"]["word_count_exception"])
        print("PASS: source ignored by Git; metadata only; complete ordered coverage; canon SHA-256 pinned")
    except (ValueError, OSError, KeyError, TypeError, IndexError, yaml.YAMLError,
            ET.ParseError, subprocess.CalledProcessError):
        # Exception details and parser messages may contain source prose.
        parser.exit(1, "Planning refused: check source/manifest/pilot SHA, IDs, canon, ignore rules and existing outputs.\n")


if __name__ == "__main__":
    main()
