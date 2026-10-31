# Báo cáo tự kiểm (Self-Check): `vol-04-ch-06-b02`

- **Task ID**: `vol-04-ch-06-b02-translator-signoff` (parent: `vol-04-ch-06-b02`)
- **Translator**: `argon-low`
- **Handoff**: `handoffs/vol-04/ch-06-b02.yml` (`handoffs/vol-04/ch-06-b02-translator-signoff.yml`)
- **Review tiếp nhận**: `reviews/prose/vol-04/ch-06-b02-argon-review.yml`
- **Tệp dịch**: `translations/vol-04/ch-06-b02.jsonl`
- **Phạm vi**: `YS-LN04/Text/chapter001_v.xhtml/p000023` → `YS-LN04/Text/chapter001_v.xhtml/p000045` (23 đoạn)
- **Trạng thái mỗi dòng**: `reviewed`

## 1. Kiểm tra tính đầy đủ, nghĩa gốc và xử lý review (`ch-06-b02-argon-review.yml`)
- Toàn bộ 23 đoạn từ `chapter001_v.xhtml/p000023` đến `chapter001_v.xhtml/p000045` đã được rà soát đối chiếu với `reviews/prose/vol-04/ch-06-b02-argon-review.yml` và cập nhật trạng thái từ `draft` sang `reviewed`.
- **Xử lý finding trong `argon-review`**:
  - `YS-LN04/Text/chapter001_v.xhtml/p000037` (`minor` / `pronoun_clarity`): Tiếp nhận khuyến nghị của reviewer Argon, chỉnh cụm `Tanya rất thích nó` ở câu đầu thành `Tanya rất thích công việc này` để tránh lặp và chuyển đổi quy chiếu đột ngột với đại từ `nó` chỉ Tanya ở câu ngay sau (`mỗi ngày nó đều được tan làm đúng giờ`), đồng thời khớp hoàn toàn với `locked_choices` của `p000037` (`nó (Tanya ở câu hai)`).
- **Tuân thủ `pending_term_recommendations` và `locked_choices`**:
  - Giữ nguyên toàn bộ các phương án thuật ngữ được đề xuất trong `pending_term_recommendations`: `*Nguồn gốc Hành động Đối ngoại của Liên bang*`, `Liên bang` (`p000040`), `Chủ nghĩa Cộng sản`, `chính trị cường quyền` (`p000041`), `quản trị nhân tài` (`p000043`).
  - Bảo đảm 23/23 đoạn tuân thủ tuyệt đối các mục `terms`, `ranks`, `pronouns`, `pov` và `markdown_emphasis` trong `locked_choices`.
