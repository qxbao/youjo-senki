# Báo cáo tự kiểm & Sign-off (Self-Check): `vol-08-ch-05-b11`

- **Task ID**: `vol-08-ch-05-b11-translator-signoff` (parent: `vol-08-ch-05-b11`)
- **Phạm vi**: `YS-LN08/Text/chapter018.xhtml/p000367` – `YS-LN08/Text/chapter018.xhtml/p000404` (38 đoạn)
- **Người dịch**: `argon-low`
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`
- **Source SHA256**: `b5e55889614fa6fbd3f59c099ac5b761978d880d2feea29cd7355a432a65d2a4`

## 1. Xử lý Findings từ Argon Review (`reviews/prose/vol-08/ch-05-b11-argon-review.yml`)
- **`YS-LN08/Text/chapter018.xhtml/p000373` (minor – `lexical_nuance`)**:
  - **Vấn đề**: Từ chỉ tính chất ở câu cuối thể hiện sự thiếu thận trọng/khinh suất khi bật cười trên chiến trường thay vì lỗi phép tắc xã giao (`khiếm nhã`).
  - **Xử lý**: Đã tiếp nhận và sửa `Dù có hơi khiếm nhã` thành `Dù có hơi thiếu thận trọng` để sát nghĩa hơn.
- **`YS-LN08/Text/chapter018.xhtml/p000390` (moderate – `meaning_logic`)**:
  - **Vấn đề**: Câu thứ hai đảo ngược quan hệ nhân quả – mục đích giữa việc sĩ quan cao cấp tự đặt mình vào nguy hiểm và cuộc giải cứu.
  - **Xử lý**: Đã tiếp nhận và sửa thành `Nghĩa là cô khó lòng gạt bỏ mối nghi vấn nghiêm túc của mình về việc liệu điều đó có đang được dùng làm cái cớ để thực hiện cuộc giải cứu hay không.`, khớp hoàn toàn với `locked_choices`.
- **Trạng thái dòng (`status`)**: Đã cập nhật trường `status` của toàn bộ 38/38 dòng trong `translations/vol-08/ch-05-b11.jsonl` từ `draft` sang `reviewed`.

## 2. Kiểm tra tính toàn vẹn & nghĩa gốc
- Đã dịch và rà soát đầy đủ 38/38 đoạn từ `p000367` đến `p000404` theo đúng thứ tự, không gộp dòng, không tách dòng, không bỏ sót bất kỳ câu hay mệnh đề nào.
- Tuyệt đối không sao chép bất kỳ câu hoặc cụm từ nguồn tiếng Anh nào vào báo cáo tự kiểm này.
- Giữ trọn nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic nhân quả và thời gian của giả định:
  - **Tanya nhận ra ý đồ để lộ vị trí sở chỉ huy của Tướng von Zettour (`p000367`–`p000378`)**: Tiếp nối nghi vấn từ lô trước, Serebryakov báo cáo rằng cô không thể phủ nhận khả năng đó nhưng từ chỉ việc lộ vị trí đang xuất hiện với tần suất rất cao (`p000367`); Tanya nhìn kỹ mặt viên sĩ quan phụ tá và hỏi lại xem có nhầm lẫn không, rồi bật cười lớn khi nhận được câu trả lời rụt rè nhưng khẳng định chắc nịch (`p000368`–`p000369`); cô thầm nghĩ chẳng lẽ Serebryakov thực sự tin rằng Zettour sẽ phạm sai lầm ngớ ngẩn đến mức tiết lộ vị trí cho đám Cộng sản, rồi khen cách hiểu “bị lộ” thật độc đáo (`p000370`–`p000371`); giữ đúng cấu trúc “không chỉ… mà còn…” ở `p000372`: từ kinh nghiệm bản thân, Tanya khẳng định một chuyên gia bàn giấy ở hậu phương như người của Cục Quân vụ không chỉ thông thạo bảo mật tình báo mà còn rành rẽ nghệ thuật cố tình “làm rò rỉ” thông tin với đủ cách sáng tạo; cô ví đây là lời mời gọi rõ ràng như lời tình nhân thì thầm trong tam thiên thế giới, thừa nhận bật cười trên chiến trường có hơi thiếu thận trọng nhưng quá buồn cười, đồng thời khẳng định tính cách con người là chất liệu ra quyết định tuyệt vời nhất vì các sĩ quan tham mưu vốn rất thận trọng và ở ngoài chiến trường thì tính cách càng tệ hại lại càng quỷ quyệt (`p000373`–`p000375`); trước vẻ ngơ ngác của Visha, Tanya chỉ ra thiên kiến do huấn luyện rằng vào lúc thế này không nói vị trí sở chỉ huy “bị lộ” mà phải nói chúng ta đã “làm lộ nó”—đó không phải trò chơi chữ mà là vấn đề về chủ thể, hay đúng hơn là sự thiếu thấu hiểu tình hình (`p000376`–`p000378`).
  - **Góc nhìn của sĩ quan tham mưu và bài học tình huống cho Trung úy Serebryakov (`p000379`–`p000404`)**: Khi Visha lo ngại làm vậy quá rủi ro và không hiểu Tướng von Zettour nghĩ gì vì dường như hoàn toàn vô ích, Tanya đồng tình rằng thông thường để lộ sở chỉ huy là quá rủi ro vì chính họ đã chứng minh cho Quân đội Liên bang thấy chiến thuật chặt đầu chỉ huy hiệu quả ra sao (`p000379`–`p000381`); cô hiểu Serebryakov nói từ góc nhìn đơn vị tác chiến hiện dịch và biết Quân đội Liên bang lẫn người dân Liên bang cực kỳ nhạy cảm với chiến thuật chặt đầu chỉ huy đến mức bảo vệ sở chỉ huy kỹ như lũ lửng (`p000382`–`p000383`); Tanya khen Visha là người đàng hoàng rồi khuyên cô tìm hiểu cách đào tạo sĩ quan tham mưu ở trường đại học quân sự—nơi dạy họ chủ động tìm ra điều người khác ghét và Lục quân Đế quốc tuyển chọn, huấn luyện nguồn nhân lực đáng tin cậy đó một cách có hệ thống (`p000384`–`p000387`); chính vì hiểu lối tư duy tham mưu nên Tanya buộc phải hành động, nhận thấy ngay cả hai Đại úy Meybert và Ahrens cũng không để ý sự bất thường khi một sĩ quan cao cấp tự đặt mình vào nguy hiểm (`p000388`–`p000389`); cô thậm chí nghi ngờ liệu điều bất thường đó có đang được dùng làm cái cớ để thực hiện cuộc giải cứu hay không, vì dù tin tưởng Zettour ở tầng sâu căn bản nhưng lý lẽ của tổ chức đôi khi có thể thổi bay cả lời hứa của một vị trung tướng (`p000390`); gạt sang một bên để bồi dưỡng cấp dưới, Tanya ví việc Tướng von Zettour làm lộ vị trí sở chỉ huy như một chiếc đèn lồng khổng lồ rồi đặt câu hỏi cho Visha về việc Quân đội Liên bang sẽ làm gì tiếp theo (`p000391`–`p000395`); Visha đáp đúng rằng họ sẽ bị Quân đội Liên bang nhắm vào—một đáp án hiển nhiên 100 phần trăm vì sau bao phen bị Lục quân Đế quốc vô hiệu hóa sở chỉ huy, bao vây và tiêu diệt hoàn toàn, tâm trí quân Liên bang hẳn đang bị độc chiếm bởi sự phấn khích trước cơ hội trả đũa và nghiền nát sở chỉ huy địch (`p000396`–`p000400`); giữ đúng giả định ở `p000401`–`p000402`: khi Tanya hỏi tiếp nếu cố tình thu hút địch thì sao, Visha nhận định họ sẽ là mồi nhử hoàn hảo nhưng thắc mắc họ lấy đâu ra đơn vị để tận dụng thời cơ khi nhử địch vào tròng; Tanya liền trêu hỏi phải chăng Serebryakov đã hóa thành hồn ma và khẽ đá nhẹ vào chân cô kèm nụ cười nhắc rằng cô vẫn có chân, tức là Kampfgruppe Salamander dưới vỏ bọc Kampfgruppe Lergen đang hiện diện ngay tại đây—dù Tanya chẳng muốn bắt đơn vị mạnh mẽ và quý giá này làm việc quá sức (`p000403`–`p000404`).

## 3. Xưng hô & giọng nhân vật (`DEC-P01-001` & `locked_choices`)
- **Góc nhìn Trung tá Tanya von Degurechaff tại Soldim 528**:
  - Trần thuật gọi Tanya là `Tanya` / `cô`; gọi Serebryakov là `Serebryakov` / `Trung úy Serebryakov` / `viên sĩ quan phụ tá` / `cô ấy`.
  - Độc thoại nội tâm của Tanya (`p000372`, `p000404`): tự xưng `mình`. Câu hỏi nội tâm hướng về Visha (`p000370`) gọi `cô`; câu chế giễu nội tâm hướng về phía Liên bang (`p000383`) gọi `các người`.
  - Đối thoại giữa Tanya và Trung úy Serebryakov: Tanya xưng `tôi` / `chúng tôi` / `chúng ta`, gọi `Visha`, `Trung úy`, `Trung úy Serebryakov`, `cô`; Serebryakov xưng `tôi`, gọi `T-Trung tá?` (`p000376`), `D-dạ, thưa Trung tá?` (`p000394`) và dùng kính ngữ `ạ` phù hợp với thái độ cấp dưới.

## 4. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002` & `locked_choices`)
- Đã đối chiếu toàn bộ 38 đoạn trong gói nguồn XHTML (`chapter018.xhtml/p000367`–`p000404`):
  - `p000368`: câu hỏi nội tâm mở đầu đặt trong thẻ nhấn mạnh -> bảo toàn bằng `*Cái gì?*`.
  - `p000370`: câu hỏi nội tâm thứ hai đặt trong thẻ nhấn mạnh -> bảo toàn bằng `*Cô—cô thực sự nghĩ Zettour sẽ phạm sai lầm ngớ ngẩn đến mức tiết lộ vị trí của mình cho đám Cộng sản biết ư?!*`.
  - `p000383`: câu chế giễu nội tâm cuối đoạn đặt trong thẻ nhấn mạnh -> bảo toàn bằng `*Các người là cái gì, lũ lửng chắc?*`.
  - `p000404`: câu hỏi ngầm qua nụ cười đặt trong thẻ nhấn mạnh -> bảo toàn bằng `*Cô có chân mà, phải không?*`.
  - 34 đoạn còn lại không có thẻ nhấn mạnh trong XHTML và bản dịch hoàn toàn không tự ý thêm dấu `*...*`.

