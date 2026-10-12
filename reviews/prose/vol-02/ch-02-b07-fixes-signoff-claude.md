# Signoff sửa lỗi b07 — vol-02-ch-02-b07-followup-signoff

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch hay file khác). Không trích văn bản nguồn.
- **Phạm vi:** p000145, p000147, p000152, p000154, p000157, p000160, p000161 (đối chiếu thêm p000158, p000159 chỉ để kiểm tra thuật ngữ Northern Army Group). Đã đối chiếu báo cáo trước, handoff, bản dịch b07 và ledger `work/run-state/pending-terms.yml`. Không đọc batch khác.

## Kết luận: `pass_with_notes` (serious 0, moderate 1, minor 3)

## Xác nhận M1–M3
- **M1 đã giải quyết:** p000145, p000147, p000152, p000154 dùng "mình" cho nội tâm Tanya, khớp DEC-P01-001 và ledger. Nhấn mạnh `*…*` ở p000147, p000154 vẫn giữ.
- **M2 đã giải quyết:** p000161 dùng "không đánh dấu nguồn gốc", đúng lựa chọn tạm trong handoff; thứ tự bốn cường quốc không đổi.
- **M3 đã giải quyết:** p000160 đã bỏ "hẳn" và thêm ý "tuyệt đối", khớp lựa chọn tạm trong handoff; không đảo nghĩa.

## Căn chỉnh ledger
- **Great Army:** p000157 dùng "Đại Quân", khớp ledger (`great-army`, `b03-great-army`, `vol02-ch02-b07-great-army`). Đã giải quyết.
- **Northern Army Group:** p000157 dùng "Cụm tập đoàn quân phương Bắc" (chữ thường), khớp ledger. **Chưa đồng bộ hoàn toàn**: xem MOD-1.

## Phát hiện moderate
- **MOD-1 — p000158, p000159:** viết "Cụm Tập đoàn quân phương Bắc" (hoa chữ T), lệch p000157 và ledger (hạ "tập đoàn quân"). Hai đoạn nằm ngoài danh sách đoạn đã sửa nên translator bỏ sót, nhưng handoff ghi `northern_army_group` đã căn chỉnh. Cần sửa hai đoạn này, hoặc ghi rõ ngoại lệ vào ledger. Mức độ nhẹ về nghĩa, nhưng ảnh hưởng nhất quán thuật ngữ trong cùng khối.

## Minor (không chặn)
- **p000160:** "tổng quân số … xét theo tổng số tuyệt đối" lặp "tổng". Có thể gọn thành "xét theo số tuyệt đối".
- **p000152:** "điều đang được yêu cầu ở mình" vẫn có thể bị đọc là Tanya (m4 của báo cáo trước, chưa xử lý). Nên đổi thành "ở họ".
- **p000157:** "Lục quân Đế quốc" so với "Quân đội Đế quốc" trong ledger vẫn chưa thống nhất (m8 cũ).

## Rủi ro
- Chỉ MOD-1 cần xử lý trước khi nâng batch lên bản chuẩn. Các thuật ngữ vẫn là đề xuất tạm, không phải canon.

## YAML
```yaml
task_id: vol-02-ch-02-b07-followup-signoff
state: done
reviewed_segments: 7
serious: 0
moderate: 1
minor: 3
findings:
  - {id: MOD-1, severity: moderate, segment_ids: [p000158, p000159], issue: "Northern Army Group viết 'Cụm Tập đoàn quân' lệch p000157 và ledger", suggestion: "hạ chữ T hoặc ghi ngoại lệ vào ledger"}
  - {severity: minor, segment_ids: [p000160], issue: "lặp 'tổng'"}
  - {severity: minor, segment_ids: [p000152], issue: "'ở mình' còn mơ hồ chủ thể"}
  - {severity: minor, segment_ids: [p000157], issue: "Lục quân/Quân đội Đế quốc chưa thống nhất"}
risks: [MOD-1 chưa đồng bộ]
next_action: người giữ quyền sửa sửa p000158/p000159 (và minor nếu muốn), chạy lại validator + git diff --check rồi commit
```
