# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-04-b21`

- **Task ID**: `vol-10-ch-04-b21`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter022.xhtml/p000521` đến `YS-LN10/Text/chapter022.xhtml/p000566` (46 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc
- Đã dịch đầy đủ 46/46 đoạn theo đúng thứ tự nguồn từ `p000521` đến `p000566`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 46 dòng đã được cập nhật từ `draft` sang `reviewed` sau khi xử lý đầy đủ review của Argon.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `p000539`: `*công việc thường nhật có độ căng thẳng cao*`
  - `p000543`: `*một bóng ma đã giáng xuống vùng eo biển*`
  - `p000563`: `*trực tiếp*`
  - Các đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` và bản dịch không tự thêm dấu `*...*`.

## 2. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Điểm nhìn nội tâm ngôi thứ nhất và độc thoại tự nói một mình của Tanya (`p000521` – `p000534`)**:
  - Tự xưng `mình` nhất quán theo `DEC-P01-001` cả trong suy nghĩ nội tâm lẫn khi tự lẩm bẩm một mình trong phòng riêng (`p000523`, `p000527`, `p000531`), nối tiếp trực tiếp mạch độc thoại từ cuối lô `ch-04-b20`.
  - Giữ cách tự quy chiếu ngôi thứ ba khách quan của Tanya (`Tanya`, `Tanya von Degurechaff`) tại `p000522` và `p000526`, cùng đại từ khái quát `chúng ta` khi nói về quyền tự nhiên của con người tại `p000526`.
  - Gọi `Being X` là `tên Being X kia` / `hắn` (`p000527`) để thể hiện đúng thái độ bức xúc của Tanya.
- **Trần thuật ngôi thứ ba và lời thoại phía Khối Thịnh vượng chung (`p000535` – `p000566`)**:
  - Tiêu đề chuyển cảnh tại `p000535` được viết hoa toàn bộ (`CÙNG NGÀY HÔM ĐÓ, TRÊN BẦU TRỜI EO BIỂN`).
  - Tại `p000544`, Tanya phát lệnh qua vô tuyến bằng hô hiệu `Fairy 01` tới toàn đơn vị, giữ giọng mệnh lệnh quân sự ngắn gọn, dứt khoát.
  - Phía lực lượng phòng không và đài kiểm soát không lưu của Khối Thịnh vượng chung: trần thuật gọi chung các binh sĩ, kiểm soát viên và sĩ quan trực ban là `họ`, gọi riêng trưởng đài kiểm soát không lưu là `ông` (`p000560`, `p000563`); trong lời thoại báo động và chỉ huy (`p000549`, `p000552`, `p000554`, `p000558`, `p000561`, `p000562`, `p000564`, `p000566`), các nhân viên và sĩ quan xưng `tôi` / `chúng ta`, gọi quân Đế quốc là `chúng` / `kẻ địch` / `quân địch`, giữ nguyên nét lắp bắp hoảng loạn `Á-Ác quỷ sông Rhine!` tại `p000561`.

## 3. Kiểm tra nghĩa, logic và quan hệ nhân quả
- **`p000522`**: Bảo toàn đối lập giữa việc làm vì nghĩa vụ công việc với sự thật không thể phủ nhận là bản thân đã trở nên hết sức chủ quan trước toàn bộ chuyện này, cùng câu hỏi tự vấn về việc biến thành nô lệ của sự cấp thiết.
- **`p000539`**: Giữ đúng cấu trúc điều kiện hoàn thành chỉ bối cảnh thực tế khi cục diện Trận Không chiến Phương Tây đã nghiêng về phía có lợi cho Khối Thịnh vượng chung, khiến việc đối phó với máy bay trinh sát và các đợt ném bom quấy rối ban đêm lẻ tẻ của Đế quốc trở thành công việc thường nhật có độ căng thẳng cao.
- **`p000550`**: Giữ rõ sự tương phản giữa việc tấn công ban đêm nhưng lại phát tín hiệu ma lực sáng rực như ngọn hải đăng, đi ngược hoàn toàn thông lệ phải luôn ẩn mình trong học thuyết của pháp sư trên không.
- **`p000563`**: Giữ đúng sự đối lập giữa những người trong phòng kiểm soát chưa từng trực tiếp chạm trán Pháp sư Định danh kia (chỉ biết nhìn trân trối) với trưởng đài kiểm soát không lưu và các sĩ quan trực ban khác (đồng loạt đá văng ghế lao tới máy bộ đàm vô tuyến).

