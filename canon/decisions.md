# Nhật ký quyết định

Các quyết định sau pilot-01 được ghi bên dưới; thuật ngữ chuyên môn chưa đủ căn cứ vẫn chờ xét.

Khi có quyết định, ghi: mã quyết định, ngày, vấn đề, các phương án, lựa chọn,
lý do, mã đoạn liên quan, người duyệt và trạng thái (đề xuất / đã duyệt / thay thế).
Chỉ quyết định đã duyệt mới được dùng làm chuẩn; giữ lịch sử khi thay đổi.

## DEC-P01-001 — Đại từ và giới hạn suy luận về nhân vật

- **Ngày:** 2026-10-12.
- **Trạng thái:** đã duyệt.
- **Người duyệt:** người giao việc, theo yêu cầu cập nhật canon sau hai lượt pilot.
- **Vấn đề:** phân biệt đại từ trần thuật và nội tâm của Tanya, giới hạn suy luận khi thiếu ngữ cảnh.
- **Phương án được xét:** “nó” trong trần thuật và “mình” trong nội tâm tự quy chiếu, theo đề xuất của lượt pilot đầu.
- **Lựa chọn:** trần thuật về Tanya ở giai đoạn này dùng “nó”; nội tâm tự quy chiếu của Tanya dùng “mình”. Không tự mở rộng quy ước này sang chủ thể hoặc giai đoạn khác.
- **Giới hạn:** không suy ra quan hệ thân thuộc, giới tính hoặc cấp bậc chỉ từ một đoạn thiếu ngữ cảnh; cách gọi trong thoại phải được xét riêng khi có đủ căn cứ.
- **Lý do:** giữ nhất quán điểm nhìn, đồng thời tránh biến phương án đại từ hoặc lời gọi thân mật thành thông tin về quan hệ nhân vật.
- **Mã đoạn liên quan:** `YS-LN01/Text/chapter001.xhtml/p000008`, `YS-LN01/Text/chapter001.xhtml/p000009`, `YS-LN01/Text/chapter001.xhtml/p000013`, `YS-LN01/Text/chapter001.xhtml/p000014`, `YS-LN01/Text/chapter001.xhtml/p000015`, `YS-LN01/Text/chapter001.xhtml/p000031` (giới hạn suy luận).
- **Căn cứ:** `reviews/pilot-01-blind-evaluation.md`, đề xuất BL-P03; giới hạn ngữ cảnh tại p000031 trong `reviews/pilot-01-argument-blind-evaluation.md`; chỉ dẫn duyệt của người giao việc.

## DEC-P01-002 — Biểu diễn chữ nghiêng/nhấn mạnh trong translation

- **Ngày:** 2026-10-12.
- **Trạng thái:** đã duyệt.
- **Người duyệt:** người giao việc, theo yêu cầu cập nhật canon sau hai lượt pilot.
- **Vấn đề:** biểu diễn dấu nhấn mạnh của nguồn trong trường `translation`.
- **Các phương án:** văn bản phẳng không đánh dấu hoặc Markdown `*...*`.
- **Lựa chọn:** dùng Markdown `*...*` chỉ khi nguồn có nhấn mạnh tương ứng; giữ đúng phạm vi nhấn mạnh, không tự thêm dựa trên loại câu hoặc điểm nhìn.
- **Lý do:** tránh mất dấu hiệu cấu trúc khi biểu diễn bản dịch trong JSONL. Quyết định này chỉ quy định trường `translation`, không quy định cách dựng hoặc sửa EPUB.
- **Mã đoạn liên quan:** `YS-LN01/Text/chapter001.xhtml/p000008`, `YS-LN01/Text/chapter001.xhtml/p000009`, `YS-LN01/Text/chapter001.xhtml/p000014`.
- **Căn cứ:** `reviews/pilot-01-blind-evaluation.md`, đề xuất BL-P05 và nhận xét kỹ thuật; chỉ dẫn duyệt của người giao việc.
