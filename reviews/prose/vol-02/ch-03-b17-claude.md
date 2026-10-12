# Review vol-02-ch-03-b17 (Claude) — checkpoint_generation 621

- Phạm vi: 45 đoạn, `YS-LN02/Text/part0018.xhtml/p000257` → `p000301`.
- Đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b17, `canon/*` (glossary, characters rỗng; style-guide, decisions, glossary-pending), các mục liên quan trong `work/run-state/pending-terms.yml` (kể cả `chapter3_b17_translation_proposals`), gói nguồn b17 (sha256 khớp handoff `f3d9045b…`), và `translations/vol-02/ch-03-b17.jsonl`. Không mở EPUB/PDF, gói nguồn hay bản dịch của lô khác.
- Mọi lựa chọn bên dưới là **đề xuất tạm, không phải canon**. Không có mục nào cần hỏi người dùng (không ảnh hưởng cốt truyện).
- Ký hiệu mã đoạn rút gọn: `pNNNNNN` = `YS-LN02/Text/part0018.xhtml/pNNNNNN`.

## Tổng hợp mức độ

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 8 |
| Nhẹ | 13 |

Nghĩa tổng thể, phủ định, chữ nghiêng (DEC-P01-002) và số đoạn (45/45, đủ mã) đều ổn; không thấy bỏ đoạn hay thêm đoạn. Các lỗi vừa chủ yếu là: vi phạm DEC-P01-001 (đại từ trần thuật), lệch ledger đã có (đơn vị, công thức, cấp bậc, biệt danh), và hai chỗ lệch nghĩa/sắc thái (p000268, p000296–p000297). Cần sửa các mục vừa trước khi tính hoàn tất lô.

## Lỗi vừa

### M1 — p000268: câu đáp của Tanya bị đổi chức năng
- Vấn đề: nguồn là lời Tanya đáp báo cáo của cấp dưới theo hướng "tôi thấy rồi/tôi biết rồi", chưa phải xác nhận mệnh lệnh. Bản dịch dùng từ xác nhận quân sự, khiến Tanya như tuân lệnh cấp dưới và mất ý "đã nhận ra địch".
- Đề xuất: mở đầu bằng "Tôi thấy rồi!" rồi giữ nguyên phần mệnh lệnh phía sau. Phương án khác: "Biết rồi!". Chọn "Tôi thấy rồi!" vì sát nghĩa nhất và dùng "tôi" theo ledger b12 (xưng "tôi" trong thoại với cấp dưới).

### M2 — p000268: cấp bậc Serebryakov lệch bản đồ ledger gần nhất
- Vấn đề: bản dịch dùng "Trung úy Serebryakov". Ledger b16 (reviewer) chốt tạm Serebryakov = Thiếu úy, Weiss = Trung úy; b12 từng nghiêng về giữ dạng cấp bậc theo từng đoạn nguồn. Nguồn b17 chỉ ghi chung một cấp "Lieutenant" cho cả Serebryakov (p000268) và Weiss (p000270), nên chưa đủ căn cứ để định cấp khác với b16.
- Đề xuất: theo mục mới nhất (b16) dùng "Thiếu úy Serebryakov" và giữ "Trung úy Weiss". Phương án khác: giữ "Trung úy Serebryakov" nếu coordinator chọn nguyên tắc "giữ dạng nguồn từng đoạn" của b12; khi đó ghi rõ vào ledger. Dù chọn cách nào cũng cần một quy tắc thống nhất cho cả chương. Độ chắc chắn thấp.

### M3 — p000270: "cậu" gán giới/độ thân thiết cho Weiss
- Vấn đề: ghi chú của translator nói xưng hô "trung tính", nhưng "cậu" mang sắc thái thân mật và hàm ý giới nam. Ledger b16 yêu cầu gọi theo cấp bậc, tránh đại từ giới tính; DEC-P01-001 cấm suy quan hệ/giới từ một đoạn thiếu ngữ cảnh.
- Đề xuất: bỏ đại từ, ví dụ "Trung úy Weiss, cứ chiếm khẩu đội pháo đó đi!". Phương án khác: "anh" cho Weiss nếu coordinator chấp nhận đề xuất b13, nhưng bằng chứng chưa đủ.

