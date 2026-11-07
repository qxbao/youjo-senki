# Báo cáo tự kiểm dịch thuật (Semantic Self-Check) — `vol-09-ch-04-b10`

## 1. Thông tin chung
- **Task ID:** `vol-09-ch-04-b10`
- **Tập / Chương:** `vol-09`, Chương 4 (`OEBPS/Text/chapter016.xhtml`)
- **Phạm vi đoạn:** `YS-LN09/Text/chapter016.xhtml/p000171` đến `YS-LN09/Text/chapter016.xhtml/p000204` (34 đoạn)
- **Tác tử thực hiện:** `argon-low`
- **Glossary version:** `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`
- **Source SHA256:** `6e752589ca5a3bd4200a77b72f89a3f7a99ab03d9c14717b32151e8e5f6cb549`

## 2. Kiểm tra tính đầy đủ và bảo toàn cấu trúc
- **Số lượng đơn vị dịch:** Đủ 34/34 dòng JSONL, khớp chính xác thứ tự và `segment_id` từ `p000171` đến `p000204`.
- **Trạng thái dòng (`status`):** Toàn bộ 34 dòng đều đã được cập nhật từ `"draft"` sang `"reviewed"` sau khi thực hiện Sign-off theo `ch-04-b10-argon-review.yml` (0 findings, tuân thủ đầy đủ `locked_choices` và `pending_term_recommendations`).
- **Bảo toàn nhấn mạnh (`DEC-P01-002`):**
  - Chỉ sử dụng dấu `*...*` ở đúng 2 đoạn có thẻ nhấn mạnh trong XHTML gốc:
    - `YS-LN09/Text/chapter016.xhtml/p000187`: `*ghê gớm*`
    - `YS-LN09/Text/chapter016.xhtml/p000203`: `*Tất nhiên rồi*`
  - Không tự ý thêm in nghiêng hoặc in đậm ở bất kỳ đoạn nào khác.

## 3. Nhất quán thuật ngữ, danh xưng và giọng văn
- **Xưng hô và ngôi kể:**
  - Độc thoại nội tâm của Tanya: tự xưng `mình` / `chúng mình`, giữ sự chuyển đổi mượt mà giữa tự sự ngôi thứ ba (`Tanya`, `cô`) và độc thoại ngôi thứ nhất theo đúng phong cách nguyên tác và `canon/style-guide.md`.
  - Đối thoại giữa Trung tá Tanya von Degurechaff và Thiếu tá Otto von Elm (Thuyền trưởng tàu ngầm U-091):
    - Tanya xưng `tôi` / `chúng tôi`, gọi Elm là `Thuyền trưởng` / `anh`.
    - Elm xưng `tôi` / `chúng tôi`, gọi Tanya là `Trung tá` (`thưa Trung tá`), gọi người đồng khóa Barchet là `cậu ấy`.
    - Tự sự ngôi thứ ba gọi Elm là `vị thuyền trưởng`, `Elm`, `anh ta` (nhất quán với cấp bậc Thiếu tá của Elm thấp hơn cấp Trung tá của Tanya và đồng bộ với các batch lân cận).
- **Thuật ngữ đã đối chiếu với `canon/` và `work/run-state/pending-terms-index.yml`:**
  - `Tiểu đoàn Pháp sư Trên không số 203` (`p000176`)
  - `Kampfgruppe Lergen` (`p000176`)
  - `Trung tá Tanya von Degurechaff` (`p000176`)
  - `Thiếu tá Otto von Elm` / `tàu U-091` (`p000177`)
  - `Thiếu tá Barchet` (`p000183`, `p000190`)
  - `hải đội tàu ngầm` (`p000183`)
  - `tàu mẹ` / `cụm tác chiến tàu sân bay` / `tàu sân bay` / `máy bay trên tàu sân bay` (`p000184`)
  - `tùng thiết trên xe tăng` / `mặt trận phía đông` (`p000187`, `p000188`)
  - `V-2` / `vũ khí dòng V` (`p000191`, `p000192`)

## 4. Điểm cần lưu ý / Thuật ngữ đề xuất
- Không phát sinh lỗi dịch sót, lệch nghĩa hay mâu thuẫn xưng hô. Các cách dịch cho tên riêng và thuật ngữ quân sự đều bám sát hệ quy chiếu hiện hành của Tập 9.
