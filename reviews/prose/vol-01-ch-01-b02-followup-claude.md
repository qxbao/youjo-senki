# Phản biện tiếp theo — vol-01 Chương 1, lô b02

Người phản biện: Claude. Task: `vol-01-ch-01-b02-review-followup`. Phạm vi: 17 đoạn p000012–p000028, tiền tố đầy đủ `YS-LN01/Text/chapter003b.xhtml/`. Báo cáo không chép câu nguồn; chỉ dùng mã đoạn và thuật ngữ nguyên gốc ngắn để nhận diện.

Đầu vào đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, handoff follow-up, gói nguồn b02 (đọc tại chỗ), bản dịch b02 sau chỉnh sửa, báo cáo đầu `vol-01-ch-01-b02-claude-review.md`, `work/run-state/pending-terms.yml`, báo cáo quyết định tạm ch-00, `canon/glossary-pending.yml`, `canon/style-guide.md`.

**Tính chất:** mọi phương án là đề xuất tạm theo AGENTS.md, không phải canon. Không sửa bản dịch, canon, handoff hay sổ pending. Validator/diff_check: not_run; commit: null. Chỉ ghi tệp này.

## 1. Kết luận

- Không có hard stop. Số phát hiện còn lại: nghiêm trọng 0, vừa 0, nhẹ 4.
- Cả sáu phát hiện vừa của báo cáo đầu (M1–M6) đã được xử lý đúng và đã xác nhận trong bản dịch hiện tại (mục 2).
- Dấu chú thích ICBM, đại từ Tanya, thuật ngữ pháo binh và phạm vi nhấn mạnh đều đạt. Lô đủ điều kiện nâng sau khi chạy validator và diff-check, nếu coordinator xử lý các mục nhẹ N1–N2 ở mục 4.

## 2. Xác nhận sáu phát hiện vừa

| Mục | Mã đoạn | Kết quả | Ghi chú |
|---|---|---|---|
| M1 đại từ Tanya | p000013, p000026, p000027 | Đã sửa | Quét toàn lô không còn "cô" làm đại từ. Trần thuật ngôi ba dùng tên lặp hoặc lược chủ ngữ, nhất quán với b01 và DEC-P01-001. Nội tâm giữ "mình" (p000013, p000016–p000020). Các "nó" còn lại (p000020, p000024) chỉ công cụ/sức mạnh Đế quốc, không chỉ Tanya. |
| M2 chú thích | p000021 | Đã sửa | "⁴" ngay sau lần xuất hiện đầu của ICBM; lần nhắc lại không có dấu. Khớp nguồn (một chú thích, số 4) và quy ước chỉ số trên ở ch-00. |
| M3 nhấn mạnh | p000027 | Đã sửa | Chỉ một cặp `*...*`, bọc đúng từ được nhấn trong nguồn ("nhỏ tuổi"); trạng từ đi trước không còn bị nhấn. Không có nhấn mạnh thừa ở đoạn khác. Đúng DEC-P01-002. |
| M4 sắc thái | p000027 | Đã sửa | (a) chủ thể của việc ví von rõ là "người ta", sắc thái chê gắn vào cách ví. (b) "thật đấy" đứng giữa hai dấu gạch như lời nhấn, không còn là phủ định tự sửa. |
| M5 ca trực | p000028 | Đã sửa | "mặc trang bị rồi vào ca trực cách đây hai mươi tư giờ"; mốc 24 giờ và 48 giờ vẫn đúng. |
| M6 pháo binh | p000012, p000014, p000015 | Đã sửa | Xem mục 3. |

## 3. Thuật ngữ pháo binh, chức danh và tên cơ quan

