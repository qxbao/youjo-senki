# Báo cáo tự kiểm (Semantic Self-Check) — `vol-10-ch-03-b02` (Sign-off)

- **Task ID:** `vol-10-ch-03-b02-translator-signoff`
- **Parent Task ID:** `vol-10-ch-03-b02`
- **Translator:** `argon-low`
- **Phạm vi:** `YS-LN10/Text/chapter016.xhtml/p000022` .. `YS-LN10/Text/chapter016.xhtml/p000049` (28 đoạn)
- **Tệp đích:** `translations/vol-10/ch-03-b02.jsonl`
- **Glossary Version:** `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra tính đầy đủ và cấu trúc dữ liệu
- **Số lượng đoạn:** Đầy đủ 28/28 đoạn từ `p000022` đến `p000049`, khớp 1:1 với tệp nguồn.
- **Trạng thái & siêu dữ liệu:** Mọi dòng đã được cập nhật sang `status: "reviewed"`, giữ nguyên `translator: "argon-low"`, `source_sha256` và `glossary_version` khớp với handoff.
- **Nhấn mạnh (`DEC-P01-002`):** Bảo toàn chính xác đánh dấu `*...*` ở đúng 3 đoạn có thẻ nhấn mạnh trong nguồn:
  - `p000035`: `*ưu thế trên không*`
  - `p000039`: `*cử người đi thay mình*`
  - `p000045`: `*Kế hoạch B*`
  - Các đoạn còn lại không tự ý thêm dấu `*...*`.

## 2. Xử lý Findings từ Argon Review (`reviews/prose/vol-10/ch-03-b02-argon-review.yml`)
- **`p000023` (moderate):** Đổi đại từ xưng hô trong thoại của sĩ quan trực ban với Tanya từ `cô` thành `Trung tá` (`“Chà, Trung tá cũng biết tính vị tướng ấy thế nào rồi đấy.”`), đúng chuẩn quân ngũ và `DEC-P01-001`.
- **`p000024` (moderate):** Đổi `Tôi đã nghe kể tường tận về thói quen...` thành `Hồi ở miền nam tôi đã hiểu quá rõ thói quen bất chợt biến mất của ngài ấy rồi.` để phản ánh chính xác trải nghiệm thực tế trực tiếp của Tanya ở chiến trường miền nam (nhất quán với `p000029`).
- **`p000031` (moderate):** Đổi `bất cứ thứ gì mình cho là lãng phí` thành `bất cứ thứ gì ông ta cho là lãng phí` để phân tách rõ chủ thể ngôi thứ ba (Romel) với điểm nhìn ngôi thứ nhất (`mình` của Tanya).
- **`p000022` (minor):** Chỉnh `gặng hỏi` thành `hỏi dò thêm` và `gật gù đồng tình` thành `đáp lại đầy đồng tình` sát sắc thái gốc.
- **`p000040` (minor):** Đổi `chúng mình` thành `chúng ta` để giữ giọng độc thoại quân sự nhất quán với `p000028`.
- **`p000041` (minor):** Chỉnh `lại đến tận đó chỉ để thị sát trong muôn vàn việc khác` thành `lại đến tận đó chỉ để thị sát cơ chứ` để câu văn tự nhiên, thoát ý cảm thán.

## 3. Xưng hô, giọng điệu, thuật ngữ và Locked Choices
- Tuân thủ đầy đủ toàn bộ 28 mục `locked_choices` và 11 mục `pending_term_recommendations` trong `ch-03-b02-argon-review.yml`:
  - `sĩ quan trực ban` (`p000022`)
  - `các quân chủng` (`p000025`, `p000032`, `p000036`)
  - `Tướng Romel` / `Romel` / `vị tướng ấy` / `trung tướng của Lục quân Đế quốc` (`p000023`, `p000028`, `p000036`, `p000039`, `p000045`, `p000049`)
  - `chiến dịch cơ động` (`p000030`)
  - `mặt trận phía tây` (`p000035`)
  - `*ưu thế trên không*` (`p000035`)
  - `pháo phòng không` (`p000036`)
  - `Lục quân Đế quốc` / `Hải quân Đế quốc` (`p000036`, `p000038`)
  - `Bộ Tư lệnh Hạm đội` (`p000040`)
  - `Kế hoạch B` (`p000042`) và `*Kế hoạch B*` (`p000045`)
  - `Khối Thịnh vượng chung` (`p000048`)