- Giữ đúng mạch nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic nhân quả và thời gian của giả định:
  - **Hy vọng Lục quân Đế quốc trụ vững để bảo toàn khoản đầu tư vốn con người và vấn đề người kế nhiệm chỉ huy Tiểu đoàn 203 (`chapter001_v/p000023`–`p000031`)**: Vì quốc gia bại trận chẳng có mấy chỗ dùng cho quân nhân cấp cao hay sự nghiệp nhà binh ngoài các công ty lính đánh thuê, và Tanya đã dành thời gian quý báu để đánh bóng hồ sơ quân ngũ của mình, nên để không lãng phí khoản đầu tư vốn con người này, tất cả những gì nó có thể làm là hy vọng Lục quân Đế quốc giành chiến thắng hoặc chí ít là tránh được thất bại chí mạng và trụ vững (`p000023`–`p000024`); phần lớn niềm hy vọng đó đặt vào người chỉ huy tiếp theo của Tiểu đoàn Pháp sư Trên không số 203—dù chưa có chỉ thị chính thức nhưng nhiều khả năng sẽ là Đại úy Weiss như nó đã đề xuất, chỉ vướng một vấn đề tiềm ẩn là theo cơ chế của Lục quân Đế quốc thì anh ta cần được thăng lên thiếu tá để tiếp nhận quyền chỉ huy tiểu đoàn, và dù anh ta thăng tiến khá nhanh nhưng cấp trên vẫn cần thêm chút thời gian vì không thể lạm dụng mãi mánh lách luật lấy danh nghĩa thành lập tiểu đoàn như Tướng von Zettour từng dùng cho Tanya (`p000025`–`p000027`); thở dài bên bàn làm việc vì sự thiếu linh hoạt đó và nén lại lời than phiền về những kẻ thích ngáng đường người khác, Tanya nhận thấy việc tiếp tục giữ chức tiểu đoàn trưởng thêm một thời gian trên danh nghĩa để Weiss tích lũy thêm kinh nghiệm cũng giúp tránh lời ra tiếng vào từ đám bàn giấy ở hậu phương về tốc độ thăng tiến của anh ta, nên nó vẫn chu toàn công tác chuẩn bị nền tảng cần thiết và xem đây là một công việc không tồi (`p000028`–`p000031`).
  - **Cuộc sống nghỉ ngơi của Tiểu đoàn 203 tại thủ đô, niềm vui làm việc bàn giấy đúng giờ của Tanya và sự đón nhận dành cho tập tài liệu nghiên cứu về Liên bang (`chapter001_v/p000032`–`p000045`)**: Sau khi lập công trong trận không chiến ở phía tây cùng các chiến dịch khác, các thành viên Tiểu đoàn Pháp sư Trên không số 203 đang nghỉ ngơi theo lịch luân phiên tiêu chuẩn tại khu lưu trú của Bộ Tổng tham mưu ở thủ đô—nhờ trực thuộc thẳng Bộ Tổng tham mưu nên cấp dưới của Tanya được tận hưởng kỳ nghỉ tại cơ sở điều dưỡng vốn chỉ dành cho sĩ quan tham mưu (`p000032`–`p000033`); về phần Tanya, trong lúc chờ Bộ Tổng tham mưu hoàn tất thẩm định bản báo cáo *Sử dụng Đơn vị và Cơ động Chiến dịch trong Cuộc chiến Hiện tại*, nó làm công việc sắp xếp lưu trữ tài liệu mật đóng dấu tối mật chuyển đến từ Phòng Nghiên cứu Chiến lược—công việc bàn giấy cần quyền tiếp cận mật và sự tín nhiệm nhưng giúp nó đào sâu hiểu biết về thực trạng Lục quân Đế quốc lẫn tình hình đối ngoại qua tin tức tình báo từ các mặt trận, và tuyệt vời nhất là được tan làm đúng giờ mỗi ngày để tận hưởng giấc ngủ yên bình thay vì phải trực đêm đánh chặn quân xâm nhập bất kể giờ giấc (`p000034`–`p000038`); nhịp sinh hoạt điều độ giúp công việc văn phòng đạt hiệu quả cao, tiêu biểu là tập tài liệu nhỏ hướng tới giới chuyên gia mang tựa đề *Nguồn gốc Hành động Đối ngoại của Liên bang*—phê phán thực tế rằng những kẻ bị tiêm nhiễm Chủ nghĩa Cộng sản cùng hệ tư tưởng đảng phái của nó thực chất lại sùng bái chính trị cường quyền hơn cả hệ tư tưởng của chính họ—vốn không được nó kỳ vọng cao nhưng lại nhận được sự đón nhận nồng nhiệt từ đủ mọi giới kể cả trong Lục quân Đế quốc (`p000039`–`p000041`); thở phào vì năng lực bàn giấy và phân tích của mình được ghi nhận và quyết tâm gắn bó trọn đời với công việc văn phòng theo nguyên tắc quản trị nhân tài, Tanya vừa đều đặn xem xét tài liệu trong quãng thời gian chẳng khác nào kỳ nghỉ sau khi trở về từ chiến tuyến phía tây, vừa âm thầm tính đường tích lũy tài sản và cân nhắc đào tẩu nếu kịch bản thất bại là không thể tránh khỏi, dù may mắn là theo báo cáo từ tiền tuyến thì các phòng tuyến vẫn đang xoay xở trụ vững (`p000042`–`p000045`).
- Không sao chép văn bản hay cụm từ tiếng Anh từ nguồn vào báo cáo.

