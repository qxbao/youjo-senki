# Protocol đánh giá mù thứ hai — pilot-01

Phạm vi: tám đoạn `YS-LN01/Text/chapter001.xhtml/p000024` đến `YS-LN01/Text/chapter001.xhtml/p000031`, theo đúng thứ tự mã đoạn.

## Dữ liệu đánh giá

Chỉ dùng các tệp trong `work/vol-01/pilot-01-argument-blind/`:

- `source.jsonl`: văn bản nguồn để đối chiếu; mã đoạn ở trường `id`.
- `candidate-a.jsonl`: Candidate A; mã đoạn ở trường `segment_id`.
- `candidate-b.jsonl`: Candidate B; mã đoạn ở trường `segment_id`.

Hai tệp ứng viên chỉ có `segment_id` và `translation`. Toàn bộ ba tệp dữ liệu phải được Git bỏ qua; không đưa dữ liệu vào commit hoặc gửi nội dung nguồn tới dịch vụ bên ngoài.

## Cách chấm

1. Dùng [rubric hiện có](pilot-rubric.md); giữ nguyên các tiêu chí, thang điểm, trọng số và cách tổng hợp mà rubric quy định.
2. Đọc theo thứ tự mã đoạn, đối chiếu mỗi ứng viên với cùng đoạn trong `source.jsonl`. Đánh giá Candidate A và Candidate B độc lập theo cùng rubric.
3. Ghi nhận xét và điểm bằng nhãn Candidate A hoặc Candidate B, kèm mã đoạn và tiêu chí liên quan. Không thêm tiêu chí hoặc suy diễn thông tin không có trong dữ liệu đánh giá.
4. Chỉ thực hiện chấm trong nhiệm vụ đánh giá được giao riêng. Việc chuẩn bị bộ dữ liệu này không chấm chất lượng, xếp hạng hoặc chọn ứng viên; không tự nâng bản nào thành bản chuẩn.

## Giữ đánh giá mù

- Chỉ gọi hai ứng viên là Candidate A và Candidate B trong quá trình chấm và báo cáo.
- Cấm mở các bản dịch gốc, lịch sử Git, handoff hoặc dữ liệu khác để tìm danh tính hay ánh xạ ứng viên.
- Cấm suy đoán mô hình, tác giả hoặc công cụ tạo bản dịch, kể cả dựa vào văn phong.
- Không ghi tên mô hình, tác giả, tệp gốc hoặc thông tin nhận diện khác vào báo cáo đánh giá.
- Nếu danh tính bị lộ, dừng lượt đánh giá và báo tình trạng lộ thông tin; không dùng suy đoán danh tính để điều chỉnh điểm.
