# Báo cáo tự kiểm (Self-Check): `vol-09-ch-03-b19` (Sign-off)

## 1. Phạm vi & tính đầy đủ
- **Task ID**: `vol-09-ch-03-b19-translator-signoff` (parent: `vol-09-ch-03-b19`)
- **Số đoạn**: 37 đoạn (`YS-LN09/Text/chapter012.xhtml/p000032` đến `YS-LN09/Text/chapter012.xhtml/p000068`).
- **Trạng thái**: Tất cả 37 dòng trong `translations/vol-09/ch-03-b19.jsonl` đã được cập nhật từ `"status": "draft"` sang `"status": "reviewed"`, giữ nguyên thứ tự `segment_id`, khớp chính xác `source_sha256` và `glossary_version` trong handoff.
- **Xử lý findings từ Argon Review (`reviews/prose/vol-09/ch-03-b19-argon-review.yml`)**:
  - `p000038` (`minor` - `pronouns`): Giữ nguyên đại từ trần thuật ngôi thứ ba `nó` theo `DEC-P01-001` và đúng `locked_choices` của `p000038`, nhất quán với chuỗi lô `ch-03-b12` đến `ch-03-b18`.
  - `p000044` (`minor` - `meaning_precision`): Tiếp nhận khuyến nghị rút gọn cụm `màn sương mù chiến tranh đầy phiền toái ấy` thành `màn sương mù đầy phiền toái ấy` để không tự thêm từ giải thích ngoài nguyên văn và khớp với `locked_choices` của `p000044`.
- Bảo đảm tuân thủ đầy đủ toàn bộ 37 `locked_choices` và 8 `pending_term_recommendations` trong báo cáo review của Argon.

## 2. Xưng hô & Điểm nhìn (`DEC-P01-001`)
- **Độc thoại nội tâm & tự thuật ngôi thứ nhất của Tanya** (`p000037`, `p000043`, `p000044`, `p000049`–`p000051`, `p000058`–`p000062`, `p000064`, `p000066`): dùng `mình` (số ít) và `bọn mình` / `chúng ta` (số nhiều tùy phạm vi đơn vị tác chiến hay phạm vi quân sự/quốc gia chung), giữ đúng giọng điệu tỉnh táo, thực dụng và pha chút châm biếm của Tanya.
- **Trần thuật ngôi thứ ba về Tanya** (`p000033`, `p000038`, `p000041`, `p000054`, `p000065`): dùng `nó` (hoặc tên riêng `Tanya`), nối tiếp hoàn toàn nhất quán với `ch-03-b18`.
- **Đối thoại giữa Tanya và Thuyền trưởng Barchet** (`p000032`, `p000035`, `p000036`, `p000039`, `p000040`, `p000042`, `p000045`–`p000048`, `p000052`–`p000056`):
  - Giữ thái độ lịch thiệp, chuyên nghiệp giữa hai sĩ quan phối hợp tác chiến: Tanya tự xưng `tôi` / `chúng tôi` / `chúng ta`, gọi Barchet là `ngài`; Barchet tự xưng `tôi` / `chúng tôi`, gọi Tanya là `Trung tá` (`thưa Trung tá` ở `p000046`), `cô` (`p000055`) và gọi đơn vị của Tanya là `các vị` (`p000048`).
  - Ở câu lẩm bẩm khép lại chương (`p000068`), giữ câu cảm thán cô đọng tự nhiên, không chèn đại từ thừa.

## 3. Bảo toàn nhấn mạnh (`DEC-P01-002`)
- Toàn bộ 37 đoạn trong XHTML gốc của `ch-03-b19` không có thẻ nhấn mạnh nào (chỉ có các thẻ neo trang tại `p000034` và `p000053`).
- Bản dịch tuân thủ nghiêm ngặt `DEC-P01-002`: không tự ý thêm bất kỳ dấu sao `*...*` nào trong cả 37 đoạn.

## 4. Thuật ngữ Canon & Pending
- Đã tra cứu và áp dụng nhất quán các thuật ngữ canon và pending theo `pending_term_recommendations`:
  - `tàu chở dầu`, `tàu chiến lớn`, `tàu sân bay` (`p000032`, `p000033`, `p000037`–`p000039`)
  - `Barchet` / `vị thuyền trưởng` (`p000033`, `p000049`, `p000054`)
  - `máy bay trinh sát` / `các phi cơ trinh sát` (`p000036`, `p000037`)
  - `tiêm kích yểm trợ trực tiếp` (`p000036`)
  - `Máy bay trên tàu sân bay` (`p000038`)
  - `đơn vị pháp sư hải quân đánh bộ` (`p000038`)
  - `tin tức tình báo tiền trạm` / `khoa học quân sự` / `Clausewitz` (`p000043`)
  - `thưa Trung tá` (`p000046`)
  - `loại động cơ đốt trong đời cũ` / `loại chạy điện đời mới` / `mồi nhử` / `ngư lôi` (`p000048`, `p000050`)
  - `Ildoa` / `Đế quốc` / `quốc gia tham chiến` / `cường quốc tham chiến` / `cường quốc trung lập nghiêm ngặt` / `chủ nghĩa Machiavelli` (`p000058`–`p000062`, `p000064`–`p000067`)
