# Rubric thử dịch LN 01

Chỉ chuẩn bị tiêu chí; chưa có bản dịch hoặc kết quả chấm. Đối chiếu nguồn
cục bộ với từng `segment_id`, xét cả ngữ cảnh liền trước/sau và canon được
ghim trong bàn giao. Không chép câu nguồn vào báo cáo phản biện.

## Thang điểm

Chấm từng tiêu chí từ 1 đến 5, không dùng điểm trung bình để che lỗi nghiêm
trọng. Mỗi điểm cần có mã đoạn và lý do bằng tiếng Việt.

| Tiêu chí | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Đúng nghĩa và quan hệ logic | Sai nghĩa chủ đạo; quan hệ logic đổ vỡ | Nhiều lỗi về điều kiện, nguyên nhân, thời gian hoặc mức độ chắc chắn | Giữ ý chính nhưng còn lệch sắc thái hoặc mắt xích lập luận | Nghĩa và logic chính xác; chỉ cần chỉnh nhẹ độ rõ | Chính xác cả chi tiết, phủ định, điều kiện, quan hệ nhân quả và mức độ chắc chắn |
| Giọng kể / giọng nhân vật | Đổi điểm nhìn hoặc làm mất giọng chủ đạo | Thường xuyên đồng nhất giọng kể, thoại và nội tâm | Nhận diện được giọng nhưng sắc thái chưa ổn định | Giữ điểm nhìn, giọng và sắc thái; vài chỗ cần tinh chỉnh | Giữ nhất quán giọng riêng, khoảng cách trần thuật, mỉa mai và nhịp lập luận |
| Văn xuôi tiếng Việt tự nhiên | Khó hiểu, nhiều câu không thành nghĩa | Gượng cấu trúc tiếng Anh, phải đọc lại nhiều lần | Đọc hiểu được nhưng nhịp và kết hợp từ còn cứng | Rõ, tự nhiên; chỉ còn vài chỗ vụng | Trôi chảy, chính xác, nhịp hợp cảnh và không mất sắc thái vì làm đẹp câu |
| Nhất quán xưng hô, quân hàm và thuật ngữ | Mâu thuẫn lan rộng, thiếu căn cứ lựa chọn | Nhiều biến thể tùy tiện hoặc xưng hô lệch ngữ cảnh | Chủ yếu nhất quán nhưng còn điểm chưa giải thích | Nhất quán với canon đã duyệt; đề xuất chưa chốt được ghi rõ | Nhất quán trong toàn gói, đúng ngữ cảnh; mọi điểm chưa chốt có mã đề xuất và căn cứ |
| Không bỏ sót hoặc thêm ý | Thêm/bớt làm thay đổi nội dung chủ đạo | Nhiều chi tiết bị thêm, lược hoặc giải thích thay nguồn | Đủ ý chính nhưng còn thiếu/thừa chi tiết nhỏ | Đủ mọi ý; chỉ cần chỉnh nhẹ cách biểu đạt | Phủ đủ từng đơn vị, chi tiết, mức độ nhấn mạnh và dấu hiệu cấu trúc; không thêm ý |

Canon hiện chưa chốt thuật ngữ và xưng hô. Không buộc người dịch tự chốt để đạt
điểm cao: đánh giá tính nhất quán của phương án tạm và cách ghi nghi vấn.
Chỗ chưa đủ căn cứ phải được giải quyết trước khi duyệt nếu ảnh hưởng đến nghĩa.
Nếu gói không có quân hàm, ghi “không xuất hiện”; không suy diễn để chấm.

## Lỗi loại trực tiếp

Chỉ một lỗi dưới đây cũng khiến gói **không đạt**, bất kể tổng điểm:

- Đảo nghĩa phủ định, kể cả phủ định kép hoặc phủ định có phạm vi điều kiện.
- Nhầm chủ thể thực hiện, nhận hành động, nói hoặc suy nghĩ.
- Sai quân hàm so với nguồn hoặc quy chuẩn đã duyệt.
- Sai quan hệ nhân vật, chẳng hạn đảo cấp trên/cấp dưới hoặc quan hệ thân thuộc.
- Bỏ nguyên một đơn vị nguồn trong dải được giao, kể cả đơn vị ngắn.

Người phản biện ghi loại lỗi, `segment_id`, vị trí và lý do; không sửa bản dịch.
Không xem lỗi chỉ là “câu chưa hay”. Đề xuất còn chưa chốt không tự động là lỗi
quân hàm/quan hệ; cần chứng minh sự sai lệch bằng đối chiếu nguồn tại chỗ.

## Điều kiện đạt và luồng phản biện

Gói đạt khi không có lỗi loại trực tiếp, **mỗi tiêu chí ít nhất 4/5** (tổng
ít nhất 20/25), đủ mã đoạn và không còn vấn đề nghĩa cần giải quyết.
“Đạt rubric” không tự chuyển trạng thái bản dịch thành approved; phải có người duyệt.

Phản biện nghĩa ghi ở `reviews/semantic/`, phụ trách nghĩa, logic, độ đủ và
quan hệ/xưng hô/quân hàm/thuật ngữ. Phản biện văn phong ghi ở `reviews/prose/`,
phụ trách giọng và tiếng Việt, đồng thời báo lại nếu sửa văn có nguy cơ đổi nghĩa.
Mỗi báo cáo ghi task_id, phiên bản bản dịch, SHA nguồn, điểm từng tiêu chí phụ
trách, danh sách lỗi và kết luận. Người giữ quyền sửa tiếp nhận, sửa rồi gửi
kiểm tra lại; mọi tác tử phản biện chỉ ghi báo cáo.
