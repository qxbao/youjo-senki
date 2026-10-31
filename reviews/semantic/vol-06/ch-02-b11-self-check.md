# Báo cáo tự kiểm & Sign-off (Self-Check): `vol-06-ch-02-b11`

- **Task ID**: `vol-06-ch-02-b11-translator-signoff` (parent: `vol-06-ch-02-b11`)
- **Phạm vi**: `YS-LN06/Text/part0013.html/p000001` .. `YS-LN06/Text/part0013.html/p000035` (35 đoạn)
- **Tác tử**: `argon-low`
- **Trạng thái dòng dịch**: `reviewed` (đã cập nhật toàn bộ 35/35 dòng từ `draft` sang `reviewed`)

## 1. Xử lý Findings từ Argon Review (`ch-02-b11-argon-review.yml`)
- **`YS-LN06/Text/part0013.html/p000020`** (`minor` — `idiom_and_nuance`):
  - **Tiếp nhận**: Chỉnh lại cấu trúc câu từ `"Dẫu vậy, sự thuận lợi về mặt chính trị mà chiến thắng này mang lại là điều không hề nói quá."` thành `"Dẫu vậy, sự thuận lợi về mặt chính trị của chiến thắng này có nhấn mạnh bao nhiêu cũng không quá lời."` để tự nhiên về cú pháp tiếng Việt và sát nghĩa thành ngữ trong nguồn.
- **`YS-LN06/Text/part0013.html/p000032`** (`minor` — `style_and_nuance`):
  - **Tiếp nhận**: Lược từ giải thích `"chôn"`, chỉnh cụm cuối câu từ `"chuẩn bị sẵn vài cái hố chôn cho chúng"` thành `"chuẩn bị sẵn vài cái hố cho chúng"` để bảo toàn đúng lối nói giảm hàm súc, lạnh lùng trong suy nghĩ của Loria theo `canon/style-guide.md`.
- **Tuân thủ `locked_choices` & `pending_term_recommendations`**:
  - Đã đối chiếu toàn bộ 35 mục `locked_choices` và 10 mục `pending_term_recommendations` trong `reviews/prose/vol-06/ch-02-b11-argon-review.yml`, bảo đảm tuân thủ 100%.

## 2. Kiểm tra tính đầy đủ & bảo toàn nghĩa
- Đã dịch và rà soát đầy đủ toàn bộ 35 đoạn từ `p000001` đến `p000035`, giữ nguyên ranh giới đoạn 1-1 theo đúng mã đoạn (`segment_id`), giữ nguyên `source_sha256` và `glossary_version`, đặt `status` là `reviewed`.
- Bảo toàn chặt chẽ nghĩa, sắc thái, quan hệ nhân quả, phủ định và mức độ khẳng định:
  - `p000001`–`p000008`: Lời thề rút lui và quyết tâm quay trở lại của Mary Sue nối tiếp ngay sau cuối `ch-02-b10`.
  - `p000009`–`p000022`: Tổng kết khách quan kết quả trận đánh từ góc nhìn hậu nghiệm đối với cả ba bên (Đế quốc đạt chiến thắng chiến thuật áp đảo và củng cố liên minh với Hội đồng Tự trị; Quân đội Liên bang và Bộ Dân ủy Nội vụ thu được tin tình báo chiến lược để buộc giới lãnh đạo Đảng và Bộ Chính trị đối diện thực tại chiến trường; các pháp sư viễn chinh của Khối Thịnh vượng chung dưới quyền Trung tá Drake đạt kết quả quân sự khiêm tốn nhưng mang lại lợi ích chính trị lớn).
  - `p000023`–`p000035`: Bối cảnh tại Moskva cùng thời điểm đó với góc nhìn của Ủy viên Dân ủy Loria trước những lời chỉ trích nội bộ, lập luận bảo vệ mục tiêu chính trị của cuộc trinh sát chiến đấu với sự ủng hộ của Bộ Tổng tham mưu, cùng suy nghĩ thâm độc và triết lý kiên nhẫn của Loria.

## 3. Xưng hô, giọng điệu & điểm nhìn (`DEC-P01-001`)
- **Đoạn `p000001`–`p000008` (điểm nhìn Mary Sue)**:
  - Trần thuật gọi Mary là `cô`.
  - Trong câu thoại tự thề (`p000003`, `p000008`), Mary tự xưng `mình` và mở rộng sang `chúng ta`, giữ sự thống nhất hoàn toàn với đoạn kết của `ch-02-b10` (`p000447`–`p000463`).
- **Đoạn `p000009`–`p000022` (trần thuật tổng quan)**:
  - Giọng trần thuật lịch sử – quân sự khách quan, mạch lạc; gọi Trung tá Drake là `ông` (`p000021`).
- **Đoạn `p000023`–`p000035` (điểm nhìn Loria tại Moskva)**:
  - Trần thuật gọi Loria là `gã`, tự quy chiếu là `mình` (`p000025`, `p000032`), đồng bộ với `ch-01-b13`..`b16`.
  - Trong phát biểu chính thức trước cuộc họp (`p000026`, `p000029`) và lời chất vấn giả định từ các cán bộ Đảng (`p000027`), sử dụng `chúng ta` và `đồng chí` đúng văn phong chính trị Liên bang.

## 4. Bảo toàn nhấn mạnh (`DEC-P01-002`)
- Đối chiếu chính xác với thẻ nhấn mạnh trong trường `xhtml` của nguồn:
  - Chỉ sử dụng dấu `*...*` tại đúng 2 đoạn có thẻ nhấn mạnh trong nguồn: `p000024` (`*lũ ngu ngốc chẳng hiểu biết gì*`) và `p000027` (`*Chẳng phải chúng ta đã thua vì đồng ý với kế hoạch của đồng chí sao?*`).
  - Toàn bộ 33 đoạn còn lại hoàn toàn không có dấu `*`.

## 5. Thuật ngữ & tính nhất quán với Canon / Pending Index
- Đã tra cứu và áp dụng nhất quán các thuật ngữ từ `canon/`, `work/run-state/pending-terms-index.yml` và `pending_term_recommendations`:
  - `Đế quốc` / `Liên bang` / `Khối Thịnh vượng chung` (`p000009`, `p000011`, `p000012`, `p000013`, `p000015`, `p000019`, `p000024`).
  - `Lục quân Đế quốc` (`p000010`, `p000013`).
  - `cuộc tiến công giới hạn` (`p000011`).
  - `Hội đồng Tự trị` (`p000011`, `p000012`, `p000015`).
  - `Quân đội Liên bang` (`p000014`, `p000016`, `p000018`).
  - `đám ly khai` (`p000015`).
  - `Bộ Tổng tham mưu Quân đội Liên bang` / `Bộ Tổng tham mưu` (`p000016`, `p000031`).
  - `Bộ Dân ủy Nội vụ` / `Ủy viên Dân ủy Loria` / `Loria` (`p000018`, `p000025`, `p000030`, `p000032`, `p000035`).
  - `Trung tá Drake` / `pháp sư hải quân đánh bộ` (`p000021`).
  - `trinh sát chiến đấu` (`p000026`).
  - `lực lượng bán vũ trang` (`p000011`)
  - `giới lãnh đạo Đảng` / `Ban Bí thư` / `Bộ Chính trị` (`p000015`, `p000016`, `p000018`, `p000031`)
  - `các pháp sư viễn chinh` (`p000019`)
  - `MOSKVA CÙNG THỜI ĐIỂM ĐÓ` (`p000023`)
