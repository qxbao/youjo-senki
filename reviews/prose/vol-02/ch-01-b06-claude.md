# Báo cáo phản biện — vol-02-ch-01-b06 (Claude)

- Task: `vol-02-ch-01-b06-review` (lô chẵn).
- Phạm vi: `YS-LN02/Text/part0010.xhtml/p000119` → `p000152`, **34 đoạn**. Đã đối chiếu đủ 34/34; tập và thứ tự segment_id của bản dịch khớp hoàn toàn với source package.
- Đầu vào đã dùng: handoff b06, source package cục bộ (sha256 `5814b5cd…33aa` khớp handoff), `canon/` (`decisions.md`, `style-guide.md`, `glossary-pending.yml`; `glossary.yml` và `characters.yml` rỗng), `work/run-state/pending-terms.yml`, `translations/vol-02/ch-01-b06.jsonl`. Không đọc bản dịch của batch khác, không sửa tệp nào ngoài báo cáo này. Có tham chiếu báo cáo review b05 chỉ để lấy quyết định sổ pending đã áp dụng.
- Metadata JSONL: 34/34 dòng có `source_sha256` đúng, `glossary_version` `d5f19d64…f5a41` (khớp `canon/glossary.yml`), `status: draft`, `notes: []`. Số từ nguồn tính lại bằng regex của handoff = 871, khớp.
- Mọi dẫn chứng bằng segment_id và mô tả ngắn, không chép câu nguồn (zero-source-quote). Các phương án tiếng Việt là **đề xuất tạm, không phải canon**.
- Lưu ý về "translator findings": trong handoff chỉ có `minor_findings: 2`, không có nội dung chi tiết; tôi không tìm thấy văn bản finding cho p000120/p000121 trong các tệp được phép đọc. Phần đánh giá bên dưới là đánh giá độc lập hai đoạn này.

## Tóm tắt

Bản dịch nhìn chung đúng nghĩa, đúng phủ định, đúng người nói ở cả 34 đoạn; không có lỗi nghiêm trọng. Có **5 lỗi vừa**, chủ yếu là lệch sổ pending/DEC (cấp bậc Serebryakov, đại từ trần thuật của Tanya, tự quy chiếu nội tâm), một chỗ mơ hồ chủ thể ở p000132 và tên tài liệu "Field Manual" ở p000151/p000152. Cộng thêm 12 lỗi nhẹ. Nhấn mạnh khớp 3/3.

## Số lượng theo mức

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 5 |
| Nhẹ | 12 |

## Nhấn mạnh (emphasis parity, DEC-P01-002)

Nguồn có **3** chỗ nhấn mạnh (`<em>`); bản dịch có **3** cặp `*...*`, không thừa.

| segment_id | Phạm vi nhấn ở nguồn | Bản dịch | Kết luận |
|---|---|---|---|
| p000120 | cả câu hỏi nội tâm mở đầu, trước chữ "nhưng" | `*…?*` cùng phạm vi | Khớp |
| p000143 | câu hỏi nội tâm ngắn của Weiss | `*…?*` | Khớp |
| p000151 | toàn bộ tên tài liệu, nằm trong dấu ngoặc kép | `“*…*”` | Khớp (dấu ngoặc ở ngoài) |

31 đoạn còn lại không có nhấn mạnh ở nguồn và không có `*`. Chữ in hoa ở p000131 (nhấn bằng chữ hoa, không phải em) được giữ bằng chữ hoa, chấp nhận được; không cần `*`.

## Lỗi vừa (cần sửa)

**M1 — p000126, p000129, p000134, p000137 — cấp bậc Serebryakov.** Bản dịch gọi Serebryakov là "Trung úy" ở bốn đoạn (cả trần thuật lẫn lời gọi của Tanya ở p000129). Sổ `vol02-ch01-b02-lieutenant` và `vol02-ch01-b04-serebryakov-address` đề xuất Serebryakov = "Thiếu úy" (theo cấp bậc nêu rõ ở p000051), Weiss = "Trung úy"; b05 đã sửa theo đó. Ở b06 cùng đoạn p000129 có cả hai người cùng bị gọi "Trung úy" (p000129 gọi Serebryakov, p000138/p000140/p000145 gọi Weiss), dễ làm người đọc nhầm chủ thể. Batch này không có căn cứ mới để bỏ ánh xạ của sổ (nguồn chỉ ghi "Lieutenant" chung).
→ Sửa: "Thiếu úy Serebryakov" ở p000126, p000134, p000137; "Thiếu úy, đi gọi…" ở p000129. Nếu coordinator chốt "Trung úy" cho cả hai thì đồng bộ toàn chương.

