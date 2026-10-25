# Báo cáo tự kiểm tra ngữ nghĩa — Batch `vol-03-ch-08-b01`

- **Phạm vi**: `YS-LN03/Text/chapter008_001.xhtml/p000002` – `YS-LN03/Text/chapter008_001.xhtml/p000017` (16 đoạn)
- **Người dịch**: `argon-low`
- **Trạng thái bản dịch**: `reviewed`

## 1. Kiểm tra tính toàn vẹn và đối chiếu với nguồn
- Toàn bộ 16 đoạn từ `chapter008_001.xhtml/p000002` đến `chapter008_001.xhtml/p000017` (Lời bạt Tập 3 của tác giả Carlo Zen) đã được dịch đầy đủ, giữ nguyên thứ tự, mã đoạn (`id`) và `source_sha256` (`74f557a5f02ccc0308519579028d46fc0a89698a81e15219feb3add22ffc96a4`).
- Không làm rò rỉ câu văn tiếng Anh từ nguồn vào báo cáo hoặc ghi chú.

## 2. Xưng hô, đại từ và giọng văn (`DEC-P01-001`)
- Đây là phần Lời bạt của tác giả Carlo Zen trò chuyện trực tiếp với độc giả, không có sự xuất hiện của nhân vật Tanya hay mạch trần thuật trong truyện.
- Tác giả tự xưng `tôi` (và dùng `mình` ở các mệnh đề tự quy chiếu nội tâm như `p000008`, `p000011`–`p000013`), gọi độc giả là `các bạn`, giữ đúng giọng điệu hài hước, tự trào pha lẫn lối nói quân sự dí dỏm đặc trưng của tác giả.

## 3. Bảo toàn nhấn mạnh (`DEC-P01-002`)
- Chỉ 2 đoạn có thẻ nhấn mạnh (`<em>`) trong XHTML gốc và đã được bảo toàn chính xác bằng dấu `*...*` đúng phạm vi nhấn mạnh của nguồn:
  - `chapter008_001.xhtml/p000008`: hai cụm `*Cái quái gì thế này?*` và `*Ồ?*`
  - `chapter008_001.xhtml/p000010`: cụm suy nghĩ `*Lẽ ra mọi chuyện đâu phải thành ra thế này*`
- Đoạn `p000017` chỉ có thẻ `<span class="bold-italic">` cho tên tác giả (không phải thẻ `<em>`/`<i>`), nên giữ văn bản thường theo quy ước `DEC-P01-002` và quy tắc kiểm tra của validator.
- Các ký hiệu dấu ngoặc đặc biệt trong nguồn như `[Ngày X]` (`p000009`) và `<Có lẽ vậy.>` (`p000010`) được bảo toàn nguyên vẹn.

## 4. Thuật ngữ và tính nhất quán nội bộ
- **Thuật ngữ đã có tiền lệ từ sổ pending và các chương trước**:
  - `Tổng hành dinh` (`p000004`) — nhất quán với cách dịch trong chính văn.
  - `ma sát` (`p000004`) — giữ nguyên khái niệm lý thuyết quân sự của Clausewitz trong ngoặc kép.
  - `gặp ảo giác` (`p000003`) — đồng bộ với mục `P05-hallucination` (`ảo giác`).
  - `chiến tranh chớp nhoáng` (`p000015`) — dịch sát nghĩa ẩn dụ quân sự cho tốc độ ra mắt tập tiếp theo.
- **Đề xuất thuật ngữ tạm mới (`pending_terms`)**:
  - `kịch truyền thanh` (`p000003`, `p000016`) — dịch tự nhiên cho sản phẩm quà tặng kèm có giới hạn thời gian của Tập 3.
  - `Tsubakiya Design` (`p000016`) — giữ nguyên tên riêng đơn vị thiết kế sách.

## 5. Sign-off (Bước 2a — `vol-03-ch-08-b01-translator-signoff`)
- **Báo cáo review đối chiếu**: `reviews/prose/vol-03/ch-08-b01-argon-review.yml` (`status: approved_for_polish`, `serious: 0`, `moderate: 0`, `minor: 0`, `findings: []`, `unresolved_findings: []`).
- **Xử lý findings**: Không phát sinh lỗi cần chỉnh sửa câu chữ; giữ nguyên toàn bộ các lựa chọn đã khóa (`locked_choices`) và các đề xuất thuật ngữ/giọng văn (`afterword_terms_and_names_vol03_ch08_b01`, `author_afterword_voice_and_address_vol03_ch08_b01`).
- **Cập nhật trạng thái**: Đã chuyển `status` của toàn bộ 16 dòng (`YS-LN03/Text/chapter008_001.xhtml/p000002` – `YS-LN03/Text/chapter008_001.xhtml/p000017`) trong `translations/vol-03/ch-08-b01.jsonl` từ `draft` sang `reviewed` để bàn giao khóa baseline cho bước tiếp theo.
