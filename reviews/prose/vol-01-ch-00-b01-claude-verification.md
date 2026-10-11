# Xác nhận bản dịch đã sửa — vol-01-ch-00-b01

- Phạm vi: xác nhận các mục từ `reviews/prose/vol-01-ch-00-b01-claude-review.md` theo ba nhóm được giao. Không thêm nhận xét văn phong mới; không sửa bản dịch.
- Căn cứ: `translations/vol-01/ch-00-b01.jsonl` (hiện tại), nguồn cục bộ của lô, `canon/` (`DEC-P01-001`, `DEC-P01-002`, `style-guide.md`), `handoffs/vol-01/ch-00-b01.yml`.
- Tiền tố mã đoạn: `YS-LN01/Text/chapter001.xhtml/`.
- Định dạng: segment_id | đã xử lý / chưa xử lý | mức độ còn lại | lý do ngắn.

## 1. Ba lỗi nghiêm trọng cũ

| segment_id | trạng thái | mức độ còn lại | lý do |
|---|---|---|---|
| p000002 | đã xử lý | không | Câu hỏi nội tâm cuối đoạn đã hỏi về “điều gì” bị quên, khớp đối tượng câu hỏi của nguồn; không còn chuyển sang hỏi lý do. |
| p000009 | đã xử lý | không | Câu hỏi đầu đoạn đã hỏi về bản chất/tình trạng, không còn thu hẹp thành địa điểm; phạm vi nhấn mạnh bao hai câu hỏi nội tâm, khớp nguồn. |
| p000017 | đã xử lý | không | Đã bỏ cách tự xưng mẹ–con; xưng hô trung tính, không còn suy ra quan hệ thân thuộc (`DEC-P01-001`). Giữ nguyên yêu cầu mở miệng và tên gọi. |

## 2. Các lỗi vừa: xưng hô/đăng ký, sắc thái, thuật ngữ

| segment_id | nhóm | trạng thái | mức độ còn lại | lý do |
|---|---|---|---|---|
| p000001 | thuật ngữ | đã xử lý | không | “năm Thống nhất” bỏ yếu tố “lịch” và được ghi trong `notes` là đề xuất, chưa chốt. Chỉ lưu ý: mục này chưa có trong `canon/glossary-pending.yml`; người giữ quyền sửa có thể bổ sung sau. |
| p000010 | sắc thái | đã xử lý | không | “khinh rẻ” thay cho “khinh ghét”, đúng mức sắc thái của nguồn. |
| p000011 | sắc thái | đã xử lý | không | Giả định đã là suy đoán hợp lý, không còn là trạng thái yên tâm; mức chắc chắn khớp nguồn. |
| p000013 | xưng hô | đã xử lý | không | Đã bỏ “ngoan”; lời gọi âu yếm không còn thành lời khen hành vi; giữ yêu cầu phát âm “a”. |
| p000015 | xưng hô | đã xử lý | không | Cùng cách gọi với p000013, nhất quán trong cảnh. |
| p000018 | xưng hô | đã xử lý | không | Đã bỏ “cô bé” và “mình” trong trần thuật; dùng “nó”, phù hợp `DEC-P01-001`. |
| p000019 | xưng hô | đã xử lý | không | “bà” đã thay bằng “nữ tu”, không còn suy ra tuổi. |
| p000020 | xưng hô | đã xử lý | không | Đã bỏ “con”; lời gọi thống nhất với p000013/p000015/p000017, không gán quan hệ mẹ–con. |

Ghi chú tổng: lời gọi “cưng” dùng nhất quán ở p000013, p000015, p000017, p000020. Đây là lựa chọn dịch chưa được duyệt thành canon, nhưng không còn gán quan hệ hay đánh giá ngoài nguồn nên không phải vấn đề nghiêm trọng hay vừa.

## 3. Cú pháp Markdown nhấn mạnh ở p000022

| segment_id | trạng thái | mức độ còn lại | lý do |
|---|---|---|---|
| p000022 | đã xử lý | không | Chuỗi hiện tại gồm một cặp `*…*` bọc phần mở đầu, “nó” để thường, rồi một cặp `*…*` bọc phần “—mình—là Tanya.”. Cả hai cặp đều có dấu mở/đóng hợp lệ theo CommonMark, nên hiển thị đúng. Phạm vi nhấn khớp nguồn: phần nhấn trong nguồn là cụm mở đầu và phần sau “it”, còn “it” để thường. |

## Kết luận

- Ba lỗi nghiêm trọng cũ: đã xử lý cả ba, không còn mức độ nghiêm trọng.
- Các lỗi vừa về xưng hô, sắc thái, thuật ngữ: đã xử lý cả tám mục, không còn mục nào ở mức nghiêm trọng hoặc vừa.
- Cú pháp nhấn mạnh p000022: hợp lệ.
- Còn lại duy nhất một lưu ý nhỏ, không chặn nghiệm thu: bổ sung đề xuất “năm Thống nhất” vào `glossary-pending` (p000001).
