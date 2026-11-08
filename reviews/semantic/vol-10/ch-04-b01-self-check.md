# Báo cáo tự kiểm (Self-Check): `vol-10-ch-04-b01`

## 1. Thông tin chung
- **Task ID**: `vol-10-ch-04-b01`
- **Tác tử**: `argon-low` (Translator)
- **Phạm vi đoạn**: `YS-LN10/Text/chapter020.xhtml/p000001` đến `YS-LN10/Text/chapter020.xhtml/p000023` (23 đoạn)
- **Phiên bản glossary**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 2. Kiểm tra bảo toàn nghĩa, số liệu, ngày tháng và cấp bậc
- **Ngày tháng & địa điểm mở đầu (`p000001`)**: Đã dịch đầy đủ ngày 14 tháng 8 Năm Thống nhất 1927 và địa danh Đế đô.
- **Mạch sự kiện và lập luận (`p000002`–`p000007`)**: Bảo toàn chính xác sự đối chiếu giữa kiếp làm công ăn lương hiện đại của nhân vật chính và vị thế hiện tại của Tanya tại Văn phòng Bộ Tổng tham mưu: đổi âu phục lấy quân phục, đổi đề xuất dự án lấy kế hoạch tác chiến, đổi cà vạt lấy huân chương và huy hiệu; vẫn ở thế yếu phải cúi đầu xin duyệt dự án mà cả bản thân lẫn cấp trên đều không muốn dính vào do thị trường ngừng vận hành bình thường.
- **Mạch sự kiện (`p000008`–`p000013`)**: Bảo toàn chính xác việc Tanya đến gõ cửa phòng chỉ huy Kampfgruppe là Đại tá Lergen để xin chữ ký vào bản báo cáo, nhưng chưa kịp nói hết câu thì một toán nhân viên văn thư ùa ra, lấy bản báo cáo và kéo cả Đại tá Lergen lẫn Tanya lên xe quân sự chở thẳng đến tòa nhà bê tông của Bộ Ngoại giao tại thủ đô.
- **Mạch độc thoại phê phán (`p000014`–`p000023`)**: Bảo toàn đầy đủ và đúng mức độ gay gắt trong suy nghĩ của Tanya về sự ăn không ngồi rồi, tắc trách ngang tầm tội ác chiến tranh của Bộ Ngoại giao; giả định về việc sa thải/đưa lên thớt nếu nắm bộ phận nhân sự; sự tiếc nuối khi Đế quốc thiếu vắng một nhân vật ngoại giao tầm cỡ như Bismarck khiến đất nước sa lầy vào cuộc chiến không lối thoát và cầm chắc thất bại ngay từ đầu.

## 3. Kiểm tra đại từ, xưng hô và giọng văn (`DEC-P01-001`)
- **Độc thoại nội tâm và tự sự ngôi thứ nhất của Tanya (`p000002`–`p000008`, `p000010`, `p000012`, `p000015`–`p000018`, `p000020`, `p000022`, `p000023`)**: Sử dụng nhất quán đại từ `mình` cho ngôi thứ nhất của Tanya; giữ nguyên tên gọi `Tanya` ở các chỗ nhân vật tự nhìn nhận bản thân từ góc nhìn khách quan (`p000002`, `p000003`).
- **Tự sự số nhiều bao hàm Lergen hoặc đất nước (`p000011`, `p000017`, `p000021`)**: Dùng `chúng tôi` khi đi cùng Đại tá Lergen (`p000011`) và `chúng ta` khi nói về đất nước/tình cảnh chung trong lập luận nội tâm (`p000017`, `p000021`).
- **Lời thoại trực tiếp (`p000009`)**: Dùng `Tôi` trang trọng theo điều lệnh quân đội khi tự giới thiệu cấp bậc (`Trung tá Degurechaff`) trước cửa phòng Đại tá Lergen.
- **Cách gọi nhân vật khác**:
  - Lergen (`p000008`, `p000010`): `Đại tá Lergen`, đại từ `ông`.

## 4. Kiểm tra định dạng nhấn mạnh (`DEC-P01-002`)
- Đã kiểm tra toàn bộ trường `xhtml` của 23 đoạn:
  - `p000010`: Có 1 cụm in nghiêng (`<html:em>`) cho từ chỉ cấp bậc bị ngắt quãng -> đã bọc `*đại tá*` đúng vị trí (bỏ qua thẻ neo trang `<html:a id="page-150" />`).
  - `p000016`: Có 1 cụm in nghiêng (`<html:em>`) cho tiếng hét nội tâm -> đã bọc `*Lo mà làm cái việc chết tiệt của các người đi!*` đúng vị trí.
  - Các đoạn còn lại không có thẻ nhấn mạnh -> hoàn toàn không tự ý thêm `*...*` hay `**...**`.

## 5. Thuật ngữ và đề xuất (Pending Terms)
- Đã đối chiếu và áp dụng nhất quán với canon cùng sổ pending (`work/run-state/pending-terms-index.yml`):
  - `ĐẾ ĐÔ` / `thủ đô` (`p000001`, `p000013`)
  - `Văn phòng Bộ Tổng tham mưu` (`p000003`, `p000011`)
  - `Kampfgruppe` (`p000008`)
  - `Đại tá Lergen` (`p000008`, `p000010`)
  - `Trung tá Degurechaff` (`p000009`)
  - `Bộ Ngoại giao` (`p000013`, `p000017`)
  - `Đế quốc` (`p000020`, `p000023`)
  - **Bismarck** (`p000020`, `p000023` - đề xuất giữ nguyên danh xưng lịch sử làm ẩn dụ)
  - `bộ phận nhân sự` (`p000018`)

## 6. Sign-off sau phản biện Argon (`vol-10-ch-04-b01-translator-signoff`)
- **Xử lý findings**:
  - `p000015` (minor): Tiếp nhận khuyến nghị của Argon, chỉnh cụm "mình không khỏi bức xúc muốn hỏi" thành "mình thấy buộc phải hỏi" để giữ đúng nhịp tăng tiến cảm xúc từ `p000015` sang `p000016` và tránh giải thích sớm sắc thái cảm xúc.
  - `p000022` (minor): Tiếp nhận khuyến nghị của Argon, chỉnh cụm "Trong cõi riêng tư bất khả xâm phạm của tâm trí" thành "Trong cõi riêng tư thiêng liêng của tâm trí" để giữ sắc thái ẩn dụ tôn giáo mỉa mai của Tanya.
- **Pending terms & Locked choices**: Đã đối chiếu và bảo đảm tuân thủ đầy đủ toàn bộ `pending_term_recommendations` cùng `locked_choices` từ `p000001` đến `p000023` trong báo cáo `reviews/prose/vol-10/ch-04-b01-argon-review.yml`.
- **Trạng thái dòng (`status`)**: Đã cập nhật toàn bộ 23 dòng trong `translations/vol-10/ch-04-b01.jsonl` từ `draft` sang `reviewed`.
