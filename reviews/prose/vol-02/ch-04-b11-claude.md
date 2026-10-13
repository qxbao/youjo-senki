# Báo cáo review — vol-02-ch-04-b11 (Claude)

- Phạm vi: 25 đoạn, `YS-LN02/Text/part0024.xhtml/p000001` … `p000025`.
- Đầu vào đã đọc: shared.md, reviewer.md, config, handoff b11, source package b11 (sha256 trong handoff), 5 tệp canon được tham chiếu, mục `chapter4_b11_translation_proposals` và các mục công thức/pháp sư thủy quân lục chiến trong `chapter4_b10_translation_proposals`, `translations/vol-02/ch-04-b11.jsonl`.
- Không đọc lô khác. Không sửa bản dịch, canon, handoff, ledger, checkpoint. Validator/diff_check: not_run.
- Canon hiện chưa chốt thuật ngữ/nhân vật nào (`glossary.yml`, `characters.yml` rỗng); chỉ có DEC-P01-001 (đại từ) và DEC-P01-002 (nhấn mạnh).

## Đánh giá chung

Nghĩa, phủ định, logic kế hoạch (kích nổ dây chuyền → khu trục hạm mất khả năng chống ngầm), thứ tự sự kiện và các chi tiết kỹ thuật (đuôi tàu, bánh lái, tốc độ, thiết giáp hạm) được giữ đúng. Không thấy đoạn bị bỏ hay thêm ý lớn. Nhấn mạnh theo DEC-P01-002 đúng ở p000002 và p000004 (nguồn chỉ nhấn hai chỗ này); không đánh dấu thừa. Chú thích ¹² (p000006) và ¹³ (p000018) giữ đúng vị trí. Chuyển điểm nhìn trần thuật → nội tâm ở p000003 xử lý đúng DEC-P01-001 ("nó" → "mình").

Vấn đề chính: (1) bản dịch **không áp dụng** hai lựa chọn tạm của coordinator (công thức/pháp sư hải quân); (2) p000021 vi phạm DEC-P01-001 ("tôi/chúng tôi"); (3) một số lỗi đại từ, sắc thái nhỏ.

## Phát hiện

### Vừa

**M1 — p000009, p000023, p000025 — thuật ngữ công thức chưa theo đề xuất tạm**
- Vấn đề: bản dịch dùng "công thức gây nổ", "công thức", "công thức" trong khi ledger b11 và b10 ghi đề xuất tạm "thuật thức" ("thuật thức nổ", "thuật thức đánh chặn").
- Căn cứ: `chapter4_b11_translation_proposals` (vol02-ch04-b11-formulas) và b10 (explosion/interceptor formulas); ledger ghi lý do là bám thuật ngữ chương 3/b10 nhưng bản JSONL không áp dụng. Ngoài ra "công thức gây nổ" lệch cả dạng "thuật thức nổ" của b10.
- Đề xuất: sửa thành "thuật thức nổ" (p000009), "thuật thức" (p000023, p000025). Nếu coordinator đổi phương án thì đổi đồng loạt cả ba chương/lô. Không có đoạn nào trong b11 viết "thuật thức" nên cần rà lại toàn lô.

**M2 — p000014 — "pháp sư hải quân" lệch đề xuất "pháp sư thủy quân lục chiến"**
- Vấn đề: nguồn dùng "marine mages", chỉ binh chủng thủy quân lục chiến; "hải quân" xóa phân biệt marine/navy và dễ nhầm với hạm đội/tàu chiến (p000019 có Hạm đội Biển Bắc, p000009 có tàu địch). Ledger đề xuất "thủy quân lục chiến" nhưng bản JSONL ghi "hải quân".
- Đề xuất: sửa "các pháp sư hải quân" → "các pháp sư thủy quân lục chiến" cho nhất quán với b06/b09/b10 và chương 3. Chỗ chỉ gọi "các pháp sư/họ" (p000013, p000015) có thể giữ.

**M3 — p000021 — "chúng tôi/tôi" vi phạm DEC-P01-001**
- Vấn đề: đoạn nội tâm của Tanya dùng "Chúng tôi lại tăng tốc", "không bắn trúng tôi", "chúng tôi cũng đang ở giữa trời mưa"; các đoạn nội tâm khác trong lô dùng "mình". Quyết định đã duyệt: nội tâm tự quy chiếu = "mình".
- Đề xuất: "Cả đội lại tăng tốc để bổ nhào" / "Bọn mình lại tăng tốc…"; "…không bắn trúng mình mà bay sượt qua"; "bọn mình cũng đang ở giữa trời mưa". Chọn một dạng cho "chúng ta" nội tâm và dùng đồng nhất (p000017 đang dùng "ta/chúng ta").

### Nhẹ

**m1 — p000003 — "nó" mơ hồ**: "đá cái xác ra xa, đã gạt nó khỏi tâm trí" — "nó" là xác chết, nhưng "nó" cũng là đại từ trần thuật của Tanya (DEC-P01-001) nên dễ đọc nhầm; "đã" cũng lệch nghĩa đồng thời ("already pushing"). Đề xuất: "…đá cái xác ra xa, đồng thời gạt xác chết khỏi tâm trí".

**m2 — p000002 — cấu trúc câu đầu rối**: "Tên lính địch lẩm bẩm điều gì đó thậm chí chẳng thành lời, đang bị thương chí mạng" gây đọc tách "lời/đang bị thương". Đề xuất: "Tên lính địch đã bị thương chí mạng, miệng lẩm bẩm thứ không thành lời."

