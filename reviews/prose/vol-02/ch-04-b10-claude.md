# Báo cáo review — vol-02-ch-04-b10 (Claude)

- Phạm vi: `YS-LN02/Text/part0022.xhtml/p000217` đến `p000245` (29 đoạn).
- Đầu vào đã đọc: shared.md, reviewer.md, config, handoff b10, gói nguồn b10 (sha256 khớp handoff), `canon/*`, mục `chapter4_b10_translation_proposals` và các mục sổ pending liên quan, `translations/vol-02/ch-04-b10.jsonl`.
- Không sửa translation, canon, handoff, ledger, checkpoint hay nguồn. Báo cáo không chép câu nguồn.
- Kết luận: không có lỗi nghiêm trọng. Nghĩa nhìn chung đầy đủ, không thấy thêm/bớt lớn. Có 3 lỗi vừa (đại từ nội tâm, tên Entente, tàu tuần dương chiến đấu) cần sửa trước khi tính hoàn tất lô; còn lại là lỗi nhẹ.

## Nghiêm trọng

Không có.

## Vừa

### M1 — p000217–p000236 (nội tâm ngôi thứ nhất dùng “tôi”)
- Vấn đề: các đoạn nội tâm ngôi thứ nhất của Tanya (p000217–219, 221–225, 227–231, 233–235) dùng “tôi”, trong khi p000242 trong cùng lô dùng “mình”.
- Căn cứ: DEC-P01-001 (đã duyệt) quy định nội tâm tự quy chiếu của Tanya dùng “mình”. Ledger ch01-b09 và ch04-b09 cũng ghi “mình” cho nội tâm. Gói nguồn có nhiều đoạn ngôi thứ nhất liền nhau, rồi chuyển sang ngôi thứ ba từ p000237.
- Đề xuất: đổi “tôi” thành “mình” trong các đoạn độc thoại nội tâm kể trên (vd. p000217 “muốn có”, p000219 “Tôi là kẻ hèn nhát”, p000221, p000222, p000223, p000227, p000233, p000234). Giữ “tôi” trong lời thoại trực tiếp (p000220, p000232, p000236).
- Độ bất định: đoạn đứng giữa hai lối là độc thoại hay trần thuật ngôi thứ nhất chưa rõ ở vài chỗ. Phương án thay thế: giữ “tôi” cho cả cụm và ghi vào ledger là ngoại lệ có chủ đích. Nên cho người giữ quyền sửa quyết định một lần để nhất quán.

### M2 — p000238, p000244 (Entente Alliance)
- Vấn đề: bản dịch dùng “Liên minh Hiệp ước”, lệch với ledger.
- Căn cứ: ledger ch04-b01, b03, b05, ch03-b20 và ch02-b03 đều đề xuất “Liên minh Entente”. Mục pending b10 ghi lý do “align with existing project pending term”, nhưng thực tế phương án “Liên minh Hiệp ước” chỉ có trong danh sách thay thế.
- Đề xuất: đổi thành “Liên minh Entente” (giữ Entente là tên riêng, như các batch trước). Sửa lại mục pending b10 cho khớp.

### M3 — p000222 (cruisers or battle cruisers)
- Vấn đề: “tuần dương hạm hay tuần dương hạm hạng nặng” dịch sai loại tàu. Battle cruiser không phải heavy cruiser.
- Căn cứ: ledger ch04-b06 đề xuất “tàu tuần dương chiến đấu” cho battle cruiser; tàu hạng nặng không có trong gói nguồn.
- Đề xuất: “tàu tuần dương hay tàu tuần dương chiến đấu” (hoặc theo thuật ngữ ledger cho cruiser). Đồng bộ với b06.

## Nhẹ

