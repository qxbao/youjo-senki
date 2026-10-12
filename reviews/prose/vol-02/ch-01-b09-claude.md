# Báo cáo phản biện — vol-02-ch-01-b09 (Claude)

- Phạm vi: `YS-LN02/Text/part0010.xhtml/p000219` → `p000243`, **25 đoạn**. Viết tắt `pNNNNNN`. Đã đối chiếu 25/25.
- Đầu vào đã đọc: handoff b09, `work/vol-02/batches/ch-01-b09-source.jsonl` (kèm XHTML để kiểm tra nhấn mạnh), `translations/vol-02/ch-01-b09.jsonl`, `canon/` (decisions, style-guide, glossary-pending, glossary, characters), `work/run-state/pending-terms.yml`, `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`. Không đọc bản dịch hay nguồn lô khác; chỉ tra sổ pending để kiểm tra nhất quán thuật ngữ và cấp bậc.
- Không chép câu nguồn. Mọi thuật ngữ dưới đây là **đề xuất tạm, không phải canon**. Không sửa bản dịch, handoff, sổ pending hay canon.

## 1. Kiểm tra cấu trúc

| Hạng mục | Kết quả |
|---|---|
| Số dòng / thứ tự `segment_id` | 25/25, khớp tuyệt đối với source package. |
| Hash package | `dd8bd5f2…` khớp handoff. Mọi dòng JSONL mang `source_sha256` `3ac53161…` và `glossary_version` `d5f19d64…`, khớp handoff. |
| Hash canon | 5/5 tệp khớp handoff. |
| Nhấn mạnh (DEC-P01-002) | Nguồn có đúng 2 chỗ in nghiêng: p000219 và p000241. Bản dịch có `*…*` đúng hai chỗ này, phạm vi khớp (p000219: cả câu nội tâm; p000241: cả câu hỏi trích nội tâm). Không thêm/bớt. |
| Phủ định / logic | Không phát hiện đảo phủ định hay sai quan hệ điều kiện. |

## 2. Phát hiện

**Tổng: nghiêm trọng 0 · vừa 4 · nhẹ 10.**

### Mức vừa

- **M1 — đại từ chỉ Tanya (p000221, p000224, p000225, p000234, p000235, p000243):** trần thuật dùng “cô” 13 lần; nội tâm ngôi nhất ở p000234 cũng dùng “cô”. DEC-P01-001 (đã duyệt) và các lô b07–b08 dùng “nó” cho trần thuật và “mình” cho nội tâm tự quy chiếu; sổ pending cũng ghi tránh “cô”. Đề xuất: đổi các “cô” trần thuật sang “nó” hoặc lặp tên Tanya/lược chủ ngữ khi “nó” dễ nhầm (p000221 nhiều “cô” liền nhau nên lược bớt; p000225 “đại đội pháp sư của nó” dễ đọc nhầm nên dùng “của Tanya”); riêng vế cuối p000234 (“không ngẩng mặt được”) là nội tâm ngôi nhất → “mình”. Phần còn lại của p000221 (“theo cách nhìn của chính…”) giữ nghĩa “từ góc nhìn của Tanya”.
- **M2 — p000225, “chút ít súng ngắn”:** nguồn nói bên kia chỉ có súng ngắn, tức giới hạn vũ khí (“không hơn gì súng ngắn”), không phải số lượng ít. “Dùng chút ít” đổi quan hệ thành lượng. Đề xuất: “chỉ với súng ngắn mà đối đầu với pháp sư ở cự ly gần…”. Căn cứ: nghĩa, không phải thuật ngữ (nguồn nêu rõ loại pistol nên “súng ngắn” ở đây đúng, khác lỗi “sidearms” ở b07).
- **M3 — p000238, biệt danh chơi chữ (finding duy nhất của translator):** nguồn dùng biệt danh gồm một tiền tố chửi tục + hậu tố “-guchi” + địa danh Imphal. Bản dịch “gã ngu ngốc ở Imphal” mất (a) hậu tố tên riêng là chỗ chơi chữ, (b) mức tục của tiền tố, (c) tính gắn với tên người. Đồng ý với translator là mất chơi chữ, nhưng nâng lên mức vừa vì mất cả sắc thái giọng Tanya (thô, mỉa, bình luận nội tâm) lẫn dấu hiệu tham chiếu; sửa chi phí thấp. Khuyến nghị ở mục 3.1.
- **M4 — p000219, “Trung úy nhất”:** “Trung úy nhất” không phải bậc quen thuộc trong hệ cấp bậc tiếng Việt và lệch với bản đồ cấp bậc tạm đã dùng suốt tập (Weiss = Trung úy; sổ pending b02, b06, b08). Cùng một người ở p000239 là “Trung úy Weiss”. Đề xuất: “Trung úy Weiss” cho p000219, nhất quán (xem mục 3.2).

