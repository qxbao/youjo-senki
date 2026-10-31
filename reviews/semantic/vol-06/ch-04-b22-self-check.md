# Báo cáo tự kiểm (Self-Check): `vol-06-ch-04-b22` (Sign-off)

- **Task ID**: `vol-06-ch-04-b22-translator-signoff`
- **Parent Task ID**: `vol-06-ch-04-b22`
- **Translator**: `argon-low`
- **Handoff**: `handoffs/vol-06/ch-04-b22.yml`, `handoffs/vol-06/ch-04-b22-translator-signoff.yml`
- **Review Report**: `reviews/prose/vol-06/ch-04-b22-argon-review.yml`
- **Tệp dịch**: `translations/vol-06/ch-04-b22.jsonl`
- **Phạm vi**: `YS-LN06/Text/part0021.html/p000210` → `YS-LN06/Text/part0021.html/p000241` (32 đoạn)
- **Trạng thái mỗi dòng**: `reviewed`

## 1. Xử lý Findings từ Argon Review
- **`YS-LN06/Text/part0021.html/p000236` (`minor` - `pronoun_and_viewpoint`)**: Tiếp nhận khuyến nghị từ `reviews/prose/vol-06/ch-04-b22-argon-review.yml`, đổi đại từ `Nó` ở đầu câu thứ nhất (quy chiếu công trình nghiên cứu) thành `Đó` (`Đó thậm chí còn chẳng phải là tài liệu của chính nước họ.`) để tách bạch hoàn toàn với đại từ `nó` ở câu thứ hai (quy chiếu Tanya theo `DEC-P01-001`), giữ nguyên mọi `locked_choices`.
- **`YS-LN06/Text/part0021.html/p000238` (`minor` - `style_and_naturalness`)**: Tiếp nhận khuyến nghị từ `reviews/prose/vol-06/ch-04-b22-argon-review.yml`, chỉnh `những giả định của bạn` thành `những giả định của mình` để đồng bộ ngôi với chủ ngữ phiếm chỉ `ai nấy` trong cùng mệnh đề, giữ nguyên vùng nhấn mạnh `*...*` theo `DEC-P01-002` và mọi `locked_choices`.

