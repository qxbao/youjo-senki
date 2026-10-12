# Báo cáo signoff sửa lỗi — vol-02-ch-02-b15-final-signoff (Claude)

- Task: `vol-02-ch-02-b15-final-signoff`; checkpoint_generation 403; vai trò: reviewer.
- Phạm vi: 25 đoạn `YS-LN02/Text/part0014.xhtml/p000392`–`p000416`; trọng tâm F01, F02 (mức vừa) và F11 (nhẹ, liên quan) ở `p000393`–`p000396`, `p000401`, `p000414`, `p000416`.
- Đầu vào đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b15 (gồm metadata `translator_followup`), gói nguồn b15, `translations/vol-02/ch-02-b15.jsonl`, báo cáo đầu `ch-02-b15-claude.md`, mục ledger `chapter2_b15_translation_proposals`. Báo cáo chi tiết của translator không có ngoài metadata handoff nên đối chiếu trực tiếp bản dịch hiện tại. Không đọc nguồn hay bản dịch của lô khác.

## Kiểm tra cấu trúc
- SHA-256 gói nguồn = `8828a7b9…1d7`, khớp handoff.
- 25/25 dòng JSONL: `segment_id` đúng thứ tự và trùng gói nguồn, `source_sha256` từng đoạn khớp, `glossary_version` khớp handoff, đủ bộ khóa (`translation`, `segment_id`, `source_sha256`, `glossary_version`, `status`, `translator`, `notes`), không thiếu/thừa đoạn.
- Nhấn mạnh (DEC-P01-002): nguồn chỉ có một vùng nhấn mạnh (`p000408`); bản dịch có đúng một cặp `*...*` ở đoạn này, không có `*` ở đoạn khác. Đạt.

## Xác minh từng sửa lỗi
**F01 — "Control": ĐÃ XỬ LÝ.**
- `p000393`: giữ "Norden Control"; câu sau dùng "Control" rút gọn. `p000394`: "không có Control". `p000395`: "Control địch". Dạng rút gọn nay nhất quán, liên kết được với Norden Control và khớp đề xuất ledger `control-short-form`.
- `p000396`: "hệ thống chỉ huy" (cho command scheme) và `p000400`: "bộ chỉ huy địch" (chữ thường, nghĩa chung) được giữ đúng như đề xuất ban đầu; `p000397`–`p000398`: "CP" giữ nguyên. Các khái niệm nguồn khác nhau không còn bị dồn vào "Bộ chỉ huy" viết hoa.

**F02 — đại từ/tự xưng (DEC-P01-001): ĐÃ XỬ LÝ.**
- `p000396`: "cô" đã đổi thành "người đó" (trung tính). Chấp nhận: chủ thể "she" chưa xác nhận trong lô nên không suy diễn; khớp ledger `uncertain-she-reference` (phương án thay thế "nó" nếu xác nhận là Tanya). Không còn "cô ấy/cô" gán quan hệ.
- `p000401` và `p000414`: nay dùng "mình" (nội tâm Tanya), thống nhất với `p000402`–`p000403`, `p000407`–`p000412`, `p000416`. Các đoạn thoại (`p000395`, `p000398`, `p000406`, `p000413`, `p000415`) giữ "tôi/ta" như cũ, đúng.

**F11 — viết hoa đơn vị: ĐÃ XỬ LÝ.** `p000416` nay là "Cụm tập đoàn quân phương Bắc" (loại đơn vị viết thường), khớp đề xuất ledger `northern-army-group`.

## Mục nhẹ còn lại (không chặn)
F03–F10, F12 của báo cáo đầu chưa được yêu cầu sửa và vẫn mở ở mức nhẹ (ví dụ "thô bạo" ở `p000393`, "ném bom" ở `p000396`, "họ" chỉ địch ở `p000399`/`p000414`, vocative "các anh" ở `p000398`, "quý ông" ở `p000415`, "gọng kìm" làm động từ ở `p000413`, "tội ác" ở `p000410`). Không có mục nào làm đổi nghĩa lớn; sửa tùy chọn khi thuận tiện.

## Kết luận
- Lỗi nghiêm trọng còn mở: 0. Lỗi vừa còn mở: 0. Không có yếu tố ảnh hưởng cốt truyện cần hỏi người dùng.
- Tất cả đề xuất thuật ngữ vẫn là tạm, không nâng canon.

```yaml
role: reviewer
task_id: vol-02-ch-02-b15-final-signoff
state: done
segment_ids: [p000393, p000394, p000395, p000396, p000401, p000414, p000416]
files_written:
  - reviews/prose/vol-02/ch-02-b15-fixes-signoff-claude.md
validator: not_run
diff_check: not_run
review_path: reviews/prose/vol-02/ch-02-b15-fixes-signoff-claude.md
finding_counts:
  serious: 0
  moderate: 0
  minor: 9
unresolved_findings: []  # không còn serious/moderate; 9 mục nhẹ (F03–F10, F12) tùy chọn
term_recommendations:
  - {source_term: Norden Control, proposed_vi: Norden Control, status: pending}
  - {source_term: Control (short form), proposed_vi: Control, status: pending}
  - {source_term: Northern Army Group, proposed_vi: Cụm tập đoàn quân phương Bắc, status: pending}
  - {source_term: she (referent uncertain), proposed_vi: người đó, status: pending}
  - {source_term: first-person interior narration, proposed_vi: mình, status: pending}
risks: []
commit: null
next_action: coordinator_complete_batch
```
