# Báo cáo tự kiểm (Semantic Self-Check) — `vol-08-ch-04-b08`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-04-b08`
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter014.xhtml/p000255` – `YS-LN08/Text/chapter014.xhtml/p000292` (38 đoạn)
- **Tệp đích**: `translations/vol-08/ch-04-b08.jsonl`

## 2. Kiểm tra đối chiếu quy chuẩn & thuật ngữ
- **Ngôi kể và điểm nhìn (`DEC-P01-001`)**:
  - Phân biệt rõ ràng giữa trần thuật ngôi thứ ba bám sát điểm nhìn của Tanya (`Tanya`, `cô`) ở các đoạn `p000255`, `p000257`, `p000260`, `p000265`, `p000268`, `p000272`, `p000273`, `p000275`, `p000276`, `p000278`, `p000280`, `p000284`, `p000288`, `p000291`, `p000292` và độc thoại nội tâm / nhận xét trực tiếp của Tanya (`mình`, `chúng ta`) ở các đoạn `p000259`, `p000263`–`p000265`, `p000277`, `p000281`, `p000284`, `p000288`.
- **Xưng hô trong hội thoại**:
  - Giữa Tanya và Trung úy Wüstemann (`p000255`–`p000272`, `p000276`, `p000289`): Tanya tự xưng `tôi` / `chúng ta`, gọi cấp dưới là `Trung úy Wüstemann`, `Trung úy`, `anh`; Wüstemann gọi Tanya là `Trung tá` (`thưa Trung tá`, `ngài`), tự xưng `tôi` / `mình`, giữ sắc thái lễ phép (`ạ`).
  - Giữa Tanya và Trung úy Tospan (`p000273`–`p000274`, `p000279`, `p000282`–`p000283`, `p000285`–`p000287`, `p000289`–`p000291`): Tanya tự xưng `tôi` / `chúng ta`, gọi Tospan là `Trung úy Tospan`, `anh`, gọi chung cả hai là `Hai Trung úy`; Tospan gọi Tanya là `Trung tá` (`thưa Trung tá`), tự xưng `tôi` / `chúng ta`, giữ sắc thái lễ phép (`ạ`).
- **Bảo toàn nhấn mạnh (`DEC-P01-002`)**:
  - Đoạn `p000281`: bảo toàn toàn bộ câu hỏi nội tâm nhấn mạnh bằng `*Một lời đề xuất ư? Từ Tospan sao?*`.
  - Tất cả 37 đoạn còn lại không có nhấn mạnh trong nguồn và không dùng dấu `*...*`.
- **Thuật ngữ và tên riêng (`pending_terms` & `glossary`)**:
  - Tuân thủ nhất quán các phương án đã có trong tập 8 và các tập trước: `Trung úy Wüstemann` / `Wüstemann`, `Trung úy Tospan` / `Tospan`, `Trung tá`, `Weiss`, `Kampfgruppe Salamander`, `sở chỉ huy`, `Quân đội Liên bang`, `vốn con người`, `Lục quân Đế quốc`, `vành đai phòng ngự vòng ngoài`, `vị trí tiền tiêu`, `trận đánh trì hoãn`, `vật tư và trang bị quân sự`, `Serebryakov`.
  - Đề xuất thuật ngữ mới trong lô: `đầu máy và toa xe chở hàng` (`p000289`).

## 3. Tự kiểm tra kỹ thuật
- Đủ 38/38 dòng JSONL, khớp thứ tự `segment_id` từ `p000255` đến `p000292`.
- Trường `status` của toàn bộ 38 dòng đã được cập nhật từ `"draft"` sang `"reviewed"` sau khi hoàn tất đối chiếu với báo cáo `ch-04-b08-argon-review.yml` (0 lỗi, khớp toàn bộ `pending_term_recommendations` và `locked_choices`), `translator` là `"argon-low"`, khớp `source_sha256` và `glossary_version` trong handoff.
- Không chép văn bản nguồn tiếng Anh vào bản dịch hoặc báo cáo tự kiểm.