**M2 — p000121, p000122, p000128, p000129, p000137 ("nó"); p000135 ("cô" ×2) — đại từ trần thuật của Tanya.** Cùng một batch dùng cả "nó" lẫn "cô" cho Tanya; trong khi sổ vol-02 (`vol02-ch01-b05-tanya-narration`, 0.6) đề xuất lặp "Tanya" hoặc lược chủ ngữ, không dùng đại từ. DEC-P01-001 ghi "nó" cho trần thuật "ở giai đoạn này" (pilot LN01) và cấm tự mở rộng sang giai đoạn khác; "cô" ở p000135 còn suy ra giới tính/quan hệ từ chỉ đại từ "she" của nguồn.
→ Đề xuất tạm: lặp "Tanya" hoặc lược chủ ngữ ở mọi chỗ trên (ví dụ p000122 "Tanya không tin nổi vào mắt mình"; p000135 "…không phải vì Tanya hiểu cử chỉ ấy theo hướng tích cực, mà chủ yếu vì chẳng để tâm đến nó"). Thay thế: "nó" nhất quán nếu coordinator giữ DEC-P01-001 cho cả LN02. Độ bất định: trung bình.

**M3 — p000132 — mơ hồ chủ thể câu cuối.** "…khiến quân đội Dacia vẫn chật vật duy trì đội hình rồi nổ súng" có thể đọc là quân Dacia nổ súng; nguồn rõ ràng là Tanya (ngôi thứ nhất) bắn. Đây là lỗi chủ thể/đối tượng hành động.
→ Sửa: tách câu, ví dụ "…duy trì đội hình. Rồi tôi bắn." (hoặc "…, và tôi nổ súng.").

**M4 — p000131, p000132, p000152 — tự quy chiếu nội tâm "tôi" so với DEC-P01-001 ("mình").** Đây là độc thoại/suy nghĩ của Tanya (cảm giác bị phản bội, "tôi cứ tưởng…", "tôi muốn dạy anh ta…"), nhưng dùng "tôi" thay vì "mình" theo sổ `vol02-ch01-b01-interior-self-reference` (0.8) và DEC-P01-001. Phần hành động ngôi thứ nhất thuần túy (p000131 "ra lệnh cho Serebryakov…", p000132 "phong ấn…/nổ súng") ở cùng mạch, nên cần quy tắc rõ để khỏi lệch giữa các đoạn.
→ Đề xuất tạm: đoạn suy nghĩ/đánh giá (nửa sau p000131, p000133 không đại từ, p000152) dùng "mình"; hành động ngôi thứ nhất giữ "tôi" như b05 chấp nhận. Thay thế: "tôi" cho toàn bộ nếu coordinator đồng bộ theo hướng đó. Độ bất định: trung bình, phụ thuộc cách b01–b05 đã chốt; không đọc các batch đó.

**M5 — p000151, p000152 — tên tài liệu "Field Manual".** (a) "thủ lệnh" thường nghĩa là lệnh viết tay/mệnh lệnh trực tiếp, không phải sách hướng dẫn; ở p000152 "viện dẫn thủ lệnh cho mọi chiến dịch" đọc như viện dẫn mệnh lệnh, lệch bình diện "manual" (sách/hướng dẫn để tra cứu; p000149 và p000150 đã dùng "sách"). (b) "tập hai mươi hai" ép đọc thành "tập" của bộ sách; nguồn chỉ là số thứ tự đứng đầu tên ("Twenty-Second …"), có thể là số bản/số hiệu. (c) "ma pháp" ở tên, nhưng p000132 dùng "ma thuật" (xem L12).
→ Xem phần thuật ngữ bên dưới.

