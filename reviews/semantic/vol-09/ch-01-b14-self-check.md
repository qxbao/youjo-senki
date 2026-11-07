# Báo cáo tự kiểm (Self-Check): vol-09-ch-01-b14

## 1. Phạm vi và kết quả chung
- **Task ID:** `vol-09-ch-01-b14`
- **Phạm vi đoạn:** `YS-LN09/Text/chapter004.xhtml/p000389` đến `YS-LN09/Text/chapter004.xhtml/p000436` (48 đoạn).
- **Trạng thái các dòng dịch:** `reviewed` (48/48 dòng, đã hoàn tất translator sign-off theo `ch-01-b14-argon-review.yml`; `findings: []`, tuân thủ toàn bộ `pending_term_recommendations` và `locked_choices`).
- **Tự kiểm chung:** Đã dịch đầy đủ 48/48 đoạn, giữ nguyên ranh giới đoạn, mã đoạn, hàm ý lập luận, sắc thái đối thoại và độc thoại nội tâm. Không chép câu nguồn tiếng Anh vào báo cáo.

## 2. Kiểm tra Điểm nhìn, Đại từ và Xưng hô (DEC-P01-001)
- **Độc thoại nội tâm của Tanya:** Dùng đại từ tự quy chiếu `mình` (`p000402`, `p000403`, `p000405`, `p000423`, `p000427`, `p000429`, `p000432`) và `chúng ta` khi quy chiếu tập thể quân đội/Đế quốc (`p000397`, `p000403`, `p000404`, `p000410`, `p000414`, `p000415`, `p000416`, `p000432`).
- **Trần thuật ngôi thứ ba:** Dùng tên riêng `Tanya` hoặc đại từ `cô` (`p000391`, `p000396`, `p000401`, `p000421`, `p000436`); dùng `ông` hoặc tên riêng `Rudersdorf` / `vị tướng` / `vị trung tướng` cho Trung tướng Rudersdorf (`p000401`, `p000409`, `p000410`, `p000414`, `p000421`, `p000422`, `p000423`, `p000427`, `p000428`, `p000429`, `p000431`, `p000432`, `p000434`, `p000436`).
- **Đối thoại giữa Trung tướng Rudersdorf và Trung tá Tanya:**
  - Rudersdorf (cấp trên, Trung tướng, Cục phó Cục Tác chiến) xưng `ta` (hoặc `chúng ta` khi nói chung về quân đội/Đế quốc), gọi Tanya là `cô` hoặc `Trung tá` (`p000393`, `p000400`, `p000408`, `p000411`, `p000413`, `p000419`, `p000424`, `p000426`, `p000431`, `p000433`), giữ đúng giọng điệu bề trên pha chút mỉa mai, cay đắng và nhất quán với lô trước (`ch-01-b13`).
  - Tanya (cấp dưới, Trung tá Pháp sư) xưng `tôi`, gọi Rudersdorf là `ngài` / `thưa Tướng quân` (`p000392`, `p000399`, `p000407`, `p000412`, `p000418`, `p000420`, `p000425`, `p000430`).

## 3. Kiểm tra Nhấn mạnh / Chữ nghiêng (DEC-P01-002)
Đã kiểm tra toàn bộ thẻ `<html:em>` trong trường `xhtml` và bảo toàn chính xác phạm vi nhấn mạnh bằng dấu `*...*`:
- `p000418`: `*Kranke*` (1 cụm từ tiếng Đức được in nghiêng).
- `p000433`: `*Kranke*` (1 cụm từ tiếng Đức được in nghiêng).
- `p000434`: `*Thanh lọc*` (1 từ nhấn mạnh ở đầu câu nội tâm phản ứng lại lời của Rudersdorf ở `p000433`).
- Các đoạn còn lại không có thẻ `<html:em>`, không tự ý thêm dấu `*...*`.

## 4. Kiểm tra Ngữ nghĩa, Logic và Giả định
- **Ẩn dụ buồng lái máy bay (`p000398`):** Giữ rõ nấc tăng tiến trong so sánh của Tanya — từ việc đang bay thì nhận tin tổ bay biến mất khỏi buồng lái sang việc nhận thông báo ngay trên chuyến bay rằng chính cái buồng lái đã biến mất.
- **Liên hệ lịch sử và phàn nàn về đãi ngộ / khế ước xã hội (`p000402`–`p000406`):** Giữ đúng điển tích về chính trị gia người Nhật từ chức vì tình hình châu Âu phức tạp và kỳ quái, cũng như chuỗi phàn nàn về đạo đức nghề nghiệp, tình hình lương thực, làm việc vượt mức lương, thiếu tiếp tế, lạm phát và sự vi phạm khế ước xã hội.
- **Ẩn dụ con bệnh và giả định điều kiện lý tưởng (`p000411`–`p000418`, `p000433`–`p000434`):**
  - `p000411`–`p000412`: Giữ đúng hình ảnh ẩn dụ Đế quốc là người mắc bệnh nan y ngay giữa độ sung sức nhất của cuộc đời và câu hỏi liệu có cách nào điều dưỡng cho bình phục không.
  - `p000413`–`p000416`: Giữ đúng cấu trúc giả định trái thực tế của Rudersdorf (nếu Liên bang không còn trong bức tranh toàn cục thì có lẽ một cuộc chiến tranh trên bộ sẽ có cơ hội) và sự châm biếm trong nội tâm Tanya về việc tưởng tượng ra các điều kiện lý tưởng bằng phép màu.
  - `p000418`, `p000433`–`p000434`: Giữ nguyên từ tiếng Đức `*Kranke*` (con bệnh) theo nguyên bản in nghiêng, kết nối tự nhiên với mạch ẩn dụ y khoa và động từ `*Thanh lọc*` (vừa mang nghĩa y khoa là tẩy rửa/loại bỏ phần hoại tử của con bệnh, vừa mang hàm ý chính trị nguy hiểm khiến Tanya cảnh giác ở `p000434`).

## 5. Thuật ngữ và Mục từ Pending
Đã đối chiếu và áp dụng nhất quán các phương án tạm đã có trong sổ pending:
- Cơ quan và quân đội (`p000392`, `p000396`, `p000403`): `Bộ Tư lệnh Tối cao`, `mục tiêu chiến lược`, `Quân đội Liên bang`, `Đế quốc`, `Lục quân Đế quốc`.
- Thuật ngữ chính trị – triết học đã có trong sổ pending (`p000395`): `lý tính nhà nước`.
- Mặt trận và địa danh (`p000391`, `p000399`, `p000400`, `p000415`, `p000431`): `thủ đô`, `miền đông`, `phía tây`.
- Thuật ngữ/từ ngoại lai mới ghi nhận đề xuất tạm:
  - `khế ước xã hội` (`p000405`).
  - `*Kranke*` (`p000418`, `p000433` — giữ nguyên từ tiếng Đức in nghiêng chỉ "con bệnh" trong phép ẩn dụ y khoa về Đế quốc).
