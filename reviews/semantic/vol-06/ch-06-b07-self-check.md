# Báo cáo tự kiểm dịch thuật — `vol-06-ch-06-b07`

## 1. Phạm vi và trạng thái
- **Task ID:** `vol-06-ch-06-b07` / `vol-06-ch-06-b07-translator-signoff`
- **Tập / Chương:** `vol-06`, chương `6`
- **Mã đoạn:** `YS-LN06/Text/part0027.html/p000219` đến `YS-LN06/Text/part0027.html/p000258` (40 đoạn)
- **Tệp bản dịch:** `translations/vol-06/ch-06-b07.jsonl` (`status: reviewed`)
- **Review đối chiếu:** `reviews/prose/vol-06/ch-06-b07-argon-review.yml` (`findings: []`, tuân thủ toàn bộ `locked_choices` và `pending_term_recommendations`)

## 2. Kiểm tra điểm nhìn, đại từ và giọng điệu (`DEC-P01-001`)
- Toàn bộ lô là độc thoại nội tâm và lời lẩm bẩm một mình của Trung tá Tanya von Degurechaff khi đánh giá sự bế tắc chiến lược, cách cai trị lãnh thổ chiếm đóng thiếu kế hoạch của Lục quân Đế quốc và tâm lý chủ quan của dư luận Đế quốc.
- **Tự quy chiếu của Tanya:** dùng `mình` trong độc thoại nội tâm và câu tự nhủ (`p000222`, `p000228`, `p000249`, `p000251`); dùng `chúng ta` / `chúng tôi` theo đúng sắc thái tự nhủ hoặc nhận diện tập thể phía Đế quốc (`p000220`, `p000222`, `p000234`, `p000235`, `p000238`, `p000254`, `p000256`, `p000258`).
- **Quy chiếu khách quan:** gọi rõ tên `Tanya` ở các câu dẫn trần thuật chuyển nhịp (`p000223`, `p000249`), dùng `bạn` cho chủ ngữ giả định khái quát (`p000237`, `p000245`).

## 3. Kiểm tra nhấn mạnh (`DEC-P01-002`)
- Đã kiểm tra toàn bộ thẻ `<html:em>` trong nguồn và bảo toàn chính xác bằng dấu `*...*`:
  - `p000223`: `*Ưm…*`
  - `p000256`: `*Làm sao chúng ta có thể biện minh cho những hy sinh này ngoài mật ngọt của chiến thắng?*`
- Các đoạn còn lại không có thẻ nhấn mạnh trong nguồn và không tự thêm `*...*`.

## 4. Kiểm tra ngữ nghĩa, cấu trúc lập luận và thuật ngữ
- **Ngữ nghĩa & logic:**
  - Giữ nguyên cấu trúc tương phản không có thất bại chí mạng nhưng cũng không có thành công ở `p000219`.
  - Giữ đúng phép ẩn dụ y khoa (chữa triệu chứng/phần ngọn, thuốc giảm đau, phẫu thuật xâm lấn) từ `p000224` đến `p000227`.
  - Giữ nguyên các liên hệ lịch sử và quân sự: Machiavelli (`p000228`), Hannibal / Cannae / Pyrrhus / Rome / Maharbal (`p000246`–`p000251`), Hạng Vũ và Lưu Bang (`p000252`), cùng liên hệ kinh tế Nhật Bản với Hai mươi năm Mất mát / Ba mươi năm Mất mát (`p000258`).
- **Thuật ngữ đã đối chiếu với sổ pending:**
  - `Imperial Army`: `Lục quân Đế quốc`
  - `the Empire` / `imperial authorities`: `Đế quốc` / `giới chức Đế quốc`
  - `former Entente Alliance territory`: `lãnh thổ cựu Liên minh Hiệp ước`
  - `interior lines strategy`: `chiến lược nội tuyến`
  - `General Staff`: `Bộ Tổng tham mưu`
- **Đề xuất thuật ngữ / tên riêng mới (status: pending):**
  - `organizational theory` -> `lý thuyết tổ chức` (`p000241`)
  - `Hannibal` / `Cannae` / `Pyrrhus` / `Rome` / `Maharbal` -> `Hannibal` / `Cannae` / `Pyrrhus` / `Rome` / `Maharbal` (`p000246`, `p000250`, `p000251`)
  - `Xiang Yu and Liu Bang` -> `Hạng Vũ và Lưu Bang` (`p000252`)
  - `Lost Twenty Years` / `Lost Thirty Years` -> `Hai mươi năm Mất mát` / `Ba mươi năm Mất mát` (`p000258`)

## 5. Kết quả công cụ kiểm tra
- `validate_translation.py`: PASS (sẽ xác nhận qua lệnh chạy kiểm tra).
