# Review vol-02-ch-04-b12 (Claude, prose/semantic)

- Phạm vi: 31 đoạn, `p000026`–`p000056` (tiền tố `YS-LN02/Text/part0024.xhtml/`).
- Đầu vào đã đọc: shared.md, reviewer.md, config, handoff b12, source package b12, 5 canon được handoff nêu (glossary, style-guide, characters, decisions, glossary-pending), `chapter4_b12_translation_proposals`, `translations/vol-02/ch-04-b12.jsonl`.
- Không sửa translation/canon/handoff/ledger/checkpoint. Validator/diff_check: not_run. Commit: null.

## 1. Kiểm tra retry theo handoff và metadata nguồn

- Hash khớp: source package `25b8fbc5…c251a4`; glossary `d5f19d64…`, style-guide `64724c03…`, characters `354f6573…`, decisions `9f173f9c…`, glossary-pending `65458cca…` đều trùng handoff.
- JSONL có đủ 31 dòng, đúng thứ tự mã đoạn p000026→p000056, không thiếu/thừa. Mọi dòng mang `source_sha256` = `3ac53161…` và `glossary_version` = `sha256:d5f19d64…`, đúng handoff. Ghi chú: `notes` rỗng ở mọi dòng. Bốn thuật ngữ được ghi ở ledger chứ không chèn vào bản dịch, đúng style-guide.
- Handoff ghi lease đã nhả, `prior_attempt: blocked_no_changes_no_translation_written`, translator session trùng session trước. Đây là mô tả của handoff, tôi không có căn cứ để kiểm tra thêm ngoài phạm vi. Không thấy dấu hiệu retry lệch handoff.
- Lưu ý: `translator` là `translator-ch04-b12`, `status: draft`. Không thấy vấn đề.

## 2. Nhận xét chung

Nghĩa nhìn chung chính xác, không có đoạn bị bỏ sót hay thêm ý lớn, không đảo phủ định. Văn phong tự nhiên, nhịp tốt. Các vấn đề chính nằm ở quy ước đã duyệt (đại từ trần thuật, chữ nghiêng), không phải ở nghĩa.

## 3. Phát hiện

### Vừa

**M1 — p000040: mất nhấn mạnh (DEC-P01-002) và đổi điểm nhìn của câu nội tâm.**
Nguồn có đoạn in nghiêng là lời nghĩ trực tiếp của Tanya, theo sau là mệnh đề dẫn "Tanya laments". Bản dịch đưa vào dạng gián tiếp ("điều Tanya mong mỏi mà thôi, cô than thở"), không dùng `*...*`, và gọi Tanya bằng tên bên trong chính câu nghĩ. Nguồn chỉ có "That's probably wishful thinking". Đề xuất: *Có lẽ chỉ là mong ước hão huyền thôi*, nó than thở (hoặc giữ cấu trúc tương đương, đặt trong `*...*`).

**M2 — p000053: mất nhấn mạnh (DEC-P01-002).**
Nguồn in nghiêng cụm "We accomplished our mission" (lời tự nhủ). Bản dịch viết "Tự nhủ rằng mình đã hoàn thành nhiệm vụ" ở dạng gián tiếp, không có `*...*`. Đề xuất: *Ta đã hoàn thành nhiệm vụ*, Tanya tự nhủ… (đại từ nội tâm theo "mình"/DEC-P01-001: *Mình đã hoàn thành nhiệm vụ*).

**M3 — p000040, p000044, p000050: đại từ trần thuật về Tanya dùng "cô".**
DEC-P01-001 (đã duyệt): trần thuật về Tanya ở giai đoạn này dùng "nó", nội tâm dùng "mình". Bản dịch dùng "cô" (p40 "cô than thở"; p44 "cô đã không chuẩn bị", "ước tính cô được cung cấp"; p50 "cô suýt bật cười"). Phần nội tâm "mình" thì đúng. Chú ý: DEC nói "không tự mở rộng sang chủ thể hoặc giai đoạn khác" và các mã đoạn căn cứ đều thuộc LN01, nên chưa rõ vol-02 ch4 có thuộc "giai đoạn này" không. Tôi không có căn cứ để đoán, và không đọc batch khác để so cách xử lý. Đề xuất: coordinator xác nhận phạm vi DEC cho vol-02 rồi áp dụng nhất quán cho cả chương; nếu áp dụng thì đổi "cô" thành "nó" ở ba đoạn này. Ghi vào ledger như lựa chọn tạm, không nâng canon.

### Nhẹ

**m1 — p000033: mất sắc thái "some of the credit".** "Cứ để hạm đội nhận lấy phần công lao này" nghe như nhường toàn bộ. Nguồn "get some of the credit" là chia một phần. Đề xuất: "nhường hạm đội một phần công lao".

**m2 — p000032: xưng hô lẫn trong cùng đoạn.** "mình nhanh chóng đưa chúng tôi vào đội hình… chúng ta cũng không làm tệ lắm". Ba cách gọi cho một nhóm. Nguồn: "I pull us… we didn't do so badly". Đề xuất: "đưa cả đội vào đội hình trở về… chúng ta cũng không làm tệ lắm".

