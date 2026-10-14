"""Synthetic, source-free integration checks for coordinator promotion."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

from promote_polished_translation import PromotionError, atomic_promote, run, verify_inputs
from validate_translation import ValidationError


class PromotionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        (self.root / ".gitignore").write_text("work/\n", encoding="utf-8")
        self.paths = {
            "baseline": self.root / "translations/vol-02/ch-01-b01.jsonl",
            "candidate": self.root / "polish-candidates/vol-02/ch-01-b01.gemini.jsonl",
            "change_log": self.root / "polish-candidates/vol-02/ch-01-b01.gemini-change-log.yml",
            "receipt": self.root / "reviews/semantic/vol-02/ch-01-b01-regression.yml",
            "locked_choices": self.root / "handoffs/vol-02/ch-01-b01-locked.yml",
            "handoff": self.root / "handoffs/vol-02/ch-01-b01.yml",
            "source": self.root / "work/vol-02/ch-01-b01-source.jsonl",
        }
        for path in self.paths.values():
            path.parent.mkdir(parents=True, exist_ok=True)
        self.task_id = "vol-02-ch-01-b01"
        self.ids = ["synthetic-001", "synthetic-002"]
        self.source = [{"id": value, "text": "Synthetic invented input for regression tests."} for value in self.ids]
        self.baseline = [{
            "segment_id": value, "translation": "Mình đã về.", "status": "reviewed",
            "translator": "luna", "glossary_version": "sha256:" + "b" * 64,
            "source_sha256": "a" * 64, "notes": [],
        } for value in self.ids]
        self.candidate = [dict(row, translation="Mình về rồi.") for row in self.baseline]
        self.log = {"task_id": self.task_id, "change_log": [
            {"segment_id": value, "types": ["rhythm"], "escalate": False} for value in self.ids
        ]}
        self.choices = {
            "task_id": self.task_id, "source_sha256": "a" * 64,
            "glossary_version": "sha256:" + "b" * 64,
            "choices": [{"segment_id": self.ids[0], "kind": "pronoun", "value": "mình"}],
        }
        self.handoff = {
            "task_id": self.task_id, "source_sha256": "a" * 64,
            "glossary_version": "sha256:" + "b" * 64,
            "source_package": "work/vol-02/ch-01-b01-source.jsonl",
        }
        self.receipt = {
            "schema_version": 1, "task_id": self.task_id,
            "reviewer_model": "gemini-4-argon-low", "decision": "accept",
            "checked_segment_ids": self.ids, "findings": [],
        }
        self.write_jsonl("source", self.source)
        self.write_jsonl("baseline", self.baseline)
        self.choices["baseline_sha256"] = self.digest("baseline")
        self.write_jsonl("candidate", self.candidate)
        self.write_yaml("change_log", self.log)
        self.write_yaml("locked_choices", self.choices)
        self.handoff["source_package_sha256"] = self.digest("source")
        self.write_yaml("handoff", self.handoff)
        self.refresh_receipt()
        self.checkpoint = self.root / "work/run-state/translation-coordinator.yml"
        self.args = argparse.Namespace(**self.paths, apply=False, coordinator="", checkpoint=self.checkpoint)

    def write_jsonl(self, key, value):
        self.paths[key].write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in value), encoding="utf-8")

    def write_yaml(self, key, value):
        self.paths[key].write_text(yaml.safe_dump(value, allow_unicode=True), encoding="utf-8")

    def digest(self, key):
        return hashlib.sha256(self.paths[key].read_bytes()).hexdigest()

    def refresh_receipt(self):
        for key, field in (
            ("baseline", "baseline_sha256"), ("candidate", "candidate_sha256"),
            ("locked_choices", "locked_choices_sha256"), ("change_log", "change_log_sha256"),
            ("source", "source_package_sha256"),
        ):
            self.receipt[field] = self.digest(key)
        self.write_yaml("receipt", self.receipt)

    def authorize(self):
        self.args.apply = True
        self.args.coordinator = "coord-test"
        lease = {
            "holder": "coord-test", "task_id": self.task_id, "state": "active",
            "allowlist": ["translations/vol-02/ch-01-b01.jsonl"],
        }
        self.handoff["lease"] = lease
        self.write_yaml("handoff", self.handoff)
        self.state = {"coordinator": "coord-test", "active_translation_editor": "coord-test", "active_worker": None, "lease": lease}
        self.checkpoint.parent.mkdir(parents=True, exist_ok=True)
        self.checkpoint.write_text(yaml.safe_dump(self.state), encoding="utf-8")

    def rejected(self, expected):
        old = self.paths["baseline"].read_bytes()
        with self.assertRaisesRegex(ValidationError, expected):
            run(self.args, self.root)
        self.assertEqual(self.paths["baseline"].read_bytes(), old)

    def test_read_only_validation_writes_nothing(self):
        before = {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        result = run(self.args, self.root)
        after = {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(before, after)
        self.assertEqual(result["result"], "ready")

    def test_apply_replaces_exact_candidate_bytes_and_reports_old_hash(self):
        self.authorize()
        old = self.digest("baseline")
        candidate = self.paths["candidate"].read_bytes()
        result = run(self.args, self.root)
        self.assertEqual(self.paths["baseline"].read_bytes(), candidate)
        self.assertEqual(result["baseline_sha256"], old)
        self.assertEqual(result["result"], "promoted")
        # Receipt cannot be reused against the now-different canonical baseline.
        self.rejected("baseline_sha256")

    def test_missing_or_incomplete_receipts(self):
        for field in ("checked_segment_ids", "decision", "findings", "candidate_sha256"):
            with self.subTest(field=field):
                saved = dict(self.receipt)
                self.receipt.pop(field)
                self.write_yaml("receipt", self.receipt)
                self.rejected("Receipt")
                self.receipt = saved
        self.receipt["checked_segment_ids"] = self.ids[:1]
        self.write_yaml("receipt", self.receipt)
        self.rejected("complete checked_segment_ids")
        self.paths["receipt"].unlink()
        self.rejected("Cannot read")

    def test_wrong_model_task_or_rejection(self):
        self.receipt["reviewer_model"] = "gpt-6-luna"
        self.write_yaml("receipt", self.receipt)
        self.assertEqual(run(self.args, self.root)["result"], "ready")
        for field, value in (("reviewer_model", "other-model"), ("task_id", "other-task"), ("decision", "reject")):
            with self.subTest(field=field):
                self.receipt[field] = value
                self.write_yaml("receipt", self.receipt)
                self.rejected(field)
                self.receipt.update(reviewer_model="gemini-4-argon-low", task_id=self.task_id, decision="accept")

    def test_blocking_and_style_findings(self):
        for severity in ("critical", "locked_choice_violation", "unknown"):
            self.receipt["findings"] = [{"segment_id": self.ids[0], "severity": severity}]
            self.write_yaml("receipt", self.receipt)
            self.rejected("finding")
        self.receipt["findings"] = [{"segment_id": self.ids[0], "severity": "style_only"}]
        self.write_yaml("receipt", self.receipt)
        self.assertEqual(run(self.args, self.root)["result"], "ready")

    def test_each_fingerprinted_input_invalidates_receipt(self):
        for key in ("baseline", "candidate", "locked_choices", "change_log", "source"):
            with self.subTest(key=key):
                original = self.paths[key].read_bytes()
                self.paths[key].write_bytes(original + b"\n")
                self.rejected("Receipt .*sha256|Invalid .* JSONL")
                self.paths[key].write_bytes(original)

    def test_candidate_cannot_mutate_metadata_or_source_fields(self):
        for field, value in (("translator", "gemini"), ("status", "approved"), ("notes", ["added"]), ("source_text", "copied")):
            with self.subTest(field=field):
                self.candidate[0][field] = value
                self.write_jsonl("candidate", self.candidate)
                self.refresh_receipt()
                self.rejected("Candidate")
                self.candidate = [dict(row, translation="Mình về rồi.") for row in self.baseline]

    def test_unreviewed_baseline_cannot_be_promoted(self):
        self.baseline[0]["status"] = "draft"
        self.candidate[0]["status"] = "draft"
        self.write_jsonl("baseline", self.baseline)
        self.choices["baseline_sha256"] = self.digest("baseline")
        self.write_yaml("locked_choices", self.choices)
        self.write_jsonl("candidate", self.candidate)
        self.refresh_receipt()
        self.rejected("already be reviewed")

    def test_missing_reordered_or_duplicate_ids(self):
        for rows in (self.candidate[:1], self.candidate[::-1], [self.candidate[0], self.candidate[0]]):
            self.write_jsonl("candidate", rows)
            self.refresh_receipt()
            self.rejected("Candidate.*IDs|Candidate.*duplicate")

    def test_source_package_hash_checked_independently_of_epub_hash(self):
        # The ordinary valid fixture intentionally uses different EPUB/package hashes.
        self.handoff["source_package_sha256"] = "c" * 64
        self.write_yaml("handoff", self.handoff)
        self.rejected("Handoff source_package_sha256")

    def test_locked_snapshot_must_describe_current_baseline_and_canon(self):
        for field in ("baseline_sha256", "source_sha256", "glossary_version"):
            with self.subTest(field=field):
                saved = self.choices[field]
                self.choices[field] = "stale-value"
                self.write_yaml("locked_choices", self.choices)
                self.refresh_receipt()
                self.rejected("Locked choices " + field)
                self.choices[field] = saved

    def test_locked_snapshot_rejects_unknown_segment(self):
        self.choices["choices"][0]["segment_id"] = "outside-batch"
        self.write_yaml("locked_choices", self.choices)
        self.refresh_receipt()
        self.rejected("Locked choice must identify")

    def test_source_must_be_ignored_and_untracked(self):
        (self.root / ".gitignore").write_text("", encoding="utf-8")
        self.rejected("not ignored")
        subprocess.run(["git", "add", "work/vol-02/ch-01-b01-source.jsonl"], cwd=self.root, check=True)
        (self.root / ".gitignore").write_text("work/\n", encoding="utf-8")
        self.rejected("not ignored|tracked")

    def test_escalation_keeps_original_text_and_allows_continuation(self):
        self.log["change_log"][0].update(types=[], escalate=True)
        self.write_yaml("change_log", self.log)
        self.refresh_receipt()
        self.rejected("Escalated segment")
        self.candidate[0] = dict(self.baseline[0])
        self.write_jsonl("candidate", self.candidate)
        self.refresh_receipt()
        self.assertEqual(run(self.args, self.root)["result"], "ready")

    def test_invalid_or_missing_change_log(self):
        self.log["change_log"][0]["types"] = ["new-imagery"]
        self.write_yaml("change_log", self.log)
        self.refresh_receipt()
        self.rejected("types")
        self.log["change_log"] = self.log["change_log"][1:]
        self.write_yaml("change_log", self.log)
        self.refresh_receipt()
        self.rejected("complete segment IDs")

    def test_paths_and_symlinks_cannot_bypass_scope(self):
        outside = self.root / "outside.jsonl"
        outside.write_bytes(self.paths["candidate"].read_bytes())
        self.args.candidate = outside
        self.rejected("polish-candidates/ or legacy translations/")
        self.args.candidate = self.paths["candidate"]
        self.paths["candidate"].unlink()
        self.paths["candidate"].symlink_to(outside)
        self.rejected("polish-candidates/|legacy translations/|Symlink|canonical input")

    def test_apply_requires_recorded_matching_exclusive_lease(self):
        self.authorize()
        for key, value in (("active_worker", "luna-active"), ("active_translation_editor", "gemini"), ("coordinator", "other")):
            with self.subTest(key=key):
                saved = self.state[key]
                self.state[key] = value
                self.checkpoint.write_text(yaml.safe_dump(self.state), encoding="utf-8")
                self.rejected("Checkpoint")
                self.state[key] = saved
        self.checkpoint.write_text(yaml.safe_dump(self.state), encoding="utf-8")
        self.handoff["lease"]["holder"] = "gemini"
        self.write_yaml("handoff", self.handoff)
        self.rejected("Handoff lease holder")

    def test_apply_without_coordinator_cannot_create_lock_or_modify_canonical(self):
        self.args.apply = True
        self.rejected("requires --coordinator")
        self.assertFalse((self.root / "work/run-state/polished-promotion.lock").exists())

    def test_lease_rejects_wrong_task_released_state_or_missing_allowlist(self):
        self.authorize()
        for key, value in (("task_id", "wrong-task"), ("state", "released"), ("allowlist", [])):
            with self.subTest(key=key):
                saved = self.state["lease"][key]
                self.state["lease"][key] = value
                self.checkpoint.write_text(yaml.safe_dump(self.state), encoding="utf-8")
                self.rejected("Checkpoint lease")
                self.state["lease"][key] = saved

    def test_inputs_rechecked_immediately_before_atomic_replace(self):
        items, *_ = verify_inputs(root=self.root, **self.paths)
        self.paths["candidate"].write_bytes(items[1].data + b"\n")
        old = self.paths["baseline"].read_bytes()
        with self.assertRaisesRegex(PromotionError, "Input changed"):
            atomic_promote(items)
        self.assertEqual(self.paths["baseline"].read_bytes(), old)
        self.assertFalse(list(self.paths["baseline"].parent.glob(".promotion-*")))

    def test_replace_failure_leaves_canonical_and_cleans_temp(self):
        items, *_ = verify_inputs(root=self.root, **self.paths)
        with patch("promote_polished_translation.os.replace", side_effect=OSError("synthetic interruption")):
            with self.assertRaises(OSError):
                atomic_promote(items)
        self.assertEqual(self.paths["baseline"].read_bytes(), items[0].data)
        self.assertFalse(list(self.paths["baseline"].parent.glob(".promotion-*")))


if __name__ == "__main__":
    unittest.main()
