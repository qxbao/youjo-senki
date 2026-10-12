# Review b09 — vol-02-ch-02-b09-review

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích câu nguồn.
- **Phạm vi:** 31 đoạn `YS-LN02/Text/part0014.xhtml/p000190`–`p000220` (dưới đây viết tắt `pNNNNNN`). Đã đọc: handoff b09, gói nguồn đã chuẩn bị, `translations/vol-02/ch-02-b09.jsonl`, `canon/` (glossary, characters, style-guide, decisions, glossary-pending) và ledger `work/run-state/pending-terms.yml` (mục `chapter2_b09_translation_proposals` cùng các mục liên quan đến "formulas"/"air supremacy"). Không đọc batch dịch khác.
- **Kiểm tra cơ học:** 31/31 đoạn, thứ tự, `segment_id` và `source_sha256` khớp gói nguồn. Chữ nghiêng (DEC-P01-002) khớp nguồn ở cả 7 đoạn có nhấn mạnh: p000192, p000197, p000207, p000215, p000216 (chỉ cụm sau "Nói cho cùng"), p000219 (hai câu đầu, phần dẫn ngoài nhấn mạnh), p000220 (cả đoạn). Không có nhấn mạnh thừa hay thiếu. Phủ định, số liệu (9.500 foot, chênh 3.500 foot, 250/230/200–210, hai mươi chiếc, năm phút/ba trăm giây) đều đúng.

## Kết luận: `needs_fixes` (serious 0, moderate 2, minor 8)

## Moderate

### MOD-1 — p000195, p000215: thuật ngữ "formulas" lệch ledger
- **Vấn đề:** bản dịch dùng "phép thức" ("né phép thức", "phép thức bắn tỉa tầm xa"), trong khi ledger đã có phương án tạm "thuật thức" (P01-formulas, b02, vol02-ch01-b05, vol02-ch01-b13) và chính mục đề xuất b09 ghi `proposed_vi: thuật thức`, `status: pending`. Như vậy bản dịch và ledger của chính batch này không khớp; "phép thức" chưa xuất hiện ở đâu trong ledger nên tạo biến thể thứ ba bên cạnh "thuật thức" và "công thức".
- **Đề xuất:** đổi cả hai đoạn sang "thuật thức" ("né thuật thức", "thuật thức bắn tỉa tầm xa"). Đây vẫn là phương án tạm, không phải canon.
- **Độ tin cậy:** 0,8 rằng cần thống nhất theo ledger; 0,6 rằng "thuật thức" là từ tốt nhất (xem phần thuật ngữ).

### MOD-2 — p000210: đối tượng câu hỏi bị đổi (hướng xuất hiện → hướng bay)
- **Vấn đề:** CP hỏi số lượng và "hướng" của máy bay ném bom; bản dịch viết "hướng bay". Câu trả lời ở p000211 là phương vị tương đối ("hướng hai giờ" theo góc nhìn của bên báo cáo), tức vị trí chứ không phải hướng di chuyển. "Hướng bay" tự thêm ý heading mà câu hỏi không nêu (style guide: không đổi đối tượng/độ mở của câu hỏi).
- **Đề xuất:** "Cho biết số lượng và chúng ở hướng nào." (hoặc "…và đang ở hướng nào").
- **Độ tin cậy:** 0,85.

## Minor (không chặn, nên sửa cùng lượt nếu tiện)

| ID | Đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| m1 | p000190 | "cấp chỉ huy" làm mất sắc thái "cấp cao" của bên được hỏi ý kiến. | "bộ chỉ huy cấp cao" hoặc "thượng cấp". |
| m2 | p000197 | "Những cỗ máy như chim" đổi hình ảnh gốc là chim cơ khí thành so sánh. | "Những con chim máy…". |
| m3 | p000202 | "phi đội" cụ thể hóa cấp đơn vị hơn nguồn (chỉ nói đơn vị máy bay ném bom). Đại từ "họ" (pháp sư) ngay sau "chúng" (máy bay) dễ gây nhầm chủ thể. | "một đơn vị máy bay ném bom… cắt đuôi đám pháp sư"; hoặc lặp danh từ thay vì "họ". |
| m4 | p000206 | "khoảng 9.500 foot" thêm tính ước chừng vào chính con số; nguồn đã nói ở vế trước là ước lượng bằng mắt và vẫn nêu con số chính xác. | Bỏ "khoảng": "…nhưng chúng ở 9.500 foot!". Độ tin cậy thấp (0,4), có thể giữ. |
| m5 | p000212 | "rét cóng" mạnh hơn nguồn ("chịu cái lạnh/khổ vì rét"). | "sẽ phải chịu rét". |
| m6 | p000217 | "Kho tiếp tế Kraggana" tự thêm "tiếp tế" (nguồn chỉ nói kho/depot) và chưa có mục ledger cho địa danh này. | Ghi mục pending mới; tạm "Kho Kraggana" hoặc "kho tiếp liệu Kraggana". Giữ nhất quán nếu tên xuất hiện lại. |
| m7 | p000219 | "dù anh đáp lại đầy tự hào" biến quan hệ đồng thời ("giọng mỉa mai, cam chịu khi đáp với niềm tự hào") thành đối lập "dù". | "…khi anh đáp lại đầy tự hào" hoặc "…trong lúc đáp lại đầy tự hào". |
| m8 | ledger | Mục `vol02-ch02-b09-air-supremacy-battles` ghi `part0010…/p000202`; đúng phải là `part0014…/p000202` của batch này. Mục `vol02-ch02-b09-formulas` mới nêu p000195, thiếu p000215. | Coordinator sửa `segment_ids` trong ledger. |