**m3 — p000039: cú pháp.** "Làm sao còn mặt mũi nào trở về căn cứ?" thừa "nào" và lủng củng. Đề xuất: "Còn mặt mũi nào mà trở về căn cứ?"

**m4 — p000040: "vẫn" thừa.** "Nhưng bầu không khí vẫn nặng nề" nguồn là "the mood is heavy because…", không có "vẫn". Đề xuất: bỏ "vẫn".

**m5 — p000052: "friends".** Nguồn "our friends" chỉ lực lượng bạn (hạm đội), "đồng đội" gợi cùng đơn vị. Đề xuất: "quân bạn" hoặc "lực lượng bạn". Cũng liên quan tới bối cảnh p33, "hạm đội".

**m6 — p000053: "straightforward summary".** "thẳng thắn" gợi sự trung thực/không giấu giếm; nguồn nghĩa là báo cáo ngắn gọn, rõ ràng. Đề xuất: "tóm tắt tình hình một cách ngắn gọn, rõ ràng".

**m7 — p000038: ký hiệu chú thích.** Bản dịch giữ "¹⁴" dạng chữ Unicode nhỏ. Style-guide yêu cầu mọi lựa chọn về chú thích phải ghi trong decisions.md trước khi áp dụng thống nhất; chưa có DEC. Đề xuất: coordinator xác nhận cách biểu diễn đánh số chú thích; không phải lỗi dịch. Ngoài ra "chưa tung hết sức" tạm ổn; nguồn "aren't unleashing their fury yet" có thể thêm sắc thái "phát huy uy lực".

**m8 — p000055: "Các anh".** Người nói là Urban Control, nói với Tanya và đơn vị. "Các anh" gán giới tính nam cho cả nhóm; nguồn không nêu. DEC-P01-001 cấm suy từ đoạn thiếu ngữ cảnh. Đề xuất: "Các bạn/Bên các vị" hoặc dùng diễn đạt trung tính: "Có thể tiếp tục bám theo địch không?" (pending, chọn trung tính).

**m9 — p000056: chủ ngữ bị lược và "họ".** Nguồn "When I promptly gave Command…", bản dịch lược "tôi" rồi dùng "họ" cho Command và "chúng tôi" trong khi phần còn lại của narration dùng "mình". Có thể chấp nhận nhưng nên thống nhất: "Mình lập tức báo… họ yêu cầu bên mình truy đuổi" hoặc tương tự.

**m10 — p000035: "For a destroyer".** "Nếu là khu trục hạm" làm yếu thành giả định. Nguồn gán loại tàu là khu trục hạm, chỉ phần "unknown ship… moderate damage" là phỏng đoán. Đề xuất: "Với một khu trục hạm thì nó di chuyển khá chậm."

## 4. Đánh giá bốn thuật ngữ pending (không phải canon)

| Mã | Thuật ngữ | Đề xuất của translator | Đánh giá | Khuyến nghị tạm |
|---|---|---|---|---|
| vol02-ch04-b12-vt-fuses (p38) | VT fuses | ngòi nổ VT | Hợp lý, giữ nhãn kỹ thuật, không suy diễn nghĩa viết tắt; kèm chú thích 14. Rủi ro: không thể kiểm tra nội dung chú thích. | Giữ "ngòi nổ VT"; ghi thay thế "ngòi VT". Cân nhắc lại khi có nội dung chú thích. |
| vol02-ch04-b12-depth-charges (p40) | depth charges | mìn sâu | Đúng với cách dùng chuyên môn tiếng Việt ("mìn sâu"), nhất quán với b10 theo ledger. Tôi không đọc b10 để kiểm tra. | Giữ "mìn sâu"; thay thế "bom chìm". |
| vol02-ch04-b12-coastal-defense-ship (p47) | coastal defense ship | tàu phòng thủ bờ biển | Dịch nghĩa đen, ổn. Có thể là loại tàu cụ thể (hộ vệ ven bờ/duyên hải). Chưa có căn cứ lore. | Giữ tạm "tàu phòng thủ bờ biển". Không ảnh hưởng cốt truyện cần hỏi người dùng. |
| vol02-ch04-b12-urban-control (p54, p55) | Urban Control | Urban Control | Giữ nguyên là lựa chọn trung tính, nhất quán với "Pixie 01" kiểu hô hiệu. Dịch "Bộ chỉ huy đô thị" sẽ suy diễn. Trong p56 "Command" đã dịch "Bộ chỉ huy". | Giữ nguyên "Urban Control". Độ bất định: cho là callsign. Ghi vào `pending-terms.yml`, không cần dừng. |

Không có quyết định ảnh hưởng cốt truyện cần hỏi người dùng.

## 5. Thống kê

- Nghiêm trọng: 0
- Vừa: 3 (M1, M2, M3)
- Nhẹ: 10 (m1–m10)

Không còn lỗi nghiêm trọng. M1–M3 cần được người giữ quyền sửa xử lý trước khi hoàn tất lô (completion yêu cầu không còn lỗi vừa).
