# Báo cáo tự kiểm (Self-Check): `vol-11-ch-01-b19` (Sign-off)

## 1. Thông tin chung
- **Task ID:** `vol-11-ch-01-b19-translator-signoff` (Parent: `vol-11-ch-01-b19`)
- **Phạm vi đoạn:** `YS-LN11/Text/chapter004.xhtml/p000198` đến `YS-LN11/Text/chapter004.xhtml/p000238` (41 đoạn)
- **Tệp bản dịch:** `translations/vol-11/ch-01-b19.jsonl`
- **Trạng thái các dòng:** `reviewed` (41/41 dòng)

## 2. Xử lý các Findings trong Argon Review (`ch-01-b19-argon-review.yml`)
- **`p000201` (minor - `pronouns_clarity`):** Đã đổi `nhưng ông ấy không thể làm theo ý mình được` thành `nhưng ông ấy không thể được như ý` để tránh trùng từ `mình` (vốn là đại từ tự quy chiếu nội tâm của Tanya) và làm rõ nghĩa Zettour không được toại nguyện.
- **`p000226` & `p000230` (minor - `pronouns_register`):** Đã đổi `Cả hai chúng tôi` (`p000226`) và `cả hai chúng tôi` (`p000230`) thành `Cả hai chúng ta` / `cả hai chúng ta` để nhất quán hệ đại từ độc thoại nội tâm của Tanya.
- **`p000227` (minor - `tone_register`):** Đã đổi `khi thốt ra từ miệng một vị trung tướng đấy ạ` thành `khi được nghe từ một vị trung tướng đấy ạ` để giữ đúng sắc thái lễ độ bề ngoài của Tanya trước cấp trên.
- **`p000231` (minor - `rank_address_register`):** Đã bỏ tiểu từ `ạ` sau danh xưng `Trung tá` trong lời thoại của Tướng Zettour nói với cấp dưới (`“Đó là lý do vì sao, Trung tá, mọi chuyện có thể sẽ trở nên cam go đối với quân của cô đấy.”`), thống nhất với `p000221` và `p000228`.

## 3. Kiểm tra theo các mốc chuẩn (Checkpoints) & Locked Choices

### 3.1. Nghĩa, logic, giả định và sắc thái
- Đảm bảo truyền tải đầy đủ lập luận của Tanya khi từ chối vị trí cánh tay phải của Zettour tại mặt trận phía đông (`p000198`–`p000205`), giữ nguyên tính giả định ở các câu nói về việc sẽ ra sao nếu nhận chức hoặc nếu có người kế nhiệm chỉ huy tại đó.
- Giữ rõ mạch đối thoại và suy nghĩ về Hội đồng Tự trị (`p000209`–`p000219`), sự bất lực của tổ chức này nếu thiếu Lục quân Đế quốc giữ tiền tuyến, cũng như tính toán thực dụng của Zettour khi tin rằng Liên bang sẽ đẩy Hội đồng Tự trị vào thế đối đầu sinh tử.
- Truyền tải rõ sắc thái bông đùa chua chát và sự chấp nhận thực tại cay đắng giữa Zettour và Tanya ở phần cuối chương (`p000220`–`p000238`).
- Tại `p000234`–`p000235`, xử lý rõ nét phép chơi chữ trong nội tâm của Tanya về sắc đen: từ sự đen tối của đất nước, màu máu oxy hóa đen kịt, trạng thái sổ sách có lãi (con số màu đen) cho đến khái niệm tổ chức/doanh nghiệp đen bóc lột và phạm pháp.

### 3.2. Đại từ và xưng hô (`DEC-P01-001` & ngữ cảnh Vol 11)
- **Nội tâm Tanya:** Dùng `mình` nhất quán khi tự quy chiếu; gọi Zettour là `Tướng Zettour` / `ông ấy` / `cấp trên của mình`. Ở các câu nhận định chung bao hàm cả hai người hoặc phía Đế quốc (`p000209`, `p000226`, `p000230`, `p000235`), dùng `chúng ta` nhất quán.
- **Trần thuật ngôi thứ ba / khách quan hóa điểm nhìn:** Dùng `Tanya` / `cô` (`p000201`, `p000203`, `p000204`) nhất quán với các lô trước của Tập 11.
- **Đối thoại Tanya – Zettour:**
  - Tanya xưng `tôi`, gọi Zettour là `ngài` (kèm từ kính ngữ `ạ` phù hợp vị thế cấp dưới đối với cấp trên trực tiếp trong Bộ Tổng tham mưu).
  - Zettour xưng `tôi`, gọi Tanya là `cô` và `Trung tá`.

### 3.3. Nhấn mạnh (`DEC-P01-002`)
- Kiểm tra toàn bộ 41 đoạn nguồn, chỉ có 2 vị trí có thẻ nhấn mạnh `<html:em>` và đã được biểu diễn chính xác bằng `*...*`:
  - `p000209`: `*độc lập*`
  - `p000225`: `*nếu*`
- Toàn bộ 39 đoạn còn lại không có nhấn mạnh trong nguồn và không dùng `*...*`.

### 3.4. Thuật ngữ và mục đang chờ xét (Pending Terms)
- Tuân thủ đầy đủ tất cả `pending_term_recommendations` và `locked_choices` trong `ch-01-b19-argon-review.yml`:
  - `các thanh tra viên` / `trung tướng` / `trung tá` (`p000198`, `p000227`)
  - `Tướng Zettour` / `Tướng Romel` / `Tướng Rudersdorf` / `sĩ quan chỉ huy` (`p000199`, `p000201`, `p000203`, `p000208`, `p000209`, `p000219`, `p000222`)
  - `Trung tá` (`p000221`, `p000228`, `p000231`)
  - `Kampfgruppe` (`p000204`)
  - `mặt trận phía đông` / `miền đông` / `Đế quốc` / `Lục quân Đế quốc` / `Liên bang` (`p000202`, `p000206`, `p000207`, `p000209`, `p000213`, `p000214`, `p000217`, `p000219`, `p000221`)
  - `Hội đồng Tự trị` / `chiến dịch tác chiến chiều sâu` (`p000210`, `p000218`, `p000219`)
  - `chủ nghĩa thực dụng` / `lý tính nhà nước` / `sự tất yếu` (`p000219`, `p000238`)
