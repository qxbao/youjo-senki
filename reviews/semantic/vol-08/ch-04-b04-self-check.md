# Báo cáo tự kiểm (Semantic Self-Check) — `vol-08-ch-04-b04`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-04-b04`
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter014.xhtml/p000097` – `YS-LN08/Text/chapter014.xhtml/p000129` (33 đoạn)
- **Tệp đích**: `translations/vol-08/ch-04-b04.jsonl`

## 2. Kiểm tra đối chiếu quy chuẩn & thuật ngữ
- **Ngôi kể và điểm nhìn (`DEC-P01-001`)**:
  - Phân biệt rõ ràng giữa trần thuật ngôi thứ ba bám sát điểm nhìn của Tanya (`Tanya`, `cô`) ở các đoạn `p000100`, `p000102`, `p000103`, `p000110`, `p000115`, `p000116`, `p000118`, `p000119`, `p000120` và độc thoại nội tâm ngôi thứ nhất của Tanya (`mình`, `chúng tôi` / `chúng ta` / `quân ta`) ở các đoạn `p000099`, `p000101`, `p000106`, `p000110`, `p000114`, `p000117`, `p000121`, `p000124`, `p000125`, `p000126`, `p000127`, `p000128`.
- **Xưng hô trong hội thoại**:
  - Tanya nói chuyện với Trung úy Serebryakov (`p000097`–`p000098`): Tanya gọi `Trung úy Serebryakov` và dùng `chúng ta`; Serebryakov đáp `Rõ, thưa Trung tá!`, tự xưng `tôi` và gọi Tanya là `ngài`.
  - Lời lẩm bẩm và cảm thán của Tanya trước cảnh lính Liên bang xung phong (`p000103`, `p000111`, `p000115`): giữ đúng sắc thái bàng hoàng và phẫn nộ.
  - Mệnh lệnh tác chiến trên tuyến đầu và cảnh báo pháo kích (`p000122`, `p000129`): câu mệnh lệnh và hô báo ngắn gọn, dứt khoát theo văn phong quân sự.
- **Bảo toàn nhấn mạnh (`DEC-P01-002`) và chú thích**:
  - Văn bản nguồn trong toàn bộ 33 đoạn từ `p000097` đến `p000129` không có thẻ nhấn mạnh (`<em>` hoặc `<i>`), do đó bản dịch hoàn toàn không sử dụng dấu `*...*`.
  - Bảo toàn ký hiệu chú thích `³` ở cuối đoạn `p000121`.
- **Thuật ngữ và tên riêng (`pending_terms` & `glossary`)**:
  - Tuân thủ nhất quán các phương án đã dùng ở các lô trước trong tập 8: `Trung úy Serebryakov` / `Serebryakov`, `Trung úy Tospan` / `Tospan`, `mặt trận Rhine`, `Năm Thống nhất 1927`, `Liên bang`, `Quân đội Liên bang`, `Đế quốc`, `Đám Cộng sản` / `Chủ nghĩa Cộng sản`, `nguồn nhân lực`, `Being X`, `người Dacia`, `mặt trận phía đông`, `hậu cần`.
  - Đề xuất thuật ngữ mới cần lưu ý: `súng trung liên` (`p000110`, `p000123`), `tấm ván của Carneades` (`p000121`), `lý tính nhà nước` (`p000126`), `đạn pháo hạng nặng` (`p000129`).

## 3. Tự kiểm tra kỹ thuật & Sign-off
- Đủ 33/33 dòng JSONL, khớp thứ tự `segment_id` từ `p000097` đến `p000129`.
- Đã đối chiếu đầy đủ với `reviews/prose/vol-08/ch-04-b04-argon-review.yml` (0 findings; tuân thủ toàn bộ `pending_term_recommendations` và `locked_choices` từ `p000097` đến `p000129`).
- Tất cả 33/33 dòng đã được cập nhật từ `status: "draft"` sang `status: "reviewed"`, giữ nguyên `translator: "argon-low"`, khớp `source_sha256` và `glossary_version` trong handoff.
- Không chép văn bản nguồn tiếng Anh vào bản dịch hoặc báo cáo tự kiểm.
