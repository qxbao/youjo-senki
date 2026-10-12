# Ký xác nhận sửa lỗi b09 — vol-02-ch-02-b09-final-signoff

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích văn bản nguồn.
- **Phạm vi:** bốn đoạn translator đã sửa: p000195, p000210, p000215, p000217 (tiền tố `YS-LN02/Text/part0014.xhtml/`). Đối chiếu với báo cáo review b09 trước, handoff b09, gói nguồn đã chuẩn bị (sha256 khớp handoff: `1903dd…ebca`), `translations/vol-02/ch-02-b09.jsonl` và mục `chapter2_b09_translation_proposals` trong `work/run-state/pending-terms.yml`. Chỉ đọc thêm p000211 để kiểm tra MOD-2. Không đọc batch dịch khác.

## Kết luận: `approved` (serious 0, moderate 0, minor 0)

## Kiểm tra từng mục

### MOD-1 — thuật ngữ "formulas": đã xử lý
- p000195 dùng "né thuật thức"; p000215 dùng "thuật thức bắn tỉa tầm xa". Cả hai khớp phương án tạm `thuật thức` của ledger (`vol02-ch02-b09-formulas`).
- Ledger đã liệt kê đủ cả hai đoạn p000195 và p000215 trong `segment_ids` (phần thiếu p000215 ở báo cáo trước đã được bổ sung). Không còn "phép thức" trong hai đoạn.
- Nghĩa, phủ định và điều kiện của hai câu không đổi. Phần nhấn mạnh ở p000215 vẫn khớp nguồn: chỉ cụm thoại nội tâm nằm trong `*...*`, đúng DEC-P01-002.

### MOD-2 — p000210: đã xử lý
- Bản dịch hiện là "số lượng và chúng ở hướng nào". Câu hỏi quay về vị trí/phương vị, không còn thêm ý "hướng bay".
- Khớp câu trả lời ở p000211 ("hướng hai giờ" theo góc nhìn của bên báo cáo). Nguồn hỏi hướng một cách mở; bản dịch giữ độ mở đó.

### Kho Kraggana — p000217: đã khớp
- Bản dịch dùng "Kho Kraggana", khớp `proposed_vi` của mục `vol02-ch02-b09-kraggana-depot` (pending, `segment_ids` = p000217). Không còn tự thêm "tiếp tế".
- Phương án thay thế được ghi trong ledger. Mục vẫn là đề xuất, chưa nâng thành canon (`canon/` chưa có mục Kraggana). Đúng quy trình.
- Phủ định/ý "tránh để bị ném bom" giữ nguyên.

### Kiểm tra phụ
- `segment_id` và `source_sha256` của bốn đoạn khớp gói nguồn; `status` vẫn là `draft`.
- Handoff ghi `changed_segments` đúng bốn đoạn, và `resolved_moderate` = MOD-1, MOD-2.
- Mục ledger `vol02-ch02-b09-air-supremacy-battles` hiện trỏ đúng `part0014.xhtml/p000202` (minor m8 cũ đã được sửa).
- Không phát hiện lỗi mới do bản sửa gây ra.

## Rủi ro còn lại (không chặn)
- Ba thuật ngữ b09 (thuật thức, ưu thế trên không, Kho Kraggana) vẫn là `pending`/`provisional_non_canon`. Nếu sau này canon chốt từ khác thì phải đồng bộ lại các đoạn liên quan.
- Các minor m1–m7 còn lại của báo cáo trước (p000190, p000197, p000202, p000206, p000212, p000219) không nằm trong lượt sửa này và không được ký xác nhận ở báo cáo này. Chúng không chặn.
- Handoff liệt kê p000202 trong `translator_followup_segments` nhưng `changed_segments` không có p000202. Phạm vi ký xác nhận này chỉ gồm bốn đoạn được giao.

## Bước tiếp theo
Coordinator đóng batch b09 và ghi trạng thái ký xác nhận vào handoff/checkpoint. Giữ các mục pending ở dạng đề xuất.
