# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-03-b13`

- **Task ID**: `vol-10-ch-03-b13`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter018.xhtml/p000307` đến `YS-LN10/Text/chapter018.xhtml/p000340` (34 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc
- Đã dịch đầy đủ 34/34 đoạn theo đúng thứ tự nguồn từ `p000307` đến `p000340`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 34 dòng đã được cập nhật từ `draft` sang `reviewed` sau khi xử lý Argon review.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter018.xhtml/p000311`: `*giọng nói*`.
  - `YS-LN10/Text/chapter018.xhtml/p000325`: `*với*`.
  - `YS-LN10/Text/chapter018.xhtml/p000333`: `*pháp sư đó*`.
- Tất cả 31 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.

## 2. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Nửa đầu batch (`p000307` – `p000328`) — Trần thuật và đối thoại xoay quanh Trung tá Drake**:
  - Trần thuật ngôi thứ ba gọi `Trung tá Drake` / `Drake` là `anh`.
  - Trong các câu độc thoại/lẩm bẩm một mình của Drake trên hành lang (`p000308`, `p000313`, `p000315`, `p000328`), Drake tự xưng `mình` (hoặc lược chủ ngữ tự nhiên), thể hiện rõ tâm trạng uất ức, bức bối khi trải nghiệm sinh tử ngoài chiến trường bị cấp trên phủ nhận.
  - Khi đề cập đến Tanya (`Ác quỷ sông Rhine` / `con tiểu quỷ`), dùng danh xưng trung tính `con ác quỷ đó` (đã điều chỉnh `p000311` để loại bỏ đại từ nữ hóa sớm khi Drake chưa biết danh tính thật ở `p000314`).
  - Trong cuộc trò chuyện tình cờ ở hành lang giữa Drake và `Kim` (một đặc vụ tình báo quen biết mặc âu phục lịch lãm, `p000318` – `p000324`), hai người xưng hô `tôi` – `anh` thân tình, tự nhiên và đúng chuẩn mực đồng nghiệp/người quen tại chính quốc.
- **Nửa sau batch (`p000329` – `p000340`) — Đánh giá của ngành tình báo Khối Thịnh vượng chung và góc nhìn của Tướng Habergram**:
  - Phân biệt rõ chủ thể đại từ giữa `Drake` (`anh` / `người đàn ông đó` / `Trung tá Drake`) và `Habergram` (`ông` / `vị tướng`):
    - Từ `p000329` đến `p000333`: đại từ ngôi thứ ba chỉ `Drake` (`anh`), mô tả sự đánh giá rất cao của Tổng hành dinh Cơ quan Tình báo Khối Thịnh vượng chung về năng lực, lòng trung thành với Lục quân Hoàng gia cùng Vương quyền, và xuất thân mẫu mực của anh.
    - Từ `p000334` đến `p000340`: điểm nhìn chuyển sang `Tướng Habergram` (`ông`). Dù ngoài mặt thẳng thừng bác bỏ Drake trong buổi báo cáo để giữ lập trường, thực chất Habergram phải cố giấu sự bàng hoàng và nghiêm túc suy xét khả năng chỉ huy của tiểu đoàn đối phương tự di chuyển một mình sang mặt trận phía đông để hỗ trợ Zettour hoặc vì mục đích liên lạc.

