# Báo cáo tự kiểm (Self-Check) — `vol-08-ch-06-b07` (Sign-off)

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-06-b07-translator-signoff` (parent: `vol-08-ch-06-b07`)
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter022.xhtml/p000227` đến `YS-LN08/Text/chapter022.xhtml/p000266` (40 đoạn)
- **Tệp bản dịch**: `translations/vol-08/ch-06-b07.jsonl`
- **Báo cáo phản biện đã xử lý**: `reviews/prose/vol-08/ch-06-b07-argon-review.yml`

## 2. Kiểm tra tính đầy đủ & siêu dữ liệu
- **Số dòng JSONL**: 40/40 đoạn, khớp 1-1 với tệp nguồn.
- **Trạng thái (`status`)**: Đã cập nhật toàn bộ 40/40 dòng từ `"draft"` sang `"reviewed"` sau khi xử lý đầy đủ review Argon.
- **Khóa định danh & băm**: `segment_id`, `source_sha256` và `glossary_version` khớp chính xác với `handoffs/vol-08/ch-06-b07.yml`.
- **Không sót đoạn / không gộp tách đoạn**: Giữ nguyên ranh giới của từng đoạn văn, dòng chuyển cảnh và lời thoại.

## 3. Xử lý các Findings từ Argon Review
- **`YS-LN08/Text/chapter022.xhtml/p000227` (minor / `tone_nuance`)**: Đổi `“lại định giở trò này nữa đấy à?!”` thành `“lại thế này nữa đấy à?!”` để loại bỏ sắc thái miệt thị không có trong nguyên bản.
- **`YS-LN08/Text/chapter022.xhtml/p000228` (minor / `pronouns_address`)**: Đổi `“Xin ngài đấy!”` thành `“Xin Trung tá đấy!”` theo đúng chuẩn xưng hô cấp dưới gọi Tanya bằng quân hàm `Trung tá` trong tập 8 và `locked_choices`.
- **`YS-LN08/Text/chapter022.xhtml/p000251` (minor / `pov_pronouns`)**: Đổi `“chúng tôi từng thấy”` thành `“chúng ta từng thấy”` để thống nhất đại từ ngôi thứ nhất số nhiều trong độc thoại nội tâm của Tanya với các đoạn lân cận (`p000250`, `p000258`, `p000259`).

## 4. Kiểm tra quy chuẩn xưng hô, giọng điệu và mạch trần thuật (`DEC-P01-001` & `locked_choices`)
- **Mạch trần thuật ngôi thứ ba (`p000230` – `p000232`, `p000236`, `p000238`, `p000241`, `p000245`, `p000260` – `p000261`, `p000264`, `p000266`)**:
  - Ở cảnh của Tiểu đoàn 203, tiếp nối nhất quán với các lô trước của chương 6 (`ch-06-b05`, `ch-06-b06`), gọi Tanya bằng tên riêng hoặc đại từ `cô`, gọi cấp dưới (`Grantz`, `Weiss`) là `anh ta` / `thuộc cấp` / `binh sĩ của mình`.
  - Ở cảnh tại Moskva (`p000264`, `p000266`), gọi `Loria` bằng danh xưng chức vụ và tên riêng, gọi viên đại tá chuyên nghiệp đối diện là `ông ta`.
- **Mạch độc thoại nội tâm & nhận định ngôi thứ nhất của Tanya (`p000234` – `p000235`, `p000239` – `p000240`, `p000246`, `p000250` – `p000254`, `p000258` – `p000259`)**:
  - Tự quy chiếu cá nhân bằng `mình` (`p000239`, `p000250`, `p000258`).
  - Khi hồi tưởng hoạt động chung của đơn vị hoặc suy tính nguyên tắc chung của phe Đế quốc dùng nhất quán `chúng ta` (`p000251`, `p000259`).
