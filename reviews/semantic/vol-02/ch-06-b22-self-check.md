# Tự kiểm tra ngữ nghĩa — vol-02-ch-06-b22 (Sign-off)

- Đã rà lại đủ 36 mã đoạn p000673–p000708, giữ nguyên ranh giới và thứ tự.
- Đã cập nhật toàn bộ `status` của 36 dòng trong `translations/vol-02/ch-06-b22.jsonl` từ `draft` sang `reviewed`.
- Nội tâm tự quy chiếu của Tanya ngoài thoại thống nhất dùng “mình” theo DEC-P01-001 (đã sửa ở p000674, p000675, p000678, p000681); lời thoại giữ “tôi”.
- Đại từ chỉ Uger trong tự thuật/nội tâm thống nhất là “ông ấy” (p000674, p000677–p000678, p000681, p000683, p000686); lời thoại của Tanya với Uger tại p000684 sửa thành “Ông” (“Ông biết chuyện gì sao?”).
- Chữ nghiêng ở p000683 giữ `*À*`; p000707 giữ phạm vi nhấn mạnh mệnh đề suy nghĩ trước dấu phẩy.

## Xử lý findings từ Argon Review (`reviews/prose/vol-02/ch-06-b22-argon-review.yml`)

- **Serious — p000684 (`pronouns_and_speaker`)**: Đổi đại từ ngôi thứ hai từ “Cô” sang “Ông” (“Ông biết chuyện gì sao?”) đúng chủ thể Tanya hỏi Uger.
- **Moderate — p000674, p000675, p000681 (`pronouns_and_viewpoint`)**: Đổi “tôi” ngoài thoại sang “mình” ở p000674 và câu sau lời thoại ở p000675; đổi “ông ta” ở p000674 thành “ông ấy”; đổi “chúng tôi” ở p000681 thành “mình và ông ấy”.
- **Moderate — p000681 (`omission`)**: Khôi phục thành phần giải thích nhấn mạnh sau dấu gạch ngang dài ở cuối câu (“...vẫn thúc đẩy các sĩ quan gắn kết với nhau—tạo thành những mối dây liên hệ.”).
- **Moderate — p000689 (`terminology_and_meaning`)**: Bổ sung định ngữ thành “các sĩ quan tác chiến được vận chuyển”.
- **Minor — p000682, p000707 (`pending_term_consistency`)**: Đổi “Tướng quân von Zettour” thành “Tướng von Zettour”.
- **Minor — p000676, p000688, p000690 (`terminology_consistency`)**: Thống nhất viết hoa tên cơ quan là “Cục Đường sắt”.
- **Minor — p000677 (`meaning_and_logic`)**: Chỉnh câu cuối thành “So với một người không phục vụ ngoài chiến trường, có lẽ ông ấy sẽ lên đến trung tá khá nhanh.” để giữ rõ quan hệ đối chiếu.
- **Minor — p000703 (`pending_term_consistency`)**: Chỉnh thành “cảm quan kinh tế và tính hợp lý của mình” đồng bộ với p000704 và lưu ý trong `canon/glossary-pending.yml`.

## Lựa chọn tạm còn pending (áp dụng theo `pending_term_recommendations` và `locked_choices`)

- `Major Uger`: “Thiếu tá Uger” (p000675, p000676, p000686).
- `Railroad Department`: “Cục Đường sắt” (p000676, p000688, p000690).
- `Logistics`: “ngành Hậu cần” (p000676, p000678).
- `war college`: “trường đại học quân sự” (p000677, p000678; đồng bộ “học đại học cùng nhau” ở p000681).
- `interior lines strategy`: “chiến lược nội tuyến” (p000690).
- `General von Zettour`: “Tướng von Zettour” (p000682, p000707).

## Rủi ro còn lại

- Các phương án thuật ngữ quân sự và tên tổ chức chưa chốt trong canon (`Cục Đường sắt`, `ngành Hậu cần`, `trường đại học quân sự`, `chiến lược nội tuyến`) được áp dụng nhất quán theo locked choices của Argon Review và vẫn mang trạng thái pending để coordinator theo dõi.
