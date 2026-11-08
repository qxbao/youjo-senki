# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-04-b20` (Sign-off)

- **Task ID**: `vol-10-ch-04-b20-translator-signoff`
- **Parent Task ID**: `vol-10-ch-04-b20`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter022.xhtml/p000481` đến `YS-LN10/Text/chapter022.xhtml/p000520` (40 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc
- Đã rà soát đầy đủ 40/40 đoạn theo đúng thứ tự nguồn từ `p000481` đến `p000520`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 40 dòng đã được cập nhật từ `draft` sang `reviewed`.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`): toàn bộ 40 đoạn trong lô này không có thẻ nhấn mạnh trong `xhtml`, và bản dịch không tự thêm dấu `*...*` ở bất kỳ đoạn nào.

## 2. Xử lý các findings trong `ch-04-b20-argon-review.yml`
- **`YS-LN10/Text/chapter022.xhtml/p000483` (`minor`)**: Đã sửa chính tả và sắc thái chuyển chủ đề thành `"Hai vai mình hơi chùng xuống, và mình quyết định chuyển sang chủ đề khác."`, đồng thời giữ nguyên mọi `locked_choices` của đoạn.
- **`YS-LN10/Text/chapter022.xhtml/p000488` (`minor`)**: Đã lược từ lặp sát nhau thành `"Lĩnh vực chuyên môn của các thuộc cấp dưới quyền mình..."` và `"Xét việc năng lực bảo vệ một hải cảng Đế quốc của họ từng được thử lửa qua thực chiến..."`, bảo toàn toàn bộ `locked_choices` của đoạn.
- **`YS-LN10/Text/chapter022.xhtml/p000520` (`minor`)**: Đã đổi cụm lặp từ `"việc đi săn việc làm"` thành `"chuyện săn tìm việc làm"`, giữ nguyên chuỗi ẩn dụ con tàu đắm và cấu trúc tăng tiến đổi chủ thể theo `locked_choices`.

## 3. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Điểm nhìn nội tâm ngôi thứ nhất và lời độc thoại tự nói một mình trong phòng riêng của Tanya (`p000481` – `p000483`, `p000485`, `p000486`, `p000488`, `p000492`, `p000493`, `p000497`, `p000498`, `p000501`, `p000504`, `p000506`, `p000510` – `p000520`)**:
  - Tự xưng `mình` nhất quán theo `DEC-P01-001` cả trong suy nghĩ nội tâm lẫn khi trở về phòng riêng tự than vãn một mình (`p000512`, `p000519`).
  - Gọi Thiếu tá Weiss là `vị phó chỉ huy` / `Thiếu tá Weiss` / `vị thiếu tá` / `Weiss` / `anh ta` (`p000486`, `p000493`, `p000497`, `p000504`, `p000506`, `p000510`), gọi Trung úy Serebryakov là `viên sĩ quan phụ tá` / `cô ấy` (`p000481`, `p000501`), gọi Đại úy Ahrens là `Ahrens` / `vị đại úy` / `anh ta` (`p000497`, `p000498`), và gọi các sĩ quan/binh sĩ dưới quyền là `họ` / `các sĩ quan của mình` / `các thuộc cấp dưới quyền mình` / `các binh sĩ của mình`.
  - Ở `p000488`, đối tượng phát ngôn tại `p000487` là `vị phó chỉ huy` (Thiếu tá Weiss), nên câu nhận xét đầu đoạn `p000488` được diễn đạt lược đại từ nhân xưng để giữ mạch tự nhiên và tránh mâu thuẫn giới tính của nhân vật.
- **Đối thoại giữa Tanya và các sĩ quan dưới quyền (`p000484`, `p000487`, `p000489` – `p000491`, `p000494` – `p000496`, `p000499`, `p000500`, `p000502`, `p000503`, `p000505`, `p000507` – `p000509`)**:
  - Tanya xưng `tôi` và `chúng ta`, gọi chung các sĩ quan là `các vị`, gọi riêng Thiếu tá Weiss là `Phó chỉ huy` / `Thiếu tá Weiss` / `anh` và Trung úy Serebryakov là `Trung úy Serebryakov` / `cô`.
  - Thiếu tá Weiss và Trung úy Serebryakov xưng `tôi` / `chúng ta`, gọi Tanya là `Thưa Trung tá` / `thưa Trung tá` kèm tiểu từ lễ phép `ạ`, gọi Đại úy Ahrens là `Đại úy Ahrens` / `anh ấy` (`p000494`, `p000496`).

## 4. Thuật ngữ đã áp dụng và xác nhận (`pending_term_recommendations`)
- Toàn bộ 12 mục `pending_term_recommendations` trong `ch-04-b20-argon-review.yml` đã được áp dụng đầy đủ và nhất quán:
  - `viên sĩ quan phụ tá` / `Trung úy Serebryakov` (`p000481`, `p000499`)
  - `quyền con người` / `các quyền con người cơ bản` (`p000482`, `p000518`)
  - `nhiệm vụ biệt kích` / `lực lượng biệt kích` (`p000484`)
  - `vị phó chỉ huy` / `Phó chỉ huy` / `Thiếu tá Weiss` / `Weiss` / `vị thiếu tá` (`p000486`, `p000493`, `p000495`, `p000497`, `p000504`, `p000506`, `p000507`, `p000510`)
  - `Meybert và Tospan` (`p000487`)
  - `Đế quốc` / `chính quốc` (`p000488`, `p000497`, `p000514`)
  - `Thưa Trung tá` / `thưa Trung tá` (`p000490`, `p000508`)
  - `Kampfgruppe` (`p000491`, `p000493`, `p000497`, `p000499`)
  - `Đại úy Ahrens` / `Ahrens` / `vị đại úy` (`p000494`, `p000497`, `p000498`)
  - `mặt trận phía tây` / `mặt trận phía đông` (`p000507`, `p000509`)
  - `vốn con người` (`p000517`)
  - `Being X` (`p000517`)
