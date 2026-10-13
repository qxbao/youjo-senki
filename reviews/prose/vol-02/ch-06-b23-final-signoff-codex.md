# Independent final signoff — vol-02-ch-06-b23

The final translation resolves all six original findings. Full signoff is withheld because the self-check still contradicts the applied choices at p000737 and p000746 and lists only six pending entries, omitting a separate unit-name entry. All seven reviewer-ledger choices match the translation and remain pending/non-canon. No serious, moderate, or material new translation issue was found in the assigned 43 rows.

```yaml
role: reviewer
task_id: vol-02-ch-06-b23-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-06-b23-final-signoff-codex.md
segment_ids:
  - YS-LN02/Text/part0030.xhtml/p000709-YS-LN02/Text/part0030.xhtml/p000751
files_written:
  - reviews/prose/vol-02/ch-06-b23-final-signoff-codex.md
source_package_sha256: 58d10ecd3c86a49f5af41f42932270d424bcbeb747fcda3a61c01da710602a4e
source_package_hash: matched
translation_sha256: 72f993aa62ce9cf2de9f635c759140b2b71a8db2f0bc93e5786cbdff594fd8ba
self_check_sha256: 070364872ac354cbdc76e4288f1ac67f1ac81945a0127502af4850b80ac22bed
counts:
  source_rows: 43
  translation_rows: 43
  reviewed_rows: 43
  original_findings_verified: 6
  original_findings_resolved_in_translation: 6
  original_findings_fully_closed: 4
  original_findings_with_self_check_residuals: 2
  serious: 0
  moderate: 0
  minor: 0
  low: 3
  total_findings: 3
  unresolved_findings: 3
  new_translation_findings: 0
  new_documentation_findings: 1
  pending_entries_expected: 7
  reviewer_ledger_entries: 7
  translation_pending_matches: 7
  self_check_pending_entries: 6
  self_check_pending_matches: 4
  self_check_pending_mismatches: 2
  self_check_pending_missing: 1
  reviewer_ledger_non_canon_entries: 7
  emphasis_spans_checked: 2
translation_signoff: true
full_signoff: false
unresolved_findings: [B23-R01, B23-R06, B23-FS01]
validator: not_run
diff_check: not_run
commit: null
findings:
  - id: B23-R01
    severity: low
    segment_id: YS-LN02/Text/part0030.xhtml/p000737
    status: translation_resolved_self_check_open
    issue: "Self-check pending_choices retains the superseded functional description as proposed_vi, despite the corrected translation and finding resolution. Its rationale and risk also describe the old choice."
    resolution: "Set proposed_vi to nhà nước gác đêm; align rationale and risk with the current broad citizen-protection argument. Preserve pending/non-canon status and alternatives."
  - id: B23-R06
    severity: low
    segment_id: YS-LN02/Text/part0030.xhtml/p000746
    status: translation_resolved_self_check_open
    issue: "Self-check proposed_vi remains dù vàng and its finding resolution claims the quoted metaphor is used. The final translation instead uses the descriptive benefits wording; only the pending rationale reflects that change. Its risk likewise concerns the superseded metaphor."
    resolution: "Set proposed_vi to các gói đãi ngộ hậu hĩnh khi rời chức; update finding resolution and risk accordingly. Keep the metaphor as an alternative, pending/non-canon."
  - id: B23-FS01
    severity: low
    segment_id: YS-LN02/Text/part0030.xhtml/p000744
    status: open
    issue: "Self-check pending_choices has six entries, with mage present but the unit designation missing as an independent seventh entry. The unit appears correctly in its finding resolution, which does not supply the missing structured entry."
    resolution: "Add the reviewer-ledger unit-name entry with proposed_vi Tiểu đoàn Pháp sư trên không 203, p000744, rationale, alternative and explicit pending/non-canon status; retain mage as a separate entry."
term_recommendations:
  - source_term: information warfare
    proposed_vi: chiến tranh thông tin
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000719]
    status: pending
    canon: false
  - source_term: night-watchman state
    proposed_vi: nhà nước gác đêm
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000737]
    status: pending
    canon: false
  - source_term: golden parachutes
    proposed_vi: các gói đãi ngộ hậu hĩnh khi rời chức
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000746]
    status: pending
    canon: false
  - source_term: information / propaganda / disinformation
    proposed_vi: thông tin / tuyên truyền / thông tin sai lệch
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000718, YS-LN02/Text/part0030.xhtml/p000719, YS-LN02/Text/part0030.xhtml/p000729]
    status: pending
    canon: false
  - source_term: rear guard
    proposed_vi: đội hậu vệ
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000744, YS-LN02/Text/part0030.xhtml/p000751]
    status: pending
    canon: false
  - source_term: mage
    proposed_vi: pháp sư
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000744]
    status: pending
    canon: false
  - source_term: Aerial 203rd Mage Battalion
    proposed_vi: Tiểu đoàn Pháp sư trên không 203
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000744]
    status: pending
    canon: false
risks:
  - "Stale self-check fields could reintroduce superseded terminology or obscure the separate unit-name proposal during a later handoff."
  - "All seven choices remain local proposals; this review neither promotes canon nor verifies usage beyond b23."
  - "Validator and diff-check were not run by this reviewer; translation signoff does not establish pipeline completion or commit eligibility."
next_action: coordinator_assign_self_check_corrections_then_reviewer_recheck_before_full_signoff
```

