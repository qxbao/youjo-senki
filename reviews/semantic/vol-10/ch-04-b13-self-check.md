# Báo cáo tự kiểm (Self-Check) — `vol-10-ch-04-b13`

- **Task ID**: `vol-10-ch-04-b13`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter022.xhtml/p000222` đến `YS-LN10/Text/chapter022.xhtml/p000258` (37 đoạn)
- **Tệp bản dịch**: `translations/vol-10/ch-04-b13.jsonl`

## 1. Kiểm tra tính đầy đủ và định dạng
- Đã dịch đầy đủ 37/37 đoạn theo đúng thứ tự trong gói nguồn.
- Giữ nguyên `id` và `source_sha256` của từng đoạn.
- Tất cả các dòng đều có `status: "reviewed"`, `translator: "argon-low"`, và `glossary_version` khớp với `handoffs/vol-10/ch-04-b13.yml`.
- Không làm rò rỉ thẻ HTML/XHTML (đã xử lý sạch các neo chuyển trang ở `p000231` và `p000245`).
- Kiểm tra quy ước nhấn mạnh (`DEC-P01-002`): Trong toàn bộ 37 đoạn nguồn của batch này không có thẻ nghiêng ngữ nghĩa nào, do đó bản dịch hoàn toàn không sử dụng dấu `*...*`.

## 2. Xưng hô và giọng điệu nhân vật (`DEC-P01-001`)
- **Độc thoại nội tâm và trần thuật của Tanya** (`p000222`, `p000224`–`p000225`, `p000228`, `p000230`, `p000235`–`p000237`, `p000241`, `p000245`–`p000246`, `p000250`, `p000254`, `p000256`–`p000258`):
  - Ngôi thứ nhất số ít tự xưng `mình`; khi nói gộp cả phía quân đội/Đế quốc dùng `chúng ta` (`p000222`, `p000246`).
  - Các đoạn trần thuật đan xen góc nhìn ngôi thứ ba nhắc đến Tanya (`p000236`, `p000241`, `p000250`, `p000254`, `p000256`) dùng `Tanya` / `cô`, nhất quán với các batch trước trong chương 4.
  - Giọng văn duy lý, thực dụng, mang màu sắc quản trị doanh nghiệp và tham mưu quân sự.
- **Đối thoại giữa Tanya và Tham tán Conrad**:
  - Tanya xưng `tôi` (hoặc `chúng tôi` khi đại diện phía quân đội ở `p000226`, `chúng ta` khi nói chung về vận mệnh Đế quốc ở `p000236`, `p000238`, `p000243`), gọi Conrad là `ông` / `thưa Tham tán`.
  - Tham tán Conrad xưng `tôi` (hoặc `chúng ta` khi nói về Đế quốc/ngành ngoại giao ở `p000234`, `p000239`), gọi Tanya là `cô` / `thưa Trung tá`.
  - Khi Conrad quay sang nói với Đại tá Lergen (`p000255`): gọi `Đại tá Lergen`, xưng `tôi`, gọi Tanya là `vị trung tá này`.

## 3. Thuật ngữ, danh xưng và tính nhất quán
- Tuân thủ nghiêm ngặt `canon/glossary.yml` và các phương án đã thiết lập trong `work/run-state/pending-terms-index.yml`:
  - `Đế quốc`, `Liên bang`, `Bộ Tổng tham mưu`, `sĩ quan Bộ Tổng tham mưu`, `Bộ Ngoại giao`, `tiểu đoàn`, `thuật thức ma pháp`.
  - `Tướng Zettour`, `vị đại tướng tương lai này` (`p000228`), `Đại tá Lergen`, `Tham tán Conrad` / `vị tham tán`, `Trung tá` / `trung tá`.
  - `lối tác chiến cơ động` (`p000227`), `ở miền đông` (`p000227`, `p000234`), `những kẻ cầm trịch` (`p000222`).
  - Giữ nguyên danh xưng `Reich` (`p000244`, `p000245`, `p000247`, `p000251`) để bảo toàn sắc thái biểu tượng chính trị - tư tưởng mà Tham tán Conrad và Tanya đang phân tích tách biệt với từ chỉ `Đế quốc` thông thường (đặc biệt trong đoạn `p000245` khi cả hai khái niệm cùng xuất hiện).

## 4. Sign-off sau phản biện Argon (`vol-10-ch-04-b13-translator-signoff`)
- Tiếp nhận finding `minor` tại `p000252` trong `reviews/prose/vol-10/ch-04-b13-argon-review.yml`: chỉnh câu đầu lời đáp của Tham tán Conrad thành `"Nghe chính cô nói ra câu đó thì thật thấm thía đấy."` để làm rõ sắc thái đồng cảm chua xót khi nghe nhận định sắc bén phát ra từ chính một thiếu nữ trạc tuổi.
- Kiểm tra và giữ nguyên toàn bộ 13 mục `pending_term_recommendations` và 37 mục `locked_choices` trong báo cáo review.
- Cập nhật `status` của toàn bộ 37 dòng trong `translations/vol-10/ch-04-b13.jsonl` từ `draft` sang `reviewed`.
