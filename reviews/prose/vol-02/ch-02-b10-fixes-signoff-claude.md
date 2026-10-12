# Signoff b10 fixes — vol-02-ch-02-b10-final-signoff

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích văn bản nguồn.
- **Phạm vi:** `p000221`, `p000233`, `p000235`, `p000237`, `p000253` (tiền tố `YS-LN02/Text/part0014.xhtml/`). Đã đọc: báo cáo b10 trước, handoff b10, gói nguồn đã chuẩn bị, `translations/vol-02/ch-02-b10.jsonl`, ledger `chapter2_b10_translation_proposals` và mục b08 `viper-interior-self-reference`. Không xem batch dịch khác.
- **Cơ học:** 37/37 đoạn khớp gói nguồn; năm đoạn sửa đều giữ `segment_id`, `source_sha256`. Phạm vi chữ nghiêng ở p000235, p000237 (toàn đoạn) và p000253 (ba câu đầu, ba câu sau không nghiêng) vẫn khớp nguồn.

## Kết luận: `pass` (serious 0, moderate 0, minor 3 còn lại, không chặn)

## Xác nhận M1–M3
- **M1 / p000221 — đã giải quyết.** Bản sửa khôi phục quan hệ đồng thời (sự việc xảy ra đúng lúc nhân vật vừa nghĩ), bỏ đánh giá "đoán đúng/sai", dùng "anh" thay cho đại từ trần thuật dành riêng cho Tanya (DEC-P01-001). Tham chiếu "chuyện đó" giữ trung tính. Khớp mục ledger cùng nhóm với p000221.
- **M2 / p000233 — đã giải quyết.** Dùng "anh", bỏ "cậu" và bỏ "đi" mang sắc thái mệnh lệnh. Khớp `vol02-ch02-b10-cp-address-to-viper02` (`anh`) và nhất quán với cách xưng "các anh" của cùng người nói ở p000228. Không suy ra cấp bậc hay thân mật. "Named" giữ nguyên, khớp lựa chọn tạm.
- **M3 / p000235, p000237 — đã giải quyết.** Cả hai đoạn nội tâm Viper 02 dùng "mình" (p000235 "mình sẽ khui…"; p000237 hai lần "mình"), khớp `vol02-ch02-b08-viper-interior-self-reference` (`mình`). Không còn "tôi" trong nội tâm. "Chúng ta" trong cùng đoạn là ngôi gộp theo nguồn, không phải biến thể xưng hô.

## Central Army / p000253
Bản dịch dùng "Quân Trung ương", đúng lựa chọn tạm đã ghi (`vol02-ch02-b10-central-army`, confidence 0,45); không tái dùng "Tập đoàn quân" nên không trùng loại đơn vị với "Cụm tập đoàn quân". Vẫn là đề xuất, chưa phải canon.

## Minor còn lại (không chặn, không bắt buộc sửa)
- p000235 (m12): "mang theo món quà" vẫn đổi chủ thể so với nguồn (nguồn: chúng ta nhận món quà).
- p000253 (m13): "Dù không muốn buộc tội" vẫn mạnh hơn nguồn một chút (nguồn: chưa đến mức buộc tội).
- Các minor m1–m11 trong báo cáo trước ở đoạn ngoài phạm vi signoff này không được xét lại.

## Rủi ro
- Các lựa chọn Named, Central Army, "anh" (CP), "mình" (Viper 02) đều là phương án tạm, `pending`; cần rà lại khi truyện giải thích hoặc có thêm ngữ cảnh.
- Do giới hạn phạm vi, không xác nhận lại tính nhất quán ở các đoạn khác của b10 ngoài năm đoạn trên.

## Hành động tiếp theo
Coordinator có thể đóng signoff b10 (đủ điều kiện commit theo `review_coordination`), cập nhật ledger giữ nguyên trạng thái pending.
