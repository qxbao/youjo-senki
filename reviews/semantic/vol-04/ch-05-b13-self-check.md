# Báo cáo tự kiểm (Self-Check): `vol-04-ch-05-b13`

- **Task ID**: `vol-04-ch-05-b13-translator-signoff` (parent: `vol-04-ch-05-b13`)
- **Translator**: `argon-low`
- **Handoff**: `handoffs/vol-04/ch-05-b13.yml`, `handoffs/vol-04/ch-05-b13-translator-signoff.yml`
- **Review Report**: `reviews/prose/vol-04/ch-05-b13-argon-review.yml`
- **Tệp dịch**: `translations/vol-04/ch-05-b13.jsonl`
- **Phạm vi**: `YS-LN04/Text/chapter001_t.xhtml/p000060` → `YS-LN04/Text/chapter001_t.xhtml/p000086` (27 đoạn)
- **Trạng thái mỗi dòng**: `reviewed`

## 1. Kiểm tra tính đầy đủ, nghĩa gốc và xử lý Argon Review
- Toàn bộ 27 đoạn từ `chapter001_t.xhtml/p000060` đến `chapter001_t.xhtml/p000086` đã được rà soát, cập nhật theo `reviews/prose/vol-04/ch-05-b13-argon-review.yml` và chuyển trạng thái `status` từ `draft` sang `reviewed`.
- Đã tiếp nhận và xử lý đầy đủ cả 4 findings trong báo cáo Argon review, bảo đảm tuân thủ toàn bộ `locked_choices` và `pending_term_recommendations`:
  - **`YS-LN04/Text/chapter001_t.xhtml/p000065` (minor — negation_and_style)**: Đổi câu nội tâm đầu đoạn thành `*Chắc chúng ta sẽ không gặp trở ngại gì khi xin phép quay về căn cứ đâu.*` để bảo toàn cấu trúc phủ định tình thái và tránh lặp từ `dễ dàng` với vế sau.
  - **`YS-LN04/Text/chapter001_t.xhtml/p000083` (moderate — terminology_and_viewpoint)**: Đổi `Áp lực đồng trang lứa` thành `Áp lực từ đồng nghiệp` cho đúng ngữ cảnh công việc/quân ngũ, đồng thời đổi đại từ ở câu cuối từ `bạn` thành `người ta` (`Nhưng một khi đã bước vào cuộc chơi, người ta buộc phải dốc toàn lực.`) để thống nhất đại từ khái quát trong lời trần thuật gián tiếp tự do.
  - **`YS-LN04/Text/chapter001_t.xhtml/p000085` (minor — pronouns_and_register)**: Đổi `Các anh nghe thấy rồi chứ?` thành `Các binh sĩ, mọi người nghe thấy rồi chứ?` để phản ánh đầy đủ danh từ gọi đáp chung toàn đơn vị và bao quát cả cấp dưới nữ (Trung úy Serebryakov).
  - **`YS-LN04/Text/chapter001_t.xhtml/p000086` (minor — style_and_grammar)**: Đổi cụm nhấn mạnh `*Hãy cứu những quân mình đó*` thành `*Hãy cứu những người bên quân mình đó*` để câu tiếng Việt tự nhiên và chuẩn ngữ pháp hơn mà vẫn giữ nguyên phạm vi nhấn mạnh.
- Tuyệt đối không sao chép văn bản hay cụm từ nguồn tiếng Anh vào báo cáo tự kiểm.

