"""Check a Gemini candidate; only an explicitly leased coordinator may apply it.

The YAML receipt in reviews/semantic/ must contain schema_version: 1, task_id,
reviewer_model: gpt-6-luna, decision: accept, checked_segment_ids (all IDs in
source order), findings (segment_id, severity), and SHA256 fields baseline_sha256,
candidate_sha256, locked_choices_sha256, change_log_sha256, source_package_sha256.
Allowed severities are critical, locked_choice_violation, and style_only.

Locked choices are coordinator YAML in handoffs/ with task_id and a choices list.
The YAML change log has task_id and change_log (one entry per segment: segment_id,
types array of syntax/rhythm/diction/punctuation, and boolean escalate). Escalated
segments must retain the baseline text, allowing pending choices to continue.
No source text is written. Running without --apply never writes any file.
"""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
import sys
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

import yaml

from validate_translation import ValidationError, check_source_is_local_only, validate


class PromotionError(ValidationError):
    """Candidate cannot safely become canonical."""


@dataclass(frozen=True)
class Snapshot:
    path: Path
    data: bytes

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.data).hexdigest()


def scoped_path(path: Path, root: Path, scope: str) -> Path:
    resolved = path.resolve()
    try:
        relative = resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise PromotionError(f"Path must be inside {scope}/") from exc
    if not relative.parts or relative.parts[0] != scope:
        raise PromotionError(f"Path must be inside {scope}/")
    # Symlinks can redirect a path between the check and atomic replacement.
    current = root.resolve()
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise PromotionError("Symlink input paths are not permitted")
    if path.absolute() != resolved:
        raise PromotionError("Use canonical input paths without symlinks or '..'")
    return resolved


def snapshot(path: Path) -> Snapshot:
    try:
        return Snapshot(path, path.read_bytes())
    except OSError as exc:
        raise PromotionError(f"Cannot read {path.name}: {exc}") from exc


def yaml_object(item: Snapshot, label: str) -> dict:
    try:
        value = yaml.safe_load(item.data)
    except (yaml.YAMLError, UnicodeError) as exc:
        raise PromotionError(f"Invalid {label} YAML") from exc
    if not isinstance(value, dict):
        raise PromotionError(f"{label} must be an object")
    return value


def jsonl_records(item: Snapshot, label: str) -> list[dict]:
    try:
        lines = item.data.decode("utf-8").splitlines()
        records = [json.loads(line) for line in lines]
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise PromotionError(f"Invalid {label} JSONL") from exc
    if not records or any(not isinstance(row, dict) for row in records):
        raise PromotionError(f"{label} must contain nonempty JSONL objects")
    return records


