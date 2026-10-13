# Signoff sau sửa — vol-02-ch-04-b20

- Phạm vi: p000250–p000277; chỉ kiểm M1–M3 và các sửa nhất quán nằm trong lô.
- Đã đọc: shared/reviewer, config, handoff b20, source package b20, canon tham chiếu, mục `chapter4_b20_translation_proposals`, báo cáo gốc, bản dịch hiện tại. Không đọc lô khác.
- Không sửa gì ngoài báo cáo này. Validator/diff_check: not_run. Commit: null.

## Kết quả M1–M3

- **M1 (p000257): đạt.** Câu mở nay là “Tin xấu mà người ta phải đánh thức Tướng Habergram dậy để báo suýt khiến ông bóp nát chiếc tẩu trong tay.” Rõ ràng tin xấu buộc phải đánh thức ông và suýt làm ông bóp nát tẩu; hết chuỗi “khiến… phải… đủ làm”. Đã dùng “Tướng Habergram” (L5 xong).
- **M2 (p000258): đạt.** “Bridge” → “đài chỉ huy”, đối lập với “khu sinh hoạt”; khớp ledger `vol02-ch04-b20-bridge`.
- **M3 (p000261): đạt.** Câu nay hỏi xác suất kẻ địch “đụng phải một tàu phụ trợ và tàu ngầm của Khối Thịnh vượng chung” và kết bằng “nhỏ đến mức thiên văn”; giữ đúng ý xác suất cực nhỏ. “Tàu phụ trợ” thay “tàu tiếp tế”, khớp ledger `vol02-ch04-b20-auxiliary-ship`. Cuối câu “thiên văn nào chứ?” hơi gượng nhưng không sai nghĩa; chỉ là lưu ý nhẹ, không cần sửa.

## Sửa nhất quán trong phạm vi

- p000273: “chúng đã thoát mất” — đạt.
- p000277: “có tiếp xúc với họ” — đạt, không còn “chạm trán”.
- p000240, p000245 nằm ngoài lô b20 (không có trong package/bản dịch này); handoff ghi unchanged — không xét.

## Còn lại

- Nghiêm trọng: 0. Vừa: 0. Nhẹ: các mục L4, L6–L10 chỉ ghi nhận như handoff; không chặn.

```yaml
role: reviewer
task_id: vol-02-ch-04-b20-fixes-signoff
state: done
review_path: reviews/prose/vol-02/ch-04-b20-fixes-signoff-claude.md
counts: {serious: 0, moderate: 0, minor: 0}
M1: resolved
M2: resolved
M3: resolved
unresolved_findings: []
term_recommendations:
  - {source: bridge, vi: đài chỉ huy, status: pending, note: giữ, không canon}
  - {source: auxiliary ship, vi: tàu phụ trợ, status: pending, note: giữ, không canon}
validator: not_run
diff_check: not_run
commit: null
next_action: signoff
```
