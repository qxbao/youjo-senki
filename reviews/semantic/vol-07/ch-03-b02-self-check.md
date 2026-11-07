# Báo cáo tự kiểm dịch thuật — `vol-07-ch-03-b02`

## 1. Thông tin chung
- **Task ID**: `vol-07-ch-03-b02`
- **Translator**: `argon-low` (`translator_luna`)
- **Phạm vi**: `YS-LN07/Text/chapter010.xhtml/p000033` đến `YS-LN07/Text/chapter010.xhtml/p000064` (32 phân đoạn)
- **Tệp bản dịch**: `translations/vol-07/ch-03-b02.jsonl`

## 2. Tự kiểm ngữ nghĩa, giả định, phủ định và quan hệ nhân quả
- **`p000033`–`p000046`**: Cuộc trao đổi ngoại giao mật giữa Tướng Igor Gassman (Quân đội Hoàng gia Ildoa) và Đại tá von Lergen (Bộ Tổng tham mưu Đế quốc). Đã bảo toàn đầy đủ sắc thái mỉa mai lịch thiệp và ẩn ý ngoại giao:
  - Các điều kiện ngừng bắn Đế quốc đưa ra (đòi bồi thường chiến phí, yêu sách lãnh thổ, mặc định đã tổ chức trưng cầu dân ý tại chỗ ở các vùng chiếm đóng) được dịch sát nghĩa và giữ nguyên cặp dấu nháy đơn trích dẫn trong lời thoại ở `p000033` và `p000040`.
  - Lập luận nội tâm của Lergen ở `p000036`–`p000037` về thượng lệnh từ bản quốc nhằm bảo đảm không gian an toàn / vùng đệm an toàn cho dù lợi ích lãnh thổ thu về có bị ép xuống mức tối thiểu được giữ đúng quan hệ nhượng bộ.
  - Ở `p000042`–`p000046`, sự chuyển dịch từ đàm phán công khai sang cuộc họp cấp chuyên viên và màn tung hứng câu chữ giữa Gassman với Lergen để tìm điểm chung đã được diễn đạt rõ ràng, không làm lệch chủ thể phát ngôn.
- **`p000047`–`p000052`**: Nội tâm và lời độc thoại của Lergen trên đường rời văn phòng Tướng Gassman trở về đại sứ quán Đế quốc. Giữ đúng cấu trúc câu giả định tiếc nuối ở `p000050` (mong muốn được ở lại mặt trận phía đông và đích thân chỉ huy `Kampfgruppe Lergen` thay vì chỉ là chỉ huy trên danh nghĩa như ở `p000051`).
- **`p000053`–`p000064`**: Cảnh họp tại Phòng Tác chiến ở Thủ đô Đế quốc Berun ngày 1 tháng 5 năm Thống nhất 1927 giữa Trung tướng von Rudersdorf, Trung tướng von Zettour và sĩ quan Cục Tác chiến:
  - Giữ đúng tương phản giữa tin mừng chiến thuật (chặn đứng cuộc tổng tấn công của địch, rút lui có tổ chức thành công, giữ vững ưu thế trên không) và thực trạng hậu cần bi đát (kho tiếp vận tiền phương từng xây dựng trên giả định tiến công đã bị phá hủy hoàn toàn khi rút lùi chiến tuyến, phần lớn vật tư tích trữ qua mùa đông sang xuân bị thiêu rụi).
  - Giữ nguyên câu hỏi tu từ và nhận định chua chát ở `p000061`–`p000062` về điểm sáng duy nhất là tiêu hủy kho tàng trước khi địch kịp chiếm đoạt.

