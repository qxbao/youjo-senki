# Báo cáo tự kiểm dịch thuật (Self-Check) — `vol-05-ch-03-b04`

- **Task ID:** `vol-05-ch-03-b04`
- **Phạm vi đoạn:** `YS-LN05/Text/part0018.html/p000094` → `YS-LN05/Text/part0018.html/p000139` (46 đoạn)
- **Người dịch:** `argon-low`

## 1. Kiểm tra nghĩa, phủ định, đối tượng câu hỏi và giả định
- **Mệnh lệnh giải thể và lập luận tổ chức (`p000094`–`p000122`):** Giữ nguyên trình tự đối đáp giữa Tướng von Rudersdorf và Trung tá Tanya von Degurechaff về quyết định giải thể Kampfgruppe Salamander để trả các đơn vị về nơi đóng quân ban đầu. Bảo toàn rõ mục đích thử nghiệm mô hình lực lượng đặc nhiệm lâm thời, nhu cầu xây dựng tri thức học thuyết ở cấp độ tổ chức và ví dụ ẩn dụ về những bánh răng có thể nhân bản, thay thế trong quân đội chịu tiêu hao.
- **Tranh luận về tình hình mặt trận phía Đông và tiêu hao nhân lực (`p000123`–`p000139`):** Giữ chính xác lập luận của Tanya khi muốn giữ Kampfgruppe làm lực lượng dự bị chiến lược trong khoảng lặng tạm thời, cũng như góc nhìn dài hạn của Tướng von Rudersdorf về tốc độ tiêu hao nghiêm trọng ở mặt trận phía Đông. Chuỗi thời gian giả định và mức độ chắc chắn (`p000133`–`p000138`: ngày mai, tuần sau, tháng sau, năm sau và ẩn dụ đồng hồ cát không thể lật ngược) được giữ nguyên sắc thái và logic nhân quả.

## 2. Kiểm tra đại từ và xưng hô (`DEC-P01-001`)
- **Trần thuật và nội tâm của Tanya:** Phân biệt nhất quán đại từ trần thuật chỉ Tanya là “nó” và đại từ tự quy chiếu trong độc thoại nội tâm là “mình” / “chúng ta” (khi xét góc nhìn tổ chức chung ở `p000121`). Ở câu hỏi nội tâm `p000098`, cấu trúc tự quy chiếu được chuyển tự nhiên sang “chính mình”.
- **Thoại giữa Tướng von Rudersdorf và Tanya:**
  - Tướng von Rudersdorf gọi Tanya là “Trung tá” / “Trung tá von Degurechaff”, xưng “tôi” (hoặc “chúng tôi” / “chúng ta” khi đại diện cho Bộ Tổng tham mưu / Lục quân Đế quốc), gọi Tanya là “cô”.
  - Tanya gọi Tướng von Rudersdorf là “Tướng quân” / “ngài”, xưng “tôi”.

## 3. Kiểm tra nhấn mạnh / chữ nghiêng (`DEC-P01-002`)
- Đối chiếu toàn bộ 46 đoạn với thẻ `<html:em>` trong nguồn:
  - `p000098`: Câu thứ hai có `<html:em>` → đánh dấu `*...*` đúng phạm vi câu hỏi nội tâm.
  - `p000101`: Toàn đoạn có `<html:em>` → đánh dấu `*...*`.
  - `p000107`: Toàn đoạn có `<html:em>` → đánh dấu `*...*`.
  - Các đoạn còn lại không có `<html:em>` trong nguồn → hoàn toàn không dùng `*...*`.

## 4. Thuật ngữ và mục đang chờ xét (Pending Terms)
- Áp dụng nhất quán các phương án tạm đã có trong sổ pending:
  - `Kampfgruppe` / `Kampfgruppen` / `Salamander Kampfgruppe` → `Kampfgruppe` / `các Kampfgruppe` / `Kampfgruppe Salamander`
  - `Colonel` / `Colonel von Degurechaff` → `Trung tá` / `Trung tá von Degurechaff`
  - `General` / `General von Rudersdorf` → `Tướng quân` / `Tướng von Rudersdorf`
  - `chain of command` → `hệ thống chỉ huy`
  - `General Staff` → `Bộ Tổng tham mưu`
  - `Imperial Army` → `Lục quân Đế quốc`
  - `eastern front` → `mặt trận phía Đông`
  - `rate of attrition` → `tốc độ tiêu hao`
  - `human resources` → `nguồn nhân lực`
  - `Kampfgruppen doctrine` → `học thuyết Kampfgruppe`
- Ghi nhận một số cụm thuật ngữ quân sự mô tả trong lô để theo dõi nhất quán:
  - `ad hoc task force` / `ad hoc formation` (`p000115`, `p000117`) → `lực lượng đặc nhiệm lâm thời` / `đội hình lâm thời`
  - `strategic reserve` (`p000127`, `p000128`) → `lực lượng dự bị chiến lược`

## 5. Xử lý Argon Review và Sign-off (`vol-05-ch-03-b04-translator-signoff`)
- **`YS-LN05/Text/part0018.html/p000095` (minor / diction):** Đổi “Tanya nín thở.” thành “Tanya nghẹn thở.” để phản ánh đúng phản xạ nghẹn thở bàng hoàng khi nghe lệnh giải thể đột ngột.
- **`YS-LN05/Text/part0018.html/p000133` (minor / grammar_and_meaning):** Đổi “sẽ lập tức xóa sổ” thành “sẽ lập tức bị xóa sổ” để đảm bảo cấu trúc bị động chuẩn xác trong tiếng Việt.
- **Pending terms & Locked choices:** Giữ nguyên toàn bộ `pending_term_recommendations` và `locked_choices` từ báo cáo `ch-03-b04-argon-review.yml`.
- **Trạng thái dòng dịch:** Đã chuyển `status` của toàn bộ 46 dòng trong `translations/vol-05/ch-03-b04.jsonl` từ `draft` sang `reviewed`.
