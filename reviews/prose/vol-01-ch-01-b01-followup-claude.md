# Phản biện follow-up b01 — vol-01 Chapter 1

Người phản biện: Claude. Task: `vol-01-ch-01-b01-review-followup`. Mã đoạn viết tắt: `A/pNNNNNN` = `YS-LN01/Text/chapter003.xhtml/pNNNNNN`; `B/pNNNNNN` = `YS-LN01/Text/chapter003b.xhtml/pNNNNNN`. Báo cáo không chép câu nguồn; chỉ dùng mã đoạn và thuật ngữ ngắn để nhận diện.

Đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, `handoffs/vol-01/review-ch-01-b01-followup.yml`, `handoffs/vol-01/revision-ch-01-b01.yml`, gói nguồn b01 (đọc tại chỗ), `translations/vol-01/ch-01-b01.jsonl`, báo cáo đầu `reviews/prose/vol-01-ch-01-b01-claude-review.md`, `work/run-state/pending-terms.yml`.

**Tính chất:** các lựa chọn là phương án tạm theo AGENTS.md, không phải canon. Không sửa bản dịch, canon, handoff hay sổ pending. Không có hard stop; không có quyết định ảnh hưởng cốt truyện. Validator/diff_check: not_run; commit: null.

## 1. Cấu trúc

- 19/19 đoạn còn nguyên, đúng thứ tự, `status: draft`; `source_sha256` và `glossary_version` khớp handoff và gói nguồn.
- Nhấn mạnh DEC-P01-002 giữ đúng hai chỗ (A/p000002, B/p000001); B/p000001 đã chuyển sang nhấn mạnh sự khẳng định, đúng đề xuất.
- "Mình" cho nội tâm nhất quán, kể cả B/p000009 (đã bỏ "em ấy").

## 2. Xác nhận sáu phát hiện vừa trước đó

| Mã đoạn | Kết quả | Ghi chú |
|---|---|---|
| A/p000006 | Đã giải quyết | Chuyển sang tốc độ mặt đất vừa phải; bỏ "ổn định" và "bay ngang". |
| A/p000008 | Đã giải quyết | "Pháp sư quan sát" + "cảnh giác" một lần; khớp "quan sát viên pháo binh" ở A/p000006 và B/p000004. |
| B/p000001 | Đã giải quyết | "Thể chất trời phú ở đời trước"; không còn gợi nở nang, không suy ra thể hình khác. |
| B/p000003 | Đã giải quyết | Lệnh chỉ còn tiến hành nhiệm vụ được giao, không mâu thuẫn B/p000002. |
| B/p000005 | Đã giải quyết, còn ghi rủi ro | Dùng "không phát hiện địch" (lựa chọn tạm 0,55), giữ lặp "xin nhắc lại", không thu hẹp thành không phận. Xem rủi ro R1. |
| B/p000009 | Đã giải quyết | "Bé gái ấy" trung tính, không gán quan hệ thân thuộc; phù hợp DEC-P01-001. |

Không còn lỗi vừa hay nghiêm trọng trong văn bản dịch.

## 3. Các lỗi nhẹ đã sửa (đối chiếu nhanh)

A/p000001 (mặt trận Norden, Năm Thống nhất), A/p000002 (ý thức được gán danh tính), A/p000005 (thuật thức, "quả cầu" nhất quán, sắc thái trớ trêu bệnh hoạn khôi phục), A/p000007 (lược đại từ), B/p000001 (đời trước), B/p000004 (đúng là chẳng ai bằng; đẩy đến tận cùng logic), B/p000006/p000008 (hô hiệu thay mật danh), B/p000007 (khai thác thay bóc lột), B/p000010 (giọng điệu công vụ). Không phát hiện lỗi nghĩa mới do các sửa này. Thuật ngữ quân sự/ma pháp nhất quán trong b01: thiếu úy ma pháp, quả cầu tính toán, thuật thức, kỹ thuật ma pháp, quan sát viên pháo binh, pháp sư quan sát, pháp sư không quân, bộ phận kiểm soát không phận, Quân đoàn Lâm thời, Bộ Tổng Tham mưu.

## 4. Vị trí ghi chú (notes)

