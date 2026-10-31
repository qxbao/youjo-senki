# Báo cáo tự kiểm & Sign-off (Translator Self-Check) — vol-05-ch-03-b10

- **Task ID**: `vol-05-ch-03-b10-translator-signoff`
- **Parent Task ID**: `vol-05-ch-03-b10`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN05/Text/part0018.html/p000342` -> `YS-LN05/Text/part0018.html/p000379` (38 đoạn)
- **Tệp bản dịch**: `translations/vol-05/ch-03-b10.jsonl`
- **Trạng thái**: `reviewed` (38/38 đoạn)

## 1. Xử lý các Findings từ Argon Review (`reviews/prose/vol-05/ch-03-b10-argon-review.yml`)
- **Finding 1 (`minor` — `YS-LN05/Text/part0018.html/p000358` & `p000353`)**:
  - **Vấn đề**: Trùng lặp đại từ `nó` vừa chỉ con tàu vừa chỉ Tanya theo `DEC-P01-001` trong cùng một câu.
  - **Giải quyết**:
    - Tại `p000353`: Đổi thành `nếu ở khoảng cách này mà nó đã nhìn thấy được thì hẳn mục tiêu đó phải khổng lồ lắm.`
    - Tại `p000358`: Đổi thành `Khi nghe anh ta bình luận về sự khổng lồ của con tàu, tất cả những gì nó có thể làm là gật đầu.`
- **Finding 2 (`minor` — `YS-LN05/Text/part0018.html/p000366`)**:
  - **Vấn đề**: Cụm `Các đơn vị tàu ngầm và không quân của Lục quân Đế quốc` gây cảm giác mâu thuẫn quân chủng.
  - **Giải quyết**: Cập nhật sang phương án thay thế đã có trong sổ pending và `locked_choices` là `Các đơn vị tàu ngầm và không quân của Quân đội Đế quốc`.
- **Finding 3 (`minor` — `YS-LN05/Text/part0018.html/p000376`)**:
  - **Vấn đề**: Câu thoại `Tôi đồng ý với anh, Thiếu tá.` thêm cụm `với anh` làm thu hẹp độ mở về chủ thể phát ngôn.
  - **Giải quyết**: Lược cụm `với anh` thành `Tôi đồng ý, Thiếu tá.` đúng theo khuyến nghị của Argon Review và `DEC-P01-001`.

## 2. Kiểm tra định dạng, bảo toàn mã đoạn, `locked_choices` và nhấn mạnh (`DEC-P01-002`)
- Tổng số dòng JSONL: 38/38 đoạn khớp chính xác thứ tự, `segment_id`, `source_sha256` và `glossary_version` từ handoff.
- Toàn bộ 38/38 dòng đã được cập nhật trường `status` từ `draft` sang `reviewed`.
- Tuân thủ toàn bộ 38 mục `locked_choices` và 13 mục `pending_term_recommendations` trong `ch-03-b10-argon-review.yml`.
- Bảo toàn chính xác nhấn mạnh `*...*` từ thẻ in nghiêng của nguồn tại 3 đoạn:
  - `YS-LN05/Text/part0018.html/p000355`: `RMS *Queen of Anjou*`
  - `YS-LN05/Text/part0018.html/p000362`: `*cung điện*`
  - `YS-LN05/Text/part0018.html/p000379`: `*tốc độ hành trình*` và `*tiết kiệm*`
- Các đoạn còn lại không có thẻ nhấn mạnh trong nguồn và hoàn toàn không tự thêm dấu `*`.
