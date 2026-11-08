# Báo cáo tự kiểm (Translator Self-Check & Sign-off) — `vol-10-ch-04-b08`

- **Task ID**: `vol-10-ch-04-b08-translator-signoff` (parent: `vol-10-ch-04-b08`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter022.xhtml/p000056` đến `YS-LN10/Text/chapter022.xhtml/p000082` (27 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ, trạng thái Sign-off và bảo toàn cấu trúc
- Đã dịch và rà soát đầy đủ 27/27 đoạn theo đúng thứ tự nguồn từ `p000056` đến `p000082`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Đã cập nhật trường `status` của toàn bộ 27 dòng trong `translations/vol-10/ch-04-b08.jsonl` từ `draft` sang `reviewed`.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter022.xhtml/p000060`: `*bên ngoài*`.
  - `YS-LN10/Text/chapter022.xhtml/p000069`: `*thứ này*`.
  - `YS-LN10/Text/chapter022.xhtml/p000070`: `*thứ này*`.
- Tất cả 24 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.

## 2. Xử lý các Findings từ Argon Review (`reviews/prose/vol-10/ch-04-b08-argon-review.yml`)
- **`YS-LN10/Text/chapter022.xhtml/p000057`** (`minor`): Tiếp nhận khuyến nghị chỉnh cụm `"tỉnh mộng khỏi giấc mộng ban ngày nhỏ nhoi của mình rồi!"` thành `"tỉnh khỏi giấc mộng ban ngày nhỏ nhoi của mình rồi!"` để tránh lặp từ `"mộng"` sát nhau, giúp câu thoại tự nhiên và gọn hơn trong khi vẫn bảo toàn `locked_choices`.
- **`YS-LN10/Text/chapter022.xhtml/p000061`** (`minor`): Tiếp nhận khuyến nghị đổi cụm `"thật khó coi"` thành `"chẳng dễ chịu gì"` (`"Chứng kiến cảnh đó lúc nào cũng chẳng dễ chịu gì—cảnh một người đánh mất vẻ điềm tĩnh và phơi bày những cảm xúc tăm tối vốn dồn nén trong lòng…"`) để khớp tự nhiên với mạch cảm thông nối tiếp ở `p000062` và bảo toàn đầy đủ `locked_choices`.

## 3. Xưng hô, giọng điệu và tính nhất quán với `locked_choices` (`DEC-P01-001`)
- Bảo đảm tuân thủ tuyệt đối 27/27 mục `locked_choices` trong báo cáo review của Argon.
- **Trần thuật và độc thoại nội tâm của Tanya (`p000056`, `p000058`–`p000068`, `p000070`, `p000072`, `p000074`, `p000076`–`p000077`, `p000079`–`p000081`)**:
  - Tự quy chiếu trong nội tâm ngôi thứ nhất của Tanya dùng `mình` (`p000060`, `p000062`, `p000065`, `p000072`); câu trần thuật ngôi thứ ba gọi Tanya là `Tanya` / `cô` (`p000058`, `p000063`–`p000065`, `p000068`, `p000070`, `p000076`, `p000081`).
  - Quy chiếu `Tham tán Conrad` là `vị tham tán` / `ông ta` / `người đàn ông này`; quy chiếu `Đại tá Lergen` là `Đại tá Lergen` / `Lergen` / `anh` (`p000070`).
- **Đối thoại giữa Tham tán Conrad và Đại tá Lergen (`p000057`, `p000069`, `p000071`, `p000073`, `p000075`, `p000078`, `p000082`)**:
  - Tham tán Conrad xưng `tôi` (hoặc `chúng ta` - `mình` khi tự giễu về ảo mộng chung ở `p000057`), gọi Lergen là `ông` (hoặc `các ông` / `các vị` khi nói gộp bên quân đội / hai sĩ quan ở `p000069`, `p000082`), gọi Tanya là `Trung tá Degurechaff` (`p000069`) và chỉ trỏ bằng từ nhấn mạnh `*thứ này*`.
  - Đại tá Lergen xưng `tôi` (hoặc `chúng tôi` khi nói đại diện cho quân đội Đế quốc ở `p000071`), gọi Conrad là `ông` kèm chức danh `thưa Tham tán Conrad` (`p000075`), và gọi Tanya ở ngôi thứ ba là `cô ấy` (`p000071`).

## 4. Thuật ngữ đã áp dụng và xác nhận theo `pending_term_recommendations`
- Toàn bộ các `pending_term_recommendations` trong `ch-04-b08-argon-review.yml` đã được áp dụng nhất quán:
  - `Tham tán Conrad` / `vị tham tán` / `thưa Tham tán Conrad` (`p000062`–`p000063`, `p000065`, `p000067`, `p000069`–`p000070`, `p000074`–`p000075`)
  - `người lính Đế quốc` / `Bộ Ngoại giao` / `Đế quốc` (`p000064`, `p000071`, `p000076`)
  - `Đại tá Lergen` / `Lergen` (`p000058`, `p000064`–`p000065`, `p000068`–`p000070`, `p000074`, `p000077`)
  - `hình nhân quang học` (`p000065`)
  - `Trung tá Degurechaff` (`p000069`)
  - `Moskva` / `Londinium` / `tiểu đoàn pháp sư trên không` (`p000071`)
  - `thiếu úy` (`p000075`, `p000078`–`p000079`)
  - `mặt trận Rhine` / `mặt trận phía đông` (`p000078`)
  - `Junker` (`p000080`)