Phần lớn đã về đúng đoạn: A/p000002, A/p000005, A/p000006, A/p000008, B/p000001, B/p000004, B/p000006, B/p000008, B/p000009, B/p000010. Còn hai chỗ chưa sạch (xem phát hiện N1, N2). Ghi chú không ảnh hưởng văn bản dịch.

## 5. Mâu thuẫn nguồn Goliath 07

Bản dịch giữ trung thực hai đoạn khác nhau (B/p000006 và B/p000008), không hòa giải; ghi chú B/p000006 và sổ pending (`pending_source_discrepancy`, `preserved_without_harmonization`) đều nêu là chưa giải quyết. Xác nhận đạt. Đề nghị bổ sung tham chiếu chéo ở ghi chú B/p000008 (N3).

## 6. Phát hiện (đều nhẹ)

- **N1 — B/p000005.** Ghi chú vẫn nói về kiểm soát không phận và bình định, hai thuật ngữ không có ở đoạn này (chúng thuộc B/p000006). Thiếu ghi chú về quyết định "không phát hiện địch" (P01-all-clear). **Đề xuất:** thay bằng ghi chú all-clear → "không phát hiện địch", phương án thay thế "khu vực an toàn", độ tin cậy 0,55.
- **N2 — B/p000007.** Ghi chú có "Provisional Corps → Quân đoàn Lâm thời", nhưng thuật ngữ này không có ở đoạn này (thuộc B/p000008, đã có ghi chú đúng). **Đề xuất:** bỏ mục thừa.
- **N3 — B/p000008.** Ghi chú chưa nhắc mâu thuẫn Goliath 07 (chỉ có ở B/p000006). **Đề xuất:** thêm tham chiếu chéo, giữ nguyên không hòa giải.
- **N4 — sổ pending.** (a) Khối `chapter1_b01_pending_terms` cũ vẫn ghi "công thức" và "pháp sư trinh sát cảnh giới", đã bị thay thế bởi khối follow-up nhưng chưa đánh dấu superseded. (b) Tham chiếu đoạn lệch: `P01-call-sign` ghi A/p000008 (thực tế B/p000006 và B/p000008); `P01-norden-control` ghi B/p000010 (thực tế A/p000004, A/p000007, B/p000003); `P01-child-soldier` ghi B/p000010 (thực tế B/p000009). Phần (b) bắt nguồn từ báo cáo đầu của chính reviewer; ghi nhận lỗi này. **Đề xuất cho coordinator:** sửa tham chiếu và đánh dấu superseded; reviewer không sửa sổ.

## 7. Rủi ro

- **R1 (B/p000005 và B/p000010):** "không phát hiện địch" ở B/p000005 và xác nhận bộ binh địch tiến ở B/p000010 có thể bị đọc là mâu thuẫn nếu coi báo cáo ở B/p000005 là tuyệt đối. Nguồn không nêu phạm vi (không phận hay mặt đất); không tự thu hẹp. Độ tin cậy thấp (0,55); không ảnh hưởng cốt truyện.
- **R2:** mâu thuẫn Goliath 07 phải giữ đến khi có thêm đoạn sau hoặc quyết định của người dùng; mọi thuật ngữ vẫn là đề xuất, không phải canon.
- **R3:** sổ pending lệch tham chiếu (N4) có thể làm lệch việc áp dụng nhất quán ở lô sau nếu không sửa.

## 8. Kết luận

b01 follow-up đạt: 6/6 lỗi vừa đã giải quyết, mâu thuẫn nguồn được bảo toàn, thuật ngữ nhất quán với lựa chọn tạm. Còn 4 lỗi nhẹ về ghi chú và sổ, không chặn hoàn tất lô ngoài việc coordinator xác nhận validator, diff_check và commit.

counts: {nghiêm_trọng: 0, vừa: 0, nhẹ: 4}
unresolved_findings: [B/p000005 (N1), B/p000007 (N2), B/p000008 (N3), pending-ledger (N4)]
term_recommendations: [không đề xuất thuật ngữ mới; đánh dấu superseded "công thức" và "pháp sư trinh sát cảnh giới"; giữ "hô hiệu", "thuật thức", "pháp sư quan sát", "đời trước"]
