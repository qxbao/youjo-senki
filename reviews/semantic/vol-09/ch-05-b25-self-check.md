# Báo cáo tự kiểm (Self-Check): `vol-09-ch-05-b25`

- **Task ID**: `vol-09-ch-05-b25-translator-signoff` (parent: `vol-09-ch-05-b25`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN09/Text/chapter020.xhtml/p000901` – `YS-LN09/Text/chapter020.xhtml/p000942` (42 đoạn)
- **File bản dịch**: `translations/vol-09/ch-05-b25.jsonl`

## 1. Kiểm tra tính đầy đủ và cấu trúc kỹ thuật
- Đã dịch và rà soát đầy đủ 42/42 đoạn từ `p000901` đến `p000942`, giữ nguyên thứ tự và mã định danh (`segment_id`).
- Trường `"status"` của toàn bộ 42 dòng đã được cập nhật từ `"draft"` sang `"reviewed"` sau khi xử lý báo cáo review của Argon (`reviews/prose/vol-09/ch-05-b25-argon-review.yml`).
- Kiểm tra thẻ nhấn mạnh (`<em>` / `<i>`) theo `DEC-P01-002`:
  - `p000907`: Đánh dấu nghiêng từ phủ định `*không*` trong câu hỏi tu từ cuối đoạn (`Bầu không khí ở đó làm sao mà *không* u ám cho được?`) khớp với thẻ `<html:em>` trong nguồn.
  - Toàn bộ 41 đoạn còn lại không có thẻ nhấn mạnh trong nguồn nên tuyệt đối không tự thêm dấu `*...*`.

## 2. Xử lý Findings & Locked Choices từ Argon Review
- **`p000909` (minor / terminology, `polish_optional`)**: Giữ nguyên cách dịch `"mô thức nhận thức"` (đồng bộ với `p000911` có `Touch: "preserve"` và khớp với `recommended_rendering` trong `pending_term_recommendations`) để câu thoại tự nhiên, rõ nghĩa trong mạch suy tư triết học của Tanya.
- **`p000938` (minor / lexical_choice, `polish_optional`)**: Tiếp thu khuyến nghị của reviewer, chỉnh `"việc đào thoát"` thành `"việc sơ tán"` để giữ đúng sắc thái bề mặt trung tính của từ gốc.
- Tuân thủ toàn bộ các `locked_choices` (`preserve`) trên 40 đoạn còn lại và toàn bộ `pending_term_recommendations` trong `reviews/prose/vol-09/ch-05-b25-argon-review.yml`.

## 3. Xưng hô, giọng điệu và mạch ngữ cảnh
- **Ngữ cảnh**: Tiếp nối trực tiếp `vol-09-ch-05-b24` (đoạn kết chương 5 tập 9). Sau khi Trung úy Serebryakov vui vẻ mang rượu vang sang cho Thiếu tá Weiss và mọi người trên chuyến tàu rời Ildoa về Đế quốc, Trung tá Tanya von Degurechaff ngồi lại một mình suy ngẫm về khoảng cách nhận thức giữa tiền tuyến, hậu phương và quốc gia trung gian hòa bình như Ildoa, đọc báo nước ngoài, dùng bữa tối cùng đơn vị trong toa ăn, rồi đi ngủ ở toa giường nằm và thức giấc khi tàu vượt qua biên giới vào hệ thống đường sắt kém bảo trì của Đế quốc.
- **Độc thoại nội tâm, lời lẩm bẩm một mình & trần thuật (góc nhìn Tanya)**:
  - Trong độc thoại nội tâm và lời tự nhủ một mình (`p000902`, `p000903`, `p000905`, `p000911`, `p000912`, `p000913`, `p000917`, `p000919`, `p000920`, `p000921`, `p000922`, `p000924`, `p000927`, `p000928`, `p000936`, `p000937`, `p000938`, `p000942`), Tanya tự quy chiếu nhất quán bằng `mình` (hoặc `chúng ta` / `ta` ở `p000911`, `p000912`, `p000919`, `p000936` khi chỉ chung con người hoặc phía Đế quốc; `cả hai` ở `p000901` khi nhắc tới bản thân và Serebryakov).
  - Trong lời dẫn ngôi thứ ba hoặc khi cái tôi nội tâm tách biệt nhìn nhận bản thể Tanya (`p000916`, `p000924`, `p000926`, `p000935`), dùng thống nhất `Tanya` / `cô`.
  - Tham chiếu Trung úy Serebryakov ở `p000902` bằng `cô ấy` (tiếp nối trực tiếp `p000899`–`p000900` của `ch-05-b24`).

## 4. Thuật ngữ và lựa chọn dịch thuật
- Áp dụng nhất quán các thuật ngữ đã có trong `canon/glossary-pending.yml`, `work/run-state/pending-terms-index.yml` và `pending_term_recommendations`:
  - `Ildoa` (`p000905`, `p000913`, `p000921`, `p000923`, `p000930`)
  - `hậu phương` / `tiền tuyến` (`p000905`, `p000907`, `p000911`)
  - `Đế quốc` / `đế đô` / `thủ đô` (`p000906`, `p000907`, `p000913`, `p000921`, `p000928`, `p000931`, `p000935`, `p000940`)
  - `chiến tranh tổng lực` (`p000907`)
  - `Bộ Tổng tham mưu Lục quân Đế quốc` / `Bộ Tư lệnh Tối cao` (`p000913`)
  - `chống Cộng` / `lũ Cộng sản` (`p000916`, `p000917`, `p000919`)
  - `tỷ lệ hiệu quả chi phí` (`p000918`, kế thừa `cost performance` -> `hiệu quả chi phí` trong `canon/glossary-pending.yml`)
  - `Liên bang` / `Khối Thịnh vượng chung` (`p000921`)
  - `toa ăn` (`p000924`)
  - `Weiss` / `phó chỉ huy` (`p000924`)
  - `xã hội học` / `quá trình xã hội hóa` (`p000903`)
  - `mô thức nhận thức` (`p000909`, `p000911`)
  - `giải cấu trúc` (`p000912`)
  - `các quốc gia phụ thuộc của Đế quốc` (`p000913`)
  - `vũ khí hạt nhân chiến lược` / `loạt phóng áp đảo một chiều` (`p000919`)
  - `toa giường nằm` (`p000925`)
  - `các liệt cường` (`p000933`)