## 3. Tự kiểm xưng hô và giọng văn nhân vật
- **Tướng Gassman ↔ Đại tá von Lergen (`p000033`–`p000046`)**:
  - Đối thoại ngoại giao giữa tướng lĩnh nước đồng minh và đặc phái viên cấp đại tá của Đế quốc: xưng `tôi` / `chúng tôi` (khi đại diện quốc gia), gọi đối phương là `ngài` / `các ngài` / `Tướng quân` (`thưa Tướng quân`), giữ đúng vẻ lịch sự ngoại giao pha lẫn thăm dò sắc bén.
  - Trong trần thuật ngôi thứ ba theo góc nhìn Lergen: gọi Lergen là `anh`, gọi Tướng Gassman là `vị tướng quân` / `Tướng Gassman`, nhất quán với các chương ngoại giao Ildoa trước đó.
- **Tại Phòng Tác chiến Berun (`p000054`–`p000064`)**:
  - Rudersdorf và Zettour trong trần thuật được gọi là `ông`; sĩ quan tham mưu / sĩ quan Cục Tác chiến được gọi là `anh ta`.
  - Khi báo cáo cho hai vị Trung tướng, sĩ quan Cục Tác chiến dùng `chúng ta` (chỉ lực lượng quân nhà) và giữ thái độ kính trọng (`Không khả quan lắm ạ`).

## 4. Tự kiểm định dạng nhấn mạnh (`DEC-P01-002`)
- Đã đối chiếu toàn bộ 32 phân đoạn với trường `xhtml`:
  - `p000041`: Có 1 cụm `<html:em>` → dịch là `*Phù.*`
  - `p000046`: Có 1 cụm `<html:em>` → dịch là `*Cảm ơn*`
  - `p000049`: Có 1 cụm `<html:em>` → dịch là `*Xin hãy chiến thắng.*`
  - Tất cả 29 phân đoạn còn lại không có thẻ `<html:em>` hay `<html:i>` và hoàn toàn không sử dụng dấu `*...*` trong bản dịch.

## 5. Thuật ngữ và mục đề xuất (Pending Terms)
- Các thuật ngữ đã khóa trong `canon/glossary.yml` và `canon/decisions.md` được áp dụng nghiêm ngặt: `Đế quốc`, `Liên bang`, `Bộ Tổng tham mưu`, `Kampfgruppe`, `Trung tướng von Rudersdorf`, `Trung tướng von Zettour`, `Đại tá von Lergen`, `Berun`, `Ildoa`, `Phòng Tác chiến`.
- Các thuật ngữ đối chiếu theo `work/run-state/pending-terms-index.yml`:
  - `General Gassman`: `Tướng Gassman` (khớp với `vol-06` và `vol-07`).
  - `Lergen Kampfgruppe`: `Kampfgruppe Lergen` (khớp với quy tắc `Kampfgruppe [Tên]` trong `canon/style-guide.md` và `pending-terms-index.yml`).
  - `Operations officer`: `sĩ quan Cục Tác chiến` (khớp với hệ thống `Operations` = `Cục Tác chiến` của Bộ Tổng tham mưu).
  - `air fleet`: `không hạm đội` (khớp với `vol-04` và `vol-07` trong `pending-terms-index.yml`).
  - `forward depot`: `kho tiếp vận tiền phương` (khớp với `vol-07` trong `pending-terms-index.yml`).

## 6. Xác nhận Translator Sign-off (`vol-07-ch-03-b02-translator-signoff`)
- **Báo cáo phản biện**: `reviews/prose/vol-07/ch-03-b02-argon-review.yml` (`serious: 0`, `moderate: 0`, `minor: 0`, `findings: []`).
- **Đối chiếu `pending_term_recommendations` và `locked_choices`**: Toàn bộ 11 khuyến nghị thuật ngữ và 32 mục `locked_choices` từ `p000033` đến `p000064` đã được kiểm tra và tuân thủ đầy đủ trong bản dịch.
- **Cập nhật trạng thái**: Toàn bộ 32 dòng trong `translations/vol-07/ch-03-b02.jsonl` đã được chuyển `status` từ `draft` sang `reviewed`.
