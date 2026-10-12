# Báo cáo phản biện — vol-02-ch-03-b21

- Người phản biện: Claude (reviewer). Phạm vi: 31 đoạn p000380–p000410 của `YS-LN02/Text/part0018.xhtml`.
- checkpoint_generation theo yêu cầu: 661, khớp `work/run-state/translation-coordinator.yml`. Handoff b21 ghi 660 ở `translation_lease.checkpoint_generation` (thế hệ lúc lease được thả); coordinator không cần xử lý.
- Đầu vào đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b21, `canon/style-guide.md`, `canon/decisions.md`, `canon/glossary.yml`, `canon/characters.yml`, `canon/glossary-pending.yml` (không có mục liên quan), khối `chapter3_b21_translation_proposals` và các mục liên quan trong `work/run-state/pending-terms.yml` (councilor, Commonwealth, Entente Alliance, Operations, armed merchant cruiser, auxiliary ship, Habergram, third lines), gói nguồn b21 (sha256 tính lại khớp `source_package_sha256` trong handoff) và `translations/vol-02/ch-03-b21.jsonl`. Không mở EPUB/PDF, gói nguồn khác hay bản dịch lô khác.
- Mã đoạn viết tắt `pNNNNNN`, thuộc `YS-LN02/Text/part0018.xhtml/`.

## Tổng quan

Bản dịch đủ 31 đoạn, thứ tự và mã đoạn đúng, hash nguồn và glossary_version khớp handoff, không bỏ sót hay thêm ý lớn. Phủ định, câu hỏi và logic điều kiện (p000381, p000388, p000402, p000408–409) đều đúng. Nguồn không có nhấn mạnh (không có thẻ in nghiêng/đậm trong gói nguồn) và bản dịch không dùng `*...*`, đúng DEC-P01-002. Xưng hô Habergram là "ông" gần như nhất quán; DEC-P01-001 chỉ áp dụng cho Tanya và không liên quan lô này. Văn phong trôi chảy, hợp giọng quân sự.

Có 5 lỗi mức vừa: một câu mâu thuẫn nội tại (p000387), một câu có nguy cơ gán sắc thái sai (p000392), một đại từ lệch hạng (p000395), một tính từ bị thay bằng đánh giá không có trong nguồn (p000404) và danh xưng Admiralty dễ đọc nhầm thành cấp bậc (p000404–p000405). Không có lỗi nghiêm trọng. Có một số lỗi nhẹ.

## Đếm theo mức

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 5 |
| Nhẹ | 11 |

## Lỗi mức vừa

**V1 — p000387 (nghĩa/logic).** Cụm "tuân thủ đến giới hạn… còn có thể cho phép mình lách qua" tự mâu thuẫn: "tuân thủ" và "lách" đối nghịch. Nguồn nói ông định đi sát ranh giới của những gì có thể lách được trong khuôn khổ luật quốc tế, tức dùng hết khoảng hở mà không vượt hẳn. Người đọc sẽ hiểu ông muốn giữ đúng luật, trái với mạch đoạn trước (đã nêu việc phá hiệp ước và ngần ngại có tính toán).
- Sửa tạm: "Ít nhất thì Tướng Habergram định chỉ đi đến sát ranh giới của những gì có thể lách được trong khuôn khổ luật quốc tế."
- Phương án khác: "…định giữ mình ở mép ngoài cùng của vùng mà luật quốc tế còn để ông lách qua."

**V2 — p000392 (sắc thái/chủ thể).** "đã vội mừng quá sớm khi cho rằng…" thêm yếu tố "mừng" (cảm xúc) và phán xét "quá sớm" như sự thật của người kể. Thành ngữ nguồn nói về việc tính trước khi có kết quả; điều bị tính trước và nội dung điều họ cho rằng nối với nhau không rõ. Bản dịch chọn một cách hiểu duy nhất, và nó có thể sai (phần suy đoán về việc Dacia sụp đổ dễ dàng đã giúp Cộng hòa và Liên minh có thêm thời gian là nội dung họ nêu ra, không phải lý do để mừng). Mức chắc chắn: trung bình; nguồn mơ hồ.
- Sửa tạm (trung tính): "Dù sao thì các nhân viên Tình báo đã tính toán trước khi có kết quả: họ cho rằng chính vì Dacia sụp đổ dễ dàng đến vậy nên Cộng hòa và Liên minh Entente mới có thêm thời gian xây dựng các tuyến thứ ba."
- Phương án khác: "…đã vội vàng đoán trước kết quả, rồi cho rằng…"; giữ "vội mừng" chỉ nếu coordinator xác nhận bối cảnh nghiêng về sự lạc quan.

