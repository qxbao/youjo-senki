# Báo cáo tự kiểm dịch thuật — `vol-05-ch-04-b17` (Sign-off)

## 1. Thông tin chung
- **Task ID:** `vol-05-ch-04-b17-translator-signoff` (Parent: `vol-05-ch-04-b17`)
- **Translator:** `argon-low`
- **Phạm vi:** `YS-LN05/Text/part0022.html/p000634` đến `YS-LN05/Text/part0022.html/p000681` (48 đoạn)
- **Tệp kết quả:** `translations/vol-05/ch-04-b17.jsonl`
- **Trạng thái các dòng:** Đã cập nhật toàn bộ 48/48 dòng từ `draft` sang `reviewed`.

## 2. Xử lý Findings từ `reviews/prose/vol-05/ch-04-b17-argon-review.yml`
- **`YS-LN05/Text/part0022.html/p000640` (minor):** Đã chỉnh cụm `lệnh giới nghiêm tắt đèn nghiêm ngặt` thành `quy định tắt đèn nghiêm ngặt` và lược bỏ từ `hối hả` trong `các viên chức ra vào bên trong` để bám sát nguyên văn, đồng thời bảo toàn cấu trúc nhượng bộ trong `locked_choices`.
- **`YS-LN05/Text/part0022.html/p000680` (minor):** Đã đổi `gã chỉ huy này` trong phần in nghiêng thành `gã này` và đổi đại từ `gã` ở câu tiếp theo thành `hắn` (`Phải chăng hắn đang cố đùn đẩy trách nhiệm?`) để tách bạch rõ người bị đổ lỗi trong báo cáo và viên sĩ quan chính trị viết báo cáo. Đồng thời tại `p000674`, đã lược bớt một từ `phải` lặp (`những kẻ chịu trách nhiệm phải hối hận`).

## 3. Kiểm tra quy chuẩn xưng hô, giọng điệu và POV
- **Cảnh 1 (`p000634`–`p000638`):** Tiếp nối góc nhìn của Trung úy Serebryakov (Visha) ngay sau khi Grantz bấm giờ kích nổ con tàu tại cảng căn cứ hải quân Liên bang ở batch trước (`ch-04-b16`).
  - Trong suy nghĩ nội tâm và lời kể ngôi thứ nhất (`p000635`, `p000636`), Visha tự xưng `mình`, gọi nhóm mình là `chúng mình` / `cả bọn`, gọi Grantz là `anh ta` (khớp với `p000633` của batch 16).
  - Trong câu dẫn ngôi thứ ba (`p000637`), chiếu theo các batch trước (`ch-04-b14`, `ch-04-b15`), Visha được gọi là `cô`.
- **Cảnh 2 (`p000639`–`p000681`):** Chuyển cảnh sang buổi tối ngày 8 tháng 10 năm Thống nhất 1926 tại tòa nhà Bộ Dân ủy Nội vụ ở Moskva, xoay quanh Loria.
  - Dẫn truyện ngôi thứ ba gọi Loria là `ông ta`, gọi viên chức thanh tra bị bắt là `anh ta` / `gã viên chức` / `gã đàn ông`, gọi viên sĩ quan chính trị viết báo cáo là `viên sĩ quan chính trị` / `hắn` / `gã đàn ông đó`.
  - Đối thoại giữa Loria và thuộc cấp:
    - Thuộc cấp gọi Loria là `Đồng chí Loria` hoặc `Đồng chí`, tự xưng `tôi` / `chúng tôi`, lính gác đáp lệnh là `Rõ!`.
    - Loria tự xưng `tôi` (hoặc `chúng ta` / `chúng tôi` khi đại diện cho ban lãnh đạo/kiểm toán nội bộ của Bộ Dân ủy Nội vụ), gọi thuộc cấp là `các người` / `anh`, gọi đội lính gác là `các đồng chí lính gác`.
    - Trong độc thoại nội tâm (`p000674`), Loria tự xưng `ta`, gọi đám cấp dưới làm hỏng việc là `chúng`.

## 4. Kiểm tra bảo toàn nghĩa, phủ định, giả định và nhấn mạnh (`*...*`)
- **Bảo toàn nhấn mạnh (`DEC-P01-002`):**
  - `p000636`: Giữ đúng 2 cụm in nghiêng độc thoại nội tâm của Visha, tách biệt phần dẫn ở giữa.
  - `p000637`: Giữ in nghiêng cụm mở đầu.
  - `p000638`: Giữ in nghiêng toàn bộ đoạn độc thoại nội tâm.
  - `p000674`: Giữ in nghiêng phần lời thề độc trong đầu Loria trước dấu phẩy.
  - `p000676`: Giữ in nghiêng từ khóa chỉ sự khoan nhượng.
  - `p000680`: Giữ in nghiêng phần trích nội dung báo cáo của viên sĩ quan chính trị ở đầu đoạn.
  - Tất cả 42 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và hoàn toàn không dùng dấu `*...*` trong bản dịch.
- **Bảo toàn phủ định, câu hỏi và câu điều kiện trái thực tế:**
  - `p000640`: Bảo toàn cấu trúc nhượng bộ (ánh sáng không hẳn tràn ra ngoài do quy định tắt đèn, nhưng người đi ngang qua vẫn thấy viên chức ra vào bên trong).
  - `p000646`, `p000648`, `p000649`: Bảo toàn chính xác chuỗi phủ định về kết quả thanh tra không tìm ra sai phạm và câu hỏi xác nhận lại của Loria.
  - `p000658`: Bảo toàn câu điều kiện trái thực tế trong quá khứ (giá như báo cáo thì mọi việc đã khác, nhưng thực tế đã nhận hối lộ mà giấu nhẹm).
  - `p000670`–`p000672`: Bảo toàn tương phản giữa việc đã tính trước thương vong, đã cấp đủ lực lượng và quyền tự quyết, nhưng vẫn thất bại trong việc bảo vệ con tàu duy nhất được giao bảo vệ bằng danh dự.
  - `p000675`: Bảo toàn mệnh đề giả định trái thực tế (may mà mang theo tài liệu, giá như phạm sai lầm không mang theo thì không biết số phận sẽ ra sao).

## 5. Thuật ngữ và `locked_choices`
- Tuân thủ đầy đủ toàn bộ `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-05/ch-04-b17-argon-review.yml`:
  - `Năm Thống nhất` (`p000639`)
  - `tàu U-152` (`p000636`)
  - `Moskva` (`p000639`, `p000640`)
  - `Bộ Dân ủy Nội vụ` (`p000639`, `p000640`, `p000641`, `p000647`)
  - `Liên bang` (`p000641`, `p000668`)
  - `Chủ nghĩa Cộng sản` (`p000642`)
  - `Đồng chí Loria` / `Đồng chí` / `Loria` (`p000646`–`p000677`)
  - `Đợt thanh tra` / `cuộc thanh tra` / `đối tượng thanh tra` / `thanh tra viên` (`p000646`, `p000656`)
  - `cuộc kiểm toán nội bộ` (`p000656`)
  - `chiếc Nữ hoàng Biển cả` (`p000664`)
  - `đám John Bull` (`p000668`)
  - `Chúa` (`p000675`)
  - `Pháp sư Định danh` (`p000677`)
  - `sĩ quan chính trị` (`p000679`)

## 6. Kết luận tự kiểm
- Đủ 48/48 đoạn, mã đoạn và `source_sha256` khớp tuyệt đối với nguồn, `status: reviewed` trên toàn bộ các dòng.
- Không có câu nguồn tiếng Anh nào trong bản dịch hoặc trong báo cáo tự kiểm này.
