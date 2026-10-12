# Review vol-02-ch-03-b18 (Claude) — checkpoint_generation 631

- Phạm vi: 33 đoạn, `YS-LN02/Text/part0018.xhtml/p000302` → `p000334`.
- Đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b18, `canon/*` (glossary, characters rỗng; style-guide, decisions, glossary-pending), các mục liên quan trong `work/run-state/pending-terms.yml` (kể cả `chapter3_b18_translation_proposals`), gói nguồn b18 (sha256 `89f1bdf9…` khớp handoff) và `translations/vol-02/ch-03-b18.jsonl`. Không mở EPUB/PDF, gói nguồn hay bản dịch của lô khác. Không sửa bản dịch, handoff, ledger, canon hay run-state.
- Mọi lựa chọn bên dưới là **đề xuất tạm, không phải canon**. Không có mục nào ảnh hưởng cốt truyện cần hỏi người dùng.
- Ký hiệu rút gọn: `pNNNNNN` = `YS-LN02/Text/part0018.xhtml/pNNNNNN`.

## Tổng hợp mức độ

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 6 |
| Nhẹ | 12 |

Kiểm tra kết cấu: 33/33 đoạn, đúng thứ tự và mã đoạn, không thấy bỏ hay thêm đoạn; `status: draft`, `glossary_version` khớp handoff. Phủ định, quan hệ nhân quả và phép giả định ở p000307, p000333 được giữ đúng. Ba chỗ nguồn có nhấn mạnh là p000305, p000329, p000334; p000305 và p000329 đã có `*...*`, **p000334 thiếu** (M2). Các lỗi vừa chủ yếu là: đại từ trần thuật về Tanya vi phạm DEC-P01-001, thiếu nhấn mạnh, một chỗ lệch nghĩa (p000332), thuật ngữ mới lệch ledger, và hai chỗ lệch ledger/sắc thái. Cần sửa các mục vừa trước khi tính hoàn tất lô.

Về ghi chú translator: trường `notes` của cả 33 đoạn đều trống; chỉ có ba ghi chú thuật ngữ ở handoff/ledger (formula, mana science technology, seizure operation). Translator **không ghi** hai vấn đề đại từ (M1, M5), nên cần coordinator chú ý.

## Lỗi vừa

### M1 — p000307, p000309, p000321: trần thuật về Tanya dùng "cô"
- Vấn đề: DEC-P01-001 (đã duyệt) quy định trần thuật về Tanya ở giai đoạn này dùng "nó", nội tâm dùng "mình". Ledger b11 áp dụng "nó"/lặp tên cho trần thuật; mục b05 cho "cô" chỉ áp dụng cho điểm nhìn ngoài của sĩ quan khác và ghi rõ "không mở rộng sang trần thuật Tanya". Ba đoạn trên là trần thuật từ điểm nhìn Tanya nhưng dùng "cô" nhiều lần (p000307 bốn lần, p000309 sáu lần, p000321 một lần), trong khi p000305 lại dùng "Tanya" rồi "mình". Mặc dù dùng "cô" cho Tanya vẫn gần như chắc chắn đúng giới, nhưng đây là lỗi nhất quán với quy ước đã duyệt.
- Đề xuất: đổi "cô" thành "nó", lặp "Tanya" hoặc lược chủ ngữ khi câu nặng chữ "nó". Ví dụ p000309: "Vừa nghĩ mình muốn bỏ chạy đến mức nào, Tanya vừa nhận ra rằng nếu làm thế, sự nghiệp đã dày công gây dựng bấy lâu sẽ tiêu tan, mà nó thì bất lực không ngăn được. Miễn cưỡng, thậm chí bất đắc dĩ, nó đành chấp nhận mạo hiểm phần nào và chiến đấu." Ví dụ p000321: "Trong cuộc trao đổi thẳng thắn với chỉ huy lực lượng tiếp viện, Tanya nói năng dứt khoát, đúng việc để chiến dịch diễn ra suôn sẻ." Phương án khác: giữ "cô" cho cả chương nếu coordinator đổi quy ước, nhưng khi đó phải sửa đồng loạt cả các lô trước; chưa có căn cứ để làm vậy.

