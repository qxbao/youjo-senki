# Báo cáo tự kiểm dịch thuật: vol-05-ch-03-b11

## 1. Tổng quan
- **Task ID:** `vol-05-ch-03-b11` (Sign-off: `vol-05-ch-03-b11-translator-signoff`)
- **Phạm vi đoạn:** `YS-LN05/Text/part0020.html/p000001` đến `YS-LN05/Text/part0020.html/p000039` (39 đoạn).
- **Trạng thái mỗi dòng:** `reviewed`
- **Tệp đích:** `translations/vol-05/ch-03-b11.jsonl`
- **Xử lý review (`ch-03-b11-argon-review.yml`):**
  - Đã xử lý finding `minor` tại `YS-LN05/Text/part0020.html/p000023`: chỉnh cụm từ chỉ các lực lượng tác chiến trên bộ từ `bộ binh mặt đất` thành `lực lượng mặt đất` để bao quát đúng nghĩa quân sự chung và không bị hẹp/trùng nghĩa.
  - Đã đối chiếu toàn bộ `pending_term_recommendations` và `locked_choices` từ báo cáo review, bảo đảm tuân thủ đầy đủ ở tất cả 39 đoạn.

## 2. Kiểm tra quy chuẩn & Canon
- **Đại từ và điểm nhìn (`DEC-P01-001`):**
  - Trần thuật ngôi thứ ba nói về Tanya dùng đại từ `nó` (`p000014`, `p000030`, `p000033`, `p000036`).
  - Nội tâm tự quy chiếu của Tanya dùng `mình` / `bọn mình` / `chúng ta` tùy phạm vi cá nhân hay tập thể đơn vị/Đế quốc (`p000005`, `p000010`, `p000015`, `p000017`, `p000025`, `p000026`, `p000031`, `p000033`).
  - Xưng hô trong thoại giữa Tanya và các sĩ quan dưới quyền (Thiếu tá Weiss, Trung úy Serebryakov) giữ chuẩn cấp trên – cấp dưới (`tôi` – `anh`/`cô` hoặc gọi theo cấp bậc `Thiếu tá Weiss`, `toàn tiểu đoàn`), cấp dưới đáp lệnh dùng `Rõ!` / `tôi` / `chúng ta`.
- **Biểu diễn nhấn mạnh (`DEC-P01-002`):**
  - Giữ đúng định dạng in nghiêng Markdown `*...*` tại các đoạn có thẻ nhấn mạnh trong nguồn: `p000006` (`*cung điện*`), `p000009` (`*Queen of Anjou*`), `p000010` (`*Queen of Anjou*`), `p000025` (toàn câu nội tâm được nhấn mạnh), `p000033` (`*Nhưng mà.*`). Không tự ý thêm in nghiêng ở các đoạn khác.
- **Ngữ nghĩa, phủ định và giả định:**
  - Giữ chính xác cấu trúc điều kiện không có thật ở `p000002`, `p000010`, `p000015`, `p000039`.
  - Giữ đúng chi tiết lỡ lời rồi tự sửa trong thoại chỉ huy tại `p000013` (gọi nhầm mục tiêu là chiến hạm rồi sửa lại thành tàu) và lời bình trần thuật tiếp nối ở `p000014`.
  - Giữ nguyên câu hỏi mở trong độc thoại phân tích ở `p000010`, `p000023` và câu hỏi phản biện trong thoại ở `p000034`, `p000039`.

## 3. Thuật ngữ & Pending Terms
- Các thuật ngữ đã đối chiếu và dùng nhất quán với sổ pending:
  - `Imperial Army`: Lục quân Đế quốc (`p000009`)
  - `commerce raiding operations`: các hoạt động tập kích tuyến thương mại (`p000009`)
  - `RMS Queen of Anjou`: RMS *Queen of Anjou* (`p000009`, `p000010`)
  - `explosion formulas`: thuật thức phát nổ (`p000013`)
  - `joint intelligence agency`: cơ quan tình báo liên hợp (`p000015`)
  - `Operations`: Cục Tác chiến (`p000015`)
  - `paradigm`: mô thức tư duy (`p000016`)
  - `aerial mages`: pháp sư trên không (`p000024`, `p000031`)
  - `Intelligence`: bên Tình báo (`p000037`)
  - `Major Weiss`: Thiếu tá Weiss (`p000039`)
- Các thuật ngữ chuyên ngành hàng hải/không quân phát sinh trong lô được dịch sát nghĩa và tự nhiên:
  - Danh hiệu giải thưởng tốc độ vượt đại dương tại `p000017`: `giải Dải Băng Xanh` (pending).
  - Thuật ngữ tác chiến không quân đánh tàu tại `p000022`, `p000023`, `p000024`: `tấn công chống hạm`, `lực lượng không quân chiến thuật`, `sức mạnh không quân hàng hải`, `ném bom bay bằng`.

## 4. Kết luận tự kiểm
- Đủ 39/39 đoạn, bảo toàn mã đoạn và `source_sha256`.
- Không trích dẫn văn bản nguồn tiếng Anh trong báo cáo.
