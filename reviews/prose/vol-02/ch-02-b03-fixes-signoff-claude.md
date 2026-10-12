# Signoff sửa lỗi — vol-02-ch-02-b03 (Claude reviewer)

- **Task:** vol-02-ch-02-b03-final-signoff
- **Phạm vi:** chỉ 8 đoạn đã sửa: p000044, p000046, p000047, p000049, p000053, p000059, p000062, p000069. Đối chiếu với báo cáo `reviews/prose/vol-02/ch-02-b03-claude.md`, handoff b03, gói nguồn b03, bản dịch b03, canon và ledger pending. Không xem batch khác. Báo cáo không trích văn bản nguồn.
- **Kết luận:** `pass`. serious = 0, moderate = 0, minor còn lại = 2 (m1, m4 cũ, không bắt buộc sửa).

## Xác nhận M1–M4

| ID | Đoạn | Kết quả |
|---|---|---|
| M1 | p000044, p000046, p000053, p000059, p000062 | **Đã giải quyết.** Toàn bộ dùng "Nghị viên" theo ledger `vol02-ch02-b02-councilor`: "Nghị viên Abensoll" (p000044, p000062), "Nghị viên Ngoại giao Abensoll" (p000046, p000059), "Nghị viên Nội vụ" (p000053), "một nghị viên" (p000046). Không còn "Ủy viên", "Hội đồng" viết hoa hay cụm miêu tả dài. Nhất quán với b02. |
| M2 | p000069 | **Đã giải quyết.** Trần thuật về Tanya lặp tên, không còn đại từ "Cô"; hợp DEC-P01-001. Chủ thể Weiss, binh sĩ và Tanya rõ ràng. |
| M3 | p000047 | **Đã giải quyết.** "đi bước đầu tiên để tiến tới việc tham chiến" khớp nghĩa nguồn (bước khởi đầu, không phải bên đầu tiên tham chiến). Hết mâu thuẫn với câu trước. |
| M4 | p000049 | **Đã giải quyết.** "đưa ra lời đề nghị này, một nửa là để sỉ nhục họ" đặt "một nửa" vào động cơ như đề xuất; không còn đọc thành giới hạn phạm vi viện trợ. Không thêm chủ thể ngoài nguồn. |

## Kiểm tra bổ sung trên 8 đoạn

- Dấu ngoặc kép thoại, người nói và nhấn mạnh (không có nhấn mạnh nguồn trong các đoạn này; không có `*…*` thừa): đạt.
- Không phát sinh lỗi mới từ các sửa đổi: không thấy sai nghĩa, thừa/thiếu ý, hay lệch thuật ngữ. "Khối Thịnh vượng chung", "Liên minh Entente", "Trung úy" (p000069) khớp lựa chọn tạm trong handoff.
- Handoff ghi `resolved_moderate: [M1–M4]` và đúng 8 đoạn thay đổi, khớp phạm vi tôi rà.

## Còn lại (minor, không chặn)

- **m1 (p000046):** "lớn tuổi hơn" vẫn gợi so sánh với Abensoll; nên là "lớn tuổi" hoặc "cao tuổi". Không sửa cũng không ảnh hưởng.
- **m4 (p000062):** "thiết giáp hạm" hẹp hơn "capital ship" (đề xuất "chiến hạm chủ lực"); dấu "?" sau "thôi đấy" hơi lủng củng. Mức nhẹ, độ tin cậy 0.6.

## Rủi ro

- Các lựa chọn "Nghị viên", "Khối Thịnh vượng chung", "Liên minh Entente", "Trung úy" vẫn chỉ là đề xuất tạm, không canon. Nếu sau này đổi "Nghị viên" thành "Ủy viên", phải đổi đồng loạt b02, b03 và các batch sau.
- Chưa xác nhận trạng thái ledger sau sửa (không được sửa/ghi); coordinator nên đảm bảo mã đoạn b03 nằm trong mục councilor.

## next_action

Coordinator có thể đóng b03: chạy validator cuối nếu cần, commit và đi tiếp. m1/m4 tùy chọn sửa lúc rà soát sau.
