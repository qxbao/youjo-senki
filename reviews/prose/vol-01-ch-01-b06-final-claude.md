# Báo cáo phản biện cuối — vol-01-ch-01-b06

- Task: `vol-01-ch-01-b06-final-review` (reviewer: Claude).
- Phạm vi: p000089, p000091, p000078, p000088, p000099, p000100 của `YS-LN01/Text/chapter003b.xhtml` (viết tắt `pNNNNNN`), cùng p000090 làm ngữ cảnh.
- Đã đối chiếu: source package cục bộ `work/vol-01/batches/ch-01-b06-source.jsonl`, `translations/vol-01/ch-01-b06.jsonl`, báo cáo tiếp theo trước, `work/run-state/pending-terms.yml`, checkpoint coordinator.
- Toàn vẹn: `source_sha256` của cả 6 đoạn khớp package; `status: draft`. Không chép câu nguồn vào báo cáo; thuật ngữ chỉ là đề xuất, không canon.
- Validator/diff_check: not_run. Commit: null.

## 1. Kết luận

**M3 đã được xử lý hoàn toàn, cả ở văn bản lẫn ghi chú.** Không còn lỗi nghiêm trọng hay vừa trong phạm vi. Không có quyết định canon ảnh hưởng cốt truyện cần hỏi người dùng.

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 0 |
| Nhẹ | 2 (không chặn) |

## 2. Đối chiếu trực tiếp với nguồn

- **p000089 — ĐẠT.** Danh từ "dominion" ở câu cuối được dịch "quyền cai trị" (trong cụm "yêu sách về quyền cai trị của Liên minh Entente"); không còn "chủ quyền" trong bản dịch đoạn này. Cấu trúc câu giữ đúng: hiệp ước chỉ tạm thời thể hiện sự tôn trọng đối với tuyên bố của hai bên, vì nể yêu sách của Entente; chủ thể bên "nể" không được suy thêm. Hai câu đầu sát nguồn: điều khoản chỉ vừa đủ chấp nhận, Khối Thịnh vượng chung làm trung gian, khu phi quân sự tạm thời thực chất là biên giới quốc gia, quyền quản lý khu vực làm vật bảo đảm. Lỗi lặp "bảo đảm" (n1 báo cáo trước) đã hết: nay là "vật bảo đảm để… được duy trì".
- **p000091 — ĐẠT.** "Sovereignty" vẫn là "chủ quyền" ("thuộc chủ quyền của Liên minh Entente"). Phân biệt với p000089 được giữ. Các sắc thái đã sửa trước đó (hão huyền, cay cú, thèm coi trọng) còn nguyên; ý mỉa mai và sự đối lập trong nước/quốc tế đúng nguồn.
- **p000078 — ĐẠT.** Giữ ý "được báo thông tin khác với thực tế"; không biến thành "hoàn toàn không được báo".
- **p000088 — ĐẠT.** Hai ý phê phán (tiếp tục khơi chủ nghĩa dân tộc; không chịu đối diện thực tế) giữ riêng; sắc thái chửi rủa giữ.
- **p000099 — ĐẠT.** "Kênh liên lạc" cho đường dây rối; ý "chưa được phân đúng tần số" nêu riêng.
- **p000100 — ĐẠT.** "Kỳ cựu" chỉ còn một lần (câu sau là "lão luyện"), lặp đã hết. Không dịch Cunningham thành cựu binh sai ngữ cảnh.

## 3. Kiểm tra ghi chú đoạn

- **p000089:** ghi chú nêu đúng `b06-dominion` (quyền cai trị; phương án khác quyền cai quản) và giữ "chủ quyền" cho sovereignty ở p000091 — **khớp văn bản thực tế**. Ghi chú thứ hai ("giảm lặp từ, giữ vai trò bảo chứng, không xác định thêm chủ thể") cũng khớp. Ledger `b06-dominion` (đề xuất quyền cai trị; thay thế quyền thống trị/quyền cai quản, pending) và `recovery_summary` của checkpoint nhất quán với văn bản.
- **p000078, p000088, p000091, p000099:** đã có ghi chú mới (trước đây rỗng), mô tả đúng nội dung bản dịch, không chứa câu nguồn. p000091 có thêm ghi chú sovereignty pending, khớp ledger (độ tin cậy 0,75).
- **Không chép nguồn:** ghi chú các đoạn trên chỉ dùng thuật ngữ ngắn và mã đoạn; không có câu nguồn tiếng Anh. Báo cáo này cũng không chứa câu nguồn.

## 4. Phát hiện mức nhẹ (không chặn)

- **n1 — ledger.** Mục `sovereignty` (dòng ~1632 `pending-terms.yml`) thiếu `id`, khác định dạng `b06-*` của mục `b06-dominion`. Nên coordinator thêm id để tránh nhầm khi tổng hợp. Reviewer không sửa ledger.
- **n2 — p000100.** "Ông" dành cho Sue vẫn ngầm suy tuổi/giới tính ở mức đã ghi nhận trước (đề xuất tạm trong ledger); chấp nhận được.
- Các mục ledger trùng ID `b06-pseudo-border` và lệch `combat-direction-center`/`airspace-control` (n2, n3 của báo cáo trước) nằm ngoài sáu đoạn được giao nên **không kiểm tra lại ở đây**; coordinator nên tự xác nhận đã làm sạch.

## 5. Khuyến nghị thuật ngữ (đề xuất, không canon)

| Thuật ngữ | Hiện tại | Khuyến nghị | Tin cậy |
|---|---|---|---|
| dominion (p000089) | quyền cai trị | Giữ; thay thế: quyền cai quản/thống trị | 0,6 |
| sovereignty (p000091) | chủ quyền | Giữ, thêm id ledger | 0,75 |

## 6. Rủi ro còn lại

- Validator và diff_check chưa chạy trong task này (not_run); coordinator xác nhận kết quả riêng.
- Mục ledger ngoài phạm vi (xem n1 và dòng cuối mục 4) cần coordinator rà soát.

## 7. YAML báo cáo

```yaml
role: reviewer
task_id: vol-01-ch-01-b06-final-review
state: done
segment_ids:
  - YS-LN01/Text/chapter003b.xhtml/p000089
  - YS-LN01/Text/chapter003b.xhtml/p000091
  - YS-LN01/Text/chapter003b.xhtml/p000078
  - YS-LN01/Text/chapter003b.xhtml/p000088
  - YS-LN01/Text/chapter003b.xhtml/p000099
  - YS-LN01/Text/chapter003b.xhtml/p000100
files_written:
  - reviews/prose/vol-01-ch-01-b06-final-claude.md
review_path: reviews/prose/vol-01-ch-01-b06-final-claude.md
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 0, minor: 2}
unresolved_findings:
  - {severity: minor, segment_id: ledger, issue: "mục sovereignty thiếu id", resolution: coordinator thêm id}
  - {severity: minor, segment_id: p000100, issue: "'ông' ngầm suy tuổi/giới", resolution: chấp nhận, đề xuất tạm}
resolved_findings: [M3, n1 p000089, n7 p000100, n4 notes p000078/p000088/p000091/p000099]
term_recommendations: xem mục 5
risks: xem mục 6
commit: null
next_action: coordinator xác nhận validator/diff_check rồi commit lô
```