## Six original findings

All segment IDs below use the prefix `YS-LN02/Text/part0030.xhtml/`. Evidence is paraphrased from the assigned package; no source sentences are reproduced.

| Finding | Segment | Final translation assessment | Self-check / closure |
| --- | --- | --- | --- |
| B23-R01 | p000737 | Uses “nhà nước gác đêm”; retains diplomacy, tax payments and the obligation to protect citizens without restricting protection to internal order. | Finding resolution updated, but pending proposal, rationale and risk remain stale. Not fully closed. |
| B23-R02 | p000744 | Uses “Tiểu đoàn Pháp sư trên không 203”; preserves reported status, possession and the rear-guard role during withdrawal, without assigning an Air Force branch. | Finding resolution agrees and calls the designation provisional/non-canon. Original finding closed; missing structured unit-name entry tracked separately as B23-FS01. |
| B23-R03 | p000742 | Uses “Thật đấy—bằng cách nào?” after the preceding question about Tanya's participation in strategy; preserves the open question and uncertainty. | No contradictory self-check claim. Closed. |
| B23-R04 | p000710 | Success depends on the opponent acting as expected; wording does not imply knowing or voluntary cooperation. | No contradictory self-check claim. Closed. |
| B23-R05 | p000718 | Uses “tung lời tuyên truyền”; preserves the third-country channel and propaganda's distinct function. | Pending distinction agrees. Closed. |
| B23-R06 | p000746 | Uses “các gói đãi ngộ hậu hĩnh khi rời chức”; preserves payments for silence, expense and criticism of that expense. | Pending rationale updated, but proposal, finding resolution and risk still point to the metaphor. Not fully closed. |

## Seven pending choices

The operative choices are in `chapter6_b23_review_recommendations`, as required by the fix handoff. `chapter6_b23_translator_proposals` contains the six earlier proposals, including superseded options at p000737 and p000746; those earlier entries are historical proposals, not evidence that the final translation should revert. The reviewer section has seven entries, all explicitly `status: pending` and `canon: false`.

| Choice | Segment(s) | Translation versus reviewer ledger | Self-check pending_choices |
| --- | --- | --- | --- |
| Information warfare | p000719 | Matches “chiến tranh thông tin”. | Matches; pending. |
| Political concept | p000737 | Matches “nhà nước gác đêm”. | Mismatch: proposed_vi retains the old functional description. |
| Financial idiom | p000746 | Matches “các gói đãi ngộ hậu hĩnh khi rời chức”. | Mismatch: proposed_vi retains “dù vàng”; rationale alone is current. |
| Information / propaganda / disinformation | p000718, p000719, p000729; neutral information also at p000711 | Preserves the three proposed labels and their distinct roles. | Matches; pending. |
| Rear guard | p000744, p000751 | Matches “đội hậu vệ” consistently. | Matches; pending/non-canon. |
| Mage | p000744 | Matches “pháp sư” within the unit name. | Separate entry present and matches; pending/non-canon. |
| Unit designation | p000744 | Matches “Tiểu đoàn Pháp sư trên không 203”. | Missing as a separate pending entry; mentioned correctly and provisionally in findings. |

Thus seven-of-seven agreement is confirmed for translation versus reviewer ledger, but cannot be confirmed for self-check. Its six entries remain pending, its global risk statement rejects canon status, and its unit finding explicitly rejects canon promotion. Named canon has no approved term or character-name entry establishing any of these seven choices. Recommended repairs preserve the existing alternatives and rationales in the reviewer report/ledger, adjusting only the stale documentation and missing entry; no new canon decision is needed.

## Scope and verification limits

Read `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`; the five b23 handoffs (primary, translation, review, review-fixes, final-signoff); the initial b23 prose review, final b23 translation and self-check; the assigned b23 package; all five canon files named by the primary handoff; and only the two assigned b23 ledger sections. The package SHA-256 and all five named canon hashes match the handoff. The translation and package each contain 43 unique, ordered matching IDs from p000709 through p000751.

Independently compared all 43 rows for meaning and prose, with particular attention to the six repaired passages, conditionality, reported knowledge, speaker agency, pronouns and pending distinctions. The two emphasis spans at p000724 and p000728 retain their corresponding scope; no additional translation emphasis was found. DEC-P01-001 and DEC-P01-002 remain applicable, without creating new character or terminology canon.

