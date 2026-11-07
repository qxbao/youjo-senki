# Báo cáo tự kiểm (Self-Check) — `vol-08-ch-06-b05`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-06-b05`
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter022.xhtml/p000148` đến `YS-LN08/Text/chapter022.xhtml/p000193` (46 đoạn)
- **Tệp bản dịch**: `translations/vol-08/ch-06-b05.jsonl`

## 2. Kiểm tra tính đầy đủ & siêu dữ liệu
- **Số dòng JSONL**: 46/46 đoạn, khớp hoàn toàn 1-1 với tệp nguồn.
- **Trạng thái (`status`)**: Toàn bộ 46/46 dòng đều đã được cập nhật sang trạng thái `"reviewed"` sau khi đối chiếu đầy đủ `reviews/prose/vol-08/ch-06-b05-argon-review.yml` (0 findings, tuân thủ toàn bộ `locked_choices` và `pending_term_recommendations`).
- **Khóa định danh & băm**: `segment_id`, `source_sha256` và `glossary_version` khớp chính xác với `handoffs/vol-08/ch-06-b05.yml`.
- **Không sót đoạn / không gộp tách đoạn**: Giữ nguyên ranh giới của từng đoạn văn và lời thoại.

## 3. Kiểm tra quy chuẩn xưng hô, giọng điệu và mạch trần thuật (`DEC-P01-001`)
- **Nửa đầu batch — Góc nhìn Trung tá Drake (`p000148` – `p000155`)**:
  - Tiếp nối trực tiếp mạch thoại từ cuối `ch-06-b04`, Drake truyền lệnh qua nhân viên thông tin liên lạc cho người đồng đội cùng phi đội năm xưa về cách kiểm soát Trung úy Sue (gọi Sue là `cô ta` / `cô nàng bất kham ấy`).
  - Trong mạch trần thuật ngôi thứ ba bám sát điểm nhìn của Drake, gọi Drake là `anh`.
  - Khi khích lệ binh sĩ dưới quyền ở `p000155`, Drake gọi `anh em`, xưng `chúng ta` / `tôi` đầy quyết liệt.
- **Nửa sau batch — Góc nhìn Tiểu đoàn Pháp sư Trên không số 203 & Tanya (`p000156` – `p000193`)**:
  - Chuyển cảnh tại `p000156` sang phía Tiểu đoàn 203.
  - Trong mạch trần thuật ngôi thứ ba (`p000159`, `p000164`, `p000167` – `p000168`, `p000171` – `p000172`, `p000174`, `p000180`, `p000188` – `p000189`), gọi Tanya là `cô` / `Tanya`, gọi Trung úy Grantz là `anh ta`.
  - Trong độc thoại nội tâm trực tiếp của Tanya (`p000165`) và góc nhìn số nhiều bao gộp cả đơn vị (`p000181`, `p000186`, `p000191`, `p000193`), dùng `mình` (tự quy chiếu cá nhân ở `p000165`), `chúng ta` (khi suy tính chiến thuật / nói về toàn đơn vị ở `p000181`, `p000186`) và `chúng tôi` (trong trần thuật ngôi thứ nhất số nhiều ở `p000191`, `p000193`).
  - Trong đối thoại giữa Tanya và các thuộc cấp (`p000157` – `p000158`, `p000160`, `p000162` – `p000163`, `p000166`, `p000169` – `p000170`, `p000173`, `p000178` – `p000180`, `p000182` – `p000184`, `p000187`, `p000190`): Tanya xưng `tôi` / `chúng ta`, gọi cấp dưới bằng cấp bậc hoặc tên (`Trung úy Grantz` / `anh`, `Weiss`); cấp dưới xưng `chúng tôi` / `tôi`, gọi Tanya là `Trung tá` / `thưa Trung tá` với thái độ tôn trọng quân kỷ.

## 4. Kiểm tra định dạng nhấn mạnh (`DEC-P01-002`)
- Chỉ bảo toàn định dạng in nghiêng (`*...*`) tại đúng 3 đoạn có thẻ nhấn mạnh trong nguyên bản XHTML:
  1. `p000167`: Câu hỏi ánh mắt của Trung úy Grantz (`*Chúng ta thực sự không thể sao ạ?*`).
  2. `p000175`: Toàn bộ đoạn độc thoại nội tâm ngắn (`*Kỳ lạ thật. Đây đáng lẽ phải là một trận truy kích cơ mà, rốt cuộc chuyện gì đang diễn ra thế này?*`).
  3. `p000177`: Từ cảm thán mở đầu đoạn (`*Đây rồi!*`).
- Toàn bộ 43 đoạn còn lại không tự ý thêm bất kỳ dấu `*...*` nào.

## 5. Kiểm tra thuật ngữ & đối chiếu Canon / Pending Terms
- Các thuật ngữ chuẩn và thuật ngữ đang đề xuất đều được áp dụng nhất quán với các batch trước:
  - `Quân đội Liên bang`, `quân Đế quốc`, `pháp sư Đế quốc`, `Lục quân Đế quốc`.
  - `Tiểu đoàn Pháp sư Trên không số 203`, `sĩ quan phụ tá`, `hệ thống chỉ huy`.
  - `đơn vị hỗn hợp Liên bang – Khối Thịnh vượng chung`, `Khối Thịnh vượng chung`, `Cộng sản`.
  - `Trung úy Grantz`, `Trung tướng von Zettour`, `Weiss`.
  - `trận truy kích`, `trận tao ngộ chiến`, `lối tiếp cận gián tiếp`, `đường rút quân`, `đòn công kích nghi binh phối hợp`, `hỏa lực ngăn chặn`.

## 6. Kết quả chạy công cụ kiểm tra
- Chạy `python3 tools/validate_translation.py --handoff handoffs/vol-08/ch-06-b05.yml --source work/vol-08/batches/ch-06-b05-source.jsonl --translation translations/vol-08/ch-06-b05.jsonl` đạt kết quả `PASS`.
