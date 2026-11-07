# Báo cáo tự kiểm dịch thuật — `vol-09-ch-04-b03`

- **Task ID**: `vol-09-ch-04-b03`
- **Phạm vi**: `YS-LN09/Text/chapter014.xhtml/p000078` đến `YS-LN09/Text/chapter014.xhtml/p000119` (42 đoạn)
- **Tác tử**: `argon-low`
- **Bản dịch**: `translations/vol-09/ch-04-b03.jsonl`
- **Trạng thái Sign-off**: Đã đối chiếu báo cáo `reviews/prose/vol-09/ch-04-b03-argon-review.yml` (0 serious, 0 moderate, 0 minor), xác nhận tuân thủ toàn bộ `locked_choices` và `pending_term_recommendations`, cập nhật toàn bộ 42 dòng từ `draft` sang `reviewed`.

## 1. Kiểm tra nghĩa, phủ định, đối tượng và logic (`meaning`)
- **`p000078`–`p000087`**: Bảo toàn trọn vẹn cú sốc và sự bàng hoàng của thủy thủ đoàn Khối Thịnh vượng chung khi chứng kiến chiến hạm lớn nhất trước chiến tranh, niềm tự hào của hải quân (`*Hood*` / `*Hood Hùng mạnh*`) bị đánh chìm chỉ bằng một đòn trúng đích duy nhất. Giữ nguyên chi tiết vị thuyền trưởng kiêu hãnh thề cùng chung số phận với con tàu trong khi thủy thủ đoàn thậm chí không kịp quằn quại trong đau đớn.
- **`p000088`–`p000091`**: Phản ánh đúng phẩm chất tinh nhuệ và kỷ luật của hạm đội Khối Thịnh vượng chung: dù đau xót nhưng lập tức phá vỡ đội hình đồng bộ để cơ động né tránh ngư lôi, song nỗ lực bẻ lái ấy vẫn trở nên vô ích.
- **`p000092`–`p000099`**: Giữ sát diễn biến tàu sân bay `*Ark Royale*` trúng đòn: cột nước dựng lên bên mạn tàu, thân tàu nhanh chóng nghiêng hẳn khiến những chiếc máy bay đang cố cất cánh trên boong đâm vào nhau bốc cháy, và nỗ lực dập lửa bất thành của các pháp sư hải quân đánh bộ cùng thủy thủ đoàn đã thoát thân kịp thời.
- **`p000100`–`p000106`**: Giữ đúng mệnh lệnh quyết liệt của thuyền trưởng tàu khu trục yêu cầu quan sát mặt nước tìm vệt rẽ nước của ngư lôi và sẵn sàng lấy thân tàu chắn đường đạn để bảo vệ thủy thủ đoàn tàu `*Hood*` cùng tàu `*Ark Royale*`, cũng như nỗi uất ức vì không thể dừng tàu cứu viện do tàu ngầm địch đang rình rập.
- **`p000107`–`p000112`**: Bảo toàn cảnh tàu tuần dương `*Yliastral*` chạy hết tốc lực ngay phía trước tàu khu trục `*Bermuda*` rồi trúng đòn gãy đôi và chìm xuống, buộc tàu `*Bermuda*` phải đổi hướng tránh bị cuốn theo, trong khi vị thuyền trưởng tiếp nhận quyền chỉ huy cố che chắn cho con tàu đang chìm và các trắc thủ sonar bắt được tín hiệu địch.
- **`p000113`–`p000119`**: Giữ nguyên chuỗi phát hiện tiếng chân vịt đẩy từ một, hai rồi cả một bầy sói tàu ngầm địch, quyết định đổi hướng bước vào tác chiến chống ngầm của các tàu tuần dương hạng nhẹ và tàu khu trục Khối Thịnh vượng chung bất chấp việc làm giảm hiệu quả sonar để ngăn chặn thêm các đợt phóng ngư lôi, cùng việc tung ra vũ khí mới là dàn cối chống ngầm Hedgehog rải nhiều đạn con.

## 2. Kiểm tra xưng hô và giọng điệu (`pronouns`)
- Toàn bộ lô thuộc góc nhìn trần thuật ngôi thứ ba bên phía Hải quân Khối Thịnh vượng chung (không có mặt Tanya).
- Trần thuật dùng đại từ trung tính, phù hợp với ngữ cảnh hải chiến (`họ`, `các thủy thủ`, `thủy thủ đoàn`, `vị thuyền trưởng`).
- Thoại mệnh lệnh và báo cáo trên tàu khu trục (`p000094`–`p000095`, `p000100`–`p000102`, `p000113`–`p000116`) giữ nhịp điệu khẩn trương, dứt khoát của hải quân trong tình huống khẩn cấp (`Rõ, thưa Thuyền trưởng!`, `chúng ta` – `chúng`).

## 3. Kiểm tra nhấn mạnh (`emphasis`)
- Tuân thủ nghiêm ngặt `DEC-P01-002`: chỉ đặt dấu `*...*` ở đúng 15 đoạn có thẻ nhấn mạnh trong `xhtml` nguồn:
  - Các đoạn nhấn mạnh câu cảm thán nội tâm: `p000078`, `p000086`, `p000087`.
  - Các đoạn in nghiêng tên riêng và biệt danh tàu chiến: `p000079`, `p000082`, `p000083`, `p000084`, `p000088`, `p000092`, `p000095`, `p000097`, `p000104`, `p000105`, `p000107`, `p000108`, `p000110`, `p000111`.
- Các thẻ neo trang trong `p000089` và `p000110` là thẻ đánh dấu vị trí trang, không sinh dấu nhấn mạnh ngoài phạm vi thẻ `em`. Toàn bộ 25 đoạn còn lại không có thẻ `em`/`i` đều không chứa dấu `*`.

## 4. Kiểm tra thuật ngữ và mục chờ duyệt (`pending_terms`)
- Đã áp dụng nhất quán các thuật ngữ trong `work/run-state/pending-terms-index.yml`:
  - `Khối Thịnh vượng chung` (`p000084`, `p000107`, `p000117`)
  - `pháp sư hải quân đánh bộ` (`p000099`)
  - `Thượng đế` (`p000107`)
  - `hải đội`, `tàu sân bay`, `tàu tuần dương`, `tàu tuần dương hạng nhẹ`, `tàu khu trục` (`p000090`, `p000096`, `p000097`, `p000101`, `p000107`, `p000108`, `p000117`)
- Ghi nhận các thuật ngữ/tên gọi mới đề xuất (`status: pending`) để điều phối viên và phản biện xem xét:
  - Tên tàu và biệt danh: `*Hood*` / `*Hood Hùng mạnh*` (`p000079`, `p000082`–`p000084`, `p000088`, `p000104`), `*Ark Royale*` (`p000092`, `p000095`, `p000097`, `p000105`), `*Bermuda*` (`p000107`, `p000111`), `*Yliastral*` (`p000108`, `p000110`).
  - Thuật ngữ hải quân và tác chiến chống ngầm: `tàu hộ tống` (`p000103`), `trắc thủ sonar` (`p000112`), `bầy sói săn mồi` (`p000113`), `tác chiến chống ngầm` (`p000116`), `dàn cối chống ngầm Hedgehog` / `đạn con` (`p000118`).
