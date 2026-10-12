# Báo cáo xác nhận sửa lỗi — vol-02-ch-02-b05-final-signoff

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger, run-state). Không trích văn bản nguồn.
- **Phạm vi:** p000093, p000096, p000100, p000101, p000108, p000109, p000112, p000117 (`YS-LN02/Text/part0014.xhtml/…`). Đối chiếu: báo cáo b05 trước, handoff b05, gói nguồn b05, bản dịch b05, canon, mục `chapter2_b05_translation_proposals` trong ledger. Không đọc batch khác.

## 1. Kết luận

- **Kết luận:** `pass`. serious = 0; moderate = 0; M1–M7 đều đã giải quyết.
- Handoff ghi `validator: pass`, `diff_check: pass`; reviewer không chạy lại.

## 2. Xác nhận từng mục

| ID | Đoạn | Kết quả |
|---|---|---|
| M1 | p000093 | Đã sửa: dùng “cơ động qua lại theo nội tuyến”, khớp đề xuất ledger `interior-lines`. |
| M2 | p000096 | Đã sửa: không còn đại từ giới tính hóa; dùng “binh lính dưới quyền mình”, nhất quán nội tâm. |
| M3 | p000101 | Đã sửa: lặp tên Tanya/Weiss, bỏ “cô”; nghĩa khớp nguồn (ra hiệu, nói không có gì đáng lo, bảo nói tiếp). |
| M4 | p000108 | Đã sửa: lời tưởng tượng lược đại từ, không còn xưng hô giới tính; phạm vi `*…*` vẫn đúng một cụm theo DEC-P01-002. |
| M5 | p000100 | Đã sửa: “lương hưu công chức lẫn lương hưu sĩ quan” giữ hai khoản, bỏ calque; khớp ledger `pension-categories`. |
| M6 | p000109, p000112 | Đã sửa: “Bộ Chỉ huy phương Bắc”, “do Trung ương điều đi”, “ở phía Bắc”; khớp ledger `northern-central-command` và tiền lệ. |
| M7 | p000117 | Đã sửa: “những người theo chủ nghĩa gia trưởng”, bỏ “kẻ”; khớp ledger `paternalism` (pending, confidence 0.5). |

Không có lỗi mới về nghĩa, phủ định, người nói hay nhấn mạnh trong 8 đoạn. Bản dịch vẫn `draft`, `notes` rỗng.

## 3. Minor còn lại (không chặn, tùy chọn)

- **m5 (p000108):** vẫn dùng “thuần hóa” cho từ trích dẫn; độ chắc thấp, chưa đối chiếu gốc Nhật.
- **m6 (p000109):** vẫn viết hoa “Cụm Tập đoàn quân phía Đông/Nam”, lệch ledger và p000114 (viết thường).
- **m10 (p000114, ngoài phạm vi sửa):** “các đạo quân khu vực” còn lệch thuật ngữ army.
- Các minor khác của báo cáo trước (m1–m4, m7–m9, m11) nằm ngoài 8 đoạn này, chưa được xác nhận ở đây.

## 4. Rủi ro

- Các thuật ngữ tạm (nội tuyến, Trung ương, lương hưu, gia trưởng) độ tin cậy 0.5–0.6, vẫn là đề xuất non-canon; nếu canon chốt khác phải đồng bộ mọi chỗ.
- Xưng hô Tanya xuyên batch chưa được kiểm tra (ngoài phạm vi).

## 5. Next action

Coordinator có thể đóng b05 và commit; cân nhắc xử lý minor ở bước dọn văn phong sau.
