# Báo cáo tự kiểm dịch thuật — `vol-07-ch-05-b07` (Sign-off)

## 1. Phạm vi và thông tin chung
- **Task ID:** `vol-07-ch-05-b07-translator-signoff` (parent: `vol-07-ch-05-b07`)
- **Tập / Chương:** `vol-07`, chương 5 (`OEBPS/Text/chapter018.xhtml`)
- **Mã đoạn:** `YS-LN07/Text/chapter018.xhtml/p000231` đến `YS-LN07/Text/chapter018.xhtml/p000270` (40 đoạn)
- **Tệp dịch:** `translations/vol-07/ch-05-b07.jsonl`
- **Trạng thái từng dòng:** `reviewed`

## 2. Xử lý findings từ `reviews/prose/vol-07/ch-05-b07-argon-review.yml`
- **`YS-LN07/Text/chapter018.xhtml/p000234` (minor):** Đã chỉnh thời gian của giả định trong lời van nài của Mary từ quá khứ hoàn tất sang giả định ở hiện tại/tương lai (`Chỉ cần chúng ta chịu bám trụ lại thôi! Chúng ta có thể giải phóng quê hương tôi mà!`), khớp ngữ cảnh đơn vị vẫn chưa rút đi và tuân thủ `locked_choices`.
- **`YS-LN07/Text/chapter018.xhtml/p000249` (minor):** Đã đổi đại từ quy chiếu Đại tá Mikel từ `giống như anh…` thành `giống như ông ấy…` để cân xứng về sắc thái tuổi tác và cấp bậc với đại từ trần thuật `ông` dùng cho Trung tá Drake.

## 3. Tự kiểm theo các điểm kiểm soát & `locked_choices`

### 3.1. Nghĩa, logic, phủ định và sắc thái giả định
- Giữ nguyên mạch hội thoại và suy nghĩ nội tâm của Trung tá Drake khi thông báo lệnh rút quân và giải thích cho Trung úy Mary Sue về thất bại trực diện của Quân đội Liên bang tại mặt trận phía đông.
- Bảo toàn sắc thái phủ định kép, cách nói giảm nói tránh (`p000236`, `p000251`) và các phán đoán cá nhân mang tính suy luận của Drake (`p000260`–`p000267`).
- Giữ đúng thời gian và tính chất giả định trong lời phản kháng của Mary Sue (`p000234`) và giả định của Drake nếu chính ông nhận lệnh bảo vệ sở chỉ huy (`p000267`).

### 3.2. Đại từ và xưng hô
- **Trần thuật:** Trung tá Drake dùng đại từ `ông`; Trung úy Mary Sue dùng đại từ `cô`; Đại tá Mikel dùng đại từ `ông ấy` (`p000249`).
- **Nội tâm:** Tự quy chiếu của Drake dùng `mình`; khi nghĩ về Mary Sue trong lúc bực dọc (`p000231`) dùng `cô ta`, khi gọi các pháp sư Đế quốc thuộc tiểu đoàn của Ác quỷ sông Rhine dùng `bọn chúng`.
- **Hội thoại:**
  - Drake → Mary Sue: xưng `tôi`, gọi `cô` / `Trung úy Sue` / `Trung úy`.
  - Mary Sue → Drake: xưng `tôi`, gọi `ngài` / `thưa Trung tá` (dịch theo quân hàm thực tế của Trung tá Drake).

### 3.3. Chữ nghiêng và nhấn mạnh (`DEC-P01-002`)
- Đã kiểm tra và bảo toàn chính xác phạm vi nhấn mạnh `*...*` tương ứng với thẻ `<html:em>` trong nguồn ở 7 đoạn:
  - `YS-LN07/Text/chapter018.xhtml/p000231`: câu cảm thán nội tâm ở cuối đoạn.
  - `YS-LN07/Text/chapter018.xhtml/p000239`: từ mở đầu suy nghĩ trước khi thở dài.
  - `YS-LN07/Text/chapter018.xhtml/p000240`: cụm từ nhấn mạnh mức độ thay đổi tận gốc rễ.
  - `YS-LN07/Text/chapter018.xhtml/p000245`: câu mệnh lệnh bị nén lại không nói ra.
  - `YS-LN07/Text/chapter018.xhtml/p000251`: phần bình luận nội tâm sau cụm từ được trích lại.
  - `YS-LN07/Text/chapter018.xhtml/p000255`: biệt danh của kẻ địch đặt giữa cặp dấu gạch ngang.
  - `YS-LN07/Text/chapter018.xhtml/p000270`: câu cảm nghĩ nội tâm ở đầu đoạn.
- Không tự ý thêm `*...*` vào các đoạn không có thẻ nhấn mạnh trong nguồn.

### 3.4. Thuật ngữ và mục chờ duyệt (`pending_term_recommendations`)
- Tuân thủ đầy đủ các `pending_term_recommendations` và `locked_choices` trong báo cáo review Argon:
  - `Trung úy Sue` / `Mary` / `Sue` / `trung úy` / `Trung úy`
  - `Drake` / `thưa Trung tá`
  - `quân du kích`
  - `mặt trận phía đông` / `Norden` / `lãnh thổ cựu Liên minh Hiệp ước`
  - `Ác quỷ sông Rhine`
  - `Liên bang` / `Quân đội Liên bang` / `dân Cộng sản` / `Đại tá Mikel`
  - `Tập đoàn quân phía Tây` / `Sở chỉ huy Tập đoàn quân phía Tây của Liên bang` / `sở chỉ huy khu vực` / `sở chỉ huy`
  - `chiến thuật chặt đầu chỉ huy` / `hệ thống chỉ huy` / `trận bao vây tiêu diệt hoàn toàn`
  - `sĩ quan ma pháp` / `Lục quân Khối Thịnh vượng chung` / `đơn vị pháp sư hải quân đánh bộ`

## 4. Kết luận tự kiểm
- Không có câu nguồn tiếng Anh trong báo cáo.
- Đủ 40 dòng JSONL khớp thứ tự, `segment_id`, `source_sha256` với gói nguồn và toàn bộ đã cập nhật `status: "reviewed"`.
