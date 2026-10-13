# Báo cáo signoff sau sửa — vol-02-ch-04-b22

- Người phản biện: Claude (reviewer). Phạm vi: 40 đoạn, `YS-LN02/Text/part0024.xhtml/p000312`–`p000351` (viết tắt `pNNNNNN`).
- Đã đọc: shared.md, reviewer.md, config, handoff b22, gói nguồn b22 (sha256 `bb7ae685…` khớp handoff), canon tham chiếu, mục `chapter4_b22_translation_proposals` trong `work/run-state/pending-terms.yml`, báo cáo review gốc, `translations/vol-02/ch-04-b22.jsonl`.
- Không đọc lô/gói khác; không mở EPUB/PDF; không sửa gì ngoài báo cáo này. Mọi lựa chọn dưới đây là đề xuất, không phải canon.

## 1. Toàn vẹn

- JSONL 40/40 dòng, mã đoạn và thứ tự khớp gói nguồn; `source_sha256` khớp.

## 2. M1 — dấu nhấn mạnh (DEC-P01-002): ĐÃ XỬ LÝ, 7/7 đúng phạm vi

Đối chiếu từng phạm vi `em` trong `xhtml` nguồn với `*...*` trong bản dịch:

| Đoạn | Phạm vi nguồn | Kết quả |
|---|---|---|
| p000328 | chỉ câu hỏi cuối | Đúng; phần kể trước đó không nghiêng |
| p000329 | chỉ câu hỏi cuối | Đúng |
| p000332 | toàn đoạn | Đúng |
| p000333 | toàn đoạn | Đúng |
| p000337 | "Nhưng, nhưng…" và câu cuối; câu giữa không nghiêng | Đúng, hai vùng riêng, câu giữa để thường |
| p000347 | chỉ câu hỏi giữa | Đúng; câu trước/sau để thường |
| p000350 | chỉ phần sau dấu hai chấm | Đúng; phần dẫn để thường |

Không có `*...*` ở đoạn nào khác (không dấu thừa). Không có dấu lồng hay lệch ranh giới.

## 3. Lỗi còn lại

- Nghiêm trọng: 0.
- Vừa: 0. Việc thêm dấu nghiêng không phát sinh lỗi mới; bản dịch cũng đã tự sửa thêm các mục L2, L3, L9, L11 và phần "mình/hai người" của L6.
- Nhẹ: 8 mục còn lại, không chặn lô, sửa hay không tùy người giữ quyền sửa:
  - L1 p000314: "vì nhầm nó là tàu khả nghi" (đề xuất "vì coi nó là tàu khả nghi"); "chỉ có hình thức" → "chỉ là hình thức".
  - L4 p000321: "không nói suông" lệch nhẹ; đề xuất "không phải lời nói cho có".
  - L5 p000328: "vừa đủ" → "đạt yêu cầu".
  - L6 p000332: "quả cầu điên loạn" đọc lạ; đề xuất "khối điên loạn".
  - L7 p000333: "bình thường" thêm nghĩa; đề xuất "một con người thôi".
  - L8 p000334: cấu trúc điều kiện khó đọc.
  - L10 p000336: "chỉ thể hiện" (thừa "chỉ") và "lời chúc mừng năm mới" (thu hẹp "season's greetings").
  - L12 p000349: nguồn chỉ "Thiếu tá von Degurechaff", bản dịch thêm "Pháp sư Tanya"; "Dù có biết hay không khi cúi chào" còn mơ hồ phạm vi. p000350 "Tôi" (nghiêng) so với p000351 "Tôi" (ngôi nhất kể), nhất quán, ghi pending.

unresolved_findings: không còn mã nghiêm trọng hoặc vừa chưa xử lý.

## 4. Thuật ngữ pending (đề xuất tạm, không canon)

Không phát sinh mục mới. Hiện dùng: "Trung ương" (Central), "pháp sư hải quân" (alt: pháp sư thủy quân lục chiến), "diễn tập chiến tranh" (alt: diễn tập quân sự), "tôi" cho lời kể ngôi nhất của Tanya ở p000351 (alt: "mình"), "Đại tá von Lergen" (alt: Trung tá, cần kiểm tra xuyên lô). Giữ nhất quán, không ảnh hưởng cốt truyện, không cần hỏi người dùng.

## 5. YAML cho coordinator

```yaml
role: reviewer
task_id: vol-02-ch-04-b22-review-signoff
state: done
segment_ids:
  - YS-LN02/Text/part0024.xhtml/p000312
  - YS-LN02/Text/part0024.xhtml/p000351
files_written:
  - reviews/prose/vol-02/ch-04-b22-fixes-signoff-claude.md
validator: not_run
diff_check: not_run
commit: null
review_path: reviews/prose/vol-02/ch-04-b22-fixes-signoff-claude.md
segment_count: 40
counts:
  serious: 0
  moderate: 0
  minor: 8
m1_status: resolved_7_of_7
unresolved_findings: []
term_recommendations:
  - {term: Central, keep: Trung ương, status: pending}
  - {term: marine mages, keep: pháp sư hải quân, alt: pháp sư thủy quân lục chiến, status: pending}
  - {term: war game, keep: diễn tập chiến tranh, alt: diễn tập quân sự, status: pending}
  - {term: Tanya first-person narration p000351, keep: tôi, alt: mình, status: pending}
  - {term: Colonel von Lergen, keep: Đại tá, alt: Trung tá, status: pending_cross_batch_check}
next_action: signoff
```
