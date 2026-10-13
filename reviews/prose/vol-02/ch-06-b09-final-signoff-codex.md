# Final-signoff — vol-02-ch-06-b09

```yaml
role: reviewer
task_id: vol-02-ch-06-b09-final-signoff
state: done
signoff: changes_required
review_path: reviews/prose/vol-02/ch-06-b09-final-signoff-codex.md
files_written: [reviews/prose/vol-02/ch-06-b09-final-signoff-codex.md]
scope:
  start: YS-LN02/Text/part0030.xhtml/p000257
  end: YS-LN02/Text/part0030.xhtml/p000284
  assigned: 28
  assessed: 28
source_package_sha256: b8e33087650cb9bb665a018e7adf731ed974f773356be5e7b132bb5d1561fe71
source_package_hash: pass
translation_sha256: 4a95be115150b12a7892350a979cab3faebf2ee26cb63914c1705a4de02c25ab
self_check_sha256: 3dfe7b9547b3793f57a0d0d473ea5e2a8ef3390654a7d09008aeefbd0cbdb8c5
counts: {serious: 0, moderate: 1, minor: 0}
resolved_counts: {serious: 0, moderate: 5, minor: 5}
unresolved_findings: [B09-F01]
term_recommendations:
  status: pending_non_canon
  assigned_clusters: 8
  recommendation: retain_current_provisional_choices
validator: not_run
diff_check: not_run
risks:
  - Self-check và fixes handoff ghi F01 đã hoàn tất nhưng bản dịch còn thiếu hai vùng nhấn mạnh.
  - Tên huy hiệu và cấp hoặc tên chính thức của cơ quan khu vực vẫn chưa được chuẩn hóa thành canon.
  - Xác nhận trạng thái pending dựa trên hồ sơ được giao; không kiểm toán ledger hoặc canon ngoài phạm vi.
commit: null
next_action: coordinator_assign_F01_fix_then_recheck
```

Đã đọc persona reviewer, shared, config, signoff handoff, fixes handoff, review ban đầu, self-check hiện tại và đúng gói/bản dịch b09. Hash gói được tính trực tiếp và khớp handoff. Hai tệp JSONL có đủ 28 ID cùng thứ tự, không lệch ranh giới. Không mở EPUB/PDF, gói khác hoặc nguồn chú thích. Chỉ ghi báo cáo này; không chạy validator hoặc diff-check, không commit.

Review hoàn tất; final-signoff chưa đạt. Đã giải quyết 10/11 finding. Số còn lại tính theo finding độc lập: **0 nghiêm trọng, 1 vừa, 0 nhẹ**. Hai vị trí thiếu nhấn mạnh và lời tự kiểm chưa đúng cùng thuộc B09-F01, không đếm thành finding mới.

## Finding còn lại

**B09-F01 — vừa — khôi phục nhấn mạnh chưa đủ.**

- `YS-LN02/Text/part0030.xhtml/p000276`: XHTML có hai vùng nhấn mạnh; bản dịch chỉ có một vùng quanh “bất kỳ ai”. Liên từ “hay” giữa lý trí và cảm xúc chưa được nghiêng. Đề xuất: chỉ đổi liên từ đó thành `*hay*`, giữ vùng nghiêng hiện có.
- `YS-LN02/Text/part0030.xhtml/p000282`: XHTML nhấn mạnh toàn đoạn; bản dịch không có dấu nghiêng. Đề xuất: bao toàn bộ bản dịch của đoạn bằng `*...*`, giữ nguyên đại từ thuộc nội tâm vị tư lệnh, không thêm dấu thoại.
- Self-check, cả gạch đầu dòng về nhấn mạnh lẫn hàng F01 và kết luận 11/11, đang báo hoàn tất trái với bản dịch hiện tại. Người giữ quyền sửa cần sửa hai vị trí rồi cập nhật self-check theo kết quả thật. Fixes handoff là hồ sơ tự báo, không thay thế đối chiếu trực tiếp.
- Đã xác nhận các vùng nhấn mạnh ở p000265, p000279, p000281 đúng phạm vi tương ứng. Không thấy chữ nghiêng thêm tại ID khác. Độ bất định của phần còn thiếu: thấp, có cấu trúc XHTML trực tiếp trong gói được giao.

## Đối chiếu F01–F11

Các hậu tố ID trong bảng đều thuộc `YS-LN02/Text/part0030.xhtml/`.

