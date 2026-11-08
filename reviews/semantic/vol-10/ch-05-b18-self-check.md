# Báo cáo tự kiểm ngữ nghĩa — `vol-10-ch-05-b18`

- **Task ID**: `vol-10-ch-05-b18` (`vol-10-ch-05-b18-translator-signoff`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter024.xhtml/p000654` → `YS-LN10/Text/chapter024.xhtml/p000686` (33 đoạn)
- **Tập tin bản dịch**: `translations/vol-10/ch-05-b18.jsonl`

## 1. Kiểm tra tính đầy đủ và cấu trúc (Sign-off)

- Đã dịch và rà soát đầy đủ 33/33 đoạn từ `p000654` đến `p000686`, giữ nguyên thứ tự và mã đoạn.
- Toàn bộ 33 dòng đã được cập nhật sang `status: "reviewed"`, giữ `translator: "argon-low"`, `source_sha256` và `glossary_version` khớp với `handoffs/vol-10/ch-05-b18.yml`.
- Không bỏ sót câu, mệnh đề, phủ định, câu hỏi giả định hay quan hệ nhân quả nào; tuân thủ toàn bộ `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-10/ch-05-b18-argon-review.yml`.

## 2. Xử lý các Findings trong Argon Review

- `YS-LN10/Text/chapter024.xhtml/p000667` (`minor` / `style_register`): Đã tiếp nhận đề xuất chỉnh câu kết in nghiêng thành `*Chiến tranh đáng lẽ chỉ nên được tiến hành khi có thể đánh một cách an toàn và dễ dàng thôi chứ!*` để giữ đúng sắc thái châm ngôn lý thuyết quân sự của Tanya.
- `YS-LN10/Text/chapter024.xhtml/p000686` (`minor` / `word_choice`): Đã tiếp nhận đề xuất đổi `Đám tân binh mới hơn` thành `Đám lính mới tuyển bổ sung` để tránh lặp nghĩa và tự nhiên hơn, đồng thời giữ nguyên cấu trúc tương phản năng lực đã khóa.

## 3. Xưng hô, điểm nhìn và giọng văn

- **Trần thuật góc nhìn khách quan / đa điểm nhìn** (`p000654`–`p000665`, `p000667`–`p000669`, `p000671`–`p000674`, `p000676`–`p000679`, `p000681`–`p000684`, `p000686`):
  - Dùng đại từ `cô` cho Trung tá Tanya von Degurechaff trong lời dẫn ngôi thứ ba (`p000667`, `p000668`, `p000682`), nhất quán với các lô trước của Tập 10.
  - Dùng đại từ `anh` cho Trung tá Drake trong lời dẫn ngôi thứ ba (`p000656`–`p000659`, `p000669`, `p000671`–`p000673`, `p000683`–`p000684`, `p000686`).
- **Độc thoại và lời thoại trực tiếp**:
  - Câu cảm thán nội tâm của Tanya ở `p000667` và câu suy nghĩ trực tiếp của Drake ở `p000673` giữ đúng giọng điệu bức bối giữa không chiến ở độ cao lớn.
  - Lời than của Tanya (`p000666`) và Drake (`p000670`), lời than đồng thanh của cả hai chỉ huy (`p000675`), cùng các mệnh lệnh tác chiến của Tanya (`p000680`) và Drake (`p000685`) được dịch quyết liệt, gãy gọn, sát sắc thái quân sự.

## 4. Thuật ngữ và tính nhất quán với Canon / Pending Terms

- `Lục quân Đế quốc` / `Đế quốc` / `tiểu đoàn pháp sư Đế quốc` (`p000654`, `p000679`, `p000683`)
- `Trung tá Drake` / `Drake` / `hai vị trung tá` (`p000656`, `p000669`, `p000671`, `p000672`, `p000678`, `p000682`, `p000683`, `p000686`)
- `Chỉ huy Ballmer` / `lữ đoàn` (`p000656`, `p000686`)
- `đại đội pháp sư át chủ bài` / `đại đội át chủ bài` / `tiểu đoàn pháp sư tinh nhuệ` (`p000659`, `p000686`)
- `Ác quỷ sông Rhine` / `mặt trận phía đông` (`p000659`, `p000667`)
- `Thượng đế` (`p000671`)
- `tiểu đoàn pháp sư hải quân đánh bộ` / `pháp sư hải quân đánh bộ` (`p000671`, `p000683`)
- `ma năng` / `quả cầu tính toán` / `thuật thức` / `tập trung hỏa lực` / `hỏa lực chế áp` (`p000672`, `p000676`, `p000680`, `p000685`, `p000686`)
- `chiến thuật chặt đầu chỉ huy` / `hệ thống chỉ huy` (`p000683`, `p000684`)

## 5. Kiểm tra định dạng nhấn mạnh (`DEC-P01-002`) và dấu câu đặc biệt

- Chỉ sử dụng dấu `*...*` tại đúng 3 đoạn có nhấn mạnh (`<html:em>`) trong nguồn:
  - `p000661`: `*A*`
  - `p000667`: `*Chiến tranh đáng lẽ chỉ nên được tiến hành khi có thể đánh một cách an toàn và dễ dàng thôi chứ!*`
  - `p000673`: `*Đầu mình đau chết mất*`
- 30 đoạn còn lại hoàn toàn không chứa ký tự `*`.
- Bảo toàn dấu ngoặc kép đôi `““...””` tại `p000675` để biểu thị câu cảm thán đồng thanh của hai vị chỉ huy theo đúng bản gốc.