## 4. Thuật ngữ đã tra cứu và đề xuất tạm (Pending Terms)
- Kế thừa nhất quán từ `pending-terms-index.yml` và các lô trước của `vol-10`:
  - `Being X` (`p000527`)
  - `Nữ thần May mắn` (`p000536`)
  - `Trận Không chiến Phương Tây` (`p000539`)
  - `Khối Thịnh vượng chung` (`p000539`, `p000546`, `p000551`, `p000555`)
  - `Đế quốc` (`p000539`, `p000545`)
  - `Fairy 01` (`p000544`)
  - `tín hiệu ma lực` (`p000549`, `p000559`)
  - `pháp sư trên không` (`p000550`, `p000556`)
  - `sĩ quan trực ban` (`p000553`, `p000563`)
  - `Ác quỷ sông Rhine` (`p000561`, `p000562`, `p000566`)
  - `Pháp sư Định danh` (`p000563`, `p000566`)
- Ghi nhận các cách diễn đạt đề xuất tạm trong lô này (không tự nâng thành canon):
  - `quyền mưu cầu hạnh phúc` (`p000526` — phương án khác: `quyền theo đuổi hạnh phúc`)
  - `CÙNG NGÀY HÔM ĐÓ, TRÊN BẦU TRỜI EO BIỂN` / `eo biển` / `vùng eo biển` (`p000535`, `p000536`, `p000543` — đồng bộ với cách dịch tại Chương 3 Tập 10)
  - `bộ phận phòng không` (`p000541` — phương án khác: `ban phòng không`)
  - `phương ngữ Đế quốc chuẩn mực` (`p000545` — phương án khác: `tiếng Đế quốc tiêu chuẩn`)
  - `đài kiểm soát không lưu` / `kiểm soát viên không lưu` / `trưởng đài kiểm soát không lưu` (`p000546`, `p000560`, `p000563` — phương án khác: `bộ phận kiểm soát không lưu` / `trưởng ban kiểm soát không lưu`)
  - `khu vực kiểm soát đánh chặn phía nam` (`p000548` — phương án khác: `vùng kiểm soát đánh chặn phía nam`)
  - `đội phản ứng nhanh` (`p000554` — phương án khác: `toán phản ứng nhanh`)
  - `Trung đoàn 3` (`p000556` — phương án khác: `Trung đoàn số 3`)
  - `khu vực tác chiến` (`p000564` — phương án khác: `AO`)

## 5. Xử lý Argon Review Sign-off (`vol-10-ch-04-b21-translator-signoff`)
- **`p000546` (minor)**: Đổi `sự hiện diện của họ` thành `sự hiện diện của chúng` để quy chiếu liền mạch với hình ảnh `một bầy quái vật` ở cuối `p000545` và khớp với điểm nhìn cảnh giác của phía Khối Thịnh vượng chung; vẫn giữ nguyên `máy móc của họ` ở câu thứ hai theo đúng `locked_choices`.
- **`p000559` (minor)**: Đổi `danh tính kẻ địch` thành `danh tính mục tiêu` để tránh lặp từ sát nhau với `tín hiệu ma lực của địch` trong cùng câu ngắn.
- **`p000563` (minor)**: Bỏ từ chỉ loại mang sắc thái kính trọng `vị` trong `vị Pháp sư Định danh kia`, chỉnh thành `Pháp sư Định danh kia` để phù hợp với tâm lý kinh hoàng của các nhân viên phòng kiểm soát Khối Thịnh vượng chung.
- Bảo toàn toàn bộ `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-10/ch-04-b21-argon-review.yml`.
- Cập nhật `status` của toàn bộ 46 dòng trong `translations/vol-10/ch-04-b21.jsonl` sang `reviewed`.