### M2 — p000334: thiếu nhấn mạnh (DEC-P01-002)
- Vấn đề: nguồn đánh dấu nhấn mạnh đúng một câu hỏi nội tâm mở đầu đoạn (phần còn lại của đoạn là lời kể thường). Bản dịch để phẳng. DEC-P01-002 yêu cầu `*...*` khi nguồn có nhấn mạnh tương ứng và giữ đúng phạm vi.
- Đề xuất: "*…Bên trong có thể là gì?* Theo lẽ thường, …", chỉ bọc câu hỏi, không bọc phần sau.

### M3 — p000332: "fleet maneuver" bị dịch thành "Đội hình hạm đội"
- Vấn đề: nguồn nói hành động điều động/xuất động của hạm đội đúng như phía Cộng hòa dự đoán (trước khi nêu chỗ trái kỳ vọng là tàu vận tải đi kèm). "Đội hình" là cách bố trí tàu, nên câu chuyển nghĩa từ "việc điều động xảy ra như dự đoán" sang "cách bố trí đúng dự đoán", và ý tương phản với vế sau ("nhưng…") bị mờ.
- Đề xuất: "Cuộc điều động hạm đội mà họ dự đoán quả thật đang diễn ra, nhưng các chiến hạm lại rời cảng cùng với vài tàu vận tải." Phương án khác: "Hạm đội xuất động đúng như họ dự đoán, nhưng…".

### M4 — p000313: thuật ngữ mới "công nghệ khoa học ma năng" lệch ledger
- Vấn đề: ledger đã dùng "mana" nguyên dạng (b16 `vol02-ch03-b16-mana`, ch2-b12 "khuynh hướng mana", "ma lực" chỉ là phương án khác). "Ma năng" là phiên âm/ghép mới, không nằm trong ledger, nên cùng khái niệm sẽ có hai cách viết trong một chương. Thứ tự "công nghệ khoa học" khá nặng nề và dễ đọc như hai danh từ ghép sai ngữ pháp.
- Đề xuất tạm: "công nghệ khoa học mana" (đã nằm trong danh sách phương án khác của translator; độ chắc ~0.5). Phương án khác tự nhiên hơn: "khoa học kỹ thuật mana". Hai lựa chọn đều giữ "mana"; chọn một và áp dụng nhất quán. Không nâng canon.
- Cùng đoạn: "thuật thức" cho "formulas" **đúng ledger** (b13, ch2-b09, b17); nên giữ. Xem thêm N1 cho các chỗ nhẹ trong cùng đoạn.

### M5 — p000302, p000303, p000304: "anh" cho Sue trong trần thuật, lệch ledger b06
- Vấn đề: ledger b06 ghi trần thuật về Sue dùng "ông", còn "anh" là cách Sue gọi Cunningham; mức tuổi vẫn chưa rõ. Bản dịch dùng "anh" cho Sue trong trần thuật (cả ba đoạn), và không có ghi chú của translator. Bằng chứng yếu cả hai phía (b17 ledger chỉ chốt "giữ từng dạng theo nguồn, chưa gộp"), nên mức này là vừa nhưng độ chắc thấp.
- Đề xuất tạm: lặp "Sue" hoặc lược chủ ngữ ở p000302–p000303 (nguồn dùng đại từ "he" nên chưa nêu tên đến p000304), ví dụ "Hay nói đúng hơn, mọi việc diễn ra như dự liệu." và "…rồi không chút do dự lao nhanh về phía mình" ở góc nhìn Sue — nhưng "mình" dễ mơ hồ, nên ưu tiên "về phía ông" nếu theo b06. Phương án chính: dùng "ông" theo b06; phương án khác: giữ "anh" nếu coordinator quyết định Sue trẻ và ghi vào ledger; trong cả hai trường hợp cần một quy ước thống nhất cho Sue trong chương. Độ chắc ~0.45.

