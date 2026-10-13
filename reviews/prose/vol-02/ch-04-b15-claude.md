# Review vol-02-ch-04-b15 (Claude, prose/semantic)

- Phạm vi: `YS-LN02/Text/part0024.xhtml/p000111`–`p000140` (30 đoạn), package hash `6d159f1e…83d0`, glossary/style-guide/decisions đúng handoff.
- Đã kiểm: nghĩa, thiếu/thừa, đại từ (DEC-P01-001), nhấn mạnh (DEC-P01-002), văn phong, 4 thuật ngữ pending, đối chiếu thuật ngữ công thức/bom chìm với các lựa chọn pending chương 4 trong `pending-terms.yml` (không đọc bản dịch lô khác).
- Kết quả: 0 nghiêm trọng, 3 vừa, 4 nhẹ. Nghĩa tổng thể đúng, không có đoạn bị bỏ hoặc thêm đáng kể; logic pháp lý (lặn ≠ từ chối kiểm tra → bắn cảnh cáo, không bắn trúng trực tiếp) được giữ chính xác.

## Phát hiện

### Vừa

**M1 — p000127, p000133, p000140: bản dịch lệch ledger thuật ngữ "formula".**
Bản dịch dùng "phép thức bắn tỉa" / "phép thức nổ mạnh", trong khi đề xuất b15 (`vol02-ch04-b15-sniping-formulas`, `-heavy-explosion-formulas`) và các lô chương 1–4 (b10, b11…) đều dùng gốc "thuật thức". "Phép thức" chỉ là phương án thay thế. Lỗi nhất quán thuật ngữ; chính bản ledger của b15 cũng ghi "reuse… root", nên bản dịch tự mâu thuẫn với báo cáo của mình.
Đề xuất: sửa thành "thuật thức bắn tỉa" (p000127), "thuật thức nổ mạnh" (p000133, p000140). Chỉ là đề xuất, không phải canon.

**M2 — p000133, p000134: "depth charge" dịch "bom chìm", ledger ghi "mìn sâu".**
Đề xuất b15 `vol02-ch04-b15-depth-charge` = "mìn sâu" (nhất quán b10/b12); bản dịch dùng phương án thay thế "bom chìm" ở cả hai đoạn. Lệch nhất quán trong chương.
Đề xuất: áp dụng một thuật ngữ cho cả chương. Phương án an toàn nhất cho b15: sửa thành "mìn sâu" theo ledger. Ghi chú cho coordinator: về mặt tự nhiên tiếng Việt, "bom chìm" là cách gọi quen thuộc hơn, độ tin cậy ~0.6; nếu muốn đổi thì phải đổi đồng loạt b10/b12/b15 và cập nhật ledger — ngoài phạm vi review này.

**M3 — p000114, p000123: mất nhấn mạnh/chữ nghiêng nội tâm (DEC-P01-002).**
Nguồn có `<em>` ở câu nội tâm (p000114 "Another extra job to do?", p000123 "Does it really matter how deep the mire goes?"); bản dịch không có dấu `*...*`. Quyết định đã duyệt yêu cầu giữ nhấn mạnh tương ứng.
Đề xuất: `*Lại có thêm việc phải làm sao?*` và `*Bùn lầy sâu đến đâu thì có thật sự quan trọng không?*`.

### Nhẹ

**L1 — p000118, p000137: `<em>` ở tên tàu *Lytol* và *Jawohl* không được đánh dấu.** Đây là nghiêm ngặt ít là nhấn mạnh hơn là quy ước tên tàu/ngoại ngữ, nên mức nhẹ. Đề xuất: `*Lytol*`, `*Jawohl*` cho đồng bộ với nguồn (hoặc coordinator quyết quy ước chung).
Liên quan: p000137 bỏ "Frau" ("thưa Thiếu tá"), làm mất sắc thái tiếng Đức của quân Đế quốc; p000138 cũng đồng bộ. Đề xuất trung tính: giữ "Jawohl" hoặc "Rõ, Frau Major" — chưa đủ căn cứ để coi là lỗi nghĩa.

