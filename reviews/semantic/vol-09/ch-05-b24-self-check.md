# Báo cáo tự kiểm (Self-Check): `vol-09-ch-05-b24`

- **Task ID**: `vol-09-ch-05-b24`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN09/Text/chapter020.xhtml/p000849` – `YS-LN09/Text/chapter020.xhtml/p000900` (52 đoạn)
- **File bản dịch**: `translations/vol-09/ch-05-b24.jsonl`

## 1. Kiểm tra tính đầy đủ và cấu trúc kỹ thuật
- Đã dịch đầy đủ 52/52 đoạn từ `p000849` đến `p000900`, giữ nguyên thứ tự và mã định danh (`segment_id`).
- Trường `"status"` của tất cả các dòng đã được cập nhật từ `"draft"` sang `"reviewed"` sau khi xử lý báo cáo review của Argon (`reviews/prose/vol-09/ch-05-b24-argon-review.yml`).
- Kiểm tra thẻ nhấn mạnh (`<em>` / `<i>`) theo `DEC-P01-002`:
  - `p000850`: Đánh dấu nghiêng mệnh đề thông điệp ngầm `*Chúng tôi đã có lòng thu xếp cho các vị một chuyến tàu về nước rồi đấy, thế nên cút đi cho khuất mắt.*` khớp với thẻ `<html:em>` trong nguồn.
  - `p000865`: Đánh dấu nghiêng đại từ chỉ định `*Đây*` trong câu kết khớp với thẻ `<html:em>` trong nguồn.
  - `p000886`: Đánh dấu nghiêng câu mở đầu `*Thế này thì không ổn rồi.*` khớp với thẻ `<html:em>` trong nguồn.
  - Toàn bộ 49 đoạn còn lại không có thẻ nhấn mạnh trong nguồn nên tuyệt đối không tự thêm dấu `*...*`.

## 2. Xưng hô, giọng điệu và mạch ngữ cảnh
- **Ngữ cảnh**: Tiếp nối trực tiếp `vol-09-ch-05-b23` trên khoang hạng nhất chuyến tàu quốc tế rời Ildoa về Đế quốc. Trung tá Tanya von Degurechaff dùng bữa sáng và uống cà phê thật trong khoang riêng cùng vị sĩ quan phụ tá là Trung úy Serebryakov, trò chuyện về sự trù phú yên bình của Ildoa rồi tặng lại số rượu vang biếu cho Serebryakov mang sang uống cùng Thiếu tá Weiss và mọi người trong đơn vị.
- **Độc thoại nội tâm & trần thuật (góc nhìn Tanya)**:
  - Khi tự quy chiếu ngôi thứ nhất trong nội tâm (`p000851`, `p000852`, `p000858`, `p000868`, `p000881`, `p000882`, `p000886`, `p000891`, `p000895`, `p000899`), Tanya xưng `mình` (hoặc `chúng ta` ở `p000851`, `p000852`, `p000853`, `p000858`, `p000869` khi chỉ chung bản thân cùng Serebryakov/đoàn Đế quốc).
  - Trong lời dẫn ngôi thứ ba hoặc khi cái tôi nội tâm tách biệt nhìn nhận hình thể Tanya (`p000853`, `p000869`, `p000870`, `p000875`, `p000877`, `p000879`, `p000889`, `p000890`, `p000891`), dùng thống nhất `Tanya` / `cô`.
  - Tham chiếu Trung úy Serebryakov trong trần thuật và nội tâm bằng `vị sĩ quan phụ tá`, `cô ấy`.
- **Đối thoại giữa Trung tá Tanya von Degurechaff và Trung úy Serebryakov**:
  - Tanya xưng `tôi` (hoặc `chúng ta` khi bao gồm cả hai ở `p000855`), gọi Serebryakov là `cô` / `Trung úy` / `Trung úy Serebryakov` (và `các vị` khi gộp chung Serebryakov, Thiếu tá Weiss cùng các sĩ quan cấp dưới ở `p000894`), giữ đúng chuẩn cấp trên lịch sự, điềm đạm như ở `ch-05-b06` và `ch-05-b07`.
  - Serebryakov xưng `tôi` (hoặc `chúng ta` ở `p000856`), gọi Tanya là `ngài` / `thưa Trung tá` / `Trung tá`, kèm tiểu từ kính ngữ `ạ` phù hợp với vai cấp dưới lễ phép, tận tụy.

## 3. Thuật ngữ, lựa chọn dịch thuật và xử lý Argon Review (`vol-09-ch-05-b24-translator-signoff`)
- **Xử lý findings từ `reviews/prose/vol-09/ch-05-b24-argon-review.yml`**:
  - `p000890` (`minor` - `explicitation`): Đã rút gọn cụm `để dùng làm đạn dược ngoại giao` thành `để dùng làm đạn dược` nhằm giữ đúng nhịp mở ẩn dụ sang `p000891`.
  - `p000891` (`minor` - `pronoun_consistency`): Đã chỉnh đại từ ngôi thứ ba chỉ Tanya ở cuối đoạn từ `cô bé` thành `cô` (`mà mình có thể giúp cô chạm tay tới`) để đồng nhất với đại từ `cô` ở `p000877`, `p000890`.
- **Bảo toàn `locked_choices` và `pending_term_recommendations`**:
  - Giữ nguyên 50/52 đoạn có `Touch: "preserve"` trong `locked_choices`.
  - Tuân thủ toàn bộ 5 nhóm `pending_term_recommendations` trong báo cáo review Argon.
- Áp dụng nhất quán các thuật ngữ đã có trong `canon/glossary.yml` và `work/run-state/pending-terms-index.yml`:
  - `người của Đế quốc` / `Đế quốc` / `đại sứ quán Đế quốc` (`p000849`, `p000851`, `p000872`)
  - `Ildoa` / `người Ildoa` (`p000851`, `p000852`, `p000867`, `p000869`, `p000874`, `p000883`, `p000890`, `p000892`)
  - `sĩ quan phụ tá` (`p000853`, `p000868`, `p000879`, `p000889`, `p000899`, `p000900`)
  - `toa ăn` (`p000855`)
  - `Trung úy` / `Trung úy Serebryakov` / `Serebryakov` (`p000857`, `p000860`, `p000875`, `p000887`, `p000895`)
  - `Thưa Trung tá` / `Trung tá` (gọi Trung tá Tanya von Degurechaff ở `p000859`, `p000880`, `p000888`, `p000896`)
  - `Đại tá Calandro` / `Calandro` (`p000868`, `p000890`)
  - `Tướng Igor Gassman`, `quỹ mật` (`p000869`, đồng bộ với `p000770` ở `ch-05-b21`)
  - `Bộ Tổng tham mưu` (`p000870`)
  - `Weiss` / `Thiếu tá Weiss` (`p000892`, `p000897`)
- Các thuật ngữ đề xuất mới (pending terms):
  - `conspicuous consumption` -> `tiêu dùng phô trương` (`p000855`)
  - `military administrator` -> `nhà quản lý quân chính` (`p000869`)
  - `hors d’oeuvres` -> `món khai vị` (`p000875`)
