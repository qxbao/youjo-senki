# Báo cáo tự kiểm (Self-Check): vol-04-ch-06-b17

## 1. Phạm vi và kết quả chung
- **Task ID:** `vol-04-ch-06-b17` (Sign-off: `vol-04-ch-06-b17-translator-signoff`)
- **Phạm vi đoạn:** `YS-LN04/Text/chapter001_v.xhtml/p000556` đến `YS-LN04/Text/chapter001_v.xhtml/p000589` (34 đoạn).
- **Trạng thái dòng:** `reviewed` trên toàn bộ 34 dòng sau khi xử lý báo cáo `reviews/prose/vol-04/ch-06-b17-argon-review.yml`.
- **Tự kiểm:** Không chép câu nguồn tiếng Anh; đảm bảo giữ nguyên nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic nhân quả, thời gian của giả định, đại từ theo điểm nhìn và đánh dấu nhấn mạnh; tuân thủ đầy đủ `locked_choices`.

## 2. Xử lý Findings từ Argon Review
- **`p000575` (`minor` – `nuance_and_register`):** Đổi `"khiến chúng ta tối tăm mặt mũi rồi"` thành `"khiến chúng ta phải căng mình hết sức rồi"` để phù hợp với phong thái điềm tĩnh của một tướng lĩnh Bộ Tổng tham mưu.
- **`p000576` (`minor` – `word_choice`):** Đổi `"tự dưng đi cắn vào trái táo độc ấy cả"` thành `"tự mình đi cắn vào trái táo độc ấy cả"` để thể hiện chính xác nét nghĩa chủ động/tự nguyện, tránh hiểu lầm thành vô cớ/bỗng dưng.
- **`p000578` (`minor` – `logic_and_condition`):** Đổi `"Nếu đạt được mục tiêu ấy thì chẳng có gì là vùng cấm cả."` thành `"Để có thể đạt được mục tiêu ấy thì chẳng có gì là vùng cấm cả."` để làm rõ quan hệ điều kiện hướng đích trong mạch lập luận của Zettour.

## 3. Kiểm tra Điểm nhìn, Đại từ và Xưng hô (`DEC-P01-001`)
- **Đoạn `p000556` – `p000580` (tiếp nối cuộc đối thoại và suy nghĩ nội tâm của Trung tướng von Zettour với Trung tá von Lergen tại Văn phòng Phó Cục trưởng Cục Quân vụ):**
  - Trần thuật ngôi thứ ba theo điểm nhìn của Trung tướng von Zettour: gọi Zettour và Lergen là `ông`, gọi Tanya (Degurechaff) là `cô`.
  - Xưng hô trong thoại:
    - Zettour xưng `tôi` / `chúng ta`, gọi Lergen là `Trung tá von Lergen` (`p000558`) / `Trung tá` (`p000579`), gọi Tanya là `Degurechaff` (`p000579`).
    - Lergen xưng `chúng ta`, gọi Zettour là `ngài` kèm `ạ` (`p000569`, `p000574`, `p000580`).
- **Đoạn `p000581` – `p000589` (trần thuật lịch sử khách quan về cuộc tranh luận chiến lược trong Bộ Tổng tham mưu Lục quân Đế quốc):**
  - Trần thuật ngôi thứ ba khách quan: gọi Tướng von Zettour là `ông`, các phe phái và lực lượng quân sự là `họ` / `chúng` phù hợp với ngữ cảnh chiến sự.

## 4. Kiểm tra Nhấn mạnh (`DEC-P01-002`)
- Chỉ sử dụng `*...*` tại đúng 1 vị trí có thẻ `<html:em>` tương ứng trong nguồn:
  - `p000572`: `*Giá mà chỉ dừng lại ở đó…*` (chỉ in nghiêng mệnh đề cảm thán nội tâm đầu câu, giữ nguyên phần trần thuật `Zettour nhăn mặt.` bên ngoài dấu sao).
- Toàn bộ 33 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và không tự thêm `*...*`.

## 5. Thuật ngữ và Tính nhất quán
- Áp dụng nhất quán các thuật ngữ đã có trong sổ pending, `pending_term_recommendations` và `locked_choices`:
  - `Unified States` -> `Hợp chúng quốc` (`p000556`, `p000557`, `p000561`, `p000569`, `p000571`, `p000573`, `p000576`)
  - `Imperial Army` / `Imperial Army General Staff` -> `Lục quân Đế quốc` / `Bộ Tổng tham mưu Lục quân Đế quốc` (`p000557`, `p000581`, `p000588`)
  - `Colonel von Lergen` / `Colonel` -> `Trung tá von Lergen` / `Trung tá` (`p000558`, `p000579`)
  - `matériel` -> `vật tư và trang bị quân sự` (`p000558`)
  - `Commonwealth` -> `Khối Thịnh vượng chung` (`p000561`, `p000569`, `p000575`)
  - `port of discharge` -> `cảng bốc dỡ` (`p000562`, đề xuất tạm)
  - `imperial air fleet` -> `Không hạm đội của Đế quốc` (`p000564`, đề xuất tạm)
  - `Federation` / `Federation Army` -> `Liên bang` / `Quân đội Liên bang` (`p000575`, `p000585`, `p000588`, `p000589`, đề xuất tạm)
  - `Great War` -> `Đại chiến` (`p000581`)
  - `General von Zettour` -> `Tướng von Zettour` (`p000581`)
  - `Rhine front` / `the Rhine` -> `mặt trận Rhine` (`p000581`, `p000587`)
  - `western faction` / `eastern faction` -> `phái miền Tây` / `phái miền Đông` (`p000581`, `p000583`, `p000584`, `p000585`, `p000587`, `p000588`, đề xuất tạm)
  - `bloodletting strategy` -> `chiến lược rỉ máu` (`p000582`, đề xuất tạm)
  - `Attritional Containment Doctrine` -> `Học thuyết Kiềm chế Tiêu hao` (`p000584`, `p000588`, đề xuất tạm)
  - `Decisive Battle Doctrine` -> `Học thuyết Quyết chiến` (`p000588`, đề xuất tạm)
  - `attract and annihilate strategy` -> `chiến lược nhử địch và tiêu diệt hoàn toàn` (`p000586`, đề xuất tạm)
  - `interior lines` -> `tuyến trong` (`p000586`)
  - `Republican Army` -> `Quân đội Cộng hòa` (`p000587`)
  - `Trouncenberg` -> `Trouncenberg` (`p000589`)