- p000012: "khẩu pháo chuẩn" + "bắn hiệu chỉnh" khớp quyết định `b02-base-piece`.
- p000014: "Bắn hiệu lực" khớp `b02-fire-for-effect`; phần xác nhận điểm rơi và sai số mười mét giữ đúng.
- p000015: "nhiệm vụ bắn pháo", có "ngay"; mã gọi Goliath 07 nhất quán với p000012.
- Cặp bắn hiệu chỉnh / bắn hiệu lực nhất quán trong lô. Đề nghị dùng cho các cảnh pháo sau (vẫn là đề xuất).
- p000026: "Xưởng Vũ khí Kỹ thuật", "Bộ Tư lệnh Hậu cần" khớp ledger follow-up. "Chuẩn úy" ở p000026 và "thiếu úy" ở p000013/p000027 khớp nhau về mốc (cadet trước, phong thiếu úy sau).
- p000028: "lục quân biên giới" và "đơn vị biên chế" khớp ledger; "lục quân" ở p000027 và p000028 thống nhất. "học viện quân sự" (p000026, p000027) tách khỏi "trường đào tạo sĩ quan ma pháp" (p000028).
- Không có điểm đổi cốt truyện; không cần hỏi người dùng.

## 4. Phát hiện còn lại (nhẹ)

| # | Mã đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| N1 | p000012, p000013, p000014, p000015, p000026, p000027, p000028 | Trường `notes` của bản dịch vẫn ghi thuật ngữ cũ (khẩu pháo cơ sở, bắn hiệu quả, Kho Vũ khí Kỹ thuật, Bộ Chỉ huy Hậu cần) trái với bản dịch đã sửa; nhiều đoạn còn chép nguyên danh sách chung không liên quan nội dung đoạn. | Translator làm mới notes theo quyết định hiện hành hoặc rút gọn đúng đoạn; không ảnh hưởng văn bản xuất bản. |
| N2 | (sổ pending) | `chapter1_b02_pending_terms` vẫn giữ giá trị cũ, `chapter1_b02_claude_decisions` và `chapter1_b02_followup_decisions` lặp ý nhau; `chapter1_b02_followup_decisions` thiếu mục cho "chuẩn úy"/"thiếu úy" viết thường khi đứng riêng và cho cặp bắn hiệu chỉnh/bắn hiệu lực. | Coordinator đồng bộ ledger, ghi giá trị ưu tiên, đánh dấu giá trị cũ là superseded. Không đưa vào canon. |
| N3 | p000026 | Phần mở đầu lặp tên Tanya hai lần trong một câu; "thường có thể được điều về" vẫn mang sắc thái tần suất thay cho "thì bình thường sẽ" (m11a của báo cáo đầu, chưa áp dụng). | Tùy chọn: lược chủ ngữ ở vế sau; "thì bình thường Tanya sẽ được điều về…". Chấp nhận được nếu giữ nguyên. |
| N4 | p000028 | "Bổ nhiệm thẳng" cho "direct promotes" hơi lệch (nghĩa là lên thẳng từ trường, không qua đơn vị khác). | Tùy chọn: "những người lên thẳng từ…". Không bắt buộc. |

Các mục nhẹ khác của báo cáo đầu (m1–m13) phần lớn đã được áp dụng; còn lại chấp nhận được.

## 5. Rủi ro

- Phạm vi "giai đoạn này" của DEC-P01-001 vẫn do coordinator diễn giải; phương án hiện tại (lặp tên/lược chủ ngữ) trung tính nên không cần đổi nếu diễn giải rộng hơn.
- Tên cơ quan và "lục quân biên giới" chỉ dựa vào ngữ cảnh một đoạn; có thể đổi khi các đoạn sau nêu rõ chức năng. Tin cậy 0,5 như báo cáo đầu.
- Người nói ở p000012/p000015 suy từ mã gọi, không có nhãn tường minh (tin cậy 0,7).
- Chưa chạy validator và diff-check; chỉ quét thủ công bằng đoạn mã đọc bản dịch (không ghi tệp).

```yaml
role: reviewer
task_id: vol-01-ch-01-b02-review-followup
state: done
review_path: reviews/prose/vol-01-ch-01-b02-followup-claude.md
files_written: [reviews/prose/vol-01-ch-01-b02-followup-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 0, minor: 4}
unresolved_findings: [N1 notes cũ, N2 ledger chưa đồng bộ, N3 p000026 tùy chọn, N4 p000028 tùy chọn]
commit: null
next_action: coordinator đồng bộ ledger (N2), translator làm mới notes (N1); chạy validator và diff-check rồi commit/nâng lô
```