**V3 — p000395 (đại từ).** "Anh ta" cho chủ thể "He" lệch hạng với cách kể về Habergram ở p000399–p000407 ("ông"). Nguồn sát p000394 và p000389 (người đứng đầu) cho thấy "he" khả dĩ nhất là Habergram, một tướng; "anh ta" làm đoạn đọc như một nhân vật khác trẻ hơn. Không suy ra quan hệ mới; chỉ đồng bộ đại từ trần thuật trong lô.
- Sửa tạm: "Ông không nghĩ rằng chất thêm một ít hàng hóa rắc rối sẽ khiến tình thế của họ thay đổi đáng kể."
- Phương án khác nếu sợ nhầm chủ thể: lặp tên "Habergram". Ghi vào pending: chủ thể p000395 là suy luận từ ngữ cảnh.

**V4 — p000404 (nghĩa/thêm ý).** "một người tai tiếng" thay cho "someone so toxic". "Tai tiếng" khẳng định người đó có tiếng xấu, một sự kiện về nhân vật không có trong nguồn và lệch với p000403 (ông được tin cậy vì bình tĩnh, không chệch hướng). Chưa rõ nguồn dùng "toxic" để chỉ người cứng rắn, nguy hiểm hay chất độc theo kiểu "lấy độc trị độc". Không nên chốt hướng cốt truyện; chọn cách diễn đạt gần chữ nhất.
- Sửa tạm: "họ đưa một người "độc" đến thế vào đó là để kiểm soát bộ phận ấy" hoặc "…một nhân vật gai góc như vậy…".
- Phương án khác: "một kẻ khó nuốt", "một người cứng rắn đến mức ấy". Ghi độ bất định vào ledger. Nếu coordinator chọn nghĩa khác, chỉ ảnh hưởng nhẹ đến cốt truyện nên chưa cần hỏi người dùng.

**V5 — p000404, p000405 (danh xưng/cấp bậc).** "Văn phòng Hải quân Đô đốc" và "Đệ nhất Quan chức Hải quân Đô đốc": "Hải quân Đô đốc" dễ bị đọc thành cấp bậc "Đô đốc hải quân", còn "Quan chức" quá chung và không giống một chức danh. Admiralty là cơ quan/bộ chỉ huy, "First Lord" là chức danh thường dịch là người đứng đầu cơ quan đó. Ledger đã ghi alt "Văn phòng Bộ Hải quân / Đệ nhất Hải vụ khanh" (độ tin 0,4). Cũng ở p000405, "có ở đó không" ngụ ý gọi từ xa, trong khi p000406–p000408 cho thấy Habergram nói trực tiếp với sĩ quan trực ban; nên dùng "có ở trong không".
- Sửa tạm: "Văn phòng Bộ Hải quân" / "Đệ nhất Lãnh chúa Hải quân" ("Bộ Hải quân" và tên chức danh theo cách dịch phổ biến của First Lord of the Admiralty). Câu thoại: "Habergram đây. Đệ nhất Lãnh chúa Hải quân có ở trong không?"
- Phương án khác: "Văn phòng Hải vụ / Đệ nhất Hải vụ khanh" (alt trong ledger); "Đô đốc phủ / Đệ nhất Đô đốc phủ" nếu coordinator muốn mang màu cổ. Giữ tất cả là đề xuất, không canon. Cần chọn một cặp và dùng nhất quán trong các lô sau.

## Lỗi mức nhẹ

