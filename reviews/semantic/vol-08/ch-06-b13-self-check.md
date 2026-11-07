# Báo cáo tự kiểm (Semantic Self-Check) — `vol-08-ch-06-b13`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-06-b13`
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter022.xhtml/p000484` – `YS-LN08/Text/chapter022.xhtml/p000527` (44 đoạn)
- **Tệp đích**: `translations/vol-08/ch-06-b13.jsonl`

## 2. Kiểm tra đối chiếu quy chuẩn & thuật ngữ
- **Ngôi kể và điểm nhìn (`DEC-P01-001`)**:
  - Trần thuật ngôi thứ ba theo điểm nhìn của Tanya ở các đoạn `p000484`, `p000488`, `p000495`, `p000497`, `p000498`, `p000502`, `p000504`, `p000509`, `p000512`, `p000515`, `p000520`, `p000524`, `p000525`: quy chiếu Tanya là `cô`, Trung tướng von Zettour là `ông` (hoặc `ông ta` trong nội tâm cảnh giác của Tanya tại `p000495`), Trung tá Uger là `anh`.
  - Độc thoại nội tâm của Tanya ở các đoạn `p000490`–`p000492`, `p000495`, `p000502`, `p000509`, `p000519`, `p000520`: tự quy chiếu cá nhân là `mình` và tự quy chiếu tập thể là `chúng ta`.
- **Xưng hô trong hội thoại**:
  - Đối thoại giữa Trung tướng von Zettour và Trung tá Tanya von Degurechaff (`p000485`–`p000487`, `p000489`, `p000493`, `p000494`, `p000496`, `p000499`–`p000501`, `p000505`–`p000507`, `p000510`, `p000511`, `p000513`, `p000514`, `p000516`–`p000518`, `p000521`–`p000523`, `p000527`): Zettour tự xưng `tôi` / `chúng ta`, gọi Tanya là `Trung tá von Degurechaff` / `cô`, gọi Uger là `Trung tá Uger` / `anh ta`; Tanya tự xưng `tôi` / `chúng ta`, gọi Zettour là `Tướng quân` (`Thưa Tướng quân`, `thưa ngài`) và `ngài`, giữ đúng sắc thái lễ độ, thận trọng của cấp dưới trước tướng lĩnh cấp cao.
- **Bảo toàn nhấn mạnh (`DEC-P01-002`)**:
  - Đoạn `p000495`: bảo toàn câu nội tâm và từ nhấn mạnh bằng `*Mình thực sự bắt đầu ghét cuộc tranh luận này rồi đấy*` và `*hoàn toàn không*`.
  - Đoạn `p000504`: bảo toàn câu bình phẩm nội tâm bằng `*Kẻ ngu xuẩn nào lại đi làm cái trò đó cơ chứ?!*`.
  - Đoạn `p000508`: bảo toàn toàn bộ đoạn nhấn mạnh bằng `*Sodom và Gomorrah, thành phố muối.*`.
  - Đoạn `p000511` và `p000512`: bảo toàn cụm nhấn mạnh bằng `*bị cai trị bởi người chết*`.
  - Đoạn `p000525`: bảo toàn câu cảm thán nội tâm bằng `*Chắc chắn anh ta không đến mức ngu xuẩn như thế!*`.
  - Đoạn `p000526`: bảo toàn toàn bộ câu hỏi nội tâm bằng `*Chuyện đó thực sự xảy ra ư?*`.
  - Tất cả các đoạn còn lại không có nhấn mạnh trong nguồn và không dùng dấu `*...*`.
- **Thuật ngữ và tên riêng (`pending_terms` & `glossary`)**:
  - Tuân thủ nhất quán các thuật ngữ đã có trong `canon/` và `pending-terms-index.yml`: `Zettour`, `Tanya`, `Thưa Tướng quân`, `cấp độ chiến lược`, `Trung tá von Degurechaff`, `Đế quốc`, `Being X`, `Bộ Tư lệnh Tối cao`, `hậu phương`, `tiền tuyến`, `Trung tá Uger`, `bản quốc`, `vốn con người`, `Lục quân Đế quốc`.
  - Đề xuất thuật ngữ / cách diễn đạt tạm trong lô: `đế đô` (`p000500`), `hòn đá triết gia` (`p000501`), `Sodom và Gomorrah, thành phố muối` (`p000508`), `hiệu ứng Concorde` (`p000519`), `kẻ ngu xuẩn cỡ siêu thiết giáp hạm` (`p000525`).

## 3. Tự kiểm tra kỹ thuật & Sign-off
- Đủ 44/44 dòng JSONL, khớp thứ tự `segment_id` từ `p000484` đến `p000527`.
- Báo cáo `reviews/prose/vol-08/ch-06-b13-argon-review.yml` có 0 findings (`serious: 0, moderate: 0, minor: 0`); toàn bộ `pending_term_recommendations` và `locked_choices` từ `p000484` đến `p000527` đều đã khớp và được tuân thủ đầy đủ.
- Đã cập nhật trường `status` của toàn bộ 44 dòng trong `translations/vol-08/ch-06-b13.jsonl` từ `"draft"` sang `"reviewed"`, giữ nguyên `translator` là `"argon-low"`, khớp `source_sha256` và `glossary_version` trong handoff.
- Không chép văn bản nguồn tiếng Anh vào bản dịch hoặc báo cáo tự kiểm.
