# Báo cáo tự kiểm (Translator Self-Check) — `vol-07-ch-05-b02`

- **Task ID**: `vol-07-ch-05-b02`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN07/Text/chapter018.xhtml/p000033` – `YS-LN07/Text/chapter018.xhtml/p000062` (30 đoạn)
- **File đầu ra**: `translations/vol-07/ch-05-b02.jsonl`

## 1. Kiểm tra định lượng & cấu trúc
- Đã dịch đầy đủ 30/30 đoạn, giữ nguyên `segment_id` theo đúng thứ tự nguồn.
- Không gộp đoạn, không tách đoạn, không bỏ sót bất kỳ mệnh đề hay câu thoại nào.
- Tất cả các dòng đều có `status: "reviewed"`, `translator: "argon-low"`, khớp `source_sha256` và `glossary_version`.

## 2. Kiểm tra thuật ngữ, xưng hô & giọng văn
- **Bối cảnh & Nhân vật**: Cuộc trao đổi tại Moskva giữa Ủy viên Dân ủy Nội vụ Loria và vị đại tá giữ vai trò trợ lý sĩ quan liên lạc từ Bộ Tổng tham mưu Quân đội Liên bang.
- **Ngôi kể & Đại từ**:
  - Trần thuật ngôi thứ ba theo điểm nhìn Loria: gọi Loria là `Loria` / `gã`, gọi vị đại tá liên lạc là `vị đại tá` / `anh ta` / `người đàn ông kia` (nhất quán với các phân cảnh Loria ở tập 6).
  - Đối thoại giữa Loria và vị đại tá: xưng `tôi`, gọi đối phương là `đồng chí` / `Đồng chí Đại tá` / `Đồng chí Loria`, giữ đúng sắc thái chính trị - quan trường Liên bang: Loria bề ngoài tỏ vẻ ôn tồn, thân mật nhưng ẩn chứa áp lực thanh trừng, trong khi vị đại tá căng thẳng, dè dặt trước người đứng đầu Bộ Dân ủy Nội vụ.
- **Thuật ngữ**:
  - `Bộ Dân ủy Nội vụ`, `Bộ Tổng tham mưu`, `Văn phòng Bộ Tổng tham mưu`, `Bộ Tổng tham mưu Quân đội Liên bang`, `chính ủy`, `trợ lý sĩ quan liên lạc`, `sĩ quan liên lạc`, `rút lui chiến thuật`, `học thuyết` / `học thuyết tác chiến`, `Đảng`, `tổ quốc`, `*lageri*` đều bám sát quy chuẩn canon và các đề xuất đã thống nhất trong sổ thuật ngữ.

## 3. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002`)
- Đã đối chiếu toàn bộ các thẻ in nghiêng từ `text_xml`:
  - `YS-LN07/Text/chapter018.xhtml/p000034`: bảo toàn nhấn mạnh ở cụm `*về cơ bản*`.
  - `YS-LN07/Text/chapter018.xhtml/p000041`: bảo toàn nhấn mạnh ở từ `*Nhỏ*` (đối ứng trực tiếp với từ `nhỏ` trong lời vị đại tá ở đoạn `p000040`).
  - `YS-LN07/Text/chapter018.xhtml/p000042`: bảo toàn nhấn mạnh ở từ `*nhỏ*`.
  - `YS-LN07/Text/chapter018.xhtml/p000054`: bảo toàn nhấn mạnh ở thuật ngữ ngoại lai `*lageri*`.
- Các đoạn còn lại không có thẻ nhấn mạnh trong nguồn và không tự ý thêm dấu `*...*`.

## 4. Xử lý Argon Review Sign-off (`vol-07-ch-05-b02-translator-signoff`)
- `YS-LN07/Text/chapter018.xhtml/p000036`: Đã đổi `"Cuộc thẩm vấn này"` thành `"Việc tìm hiểu này"` để khớp với ngữ điệu trấn an của Loria.
- `YS-LN07/Text/chapter018.xhtml/p000044`: Đã đổi `"một thứ thuốc phiện giả cầy"` thành `"một thứ thuốc phiện trá hình"` để giữ thanh điệu chính luận và đối ứng chuẩn xác với `"liều thuốc vạn năng"`.
- Đã kiểm tra và tuân thủ đầy đủ mọi `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-07/ch-05-b02-argon-review.yml`.
- Đã cập nhật toàn bộ 30/30 dòng trong `translations/vol-07/ch-05-b02.jsonl` từ `status: "draft"` sang `status: "reviewed"`.