## 3. Kiểm tra các cấu trúc ngữ pháp và sắc thái dễ lệch nghĩa
- **`p000307` – `p000312`**: Giữ nguyên sự tương phản giữa thực tế y học (vết thương ở vai đã được chữa lành hoàn toàn bằng ma pháp tại chính quốc) và cảm giác đau nhức dữ dội mang tính tâm lý/ký ức chiến trường, cùng sự khẳng định tuyệt đối của Drake rằng ở cự ly áp sát phải tung đòn cảm tử để thoát thân, ngay cả `thuật thức nghi binh quang học` cũng không thể đánh lừa được anh—đặc biệt là cái `*giọng nói*` không thể nhầm lẫn của đối phương đã làm lộ tẩy tất cả.
- **`p000321` – `p000325`**: Phản ánh đúng nét hài hước chua chát trong suy nghĩ của Drake: anh rất cảm kích sự hiếu khách tại chính quốc và muốn ra quán rượu xả cơn bực tức, nhưng vừa phải điền biểu mẫu bắt buộc suốt buổi tối, vừa chẳng thể đi nói xấu cơ quan tình báo `*với*` chính một đặc vụ của cơ quan đó.
- **`p000331` – `p000332`**: Bảo toàn phép so sánh về lòng trung thành của Drake với `Lục quân Hoàng gia` và `Vương quyền` ngang ngửa bất kỳ `pháp sư hải quân` nào (vốn là lực lượng nòng cốt rất được tin cậy của Khối Thịnh vượng chung), giải thích lý do anh được chọn cử tới `Liên bang`.
- **`p000338` – `p000340`**: Giữ đúng mạch lập luận tình báo của Habergram: nguồn tin báo `Ác quỷ sông Rhine` cùng tiểu đoàn của cô ta đang ở phía tây đã được kiểm chứng và củng cố bởi nhiều báo cáo từ tuyến phòng thủ dọc eo biển; nhưng vì báo cáo của Drake từ phía đông vừa mới mẻ vừa đáng tin cậy, Habergram buộc phải tính đến giả thuyết chỉ huy đơn vị di chuyển độc lập tách khỏi tiểu đoàn.

## 4. Thuật ngữ đã áp dụng và đề xuất (`pending_terms`)
- Kế thừa nhất quán các phương án từ `work/run-state/pending-terms-index.yml` và `argon-review`:
  - `chính quốc` (`p000307`, `p000318`, `p000325`)
  - `thuật thức nghi binh quang học` (`p000310`)
  - `Ác quỷ sông Rhine` (`p000314`, `p000336`, `p000338`, `p000340`)
  - `Drake` / `Trung tá Drake` (`p000316`, `p000318`, `p000321`, `p000325`, `p000326`, `p000329`, `p000339`)
  - `Kim` (`p000319`)
  - `ông Johnson` (`p000326`)
  - `sĩ quan ma pháp trên không` (`p000329`)
  - `cơ quan tình báo của Khối Thịnh vượng chung` (`p000329`)
  - `Tổng hành dinh Cơ quan Tình báo Khối Thịnh vượng chung` (`p000330`)
  - `Lục quân Hoàng gia` (`p000331`)
  - `Vương quyền` (`p000331`)
  - `pháp sư hải quân` (`p000331`)
  - `Liên bang` (`p000332`)
  - `Khối Thịnh vượng chung` (`p000332`)
  - `Habergram` (`p000333`)
  - `át chủ bài của Đế quốc` (`p000339`)
  - `Zettour` (`p000339`)

## 5. Xử lý Argon Review (Translator Sign-off)
- **`YS-LN10/Text/chapter018.xhtml/p000311` (minor)**: Tiếp nhận khuyến nghị của Argon Reviewer, chỉnh từ `"mới là thứ thực sự tố giác cô ta!"` thành `"mới là thứ thực sự làm lộ tẩy tất cả!"` để giữ tính trung tính về danh tính đối phương trong góc nhìn của Drake.
- **`YS-LN10/Text/chapter018.xhtml/p000331` (minor)**: Tiếp nhận khuyến nghị của Argon Reviewer, đổi danh từ thứ hai thành `"Vương quyền"` (`"Lục quân Hoàng gia và Vương quyền"`) để tránh lặp cụm từ `"Hoàng gia"` sát nhau.
- Đã kiểm tra và tuân thủ đầy đủ toàn bộ `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-10/ch-03-b13-argon-review.yml`.
- Đã cập nhật `status` của toàn bộ 34/34 dòng từ `draft` sang `reviewed`.
