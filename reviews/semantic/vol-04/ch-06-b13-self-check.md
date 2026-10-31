# Báo cáo tự kiểm (Self-Check): vol-04-ch-06-b13

## 1. Phạm vi và kết quả chung
- **Task ID:** `vol-04-ch-06-b13` (Sign-off: `vol-04-ch-06-b13-translator-signoff`)
- **Phạm vi đoạn:** `YS-LN04/Text/chapter001_v.xhtml/p000389` đến `YS-LN04/Text/chapter001_v.xhtml/p000429` (41 đoạn).
- **Trạng thái dòng:** `reviewed` trên toàn bộ 41 dòng sau khi xử lý báo cáo review Argon.
- **Tự kiểm:** Không chép câu nguồn tiếng Anh; đảm bảo giữ nguyên nghĩa, đối tượng câu hỏi, cấu trúc giả định, đại từ, đánh dấu nhấn mạnh và tuân thủ toàn bộ `locked_choices`.

## 2. Xử lý Findings từ Argon Review
- **`YS-LN04/Text/chapter001_v.xhtml/p000394` (minor - `pronouns_and_register`):** Đã đổi `bọn chúng / lũ này / chúng` thành `đám tân binh này / họ / bọn họ / họ` để giữ giọng điềm đạm của vị sĩ quan cấp cao thuộc Bộ Tổng tham mưu, phù hợp với tâm lý nhân vật ở `p000400`–`p000403` và tạo tương phản rõ với lời quát tháo của Degurechaff ở `p000421`.
- **`YS-LN04/Text/chapter001_v.xhtml/p000427` (minor - `pronouns_and_addressing`):** Đã đổi `*cô*` thành `*ngài*` (`Có kẻ dám bất tuân lệnh của *ngài* sao, thưa Trung tá?`) để nhất quán sắc thái quân phong cấp dưới – cấp trên khi Đại úy Weiss hỏi trực diện Trung tá Degurechaff.

## 3. Kiểm tra Điểm nhìn, Đại từ và Xưng hô (`DEC-P01-001`)
- **Nửa đầu lô (`p000389` – `p000409`, cảnh đối thoại giữa vị sĩ quan cấp cao Bộ Tổng tham mưu và Trung tá Tanya von Degurechaff):**
  - Trần thuật từ điểm nhìn của vị sĩ quan cấp cao dùng đại từ `ông` cho ông và `cô` cho Tanya von Degurechaff; các tân binh pháp sư được gọi là `họ` trong trần thuật và `đám tân binh này` / `bọn họ` / `họ` trong lời thoại.
  - Xưng hô trong thoại: sĩ quan cấp cao xưng `tôi` – gọi Tanya là `cô`; Tanya xưng `tôi` – gọi cấp trên là `ngài` (kèm kính ngữ `ạ`).
- **Nửa sau lô (`p000410` – `p000429`, cảnh tại doanh trại đồn trú tạm thời của Tiểu đoàn Pháp sư Trên không số 203):**
  - Trần thuật chuyển sang điểm nhìn của các sĩ quan Tiểu đoàn 203 và Đại úy Weiss: dùng `cô` / `Trung tá von Degurechaff` / `vị trung tá` cho Tanya, `anh` cho Đại úy Weiss và Trung úy Grantz.
  - Xưng hô trong thoại giữa Đại úy Weiss và Tanya (`p000421` – `p000427`): Weiss gọi Tanya là `*ngài*` / `thưa Trung tá`; Tanya xưng `tôi` khi nổi giận quát tháo về đám lính mới.

## 4. Kiểm tra Nhấn mạnh (`DEC-P01-002`)
- Chỉ sử dụng `*...*` tại các đoạn có thẻ `<html:em>` tương ứng trong nguồn:
  - `p000408`: `*Chẳng lẽ…*`
  - `p000409`: `*Chẳng lẽ không một ai thấy chuyện này kỳ lạ sao?*`
  - `p000412`: `*Kẻ ngu xuẩn nào lại đi đùa với lửa ngay trên kho thuốc súng thế không biết?*` (chỉ in nghiêng câu cảm thán đầu đoạn đúng theo phạm vi thẻ `<html:em>`).
  - `p000420`: `*Ôi trời ơi.*` (chỉ in nghiêng từ cảm thán cuối đoạn).
  - `p000427`: `*ngài*` (nhấn mạnh đúng đại từ làm tân ngữ của hành động bất tuân lệnh).
  - `p000429`: `*Bất tuân thượng lệnh và… vô kỷ luật ư?*` (chỉ in nghiêng câu đầu đoạn).
- Các đoạn không có thẻ nhấn mạnh trong nguồn tuyệt đối không tự thêm `*...*`.

## 5. Thuật ngữ và Tính nhất quán (`pending_term_recommendations` & `locked_choices`)
- Đảm bảo khớp đầy đủ các phương án thuật ngữ trong `argon-review`:
  - `direct support` -> `yểm trợ trực tiếp` (`p000390`)
  - `maneuver battles` -> `các trận đánh cơ động` (`p000392`)
  - `limited defensive battles` -> `những trận đánh phòng ngự giới hạn` (`p000392`)
  - `acceptable attrition rate` -> `tỷ lệ tiêu hao có thể chấp nhận được` (`p000393`)
  - `instructors` -> `các sĩ quan huấn luyện`; `formulas` -> `các thuật thức` (`p000395`)
  - `firing squad` -> `đội xử bắn` (`p000397`)
  - `substitutability and cost consciousness` -> `khả năng thay thế và ý thức về chi phí` (`p000403`)
  - `Salamander Kampfgruppe` -> `Kampfgruppe Salamander` (`p000405`)
  - `inspection` -> `đợt thanh tra` (`p000410`)
  - `203rd Aerial Mage Battalion` -> `Tiểu đoàn Pháp sư Trên không số 203` (`p000411`, `p000417`)
  - `First Lieutenant Serebryakov` -> `Trung úy Serebryakov` (`p000411`)
  - `Lieutenant Colonel von Degurechaff` / `Colonel von Degurechaff` -> `Trung tá von Degurechaff` (`p000413`, `p000414`)
  - `First Lieutenant Grantz` -> `Trung úy Grantz` (`p000416`)
  - `long-range, low-altitude, decentralized raid exercise` -> `buổi diễn tập đột kích phân tán tầm xa ở độ cao thấp` (`p000416`)
  - `mana signals` -> `tín hiệu ma lực` (`p000417`)
  - `duty personnel` -> `nhân sự trực ban` (`p000419`)
  - `Captain Weiss` -> `Đại úy Weiss` (`p000419`)
  - `the Kampfgruppe commander’s adjutant` -> `sĩ quan phụ tá cho chỉ huy Kampfgruppe` (`p000425`)
  - `disobedience and insubordination` -> `bất tuân thượng lệnh và vô kỷ luật` (`p000426`, `p000429`)
