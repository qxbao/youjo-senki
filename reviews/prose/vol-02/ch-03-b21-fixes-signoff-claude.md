# Báo cáo ký duyệt sau sửa — vol-02-ch-03-b21

- Người phản biện: Claude (reviewer). Task: `vol-02-ch-03-b21-review-signoff`, checkpoint_generation 665 (khớp `work/run-state/translation-coordinator.yml`).
- Phạm vi: 31 đoạn p000380–p000410 của `YS-LN02/Text/part0018.xhtml`. Mã đoạn viết tắt `pNNNNNN`.
- Đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b21, báo cáo đầu `ch-03-b21-claude.md`, gói nguồn b21 đã chuẩn bị (local) và `translations/vol-02/ch-03-b21.jsonl`. Không mở EPUB/PDF, gói/bản dịch lô khác; không sửa gì ngoài báo cáo này. Mọi thuật ngữ vẫn là đề xuất, không canon.

## Kết luận

Cả 5 lỗi mức vừa trước đó đã được xử lý. Không còn lỗi nghiêm trọng hay vừa trong lô 31 đoạn. Còn một số lỗi nhẹ, không chặn đóng lô.

## Đếm theo mức (sau sửa)

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 0 |
| Nhẹ | 5 |

`prior_moderate_resolved: 5/5` — `unresolved_finding_ids: []` (không còn mã lỗi serious/moderate tồn đọng).

## Đối chiếu 5 lỗi vừa

| ID | Đoạn | Kết quả | Ghi chú |
|---|---|---|---|
| V1 | p000387 | Đã giải quyết | Nay là "định chỉ đi đến sát ranh giới của những gì có thể lách được trong khuôn khổ luật quốc tế"; hết mâu thuẫn "tuân thủ/lách", đúng nghĩa nguồn. |
| V2 | p000392 | Đã giải quyết | Bỏ "vội mừng quá sớm"; dùng "đã tính toán trước khi có kết quả: họ cho rằng…", trung tính, không thêm cảm xúc. Nguồn vốn mơ hồ nên giữ tạm. "các tuyến thứ ba" cũng đã bỏ "phòng thủ" (N8). |
| V3 | p000395 | Đã giải quyết | "Ông" nhất quán với Habergram ở các đoạn lân cận. Chủ thể vẫn là suy luận từ ngữ cảnh (đã đề nghị ghi pending). |
| V4 | p000404 | Đã giải quyết | Bỏ "tai tiếng"; dùng "một người độc đến thế", gần chữ nguồn, không gán phán xét. Còn hơi gượng (xem lỗi nhẹ). |
| V5 | p000404–405 | Đã giải quyết | "Văn phòng Bộ Hải quân" / "Đệ nhất Lãnh chúa Hải quân"; "có ở trong không" khớp p000408–410. Dùng nhất quán trong lô; vẫn là đề xuất pending. |

Các lỗi nhẹ N1, N4, N5, N6, N11 cũng đã sửa; N9 không còn xuất hiện ("cơ quan Tình báo" ở p000397). Kiểm tra lại: đủ 31 đoạn, đúng thứ tự, không thêm lỗi mới về nghĩa, phủ định, câu hỏi hay đại từ; không dùng `*...*` (nguồn không có nhấn mạnh).

## Lỗi nhẹ còn lại (không chặn)

- **p000382** — "cảm thấy rõ hơn bao giờ hết" thêm so sánh không có trong nguồn (N2). Gợi ý: "đang cảm nhận rất rõ".
- **p000384** — "Một người ở nơi khác" và "một trận ầm ĩ" hơi ngượng/khẩu ngữ (N3). Gợi ý: "Từ một phía khác"; "sẽ gây náo động lớn".
- **p000393** — "đang được bí mật đưa lên tàu" đổi trạng thái (đã nằm sẵn) thành hành động đang diễn ra (N7). Gợi ý: "đều nằm sẵn trên tàu, được giấu kín".
- **p000398** — "chính phủ tiền nhiệm có đủ thẩm quyền" hơi lệch sắc thái so với "chính phủ trước đó" (N10); tùy chọn.
- **p000404** — "một người độc đến thế" đọc gượng (hệ quả V4); tùy chọn đổi "một nhân vật gai góc như vậy". Độ bất định nghĩa nguồn ghi pending, không cần hỏi người dùng.

## Thuật ngữ pending (đều là đề xuất)

Không có thuật ngữ mới ảnh hưởng cốt truyện. Cặp Office of the Admiralty / First Lord of the Admiralty (p000404–405), "các tuyến thứ ba" (p000392), chủ thể p000395 và nghĩa "toxic" (p000404) nên được coordinator ghi/cập nhật trong ledger `work/run-state/pending-terms.yml` với độ bất định đã nêu; không tự nâng thành canon.

```yaml
role: reviewer
task_id: vol-02-ch-03-b21-review-signoff
state: done
segment_ids:
  - YS-LN02/Text/part0018.xhtml/p000380..p000410
review_path: reviews/prose/vol-02/ch-03-b21-fixes-signoff-claude.md
files_written:
  - reviews/prose/vol-02/ch-03-b21-fixes-signoff-claude.md
validator: not_run
diff_check: not_run
counts:
  serious: 0
  moderate: 0
  minor: 5
prior_moderate_resolved: true  # 5/5 (V1-V5)
unresolved_findings: []
unresolved_serious_or_moderate: 0
findings:
  - {severity: minor, segment_id: YS-LN02/Text/part0018.xhtml/p000382, issue: "so sánh 'hơn bao giờ hết' không có trong nguồn", resolution: "tùy chọn: 'cảm nhận rất rõ'"}
  - {severity: minor, segment_id: YS-LN02/Text/part0018.xhtml/p000384, issue: "'Một người ở nơi khác', 'trận ầm ĩ' hơi ngượng", resolution: "tùy chọn"}
  - {severity: minor, segment_id: YS-LN02/Text/part0018.xhtml/p000393, issue: "trạng thái đã nằm trên tàu bị đổi thành hành động đang diễn ra", resolution: "tùy chọn"}
  - {severity: minor, segment_id: YS-LN02/Text/part0018.xhtml/p000398, issue: "'tiền nhiệm' lệch nhẹ sắc thái", resolution: "tùy chọn"}
  - {severity: minor, segment_id: YS-LN02/Text/part0018.xhtml/p000404, issue: "'người độc đến thế' đọc gượng; nghĩa nguồn bất định", resolution: "tùy chọn; ghi pending"}
term_recommendations:
  - {source_term: "Office of the Admiralty / First Lord of the Admiralty", proposed_vi: "Văn phòng Bộ Hải quân / Đệ nhất Lãnh chúa Hải quân", segment_ids: [p000404, p000405], status: pending, non_canon: true}
  - {source_term: third lines, proposed_vi: "các tuyến thứ ba", segment_ids: [p000392], status: pending, non_canon: true}
  - {source_term: "toxic", proposed_vi: "người độc đến thế", segment_ids: [p000404], status: pending, non_canon: true, uncertainty: high}
risks:
  - "chủ thể 'He' ở p000395 là suy luận ngữ cảnh (Habergram); ghi pending"
commit: null
next_action: coordinator_may_close_batch
```