## 2. Kiểm tra tính đầy đủ, nghĩa gốc và `locked_choices`
- Đã kiểm tra đầy đủ 32/32 đoạn trong `translations/vol-06/ch-04-b22.jsonl`, khớp 1:1 theo `segment_id` và tuân thủ toàn bộ 32 mục `locked_choices` trong `reviews/prose/vol-06/ch-04-b22-argon-review.yml`.
- Bảo đảm giữ nguyên nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic nhân quả và thời gian của giả định:
  - **Đề xuất giải pháp chính trị qua Tướng von Zettour và phản ứng thận trọng của Uger (`p000210`–`p000216`)**: Tanya nhận định tình hình đang bất lợi khi Đế quốc say sưa trong ảo tưởng chiến thắng nhưng thực chất đang bị bùn lầy ngoài tiền tuyến nuốt chửng và cỗ máy bạo lực chính xác của Đế quốc đang mục ruỗng dần; từ mệnh đề rằng quân sự chỉ là sự tiếp nối của chính trị và đòi hỏi giải pháp chính trị, nó nhờ Uger thông qua Tướng von Zettour đề xuất điều đó lên cấp trên (`p000210`); Uger nhận lời sẽ nói chuyện với ông nhưng hạ giọng dặn trước đừng kỳ vọng nhiều vì sẽ không thể hành động ngay, hay đúng hơn là anh không thể khiến họ hành động được (`p000211`–`p000215`); dù không nêu đích danh ai, Tanya hiểu ngay ẩn ý rằng ngay cả khi Zettour ghi nhận đề xuất thì nó cũng chưa chắc có được màn chuyển hướng quyết liệt như mong muốn (`p000216`).
  - **Sự thiếu vắng kế hoạch viễn chinh và văn hóa tùy cơ ứng biến của Lục quân Đế quốc (`p000217`–`p000228`)**: Tanya hỏi thẳng Trung tá Uger vì sao quá nhiều việc bị gác lại—liệu có phải do phá hoại ngầm hay có kẻ nổi loạn trong tổ chức hay không (`p000217`); Weiss định ngăn Tanya vì cho rằng nó đã lỡ lời đi quá giới hạn nhưng Uger mỉm cười buồn bã ngăn anh ta lại và thừa nhận mình cũng vừa mới chợt nhận ra gốc rễ vấn đề (`p000218`–`p000220`); với tư cách một thành viên Bộ Tổng tham mưu, Uger tiết lộ rằng Bộ Tổng tham mưu chưa từng hình dung tới việc tiến hành các chiến dịch viễn chinh ở nước ngoài, Lục quân Đế quốc chỉ được thiết kế để phòng ngự cơ động gần biên giới và thậm chí không có sẵn kế hoạch xâm lược lãnh thổ địch, dẫn tới việc toàn quân phải tùy cơ ứng biến và đối phó chắp vá ngoài chiến trường (`p000221`); khi Tanya hỏi lại có phải nhờ nỗ lực hết sức của các cá nhân ngoài thực địa nên mới tránh được sụp đổ hoàn toàn hay không, Uger thừa nhận cách nói đó tuy gay gắt nhưng chính xác và ngước nhìn trần nhà với đôi vai như phủ bụi, thể hiện rõ mức độ trầm trọng của tình cảnh mà Bộ Tổng tham mưu đang đối mặt (`p000222`–`p000223`); Tanya nhận xét rằng văn hóa tổ chức của Lục quân Đế quốc xoay quanh việc tùy cơ ứng biến, việc đến đâu xử lý đến đó—dù mang lại sự linh hoạt chiến thuật đáng kinh ngạc nhưng quên bẵng chiến lược chẳng khác nào đặt cỗ xe trước con ngựa, và nếu ngay cả các chuyên gia chiến lược như Trung tướng von Zettour và Trung tướng von Rudersdorf cũng tự giới hạn trong phạm vi thuần túy quân sự thì Đế quốc thực chất không có chiến lược quốc gia, sẽ đi vào vết xe đổ của Hannibal: thắng mãi trên chiến trường cho đến một trận chiến cuối cùng không thể cứu vãn nổi (`p000224`–`p000228`).
  - **Bí mật quốc gia về nguồn gốc lý thuyết hậu cần đường sắt ở phía Đông (`p000229`–`p000241`)**: Uger tiết lộ thêm một bí mật quốc gia về công tác phân phối bằng mạng lưới đường sắt ở phía Đông: do thiếu kinh nghiệm lập kế hoạch tấn công, Bộ Tổng tham mưu đã học hỏi từ một tài liệu nọ (`p000229`); Tanya lấy làm lạ vì chưa từng nghe tới nghiên cứu cơ bản nào như thế và đoán đùa phải chăng lấy từ bài tập của học viên sĩ quan (`p000230`); câu trả lời tự giễu của Uger khiến nó há hốc mồm rồi cứng họng: những nguyên lý cơ bản được lấy từ công trình nghiên cứu chung giữa Bộ Tổng tham mưu Quân đội Cộng hòa và Ban Biên soạn Lịch sử Chiến tranh mang tên *Khảo cứu về Công tác Hậu cần khi Xâm lược Đế quốc* (`p000231`–`p000235`); đó thậm chí không phải tài liệu của nước nhà, và nếu không phải nghe từ Uger thì nó sẽ chẳng đời nào tin nổi (`p000236`–`p000237`); Tanya sực nhận ra trước nay mình đã đánh giá họ quá cao khi mặc định rằng Lục quân Đế quốc giỏi ứng biến là nhờ chuẩn bị bài vở kỹ lưỡng ở trường đại học quân sự và hẳn phải có ai đó nghiên cứu về chiến dịch viễn chinh (`p000238`–`p000240`); lô khép lại bằng lời bộc bạch đi kèm nụ cười gượng gạo đầy chấn động của Uger rằng không thể đem lý thuyết vận hành đường sắt vốn tối ưu hóa cho chiến lược nội tuyến ra áp dụng ở nước ngoài (`p000241`).
- Tuyệt đối không sao chép câu hoặc cụm từ nguồn tiếng Anh vào báo cáo.

