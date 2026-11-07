# Báo cáo tự kiểm (Self-Check): `vol-08-ch-03-b07`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-03-b07`
- **Phạm vi**: `YS-LN08/Text/chapter010.xhtml/p000191` → `YS-LN08/Text/chapter010.xhtml/p000227` (37 đoạn)
- **Tác tử**: `argon-low`
- **Tệp đầu ra**: `translations/vol-08/ch-03-b07.jsonl`

## 2. Kiểm tra tính đầy đủ & cấu trúc kỹ thuật
- Đã dịch đủ 37/37 đoạn theo đúng thứ tự và khớp hoàn toàn `segment_id` với tệp nguồn.
- Không tách dòng, không gộp đoạn, không bỏ sót câu hay mệnh đề nào.
- Trường `status` của toàn bộ 37 dòng đều được cập nhật từ `"draft"` sang `"reviewed"` sau khi Argon review xác nhận không có lỗi (`findings: []`) và toàn bộ bản dịch tuân thủ đầy đủ `locked_choices` cùng `pending_term_recommendations`.
- Trường `glossary_version` và `source_sha256` khớp chính xác với thông tin trong `handoffs/vol-08/ch-03-b07.yml`.
- Bảo toàn chính xác thẻ nhấn mạnh theo quy định `DEC-P01-002`: chỉ dùng `*...*` cho phần suy nghĩ nội tâm được in nghiêng ở đoạn `p000205`, không tự ý thêm dấu nhấn mạnh ở các đoạn khác.

## 3. Kiểm tra thuật ngữ, danh xưng & giọng văn
- **Thuật ngữ chuẩn và đề xuất đã đối chiếu**:
  - `Serebryakov` / `Lieutenant Serebryakov`: Serebryakov (`p000191`) / Trung úy Serebryakov (`p000205`)
  - `Grantz`: Grantz (`p000191`, `p000203`)
  - `Wüstemann` / `Lieutenant Wüstemann`: Wüstemann (`p000192`) / Trung úy Wüstemann (`p000201`, `p000205`)
  - `Major Weiss`: Thiếu tá Weiss (`p000201`)
  - `General von Zettour`: Tướng von Zettour (`p000203`)
  - `adjutant`: sĩ quan phụ tá (`p000205`)
  - `air superiority`: ưu thế trên không (`p000206`)
  - `replacement company`: đại đội bổ sung (`p000209`)
  - `Elinium Arms Type 97 Assault Computation Orbs`: những Quả cầu Tính toán Xung kích Type 97 của Elinium Arms (`p000210`)
  - `human capital`: vốn con người (`p000212`) — khớp với `P03-human-capital` trong `canon/glossary-pending.yml`
  - `Imperial Army` / `the Empire`: Lục quân Đế quốc (`p000214`, `p000220`) / Đế quốc (`p000220`)
  - `aerial mages`: pháp sư trên không (`p000214`)
  - `front lines` / `the front`: tiền tuyến (`p000215`) / tuyến đầu (`p000218`)
  - `Federation`: Liên bang (`p000219`, `p000220`, `p000221`)
  - `01`: 01 (`p000225`)
  - `optical sniper formulas`: thuật thức bắn tỉa quang học (`p000226`)
  - `tyranny of distance`: sự bạo ngược của khoảng cách (`p000226`)
  - `formula bullets`: đạn thuật thức (`p000227`)
- **Xưng hô và giọng nhân vật**:
  - Ngôi kể thứ ba gọi Tanya là `cô`, gọi Weiss là `anh ta` (`p000200`).
  - Trong độc thoại nội tâm (`p000200`, `p000202`, `p000203`, `p000207`, `p000209`, `p000214`, `p000216`, `p000219`, `p000223`, `p000227`), Tanya tự xưng `mình` (và `chúng tôi` / `chúng ta` khi bao gồm đơn vị hoặc quân đội Đế quốc), giữ rõ giọng điệu thực dụng, toan tính về quản trị nhân sự và hiệu suất chiến tranh.
  - Trong đối thoại, Tanya xưng `tôi` / `chúng tôi` / `chúng ta`, gọi Wüstemann là `Trung úy` / `Trung úy Wüstemann` / `anh`, gọi Weiss là `Thiếu tá` / `Thiếu tá Weiss` / `anh`, và gọi Serebryakov là `Trung úy Serebryakov` / `cô`.
  - Cấp dưới (Wüstemann, Weiss, Serebryakov) xưng `tôi`, gọi Tanya là `Trung tá` / `thưa Trung tá` / `ngài` (`p000194`, `p000196`, `p000198`, `p000204`) đúng chuẩn quân phong.

## 4. Điểm cần lưu ý cho bước duyệt tiếp theo
- Thuật ngữ mới ghi nhận bổ sung vào danh sách chờ xét:
  - `on-the-job training` → `đào tạo tại chỗ` (`p000202`)
  - `retention rate` → `tỷ lệ duy trì quân số` (`p000216`)
  - `meat shields` → `những tấm lá chắn thịt` (`p000216`)
- Không có vấn đề ngữ nghĩa hay xưng hô nào gây tắc nghẽn.
