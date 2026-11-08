# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-04-b18`

- **Task ID**: `vol-10-ch-04-b18`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter022.xhtml/p000395` đến `YS-LN10/Text/chapter022.xhtml/p000433` (39 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc
- Đã dịch đầy đủ 39/39 đoạn theo đúng thứ tự nguồn từ `p000395` đến `p000433`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 39 dòng đã được cập nhật từ `draft` sang `reviewed` sau khi xử lý xong báo cáo review của Argon.
- Không tách hoặc gộp đoạn.
- Đã tiếp nhận và xử lý đầy đủ 3 minor findings trong `reviews/prose/vol-10/ch-04-b18-argon-review.yml`:
  - `YS-LN10/Text/chapter022.xhtml/p000409`: Đổi `chuyện thường ngày ở huyện` thành `chuyện thường ngày` để phù hợp bối cảnh quân sự phương Tây.
  - `YS-LN10/Text/chapter022.xhtml/p000413`: Đổi `rắn rỏi như đinh đóng cột` thành `rắn rỏi như thép tôi` để kết hợp từ tự nhiên và hợp ngữ cảnh khen ngợi binh sĩ dày dạn.
  - `YS-LN10/Text/chapter022.xhtml/p000415`: Đồng bộ đại từ quy chiếu tập thể ở câu đầu thành `chúng ta` (`Chúng ta sắp sửa tấn công một vùng đất mà trước đây chúng ta từng ghé thăm`).
- Bảo toàn tuyệt đối toàn bộ `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-10/ch-04-b18-argon-review.yml`.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter022.xhtml/p000405`: `*Thôi xong, chết tiệt thật.*`
  - `YS-LN10/Text/chapter022.xhtml/p000425`: `*thiếu hụt kinh phí*`
  - `YS-LN10/Text/chapter022.xhtml/p000427`: `*Nhìn xem quân số của bọn chúng ít ỏi đến mức nào kìa*`
- Tất cả 36 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.

## 2. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Đối thoại giữa Tướng Romel và Tanya (`p000395` – `p000397`, `p000400` – `p000402`, `p000404`, `p000407`)**:
  - Kế thừa trực tiếp mạch hội thoại từ cuối lô `vol-10-ch-04-b17`: Tướng Romel xưng `ta` (hoặc `chúng ta`), gọi Tanya là `Trung tá` / `Trung tá Degurechaff` / `cô` (và `các cô` khi gộp cả đơn vị).
  - Tanya xưng `tôi` (hoặc `chúng tôi`), gọi Tướng Romel là `thưa Tướng quân` / `ngài`, giữ giọng điệu lễ phép, chuyên nghiệp nhưng cố gắng khéo léo chỉ ra sự bất cập về quy mô lực lượng trước khi buộc phải nhận lệnh.
- **Điểm nhìn nội tâm ngôi thứ nhất của Tanya (`p000398`, `p000399`, `p000403`, `p000405`, `p000406`, `p000409`, `p000410`, `p000412`, `p000413`, `p000415` – `p000417`, `p000419`, `p000421`, `p000422`, `p000424` – `p000426`, `p000428` – `p000430`, `p000432`, `p000433`)**:
  - Tự xưng `mình` nhất quán theo `DEC-P01-001`; tự quy chiếu ngôi thứ ba `Tanya` ở `p000398` theo đúng biểu đạt của nguyên tác; dùng `chúng ta` khi quy chiếu chung về Tiểu đoàn 203/phe Đế quốc (`p000415`, `p000416`, `p000428`).
  - Gọi Tướng Romel là `ông ta` (`p000398`) và gọi binh sĩ thuộc quyền là `họ` (`p000403`, `p000409`, `p000410`, `p000412`, `p000413`, `p000421`, `p000422`, `p000425`, `p000429`, `p000432`).
- **Diễn văn của Tanya trước Tiểu đoàn Pháp sư Trên không số 203 (`p000411`, `p000414`, `p000418`, `p000420`, `p000423`, `p000427`, `p000431`)**:
  - Tanya xưng `tôi` và `chúng ta`, gọi cấp dưới là `các chiến hữu` / `các vị`, giữ giọng điệu hùng hồn, đanh thép, giàu sức khích lệ của một tiểu đoàn trưởng trước giờ xuất kích.

