# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-04-b10`

- **Task ID**: `vol-10-ch-04-b10`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter022.xhtml/p000127` đến `YS-LN10/Text/chapter022.xhtml/p000161` (35 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ, trạng thái và bảo toàn cấu trúc
- Đã dịch đầy đủ 35/35 đoạn theo đúng thứ tự nguồn từ `p000127` đến `p000161`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 35 dòng trong `translations/vol-10/ch-04-b10.jsonl` được cập nhật từ `draft` sang `reviewed` ở bước Sign-off.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter022.xhtml/p000140`: `*đó*` và `*mình*`.
  - `YS-LN10/Text/chapter022.xhtml/p000150`: `*Chuyện gì đang diễn ra thế này?*`.
- Tất cả 33 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.
- **Xử lý review ở bước Sign-off (`vol-10-ch-04-b10-translator-signoff`)**:
  - Tiếp nhận finding `minor` tại `YS-LN10/Text/chapter022.xhtml/p000158`: chỉnh cụm thời gian cuối câu từ `chỉ mới vài giây trước đó` thành `chỉ mới chốc lát trước đó` để khớp mạch thời gian cuộc đối thoại mà vẫn giữ nguyên `locked_choices`.
  - Tuân thủ toàn bộ `pending_term_recommendations` và `locked_choices` từ `reviews/prose/vol-10/ch-04-b10-argon-review.yml`.

## 2. Xưng hô, điểm nhìn và giọng điệu (`DEC-P01-001`)
- **Trần thuật và độc thoại nội tâm của Tanya (`p000128`, `p000131`, `p000134`, `p000138`–`p000142`, `p000144`–`p000150`, `p000152`, `p000154`–`p000155`, `p000157`–`p000158`)**:
  - Tự quy chiếu trong nội tâm ngôi thứ nhất của Tanya dùng `mình` (`p000138`–`p000142`, `p000144`–`p000149`, `p000152`, `p000155`, `p000157`); câu trần thuật ngôi thứ ba (hoặc góc nhìn tách biệt giữa bản ngã nội tâm và nhân vật Tanya) gọi Tanya là `Tanya` / `cô` (`p000128`, `p000149`, `p000158`).
  - Quy chiếu `Tham tán Conrad` là `Tham tán Conrad` / `vị tham tán` / `ông ta`; quy chiếu `Đại tá Lergen` là `Đại tá Lergen` / `vị đại tá` / `cấp trên của mình` / `sếp` / `ông ấy` (trong nội tâm Tanya) hoặc `ông` (trong câu trần thuật khách quan `p000158`).
- **Đối thoại giữa Tham tán Conrad, Đại tá Lergen và Trung tá Tanya von Degurechaff (`p000127`, `p000129`–`p000130`, `p000132`–`p000133`, `p000135`–`p000137`, `p000143`, `p000146`, `p000151`, `p000153`, `p000156`, `p000159`–`p000161`)**:
  - Tanya nói với Conrad và Lergen bằng giọng lịch thiệp, đúng lễ tiết quân đội: xưng `tôi`, gọi Lergen là `Thưa Đại tá` (`p000143`).
  - Đại tá Lergen xưng `tôi` / `chúng tôi` (đại diện cho phía Bộ Tổng tham mưu/lục quân ở `p000133`), gọi Conrad là `Thưa Tham tán` / `thưa Tham tán` / `ông` (`p000129`, `p000136`, `p000153`, `p000161`), và gọi Tanya là `Trung tá` / `cô` (`p000146`, `p000151`).
  - Tham tán Conrad xưng `tôi` / `chúng tôi` (đại diện cho phía Bộ Ngoại giao ở `p000160`) hoặc `cả hai chúng ta` (`p000130`), gọi Lergen là `Đại tá Lergen` / `thưa Đại tá` / `ông` / `các ông` (`p000130`, `p000132`, `p000135`, `p000137`).

