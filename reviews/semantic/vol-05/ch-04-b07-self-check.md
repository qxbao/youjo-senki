# Báo cáo tự kiểm dịch thuật & Sign-off: `vol-05-ch-04-b07`

## 1. Thông tin chung
- **Task ID**: `vol-05-ch-04-b07-translator-signoff` (parent: `vol-05-ch-04-b07`)
- **Phạm vi**: `YS-LN05/Text/part0022.html/p000237` đến `YS-LN05/Text/part0022.html/p000268` (32 đoạn)
- **Tác tử dịch**: `argon-low`
- **Tệp đầu ra**: `translations/vol-05/ch-04-b07.jsonl`
- **Báo cáo phản biện đã xử lý**: `reviews/prose/vol-05/ch-04-b07-argon-review.yml`

## 2. Xử lý các Findings trong Argon Review
- **`p000254` (moderate)**: Đã đổi `Bảo châu` thành `quả cầu` để khớp với thuật ngữ pending đã khóa xuyên suốt từ vol-01 đến vol-05.
- **`p000259` (moderate)**: Đã đổi `các đơn vị ma đạo sư` thành `các đơn vị pháp sư` để đồng bộ với sổ pending toàn dự án.
- **`p000261` (moderate)**: Đã đổi `những ma đạo sư` thành `những pháp sư` và đổi đại từ độc thoại nội tâm của Đại tá Mikel từ `chúng mình` sang `chúng ta` (`*Ắt hẳn họ triệu tập chúng ta là vì đang thua trận.*`), tuân thủ `locked_choices` và `DEC-P01-001`.
- **`p000243` (minor)**: Đã đồng bộ đại từ ngôi thứ nhất số nhiều trong độc thoại nội tâm của Tanya từ `Chúng mình / chúng mình` thành `Bọn mình / bọn mình` cho liền mạch với batch `ch-04-b06`.
- **`p000244` (minor)**: Đã chỉnh `Một người biết điều như Weiss` thành `Một người chín chắn như Weiss` để diễn đạt chuẩn xác phẩm chất khách quan, hợp lý của cấp dưới.
- **`p000248` (minor)**: Đã đồng bộ `Bàn tay vô hình của Chúa` thành `Bàn tay vô hình của Thượng đế` khớp với sổ pending của vol-05.

## 3. Kiểm tra tính đầy đủ, định dạng và Locked Choices
- Đã cập nhật trường `status` của toàn bộ 32/32 dòng từ `"draft"` sang `"reviewed"`.
- Trường `glossary_version` và `source_sha256` khớp chính xác với thông tin trong tệp bàn giao `handoffs/vol-05/ch-04-b07.yml`.
- Bảo toàn tuyệt đối dấu nhấn in nghiêng `*...*` theo đúng thẻ nhấn trong nguyên bản tại `p000244` và `p000261` theo `DEC-P01-002`.
- Tuân thủ đầy đủ toàn bộ `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-05/ch-04-b07-argon-review.yml`:
  - Bộ Tổng tham mưu (`p000237`, `p000246`), thuật chú giải văn bản / lối diễn giải mở rộng (`p000239`, `p000240`), tàu viễn dương (`p000241`), khu vực tác chiến / giới chóp bu (`p000243`).
  - Thiếu tá Weiss (`p000244`, `p000248`), Trung úy Grantz / Trung úy Serebryakov (`p000248`), Bàn tay vô hình của Thượng đế (`p000248`), Chúa (`p000255`).
  - Liên bang / Căn cứ Novo Kholmo (`p000249`, `p000258`), Đại tá Mikel (`p000250`–`p000253`, `p000268`), trại gulag / trại tập trung (`p000251`, `p000253`, `p000264`), quả cầu (`p000254`), Đảng Cộng sản / những người Cộng sản (`p000256`, `p000259`), các đơn vị pháp sư / những pháp sư (`p000259`, `p000261`).