def require_match(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise PromotionError(f"{label} does not match")


def verify_inputs(
    *, root: Path, baseline: Path, candidate: Path, receipt: Path,
    locked_choices: Path, change_log: Path, handoff: Path, source: Path,
) -> tuple[list[Snapshot], dict, dict, list[str]]:
    candidate_abs = candidate if candidate.is_absolute() else root / candidate
    try:
        candidate_root = candidate_abs.resolve().relative_to(root.resolve()).parts[0]
    except (ValueError, IndexError) as exc:
        raise PromotionError("Candidate must be inside polish-candidates/ or legacy translations/") from exc
    if candidate_root not in {"polish-candidates", "translations"}:
        raise PromotionError("Candidate must be inside polish-candidates/ or legacy translations/")
    paths = [scoped_path(path, root, scope) for path, scope in (
        (baseline, "translations"), (candidate, candidate_root),
        (receipt, "reviews"), (locked_choices, "handoffs"),
        (change_log, candidate_root), (handoff, "handoffs"), (source, "work"),
    )]
    baseline, candidate, receipt, locked_choices, change_log, handoff, source = paths
    relative = baseline.relative_to(root.resolve())
    if not re.fullmatch(r"translations/vol-\d{2}/ch-\d{2}-b\d{2}\.jsonl", relative.as_posix()):
        raise PromotionError("Baseline must be translations/vol-xx/ch-xx-byy.jsonl")
    legacy_candidate = baseline.with_name(baseline.stem + ".gemini.jsonl")
    isolated_candidate = root.resolve() / "polish-candidates" / relative.parts[1] / (baseline.stem + ".gemini.jsonl")
    if candidate not in {legacy_candidate, isolated_candidate}:
        raise PromotionError("Candidate filename does not match the baseline batch")
    expected_log = candidate.with_name(baseline.stem + ".gemini-change-log.yml")
    require_match(change_log, expected_log, "Change-log filename")
    if receipt.relative_to(root.resolve()).parts[:2] != ("reviews", "semantic"):
        raise PromotionError("Receipt must be inside reviews/semantic/")
    check_source_is_local_only(source, root)
    items = [snapshot(path) for path in paths]
    before, after, report, locked, log, assignment, package = items
    h = yaml_object(assignment, "Handoff")
    r = yaml_object(report, "Receipt")
    choices = yaml_object(locked, "Locked choices")
    rows = jsonl_records(before, "Baseline")
    candidate_rows = jsonl_records(after, "Candidate")
    source_rows = jsonl_records(package, "Source")
    change_document = yaml_object(log, "Change log")
    changes = change_document.get("change_log")
    if not isinstance(changes, list) or any(not isinstance(row, dict) for row in changes):
        raise PromotionError("Change log must contain a change_log array of objects")
    task_id = h.get("task_id")
    if not isinstance(task_id, str) or not task_id.strip():
        raise PromotionError("Handoff must have a task_id")
    require_match(task_id, f"{relative.parts[1]}-{baseline.stem}", "Handoff batch task_id")
    if type(r.get("schema_version")) is not int:
        raise PromotionError("Receipt schema_version must be an integer")
    require_match(r.get("schema_version"), 1, "Receipt schema_version")
    require_match(r.get("task_id"), task_id, "Receipt task_id")
    require_match(choices.get("task_id"), task_id, "Locked choices task_id")
    require_match(change_document.get("task_id"), task_id, "Change log task_id")
    if not isinstance(choices.get("choices"), list):
        raise PromotionError("Locked choices must contain a choices list")
    require_match(choices.get("baseline_sha256"), before.sha256, "Locked choices baseline_sha256")
    require_match(choices.get("source_sha256"), h.get("source_sha256"), "Locked choices source_sha256")
    require_match(choices.get("glossary_version"), h.get("glossary_version"), "Locked choices glossary_version")
    require_match(r.get("reviewer_model"), "gpt-6-luna", "Receipt reviewer_model")
    require_match(r.get("decision"), "accept", "Receipt decision")
    for key, item in (
        ("baseline_sha256", before), ("candidate_sha256", after),
        ("locked_choices_sha256", locked), ("change_log_sha256", log),
        ("source_package_sha256", package),
    ):
        require_match(r.get(key), item.sha256, f"Receipt {key}")
    # source_sha256 identifies the EPUB; source_package_sha256 hashes JSONL bytes.
    require_match(h.get("source_package_sha256"), package.sha256, "Handoff source_package_sha256")
    if "source_package" in h:
        require_match(h["source_package"], source.relative_to(root.resolve()).as_posix(), "Handoff source_package")
    for label, translation_rows in (("Baseline", rows), ("Candidate", candidate_rows)):
        results = validate(h, source_rows, translation_rows)
        errors = [error for error in results if not error.startswith("WARNING:")]
        if errors:
            raise PromotionError(f"{label}: " + "; ".join(errors))
    if any(row["status"] not in {"reviewed", "approved"} for row in rows):
        raise PromotionError("Baseline must already be reviewed or approved")
    for old, new in zip(rows, candidate_rows):
        require_match(
            json.dumps({key: value for key, value in new.items() if key != "translation"}, sort_keys=True),
            json.dumps({key: value for key, value in old.items() if key != "translation"}, sort_keys=True),
            f"Candidate metadata for {old['segment_id']}",
        )
    ids = [row["segment_id"] for row in rows]
    for choice in choices["choices"]:
        if not isinstance(choice, dict) or choice.get("segment_id") not in ids:
            raise PromotionError("Locked choice must identify a batch segment")
        if not isinstance(choice.get("kind"), str) or not choice["kind"].strip() or not isinstance(choice.get("value"), str) or not choice["value"].strip():
            raise PromotionError("Locked choice must have nonempty kind and value")
    require_match(r.get("checked_segment_ids"), ids, "Receipt complete checked_segment_ids")
    findings = r.get("findings")
    if not isinstance(findings, list):
        raise PromotionError("Receipt findings must be an explicit list")
    for finding in findings:
        if not isinstance(finding, dict) or finding.get("segment_id") not in ids:
            raise PromotionError("Receipt finding must identify a batch segment")
        severity = finding.get("severity")
        if not isinstance(severity, str):
            raise PromotionError("Receipt finding severity must be a string")
        if severity in {"critical", "locked_choice_violation"}:
            raise PromotionError(f"Blocking finding: {finding['segment_id']} {severity}")
        if severity != "style_only":
            raise PromotionError("Unknown receipt finding severity")
    require_match([row.get("segment_id") for row in changes], ids, "Change log complete segment IDs")
    allowed = {"syntax", "rhythm", "diction", "punctuation"}
    for row, old, new in zip(changes, rows, candidate_rows):
        types = row.get("types")
        if type(row.get("escalate")) is not bool:
            raise PromotionError("Change log escalate must be an explicit boolean")
        if row["escalate"] and (types != [] or old["translation"] != new["translation"]):
            raise PromotionError(f"Escalated segment must retain baseline text and types: []: {row['segment_id']}")
        if set(row) - {"segment_id", "types", "escalate"}:
            raise PromotionError("Change log may contain only segment_id, types and escalate")
        if not isinstance(types, list) or any(not isinstance(value, str) or value not in allowed for value in types):
            raise PromotionError("Change log types must be syntax/rhythm/diction/punctuation")
        if old["translation"] != new["translation"] and not types:
            raise PromotionError(f"Changed segment lacks a change log: {row['segment_id']}")
    return items, h, r, ids


def verify_coordinator(root: Path, handoff: dict, checkpoint: Snapshot, coordinator: str, baseline: Path) -> None:
    if not coordinator:
        raise PromotionError("--apply requires --coordinator (the active coordinator identity)")
    state = yaml_object(checkpoint, "Checkpoint")
    require_match(state.get("coordinator"), coordinator, "Checkpoint coordinator")
    if state.get("active_worker"):
        raise PromotionError("Checkpoint still has an active_worker")
    worker_leases = state.get("worker_leases", [])
    if not isinstance(worker_leases, list):
        raise PromotionError("Checkpoint worker_leases must be a list")
    for worker in worker_leases:
        if not isinstance(worker, dict):
            raise PromotionError("Checkpoint worker_leases entries must be objects")
        allowlist = worker.get("allowlist", [])
        if not isinstance(allowlist, list):
            raise PromotionError("Worker lease allowlist must be a list")
        if any(isinstance(path, str) and path.startswith("translations/") for path in allowlist):
            raise PromotionError("A worker still leases a canonical translation under translations/")
    require_match(state.get("active_translation_editor"), coordinator, "Checkpoint active_translation_editor")
    relative = baseline.relative_to(root.resolve()).as_posix()
    for label, document in (("Handoff", handoff), ("Checkpoint", state)):
        lease = document.get("lease")
        if not isinstance(lease, dict):
            raise PromotionError(f"{label} must record the exclusive coordinator lease")
        require_match(lease.get("holder"), coordinator, f"{label} lease holder")
        require_match(lease.get("task_id"), handoff["task_id"], f"{label} lease task_id")
        require_match(lease.get("state"), "active", f"{label} lease state")
        allowlist = lease.get("allowlist", document.get("allowlist"))
        if not isinstance(allowlist, list) or relative not in allowlist:
            raise PromotionError(f"{label} lease allowlist must contain canonical translation")


@contextmanager
def promotion_lock(root: Path):
    """Serialize promotions; the recorded pipeline lease also excludes workers."""
    path = scoped_path(root / "work/run-state/polished-promotion.lock", root, "work")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise PromotionError("Another coordinator is promoting a translation") from exc
        try:
            yield
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def assert_unchanged(items: list[Snapshot]) -> None:
    for item in items:
        if snapshot(item.path).data != item.data:
            raise PromotionError(f"Input changed during promotion: {item.path.name}")


def atomic_promote(items: list[Snapshot]) -> None:
    before, after = items[:2]
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(dir=before.path.parent, prefix=".promotion-", delete=False) as stream:
            temp_path = Path(stream.name)
            stream.write(after.data)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temp_path, before.path.stat().st_mode & 0o777)
        assert_unchanged(items)
        os.replace(temp_path, before.path)
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


