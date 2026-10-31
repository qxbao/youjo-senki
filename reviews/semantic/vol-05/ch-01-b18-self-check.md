# Báo cáo tự kiểm (Self-Check) — `vol-05-ch-01-b18` (Sign-off)

## 1. Phạm vi và trạng thái
- **Task ID:** `vol-05-ch-01-b18-translator-signoff` (parent: `vol-05-ch-01-b18`)
- **Tập / Chương:** `vol-05`, Chương 1
- **Mã đoạn:** `YS-LN05/Text/part0010.html/p000611` đến `YS-LN05/Text/part0010.html/p000653` (43 đoạn)
- **Tệp bản dịch:** `translations/vol-05/ch-01-b18.jsonl`
- **Trạng thái các dòng:** `reviewed` (43/43 dòng đã cập nhật từ `draft` sang `reviewed`)

## 2. Xử lý kết quả phản biện (`reviews/prose/vol-05/ch-01-b18-argon-review.yml`)
- **`YS-LN05/Text/part0010.html/p000613` (minor / word_choice):** Đã chỉnh cụm `"những kẻ có cảm tình cốt cán với Cộng sản"` thành `"những phần tử cốt cán có cảm tình với Cộng sản"` theo khuyến nghị của Argon để trật tự bổ nghĩa tự nhiên trong tiếng Việt.
- **`YS-LN05/Text/part0010.html/p000636` (minor / context_nuance):** Đã chỉnh lời thoại của Serebryakov từ `"Của Trung tá đây ạ."` thành `"Đây ạ, thưa Trung tá."` để thể hiện rõ hành động đưa mảnh ghi chép viết tay mới cho Tanya thay vì trả lại tập tài liệu.
- **`YS-LN05/Text/part0010.html/p000643` (minor / pronouns_voice):** Đã chỉnh cụm `"với hệ tư tưởng của mình"` thành `"với hệ tư tưởng của họ"` để tránh lặp từ và tách biệt rõ với đại từ nội tâm `"Mình"` (quy chiếu Tanya theo `DEC-P01-001`) ở đầu câu.
- **Tuân thủ `locked_choices` & `pending_term_recommendations`:** Bảo toàn đầy đủ tất cả các lựa chọn đã khóa và toàn bộ thuật ngữ đề xuất (`những người Cộng sản / Cộng sản`, `lực lượng Feldgendarmerie`, `Liên bang`, `quân cảnh / bên quân cảnh`, `Thiếu tá Weiss`, `phó chỉ huy`, `Trung tá`, `Trung úy Serebryakov`, `quốc gia đa sắc tộc`, `tiếng Liên bang / ngôn ngữ Liên bang chính thức`, `Lục quân Đế quốc`, `Kampfgruppe`, `huấn luyện kháng thẩm vấn`, `các hạ sĩ quan`, `các chính ủy`).

## 3. Kiểm tra điểm chính (Checkpoints)
- **Nghĩa và logic (`meaning`):**
  - Đảm bảo truyền tải chính xác tiến trình lập luận và sự chuyển biến nhận thức của Tanya: từ thất vọng trước các báo cáo thẩm vấn tù binh rập khuôn của quân cảnh (`p000611`–`p000616`), cuộc trao đổi với Thiếu tá Weiss về động cơ chiến đấu liều lĩnh của lính Liên bang (`p000617`–`p000621`), lời đề xuất của Trung úy Serebryakov và băn khoăn của Tanya về rào cản ngôn ngữ / phương ngữ ở quốc gia đa sắc tộc (`p000622`–`p000629`), cho đến bất ngờ lớn khi đọc mảnh ghi chép thẩm vấn sơ bộ do Serebryakov thực hiện (`p000630`–`p000653`).
  - Giữ nguyên cấu trúc phủ định, mức độ chắc chắn và giả định (như nhận định của Tanya ở `p000625`, `p000626`, `p000643`, và câu trả lời chuẩn xác của Serebryakov ở `p000651`, `p000653`).
- **Đại từ và xưng hô (`pronouns`):**
  - Trần thuật ngôi thứ ba gọi Tanya là `cô`, Weiss là `anh`, Serebryakov là `cô`.
  - Độc thoại nội tâm của Tanya dùng `mình` (`p000614`, `p000616`, `p000643`) và `chúng ta` khi quy chiếu tập thể quân Đế quốc (`p000613`, `p000614`, `p000616`).
  - Trong đối thoại: Weiss và Serebryakov xưng `tôi` (hoặc `chúng tôi` ở `p000651`), gọi Tanya là `chỉ huy` (`p000620`) hoặc `Trung tá` (`p000622`, `p000632`, `p000636`), có đệm từ kính ngữ `ạ` phù hợp với vị thế cấp dưới; Tanya xưng `tôi`, gọi cấp dưới bằng quân hàm + tên (`Thiếu tá Weiss`, `Trung úy Serebryakov`) hoặc `cô` với Serebryakov (`p000639`, `p000650`, `p000652`).
- **Nhấn mạnh và định dạng (`emphasis`):**
  - Tuân thủ `DEC-P01-002`: chỉ dùng `*...*` tại đúng phần có thẻ nhấn mạnh trong nguồn ở `p000626` (`*Ngôn ngữ đúng là một vấn đề phiền phức thật…*`). Các đoạn khác không có nhấn mạnh trong nguồn nên không tự ý thêm `*...*`.
  - Bảo toàn dấu ngoặc kép cho các cụm từ được đóng ngoặc kép trong nguồn tại `p000625` (“ngôn ngữ Liên bang chính thức”), `p000642` (“người lính bình thường”), `p000644` (“những người Cộng sản”) và dấu nháy đơn trong thoại tại `p000652` (‘những người Cộng sản’).

## 4. Kết quả công cụ kiểm tra
- Đã chạy `validate_translation.py` và đảm bảo kết quả đạt yêu cầu (`PASS`).