## 3. Kiểm tra các cấu trúc ngữ pháp và sắc thái dễ lệch nghĩa
- **`p000395` – `p000407`**: Giữ đúng tình huống bi hài của Tanya: vừa mới phân tích ở lô trước rằng chiến dịch cần ưu thế trên không cục bộ để bảo vệ các trọng điểm/điểm nghẽn, Tướng Romel liền tận dụng chính lập luận đó để giao luôn nhiệm vụ giữ vững các trọng điểm trong một đêm cho Tiểu đoàn Pháp sư Trên không số 203 (`p000395` – `p000397`). Dù Tanya cố viện lý do đơn vị mình chỉ là một tiểu đoàn chứ không phải trung đoàn hay lữ đoàn (`p000400` – `p000403`), Romel vẫn khóa chặt đường lui bằng lời khen ngợi rằng nếu Tiểu đoàn 203 không làm được thì chẳng ai trong Đế quốc làm nổi (`p000404`), khiến Tanya chỉ biết chửi thầm trong bụng mà ngoài mặt vẫn phải mỉm cười, đáp lại bằng lời xã giao nhã nhặn và chào nhận lệnh (`p000405` – `p000407`).
- **`p000408` – `p000416`**: Bảo toàn mốc thời gian – địa điểm (`0100 GIỜ NGÀY 17 THÁNG 8 NĂM THỐNG NHẤT 1927, DOANH TRẠI TIỂU ĐOÀN PHÁP SƯ TRÊN KHÔNG SỐ 203`) và sự đối lập giữa tác phong kỷ luật sắc bén của binh sĩ Tiểu đoàn 203 với nhiệm vụ vô lý sắp tới (`p000409` – `p000413`). Trong lời mở đầu diễn văn và suy nghĩ nối tiếp (`p000414` – `p000416`), giữ rõ mạch lập luận: sau thắng lợi ở Chiến dịch Cánh cửa xoay trên mặt trận phía tây, nay đơn vị chuẩn bị tiến đánh bản thổ Khối Thịnh vượng chung; vì pháp sư không thể trấn giữ lãnh thổ như bộ binh nên cần đưa cả bộ binh đi cùng.
- **`p000417` – `p000433`**: Giữ nguyên sự đan xen giữa lời diễn văn hùng hồn bên ngoài và dòng độc thoại nội tâm tỉnh táo, chua chát của Tanya bên trong:
  - Tanya hiểu rõ Đế quốc đang mắc căn bệnh kinh niên `*thiếu hụt kinh phí*` nên không đủ tiền đầu tư cho chiến thắng (`p000425`), và thẳng thắn thừa nhận với binh sĩ rằng quân địch sẽ cười nhạo quân số ít ỏi của một tiểu đoàn pháp sư đơn độc đi làm lực lượng tăng viện (`p000427` – `p000428`).
  - Tuy nhiên, để duy trì sĩ khí trước sự chi phối khắc nghiệt của tình thế cấp thiết (`p000429` – `p000430`), Tanya khích lệ lòng tự tôn của các pháp sư tinh nhuệ đã được tôi luyện bằng máu và sắt (`p000431`), đồng thời tự nhủ trong đoạn kết (`p000433`) rằng ý chí là thứ tiện lợi giúp con người tự bịt mắt mình khi hết đường lui và cất kín niềm tin cùng sự bất lực, nhưng tuyệt đối không được đánh mất cảm giác tự chán ghét bản thân vì mất đi khả năng nhận biết cái sai chính là con đường dẫn tới sự bất tài thực sự.

## 4. Thuật ngữ đã áp dụng và đề xuất (`pending_terms`)
- Kế thừa nhất quán các phương án từ `canon/glossary-pending.yml` và `work/run-state/pending-terms-index.yml`:
  - `Trung tá` / `Trung tá Degurechaff` (`p000395`, `p000397`, `p000404`)
  - `ưu thế trên không cục bộ` (`p000397`)
  - `Tướng Zettour` / `Tướng Romel` / `thưa Tướng quân` (`p000399`, `p000400`, `p000407`)
  - `Lục quân Đế quốc` / `Đế quốc` (`p000399`, `p000404`, `p000425`)
  - `Tiểu đoàn Pháp sư Trên không số 203` / `Tiểu đoàn 203` (`p000404`, `p000408`, `p000409`, `p000421`)
  - `mặt trận phía tây` (`p000414`)
  - `Khối Thịnh vượng chung` / `bản thổ của Khối Thịnh vượng chung` (`p000414`, `p000415`)
  - `Văn phòng Bộ Tổng tham mưu` (`p000421`)
- Ghi nhận các thuật ngữ/tiêu đề đề xuất mới trong lô (`status: pending`):
  - `0100 HOURS AUGUST 17, UNIFIED YEAR 1927, 203RD AERIAL MAGE BATTALION ENCAMPMENT` -> `0100 GIỜ NGÀY 17 THÁNG 8 NĂM THỐNG NHẤT 1927, DOANH TRẠI TIỂU ĐOÀN PHÁP SƯ TRÊN KHÔNG SỐ 203` (`p000408`)
  - `Operation Revolving Door` -> `Chiến dịch Cánh cửa xoay` (`p000414`; đồng bộ với `revolving door operation` -> `chiến dịch cánh cửa xoay` và `Operation Mini–Revolving Door` -> `Chiến dịch Cánh cửa xoay Thu nhỏ` trong sổ pending)