### M4 — p000273: "cô" trong trần thuật về Tanya
- Vấn đề: DEC-P01-001 (đã duyệt) quy định trần thuật về Tanya ở giai đoạn này dùng "nó"; đoạn này dùng "cô" hai lần, trong khi p000276 lại dùng "nó". Ngoài ra ghi chú của translator không nêu chỗ này.
- Đề xuất: "Đúng là nó…" và "nó phải lên cao hơn chúng", hoặc lặp "Tanya" nếu câu nặng chữ "nó" (ledger b11 chấp nhận lặp tên). Cùng đoạn xem thêm N6.

### M5 — p000267: tên tiểu đoàn "Không vận" lệch ledger và lệch nghĩa
- Vấn đề: ledger b06/b10 đã chọn "Tiểu đoàn Pháp sư Không quân 203"; b06 review ghi rõ cần phân biệt "không quân" với "không vận" (vận tải đường không). Bản dịch dùng "Không vận", dễ hiểu thành đơn vị vận chuyển.
- Đề xuất: "Tiểu đoàn Pháp sư Không quân 203". Phương án khác: "Tiểu đoàn Pháp sư trên không 203". Giữ nhất quán với ledger; không nâng canon.

### M6 — p000296: mất hình ảnh gỉ và thêm sắc thái hạ thấp
- Vấn đề: (a) ghi chú translator cho rằng nguồn không gợi nghĩa đen "gỉ sắt", nhưng chính p000298–p000299 dựng chuỗi hình ảnh gỉ (biệt danh, "hoen gỉ trong máu"); câu ở p000296 là mầm của chuỗi đó, nên "dai như đỉa" cắt đứt mạch. (b) "Con này" và "nó" thêm sắc thái súc vật hóa không có trong cụm chỉ người của nguồn (quy tắc style-guide: không thêm phán xét); các đoạn p000295/p000299 cùng điểm nhìn Sue dùng "cô ta/cô gái".
- Đề xuất: giữ "gỉ" và dùng "cô ta", ví dụ "Đối thủ này bám dai như gỉ. Giữ khoảng cách rồi bắn áp chế. *Đừng* để cô ta áp sát!". Phương án khác: "dai như gỉ sét", "Đứa này…". Nếu coordinator thấy "bám dai như gỉ" lạ tai, phương án dự phòng trung tính: "Cái đứa này bám dai quá." (mất hình ảnh gỉ, chỉ dùng khi buộc phải). Giữ nhấn mạnh *Đừng* như hiện tại.

### M7 — p000297 và p000298: sắc thái câu nguồn, và biệt danh
- Vấn đề (p000297):
  - "chết tiệt" mạnh hơn sắc thái "khó ưa/đáng ghét" của nguồn (thêm thô tục);
  - dấu hiệu lơ đãng/coi thường của cụm "gì gì đó" bị thay bằng "chứ gì" (đổi thành câu hỏi xác nhận);
  - "huân chương" cụ thể hóa hơn "được thưởng/khen thưởng" của nguồn;
  - "Hừ" thay cho tiếng cười khẩy (nhẹ).