No EPUB/PDF, other source package, manifest, other batch report or graph corpus was opened. No translation, self-check, canon, ledger, handoff or run-state file was edited. Only this report was written; no commit or pipeline validator/diff-check was performed. Review is complete, but full signoff remains false until the three documentation residuals are corrected and rechecked.

## Final correction addendum — 2026-10-14

Full reviewer signoff is granted. This addendum supersedes the withheld signoff and open documentation statuses above; the earlier assessment remains as review history. Rechecked only the three self-check residuals against the assigned b23 package, translation, corrected self-check, both b23 ledger sections and b23 reports/handoffs. No EPUB/PDF, other package or graph corpus was opened.

| Residual | Correction verified | Closure |
| --- | --- | --- |
| p000737 choice/risk — B23-R01 / B23-SELF-C01 | Both finding resolution and pending proposal now use “nhà nước gác đêm”, consistent with the translation and operative reviewer ledger. The rationale preserves the broad citizen-protection argument; the stale risk rejecting the applied label is gone. “Nhà nước tối thiểu” and “nhà nước bảo hộ tối thiểu” remain alternatives, while “nhà nước chỉ lo giữ gìn trật tự” is explicitly superseded history/an alternative. | Resolved; pending/non-canon. |
| p000746 choice/risk — B23-R06 / B23-SELF-C02 | Both finding resolution and pending proposal now use “các gói đãi ngộ hậu hĩnh khi rời chức”, matching the translation and operative reviewer ledger. The rationale accurately describes benefits on leaving employment; the stale metaphor risk is gone. “Gói đãi ngộ dù vàng”, “khoản trợ cấp thôi việc hậu hĩnh” and the historical “dù vàng” remain alternatives. | Resolved; pending/non-canon. |
| p000744 separate unit entry — B23-FS01 / B23-SELF-C03 | “Aerial 203rd Mage Battalion” now has its own structured pending entry, proposing “Tiểu đoàn Pháp sư trên không 203” at p000744, separate from “mage” → “pháp sư”. The rationale avoids assigning an Air Force branch; the alternative of retaining the unit name without a branch label is preserved in Vietnamese. The source uses a different word order for the same designation; the ledger identification remains unambiguous. | Resolved; pending/non-canon. |

The corrected self-check has seven separate pending entries. Its retained global risk explicitly states that the terminology and military proposals are pending and must not be treated as canon; the three corrected entries also explicitly state non-canon status in their rationales/resolutions. Removing the obsolete choice-specific risks leaves no contradiction with the current choices. The earlier translator-ledger proposals remain historical alternatives, while the reviewer-ledger recommendations remain operative. No alternative was promoted to canon.

The assigned package hash matches the handoff, and the translation hash is identical to the translation reviewed in the withheld report. Consequently, the existing translation resolutions for B23-R01 through B23-R06 remain valid without reopening the 43-row review. The two residual self-check closures complete B23-R01 and B23-R06; B23-R02 through B23-R05 remain closed, and B23-FS01 is now closed. No unresolved finding remains within this signoff task.

```yaml
role: reviewer
task_id: vol-02-ch-06-b23-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-06-b23-final-signoff-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b23-final-signoff-codex.md
source_package_sha256: 58d10ecd3c86a49f5af41f42932270d424bcbeb747fcda3a61c01da710602a4e
source_package_hash: matched
translation_sha256: 72f993aa62ce9cf2de9f635c759140b2b71a8db2f0bc93e5786cbdff594fd8ba
translation_unchanged_since_withheld_review: true
self_check_sha256: f2dbef190512f127fdb4a21ce1c5b78c2fd609fd74b4bdc8d8791072c8c62397
counts:
  residuals_rechecked: 3
  residuals_resolved: 3
  original_findings_fully_closed: 6
  self_check_pending_entries: 7
  serious: 0
  moderate: 0
  minor: 0
  low: 0
  unresolved_findings: 0
translation_signoff: true
full_signoff: true
unresolved_findings: []
term_recommendations:
  - {source_term: night-watchman state, proposed_vi: nhà nước gác đêm, segment_ids: [YS-LN02/Text/part0030.xhtml/p000737], status: pending, canon: false}
  - {source_term: golden parachutes, proposed_vi: các gói đãi ngộ hậu hĩnh khi rời chức, segment_ids: [YS-LN02/Text/part0030.xhtml/p000746], status: pending, canon: false}
  - {source_term: Aerial 203rd Mage Battalion, proposed_vi: Tiểu đoàn Pháp sư trên không 203, segment_ids: [YS-LN02/Text/part0030.xhtml/p000744], status: pending, canon: false}
validator: not_run
diff_check: not_run
commit: null
risks:
  - "All terminology choices remain local pending proposals; reviewer signoff does not promote canon or establish pipeline completion."
next_action: coordinator_resume_pipeline_completion_checks
```

Only this report was appended. No translation, self-check, ledger, canon, handoff or run-state file was edited, and no commit or pipeline validator was run.
