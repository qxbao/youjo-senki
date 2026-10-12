# Review vol-02-ch-04-b07 (Claude, checkpoint_generation 745)

- Phạm vi: 32 đoạn, `p000138`–`p000169` (`YS-LN02/Text/part0022.xhtml/`). Mã đoạn dưới đây viết tắt `pNNNNNN`.
- Đầu vào đã đọc: shared.md, reviewer.md, config, handoff b07, canon (glossary rỗng, characters rỗng, style-guide, decisions, glossary-pending), mục liên quan trong `work/run-state/pending-terms.yml`, source package b07 (sha256 khớp `fa2f54d2…`), `translations/vol-02/ch-04-b07.jsonl`. Không mở EPUB/PDF hay batch khác. Không sửa bản dịch, handoff, ledger, canon, run-state.
- Kiểm tra cơ học: 32/32 segment_id khớp thứ tự với package; `source_sha256`, `glossary_version` khớp handoff; status `draft`; `notes` rỗng ở mọi đoạn.

## Tổng quan

Bản dịch bám sát nghĩa, không có thiếu/thừa câu, không đảo phủ định, không sai chủ thể nghiêm trọng. Lỗi chính: đại từ trần thuật Tanya lệch DEC-P01-001, thiếu nhấn mạnh ở p000165, hai đoạn mất độ mở/cấu trúc (p000152, p000156), và vài thuật ngữ lệch ledger tạm hoặc chưa ghi ledger.

## Số lượng

| Mức | Số |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 7 |
| Nhẹ | 11 |

## Lỗi mức vừa

**M1 — p000153, p000155, p000158, p000161, p000162: đại từ trần thuật “cô” cho Tanya.**
- Căn cứ: DEC-P01-001 (đã duyệt) quy định trần thuật về Tanya dùng “nó”, nội tâm dùng “mình”; ledger vol-02 (`vol02-ch01-b09-tanya-narration`, `vol02-ch01-b14-tanya-narration`) ưu tiên “nó” hoặc lặp tên/lược chủ ngữ, “cô” chỉ là phương án thay thế. Bản dịch dùng “cô” 6 lần ở 5 đoạn, trong khi p000153 vừa dùng tên “Tanya”.
- Đề xuất tạm: đổi sang “nó” hoặc lặp “Tanya”/lược chủ ngữ, ví dụ p000158 “…khiến nó chú ý…”, p000161 “Nó nheo mắt…”, p000162 “…mắt nó mở to”. Chọn một cách và dùng nhất quán trong chương.
- Phương án khác: giữ “cô” cho cả chương nếu người duyệt về sau chuyển DEC sang “cô”. Việc này là quyết định canon, không tự áp dụng.

**M2 — p000165: thiếu hai chỗ nhấn mạnh có trong nguồn.**
- Căn cứ: DEC-P01-002. Nguồn nhấn mạnh (in nghiêng) tên “aal” và đại từ chỉ đối tượng bị “bắn đi” (đội phát triển). Bản dịch không đánh dấu `*...*` nào ở đoạn này.
- Đề xuất: “Sáu quả *aal*¹¹ …” và “…vào ống phóng rồi bắn *họ* đi.” (hoặc “bắn *chúng* đi”, chọn đại từ cùng bậc với “đám”). Ở p000155 dấu `*...*` đúng phạm vi (ba câu nội tâm nghiêng, câu dẫn không nghiêng), giữ nguyên.
- Phương án khác: bỏ dấu nhấn ở “aal” nếu coi đó là tên riêng, nhưng nguồn dùng nghiêng nên khuyến nghị giữ. Cũng cân nhắc bỏ “s” sau aal (“aals” kết hợp “Sáu quả” thành dư số nhiều).