- **p000236** (depth charges): “khối thuốc nổ chống tàu ngầm” dài và dễ hiểu sai thành thuốc nổ rời. Gợi ý “mìn sâu”/“bom chìm” (đề xuất, chưa canon). Cần thêm mục pending.
- **p000236 / p000241 / p000238** (explosion/interceptor formulas): xem đánh giá thuật ngữ bên dưới; sổ trước dùng “thuật thức”.
- **p000223, p000244** (defensive shell): “khiên phòng thủ” / “lớp khiên phòng thủ”, lệch ledger ch01-b07 “lớp vỏ phòng ngự”. Nên thống nhất một cách (shell ≠ shield). Gợi ý theo ledger.
- **p000224** (big ships): “chiến hạm lớn” có thể thu hẹp thành battleship; nguồn chỉ nói tàu lớn. Gợi ý “những con tàu lớn”.
- **p000228** (destroyer): “khu trục hạm” lệch với “tàu khu trục” ở các đoạn khác trong lô. Thống nhất “tàu khu trục”.
- **p000237** (most certainly a result of training): “hẳn là nhờ luyện tập” yếu hơn nguồn. Gợi ý “chắc chắn là nhờ huấn luyện”.
- **p000237** (lời lẩm bẩm): “Mình né được chúng” là lời nói thành tiếng; DEC-P01-001 chỉ chốt “mình” cho nội tâm. Không sai, nhưng độ bất định về xưng hô lời thoại; giữ nếu coordinator xem là lời tự nhủ.
- **p000242** (literally assault): “thật sự lao vào hắn” mất chơi chữ với “assault formation” ở p000230 (“đội hình xung kích”). Gợi ý “xung kích đúng nghĩa đen”/“tấn công thẳng vào hắn”.
- **p000244** (twists into him): bỏ chi tiết xoáy lưỡi lê; bản dịch chỉ nói “cắm sâu”. Gợi ý “xoáy sâu vào người hắn”. Đơn vị “hải lý/giờ” gượng; gợi ý “hải lý một giờ” hoặc “knot”.
- **p000219** (“của anh”): “mức độ hèn nhát của anh” nghe như gọi người nghe; gợi ý “của mỗi người”.

## Đã kiểm tra, không thấy lỗi
- Nhấn mạnh (DEC-P01-002): italic ở p000238, 239, 242 khớp đúng phạm vi nguồn; không thêm italic thừa.
- Số liệu (127 mm, 4.500 feet, hơn bốn trăm knot) khớp. Phủ định và logic suy luận ở p000228–230 giữ nguyên.
- Đại từ trần thuật ngôi thứ ba p000237–245 dùng “nó”, đúng DEC-P01-001. Không thấy cấp bậc nhân vật cần xét trong lô.

## Đánh giá ba lựa chọn tạm trong mục pending b10 (không nâng canon)

1. **spindle shape → “đội hình con thoi”** (p000231): chấp nhận được như nhãn tạm. “Con thoi” trong tiếng Việt thường gợi hình thoi (rhombus) hoặc con thoi dệt, không hẳn là hình suốt/thon hai đầu. Giữ pending, độ tin cậy 0.45 là hợp lý. Phương án thay thế “đội hình hình thoi dài” gần nghĩa hơn một chút; không có ví dụ trước trong sổ để đối chiếu.
2. **explosion formulas → “công thức nổ”** (p000236): chưa khớp lối chung của sổ, vì P01-formulas và ch01-b05 dùng “thuật thức”. Lý do mục pending (“matching existing register”) chưa chính xác. Đề xuất: “thuật thức nổ” nếu coordinator muốn nhất quán toàn bộ; nếu giữ “công thức” thì ghi rõ là lệch. Cũng áp dụng cho “công thức đánh chặn” (p000238).
3. **Entente Alliance → “Liên minh Hiệp ước”** (p000238, p000244): không nên giữ; xem M2. Đề xuất “Liên minh Entente”.

## Ghi chú thuật ngữ mới đề nghị đưa vào ledger (pending, không canon)
- depth charges: đề xuất “mìn sâu” (thay thế: “bom chìm”).
- cruiser / battle cruiser: dùng “tàu tuần dương” / “tàu tuần dương chiến đấu” cho nhất quán.
- Không có quyết định nào ảnh hưởng cốt truyện.

## Độ bất định
- M1 phụ thuộc cách coordinator phân loại các đoạn ngôi thứ nhất là nội tâm hay trần thuật. Tôi chưa đọc translations các batch trước nên không đối chiếu trực tiếp văn bản, chỉ dựa vào ledger.

```yaml
role: reviewer
task_id: vol-02-ch-04-b10
state: done
segment_ids: [YS-LN02/Text/part0022.xhtml/p000217 .. YS-LN02/Text/part0022.xhtml/p000245]
files_written: [reviews/prose/vol-02/ch-04-b10-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 3, minor: 11}
unresolved_findings: [M1, M2, M3]
term_recommendations:
  - {source_term: Entente Alliance, proposed_vi: Liên minh Entente, segment_ids: [p000238, p000244], status: pending}
  - {source_term: explosion/interceptor formulas, proposed_vi: thuật thức nổ / thuật thức đánh chặn, segment_ids: [p000236, p000238, p000241], status: pending}
  - {source_term: battle cruiser, proposed_vi: tàu tuần dương chiến đấu, segment_ids: [p000222], status: pending}
  - {source_term: depth charge, proposed_vi: mìn sâu, segment_ids: [p000236], status: pending}
  - {source_term: spindle shape, proposed_vi: đội hình con thoi (giữ pending; thay thế đội hình hình thoi dài), segment_ids: [p000231], status: pending}
review_path: reviews/prose/vol-02/ch-04-b10-claude.md
risks: [pronoun_consistency_M1]
commit: null
next_action: translator_fix
```
