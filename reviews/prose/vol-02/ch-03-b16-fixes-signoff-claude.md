# Báo cáo signoff sau sửa vol-02-ch-03-b16 (Claude)

- Task: `vol-02-ch-03-b16-review-signoff`, checkpoint_generation 615.
- Phạm vi: 42 đoạn, `YS-LN02/Text/part0018.xhtml/p000215`–`p000256`.
- Đã đọc: shared.md, reviewer.md, config, handoff b16, báo cáo review trước, source package b16 (sha256 `200b552f…cd4421`, khớp handoff) và chỉ `translations/vol-02/ch-03-b16.jsonl`. Không mở EPUB/PDF, package hay bản dịch lô khác. Không sửa tệp nào ngoài báo cáo này. Không chép câu nguồn. Mọi thuật ngữ bên dưới là đề xuất tạm, không canon.
- Tính toàn vẹn: bản dịch vẫn đủ 42 dòng, mã đoạn đúng thứ tự, `source_sha256` các dòng khớp handoff.

## Kết luận

Cả 4 phát hiện mức vừa trước đó đã được xử lý. Không còn lỗi nghiêm trọng hay mức vừa trong lô b16. Không phát hiện lỗi mới do đợt sửa gây ra.

Đếm: nghiêm trọng 0, vừa 0, nhẹ 11 (các mục nhẹ cũ không bắt buộc sửa; xem bên dưới).

## Kiểm tra từng phát hiện vừa

| Mã | Đoạn | Kết quả | Căn cứ |
|---|---|---|---|
| M1 | p000222 | Đã xử lý | Serebryakov nay là “thiếu úy”, Weiss giữ “trung úy”, khớp bản đồ cấp bậc tạm của ledger. Đối chiếu nguồn: cả hai dùng chung một từ cấp bậc nên đây là lựa chọn tạm, không phải sự thật đã chốt. |
| M2 | p000215, p000222, p000224, p000229 | Đã xử lý | Không còn đại từ “cô”. Gọi theo cấp bậc (“Trung úy”, “thiếu úy”, “trung úy”), trung lập về giới, phù hợp DEC-P01-001. Nghĩa mệnh lệnh, điều kiện và phủ định giữ đúng nguồn. |
| M3 | p000228 | Đã xử lý | Nội tâm dùng “Mình”, thống nhất với p000232. Lời thừa nhận nay giới hạn vào “câu đùa đó”, khớp phạm vi nguồn và sắc thái hơi miễn cưỡng. |
| M4 | p000248, p000252 | Đã xử lý | Hai chỗ picket line và cụm surface warning line cùng dùng gốc “tuyến cảnh giới”. “Tuyến tuần tra” ở p000246 giữ riêng, đúng nguồn dùng từ khác. |

prior_moderate_resolved: true (4/4)

## Phát hiện còn lại

- Nghiêm trọng: không.
- Vừa: không.
- Nhẹ: 11 mục cũ (p000216, p000221, p000225, p000232, p000236, p000245, p000248 “chiếm lấy một chiếc”, p000250, p000253, p000256 và quy ước viết hoa chức danh) vẫn như cũ. Đều là tùy chọn, không chặn đóng lô. Ưu tiên nếu có dịp sửa: p000236, p000250, p000253.
- Lưu ý nhỏ: ở p000222, “thiếu úy” lặp hai lần liền (gọi tên rồi xưng hô) khá cứng nhưng đúng và nhất quán; không cần sửa.

unresolved_findings: 0 (serious/moderate)

## Đề xuất thuật ngữ (tạm, chưa canon)

- Cấp bậc Serebryakov = thiếu úy, Weiss = trung úy; độ chắc ~0,6. Nếu coordinator sau này đồng bộ một cấp cho cả hai thì phải đổi ở mọi lô.
- picket line / surface warning line = tuyến cảnh giới; thay thế: tuyến canh phòng; độ chắc ~0,55.
- Cách gọi Weiss/Serebryakov = theo cấp bậc, tránh “cô/anh”; độ chắc ~0,65.
- Không có mục ảnh hưởng cốt truyện cần hỏi người dùng.

## YAML cho coordinator

```yaml
role: reviewer
task_id: vol-02-ch-03-b16-review-signoff
state: done
review_path: reviews/prose/vol-02/ch-03-b16-fixes-signoff-claude.md
segment_ids:
  - YS-LN02/Text/part0018.xhtml/p000215..p000256 (42)
checkpoint_generation: 615
counts:
  serious: 0
  moderate: 0
  minor: 11
prior_moderate_resolved: true
files_written:
  - reviews/prose/vol-02/ch-03-b16-fixes-signoff-claude.md
validator: not_run
diff_check: not_run
findings: []
unresolved_findings: []
term_recommendations:
  - {source_term: Lieutenant (Serebryakov), proposed_vi: thiếu úy, alternatives: [trung úy], segment_ids: [p000222], status: pending, confidence: 0.6}
  - {source_term: picket line / surface warning line, proposed_vi: tuyến cảnh giới, alternatives: [tuyến canh phòng], segment_ids: [p000248, p000252], status: pending, confidence: 0.55}
risks:
  - "Cấp bậc Serebryakov/Weiss chỉ là bản đồ tạm; nguồn trong lô dùng chung một từ"
commit: null
next_action: coordinator_close_batch
```
