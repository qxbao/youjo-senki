# Báo cáo tự kiểm (Self-Check): `vol-08-ch-03-b06`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-03-b06`
- **Phạm vi**: `YS-LN08/Text/chapter010.xhtml/p000155` → `YS-LN08/Text/chapter010.xhtml/p000190` (36 đoạn)
- **Tác tử**: `argon-low`
- **Tệp đầu ra**: `translations/vol-08/ch-03-b06.jsonl`

## 2. Kiểm tra tính đầy đủ & cấu trúc kỹ thuật
- Đã dịch đủ 36/36 đoạn theo đúng thứ tự và khớp hoàn toàn `segment_id` với tệp nguồn.
- Không tách dòng, không gộp đoạn, không bỏ sót bất kỳ câu hoặc mệnh đề nào.
- Trường `status` của toàn bộ 36 dòng đã được cập nhật từ `"draft"` sang `"reviewed"` sau khi hoàn tất sign-off theo `reviews/prose/vol-08/ch-03-b06-argon-review.yml` (0 lỗi, tuân thủ đầy đủ `locked_choices` và `pending_term_recommendations`).
- Đã sửa từ Hán tự bị lẫn ở mục 3 của báo cáo tự kiểm sang tiếng Việt chuẩn (`quân kỷ`).
- Trường `glossary_version` và `source_sha256` khớp chính xác với thông tin trong `handoffs/vol-08/ch-03-b06.yml`.
- Bảo toàn chính xác thẻ nhấn mạnh theo quy định `DEC-P01-002`: không có đoạn nào trong lô này chứa thẻ nhấn mạnh trong nguyên bản, nên bản dịch hoàn toàn không tự ý thêm dấu `*...*`.

## 3. Kiểm tra thuật ngữ, danh xưng & giọng văn
- **Thuật ngữ chuẩn và đề xuất đã đối chiếu**:
  - `front lines` / `the rear`: tiền tuyến (`p000156`) / hậu phương (`p000184`)
  - `Major Weiss`: Thiếu tá Weiss (`p000157`, `p000171`)
  - `Captain Meybert`: Đại úy Meybert (`p000157`)
  - `Lieutenant Serebryakov` / `First Lieutenant Serebryakov`: Trung úy Serebryakov (`p000157`, `p000164`, `p000171`, `p000175`)
  - `marshaling point`: điểm tập kết (`p000159`)
  - `First Lieutenant Grantz`: Trung úy Grantz (`p000161`)
  - `First Lieutenant Wüstemann` / `Lieutenant Wüstemann`: Trung úy Wüstemann (`p000161`, `p000171`, `p000186`)
  - `Commies`: đám Cộng sản (`p000167`)
  - `Being X`: Being X (`p000167`)
  - `Heinrich’s Law`: Định luật Heinrich (`p000169`)
  - `the Rhine`: mặt trận Rhine (`p000171`)
  - `Nightingale` / `Crimea`: Nightingale / Crimea (`p000180`, `p000181`)
  - `human capital`: vốn con người (`p000180`, `p000181`) — khớp với `P03-human-capital` trong `canon/glossary-pending.yml`
  - `replacement company`: đại đội bổ sung (`p000185`)
  - `First Lieutenant Tospan`: Trung úy Tospan (`p000189`)
- **Xưng hô và giọng nhân vật**:
  - Ngôi kể thứ ba gọi Tanya và Serebryakov là `cô`, gọi Weiss và Wüstemann là `anh` / `anh ta`.
  - Trong độc thoại nội tâm (`p000165`, `p000166`, `p000167`, `p000174`, `p000180`, `p000184`), Tanya tự xưng `mình` (và dùng `bạn` cho chủ thể giả định chung ở `p000160`, `p000180`), giữ rõ nét giọng điệu lý tính, thực dụng và coi trọng quy chuẩn văn minh cũng như quản trị nhân sự.
  - Trong đối thoại, Tanya xưng `tôi` / `chúng tôi` / `chúng ta`, gọi Weiss là `Thiếu tá Weiss` / `anh`, gọi Meybert là `Đại úy Meybert` / `anh`, gọi Serebryakov là `Trung úy Serebryakov` / `cô`, gọi Wüstemann là `Trung úy Wüstemann` / `anh`, và gọi binh sĩ toàn tiểu đoàn là `Các binh sĩ` / `các anh`.
  - Cấp dưới (Weiss, Serebryakov, Wüstemann) xưng `tôi`, gọi Tanya là `thưa Trung tá` / `Trung tá` với thái độ nghiêm túc, đúng quân kỷ.

## 4. Điểm cần lưu ý cho bước duyệt tiếp theo
- Thuật ngữ mới ghi nhận bổ sung vào danh sách chờ xét: `Heinrich’s Law` → `Định luật Heinrich` (`p000169`) và `Nightingale` / `Crimea` → `Nightingale` / `Crimea` (`p000180`, `p000181`).
- Không có vấn đề ngữ nghĩa hay xưng hô nào gây tắc nghẽn.
