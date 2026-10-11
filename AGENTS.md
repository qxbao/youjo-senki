# Quy tắc làm việc

- EPUB/PDF gốc ở `../youjo-senki-source/` chỉ được đọc tại chỗ. Tuyệt đối không sao chép, sửa, đưa vào Git hoặc tải lên nơi khác; không gửi nội dung nguồn tới dịch vụ bên ngoài.
- Chỉ **một tác tử** được sửa `translations/` tại một thời điểm, kể cả khi làm ở các đoạn khác nhau. Ghi người giữ quyền sửa và phạm vi công việc trong `handoffs/` trước khi bắt đầu; bàn giao rồi mới đổi người sửa.
- Tác tử phản biện chỉ ghi báo cáo trong `reviews/semantic/` hoặc `reviews/prose/`; không sửa bản dịch. Người giữ quyền sửa tiếp nhận báo cáo và thực hiện sửa.
- Giữ mã đoạn ổn định giữa bản dịch, báo cáo và bàn giao. Không lưu văn bản nguồn trong Git; dữ liệu tách nguồn chỉ được lưu cục bộ trong `work/` bị Git bỏ qua. Không dùng `git add -f` cho dữ liệu này.
- Tra cứu `canon/` trước khi dịch. Thuật ngữ, tên gọi và lựa chọn còn chưa rõ phải ghi là đề xuất, không tự xem là đã chốt.
- Không tự tạo nội dung dịch khi chưa có nhiệm vụ dịch cụ thể. Công cụ chuẩn bị dữ liệu hiện chỉ được áp dụng LN 01 theo phạm vi đã giao; không tự mở rộng sang tập khác.