## Lỗi nhẹ

- **L1 — p000120:** "another power" dịch "thế lực khác"; ngữ cảnh địa chính trị gợi "một cường quốc khác" sát hơn; "thế lực" mơ hồ. Đánh giá finding p000120 của translator: các điểm khác (phạm vi nhấn, "học thuyết/công nghệ", "giả thuyết khó xảy ra") đúng; chỉ nên đổi "thế lực".
- **L2 — p000121:** finding của translator: dịch "bùng nổ theo bản năng" cho "instinctively explodes" đúng nghĩa; "Sao anh lại bỏ chạy?!" giữ đúng câu hỏi (đối tượng = hành vi chạy đi). Chỉ còn lưu ý đại từ "nó" (M2). Không cần sửa thêm.
- **L3 — p000123:** "khốn khổ thật" làm nhẹ "poor bastards" (mang giọng thô, mỉa của Tanya); "nguồn nhân lực" khác "nhân lực" của sổ `vol02-ch01-b04-human-resources` (alt có "nguồn nhân lực", chấp nhận được).
- **L4 — p000129:** "hắn" cho Weiss thêm sắc thái miệt thị không có ở nguồn (style guide cấm thêm sắc thái miệt thị) và lệch "anh ta" ở p000131/p000137. Gợi ý: "anh ta".
- **L5 — p000125, p000130, p000136:** "Thiếu tá" viết hoa/thường không đồng nhất khi làm lời gọi ("Thiếu tá!!" vs "thưa thiếu tá"). Thống nhất viết hoa.
- **L6 — p000132:** "Tôi thầm cảm ơn" thêm "thầm" không có ở nguồn; "đạn ma thuật" lệch "ma pháp" (xem L12); "công thức nổ liên hợp" lệch sổ `P01-formulas` ("thuật thức", alt công thức) — hai mục sổ mâu thuẫn nên chỉ nhắc đồng bộ.
- **L7 — p000137:** "sầm sập" mô tả tiếng/độ dồn dập; nguồn chỉ nói áp sát như muốn cắn. Gợi ý "áp sát".
- **L8 — p000138, p000139:** "excuse" dịch "lý do" mất sắc thái biện bạch/đã có lỗi (p000148 dùng "lời biện bạch"). Gợi ý "lời biện bạch/bào chữa" cho nhất quán.
- **L9 — p000140:** "…hay ta thẩm vấn anh tại tòa án quân sự nhé!" — "nhé" làm giọng nhẹ đi so với cơn giận; "ta" thêm sắc thái cùng làm. Gợi ý: "thì cứ để tòa án quân sự tra hỏi anh!".
- **L10 — p000142:** "bỏ bê nhiệm vụ" yếu hơn "abandon" (cáo buộc là bỏ chạy/đào ngũ); "Người của tôi và tôi" gượng. Gợi ý: "Tôi và binh sĩ dưới quyền tuyệt đối không bỏ nhiệm vụ…".
- **L11 — p000147:** "quay đuôi bỏ chạy" không tự nhiên và lệch "quay đầu" ở p000145; gợi ý "quay đầu bỏ chạy".
- **L12 — magic/ma thuật:** p000132 "đạn ma thuật" lệch "ma pháp" trong sổ (thiếu úy ma pháp, kỹ thuật ma pháp) và ở p000151. Gợi ý "đạn ma pháp".

## Kiểm tra theo tiêu chí

