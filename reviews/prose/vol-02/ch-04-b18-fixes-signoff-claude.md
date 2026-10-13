# Signoff vol-02-ch-04-b18 (Claude) — checkpoint_generation 826

- Phạm vi: 27 đoạn, `YS-LN02/Text/part0024.xhtml/p000199` → `p000225`. Ký hiệu `pNNNNNN` = `YS-LN02/Text/part0024.xhtml/pNNNNNN`.
- Đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b18, gói nguồn b18 (sha256 `d1199b9a…` khớp handoff), canon (style-guide, decisions, characters, glossary), mục `chapter4_b18_translation_proposals` trong pending-terms, báo cáo review ban đầu và `translations/vol-02/ch-04-b18.jsonl`. Không đọc lô/gói khác. Không sửa bản dịch, handoff, ledger hay canon.
- Mọi lựa chọn dưới đây là **đề xuất tạm, không phải canon**.
- Kiểm tra kết cấu: 27/27 đoạn, đúng thứ tự, không rỗng, `status: draft`, `glossary_version` và `source_sha256` khớp handoff. Không có `*...*` (nguồn không có nhấn mạnh) → khớp DEC-P01-002.

## Tổng hợp mức độ (sau sửa)

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 0 |
| Nhẹ | 3 (còn lại, không chặn) |

`prior_moderate_resolved: true` (1/1). `unresolved_moderate: []`. `unresolved_serious: []`.

## Đối chiếu lỗi vừa trước

| ID | Đoạn | Kết quả | Căn cứ |
|---|---|---|---|
| M1 | p000212 | Đã sửa | Nay là "đơn vị Named được cho là đã triển khai ở khu vực phía bắc" — tình thái nhận thức (được cho là), không còn nghĩa phản thực/chuẩn mực của "lẽ ra". Khớp p000213 ("dường như đang yểm trợ") và không thêm chắc chắn. Câu hỏi "Vì sao … mai phục chúng ta ở đây" giữ đúng đối tượng. |

## Named (vol02-ch04-b18-named) — đề xuất tạm

- Bản dịch dùng "đơn vị Named" nhất quán ở cả 7/7 đoạn trong ledger: p000212, p000213, p000214, p000215, p000216, p000217, p000221. Không còn "Danh Hiệu" ở đoạn nào.
- Khớp ledger: proposed_vi "đơn vị Named", thay thế "đơn vị Danh Hiệu", status pending, confidence 0.35. Không có đoạn nào ngoài danh sách dùng thuật ngữ này.
- Vẫn là đề xuất, không ảnh hưởng cốt truyện trong lô này; không cần hỏi người dùng.

## Kiểm tra hồi quy các bản sửa đã hỗ trợ

- p000212: "các vị" trung tính (thay "các anh"); không suy giới tính.
- p000214: "Trung ương" trung tính; p000215: bỏ "được cho là", nay nêu như dữ kiện ("khu vực họ được bố trí đóng quân").
- p000219: "sau chiến dịch đổ bộ bất chấp các tuyến liên lạc…" — quan hệ vẫn gần nguồn; chấp nhận.
- p000220: "Đó là những người…" bỏ sắc thái miệt thị; logic "kế hoạch, không phải trùng hợp" giữ.
- p000221: giả định quá khứ giữ ("đã được rút đi rồi xuất hiện … có thể xem đó là bằng chứng"); "không còn thấy … xuất hiện" không nói quá "biến mất"; chủ thể thống nhất "đơn vị ấy"/"nó".
- p000223: "trên thực tế, hạm đội đã phải rời đội hình … với thời điểm quá hoàn hảo" — không còn lặp "đội hình", giữ ý "quá hoàn hảo". Chấp nhận.
- p000225: "đợt đánh chặn hầu như chưa kịp diễn ra" khớp "just barely occurred"; logic "nếu là trùng hợp… nhưng bất khả thi" nguyên vẹn.
- p000208: "những tàu khác" (thay "chiến hạm"); phủ định/tăng tiến "không chỉ… mà còn…" ở p000208 đúng.
- Không phát sinh lỗi nghĩa, phủ định, đối tượng câu hỏi (p000199, p000212, p000218, p000219), nhấn mạnh hay thuật ngữ mới do các bản sửa.

## Lỗi nhẹ còn lại (không chặn, tùy chọn)

- p000210: "battle cruiser" → "tuần dương hạm" vẫn mất "battle" (m4 cũ, chưa xử lý). Gợi ý "tuần dương hạm chiến đấu" hoặc ghi nghi vấn loại tàu.
- p000222: "chẳng thèm nhìn" vẫn nặng hơn "without even looking" (m7 cũ, nửa còn lại). Gợi ý "chẳng buồn liếc" / "không hề nhìn".
- p000203, p000207 (và p000201): đại từ "tôi" cho người kể quan sát theo đề xuất coordinator. Nguồn p000203 ("he couldn't accept it") và p000207 ("he projected") là ngôi ba, còn p000201 không có chủ ngữ; bản dịch ghi "tôi", và ở p000207 có thể hiểu "tôi chiếu" = người nói ở p000206/p000212 ("ông"), gây lệch chủ thể. Nguồn mơ hồ nên không nâng thành lỗi vừa; đề xuất tạm: giữ "tôi" theo coordinator nhưng cân nhắc dạng trung tính ở p000207 ("Đoạn phim trận chiến được chiếu lên…") nếu coordinator muốn tránh gán chủ thể. Đề xuất ghi độ bất định vào pending-terms (chưa có mục riêng).

## Kết luận

Không còn lỗi nghiêm trọng hay vừa trong lô; M1 đã được xử lý đúng và Named nhất quán. Lô đủ điều kiện qua review chữ nghĩa/văn phong.

## Coordinator YAML

```yaml
role: reviewer
task_id: vol-02-ch-04-b18-review-signoff
state: done
segment_ids: [YS-LN02/Text/part0024.xhtml/p000199, YS-LN02/Text/part0024.xhtml/p000225]  # 27 đoạn liên tiếp
files_written: [reviews/prose/vol-02/ch-04-b18-fixes-signoff-claude.md]
validator: not_run
diff_check: not_run
review_path: reviews/prose/vol-02/ch-04-b18-fixes-signoff-claude.md
counts: {serious: 0, moderate: 0, minor: 3}
prior_moderate_resolved: true
prior_moderate_checked: [M1]
unresolved_findings: []
unresolved_finding_ids: []
optional_minor: [m4 p000210, m7 p000222, narrator-pronoun p000203/p000207]
term_recommendations:
  - {source_term: Named, proposed_vi: đơn vị Named, alternatives: [đơn vị Danh Hiệu], segment_ids: [p000212, p000213, p000214, p000215, p000216, p000217, p000221], status: pending, confidence: 0.35}
  - {source_term: observer narrator pronoun, proposed_vi: tôi, alternatives: [dạng trung tính/bị động, lặp danh từ], segment_ids: [p000201, p000203, p000207], status: pending, confidence: 0.4}
risks: ["Đại từ người kể 'tôi' vs 'he' nguồn ở p000203/p000207 còn mơ hồ", "Loại tàu 'battle cruiser' p000210 chưa chốt"]
commit: null
next_action: signoff
```