### M6 — p000305: "bóc lột sức lao động" thêm phán xét
- Vấn đề: nguồn nói Tanya nghĩ mình bị bắt làm việc quá mức so với đồng lương (than phiền hài hước, bình diện công việc/lương). "Bóc lột sức lao động" mang sắc thái chính trị-đạo đức (bị lợi dụng bất công) và nặng hơn, trái quy tắc style-guide "không thêm sắc thái phán xét/đạo đức không có trong nguồn". Phần còn lại của đoạn (nhấn mạnh trong dấu nháy, "quân đội không vận hành như thế") đúng.
- Đề xuất: "Tanya thầm nghĩ mình đang bị bắt làm việc quá sức so với đồng lương nhận được, nhưng …". Phương án khác: "phải làm việc nhiều quá mức so với đồng lương".

## Lỗi nhẹ

- N1 p000313: "Đạn súng" gượng (nguồn là hỏa lực/đạn bắn nói chung); đề xuất "Hỏa lực và thuật thức đan chéo nhau". "một thế giới kỳ ảo" thêm "thế giới" — nguồn là một giấc mơ/huyễn tưởng mang tính mỉa mai; đề xuất "một thứ huyễn tưởng". "đang phát huy tác dụng" hơi trung tính; có thể "đang được phô diễn".
- N2 p000319: "đang quét dọn" dễ đọc thành dọn vệ sinh; nguồn là càn quét nốt tàn dư. Đề xuất "đang quét sạch phần còn lại" hoặc "đang dọn sạch tàn quân".
- N3 p000320: "Hai tiểu đoàn các anh" gán giới tính cho người nhận chưa rõ (ledger b16/DEC-P01-001 tránh đại từ giới tính). Đề xuất "Hai tiểu đoàn kia, chi viện cho thiếu tá!"; phương án khác: "Hai tiểu đoàn, …".
- N4 p000321: "nói năng công vụ" lạ tai; nguồn là lời lẽ gọn, đúng việc. Đề xuất "nói năng dứt khoát, đúng việc" (xem M1 về "cô").
- N5 p000323: "Chẳng bao lâu nữa… tương lai gần" lặp ý. Đề xuất "Chiến thắng… Điều đó sẽ sớm thành sự thật hiển nhiên đối với Lục quân Đế quốc."
- N6 p000324: "phản kháng" nghiêng về chống cự; nguồn là khả năng phản đối. Đề xuất "không còn đủ sức để phản đối" (phương án khác: "để lên tiếng ngăn cản").
- N7 p000325: "tuyến cảnh giới sớm" lạ; ledger đã chọn "tuyến cảnh giới" (b-ledger mục tuyến cảnh giới/cảnh báo). Đề xuất "tuyến cảnh báo sớm" hoặc "tuyến cảnh giới" cho cả p000325 và p000326, miễn nhất quán.
- N8 p000328: (a) thuật ngữ mới DEFCON không có trong ledger và translator không báo; giữ nguyên "DEFCON 1" là hợp lý (phương án khác: "báo động cấp 1"). (b) "Ra lệnh nâng mức báo động lên" bổ sung diễn giải; đề xuất "Phát lệnh DEFCON 1." (c) "chịu xuất hiện" thêm sắc thái "chịu"; đề xuất "Cuối cùng chúng cũng xuất hiện."
- N9 p000309: "đầy ngán ngẩm" lệch sắc thái so với "bất đắc dĩ/miễn cưỡng"; đề xuất "bất đắc dĩ".
- N10 p000331: "họ" gọi hạm đội địch; trong p000311, p000312, p000316 phe địch gọi là "chúng". Đề xuất "Ờ, chúng có… tàu vận tải đi cùng à?" hoặc "bên đó".
- N11 p000330: "một lũ ăn không ngồi rồi" thêm sắc thái coi thường nhóm; nguồn chỉ nói bị chế giễu là kẻ lười. Đề xuất "bị chế giễu là bọn ăn không ngồi rồi" hoặc "là kẻ ăn không ngồi rồi".
- N12 p000334: "hẳn đó là" tăng mức chắc chắn; nguồn chỉ nêu cách nghĩ thông thường. Đề xuất "đó là than, dầu, …" hoặc "chắc là".

## Đánh giá thuật ngữ mới / ghi chú translator