## 5. Thuật ngữ Canon & Pending đã áp dụng nhất quán (`pending_term_recommendations` & `locked_choices`)
- `viên sĩ quan phụ tá`, `Trung úy Serebryakov`, `Serebryakov`, `Visha`, `Trung úy` (`p000368`, `p000377`, `p000382`, `p000384`, `p000393`, `p000403`, `p000404`)
- `Zettour`, `Tướng von Zettour`, `vị tướng ấy`, `trung tướng` (`p000370`, `p000373`, `p000381`, `p000390`, `p000391`)
- `đám Cộng sản` (`p000370`)
- `hậu phương`, `Cục Quân vụ` (`p000372`)
- `tam thiên thế giới` (`p000373`)
- `các sĩ quan tham mưu`, `sĩ quan tham mưu` (`p000375`, `p000386`, `p000388`, `p000391`)
- `T-Trung tá?`, `D-dạ, thưa Trung tá?` (`p000376`, `p000394`)
- `sở chỉ huy` (`p000377`, `p000380`, `p000383`, `p000391`, `p000395`, `p000399`)
- `Quân đội Liên bang`, `Liên bang`, `Lục quân Đế quốc` (`p000380`, `p000382`, `p000383`, `p000387`, `p000395`, `p000396`, `p000399`)
- `chiến thuật chặt đầu chỉ huy` (`p000380`, `p000383`)
- `đơn vị tác chiến hiện dịch` (`p000382`)
- `trường đại học quân sự`, `nguồn nhân lực` (`p000386`, `p000387`)
- `hai vị đại úy là Meybert và Ahrens`, `sĩ quan cao cấp` (`p000389`)
- `vô hiệu hóa sở chỉ huy, bao vây và tiêu diệt hoàn toàn` (`p000399`)
- `mồi nhử` (`p000402`)
- `Kampfgruppe Salamander`, `Kampfgruppe Lergen` (`p000404`)

## 6. Kết quả chạy Validator
- Lệnh thực thi: `python3 tools/validate_translation.py --handoff handoffs/vol-08/ch-05-b11.yml --source work/vol-08/batches/ch-05-b11-source.jsonl --translation translations/vol-08/ch-05-b11.jsonl`
- Kết quả: `PASS` (38 dòng khớp thứ tự mã đoạn, trạng thái `reviewed` và metadata trong handoff).
