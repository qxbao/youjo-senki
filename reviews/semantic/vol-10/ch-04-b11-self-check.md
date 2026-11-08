# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-04-b11`

- **Task ID**: `vol-10-ch-04-b11`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter022.xhtml/p000162` đến `YS-LN10/Text/chapter022.xhtml/p000196` (35 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ, trạng thái và bảo toàn cấu trúc
- Đã dịch đầy đủ 35/35 đoạn theo đúng thứ tự nguồn từ `p000162` đến `p000196`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 35 dòng trong `translations/vol-10/ch-04-b11.jsonl` được cập nhật từ `draft` sang `reviewed` ở bước Sign-off.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter022.xhtml/p000162`: `*sao ông ta nhận ra được chứ?*`.
- Tất cả 34 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.
- **Xử lý review ở bước Sign-off (`vol-10-ch-04-b11-translator-signoff`)**:
  - Tiếp nhận finding `minor` tại `YS-LN10/Text/chapter022.xhtml/p000195`: đổi cụm mở đầu từ `Thực tế vấn đề là` thành `Thực tế là` để câu tiếng Việt tự nhiên hơn, đồng thời giữ nguyên toàn bộ nghĩa và `locked_choices`.
  - Tiếp nhận finding `minor` tại `YS-LN10/Text/chapter022.xhtml/p000196`: đổi `khi đất nước của bạn đang cố` thành `khi chính quốc gia của mình đang cố` để nhất quán điểm nhìn nội tâm trong cùng đoạn và tương đồng với `p000193`, giữ nguyên mọi `locked_choices`.
  - Tuân thủ toàn bộ `pending_term_recommendations` và `locked_choices` từ `reviews/prose/vol-10/ch-04-b11-argon-review.yml`.

## 2. Xưng hô, điểm nhìn và giọng điệu (`DEC-P01-001`)
- **Trần thuật và độc thoại nội tâm của Tanya (`p000162`–`p000164`, `p000166`, `p000169`, `p000171`–`p000173`, `p000175`, `p000177`, `p000180`, `p000182`–`p000184`, `p000186`, `p000192`–`p000196`)**:
  - Tự quy chiếu trong nội tâm ngôi thứ nhất của Tanya dùng `mình` (`p000162`, `p000164`, `p000193`–`p000196`); câu trần thuật ngôi thứ ba (hoặc góc nhìn tách biệt giữa bản ngã nội tâm và nhân vật Tanya) gọi Tanya là `Tanya` / `cô` (`p000162`, `p000173`, `p000175`, `p000177`, `p000180`, `p000182`–`p000184`, `p000186`, `p000192`).
  - Trong câu giả định khái quát ở `p000196`, dùng `Người ta` và `chính quốc gia của mình` phù hợp với giọng bình luận nội tâm.
  - Quy chiếu `Tham tán Conrad` là `Tham tán Conrad` / `vị tham tán` / `ông ta`; quy chiếu `Đại tá Lergen` là `Đại tá Lergen` / `vị đại tá` / `cấp trên của mình` / `ông ấy` (trong nội tâm ngôi thứ nhất của Tanya ở `p000162`–`p000164`) hoặc `ông` (trong các câu trần thuật ngôi thứ ba `p000169`, `p000177`, `p000180`, `p000186`).
- **Đối thoại giữa Tham tán Conrad, Đại tá Lergen và Trung tá Tanya von Degurechaff (`p000165`, `p000167`–`p000170`, `p000174`, `p000176`, `p000178`–`p000179`, `p000181`, `p000185`, `p000187`–`p000191`, `p000194`)**:
  - Tham tán Conrad xưng `tôi`, gọi Lergen là `Đại tá Lergen` / `thưa Đại tá` / `ông` (`p000165`, `p000168`).
  - Đại tá Lergen xưng `tôi` / `chúng ta`, gọi Conrad là `Ông` / `ông` (`p000167`, `p000174`), và gọi Tanya là `Trung tá` / `cô` (`p000179`, `p000187`, `p000189`, `p000191`).
  - Tanya xưng `tôi` / `mình` (tự quy chiếu trong câu hỏi tu từ `p000190`) / `chúng ta`, gọi Lergen là `thưa Đại tá` / `Đại tá` kèm kính ngữ `ạ` phù hợp khi chất vấn cấp trên (`p000176`, `p000178`, `p000181`, `p000185`, `p000188`, `p000190`).

