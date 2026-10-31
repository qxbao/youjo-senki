# Báo cáo tự kiểm dịch thuật & Sign-off — `vol-06-ch-01-b03`

- **Nhiệm vụ:** `vol-06-ch-01-b03-translator-signoff` (parent: `vol-06-ch-01-b03`)
- **Tập / Chương:** `vol-06`, chương `1`
- **Phạm vi đoạn:** `YS-LN06/Text/part0008.html/p000078` → `YS-LN06/Text/part0008.html/p000115` (38 đoạn)
- **Tác tử dịch:** `argon-low`
- **Trạng thái dòng dịch:** Đã cập nhật toàn bộ 38 dòng từ `draft` sang `reviewed`.

## 1. Tiếp nhận và xử lý Argon Review (`reviews/prose/vol-06/ch-01-b03-argon-review.yml`)
- **`YS-LN06/Text/part0008.html/p000082` (moderate - `meaning_logic`):**
  - *Vấn đề:* Cấu trúc cũ dễ gây hiểu nhầm đối tượng không tỉnh táo là trạng thái của Tanya thay vì hành vi đổ ngân sách và chồng chất nợ nần của các quốc gia tham chiến.
  - *Xử lý:* Đã sửa câu đầu thành `"Trong mắt nó, cảnh từng quốc gia tham chiến đổ dồn ngân sách vào cuộc chiến này và chất chồng nợ nần chẳng có vẻ gì là tỉnh táo."` đúng theo khuyến nghị và `locked_choices`.
- **`YS-LN06/Text/part0008.html/p000078` (minor - `terminology_context`):**
  - *Vấn đề:* Cụm `"bất chấp mùa màng thời tiết"` làm phát sinh nét nghĩa nông nghiệp/canh tác không có trong nguồn.
  - *Xử lý:* Đã đổi thành `"bất chấp đang là mùa nào"` theo đúng khuyến nghị và `locked_choices`.
- **Tuân thủ `locked_choices` & `pending_term_recommendations`:**
  - Đã rà soát toàn bộ 38 đoạn (`p000078`–`p000115`), bảo đảm giữ nguyên mọi lựa chọn đã khóa và áp dụng nhất quán các thuật ngữ đề xuất (`Đế quốc`, `Liên bang`, `Tướng Mùa Đông`, `Trung tá`, `sở chỉ huy tiền tuyến của Kampfgruppe`, `Kampfgruppe`, `Trung úy`, `Serebryakov`, `phiên bản thay thế`, `cà phê thay thế`, `khẩu phần chính phủ cấp phát`, `vốn con người`, `mặt trận phía đông`, `chứng bỏng lạnh`, `quân trang chống rét`, `bất hòa nhận thức`).

## 2. Kiểm tra nghĩa, logic và mạch trần thuật
- Đảm bảo truyền tải đầy đủ tất cả các chi tiết trong 38 đoạn từ `p000078` đến `p000115`, không lược bỏ ý hoặc tự ý thêm thắt giải thích.
- Giữ nguyên cấu trúc tương phản, điều kiện, giả định và nhân quả:
  - Ở `p000078`–`p000082`: Đối lập mùa đông ở Đế quốc (bầu trời u ám) với mùa đông của Liên bang (cuộc chiến sinh tồn chống lại Tướng Mùa Đông); chỉ ra sự phung phí tài nguyên bất chấp đang là mùa nào của hai bên tham chiến và mức ngân sách quốc gia bị chi phí quân sự nuốt trọn.
  - Ở `p000083`–`p000087`: Lập luận về sự hiếm hoi của sự tỉnh táo trong hoàn cảnh bất thường thời chiến qua ví dụ quy luật cung cầu sụp đổ; giữ đúng sắc thái giả định có điều kiện về việc viết luận án lấy bằng tiến sĩ sau khi chiến tranh kết thúc.
  - Ở `p000088`–`p000104`: Bổn phận duy trì thể trạng, giảm tiêu hao trên chiến trường và niềm vui bất ngờ khi Trung úy Serebryakov mang tới cà phê thật (khẩu phần chính phủ cấp phát nhưng chất lượng tốt khác hẳn cà phê thay thế của quân đội), đồng thời ghi nhận vai trò của người pha chế bên cạnh yếu tố hạt cà phê.
  - Ở `p000105`–`p000115`: Sự bất hòa nhận thức khi vừa uống cà phê ngon vừa viết tờ trình phản ánh chứng bỏng lạnh làm hao hụt sức chiến đấu của Kampfgruppe và xin cấp tất cùng quân trang chống rét; nhấn mạnh nhu cầu thiết yếu (ăn, mặc, ở, calo, giấc ngủ) để duy trì năng lượng và sức chiến đấu của binh lính, kết thúc bằng câu tự hỏi nửa đùa nửa thật về việc cho lính hạn chế vận động và ngủ bù như khi ở dưới tàu ngầm.

## 3. Kiểm tra đại từ và xưng hô (`DEC-P01-001`)
- **Trần thuật ngôi thứ ba về Tanya:** Dùng nhất quán đại từ `nó` (`p000082`, `p000091`, `p000092`, `p000095`, `p000096`, `p000105`).
- **Nội tâm tự quy chiếu của Tanya:** Dùng `mình` cho ngôi thứ nhất số ít (`p000086`, `p000087`, `p000100`, `p000102`); dùng `bạn` cho các câu nhận định khái quát ngôi thứ hai (`p000083`, `p000088`, `p000106`).
- **Đối thoại giữa Tanya và Trung úy Serebryakov:** Tanya xưng `tôi` – gọi `Trung úy`, dùng `chúng ta` khi nói về đơn vị (`p000107`, `p000115`); Serebryakov xưng `tôi` – gọi `Trung tá` (có đệm `ạ` lịch sự đúng mực cấp dưới với cấp trên ở `p000090`, `p000094`, `p000099`).
- **Trần thuật/nội tâm về Serebryakov:** Dùng `cô ấy` (`p000100`).

## 4. Kiểm tra nhấn mạnh / chữ nghiêng (`DEC-P01-002`)
- Đối chiếu chính xác thẻ `<html:em>` từ dữ liệu nguồn:
  - `p000079`: `*Giỏi lắm, tất cả mọi người.*`
  - `p000091`: `*Có rồi sao?*`
  - `p000096`: `*Ààà, thì ra đây chính là cảm giác xúc động dâng trào!*`
- Không tự ý thêm `*...*` vào các đoạn nội tâm hoặc cảm thán khác không có thẻ nhấn mạnh trong nguồn.
