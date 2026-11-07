# Báo cáo tự kiểm dịch thuật & Sign-off — `vol-07-ch-05-b08`

## 1. Phạm vi và thông tin chung
- **Task ID:** `vol-07-ch-05-b08-translator-signoff` (parent: `vol-07-ch-05-b08`)
- **Tập / Chương:** `vol-07`, chương 5 (`OEBPS/Text/chapter018.xhtml`)
- **Mã đoạn:** `YS-LN07/Text/chapter018.xhtml/p000271` đến `YS-LN07/Text/chapter018.xhtml/p000301` (31 đoạn)
- **Tệp dịch:** `translations/vol-07/ch-05-b08.jsonl`
- **Trạng thái từng dòng:** `reviewed`

## 2. Tiếp nhận và xử lý Argon Review (`reviews/prose/vol-07/ch-05-b08-argon-review.yml`)
- **`YS-LN07/Text/chapter018.xhtml/p000274` (minor):** Tiếp nhận. Đổi đại từ chỉ Ác quỷ sông Rhine trong lời thoại của Trung tá Drake từ `ả` sang `cô ta` (`Có dấu hiệu cho thấy cô ta đang hoạt động ở mặt trận phía đông.`) để giữ sắc thái trung tính, chuẩn mực của sĩ quan Khối Thịnh vượng chung khi trao đổi công việc.
- **`YS-LN07/Text/chapter018.xhtml/p000299` (minor):** Tiếp nhận. Chỉnh cấu trúc mệnh đề điều kiện để tách rõ vị trí cố thủ và hành động kháng cự có tổ chức (`Nếu quân du kích và các pháp sư cố thủ ngay tại gốc rễ của các tuyến giao thông liên lạc hoặc một cứ điểm bàn đạp rồi tiến hành kháng cự có tổ chức, một đơn vị vũ trang hạng nặng sẽ xuất hiện.`).
- **Locked choices & Pending term recommendations:** Đã rà soát toàn bộ 31 đoạn, bảo đảm tuân thủ đầy đủ mọi `locked_choices` và `pending_term_recommendations` trong báo cáo review của Argon.

## 3. Tự kiểm theo các điểm kiểm soát

### 3.1. Nghĩa, logic, phủ định và sắc thái giả định
- Giữ nguyên mạch hội thoại và suy nghĩ nội tâm của Trung tá Drake khi tiếp tục giải thích cho Trung úy Mary Sue về lý do phải rút khỏi khu vực lãnh thổ cựu Liên minh Hiệp ước để chuyển lực lượng chiến đấu sang mặt trận phía đông theo quyết định của Sở chỉ huy liên hợp.
- Bảo toàn chính xác các cấu trúc giả định và nhượng bộ:
  - Giả định trái thực tế ở quá khứ của Drake nếu đối diện là một sĩ quan ma pháp hải quân đánh bộ của Khối Thịnh vượng chung (`p000275`).
  - Lập luận chiến lược về tác chiến trên nhiều mặt trận, hỗ trợ du kích, bài học từ sự kiện Arene của Quân đội Cộng hòa trên mặt trận Rhine (`p000279`–`p000292`).
  - Nhận định về thái độ kiềm chế có tính toán của Lục quân Đế quốc trước các cuộc tấn công lẻ tẻ của du kích và giới hạn mà nếu vượt qua sẽ kích hoạt phản ứng tàn khốc vì lý trí quốc gia (`p000294`–`p000300`).
  - Lời đề nghị bỏ lửng của Mary ở cuối lô (`p000301`).
- Không thêm bớt ý hay tự suy diễn ngoài văn cảnh nguồn.

### 3.2. Đại từ và xưng hô (`DEC-P01-001`)
- **Trần thuật:** Trung tá Drake dùng đại từ `ông`; Trung úy Mary Sue dùng đại từ `cô`; Lục quân Đế quốc / quân địch dùng `chúng` (theo điểm nhìn của Drake), Ác quỷ sông Rhine trong lời thoại của Drake dùng `cô ta` (`p000274`).
- **Nội tâm / tự quy chiếu:** Tự quy chiếu của Drake dùng `mình`.
- **Hội thoại:**
  - Drake → Mary Sue: xưng `tôi`, gọi `cô` / `Trung úy`.
  - Mary Sue → Drake: xưng `tôi`, gọi `ngài`.

### 3.3. Chữ nghiêng và nhấn mạnh (`DEC-P01-002`)
- Đã kiểm tra và bảo toàn chính xác phạm vi nhấn mạnh `*...*` tương ứng với thẻ `<html:em>` trong nguồn ở 3 đoạn:
  - `YS-LN07/Text/chapter018.xhtml/p000271`: cụm thuật ngữ mở đầu đoạn (`*Chiến thuật chặt đầu chỉ huy.*`).
  - `YS-LN07/Text/chapter018.xhtml/p000289`: tính từ được hỏi lại trong lời thoại của Mary (`*hạn chế*`).
  - `YS-LN07/Text/chapter018.xhtml/p000295`: cụm trạng từ đầu câu thứ hai (`*bất ngờ thay*`).
- Không tự ý thêm `*...*` vào các đoạn không có thẻ nhấn mạnh trong nguồn.

### 3.4. Thuật ngữ và mục chờ duyệt (`pending_terms`)
- Dùng nhất quán các phương án tạm đã khóa trong `reviews/prose/vol-07/ch-05-b08-argon-review.yml`:
  - `chiến thuật chặt đầu chỉ huy`, `Lục quân Đế quốc`, `các pháp sư trên không`, `yểm trợ trực tiếp`, `pháo phòng không`, `Ác quỷ sông Rhine`
  - `mặt trận phía đông`, `Sở chỉ huy liên hợp`, `cấp trên`
  - `sĩ quan ma pháp hải quân đánh bộ của Khối Thịnh vượng chung`, `tiền tuyến`, `tuyến tiền tiêu`, `các chiến tuyến chính`, `các tuyến giao thông liên lạc`, `mặt trận thống nhất quốc tế`
  - `Liên minh Hiệp ước`, `Trung úy`, `Đại tá Mikel`, `Liên bang`, `Quân đội Liên bang`, `quân du kích` / `lực lượng du kích`
  - `Quân đội Cộng hòa`, `mặt trận Rhine`, `Arene`, `dân quân`
  - `lý trí quốc gia`

## 4. Kết luận tự kiểm
- Không có câu nguồn tiếng Anh trong báo cáo.
- Đủ 31 dòng JSONL khớp thứ tự, `segment_id`, `source_sha256` với gói nguồn và toàn bộ đã cập nhật `status: "reviewed"`.
