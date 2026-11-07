# Báo cáo tự kiểm (Self-Check) — vol-07-ch-02-b08

## 1. Phạm vi và thông tin chung
- **Task ID:** `vol-07-ch-02-b08`
- **Tập / Chương:** `vol-07`, chương 2
- **Dải đoạn:** `YS-LN07/Text/chapter008.xhtml/p000001` đến `YS-LN07/Text/chapter008.xhtml/p000038` (38 đoạn)
- **Tệp bản dịch:** `translations/vol-07/ch-02-b08.jsonl`
- **Trạng thái dòng:** `reviewed` (đã sign-off sau `reviews/prose/vol-07/ch-02-b08-argon-review.yml`; 0 findings, bảo đảm tuân thủ đầy đủ `locked_choices` và `pending_term_recommendations`)

## 2. Kiểm tra nghĩa, logic và thời gian giả định
- Đảm bảo giữ nguyên luồng đối thoại giữa Trung tá Tanya von Degurechaff và Đại tá von Lergen tiếp nối từ cuối lô trước (`ch-02-b07`) về việc tiếp nhận một quan sát viên quân sự người Ildoa vào Kampfgruppe Salamander.
- Giữ chuẩn xác quan hệ nhân quả và mạch suy luận nội tâm của Tanya: từ chỗ nghi ngờ thủ tục nhân sự hoàn tất quá nhanh mà không có thông báo trước (`p000014`–`p000021`), đến giả định về việc che giấu dấu vết hay cùng làm đồng phạm (`p000026`), và cuối cùng đoán ra mục đích đàm phán ngoại giao ngầm dưới sự chuẩn y của Tướng von Zettour (`p000028`–`p000037`).
- Giữ đúng tính chất giả định và mức độ chắc chắn ở các câu suy đoán nội tâm (`p000019`, `p000025`, `p000026`, `p000036`, `p000037`).

## 3. Kiểm tra đại từ và xưng hô (DEC-P01-001)
- **Trần thuật:** Quy chiếu Tanya là `nó`; quy chiếu Đại tá von Lergen là `ông` / `vị đại tá`; quy chiếu Tướng von Zettour trong suy nghĩ của Tanya ở `p000037` là `ông ấy`.
- **Nội tâm của Tanya:** Tự quy chiếu là `mình` / `chúng mình` (`p000026`), gọi Lergen là `ngài` (`p000005`) hoặc `ông ấy` (`p000026`).
- **Thoại:**
  - Tanya với Lergen (cấp dưới nói với cấp trên): xưng `tôi`, gọi `ngài` / `Đại tá`, có đệm lịch sự `ạ` phù hợp với ngữ cảnh đối thoại nghiêm túc nhưng thẳng thắn.
  - Lergen với Tanya (cấp trên nói với cấp dưới): xưng `tôi`, gọi `cô` / `Trung tá von Degurechaff`. Lưu ý tại `p000013`, cách gọi tắt cấp bậc trong lời Lergen được dịch đúng cấp bậc thực tế của Tanya là `Trung tá von Degurechaff` theo quy ước đã thống nhất ở các lô trước.

## 4. Kiểm tra nhấn mạnh / chữ nghiêng (DEC-P01-002)
Đã kiểm tra đối chiếu toàn bộ các thẻ nhấn mạnh từ nguồn và chỉ sử dụng `*...*` đúng phạm vi tương ứng:
- `p000003`: hai từ nhấn mạnh đối lập `*khó khăn*` và `*bất khả thi*`.
- `p000005`: câu nội tâm mở đầu đoạn `*Vậy nếu ngài đã hiểu rồi thì…*`.
- `p000007`: động từ nhấn mạnh trong lời thoại `*nhờ vả*`.
- `p000014`: trạng từ chỉ thời gian nhấn mạnh cuối câu hỏi `*lúc này*`.
- `p000026`: toàn bộ đoạn suy nghĩ nội tâm được bọc `*...*`.
- `p000027`: toàn bộ đoạn câu hỏi nội tâm được bọc `*...*`.
- `p000028`: thán từ xen giữa câu `*Ồồồ*`.
- `p000029`: câu hỏi thứ hai trong lời thoại được bọc `*...*`.
- `p000036`: cụm lời dẫn giả định của Zettour được bọc `*‘Hãy cho họ thấy tình hình đang diễn ra thế nào.’*`.
- `p000037`: thán từ mở đầu đoạn `*Ààà.*`.
- Các đoạn còn lại không có nhấn mạnh trong nguồn nên giữ văn bản phẳng.

## 5. Thuật ngữ và mục đang chờ duyệt (Pending Terms)
- Áp dụng nhất quán các phương án tạm đã có trong sổ pending:
  - `Kampfgruppe` / `Salamander Kampfgruppe` -> `Kampfgruppe` / `Kampfgruppe Salamander` (`p000001`, `p000013`, `p000025`).
  - `observer` / `military observer` -> `quan sát viên` / `quan sát viên quân sự` (`p000001`, `p000025`, `p000026`, `p000033`).
  - `General Staff` / `General Staff officer` -> `Bộ Tổng tham mưu` / `sĩ quan Bộ Tổng tham mưu` (`p000008`, `p000009`, `p000016`, `p000029`, `p000037`).
  - `Ildoan officer` / `Ildoan` -> `sĩ quan người Ildoa` / `Ildoa` (`p000024`, `p000034`).
  - `Lieutenant Colonel Uger` -> `Trung tá Uger` (`p000032`).
  - `General von Zettour` -> `Tướng von Zettour` (`p000035`).
- Các thuật ngữ / cụm chức danh mới ghi nhận để theo dõi thêm:
  - `mobile task force` -> `lực lượng đặc nhiệm cơ động` (`p000013`)
  - `Personnel` -> `bên Nhân sự` (`p000014`)
  - `military bureaucrat` -> `quan chức hành chính quân sự` (`p000016`, `p000019`)
  - `Lergen Kampfgruppe` -> `Kampfgruppe Lergen` (`p000026`)
