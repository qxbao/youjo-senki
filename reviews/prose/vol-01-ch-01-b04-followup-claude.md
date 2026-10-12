# Phản biện follow-up — vol-01 Chương 1, lô b04

Người phản biện: Claude. Task: `vol-01-ch-01-b04-review-fixes-followup`. Phạm vi: 11 đoạn p000044–p000054, tiền tố đầy đủ `YS-LN01/Text/chapter003b.xhtml/`. Báo cáo không chép câu nguồn; chỉ dùng mã đoạn và thuật ngữ ngắn để nhận diện.

Đầu vào đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, handoff `review-revision-ch-01-b04.yml`, gói nguồn b04 (đọc tại chỗ, lượt trước trong cùng phiên), bản dịch b04 hiện tại, báo cáo b04 ban đầu, `work/run-state/pending-terms.yml` (mục `chapter1_b04_claude_decisions`), `canon/style-guide.md`, `canon/decisions.md`; `canon/glossary.yml` và `canon/characters.yml` vẫn rỗng.

**Tính chất:** mọi phương án dưới đây là đề xuất tạm, không phải canon. Không sửa bản dịch, canon, handoff hay sổ pending. Validator/diff_check: not_run; commit: null.

Thang tin cậy: cao ≥ 0,75; vừa 0,5–0,74; thấp < 0,5.

## 1. Kết luận

- Ba phát hiện mức vừa trước đây đều đã được xử lý; không phát sinh lỗi nghiêm trọng hay vừa mới.
- Còn 4 điểm nhẹ, không chặn commit. Một mục cần coordinator ở cấp quy ước (đại từ "nó" so với b02–b03), không phải lỗi bản dịch.
- 11/11 hàng giữ nguyên `segment_id`, thứ tự, `source_sha256` và `glossary_version`. Nguồn không có chữ nghiêng; bản dịch không có `*...*`: đúng DEC-P01-002. Ngoặc kép giữ đúng ở p000045, p000049, p000050 (hai cụm).
- Không có điểm ảnh hưởng cốt truyện; không cần hỏi người dùng.

## 2. Xác nhận ba phát hiện vừa cũ

| Mã đoạn | Kết quả | Căn cứ |
|---|---|---|
| p000044 | Đã sửa | "Nếu khi ấy được nói thẳng… có lẽ Tanya đã mô tả": khôi phục giả định phản thực tại về quá khứ (khi ấy… đã). "ý muốn chết" thay "tự tìm đến cái chết", bỏ ý chủ động; vẫn giữ mức phỏng đoán và không thành hành động tự sát cụ thể. Lặp tên Tanya xóa mơ hồ chủ thể. |
| p000051 | Đã sửa | (a) Cảm xúc: "thấy khó chịu" thay "ái ngại", đúng bình diện không thiện cảm. (b) Logic: "Ở đó vốn đã khó lập thành tích, mà điều kiện còn bất lợi hơn vì…" — ngoại hình là lý do làm điều kiện tệ hơn, không còn đọc thành mục đích; bỏ "nhiều" thêm. |
| p000044–p000054 (đại từ) | Đã xử lý ở mức bản dịch | Dùng "nó" (trần thuật) và "mình" (nội tâm tự quy chiếu) nhất quán theo DEC-P01-001; ở các chỗ dễ nhầm quy chiếu (p000044, p000046) đã lặp tên Tanya. Mục `b04-tanya-narration` trong sổ pending ghi đúng tính tạm thời, độ tin cậy 0,55 và việc rà đồng bộ b02–b03 còn mở. |

## 3. Đại từ và điểm nhìn: không gán người nói

- p000051 (câu cuối) và p000054 (câu có ngôi thứ nhất): bản dịch giữ "mình … nó" ở cả hai nơi, không thêm nhãn người nói, không đồng nhất hay tách "mình" khỏi Tanya. Ghi chú p000051 và p000054 nêu rõ rủi ro quy chiếu (0,55) và "không xác định người nói": khớp yêu cầu.
- Rủi ro còn lại (đã biết từ báo cáo trước, không phải lỗi): "mình" theo DEC-P01-001 nghiêng nhẹ về cách hiểu Tanya tự nói về mình. Nguồn không khẳng định; giữ nguyên, ghi bất định, rà lại nếu các đoạn sau làm rõ.
- p000049: "mình" trong "tin mình sẽ được điều" là đại từ tự quy chiếu trong lời kể gián tiếp, phù hợp.
- Chưa có bằng chứng để thay "mình" bằng "tôi" hay lược bỏ.

