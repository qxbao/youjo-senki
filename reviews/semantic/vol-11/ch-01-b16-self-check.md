# Báo cáo tự kiểm dịch thuật — `vol-11-ch-01-b16` (Sign-off)

## 1. Phạm vi và kết quả chung
- **Task ID:** `vol-11-ch-01-b16-translator-signoff` (parent: `vol-11-ch-01-b16`)
- **Phạm vi đoạn:** `YS-LN11/Text/chapter004.xhtml/p000093` đến `YS-LN11/Text/chapter004.xhtml/p000121` (29 đoạn)
- **Trạng thái các dòng dịch:** `reviewed` (đã cập nhật toàn bộ 29 dòng từ `draft` sang `reviewed`)
- **Tự kiểm tổng quát:** Đã tiếp nhận và xử lý đầy đủ toàn bộ 3 findings (mức `minor`) và các `pending_term_recommendations` có căn cứ trong `reviews/prose/vol-11/ch-01-b16-argon-review.yml`, bảo đảm tuân thủ tất cả `locked_choices`. Tuyệt đối không trích dẫn câu nguồn tiếng Anh.

## 2. Xử lý các Findings từ Argon Review
- **`YS-LN11/Text/chapter004.xhtml/p000098` (minor / word_choice):** Đổi `cuộc tiểu phẫu nhỏ của chúng ta` thành `ca phẫu thuật nhỏ của chúng ta` để tránh lặp nghĩa Hán-Việt và đồng bộ mạch ẩn dụ y khoa với `các ca phẫu thuật` ở `p000108`.
- **`YS-LN11/Text/chapter004.xhtml/p000101` (minor / meaning_and_pronouns):** Đổi `sự thiếu sáng suốt chẳng giống mình ấy` thành `sự thiếu sáng suốt chẳng xứng với tầm vóc của ông ấy chút nào` để bám sát nghĩa gốc và tách bạch chủ thể quy chiếu Zettour (`ông ấy`) với đại từ nội tâm tự quy chiếu của Tanya (`mình` trong `vị cấp trên của mình`) theo `DEC-P01-001`.
- **`YS-LN11/Text/chapter004.xhtml/p000109` (minor / pronouns):** Đổi `như thể mình là một giáo sư tại học viện quân sự vậy` thành `như thể ông ấy là một giáo sư tại học viện quân sự vậy` để tách bạch chủ thể Zettour với đại từ nội tâm `Mình` của Tanya ở câu kế tiếp theo `DEC-P01-001`.

## 3. Kiểm tra đại từ và giọng nhân vật (`DEC-P01-001`)
- **Nội tâm / trần thuật ngôi thứ nhất của Tanya:** Dùng `mình` khi tự quy chiếu (`p000101`, `p000109`, `p000110`, `p000118`, `p000121`) và `chúng ta` khi bao hàm tập thể Đế quốc / phe Zettour–Tanya (`p000093`, `p000110`, `p000113`, `p000114`, `p000117`).
- **Đối thoại giữa Tanya và Tướng Zettour:**
  - Tanya xưng `tôi`, gọi Zettour là `ngài` (kèm `ạ` ở các câu trình bày/đáp lời lịch sự với cấp trên trực tiếp: `p000094`, `p000099`, `p000107`).
  - Zettour xưng `tôi`, gọi Tanya là `cô` và `Trung tá` (`p000095`, `p000098`, `p000100`, `p000108`, `p000111`, `p000115`).
  - Trong trần thuật của Tanya, Zettour được gọi là `Tướng Zettour` / `ông ấy`; Rudersdorf khi là mục tiêu bị nhắm tới trong bàn bạc và suy tính được gọi là `Tướng Rudersdorf` / `ông ta` (`p000112`, `p000113`, `p000114`, `p000116`, `p000119`).

## 4. Kiểm tra nhấn mạnh (`DEC-P01-002`)
- Trong phạm vi `p000093`–`p000121`, văn bản gốc không có thẻ nhấn mạnh (`<em>` / `<i>`). Các thẻ `<html:a id="page-038" />` (`p000101`) và `<html:a id="page-039" />` (`p000116`) chỉ là mốc trang trong EPUB. Do đó, bản dịch không sử dụng dấu `*...*` ở bất kỳ đoạn nào.

## 5. Thuật ngữ và mục đang chờ xét (Pending Terms)
Đã áp dụng nhất quán các phương án trong `pending_term_recommendations` và `locked_choices`:
- `miền đông` (`p000093`, `p000098`, `p000117`, `p000119`) / `mặt trận phía đông` (`p000114`, `p000116`)
- `Đế quốc` (`p000093`, `p000106`)
- `công binh, pháp sư, pháo binh và bộ binh` (`p000093`, `p000098`)
- `nhân viên trị an mặc sắc phục` (`p000093`) / `đơn vị quân cảnh` (`p000094`) / `lực lượng quân cảnh` (`p000102`)
- `cuộc đảo chính` (`p000094`, `p000113`), `Cuộc thanh trừng` (`p000113`)
- `Bộ Tổng tham mưu` (`p000095`), `Văn phòng Bộ Tổng tham mưu` (`p000112`), `Phó Tổng tham mưu trưởng Văn phòng Bộ Tổng tham mưu` (`p000114`)
- `Tướng Zettour` (`p000096`, `p000098`, `p000105`), `Tướng Rudersdorf` (`p000112`, `p000119`), `Đại tá Lergen` (`p000119`), `Trung tá` (`p000111`)
- `quân đội` (`p000104`), `lục quân` (`p000116`)
- `giáo sư tại học viện quân sự` (`p000109`)
- `kinh tế học đô thị`, `quyền bính` (`p000117`)