**m3 — p000004 vs p000012 — cách tự xưng trong lời nói không đồng nhất**: p000004 "chẳng còn gì cản đường ta nữa" (lời khẽ nói thành tiếng), p000012 "Mình sẽ làm một trận ra trò!" (trong dấu thoại). DEC-P01-001 chưa quy định xưng hô trong thoại. Căn cứ: không đủ để suy; chưa có ledger thoại tự nói của Tanya trong phạm vi được đọc. Đề xuất: coordinator đối chiếu ledger rồi dùng một dạng ("mình" hoặc bỏ đại từ) cho cả hai; tạm nên tránh "ta" nếu chưa có tiền lệ vì tạo giọng khác.

**m4 — p000013, p000014, p000015, p000017 — "họ/chúng" chỉ hai phía lẫn nhau**: "họ" chỉ pháp sư địch ở p000013–p000015, rồi "họ" ở p000017 chỉ cấp dưới phe mình, "chúng" lại chỉ địch. Có thể đọc nhầm "họ chắc chắn sẽ được tưởng thưởng". Đề xuất: dùng "chúng" cho phía địch xuyên suốt (như ở cuối p000014, p000009), "họ" cho phía mình; hoặc ghi rõ "những người cầm chân".

**m5 — p000020 — "vô tích sự" lệch nghĩa**: nguồn nhấn vào việc chưa có thành tích (no-achievement) và tính chất ngốc nghếch (knuckleheads); "vô tích sự" chỉ là vô dụng. Đề xuất: "lũ đầu đất chưa lập được chiến công nào" hoặc "lũ ngố không có thành tích".

**m6 — p000006 — sắc thái "gentlemanly"/"sophisticated"**: "tao nhã" và "tinh tế" làm mất ý ra vẻ quý ông/lịch lãm mỉa mai; "trò cricket tinh tế" hơi khó hiểu. Đề xuất: "cuộc đấu sinh tồn kiểu quý ông" và "trò cricket lịch lãm/sang trọng".

**m7 — p000024 — "gã" và "mừng thầm" thêm sắc thái**: "gã" thêm chút khinh nhờn về cấp dưới; "mừng thầm" thêm ý giấu kín không có trong "happy miscalculation". "Trường hợp hiếm hoi" cũng nhẹ hơn "fluke" (xui rủi/ngẫu nhiên). Đề xuất: "người vừa bị bắn trúng lúc nãy"; "trái với tính toán của mình, may mắn là chẳng ai bị loại"; "chỉ là một sự xui rủi ngẫu nhiên".

**m8 — p000025, p000013, p000023 — chi tiết nhỏ**: p000025 "rất nhanh chóng" chuyển "efficiently" từ hiệu quả/gọn sang tốc độ; p000013 mất chủ ngữ "chúng tôi/ta" của báo cáo ("Đã dụ được" — chấp nhận được nhưng nên cân nhắc "Chúng tôi đã dụ…"); p000023 mất tính mệnh lệnh ("Tất cả triển khai…" → "Toàn đại đội, triển khai thuật thức!").

**m9 — p000018 / p000006 — chú thích và viết tắt**: bản dịch bung RTB thành "quay về căn cứ" nhưng giữ số chú thích ¹³; khi dịch chú thích cần kiểm tra chú thích không lặp thừa. Chưa có văn bản chú thích trong package nên chỉ ghi rủi ro, không kết luận lỗi. Tương tự ¹² (cricket).

## Thuật ngữ chưa canon — khuyến nghị (không tự nâng canon)

| Mục | Phương án tạm | Đánh giá | Ảnh hưởng cốt truyện |
|---|---|---|---|
| formula(s) | **thuật thức** | Giữ làm phương án tạm, độ tin cậy ~0.6. Ưu: nhất quán với chương 3, b10; nghe như thuật ngữ ma pháp, hợp với "thời gian kích hoạt", "triển khai". Nhược: là Hán–Việt chuyên biệt, độ chắc chắn về tương ứng với thuật ngữ gốc tiếng Nhật chỉ dựa trên hiểu biết ngoài package nên không dùng làm căn cứ; "công thức" là phương án literal, ít suy diễn hơn. Vì cả lô trước đã dùng, đổi sau rẻ nếu áp dụng nhất quán. Phải sửa p000009/23/25 cho khớp. | Không |
| marine mages | **pháp sư thủy quân lục chiến** | Chấp nhận làm phương án tạm (0.6–0.65): "marine" ≠ "navy" nên "hải quân" làm mờ đơn vị; nhất quán với b06/b09/b10. Hơi dài nhưng chấp nhận được. Sửa p000014. | Không |
| RTB | quay về căn cứ | Chấp nhận (literal, trung tính); kiểm tra lại khi dịch chú thích. | Không |
| imperial magic bullets | đạn phép của Đế quốc | Chấp nhận; giữ literal, không suy ra loại đạn đặc biệt. | Không |
| Entente Alliance | Liên minh Entente | Chấp nhận theo tên pending hiện có. | Không |
| Northern Sea Fleet | Hạm đội Biển Bắc | Chấp nhận tạm cho nhất quán chương 4; lưu ý "Biển Bắc" dễ trùng địa danh North Sea, "Bắc Hải" cũng trùng biển Trung Quốc; nếu có bằng chứng thì xét lại. | Không |

Không mục nào cần hỏi người dùng.

## Kết luận

Chưa có lỗi nghiêm trọng. Có 3 lỗi vừa (M1–M3) cần translator sửa trước khi lô được tính hoàn tất; nhẹ có thể xử lý cùng lúc. Sau khi sửa nên kiểm tra lại p000009, p000014, p000021, p000023, p000025.