**M3 — p000152: đối tượng của câu “chưa… trong một thời gian” bị bỏ lửng.**
- Căn cứ: câu đang đáp lại câu hỏi thời tiết ở p000149; nguồn là câu tỉnh lược phủ định (“sẽ không … trong một thời gian”). Bản dịch “Có vẻ một thời gian nữa mới có” khiến người đọc hiểu là dữ liệu chưa tới, còn đối tượng thật là thời tiết chưa cải thiện; mất phủ định tường minh và chủ thể.
- Đề xuất tạm: “Có vẻ trời sẽ chưa khá lên trong một lúc nữa.” (đọc theo nghĩa thời tiết).
- Phương án khác nếu người duyệt hiểu là dữ liệu chưa tới: “Có vẻ phải một lúc nữa mới có dữ liệu.” Độ chắc chắn của cách hiểu thời tiết: khoảng 0,65 (do ngữ cảnh p000149 và p000153).

**M4 — p000154: “Phi đội Một” giả định đơn vị bay.**
- Căn cứ: nguồn nói đơn vị rời căn cứ hải quân; câu sau tách riêng “không quân” như một lực lượng khác. “Phi đội” (đơn vị bay) vì vậy dễ sai loại đơn vị, và có thể lẫn với chính phi đội Pixie.
- Đề xuất tạm: “Hải đội Một” (giả định thủy quân). Nếu muốn trung tính hơn: “Đội Một”.
- Phương án khác: giữ “Phi đội Một” nếu các đoạn khác của chương chứng minh là đơn vị bay. Chưa ghi ledger; đề nghị coordinator ghi mục pending (xem YAML).

**M5 — p000156: mất cấu trúc câu bị ngắt giữa chừng.**
- Căn cứ: nguồn kết thúc câu hỏi bằng từ bị cắt dở rồi chuyển sang “Phía dưới rất xa” và âm thanh bất ngờ ở p000158. Bản dịch viết một câu hỏi hoàn chỉnh (“…được không…?”), nên hiệu ứng bị ngắt/bị phân tâm biến mất. Ngoài ra “ships” dịch “chiến hạm” là thêm sắc thái “chiến”.
- Đề xuất tạm: “Pixie 01 nghe rõ. Cho tôi biết các tàu của Khối Thịnh vượng chung đang diễn tập hiện ở…?”
- Phương án khác: “…đang diễn tập hiện nằm ở đâ…?” (cắt giữa từ).

**M6 — p000148, p000152: “Control” và “Urban Control” dịch “Trung tâm”, “Trung tâm Đô thị”.**
- Căn cứ: ledger vol-02 có mục tạm `vol02-ch02-b15-control-short-form` cho “Control” (đề xuất “Control”, phương án “Norden Control”/“Bộ chỉ huy”); ledger cũng có “Central” → “Trung ương”. “Trung tâm” dễ lẫn với “Central”, còn “Trung tâm Đô thị” là cách hiểu “Urban” chưa có căn cứ. Các mục này không có trong ledger b07.
- Đề xuất tạm: p000148 “Control gọi Pixie…”; p000152 giữ “Urban Control” nguyên dạng (trung tính, ít suy diễn). Ghi pending.
- Phương án khác: “Trung tâm Kiểm soát Đô thị” (kém khuyến nghị: tự diễn giải “Urban”).

**M7 — p000151: “defensive shell(s)” dịch “lá chắn phòng vệ”.**
- Căn cứ: ledger `vol02-ch01-b07-defensive-shell` đề xuất tạm “lớp vỏ phòng ngự” (phương án: “kết giới phòng ngự”, “màn chắn phòng thủ”). Bản dịch lệch cả từ trung tâm và không ghi note.
- Đề xuất tạm: “Dù lớp vỏ phòng ngự ngăn được nước…”.
- Phương án khác: “màn chắn phòng thủ”. Chọn một và dùng chung cả chương.

## Lỗi mức nhẹ