## 3. Kiểm tra đại từ, xưng hô và giọng văn (`DEC-P01-001`)
- Phân biệt rõ điểm nhìn và quy ước đại từ theo `DEC-P01-001`, `canon/style-guide.md` và `locked_choices`:
  - **Trong trần thuật ngôi thứ ba bám sát điểm nhìn của Tanya (`p000210`, `p000212`, `p000216`, `p000220`, `p000221`, `p000223`, `p000224`, `p000229`, `p000233`, `p000235`, `p000236`, `p000241`)**: quy chiếu Tanya bằng `Tanya` và đại từ `nó`; quy chiếu Trung tá Uger bằng `Uger` và `anh ấy`; quy chiếu Thiếu tá Weiss bằng `Weiss` và `anh ta`.
  - **Trong độc thoại nội tâm trực tiếp và bình luận điểm nhìn của Tanya (`p000223`–`p000228`, `p000236`, `p000238`–`p000240`)**: Tanya tự quy chiếu bằng `mình` (`p000240`), dùng đại từ giả định khái quát `bạn` (`p000223`) và phản thân `mình` đi với chủ ngữ phiếm chỉ `ai nấy` (`p000238`).
  - **Trong lời thoại trực tiếp**:
    - Tanya (`Trung tá Tanya von Degurechaff`) nói với Uger (`p000210`, `p000212`, `p000214`, `p000217`, `p000222`, `p000230`, `p000232`, `p000237`) xưng `tôi` (và `chúng ta` khi nói chung về phía Đế quốc), gọi Uger là `Trung tá Uger` / `anh`, quy chiếu Tướng von Zettour là `Tướng von Zettour`.
    - Trung tá Uger nói với Tanya (`p000211`, `p000213`, `p000215`, `p000219`, `p000221`, `p000223`, `p000229`, `p000231`, `p000234`, `p000241`) xưng `tôi` / `chúng ta`, gọi Tanya là `cô`, quy chiếu Tướng von Zettour là `ngài ấy` (`p000211`).
    - Thiếu tá Weiss gọi Tanya (`p000218`) là `Trung tá von Degurechaff`.

## 4. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002`)
- Đối chiếu toàn bộ 32 đoạn với thẻ `<html:em>` trong XHTML nguồn:
  - `part0021.html/p000228`: bảo toàn cụm nhấn mạnh bằng `*cho đến một trận chiến cuối cùng không thể nào cứu vãn nổi.*`
  - `part0021.html/p000234`: bảo toàn hai cụm nhấn mạnh bằng `*Cộng hòa*` và `*Khảo cứu về Công tác Hậu cần khi Xâm lược Đế quốc.*`
  - `part0021.html/p000238`: bảo toàn toàn bộ đoạn nhấn mạnh nội tâm bằng `*...*`.
  - `part0021.html/p000239`: bảo toàn toàn bộ đoạn nhấn mạnh nội tâm bằng `*...*`.
- Toàn bộ 28 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và không tự ý thêm dấu `*...*`.

## 5. Thuật ngữ và lựa chọn tạm (`pending_term_recommendations`)
- Đảm bảo khớp đầy đủ toàn bộ 11 mục `pending_term_recommendations` trong `reviews/prose/vol-06/ch-04-b22-argon-review.yml`:
  - `Tướng von Zettour` / `Trung tướng von Zettour` / `Zettour` (`p000210`, `p000216`, `p000226`).
  - `Trung tá Uger` / `Uger` (`p000212`, `p000217`, `p000220`, `p000229`, `p000236`, `p000241`).
  - `Trung tá von Degurechaff` (`p000218`).
  - `Bộ Tổng tham mưu` (`p000221`, `p000223`, `p000227`, `p000229`).
  - `Lục quân Đế quốc` (`p000221`, `p000224`, `p000238`).
  - `phòng ngự cơ động` (`p000221`).
  - `Trung tướng von Rudersdorf` (`p000226`).
  - `Bộ Tổng tham mưu Quân đội Cộng hòa` / `Ban Biên soạn Lịch sử Chiến tranh` (`p000234`).
  - `*Khảo cứu về Công tác Hậu cần khi Xâm lược Đế quốc*` (`p000234`).
  - `trường đại học quân sự` (`p000238`).
  - `lý thuyết vận hành đường sắt` / `chiến lược nội tuyến` (`p000241`).

## 6. Kiểm tra định dạng và công cụ xác thực
- Đã cập nhật trường `status` của toàn bộ 32 dòng trong `translations/vol-06/ch-04-b22.jsonl` từ `draft` sang `reviewed`.
- Chạy `python3 tools/validate_translation.py --handoff handoffs/vol-06/ch-04-b22.yml --source work/vol-06/batches/ch-04-b22-source.jsonl --translation translations/vol-06/ch-04-b22.jsonl` đạt `PASS`.
