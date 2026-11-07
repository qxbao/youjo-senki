# Báo cáo tự kiểm (Semantic Self-Check) — `vol-08-ch-04-b03`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-04-b03`
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter014.xhtml/p000062` – `YS-LN08/Text/chapter014.xhtml/p000096` (35 đoạn)
- **Tệp đích**: `translations/vol-08/ch-04-b03.jsonl`

## 2. Kiểm tra đối chiếu quy chuẩn & thuật ngữ
- **Ngôi kể và điểm nhìn (`DEC-P01-001`)**:
  - Phân biệt rõ ràng giữa trần thuật ngôi thứ ba bám sát điểm nhìn của Tanya (`Tanya`, `cô`) ở các đoạn `p000062`, `p000065`, `p000068`, `p000077`, `p000080`, `p000085`, `p000087`, `p000092`, `p000093`, `p000095` và độc thoại nội tâm ngôi thứ nhất của Tanya (`mình`) ở các đoạn `p000063`, `p000064`, `p000070`, `p000071`, `p000082`, `p000086`, `p000096`.
  - Trong đoạn độc thoại nội tâm hướng trực tiếp về phía Trung úy Tospan (`p000064`), Tanya tự xưng `mình` và gọi đối phương là `anh`, nhất quán với cách xử lý ở lô trước (`ch-04-b02`).
- **Xưng hô trong hội thoại**:
  - Tanya nói chuyện qua điện đàm với Trung úy Tospan (`p000065`–`p000079`): Tanya xưng `tôi` – `anh` (`Trung úy Tospan`) hoặc `chúng ta` khi nói về tình thế chung bị bao vây (`p000069`); Tospan đáp lễ nghiêm túc theo quân kỷ (`Dạ, thưa Trung tá?`, `Rõ, thưa Trung tá`, `Xin cảm ơn Trung tá ạ!`, xưng `tôi` – `Trung tá`).
  - Tanya giao nhiệm vụ cho Trung úy Wüstemann (`p000083`–`p000084`): Tanya xưng `tôi` – `anh` (`Trung úy Wüstemann`), gọi Tospan là `Trung úy Tospan` / `anh ấy`; Wüstemann đáp `Rõ, thưa Trung tá!`.
  - Tanya bàn giao quyền chỉ huy tại sở chỉ huy cho Đại úy Meybert (`p000090`–`p000094`): Tanya xưng `tôi` – `anh` (`Đại úy Meybert`); Meybert đáp `Rõ, thưa Trung tá!`, xưng `tôi` – `Trung tá` và dùng tiểu từ lễ phép `ạ`.
- **Bảo toàn nhấn mạnh (`DEC-P01-002`)**:
  - Văn bản nguồn trong toàn bộ 35 đoạn từ `p000062` đến `p000096` không có thẻ nhấn mạnh (`<em>` hoặc `<i>`), do đó bản dịch hoàn toàn không sử dụng dấu `*...*`.
- **Thuật ngữ và tên riêng (`pending_terms` & `glossary`)**:
  - Tuân thủ nhất quán các phương án đã dùng ở các lô trước trong tập 8: `Trung úy Tospan` (`Lieutenant Tospan`), `Đại tá von Lergen` (`Colonel von Lergen`), `Trung úy Grantz` (`First Lieutenant Grantz`), `Trung tướng von Zettour` (`Lieutenant General von Zettour`), `Trung úy Wüstemann` (`First Lieutenant Wüstemann` / `Lieutenant Wüstemann`), `đại đội pháp sư` (`mage company`), `Ahrens` và `Meybert` (`Đại úy Meybert`), `lực lượng dự bị chiến lược` (`strategic reserves`), `bộ tổng tham mưu` (`general staff`), `sĩ quan trực ban` (`duty officer`), `sở chỉ huy` (`headquarters` / `command post`), `tiền tuyến` (`front lines`), `Đế quốc` (`the Empire`).
  - Đề xuất thuật ngữ mới cần lưu ý: `bộ binh độc lập` (`p000074`), `công ty mẹ nắm giữ cổ phần` (`p000076`), `động vật chính trị` (`p000089`).

## 3. Tự kiểm tra kỹ thuật & Sign-off
- Đủ 35/35 dòng JSONL, khớp thứ tự `segment_id` từ `p000062` đến `p000096`.
- Đã đối chiếu báo cáo `reviews/prose/vol-08/ch-04-b03-argon-review.yml`: không có lỗi cần sửa (`findings: []`), toàn bộ `pending_term_recommendations` và `locked_choices` từ `p000062` đến `p000096` đều đã được tuân thủ nhất quán.
- Tất cả 35/35 dòng trong `translations/vol-08/ch-04-b03.jsonl` đã được cập nhật `status` từ `"draft"` sang `"reviewed"`, giữ nguyên `translator: "argon-low"`, khớp `source_sha256` và `glossary_version` trong handoff.
- Không chép văn bản nguồn tiếng Anh vào bản dịch hoặc báo cáo tự kiểm.
