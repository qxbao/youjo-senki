# Signoff vol-02-ch-04-b15 (Claude, sau sửa M1–M3)

- Phạm vi: `p000111`–`p000140` (30 đoạn), source package đúng handoff, `translations/vol-02/ch-04-b15.jsonl` sau sửa; đối chiếu `pending-terms.yml#chapter4_b15_translation_proposals` và báo cáo review gốc. Không đọc lô khác.
- Kết quả: **0 nghiêm trọng, 0 vừa**; còn 4 nhẹ (L3, L4 ghi nhận từ báo cáo gốc; L1 phần "Frau" còn lại; không chặn signoff).

## Kiểm tra các mục đã sửa

| Mục | Kết quả | Chi tiết |
|---|---|---|
| M1 công thức | Đạt | p000127 "thuật thức bắn tỉa"; p000133, p000140 "thuật thức nổ mạnh". Khớp ledger, không còn "phép thức". |
| M2 depth charge | Đạt | p000133, p000134 đều "mìn sâu", khớp ledger b10/b12 (đề xuất, không phải canon). |
| M3 phạm vi nghiêng | Đạt | p000114 `*Lại có thêm việc phải làm sao?*` (nguồn `<em>` chỉ bao câu nội tâm, không bao "Tanya than thầm"); p000123 `*Bùn lầy sâu đến đâu thì có thật sự quan trọng không?*` (em bao đúng câu hỏi, không bao phần "thỏa hiệp…"). Đúng DEC-P01-002. |
| L1 nhấn mạnh tên | Đạt | p000118 `*Lytol*`, p000137 `*Jawohl*`, phạm vi khớp `<em>` nguồn. Không có nghiêng thừa ở đoạn khác (nguồn chỉ có 4 đoạn có `<em>`). |
| L2 đại từ | Đạt | p000111–p000113 dùng "tôi" cho người kể không phải Tanya; không mở rộng "mình" của DEC-P01-001. Tanya vẫn "nó" (trần thuật: p000114, p000117) và "mình" (nội tâm). Ledger đã có mục `vol02-ch04-b15-other-narrator-pronoun` (độ tin cậy 0.5). |

Không thấy hồi quy nghĩa/logic pháp lý (lặn ≠ từ chối kiểm tra; bắn cảnh cáo, không bắn trúng trực tiếp), không thiếu/thừa đoạn, chú thích ¹⁵ giữ nguyên.

## Còn lại (nhẹ, không chặn)

- L1 (phần còn lại) — p000137: "Frau" không được dịch ("thưa Thiếu tá"); mất sắc thái Đức, không sai nghĩa. Tùy chọn: "*Jawohl*, Frau Major!" nếu coordinator muốn giữ.
- L3 — p000113: "Hẳn họ không phải chẳng có quan hệ gì với nhau" nặng; gợi ý "Không thể nào họ không liên quan."
- L4 — p000117: "tình hình vẫn tiếp diễn" → "vẫn đang diễn biến".

## Thuật ngữ (đề xuất, không phải canon)

thuật thức bắn tỉa; thuật thức nổ mạnh; mìn sâu (đổi "bom chìm" chỉ nếu đổi đồng loạt b10/b12/b15 và ledger); tàu của Khối Thịnh vượng chung; "tôi" cho người kể khác Tanya (p000111–p000113). Không mục nào ảnh hưởng cốt truyện.

## Kết luận

Không còn lỗi nghiêm trọng/vừa; có thể signoff. Validator/diff_check: not_run (do coordinator chạy).

```yaml
role: reviewer
task_id: vol-02-ch-04-b15
state: done
segment_ids: [YS-LN02/Text/part0024.xhtml/p000111, YS-LN02/Text/part0024.xhtml/p000140]
files_written: [reviews/prose/vol-02/ch-04-b15-fixes-signoff-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 0, minor: 3}
findings:
- {id: M1, severity: moderate, status: resolved}
- {id: M2, severity: moderate, status: resolved}
- {id: M3, severity: moderate, status: resolved}
- {id: L1, severity: minor, status: resolved_except_Frau_optional}
- {id: L2, severity: minor, status: resolved}
- {id: L3, severity: minor, status: open_recorded_only}
- {id: L4, severity: minor, status: open_recorded_only}
unresolved_findings: []  # chỉ còn L3, L4 và "Frau" ở L1 (nhẹ, không chặn)
term_recommendations:
- {source_term: sniping formulas, proposed_vi: thuật thức bắn tỉa, status: pending}
- {source_term: heavy explosion formulas, proposed_vi: thuật thức nổ mạnh, status: pending}
- {source_term: depth charge, proposed_vi: mìn sâu, status: pending}
- {source_term: Commonwealth vessel, proposed_vi: tàu của Khối Thịnh vượng chung, status: pending}
- {source_term: first-person narrator other than Tanya, proposed_vi: tôi, status: pending}
review_path: reviews/prose/vol-02/ch-04-b15-fixes-signoff-claude.md
commit: null
next_action: signoff
```