## Điểm đã kiểm tra, không có lỗi
- **Người nói/đại từ:** "Sở chỉ huy, rõ" ở p000191 và p000214 là CP tự xưng (khớp "Đây là sở chỉ huy" ở p000205); p000194 và p000218 là lời người ở tiền tuyến. Dùng "anh" cho người chỉ huy tiểu đoàn Viper có căn cứ từ nguồn ("his" ở p000197, p000200); nội tâm p000219–p000220 giữ "tôi/mình" nhất quán, không áp DEC-P01-001 (chỉ dành cho Tanya) sang chủ thể khác. Rủi ro còn lại: do không đọc batch khác, không xác minh được "anh" ở p000192/p000207/p000215 và "người chỉ huy Tiểu đoàn Viper" ở p000219 là cùng một người; trong phạm vi batch này cách đọc đó là hợp lý.
- **Logic và giả định:** p000190 (kháng cự tốt hơn khi hợp quân), p000203, p000209, p000213 (câu "đưa cả… lẫn…"), p000216 (điều kiện "đủ quân số và khai hỏa có kỷ luật thì có lẽ còn được") giữ đúng điều kiện và mức chắc chắn. "Họa vô đơn chí" (p000213) tương ứng tốt thành ngữ nguồn.
- **Đơn vị:** "foot" nhất quán ở p000201, p000206, p000216; "9.500" ở p000199 không kèm đơn vị đúng như nguồn.

## Thuật ngữ pending được báo cáo

### 1. "air supremacy battles" — p000202
- **Đánh giá:** cụm là danh từ xác định chỉ loại hình giao chiến của các đơn vị chuyên đánh chặn (giành quyền kiểm soát bầu trời), không phải tên chiến dịch. Bản dịch hiện tại "luôn giao chiến để giành ưu thế trên không" truyền đúng nghĩa và đọc tự nhiên. Ledger có sẵn "ưu thế trên không" cho "air supremacy" (vol02-ch01-b08, cùng mã số đoạn nhưng ở part0010), nên nên giữ để nhất quán.
- **Chọn tạm:** "các trận chiến giành ưu thế trên không" (dạng danh ngữ) hoặc giữ cấu trúc động từ hiện có. **Độ tin cậy:** 0,6.
- **Phương án thay thế:** "các trận tranh giành quyền kiểm soát bầu trời" (sát supremacy hơn, nhưng lệch ledger); "không chiến giành ưu thế trên không" (không khuyên dùng vì "không chiến" đã dùng cho dogfight ở p000216).
- **Lưu ý:** "ưu thế" thiên về superiority hơn supremacy; chỉ đáng đổi nếu sau này chốt thuật ngữ "quyền kiểm soát/chế ngự trên không" cho toàn bộ series.

### 2. "formulas" — p000195, p000215
- **Đánh giá:** nên theo thuật ngữ ledger "thuật thức". Đây là ma thuật được thi triển/né/bắn tỉa; "công thức" (phương án sớm nhất ở chapter003) mất nghĩa ma pháp và đọc như phép toán ("né công thức", "công thức bắn tỉa") nên không phù hợp ngữ cảnh chiến đấu; "phép thức" không có tiền lệ trong ledger.
- **Chọn tạm:** "thuật thức" (p000195: "né thuật thức"; p000215: "thuật thức bắn tỉa tầm xa"). **Độ tin cậy:** 0,6.
- **Phương án thay thế:** "phép thức", "công thức", hoặc "thuật thức" kèm danh từ khi cần rõ nghĩa ("thuật thức ma pháp").
- **Lưu ý:** nên ghi thêm p000215 vào `segment_ids` và dùng nhất quán từ nay.

### 3. Mới phát sinh (đề xuất ghi ledger)
- "Kraggana Depot" — p000217: chưa có mục; tạm "Kho Kraggana" (0,5), thay thế "Kho tiếp tế Kraggana", "kho tiếp liệu Kraggana".

## Rủi ro
- Nếu không sửa MOD-1, ba cách dịch "formulas" cùng tồn tại trong ledger/bản dịch, làm khó khi canon hóa thuật ngữ sau này.
- Lỗi `segment_ids` của ledger (m8) có thể khiến tra cứu thuật ngữ trỏ nhầm sang part0010.
- Nhận diện người chỉ huy Viper giữa các đoạn (p000192, p000207, p000215, p000219) chưa thể xác minh ngoài batch này.

## Đề nghị bước tiếp theo
Người giữ quyền sửa áp dụng MOD-1, MOD-2 và các minor đáng làm (m1–m3, m5–m7), cập nhật ledger (m8, mục Kraggana) rồi chuyển lại để phản biện ký xác nhận phạm vi các đoạn p000195, p000202, p000210, p000215, p000217, p000219.
