# Báo cáo tự kiểm (Self-Check): `vol-05-ch-03-b01` (Translator Sign-off)

- **Task ID**: `vol-05-ch-03-b01-translator-signoff` (parent: `vol-05-ch-03-b01`)
- **Translator**: `argon-low`
- **Handoff**: `handoffs/vol-05/ch-03-b01.yml`, `handoffs/vol-05/ch-03-b01-translator-signoff.yml`
- **Review tiếp nhận**: `reviews/prose/vol-05/ch-03-b01-argon-review.yml`
- **Tệp dịch**: `translations/vol-05/ch-03-b01.jsonl`
- **Phạm vi**: `YS-LN05/Text/part0008.html/p000001` → `YS-LN05/Text/part0018.html/p000015` (34 đoạn)
- **Trạng thái mỗi dòng**: `reviewed`

## 1. Xử lý các phát hiện trong `argon-review` (`findings` & `locked_choices`)
- Đã tiếp nhận và chỉnh sửa đầy đủ 2 phát hiện mức `minor` từ `reviews/prose/vol-05/ch-03-b01-argon-review.yml`, đồng thời bảo đảm tuân thủ toàn bộ `locked_choices` và `pending_term_recommendations`:
  - **`YS-LN05/Text/part0008.html/p000012`** (`minor`): Thống nhất đại từ tự xưng của Mary Sue trong cả ba mệnh đề thành `Con / con` (thay cho hai chỗ `cháu` ở sau) khi gọi `Bà` trong bức thư gửi chung cho Mẹ và Bà, bảo đảm mạch xưng hô liền lạc xuyên suốt bức thư từ `p000002` đến `p000018` và khớp với `locked_choices`.
  - **`YS-LN05/Text/part0018.html/p000008`** (`minor`): Chỉnh cụm từ chỉ tác nhân thứ ba lấy mất chỗ trên tàu từ `một đơn vị nào khác chen ngang` thành `bên nào khác chen ngang` theo khuyến nghị của reviewer để giữ đúng độ mở của đại từ bất định trong nguyên bản.
- Đã cập nhật trường `status` của toàn bộ 34 dòng trong `translations/vol-05/ch-03-b01.jsonl` từ `draft` sang `reviewed`.

