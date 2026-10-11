# Youjo Senki — dự án dịch light novel Anh–Việt

Kho này lưu quy chuẩn, bản dịch, báo cáo và bàn giao. Chưa có nội dung dịch
hoặc thuật ngữ riêng nào được chốt trong bước thiết lập.

EPUB/PDF gốc nằm ở thư mục anh em `../youjo-senki-source/`. Chỉ đọc tại chỗ:
tuyệt đối không sao chép, sửa, đưa vào Git hay tải lên nơi khác. Không gửi nội dung
nguồn tới dịch vụ bên ngoài. Văn bản tách từ nguồn cũng phải được lưu cục bộ
ngoài kho và không được đưa vào Git. `.gitignore` là lớp hỗ trợ, không thay thế quy tắc này.

Sao chép `project.local.example.yml` thành `project.local.yml` để cấu hình cục bộ.
Không sao chép sách nguồn. Chưa có công cụ xử lý EPUB ở giai đoạn này.

## Cấu trúc

| Thư mục | Mục đích |
| --- | --- |
| `canon/` | Thuật ngữ, nhân vật, văn phong và quyết định đã duyệt |
| `context/` | Ghi chú ngữ cảnh, không chép văn bản nguồn |
| `segments/` | Danh mục mã đoạn và vị trí đối chiếu, không lưu văn bản nguồn |
| `translations/` | Bản dịch tiếng Việt theo mã đoạn |
| `reviews/semantic/` | Báo cáo phản biện nghĩa |
| `reviews/prose/` | Báo cáo phản biện văn phong |
| `handoffs/` | Phạm vi công việc, quyền sửa và biên bản bàn giao |
| `evals/` | Tiêu chí và kết quả kiểm tra |
| `tools/` | Tài liệu công cụ cần xây dựng sau này |
| `output/` | EPUB xuất cục bộ; toàn bộ thư mục được Git bỏ qua |

## Quy trình

1. **Chuẩn bị:** cấu hình đường dẫn nguồn; đọc tại chỗ; lập danh mục mã đoạn ổn định và vị trí nguồn trong `segments/`, ghi ngữ cảnh trong `context/`. Ghi người giữ quyền sửa trong `handoffs/`.
2. **Dịch:** tác tử được giao quyền sửa viết vào `translations/`, theo mã đoạn và quy chuẩn trong `canon/`; ghi các điểm chưa rõ để xem xét.
3. **Phản biện nghĩa và văn phong:** người phản biện đối chiếu nguồn tại chỗ, chỉ ghi báo cáo vào hai thư mục `reviews/`. Mỗi vấn đề có mã đoạn, mức độ, lý do và đề xuất sửa.
4. **Sửa:** người giữ quyền sửa xử lý báo cáo, ghi kết quả hoặc lý do chưa tiếp nhận. Các lựa chọn cần thống nhất được đề xuất và duyệt trong `canon/decisions.md`.
5. **Kiểm tra:** kiểm tra mã đoạn thiếu/trùng, mức độ hoàn tất, tính nhất quán và các vấn đề phản biện còn mở; lưu kết quả trong `evals/`.
6. **Xuất EPUB:** khi nội dung đã được duyệt và có công cụ dựng, tạo EPUB tiếng Việt trong `output/`, kiểm tra cấu trúc và khả năng đọc. Không sửa sách gốc hoặc đưa sản phẩm xuất vào Git.

Đọc `AGENTS.md` trước khi làm việc. Toàn dự án chỉ có một tác tử được sửa
bản dịch tại một thời điểm; tác tử phản biện chỉ ghi báo cáo.
