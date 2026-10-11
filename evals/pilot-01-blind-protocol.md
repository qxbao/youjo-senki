# Pilot-01: quy trình đánh giá mù

## Tài liệu được phép đọc

Người chấm chỉ được đọc đúng ba tệp trong `work/vol-01/pilot-01-blind/` (`source.jsonl`, `candidate-a.jsonl`, `candidate-b.jsonl`), các tài liệu trong `canon/` và rubric `evals/pilot-rubric.md`. Không mở các bản dịch gốc, không tra tên tệp gốc và không đọc báo cáo thuật ngữ. Không tìm kiếm hay suy đoán danh tính người dịch hoặc mô hình từ nội dung.

Đối chiếu từng ứng viên với nguồn theo `segment_id`; dùng canon để phân biệt quyết định đã chốt với lựa chọn còn là đề xuất. Đánh giá hai ứng viên độc lập theo cùng một rubric.

## Rubric phải dùng

Chấm riêng từng tiêu chí sau trên thang 1–5 theo mô tả mức điểm tương ứng trong `evals/pilot-rubric.md`:

1. Đúng nghĩa và quan hệ logic.
2. Giọng kể / giọng nhân vật.
3. Văn xuôi tiếng Việt tự nhiên.
4. Nhất quán xưng hô, quân hàm và thuật ngữ.
5. Không bỏ sót hoặc thêm ý.

Áp dụng cả mục **Lỗi loại trực tiếp** của rubric. Không dùng điểm trung bình để che lỗi nghiêm trọng. Với mỗi tiêu chí, ghi điểm và lý do ngắn bằng tiếng Việt. Nêu từng lỗi cụ thể kèm `segment_id`, tiêu chí liên quan và mô tả ngắn; nếu có lỗi loại trực tiếp, ghi rõ loại lỗi và mã đoạn. Khi không có nội dung liên quan đến quân hàm, ghi “không xuất hiện”.

Không viết lại toàn bộ bản dịch hoặc đề xuất một bản dịch hoàn chỉnh. Chỉ trích dẫn/nhắc phần cần thiết để mô tả lỗi, gắn với mã đoạn. Không nêu tên mô hình, không đoán mô hình hay danh tính ứng viên. Giữ nhãn ứng viên A/B như trong gói khi ghi nhận kết quả.