## 3. Kiểm tra nghĩa, phủ định, giả định và logic
- **`p000162`–`p000164`**: Giữ đúng nhận xét của Tanya rằng cách dùng từ lạ lùng của Lergen thực chất là cách ông ấy lảng tránh vấn đề: bề ngoài có vẻ điềm tĩnh như thường ngày nhưng ẩn sau đó là sự do dự và giằng xé nội tâm mà Tham tán Conrad khó lòng nhận ra; đồng thời bảo toàn giả định trái thực tế ở quá khứ (`p000164`) rằng nếu không biết các sĩ quan Bộ Tổng tham mưu coi trọng sự ngắn gọn súc tích đến mức nào thì có lẽ Tanya cũng chẳng bao giờ nhận ra bộ mặt lạnh tanh kín như bưng đó thực chất là gì.
- **`p000165`–`p000174`**: Bảo toàn mạch đối thoại khi Conrad rút thêm điếu xì gà và yêu cầu Lergen giải thích rõ, để rồi Lergen châm thuốc lá và tiết lộ sự thật phũ phàng đầy mỉa mai: điều duy nhất mọi người thống nhất được là hoàn toàn không có sự đồng thuận nào giữa Bộ Tổng tham mưu, Bộ Tư lệnh Tối cao và chính phủ về việc giảng hòa, thậm chí tìm được ai từng nghĩ đến chuyện đó cũng đã là may.
- **`p000175`–`p000185`**: Giữ đúng phản ứng bàng hoàng và bức xúc của Tanya khi cao giọng hỏi chẳng lẽ bên lục quân không có lấy những định hướng chỉ đạo hay chưa từng cân nhắc việc đó với tư cách một tổ chức, rồi ngắt lời Lergen để khẳng định rằng dù quân nhân chỉ là những người lính đơn thuần thì việc không chí ít cân nhắc đến ý tưởng đó vẫn thật lố bịch, vì đây là điều cô đã cố truyền đạt bằng mọi cách suốt thời gian qua.
- **`p000186`–`p000192`**: Bảo toàn hình ảnh Lergen phả làn khói thuốc đầy nicotine và hắc ín rồi khuyên Tanya rằng cô cần phải bọc đường thật hào phóng cho những viên thuốc đắng nhất, đáp lại bằng câu nói mỉa mai mang màu sắc thời chiến của Tanya rằng các cánh đồng củ cải đường đã bị chuyển thành ruộng khoai tây từ lâu nên lấy đâu ra đường, và lời kết luận đầy mệt mỏi của Lergen rằng chẳng có mấy ai nuốt trôi nổi viên thuốc đắng mang tên thực tại, nhất là trong chiến tranh khi lẽ thường bị quẳng qua cửa sổ.
- **`p000193`–`p000196`**: Giữ đúng tâm trạng bế tắc và hối hận của Tanya khi biết được bí mật đen tối nhất của đất nước cũng như cảm giác sự nghiệp của mình vốn vô nghĩa ngay từ đầu; bảo toàn chuỗi ẩn dụ tài chính – tín dụng rằng Đế quốc hiện không còn vận hành bình thường, séc có thể bị từ chối thanh toán bất cứ lúc nào, đất nước đang bấu víu vào tín dụng quay vòng vì thiếu tiền mặt trả nợ, và nguyên tắc về quyền (kể cả quyền được tắc trách) cũng bay biến khi quốc gia cố đánh một cuộc chiến bằng các khoản vay ứng trước.

## 4. Thuật ngữ đã áp dụng và đề xuất mới (Pending Terms)
- Áp dụng nhất quán các thuật ngữ đã có trong sổ pending của Tập 10:
  - `Đại tá Lergen` / `vị đại tá` / `thưa Đại tá` (`p000162`, `p000165`–`p000166`, `p000168`–`p000169`, `p000173`, `p000177`, `p000181`, `p000186`, `p000188`, `p000192`)
  - `Tham tán Conrad` / `vị tham tán` (`p000162`, `p000166`, `p000173`)
  - `chính quốc` (`p000163`)
  - `sĩ quan Bộ Tổng tham mưu` / `Bộ Tổng tham mưu` / `Văn phòng Bộ Tổng tham mưu` (`p000164`, `p000170`, `p000178`, `p000183`)
  - `Bộ Tư lệnh Tối cao` (`p000170`)
  - `giảng hòa` (`p000174`)
  - `bên lục quân` (`p000176`)
  - `Trung tá` (`p000179`, `p000187`)
  - `Đế quốc` (`p000195`)
- Ghi nhận các thuật ngữ/cụm từ đề xuất trong lô này để coordinator theo dõi:
  - `revolving credit` → `tín dụng quay vòng` (`p000195`)
  - `advance loans` → `các khoản vay ứng trước` (`p000196`)
