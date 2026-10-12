# Signoff sửa lỗi — vol-02-ch-01-b12-fixes-signoff

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon).
- Phạm vi: các đoạn đã sửa p000304, p000307, p000320, p000322, p000325; ngữ cảnh cấp bậc trong lô p000299, p000313, p000316.
- Nguồn đối chiếu: báo cáo b12 gốc, handoff b12, `translations/vol-02/ch-01-b12.jsonl`, gói nguồn b12. Không xem b11 hay lô khác. Các tham chiếu p000276–p000277 và p000296 nằm ngoài b12, không tính.
- Báo cáo không trích câu nguồn. Mọi thuật ngữ vẫn là đề xuất tạm, chưa phải canon.

## 1. Kết quả theo hạng mục

| Hạng mục | Đoạn | Kết quả |
|---|---|---|
| Bản đồ cấp bậc (M1) | p000299, p000313: Thiếu úy Serebryakov; p000307: Trung úy Weiss | **Đạt.** Khớp bản đồ tạm Serebryakov = Thiếu úy / Weiss = Trung úy và khớp `provisional_review_choices` trong handoff. p000316 vẫn bỏ chức danh trong phần trần thuật, không mâu thuẫn bản đồ (xem N9 bên dưới). |
| Xưng hô trung lập (M2) | p000307, p000320 | **Đạt.** p000307 gọi theo cấp bậc và tên, lược chủ ngữ ở vế sau. p000320 gọi bằng cấp bậc. Không còn đại từ mang giới tính. Từ "nỗi sợ" ở p000307 cũng hết lệch so với bản gốc, nên N8 coi như xử lý xong. |
| Lối nói ngọng nhẹ (M3) | p000322, p000325 | **Đạt ở mức chấp nhận được.** Cả hai đoạn đều có dấu hiệu ngọng nhẹ, chỉ ở từ chính của câu, không kéo dài cả đoạn, không đổi nghĩa. Còn một điểm nhẹ về tính đồng nhất, xem m1. |
| Cách diễn đạt p000304 (N12) | p000304 | **Đạt.** Hết lặp "phát" liền kề; thông tin nội dung và kênh báo nguy quốc tế giữ đúng, nhất quán với p000324. Chỉ còn một "phát" ở cuối câu. |
| Cơ học | p000304, 307, 320, 322, 325 | `notes` rỗng, `translation` giữ nguyên dấu ngoặc kép. Không có `*...*` thừa hay thiếu trong các đoạn này. Đại từ Tanya p000322 dùng "nó" đúng DEC-P01-001. |

## 2. Còn lại

Đếm: **nghiêm trọng 0 · vừa 0 · nhẹ 3**.

- **m1 — p000322 / p000325: cơ chế ngọng chưa cùng kiểu.** p000322 đổi dấu ở từ chính, và dạng đó dễ bị đọc là lỗi gõ. p000325 dùng kéo dài nguyên âm, tức là kiểu "kéo giọng". Cả hai đều gợi giọng trẻ con, nhưng không phải cùng một quy tắc thay âm như nguồn. Không ảnh hưởng nghĩa. Nếu coordinator muốn đồng nhất, có thể chọn một quy tắc duy nhất (ví dụ cùng thay một âm đầu cho cả hai từ chính). Không bắt buộc cho signoff.
- **N4 (p000313), chưa đổi:** "Ra thông báo cảnh báo. Ra lệnh…" vẫn lặp "ra" và thừa "thông báo". Đây là ngữ cảnh, không thuộc nhóm sửa, mức nhẹ.
- **N9 (p000316), chưa đổi:** vẫn bỏ chức danh trước hai tên và dùng "non nớt" hơi nặng. Mức nhẹ, không xung đột cấp bậc.

Các mục nhẹ N1–N3, N5–N7, N10–N11 của báo cáo gốc không thuộc phạm vi signoff này; tình trạng của chúng không được kiểm tra lại ở đây.

## 3. Rủi ro

- Bản đồ cấp bậc vẫn là đề xuất tạm (độ tin cậy 0,55 trong báo cáo gốc). Nếu về sau nguồn lô khác đổi, chỉ cần sửa p000299, p000307, p000313, p000320.
- Xưng hô giới tính của Serebryakov/Weiss vẫn chưa có căn cứ chắc, tiếp tục dùng cấp bậc/tên để tránh phải sửa ngược.
- Quy ước ngọng chưa nâng thành canon; người dịch lô sau cần đọc mục pending để giữ nhất quán.

## 4. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-01-b12-fixes-signoff
state: done
segment_ids: [p000304, p000307, p000320, p000322, p000325]
context_segment_ids: [p000299, p000313, p000316]
files_written: [reviews/prose/vol-02/ch-01-b12-fixes-signoff-claude.md]
review_path: reviews/prose/vol-02/ch-01-b12-fixes-signoff-claude.md
fixes_pass: true
resolved: [M1, M2, M3, N8, N12]
counts: {serious: 0, moderate: 0, minor: 3}
remaining_minor: [m1_mispronunciation_mechanism_uneven, N4, N9]
risks: [rank_map_provisional, gender_unknown_serebryakov_weiss, mispronunciation_convention_non_canon]
term_status: pending_non_canon
commit: null
next_action: coordinator_may_commit_b12; optional_unify_mispronunciation_m1
```
