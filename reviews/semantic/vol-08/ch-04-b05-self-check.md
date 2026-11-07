# Báo cáo tự kiểm (Semantic Self-Check) — `vol-08-ch-04-b05`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-04-b05`
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter014.xhtml/p000130` – `YS-LN08/Text/chapter014.xhtml/p000168` (39 đoạn)
- **Tệp đích**: `translations/vol-08/ch-04-b05.jsonl`

## 2. Kiểm tra đối chiếu quy chuẩn & thuật ngữ
- **Ngôi kể và điểm nhìn (`DEC-P01-001`)**:
  - Phân biệt rõ ràng giữa trần thuật ngôi thứ ba bám sát điểm nhìn của Tanya (`Tanya`, `cô`) ở các đoạn `p000130`, `p000137`, `p000140`, `p000141`, `p000143`, `p000147`, `p000148`, `p000149`, `p000151`, `p000152`, `p000161`, `p000162` và độc thoại nội tâm ngôi thứ nhất của Tanya (`mình`, `chúng tôi` / `chúng ta`) ở các đoạn `p000131`, `p000132`, `p000134`, `p000137`, `p000142`, `p000147`, `p000149`, `p000153`, `p000154`, `p000158`, `p000161`, `p000166`, `p000167`, `p000168`.
- **Xưng hô trong hội thoại**:
  - Giữa Tanya và Trung úy Serebryakov (`p000135`–`p000151`): Serebryakov gọi Tanya là `Trung tá` (`thưa Trung tá`), tự xưng `tôi`, gọi Đại úy Meybert là `anh ấy`; Tanya tự xưng `tôi`, dùng `chúng ta` khi nói chung đơn vị, giọng mệnh lệnh dứt khoát.
  - Giữa Tanya và Thiếu tá Weiss qua điện thoại (`p000155`–`p000165`): Weiss gọi Tanya là `Trung tá` (`thưa Trung tá`), tự xưng `tôi` / `chúng tôi`; Tanya gọi Weiss là `Thiếu tá` / `Thiếu tá Weiss` và `anh` / `các anh`, tự xưng `tôi`.
- **Bảo toàn nhấn mạnh (`DEC-P01-002`)**:
  - Đoạn `p000142` có một cụm nhấn mạnh trong văn bản nguồn được bảo toàn chính xác bằng dấu `*...*` (`*Thổi bay lũ pháo thủ địch chướng mắt đó đi*`).
  - Các đoạn còn lại từ `p000130` đến `p000168` không có thẻ nhấn mạnh trong nguồn và không dùng dấu `*...*`.
- **Thuật ngữ và tên riêng (`pending_terms` & `glossary`)**:
  - Tuân thủ nhất quán các phương án đã dùng ở các lô trước trong tập 8: `sĩ quan phụ tá`, `Liên bang`, `đám Cộng sản`, `tín hiệu`, `Serebryakov`, `Đại úy Meybert` / `Meybert`, `Being X`, `Thiếu tá Weiss` / `Weiss`, `bản quốc`, `đại đội pháp sư trên không`, `thao trường`, `Tospan`.
  - Đề xuất thuật ngữ mới cần lưu ý: `phản pháo` (`p000137`), `điện thoại dã chiến` (`p000137`), `logic tổ chức` (`p000149`), `mật độ binh lực` (`p000164`), `thái độ duy ý chí` (`p000166`), `quản lý cấp trung` (`p000168`).

## 3. Tự kiểm tra kỹ thuật & Sign-off
- Đủ 39/39 dòng JSONL, khớp thứ tự `segment_id` từ `p000130` đến `p000168`.
- Đã rà soát báo cáo `reviews/prose/vol-08/ch-04-b05-argon-review.yml`: không có lỗi (`serious: 0`, `moderate: 0`, `minor: 0`, `findings: []`); toàn bộ `pending_term_recommendations` và `locked_choices` cho cả 39 đoạn đều được tuân thủ đầy đủ.
- Đã cập nhật trường `status` của toàn bộ 39 dòng trong `translations/vol-08/ch-04-b05.jsonl` từ `"draft"` sang `"reviewed"` cho bước `vol-08-ch-04-b05-translator-signoff`; `translator` là `"argon-low"`, khớp `source_sha256` và `glossary_version` trong handoff.
- Không chép văn bản nguồn tiếng Anh vào bản dịch hoặc báo cáo tự kiểm.
