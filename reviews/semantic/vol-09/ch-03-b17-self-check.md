# Báo cáo tự kiểm (Self-Check): `vol-09-ch-03-b17`

- **Task ID**: `vol-09-ch-03-b17` (`vol-09-ch-03-b17-translator-signoff`)
- **Translator**: `argon-low`
- **Phạm vi đoạn**: `YS-LN09/Text/chapter010.xhtml/p000660` .. `YS-LN09/Text/chapter010.xhtml/p000688` (29 đoạn)
- **Tệp đầu ra**: `translations/vol-09/ch-03-b17.jsonl`
- **Trạng thái dòng**: `reviewed` (29/29 dòng — đã sign-off theo `ch-03-b17-argon-review.yml`)

## 1. Kiểm tra tính đầy đủ và bảo toàn mã đoạn
- Toàn bộ 29 đoạn từ `p000660` đến `p000688` đã được dịch đầy đủ sang tiếng Việt, giữ nguyên thứ tự và mã định danh (`segment_id`).
- Các trường bắt buộc (`segment_id`, `translation`, `status`, `translator`, `glossary_version`, `source_sha256`, `notes`) đã được điền đầy đủ; `status` của toàn bộ 29 dòng đã được cập nhật từ `draft` sang `reviewed`.
- Không bỏ sót mệnh đề, câu văn hay chi tiết nội dung nào trong cả 29 đoạn.

## 2. Kiểm tra đại từ, điểm nhìn và giọng văn (`DEC-P01-001`)
- **Tự sự ngôi thứ ba chỉ Tanya**: Sử dụng đại từ `nó` nhất quán tại các đoạn có góc nhìn ngôi thứ ba (`p000670`, `p000671`, `p000674`, `p000680`, `p000687`).
- **Độc thoại nội tâm / tự sự ngôi thứ nhất của Tanya**: Sử dụng đại từ `mình` / `bọn mình` / `chúng ta` nhất quán (`p000669`, `p000671`, `p000672`, `p000677`, `p000681`, `p000685`), đặc biệt tại `p000671` khi câu văn chuyển đổi mượt mà từ ngôi thứ ba (`Nó đã bị phân tâm...`) sang ngôi thứ nhất (`đến chính mình cũng phải ngạc nhiên...`).
- **Lời thoại trực tiếp trên boong tàu của Tanya** (`p000676`, `p000679`): Dùng `mình` / `chúng ta` tự nhiên, thể hiện đúng giọng điệu mỉa mai, khô khan nhưng tỉnh táo của Tanya khi quan sát mặt biển và tiến độ hành quân.
- **Thuật ngữ và giọng điệu quân sự**: Giữ vững phong cách thực dụng, châm biếm nội tâm của Tanya đối với Kỹ sư trưởng Schugel, Xưởng Kỹ thuật và tư duy lục quân của Bộ Tổng tham mưu.

## 3. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002`)
- Đối chiếu toàn bộ thẻ nhấn mạnh trong `xhtml` nguồn:
  - `p000663`: Bảo toàn in nghiêng `*Cái quái gì thế này?*`.
  - `p000664`: Bảo toàn in nghiêng `*Mấy gã này mất trí cả rồi*` (thẻ neo trang không phải là nhấn mạnh).
  - `p000667`: Bảo toàn in nghiêng `*Các người định làm trò này thật đấy à?*`.
  - `p000668`: Bảo toàn in nghiêng `*thực sự*`.
  - `p000669`: Bảo toàn in nghiêng `*chúng nó*`.
  - `p000681`: Bảo toàn in nghiêng tên ngư lôi `*Aal*`.
  - `p000687`: Bảo toàn in nghiêng `*Các người bị ngu à?*`.
- Không tự ý thêm bất kỳ dấu `*...*` nào ở các đoạn không có thẻ nhấn mạnh trong nguồn.

## 4. Thuật ngữ Canon và Pending Terms
- Tuân thủ nghiêm ngặt `canon/glossary.yml` và các phương án đã thống nhất trong `work/run-state/pending-terms-index.yml`:
  - `Văn phòng Bộ Tổng tham mưu` / `Bộ Tổng tham mưu` (`p000683`, `p000685`)
  - `Khối Thịnh vượng chung` (`p000669`, `p000681`)
  - `Xưởng Kỹ thuật` (`p000665`, `p000667`)
  - `Kỹ sư trưởng Schugel` (`p000667`)
  - `pháp sư trên không` (`p000665`, `p000673`)
  - `tàu ngầm mẹ` (`p000664`)
  - `V-2` (`p000664`)
  - `Jabo` (`p000669`)
  - `nhân sự trực ban` (`p000675`)
  - `lũ Cộng sản`, `miền đông` / `Mặt trận phía đông` (`p000678`, `p000680`)
  - `Nội hải` (`p000680`)
  - `tìm và diệt` (`p000680`, `p000685`)
  - `*Aal*` (`p000681`)
  - `Hải quân Đế quốc Nhật Bản` (`p000682`, `p000684`)
- Các thuật ngữ chuyên ngành hải quân mới xuất hiện trong ngữ cảnh so sánh lịch sử của Tanya (`p000682`, `p000684`) được dịch rõ nghĩa, chuẩn xác theo thuật ngữ quân sự (`tàu ngầm hạm đội`, `Chiến lược đánh chặn`) và ghi nhận vào danh sách `pending_terms` của báo cáo điều phối.

## 5. Xử lý Argon Review Sign-off (`vol-09-ch-03-b17-translator-signoff`)
- **`YS-LN09/Text/chapter010.xhtml/p000662` (`minor` / `terminology_consistency`)**: Tiếp nhận theo khuyến nghị của Reviewer Argon, giữ nguyên thuật ngữ `hạm trưởng` (hoàn toàn chuẩn xác về mặt thuật ngữ hải quân để chỉ người chỉ huy tàu ngầm quân sự và phù hợp với `locked_choices` của `p000662`).
- **`YS-LN09/Text/chapter010.xhtml/p000671` (`minor` / `pronouns`)**: Tiếp nhận theo khuyến nghị của Reviewer Argon, giữ nguyên đại từ trần thuật ngôi thứ ba `nó` cho Tanya tại `p000671`, `p000674`, `p000687` theo đúng `DEC-P01-001`, tuân thủ `locked_choices` của các đoạn tương ứng và bảo đảm tính nhất quán với chuỗi lô `ch-03-b11` đến `ch-03-b16` liền trước.
- **`YS-LN09/Text/chapter010.xhtml/p000675` (`minor` / `style_redundancy`)**: Tiếp nhận khuyến nghị của Reviewer Argon, tinh giản cụm mở đầu từ `Điều gây hoang mang nhất hơn cả là` thành `Điều gây hoang mang hơn cả là` để câu văn tự nhiên, thoát ý và tránh trùng lặp dấu hiệu so sánh bậc nhất, đồng thời vẫn tuân thủ đầy đủ `locked_choices` của `p000675`.
- **Toàn bộ `pending_term_recommendations` và `locked_choices`**: Đã đối chiếu đầy đủ 12 mục thuật ngữ đề xuất và 29 mục `locked_choices`, xác nhận tuân thủ 100%.
- **Cập nhật trạng thái**: Đã chuyển trường `status` của toàn bộ 29/29 dòng trong `translations/vol-09/ch-03-b17.jsonl` từ `draft` sang `reviewed`.
