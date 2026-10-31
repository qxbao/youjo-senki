# Báo cáo tự kiểm (Self-Check): `vol-06-ch-02-b16`

- **Task ID:** `vol-06-ch-02-b16`
- **Translator:** `argon-low`
- **Phạm vi đoạn:** `YS-LN06/Text/part0013.html/p000184` đến `YS-LN06/Text/part0013.html/p000213` (30 phân đoạn)
- **Tệp bản dịch:** `translations/vol-06/ch-02-b16.jsonl`
- **Trạng thái:** `reviewed` (30/30 dòng — đã sign-off sau `ch-02-b16-argon-review`)

## 1. Kiểm tra tính đầy đủ, nghĩa và logic
- Toàn bộ 30 phân đoạn trong tệp nguồn đã được dịch đầy đủ, giữ nguyên thứ tự và mã định danh `segment_id`.
- Bảo toàn chính xác ý nghĩa, các cấu trúc phủ định, giả định và tiến trình tâm lý – hành động trong vở kịch tranh cãi giữa Trung tá Drake và Đại tá Mikel trước mặt sĩ quan chính trị Liliya cùng các thông dịch viên:
  - `p000184`–`p000191`: Drake kìm nén cơn giận trước đám Cộng sản để giữ sức tìm điểm đột phá, cố tình nhắc tới danh dự của những người lính tận trung với Đức Vua Bệ hạ dưới ngọn cờ Lục quân Khối Thịnh vượng chung nhằm chọc tức phía Cộng sản; thấy Liliya suýt buột miệng phản ứng, ông thầm chất vấn vì sao cô ta hiểu được mà không dùng phương ngữ Nữ hoàng ngay từ đầu.
  - `p000192`–`p000200`: Drake cao giọng cảnh cáo việc can thiệp qua kênh không chính thức là vi phạm hiệp ước, đồng thời thầm cảm thông với Mikel vì luôn bị giám sát như có dây xích quanh cổ và ngao ngán khi bản thân phải đóng vai kẻ làm nền trong trò hề này; sau đó ông dùng ẩn dụ luật đi săn của giới quý tộc để đòi lại con mồi mà quân mình đã bắt được.
  - `p000201`–`p000208`: Màn tung hứng ứng biến ăn ý giữa Drake và Mikel nhằm duy trì sức ép hình thức mà không gây nghi ngờ, buộc phía chính ủy phải tự đưa ra một giải pháp chính trị vì bản thân Mikel không có đủ thẩm quyền tự ý trả tù binh.
  - `p000209`–`p000213`: Mikel viện lý do thẩm quyền của sĩ quan chính trị và luật pháp trên lãnh thổ Liên bang đối với công dân nước mình; Drake lập tức phản pháo rằng chưa chắc họ là công dân Liên bang và hai nước chưa hề ký hiệp ước chuyển giao tù binh; kết cục phía Liên bang phải nhượng bộ trước để giải quyết bằng một thỏa hiệp tại thực địa trước khi vấn đề leo thang thành rắc rối pháp lý nhạy cảm và chuyện giữ thể diện.

## 2. Kiểm tra quy chuẩn xưng hô và giọng văn (`DEC-P01-001`)
- **Trung tá Drake**:
  - Trần thuật ngôi thứ ba: dùng `ông` nhất quán nối tiếp từ `ch-02-b14` và `ch-02-b15`.
  - Độc thoại nội tâm:
    - Hướng tới Liliya (`p000190`): xưng `tôi`, gọi `cô`.
    - Tự cảm thán với bản thân (`p000195`, `p000196`): tự xưng `Mình` / `bản thân`.
  - Thoại trực tiếp (trong vở kịch tranh cãi): xưng `tôi` / `chúng tôi` / `chúng ta`, gọi Mikel là `Đại tá Mikel` / `ông`, gọi chung phía Liên bang/sĩ quan chính trị là `các người`.
- **Đại tá Mikel / Liliya**:
  - Thoại trực tiếp với Drake (`p000202`, `p000209`): xưng `tôi`, gọi `Trung tá Drake` / `ông`, giữ thái độ vừa cứng rắn theo đúng vai diễn vừa nêu rõ rào cản thẩm quyền của sĩ quan chính trị.
  - Trần thuật ngôi thứ ba (từ điểm nhìn của Drake đối với Liliya): gọi là `viên sĩ quan chính trị, Liliya`, `con chó canh này`, `viên chính ủy`.

## 3. Kiểm tra bảo toàn định dạng nhấn mạnh (`DEC-P01-002`)
- Chỉ sử dụng dấu `*...*` tại đúng 5 phân đoạn có thẻ nhấn mạnh trong nguyên bản XHTML:
  - `p000187`: 2 cụm nhấn mạnh trong lời tuyên bố của Drake về danh dự và lòng tận trung với nhà vua.
  - `p000190`: 1 cụm bọc toàn bộ câu chất vấn nội tâm hướng về Liliya.
  - `p000195`: 1 cụm bọc toàn bộ câu cảm thán nội tâm ngắn.
  - `p000196`: 1 cụm bọc toàn bộ câu độc thoại nội tâm.
  - `p000200`: 3 cụm nhấn mạnh xoay quanh hình ảnh người lính Khối Thịnh vượng chung, thú tiêu khiển quý tộc và con mồi của mình.
- Toàn bộ 25 phân đoạn còn lại không có thẻ nhấn mạnh trong nguồn và hoàn toàn không sử dụng dấu `*`.

## 4. Thuật ngữ và tính nhất quán
- Tuân thủ đầy đủ các thuật ngữ trong `canon/glossary.yml` và `work/run-state/pending-terms-index.yml`, đồng bộ chặt chẽ với `ch-02-b14` và `ch-02-b15`:
  - `Lục quân Khối Thịnh vượng chung`, `Khối Thịnh vượng chung`, `Quân đội Liên bang`, `Liên bang`, `lãnh thổ Liên bang`, `đám Cộng sản`.
  - `sĩ quan chính trị`, `chính ủy`, `phương ngữ Nữ hoàng`, `hệ thống chỉ huy`, `người thông dịch` / `thông dịch viên`.
  - Danh xưng và cấp bậc: `Trung tá Drake`, `Đại tá Mikel`, `Liliya`.
- Ghi nhận các mục đề xuất thuật ngữ tạm trong `notes`:
  - `p000187`: `Đức Vua Bệ hạ`
  - `p000197`: `Đại tá Mikel` (đồng bộ với `ch-02-b14`)
  - `p000212`: `hiệp ước chuyển giao tù binh`
