# Báo cáo tự kiểm (Self-Check): `vol-10-ch-04-b14`

- **Task ID**: `vol-10-ch-04-b14`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter022.xhtml/p000259` .. `YS-LN10/Text/chapter022.xhtml/p000293` (35 đoạn)
- **Tệp bản dịch**: `translations/vol-10/ch-04-b14.jsonl`
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra tính đầy đủ và định dạng
- Đã dịch đầy đủ 35/35 đoạn từ `p000259` đến `p000293`, khớp hoàn toàn `id` và `source_sha256` với tệp nguồn.
- Không tách dòng, không gộp dòng, không bỏ sót bất kỳ câu hay mệnh đề nào.
- Trường `status` của toàn bộ 35 dòng được cập nhật sang `"reviewed"` sau khi hoàn tất sign-off với Argon Review (`0 serious, 0 moderate, 0 minor`, tuân thủ toàn bộ `locked_choices` và `pending_term_recommendations`).
- Các thẻ đánh dấu số trang trong XHTML (`page-178` ở `p000263`, `page-179` ở `p000280`, `page-180` ở `p000292`) đã được lược bỏ sạch sẽ trong văn bản tiếng Việt.
- Kiểm tra quy tắc in nghiêng (`DEC-P01-002`):
  - Đoạn `p000277` có thẻ nhấn mạnh ở mệnh đề kết câu (`*Con tàu này đã đang chìm rồi*`) -> đã bảo toàn bằng dấu `*...*`.
  - Đoạn `p000293` có thẻ nhấn mạnh ở tên kế hoạch (`*Kế hoạch B*`) -> đã bảo toàn bằng dấu `*...*` (nhất quán với `ch-03-b02` `p000042` và `p000045`).
  - Toàn bộ 33 đoạn còn lại không có thẻ nhấn mạnh trong XHTML -> không tự ý thêm dấu `*...*`.

## 2. Kiểm tra giọng văn và đại từ xưng hô
- **Độc thoại nội tâm và trần thuật của Tanya** (`p000259`, `p000263`–`p000265`, `p000267`, `p000269`, `p000272`–`p000293`):
  - Tự xưng `mình` (hoặc `chúng ta` khi gộp chung với Đế quốc/quân đội ở `p000273`, `p000275`; `chúng tôi` khi đi cùng Đại tá Lergen ở `p000290`).
  - Các đoạn đan xen góc nhìn ngôi thứ nhất và ngôi thứ ba (`p000272`, `p000278`, `p000279`, `p000282`, `p000291`): giữ nguyên cách gọi `Tanya` / `cô` kết hợp với `mình` theo đúng phong cách đặc trưng của tác phẩm và nhất quán với các batch trước.
  - Gọi Tham tán Conrad là `Tham tán Conrad`, `nhà ngoại giao ấy`, `ông ta`; gọi Đại tá Lergen là `Đại tá Lergen`, `vị đại tá`, `ông ấy`; gọi Tướng Romel là `Tướng Romel`.
- **Thoại giữa Tanya, Tham tán Conrad và Đại tá Lergen** (`p000260`–`p000262`, `p000266`, `p000268`, `p000270`, `p000271`):
  - Tanya xưng `tôi`, giữ giọng điềm tĩnh, lý tính và thực dụng.
  - Tham tán Conrad xưng `tôi` (và `chúng ta` khi nói về lợi ích chung của Đế quốc), gọi Tanya là `thưa Trung tá` (`p000270`).

## 3. Thuật ngữ Canon & Pending Terms
- Tuân thủ nghiêm ngặt `canon/glossary.yml`, `canon/characters.yml` và các đề xuất trong `work/run-state/pending-terms-index.yml`:
  - `Empire` -> `Đế quốc`
  - `General Staff Office` -> `Văn phòng Bộ Tổng tham mưu` (`p000288`)
  - `Colonel Lergen` -> `Đại tá Lergen`
  - `Counselor Conrad` -> `Tham tán Conrad`
  - `General Romel` -> `Tướng Romel`
  - `Lieutenant Colonel` -> `Trung tá` (`p000270`)
  - `western front` -> `mặt trận phía tây` (`p000287`)
  - `quartermasters` -> `các sĩ quan quân nhu` (`p000289`)
  - `*Plan B*` -> `*Kế hoạch B*` (`p000293`, nhất quán với `ch-03-b02`)
- Các cách diễn đạt theo ngữ cảnh:
  - `rapprochement` (`p000266`) -> dịch thoát nghĩa sát ngữ cảnh ngoại giao là `việc nối lại quan hệ hòa hảo`.
  - Câu trích dẫn kinh điển của Clausewitz ở `p000271` -> `chiến tranh cũng chỉ là sự nối dài của chính trị`.
  - Các ẩn dụ quản trị/doanh nghiệp của Tanya (`middle managers`, `upper management`, `recruiters`, `overtime`) được chuyển ngữ tự nhiên, giữ đúng chất dân văn phòng thực dụng của nhân vật.
