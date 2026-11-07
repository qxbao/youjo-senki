# Báo cáo tự kiểm (Semantic Self-Check) — `vol-08-ch-04-b06`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-04-b06`
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter014.xhtml/p000169` – `YS-LN08/Text/chapter014.xhtml/p000207` (39 đoạn)
- **Tệp đích**: `translations/vol-08/ch-04-b06.jsonl`

## 2. Kiểm tra đối chiếu quy chuẩn & thuật ngữ
- **Ngôi kể và điểm nhìn (`DEC-P01-001`)**:
  - Phân biệt rõ ràng giữa trần thuật ngôi thứ ba bám sát điểm nhìn của Tanya (`Tanya`, `cô`) ở các đoạn `p000172`, `p000173`, `p000177`, `p000180`, `p000182`, `p000185`, `p000189`, `p000191`, `p000194`, `p000196`, `p000198`, `p000199` và độc thoại nội tâm / nhận xét tổng quát của Tanya (`chúng tôi`, `chúng ta`) ở các đoạn `p000170`, `p000173`, `p000174`, `p000183`, `p000184`, `p000185`, `p000186`, `p000192`, `p000195`, `p000201`, `p000202`, `p000203`, `p000206`.
- **Xưng hô trong hội thoại**:
  - Giữa Thiếu tá Weiss và Tanya (`p000169`): Weiss xưng `chúng tôi`, giọng ngập ngừng tuân lệnh.
  - Giữa Tanya và Trung úy Serebryakov (`p000178`–`p000181`, `p000187`–`p000191`, `p000193`): Tanya tự xưng `tôi` / `chúng ta`, gọi Serebryakov là `cô`, `*Trung úy Pháp sư*`, `Trung úy Serebryakov`; Serebryakov gọi Tanya là `Trung tá` (`thưa Trung tá`), lễ phép (`ạ`).
  - Lệnh chỉ huy của Tanya cho đơn vị (`p000175`, `p000197`, `p000207`): Tanya xưng `tôi` / `01` / `chúng ta`, giọng chỉ huy dứt khoát và pha chút hài hước khô khan ở `p000207`.
- **Bảo toàn nhấn mạnh (`DEC-P01-002`)**:
  - Đoạn `p000180`: bảo toàn cụm nhấn mạnh bằng `*Trung úy Pháp sư*`.
  - Đoạn `p000200`: bảo toàn cụm từ tượng thanh nhấn mạnh bằng `*Pằng, pằng-pằng-pằng.*`.
  - Tất cả các đoạn còn lại không có nhấn mạnh trong nguồn và không dùng dấu `*...*`.
- **Thuật ngữ và tên riêng (`pending_terms` & `glossary`)**:
  - Tuân thủ nhất quán các phương án đã có trong tập 8 và các tập trước: `Tospan` / `Trung úy Tospan`, `Serebryakov` / `Trung úy Serebryakov`, `Tướng von Zettour`, `sĩ quan phụ tá`, `Liên bang`, `sĩ quan ma pháp`, `khẩu tiểu liên`, `đạn thuật thức`, `thuật thức phát nổ`, `01`.
  - Đề xuất thuật ngữ / cấp bậc trong lô: `*Trung úy Pháp sư*` (`p000180`).

## 3. Tự kiểm tra kỹ thuật & Sign-off
- Đủ 39/39 dòng JSONL, khớp thứ tự `segment_id` từ `p000169` đến `p000207`.
- Đã đối chiếu báo cáo `reviews/prose/vol-08/ch-04-b06-argon-review.yml`: 0 lỗi (`findings: []`), toàn bộ `pending_term_recommendations` và `locked_choices` từ `p000169` đến `p000207` đều đã được tuân thủ đầy đủ.
- Trường `status` của toàn bộ 39 dòng đã được cập nhật từ `"draft"` sang `"reviewed"`, `translator` là `"argon-low"`, khớp `source_sha256` và `glossary_version` trong handoff.
- Không chép văn bản nguồn tiếng Anh vào bản dịch hoặc báo cáo tự kiểm.
