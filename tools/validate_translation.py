"""Validate a translation JSONL file against its local source package and handoff."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml


REQUIRED_FIELDS = {
    "segment_id", "translation", "status", "translator", "glossary_version",
    "source_sha256", "notes",
}
ALLOWED_STATUS = {"draft", "reviewed", "approved"}
FORBIDDEN_SOURCE_FIELDS = {"source", "source_text"}
MARKDOWN_EMPHASIS = re.compile(r"(?<!\\)(\*)")


class ValidationError(Exception):
    """An actionable validation failure."""


def read_jsonl(path: Path, label: str) -> list[dict]:
    records = []
    try:
        with path.open(encoding="utf-8") as stream:
            for number, line in enumerate(stream, 1):
                if not line.strip():
                    raise ValidationError(f"{label}:{number}: blank lines are not allowed")
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValidationError(f"{label}:{number}: invalid JSON ({exc.msg})") from exc
                if not isinstance(record, dict):
                    raise ValidationError(f"{label}:{number}: each JSONL row must be an object")
                records.append(record)
    except OSError as exc:
        raise ValidationError(f"Cannot read {label}: {exc}") from exc
    return records


def check_source_is_local_only(path: Path, repo_root: Path) -> None:
    try:
        relative = path.resolve().relative_to(repo_root.resolve())
    except ValueError as exc:
        raise ValidationError("Source package must be inside the repository's work/ directory") from exc
    if not relative.parts or relative.parts[0] != "work":
        raise ValidationError("Source package must be inside the repository's work/ directory")
    try:
        ignored = subprocess.run(
            ["git", "check-ignore", "--quiet", str(relative)], cwd=repo_root, check=False
        ).returncode == 0
        tracked = subprocess.run(
            ["git", "ls-files", "--error-unmatch", "--", str(relative)],
            cwd=repo_root, check=False, capture_output=True, text=True,
        ).returncode == 0
    except OSError as exc:
        raise ValidationError(f"Could not check Git status of source package: {exc}") from exc
    if not ignored:
        raise ValidationError("Source package is not ignored by Git")
    if tracked:
        raise ValidationError("Source package is tracked by Git")


def markdown_emphasis_balanced(text: str) -> bool:
    return len(MARKDOWN_EMPHASIS.findall(text)) % 2 == 0


def source_has_emphasis(record: dict) -> bool:
    markup = record.get("xhtml", "")
    return isinstance(markup, str) and bool(re.search(r"<\s*(?:em|i)\b", markup, re.I))


def validate(handoff: dict, source_records: list[dict], translations: list[dict]) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []
    expected_ids = [row.get("id") for row in source_records]
    actual_ids = [row.get("segment_id") for row in translations]

    if any(not isinstance(value, str) or not value for value in expected_ids):
        errors.append("Source rows must each have a non-empty id")
    if all(isinstance(value, str) for value in expected_ids) and len(set(expected_ids)) != len(expected_ids):
        errors.append("Source package contains duplicate segment IDs")
    if all(isinstance(value, str) for value in actual_ids) and len(set(actual_ids)) != len(actual_ids):
        errors.append("Translation contains duplicate segment_id values")
    if expected_ids != actual_ids:
        errors.append("Translation segment IDs must match source IDs exactly and in order")

    expected_sha = handoff.get("source_sha256")
    expected_glossary = handoff.get("glossary_version")
    for index, row in enumerate(translations, 1):
        missing = REQUIRED_FIELDS - row.keys()
        if missing:
            errors.append(f"Translation row {index} missing fields: {', '.join(sorted(missing))}")
        forbidden = FORBIDDEN_SOURCE_FIELDS.intersection(row)
        if forbidden:
            errors.append(f"Translation row {index} has forbidden source fields: {', '.join(sorted(forbidden))}")
        translation = row.get("translation")
        if not isinstance(translation, str) or not translation.strip():
            errors.append(f"Translation row {index} translation must be a non-empty string")
            translation = ""
        if row.get("status") not in ALLOWED_STATUS:
            errors.append(f"Translation row {index} status must be draft, reviewed, or approved")
        if not isinstance(row.get("translator"), str) or not row["translator"].strip():
            errors.append(f"Translation row {index} translator must be a non-empty string")
        if not isinstance(row.get("notes"), list) or any(not isinstance(note, str) for note in row.get("notes", [])):
            errors.append(f"Translation row {index} notes must be an array of strings")
        if row.get("source_sha256") != expected_sha:
            errors.append(f"Translation row {index} source_sha256 does not match handoff")
        if row.get("glossary_version") != expected_glossary:
            errors.append(f"Translation row {index} glossary_version does not match handoff")
        if not markdown_emphasis_balanced(translation):
            errors.append(f"Translation row {index} has unbalanced Markdown * emphasis")

    for index, source in enumerate(source_records):
        if index >= len(translations):
            continue
        source_text = source.get("text")
        translation = translations[index].get("translation")
        if isinstance(source_text, str):
            normalized_source = " ".join(source_text.split())
            copied_candidates = [value for value in translations[index].values() if isinstance(value, str)]
            notes = translations[index].get("notes", [])
            if isinstance(notes, list):
                copied_candidates.extend(value for value in notes if isinstance(value, str))
            normalized_translation = " ".join(" ".join(copied_candidates).split())
            if len(normalized_source) >= 16 and normalized_source in normalized_translation:
                errors.append(f"Translation row {index + 1} appears to contain copied source text")
        if source_has_emphasis(source) and isinstance(translation, str) and "*" not in translation:
            warnings.append(f"{translations[index].get('segment_id', f'row {index + 1}')}: source emphasis has no Markdown emphasis in translation")

    return errors + [f"WARNING: {warning}" for warning in warnings]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--handoff", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--translation", required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        check_source_is_local_only(args.source, root)
        handoff = yaml.safe_load(args.handoff.read_text(encoding="utf-8"))
        if not isinstance(handoff, dict):
            raise ValidationError("Handoff YAML must contain an object")
        source = read_jsonl(args.source, "source")
        translation = read_jsonl(args.translation, "translation")
        results = validate(handoff, source, translation)
    except (OSError, yaml.YAMLError, ValidationError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    errors = [item for item in results if not item.startswith("WARNING:")]
    for item in results:
        print(("ERROR: " if not item.startswith("WARNING:") else "") + item)
    if errors:
        return 1
    print(f"PASS: {len(translation)} translation rows match source order and handoff metadata")
    print("PASS: source package is Git-ignored and untracked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