## 2. Kiểm tra tính đầy đủ và nghĩa gốc (`meaning`)
- Đã dịch đầy đủ toàn bộ 34 đoạn từ `YS-LN05/Text/part0008.html/p000001` đến `YS-LN05/Text/part0018.html/p000015` theo đúng thứ tự trong gói nguồn.
- Bảo toàn nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic nhân quả và thời gian của giả định:
  - **Lá thư gửi về gia đình của Mary Sue (`part0008.html/p000001`–`p000019`)**:
    - Mary gửi lời chào và hỏi thăm sức khỏe của Mẹ và Bà khi mùa hè vừa khép lại và những cơn gió thu se lạnh sắp thổi về, dặn hai người giữ gìn sức khỏe kẻo bị cảm lạnh (`p000001`–`p000003`).
    - Cô báo tin mình vẫn khỏe nhưng xin lỗi vì không thể viết bất kỳ chi tiết nào, kể cả ngày tháng hay địa điểm hiện tại, do quy định của quân đội (`p000004`–`p000006`).
    - Cô kể rằng danh sách các điều cấm viết trong thư vừa mới được cập nhật cách đó mấy hôm: không được tiết lộ loại bánh mì đã ăn, loại thịt đã ăn (thịt bò, thịt lợn, thịt gà, thịt cừu) hay ngày chính xác nhận được thư từ gia đình; có quá nhiều quy định hạn chế đến mức rất khó nhớ xuể (`p000007`–`p000011`).
    - Cô dẫn ví dụ rằng mình có thể nói nhớ món bánh nướng nhân táo của Bà, nhưng nếu nói ở doanh trại đã được ăn bánh táo hay chưa thì sẽ bị quy vào tội làm lộ bí mật quân sự; dù đã cố cẩn thận khi viết nhưng một phần bức thư vẫn có khả năng bị bộ phận kiểm duyệt bôi đen (`p000012`–`p000013`).
    - Dù cảm thấy bức bối vì không được kể những điều mình muốn, Mary trấn an gia đình rằng chưa có chuyện gì lớn xảy ra; cô cho biết đơn vị hiện đang huấn luyện và tái tổ chức—thông tin đã được sĩ quan cấp trên (người cũng dặn không được tiết lộ danh tính của vị ấy) cho phép viết—và họ vẫn chưa biết sắp tới sẽ được điều động đi đâu, cuối cùng khép lại bức thư bằng lời chúc yêu thương từ một căn cứ không thể tiết lộ địa điểm (`p000014`–`p000019`).
  - **Mở đầu Chương III tại Thủ đô Đế quốc Berun (`part0018.html/p000001`–`p000015`)**:
    - Mở đầu vào ngày 28 tháng 9, Năm Thống nhất 1926 tại Thủ đô Đế quốc Berun (`p000001`); mỗi lần bước qua cổng Văn phòng Bộ Tổng tham mưu, Tanya lại thầm nghĩ cấp trên chỉ toàn làm theo ý họ (`p000002`).
    - Mới chỉ vài giờ trôi qua kể từ khi Tanya rút Kampfgruppe của mình khỏi miền đông về thủ đô Đế quốc; họ từng được cử tới đó dưới danh nghĩa khảo sát tình hình nhưng lại bị triệu hồi chỉ bằng một mệnh lệnh đột ngột (`p000003`).
    - Trung tá Tanya von Degurechaff vốn là người cần mẫn, có đạo đức nghề nghiệp cao và khác hẳn những kẻ lười biếng ghét làm việc xứng với đồng lương, nhưng ngay cả nó cũng thấy bất mãn khi Bộ Tổng tham mưu liên tục thay đổi nhiệm vụ của mình (`p000004`).
    - Việc di chuyển cả một Kampfgruppe từ miền đông về lại thủ đô vô cùng vất vả: dù đơn vị trực thuộc Bộ Tổng tham mưu và chỉ đồn trú chứ không phải biệt phái cho mượn tại khu vực thuộc quyền quản hạt của Cụm tập đoàn quân phía Đông ở mặt trận phía Đông, việc rút quân gấp rút không thể nào diễn ra suôn sẻ (`p000005`–`p000006`).
    - Khó khăn lớn nhất là phương tiện quay về thủ đô vì không đơn giản như đi tàu đường dài bằng thẻ thông minh: số toa tàu Lục quân Đế quốc được sử dụng có giới hạn, những cam kết hỗ trợ trên giấy tờ không phải lúc nào cũng đúng ngoài thực địa, và ngay cả chỗ trên tàu đã được bảo đảm trong kế hoạch đóng dấu chính thức vẫn có thể mất trắng vì thời tiết, sự cố kỹ thuật hoặc bên nào khác chen ngang (`p000007`–`p000008`).
    - Điểm lại lịch trình dồn dập: khoảng một tuần trước, Tanya phải chạy đôn chạy đáo thu xếp chỗ chở đơn vị thiết giáp cùng khí tài hạng nặng của pháo binh và kịp nhờ viên sĩ quan phụ tá đắc lực mua giúp ít quà lưu niệm từ miền đông; vài ngày trước, nó chỉ vừa vặn chợp mắt được một lát trong khoang tàu hạng nhất chật hẹp; đêm qua, nó mới đặt chân tới thủ đô (`p000009`–`p000011`).
    - Giữa lúc bận rộn như vậy, trước cả khi kịp trình diện báo cáo, nó lại nhận thêm một bức điện tín từ Trung tướng von Rudersdorf thuộc Bộ Tổng tham mưu yêu cầu có mặt lúc tờ mờ sáng; không thể từ chối yêu cầu dựa trên chức trách và thẩm quyền chính đáng, Tanya quyết định tranh thủ chợp mắt vài tiếng để giữ đầu óc tỉnh táo, rồi khi được viên sĩ quan phụ tá đánh thức, nó khoác lên mình bộ quân phục phẳng phiu, cậy mắt mở ra bằng chút cà phê thay thế của một sĩ quan ma pháp thuộc Lục quân Đế quốc để bắt đầu ngày làm việc (`p000012`–`p000015`).
- Tuyệt đối không chép câu hoặc cụm từ nguồn tiếng Anh vào báo cáo.

