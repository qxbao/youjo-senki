# Báo cáo tự kiểm (Self-Check): `vol-09-ch-03-b18`

## 1. Phạm vi & tính đầy đủ
- **Task ID**: `vol-09-ch-03-b18`
- **Số đoạn**: 31 đoạn (`YS-LN09/Text/chapter012.xhtml/p000001` đến `YS-LN09/Text/chapter012.xhtml/p000031`).
- **Trạng thái**: Tất cả 31 dòng trong `translations/vol-09/ch-03-b18.jsonl` đều có `"status": "reviewed"`, giữ nguyên thứ tự `segment_id`, khớp `source_sha256` và `glossary_version` trong handoff.
- Không bỏ sót câu, mệnh đề, thông tin quân sự hoặc chi tiết chuyển cảnh nào.

## 5. Xử lý Argon Review & Sign-off (`vol-09-ch-03-b18-translator-signoff`)
- **Finding 1 (`p000003`, minor - pronouns)**: Giữ nguyên đại từ trần thuật ngôi thứ ba `nó` theo đúng `DEC-P01-001` và `locked_choices` tại `p000003`, `p000012`, `p000014`, `p000027`, đảm bảo nhất quán hoàn toàn với chuỗi lô `ch-03-b12` đến `ch-03-b17`.
- **Finding 2 (`p000004`, minor - style_repetition)**: Đổi đại từ `nó` đầu tiên (chỉ chương trình học) thành `chương trình ấy` (`chương trình ấy *lẽ ra phải* truyền đạt cho nó`) theo đúng khuyến nghị của Argon Reviewer để tránh lặp đại từ khác quy chiếu mà vẫn tuân thủ `locked_choices` và `DEC-P01-002`.
- **Pending Terms & Locked Choices**: Tất cả 8 mục `pending_term_recommendations` và toàn bộ 31 mục `locked_choices` trong `reviews/prose/vol-09/ch-03-b18-argon-review.yml` đều đã được áp dụng chính xác và bảo toàn đầy đủ.
- **Cập nhật trạng thái**: Đã chuyển `"status"` của toàn bộ 31 dòng trong `translations/vol-09/ch-03-b18.jsonl` từ `"draft"` sang `"reviewed"`.

## 2. Xưng hô & Điểm nhìn (`DEC-P01-001`)
- **Độc thoại nội tâm & tự thuật ngôi thứ nhất của Tanya** (`p000002`, `p000005`–`p000009`, `p000017`, `p000020`, `p000021`, `p000024`, `p000028`, `p000030`): dùng `mình` / `bọn mình` tự nhiên, giữ đúng chất thực dụng, châm biếm ngầm và ngao ngán khi phải gánh vác nhiệm vụ ngoài sở trường chính quy.
- **Trần thuật ngôi thứ ba về Tanya** (`p000003`, `p000004`, `p000009`, `p000012`, `p000014`, `p000027`, `p000028`): dùng `nó`, thống nhất hoàn toàn với các batch trước của chương 3 (`ch-03-b11` đến `ch-03-b17`).
- **Đối thoại trên tàu ngầm** (`p000018`, `p000019`, `p000022`, `p000023`, `p000025`, `p000026`, `p000029`, `p000031`):
  - Thủy thủ báo cáo với Tanya (`p000018`): gọi `Thưa Trung tá`, xưng hô lịch sự `cô`, nhắc tới chỉ huy tàu là `Thuyền trưởng Barchet`.
  - Tanya đáp lời thủy thủ (`p000019`): tự xưng `tôi`, gọi Thuyền trưởng Barchet là `ngài ấy`.
  - Tanya và Thuyền trưởng Barchet (`p000022`, `p000023`, `p000025`, `p000026`, `p000031`): cả hai giữ thái độ lịch thiệp giữa sĩ quan không quân ma pháp đi nhờ tàu và hạm trưởng tàu ngầm hải quân; Tanya tự xưng `tôi` — gọi `Thuyền trưởng` / `Thuyền trưởng Barchet` / `ngài`; Barchet tự xưng `tôi` (ẩn chủ ngữ lịch sự) — gọi `Trung tá` / `Trung tá Degurechaff` / `cô`.

## 3. Bảo toàn nhấn mạnh (`DEC-P01-002`)
- Chỉ duy nhất đoạn `YS-LN09/Text/chapter012.xhtml/p000004` có thẻ nhấn mạnh trong XHTML gốc và đã được bảo toàn chính xác bằng dấu sao đơn `*lẽ ra phải*`.
- Các thẻ neo trang ở `p000001` và `p000016` là thẻ đánh dấu vị trí trang, không phải nhấn mạnh nên không sinh dấu `*...*`.
- Tất cả 30 đoạn còn lại không có nhấn mạnh trong nguồn và bản dịch hoàn toàn không tự ý thêm dấu `*...*`.

## 4. Thuật ngữ Canon & Pending
- Đã đối chiếu và áp dụng nhất quán các thuật ngữ canon và pending trong sổ cái:
  - `Tổng hành dinh Bộ Tổng tham mưu` (`p000002`)
  - `học viện quân sự` / `học viện` (`p000002`, `p000003`)
  - `trường đại học quân sự` (`p000003`)
  - `Đế quốc` / `Hải quân Đế quốc` (`p000003`, `p000005`)
  - `các chiến dịch tác chiến liên hợp` (`p000005`)
  - `học thuyết hải quân` (`p000006`)
  - `các chuyến khảo sát thực địa của bộ tham mưu` (`p000007`)
  - `sĩ quan tham mưu` / `sĩ quan ma pháp` (`p000007`)
  - `Không hạm đội 16` / `máy bay trinh sát` (`p000013`)
  - `Trung tá` / `Trung tá Degurechaff` (`p000018`, `p000023`, `p000026`)
  - `Thuyền trưởng Barchet` / `Thuyền trưởng` / `thuyền trưởng` (`p000018`, `p000021`, `p000022`, `p000024`, `p000025`)
  - `thiếu tá` (`p000024`)
  - `hải đội` (`p000028`)
  - `tàu chủ lực`, `tàu tuần dương`, `tàu tuần dương hạng nặng`, `tàu khu trục`, `tàu tuần dương hạng nhẹ`, `tàu sân bay` (`p000029`, `p000031`)
  - `Khối Thịnh vượng chung` (`p000031`)
