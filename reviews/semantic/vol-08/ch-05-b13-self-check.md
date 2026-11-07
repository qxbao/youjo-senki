# Báo cáo tự kiểm (Semantic Self-Check) — `vol-08-ch-05-b13` (Sign-off)

- **Task ID**: `vol-08-ch-05-b13-translator-signoff` (parent: `vol-08-ch-05-b13`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter018.xhtml/p000439` – `YS-LN08/Text/chapter018.xhtml/p000480` (42 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`
- **Trạng thái dòng (`status`)**: Đã cập nhật toàn bộ 42/42 dòng từ `draft` sang `reviewed`.

## 1. Xử lý các Findings từ Argon Review (`reviews/prose/vol-08/ch-05-b13-argon-review.yml`)
- **`YS-LN08/Text/chapter018.xhtml/p000440` (minor - meaning_and_precision)**:
  - **Vấn đề**: Cụm "thọc sườn hậu phương địch" ghép nhầm khái niệm đánh vào sườn với đánh vào hậu phương; đồng thời câu đầu bổ sung sớm từ "ma lực" khi ở `p000440` chỉ mới nêu tín hiệu nói chung.
  - **Xử lý**: Đã chỉnh thành "chế áp tín hiệu phục vụ cuộc tách đội" và "đánh úp vào hậu phương địch".
- **`YS-LN08/Text/chapter018.xhtml/p000441` (minor - terminology_consistency)**:
  - **Vấn đề**: Cần đồng bộ "sĩ quan pháp sư hàng không" / "pháp sư hàng không" và "tín hiệu ma lực" về phương án tạm xuyên suốt tập 8 ("sĩ quan pháp sư trên không" / "pháp sư trên không" và "tín hiệu ma năng").
  - **Xử lý**: Đã đồng bộ thành "các sĩ quan pháp sư trên không" (`p000441`), "pháp sư trên không" (`p000480`), và "tín hiệu ma năng" (`p000441`, `p000444`, `p000459`).

## 2. Kiểm tra nghĩa, ngữ cảnh và mạch văn
- **Độ phủ**: Đầy đủ 42/42 đoạn từ `p000439` đến `p000480`, bảo toàn `segment_id` và `source_sha256` của từng dòng.
- **Mạch nội dung**:
  - `p000439`–`p000446`: Giải thích nghịch lý chiến trường từ góc nhìn trần thuật: mệnh lệnh chính thống, đúng giáo phạm của Trung tá von Degurechaff buộc toàn bộ pháp sư dưới quyền chế áp tín hiệu ma năng để bí mật tách đội khỏi cứ điểm Soldim 528 vô tình tạo ra một khoảng thiếu hụt bất thường so với trạng thái sinh hoạt thường ngày (khi lực lượng đồn trú thay phiên chợp mắt và không thể giấu tín hiệu 24/24 giờ).
  - `p000447`–`p000470`: Góc nhìn của Trung tá Drake (sĩ quan ma pháp hải quân đánh bộ thuộc Khối Thịnh vượng chung đang quan sát từ tuyến bao vây thứ nhất). Giữa trận địa phòng ngự hiệp đồng kiên cố gồm bộ binh, pháo binh và thiết giáp của Đế quốc, Drake nhận ra sự sụt giảm đột ngột của các tín hiệu ma năng quân địch. Bằng trực giác chiến trường dày dạn, anh loại trừ khả năng nghi binh phục kích và kết luận tiểu đoàn pháp sư tinh nhuệ cùng "con quái vật đó" đã rút khỏi cứ điểm.
  - `p000471`–`p000480`: Drake lập tức chạy từ khu vực của quân Khối Thịnh vượng chung tới sở chỉ huy đơn vị đa quốc gia. Trên đường đi, anh bị sĩ quan chính trị Liên bang là Trung úy Tanechka chặn hỏi, nhưng nhanh chóng tận dụng cô làm cầu nối để yêu cầu gặp Đại tá Mikel và báo cáo việc quân Đế quốc đã bí mật rút các đơn vị pháp sư trên không (những kẻ từng gây ác mộng tại Arene) ra ngoài.

## 3. Kiểm tra quy chuẩn xưng hô, giọng điệu và `locked_choices`
- Tuân thủ đầy đủ toàn bộ `locked_choices` và `pending_term_recommendations` trong `ch-05-b13-argon-review.yml`.
- **Trần thuật góc nhìn thứ ba theo Drake (`p000447`–`p000480`)**: Dùng đại từ `anh` cho Drake, giữ giọng văn thực chiến, gai góc của một sĩ quan hải quân đánh bộ kỳ cựu. Trong câu độc thoại tự nhủ trực tiếp (`p000448`, `p000458`), Drake tự xưng `mình`.
- **Đối thoại giữa Trung úy Tanechka và Trung tá Drake (`p000473`–`p000478`)**:
  - Trung úy Tanechka gọi Drake là `Trung tá Drake` / `Đồng chí Trung tá`, xưng `tôi` – `ngài`.
  - Trung tá Drake gọi Tanechka là `Trung úy Tanechka`, nhắc tới chỉ huy Liên bang là `Đại tá Mikel`, xưng `tôi`. Trong trần thuật nội tâm của Drake (`p000477`), Tanechka được gọi là `cô ta`.

## 4. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002`)
- `YS-LN08/Text/chapter018.xhtml/p000446`: `*Vậy thì…* Hãy tiếp tục nào.` (khớp 1 cụm in nghiêng).
- `YS-LN08/Text/chapter018.xhtml/p000458`: `*Tại sao nhỉ?*` (khớp 1 cụm in nghiêng).
- Toàn bộ 40 đoạn còn lại không có thẻ nhấn mạnh trong XHTML gốc và bản dịch hoàn toàn không phát sinh dấu `*`.
