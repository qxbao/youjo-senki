# Báo cáo tự kiểm dịch thuật (Self-Check)

- **Task ID:** `vol-10-ch-04-b15`
- **Model:** Gemini 4 Argon Low (`argon-low`)
- **Phạm vi:** `YS-LN10/Text/chapter022.xhtml/p000294` – `YS-LN10/Text/chapter022.xhtml/p000323` (30 đoạn)
- **Tệp dịch:** `translations/vol-10/ch-04-b15.jsonl`

## 1. Kiểm tra nghĩa, logic và mạch trần thuật
- Đã rà soát toàn bộ 30 đoạn văn bản từ `p000294` đến `p000323`, bảo toàn đầy đủ ý nghĩa, quan hệ nhân quả, giả định và sắc thái mỉa mai trong dòng độc thoại nội tâm của nhân vật chính về tiến trình phê duyệt đề xuất tác chiến, mưu tính đào tẩu / chuyển việc sang quốc gia khác, cũng như cảnh mở đầu tại Trung tâm Chỉ huy phía Tây của Lục quân Đế quốc.
- Tại `p000318`, giữ sát hình ảnh ẩn dụ về chiếc tổ chim khi rời đi theo đúng bề mặt biểu đạt của văn bản, tránh tự ý thay bằng thành ngữ khác làm lệch hình ảnh gốc.
- Tại `p000322`, dịch đầy đủ dòng tiêu đề thời gian và địa điểm theo quy ước viết hoa đồng bộ với các lô trước của Tập 10.

## 2. Đại từ và xưng hô (`DEC-P01-001`)
- Trong độc thoại nội tâm và trần thuật ngôi thứ nhất của Tanya: dùng đại từ tự quy chiếu `mình` nhất quán; ở câu phối hợp hành động với Đại tá Lergen (`p000295`) dùng `chúng tôi`.
- Khi nhân vật tự nhìn nhận "Tanya" ở ngôi thứ ba khách quan hóa (`p000296`, `p000312`, `p000318`): dùng `Tanya` và đại từ `cô` nhất quán với các lô trước của Tập 10 (`ch-04-b14`).
- Các câu nhận định mang tính quy luật chung (`p000311`, `p000315`, `p000319`): dùng `bạn` tự nhiên, rõ nghĩa.
- Cấp bậc và danh xưng: `Đại tá Lergen` (`p000295`, `p000297`), `Trung tướng Rudersdorf` (`p000295`).

## 3. Nhấn mạnh và định dạng (`DEC-P01-002`)
- Chỉ sử dụng dấu nhấn mạnh `*...*` tại đúng các vị trí có thẻ nhấn mạnh trong cấu trúc nguồn:
  - `p000306`: `*Titanic*`
  - `p000308`: `*bằng cách nào*`
  - `p000316`: `*kẻ phản bội*`
- Tất cả các đoạn còn lại không có nhấn mạnh trong nguồn đều giữ văn bản phẳng.

## 4. Thuật ngữ và mục chờ xét (Pending Terms)
- Tuân thủ các cách dịch đã dùng nhất quán trong Tập 10: `mặt trận phía tây`, `Văn phòng Bộ Tổng tham mưu`, `Bộ Ngoại giao`, `Lục quân Đế quốc`, `Đế quốc`, `Kế hoạch B`.
- Ghi nhận các cụm từ/thuật ngữ đáng chú ý trong lô để đối chiếu:
  - `p000296`: `Kế hoạch B`
  - `p000306`: `*Titanic*`
  - `p000313`: `nhân sự có kinh nghiệm`
  - `p000317`: `gián điệp công nghiệp`
  - `p000322`: `NGÀY 14 THÁNG 8 NĂM THỐNG NHẤT 1927, TRUNG TÂM CHỈ HUY PHÍA TÂY CỦA LỤC QUÂN ĐẾ QUỐC`

## 5. Sign-off sau phản biện Argon (`vol-10-ch-04-b15-translator-signoff`)
- Báo cáo phản biện `reviews/prose/vol-10/ch-04-b15-argon-review.yml`: 0 lỗi (`serious: 0`, `moderate: 0`, `minor: 0`), `findings: []`.
- Đã đối chiếu toàn bộ `pending_term_recommendations` và `locked_choices` từ `p000294` đến `p000323`: tất cả đều đã khớp hoàn toàn trong bản dịch hiện tại.
- Đã cập nhật trường `status` của toàn bộ 30 dòng trong `translations/vol-10/ch-04-b15.jsonl` từ `draft` sang `reviewed`.

## 6. Kết quả công cụ kiểm tra
- `validate_translation.py`: PASS (30 units, `status: reviewed`).
