# Tự kiểm ngữ nghĩa — vol-02-ch-06-b17

- Phạm vi: `YS-LN02/Text/part0030.xhtml/p000510`–`p000553` (44 đoạn), đối chiếu đúng gói nguồn được giao và hoàn tất sign-off theo `reviews/prose/vol-02/ch-06-b17-argon-review.yml`.
- Đã xử lý đầy đủ toàn bộ các findings trong `ch-06-b17-argon-review.yml` (B17-F01 đến B17-F05), áp dụng nhất quán các `pending_term_recommendations` và tuân thủ mọi `locked_choices`. Toàn bộ 44 dòng trong `translations/vol-02/ch-06-b17.jsonl` đã được cập nhật `status` từ `draft` sang `reviewed`.
- Điểm nhìn: tuân thủ DEC-P01-001 xuyên suốt 44 đoạn (trần thuật ngôi thứ ba dùng `Tanya` / `nó` và phản thân `mình`; nội tâm Tanya tự xưng `mình` và `chúng ta` / `ta`). Bảo toàn chính xác duy nhất 1 cụm nhấn mạnh `*yee-haw*` tại `p000516` theo DEC-P01-002.

## Findings trong Argon Review đã xử lý (Sign-off)

| Finding | Mức độ | Đoạn | Cách xử lý |
|---|---|---|---|
| B17-F01 | moderate | p000545 | Đổi thành `“Có cần bảo vệ không ạ?”` để làm rõ câu hỏi nhu cầu bảo vệ/hộ tống từ thuộc cấp trước khi Tanya giao Đại đội 2 đảm nhiệm yểm trợ trực tiếp ở `p000546`, tránh cấu trúc bị động trống không. |
| B17-F02 | moderate | p000548 | Đổi thành `“Được rồi, gọi cho họ thôi.”` để giữ chủ thể bao gồm người nói, thống nhất với nội tâm của Tanya ở `p000550` và `p000553`. |
| B17-F03 | minor | p000522 | Đổi thành `Nếu ngoài kia còn pháp sư địch sung sức thì ít nhiều gì chúng ta cũng phải dần cho chúng một trận.` để sát sắc thái tác chiến và thống nhất đại từ `chúng` với `p000523`–`p000531`. |
| B17-F04 | minor | p000528 | Đổi thành `Hay nói đúng hơn, nếu lực lượng của Tanya quét sạch được các pháp sư khỏi những khu vực có thể tấn công ở ven thành phố, nhiệm vụ của Tanya coi như phần lớn đã hoàn thành.` để tránh lặp từ nối với `p000527` và bám sát cấu trúc bổ nghĩa của câu. |
| B17-F05 | minor | p000551 | Đồng bộ thành `cấp trên` và rút gọn thành `phòng ngừa rủi ro` trong mạch liên tưởng kinh tế - hậu cần của Tanya. |

## Lựa chọn pending/non-canon đã áp dụng

| Mã | Đoạn | Đề xuất tạm | Phương án khác / ghi chú |
|---|---|---|---|
| vol02-ch06-b17-ranks-units-and-proper-nouns | p000511, p000514, p000518, p000519, p000524, p000528, p000530, p000533, p000535, p000546, p000551 | `Tanya / Thưa thiếu tá / Chỉ huy / Trung úy König / Trung úy Weiss / Rudel / Liên Xô / đại đội / Đại đội 2 / hậu cần / cấp trên` | Các lựa chọn tạm theo `pending_term_recommendations`, không tự nâng thành canon. |
| vol02-ch06-b17-legal-tactical-and-economic-terms | p000510, p000511, p000521, p000523, p000525–p000527, p000529, p000531, p000533–p000535, p000540–p000542, p000546, p000547, p000549, p000551 | `pháp luật hiện đại / hành vi không hành động / chủ thể trực tiếp của hành vi / nghĩa vụ báo cáo / đoàn tàu bọc thép / xuất kích / tác chiến chống pháp sư / kiềm chế đối phương / giao chiến tầm gần / phục kích (ổ phục kích) / chặn đánh / hủy đợt xung phong / giai đoạn truy quét / tác chiến đô thị / lệnh cảnh báo yêu cầu đầu hàng / lời kêu gọi đầu hàng / cảnh báo đầu hàng / pháo binh / đơn vị máy bay ném bom / đợt oanh kích / yểm trợ trực tiếp / chủ nghĩa khắc kỷ / sa thải / chủ nghĩa tư bản / phòng ngừa rủi ro / cắt giảm chi phí` | Giữ nhất quán hệ thuật ngữ pháp lý, quân sự và kinh tế trong toàn batch. |
| vol02-ch06-b17-pronouns-pov-and-single-emphasis | p000510–p000553 | Tuân thủ DEC-P01-001 về đại từ trần thuật (`Tanya` / `nó`), nội tâm (`mình` / `chúng ta` / `ta`), thoại vô tuyến (`Thưa thiếu tá` - `tôi`, `Chỉ huy`, tiểu từ `ạ`) và DEC-P01-002 (`*yee-haw*` tại `p000516`). | Không suy diễn thêm quan hệ hay cấp hàm ngoài phạm vi đã khóa. |

## Rủi ro còn lại

- Không còn lỗi ngữ nghĩa hay lệch điểm nhìn. Các thuật ngữ và cách xưng hô trong bảng trên vẫn giữ trạng thái `pending` để coordinator quản lý trong sổ chung.
