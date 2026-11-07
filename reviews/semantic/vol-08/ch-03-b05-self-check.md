# Báo cáo tự kiểm (Self-Check): `vol-08-ch-03-b05`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-03-b05`
- **Phạm vi**: `YS-LN08/Text/chapter010.xhtml/p000112` → `YS-LN08/Text/chapter010.xhtml/p000154` (43 đoạn)
- **Tác tử**: `argon-low`
- **Tệp đầu ra**: `translations/vol-08/ch-03-b05.jsonl`

## 2. Kiểm tra tính đầy đủ & cấu trúc kỹ thuật
- Đã dịch đủ 43/43 đoạn theo đúng thứ tự và khớp hoàn toàn `segment_id` với tệp nguồn.
- Không tách dòng, không gộp đoạn, không bỏ sót bất kỳ câu hoặc mệnh đề nào.
- Trường `status` của toàn bộ 43 dòng đều đã được cập nhật thành `"reviewed"` sau khi đối chiếu với `reviews/prose/vol-08/ch-03-b05-argon-review.yml` (0 lỗi, tuân thủ đầy đủ `locked_choices` và `pending_term_recommendations`).
- Trường `glossary_version` và `source_sha256` khớp chính xác với thông tin trong `handoffs/vol-08/ch-03-b05.yml`.
- Bảo toàn chính xác thẻ nhấn mạnh theo quy định `DEC-P01-002`: chỉ sử dụng dấu `*...*` ở hai đoạn duy nhất có thẻ nhấn mạnh trong nguyên bản (`p000116` và `p000149`), không tự ý thêm in nghiêng ở các đoạn độc thoại nội tâm khác.

## 3. Kiểm tra thuật ngữ, danh xưng & giọng văn
- **Thuật ngữ chuẩn và đề xuất đã đối chiếu**:
  - `eastern army`: đạo quân phía đông (`p000115`)
  - `the academy`: học viện (`p000116`)
  - `vanguard`: đội tiên phong (`p000120`)
  - `THE EASTERN FRONT` / `eastern front`: MẶT TRẬN PHÍA ĐÔNG (`p000123`) / mặt trận phía đông (`p000144`)
  - `Imperial Army`: Lục quân Đế quốc (`p000124`, `p000125`)
  - `Soldim 528`: Soldim 528 (`p000124`, `p000125`, `p000126`, `p000149`)
  - `Federation`: Liên bang (`p000124`, `p000144`)
  - `Operation Iron Hammer`: Chiến dịch Búa Sắt (`p000125`)
  - `Operation Andromeda`: Chiến dịch Andromeda (`p000125`)
  - `A Group`: Cụm A (`p000125`)
  - `Lieutenant Colonel Tanya von Degurechaff`: Trung tá Tanya von Degurechaff (`p000126`)
  - `First Lieutenant Serebryakov` / `Lieutenant`: Trung úy Serebryakov (`p000126`) / Trung úy (`p000130`)
  - `Major Weiss`: Thiếu tá Weiss (`p000133`)
  - `adjutant`: viên sĩ quan phụ tá (`p000135`)
  - `John Bulls`: đám John Bull (`p000137`)
  - `Commies`: đám Cộng sản (`p000137`)
  - `international Communists`: đám Cộng sản quốc tế (`p000139`)
  - `the Rhine`: mặt trận Rhine (`p000148`)
  - `aerial superiority`: ưu thế trên không (`p000150`)
  - `Captain Meybert`: Đại úy Meybert (`p000152`)
- **Xưng hô và giọng nhân vật**:
  - Phân cảnh hội nghị tại Cụm B (`p000112`–`p000122`): Các sĩ quan tham mưu gọi Zettour là `thưa Tướng quân`, xưng `chúng ta`. Zettour xưng `tôi`, gọi các sĩ quan là `các vị`, giữ thái độ thực dụng, lạnh lùng và quyết đoán.
  - Phân cảnh tại cứ điểm Soldim 528 (`p000124`–`p000154`): Ngôi kể thứ ba gọi Tanya và Serebryakov là `cô`, gọi Weiss là `anh`. Trong độc thoại nội tâm (`p000129`, `p000135`, `p000144`, `p000154`), Tanya tự xưng `mình` (và `tất cả chúng tôi` khi nói chung toàn quân ở `p000144`), thể hiện rõ nét giọng điệu châm biếm, thực dụng và ghét rủi ro nơi tiền tuyến. Trong đối thoại, Tanya xưng `tôi`, gọi Serebryakov là `Trung úy`, gọi Weiss là `Thiếu tá Weiss` / `anh`; Serebryakov và Weiss xưng `tôi`, gọi Tanya là `thưa Trung tá` / `Trung tá` / `ngài`.

## 4. Điểm cần lưu ý cho bước duyệt tiếp theo
- Không có thuật ngữ mới gây tắc nghẽn. Các lựa chọn từ vựng và xưng hô đều bám sát ngữ cảnh các batch trước của Chương 3 (`ch-03-b01` → `ch-03-b04`) và sổ cái thuật ngữ hiện hành.
