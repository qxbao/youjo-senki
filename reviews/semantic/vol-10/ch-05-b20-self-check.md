# Báo cáo tự kiểm ngữ nghĩa — `vol-10-ch-05-b20` (Sign-off)

- **Task ID**: `vol-10-ch-05-b20-translator-signoff`
- **Parent Task ID**: `vol-10-ch-05-b20`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter024.xhtml/p000726` → `YS-LN10/Text/chapter024.xhtml/p000763` (38 đoạn)
- **Tập tin bản dịch**: `translations/vol-10/ch-05-b20.jsonl`

## 1. Kiểm tra tính đầy đủ, cấu trúc và trạng thái Sign-off

- Đã dịch và rà soát đầy đủ 38/38 đoạn theo đúng thứ tự trong `work/vol-10/batches/ch-05-b20-source.jsonl`.
- Mã đoạn (`segment_id`), `source_sha256`, `glossary_version` khớp với `handoffs/vol-10/ch-05-b20.yml`.
- Toàn bộ 38 dòng đã được cập nhật từ `status: "draft"` sang `status: "reviewed"`, giữ `translator: "argon-low"`.

## 2. Xử lý các Findings từ Argon Review (`ch-05-b20-argon-review.yml`)

- **`YS-LN10/Text/chapter024.xhtml/p000758` (`minor` — `style_register`)**:
  - Tiếp nhận khuyến nghị: Chỉnh từ `"cô bay lượn trên cao phía trên anh khi khúc thánh ca của mình chuyển từ cao trào thành một tiếng gầm khải hoàn"` thành `"cô bay vút phía trên anh khi khúc thánh ca của mình chuyển từ cao trào thành một tiếng ngân vang khải hoàn"`, khắc phục lặp từ `"trên"` và giữ đúng âm hưởng thánh ca.
- **`YS-LN10/Text/chapter024.xhtml/p000762` (`minor` — `word_choice`)**:
  - Tiếp nhận khuyến nghị: Chỉnh từ `"kỹ năng tác chiến"` thành `"trình độ kỹ thuật"` để giữ thế đối lập từ vựng trực tiếp với `"công nghệ vượt trội"` ở vế trước.

## 3. Xưng hô, điểm nhìn, thuật ngữ và tuân thủ `locked_choices`

- **Trần thuật góc nhìn thứ ba / đa điểm nhìn** (`p000726`, `p000728`–`p000732`, `p000734`, `p000736`–`p000763`):
  - Dùng đại từ `cô` cho Trung tá Tanya von Degurechaff trong trần thuật và nội tâm tự quy chiếu `mình` khi cần phân biệt (`p000726`, `p000728`–`p000732`, `p000734`, `p000754`–`p000755`, `p000758`), nhất quán với các lô trước của Tập 10.
  - Dùng đại từ `anh` cho Trung tá Drake trong trần thuật khách quan (`p000726`, `p000751`, `p000752`, `p000758`) và `hắn` / `gã` / `kẻ đó` trong dòng suy nghĩ nội tâm thù địch của Tanya khi nhận ra kẻ địch từng giao chiến ở miền đông (`p000728`, `p000729`, `p000731`).
- **Lời thoại trực tiếp trên chiến trường** (`p000727`, `p000733`, `p000735`):
  - Giữa cuộc đụng độ sinh tử ở cự ly gần, cả Tanya (`p000733`) và Drake (`p000735`) đều gầm lên thách thức đối phương với xưng hô `tao` – `mày`, thể hiện đúng sắc thái quyết liệt của hai kẻ cựu thù quyết ăn thua đủ trên không trung.
- **Thuật ngữ và `pending_term_recommendations`**:
  - `lũ Cộng sản`: dùng tại `p000730`.
  - `Bạch Ngân Rỉ Sét`: dùng tại `p000735`.
  - `các thuật thức phát nổ` / `thuật thức phát nổ` / `nhiều thuật thức` / `ma pháp bay` / `thuật thức bay` / `ma pháp cường hóa hô hấp`: dùng nhất quán tại `p000742`–`p000744`, `p000750`–`p000752`, `p000755`, `p000758`.
  - `màn chắn bảo hộ` và `lớp vỏ phòng thủ`: dùng tại `p000745`, `p000755`.
  - `Trung tá Drake` / `Drake`: dùng tại `p000734`, `p000739`, `p000750`.
  - `quả cầu Type 95` / `bốn lõi` / `Quả cầu Tính toán Type 95` / `những quả cầu` / `thánh vật`: dùng tại `p000754`–`p000756`.
- Toàn bộ 38 đoạn bảo đảm tuân thủ tuyệt đối các mục `locked_choices` trong `reviews/prose/vol-10/ch-05-b20-argon-review.yml`.

## 4. Kiểm tra định dạng nhấn mạnh (`DEC-P01-002`)

- Toàn bộ 38 đoạn trong nguồn không chứa thẻ nhấn mạnh (`<em>` / `<i>`), nên bản dịch hoàn toàn không sử dụng dấu `*...*`.
