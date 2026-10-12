# Signoff sửa lỗi — vol-02-ch-01-b06 (Claude)

- Task: `vol-02-ch-01-b06-fixes-signoff`. Vai trò: reviewer, không sửa bản dịch, handoff hay ledger.
- Phạm vi: 12 đoạn đã sửa của `YS-LN02/Text/part0010.xhtml`: p000121, p000122, p000126, p000128, p000129, p000131, p000132, p000134, p000135, p000137, p000151, p000152.
- Đầu vào đã dùng: báo cáo gốc `reviews/prose/vol-02/ch-01-b06-claude.md`, handoff b06, `translations/vol-02/ch-01-b06.jsonl`, source package `work/vol-02/batches/ch-01-b06-source.jsonl`. Không đọc bản dịch batch khác. Không chép nguồn (zero-source-quote). Mọi lựa chọn thuật ngữ vẫn là **đề xuất tạm, không phải canon**.
- Metadata 12/12 dòng: `notes: []`, `status: draft`. Chưa chạy validator hay diff_check (không thuộc phạm vi).

## Kết luận

**Fixes pass.** M1–M5 đều đã giải quyết; không còn lỗi nghiêm trọng hay vừa trong 12 đoạn đã sửa. Nghĩa, phủ định, chủ thể và nhấn mạnh khớp với nguồn ở cả 12 đoạn.

| Mức | Còn lại |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 0 |
| Nhẹ (có thể xử lý) | 5 |

## Kiểm tra M1–M5

| Mã | Trạng thái | Chứng cứ |
|---|---|---|
| M1 cấp bậc | **Đã giải quyết** | Serebryakov là "Thiếu úy" ở p000126, p000129 (lời gọi), p000134, p000137. Weiss là "Trung úy" ở p000122, p000134 (câu giới thiệu), p000131. Không còn đoạn nào gọi hai người cùng cấp. |
| M2 đại từ trần thuật Tanya | **Đã giải quyết** | Hết "nó" và "cô" chỉ Tanya. Dùng tên "Tanya" hoặc lược chủ ngữ ở p000121, p000122, p000128, p000129, p000135, p000137. "mình" ở p000122/p000128 là phản thân hoặc sở hữu, trung tính. Ở p000135, "Tanya" lặp hai lần trong một câu hơi nặng nhưng đúng phương án đã đề xuất. |
| M3 chủ thể p000132 | **Đã giải quyết** | Câu đã tách. "Rồi tôi nổ súng." nêu rõ người bắn là người kể, không còn đọc được thành quân Dacia nổ súng. |
| M4 mình/tôi | **Đã giải quyết** | Suy nghĩ nội tâm dùng "mình" ở p000131 (ba chỗ) và p000152. Hành động dùng "tôi" ở p000131 (ra lệnh) và p000132 (phong ấn, nổ súng). Xem nhẹ m5 về một câu lai ở p000132. |
| M5 tên tài liệu | **Đã giải quyết** | p000151 dùng "Sổ tay … dã chiến, bản thứ hai mươi hai". p000152 chỉ dùng "sổ tay" (hai lần). Hết "thủ lệnh" và "tập". Nghĩa "manual" đã sát hơn. |

## Nhấn mạnh (DEC-P01-002)

Nguồn trong 12 đoạn có 1 chỗ nhấn mạnh (p000151, toàn bộ tên tài liệu), bản dịch có 1 cặp `*…*` cùng phạm vi, dấu ngoặc kép nằm ngoài. 11 đoạn còn lại không có nhấn ở nguồn và không có `*`. Chữ hoa ở p000131 được giữ. **Khớp 1/1, không thừa.**

## Nghĩa và sắc thái ở các đoạn đã sửa

Không phát hiện lệch nghĩa, mất phủ định hay đảo người nói. Giọng giận của Tanya ở p000129 và p000137 còn nguyên. Chỉ có các lỗi nhẹ bên dưới.

## Lỗi nhẹ còn lại (chưa bắt buộc, nên xử lý ở lượt chỉnh văn sau)

Các mục này chưa được xử lý trong lượt sửa M1–M5, đã có trong báo cáo gốc (L4, L6, L7, L12) trừ m5.

