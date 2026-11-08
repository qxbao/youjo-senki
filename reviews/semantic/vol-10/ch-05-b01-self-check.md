# Báo cáo tự kiểm (Self-Check): `vol-10-ch-05-b01`

- **Task ID:** `vol-10-ch-05-b01`
- **Phạm vi đoạn:** `YS-LN10/Text/chapter024.xhtml/p000001` đến `YS-LN10/Text/chapter024.xhtml/p000031` (31 đoạn)
- **Tệp bản dịch:** `translations/vol-10/ch-05-b01.jsonl`
- **Trạng thái dòng:** `reviewed` (đã hoàn tất `vol-10-ch-05-b01-translator-signoff`)

## 1. Kiểm tra nghĩa, logic và giả định
- Đã đối chiếu đầy đủ 31 đoạn từ `p000001` đến `p000031`, bảo toàn lập luận mở đầu về vai trò của thương mại trà, vận tải biển và lực lượng hải quân đối với quyền bá chủ của Khối Thịnh vượng chung.
- Giữ nguyên cấu trúc tự hiệu chỉnh ở `p000018` và các câu điều kiện giả định trái thực tế ở `p000023` (giả định nếu đây là lần đầu ghé tới và nếu không biết trước chất lượng của khách sạn).
- Bảo toàn các chi tiết so sánh chất lượng trà hộp thiếc của Hợp chúng quốc ở doanh trại Liên bang (`p000018`–`p000019`) cũng như sự xuống cấp của bánh scone, bơ thay thế và mứt thiếu đường tại phòng trà khách sạn (`p000027`–`p000031`).
- **Xử lý findings từ Argon review (`ch-05-b01-argon-review.yml`):**
  - `p000023` (minor): Tiếp nhận đề xuất của reviewer, chỉnh `các cô` thành `bên cô` trong câu phàn nàn của Drake để phân tách rõ ý trách chung phía cơ sở khách sạn với câu hỏi cá nhân dành cho người nữ phục vụ kế tiếp, đồng thời tuân thủ đầy đủ `locked_choices`.
  - `p000028` (minor): Giữ nguyên `món mứt quả ninh nhừ` theo đúng phương án tạm đã được reviewer khóa tại `pending_term_recommendations` (`scones / fruit compote` -> `bánh scone / món mứt quả ninh nhừ`).

## 2. Điểm nhìn và quy chuẩn xưng hô
- Nhân vật trung tâm của đoạn là Trung tá Drake (`Lieutenant Colonel Drake`). Trần thuật ngôi thứ ba quy chiếu Drake bằng `anh` nhất quán với các chương trước của Tập 10.
- Độc thoại nội tâm trực tiếp của Drake (`p000020`, `p000030`) tự quy chiếu bằng `mình`.
- Trong hội thoại giữa Drake và nữ phục vụ (`p000022`–`p000025`): nữ phục vụ gọi Drake là `thưa Trung tá` / `ngài` và xưng `chúng tôi` (đại diện phía khách sạn/phòng trà); Drake xưng `tôi` và gọi đối phương là `cô` (`bên cô` khi chỉ phía cơ sở dịch vụ).

## 3. Nhấn mạnh và định dạng (`DEC-P01-002`)
- Chỉ sử dụng dấu nhấn mạnh `*...*` tại đúng 2 vị trí có thẻ `<html:em>` trong nguồn:
  - `YS-LN10/Text/chapter024.xhtml/p000020`: toàn bộ câu nội tâm.
  - `YS-LN10/Text/chapter024.xhtml/p000030`: câu đầu tiên trong đoạn.
- Không tự ý thêm chữ nghiêng ở các đoạn trần thuật hoặc lời thoại khác.

## 4. Thuật ngữ và mục chờ xét (Pending Terms)
- Áp dụng nhất quán các thuật ngữ đã có trong sổ pending:
  - `Commonwealth`: Khối Thịnh vượng chung
  - `Lieutenant Colonel Drake`: Trung tá Drake
  - `homeland` (bối cảnh Khối Thịnh vượng chung ở `p000011`): bản thổ
  - `Federation`: Liên bang
  - `Unified States`: Hợp chúng quốc
  - `Imperial Navy`: Hải quân Đế quốc
- **Đề xuất thuật ngữ mới (`pending_terms`):**
  - `tea clippers` (`p000009`): `những con tàu buồm tốc độ cao chở trà` (trạng thái: `pending`).
  - `scones` / `scone` (`p000021`, `p000026`, `p000030`): `bánh scone` (trạng thái: `pending`).
  - `fruit compote` (`p000028`): `món mứt quả ninh nhừ` (trạng thái: `pending`).