- **Nghĩa/phủ định/logic:** p000119 (hai câu hỏi), p000127 (không có dấu hiệu phản công), p000140/p000147 (nghi bỏ chạy, giải thích), p000142 ("tuyệt đối không bỏ…"), p000143–p000144, p000148–p000152 đều giữ đúng; ngoại trừ M3, M5.
- **Người nói/chủ thể:** p000125 = Serebryakov, p000130/p000136 = Serebryakov, p000138/p000140/p000145/p000147/p000150 = Tanya, p000139/p000142/p000146/p000149/p000151 = Weiss, p000134 = Serebryakov báo cáo. Phân vai đúng; lỗi duy nhất ở M3. p000141 nguồn nói "sĩ quan phụ tá của chỉ huy tiểu đoàn" trong khi p000137 gọi Tanya là "chỉ huy"; bản dịch giữ literal, đúng nguồn. Quan hệ thực giữa "adjutant" ở đây với Tanya chưa rõ — không suy diễn, giữ literal "sĩ quan phụ tá" theo sổ (ghi như rủi ro R2).
- **Thuật ngữ khớp sổ:** Chúa (P06-lord), Dacia, sĩ quan phụ tá, đội hình vuông của bộ binh địch (≈ `vol02-ch01-b05-infantry-square`), Cụm Tập đoàn quân phía Đông (≈ `vol02-ch01-b02-regional-army-group`, nguồn nêu "Eastern Army Group", chấp nhận) — khớp hoặc gần khớp.
- **Giọng/đại từ:** Tanya↔Weiss "anh/tôi", Weiss↔Tanya "Thiếu tá/tôi" nhất quán; không suy quan hệ. Italic nội tâm của Weiss dùng "Mình" (p000143): không mở rộng DEC cho Tanya sang Weiss, nhưng chấp nhận được vì đây là tự quy chiếu nội tâm trung tính.

## Đề xuất thuật ngữ (4 mục pending; đều tạm, không phải canon)

| Mục | Hiện tại | Khuyến nghị tạm | Thay thế | Căn cứ (segment_id) | Độ tin cậy / bất định |
|---|---|---|---|---|---|
| vice commander | phó chỉ huy | **Giữ "phó chỉ huy"** | tiểu đoàn phó; phó tiểu đoàn trưởng | p000129, p000131 (nêu rõ phó chỉ huy của tiểu đoàn 203); p000137/p000141 dùng "chỉ huy", "chỉ huy tiểu đoàn" → "phó chỉ huy" cặp đối xứng, trung tính về chức danh chính thức | 0.65; thấp vì chức danh chính thức chưa rõ |
| Aerial Mage Battalion | Tiểu đoàn Pháp sư Không quân | **Giữ**; viết "Tiểu đoàn Pháp sư Không quân 203" | Tiểu đoàn Pháp sư Không quân số 203 | p000131; khớp `vol02-ch01-b04-aerial-mage` ("pháp sư không quân", 0.7); tránh "trên không" theo ghi chú ledger | 0.65; chưa rõ tên đơn vị chính thức |
| containment fire | bắn chế áp | **Đổi sang "bắn kiềm chế"** (hoặc "bắn khống chế") | bắn ghìm chân | p000149: lùi ra rìa tầm bắn rồi bắn vào đơn vị địch → ý nghĩa là giữ chân/kiềm chế địch, không nhất thiết áp chế hỏa lực. "chế áp" gần nghĩa "áp chế" của `vol02-ch01-b05-suppressive-fire` ("hỏa lực áp chế") → dễ nhầm hai thuật ngữ nguồn khác nhau | 0.55; trung bình, thuật ngữ quân sự nguồn chưa rõ |
| Aerial Magic Combat Field Manual | Dã chiến thủ lệnh tác chiến ma pháp không quân, tập hai mươi hai | **"Sổ tay tác chiến ma pháp không quân dã chiến, bản thứ hai mươi hai"** hoặc để số ở đầu: "Sổ tay dã chiến tác chiến ma pháp không quân (bản thứ hai mươi hai)"; ở p000152 chỉ dùng "sổ tay" | "Cẩm nang…"; "Điều lệnh…" (tránh nếu muốn chắc nghĩa "manual") | p000149–p000152: "sách" → "sổ tay/thủ lệnh/manual" cùng chỉ một tài liệu tra cứu dùng như quy chuẩn; p000152 "đến một mức nào đó" cho thấy phạm vi bao quát giới hạn như một sổ tay. "Tập" thêm hàm ý bộ sách; "bản/lần thứ" trung tính hơn nhưng vẫn là phỏng đoán | 0.45; thấp, đồng thời "ma pháp" nên đồng bộ với ledger |

