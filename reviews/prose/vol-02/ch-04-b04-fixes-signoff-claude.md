# Signoff sau sửa — vol-02-ch-04-b04 (Claude)

- Task: `vol-02-ch-04-b04-review-signoff`; checkpoint_generation: 719; phạm vi: 33 đoạn `p000063`–`p000095` (part0022.xhtml).
- Đã đọc: shared.md, reviewer.md, config/translation-pipeline.yml, handoff b04, báo cáo review ban đầu (`ch-04-b04-claude.md`), gói nguồn b04 (hash khớp handoff theo báo cáo đầu; không tính lại), và chỉ `translations/vol-02/ch-04-b04.jsonl`.
- Không mở EPUB/PDF hay gói nguồn/bản dịch khác; không sửa bản dịch, handoff, ledger, canon, run-state. Báo cáo không trích câu nguồn. Mọi thuật ngữ vẫn là đề xuất tạm, không phải canon.
- Kỹ thuật: 33/33 mã đoạn, đúng thứ tự, status `draft`, `notes` rỗng. Chữ nghiêng p000090–p000091 vẫn đúng DEC-P01-002.

## Số lượng sau sửa

| Mức | Còn lại trong b04 |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 0 |
| Nhẹ | 15 (mang từ báo cáo đầu, chưa sửa, không chặn; N15 đã được giải quyết nhờ sửa p000092) |

`prior_moderate_resolved: 6/6 trong phạm vi b04` (xem lưu ý phạm vi bên dưới về cách đánh số M6).

## Kiểm tra từng lỗi vừa

| ID báo cáo | Đoạn | Kết quả |
|---|---|---|
| M1 | p000074 | Đã sửa: "vì người gặp chuyện không phải là họ"; không còn "mình" chỉ nhầm Tanya, đối tượng câu hỏi đã đúng. |
| M2 | p000078 | Đã sửa: "lính phục vụ" khớp ledger; "xe … cấp dưới ngồi sau tay lái đã chờ sẵn" phục hồi chi tiết xe chờ/người lái. Còn "chu đáo" lặp hai lần (N10, nhẹ). |
| M3 | p000087 | Đã sửa: "mọi người đang nghỉ phép nửa ngày" đúng phạm vi. |
| M4 | p000092 | Đã sửa: "Cục Tác chiến" khớp ledger; "đích thân có mặt ở Norden" đặt đúng chỗ nhấn; "chỉ định riêng nó" thay "đích thân chọn". |
| M5 | p000093 | Đã sửa: "Hạm đội Biển Bắc" khớp ledger b04 (pending, độ tin thấp). |
| M6 | p000079 | Đã sửa: cả hai câu dùng "nó", đúng trần thuật ngôi ba theo DEC-P01-001. |

Không phát sinh lỗi vừa/nghiêm trọng mới do các chỉnh sửa; đã đọc lại toàn bộ p000063–p000095 và không thấy đảo phủ định, mất ý, đổi đối tượng, hay lệch thuật ngữ ledger nào ở mức vừa trở lên. Trong b04, "mình" nội tâm (p000065, 066, 071, 083, 085, 088, 095) và "nó" trần thuật nhất quán.

## Chênh lệch phạm vi (nêu rõ)

1. **Đánh số M6 không khớp giữa handoff và báo cáo.** Báo cáo review ban đầu có M6 = p000079 (đại từ trần thuật). Handoff liệt kê `unresolved_findings` thứ sáu là "p000045+p000046+p000051+p000053 dùng 'mình' nhất quán trong nội tâm Tanya", và `risk_notes` gắn nhãn M6 cho p000045–p000053. Mục này **không có trong báo cáo review b04** mà tôi đọc và nằm ngoài p000063–p000095. Translator đã sửa p000079 (trong phạm vi) và bỏ qua p000045/046/051/053 (đúng quyền hạn). Với b04, M6 thực tế của báo cáo (p000079) đã xong; mục p000045–p000053 không phải yêu cầu sửa của b04 và tôi không đánh giá được vì không đọc bản dịch ngoài phạm vi. Coordinator nên đối chiếu nguồn gốc mục này (có thể từ review khác) và xử lý ở batch/task sở hữu các đoạn đó.
2. **p000392 (ngữ cảnh ngoài phạm vi).** Không thuộc handoff b04 nên không phải yêu cầu sửa của b04 và không được tính vào số lượng. Tôi không đọc được đoạn này (ngoài `ch-04-b04.jsonl`), nên **không xác minh được** ngữ cảnh p000392; không có căn cứ để kết luận gì về nó. Nếu cần kiểm tra, giao cho review của batch chứa đoạn đó.
3. Handoff ghi "2 ghi chú thuật ngữ mức nhẹ" của translator nhưng `notes` JSONL rỗng ở mọi đoạn (đã nêu ở báo cáo đầu, không đổi).

## unresolved_ids trong b04

Không có (serious/moderate). Các mục nhẹ còn lại (N1–N14, N16) là tùy chọn, không chặn hoàn tất; đáng chú ý nhất là N10 (p000078, "chu đáo" lặp), N12 (p000082, "thưa Thiếu tá" so với ledger "thưa chỉ huy"), N13 (p000083, "chạy nhanh" thêm ý), N7 (p000073, "cô" cạnh "Thiếu tá").

## Báo cáo coordinator

```yaml
role: reviewer
task_id: vol-02-ch-04-b04-review-signoff
state: done
segment_ids:
  - YS-LN02/Text/part0022.xhtml/p000063..p000095
files_written:
  - reviews/prose/vol-02/ch-04-b04-fixes-signoff-claude.md
validator: not_run
diff_check: not_run
findings: []   # không còn lỗi nghiêm trọng/vừa trong b04
review_path: reviews/prose/vol-02/ch-04-b04-fixes-signoff-claude.md
counts: {serious: 0, moderate: 0, light: 15}
prior_moderate_resolved: true   # 6/6 trong phạm vi b04 (M1-M5 và p000079)
unresolved_findings: []
scope_discrepancies:
  - "handoff gắn M6 cho p000045/046/051/053 (ngoài b04, không có trong báo cáo review b04); báo cáo ghi M6 = p000079, đã sửa"
  - "p000392 ngoài phạm vi b04; không đọc, không xác minh, không tính"
  - "notes JSONL rỗng dù handoff nhắc 2 ghi chú thuật ngữ nhẹ"
term_recommendations: []   # giữ nguyên các đề xuất tạm của báo cáo đầu; tất cả pending, không canon
risks:
  - "Mục p000045-p000053 (mình nhất quán) cần được xử lý hoặc xác nhận ở task sở hữu các đoạn đó, không thuộc b04"
commit: null
next_action: coordinator_may_mark_b04_review_resolved
```
