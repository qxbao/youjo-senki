# Chuẩn bị LN 01

Chạy từ gốc kho, với `source_dir` trong `project.local.yml` trỏ đến thư mục
EPUB ngoài kho. Dùng môi trường và phụ thuộc hiện có trong `pyproject.toml`.

```sh
uv run python tools/extract_epub.py vol-01 --dry-run
uv run python tools/extract_epub.py vol-01
uv run python tools/validate_segments.py vol-01
```

Dry-run đọc và kiểm tra nhưng không tạo thư mục/tệp dữ liệu. Chạy thật tạo:

- `segments/vol-01/manifest.yml`: metadata, locator, markup dạng cấu trúc không
  chứa chữ nguồn, vị trí ảnh/pagebreak/space-break và liên kết chú thích; lưu Git.
- `work/vol-01/source.jsonl`: chữ và XHTML của từng p, chỉ cục bộ, Git bỏ qua.
  Không thêm bằng `git add -f`, sao chép sang thư mục được theo dõi hoặc tải lên.

Chỉ Chapter 0–V và 20 chú thích được lấy, theo spine. Tiêu đề chương không tạo
đơn vị văn bản trong bước này. Một p là một đơn vị, kể cả p trong li; ordinal
đếm mọi p theo DOM từng tài liệu, mã p có sáu chữ số. ID chú thích dùng ID p gốc.
Không lấy nội dung ngoài phạm vi, sao chép ảnh, OCR hoặc sửa EPUB.

SHA-256 nguồn được lưu trong manifest. Nếu bản nguồn đổi, lệnh từ chối ghi đè;
sau khi tự đối chiếu bản nguồn và tác động tới mã đoạn, có thể dùng:

```sh
uv run python tools/extract_epub.py vol-01 --force
```

`--force` chỉ bỏ chặn thay SHA; kiểm tra phạm vi/số đoạn vẫn bắt buộc. Cùng SHA
thì có thể chạy lại để tái tạo tệp. Nếu chạy bị gián đoạn giữa hai lần ghi tệp,
chạy lại rồi kiểm tra trước khi sử dụng dữ liệu. Chỉ hỗ trợ `vol-01`.

Công cụ dựng EPUB vẫn cần triển khai sau này; sản phẩm xuất sẽ nằm ở `output/`.
