# Signoff b14 fixes — vol-02-ch-02-b14-final-signoff

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích văn bản nguồn.
- **Phạm vi:** p000354, p000357, p000374, p000381–p000389, p000391 (13 đoạn, tiền tố `YS-LN02/Text/part0014.xhtml/`). Đối chiếu với báo cáo review b14 trước, handoff, gói nguồn đã chuẩn bị, `translations/vol-02/ch-02-b14.jsonl`, mục `chapter2_b14_translation_proposals` và các mục cấp bậc Serebryakov trong ledger. Ngoài ra chỉ đọc p000369, p000373, p000375, p000378–p000380 để kiểm tra nhất quán thuật ngữ. Không đọc batch dịch khác.
- **Kiểm tra cơ học:** 38/38 đoạn, `notes` rỗng, status `draft`. Handoff ghi `translator_followup` done và 13 đoạn đã đổi, khớp phạm vi yêu cầu.

## Kết luận: `approved` (serious 0, moderate 0, minor 2)

## Xác nhận MOD-1 đến MOD-5

| ID | Kết quả | Căn cứ |
|---|---|---|
| MOD-1 | Đã giải quyết | p000374 và p000385 được bọc `*...*` toàn đoạn. p000391 chỉ nhấn đúng một từ "hỗn loạn". Khớp nhấn mạnh trong XHTML nguồn (p000374, p000385 nghiêng toàn đoạn; p000391 một từ). p000378 và p000387 không thêm nhấn mạnh, đúng. |
| MOD-2 | Đã giải quyết | Trần thuật về Tanya (p000381–p000389) không còn "cô"; dùng lặp tên Tanya hoặc lược chủ ngữ. p000381 lặp tên Serebryakov nên không lẫn người nói. p000391 nội tâm dùng "Mình". p000387 gọi "Thiếu tá". Không dùng "nó" nhưng báo cáo trước đã chấp nhận "lặp tên hoặc lược chủ ngữ". |
| MOD-3 | Đã giải quyết | p000381 dùng "Thiếu úy Serebryakov", khớp ledger. |
| MOD-4 | Đã giải quyết | p000357 chuyển thành "Mục tiêu của họ là ném bom một kho nhiên liệu"; không còn nghĩa sự kiện đang diễn ra. |
| MOD-5 | Đã giải quyết | p000354 có chủ thể trung tính "phía đối phương" và "hậu thuẫn" (backup), đúng lựa chọn trong ledger, không suy diễn danh tính. |

## Nhất quán thuật ngữ tạm (provisional, không phải canon)

- **sóng giám sát:** p000381, p000383, p000384 thống nhất, khớp ledger. Các sửa m9/m10 đã áp dụng (sóng "bị ngắt", "phát ra sóng giám sát mạnh liên tục").
- **thuật thức oanh kích ma pháp:** p000373, p000379 thống nhất. p000380 dùng "Oanh kích ma pháp" cho bản thân đòn đánh, hợp lý, không mâu thuẫn.
- **đoàn tàu giám sát mặt đất:** p000384, khớp ledger.
- **phía đối phương; hậu thuẫn:** p000354, khớp ledger.
- **Thiếu úy (Serebryakov):** khớp ledger.
- **Đại từ Tanya:** trần thuật không dùng "cô"; nội tâm dùng "mình". "cô ta" dành cho Named (p000373, p000375) giữ như cũ.

## Minor còn lại (không chặn, không bắt buộc sửa)

- **m-A — p000354:** "họ" đứng ngay sau "phía đối phương" có thể bị đọc nhầm là phía đối phương đang tính rút lui, trong khi chủ thể rút lui là phía Thịnh vượng chung. Câu sau ("mình đã hy sinh") giúp tháo nhầm lẫn. Nếu sửa, đổi "họ" thành "phía Thịnh vượng chung" hoặc "bên này". Độ tin cậy 0,35.
- **m-B — p000388:** "kiểm soát viên" còn khác "Người điều khiển" (p000373) và "đơn vị điều khiển" (p000384, p000369). Đây là m8 cũ, ngoài danh sách MOD, nên không phải điều kiện signoff. Nên thống nhất ở lượt rà đồng bộ chương. Độ tin cậy 0,45.

## Rủi ro

- Các lựa chọn thuật ngữ trên vẫn là tạm thời (`provisional_non_canon`); không tự nâng thành canon.
- Handoff `review_coordination.translator_followup_segments` liệt kê 11 đoạn, thiếu p000383 và p000384 so với `translator_followup.changed_segments` (13 đoạn). Chỉ là sai lệch ghi chép, không ảnh hưởng bản dịch.