## 2. Kiểm tra đại từ, xưng hô và giọng văn (`DEC-P01-001`)
- Tuân thủ nghiêm ngặt `DEC-P01-001`, `canon/style-guide.md` và `locked_choices`:
  - **Trong trần thuật ngôi thứ ba bám sát điểm nhìn của Tanya**: quy chiếu `Tanya` nhất quán bằng tên riêng và đại từ `nó` kết hợp phản thân `mình` (`p000023`–`p000025`, `p000027`–`p000028`, `p000030`, `p000033`–`p000040`, `p000042`, `p000044` — tuyệt đối không dùng `cô` / `cô ấy` cho Tanya trong lời kể hay độc thoại nội tâm; riêng `p000037` đã chỉnh câu đầu thành `Tanya rất thích công việc này` để dành đại từ `nó` ở câu hai quy chiếu duy nhất về Tanya).
  - **Trong độc thoại nội tâm và câu bình luận trực tiếp từ điểm nhìn ngôi thứ nhất của Tanya (`p000027`, `p000029`, `p000041`, `p000043`)**: tự quy chiếu ngôi thứ nhất số ít bằng `Mình` / `mình`.
  - **Quy chiếu các nhân vật và tập thể khác**: quy chiếu `Đại úy Weiss` / `Weiss` bằng `anh ta` (`p000025`, `p000026`, `p000029`), quy chiếu Bộ Tổng tham mưu / Lục quân Đế quốc / những người theo Chủ nghĩa Cộng sản bằng `họ` (`p000023`, `p000026`–`p000028`, `p000041`).

## 3. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002`)
- Kiểm tra toàn bộ 4 đoạn có thẻ `<html:em>` trong XHTML nguồn và bảo toàn chính xác bằng cặp dấu `*...*` đúng phạm vi nhấn mạnh:
  - `chapter001_v/p000028`: có 2 cụm nhấn mạnh tách biệt trong cùng đoạn—chỉ bọc câu nội tâm đầu đoạn (`*Họ chẳng linh hoạt chút nào.*`) và câu than phiền nội tâm nằm giữa cặp dấu gạch ngang dài (`*Có quá nhiều kẻ cứ tìm cách ngáng đường người khác*`), phần trần thuật còn lại nằm ngoài dấu `*`.
  - `chapter001_v/p000034`: chỉ bọc nhan đề bản báo cáo của Tanya (`*Sử dụng Đơn vị và Cơ động Chiến dịch trong Cuộc chiến Hiện tại*`), phần còn lại của đoạn nằm ngoài dấu `*`.
  - `chapter001_v/p000040`: chỉ bọc nhan đề tập tài liệu chuyên khảo của Tanya (`*Nguồn gốc Hành động Đối ngoại của Liên bang*`), phần còn lại của đoạn nằm ngoài dấu `*`.
  - `chapter001_v/p000045`: chỉ bọc liên từ nhấn mạnh ở đầu câu đầu tiên (`*Nhưng*`), toàn bộ phần còn lại của đoạn nằm ngoài dấu `*`.
- Toàn bộ 19 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và không phát sinh dấu `*` ngoài nguồn.

## 4. Kiểm tra thuật ngữ và tính nhất quán (`canon/` & `pending_term_recommendations`)
- Áp dụng đồng bộ các thuật ngữ và tên gọi từ `canon/` và các lô trước:
  - `vốn con người` (`p000024` — đồng bộ `P03-human-capital` trong `canon/glossary-pending.yml`)
  - `Lục quân Đế quốc` (`p000024`, `p000026`, `p000037`, `p000041`)
  - `Tiểu đoàn Pháp sư Trên không số 203`, `Đại úy Weiss`, `Tướng von Zettour`, `tiểu đoàn trưởng` (`p000025`, `p000027`, `p000029`, `p000032`)
  - `Bộ Tổng tham mưu`, `cơ sở điều dưỡng`, `Phòng Nghiên cứu Chiến lược` (`p000032`–`p000034`, `p000037`)
  - `*Sử dụng Đơn vị và Cơ động Chiến dịch trong Cuộc chiến Hiện tại*` (`p000034` — đồng bộ `vol-04-ch-06-b01`).
- Ghi nhận và áp dụng nhất quán các thuật ngữ/cách diễn đạt trong `pending_term_recommendations` của `argon-review`:
  - `*Nguồn gốc Hành động Đối ngoại của Liên bang*`, `Liên bang` (`p000040`)
  - `Chủ nghĩa Cộng sản`, `chính trị cường quyền` (`p000041`)
  - `quản trị nhân tài` (`p000043`).

## 5. Kiểm tra định dạng và công cụ xác thực
- Chạy `python3 tools/validate_translation.py --handoff handoffs/vol-04/ch-06-b02.yml --source work/vol-04/batches/ch-06-b02-source.jsonl --translation translations/vol-04/ch-06-b02.jsonl`: kết quả `PASS` (exit code `0`, 23 dòng ở trạng thái `reviewed`, khớp hoàn toàn thứ tự mã đoạn và metadata).
