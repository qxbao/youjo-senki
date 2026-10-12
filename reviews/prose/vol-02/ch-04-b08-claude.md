# Review vol-02-ch-04-b08 (Claude, checkpoint_generation 755)

- Phạm vi: 22 đoạn, `p000170`–`p000191` (`YS-LN02/Text/part0022.xhtml/`). Mã đoạn dưới đây viết tắt `pNNNNNN`.
- Đầu vào đã đọc: shared.md, reviewer.md, config, handoff b08, canon (glossary và characters gần như rỗng, style-guide, decisions DEC-P01-001/002, glossary-pending), các mục liên quan trong `work/run-state/pending-terms.yml` (gồm `chapter4_b08_translation_proposals`), source package b08, `translations/vol-02/ch-04-b08.jsonl`. Không mở EPUB/PDF hay batch khác. Không sửa bản dịch, handoff, ledger, canon, run-state.
- Kiểm tra cơ học: 22/22 `segment_id` khớp thứ tự với package; `source_sha256` mỗi đoạn và `glossary_version` khớp handoff; package sha256 `3fcd121b…` khớp handoff; status `draft`; `notes` rỗng ở mọi đoạn (các nghi vấn nằm trong ledger, giống b07).

## Tổng quan

Bản dịch bám sát nghĩa. Không thấy thiếu hoặc thừa câu đáng kể, không đảo phủ định, không sai chủ thể hay quân hàm. Đại từ trần thuật về Tanya dùng “nó” đúng DEC-P01-001. Chữ nghiêng duy nhất của nguồn (p000188, câu nội tâm) được đánh `*...*` đúng phạm vi, các đoạn còn lại không tự thêm nhấn mạnh, đúng DEC-P01-002. Còn lại là các điểm nhẹ về đại từ nhập nhằng, chọn từ và thuật ngữ chưa vào ledger. Không có lỗi nghiêm trọng hay vừa.

## Số lượng

| Mức | Số |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 0 |
| Nhẹ | 10 |

## Lỗi mức nghiêm trọng / vừa

Không có.

## Lỗi mức nhẹ

