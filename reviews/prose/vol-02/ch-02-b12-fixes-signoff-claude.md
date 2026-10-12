# Signoff sửa lỗi — vol-02-ch-02-b12-final-signoff

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon). Không trích văn bản nguồn.
- Phạm vi: p000301, p000303, p000308, p000310, p000311, p000314, p000316, p000317, p000318, p000319 (viết tắt `pNNNNNN`, thuộc `YS-LN02/Text/part0014.xhtml`). Đã đối chiếu: báo cáo b12 gốc, handoff b12, gói nguồn đã chuẩn bị, `translations/vol-02/ch-02-b12.jsonl`, mục `chapter2_b12_translation_proposals` trong `work/run-state/pending-terms.yml`. Không xem batch dịch khác. Mọi thuật ngữ vẫn là đề xuất tạm, chưa phải canon.

## Kết luận: `approved` (serious 0, moderate 0, minor 3)

## 1. Kết quả theo hạng mục

| Hạng mục | Đoạn | Kết quả |
|---|---|---|
| M1 — sắc thái miệt thị | p000301 | **Đạt.** "phía Cộng hòa" và "chỉ đang mơ mộng thôi" đã bỏ khinh miệt và đánh giá "viển vông". Khớp ledger `republicans-casual-reference`. |
| M2 — quan hệ "nên" | p000310 | **Đạt.** Nay hiểu là giao tranh bên đó phần lớn đã kết thúc, nên có thể điều đơn vị đi nơi khác. Hết mâu thuẫn logic, khớp p000311 ("khi rảnh tay") và p000318 (Dacia thất thủ nhanh). Phủ định và đối tượng câu hỏi giữ nguyên. |
| M3 — đại từ sĩ quan tình báo | p000311, p000314, p000317, p000318 | **Đạt.** Cả bốn đoạn dùng "anh ta", không còn "ông". Khớp ledger `intelligence-officer-pronoun` và `review_provisional_choices` trong handoff. p000314 vẫn dùng chức danh ở câu mở, nên không bị đọc thành hai người. |

## 2. Căn chỉnh ledger đã chọn

| Mục ledger | Đoạn | Kết quả |
|---|---|---|
| high command → bộ chỉ huy cấp cao | p000303 | Khớp. |
| record library → thư viện dữ liệu | p000308, p000316 | Khớp. |
| Western Army Group → Cụm tập đoàn quân phương Tây | p000319 | Khớp. "phương Bắc" đi cùng "phương Tây", dạng nhất quán. |
| mana inclination → khuynh hướng mana | p000314 | Khớp. |
| intelligence officer pronoun → anh ta | p000311, p000314, p000317, p000318 | Khớp. |
| Republicans (casual) → phía Cộng hòa | p000301 | Khớp. |

Cơ học: `notes` rỗng; dấu ngoặc kép đóng/mở đúng; `*...*` chỉ ở p000311 (nguồn có nhấn mạnh), không thừa ở các đoạn khác trong phạm vi.

## 3. Còn lại — nhẹ (không bắt buộc)

- **m-a — p000311:** vẫn "mấy cậu Hướng đạo sinh" (thêm "cậu" thân mật) và "cuộc càn quét" (nghĩa quân sự hơn nguồn). Chưa đổi từ minor m7 gốc, độ tin cậy 0,4.
- **m-b — p000314:** vẫn "có thể đang trò chuyện", biến nhượng bộ thành phỏng đoán. Chưa đổi từ minor m9 gốc, độ tin cậy 0,5. Không đổi nghĩa chính.
- **m-c — p000301 (cùng p000300, p000304, p000305):** "cô ta" cho Tanya là minor m1 gốc, không thuộc nhóm sửa. Không suy diễn danh tính. Giữ được nếu coordinator chọn góc nhìn kẻ thù.

p000316: "Chúng" nay chỉ còn một lần, chỉ kẻ địch, và vế sau dùng "mật mã và giao thức ấy". Minor m11 coi như xử lý đủ.

## 4. Rủi ro

- Các lựa chọn đại từ, thuật ngữ và đơn vị vẫn ở trạng thái `provisional_non_canon`. Nếu sau này đổi, chỉ cần sửa trong các đoạn đã liệt kê ở mục 2.
- Ledger vẫn lệch giữa "phía Đông" và "phương Bắc/Tây" của các cụm tập đoàn quân. Cần coordinator hài hòa sau, không chặn b12.
- Không có hard stop; không cần hỏi người dùng.

## 5. Bước tiếp theo

Coordinator có thể chạy lại validator/diff-check rồi commit b12 và chuyển batch kế. Các minor ở mục 3 có thể bỏ qua hoặc gom vào lượt sửa chung.
