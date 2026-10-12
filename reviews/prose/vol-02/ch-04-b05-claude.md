# Báo cáo review — vol-02-ch-04-b05 (Claude)

- Task: `vol-02-ch-04-b05`; checkpoint_generation: 725; phạm vi: 18 đoạn, từ `YS-LN02/Text/part0022.xhtml/p000096` đến `p000113` (dưới đây viết tắt là pNNNNNN).
- Đầu vào đã đọc: shared.md, reviewer.md, config/translation-pipeline.yml, handoff b05, canon (style-guide, decisions, glossary-pending, glossary, characters), các mục liên quan trong `work/run-state/pending-terms.yml` (`chapter4_b05_translation_proposals` và các mục Serebryakov / radio operator / Norden Control / ma'am / Northern Sea Fleet), gói nguồn b05 và `translations/vol-02/ch-04-b05.jsonl`.
- Không mở EPUB/PDF, gói nguồn hay bản dịch khác; không sửa bản dịch, handoff, ledger, canon, run-state. Báo cáo không trích câu nguồn; mọi đề xuất là phương án tạm, không phải canon.
- Đối chiếu kỹ thuật: sha256 gói nguồn khớp handoff (`9fef114e…ed17b`); 18/18 mã đoạn khớp và cùng thứ tự; `source_sha256` và `glossary_version` từng đoạn khớp; status `draft`; `notes` rỗng ở mọi đoạn (handoff nhắc "3 ghi chú thuật ngữ mức nhẹ" nhưng không có trong JSONL nên không đánh giá được). Chữ nghiêng: nguồn có nhấn mạnh ở một từ trong p000103 và ở vế đầu p000109; bản dịch dùng `*...*` đúng phạm vi theo DEC-P01-002; không có nhấn mạnh thừa/thiếu ở đoạn khác.

## Số lượng

| Mức | Số |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 3 |
| Nhẹ | 10 |

Không bỏ sót đoạn, không đảo phủ định, không thêm ý lớn; logic điều kiện, câu hỏi nội tâm và giả định (p000096, p000113) được giữ đúng. Các lỗi vừa nằm ở đại từ trần thuật về Tanya (p000097), đại từ ngôi thứ nhất lẫn lộn trong một đoạn (p000102) và cấp bậc của Serebryakov lệch ledger (p000099, p000100, p000107, p000111).

## Phát hiện mức vừa

**M1 — p000097: "cô" dùng cho Tanya, trái DEC-P01-001.**
- Căn cứ: trần thuật về Tanya ở giai đoạn này dùng "nó" (DEC-P01-001) và chính bản dịch dùng "nó" ở p000096, p000099, p000109, p000111, p000112. Ở p000097, "yêu cầu của cô" quy chiếu Tanya; đồng thời "Cô" ở p000102 lại chỉ Serebryakov, nên "cô" bị dùng cho hai người khác nhau trong hai đoạn gần nhau, dễ gây nhầm người đưa yêu cầu.
- Đề xuất tạm: đổi thành "yêu cầu của nó". Giữ "cô" ở p000102 cho Serebryakov (nguồn ghi giới nữ rõ ràng ở đoạn đó).
- Phương án thay thế: "yêu cầu của Tanya" nếu muốn tránh lặp "nó" trong câu.

**M2 — p000102: tự quy chiếu nội tâm lẫn "tôi / chúng tôi" với "mình" trong cùng một đoạn.**
- Căn cứ: nguồn chuyển sang ngôi thứ nhất nội tâm của Tanya. Bản dịch dùng "cho tôi", "Chúng tôi chỉ trao đổi", "nối máy cho tôi" rồi ngay sau đó "cho mình" ở câu cuối; các đoạn nội tâm khác (p000100, p000103–p000105, p000113) dùng "mình/bọn mình". DEC-P01-001: nội tâm tự quy chiếu dùng "mình"; ledger (b12 ch3) chỉ dành "tôi" cho thoại nói với cấp dưới. Lẫn hai đại từ làm người đọc tưởng đổi người kể.
- Đề xuất tạm: "...đưa bản đồ và ống nghe cho mình... Bọn mình chỉ trao đổi đôi ba câu, rồi nhân viên điện đài nối máy cho mình với..."; giữ "mình" ở câu cuối.
- Phương án thay thế: giữ "tôi" cho cả đoạn nếu coordinator muốn coi đây là ngôi thứ nhất trần thuật (khi đó phải đổi "mình" cuối đoạn và rà lại các đoạn kế); kém ưu tiên vì khác DEC-P01-001.

**M3 — p000099, p000100, p000107, p000111: cấp bậc của Serebryakov ("Trung úy") lệch phương án tạm trong ledger.**
- Căn cứ: ledger gần nhất (ch3 b16, b17) tạm đặt Serebryakov = thiếu úy, Weiss = trung úy; ch3 b12 cho phép giữ nguyên cấp theo từng dạng nguồn khi nguồn có biến thể. Nguồn b05 chỉ có một dạng cấp bậc chung, không có biến thể rõ để biện minh cho việc đổi; bản dịch dùng "Trung úy" ở cả 4 đoạn và không ghi vào `chapter4_b05_translation_proposals`, báo cáo translator cũng không nêu. Đổi cấp bậc nhân vật giữa các chương mà không ghi lý do sẽ khiến người đọc tưởng là hai người hoặc thăng cấp.
- Đề xuất tạm: dùng "Thiếu úy Serebryakov" / gọi "Thiếu úy" ở p000099, p000100, p000107, p000111 để nhất quán với ledger gần nhất; coordinator ghi mục ledger riêng cho b05, độ chắc chắn thấp (~0.5), không nâng canon.
- Phương án thay thế: giữ "Trung úy" nếu coordinator muốn dịch sát nguồn từng dạng (theo ch3 b12) — khi đó cần ghi mục ledger giải thích và rà lại các đoạn ch4 b01–b04 để thống nhất.

## Phát hiện mức nhẹ

- **L1 — p000096, p000102: "radio operator" dịch "nhân viên điện đài"**, ledger (ch2 b18, ch3 b20) tạm dùng "báo vụ viên". Đề xuất tạm: "báo vụ viên" cho nhất quán, hoặc ghi mục mới nếu giữ "nhân viên điện đài" (phương án thay thế: nhân viên vô tuyến).
- **L2 — p000102: "máy thu"** cho vật được trao cùng bản đồ để gọi liên lạc; "máy thu" dễ hiểu là thiết bị thu sóng. Đề xuất: "ống nghe" (hoặc "thiết bị liên lạc").
- **L3 — p000097: "mọi cuộc diễn tập trước đó"** diễn giải cụ thể hơn "maneuvers" (có thể là cơ động). Chấp nhận được vì p000113 nói chưa từng tập trên biển; có thể thay bằng "mọi hoạt động cơ động trước đó" nếu muốn trung tính hơn.
- **L4 — p000099: "vùng trời mà chẳng biết phương hướng"** hơi lệch so với ý "không có cảm giác về nơi chốn/vị trí". Đề xuất: "vùng trời mà chẳng có chút cảm giác nào về vị trí".
- **L5 — p000101: "thưa thiếu tá"** thêm cấp bậc khi nguồn chỉ có kính ngữ chung. Có căn cứ ledger b08 ("thưa Thiếu tá") nhưng ch3 b16 đề xuất "thưa chỉ huy". Chấp nhận, ghi độ bất định; phương án trung tính: "Vâng, thưa chỉ huy."
- **L6 — p000108: "ạ"** thêm sắc thái kính ngữ không có trong nguồn; chấp nhận được với cấp dưới nhưng nên bỏ nếu muốn khớp p000101.
- **L7 — p000109: "hạm đội phe mình"** trong lời kể ngôi ba; "mình" dành cho nội tâm Tanya theo DEC-P01-001 nên dễ đọc nhầm. Đề xuất: "hạm đội phe ta" hoặc "hạm đội bên ta".
- **L8 — p000110: "Hạm đội Viễn dương" (High Seas Fleet)** — tên hạm đội mới, đã ghi trong ledger. Phương án thay thế "Hạm đội Biển khơi" gần cách gọi thường thấy của hạm đội tương ứng trong lịch sử hơn; giữ pending, nhất quán với "Hạm đội Biển Bắc".
- **L9 — p000112: "những hơi thở ngắn"** cho hơi thở nhỏ để không bị chú ý; "ngắn" gợi nhịp thở gấp, mâu thuẫn "hít thật sâu". Đề xuất: "những hơi thở khẽ".
- **L10 — p000113: hai chỗ nhỏ.** (a) "thâu tóm một công ty" thêm đối tượng "công ty" (nguồn nói thương vụ mua lại); đề xuất "một thương vụ thâu tóm". (b) "Nếu mình có ưu thế áp đảo" — "mình" dễ bị hiểu chỉ riêng Tanya, trong khi nguồn chỉ cả phía ta; đề xuất "Nếu phía mình có ưu thế...".

## Đánh giá thuật ngữ pending

Các phương án trong `chapter4_b05_translation_proposals` đều là tạm, giữ pending, không nâng canon.

- Norden (p000099): giữ "Norden"; đồng ý. "Norden Control" (p000100, p000102) khớp ledger ch2 b15; chưa có mục ghi cho dạng "Norden Control" trong b05 nên nên thêm tham chiếu đoạn.
- Northern Sea Fleet = "Hạm đội Biển Bắc" (p000100, p000107, p000110) và "khu vực Biển Bắc": khớp, nhất quán.
- Entente Alliance = "Liên minh Entente" (p000109, p000113): đồng ý.
- capital ships = "tàu chiến chủ lực" (p000110): đồng ý; "chiến hạm" (ships/warships) dùng cho tàu nói chung ở p000109, p000113 chưa vấn đề.
- High Seas Fleet = "Hạm đội Viễn dương": chấp nhận tạm; xem L8.
- search and destroy = "tìm diệt" (p000097, p000098): nhất quán giữa hai đoạn; phương án "truy tìm và tiêu diệt" dài hơn, có thể dùng cho lời lệnh trang trọng.
- corporate warrior = "chiến binh công sở" (p000105): giữ ẩn dụ, không thêm giải thích; đồng ý.
- Cần bổ sung vào ledger: cấp bậc Serebryakov ở b05 (M3), "radio operator" (L1), "ma'am" (L5), "combat control map" = "bản đồ kiểm soát tác chiến" (chưa có mục).
- Không có mục nào ảnh hưởng cốt truyện cần hỏi người dùng.

## Báo cáo cho coordinator

```yaml
role: reviewer
task_id: vol-02-ch-04-b05
state: done
segment_ids:
  start: YS-LN02/Text/part0022.xhtml/p000096
  end: YS-LN02/Text/part0022.xhtml/p000113
  count: 18
review_path: reviews/prose/vol-02/ch-04-b05-claude.md
files_written:
- reviews/prose/vol-02/ch-04-b05-claude.md
validator: not_run
diff_check: not_run
counts:
  serious: 0
  moderate: 3
  minor: 10
findings:
- {severity: moderate, segment_id: YS-LN02/Text/part0022.xhtml/p000097, issue: "'cô' chỉ Tanya, trái DEC-P01-001 (trần thuật dùng 'nó')", resolution: "đổi thành 'yêu cầu của nó'"}
- {severity: moderate, segment_id: YS-LN02/Text/part0022.xhtml/p000102, issue: "lẫn 'tôi/chúng tôi' với 'mình' trong nội tâm một đoạn", resolution: "dùng 'mình/bọn mình' cả đoạn; 'ống nghe' thay 'máy thu' (L2)"}
- {severity: moderate, segment_id: "YS-LN02/Text/part0022.xhtml/p000099, p000100, p000107, p000111", issue: "Serebryakov dịch 'Trung úy' lệch ledger gần nhất (Thiếu úy)", resolution: "dùng 'Thiếu úy' hoặc ghi mục ledger giải thích nếu giữ 'Trung úy'"}
- {severity: minor, segment_id: "p000096, p000102", issue: "radio operator: điện đài vs ledger báo vụ viên", resolution: "L1"}
- {severity: minor, segment_id: "p000097, p000099, p000101, p000108, p000109, p000110, p000112, p000113", issue: "L3–L10: diễn giải/sắc thái nhỏ", resolution: "xem mục Phát hiện mức nhẹ"}
unresolved_findings: 3  # mức vừa chờ translator sửa; không có mức nghiêm trọng
term_recommendations:
- {source_term: "Serebryakov rank (b05)", proposed_vi: "Thiếu úy Serebryakov", alternatives_vi: ["Trung úy Serebryakov"], segment_ids: [p000099, p000100, p000107, p000111], status: pending, confidence: 0.5}
- {source_term: "radio operator", proposed_vi: "báo vụ viên", alternatives_vi: ["nhân viên điện đài", "nhân viên vô tuyến"], segment_ids: [p000096, p000102], status: pending, confidence: 0.5}
- {source_term: "ma'am without explicit rank", proposed_vi: "thưa chỉ huy", alternatives_vi: ["thưa thiếu tá"], segment_ids: [p000101], status: pending, confidence: 0.45}
- {source_term: "High Seas Fleet", proposed_vi: "Hạm đội Viễn dương", alternatives_vi: ["Hạm đội Biển khơi"], segment_ids: [p000110], status: pending, confidence: 0.5}
- {source_term: "combat control map", proposed_vi: "bản đồ kiểm soát tác chiến", alternatives_vi: [], segment_ids: [p000100], status: pending, confidence: 0.5}
- {source_term: "receiver (handset)", proposed_vi: "ống nghe", alternatives_vi: ["thiết bị liên lạc"], segment_ids: [p000102], status: pending, confidence: 0.55}
risks:
- "Cấp bậc Serebryakov có thể còn lệch ở các lô ch4 b01–b04 (không đọc trong task này)."
- "Mục `notes` rỗng nên không kiểm được 3 ghi chú nhẹ mà handoff nhắc."
commit: null
next_action: translator_fix_then_signoff
```