## 2. Kiểm tra đại từ, xưng hô và giọng văn (`DEC-P01-001`)
- Tuân thủ nghiêm ngặt `DEC-P01-001` và mọi `locked_choices` trong `ch-05-b13-argon-review.yml`:
  - **Trần thuật về Tanya**: Dùng tên riêng `Tanya` và đại từ `nó` (`p000063`, `p000065`, `p000067`, `p000069`, `p000073`, `p000080`, `p000081`), tuyệt đối không dùng `cô` cho Tanya trong trần thuật.
  - **Độc thoại nội tâm và lời trần thuật gián tiếp tự do của Tanya**: Dùng `chúng ta` khi quy chiếu tập thể đơn vị mình (`p000065`, `p000067`, `p000084`) và dùng nhất quán `người ta ... mình` cho nhận định khái quát về giao lưu xã giao vì công việc và áp lực từ đồng nghiệp (`p000083`).
  - **Trần thuật về các nhân vật khác**: Quy chiếu viên sĩ quan điều khiển mặt đất (`Galba 15`) bằng `sĩ quan điều khiển` / `viên sĩ quan điều khiển` / `anh ta` (`p000067`, `p000069`, `p000073`, `p000075`); quy chiếu Đại úy Weiss bằng `Đại úy Weiss` / `anh` và hai cấp dưới là `Hai Trung úy Serebryakov và Grantz` (`p000086`).
  - **Trong đối thoại vô tuyến và đối thoại nội bộ đơn vị**:
    - Giữa `Fairy 01` (Tanya) và `Galba 15`: Xưng `tôi` / `chúng tôi`, gọi đối phương lịch sự, chuẩn điều lệnh quân sự là `các vị` / `bên đó` (`p000062`, `p000066`, `p000068`, `p000070`, `p000072`, `p000074`, `p000076`–`p000079`, `p000082`).
    - Khi Tanya nói với binh sĩ dưới quyền trong tiểu đoàn (`p000085`): Dùng `Các binh sĩ, mọi người` và `Chúng ta`.

## 3. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002`)
- Kiểm tra toàn bộ 6 đoạn có thẻ `<html:em>` trong XHTML nguồn và bảo toàn chính xác bằng cặp dấu `*...*` đúng phạm vi nhấn mạnh đã khóa:
  - `chapter001_t/p000063`: `*Ồ, ra vậy.*`
  - `chapter001_t/p000065`: `*Chắc chúng ta sẽ không gặp trở ngại gì khi xin phép quay về căn cứ đâu.*`
  - `chapter001_t/p000067`: `*Các đơn vị khác đều được hủy nhiệm vụ, còn chúng ta lại phải nhận một nhiệm vụ mới sao? Lần này tin tức sẽ còn tệ hại đến mức nào nữa đây?*`
  - `chapter001_t/p000075`: `*Không may thay*`
  - `chapter001_t/p000080`: `*…Thật hết nói nổi mà…*`
  - `chapter001_t/p000086`: `*Hãy cứu những người bên quân mình đó*`
- Toàn bộ 21 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và không phát sinh dấu `*` trong bản dịch.

## 4. Kiểm tra thuật ngữ và tính nhất quán (`canon/` & `pending_term_recommendations`)
- Tuân thủ đầy đủ toàn bộ 13 mục `pending_term_recommendations` trong `reviews/prose/vol-04/ch-05-b13-argon-review.yml`:
  - `Đài Kiểm soát Galba` / `Galba 15` / `đài kiểm soát mặt đất` (`p000060`, `p000061`, `p000063`, `p000064`, `p000066`, `p000070`, `p000074`, `p000077`, `p000078`)
  - `Tiểu đoàn Fairy` / `Fairy 01` (`p000061`, `p000064`, `p000066`, `p000070`, `p000074`, `p000076`–`p000078`, `p000082`)
  - `sĩ quan điều khiển` / `sĩ quan điều khiển mặt đất` (`p000067`, `p000069`, `p000073`, `p000075`)
  - `Tư lệnh Sư đoàn Không quân số 114` / `Sư đoàn Không quân số 114` (`p000068`, `p000070`)
  - `tìm kiếm và giải cứu chiến đấu` / `CSAR` (`p000068`, `p000076`, `p000077`)
  - `bản thổ Khối Thịnh vượng chung` (`p000071`)
  - `tấn công mặt đất` (`p000072`)
  - `RTB` (`p000076`)
  - `Bộ Tổng tham mưu` (`p000079`–`p000081`)
  - `Cụm tập đoàn quân phía Tây` (`p000081`)
  - `nghiên cứu kỹ năng tác chiến` (`p000081`)
  - `Đại úy Weiss` (`p000086`)
  - `Hai Trung úy Serebryakov và Grantz` (`p000086`)

## 5. Kiểm tra định dạng và công cụ xác thực
- Tệp `translations/vol-04/ch-05-b13.jsonl` gồm đúng 27 dòng JSON hợp lệ, mỗi dòng có đủ các trường `segment_id`, `translation`, `status` (`reviewed`), `translator` (`argon-low`), `glossary_version`, `source_sha256`, `notes` (`[]`).
- Chạy `python3 tools/validate_translation.py --handoff handoffs/vol-04/ch-05-b13.yml --source work/vol-04/batches/ch-05-b13-source.jsonl --translation translations/vol-04/ch-05-b13.jsonl` để xác nhận `PASS`.
