# Tự kiểm — vol-02-ch-06-b09-review-fixes

- Đã đối chiếu đủ 28 ID trong phạm vi p000257–p000284; giữ nguyên thứ tự, mã đoạn và ranh giới. Gói cục bộ khớp SHA-256 handoff: `b8e33087650cb9bb665a018e7adf731ed974f773356be5e7b132bb5d1561fe71`.
- Đã kiểm tra canon trước khi sửa: DEC-P01-001 điều chỉnh đại từ trần thuật/nội tâm; DEC-P01-002 yêu cầu dùng `*...*` đúng vùng được nhấn trong nguồn.
- Các mệnh đề pháp lý ở p000264 vẫn là hai điều kiện liên tiếp. Ở p000265, hành động gây nổ giữ dạng giả định, không nêu phương tiện ngoài gói; lời bình về hệ quả vẫn nằm ngoài vùng nghiêng.
- Các vùng nhấn mạnh khớp XHTML: p000265 có 1; p000276 có 2 (*hay* và *bất kỳ ai*); p000279 có 3; p000281 có 1; p000282 nghiêng toàn bộ đoạn (1 vùng). Tổng cộng 8 vùng nhấn mạnh trên 5 đoạn; không thêm chữ nghiêng ở ID khác.
- Dùng “nó” cho Tanya trong lời trần thuật tại p000274, p000276, p000278, p000279, p000281; giữ riêng lời thoại, lời đồn được dẫn và nội tâm vị tư lệnh ở p000282. Tại p000258 dùng “mình” cho lời tự nhủ, không thêm dấu thoại.
- Thuật ngữ trong phạm vi theo lựa chọn pending, không phải canon: `law of war` → “luật chiến tranh”; `noncombatants` → “người không tham chiến”; `sophistry` → “ngụy biện”; `militia` → “dân quân”; `Area Command` → “bộ chỉ huy khu vực”; `army corps commander` → “tư lệnh quân đoàn”; `Silver Wings Assault Badge` → “Huy hiệu Đột kích Cánh bạc”; `pacify the city` → “dẹp yên thành phố”.
- Các lựa chọn coordinator cho `legal opportunists` (“những kẻ lợi dụng luật pháp để kiếm lợi”), `rational marketplace` (“thị trường vận hành hợp lý”) và `purposive rationality` (“tính hợp lý trong việc đạt mục đích”) vẫn pending/non-canon; các ID liên quan nằm ngoài gói b09 này nên không có chỗ áp dụng trong bản dịch đang giao.

## Findings

| Finding | Mức | Xử lý |
|---|---|---|
| B09-F01 | Vừa | Đã thêm *hay* tại p000276, giữ *bất kỳ ai*; bao toàn bộ bản dịch p000282 bằng *...*, giữ nguyên đại từ nội tâm vị tư lệnh. Nhấn mạnh khớp nguồn: p000265 (1), p000276 (2), p000279 (3), p000281 (1), p000282 (1 toàn đoạn), tổng 8 vùng trên 5 đoạn. |
| B09-F02 | Vừa | p000264 giữ cả tuyên bố và cách diễn giải trong điều kiện; không biến cách diễn giải thành bước đã quyết định. |
| B09-F03 | Vừa | p000265 bỏ phương tiện không có căn cứ; giữ giả định có điều kiện và đúng vùng nghiêng. |
| B09-F04 | Vừa | p000279 dùng tạm “Huy hiệu Đột kích Cánh bạc”, giữ loại vật phẩm và định danh. |
| B09-F05 | Vừa | p000279 diễn đạt kiểu lính trẻ em trong truyền thuyết, không gán lai lịch truyền thuyết cho cá nhân. |
| B09-F06 | Vừa | Đã dùng “nó” trong trần thuật về Tanya ở đúng năm ID được giao; giữ riêng thoại, lời đồn dẫn và nội tâm người khác. |
| B09-F07 | Nhẹ | p000276 đổi mô tả đôi mắt sang hình ảnh lạnh/vô tri; giữ rõ cảm xúc hiện diện ở vế sau. |
| B09-F08 | Nhẹ | p000274 tăng mức xa lạ thành “rất xa lạ”, không thêm phép so với kỳ vọng. |
| B09-F09 | Nhẹ | p000270 khôi phục chênh lệch bằng “một sĩ quan chỉ mang hàm thiếu tá”; giữ chức danh tư lệnh quân đoàn. |
| B09-F10 | Nhẹ | p000271 nói rõ đó mới chỉ là một khả năng. |
| B09-F11 | Nhẹ | p000258 dùng “mình” trong lời tự nhủ, không thêm dấu thoại. |

## Kết quả và rủi ro

- Số finding đã xử lý: 11/11 (6 vừa, 5 nhẹ); B09-F01 vừa đã xử lý ở cả hai vị trí còn thiếu; finding nghiêm trọng: 0.
- Thuật ngữ nêu trên tiếp tục là lựa chọn tạm, không tự nâng thành canon. Tên tiếng Việt chính thức của huy hiệu và cấp/tên chính thức của bộ chỉ huy khu vực còn chưa được xác nhận.
- `legal opportunists`, `rational marketplace`, `purposive rationality` được ghi nhận theo quyết định coordinator nhưng thuộc đoạn ngoài phạm vi; không sửa bản dịch khác.
- Tệp được phép ghi: bản dịch lô b09 và self-check này. Commit: null; bước tiếp theo: `review_signoff`.
