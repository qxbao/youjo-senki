# Youjo Senki — dự án dịch light novel Anh–Việt

Kho này lưu quy chuẩn, bản dịch, báo cáo và bàn giao. Quy tắc đã duyệt sau
pilot nằm trong `canon/`; thuật ngữ chưa đủ căn cứ vẫn ở trạng thái chờ xét.

EPUB/PDF gốc nằm ở thư mục anh em `../youjo-senki-source/`. Chỉ đọc tại chỗ:
tuyệt đối không sao chép, sửa, đưa vào Git hay tải lên nơi khác. Không gửi nội dung
nguồn tới dịch vụ bên ngoài. Văn bản tách từ nguồn chỉ được lưu cục bộ trong
`work/` bị Git bỏ qua và không được đưa vào Git. `.gitignore` là lớp hỗ trợ, không thay thế quy tắc này.

Sao chép `project.local.example.yml` thành `project.local.yml` để cấu hình cục bộ.
Không sao chép sách nguồn. Công cụ chuẩn bị LN 01 và lệnh kiểm tra được mô tả
trong `tools/README.md`; công cụ dựng EPUB chưa được triển khai.

## Cấu trúc

| Thư mục | Mục đích |
| --- | --- |
| `canon/` | Thuật ngữ, nhân vật, văn phong và quyết định đã duyệt |
| `context/` | Ghi chú ngữ cảnh, không chép văn bản nguồn |
| `segments/` | Danh mục mã đoạn và vị trí đối chiếu, không lưu văn bản nguồn |
| `work/` | Văn bản nguồn làm việc cục bộ; toàn bộ thư mục được Git bỏ qua |
| `translations/` | Bản dịch tiếng Việt theo mã đoạn |
| `reviews/semantic/` | Báo cáo phản biện nghĩa |
| `reviews/prose/` | Báo cáo phản biện văn phong |
| `handoffs/` | Phạm vi công việc, quyền sửa và biên bản bàn giao |
| `evals/` | Tiêu chí và kết quả kiểm tra |
| `tools/` | Công cụ tách nguồn, kiểm tra danh mục và lập lô |
| `output/` | EPUB xuất cục bộ; toàn bộ thư mục được Git bỏ qua |

## Quy trình

Luồng lô chính thức: **lập lô → dịch Codex medium → kiểm tra tự động → phản
biện lấy mẫu Claude Sonnet → duyệt**. Chuẩn bị EPUB bằng adapter chung, ví dụ
`uv run python tools/extract_epub.py vol-02 --dry-run`, rồi lập lô một chương bằng
`uv run python tools/plan_batches.py vol-02 chapter-01`; xem
`tools/README.md` để chạy thử và kiểm tra. Bước lập lô chỉ tạo handoff metadata
và gói nguồn cục bộ. Kiểm tra tự động bản dịch và phản biện lấy mẫu là các
bước tiếp theo, không được thực hiện bởi công cụ lập lô. Đối chiếu nguồn
chỉ tại chỗ; không gửi nguồn đến dịch vụ bên ngoài. Điều phối viên duyệt
và nâng bản nháp thành bản chuẩn sau khi xử lý các vấn đề còn mở.

1. **Chuẩn bị:** cấu hình đường dẫn nguồn; đọc tại chỗ; lập danh mục mã đoạn ổn định và vị trí nguồn trong `segments/`, ghi ngữ cảnh trong `context/`. Ghi người giữ quyền sửa trong `handoffs/`.
2. **Dịch:** tác tử được giao quyền sửa viết vào `translations/`, theo mã đoạn và quy chuẩn trong `canon/`; ghi các điểm chưa rõ để xem xét.
3. **Phản biện nghĩa và văn phong:** người phản biện đối chiếu nguồn tại chỗ, chỉ ghi báo cáo vào hai thư mục `reviews/`. Mỗi vấn đề có mã đoạn, mức độ, lý do và đề xuất sửa.
4. **Sửa:** người giữ quyền sửa xử lý báo cáo, ghi kết quả hoặc lý do chưa tiếp nhận. Các lựa chọn cần thống nhất được đề xuất và duyệt trong `canon/decisions.md`.
5. **Kiểm tra:** kiểm tra mã đoạn thiếu/trùng, mức độ hoàn tất, tính nhất quán và các vấn đề phản biện còn mở; lưu kết quả trong `evals/`.
6. **Xuất EPUB:** khi nội dung đã được duyệt và có công cụ dựng, tạo EPUB tiếng Việt trong `output/`, kiểm tra cấu trúc và khả năng đọc. Không sửa sách gốc hoặc đưa sản phẩm xuất vào Git.

Đọc `AGENTS.md` trước khi làm việc. Toàn dự án chỉ có một tác tử được sửa
bản dịch tại một thời điểm; tác tử phản biện chỉ ghi báo cáo.