### Mức nhẹ

- **L1 — p000226:** “chiến lợi phẩm quý giá” thêm tính từ “quý giá” và bỏ ý “quà lưu niệm” (souvenir) vốn mang giọng đùa, nối mạch với “món quà chia tay” (p000228) và “tham quan” (p000231). Đề xuất: “quà lưu niệm” hoặc “món quà mang về”.
- **L2 — p000234:** “Tình hình căng thẳng thấp” sát chữ, dễ đọc thành “tình hình chưa căng”; nguồn nói mức căng thẳng/cảnh giác của binh lính thấp. Đề xuất: “việc họ chùng xuống cũng dễ hiểu”. “Cảnh cáo” (warn) nặng hơn “nhắc nhở/cảnh báo”; “cảnh giác” lặp ba lần trong ba câu.
- **L3 — p000235:** “thành hàng dọc” thêm ý “cột dọc”; nguồn chỉ nói theo hàng ngũ. Đề xuất: “thành hàng ngũ” / “theo đội hình hành quân”. “cổ đại” cho “ancient” hơi cực đoan; có thể “cổ xưa/lạc hậu” nếu muốn gần giọng Tanya.
- **L4 — p000232:** “anh” gán xưng hô thân mật/giới tính cho người được gọi, trong khi nguồn không cho biết người nói và người nghe (có thể Weiss hoặc Serebryakov; người nói là một binh sĩ chưa xác định). DEC-P01-001 cấm suy ra từ một đoạn thiếu ngữ cảnh. Đề xuất lược đại từ: “Trung úy có sơn không? Tôi muốn làm…”. Rủi ro chủ thể: ghi vào pending.
- **L5 — p000240:** “những người khác” có thể đọc thành thuộc hạ khác của Weiss. Ngữ cảnh p000241 cho thấy là số quân địch còn lại. Đề xuất: “Còn số còn lại thì sao?” (giữ độ mở).
- **L6 — p000225:** “kết cục chắc chắn sẽ được ghi vào sách giáo khoa Dacia đã thành hiện thực” lủng củng; đề xuất “kết cục mà sách giáo khoa Dacia hẳn sẽ ghi lại không mấy chốc đã thành hình”.
- **L7 — p000242:** “Không quân” cho “air fleet” bỏ sắc thái đơn vị (một biên chế bay, không phải binh chủng). Ứng viên: “phi đội/đội bay”. Chưa đủ căn cứ chọn; thêm vào pending như thuật ngữ mới nhưng không bắt buộc sửa.
- **L8 — p000231:** “tờ rơi” hơi lệch so với pamphlet du lịch; “tờ gấp” hoặc “sổ tay hướng dẫn” gần hơn. Không bắt buộc.
- **L9 — p000241:** “anh ta/gã này” cho Weiss trong nội tâm Tanya chấp nhận được; không phát hiện lỗi chủ thể. Ghi nhận trùng quy ước ngôi ba nam ở sổ pending (không phải lỗi).
- **L10 — p000230:** “mánh cổ điển; chiến thuật ấy…” dùng dấu chấm phẩy làm câu hơi gãy; đề xuất “nhưng cũng là chiêu kinh điển, được dùng lâu nay vì nó hiệu quả”. Nghĩa đúng.