- Biệt danh: ledger b10 đã có "Bạch Ngân" (confidence 0.4, phương án khác "Bạc Trắng"). b17 chọn "Bạc Trắng / Bạc Gỉ" mà không tham chiếu. Vì cùng một biệt danh xuất hiện xuyên chương, cần nhất quán; bằng chứng đều yếu.
- Đề xuất cho p000297 (câu nghiêng thứ nhất): "*Cái biệt danh Bạch Ngân gì đó khó ưa của cô ta.*" và đổi "được trao huân chương" thành "còn được khen thưởng". Giữ câu nghiêng thứ hai; có thể đổi "Hừ" thành "Ha".
- Đề xuất biệt danh (tạm): "Bạch Ngân" / "Ngân Gỉ" (bỏ "Bạch" tương ứng việc nguồn bỏ "White" ở dạng thứ hai; "gỉ" nối với "hoen gỉ" ở p000299). Phương án khác: "Bạc Trắng / Bạc Gỉ" (cặp translator, literal nhất, cần áp dụng cho cả ledger b10), "Bạch Ngân / Bạch Ngân Hoen Gỉ". Độ chắc chắn ~0.4. Cặp từ phải đồng nhất; không nâng canon.

### M8 — p000301: thuật ngữ "formula" lệch ledger
- Vấn đề: ledger vol-02 ch1 b13 (và các mục trước) dùng "thuật thức" (confidence 0.6), "công thức" chỉ là phương án khác. "Bắn công thức" cũng khó đọc hơn "phóng thuật thức". Câu cũng bỏ nét "even/còn cả" (Sue còn cầu nguyện lúc phóng) và nét "đúng như … nên" (logic mỉa mai).
- Đề xuất: "Sue thậm chí còn cầu nguyện lúc phóng thuật thức; đúng như một đòn tấn công chất đầy hy vọng mãnh liệt, nó lao thẳng vào đội hình địch." Phương án khác: "bắn công thức" nếu coordinator muốn giữ nghĩa đen; ghi rõ vì sao lệch ledger.

## Lỗi nhẹ

- N1 p000258: "Trên không ngay!" tối nghĩa/không tự nhiên. Đề xuất "Lên không ngay!"; "Báo động xuất kích!" giữ; "Nổ máy!" thay "Khởi động động cơ!" nếu cần gọn.
- N2 p000259: "không mấy sung túc" nghiêng về giàu có hơn là thiếu thốn/thiếu đầy đủ; đề xuất "không mấy đầy đủ". Cũng "lực lượng đồn trú tĩnh tại" chấp nhận được.
- N3 p000259, p000263, p000280: nguồn dùng "Sue" và "Anson" cho cùng một đơn vị/chỉ huy (đơn vị, tiểu đoàn, thành phố Os, Đại tá). Bản dịch giữ nguyên hai tên vì canon characters rỗng; khuyến nghị coordinator ghi vào ledger "Anson/Sue = một nhân vật theo ngữ cảnh, giữ từng dạng theo nguồn, chưa gộp". Không tự gộp trong bản dịch. Ở p000263 "một mớ lẫn lộn giữa vàng thau" nên đổi "vàng thau lẫn lộn" cho tự nhiên (ghi chú translator chấp nhận).
- N4 p000265: bỏ "chủ yếu" của cụm "chủ yếu là chửi rủa" (thiếu một sắc thái nhỏ); "chỉ huy Quân đội Đế quốc" có thể bị hiểu là tổng chỉ huy cả quân đội. Đề xuất: "chủ yếu là chửi rủa" và "chỉ huy phía Đế quốc tại đây" hoặc giữ nguyên nếu coordinator muốn sát chữ. "Chúa/ác quỷ" chấp nhận.
- N5 p000272: "đánh cho tơi tả" làm mềm giọng thô của độc thoại nội tâm (nguồn thô hơn). Đề xuất "bị đánh cho nát bét" hoặc tương đương khẩu ngữ hơn, không thêm tục tĩu.
- N6 p000273: "chẳng hề muốn" mạnh hơn mức "không mấy hào hứng" của nguồn; "nỗi sợ bị chúng áp sát" mất hình ảnh bị địch ở phía trên đầu, vốn nối với câu sau ("phải lên cao hơn chúng"). Đề xuất: "không mấy hào hứng" và "nỗi sợ bị chúng chiếm vị trí trên đầu".
- N7 p000276: câu hai "Nhanh chóng lên cao, nó nhắm chiếm…" lặp "lên cao/leo cao" và chủ ngữ lơ lửng. Đề xuất: "Vừa vút lên nhanh, nó vừa nhắm chiếm độ cao tác chiến ngang bằng hoặc cao hơn đối phương, rồi trông thấy…".
- N8 p000278–p000279: p000278 thêm "lực lượng" (ghi chú translator giải thích); trung tính hơn: "Không liên lạc xuống mặt đất được!". p000279 "bay lên phía chúng ta" nên là "bay lên đón đầu chúng ta"; "địch" là thêm nhẹ, có thể đổi "Tôi thấy chúng rồi!".
- N9 p000259, p000280: "Os" giữ nguyên là hợp lý; "Ôs" không nên dùng (thêm dấu không có ở nguồn, trái chuẩn tên địa danh Latin). "Osfjord" (p000280) là thuật ngữ mới chưa vào ledger; ledger b14 dịch "fjord" là "vịnh hẹp". Đề xuất tạm giữ "Osfjord" như địa danh nguyên dạng; phương án khác "vịnh hẹp Os". Không khẳng định quan hệ giữa "Os" và "Osfjord" (chưa có căn cứ).
- N10 p000286: "lý trí thực tế" thêm "lý trí" ngoài nguồn; "Phần…" viết hoa sau dấu hỏi trong khi đây là mệnh đề dẫn tiếp. Đề xuất "phần thực tế trong đầu ông mỉa mai".
- N11 p000287: "Đánh bật chúng lại!" thừa "lại". Đề xuất "Đánh bật chúng ra!" hoặc "Đẩy lùi chúng!".
- N12 p000297: xem M7 cho "Hừ"/"huân chương" nếu coordinator không nâng chúng lên mức vừa.
- N13 p000301: nét "even" và "should" (xem M8) nếu coordinator chỉ xử lý theo mức nhẹ.