- **m1 — p000170, p000171, p000172, p000178: đại từ “họ”/“chúng” trôi và nhập nhằng.** Ở p000170, “họ” đầu chỉ phía tạo ra pha hỗ trợ, “họ” sau chỉ hạm đội Liên minh Entente. Sang p000171, “họ” chỉ phía hạm đội, nhưng câu mệnh lệnh liền sau lại dùng “chúng” cho cùng đối tượng. Nguồn cũng dùng đại từ nhập nhằng, nên giữ được là chấp nhận được. Đề xuất tạm: thống nhất “chúng” hoặc “họ” cho phía hạm đội Entente trong cả đoạn, hoặc lặp danh từ (“phía hạm đội”) ở chỗ đổi chủ thể.
- **m2 — p000176: “bất ngờ” là phần thêm.** Nguồn chỉ có hành động tăng tốc lao hết tốc lực. “Bất ngờ” là cách hiểu của người dịch, dù hợp ngữ cảnh. Đề xuất tạm: “…tăng hết tốc lực lao thẳng vào soái hạm.”
- **m3 — p000180: “cuộc điều tra” hơi hẹp.** Nguồn nói về việc khoảnh khắc ấy sẽ bị đem ra xét hỏi, bàn luận nhiều năm sau, chưa chắc là điều tra chính thức. Đề xuất tạm: “nhiều cuộc truy xét/nghiên cứu” hoặc giữ “điều tra” nếu muốn giữ sắc thái hậu chiến. Phần chuyển sang thì hiện tại của nguồn mất dấu nhưng không ảnh hưởng nghĩa.
- **m4 — p000183: “nó” có hai chủ thể.** Câu đầu của đoạn dùng “Nó cho đơn vị tản ra” (Tanya), vài câu sau lại “nó có hiệu quả hay không” (chiến thuật). Dễ đọc nhầm. Đề xuất tạm: “chiến thuật này có hiệu quả hay không”. Ngoài ra “bài tập đã luyện” nên là “bài diễn tập” cho nhất quán với p000184 (“diễn tập”).
- **m5 — p000185: “đấu súng” hơi lệch.** Đây là giao tranh giữa pháp sư và pháo tàu. “Đấu súng” gợi cảnh tay đôi, nghe nhỏ hơn quy mô thật. Đề xuất tạm: “cuộc giao tranh”/“trận hỏa chiến”.
- **m6 — p000188: giọng bực của Tanya yếu đi.** “Rốt cuộc ý anh là gì khi bảo sẽ không có địch?” nhẹ hơn lời chửi thề của nguồn. Ngoài ra “người báo vụ viên” thừa “người”, và “có vẻ thảnh thơi” thêm “có vẻ” không có trong nguồn. Đề xuất tạm: “*Anh bảo không có địch là cái quái gì vậy?*” và “báo vụ viên ở CP vô tư kia”. Phạm vi nghiêng giữ nguyên, đúng.
- **m7 — p000189: “Đế quốc Mỹ” và “đơn vị trinh sát”.** (a) Ledger b06 có mục tạm “Hợp chúng quốc” cho tham chiếu U.S./Marianas (độ chắc 0,4). Cụm “American empire” ở đây chưa có mục riêng, và “Đế quốc Mỹ” mang sắc thái chính trị mạnh. Chỉ kết luận là chưa ghi ledger và cần thống nhất. Đề xuất tạm: giữ “Đế quốc Mỹ” (sát nguồn) kèm ghi ledger, phương án khác “đế quốc Hoa Kỳ”. (b) “search units” dịch “đơn vị trinh sát”; “tìm kiếm” hoặc “lục soát” sát hơn. Chưa rõ chức năng nên chưa kết luận.
- **m8 — p000190: “tuần dương hạm” mất chữ “battle”.** Theo ledger đây là phương án tạm (độ chắc 0,5, phương án khác “tàu tuần dương chiến đấu”). “Tuần dương hạm” nói chung dễ lẫn với tàu tuần dương thường. Chưa đối chiếu được với b06 (không thuộc phạm vi đọc). Đề xuất tạm: giữ theo ledger nếu b06 đã dùng như vậy, nếu không thì “tàu tuần dương chiến đấu”. Số đo “hai trăm” nguồn không ghi đơn vị, bản dịch giữ nguyên là đúng, không tự thêm đơn vị.
- **m9 — p000191: “súng bộ binh” cho small arms; “chúng ta” cuối đoạn.** “Small arms” là vũ khí cầm tay/súng nhỏ, “súng bộ binh” thu hẹp theo binh chủng. Câu cuối là suy nghĩ của Tanya về cả đội, “chúng ta” chấp nhận được; “bọn mình” gần giọng nội tâm hơn nhưng nguồn không nghiêng nên không bắt buộc. Đề xuất tạm: “súng cầm tay/vũ khí nhỏ”.
- **m10 — p000175: “người quan sát” cho lookouts; “khu trục hạm”, “soái hạm” chưa có ledger.** “Lookouts” là người canh/trực quan sát trên tàu. “Người quan sát” hơi chung, có thể gợi quan sát viên. Đề xuất tạm: “lính canh quan sát”/“lính quan sát”. “Khu trục hạm” (destroyer) và “soái hạm” (flagship) là lựa chọn hợp lý nhưng nên ghi ledger để dùng nhất quán trong chương.

## Đánh giá thuật ngữ pending (đều chưa phải canon)

| Mục | Đánh giá | Phương án tạm | Độ chắc |
|---|---|---|---|
| counter-sub combat (p000170, p000175) | Đồng ý ledger, nhất quán hai đoạn | tác chiến chống tàu ngầm; alt: tác chiến chống ngầm | 0,5 |
| marine mages (p000175) | Đồng ý, nhất quán với b06 | pháp sư thủy quân lục chiến; alt: pháp sư hải quân | 0,5 |
| Aerial Mage Battalion (p000180, p000183) | Khớp ledger; bản dịch thêm “203” từ nguồn, hợp lý | Tiểu đoàn Pháp sư Không quân 203; alt: Tiểu đoàn Pháp sư trên không | 0,6 |
| CP (p000186, p000187, p000188) | Giữ nguyên acronym là trung tính, chấp nhận | CP | 0,4 |
| battle cruiser (p000190) | Khớp ledger nhưng mất “battle”, xem m8 | tuần dương hạm; alt: tàu tuần dương chiến đấu | 0,5 |
| Wiengenberg (p000190) | Giữ nguyên tên riêng | Wiengenberg | 0,5 |
| high-angle guns / autocannon (p000191) | Khớp ledger; phương án khác “pháo phòng không” ở cuối đoạn cũng đang dùng, nên thống nhất | pháo góc cao / pháo tự động | 0,45 |
| American empire (p000189) | Chưa vào ledger; xem m7 | Đế quốc Mỹ; alt: đế quốc Hoa Kỳ / Hợp chúng quốc (theo b06) | 0,4 |
| flagship / destroyer / lookouts (p000175) | Chưa vào ledger; xem m10 | soái hạm / khu trục hạm / lính quan sát | 0,5 |
| Anson / Sue, quân hàm (p000172, p000177–p000179) | Đúng ledger (giữ từng dạng; “ông” cho Sue trần thuật) | Đại tá Anson Sue / Đại tá Sue / “ông” | — |
| Major von Degurechaff (p000180) | Quân hàm đúng | Thiếu tá von Degurechaff | — |

