# Báo cáo tự kiểm (Self-Check): `vol-06-ch-09-b01`

- **Task ID**: `vol-06-ch-09-b01` (Sign-off: `vol-06-ch-09-b01-translator-signoff`)
- **Translator**: `argon-low`
- **Handoff**: `handoffs/vol-06/ch-09-b01.yml` / `handoffs/vol-06/ch-09-b01-translator-signoff.yml`
- **Báo cáo review**: `reviews/prose/vol-06/ch-09-b01-argon-review.yml`
- **Tệp dịch**: `translations/vol-06/ch-09-b01.jsonl`
- **Phạm vi**: `YS-LN06/Text/part0037.html/p000001` → `YS-LN06/Text/part0037.html/p000003` (3 đoạn)
- **Trạng thái mỗi dòng**: `reviewed`

## 1. Kiểm tra tính đầy đủ và nghĩa gốc
- Đã dịch đầy đủ toàn bộ 3 đoạn từ `part0037.html/p000001` đến `part0037.html/p000003` (trang thông báo đăng ký nhận bản tin cuối sách của nhà xuất bản Yen Press ở cuối Tập 6).
- Giữ nguyên nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic nhân quả và thời gian của giả định:
  - **Lời mời đăng ký nhận bản tin (`p000001`)**: Nêu rõ mục đích nhận tin tức về các bộ manga, tiểu thuyết đồ họa và light novel mới nhất từ Yen Press, đi kèm những ưu đãi đặc biệt và nội dung độc quyền, đồng thời truyền đạt lời mời đăng ký nhận bản tin của Yen Press.
  - **Nút hành động (`p000002`)**: Dịch gọn, chuẩn xác nhãn nút kêu gọi đăng ký.
  - **Chỉ dẫn truy cập trang mạng (`p000003`)**: Giữ nguyên lựa chọn thay thế là ghé thăm nhà xuất bản tại địa chỉ đường dẫn `www.yenpress.com/booklink`.
- Tuyệt đối không sao chép câu hoặc cụm từ nguồn tiếng Anh vào báo cáo.

## 2. Kiểm tra đại từ, xưng hô và giọng văn (`DEC-P01-001`)
- Đây là trang thông tin cuối sách của nhà xuất bản Yen Press (ngoài cốt truyện chính của Tanya), do đó không áp dụng đại từ `nó` của Tanya trong `DEC-P01-001`:
  - Nhà xuất bản tự xưng `chúng tôi` ở `p000003`.
  - Câu cầu khiến lịch sự, tự nhiên, đúng chuẩn văn phong xuất bản phẩm thương mại ở `p000001`–`p000003`.

## 3. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002`)
- Đối chiếu toàn bộ 3 đoạn với XHTML nguồn: không có đoạn nào chứa thẻ `<html:em>` hay `<html:i>`, nên bản dịch hoàn toàn không dùng dấu `*...*`, đảm bảo tuân thủ nghiêm ngặt `DEC-P01-002`.

## 4. Kiểm tra thuật ngữ và tên riêng (`canon/` & `work/run-state/pending-terms-index.yml`)
- Giữ nguyên tên nhà xuất bản `Yen Press`, thuật ngữ quen thuộc `manga`, `light novel` và địa chỉ liên kết `www.yenpress.com/booklink`; ghi nhận đề xuất thuật ngữ xuất bản ở `p000001` (`tiểu thuyết đồ họa`, `bản tin`).

## 5. Kiểm tra định dạng, Sign-off và công cụ xác thực
- Báo cáo `reviews/prose/vol-06/ch-09-b01-argon-review.yml` có 0 finding (`serious: 0, moderate: 0, minor: 0`) và 0 `pending_term_recommendations`; toàn bộ `locked_choices` từ `p000001` đến `p000003` đã được giữ nguyên nhất quán.
- Tệp `translations/vol-06/ch-09-b01.jsonl` gồm đúng 3 dòng JSONL hợp lệ, đầy đủ các trường bắt buộc (`segment_id`, `translation`, `status: "reviewed"`, `translator: "argon-low"`, `glossary_version`, `source_sha256`, `notes: []`).
- Chạy `python3 tools/validate_translation.py --handoff handoffs/vol-06/ch-09-b01.yml --source work/vol-06/batches/ch-09-b01-source.jsonl --translation translations/vol-06/ch-09-b01.jsonl` đạt `PASS`.
