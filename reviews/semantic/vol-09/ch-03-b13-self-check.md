# Báo cáo tự kiểm dịch thuật — `vol-09-ch-03-b13` (Sign-off)

- **Task ID:** `vol-09-ch-03-b13-translator-signoff`
- **Parent Task ID:** `vol-09-ch-03-b13`
- **Phạm vi đoạn:** `YS-LN09/Text/chapter010.xhtml/p000487` đến `YS-LN09/Text/chapter010.xhtml/p000534` (48 đoạn)
- **Người dịch:** `argon-low`
- **Trạng thái dòng:** `reviewed` (48/48 dòng)

## 1. Xử lý Findings từ `ch-03-b13-argon-review.yml`

- **`YS-LN09/Text/chapter010.xhtml/p000487` (minor / pronouns):** Giữ nguyên đại từ trần thuật ngôi thứ ba `nó` xuyên suốt lô `ch-03-b13` theo đúng `DEC-P01-001` và `locked_choices` của `p000487` (nhất quán với lô `ch-03-b12` liền trước).
- **`YS-LN09/Text/chapter010.xhtml/p000507` (minor / address_register):** Tiếp nhận đề xuất của Argon Reviewer, lược bỏ tiểu từ `ạ` để đổi thành `“…Sao cơ?”`, phản ánh đúng phản xạ buột miệng khi bàng hoàng và giữ vị thế cấp bậc cân xứng của Tanya trong cuộc họp.

## 2. Kiểm tra nghĩa, logic, phủ định và giả định (`locked_choices`)

- Đảm bảo tuân thủ đầy đủ toàn bộ `locked_choices` từ `p000487` đến `p000534`.
- Truyền tải đầy đủ lập luận của Tanya trong cuộc họp nghiên cứu kỹ thuật: đề xuất sử dụng đòn tấn công ngư lôi (mặc định trong đầu là không quân ném ngư lôi phối hợp tàu ngầm hỗ trợ) để đối phó với hạm đội địch vượt trội, và cú sốc khi phát hiện không quân Đế quốc chưa hề có máy bay ném ngư lôi mà chỉ dùng máy bay ném bom bổ nhào đánh tàu nhỏ.
- Giữ chính xác các chi tiết lịch sử trong ký ức của Tanya: một tàu ngầm đơn độc đánh chìm ba tàu tuần dương hạng nặng trong Thế chiến thứ nhất (`p000488`), các đợt không kích ngư lôi ở chiến trường Thái Bình Dương và mẫu máy bay Fairey Swordfish đánh trúng thiết giáp hạm *Bismarck* (`p000504`).
- Bảo toàn mạch nối câu giữa `p000531` và `p000532` (quan hệ nhượng bộ và nét tự trào về việc đề cao tính hợp lý kinh tế nhưng lại khó bỏ được nỗi căm ghét trớ trêu đối với sự phi lý).

## 3. Kiểm tra đại từ và xưng hô (`DEC-P01-001`)

- **Trần thuật ngôi thứ ba:** Dùng `nó` cho Tanya xuyên suốt các đoạn trần thuật theo đúng điểm nhìn và quy ước `DEC-P01-001`.
- **Nội tâm trực tiếp:** Các câu độc thoại nội tâm của Tanya (`p000490`, `p000494`, `p000509`–`p000511`) không xuất hiện đại từ tự quy chiếu ngôi thứ nhất nhưng giữ đúng giọng điệu độc thoại của nhân vật.
- **Đối thoại trong cuộc họp:** Tanya tự xưng `tôi`, các thành viên trong cuộc họp gọi Tanya là `Trung tá` (`p000493`, `p000499`) và gọi bằng đại từ `cô` (`p000513`, `p000527`), câu hỏi buột miệng tại `p000507` đã chỉnh thành `“…Sao cơ?”` đảm bảo tự nhiên và cân xứng vị thế.

## 4. Kiểm tra nhấn mạnh / chữ nghiêng (`DEC-P01-002`)

- Chỉ đánh dấu `*...*` đúng tại những vị trí văn bản gốc có thẻ nhấn mạnh:
  - `YS-LN09/Text/chapter010.xhtml/p000490`: câu cảm thán mở đầu trong suy nghĩ của Tanya.
  - `YS-LN09/Text/chapter010.xhtml/p000494`: toàn bộ câu hỏi nội tâm.
  - `YS-LN09/Text/chapter010.xhtml/p000504`: tên riêng tàu chiến `*Bismarck*`.
  - `YS-LN09/Text/chapter010.xhtml/p000509`: toàn bộ câu hỏi nội tâm.
  - `YS-LN09/Text/chapter010.xhtml/p000510`: toàn bộ câu hỏi nội tâm.
  - `YS-LN09/Text/chapter010.xhtml/p000511`: toàn bộ câu hỏi nội tâm.
  - `YS-LN09/Text/chapter010.xhtml/p000520`: cụm từ chỉ nơi chốn `*đâu đó*` ở cuối câu.
- Không thêm nhấn mạnh Markdown tại vị trí thẻ neo trang ở `p000503` và `p000522`.

## 5. Thuật ngữ và mục chờ xét (`pending_term_recommendations`)

- Toàn bộ 11 mục trong `pending_term_recommendations` của Argon Reviewer đã được áp dụng đồng bộ và chính xác trên các đoạn tương ứng:
  - `đội tập kích` / `đơn vị tập kích đặt căn cứ trên bộ` (`p000487`, `p000496`)
  - `tàu tuần dương hạng nặng` / `tàu chủ lực` / `tàu khu trục` / `tàu chở quân` / `tàu phóng lôi` (`p000488`, `p000496`, `p000522`, `p000533`)
  - `quân đội Đế quốc` / `Hải quân Đế quốc` / `Đế quốc` / `Đại Quân` (`p000491`, `p000496`, `p000523`, `p000529`)
  - `Trung tá` (`thưa Trung tá`) / `Trung tá Pháp sư Tanya von Degurechaff` / `Tanya` (`p000493`, `p000496`, `p000499`, `p000503`, `p000506`, `p000519`, `p000523`, `p000528`)
  - `không đoàn tàu sân bay` (`p000496`)
  - `máy bay ném ngư lôi` / `máy bay ném bom bổ nhào` / `máy bay cường kích` / `các đơn vị cường kích` (`p000503`, `p000505`, `p000517`, `p000518`, `p000520`, `p000521`, `p000522`, `p000526`)
  - `chiến trường Thái Bình Dương` / `*Bismarck*` / `Fairey Swordfish` (`p000504`)
  - `chương trình đào tạo cấp tốc` / `tác chiến liên hợp` / `hỏa lực yểm trợ cơ hữu` (`p000519`)
  - `quốc gia lục địa` / `quyền làm chủ bầu trời` / `các nhiệm vụ yểm trợ đường không tầm gần` (`p000523`, `p000525`)
  - `tài sản vô hình` / `bí quyết công nghệ` (`p000530`)
  - `tính hợp lý kinh tế` / `sự phi lý` (`p000532`)
