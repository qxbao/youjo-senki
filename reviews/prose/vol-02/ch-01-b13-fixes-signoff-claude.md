# Signoff sửa lỗi — vol-02-ch-01-b13-fixes-signoff

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon).
- Phạm vi: chỉ 13 đoạn đã sửa của b13: p000330, 331, 332, 333, 335, 337, 338, 342, 343, 346, 348, 351, 364 (mã đầy đủ `YS-LN02/Text/part0010.xhtml/pNNNNNN`).
- Đối chiếu: báo cáo gốc `reviews/prose/vol-02/ch-01-b13-claude.md`, `handoffs/vol-02/ch-01-b13.yml`, `translations/vol-02/ch-01-b13.jsonl`, gói nguồn cục bộ `work/vol-02/batches/ch-01-b13-source.jsonl` (đọc tại chỗ, không trích nguồn trong báo cáo), `work/run-state/pending-terms.yml`.
- Mọi lựa chọn vẫn là đề xuất tạm, không phải canon.

## 1. Kết quả M1–M5

| Mã | Yêu cầu | Kết quả | Ghi chú |
|---|---|---|---|
| M1 | Nghiêng đúng phạm vi | **Đạt** | Gói nguồn có đúng hai phần `<em>`: toàn bộ câu nội tâm của Visha ở p000333 và câu thành ngữ ngắn ở p000346. Bản dịch có đúng hai cặp `*…*` tương ứng, không thừa, không thiếu, không còn ngoặc kép thừa ở p000333. Phần dẫn "Không, suy nghĩ của cô là:" nằm ngoài dấu nghiêng, đúng như nguồn. |
| M2 | Tanya: "nó"/tên trong trần thuật, "mình" nội tâm; Visha vẫn "cô" | **Đạt** | Trần thuật về Tanya dùng "nó" hoặc tên ở p000331, 332, 337 (cả "tuổi của nó"), 338, 342, 343, 346, 348, 364. "mình" chỉ còn trong nội tâm p000331. "cô" ở p000333 chỉ Visha, không còn mơ hồ. "anh" cho Weiss ở p000337 nhất quán với giới nam đã ghi tạm. |
| M3 | Phát âm trẻ con nhẹ ở p000330 | **Đạt** | Hai điểm đổi âm nhẹ ("chân chọng", "nười"), đúng hai từ nguồn bị sai âm, khớp quy ước b12. Phần còn lại là tiếng Việt chuẩn, dễ đọc, không có chú thích hay lời dẫn thêm. |
| M4 | p000351 gọi rõ "quan sát viên" | **Đạt** | Cả hai mệnh lệnh đều có; đối tượng hô gọi "Các quan sát viên" xuất hiện, khớp mục `vol02-ch01-b13-observers`. |
| M5 | p000335 gọi theo cấp bậc, không "chị" | **Đạt** | Dùng "Thiếu tá", không có đại từ giới tính hay "ạ". |

## 2. Nghĩa và thuật ngữ

- **Không đổi nghĩa**: so sánh từng đoạn với nguồn. Phủ định, nhượng bộ, đối tượng, thời điểm và logic (p000331 nhượng bộ "đã đủ tệ… nhưng vẫn…", p000332 "cô"/Visha quan sát, p000342 "bình thường… nhưng hôm nay…", p000364 nổ ngay lúc Weiss định nói) đều giữ đúng. Không thêm hay bớt chi tiết ngoài phần phát âm đã chủ ý ở p000330.
- **Thuật ngữ vẫn tạm**: các mục liên quan trong `pending-terms.yml` (`formula`, `projection-formula`, `observers`, `weiss-gender`) đều `status: pending`, `provisional_non_canon`. Handoff ghi `pending_status: provisional_non_canon`. Bản dịch dùng "thuật thức", "thuật thức phóng chiếu", "quan sát viên" nhất quán, không gắn nhãn canon.
- `notes` của 13 đoạn rỗng; `status: draft`; không có dấu chú thích.

## 3. Đếm còn lại (phạm vi 13 đoạn)

Nghiêm trọng **0** · vừa **0** · nhẹ **2** (không chặn):
1. p000335: "Thiếu tá, Thiếu tá đã từng…" lặp danh xưng hơi nặng; chấp nhận được, có thể lược vế đầu sau này. Không cần sửa ngay.
2. p000338, p000346: "thiếu tá von Degurechaff" viết thường, trong khi p000333/335 viết hoa khi xưng hô trực tiếp. Nhất quán nội bộ theo cách danh xưng đi kèm tên; chỉ lưu ý khi rà toàn chương.

N1–N14 của báo cáo gốc nằm ngoài phạm vi signoff này, không xét lại.

## 4. Rủi ro

- Việc ghi lại danh sách đoạn của `formula` và hai mục thiếu (Carberius, Tamaya) trong sổ pending thuộc coordinator; signoff này chỉ thấy các mục đó đã có trong sổ, không đánh giá phần ngoài phạm vi.
- Nếu về sau canon chốt đại từ Tanya khác, cần rà lại các đoạn trên.
- Chi tiết ngọng ở p000330 là đề xuất tạm; giữ nhất quán với các lô sau.

## 5. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-01-b13-fixes-signoff
state: done
segment_ids: [p000330, p000331, p000332, p000333, p000335, p000337, p000338, p000342, p000343, p000346, p000348, p000351, p000364]
files_written: [reviews/prose/vol-02/ch-01-b13-fixes-signoff-claude.md]
review_path: reviews/prose/vol-02/ch-01-b13-fixes-signoff-claude.md
fixes_pass: true
m_status: {M1: pass, M2: pass, M3: pass, M4: pass, M5: pass}
meaning_changes: none
terms_status: provisional_non_canon
counts: {serious: 0, moderate: 0, minor: 2}
risks: [coordinator còn phải cập nhật sổ pending ngoài phạm vi signoff, đại từ Tanya có thể đổi nếu canon chốt khác, ngọng p000330 là đề xuất tạm]
commit: null
next_action: coordinator_may_commit_b13 # không cần dịch lại; không hỏi người dùng
```