Nhận xét ledger: handoff ghi “6 pending terminology notes” nhưng `pending_term_count` là 7 và ledger b08 có 7 mục. Đây là chênh lệch ghi chép, không phải lỗi dịch. Không có quyết định nào ảnh hưởng cốt truyện cần hỏi người dùng. Các lựa chọn nêu trên đều chỉ là đề xuất tạm, không nâng thành canon.

## Đã kiểm tra, không có lỗi

p000173, p000174, p000177, p000179, p000181, p000182, p000184, p000186, p000187: đúng nghĩa, phủ định, đối tượng, giọng thoại và quân hàm. p000182 “nó” cho Tanya đúng DEC-P01-001. Các đoạn còn lại chỉ có điểm nhẹ ở trên.

## Báo cáo coordinator

```yaml
role: reviewer
task_id: vol-02-ch-04-b08
state: done
segment_ids:
  - YS-LN02/Text/part0022.xhtml/p000170
  - YS-LN02/Text/part0022.xhtml/p000191
files_written:
  - reviews/prose/vol-02/ch-04-b08-claude.md
validator: not_run
diff_check: not_run
review_path: reviews/prose/vol-02/ch-04-b08-claude.md
counts:
  serious: 0
  moderate: 0
  minor: 10
findings:
  - {severity: minor, segment_id: "p000170,p000171,p000172,p000178", issue: "Pronoun 'họ'/'chúng' drifts and is ambiguous for the fleet side", resolution: "Use one pronoun or repeat the noun at subject changes"}
  - {severity: minor, segment_id: "p000176", issue: "'bất ngờ' not in source", resolution: "Remove or keep as judgement call"}
  - {severity: minor, segment_id: "p000180", issue: "'điều tra' narrower than source sense", resolution: "Consider 'truy xét/nghiên cứu'"}
  - {severity: minor, segment_id: "p000183", issue: "'nó' refers to both Tanya and the tactic; 'bài tập' vs 'diễn tập'", resolution: "'chiến thuật này'; 'bài diễn tập'"}
  - {severity: minor, segment_id: "p000185", issue: "'đấu súng' understates the engagement", resolution: "'giao tranh'/'hỏa chiến'"}
  - {severity: minor, segment_id: "p000188", issue: "Tanya's griping register weakened; 'người báo vụ viên' redundant", resolution: "Stronger colloquial wording; drop 'người'"}
  - {severity: minor, segment_id: "p000189", issue: "'Đế quốc Mỹ' not in ledger and differs from b06 'Hợp chúng quốc'; 'search units' rendered 'trinh sát'", resolution: "Record in ledger, keep one form"}
  - {severity: minor, segment_id: "p000190", issue: "'tuần dương hạm' drops 'battle'", resolution: "Keep per ledger or 'tàu tuần dương chiến đấu' after reconciling with b06"}
  - {severity: minor, segment_id: "p000191", issue: "'súng bộ binh' narrows 'small arms'", resolution: "'súng cầm tay/vũ khí nhỏ'"}
  - {severity: minor, segment_id: "p000175", issue: "'người quan sát' generic for lookouts; destroyer/flagship unledgered", resolution: "'lính quan sát'; add ledger entries"}
unresolved_findings: []
term_recommendations:
  - {source_term: "American empire", proposed_vi: "Đế quốc Mỹ", alternatives_vi: ["đế quốc Hoa Kỳ", "Hợp chúng quốc"], segment_ids: ["p000189"], status: pending, confidence: 0.4}
  - {source_term: "flagship / destroyer / lookouts", proposed_vi: "soái hạm / khu trục hạm / lính quan sát", alternatives_vi: [], segment_ids: ["p000175"], status: pending, confidence: 0.5}
  - {source_term: "battle cruiser", proposed_vi: "tuần dương hạm (theo ledger)", alternatives_vi: ["tàu tuần dương chiến đấu"], segment_ids: ["p000190"], status: pending, confidence: 0.5}
  - {source_term: "search units", proposed_vi: "đơn vị trinh sát", alternatives_vi: ["đơn vị tìm kiếm"], segment_ids: ["p000189"], status: pending, confidence: 0.4}
  - {source_term: "high-angle guns", proposed_vi: "pháo góc cao", alternatives_vi: ["pháo phòng không"], segment_ids: ["p000191"], status: pending, confidence: 0.45}
commit: null
next_action: coordinator_review
```