### Các đoạn đã kiểm tra, không có phát hiện thêm

p000220, 222, 223, 224, 227–229, 233, 236, 237, 239, 243: nghĩa, chủ thể, xưng hô, giọng ra lệnh/mỉa của Tanya đều đạt. Đối thoại Tanya với tù binh dùng “Các vị”, khớp bản đồ tạm đã dùng (Gentlemen = Các vị); “Rõ, Thiếu tá” (p000240) khớp Major = Thiếu tá.

## 3. Đề xuất thuật ngữ tạm (không canon)

### 3.1 p000238 — biệt danh chơi chữ

Nguyên tắc ít suy diễn: giữ “Imphal” như nguồn; không tự mở rộng thành họ tên đầy đủ hay thêm chú thích (việc nhận diện nhân vật lịch sử là suy luận lore, không được nguồn xác nhận trong đoạn). Giữ cấu trúc “tiền tố chửi + -guchi”, mức tục và giọng độc thoại của Tanya.

| Thứ hạng | Phương án | Độ tin cậy | Ghi chú |
|---|---|---|---|
| 1 (đề xuất) | “gã Khốn-guchi ở Imphal” | 0,50 | Giữ hậu tố, mức chửi vừa phải, đúng giọng mỉa của Tanya. |
| 2 | “gã Cứt-guchi ở Imphal” | 0,40 | Sát nghĩa đen nhất; tục hơn, rủi ro lệch giọng xuất bản. |
| 3 | “gã Nhảm-guchi ở Imphal” | 0,40 | Nhẹ hơn, nghĩa “nói nhảm/toàn chuyện nhảm” gần ý “đầy rác”. |
| 4 | giữ “gã ngu ngốc ở Imphal” | 0,35 | An toàn nhưng mất hậu tố và mức tục; chỉ dùng nếu không chấp nhận gạch nối. |

Bất định: chưa biết các lần xuất hiện khác trong tập/bộ truyện dùng biệt danh này thế nào; coordinator nên ghi vào sổ pending để dịch nhất quán nếu lặp lại. Không ảnh hưởng cốt truyện nên không cần hỏi người dùng.

### 3.2 Sáu thuật ngữ

| Nguồn | Mã đoạn | Đề xuất tạm | Phương án thay | Độ tin cậy | Nhận xét |
|---|---|---|---|---|---|
| First Lieutenant | p000219 | **Trung úy** (Weiss) | “Thượng úy” (nếu bản đồ cấp bậc chuyển lên một bậc); “Trung úy nhất” không khuyến nghị | 0,55 | Phù hợp bản đồ đang dùng (Weiss = Trung úy) và p000239. Nếu sau này cần phân biệt “Lieutenant” với “First Lieutenant” thì xét lại toàn tập cùng lúc. |
| close-quarters battle | p000225 | **giao chiến ở cự ly gần** (giữ) | “chiến đấu cự ly gần”, “cận chiến” | 0,65 | “Cận chiến” dễ gợi tay không/binh khí lạnh, lệch với pháp sư và súng ngắn. |
| booby trap | p000227, p000230 | p000227: **bẫy** (giữ trung tính); p000230: **bẫy nổ** | “bẫy gài”, “mìn bẫy” | 0,60 | p000229 xác nhận cơ chế nổ, nên “bẫy nổ” có căn cứ ở p000230; “mìn” suy diễn loại thuốc nổ nên không dùng. Nếu muốn một từ duy nhất cho cả hai đoạn: “bẫy gài”. |
| Principality | p000235 | **Công quốc** (giữ) | “lãnh địa công tước” | 0,75 | Khớp b02 và quen thuộc trong tiếng Việt. Ở đoạn này là cách gọi khác của Dacia; đã đúng. |
| aerial mage | p000235 | **pháp sư không quân** (giữ vì nhất quán) | “pháp sư trên không” | 0,65 | “Không quân” có thể gợi binh chủng; cân nhắc “trên không” nhưng đổi giữa chừng sẽ phá nhất quán b01–b08. Giữ nguyên, ghi rủi ro cho coordinator xét toàn cục nếu muốn. Tên tiểu đoàn giữ “Tiểu đoàn Pháp sư Không quân 203” như b06. |
| blitzkrieg tactics | p000238 | **chiến thuật chiến tranh chớp nhoáng** | “chiến thuật chớp nhoáng” (hiện tại); giữ “Blitzkrieg” nguyên văn | 0,55 | “Chiến thuật chớp nhoáng” hơi chung (có thể là “nhanh”); thêm “chiến tranh” giữ đúng tham chiếu. Ngữ cảnh không ảnh hưởng cốt truyện. |