## Đánh giá ghi chú của translator và thuật ngữ tạm

| Mục | Đánh giá |
|---|---|
| White Silver / Rusted Silver (p000297–298) | Chưa chấp nhận; xem M7. Tạm đề xuất "Bạch Ngân / Ngân Gỉ", dự phòng "Bạc Trắng / Bạc Gỉ". |
| formula (p000301) | Không chấp nhận mặc định "công thức"; ledger đã có "thuật thức"; xem M8. |
| Os (p000259) | Chấp nhận giữ "Os". Bổ sung "Osfjord" (N9). |
| Đơn vị 203 (p000267) | Sửa theo ledger (M5). |
| Tên đơn vị quân sự khác (Đại đội Một, khẩu đội, tiểu đoàn) | Chấp nhận. "Khẩu đội" khớp ledger b16. |
| Ghi chú "wheat and chaff = vàng thau" | Chấp nhận (N3). |
| Ghi chú "commander = chỉ huy" (p000265) | Chấp nhận có điều kiện (N4). |
| Ghi chú "group = nhóm" (p000269) | Chấp nhận. |
| Ghi chú xưng hô p000270 | Không chấp nhận (M3). |
| Ghi chú "get through to the surface" (p000278) | Chấp nhận một phần (N8). |
| Ghi chú "cô ta" (p000295) | Chấp nhận. |
| Ghi chú "dai như đỉa" (p000296) | Không chấp nhận (M6). |
| Ghi chú "sworn enemy" (p000299) | Chấp nhận. |

## Kiểm tra theo checkpoint

- Nghĩa/phủ định/thời gian giả định: ổn, ngoại trừ M1, M8, N4, N6.
- Đại từ (DEC-P01-001): "mình" nội tâm đúng (p000272, p000257, p000292, p000295, p000300); lỗi "cô" ở p000273 (M4); "cậu" ở p000270 (M3).
- Nhấn mạnh (DEC-P01-002): phạm vi nghiêng khớp nguồn ở p000257, p000286, p000291, p000292, p000295–p000298, p000300; không đánh dấu thừa.
- Ngữ liệu thuật ngữ: xem bảng trên; không có mục nào cần hỏi người dùng.

