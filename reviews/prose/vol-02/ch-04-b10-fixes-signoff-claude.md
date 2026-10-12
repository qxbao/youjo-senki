# Signoff review sau sửa — vol-02-ch-04-b10 (Claude)

- Phạm vi: `YS-LN02/Text/part0022.xhtml/p000217` đến `p000245` (29 đoạn).
- Đầu vào đã đọc: shared.md, reviewer.md, config, handoff b10, gói nguồn b10 (sha256 `f4733bf1…` khớp handoff), canon liên quan (DEC-P01-001), mục `chapter4_b10_translation_proposals` trong `work/run-state/pending-terms.yml`, báo cáo review gốc, `translations/vol-02/ch-04-b10.jsonl`.
- Không sửa translation, canon, handoff, ledger, checkpoint hay nguồn. Báo cáo không chép câu nguồn.
- Kết luận: M1, M2, M3 đã được sửa đúng. Không còn lỗi nghiêm trọng hoặc vừa. Các lỗi nhẹ còn lại đã ghi ở báo cáo gốc và không chặn signoff.

## Kiểm tra các sửa của translator

### M1 — đại từ nội tâm của Tanya: ĐẠT
- Nội tâm dùng “mình”: p000217, 219, 221, 222, 223, 224 (không có đại từ), 225, 227, 233, 234, 242. Các đoạn không chứa đại từ (p000218, 228–229, 235) không bị đổi sai; p000230–231, 233, 235 dùng “chúng tôi” cho chủ ngữ số nhiều, đúng nghĩa nguồn.
- Lời thoại trực tiếp giữ “tôi”: p000220, p000232; p000236 không có đại từ ngôi thứ nhất nên không có chỗ lệch.
- Trần thuật ngôi thứ ba p000237–245 vẫn dùng “nó”, đúng DEC-P01-001; “mình” trong p000237 (lẩm bẩm, “đơn vị mình”) và p000242 nhất quán với nội tâm. Không phát hiện đoạn nào trong danh sách coordinator thực chất không phải nội tâm.
- Không còn “tôi” sót trong đoạn nội tâm.

### M2 — Entente: ĐẠT
- p000238 và p000244 đều dùng “Liên minh Entente”; khớp mục pending `vol02-ch04-b10-entente-alliance` và các batch trước. Không còn “Liên minh Hiệp ước”.

### M3 — cruiser / battle cruiser: ĐẠT
- p000222 dùng “tàu tuần dương hay tàu tuần dương chiến đấu”; đúng hai loại tàu của nguồn, khớp mục pending `cruiser` và `battle-cruiser`. Không còn “hạng nặng”.

## Kiểm tra lỗi còn lại

Nghiêm trọng: không có. Vừa: không có. Nghĩa, phủ định, số liệu (127 mm, 4.500 feet, hơn bốn trăm knot), logic p000228–230 và nhấn mạnh (*…* ở p000238, 239, 242) không thay đổi so với lần review gốc và vẫn đúng.

Nhẹ còn mở (không chặn, chỉ ghi nhận; coordinator đã ghi “minor_findings_recorded_only”):
- p000236: “khối thuốc nổ chống tàu ngầm” (depth charge) vẫn dài/dễ hiểu sai; ledger đề xuất “mìn sâu”/“bom chìm”.
- p000236, p000238, p000241: bản dịch dùng “công thức nổ/đánh chặn”, trong khi ledger b10 ghi đề xuất chính là “thuật thức nổ/đánh chặn” (“công thức” là phương án thay thế). Lệch giữa bản dịch và ledger; không ảnh hưởng nghĩa.
- p000223, p000244 “khiên phòng thủ”; p000228 “khu trục hạm”; p000224 “chiến hạm lớn”; p000219 “của anh”; p000237 “hẳn là nhờ luyện tập”; p000242 mất chơi chữ “assault”; p000244 “hải lý/giờ” và chi tiết xoáy lưỡi lê.

## Đề xuất thuật ngữ (pending, không canon)
- Coordinator nên làm cho ledger và bản dịch khớp nhau ở “thuật thức/công thức” (nghiêng về chọn một cách duy nhất cho toàn chương) và ghi quyết định vào ledger.
- depth charge: “mìn sâu” (thay thế “bom chìm”) nếu sau này sửa nhẹ.
- Không có quyết định nào ảnh hưởng cốt truyện.

```yaml
role: reviewer
task_id: vol-02-ch-04-b10
state: done
segment_ids: [YS-LN02/Text/part0022.xhtml/p000217 .. YS-LN02/Text/part0022.xhtml/p000245]
files_written: [reviews/prose/vol-02/ch-04-b10-fixes-signoff-claude.md]
validator: not_run
diff_check: not_run
findings:
  - {severity: moderate, id: M1, status: resolved}
  - {severity: moderate, id: M2, status: resolved}
  - {severity: moderate, id: M3, status: resolved}
counts: {serious: 0, moderate: 0, minor: 11}
unresolved_findings: []
term_recommendations:
  - {source_term: explosion/interceptor formulas, proposed_vi: "thống nhất một cách (ledger đang ghi thuật thức, bản dịch dùng công thức)", segment_ids: [p000236, p000238, p000241], status: pending}
  - {source_term: depth charge, proposed_vi: mìn sâu (thay thế bom chìm), segment_ids: [p000236], status: pending}
review_path: reviews/prose/vol-02/ch-04-b10-fixes-signoff-claude.md
risks: []
commit: null
next_action: signoff
```
