# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-04-b23`

- **Task ID**: `vol-10-ch-04-b23-translator-signoff` (parent: `vol-10-ch-04-b23`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter022.xhtml/p000610` đến `YS-LN10/Text/chapter022.xhtml/p000659` (50 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ, bảo toàn cấu trúc và Sign-off theo Argon Review
- Đã đối chiếu toàn bộ 50/50 đoạn từ `p000610` đến `p000659` (kết thúc Chương 4 Tập 10) với `reviews/prose/vol-10/ch-04-b23-argon-review.yml`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 50 dòng trong `translations/vol-10/ch-04-b23.jsonl` đã được cập nhật từ `draft` sang `reviewed`.
- Đã tiếp nhận và xử lý đầy đủ 3 findings mức `minor` có căn cứ trong `ch-04-b23-argon-review.yml` đồng thời bảo toàn mọi `locked_choices`:
  - `p000614`: Chỉnh cụm `"giáng một đòn tâm lý nặng nề lên tinh thần họ"` thành `"giáng một đòn nặng nề lên tâm trí họ"` để tránh lặp nghĩa giữa `"tâm lý"` và `"tinh thần"`.
  - `p000621`: Chỉnh cụm `"ở đầu dây bên kia"` thành `"ở đầu sóng bên kia"` cho chuẩn ngữ cảnh liên lạc vô tuyến.
  - `p000648`: Chỉnh cụm `"bị bỏ lại phía sau lưng"` thành `"bị bỏ xa phía sau"` cho tự nhiên, cô đọng.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `p000626`: `*Chúng đã hạ gục đài kiểm soát đánh chặn phía nam rồi.*`
  - `p000628`: `“*Veni, vidi, vici.*”`
  - `p000635`: `*Tàn phá, gieo rắc hỗn loạn, rồi cuối cùng gây ra sự sụp đổ toàn diện.*`
  - `p000649`: `*Đến lúc đuổi theo chúng rồi*`
  - Các đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` và bản dịch không tự thêm dấu `*...*`.

## 2. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Trần thuật ngôi thứ ba và điểm nhìn phía quân đội Khối Thịnh vượng chung (`p000610` – `p000659`)**:
  - Nối tiếp trực tiếp mạch cảnh từ cuối lô `ch-04-b22` (`p000609`): các kiểm soát viên không lưu, nhân viên thông tin vô tuyến tại phòng kiểm soát và các pháp sư Khối Thịnh vượng chung được gọi là `họ`.
  - Đối với chỉ huy Tiểu đoàn Scotch (`Scotch Leader`, vị tiểu đoàn trưởng ở `p000633` – `p000659`): trần thuật dùng đại từ `anh` nhất quán (`p000636`, `p000641`, `p000642`, `p000644`, `p000656`, `p000658`).
  - Trong lời thoại tại phòng kiểm soát và qua sóng vô tuyến (`p000612`, `p000617`, `p000619`, `p000620`, `p000622`): nhân viên vận hành và người báo tin xưng `chúng ta` / `chúng tôi`, gọi quân Đế quốc là `kẻ địch` / `chúng`.
  - Trong lời thoại của chỉ huy Tiểu đoàn Scotch và thuộc cấp (`p000631`, `p000633`, `p000638` – `p000640`, `p000645`, `p000647`, `p000650`, `p000654` – `p000659`):
    - Thuộc cấp gọi chỉ huy là `Thưa Chỉ huy`, xưng `chúng tôi` / `chúng ta`.
    - Khi liên lạc vô tuyến với trung tâm kiểm soát tích hợp (`p000633`, `p000654` – `p000657`): trung tâm kiểm soát tích hợp xưng `chúng tôi`, gọi `Scotch Leader`; `Scotch Leader` xưng `tôi` (trong câu nhắc lại theo quy ước vô tuyến ở `p000633`) và `chúng tôi` / `chúng ta`, gọi phía đài kiểm soát mặt đất là `các người` khi nổi giận bác bỏ yêu cầu truy kích thiếu suy nghĩ (`p000655`, `p000657`).

## 3. Kiểm tra nghĩa, logic và quan hệ nhân quả
- **`p000610` – `p000616`**: Giữ trọn vẹn sức nặng tâm lý lên các kiểm soát viên không lưu và nhân viên thông tin vô tuyến khi phải ngồi nghe những tiếng kêu cứu, báo cáo thương vong thảm khốc và tiếng thét trước khi mất liên lạc; bảo toàn quan hệ nhân quả ở `p000616`: vì không biết liệu sự hy sinh của đồng đội có xứng đáng hay không nên họ lại càng không muốn bỏ sót bất kỳ thông điệp nào.
- **`p000617` – `p000624`**: Bảo toàn diễn tiến báo động không kịp lúc: Tiểu đoàn Scotch phát hiện pháp sư trên không của địch lẻn qua vành đai phòng thủ ở độ cao thấp, nhưng lời cảnh báo gửi tới đài kiểm soát đánh chặn phía nam không kịp đến nơi trước khi đài này bị tấn công và mất liên lạc hoàn toàn sau một tiếng nổ lớn.
- **`p000625` – `p000631`**: Giữ rõ việc các pháp sư Khối Thịnh vượng chung trên không nhận ra đài kiểm soát đánh chặn phía nam đã bị hạ gục, tiếp đó bắt được thông điệp khoe khoang bằng tiếng Latinh phát trên mọi tần số ở `p000628` và câu dịch nghĩa kèm tiếng chửi thề của người lính ở `p000631`.
- **`p000633` – `p000644`**: Giữ đúng mạch tâm lý của `Scotch Leader`: từng tận mắt chứng kiến nỗi kinh hoàng trên mặt trận Rhine nên hiểu rõ lối đánh tàn phá, gieo rắc hỗn loạn dẫn tới sụp đổ toàn diện của Đế quốc; vừa tự hào về sự sẵn sàng của binh sĩ dưới quyền, vừa hoài nghi không biết đạn của đơn vị mình có bắn trúng nổi những con quái vật ấy không, nhưng những hoài nghi và nỗi sợ ấy đã không bị đem ra thử thách trong đêm đó.
- **`p000645` – `p000659`**: Bảo toàn bước ngoặt khi quân Đế quốc bất ngờ ngoặt hướng rút lui thần tốc sau khi san phẳng trung tâm kiểm soát đánh chặn phía nam; `Scotch Leader` lập tức kìm giữ đơn vị không truy kích vì nhận ra đó là cạm bẫy dẫn tới địa ngục trần gian, đồng thời kiên quyết bác bỏ yêu cầu truy kích thiếu suy nghĩ từ trung tâm kiểm soát tích hợp để bảo toàn lực lượng và hạ cánh xuống một căn cứ khác.

## 4. Thuật ngữ đã tra cứu và đề xuất tạm (Pending Terms)
- Tuân thủ đầy đủ `pending_term_recommendations` đã được Argon review xác nhận trong `ch-04-b23-argon-review.yml`:
  - `kiểm soát viên không lưu` (`p000611`) / `nhân viên thông tin vô tuyến` (`p000614`) / `nhân viên vận hành tại trung tâm chỉ huy` (`p000623`) / `nhân viên mặt đất` (`p000658`)
  - `phòng kiểm soát` (`p000615`) / `trung tâm chỉ huy` (`p000623`) / `đài kiểm soát đánh chặn phía nam` (`p000618`, `p000623`, `p000626`, `p000633`) / `trung tâm kiểm soát đánh chặn phía nam` (`p000646`) / `trung tâm kiểm soát tích hợp` (`p000633`, `p000654`) / `đài kiểm soát mặt đất` (`p000653`)
  - `Tiểu đoàn Scotch` (`p000617`) / `Scotch Leader` (`p000633`, `p000641`, `p000653`, `p000654`, `p000658`) / `tiểu đoàn trưởng` (`p000643`) / `Chỉ huy` (`p000639`)
  - `các pháp sư trên không` (`p000617`) / `các pháp sư Khối Thịnh vượng chung` (`p000625`) / `các pháp sư Đế quốc` (`p000630`)
  - `“*Veni, vidi, vici.*”` (`p000628`)
  - `mặt trận Rhine` (`p000634`, `p000643`) / `Đế quốc` (`p000636`, `p000638`, `p000648`) / `Lục quân Đế quốc` (`p000643`) / `con ác quỷ đó` (`p000651`)
