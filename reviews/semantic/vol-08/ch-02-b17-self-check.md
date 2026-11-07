# Báo cáo tự kiểm dịch thuật — `vol-08-ch-02-b17`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-02-b17`
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter008.xhtml/p000326` đến `YS-LN08/Text/chapter008.xhtml/p000366` (41 đoạn)
- **Tệp đích**: `translations/vol-08/ch-02-b17.jsonl`
- **Trạng thái mỗi dòng**: `reviewed`

## 2. Kiểm tra tính đầy đủ và siêu dữ liệu
- **Số lượng đoạn**: Đủ 41/41 đoạn theo đúng thứ tự từ `p000326` đến `p000366`.
- **Trường dữ liệu**: Đầy đủ `segment_id`, `translation`, `status` (`reviewed`), `translator` (`argon-low`), `glossary_version`, `source_sha256`, `notes` (`[]`).
- **Bảo toàn nhấn mạnh (`DEC-P01-002`)**:
  - Chỉ đặt dấu sao `*...*` ở đúng 3 đoạn có thẻ nhấn mạnh trong nguyên bản:
    - `YS-LN08/Text/chapter008.xhtml/p000333`: Cụm cảnh báo được lặp lại ở đầu câu (*Chúng đang kéo tới, chúng đang kéo tới đấy*).
    - `YS-LN08/Text/chapter008.xhtml/p000344`: Giả định mang tính suy nghĩ viển vông (*Biết đâu chúng đã kiệt sức rồi*).
    - `YS-LN08/Text/chapter008.xhtml/p000354`: Hai cụm từ tu từ được đem ra so sánh (*gần như vô tận* và *vô hạn*).
  - Toàn bộ 38 đoạn còn lại tuyệt đối không tự ý thêm `*...*`.

## 3. Kiểm tra thuật ngữ và danh xưng
- **Thuật ngữ đã chốt và kế thừa từ các batch trước**:
  - `Thiếu tá Weiss` / `Weiss` (`p000330`, `p000343`, `p000356`, `p000357`)
  - `Cụm B` (`p000335`, `p000341`), `Cụm A` (`p000353`)
  - `viên sĩ quan phụ tá` (`p000339`), `Trung úy Serebryakov` (`p000363`)
  - `đơn vị quan sát` (`p000339`)
  - `trung đoàn tăng cường` (`p000340`)
  - `quân Liên bang` (`p000341`), `Quân đội Liên bang` (`p000341`, `p000349`), `Liên bang` (`p000354`)
  - `Trung tướng von Zettour` (`p000344`)
  - `suy nghĩ viển vông` (`p000344`)
  - `sư đoàn Cận vệ` / `các sư đoàn Cận vệ` (`p000345`, `p000346`, `p000349`, `p000355`)
  - `vị phó chỉ huy` (`p000348`)
  - `Tình báo Lục quân Đế quốc` (`p000349`), `Lục quân Đế quốc` (`p000355`), `Đế quốc` (`p000354`)
  - `Chiến dịch Andromeda` (`p000354`)
  - `trinh sát chiến đấu` (`p000356`)
  - `pháp sư` / `thiết giáp` (`p000356`), `pháp sư trên không` (`p000358`)
  - `sĩ quan cấp tá` (`p000357`)
  - `mặt trận Rhine` (`p000364`)

## 4. Kiểm tra xưng hô và giọng văn (`DEC-P01-001`)
- **Tường thuật và độc thoại của Tanya**:
  - Ngôi thứ ba gọi Tanya là `nó` (`p000339`, `p000348`) hoặc `Tanya` (`p000326`, `p000340`, `p000348`, `p000359`, `p000361`, `p000366`).
  - Độc thoại nội tâm của Tanya xưng `mình` (`p000336`, `p000344`, `p000358`, `p000366`) hoặc `chúng ta` khi tính cả đơn vị (`p000333`, `p000339`, `p000344`).
- **Đối thoại giữa Tanya, Thiếu tá Weiss và Trung úy Serebryakov (`p000329`–`p000365`)**:
  - Tanya nói với Weiss / thuộc cấp: xưng `tôi`, gọi `anh` / `Thiếu tá Weiss` (`p000330`, `p000332`, `p000334`, `p000337`, `p000343`, `p000346`, `p000349`, `p000351`, `p000353`, `p000359`). Ở `p000337`, đã bỏ tiểu từ `ạ` ở cuối câu hỏi về trinh sát không quân theo báo cáo review Argon để giữ đúng vị thế chỉ huy.
  - Tanya nói với Serebryakov: xưng `tôi`, gọi `cô` / `Trung úy Serebryakov` (`p000363`), và gọi chung cả hai thuộc cấp hiếu chiến là `lũ hiếu chiến các người` (`p000365`).
  - Weiss nói với Tanya: xưng `tôi` / `chúng ta`, gọi `ngài` / `thưa Trung tá`, giữ sắc thái tôn trọng cấp trên (`p000329`, `p000331`, `p000342`, `p000345`, `p000347`, `p000350`, `p000356`, `p000360`).
  - Serebryakov nói với Tanya: xưng `tôi` / `chúng ta`, giữ tiểu từ lễ phép `ạ` (`p000338`, `p000362`, `p000364`).

## 5. Xử lý phản biện Argon & Sign-off
- Đã tiếp nhận và xử lý finding mức `moderate` tại `YS-LN08/Text/chapter008.xhtml/p000337`: bỏ tiểu từ `ạ` ở cuối câu thoại của Tanya.
- Đã đối chiếu toàn bộ 13 mục `pending_term_recommendations` và 41 mục `locked_choices` trong `reviews/prose/vol-08/ch-02-b17-argon-review.yml`: tuân thủ 100%.
- Đã cập nhật `status` của toàn bộ 41 dòng trong `translations/vol-08/ch-02-b17.jsonl` từ `draft` sang `reviewed`.