Không mục nào ảnh hưởng cốt truyện, không cần hỏi người dùng. Không tự nâng canon.

## Rủi ro

- **R1:** M1/M2/M4 phụ thuộc cách b01–b05 đã áp dụng sổ; tôi không đọc các batch đó. Coordinator cần đồng bộ chéo cấp bậc Serebryakov, đại từ trần thuật Tanya, tự quy chiếu nội tâm và "thuật thức/công thức" trên toàn chương.
- **R2:** p000141 ("sĩ quan phụ tá của chỉ huy tiểu đoàn") có thể là sai lệch của nguồn dịch Anh hoặc chỉ một vai trò khác của Tanya; giữ literal, không suy ra quan hệ chỉ huy.
- **R3:** Không có văn bản chi tiết của "translator findings" trong handoff; việc xét p000120/p000121 chỉ là đánh giá độc lập.
- **R4:** Thuật ngữ quân sự (containment fire, Field Manual) dựa vào ngữ cảnh một batch; bằng chứng hạn chế, nên giữ wording trung tính và ghi bất định trong `pending-terms.yml`.

## Báo cáo coordinator

```yaml
role: reviewer
task_id: vol-02-ch-01-b06-review
state: done
segment_ids: [p000119..p000152]  # 34 đoạn, YS-LN02/Text/part0010.xhtml
files_written: [reviews/prose/vol-02/ch-01-b06-claude.md]
review_path: reviews/prose/vol-02/ch-01-b06-claude.md
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 5, minor: 12}
findings:
  - {severity: moderate, segment_id: "p000126,p000129,p000134,p000137", issue: "Serebryakov bị gọi Trung úy, lệch sổ (Thiếu úy)", resolution: "đổi Thiếu úy hoặc coordinator chốt Trung úy cho cả hai"}
  - {severity: moderate, segment_id: "p000121,p000122,p000128,p000129,p000137,p000135", issue: "Tanya lúc 'nó', lúc 'cô'; lệch sổ (lặp tên/lược chủ ngữ)", resolution: "lặp Tanya hoặc lược chủ ngữ"}
  - {severity: moderate, segment_id: "p000132", issue: "mơ hồ chủ thể 'rồi nổ súng' (có thể đọc là quân Dacia bắn)", resolution: "tách câu, nêu rõ Tôi bắn"}
  - {severity: moderate, segment_id: "p000131,p000132,p000152", issue: "tự quy chiếu nội tâm dùng 'tôi' thay vì 'mình' (DEC-P01-001)", resolution: "dùng 'mình' cho đoạn suy nghĩ; 'tôi' cho hành động; đồng bộ coordinator"}
  - {severity: moderate, segment_id: "p000151,p000152", issue: "'thủ lệnh' lệch nghĩa 'manual'; 'tập hai mươi hai' thêm hàm ý", resolution: "sổ tay…, bản thứ hai mươi hai; dùng 'sổ tay' ở p000152"}
unresolved_findings: 5  # chờ translator sửa
pending_terms: []
term_recommendations:
  - {source_term: vice commander, proposed_vi: phó chỉ huy, alternatives: [tiểu đoàn phó], segment_ids: [p000129, p000131], status: pending, confidence: 0.65}
  - {source_term: Aerial Mage Battalion, proposed_vi: Tiểu đoàn Pháp sư Không quân 203, alternatives: [Tiểu đoàn Pháp sư Không quân số 203], segment_ids: [p000131], status: pending, confidence: 0.65}
  - {source_term: containment fire, proposed_vi: bắn kiềm chế, alternatives: [bắn khống chế, bắn ghìm chân], segment_ids: [p000149], status: pending, confidence: 0.55}
  - {source_term: Aerial Magic Combat Field Manual, proposed_vi: Sổ tay tác chiến ma pháp không quân dã chiến, bản thứ hai mươi hai, alternatives: [Cẩm nang…], segment_ids: [p000151, p000152], status: pending, confidence: 0.45}
risks: [R1, R2, R3, R4]
commit: null
next_action: translator_fix_moderate_findings_then_claude_signoff
```
