# Báo cáo signoff sửa lỗi vol-02-ch-03-b12 (Claude)

- Task: `vol-02-ch-03-b12-final-signoff`; checkpoint_generation 580; 25 đoạn `YS-LN02/Text/part0018.xhtml/p000116`–`p000140`.
- Package nguồn: `work/vol-02/batches/ch-03-b12-source.jsonl`, sha256 `fc8dccfe…c43eff` — khớp handoff.
- Phạm vi đọc: shared.md, reviewer.md, config, handoff b12 (gồm metadata `translator_followup`), package b12, bản dịch b12 hiện tại, báo cáo review đầu `ch-03-b12-claude.md`, mục `chapter3_b12_translation_proposals` trong sổ pending. Không mở batch khác, không mở EPUB/PDF.
- Báo cáo không trích câu nguồn. Mọi lựa chọn thuật ngữ vẫn là đề xuất tạm, không phải canon.

## Kết luận

Hai lỗi mức vừa M1 và M2 đã được sửa đúng. Chín điểm mức nhẹ được translator xử lý đều đạt. Cấu trúc 25 dòng đúng, nhấn mạnh đúng. Không còn lỗi nghiêm trọng hay mức vừa. Có thể cho qua signoff.

## Xác minh M1 và M2

- **M1 — p000123 (đối tượng "mua"): đã sửa.** Câu dịch nay nói Tiểu đoàn Viper bỏ tiền túi mua "số rượu này", đúng đối tượng, khớp p000121 (nguồn gốc rượu) và p000125 (mời tiệc). Phần còn lại giữ nguyên nghĩa, không đổi sắc thái.
- **M2 — p000117 (đại từ Tanya): đã sửa.** Chủ ngữ trần thuật nay là "nó", nhất quán với p000120 và p000134–p000138 theo DEC-P01-001. Đối tượng được gọi rõ bằng "cô ấy", nên không còn nhầm chủ thể giữa Tanya và Trung úy Serebryakov. Câu vẫn dừng ở dấu gạch ngang như cấu trúc ngắt lời.

## Xác minh các điểm nhẹ đã sửa (translator_followup)

| Đoạn | Kết quả |
|---|---|
| p000122 | Đạt: "Một phần cũng vì…" giữ đúng nghĩa "một phần", không còn thành phỏng đoán. |
| p000125 | Đạt: lời thoại dùng "tôi đãi tiểu đoàn mình"; "nâng ly cảm ơn" khớp ngữ cảnh p000126. Nội tâm vẫn dùng "mình". |
| p000126 | Đạt: "Vâng" trung tính, không áp đặt quan hệ. |
| p000127 | Đạt: "phụ cấp nguy hiểm" song song với các khoản phụ cấp khác. |
| p000128 | Đạt: "Đây cũng là dịp tốt" đúng nghĩa cơ hội. |
| p000133 | Đạt: "sợ giao tranh" thay cho "sợ chiến tranh". |
| p000137 | Đạt: "quyết tâm" đúng nghĩa. |
| p000138 | Đạt: "Đáp xuống, chiếm các khẩu pháo bờ biển" không còn trùng "đổ bộ" của p000135. |
| p000140 | Đạt: "một nhân viên tham mưu Hải quân Đế quốc" không thêm cấp bậc. |

Chín đoạn trên khớp danh sách `also_resolved_minor` trong handoff. Danh sách `changed_segments` (11 đoạn) khớp với các đoạn cần sửa của báo cáo đầu.

## Cấu trúc và nhấn mạnh

- **Cấu trúc:** đủ 25 dòng JSONL, `segment_id` liên tục từ p000116 đến p000140, không trùng, không thiếu. Mã đoạn ổn định, `source_sha256` và `glossary_version` đúng handoff.
- **Nhấn mạnh (DEC-P01-002):** nguồn chỉ có một đoạn có thẻ nhấn mạnh là p000124, nằm ở phần mở đầu, gồm hai từ. Bản dịch chỉ có một cặp `*...*` ở đúng đoạn đó, đúng vị trí đầu câu và đúng độ dài hai từ. Không đoạn nào khác có dấu `*`.

## Điểm còn lại (mức nhẹ, không chặn)

- p000132: "căng như dây đàn" và "nghẹt thở" vẫn là hình ảnh bổ sung nhẹ so với nguồn. Báo cáo đầu đã ghi là có thể giữ như lựa chọn văn phong; không cần sửa.
- p000122: "mình" trong trần thuật phản thân quanh Tanya là cách dùng chấp nhận được, không gây mơ hồ.
- p000138: "vịnh hẹp" cho fjord vẫn là cách dịch tạm; nếu canon sau này giữ "fjord" thì thống nhất lại. Đây là thuật ngữ pending, không phải lỗi.
- Các điểm "chấp nhận được" ở báo cáo đầu (p000116, p000120, p000129, p000135) không đổi.

## Mức độ còn lại

| Mức | Số lượng | Mã đoạn |
|---|---|---|
| Nghiêm trọng | 0 | — |
| Vừa | 0 | — |
| Nhẹ | 0 (chặn) | — (chỉ các ghi chú không chặn ở trên) |

## Thuật ngữ — đề xuất tạm (không đổi so với báo cáo đầu)

- Northern Sea Fleet (p000134): giữ "Hạm đội Bắc Hải"; thay thế "Hạm đội Biển Bắc"; độ bất định 0,5; không suy lore thực.
- Viper Battalion (p000123, p000125): giữ "Tiểu đoàn Viper"; thay thế "Tiểu đoàn Rắn lục"; độ bất định 0,7.
- Sĩ quan trực ban tuần: "sĩ quan trực ban tuần" (đề xuất đã ghi trong handoff).
- Cấp bậc Serebryakov: giữ nguyên dạng từng đoạn nguồn, chưa chuẩn hóa.
- Xưng hô thoại Tanya với cấp dưới: "tôi"; nội tâm giữ "mình".
- Đáp lời trung tính: "Vâng".
- "phụ cấp nguy hiểm".

## Rủi ro còn lại

Không có lỗi nghiêm trọng hay vừa. Các thuật ngữ trên vẫn pending, chưa canon; coordinator ghi nhận trong sổ pending. Validator và diff_check chưa chạy trong vai trò reviewer; coordinator chạy trước khi commit.
