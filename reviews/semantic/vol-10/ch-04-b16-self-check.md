# Báo cáo tự kiểm dịch thuật (Self-Check)

- **Task ID:** `vol-10-ch-04-b16`
- **Model:** Gemini 4 Argon Low (`argon-low`)
- **Phạm vi:** `YS-LN10/Text/chapter022.xhtml/p000324` – `YS-LN10/Text/chapter022.xhtml/p000360` (37 đoạn)
- **Tệp dịch:** `translations/vol-10/ch-04-b16.jsonl`

## 1. Kiểm tra nghĩa, logic và mạch trần thuật
- Đã rà soát toàn bộ 37 đoạn văn bản từ `p000324` đến `p000360`, bảo toàn đầy đủ ý nghĩa, quan hệ nhân quả và sắc thái trong cuộc đối thoại giữa Tanya và Tướng Romel tại sở chỉ huy phía tây, cũng như dòng độc thoại nội tâm của Tanya về sự thiếu phối hợp giữa quân đội với ngành ngoại giao và những rủi ro chiến thuật của chiến dịch hải quân sắp tới.
- Tại `p000357`, giữ nguyên hình ảnh ẩn dụ lịch sử về những bức tường gỗ bảo vệ quốc đảo để đảm bảo độ trung thành với bề mặt biểu đạt của văn bản.
- Tại `p000359` và `p000360`, diễn đạt rõ ràng lập luận chiến thuật về tốc độ của tàu chiến so với phương tiện bay và điểm yếu khi tàu phải đứng yên trong lúc thực hiện đổ bộ.

## 2. Đại từ và xưng hô (`DEC-P01-001`)
- Trong độc thoại nội tâm và trần thuật ngôi thứ nhất của Tanya: dùng đại từ tự quy chiếu `mình` nhất quán; dùng `chúng ta` khi bao hàm phía Đế quốc / quân đội Đế quốc (`p000335`, `p000349`, `p000351`, `p000359`).
- Khi trần thuật chuyển điểm nhìn sang ngôi thứ ba ở `p000356`: dùng `cấp trên của cô` nhất quán với quy ước của Tập 10.
- Khi Tanya nhắc tới Tướng Romel trong trần thuật: dùng `Tướng Romel`, `vị tướng`, `ông ta` đồng bộ với các lô trước của Tập 10 (`ch-03-b03`, `ch-03-b04`).
- Trong đối thoại giữa Tanya và Tướng Romel:
  - Tanya xưng `tôi`, gọi `Tướng Romel` / `ngài` (`p000324`, `p000327`, `p000334`, `p000338`, `p000343`, `p000350`, `p000355`).
  - Tướng Romel gọi Tanya là `Trung tá` / `cô`, dùng `chúng ta` khi nói về phía Đế quốc (`p000325`, `p000330`, `p000333`, `p000339`, `p000342`, `p000344`, `p000353`, `p000357`).

## 3. Nhấn mạnh và định dạng (`DEC-P01-002`)
- Chỉ sử dụng dấu nhấn mạnh `*...*` tại đúng 2 đoạn có thẻ nhấn mạnh trong cấu trúc nguồn:
  - `p000347`: `*tối mật*`
  - `p000356`: `*Chính xác*`
- Tất cả 35 đoạn còn lại không có nhấn mạnh trong nguồn đều giữ văn bản phẳng.

## 4. Thuật ngữ và mục chờ xét (Pending Terms)
- Tuân thủ các cách dịch đã khóa và đề xuất trong Tập 10: `Tướng Romel`, `Kế hoạch B`, `Văn phòng Bộ Tổng tham mưu`, `chính quốc`, `Tham tán Conrad`, `Bộ Ngoại giao`, `Norden`, `Đế quốc`, `Lục quân Đế quốc`, `bản thổ Khối Thịnh vượng chung`.
- Ghi nhận các thuật ngữ/tên gọi đáng chú ý trong lô:
  - `p000346`: `Chiến dịch Gõ cửa`
  - `p000348`: `tàu chiến-tuần dương`, `tàu tuần dương hạng nhẹ`, `tàu khu trục xung kích`, `lính thủy đánh bộ`
  - `p000349`: `tàu mặt nước`
  - `p000359`: `hải đội xung kích tốc độ cao`
  - `p000360`: `tác chiến đổ bộ`

## 5. Kết quả công cụ kiểm tra và Sign-off
- Đã đối chiếu `reviews/prose/vol-10/ch-04-b16-argon-review.yml`: `findings: []` (0 serious, 0 moderate, 0 minor); toàn bộ 13 `pending_term_recommendations` và 37 `locked_choices` đều đã khớp hoàn toàn trong bản dịch.
- Đã cập nhật `status` của toàn bộ 37 dòng trong `translations/vol-10/ch-04-b16.jsonl` từ `draft` sang `reviewed`.
- `validate_translation.py`: PASS (37 units, `status: reviewed`).
