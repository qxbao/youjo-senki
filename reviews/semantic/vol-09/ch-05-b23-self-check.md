# Báo cáo tự kiểm (Self-Check): `vol-09-ch-05-b23`

- **Task ID**: `vol-09-ch-05-b23`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN09/Text/chapter020.xhtml/p000814` – `YS-LN09/Text/chapter020.xhtml/p000848` (35 đoạn)
- **File bản dịch**: `translations/vol-09/ch-05-b23.jsonl`

## 1. Kiểm tra tính đầy đủ và cấu trúc kỹ thuật
- Đã dịch đầy đủ 35/35 đoạn từ `p000814` đến `p000848`, giữ nguyên thứ tự và mã định danh (`segment_id`).
- Trường `"status"` của tất cả các dòng đều đã được cập nhật sang `"reviewed"` sau khi xử lý báo cáo Argon review.
- Toàn bộ 35 đoạn trong XHTML nguồn không có thẻ nhấn mạnh (`<em>` hoặc `<i>`), do đó bản dịch tuân thủ `DEC-P01-002`, tuyệt đối không tự thêm dấu `*...*`.
- **Xử lý Argon Review (`vol-09-ch-05-b23-argon-review.yml`)**:
  - Đã xử lý finding `minor` tại `p000839` (`Touch: polish_optional`): tinh chỉnh cụm lặp từ thành `"cập bến thiện chí tại cảng của các ngài"`.
  - Giữ nguyên toàn bộ 34 đoạn có `Touch: preserve` và bảo đảm tuân thủ đầy đủ các `pending_term_recommendations`.

## 2. Xưng hô, giọng điệu và mạch ngữ cảnh
- **Ngữ cảnh**: Tiếp nối trực tiếp `vol-09-ch-05-b22` tại nhà ga vương đô Ildoa khi Trung tá Tanya von Degurechaff và Đại tá Calandro đấu khẩu ngoại giao ngầm trước khi Tanya nhận phong bì thị thực cùng tấm séc chi phí (`p000814`–`p000844`), sau đó chuyển cảnh sang ngày 21 tháng 7 năm Thống nhất 1927 trên khoang hạng nhất chuyến tàu quốc tế rời Ildoa (`p000845`–`p000848`).
- **Độc thoại nội tâm & trần thuật (góc nhìn Tanya)**:
  - Khi tự quy chiếu trong nội tâm (`p000815`, `p000842`, `p000846`), Tanya xưng `mình` (hoặc `chúng ta` ở `p000842` khi đại diện cho phía Đế quốc).
  - Trong lời dẫn khách quan hoặc góc nhìn bán khách quan (`p000816`, `p000823`, `p000824`, `p000825`, `p000828`, `p000829`, `p000830`, `p000833`, `p000836`, `p000841`, `p000843`, `p000847`), dùng `Tanya` / `cô` và `Calandro` / `ông ta`.
- **Đối thoại giữa Tanya và Đại tá Calandro**:
  - Tanya xưng `tôi` (hoặc `chúng tôi` khi nói thay toàn đoàn ở `p000835`, `p000844`; `chúng ta` khi nhắc kỷ niệm gặp gỡ ở `p000815`), gọi Calandro là `ngài` / `thưa Đại tá` (và `các ngài` khi chỉ phía Ildoa ở `p000839`). Giọng lịch thiệp bề ngoài nhưng sắc bén, châm biếm ngầm rồi khéo léo xuống thang đúng mực ngoại giao.
  - Calandro xưng `tôi` (hoặc `chúng tôi` khi đại diện phía Ildoa ở `p000838`, `p000840`; `chúng ta` ở `p000816`), gọi Tanya là `cô` / `thưa Trung tá`. Giọng điềm tĩnh, khéo léo, giữ vững lập trường nước trung lập kiêm đồng minh trên danh nghĩa.

## 3. Thuật ngữ và lựa chọn dịch thuật
- Áp dụng nhất quán các thuật ngữ đã có trong `canon/glossary.yml` và `work/run-state/pending-terms-index.yml`:
  - `Đại tá Calandro` / `Calandro` / `thưa Đại tá` (`p000814`, `p000816`, `p000824`, `p000828`, `p000830`, `p000833`, `p000837`, `p000842`, `p000844`)
  - `quân đội Đế quốc` / `Đế quốc` (`p000814`, `p000817`, `p000820`, `p000826`, `p000848`)
  - `mặt trận phía đông` (`p000815`)
  - `sĩ quan cấp tá` (`p000815`, `p000821`, `p000822`)
  - `sĩ quan tham mưu`, `trường đại học quân sự` (`p000817`)
  - `Bộ Tổng tham mưu`, `Kampfgruppe Lergen` (`p000819`)
  - `thưa Trung tá` (Calandro gọi Trung tá Tanya von Degurechaff ở `p000831`)
  - `tính hợp lý` (`p000841`)
  - `NGÀY 21 THÁNG 7 NĂM THỐNG NHẤT 1927, LÃNH THỔ ILDOA, KHOANG HẠNG NHẤT TRÊN CHUYẾN TÀU QUỐC TẾ` (`p000845`)
- Các thuật ngữ đề xuất mới (pending terms):
  - `alpine expert` / `alpine troops` -> `chuyên gia tác chiến sơn cước` / `bộ đội sơn cước` (`p000815`, `p000822`)
  - `military observer` -> `quan sát viên quân sự` (`p000819`)
  - `good neighbor policy` -> `chính sách láng giềng thân thiện` (`p000840`)
  - `weather vane nation` / `weather vane diplomacy` -> `quốc gia gió chiều nào xoay chiều ấy` / `chính sách ngoại giao gió chiều nào xoay chiều ấy` (`p000841`, `p000847`, đồng bộ với cách dịch ẩn dụ cùng gốc tại `p000788`, `p000803` ở `ch-05-b22`)