- **m1 — p000140:** “chúng” rồi “họ” cùng chỉ địch/pháp sư địch; thống nhất “chúng” (hoặc “bọn chúng”).
- **m2 — p000146, p000147, p000150:** tự xưng ngôi nhất “tôi” (p000146, p000150), “mình” (p000147) trong cùng một chuỗi. Nên chọn “tôi” cho tự sự và chỉ dùng “mình” cho nội tâm nhận diện rõ (p000143, p000147). Chấp nhận được nhưng cần thống nhất.
- **m3 — p000145:** “của chúng tôi” sau “tầm nhìn” là phần thừa nhẹ.
- **m4 — p000147:** “hẳn không có ai” hơi chắc hơn mức “chắc là không có ai”.
- **m5 — p000152:** “bộ binh” thu hẹp “ground troops”; “lính mặt đất/lục quân” trung tính hơn. “khổ sở lắm” làm nhẹ ý “như ở địa ngục”.
- **m6 — p000153:** “khiến cô không tài nào hiểu nổi” lệch sang “không hiểu được”; ý gốc là choáng/ngán ngẩm. Gợi ý: “khiến nó choáng váng/ngán ngẩm”.
- **m7 — p000160:** “ùng ục” gợi tiếng sủi; nên “tiếng nổ ùng trầm đục” hoặc “tiếng nổ trầm đục”.
- **m8 — p000162:** “đèn pha” → “đèn rọi” sát hơn (đèn tìm kiếm); “mắt mở to” hơi nhẹ so với mắt trợn tròn.
- **m9 — p000164:** thiếu quá khứ hoàn thành: “Ngư lôi đã phát nổ sớm.”
- **m10 — p000167:** “sẽ không chìm” như dự đoán; nên “vẫn không chìm”. “tin chắc sẽ thành công” mạnh hơn “kỳ vọng thành công”. “chiến hạm” thêm sắc thái “chiến” cho “vessels”.
- **m11 — p000168, p000169:** “khựng suy nghĩ” hơi lủng củng, gợi ý “dòng suy nghĩ cũng khựng lại”; p000169 “sai lầm ngớ ngẩn” ngụ ý lỗi con người, trong khi nguồn nói về sự cố hỏng hóc (đang đổ lỗi cho đội phát triển); gợi ý “sự cố ngớ ngẩn”.

## Đánh giá thuật ngữ pending (đều chưa phải canon)

| Mục | Đánh giá | Phương án tạm | Độ chắc |
|---|---|---|---|
| marine mage (p000140, p000169) | Đồng ý ledger, nhất quán với b06 | pháp sư thủy quân lục chiến; alt: pháp sư hải quân | 0,5 |
| special force recon company (p000154) | Chấp nhận; “đặc nhiệm” là diễn giải thiên về “special force”, chưa chắc | đại đội trinh sát đặc nhiệm; alt: đại đội trinh sát lực lượng đặc biệt | 0,5 |
| aal (p000165) | Giữ nguyên là hợp lý, có chú thích ¹¹; ý đùa “aal/lươn” vẫn còn nhờ câu sau | aal (nghiêng); alt: aal (lươn) | 0,4 |
| Control / Urban Control (p000148, p000152) | Mới, lệch M6 | Control; Urban Control | 0,4 |
| First Squadron (p000154) | Mới, lệch M4 | Hải đội Một; alt: Đội Một | 0,4 |
| defensive shell (p000151) | Lệch ledger | lớp vỏ phòng ngự | 0,5 |
| navigation officer (p000168) | Mới; “sĩ quan hoa tiêu” chấp nhận được, chưa rõ nghĩa “hoa tiêu” (dẫn đường) | sĩ quan hoa tiêu; alt: sĩ quan hàng hải | 0,45 |
| Task Force 13 / Northern Sea Fleet / Entente Alliance / Commonwealth (p000163, p000167, p000169, p000156) | Khớp ledger | Lực lượng đặc nhiệm tàu ngầm số 13; Hạm đội Biển Bắc Đế quốc; Liên minh Entente; Khối Thịnh vượng chung | 0,5–0,55 |
| Kiël (p000154) | Giữ nguyên, ổn | Kiël | — |

Không có quyết định nào ảnh hưởng cốt truyện cần hỏi người dùng. Phần diễn giải “Urban Control”, “First Squadron” là phỏng đoán có độ chắc thấp, không dùng làm sự thật về lore.

## Đã kiểm tra, không có lỗi

p000138–p000139, p000141–p000144 (trừ m2), p000148–p000150, p000157, p000159, p000163, p000166: đúng nghĩa, phủ định, đối tượng. Các đoạn 1.º chuyển ngôi (p000143–p000151 ngôi nhất, p000153 sang ngôi ba “Tanya”) đúng theo nguồn.

## Báo cáo coordinator

