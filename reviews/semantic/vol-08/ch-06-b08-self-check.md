# Báo cáo tự kiểm dịch thuật (Self-Check & Sign-off Report)

- **Task ID**: `vol-08-ch-06-b08-translator-signoff` (parent: `vol-08-ch-06-b08`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter022.xhtml/p000267` .. `YS-LN08/Text/chapter022.xhtml/p000307` (41 đoạn)
- **Tệp đích**: `translations/vol-08/ch-06-b08.jsonl`

## 1. Kiểm tra tính toàn vẹn & định dạng
- Đã dịch và rà soát đầy đủ 41/41 đoạn theo đúng thứ tự trong tệp nguồn, giữ nguyên `segment_id` và `source_sha256`.
- Đảm bảo bảo toàn thẻ nhấn mạnh (`<html:em>` -> `*...*`) theo đúng `DEC-P01-002` tại các đoạn `p000279` (hai cụm nhấn mạnh), `p000283`, `p000293`, `p000296`, `p000297`, `p000298`, `p000299`, `p000300`, và không tự ý thêm dấu `*...*` ở các đoạn khác.
- Đã cập nhật trường `status` của toàn bộ 41 dòng từ `"draft"` sang `"reviewed"`.

## 2. Xử lý Findings từ Argon Review (`reviews/prose/vol-08/ch-06-b08-argon-review.yml`)
- **`p000269` (minor / meaning_nuance)**: Đã đổi `"phải vắt kiệt sức mới thốt ra được"` thành `"phải khó nhọc lắm mới thốt ra được"` để diễn tả đúng sắc thái nghẹn giọng vì căng thẳng, sợ hãi.
- **`p000287` (minor / addition)**: Đã lược bỏ cụm giải thích tự thêm `"để giữ thành"`, giữ đúng `"cam kết dốc toàn bộ mọi thứ hiện có giờ đã là chuyện của quá khứ xa xôi rồi"` theo `locked_choices`.
- **`p000306` (minor / style_naturalness)**: Đã đổi `"ngay cả nhóm nhà báo giới hạn kia đặt chân vào"` thành `"ngay cả nhóm nhỏ nhà báo được phép vào một cách hạn chế như vừa qua đặt chân tới"` để tự nhiên, rõ nghĩa và tuân thủ `locked_choices`.

## 3. Nhất quán thuật ngữ, nhân vật, đại từ xưng hô & Locked Choices
- **Bối cảnh & Xưng hô**:
  - Đối thoại giữa Loria và vị đại tá Quân đội Liên bang nối tiếp trực tiếp từ cuối batch `ch-06-b07`: dùng cặp đại từ `tôi` - `đồng chí` / `Đồng chí Đại tá`, vị đại tá đáp lễ phép (`Vâng` ở `p000268`, `p000304`), giữ đúng không khí chính trị Liên bang.
  - Tự sự ngôi thứ ba gọi Loria và vị đại tá là `ông ta` (thống nhất với `ch-06-b07/p000266`).
  - Độc thoại nội tâm của Loria khi nghĩ về Tanya (`p000296`–`p000300`): dùng `ta` và gọi Tanya là `*Nàng...*`, `*Nàng tiên nhỏ đáng yêu, tinh nghịch của ta...*`, `*Tiểu ác quỷ của ta...*`; trong khi lời thoại bên ngoài (`p000295`, `p000301`) giữ vẻ thản nhiên giả tạo, gọi là `con bé` / `nó`.
- **Thuật ngữ & Pending Terms Recommendations**:
  - Đã kiểm tra và áp dụng nhất quán toàn bộ `pending_term_recommendations` và `locked_choices` trong `ch-06-b08-argon-review.yml`:
    - `Lục quân Đế quốc` / `Cụm B` (`p000267`, `p000278`, `p000291`)
    - `dân ủy` / `Đồng chí Đại tá` / `các đồng chí chiến hữu` (`p000269`, `p000272`, `p000274`)
    - `sự bạo ngược của khoảng cách` / `chủ nghĩa dân tộc` (`p000278`)
    - `ban lãnh đạo Đảng` / `Tổng Bí thư` / `đồng chí Tổng Bí thư` / `Josefgrad` (`p000280`, `p000282`, `p000283`, `p000286`, `p000287`, `p000288`)
    - `đòn tấn công kiềm chế` (`p000292`)
    - `Ác quỷ sông Rhine` (`p000295`)
    - `đơn vị đa quốc gia` / `Đồng chí Đại tá Mikel` / `Đại tá Mikel` / `pháp sư hải quân đánh bộ` / `Drake` / `Khối Thịnh vượng chung` (`p000302`–`p000305`)
    - `Chủ nghĩa Cộng sản` / `Quân đội Khối Thịnh vượng chung` (`p000306`, `p000307`)