**L2 — p000111–p000113: đại từ "mình" cho người kể không phải Tanya.**
Ba đoạn này là ngôi thứ nhất của một người quan sát (khác Tanya; đoạn p000114 mới chuyển sang Tanya ở ngôi thứ ba). DEC-P01-001 chỉ duyệt "mình" cho nội tâm tự quy chiếu của Tanya và cấm tự mở rộng sang chủ thể khác. Bản dịch dùng "mình" cho người quan sát, chưa có căn cứ về danh tính/quan hệ.
Đề xuất tạm: giữ "mình" nhưng ghi vào ledger là độ bất định, hoặc dùng cách diễn đạt trung tính ("tôi"). Tôi nghiêng về "tôi" vì tránh áp quy ước của Tanya lên chủ thể khác (độ tin cậy ~0.5). Không ảnh hưởng cốt truyện.

**L3 — p000113: "Hẳn họ không phải chẳng có quan hệ gì với nhau."** Phủ định kép đúng nghĩa nhưng nặng và dễ gây hiểu sai thành khẳng định chắc chắn (nguồn: "không thể không liên quan"). Đề xuất: "Hai người đó chắc chắn có liên quan với nhau."/ "Không thể nào họ không liên quan." Hai đoạn p000113 còn lại ổn.

**L4 — p000117: "tình hình vẫn tiếp diễn"** hơi yếu so với "the situation was developing" (tình hình đang diễn biến). Đề xuất: "tình hình vẫn đang diễn biến".

## Đại từ, nhấn mạnh, nghĩa — tóm tắt

- Tanya trần thuật dùng "nó" (p000114, p000117), nội tâm "mình" (p000119–p000124, p000128–p000136): đúng DEC-P01-001.
- Thoại và mệnh lệnh: "Trung úy Weiss", "Thiếu tá", "các anh": tự nhiên, không suy diễn quan hệ.
- Phần luật chiến tranh (p000115–p000116, p000121, p000131): giữ đúng điều kiện, phủ định, "cảnh cáo trước". "Lặn xuống không có nghĩa là từ chối kiểm tra" đúng.
- Ẩn dụ bùn/ga trắng (p000123–p000124, p000130–p000131): giữ được hình ảnh; "chẳng hại gì nó" (p000124) hơi mơ hồ về đại từ "nó" nhưng chấp nhận được.
- Chú thích ¹⁵ ở p000112 được giữ.

## Thuật ngữ pending (4 mục b15)

| id | source_term | đề xuất ledger | bản dịch | đánh giá |
|---|---|---|---|---|
| vol02-ch04-b15-sniping-formulas | sniping formulas | thuật thức bắn tỉa | phép thức bắn tỉa (p000127) | lệch — M1 |
| vol02-ch04-b15-heavy-explosion-formulas | heavy explosion formulas | thuật thức nổ mạnh | phép thức nổ mạnh (p000133, p000140) | lệch — M1 |
| vol02-ch04-b15-depth-charge | depth charge(s) | mìn sâu | bom chìm (p000133, p000134) | lệch — M2 |
| vol02-ch04-b15-commonwealth-vessel | Commonwealth vessel | tàu của Khối Thịnh vượng chung | tàu của Khối Thịnh vượng chung (p000138) | khớp, chấp nhận |

Khuyến nghị tạm (đều không phải canon): thuật thức bắn tỉa; thuật thức nổ mạnh; mìn sâu (theo ledger, đổi sang "bom chìm" chỉ khi coordinator đổi đồng loạt); tàu của Khối Thịnh vượng chung. Ledger đề xuất cần được cập nhật nếu bản dịch được giữ nguyên.

## Kết luận

Cần sửa M1–M3 trước khi tính hoàn tất lô; các mục nhẹ L1–L4 sửa hoặc ghi nhận tùy người giữ quyền sửa. Không có hard stop; không có mục nào ảnh hưởng cốt truyện.
