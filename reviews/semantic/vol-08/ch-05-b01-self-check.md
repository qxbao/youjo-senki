# Báo cáo tự kiểm (Semantic Self-Check) — `vol-08-ch-05-b01`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-05-b01`
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter018.xhtml/p000001` – `YS-LN08/Text/chapter018.xhtml/p000027` (27 đoạn)
- **Tệp đích**: `translations/vol-08/ch-05-b01.jsonl`

## 2. Kiểm tra đối chiếu quy chuẩn & thuật ngữ
- **Ngôi kể và điểm nhìn (`DEC-P01-001`)**:
  - Trần thuật ngôi thứ ba khách quan xen lẫn điểm nhìn chiến trường ở các đoạn `p000002`–`p000017`, `p000021`, `p000023`, `p000026`–`p000027`: Chỉ huy Cramm và Trung tướng von Zettour được quy chiếu là `ông`, Trung úy Grantz được quy chiếu là `anh`.
  - Độc thoại nội tâm trực tiếp của Trung tướng von Zettour ở đoạn `p000022`: tự xưng `mình`, gọi Tanya là `Trung tá von Degurechaff` / `cô ta`.
- **Xưng hô trong hội thoại**:
  - Mệnh lệnh của Chỉ huy Cramm trước toàn sư đoàn (`p000011`, `p000014`–`p000016`): tự xưng `tôi`, gọi binh sĩ dưới quyền là `các anh`.
  - Đối thoại giữa Trung tướng von Zettour và Trung úy Grantz (`p000018`–`p000021`, `p000023`–`p000025`): Zettour tự xưng `tôi` / `chúng ta`, gọi Grantz là `Trung úy Grantz` / `Trung úy` / `anh`; Grantz tự xưng `tôi`, gọi Zettour là `Tướng quân` (`Thưa Tướng quân`, `thưa Tướng quân`) và `ngài`, giữ đúng sắc thái lễ phép nhưng thẳng thắn của sĩ quan dưới quyền Tanya.
- **Bảo toàn nhấn mạnh (`DEC-P01-002`)**:
  - Đoạn `p000009`: bảo toàn từ nhấn mạnh bằng `*quân địch*`.
  - Đoạn `p000015`: bảo toàn hai cụm thông điệp qua cử chỉ/ánh mắt bằng `*Theo tôi!*` và `*Ông già nhà mình cũng y hệt thế!*`.
  - Đoạn `p000021`: bảo toàn câu ý nghĩ ngầm qua ánh mắt của Grantz bằng `*Chẳng phải chính mong muốn ra tận tiền tuyến của ngài đã dẫn đến tình cảnh này sao, thưa Tướng quân?*`.
  - Đoạn `p000022`: bảo toàn toàn bộ đoạn độc thoại nội tâm của Zettour trong cặp dấu `*...*`.
  - Tất cả các đoạn còn lại không có nhấn mạnh trong nguồn và không dùng dấu `*...*`.
- **Thuật ngữ và tên riêng (`pending_terms` & `glossary`)**:
  - Tuân thủ nhất quán các thuật ngữ đã thiết lập trong `canon/` và `pending-terms-index.yml`: `NĂM THỐNG NHẤT 1927`, `PHÒNG TUYẾN PHÍA ĐÔNG`, `ĐƠN VỊ GIẢI CỨU`, `sư đoàn thiết giáp của Lục quân Đế quốc`, `Soldim 528`, `mặt trận phía đông`, `Quân đội Liên bang`, `Chỉ huy Cramm`, `Trung tướng von Zettour` / `Zettour`, `Trung úy Grantz` / `Grantz`, `Trung tá von Degurechaff`, `thanh tra viên`, `tiền tuyến`, `hậu phương`.
  - Đề xuất thuật ngữ / cách diễn đạt tạm trong lô: `MŨI TIÊN PHONG ĐI ĐẦU` (`p000001`), `tư lệnh của cả sư đoàn` (`p000012`), `công tác đào tạo ở hậu phương` (`p000022`).

## 3. Tự kiểm tra kỹ thuật & Sign-off
- Đủ 27/27 dòng JSONL, khớp thứ tự `segment_id` từ `p000001` đến `p000027`.
- Đã đối chiếu với `reviews/prose/vol-08/ch-05-b01-argon-review.yml`: `findings: []` (0 lỗi serious/moderate/minor), tuân thủ đầy đủ mọi `locked_choices` và `pending_term_recommendations` từ `p000001` đến `p000027`.
- Đã cập nhật trường `status` của toàn bộ 27 dòng từ `"draft"` sang `"reviewed"`, `translator` là `"argon-low"`, khớp `source_sha256` và `glossary_version` trong handoff.
- Không chép văn bản nguồn tiếng Anh vào bản dịch hoặc báo cáo tự kiểm.
