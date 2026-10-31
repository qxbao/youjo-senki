# Báo cáo tự kiểm (Self-Check): `vol-06-ch-02-b14`

- **Task ID:** `vol-06-ch-02-b14`
- **Translator:** `argon-low`
- **Phạm vi đoạn:** `YS-LN06/Text/part0013.html/p000105` đến `YS-LN06/Text/part0013.html/p000143` (39 đoạn)
- **Tệp bản dịch:** `translations/vol-06/ch-02-b14.jsonl`

## 1. Kiểm tra tính đầy đủ và cấu trúc dữ liệu
- Toàn bộ 39 đoạn trong `work/vol-06/batches/ch-02-b14-source.jsonl` đã được dịch đầy đủ, giữ nguyên thứ tự và mã định danh `segment_id`.
- Mỗi dòng trong `translations/vol-06/ch-02-b14.jsonl` đều có đầy đủ các trường bắt buộc: `segment_id`, `translation`, `status: "reviewed"`, `translator: "argon-low"`, `glossary_version`, `source_sha256` và `notes: []`.
- Không bỏ sót câu, mệnh đề phụ, con số, mốc thời gian hay địa danh nào.

## 2. Kiểm tra thuật ngữ, quy chuẩn xưng hô và giọng văn
- **Cảnh 1 (`p000105`–`p000116`, phòng họp ngầm tại Moskva):**
  - Loria trao đổi với các quan chức Đảng Cộng sản: gọi nhau là `Đồng chí` / `đồng chí`, xưng `tôi`, gọi tập thể lãnh đạo Đảng là `chúng ta`, gọi những phần tử trong trại cải tạo là `bọn chúng` / `chúng`.
  - Giữ đúng các thuật ngữ đã thống nhất từ các batch trước: `Đảng`, `Liên bang`, `mẫu quốc`, `Đế quốc`, `*lageri*`, `chủ nghĩa dân tộc`.
  - Giọng văn của Loria duy trì sắc thái thực dụng, lạnh lùng và toan tính chính trị khi bàn về việc đồng nhất Đảng với quốc gia để lợi dụng lòng yêu nước.
- **Cảnh 2 (`p000117`–`p000143`, doanh trại đồn trú của Lực lượng Đa quốc gia trong lãnh thổ Liên bang vào ngày Giáng sinh Năm Thống nhất 1926):**
  - Tiêu đề chuyển cảnh `p000117` viết hoa toàn bộ theo đúng quy ước: `NGÀY GIÁNG SINH, NĂM THỐNG NHẤT 1926, LÃNH THỔ LIÊN BANG, DOANH TRẠI ĐỒN TRÚ CỦA LỰC LƯỢNG ĐA QUỐC GIA`.
  - Nhân vật `Trung tá Drake`: trong trần thuật ngôi thứ ba gọi là `ông`, độc thoại nội tâm trực tiếp (`p000137`) xưng `mình`; cấp dưới báo cáo (`p000129`) thưa là `Thưa Trung tá` theo đúng hệ thống cấp bậc đã ghi nhận trong sổ tay thuật ngữ.
  - Các thuật ngữ quân sự và tổ chức được áp dụng nhất quán: `Khối Thịnh vượng chung`, `pháp sư hải quân đánh bộ`, `chiến dịch trinh sát chiến đấu`, `Quân đội Liên bang`, `sở chỉ huy`, `sĩ quan trực ban`, `quán trọ đặt sở chỉ huy`, `Đại tá Mikel`.

## 3. Kiểm tra bảo toàn định dạng nhấn mạnh (`DEC-P01-002`)
- Chỉ sử dụng dấu `*...*` ở đúng 3 đoạn có thẻ nhấn mạnh trong văn bản gốc:
  - `p000109`: `*lageri*`
  - `p000133`: `*Đùa nhau chắc!*`
  - `p000137`: `*Sao mình lại phải lo cái chuyện này vào đúng ngày Giáng sinh cơ chứ?*`
- Các đoạn còn lại hoàn toàn không phát sinh dấu sao ngoài nguồn.

## 4. Thuật ngữ và cách dịch đề xuất
- Không phát sinh điểm mơ hồ chặn tiến độ; toàn bộ thuật ngữ tổ chức, chức danh và địa danh đã bám sát `canon/glossary.yml` và `work/run-state/pending-terms-index.yml`.

## 5. Translator Sign-off (`vol-06-ch-02-b14-translator-signoff`)
- Đã tiếp nhận và xử lý finding mức `minor` tại `YS-LN06/Text/part0013.html/p000126` từ `reviews/prose/vol-06/ch-02-b14-argon-review.yml`: đồng bộ cụm `pháp sư thủy quân lục chiến` thành `pháp sư hải quân đánh bộ` theo sổ pending từ `vol-04` và `vol-05`.
- Đã đối chiếu và bảo đảm tuân thủ đầy đủ toàn bộ `pending_term_recommendations` và `locked_choices` từ `p000105` đến `p000143`.
- Đã cập nhật trường `status` của toàn bộ 39 dòng trong `translations/vol-06/ch-02-b14.jsonl` từ `draft` sang `reviewed`.