1. **m1 — p000129 ("hắn" ×2):** "hắn" thêm sắc thái miệt thị cho Weiss, lệch với "anh ta" ở p000131 và p000137. Gợi ý: "anh ta".
2. **m2 — p000132 ("thầm cảm ơn"):** "thầm" không có ở nguồn. Gợi ý: "Tôi cảm ơn…".
3. **m3 — p000132 ("đạn ma thuật"):** lệch "ma pháp" dùng ở p000151 và trong sổ. Gợi ý: "đạn ma pháp". Cụm "công thức nổ liên hợp" vẫn chờ ledger chốt "công thức" hay "thuật thức"; giữ nguyên, không tính lỗi.
4. **m4 — p000137 ("sầm sập"):** thêm hàm ý tiếng động, nguồn chỉ nói áp sát. Gợi ý: "áp sát". Câu đầu đoạn ("Ngay cả cuộc trao đổi vẫn tiếp diễn…") hơi vụng; có thể gọn thành "Ngay cả việc họ còn trao đổi cũng khiến Tanya bực mình".
5. **m5 — p000132 (câu lai mình/tôi):** "Ít nhất, tôi muốn chuyển hóa cơn giận…" là mong muốn nội tâm nhưng dùng "tôi", trong khi cấu trúc tương tự ở p000152 dùng "mình". Chấp nhận được vì cùng câu có hành động "phong ấn". Nếu muốn nhất quán chặt: "Ít nhất, mình muốn chuyển hóa cơn giận… nên tôi phong ấn…". Tùy coordinator.

## Rủi ro

- **R1:** Đồng bộ chéo toàn chương (cấp bậc Serebryakov, trần thuật Tanya, mình/tôi, ma pháp/ma thuật) vẫn phụ thuộc cách b01–b05 áp dụng; tôi không đọc các batch đó.
- **R2:** Quy tắc "mình cho nội tâm, tôi cho hành động" là phỏng đoán về ranh giới ở câu lai (m5), độ bất định trung bình.
- **R3:** p000141 (sĩ quan phụ tá) vẫn giữ literal, ngoài phạm vi signoff này.

## Báo cáo coordinator

```yaml
role: reviewer
task_id: vol-02-ch-01-b06-fixes-signoff
state: done
segment_ids: [p000121, p000122, p000126, p000128, p000129, p000131, p000132, p000134, p000135, p000137, p000151, p000152]
files_written: [reviews/prose/vol-02/ch-01-b06-fixes-signoff-claude.md]
review_path: reviews/prose/vol-02/ch-01-b06-fixes-signoff-claude.md
validator: not_run
diff_check: not_run
fixes_pass: true
resolved: {M1: true, M2: true, M3: true, M4: true, M5: true}
emphasis: {source: 1, translation: 1, status: match}
counts: {serious: 0, moderate: 0, minor: 5}
minor_findings:
  - {id: m1, segment_id: p000129, issue: "hắn thêm sắc thái miệt thị", suggestion: "anh ta"}
  - {id: m2, segment_id: p000132, issue: "thầm không có ở nguồn", suggestion: "bỏ thầm"}
  - {id: m3, segment_id: p000132, issue: "đạn ma thuật lệch ma pháp", suggestion: "đạn ma pháp"}
  - {id: m4, segment_id: p000137, issue: "sầm sập thêm hàm ý tiếng động; câu đầu vụng", suggestion: "áp sát; gọn câu đầu"}
  - {id: m5, segment_id: p000132, issue: "câu lai: mong muốn nội tâm dùng tôi", suggestion: "mình muốn…, nên tôi phong ấn… (tùy coordinator)"}
pending_terms: provisional_non_canon
term_status:
  serebryakov_rank: Thiếu úy
  weiss_rank: Trung úy
  tanya_third_person_narration: repeat Tanya or omit subject
  tanya_interior_self_reference: mình; tôi for narrated action
  aerial_magic_combat_field_manual: "Sổ tay tác chiến ma pháp không quân dã chiến, bản thứ hai mươi hai; p000152 sổ tay"
risks: [R1, R2, R3]
commit: null
next_action: coordinator_accept_signoff_then_commit_b06; minors m1-m5 optional (batch into a later polish pass)
```