```yaml
role: reviewer
task_id: vol-02-ch-04-b07
state: done
segment_ids:
  - YS-LN02/Text/part0022.xhtml/p000138
  - YS-LN02/Text/part0022.xhtml/p000169
files_written:
  - reviews/prose/vol-02/ch-04-b07-claude.md
validator: not_run
diff_check: not_run
review_path: reviews/prose/vol-02/ch-04-b07-claude.md
counts:
  serious: 0
  moderate: 7
  minor: 11
findings:
  - {severity: moderate, segment_id: "p000153,p000155,p000158,p000161,p000162", issue: "Narration pronoun for Tanya uses 'cô' contrary to DEC-P01-001", resolution: "Use 'nó' or repeat Tanya/omit subject; consistent in chapter"}
  - {severity: moderate, segment_id: "p000165", issue: "Source emphasis on 'aal' and on the object of 'bắn đi' not marked", resolution: "Add *...* per DEC-P01-002"}
  - {severity: moderate, segment_id: "p000152", issue: "Elliptical negative lost its subject; reads as data delay instead of weather not improving", resolution: "Weather reading; alt data reading"}
  - {severity: moderate, segment_id: "p000154", issue: "'Phi đội' assumes air unit for a unit leaving a naval base", resolution: "Hải đội Một provisional; alt Đội Một"}
  - {severity: moderate, segment_id: "p000156", issue: "Interrupted question rendered as complete; 'chiến hạm' adds 'war'", resolution: "Cut the sentence off; use 'tàu'"}
  - {severity: moderate, segment_id: "p000148,p000152", issue: "Control/Urban Control rendered 'Trung tâm'/'Trung tâm Đô thị', unledgered, confusable with Central", resolution: "Control; keep Urban Control; record pending"}
  - {severity: moderate, segment_id: "p000151", issue: "Defensive shell deviates from ledger provisional", resolution: "lớp vỏ phòng ngự"}
unresolved_findings:
  - M1
  - M2
  - M3
  - M4
  - M5
  - M6
  - M7
term_recommendations:
  - {source_term: "Tanya third-person narration", proposed_vi: "nó / lặp Tanya / lược chủ ngữ", segment_ids: ["YS-LN02/Text/part0022.xhtml/p000153", "YS-LN02/Text/part0022.xhtml/p000155", "YS-LN02/Text/part0022.xhtml/p000158", "YS-LN02/Text/part0022.xhtml/p000161", "YS-LN02/Text/part0022.xhtml/p000162"], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "Control (short form)", proposed_vi: "Control", segment_ids: ["YS-LN02/Text/part0022.xhtml/p000148"], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "Urban Control", proposed_vi: "Urban Control (giữ nguyên)", segment_ids: ["YS-LN02/Text/part0022.xhtml/p000152"], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "First Squadron", proposed_vi: "Hải đội Một; alt Đội Một", segment_ids: ["YS-LN02/Text/part0022.xhtml/p000154"], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "defensive shell", proposed_vi: "lớp vỏ phòng ngự", segment_ids: ["YS-LN02/Text/part0022.xhtml/p000151"], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "navigation officer", proposed_vi: "sĩ quan hoa tiêu; alt sĩ quan hàng hải", segment_ids: ["YS-LN02/Text/part0022.xhtml/p000168"], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "aal", proposed_vi: "aal (nghiêng, giữ nguyên)", segment_ids: ["YS-LN02/Text/part0022.xhtml/p000165"], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "marine mage(s)", proposed_vi: "pháp sư thủy quân lục chiến", segment_ids: ["YS-LN02/Text/part0022.xhtml/p000140", "YS-LN02/Text/part0022.xhtml/p000169"], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "special force recon company", proposed_vi: "đại đội trinh sát đặc nhiệm", segment_ids: ["YS-LN02/Text/part0022.xhtml/p000154"], volume: vol-02, chapter: 4, status: pending}
risks:
  - "M1 là lệch với DEC-P01-001 đã duyệt; nếu người giao việc muốn chuyển sang 'cô' thì cần quyết định canon riêng."
  - "M3 phụ thuộc cách đọc đối tượng của câu tỉnh lược; độ chắc ~0,65."
commit: null
next_action: translator_fix_then_signoff
```
