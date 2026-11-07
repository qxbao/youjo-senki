# Báo cáo tự kiểm (Self-Check): `vol-09-ch-04-b01` (Translator Sign-off)

## 1. Phạm vi & tính đầy đủ
- **Task ID**: `vol-09-ch-04-b01-translator-signoff` (parent: `vol-09-ch-04-b01`)
- **Số đoạn**: 38 đoạn (`YS-LN09/Text/chapter014.xhtml/p000001` đến `YS-LN09/Text/chapter014.xhtml/p000038`).
- **Trạng thái**: Tất cả 38 dòng trong `translations/vol-09/ch-04-b01.jsonl` đã được cập nhật sang `"status": "reviewed"`, giữ nguyên thứ tự `segment_id`, khớp `source_sha256` và `glossary_version` trong handoff.
- Không bỏ sót câu, mệnh đề, thông tin quân sự, chỉ dẫn thời gian/địa điểm hoặc chi tiết chuyển cảnh nào.

## 2. Xử lý các Findings trong Argon Review (`ch-04-b01-argon-review.yml`)
- **`YS-LN09/Text/chapter014.xhtml/p000003` (minor - `style_pronoun_agreement`)**: Đã sửa đại từ quy chiếu ở mệnh đề sau từ `chúng` thành `nó` (`nhưng nó vẫn phát huy tác dụng rất tốt khi đối phó với thiết giáp hạm`) để thống nhất số ít với cụm danh từ chủ ngữ `Chiến thuật bầy sói này`, đồng thời giữ trọn `locked_choices`.
- **`YS-LN09/Text/chapter014.xhtml/p000029` (minor - `pronouns`)**: Giữ nguyên đại từ trần thuật ngôi thứ ba `nó` quy chiếu Tanya theo sát `DEC-P01-001` và đúng `locked_choices` của đoạn `p000029`, `p000037` trong báo cáo review.
- **`YS-LN09/Text/chapter014.xhtml/p000031` (minor - `meaning_nuance`)**: Đã khôi phục chủ ngữ danh từ `sự cấp thiết` theo khuyến nghị của reviewer (`Nhưng sự cấp thiết vốn là mẹ đẻ của phát minh, là người bảo trợ cho sự đổi mới bắt buộc, và suy cho cùng, chính là cái thứ cực kỳ gai góc mang tên mệnh lệnh từ sĩ quan cấp trên.`), bảo đảm cấu trúc ba vị ngữ đẳng lập rõ ràng và tuân thủ `locked_choices`.

## 3. Xưng hô & Điểm nhìn (`DEC-P01-001`)
- **Độc thoại nội tâm & tự thuật ngôi thứ nhất của Tanya** (`p000019`, `p000020`, `p000023`, `p000030`, `p000031`): dùng `mình` / `bọn mình` tự nhiên, giữ đúng chất thực dụng, sắc sảo và đôi chút châm biếm của Tanya khi bàn về chiến thuật tàu ngầm cũng như mệnh lệnh từ cấp trên.
- **Trần thuật ngôi thứ ba về Tanya** (`p000014`, `p000026`, `p000029`, `p000032`, `p000034`, `p000037`, `p000038`): dùng tên `Tanya` hoặc đại từ `nó` (`p000029`, `p000037`), thống nhất với quy ước `DEC-P01-001` và các lô trước của tập 9.
- **Đối thoại**:
  - Giữa các thủy thủ trong phòng điều khiển tàu ngầm (`p000006`–`p000011`): câu khẩu lệnh và báo cáo ngắn gọn, khẩn trương, đúng không khí tác chiến trên tàu ngầm.
  - Giữa Thuyền trưởng Barchet và Trung tá Tanya von Degurechaff (`p000016`–`p000018`, `p000021`, `p000022`, `p000024`–`p000028`, `p000032`, `p000033`): Barchet gọi Tanya là `Trung tá Degurechaff` / `cô`, tự xưng `tôi` / `chúng tôi`; Tanya gọi Barchet là `Thuyền trưởng` / `ngài`, tự xưng `tôi` / `chúng ta`, giữ đúng sắc thái lịch sự giữa sĩ quan ma pháp đi nhờ tàu và hạm trưởng tàu ngầm hải quân đã thiết lập ở chương 3.
  - Giữa Trung úy Serebryakov và Tanya (`p000035`–`p000037`): Serebryakov gọi `thưa Trung tá`; Tanya gọi `Trung úy`, xưng `chúng ta` với thuộc cấp cùng xuất kích.

## 4. Bảo toàn nhấn mạnh (`DEC-P01-002`)
- Chỉ duy nhất đoạn `YS-LN09/Text/chapter014.xhtml/p000037` có thẻ nhấn mạnh trong XHTML gốc và đã được bảo toàn chính xác bằng dấu sao đơn `*Và đó là lý do…*`.
- Các thẻ neo trang ở `p000021` và `p000037` là thẻ đánh dấu vị trí trang, không phải nhấn mạnh nên không sinh dấu `*...*`.
- Tất cả 37 đoạn còn lại không có nhấn mạnh trong nguồn và bản dịch hoàn toàn không tự ý thêm dấu `*...*`.

## 5. Thuật ngữ Canon & Pending (`pending_term_recommendations` & `locked_choices`)
- Đã kiểm tra và tuân thủ toàn bộ 11 mục `pending_term_recommendations` và 38 mục `locked_choices` trong `ch-04-b01-argon-review.yml`:
  - `NGÀY 15 THÁNG 7 NĂM THỐNG NHẤT 1927, MẶT TRẬN NỘI HẢI` (`p000001`)
  - `chiến thuật bầy sói`, `tàu buôn`, `thiết giáp hạm`, `đoàn tàu có hộ tống` (`p000002`, `p000003`, `p000010`)
  - `hải đội`, `tàu bạn trong hải đội`, `sonar`, `chân vịt`, `ngư lôi`, `phòng điều khiển`, `những người lính tàu ngầm` (`p000005`–`p000007`, `p000009`, `p000011`, `p000012`, `p000014`)
  - `Thuyền trưởng Barchet` / `Barchet` / `vị thuyền trưởng` / `Thuyền trưởng` (`p000013`, `p000015`, `p000023`, `p000026`, `p000029`, `p000032`, `p000034`)
  - `Trung tá Degurechaff` / `thưa Trung tá` (`p000016`, `p000035`)
  - `V-2`, `mẫu V-1` (`p000018`, `p000037`)
  - `Norden` (`p000026`)
  - `sĩ quan ma pháp` (`p000029`)
  - `Nữ thần May mắn` (`p000032`)
  - `Quân đoàn Viễn chinh Lục địa Phía nam` (`p000033`)
  - `Trung úy Serebryakov` / `Trung úy` (`p000034`, `p000036`)