- **N1 — p000380.** "điều quân đóng tại" làm mờ ý "tie up" (bị giữ chân). Gợi ý: "buộc phải giữ chân một lực lượng quân đội trên lãnh thổ Liên minh Entente".
- **N2 — p000382.** "cảm thấy rõ hơn bao giờ hết" thêm so sánh không có trong nguồn (nguồn chỉ nói cảm nhận sâu sắc/mạnh mẽ). Gợi ý: "đang cảm nhận rất rõ".
- **N3 — p000384.** "Một người ở nơi khác" thêm "một người" và đọc ngượng; nguồn nói đề nghị đến từ một phía khác. Gợi ý: "Từ một phía khác lại có đề nghị xử lý tình hình thận trọng." "một trận ầm ĩ" hơi khẩu ngữ, có thể đổi thành "sẽ gây náo động lớn".
- **N4 — p000385.** "ngần ngại đúng lúc" thêm "đúng lúc". Gợi ý: "biết cân nhắc thiệt hơn mà ngần ngại".
- **N5 — p000388.** "khám xét" lệch với "inspection" ở p000394 (kiểm tra) và mất ý "lên tàu". Gợi ý: "bị lên tàu kiểm tra".
- **N6 — p000391.** "chẳng tạo ra khác biệt gì" mạnh hơn "không khác biệt nhiều". Gợi ý: "cũng chẳng khác biệt là bao".
- **N7 — p000393.** "đang được bí mật đưa lên tàu" đổi trạng thái (đã nằm trên tàu) thành hành động đang diễn ra và để "tàu" mơ hồ giữa tàu phụ trợ và con tàu đang chất hàng. Gợi ý: "đều nằm sẵn trên tàu, được giấu kín" (tạm; xác minh lại nếu coordinator có cảnh trước).
- **N8 — p000392 (thuật ngữ).** "các tuyến phòng thủ thứ ba" thêm "phòng thủ" (suy diễn). Theo nguyên tắc literal ít suy diễn, nên dùng "các tuyến thứ ba" (alt đã có trong ledger).
- **N9 — p000397.** "ngành Tình báo" là cách gọi mới, khác ledger ("phía Tình báo", "Cục Tình báo"). Đề xuất dùng "phía Tình báo" hoặc "Cục Tình báo" để thống nhất; đây là đề xuất.
- **N10 — p000398.** "chính phủ tiền nhiệm" hơi lệch nghĩa so với "chính phủ trước đó" (người có thẩm quyền hợp lệ lúc đó). Gợi ý: "chính phủ trước đó, khi còn đủ thẩm quyền".
- **N11 — p000404.** "ban ngành" nghe như tập hợp nhiều cơ quan; nguồn nói một bộ phận. Gợi ý: "bộ phận ấy". Cũng cân nhắc "lập tức lên đường đến" thay "đến" cho "left at once for".

## Đánh giá thuật ngữ pending và ghi chú của translator

Phần `notes` trong JSONL đều rỗng; handoff nêu "2 low-level terminology notes" nhưng không nằm trong JSONL. Ledger có 3 mục `chapter3_b21_translation_proposals`. Tất cả là đề xuất, không canon.

| Thuật ngữ | Đoạn | Dùng trong bản dịch | Đánh giá | Phương án khác |
|---|---|---|---|---|
| government-in-exile | p000382, 397, 398, 401 | chính phủ lưu vong | Chấp nhận; nên giữ nhất quán (xem p000398 "bổ nhiệm vào chính phủ lưu vong" để gần hơn với nghĩa "làm" chính phủ lưu vong). | chính phủ tị nạn |
| third lines | p000392 | các tuyến phòng thủ thứ ba | Đề nghị đổi thành "các tuyến thứ ba" (N8). | các tuyến thứ ba |
| Office of the Admiralty / First Lord of the Admiralty | p000404, 405 | Văn phòng Hải quân Đô đốc / Đệ nhất Quan chức Hải quân Đô đốc | Không chấp nhận như hiện tại (V5). | Văn phòng Bộ Hải quân / Đệ nhất Lãnh chúa Hải quân; Văn phòng Bộ Hải quân / Đệ nhất Hải vụ khanh |
| armed merchant cruiser | p000383 | tàu tuần dương thương mại vũ trang | Khớp ledger b20 (giữ yếu tố cruiser). Lưu ý báo cáo b20 từng đề nghị "tàu buôn vũ trang"; ledger và bản dịch hiện theo "tuần dương". Coordinator nên đối chiếu để các lô sau không lệch. | tàu buôn vũ trang |
| councilor (of state) | p000397 | nghị viên nhà nước | Khớp ledger b20. Chấp nhận. | ủy viên nhà nước; cố vấn nhà nước |
| Commonwealth / Entente Alliance | p000380, 397, 401 | Khối Thịnh vượng chung / Liên minh Entente | Khớp ledger. | Liên bang / Liên minh Hiệp ước Entente |
| Operations / Intelligence (staff) | p000382, 389, 392, 397 | Tác chiến / Tình báo | Khớp ledger, trừ "ngành Tình báo" (N9). | — |
| auxiliary ship | p000393 | tàu phụ trợ | Khớp ledger b20. | tàu hỗ trợ |
| General Habergram | p000387, 399, 402 | Tướng Habergram | Khớp ledger (không cụ thể hóa cấp bậc). | — |
| duty officer / military policeman | p000406–410 | sĩ quan trực ban / quân cảnh | Chấp nhận. | — |