## 4. Rủi ro

- Chủ thể/người nghe ở p000232 không rõ (L4); chưa đủ căn cứ chọn giữa Weiss và Serebryakov.
- Tham chiếu lịch sử (Ý–Ethiopia ở p000234; Imphal ở p000238) được dịch giữ nguyên tên địa danh/quốc gia; không nên thêm chú thích khi chưa có quyết định định dạng chú thích trong `decisions.md`.
- Việc đổi “cô” → “nó” (M1) có thể gây nhầm đối tượng trong một số câu; ưu tiên lặp tên hoặc lược chủ ngữ.

## 5. Báo cáo (YAML)

```yaml
role: reviewer
task_id: vol-02-ch-01-b09
state: done
segment_ids: [p000219..p000243]   # 25/25, YS-LN02/Text/part0010.xhtml
review_path: reviews/prose/vol-02/ch-01-b09-claude.md
files_written: [reviews/prose/vol-02/ch-01-b09-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 4, minor: 10}
unresolved_findings:
  - {severity: moderate, segment_id: p000221/p000224/p000225/p000234/p000235/p000243, issue: "dùng “cô” cho Tanya thay vì “nó”/“mình”", resolution: "đổi theo DEC-P01-001"}
  - {severity: moderate, segment_id: p000225, issue: "“chút ít súng ngắn” đổi giới hạn vũ khí thành lượng", resolution: "“chỉ với súng ngắn”"}
  - {severity: moderate, segment_id: p000238, issue: "mất chơi chữ/mức tục của biệt danh", resolution: "“gã Khốn-guchi ở Imphal” (phương án thay ở mục 3.1)"}
  - {severity: moderate, segment_id: p000219, issue: "“Trung úy nhất” lệch bản đồ cấp bậc", resolution: "“Trung úy Weiss”"}
term_recommendations:
  - {source_term: First Lieutenant, proposed_vi: "Trung úy", segment_ids: [p000219], status: pending, confidence: 0.55}
  - {source_term: close-quarters battle, proposed_vi: "giao chiến ở cự ly gần", segment_ids: [p000225], status: pending, confidence: 0.65}
  - {source_term: booby trap, proposed_vi: "bẫy (p000227) / bẫy nổ (p000230)", segment_ids: [p000227, p000230], status: pending, confidence: 0.60}
  - {source_term: Principality, proposed_vi: "Công quốc", segment_ids: [p000235], status: pending, confidence: 0.75}
  - {source_term: aerial mage, proposed_vi: "pháp sư không quân", segment_ids: [p000235], status: pending, confidence: 0.65}
  - {source_term: blitzkrieg tactics, proposed_vi: "chiến thuật chiến tranh chớp nhoáng", segment_ids: [p000238], status: pending, confidence: 0.55}
  - {source_term: "nickname with -guchi suffix (Imphal)", proposed_vi: "gã Khốn-guchi ở Imphal", segment_ids: [p000238], status: pending, confidence: 0.50}
  - {source_term: air fleet, proposed_vi: "chưa chốt; ứng viên “phi đội/đội bay”", segment_ids: [p000242], status: pending, confidence: 0.35}
risks:
  - "p000232: chủ thể/người nghe không rõ; tránh “anh”."
  - "Tham chiếu lịch sử p000234/p000238: không chú thích khi chưa có quyết định."
commit: null
next_action: translator_fix_then_resignoff   # sửa M1–M4 (và L1–L5 nếu tiện), không cần hỏi người dùng
```
