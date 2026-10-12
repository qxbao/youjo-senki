# Signoff sau sửa b11 — vol-02-ch-02-b11-final-signoff

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích câu nguồn.
- **Phạm vi:** 11 đoạn `YS-LN02/Text/part0014.xhtml/` p000258, p000259, p000263, p000264, p000265, p000271, p000280, p000283, p000295, p000297, p000298. Đã đối chiếu: báo cáo `ch-02-b11-claude.md`, handoff b11, gói nguồn đã chuẩn bị (sha256 gói khớp handoff: 474d499a…), `translations/vol-02/ch-02-b11.jsonl`, ledger `work/run-state/pending-terms.yml` (mục `chapter2_b11_translation_proposals`, b06/b10 đơn vị, b06 cơ động, b09 thuật thức). Không đọc batch dịch khác.
- **Cơ học:** `notes` rỗng ở cả 11 đoạn; không có ghi chú làm việc lẫn vào bản dịch.

## Kết luận: `approved` — serious 0, moderate 0

## M1–M7
| ID | Đoạn | Kết quả |
|---|---|---|
| M1 | p000258 | Đã sửa: tên đơn vị theo ledger b06/b10 (Pháp sư Không quân 203); hết nghĩa "vận tải". |
| M2 | p000258 | Đã sửa: nháy đơn đóng cụm hiệu gọi, nháy kép đóng sau tiếng ngập ngừng; ngoặc cân bằng. |
| M3 | p000263 | Đã sửa: nghiêng hai câu đầu, nghiêng hai từ đối lập ấn tượng/quá; "tự phụ" đổi thành "tự tin" (cũng xử lý m3). Đúng DEC-P01-002. |
| M4 | p000271 | Đã sửa: cụm bị nuốt lại dùng `*...*`, hết ngoặc kép. |
| M5 | p000265 | Đã sửa: giữ nghĩa bị buộc/được mong đợi, chủ thể "họ" bỏ mơ hồ đúng như đề xuất. Từ "Chẳng lẽ" thêm sắc thái tu từ nhẹ, chấp nhận được. |
| M6 | p000297 | Đã sửa: "thuật thức gây nhiễu", khớp ledger b09/b02 và mục b11-interference-formulas. |
| M7 | p000264 | Đã sửa: "cơ động cấp tốc" thay "hành quân cưỡng bức"; "Có vẻ" thay "Rõ ràng"; hết "đang tấn công". |

## Thuật ngữ minor đã chọn — khớp ledger
- **call sign** (p000259): "hiệu gọi" — khớp `vol02-ch02-b11-call-sign`.
- **đơn vị độ cao** (p000280, p000283): "feet", không quy đổi, không thêm đơn vị vào số trần — khớp `vol02-ch02-b11-height-unit`. Không còn "foot" trong b11 (đã grep trên bản dịch b11).
- **death zone** (p000295): "vùng chết" — khớp `vol02-ch02-b11-death-zone`.
- **Republican Army contact** (p000298): "đầu mối trong Quân đội Cộng hòa" — khớp `vol02-ch02-b11-republican-army-contact`.

## Minor còn lại (không chặn)
- **s1 — p000264:** vị trí "Có vẻ" trước chủ ngữ khiến phạm vi nghi vấn hơi mơ hồ, đọc hơi dài; nguồn mạnh hơn "có vẻ" một chút. Đề xuất nếu tiện: "Một tiểu đoàn tấn công vừa tới sau chặng cơ động cấp tốc thì có vẻ khó lòng tự mình xử lý nổi chuyện đó." Độ tin cậy 0,4.
- **s2 — p000280:** m8 chưa áp dụng ("Có thể dữ liệu ghi kỷ lục là…" vẫn đọc như khả năng; "hợp lý" hơi yếu cho "theo lẽ thường"). Không đổi nghĩa chính.
- **s3 — p000295/p000297:** "Kẻ" (m12) vẫn dùng; sắc thái hạ thấp nhẹ, chưa chốt thống nhất. p000298: "cười nhạo" và "đang say rượu" (m13) chưa chỉnh.
- Các minor khác của báo cáo gốc nằm ngoài 11 đoạn này, không xét lại.

## Rủi ro
- Không còn rủi ro chặn commit trong phạm vi 11 đoạn. Các lựa chọn thuật ngữ vẫn `provisional_non_canon`, chưa nâng thành canon.
- Handoff ghi `risk_flag` đơn vị feet đang chờ review; có thể gỡ cờ sau signoff này (việc của coordinator).

## Bước tiếp theo
Coordinator đóng cờ `risk_flag`, có thể cho commit b11 (minor s1–s3 tùy chọn).
