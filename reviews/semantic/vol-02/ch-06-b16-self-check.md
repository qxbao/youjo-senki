# B16 semantic self-check (Translator Sign-off)

Phạm vi: `YS-LN02/Text/part0030.xhtml/p000479`–`p000509` (31 đoạn). Đã xử lý đầy đủ toàn bộ các findings và `pending_term_recommendations` có căn cứ trong `reviews/prose/vol-02/ch-06-b16-argon-review.yml`, bảo đảm tuân thủ mọi `locked_choices`, và cập nhật trường `status` của toàn bộ 31 dòng trong `translations/vol-02/ch-06-b16.jsonl` từ `draft` sang `reviewed`.

## Findings từ Argon review đã xử lý

- **B16-F01 — p000492 (moderate):** Đổi “người phụ tá tài giỏi” thành “người trợ thủ tài giỏi” để phân biệt rõ vai trò cấp phó/cánh tay phải của Weiss với chức danh sĩ quan phụ tá (“viên phụ tá”) của Serebryakov ở `p000483`.
- **B16-F02 — p000493 (moderate):** Đổi “viên Thượng úy Weiss xuất sắc” thành “chàng Trung úy Weiss tử tế” để đồng bộ quân hàm “Trung úy Weiss” với `p000482`, `p000484` và khớp sắc thái phẩm chất lương thiện/tử tế tương ứng với `p000506`.
- **B16-F03 — p000508 (moderate):** Đổi “phe thân Cộng hòa ở Arene” thành “quân du kích ở Arene” để tách bạch thuật ngữ quân sự - pháp lý chỉ lực lượng du kích kháng chiến với đối tượng “đám thân Cộng hòa cố thủ ở Arene” ở `p000504`.
- **B16-F04 — p000479 (minor):** Đồng bộ “hỏa lực được tổ chức bài bản của Cộng hòa” thành “hỏa lực có kiểm soát của Cộng hòa” theo `locked_choices` và sổ thuật ngữ tạm.
- **B16-F05 — p000499 (minor):** Đổi “trong cuộc chiến vô nghĩa này” thành “vào sự lãng phí mang tên chiến tranh này” để giữ trọn ẩn dụ kinh tế học trong lăng kính của Tanya.

## Đề xuất tạm về thuật ngữ, quân hàm, đại từ và nhấn mạnh

- **Quân hàm, chức danh và danh từ riêng (`vol02-ch06-b16-ranks-roles-and-proper-nouns`):**
  - Giữ nguyên địa danh `Rhine`, `Norden`, `Arene` và danh hiệu `Ace of Aces` (`p000493`).
  - Thống nhất `Trung úy Weiss` (`p000482`, `p000484`, `p000493`), `Phó chỉ huy` (`p000482`), `người trợ thủ tài giỏi` (`p000492`), `Trung úy Serebryakov` (`p000481`), `viên phụ tá` (`p000483`), `thưa thiếu tá` (`p000495`).
  - Phân biệt `đám thân Cộng hòa` (`p000504`) và `quân du kích ở Arene` (`p000508`).
- **Thuật ngữ chiến thuật, y tế và tư tưởng (`vol02-ch06-b16-tactical-medical-and-ideological-terms`):**
  - Dùng nhất quán `đợt phản công`, `đội hình tấn công`, `hỏa lực có kiểm soát`, `các vị trí khai hỏa của địch`, `cơ động phân tán`, `tốc độ là áo giáp` (`p000479`); `hỏa lực`, `quân Đỏ` (`p000480`); `thuốc bổ` (`p000481`); `nhiên liệu của người lính` (`p000483`); `garô` (`p000486`); `sơ cứu`, `những kẻ cuồng chiến`, `adrenaline` (`p000487`); `meth`, `đám nghiện chiến tranh` (`p000488`); `kẻ cuồng chiến`, `chuỗi chỉ huy` (`p000492`); `những tay đánh chặn` (`p000494`); `đưa họ về căn cứ` (`p000496`); `đám cuồng chiến` (`p000497`); `lý trí và thị trường`, `xã hội tư bản` (`p000499`); `nhân quyền`, `có lòng nhân ái` (`p000505`); `cuộc thảm sát` (`p000507`); `ba con khỉ thông thái` (`p000509`).
- **Đại từ, điểm nhìn và nhấn mạnh (`vol02-ch06-b16-pronouns-pov-and-three-emphases`):**
  - Tuân thủ `DEC-P01-001`: trần thuật ngôi thứ ba quy chiếu Tanya bằng `Tanya` / `nó`; độc thoại nội tâm Tanya tự xưng `mình` / `chúng ta`, gọi Weiss là `anh` / `anh ta` và Serebryakov là `cô ấy`.
  - Tuân thủ `DEC-P01-002`: giữ chính xác 3 đoạn có nhấn mạnh bằng `*...*` tại `p000480` (toàn câu), `p000507` (câu cuối) và `p000508` (hai vế kẹp giữa cụm trần thuật `, nó tự giễu,`).

## Rủi ro và trạng thái

- Toàn bộ 31 dòng trong `translations/vol-02/ch-06-b16.jsonl` đã được cập nhật `status: "reviewed"`.
- Các lựa chọn thuật ngữ, quân hàm và xưng hô vẫn ở trạng thái pending, không tự nâng thành canon.