## 3. Kiểm tra đại từ, xưng hô và giọng văn (`pronouns`, `DEC-P01-001`)
- Phân biệt rõ điểm nhìn và quy ước đại từ theo `DEC-P01-001` cùng `canon/style-guide.md`:
  - **Trong thư của Mary Sue gửi Mẹ và Bà (`part0008.html/p000001`–`p000019`)**: Mary tự xưng `Con / con` xuyên suốt bức thư (và `bọn con` khi nói chung về các binh sĩ trong đơn vị), gọi người nhận là `Mẹ và Bà` / `Bà` / `hai người` / `gia đình`, giữ giọng văn lễ phép, tình cảm, gần gũi và hơi hồn nhiên của cô gái trẻ viết thư về nhà từ quân ngũ.
  - **Trong trần thuật ngôi thứ ba bám sát điểm nhìn của Tanya (`part0018.html/p000002`–`p000004`, `p000009`–`p000015`)**: quy chiếu Tanya bằng tên/chức danh (`Tanya`, `Trung tá Tanya von Degurechaff`) và đại từ `nó` kết hợp phản thân `mình`.
  - **Trong độc thoại nội tâm và suy ngẫm trực tiếp của Tanya (`part0018.html/p000002`, `p000005`–`p000008`)**: Tanya dùng `chúng tôi` khi đại diện cho toàn bộ đơn vị Kampfgruppe của mình và dùng `người ta` ở câu nhận xét khái quát (`p000012`), giữ giọng văn thực dụng, sắc sảo và pha chút châm biếm của một sĩ quan tham mưu có tư duy công sở hiện đại.

## 4. Kiểm tra bảo toàn nhấn mạnh (`emphasis`, `DEC-P01-002`)
- Đối chiếu toàn bộ 34 đoạn với thẻ `<html:em>` trong XHTML nguồn:
  - `YS-LN05/Text/part0008.html/p000001` → `p000019` (19 đoạn): toàn bộ nội dung mỗi đoạn trong lá thư của Mary Sue đều nằm trong thẻ `<html:em>` và đã được bọc đầy đủ bằng dấu `*...*`.
  - `YS-LN05/Text/part0018.html/p000002`: phần suy nghĩ cuối câu nằm trong thẻ `<html:em>` và đã được bọc chính xác bằng `*Cấp trên đúng là chỉ toàn làm theo ý mình*`.
- Toàn bộ 14 đoạn còn lại (`part0018.html/p000001` và `p000003`–`p000015`) không có thẻ nhấn mạnh trong nguồn và không tự ý thêm dấu `*...*`.

## 5. Kiểm tra thuật ngữ và tính nhất quán (`canon/` & `pending_term_recommendations`)
- Áp dụng nhất quán toàn bộ các thuật ngữ trong `pending_term_recommendations` của `argon-review`:
  - `Mary Sue` (`part0008.html/p000019`)
  - `Thủ đô Đế quốc Berun` (`part0018.html/p000001`)
  - `Văn phòng Bộ Tổng tham mưu` / `Bộ Tổng tham mưu` (`part0018.html/p000002`, `p000004`, `p000006`, `p000012`)
  - `Kampfgruppe` (`part0018.html/p000003`, `p000005`)
  - `Trung tá Tanya von Degurechaff` (`part0018.html/p000004`)
  - `mặt trận phía Đông` (`part0018.html/p000006`)
  - `Cụm tập đoàn quân phía Đông` (`part0018.html/p000006`)
  - `Lục quân Đế quốc` (`part0018.html/p000007`, `p000015`)
  - `sĩ quan phụ tá` (`part0018.html/p000009`, `p000015`)
  - `Trung tướng von Rudersdorf` (`part0018.html/p000012`)
  - `sĩ quan ma pháp` (`part0018.html/p000015`)
  - `cà phê thay thế` (`part0018.html/p000015`).

## 6. Kết quả chạy công cụ kiểm tra (`validator`)
- Tệp `translations/vol-05/ch-03-b01.jsonl` gồm đúng 34 dòng JSONL hợp lệ, tất cả đều có `status: "reviewed"`.
- Chạy lệnh xác thực:
  `python3 tools/validate_translation.py --handoff handoffs/vol-05/ch-03-b01.yml --source work/vol-05/batches/ch-03-b01-source.jsonl --translation translations/vol-05/ch-03-b01.jsonl`
- Kết quả: **PASS** (34 dòng khớp hoàn toàn thứ tự mã đoạn và metadata trong handoff).
