# Signoff sửa lỗi b13 — vol-02-ch-02-b13-final-signoff

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích câu nguồn.
- **Phạm vi:** `p000329`, `p000330`, `p000335`, `p000338`, `p000341`, `p000342` (tiền tố `YS-LN02/Text/part0014.xhtml/`). `p000344` chỉ đối chiếu thuật ngữ "đơn vị hỗn hợp" với ledger. Đã đọc: báo cáo b13 ban đầu, handoff, gói nguồn đã chuẩn bị, `translations/vol-02/ch-02-b13.jsonl`, `work/run-state/pending-terms.yml` (mục `chapter2_b13_translation_proposals`). Không đọc batch khác.

## Kết luận: `approved_with_minor` (serious 0, moderate 0, minor 3)

Cả bốn MOD đã được xử lý. Không còn serious hay moderate.

## Kiểm tra MOD

- **MOD-1 (đại từ Named) — đã giải quyết.** p000335, p000341, p000342 đều dùng "Named này/đó" kèm "cô ấy"; không còn "nó" hay "con". Khớp lựa chọn `named` trong handoff (Named đó/này; cô ta hoặc cô ấy; tránh nó/con). Không suy diễn danh tính.
- **MOD-2 (p000330) — đã giải quyết.** Quan hệ "vì… nên…" được khôi phục, bỏ "quả thật" và dấu chấm phẩy; nghĩa nguyên nhân–hệ quả khớp nguồn.
- **MOD-3 (p000338) — đã giải quyết.** Dùng phương án trung lập theo đề xuất, bỏ "chỉ", không ép nghĩa "đúng/sai". Độ mơ hồ vẫn còn trong nguồn, xem m-A về ledger.
- **MOD-4 (p000329) — đã giải quyết.** "những người lão luyện trong công tác thu thập tình báo" khớp mục `vol02-ch02-b13-intelligence-gathering-veterans`; không còn mâu thuẫn với p000333/p000336. p000344 "đơn vị hỗn hợp" khớp mục `vol02-ch02-b13-composite-unit`.

## Minor còn lại

- **m-A — Ledger chưa ghi hết lựa chọn tạm.** `chapter2_b13_translation_proposals` chỉ có 2 mục (veterans, composite unit). Lựa chọn đại từ Named (MOD-1) và độ bất định ngữ nghĩa của p000338 (MOD-3, độ tin cậy 0,5) mới chỉ ghi ở handoff/báo cáo, chưa có trong ledger hay `pending-terms.yml`. Coordinator nên bổ sung hai mục `provisional_non_canon` (p000335/p000341/p000342 và p000338). Không ảnh hưởng bản dịch.
- **m-B — p000341:** nguồn có lời chửi ở cuối vế sau; bản dịch hiện bỏ hẳn sắc thái đó (trước đây là "tên khốn"). Mất chút giọng thoại; không đổi nghĩa. Tùy chọn: thêm "tên khốn đó" sau "cô ấy" hoặc thay chủ ngữ, nhưng cần giữ nhất quán đại từ.
- **m-C — p000342:** "có một Named đó" hơi gượng (nguồn là mạo từ bất định); cân nhắc "có một Named". Ngoài ra "trật lất" ở p000335 (m3 cũ) vẫn còn, chỉ là vấn đề văn phong.

## Rủi ro
Thấp. Các lựa chọn vẫn là đề xuất, chưa phải canon.
