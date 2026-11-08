# Báo cáo tự kiểm (Translator Self-Check & Sign-off) — `vol-10-ch-04-b22`

- **Task ID**: `vol-10-ch-04-b22-translator-signoff` (Parent: `vol-10-ch-04-b22`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter022.xhtml/p000567` đến `YS-LN10/Text/chapter022.xhtml/p000609` (43 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ, trạng thái Sign-off và bảo toàn cấu trúc
- Đã dịch và rà soát đầy đủ 43/43 đoạn theo đúng thứ tự nguồn từ `p000567` đến `p000609`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 43 dòng trong `translations/vol-10/ch-04-b22.jsonl` đã được cập nhật từ `draft` sang `reviewed`.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `p000573`: `*đã giao chiến*`
  - `p000579`: `*Chúng ta phải chặn đứng chúng lại.*`
  - `p000581`: `*Không thể nào.*`
  - `p000590`: `*Lại thêm tin xấu nữa ư?*`
  - `p000596`: `*Ác quỷ sông Rhine*`, `*ác mộng*`
  - Các đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` và bản dịch không tự thêm dấu `*...*`.

## 2. Xử lý Findings và Pending Term Recommendations từ Argon Review
- **`p000567` (`minor`)**: Đã tiếp nhận và chỉnh từ `máy bộ đàm vô tuyến` thành `máy bộ đàm` ở câu đầu để tránh lặp cụm từ `vô tuyến` sát nhau ở câu thứ hai (`các tần số vô tuyến`), giúp nhịp văn cô đọng và tự nhiên hơn.
- **`p000569` (`minor`)**: Đã tiếp nhận và chỉnh cụm `đang tìm cách càn lướt mở đường máu xuyên qua!` thành `đang tìm cách càn lướt đột phá xuyên qua!`, phản ánh chính xác sắc thái đại đội Pháp sư Định danh của Đế quốc đang áp đảo và cậy sức mạnh xuyên thủng tuyến phòng không.
- **`p000583` (`minor`)**: Đã tiếp nhận và chỉnh cụm `Lũ chó săn Đế quốc khốn kiếp!` thành `Lũ chó Đế quốc khốn kiếp!`, giữ đúng sắc thái lời chửi nhắm trực tiếp vào quân Đế quốc.
- **Pending Term Recommendations & Locked Choices**: Đã kiểm tra và bảo đảm tuân thủ đầy đủ toàn bộ `pending_term_recommendations` và `locked_choices` từ `p000567` đến `p000609` trong `reviews/prose/vol-10/ch-04-b22-argon-review.yml`.

## 3. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Trần thuật ngôi thứ ba và điểm nhìn phía phòng kiểm soát của Khối Thịnh vượng chung (`p000567` – `p000609`)**:
  - Nối tiếp trực tiếp mạch cảnh từ cuối lô `ch-04-b21` (`p000566`): người phát cảnh báo qua máy bộ đàm và vị sĩ quan chỉ huy/phụ trách tại phòng kiểm soát được gọi là `ông` (`p000567`, `p000596`), tập thể các sĩ quan trực ban, nhân viên vận hành và lực lượng phòng không Khối Thịnh vượng chung được gọi là `họ`.
  - Trong lời thoại vô tuyến từ đội tuần tra đang bị tấn công (`p000568` – `p000570`): người báo tin xưng `chúng tôi`, gọi các pháp sư Đế quốc là `chúng`, giữ đúng nhịp cầu cứu dồn dập và câu báo cáo bị cắt ngang ở `p000570` (`Chỉ huy bị bắn hạ rồi! Chỉ huy bị—`).
  - Trong lời thoại tại phòng kiểm soát và trung tâm chỉ huy (`p000573` – `p000607`): các sĩ quan và nhân viên vận hành xưng `tôi` / `chúng ta`, gọi nhau là `anh` (`p000589`) hoặc `các anh` khi phát cảnh báo cho Tiểu đoàn Whiskey (`p000604`); gọi quân Đế quốc là `địch` / `quân địch` / `kẻ địch` / `chúng` / `lũ chó Đế quốc`.
  - Trong độc thoại nội tâm chung hoặc của sĩ quan chỉ huy tại phòng kiểm soát (`p000579`, `p000581`, `p000590`, `p000596`, `p000598`, `p000599`): dùng `chúng ta` cho quyết tâm chung của sở chỉ huy (`p000579`) và `mình` cho nhận thức nội tâm của vị sĩ quan (`p000596`).

## 4. Kiểm tra nghĩa, logic và quan hệ nhân quả
- **`p000567`**: Bảo toàn quan hệ đối lập giữa nỗ lực phát thông điệp khẩn cấp qua sóng vô tuyến với thực tế là mọi chuyện đã quá muộn khi tiếng gào thét của đội tuần tra trên không đã vang vọng khắp bầu trời đêm.
- **`p000572`**: Giữ đúng mức độ nhấn mạnh (nói vùng eo biển rơi vào hỗn loạn đêm đó vẫn còn là nói giảm nói tránh) và sự tương phản giữa quy tắc giữ bình tĩnh chuyên nghiệp thường ngày của phòng kiểm soát với cảnh vị sĩ quan chỉ huy gào thét văng cả nước bọt giữa vòng xoáy hỗn loạn.
- **`p000585` – `p000589`**: Giữ rõ mạch suy luận về tác chiến điện tử: chỉ huy yêu cầu dò tìm tín hiệu dẫn đường điện tử của Đế quốc để đoán mục tiêu và nhắc đừng mắc lừa tín hiệu mồi nhử, nhưng nhân viên báo cáo vấn đề không phải ở mồi nhử mà là hoàn toàn không có tín hiệu nào phát ra từ đài kiểm soát tuyến của địch.
- **`p000591` – `p000595`**: Bảo toàn diễn tiến sụp đổ cực nhanh của lực lượng phản ứng nhanh tinh nhuệ: chỉ huy của phân đội Argyle bị hạ, phân đội Carbene xin chi viện khẩn, rồi ngay sau đó Carbene xác nhận Argyle đã bị xóa sổ hoàn toàn chỉ sau vài phút vừa chạm trán.
- **`p000600` – `p000607`**: Giữ chính xác diễn biến cơ động chiến thuật: pháp sư địch xuyên thủng không vực mười hai khi Tiểu đoàn Whiskey đang tới tuyến đánh chặn số hai, sau đó toán địch ở không vực mười hai quay đầu lại hội quân với toán ở không vực mười sáu để nhắm vào Tiểu đoàn Whiskey; phòng kiểm soát lập tức cảnh báo Whiskey, đồng thời Tiểu đoàn Scotch cất cánh tiếp ứng và rút ngắn thời gian dự kiến tới nơi từ bốn trăm giây xuống còn 360 giây.

## 5. Thuật ngữ đã tra cứu và đề xuất tạm (Pending Terms)
- Kế thừa nhất quán từ `pending-terms-index.yml`, lô `ch-04-b21` và khuyến nghị của Argon review:
  - `vùng eo biển` (`p000572`)
  - `pháp sư trên không` / `đại đội pháp sư trên không` (`p000569`, `p000573`)
  - `Pháp sư Định danh` / `đơn vị Pháp sư Định danh` (`p000569`, `p000580`, `p000581`)
  - `đội phản ứng nhanh` / `Đội phản ứng nhanh số hai` / `lực lượng phản ứng nhanh tinh nhuệ` (`p000575`, `p000592`, `p000594`)
  - `lực lượng dự bị` (`p000577`)
  - `Lục quân Đế quốc` / `Đế quốc` (`p000580`, `p000583`, `p000585`)
  - `Ác quỷ sông Rhine` (`p000581`, `p000596`)
  - `mặt trận Rhine` / `Trận Không chiến sông Rhine` / `chiến dịch Rhine` (`p000581`, `p000582`, `p000583`)
  - `sĩ quan trực ban` (`p000584`)
  - `khu vực kiểm soát đánh chặn phía nam` (`p000584`)
  - `Cộng hòa François` (`p000596`)
  - `Khối Thịnh vượng chung` (`p000605`, `p000609`)
  - `đội tuần tra trên không` / `chỉ huy đội hình` (`p000567`, `p000568`)
  - `đài kiểm soát đánh chặn` / `phòng kiểm soát` / `trung tâm chỉ huy` / `trung tâm kiểm soát tích hợp` / `đài kiểm soát tuyến` (`p000568`, `p000572`, `p000579`, `p000583`, `p000588`)
  - `hai phân đội Argyle và Carbene` / `Argyle` / `Carbene` (`p000574`, `p000591`, `p000593`)
  - `không vực mười hai` / `không vực mười sáu` / `tuyến đánh chặn số hai` (`p000580`, `p000600`, `p000601`, `p000602`)
  - `tác chiến điện tử` / `các tín hiệu dẫn đường` / `hỗ trợ dẫn đường` / `các tín hiệu mồi nhử` (`p000585`, `p000587`)
  - `Tiểu đoàn Whiskey` / `Whiskey` / `Tiểu đoàn Scotch` (`p000600`, `p000602`, `p000604`, `p000606`)