- **Mạch đối thoại (`p000227` – `p000229`, `p000233`, `p000236` – `p000237`, `p000242` – `p000244`, `p000247` – `p000249`, `p000255` – `p000257`, `p000260` – `p000262`, `p000265`)**:
  - Tanya giữ giọng chỉ huy thực dụng, điềm tĩnh, xưng `tôi` / `chúng ta`, gọi cấp dưới là `Trung úy Grantz`, `Thiếu tá` (`Weiss`) và `anh`.
  - Grantz khẩn khoản xin truy kích ở `p000228` (`Xin Trung tá đấy!`) và tuân lệnh ở `p000237` (`...Đã rõ.`).
  - Sĩ quan cấp dưới / Weiss hỏi thăm và trao đổi lễ phép với Tanya (`thưa Trung tá` / `Trung tá` ở `p000243`, `tôi` – `chúng ta` ở `p000256`).
  - Loria hỏi ngắn gọn, lạnh lùng (`Chúng ta thua sao?` ở `p000265`).

## 5. Kiểm tra định dạng nhấn mạnh (`DEC-P01-002`)
- Chỉ bảo toàn định dạng in nghiêng (`*...*`) tại đúng các vị trí có thẻ nhấn mạnh trong nguyên bản XHTML:
  1. `p000245`: Câu định nói tiếp trong suy nghĩ của Tanya (`*Đó là về tầm quan trọng của việc thay đổi góc nhìn*`).
  2. `p000246`: Ba cụm từ nhấn mạnh trong phép chơi chữ về góc nhìn từ trên cao xuống bên dưới (`*bỏ lỡ*`, `*nhìn xuống mà bỏ sót*`, `*bên dưới*`).
  3. `p000258`: Tên tác phẩm binh thư (`*Binh pháp Tôn Tử*`).
- Toàn bộ 37 đoạn còn lại không có nhấn mạnh trong nguồn và không tự ý thêm bất kỳ dấu `*...*` nào.

## 6. Kiểm tra thuật ngữ & đối chiếu Canon / Pending Terms / Locked Choices
- Đã kiểm tra và tuân thủ đầy đủ toàn bộ 40 mục `locked_choices` và 10 mục `pending_term_recommendations` trong `reviews/prose/vol-08/ch-06-b07-argon-review.yml`:
  - `Trung úy Grantz`, `Grantz`, `Thiếu tá` (`Weiss`), `Weiss`, `Trung tá` (`Tanya`), `Loria`, `đại tá`.
  - `lực lượng mặt đất`, `lực lượng mặt đất của địch`, `hiệu quả chi phí`, `tỷ lệ tiêu diệt`, `quỹ tín thác`, `giao dịch lướt sóng trong ngày`, `vốn con người`, `nguồn nhân lực`.
  - `cuộc tháo chạy tán loạn`, `Cộng hòa François`, `cánh cửa xoay`, `cuộc rút lui có tổ chức`.
  - `khí tài pháo binh của Liên bang`, `phí phát hiện`, `các kênh thu mua`, `quy trình tiếp vận`.
  - `*Binh pháp Tôn Tử*`, `Tôn Tử`, `bản quốc`, `nền kinh tế cướp bóc`, `thu giữ chiến lợi phẩm`, `Đế quốc Mỹ`.
  - `LIÊN BANG, MỘT NƠI NÀO ĐÓ TẠI MOSKVA, VĂN PHÒNG BỘ DÂN ỦY NỘI VỤ, CƠ QUAN TỒN TẠI ĐỂ PHỤC VỤ NHÂN DÂN`, `ủy viên dân ủy nội vụ`.

## 7. Kết quả chạy công cụ kiểm tra
- Chạy `python3 tools/validate_translation.py --handoff handoffs/vol-08/ch-06-b07.yml --source work/vol-08/batches/ch-06-b07-source.jsonl --translation translations/vol-08/ch-06-b07.jsonl` đạt kết quả `PASS`.
