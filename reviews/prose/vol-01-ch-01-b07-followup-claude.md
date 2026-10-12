# Báo cáo review follow-up vol-01-ch-01-b07 (Claude, reviewer)

- Task: `vol-01-ch-01-b07-review-fixes-followup`; lô `vol-01-ch-01-b07`; 28 đoạn `chapter003b.xhtml/p000101`–`p000128` (viết tắt `pNNNNNN`).
- Đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff review-revision, báo cáo review lượt đầu, source package cục bộ, `translations/vol-01/ch-01-b07.jsonl`, `work/run-state/pending-terms.yml`, `canon/decisions.md`, `canon/glossary-pending.yml`. Không đọc `footnote.xhtml` (ngoài phạm vi). Không ghi tệp nào ngoài báo cáo này.
- Cấu trúc: đủ 28/28 dòng, đúng thứ tự, trạng thái `draft`. Không có đoạn thiếu, thừa hay gộp.

## Kết luận

Không còn lỗi nghiêm trọng hay vừa. Hai lỗi vừa của lượt trước (p000119, p000108) đã được xử lý đúng. Không phát sinh lỗi nghiêm trọng/vừa mới. Còn 3 lỗi nhẹ, đều không chặn lô.

## 1. Kiểm tra các điểm được yêu cầu

| Mục | Kết quả |
|---|---|
| p000119 (M1) | Đã đạt. "tín hiệu số" đã thay bằng "các dãy số"; đại từ đổi thành "chúng". Hết nhầm với digital signal. Đại từ đã tách khỏi Sư đoàn 6 ở p000116–p000118; p000120 làm rõ chủ thể là phía địch. |
| p000108 (M2) | Đã đạt. Chỉ còn "người điều phối tiền phương được chỉ định", không có cấp bậc. Ghi chú nêu rõ pending, không suy cấp bậc, nêu phương án khác. Khớp ledger `b07-forward-controller`. |
| p000128 | Đã đạt. Nguồn có đúng một thẻ `<em>` bao toàn đoạn; bản dịch bọc toàn đoạn bằng `*…*`, đúng DEC-P01-002. Không có dấu `*` nào ở đoạn khác, không có nhấn mạnh thừa. |
| Lỗi nhẹ lượt trước | Đã áp dụng m1–m9: p000101–102 bỏ "diễn trò", "để lộ dấu hiệu…"; p000106 "một ổ toàn lũ ngu xuẩn"; p000115 "cản trở"; p000116 "Sư đoàn 6 lục quân"; p000117 thành câu hỏi thăm dò; p000120 và p000122 đã đồng bộ; p000125 "vốn dĩ… sao". Dấu ⁷ giữ nguyên vị trí ở p000122. |
| Ledger m10 | Đã sửa: `b07-brinkmanship-diplomacy` có "chiến tranh", khớp bản dịch và ghi chú p000101/p000102. |

## 2. Phát hiện

### Nghiêm trọng: 0 · Vừa: 0

### Nhẹ (3)

**n1 — Ledger `b07-artillery-observer` thiếu mã đoạn.**
- `segment_ids` chỉ có p000117 và p000120, nhưng bản dịch cũng dùng "quan sát viên" ở p000115. p000114 vẫn dùng "những người quan sát" cho cùng vai trò (nguồn "observers").
- Đề xuất: coordinator thêm p000115 (và p000114 nếu translator đồng bộ) vào ledger. Lúc đó có thể đổi p000114 thành "quan sát viên" cho nhất quán hoặc giữ, vì dạng chung "người quan sát" ở câu hỏi đầu vẫn hiểu được. Độ tin cậy: 0.55.

**n2 — Ledger `b07-observer-mage` có hai trường ghi chú lặp (`rationale` và `note`).**
- Nội dung cùng ý, không mâu thuẫn. Đề xuất: gộp cho gọn khi coordinator cập nhật sổ. Không ảnh hưởng bản dịch.

**n3 — p000119: "Chúng" ở đầu câu vẫn hơi mơ hồ trong khoảnh khắc đọc.**
- Đoạn ngay trước (p000118) nói về sư đoàn; "Chúng" phải đợi p000120 mới rõ là phía địch. Đây là hệ quả của yêu cầu dùng "chúng" và chấp nhận được. Nếu muốn chắc hơn, có thể dùng "Bọn chúng", hoặc để nguyên. Không cần sửa. Độ tin cậy: 0.4.

