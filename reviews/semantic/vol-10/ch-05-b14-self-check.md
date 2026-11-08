# Báo cáo tự kiểm dịch thuật — `vol-10-ch-05-b14`

- **Vai trò:** Translator (`argon-low`)
- **Phạm vi:** `YS-LN10/Text/chapter024.xhtml/p000490` đến `YS-LN10/Text/chapter024.xhtml/p000532` (43 đoạn)
- **Tệp dịch:** `translations/vol-10/ch-05-b14.jsonl`

## 1. Kiểm tra nghĩa, phủ định, đối tượng câu hỏi và logic
- Đã đối chiếu toàn bộ 43 đoạn với gói nguồn cục bộ.
- Tại `p000494`, bản tiếng Anh ghi thiếu từ phủ định trong mệnh đề trần thuật về việc các pháp sư át chủ bài đứng nhìn tình hình xấu đi, nhưng ngay đoạn tiếp theo (`p000495`) và toàn bộ mạch tâm lý trước/sau đều khẳng định họ buộc phải can thiệp và không thể đứng nhìn; đã dịch đúng theo logic ngữ cảnh và ghi chú finding để reviewer/coordinator xác nhận.
- Tại `p000508`–`p000510`, giữ nguyên cấu trúc câu hỏi nội tâm và mối băn khoăn của Drake về việc người trả lời vô tuyến là sĩ quan phụ tá thay vì Lữ đoàn trưởng Ballmer, cũng như câu hỏi về việc có nên tiếp tục giữ vai trò lính dự bị hay không.
- Tại `p000526`, giữ rõ câu hỏi và suy luận của Drake về mục tiêu tiếp theo của đối phương (những chiến hạm đã truy đuổi quân Đế quốc bên dưới).
- Tại `p000531`, giữ nguyên phép ẩn dụ nhân hai số âm để ra số dương nhằm chỉ việc dùng khí thế cưỡng ép xoay chuyển cục diện bi đát.

## 2. Kiểm tra đại từ và xưng hô (`DEC-P01-001`)
- Điểm nhìn trần thuật ngôi thứ ba theo sát Trung tá Drake: dùng `anh` cho Drake trong trần thuật và `mình` trong câu hỏi nội tâm trực tiếp (`p000514`).
- Giữa Drake và người đồng đội/thuộc cấp cùng đơn vị pháp sư hải quân đánh bộ (`p000490`–`p000498`): thuộc cấp gọi Drake là `thưa Trung tá`, xưng hô đối đáp là `tôi – cậu`, dùng `chúng ta`/`ta` cho phe Khối Thịnh vượng chung.
- Khi gọi vô tuyến (`p000505`–`p000506`, `p000530`) và quát tháo chấn chỉnh các binh sĩ trẻ trên chiến trường (`p000532`): giữ giọng mệnh lệnh dứt khoát của chỉ huy chiến trường (`tôi – các cậu`).
- Đối với Tanya / Ác quỷ sông Rhine dưới góc nhìn thù địch của Drake (`p000528`): dùng `đứa con gái ngoài kia` và `ả` để phản ánh đúng thái độ dè chừng, căm giận của đối phương.

## 3. Kiểm tra nhấn mạnh (`DEC-P01-002`)
- Chỉ sử dụng dấu `*...*` tại đúng 3 đoạn có thẻ `<html:em>` trong nguồn:
  - `p000514`: `*Mình có nên nhảy vào nói trên sóng vô tuyến không?*`
  - `p000520`: `*Chuyện này không thể nào là thật được*`
  - `p000522`: `*À, phải rồi…*`
- Các đoạn còn lại không có nhấn mạnh trong nguồn và không tự ý thêm `*...*`.

## 4. Thuật ngữ và mục đang chờ xét (Pending Terms)
- Đã áp dụng nhất quán các phương án tạm trong sổ pending của tập 10 và các tập trước:
  - `ace` / `ace mages`: át chủ bài / những pháp sư át chủ bài
  - `marine mage battalion` / `marine mage units` / `marine mage`: tiểu đoàn pháp sư hải quân đánh bộ / các đơn vị pháp sư hải quân đánh bộ / pháp sư hải quân đánh bộ
  - `Colonel` / `Lieutenant Colonel Drake`: thưa Trung tá / Trung tá Drake (theo cấp bậc Lieutenant Colonel của Drake)
  - `Commonwealth`: Khối Thịnh vượng chung
  - `Commander Ballmer` / `brigade commander`: Chỉ huy Ballmer / lữ đoàn trưởng
  - `decapitation tactics`: chiến thuật chặt đầu chỉ huy
  - `Devil of the Rhine`: Ác quỷ sông Rhine
  - `area of operations`: khu vực tác chiến
- Ghi nhận các mục pending mới phát sinh trong lô:
  - `pseudo-unit` → `đơn vị bán chính quy` (`p000491`)
  - `Daniel 01` / `Daniel 06` / `Pirate Commander` → `Daniel 01` / `Daniel 06` / `Chỉ huy Pirate` (`p000505`, `p000506`, `p000517`, `p000530`)
  - `surgical attacks` → `những đòn đánh điểm huyệt` (`p000524`)

## 5. Xử lý Argon Review và Sign-off (`vol-10-ch-05-b14-translator-signoff`)
- **`p000491` (minor / terminology_nuance):** Giữ nguyên phương án đề xuất chính `đơn vị bán chính quy` và vế `bọn họ gần giống các pháp sư thực thụ rồi` theo đúng `pending_term_recommendations` và `locked_choices` của Argon Review.
- **`p000512` (minor / diction):** Tiếp nhận góp ý và chỉnh `cố gằn cao giọng` thành `cố nâng cao giọng` trên sóng vô tuyến để chuẩn xác kết hợp từ tiếng Việt mà vẫn tuân thủ toàn bộ `locked_choices`.
- Đã kiểm tra toàn bộ 43 đoạn bảo đảm tuân thủ đầy đủ `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-10/ch-05-b14-argon-review.yml`.
- Đã cập nhật trường `status` của toàn bộ 43 dòng trong `translations/vol-10/ch-05-b14.jsonl` từ `draft` sang `reviewed`.
