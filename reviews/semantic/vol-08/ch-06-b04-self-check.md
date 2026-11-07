# Báo cáo tự kiểm (Self-Check) — `vol-08-ch-06-b04`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-06-b04`
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter022.xhtml/p000108` đến `YS-LN08/Text/chapter022.xhtml/p000147` (40 đoạn)
- **Tệp bản dịch**: `translations/vol-08/ch-06-b04.jsonl`

## 2. Kiểm tra tính đầy đủ & siêu dữ liệu
- **Số dòng JSONL**: 40/40 đoạn, khớp hoàn toàn 1-1 với tệp nguồn.
- **Trạng thái (`status`)**: Toàn bộ 40/40 dòng đã được cập nhật từ `"draft"` sang `"reviewed"` sau khi đối chiếu với `reviews/prose/vol-08/ch-06-b04-argon-review.yml` (0 findings, tuân thủ đầy đủ các `pending_term_recommendations` và `locked_choices`).
- **Khóa định danh & băm**: `segment_id`, `source_sha256` và `glossary_version` khớp chính xác với `handoffs/vol-08/ch-06-b04.yml`.
- **Không sót đoạn / không gộp tách đoạn**: Giữ nguyên ranh giới của từng đoạn văn và lời thoại.

## 3. Kiểm tra quy chuẩn xưng hô, giọng điệu và mạch trần thuật (`DEC-P01-001`)
- **Trần thuật & độc thoại góc nhìn Trung tá Drake (`p000108` – `p000147`)**:
  - Trong mạch trần thuật ngôi thứ ba bám sát điểm nhìn của Trung tá Drake, gọi Drake là `anh`, gọi Trung úy Sue là `cô ta`.
  - Trong độc thoại nội tâm trực tiếp (`p000112`, `p000118`, `p000120`, `p000121`), Drake tự xưng `mình` / `chúng ta` (hoặc `chúng con` trong lời cầu nguyện/ca tụng hướng về Khối Thịnh vượng chung ở `p000120`).
- **Đối thoại giữa Trung tá Drake và Đại tá Mikel (`p000108` – `p000109`, `p000113` – `p000116`, `p000123`, `p000126` – `p000129`, `p000132` – `p000135`, `p000137` – `p000138`)**:
  - Tiếp nối trực tiếp mạch thoại từ batch `ch-06-b03`, hai vị chỉ huy đồng minh giữ cách xưng hô tôn trọng, lịch thiệp giữa các sĩ quan: xưng `tôi`, gọi đối phương là `ngài`, hoặc gọi kèm cấp bậc (`Thưa Trung tá`, `Trung tá Drake`, `Đại tá Mikel`).
  - Khi nhắc đến nữ sĩ quan chính trị Liên bang (`p000133` – `p000134`, `p000137` – `p000138`), Drake dùng `cô ta` thể hiện sự dè chừng và ác cảm, trong khi Mikel dùng `cô ấy` với thái độ khách quan, ôn hòa hơn.
- **Đối thoại giữa Trung tá Drake và binh lính thông tin dưới quyền (`p000140`, `p000144` – `p000145`)**:
  - Người lính thông tin báo cáo và nhận lệnh nghiêm chỉnh (`Thưa Trung tá!`, `Rõ, thưa Trung tá!`, xưng `tôi`, gọi Trung úy Sue là `cô ấy`).
  - Drake ra lệnh ngắn gọn, dứt khoát, gọi Sue là `cô ta`.

## 4. Kiểm tra định dạng nhấn mạnh (`DEC-P01-002`)
- Chỉ bảo toàn định dạng in nghiêng (`*...*`) tại đúng 6 đoạn có thẻ nhấn mạnh trong nguyên bản XHTML:
  1. `p000111`: Cụm giả định ở đầu đoạn (`*Nếu không vì cơn cuồng loạn của Sue*`).
  2. `p000112`: Toàn bộ đoạn độc thoại tự trách của Drake (`*Chính mình đã giết chết họ — đơn vị này nằm dưới quyền chỉ huy của mình. Mình phải tạ tội với gia đình họ. Mình đáng bị trừng phạt. Đây phải là nỗi nhục mà chính mình gánh chịu.*`).
  3. `p000118`: Toàn bộ câu độc thoại ngắn (`*Những gì chúng ta đang làm đều có ý nghĩa.*`).
  4. `p000120`: Câu cầu nguyện/tôn vinh ở cuối đoạn (`*Hỡi Khối Thịnh vượng chung yêu dấu, nguyện xin người hân hoan đón nhận lòng tôn kính vô song của chúng con.*`).
  5. `p000121`: Toàn bộ câu tự nhủ ngắn (`*Thôi được rồi, giờ thì tạm gác những suy tư ủy mị sang một bên đã.*`).
  6. `p000135`: Từ nhấn mạnh được lặp lại trong câu thoại của Drake (`*khá khẩm hơn*`).
- Toàn bộ 34 đoạn còn lại không tự ý thêm bất kỳ dấu `*...*` nào.

## 5. Kiểm tra thuật ngữ & đối chiếu Canon / Pending Terms
- Các thuật ngữ chuẩn và thuật ngữ đang đề xuất đều được áp dụng nhất quán với các batch trước:
  - `Trung tá Drake`, `Đại tá Mikel`, `Trung úy Sue` / `trung úy`.
  - `Thượng đế`, `Tổ quốc`, `bản quốc`, `chính quốc`.
  - `Khối Thịnh vượng chung`, `Lục quân Đế quốc`, `quân Đế quốc`, `Ác quỷ sông Rhine`, `Soldim 528`.
  - `đơn vị đa quốc gia`, `tiểu đoàn pháp sư`, `đơn vị pháp sư Đế quốc`, `sĩ quan chính trị`, `vị trí đoạn hậu`.
- Không phát sinh thuật ngữ mới gây mơ hồ cần bổ sung ngoài danh mục đã có.

## 6. Kết quả chạy công cụ kiểm tra
- Đã kiểm tra bằng `tools/validate_translation.py` và đạt kết quả `PASS`.
