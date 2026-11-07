# Báo cáo tự kiểm (Self-Check) — `vol-08-ch-06-b06` (Sign-off)

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-06-b06-translator-signoff` (parent: `vol-08-ch-06-b06`)
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter022.xhtml/p000194` đến `YS-LN08/Text/chapter022.xhtml/p000226` (33 đoạn)
- **Tệp bản dịch**: `translations/vol-08/ch-06-b06.jsonl`
- **Báo cáo phản biện đối chiếu**: `reviews/prose/vol-08/ch-06-b06-argon-review.yml`

## 2. Kiểm tra tính đầy đủ & siêu dữ liệu (Sign-off)
- **Số dòng JSONL**: 33/33 đoạn, khớp 1-1 với tệp nguồn.
- **Trạng thái (`status`)**: Đã cập nhật toàn bộ 33/33 dòng từ `"draft"` sang `"reviewed"`.
- **Xử lý phản biện (`argon-review`)**:
  - Số lỗi (`findings`): 0 (`serious: 0`, `moderate: 0`, `minor: 0`).
  - Toàn bộ `pending_term_recommendations` và `locked_choices` cho 33 đoạn (`p000194` – `p000226`) trong `ch-06-b06-argon-review.yml` đã được kiểm tra và tuân thủ chính xác.
- **Khóa định danh & băm**: `segment_id`, `source_sha256` và `glossary_version` khớp chính xác với `handoffs/vol-08/ch-06-b06.yml`.
- **Không sót đoạn / không gộp tách đoạn**: Giữ nguyên ranh giới của từng đoạn văn và lời thoại.

## 3. Kiểm tra quy chuẩn xưng hô, giọng điệu và mạch trần thuật (`DEC-P01-001`)
- **Mạch trần thuật ngôi thứ ba (`p000197`, `p000208`, `p000217`, `p000224`, `p000226`)**:
  - Tiếp nối nhất quán với các batch trước của tập 8 (`ch-06-b05`), gọi Tanya bằng tên riêng hoặc đại từ `cô`, gọi cấp dưới (`Grantz`, `Weiss`, `Serebryakov`) là `anh ta` / `thuộc cấp của mình` / `binh sĩ thuộc quyền`.
- **Mạch độc thoại nội tâm & suy tính chiến thuật của Tanya (`p000194` – `p000195`, `p000198`, `p000200` – `p000201`, `p000203` – `p000204`, `p000209` – `p000210`, `p000212` – `p000214`, `p000216`, `p000218`, `p000220` – `p000223`)**:
  - Tự quy chiếu cá nhân bằng `mình` / `bản thân`.
  - Khi suy tính chung về đơn vị, quyền lợi sĩ quan hoặc hoạt động tác chiến của tiểu đoàn, dùng `chúng ta` / `chúng mình` (trong suy nghĩ nội tâm) và `chúng tôi` (trong trần thuật ngôi thứ nhất số nhiều ở `p000222`).
- **Mạch đối thoại giữa Tanya và các thuộc cấp (`p000196`, `p000199`, `p000202`, `p000205` – `p000207`, `p000211`, `p000215`, `p000219`, `p000224` – `p000225`)**:
  - Tanya giữ giọng chỉ huy thực dụng, quyết đoán, xưng `chúng ta`, gọi cấp dưới bằng tên (`Grantz`, `Weiss`) hoặc `anh` (`p000211`).
  - Grantz giữ vẻ hăng hái, nôn nóng muốn truy kích quân địch (`p000205`, `p000207`, `p000215`, `p000225`).

## 4. Kiểm tra định dạng nhấn mạnh (`DEC-P01-002`)
- Chỉ bảo toàn định dạng in nghiêng (`*...*`) tại đúng 1 vị trí có thẻ nhấn mạnh trong nguyên bản XHTML:
  1. `p000194`: Âm tiết chơi chữ trong độc thoại của Tanya (`*mee*`).
- Toàn bộ 32 đoạn còn lại không có nhấn mạnh trong nguồn và không tự ý thêm bất kỳ dấu `*...*` nào.

## 5. Kiểm tra thuật ngữ & đối chiếu Canon / Pending Terms
- Các thuật ngữ đã có trong sổ pending được áp dụng nhất quán:
  - `Đám Ăng-lê và lũ Cộng sản`, `Khối Thịnh vượng chung`, `Liên bang`, `Người Ildoa`.
  - `Trung úy Serebryakov`, `Grantz`, `Weiss`, `Zettour`.
  - `trận truy kích`, `đòn nghi binh`, `công đoàn`, `máy bay tiêm kích`, `thuật thức phát nổ`, `hạm đội hiện hữu`, `Type 97`, `chương trình giáo dục bắt buộc`, `chương trình đào tạo sĩ quan tham mưu`, `đạn thuật thức`, `thuật thức bắn tỉa quang học`, `pháp sư trên không`, `ba lô`.
- Các đề xuất thuật ngữ mới trong lô (`pending_terms`):
  - `p000203`: `quyền thương lượng tập thể` (cho quyền đàm phán tập thể của người lao động/công chức).
  - `p000203`, `p000204`: `thanh tra tiêu chuẩn lao động` (chức danh thanh tra giám sát tiêu chuẩn lao động).
  - `p000205`: `chế áp diện rộng trong không gian` (đòn chế áp khu vực không gian bằng thuật thức phát nổ).
  - `p000209`: `tác chiến phòng không` (hoạt động giao chiến chống máy bay địch).
  - `p000218`: `bán phá giá` (thuật ngữ kinh tế chỉ hành vi hạ giá bán sức lao động dưới mức giá trị thực).

## 6. Kết quả chạy công cụ kiểm tra
- Chạy `python3 tools/validate_translation.py --handoff handoffs/vol-08/ch-06-b06.yml --source work/vol-08/batches/ch-06-b06-source.jsonl --translation translations/vol-08/ch-06-b06.jsonl` đạt kết quả `PASS`.
