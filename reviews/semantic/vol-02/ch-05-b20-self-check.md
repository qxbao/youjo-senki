role: translator
task_id: vol-02-ch-05-b20
state: done
segment_ids:
  start: YS-LN02/Text/part0026.xhtml/p000496
  end: YS-LN02/Text/part0026.xhtml/p000534
  count: 39
checks:
  - meaning, negation, conditionality, chronology, and speaker viewpoint checked against the assigned package
  - italic emphasis retained for the letter and italicized thoughts
  - segment identifiers and order preserved
findings:
  - id: B20-F01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000497
    issue: hypothetical past rendered as present/future possibility
    resolution: restored past hypothetical without implying the outcome occurred
  - id: B20-F02
    severity: moderate
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000508, YS-LN02/Text/part0026.xhtml/p000509, YS-LN02/Text/part0026.xhtml/p000510, YS-LN02/Text/part0026.xhtml/p000511, YS-LN02/Text/part0026.xhtml/p000529]
    issue: pronoun choice in Tanya narration differed from the provisional chapter choice
    resolution: repeated Tanya where needed and omitted pronouns where clear; at p000529 kept “mình” inside the interior thought and used Tanya in the following narration, preserving the distinct first-person letter voice at p000530–p000534
  - id: B20-F03
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000534
    issue: laughter target and speaker were reversed
    resolution: restored the meaning that others laugh at an officer who loses a soldier to bad potatoes; retained the final denial that it is funny
  - id: B20-F04
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000514
    issue: added an unsupported direct-supervisor relationship
    resolution: changed to “cấp trên của anh ấy”
  - id: B20-F05
    segment_id: YS-LN02/Text/part0026.xhtml/p000516
    severity: minor
    issue: operational context was rendered more specifically as a campaign
    resolution: changed to “trong một nhiệm vụ tác chiến”; preserved sudden illness and long-term serviceability assessment
  - id: B20-F06
    severity: minor
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000514, YS-LN02/Text/part0026.xhtml/p000526]
    issue: Magic Major differed from the nearest chapter reviewer proposal
    resolution: applied coordinator choice “Thiếu tá Pháp sư” at both occurrences; remains pending and non-canon
  - id: B20-F07
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000530
    issue: protective films wording differed from the earlier local proposal
    resolution: changed to “màn bảo hộ”, distinct from “lớp vỏ phòng ngự”; added no mechanism
pending_terms:
  - source_term: computation orb
    proposed_vi: quả cầu tính toán
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000500]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: Magic Major
    proposed_vi: Thiếu tá Pháp sư
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000514, YS-LN02/Text/part0026.xhtml/p000526]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: Warrant Officer
    proposed_vi: Chuẩn úy
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000513]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: Field Service Badge First Class
    proposed_vi: Huy hiệu Phục vụ Chiến trường Hạng Nhất
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000523]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: Disability Medal
    proposed_vi: Huân chương Thương tật
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000523]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: NBC weapon
    proposed_vi: vũ khí NBC
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000530]
    volume: vol-02
    chapter: 5
    status: pending
risks:
  - All new term and rank renderings are provisional proposals, not canon.
  - Medical and military administrative terms may need consistent treatment in later batches.
validator: pass
validator_exit_code: 0
diff_check: pass
files_written:
  - translations/vol-02/ch-05-b20.jsonl
  - reviews/semantic/vol-02/ch-05-b20-self-check.md
commit: null
