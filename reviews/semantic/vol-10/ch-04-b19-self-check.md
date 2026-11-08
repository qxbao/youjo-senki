# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-04-b19`

- **Task ID**: `vol-10-ch-04-b19-translator-signoff` (parent: `vol-10-ch-04-b19`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter022.xhtml/p000434` đến `YS-LN10/Text/chapter022.xhtml/p000480` (47 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc (Sign-off)
- Đã dịch và rà soát đầy đủ 47/47 đoạn theo đúng thứ tự nguồn từ `p000434` đến `p000480`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 47 dòng đã được cập nhật từ `draft` sang `reviewed` theo đúng quy trình sign-off.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter022.xhtml/p000446`: `*nghĩ*`
  - `YS-LN10/Text/chapter022.xhtml/p000466`: `*bản thổ Khối Thịnh vượng chung*`
- Tất cả 45 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.

## 2. Xử lý các findings từ `ch-04-b19-argon-review.yml` và tuân thủ `locked_choices`
- Toàn bộ `locked_choices` từ `p000434` đến `p000480` và tất cả 11 mục `pending_term_recommendations` trong `reviews/prose/vol-10/ch-04-b19-argon-review.yml` đều được bảo toàn nghiêm ngặt.
- Tiếp nhận và xử lý đầy đủ 3 minor findings có căn cứ trong báo cáo review của Argon:
  - `YS-LN10/Text/chapter022.xhtml/p000447`: Thay đại từ `họ` bằng `phe ta` (`khiến chúng tưởng rằng phe ta đang cố buộc chúng phải rút bớt quân khỏi tiền tuyến`) để phân tách rõ chủ thể với `chúng` mà không lặp từ `Đế quốc` ở đầu câu.
  - `YS-LN10/Text/chapter022.xhtml/p000465`: Chỉnh `khi những đôi giày ủng da ấy đặt chân lên mặt đất` thành `khi những đôi giày ủng da ấy giẫm lên mặt đất` để kết hợp từ tự nhiên hơn với chủ ngữ chỉ vật.
  - `YS-LN10/Text/chapter022.xhtml/p000473`: Chỉnh cụm thứ hai từ `lại làm mình bất ngờ` thành `lại làm mình không kịp trở tay` để tránh lặp từ `bất ngờ` ở câu liền trước và thể hiện rõ sắc thái không lường trước được phản ứng của Visha.

## 3. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Điểm nhìn nội tâm ngôi thứ nhất của Tanya (`p000434`, `p000436`, `p000438`, `p000439`, `p000441`, `p000444`, `p000445`, `p000447`, `p000449`, `p000451`, `p000454`, `p000457`, `p000459`, `p000462` – `p000466`, `p000468`, `p000471`, `p000473`, `p000477`, `p000478`)**:
  - Tự xưng `mình` nhất quán theo `DEC-P01-001`; dùng `chúng ta` / `phe ta` khi quy chiếu chung về Tiểu đoàn 203/phe Đế quốc (`p000434`, `p000447`, `p000465`).
  - Gọi Thiếu tá Weiss là `vị phó chỉ huy` / `Thiếu tá Weiss` / `anh ta` (`p000441`, `p000451`, `p000454`, `p000462`, `p000464`, `p000468`, `p000473`), gọi Trung úy Serebryakov là `Trung úy Serebryakov` / `Visha` / `viên sĩ quan phụ tá` / `cô ấy` (`p000451`, `p000464`, `p000471`, `p000473`, `p000477`), và gọi các sĩ quan/binh sĩ thuộc quyền là `họ` / `bọn họ` (hoặc `tất cả các người` trong câu hỏi nội tâm hướng tới nhóm sĩ quan ở `p000473`).
- **Diễn văn phổ biến nhiệm vụ trước toàn tiểu đoàn và đối thoại với các sĩ quan (`p000435`, `p000437`, `p000440`, `p000442`, `p000443`, `p000446`, `p000448`, `p000450`, `p000452`, `p000453`, `p000455`, `p000456`, `p000458`, `p000460` – `p000462`, `p000467`, `p000469`, `p000470`, `p000472`, `p000474` – `p000476`, `p000479`, `p000480`)**:
  - Tanya xưng `tôi` và `chúng ta`, gọi chung cấp dưới là `các vị` / `các chiến hữu`, gọi riêng Thiếu tá Weiss là `Thiếu tá Weiss` / `Thiếu tá` / `anh` và Trung úy Serebryakov là `Trung úy Serebryakov` / `cô`.
  - Thiếu tá Weiss và Trung úy Serebryakov xưng `tôi` / `chúng ta`, gọi Tanya là `thưa Trung tá` / `Trung tá` kèm tiểu từ lễ phép `ạ`, thể hiện đúng thái độ tôn kính của cấp dưới nhưng không giấu được sự bàng hoàng trước tính chất táo bạo của kế hoạch đổ bộ lên bản thổ Khối Thịnh vượng chung.

## 4. Thuật ngữ đã áp dụng và đề xuất (`pending_terms`)
- Khớp đầy đủ với `pending_term_recommendations` trong `ch-04-b19-argon-review.yml`:
  - `trinh sát chiến đấu` (`p000437`, `p000438`)
  - `đại đội` (`p000437`)
  - `Khối Thịnh vượng chung` / `*bản thổ Khối Thịnh vượng chung*` (`p000437`, `p000447`, `p000460`, `p000461`, `p000465`, `p000466`)
  - `hệ thống phòng không` (`p000437`)
  - `công tác phản gián` / `những quả trứng ung` (`p000440`, `p000442`, `p000446`)
  - `vị phó chỉ huy` / `Thiếu tá Weiss` / `Thiếu tá` (`p000441`, `p000443`, `p000451`, `p000452`, `p000464`, `p000468`, `p000473`)
  - `Trận Không chiến Phương Tây` (`p000443`)
  - `ưu thế trên không` (`p000448`)
  - `Trung úy Serebryakov` / `Visha` / `viên sĩ quan phụ tá` (`p000451`, `p000464`, `p000471`, `p000473`, `p000476`, `p000477`)
  - `Tướng Romel` (`p000465`)
  - `chiến tranh tổng lực` (`p000473`, `p000479`)