| Finding | Mức ban đầu | Kết quả | Căn cứ trong bản hiện tại |
|---|---|---|---|
| B09-F01 | Vừa | Còn mở | Thiếu nghiêng liên từ ở p000276 và toàn đoạn p000282; ba ID còn lại đã đúng. |
| B09-F02 | Vừa | Đã giải quyết | p000264 giữ cả tuyên bố và diễn giải trong hai điều kiện, không xác lập diễn giải như bước đã quyết định. |
| B09-F03 | Vừa | Đã giải quyết | p000265 dùng hành động cho nổ tung trong giả định; không tự thêm phương tiện ném bom; vùng giả định được nghiêng. |
| B09-F04 | Vừa | Đã giải quyết | p000279 dùng Huy hiệu Đột kích Cánh bạc, giữ loại vật phẩm và định danh theo lựa chọn tạm. |
| B09-F05 | Vừa | Đã giải quyết | p000279 nói về kiểu lính trẻ em như trong truyền thuyết; không biến lai lịch cá nhân thành truyền thuyết. |
| B09-F06 | Vừa | Đã giải quyết | p000274/p000276/p000278/p000279/p000281 dùng “nó” hoặc tên Tanya trong trần thuật. Thoại p000277 và nội tâm vị tư lệnh p000282 vẫn được xét riêng. |
| B09-F07 | Nhẹ | Đã giải quyết | p000276 giữ hình ảnh đôi mắt lạnh như vật vô tri, đồng thời giữ cảm xúc bộc lộ ở vế sau. |
| B09-F08 | Nhẹ | Đã giải quyết | p000274 giữ mức “rất xa lạ”, không thêm đối chiếu kỳ vọng. |
| B09-F09 | Nhẹ | Đã giải quyết | p000270 giữ sắc thái sĩ quan chỉ mang hàm thiếu tá, không đổi chức vụ tư lệnh quân đoàn. |
| B09-F10 | Nhẹ | Đã giải quyết | p000271 nói rõ đây mới chỉ là một khả năng và giữ tính giả định của việc nói với ông. |
| B09-F11 | Nhẹ | Đã giải quyết | p000258 tự quy chiếu bằng “mình”, không thêm dấu thoại. |

Không phát hiện finding độc lập mới trong 28 ID được giao. Lập luận pháp lý vẫn là diễn giải giả định của nhân vật; báo cáo không xác minh pháp luật ngoài tác phẩm.

## Thuật ngữ tạm

Fixes handoff yêu cầu mọi lựa chọn tiếp tục pending/non-canon; self-check hiện tại cũng ghi rõ điều đó. Bản dịch áp dụng nhất quán tám cụm được giao dưới đây. Việc chấp nhận tạm cách dịch không nâng chúng thành canon. Không đọc hay sửa ledger/canon ngoài đầu vào được phép, nên xác nhận này giới hạn ở hồ sơ b09.

| Vị trí | Giữ đề xuất tạm | Phương án khác / giới hạn |
|---|---|---|
| p000260 | luật chiến tranh | luật về chiến tranh; giữ mức khái quát, chưa chuẩn hóa chuyên ngành. |
| p000260/p000262, quan hệ ngữ cảnh p000264 | người không tham chiến | người không trực tiếp tham chiến; phương án sau thêm giới hạn chưa được gói xác lập. |
| p000259 | ngụy biện | lập luận ngụy biện; lựa chọn hiện tại giữ giọng mỉa mai. |
| p000264 | dân quân | thành viên lực lượng dân quân; không suy ra tổ chức cụ thể hoặc công nhận tư cách pháp lý. |
| p000277 | bộ chỉ huy khu vực | bộ tư lệnh khu vực; cấp tổ chức và tên riêng chưa xác nhận. Nhãn Area Command trong hồ sơ không thay từ thực tế của gói. |
| p000270/p000274 | tư lệnh quân đoàn | chỉ huy quân đoàn; không suy ra quân hàm từ chức vụ. |
| p000279 | Huy hiệu Đột kích Cánh bạc | Huy hiệu Xung kích Cánh bạc; giữ loại huy hiệu, tên tiếng Việt chính thức vẫn pending. |
| p000283/p000284 | dẹp yên thành phố / dẹp yên Arene | bình định; lựa chọn hiện tại tránh thêm hàm ý quản trị lâu dài. |

Ba lựa chọn ngoài b09 được self-check nhắc đến vẫn được ghi là pending/non-canon; không đối chiếu các đoạn ấy hoặc gói khác. Giữ các đề xuất về quân hàm, cơ quan ngoại giao và xưng hô theo hồ sơ được giao, không tạo quyết định canon mới.