## 4. Kiểm tra các sửa đổi khác (đều đạt)

p000045 ("Vừa mới đây"; "tin giao tranh đã nổ ra"), p000046 ("phía dưới chỗ Tanya", hết nhầm quy chiếu), p000047 ("màn quảng bá", "vượt trội hẳn"), p000048 ("giới chỉ huy cấp cao", "danh nghĩa chính đáng" đồng bộ b03 p000043), p000049 ("một người tốt, tử tế"), p000050 ("hoàn toàn không phản đối", "món hời"), p000052 ("nhận quân hàm sĩ quan"), p000054 ("được vinh danh và khen thưởng nhiều lần", không suy thành huân chương). Nghĩa khớp nguồn, không thêm/bớt đáng kể. p000053 không đổi và không có lỗi.

## 5. Phát hiện còn lại (nhẹ)

| Mức | Mã đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| nhẹ | p000044 | "được chứng kiến" gợi sắc thái may mắn/được ban; nguồn chỉ nói chứng kiến. | "như đang chứng kiến" (0,6). Tùy chọn. |
| nhẹ | p000049 | "các người" (số nhiều) cho nhà nước chưa có mục riêng trong sổ pending; ghi chú đã nêu là cách gọi tạm. | Coordinator thêm mục tạm (0,5); thay thế "cái đất nước này". |
| nhẹ | p000054 | "nhiều lần" thêm tần suất; nguồn chỉ nói giành nhiều vinh dự (accumulate). Ảnh hưởng nhỏ. | Giữ hoặc bỏ "nhiều lần". Tùy chọn. |
| nhẹ | quy ước | Đại từ "nó" ở b04 khác lặp tên/lược chủ ngữ ở b02–b03; mục sổ pending ghi việc rà đồng bộ "theo quyền sửa riêng". | Coordinator quyết định sau; không chặn b04. |

## 6. Thuật ngữ — vẫn là đề xuất tạm

Đối chiếu mục `chapter1_b04_claude_decisions`: 17 mục đều `status: pending`, `provisional_non_canon`, có độ tin cậy, khớp bản dịch (giới chỉ huy cấp cao, màn quảng bá, danh nghĩa chính đáng, nhận quân hàm sĩ quan, được vinh danh và khen thưởng, Liên minh Entente Regadonia, Lãnh thổ Norden, Chiến tranh Vùng Vịnh, huấn luyện thực địa, nhà nước quân sự, bậc lương, pháp sư bé gái, lực lượng thiết giáp, phóng viên chiến trường, truyền thông đại chúng, Being X, nó/mình). Không có mục nào bị nâng thành canon. Khuyến nghị còn mở: thêm "các người" (p000049); đồng bộ "Lãnh thổ Norden" với "mặt trận Norden" khi chốt; "giới chỉ huy cấp cao"/"màn quảng bá"/"được vinh danh và khen thưởng" tin cậy 0,5.

## 7. Rủi ro

- Điểm nhìn p000051/p000054 chưa rõ người nói (0,55); đại từ "nó" lệch b02–b03 (coordinator).
- Nguồn có ngắt cảnh trước p000044; JSONL không biểu diễn, cần giữ khi dựng bản.
- Chưa chạy validator và diff-check; chưa mở EPUB/PDF.

```yaml
role: reviewer
task_id: vol-01-ch-01-b04-review-fixes-followup
state: done
review_path: reviews/prose/vol-01-ch-01-b04-followup-claude.md
segment_ids: [p000044, p000045, p000046, p000047, p000048, p000049, p000050, p000051, p000052, p000053, p000054]
files_written: [reviews/prose/vol-01-ch-01-b04-followup-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 0, minor: 4}
unresolved_findings: []
term_recommendations: [thêm mục tạm cho "các người" ở p000049 (0,5), "Lãnh thổ Norden" đồng bộ với "mặt trận Norden", giữ nó/mình theo DEC-P01-001 và rà đồng bộ b02-b03, các mục tin cậy 0,5 vẫn là đề xuất tạm]
risks: [điểm nhìn p000051/p000054 chưa rõ người nói (0,55), đại từ nó lệch quy ước b02-b03 chờ coordinator, ngắt cảnh trước p000044 không biểu diễn trong JSONL, chưa chạy validator]
commit: null
next_action: coordinator chạy validator và git diff --check rồi commit b04; ghi mục "các người" vào sổ pending và đưa việc đồng bộ đại từ b02-b03 vào kế hoạch riêng
```
