# Xác nhận sửa lỗi — vol-02-ch-02-b02 (signoff)

- **Người phản biện:** Claude (chỉ ghi báo cáo; không sửa bản dịch, handoff, canon, ledger, run-state). Không trích văn bản nguồn.
- **Phạm vi:** p000025, p000026, p000043 (`YS-LN02/Text/part0014.xhtml/…`), đối chiếu `reviews/prose/vol-02/ch-02-b02-claude.md`, handoff, gói nguồn, bản dịch b02, mục `chapter2_b02_translation_proposals` trong `work/run-state/pending-terms.yml`. Chỉ đọc p000027, p000029, p000033 để kiểm tra nhất quán thuật ngữ.

## Kết luận

`pass`. serious = 0; moderate = 0; minor còn lại = các mục m1–m8 cũ (không bắt buộc).

## Xác nhận từng mục

- **M1 — đạt.** p000025 nay có `*Khoan đã.*`, đúng phạm vi câu ngắn mở đầu có nhấn mạnh trong nguồn; phần sau không bị đánh dấu thừa. Khớp DEC-P01-002.
- **M2 — đạt (tạm thời, không canon).** p000043 dùng “Đại công quốc”, viết hoa theo quy ước (chỉ âm tiết đầu), không tự thêm “Dacia”. Khớp ledger `vol02-ch02-b02-grand-duchy` (pending, 0.55). p000033 vẫn là “Công quốc Dacia” theo nguồn; việc hai danh xưng cùng chỉ một nước vẫn là suy luận ngữ cảnh, chưa phải xác nhận.
- **M3 — đạt.** homeland → “quê hương” ở cả p000025 và p000026; “home” → “mái nhà” (p000025) và “quê nhà” (p000026), cùng trường nghĩa, không còn nhập với “Tổ quốc”. fatherland → “Tổ quốc” giữ riêng (p000025 cuối, p000027, p000029). Khớp ledger `vol02-ch02-b02-homeland-vs-fatherland`.

## Kiểm tra bổ sung

- Hash nguồn và `glossary_version` của ba record khớp handoff; `status: draft`, `notes` rỗng; không có ghi chú làm việc lọt vào bản dịch.
- Không phát hiện lỗi nghĩa, phủ định, người nói hay thời gian mới do bản sửa.

## Minor còn mở (không chặn)

- m6 (p000043): “chẳng dễ chịu chút nào” vẫn nhẹ hơn nguồn so với “wretched”; có thể đổi “nghe thật tệ hại”. Các minor khác từ báo cáo trước (p000029/30/33/38/41) không thuộc phạm vi signoff này, chưa xác nhận lại.

## Rủi ro

- Grand Duchy = Dacia chỉ là suy luận; nếu batch sau nêu rõ thì coordinator rà lại ch01 và p000033/p000043.
- Mọi lựa chọn thuật ngữ (nghị viên, Đại công quốc, quê hương/Tổ quốc) vẫn là đề xuất, không nâng canon.
