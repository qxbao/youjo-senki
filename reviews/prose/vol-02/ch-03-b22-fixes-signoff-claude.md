# Báo cáo signoff sau sửa — vol-02-ch-03-b22

- Người phản biện: Claude (reviewer). Task: `vol-02-ch-03-b22-review-signoff`. Checkpoint_generation: 675.
- Phạm vi: 28 đoạn từ `YS-LN02/Text/part0018.xhtml/p000411` đến `p000438`.
- Đã đọc: shared.md, reviewer.md, config, handoff b22, báo cáo review ban đầu (`reviews/prose/vol-02/ch-03-b22-claude.md`), gói nguồn b22 (sha256 `8622c372…176312c`, khớp handoff) và `translations/vol-02/ch-03-b22.jsonl`.
- Không mở EPUB/PDF, không đọc gói nguồn hay bản dịch của lô khác. Không sửa bản dịch, handoff, ledger, canon hay run-state. Báo cáo không trích câu nguồn.
- Mọi lựa chọn dưới đây chỉ là đề xuất tạm, không phải canon.

## 1. Kiểm tra toàn vẹn

- JSONL có đúng 28 dòng, mã đoạn khớp 28/28 với gói nguồn, không thiếu/thừa/trùng.
- `source_sha256` và `glossary_version` ở mọi dòng khớp handoff.
- Dấu nhấn mạnh `*Lytol*` chỉ ở p000420, p000428, p000432, p000433, đúng bốn đoạn như báo cáo đầu; không có dấu thừa (DEC-P01-002).

## 2. Đối chiếu năm lỗi mức vừa trước đó

| ID | Đoạn | Kết quả | Ghi chú |
|---|---|---|---|
| V1 | p000412 | Đã xử lý | Bỏ "Thưa/ngài", dùng "Tướng … ông": hướng xưng hô đúng thứ bậc, khớp p000413–p000414. |
| V2 | p000428 | Đã xử lý | Tốc độ là "hải lý/giờ", đúng đơn vị. |
| V3 | p000430 | Đã xử lý | "Bị phát hiện" thay cho sắc thái bắt quả tang; "được canh giữ cẩn thận" trung tính; chủ thể "phía tàu" rõ. Còn "người tị nạn" theo đề xuất tạm cũ. |
| V4 | p000431 | Đã xử lý | "Đội lên tàu khám xét" đúng thuật ngữ, khớp "khám xét" ở p000429; "giao chiến" giữ đúng cường độ. |
| V5 | p000434 | Đã xử lý | Cụm chỉ nơi chuyển giao nay là "ngay trên mặt nước"; không còn thêm trạng thái "đang hoạt động" của tàu ngầm, không mâu thuẫn với p000437. Còn một độ mơ hồ nhỏ về phạm vi bổ nghĩa, trùng mức mơ hồ của nguồn, không tính lỗi. |

prior_moderate_resolved: 5/5 (V1, V2, V3, V4, V5).

## 3. Phát hiện còn lại

- Nghiêm trọng: 0.
- Vừa: 0. Không phát sinh lỗi vừa mới sau khi sửa; các đoạn đã sửa không gây sai lệch với đoạn liền kề.
- Nhẹ: 10 mục cũ, không bắt buộc sửa và không chặn hoàn tất lô (p000413, p000415, p000416, p000417/p000419, p000419, p000426, p000428 "vòi nước", p000431 câu thành ngữ làm nhã, p000432 "vượt được", lặp "Dù sao thì" ở p000415/p000421/p000429/p000438). Chi tiết giữ nguyên ở báo cáo ban đầu.

unresolved_findings: [] (không còn mã lỗi nghiêm trọng hoặc vừa chưa xử lý).

## 4. Thuật ngữ pending (đề xuất tạm, không canon)

Không phát sinh thuật ngữ mới. Các lựa chọn hiện dùng là đề xuất tạm, áp dụng nhất quán: "Tướng" (General, p000412), "Đệ nhất Lãnh chúa Hải quân" / "Văn phòng Bộ Hải quân", "nghị viên" (councilor), "xin tị nạn" / "người tị nạn". Không ảnh hưởng cốt truyện; không cần hỏi người dùng.

## 5. YAML cho coordinator

```yaml
role: reviewer
task_id: vol-02-ch-03-b22-review-signoff
state: done
segment_ids:
  - YS-LN02/Text/part0018.xhtml/p000411
  - YS-LN02/Text/part0018.xhtml/p000438
files_written:
  - reviews/prose/vol-02/ch-03-b22-fixes-signoff-claude.md
validator: not_run
diff_check: not_run
review_path: reviews/prose/vol-02/ch-03-b22-fixes-signoff-claude.md
segment_count: 28
counts:
  serious: 0
  moderate: 0
  minor: 10
prior_moderate_resolved: 5/5
fixed_confirmed: [V1-p000412, V2-p000428, V3-p000430, V4-p000431, V5-p000434]
unresolved_findings: []
findings: []
pending_terms: []
term_recommendations:
  - {source_term: General, proposed_vi: "Tướng", segment_ids: [p000412], status: pending, note: "đề xuất tạm, không canon"}
  - {source_term: "First Lord / Office of the Admiralty", proposed_vi: "giữ Đệ nhất Lãnh chúa Hải quân / Văn phòng Bộ Hải quân", segment_ids: [p000414, p000427, p000435], status: pending, note: "không canon"}
  - {source_term: councilor, proposed_vi: "giữ nghị viên", segment_ids: [p000416], status: pending, note: "không canon"}
  - {source_term: "asylum / refugee", proposed_vi: "giữ xin tị nạn / người tị nạn", segment_ids: [p000425, p000430], status: pending, note: "không canon"}
risks: ["10 lỗi nhẹ chưa sửa, không chặn lô"]
commit: null
next_action: coordinator_may_accept_b22_review_resolved
```
