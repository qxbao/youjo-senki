# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-02-b20`

- **Task ID**: `vol-10-ch-02-b20`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter010.xhtml/p000331` đến `YS-LN10/Text/chapter010.xhtml/p000362` (32 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc
- Đã dịch đầy đủ 32/32 đoạn theo đúng thứ tự nguồn từ `p000331` đến `p000362`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter010.xhtml/p000331`: 1 cụm in nghiêng ở đầu câu.
  - `YS-LN10/Text/chapter010.xhtml/p000340`: 1 câu cảm thán in nghiêng ở giữa đoạn.
  - `YS-LN10/Text/chapter010.xhtml/p000342`: 2 cụm in nghiêng (câu hỏi độc thoại nội tâm và cụm nhấn mạnh ở cuối câu).
  - `YS-LN10/Text/chapter010.xhtml/p000346`: 1 câu hỏi độc thoại nội tâm in nghiêng ở đầu đoạn.
  - `YS-LN10/Text/chapter010.xhtml/p000358`: 2 cụm in nghiêng (độc thoại nội tâm về việc bị áp đảo và lời cảm thán cầu Chúa).
- Các đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.

## 2. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Trung tá Drake**:
  - Tự sự ngôi thứ ba gọi là `Trung tá Drake`, `Drake`, đại từ `anh` (nhất quán với `ch-02-b19`).
  - Độc thoại nội tâm của Drake tự xưng `mình` (`p000358`).
  - Khi nói thành tiếng hoặc ra lệnh và hô hào binh lính trong đơn vị (`p000335`, `p000339`, `p000344`, `p000347`, `p000350`, `p000355`): xưng `tôi`, gọi địch là `chúng`, câu lệnh ngắn, gấp gáp, dứt khoát đúng phong thái chỉ huy chiến trường đang chịu áp lực cực lớn.
- **Pháp sư Đế quốc**:
  - Dưới góc nhìn chiến trường của Drake: gọi chung hai pháp sư Đế quốc là `chúng`, gọi cá nhân pháp sư Đế quốc thấp bé đang áp sát là `đối phương` / `đối thủ` / `pháp sư Đế quốc thấp bé` / `pháp sư Đế quốc nhỏ con kia`.

## 3. Kiểm tra các cấu trúc ngữ pháp dễ lệch nghĩa
- **Cấu trúc bổ sung hai vế (`p000342`, `p000345`, `p000351`)**:
  - `YS-LN10/Text/chapter010.xhtml/p000342`: Giữ rõ hai vế tăng tiến (`chẳng những phản ứng chậm chạp mà lại còn đang *chờ lệnh*`).
  - `YS-LN10/Text/chapter010.xhtml/p000345`: Giữ rõ vế bổ sung (`Đã thế, đường đạn của họ còn loạn xạ khắp nơi`).
  - `YS-LN10/Text/chapter010.xhtml/p000351`: Giữ rõ hai vế (`chẳng những mất bình tĩnh mà còn hoàn toàn bất lực trong việc dồn một lượng hỏa lực đáng kể lên các mục tiêu`).
- **Cấu trúc giả định, phủ định và đối lập (`p000337`, `p000338`, `p000352`, `p000353`, `p000355`, `p000362`)**:
  - `YS-LN10/Text/chapter010.xhtml/p000337`: Bảo toàn giả định trái thực tế (`Bình thường Drake hẳn sẽ bật cười trước ý tưởng ấy nếu anh không phải đang đối đầu với một con ác quỷ theo đúng nghĩa đen`).
  - `YS-LN10/Text/chapter010.xhtml/p000338`: Bảo toàn quan hệ mức độ (`hầu như chẳng làm các pháp sư Đế quốc nao núng, chứ đừng nói đến chuyện cản bước chúng`).
  - `YS-LN10/Text/chapter010.xhtml/p000352`: Bảo toàn phủ định toàn phần đi kèm tình thái biểu kiến và đồng nhất thuật ngữ (`hỏa lực chế áp dường như không hề ảnh hưởng gì đến sự tự do cơ động của kẻ địch`).
  - `YS-LN10/Text/chapter010.xhtml/p000355`: Bảo toàn giả định tiếc nuối (`Lý tưởng nhất là anh đã có thể tận dụng lợi thế sải tay để tung đòn trước, nhưng pháp sư Đế quốc nhỏ con kia đã áp sát quá gần`).
  - `YS-LN10/Text/chapter010.xhtml/p000362`: Bảo toàn sự đối lập hai chiều ở cự ly cực gần mà không tự thu hẹp phương thức hành động (`Với sự chênh lệch về vóc dáng và vị trí hiện tại, pháp sư Đế quốc thấp bé kia nắm trọn ưu thế. Ngược lại, khoảng cách ngăn giữa hai người ngắn đến mức anh cũng không tài nào trượt mục tiêu được`).

## 4. Thuật ngữ đã áp dụng và đề xuất (`pending_terms`)
- Các thuật ngữ kế thừa nhất quán từ `canon/` và `work/run-state/pending-terms-index.yml`:
  - `Trung tá Drake` / `Drake`
  - `màn chắn bảo hộ` / `lớp vỏ phòng thủ`
  - `hệ thống chỉ huy`
  - `đòn tập kích chặt đầu chỉ huy`
  - `Ác quỷ sông Rhine`
  - `đơn vị tình nguyện đa quốc gia` / `binh lính đa quốc gia`
  - `thuật thức phát nổ`
  - `các pháp sư Đế quốc` / `pháp sư Đế quốc`
  - `hỏa lực chế áp`
  - `mồi nhử`
  - `mặt trận Rhine`
  - `lưỡi kiếm ma pháp`
- Thuật ngữ tổ hợp ghi nhận bổ sung:
  - `thuật thức ngụy trang quang học` (`YS-LN10/Text/chapter010.xhtml/p000341`, `YS-LN10/Text/chapter010.xhtml/p000348`): kết hợp nhất quán quy chuẩn `thuật thức quang học` trong `canon/glossary.yml` với nghĩa ngụy trang/tạo mồi nhử ảo ảnh trong ngữ cảnh.

## 5. Xử lý Argon Review Sign-off (`vol-10-ch-02-b20-translator-signoff`)
- `YS-LN10/Text/chapter010.xhtml/p000339`: Tiếp nhận finding về phân biệt đại từ trong thoại với độc thoại nội tâm theo `DEC-P01-001`, chỉnh thành `“Chúng định lao thẳng vào tôi sao?!”`.
- `YS-LN10/Text/chapter010.xhtml/p000352`: Tiếp nhận finding về phủ định toàn phần và đồng nhất thuật ngữ `hỏa lực chế áp` với `p000344`, chỉnh thành `hỏa lực chế áp dường như không hề ảnh hưởng gì đến sự tự do cơ động của kẻ địch`.
- `YS-LN10/Text/chapter010.xhtml/p000362`: Tiếp nhận finding về không tự thu hẹp phương thức hành động ở cảnh cận chiến, chỉnh thành `anh cũng không tài nào trượt mục tiêu được`.
- Đã đối chiếu toàn bộ `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-10/ch-02-b20-argon-review.yml`, đồng thời cập nhật `status` của cả 32 dòng trong `translations/vol-10/ch-02-b20.jsonl` từ `draft` sang `reviewed`.
