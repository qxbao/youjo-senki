# Signoff vol-02-ch-04-b17 (Claude)

Phạm vi: 26 đoạn `YS-LN02/Text/part0024.xhtml/p000173`–`p000198`. `pNNNNNN` viết tắt mã đoạn đầy đủ. Người phản biện không sửa bản dịch, canon, handoff, ledger hay checkpoint. Mọi lựa chọn thuật ngữ dưới đây là đề xuất tạm, không phải canon.

Đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b17, gói nguồn b17, mục `chapter4_b17_translation_proposals`, báo cáo review ban đầu `reviews/prose/vol-02/ch-04-b17-claude.md`, bản dịch hiện tại `translations/vol-02/ch-04-b17.jsonl` (26 dòng, đủ mã, đúng thứ tự, `notes` rỗng). Không đọc lô/gói khác, không mở EPUB/PDF. Không tính lại SHA gói (validator: not_run).

## Kết luận

Không còn lỗi nghiêm trọng hoặc vừa. V1 đã xử lý. Lô đủ điều kiện signoff về mặt review; phần validator/commit do coordinator.

## V1 — đã xử lý

- p000175, p000176, p000179, p000180: thuyền trưởng nhất quán là "ông" (p000177 dùng danh từ "thuyền trưởng", đúng nguồn). Không còn "anh ta"/"anh" cho thuyền trưởng.
- p000182: mở đầu bằng "Sĩ quan phó tỉnh lại…", nêu rõ chủ thể là sĩ quan phó, tách khỏi thuyền trưởng (nhắc ở ngôi thứ ba ngay sau đó). "anh" ở câu kế tiếp bám vào chủ ngữ "Sĩ quan phó", không còn mơ hồ.
- p000183–p000192: "anh" nhất quán chỉ sĩ quan phó; thuyền trưởng bất tỉnh không bị lẫn.
- Không phát sinh lỗi mới do bản sửa; giữ nhấn mạnh `*Mình phải cử động.*` ở p000180 đúng phạm vi nguồn (DEC-P01-002).

## Số lượng theo mức

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 0 |
| Nhẹ | 9 (không chặn, chưa sửa) |

## Lỗi nhẹ còn lại (tùy chọn, không chặn)

Giữ nguyên đề xuất ở báo cáo đầu: N1 p000173, N2 p000178, N3 p000180 (ghi nhận), N4 p000183, N5 p000185, N6 p000190, N7 p000192, N8 p000193, N9 p000196.

## Thuật ngữ (đề xuất tạm, status pending)

- technical officer → "sĩ quan kỹ thuật" (p000187, p000189, p000190, p000192): chấp nhận tạm, dùng nhất quán; thay thế "sĩ quan phụ trách kỹ thuật". Không ảnh hưởng cốt truyện cần hỏi người dùng.
- Foreign Strategy Division → "Cục Chiến lược Đối ngoại" (p000195): chấp nhận tạm; thay thế "Ban Chiến lược Đối ngoại". Không ảnh hưởng cốt truyện cần hỏi người dùng.

## Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-04-b17-review-signoff
state: done
segment_ids: [YS-LN02/Text/part0024.xhtml/p000173, YS-LN02/Text/part0024.xhtml/p000198]
review_path: reviews/prose/vol-02/ch-04-b17-fixes-signoff-claude.md
files_written:
  - reviews/prose/vol-02/ch-04-b17-fixes-signoff-claude.md
counts: {serious: 0, moderate: 0, minor: 9}
v1_status: resolved
prior_moderate_resolved: true
unresolved_findings: []  # không còn serious/moderate
optional_minor_segments: [p000173, p000178, p000180, p000183, p000185, p000190, p000192, p000193, p000196]
term_recommendations:
  - {source_term: technical officer, proposed_vi: "sĩ quan kỹ thuật", action: accept_provisional, status: pending}
  - {source_term: Foreign Strategy Division, proposed_vi: "Cục Chiến lược Đối ngoại", action: accept_provisional, status: pending}
validator: not_run
diff_check: not_run
commit: null
next_action: signoff
```
