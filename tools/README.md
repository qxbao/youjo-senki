# Công cụ dự kiến

Chỉ liệt kê yêu cầu; chưa triển khai công cụ xử lý EPUB ở bước này.

- **Tách EPUB:** đọc sách gốc tại chỗ, lập mã đoạn ổn định và vị trí đối chiếu. Văn bản tách phải lưu ngoài kho; không sao chép hoặc sửa EPUB gốc, không tải nguồn lên dịch vụ ngoài.
- **Kiểm tra mã đoạn:** phát hiện mã thiếu, trùng, sai thứ tự hoặc không khớp giữa danh mục đoạn, bản dịch và báo cáo; xuất kết quả kiểm tra vào `evals/` mà không chứa văn bản nguồn.
- **Dựng EPUB:** dựng sách tiếng Việt từ bản dịch đã duyệt, giữ thứ tự chương, mục lục và định dạng đã thống nhất; ghi sản phẩm vào `output/`, không thay đổi sách gốc.