### Đã đối chiếu, không vấn đề mới
p000101–p000118, p000120–p000127 giữ nghĩa, giọng và quan hệ nhân quả. Đại từ địch thống nhất "chúng" (p000119, p000121, p000122, p000125, p000126). Ghi chú p000108, p000116, p000117, p000120, p000122 khớp văn bản và ledger.

## 3. Khuyến nghị thuật ngữ (chỉ là đề xuất, không phải canon; tất cả vẫn pending)

| Mục ledger | Văn bản hiện tại | Khuyến nghị |
|---|---|---|
| b07-brinkmanship-diplomacy | ngoại giao bên miệng hố chiến tranh | Giữ tạm; khớp. Phương án khác "ngoại giao đẩy sát bờ vực chiến tranh". |
| b07-warning-line | tuyến cảnh giới (đồ sộ) | Giữ tạm. Đối chiếu chú thích ⁷ và p000123 ("tuyến phòng không") khi có điều kiện; chưa đủ căn cứ để hợp nhất. |
| b07-ground-division-six | Sư đoàn 6 lục quân | Giữ tạm; rationale và ghi chú đã khớp. Nếu về sau có thêm sư đoàn đánh số thì thống nhất công thức. |
| b07-observer-mage | pháp sư quan sát | Giữ tạm, riêng với `spotter magician → pháp sư trinh sát cảnh giới` (đã có ở chapter003) cho tới khi có căn cứ quan hệ giữa hai nhãn. |
| b07-forward-controller | người điều phối tiền phương được chỉ định | Giữ tạm; không gán cấp bậc. |
| b07-artillery-observer | quan sát viên pháo binh | Giữ tạm; khớp p000117, p000120 và p000115. Cập nhật `segment_ids` (n1). Phương án khác "trinh sát pháo binh". |

Cả năm mục đều khớp giữa ghi chú bản dịch, văn bản và ledger, trừ chi tiết mã đoạn ở n1. Không có mục nào ảnh hưởng cốt truyện hay cần hỏi người dùng.

## 4. Rủi ro còn lại

1. Chú thích ⁷ chưa đối chiếu (ngoài phạm vi); có thể làm thay đổi "tuyến cảnh giới".
2. Nhóm quan sát/trinh sát/spotter/observer mage trải nhiều lô; cần theo dõi đồng bộ.
3. Xưng hô "cậu"/"các anh" và "Chúa" chưa có canon; hiện nhất quán, cần giữ ổn định (liên quan Being X).
4. Validator và diff_check chưa chạy trong task này (không thuộc phạm vi reviewer).

## 5. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-01-ch-01-b07-review-fixes-followup
state: done
segment_ids: [p000101..p000128, 28 đoạn theo handoff]
files_written:
  - reviews/prose/vol-01-ch-01-b07-followup-claude.md
review_path: reviews/prose/vol-01-ch-01-b07-followup-claude.md
validator: not_run
diff_check: not_run
counts:
  serious: 0
  moderate: 0
  minor: 3
unresolved_findings:
  - {severity: minor, segment_ids: [p000114, p000115], issue: 'ledger b07-artillery-observer thiếu p000115; p000114 dùng "người quan sát" (n1)'}
  - {severity: minor, segment_id: p000120, issue: 'ledger b07-observer-mage có rationale và note lặp (n2)'}
  - {severity: minor, segment_id: p000119, issue: '"Chúng" hơi mơ hồ đến p000120, chấp nhận được (n3)'}
term_recommendations:
  - {id: b07-brinkmanship-diplomacy, keep_provisional: true}
  - {id: b07-warning-line, keep_provisional: true, note: 'đối chiếu chú thích ⁷ và p000123'}
  - {id: b07-ground-division-six, keep_provisional: true}
  - {id: b07-observer-mage, keep_provisional: true, note: 'giữ riêng với spotter magician tới khi có căn cứ'}
  - {id: b07-forward-controller, keep_provisional: true, note: 'không gán cấp bậc'}
  - {id: b07-artillery-observer, keep_provisional: true, note: 'thêm p000115 vào segment_ids'}
risks:
  - 'Chú thích ⁷ chưa đối chiếu (ngoài phạm vi)'
  - 'Thuật ngữ quan sát/trinh sát/spotter cần đồng bộ ở các lô sau'
  - 'Xưng hô và "Chúa" chưa có canon'
commit: null
next_action: coordinator chạy validator/diff_check và cập nhật ledger (n1, n2); không còn lỗi nghiêm trọng/vừa
```