## 3. Kiểm tra nghĩa, phủ định, giả định và logic
- **`p000129`–`p000132`**: Giữ đúng mạch đối đáp có phần chua chát khi Lergen yêu cầu Conrad ngừng lôi kéo nhân sự của Văn phòng Bộ Tổng tham mưu, trước khi Conrad cười xòa và quay lại câu hỏi chính về điều kiện giảng hòa mà lục quân mong muốn cũng như vị thế của Đế quốc sau khi mọi chuyện ngã ngũ.
- **`p000133`–`p000137`**: Bảo toàn câu trả lời ngắn gọn của Lergen rằng phía họ không biết, phản ứng nhíu mày ngậm chặt xì gà đầy bất mãn của Conrad, và lời khẳng định của Conrad rằng tuy là tham tán nhưng ông ta cũng là thành viên Bộ Tư lệnh Tối cao nên có thẩm quyền tiếp cận mọi bí mật quân sự liên quan.
- **`p000138`–`p000145`**: Giữ đúng chuỗi suy luận nội tâm của Tanya: từ việc xác nhận yêu cầu của Conrad hoàn toàn hợp lý dù quân đội chia sẻ thông tin theo nguyên tắc chỉ-biết-khi-cần, đến việc chợt nhận ra người không đủ thẩm quyền ở đây chính là mình (một trung tá pháp sư) và tự trách bản thân đã mất đi sự nhạy bén nơi công sở nên mới quên mất kỹ năng cơ bản là lặng lẽ xin phép rút lui.
- **`p000146`–`p000152`**: Giữ đúng tình huống Lergen bất ngờ bảo Tanya cứ ngồi yên tại chỗ khi cô mới nhổm dậy được nửa chừng, khiến Tanya hoang mang không hiểu chuyện gì đang diễn ra, trước khi Lergen cảnh báo rằng đây là điều có lẽ cô sẽ không muốn biết.
- **`p000153`–`p000161`**: Bảo toàn lời rào đón trang nghiêm của Lergen rằng chuyện ông sắp nói hoàn toàn không phải bí mật nên xét ở một khía cạnh nào đó lại càng nghiêm trọng hơn rất nhiều; giữ đúng sự tương phản khi Lergen nói Văn phòng Bộ Tổng tham mưu, Bộ Tư lệnh Tối cao và chính phủ đều có chung một quan điểm, khiến Conrad thắc mắc vì sao một điều ai cũng biết như vậy mà phía họ lại chưa hay biết, để rồi Lergen khẳng định thực tế hoàn toàn và tuyệt đối ngược lại.

## 4. Thuật ngữ đã áp dụng và đề xuất mới (Pending Terms)
- Áp dụng nhất quán các thuật ngữ đã có trong sổ pending của Tập 10:
  - `Tham tán Conrad` / `vị tham tán` / `thưa Tham tán` / `tham tán` (`p000129`, `p000131`, `p000134`, `p000136`–`p000138`, `p000140`, `p000153`, `p000157`–`p000158`, `p000161`)
  - `Đại tá Lergen` / `vị đại tá` / `thưa Đại tá` (`p000128`, `p000134`–`p000135`, `p000137`, `p000143`, `p000146`–`p000147`, `p000149`, `p000158`)
  - `Văn phòng Bộ Tổng tham mưu` (`p000129`, `p000159`)
  - `giảng hòa` (`p000132`)
  - `bên lục quân` / `quân đội` (`p000132`, `p000138`)
  - `Đế quốc` (`p000132`)
  - `Bộ Tư lệnh Tối cao` (`p000137`, `p000159`)
  - `trung tá pháp sư` / `Trung tá` (`p000141`, `p000151`)
  - `tiền tuyến` (`p000144`)
- Ghi nhận các thuật ngữ/cụm từ đề xuất trong lô này để coordinator theo dõi:
  - `need-to-know basis` → `nguyên tắc chỉ-biết-khi-cần` (`p000138`)
  - `geopolitical interests` → `lợi ích địa chính trị` (`p000141`)