## Báo cáo cho coordinator

```yaml
role: reviewer
task_id: vol-02-ch-03-b17
state: done
review_path: reviews/prose/vol-02/ch-03-b17-claude.md
segment_ids: [p000257-p000301]  # YS-LN02/Text/part0018.xhtml
files_written:
  - reviews/prose/vol-02/ch-03-b17-claude.md
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 8, minor: 13}
findings:
  - {severity: moderate, segment_id: p000268, issue: "dap lai xac nhan quan su thay cho 'toi thay roi'", resolution: "sua M1"}
  - {severity: moderate, segment_id: p000268, issue: "cap bac Serebryakov lech ban do ledger b16", resolution: "sua M2 theo quy tac thong nhat"}
  - {severity: moderate, segment_id: p000270, issue: "'cau' gan gioi/than mat cho Weiss", resolution: "bo dai tu M3"}
  - {severity: moderate, segment_id: p000273, issue: "'co' vi pham DEC-P01-001", resolution: "doi 'no' M4"}
  - {severity: moderate, segment_id: p000267, issue: "'Khong van' lech ledger va nghia", resolution: "doi 'Khong quan' M5"}
  - {severity: moderate, segment_id: p000296, issue: "mat hinh anh gi, them sac thai suc vat hoa", resolution: "sua M6"}
  - {severity: moderate, segment_id: p000297, issue: "thong tuc, mat 'gi gi do', bien danh lech ledger", resolution: "sua M7"}
  - {severity: moderate, segment_id: p000301, issue: "formula lech ledger 'thuat thuc'; mat 'even/should'", resolution: "sua M8"}
unresolved_findings: 8  # tat ca moderate; translator can xu ly truoc khi hoan tat
term_recommendations:
  - {source_term: "White Silver / Rusted Silver", proposed_vi: "Bạch Ngân / Ngân Gỉ", alternatives_vi: ["Bạc Trắng / Bạc Gỉ", "Bạch Ngân / Bạch Ngân Hoen Gỉ"], segment_ids: [p000297, p000298], confidence: 0.4, status: pending}
  - {source_term: formula, proposed_vi: "thuật thức", alternatives_vi: ["công thức"], segment_ids: [p000301], confidence: 0.6, status: pending}
  - {source_term: "Aerial Mage Battalion", proposed_vi: "Tiểu đoàn Pháp sư Không quân 203", alternatives_vi: ["Tiểu đoàn Pháp sư trên không 203"], segment_ids: [p000267], confidence: 0.6, status: pending}
  - {source_term: "Os", proposed_vi: "Os", alternatives_vi: ["Ôs"], segment_ids: [p000259], confidence: 0.55, status: pending}
  - {source_term: "Osfjord", proposed_vi: "Osfjord", alternatives_vi: ["vịnh hẹp Os"], segment_ids: [p000280], confidence: 0.45, status: pending}
  - {source_term: "Lieutenant Serebryakov", proposed_vi: "Thiếu úy Serebryakov", alternatives_vi: ["Trung úy Serebryakov"], segment_ids: [p000268], confidence: 0.5, status: pending}
  - {source_term: "address to Weiss", proposed_vi: "gọi theo cấp bậc, bỏ đại từ", alternatives_vi: ["anh"], segment_ids: [p000270], confidence: 0.6, status: pending}
  - {source_term: "Anson / Sue", proposed_vi: "giữ từng dạng theo nguồn, chưa gộp", alternatives_vi: [], segment_ids: [p000259, p000263, p000280], confidence: 0.5, status: pending}
risks:
  - "Biệt danh và tên đơn vị phải đồng bộ với các lô trước/sau; coordinator kiểm tra ledger toàn chương."
commit: null
next_action: translator_fix_then_resignoff
```
