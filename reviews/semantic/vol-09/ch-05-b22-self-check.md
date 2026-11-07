# Báo cáo tự kiểm (Self-Check): `vol-09-ch-05-b22`

- **Task ID**: `vol-09-ch-05-b22`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN09/Text/chapter020.xhtml/p000775` – `YS-LN09/Text/chapter020.xhtml/p000813` (39 đoạn)
- **File bản dịch**: `translations/vol-09/ch-05-b22.jsonl`

## 1. Kiểm tra tính đầy đủ và cấu trúc kỹ thuật
- Đã dịch đầy đủ 39/39 đoạn từ `p000775` đến `p000813`, giữ nguyên thứ tự và mã định danh (`segment_id`).
- Đã hoàn tất bước Sign-off (`vol-09-ch-05-b22-translator-signoff`) sau khi tiếp nhận `reviews/prose/vol-09/ch-05-b22-argon-review.yml`:
  - Xử lý finding `minor` tại `p000777` (`Touch: polish_optional`): chỉnh cụm `"ăn uống khá là tốn kém đấy"` thành `"ăn khỏe uống nhiều lắm đấy"` để bám sát nghĩa gốc và giữ trọn giọng bông đùa tỉnh bơ của Tanya.
  - Bảo toàn nguyên vẹn toàn bộ 38 đoạn có `Touch: preserve` và tất cả các `pending_term_recommendations` trong báo cáo review của Argon.
  - Đã cập nhật trường `"status"` của toàn bộ 39/39 dòng trong `translations/vol-09/ch-05-b22.jsonl` từ `"draft"` sang `"reviewed"`.
- Toàn bộ 39 đoạn trong XHTML nguồn không có thẻ nhấn mạnh (`<em>` hoặc `<i>`), do đó bản dịch tuân thủ `DEC-P01-002`, tuyệt đối không tự thêm dấu `*...*`.

## 2. Xưng hô, giọng điệu và mạch ngữ cảnh
- **Ngữ cảnh**: Tiếp nối trực tiếp batch `ch-05-b21` tại nhà ga vương đô Ildoa, khi Đại tá Calandro trao ngân phiếu khống từ quỹ mật của Tướng Gassman cho Trung tá Tanya von Degurechaff.
- **Độc thoại nội tâm & trần thuật (góc nhìn Tanya)**:
  - Tanya tự xưng `mình` (và `chúng ta` ở `p000775` khi nói về thể diện của đoàn mình/Đế quốc); gọi Calandro là `Calandro`, `ông ta`.
  - Ở `p000788`, lối tự nhắc tên mình ở ngôi thứ ba của Tanya được giữ nguyên (`Tanya sẽ hạ cố tỏ ra khó chịu ít nhất là trong chốc lát`).
  - Trong lời dẫn khách quan (`p000778`, `p000787`, `p000793`, `p000801`, `p000811`, `p000813`), dùng `Tanya` / `cô` và `Calandro` / `ông ta`.
- **Đối thoại giữa Tanya và Đại tá Calandro**:
  - Tanya xưng `tôi`, gọi Calandro là `ngài` / `Đại tá` / `thưa Đại tá` (hoặc `các ngài` khi chỉ phía Ildoa ở `p000785`, `p000805`). Giọng lịch thiệp bề ngoài nhưng sắc sảo, châm biếm ngầm khi thực hiện màn thăm dò phản ứng (`trinh sát chiến đấu`).
  - Calandro xưng `tôi` (hoặc `chúng tôi` khi đại diện phía Ildoa), gọi Tanya là `cô` / `Trung tá` (hoặc `các vị` khi chỉ chung đoàn của Tanya ở `p000776`, `p000781`). Giọng điềm tĩnh, khéo léo kiểu sĩ quan tham mưu kiêm ngoại giao quân sự.

## 3. Thuật ngữ và điểm lưu ý về cấp bậc
- Áp dụng nhất quán các thuật ngữ theo `canon/glossary.yml` và `work/run-state/pending-terms-index.yml`:
  - `Kampfgruppe` (`p000777`)
  - `xăng có chỉ số octan cao` (`p000781`, `p000784`, `p000797`), `nhiên liệu hàng không` (`p000798`)
  - `Đại tá Lergen` (`p000783`)
  - `Quân đoàn Viễn chinh Lục địa Phía nam` (`p000785`)
  - `trinh sát chiến đấu` (`p000804`)
  - `sĩ quan cấp tá` (`p000809`)
  - `Huy hiệu Xung kích Cánh Bạc` (`p000810`)
  - `sĩ quan tham mưu`, `Thập Nhị Hiệp Sĩ`, `trường đại học quân sự` (`p000810`)
  - `chỉ huy tiền tuyến` (`p000813`)
- **Lưu ý tại `p000812`**: Ngay sau khi gọi Tanya là trung tá ở `p000810` và nhìn thẳng vào Tanya ở `p000811`, văn bản nguồn tiếng Anh ở `p000812` ghi thiếu chữ thành cấp úy khi Calandro gọi trực tiếp Tanya. Căn cứ thực tế cấp bậc của Tanya (`Trung tá`) và cách gọi xuyên suốt cuộc trò chuyện (`p000783`, `p000786`, `p000810`), bản dịch dịch chuẩn hóa là `Trung tá` để đảm bảo tính nhất quán nội tại của nhân vật và ngữ cảnh.
