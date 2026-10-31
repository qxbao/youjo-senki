# Báo cáo tự kiểm dịch thuật — `vol-05-ch-03-b16` (Sign-off)

- **Task ID**: `vol-05-ch-03-b16-translator-signoff` (`parent_task_id`: `vol-05-ch-03-b16`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN05/Text/part0020.html/p000194` – `YS-LN05/Text/part0020.html/p000257` (64 đoạn)
- **Tệp đích**: `translations/vol-05/ch-03-b16.jsonl`

## 1. Kiểm tra tính đầy đủ và cấu trúc kỹ thuật
- Đã dịch và rà soát đầy đủ 64/64 đoạn theo đúng thứ tự trong tệp nguồn, không gộp hay tách đoạn.
- Toàn bộ 64 dòng trong tệp JSONL đã được cập nhật sang `status: "reviewed"`, giữ nguyên `translator: "argon-low"`, `glossary_version` và `source_sha256` khớp chính xác với thông tin bàn giao.
- Đã bảo toàn đầy đủ định dạng nhấn mạnh `*...*` tương ứng với thẻ in nghiêng trong XHTML nguồn ở các đoạn `p000197`, `p000198`, `p000206`–`p000214`, `p000216`–`p000220`, `p000222`–`p000225`, `p000227`–`p000229`, `p000232`, `p000235`, `p000236`, `p000240`, `p000241`, `p000243`, `p000244`. Các đoạn không có thẻ nhấn mạnh trong XHTML nguồn (`p000230`, `p000231`) được giữ nguyên dạng văn bản thường theo đúng quy chuẩn `DEC-P01-002`.

## 2. Xử lý các Findings từ Argon Review (`reviews/prose/vol-05/ch-03-b16-argon-review.yml`)
- **`p000203` (minor)**: Đổi `"Tình hình bên đó thế nào?!"` thành `"Tình trạng của chúng thế nào?!"` để làm rõ câu hỏi nhắm vào đơn vị Pháp sư Định danh địch vừa bị phát hiện.
- **`p000218` & `p000221` (minor)**: Đổi `"Các cô"` ở `p000218` thành `"Đơn vị của cô"` và `"của các cô"` ở `p000221` thành `"của đơn vị cô"`, tránh mặc định toàn bộ đơn vị tình nguyện đi cùng Mary đều là nữ giới theo `DEC-P01-001`.
- **`p000224` (minor)**: Đổi `"trấn giữ hậu phương"` thành `"chốt giữ tại chỗ"` để tránh nhầm lẫn với vùng hậu phương và phản ánh đúng nhiệm vụ ở lại canh giữ ngay trên tàu.
- **`p000244` (minor)**: Đổi `"*Chúng tao sẽ không để lũ mày thoát tội đâu.*"` thành `"*Chúng mình sẽ không để bọn ngươi thoát tội đâu.*"` nhằm giữ mạch đại từ độc thoại nội tâm `"mình / chúng mình"` xuyên suốt của Mary Sue.
- **`p000248` (minor)**: Đổi `"em"` thành `"tôi"` (`"“Trung úy Grantz, tôi không sao đâu…”"`) theo đúng chuẩn xưng hô quân ngũ trong `DEC-P01-001`.

## 3. Điểm nhìn, giọng văn và quy chuẩn xưng hô
- **Cụm 1 (`p000194`–`p000198`) — Tiểu đoàn Pháp sư Trên không số 203**:
  - Đối thoại giữa Visha và Weiss trên mạng vô tuyến dùng `tôi – cô` (`Trung úy Serebryakov`), Weiss gọi toàn đơn vị là `toàn quân`.
  - Độc thoại nội tâm của Tanya dùng `mình` / `bọn mình`; trần thuật ngôi thứ ba gọi `Trung tá Tanya von Degurechaff`.
- **Cụm 2 (`p000199`–`p000244`) — Điểm nhìn của Mary Sue trên tàu RMS *Queen of Anjou***:
  - Trần thuật ngôi thứ ba gọi `Mary Sue` / `Mary` và dùng đại từ `cô`.
  - Độc thoại nội tâm của Mary Sue dùng `mình` / `chúng mình` xuyên suốt (kể cả câu thề quyết tâm ở `p000244`: `chúng mình – bọn ngươi`).
  - Đối thoại giữa Mary Sue và Trung tá Drake: Mary xưng `chúng tôi`, gọi `Trung tá Drake` / `thưa Trung tá`; Drake gọi `Trung úy Sue`, xưng `tôi` / `chúng tôi` và gọi nhóm của Mary là `cô` / `đơn vị của cô`.
- **Cụm 3 (`p000245`–`p000257`) — Điểm nhìn của Tanya**:
  - Trần thuật ngôi thứ ba về Tanya dùng `Tanya` / `nó`; độc thoại nội tâm của Tanya dùng `mình` / `bọn mình` với giọng thực dụng, duy lý, coi trọng bảo toàn nguồn nhân lực.
  - Đối thoại giữa Grantz và cấp dưới bị thương (`p000247`–`p000249`): cấp dưới gọi `Trung úy Grantz`, xưng `tôi`; Grantz xưng `tôi`, nhắc tới Tanya là `Trung tá`.
  - Đối thoại giữa Weiss và Tanya (`p000255`–`p000256`): Weiss hỏi ngắn gọn `Trung tá?`, Tanya ra lệnh rút lui với đại từ `chúng ta`.

## 4. Nhất quán thuật ngữ và các mục đề xuất (`pending_term_recommendations` & `locked_choices`)
- Đã tuân thủ toàn bộ 64 `locked_choices` và áp dụng nhất quán các thuật ngữ trong `canon/glossary.yml` cùng `pending_term_recommendations`:
  - `mặt trận Rhine` (`p000194`, `p000204`)
  - `RMS *Queen of Anjou*` (`p000197`, `p000218`)
  - `đơn vị Pháp sư Định danh` (`p000202`)
  - `pháp sư hải quân đánh bộ` (`p000215`)
  - `Trung tá Drake` (`p000216`, `p000220`)
  - `Trung úy Sue` (`p000218`, `p000237`)
  - `nhiệm vụ yểm trợ trực tiếp` / `đơn vị yểm trợ trực tiếp` (`p000218`, `p000237`)
  - `Khối Thịnh vượng chung` (`p000219`, `p000254`)
  - `đội quân tình nguyện` (`p000219`, `p000228`)
  - `nguồn nhân lực` (`p000246`)
  - `Trung úy Grantz` / `trung úy` (`p000248`, `p000249`)
  - `thuật thức bắn tỉa tầm xa` (`p000254`)
  - `phó chỉ huy` (`p000257`)
  - `sự tiêu hao nhân lực` (`p000257`)