Không có quyết định nào ảnh hưởng cốt truyện đến mức phải hỏi người dùng. Hai điểm bất định (chủ thể p000395 và "toxic" ở p000404) nên được ghi vào `work/run-state/pending-terms.yml` theo AGENTS.md.

## Ghi chú còn tồn đọng cho coordinator

- V1–V5 cần translator sửa trước khi đóng lô; N1–N6, N8 và N9 nên sửa cùng lượt; N7, N10, N11 tùy chọn.
- Cập nhật ledger: thay mục `admiralty-titles` bằng đề xuất ở V5; đổi `third-lines` theo N8; ghi hai mục bất định (p000395, p000404).
- Đối chiếu việc báo cáo b20 và ledger khác nhau về "armed merchant cruiser".
- Hash gói nguồn đã đối chiếu; không phát hiện sai khác.

```yaml
role: reviewer
task_id: vol-02-ch-03-b21
state: done
segment_ids:
  - YS-LN02/Text/part0018.xhtml/p000380..p000410
review_path: reviews/prose/vol-02/ch-03-b21-claude.md
files_written:
  - reviews/prose/vol-02/ch-03-b21-claude.md
validator: not_run
diff_check: not_run
counts:
  serious: 0
  moderate: 5
  minor: 11
findings:
  - {severity: moderate, segment_id: YS-LN02/Text/part0018.xhtml/p000387, issue: "'tuân thủ' đối nghịch 'lách', đảo ý định đi sát ranh giới", resolution: "đi đến sát ranh giới những gì có thể lách được"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0018.xhtml/p000392, issue: "'vội mừng quá sớm' thêm cảm xúc và phán xét; nguồn mơ hồ", resolution: "diễn đạt trung tính 'tính toán trước khi có kết quả' (tạm)"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0018.xhtml/p000395, issue: "'Anh ta' lệch hạng với 'ông' dành cho Habergram", resolution: "'Ông' (chủ thể suy luận từ ngữ cảnh, ghi pending)"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0018.xhtml/p000404, issue: "'tai tiếng' thay cho 'toxic', thêm đánh giá nhân vật không có trong nguồn", resolution: "'người độc đến thế' / 'gai góc' (tạm, bất định)"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0018.xhtml/p000405, issue: "'Hải quân Đô đốc' dễ đọc thành cấp bậc; 'Quan chức' không phải chức danh; 'ở đó' ngụ ý gọi từ xa", resolution: "Bộ Hải quân / Đệ nhất Lãnh chúa Hải quân; 'có ở trong không' (tạm; p000404 cùng sửa)"}
unresolved_findings: 5
term_recommendations:
  - {source_term: "Office of the Admiralty / First Lord of the Admiralty", proposed_vi: "Văn phòng Bộ Hải quân / Đệ nhất Lãnh chúa Hải quân", alternatives: ["Văn phòng Bộ Hải quân / Đệ nhất Hải vụ khanh", "Văn phòng Hải vụ / Đệ nhất Hải vụ khanh"], segment_ids: [p000404, p000405], status: pending, confidence: 0.45}
  - {source_term: third lines, proposed_vi: "các tuyến thứ ba", alternatives: ["các tuyến phòng thủ thứ ba"], segment_ids: [p000392], status: pending, confidence: 0.5}
  - {source_term: government-in-exile, proposed_vi: "chính phủ lưu vong", alternatives: ["chính phủ tị nạn"], segment_ids: [p000382, p000397, p000398, p000401], status: pending, confidence: 0.6}
  - {source_term: "toxic (someone so toxic)", proposed_vi: "người độc / nhân vật gai góc", alternatives: ["kẻ khó nuốt", "người cứng rắn đến mức ấy"], segment_ids: [p000404], status: pending, confidence: 0.35}
  - {source_term: armed merchant cruiser, proposed_vi: "tàu tuần dương thương mại vũ trang", alternatives: ["tàu buôn vũ trang"], segment_ids: [p000383], status: pending, confidence: 0.45}
risks:
  - "chủ thể 'He' ở p000395 và nghĩa 'toxic' ở p000404 là suy luận từ ngữ cảnh, cần ghi vào pending-terms.yml"
  - "báo cáo b20 và ledger khác nhau về 'armed merchant cruiser'"
commit: null
next_action: translator_fix_then_recheck
```
