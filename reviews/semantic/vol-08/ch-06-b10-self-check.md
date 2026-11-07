# Báo cáo tự kiểm dịch thuật — `vol-08-ch-06-b10`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-06-b10`
- **Tác tử**: `argon-low` (Translator)
- **Phạm vi đoạn**: `YS-LN08/Text/chapter022.xhtml/p000355` đến `YS-LN08/Text/chapter022.xhtml/p000396` (42 đoạn)
- **Tệp đích**: `translations/vol-08/ch-06-b10.jsonl`
- **Trạng thái các dòng**: `reviewed` (42/42 dòng — đã xử lý Sign-off theo `ch-06-b10-argon-review.yml`, không có lỗi cần sửa và tuân thủ đầy đủ `locked_choices` cùng `pending_term_recommendations`)

## 2. Tự kiểm theo quy chuẩn & quyết định
1. **Bảo toàn nghĩa, phủ định, điều kiện và quan hệ nhân quả**:
   - Đã rà soát toàn bộ 42 đoạn đối chiếu với nguồn.
   - Bảo toàn chính xác sắc thái đánh giá bi quan của Trung tướng von Zettour về toàn cục sau khi chứng kiến cả hậu phương lẫn tiền tuyến (`p000355`), việc Zettour dùng sở chỉ huy làm mồi nhử mà không hề tin chắc mình sẽ được cứu (`p000362`–`p000366`), và sự chấn động trong nhận thức của Tanya khi phát hiện người mình từng đánh giá là thực dụng lại sẵn sàng xả thân trong lúc ngặt nghèo (`p000364`, `p000367`, `p000368`).
   - Giữ đúng mạch đối đáp ẩn ý giữa hai người về trách nhiệm đối với thương vong ở Soldim 528 (`p000369`–`p000373`), quan điểm về quyền tự quyết và tự chịu trách nhiệm của Tanya (`p000374`–`p000382`), cũng như màn bình phẩm về lá trà do Đại tá Calandro gửi tặng và câu hỏi xoáy cuối đoạn về thiện chí/ác ý cùng lẽ thường giữa bản quốc và mặt trận phía đông (`p000383`–`p000396`).
2. **Hệ thống đại từ và xưng hô (`DEC-P01-001`)**:
   - **Trần thuật**: Gọi Tanya là `cô`, gọi Zettour là `ông`, gọi Đại tá Calandro là `ông ta`.
   - **Nội tâm tự quy chiếu của Tanya**: Dùng `mình` ở các đoạn độc thoại nội tâm trực tiếp (`p000367`, `p000376`, `p000377`, `p000382`); dùng `bạn` / `con người ta` cho các mệnh đề khái quát mang tính châm ngôn (`p000368`, `p000375`).
   - **Đối thoại**: Zettour xưng `tôi`, gọi Tanya là `Trung tá` / `Trung tá von Degurechaff` / `cô`; Tanya xưng `tôi`, gọi Zettour là `ngài` / `thưa Tướng quân`, gọi chung phía Đế quốc là `chúng ta`. Khi nói lời cảm ơn lính cần vụ mang trà lên (`p000384`), dịch là `"Cảm ơn nhé."` tự nhiên và phù hợp ngữ cảnh.
3. **Quy tắc nhấn mạnh (`DEC-P01-002`)**:
   - Kiểm tra trường `xhtml` của toàn bộ 42 đoạn: chỉ có 2 vị trí chứa thẻ nhấn mạnh là `YS-LN08/Text/chapter022.xhtml/p000357` (`*Ồ!*`) và `YS-LN08/Text/chapter022.xhtml/p000368` (`*Nếu đi theo một ai đó vô điều kiện, bạn sẽ có nguy cơ bị dẫn dắt vào chỗ hiểm nguy*`).
   - Đã biểu diễn chính xác bằng Markdown `*...*` đúng phạm vi thẻ nhấn mạnh của nguồn và không tự thêm dấu sao ở bất kỳ đoạn nào khác.
4. **Thuật ngữ Canon & Pending**:
   - Tuân thủ nhất quán các phương án trong sổ pending của tập 08: `Trung tá von Degurechaff`, `Tướng quân`, `sở chỉ huy`, `Soldim 528`, `Đại tá von Lergen`, `Being X`, `lính cần vụ`, `mặt trận phía đông`, `người Ildoa`, `Đại tá Calandro`, `tuyến đầu tiên`, `bản quốc`.
   - Không phát sinh thuật ngữ mới gây mơ hồ cần đăng ký thêm.
