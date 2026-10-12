role: reviewer
task_id: vol-01-ch-01-b08-fixes-signoff
state: done
scope: xác nhận sửa M1–M7 của reviews/prose/vol-01-ch-01-b08-claude.md
inputs_read:
  - handoffs/vol-01/ch-01-b08.yml
  - reviews/prose/vol-01-ch-01-b08-claude.md
  - translations/vol-01/ch-01-b08.jsonl
  - work/vol-01/batches/ch-01-b08-source.jsonl (cục bộ, bị Git bỏ qua)
  - work/run-state/pending-terms.yml (chỉ tra mục b08-*)
files_written:
  - reviews/prose/vol-01-ch-01-b08-fixes-signoff-claude.md
translations_edited: false
commit: null
workers_launched: false
counts:
  resolved: 7
  unresolved_serious: 0
  unresolved_moderate: 0
  new_serious: 0
  new_moderate: 0
verdicts:
  - id: M1
    segment_ids: [p000129, p000136, p000139, p000143]
    status: resolved
    evidence: 'Cả 4 đoạn dùng nguyên "Norden Control" (p129 "Một nhân viên ở Norden Control"; p136 "Norden Control gọi Fairy 08"; p139 "Norden Control, đã rõ"; p143 "gọi Norden Control"). Không còn "Đài kiểm soát Norden".'
  - id: M2
    segment_ids: [p000130]
    status: resolved
    evidence: '"air bursts" → "dùng đạn nổ trên không", khớp ledger b08-air-burst; không còn "khai hỏa trên không".'
  - id: M3
    segment_ids: [p000130]
    status: resolved
    evidence: '"time on target missions" → "bắn cho đạn cùng rơi trúng mục tiêu một lúc", đúng ý đạn cùng rơi một lúc, khớp ledger b08-time-on-target (vẫn là đề xuất tạm, confidence 0.55).'
  - id: M4
    segment_ids: [p000132]
    status: resolved
    evidence: 'Câu cuối nguồn "If I report…" → "Nếu mình báo cho các vị thần chiến tranh…"; nội tâm dùng "mình" theo DEC-P01-001.'
  - id: M5
    segment_ids: [p000133]
    status: resolved
    evidence: '"Fuji Firepower Review" → "buổi trình diễn hỏa lực Fuji", khớp b05 và ledger b08-fuji-firepower-review; không còn "Lễ duyệt binh". (Sắc thái "cute" → "nhỏ bé" là lỗi nhẹ m5, ngoài phạm vi M1–M7.)'
  - id: M6
    segment_ids: [p000136]
    status: resolved
    evidence: '"commencing observed fire" → "bắt đầu bắn có quan sát"; không còn "hiệu chỉnh", không mâu thuẫn với p137 "Không cần chỉnh làn bắn".'
  - id: M7
    segment_ids: [p000137]
    status: resolved
    evidence: '"Initiate fire for effect" → "Bắt đầu bắn hiệu lực"; không còn "bắn tiêu diệt mục tiêu".'
unresolved_findings: []
corrections_needed: []
notes:
  - 'Chỉ kiểm M1–M7; các lỗi nhẹ m1–m13 không được đánh giá lại trong lượt này, coordinator/translator tự quyết việc áp dụng.'
  - 'Thuật ngữ b08-* vẫn là đề xuất tạm, không nâng thành canon. Độ bất định còn lại: time on target (0.55) và radio Over/Out/roger (0.4).'
  - 'Quan sát ngoài phạm vi: p139/p140 vẫn dùng "đã rõ" (b01/b05 dùng "rõ") — thuộc m10, mức nhẹ.'
next_action: coordinator có thể đóng M1–M7 trong handoff (serious 0, moderate 0 còn lại)