| Thuật ngữ | Bản dịch | Đánh giá | Đề xuất tạm | Độ chắc |
|---|---|---|---|---|
| formula (p000313) | thuật thức | Đúng ledger | giữ "thuật thức"; "công thức" là phương án khác | 0.6 |
| mana science technology (p000313) | công nghệ khoa học ma năng | Lệch "mana" của ledger (xem M4) | "công nghệ khoa học mana"; phương án khác "khoa học kỹ thuật mana" | 0.5 |
| seizure operation (p000318) | chiến dịch chiếm lĩnh | Chấp nhận được; "chiếm" khớp "bị chiếm" ở p000322; "chiếm đóng" hàm ý chiếm giữ lãnh thổ lâu dài nên kém hợp | giữ "chiến dịch chiếm lĩnh"; phương án khác "chiến dịch đánh chiếm" | 0.5 |
| DEFCON 1 (p000328) | giữ nguyên | Translator chưa báo; giữ nguyên là trung tính | giữ "DEFCON 1"; phương án khác "báo động cấp 1" | 0.5 |
| Sue (trần thuật) | anh | Lệch ledger b06 (xem M5) | "ông" hoặc lặp tên | 0.45 |

Các thuật ngữ khác khớp ledger: "Cộng hòa/Hải quân Cộng hòa", "Bộ chỉ huy", "pháo bờ biển", "Rhine", "tiểu đoàn/trung đoàn", cấp bậc "Thiếu tá/Đại tá". Không có mục nào cần quyết định canon; không nâng canon.

## Coordinator YAML

```yaml
role: reviewer
task_id: vol-02-ch-03-b18
state: done
segment_ids: [YS-LN02/Text/part0018.xhtml/p000302, YS-LN02/Text/part0018.xhtml/p000334]  # 33 đoạn liên tiếp
files_written: [reviews/prose/vol-02/ch-03-b18-claude.md]
validator: not_run
diff_check: not_run
review_path: reviews/prose/vol-02/ch-03-b18-claude.md
counts: {serious: 0, moderate: 6, minor: 12}
unresolved_findings:
  - {severity: moderate, segment_id: "p000307/p000309/p000321", issue: "Trần thuật Tanya dùng 'cô', vi phạm DEC-P01-001", resolution: "dùng 'nó'/lặp Tanya/lược chủ ngữ"}
  - {severity: moderate, segment_id: p000334, issue: "Thiếu *...* cho câu hỏi nội tâm đầu đoạn (DEC-P01-002)", resolution: "bọc đúng câu hỏi bằng *...*"}
  - {severity: moderate, segment_id: p000332, issue: "'Đội hình hạm đội' lệch nghĩa 'fleet maneuver'", resolution: "'Cuộc điều động hạm đội…'"}
  - {severity: moderate, segment_id: p000313, issue: "'ma năng' lệch ledger 'mana'", resolution: "'công nghệ khoa học mana'"}
  - {severity: moderate, segment_id: "p000302-p000304", issue: "'anh' cho Sue lệch ledger b06 'ông'; độ chắc thấp", resolution: "'ông' hoặc lặp tên; ghi ledger"}
  - {severity: moderate, segment_id: p000305, issue: "'bóc lột sức lao động' thêm phán xét", resolution: "'bị bắt làm việc quá sức so với đồng lương'"}
term_recommendations:
  - {source_term: formula, proposed_vi: thuật thức, alternatives: [công thức], segment_ids: [p000313], status: pending, confidence: 0.6}
  - {source_term: mana science technology, proposed_vi: công nghệ khoa học mana, alternatives: [khoa học kỹ thuật mana], segment_ids: [p000313], status: pending, confidence: 0.5}
  - {source_term: seizure operation, proposed_vi: chiến dịch chiếm lĩnh, alternatives: [chiến dịch đánh chiếm], segment_ids: [p000318], status: pending, confidence: 0.5}
  - {source_term: DEFCON 1, proposed_vi: DEFCON 1, alternatives: [báo động cấp 1], segment_ids: [p000328], status: pending, confidence: 0.5}
  - {source_term: Sue narration pronoun, proposed_vi: ông (hoặc lặp tên), alternatives: [anh], segment_ids: [p000302, p000303, p000304], status: pending, confidence: 0.45}
risks: ["Lệch quy ước đại từ Tanya/Sue có thể lan sang lô khác", "Cần thống nhất 'mana' xuyên chương"]
commit: null
next_action: translator_fix_then_signoff
```
