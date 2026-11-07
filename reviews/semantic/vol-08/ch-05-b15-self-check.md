# Báo cáo tự kiểm (Self-Check): `vol-08-ch-05-b15`

- **Phạm vi:** `YS-LN08/Text/chapter018.xhtml/p000518` đến `YS-LN08/Text/chapter018.xhtml/p000554` (37 đơn vị).
- **Người dịch:** `argon-low`
- **Tệp đích:** `translations/vol-08/ch-05-b15.jsonl`
- **Trạng thái Sign-off:** Đã rà soát theo `reviews/prose/vol-08/ch-05-b15-argon-review.yml` (0 lỗi serious/moderate/minor; tuân thủ toàn bộ `locked_choices` và `pending_term_recommendations`) và cập nhật toàn bộ 37/37 dòng sang `status: "reviewed"`.

## 1. Kiểm tra nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic và thời gian của giả định (`meaning`)
- **`p000518`–`p000528`:** Giữ trọn vẹn mạch tranh luận gay gắt giữa Trung tá Drake và nữ sĩ quan chính trị Liên bang. Bảo toàn lập luận của Drake về nguyên tắc chỉ huy theo ý định mệnh lệnh của quân nhân Khối Thịnh vượng chung, sự phản bác việc bị ràng buộc bởi mệnh lệnh của Đảng Cộng sản nước khác, đề xuất chỉ huy động xe tăng Liên bang phối hợp với pháp sư Khối Thịnh vượng chung, và yêu cầu nối máy với Đại tá Mikel tại Sở chỉ huy khi phát hiện Ác quỷ sông Rhine đã biến mất khỏi trận địa.
- **`p000529`–`p000541`:** Giữ đúng diễn biến Trung úy Mary Sue vô tình nghe thấy tin tức về kẻ thù, đánh rơi bi đông và tự ý bay vút đi truy kích bất chấp nỗ lực cản trở của các pháp sư tình nguyện đang trực chiến cũng như tiếng gọi của Drake.
- **`p000542`–`p000552`:** Bảo toàn độc thoại nội tâm và tính toán chiến thuật của Drake: nhận thức sự điên rồ khi đơn độc đối đầu lực lượng phòng ngự chủ lực của địch và nỗi đau của các gia đình có người tử trận ở chính quốc, nhưng vẫn quyết định hủy kế hoạch đột kích trận địa để đuổi theo cầm chân pháp sư thuộc Kampfgruppe Lergen, đồng thời gửi thông báo về Sở chỉ huy cho Đại tá Mikel.
- **`p000553`–`p000554`:** Chuyển cảnh sang không phận Quân khu phía Đông ở đầu đội hình Tiểu đoàn Pháp sư Trên không số 203; giữ đúng ý đồ bay lặng lẽ để xuyên thủng và tập kích vào hậu phương quân địch.

## 2. Kiểm tra xưng hô và giọng nhân vật (`pronouns`)
- **Trung tá Drake và nữ sĩ quan chính trị (`p000518`–`p000528`):** Tiếp nối nhất quán từ `ch-05-b14`: Drake xưng `tôi` (hoặc `chúng tôi` / `chúng ta` tùy ngữ cảnh đồng minh hay đơn vị riêng), gọi nữ sĩ quan chính trị là `cô` / `thưa cô`; nữ sĩ quan chính trị xưng `tôi` / `chúng tôi` / `chúng ta`, gọi Drake là `ngài`. Trong trần thuật, Drake được gọi là `ông`, độc thoại nội tâm xưng `mình`.
- **Trung úy Mary Sue (`p000530`–`p000541`):** Trong trần thuật gọi là `cô` / `cô nàng`; trong lời thoại và suy nghĩ bực tức của Drake gọi là `con bé đó` (`p000536`) hoặc `cô ta` (`p000537`, `p000539`, `p000541`); đối tượng mà Mary Sue truy đuổi (Ác quỷ sông Rhine) được gọi là `ả ta` / `ả` (`p000532`, `p000539`) để phân biệt rõ hai nhân vật nữ trong cùng câu.
- **Đoạn mở đầu góc nhìn Tiểu đoàn 203 (`p000554`):** Dịch ngôi thứ nhất số nhiều là `chúng tôi` theo giọng trần thuật của Tanya khi nói về hành động của toàn tiểu đoàn.

## 3. Kiểm tra nhấn mạnh (`emphasis`)
- Đối chiếu trực tiếp trường `xhtml` theo quy chuẩn `DEC-P01-002`:
  - `p000520`: Có một cụm `<html:em>` ở câu hỏi tu từ cuối đoạn -> bọc `*...*` đúng phạm vi câu cuối.
  - `p000537`: Có một cụm `<html:em>` ở suy nghĩ trực tiếp của Drake -> bọc `*Mình phải ngăn cô ta lại*`.
  - `p000542`: Toàn bộ đoạn nằm trong `<html:em>` -> bọc `*...*` toàn bộ đoạn dịch.
  - `p000546`: Câu hỏi trách móc ở cuối đoạn nằm trong `<html:em>` -> bọc `*...*` đúng phạm vi câu hỏi.
  - Toàn bộ 33 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` và không sử dụng dấu `*` trong bản dịch.

## 4. Thuật ngữ và mục chờ chốt (`pending_terms`)
- Đã tra cứu `canon/glossary.yml`, `canon/glossary-pending.yml` và `work/run-state/pending-terms-index.yml`, áp dụng nhất quán các phương án đã dùng ở các batch trước:
  - `Khối Thịnh vượng chung`, `Đại tá Mikel`, `Đảng Cộng sản`, `các nhà báo phương Tây`, `Đế quốc`, `sĩ quan chính trị`, `Sở chỉ huy`, `trường sĩ quan`, `mặt trận phía đông`, `Ác quỷ sông Rhine`, `cuộc tổng tấn công`, `trung úy pháp sư`, `Trung úy Sue`, `các pháp sư tình nguyện`, `chính quốc`, `Kampfgruppe Lergen`, `trận đánh truy kích`, `Quân khu phía Đông`, `Tiểu đoàn Pháp sư Trên không số 203`.
- Không phát sinh thuật ngữ mới gây mơ hồ cần dừng pipeline.