def run(args: argparse.Namespace, root: Path) -> dict:
    inputs = {key: getattr(args, key) for key in (
        "baseline", "candidate", "receipt", "locked_choices", "change_log", "handoff", "source",
    )}
    if args.apply:
        if not args.coordinator:
            raise PromotionError("--apply requires --coordinator (the active coordinator identity)")
        with promotion_lock(root):
            items, handoff, receipt, ids = verify_inputs(root=root, **inputs)
            checkpoint_path = scoped_path(args.checkpoint, root, "work")
            checkpoint = snapshot(checkpoint_path)
            verify_coordinator(root, handoff, checkpoint, args.coordinator, items[0].path)
            atomic_promote(items + [checkpoint])
    else:
        items, handoff, receipt, ids = verify_inputs(root=root, **inputs)
    return {
        "result": "promoted" if args.apply else "ready", "task_id": handoff["task_id"],
        "segment_count": len(ids), "baseline_sha256": items[0].sha256,
        "candidate_sha256": items[1].sha256, "receipt_sha256": items[2].sha256,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("baseline", "candidate", "receipt", "locked-choices", "change-log", "handoff", "source"):
        parser.add_argument("--" + name, required=True, type=Path)
    parser.add_argument("--apply", action="store_true", help="Atomically replace canonical after coordinator lease checks")
    parser.add_argument("--coordinator", default="", help="Active coordinator identity recorded in handoff/checkpoint")
    parser.add_argument("--checkpoint", type=Path, default=Path("work/run-state/translation-coordinator.yml"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        result = run(args, root)
    except (OSError, ValidationError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
