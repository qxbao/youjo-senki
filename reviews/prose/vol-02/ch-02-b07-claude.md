# Báo cáo phản biện văn phong và ngữ nghĩa — vol-02-ch-02-b07-review (batch lẻ, cờ risk_flags + new_pending_terms)

- **Người phản biện:** Claude (reviewer; chỉ ghi báo cáo này, không sửa bản dịch, handoff, canon, ledger hay run-state). Báo cáo không trích văn bản nguồn.
- **Phạm vi:** 27 đoạn p000141–p000167 (`YS-LN02/Text/part0014.xhtml/…`, viết tắt `pNNNNNN`). Đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, handoff b07, gói nguồn b07, bản dịch b07, `canon/*` (glossary rỗng; characters rỗng; style-guide; DEC-P01-001/002), `canon/glossary-pending.yml`, và ledger `work/run-state/pending-terms.yml` (mục `chapter2_b07_translation_proposals` cùng các tiền lệ: đại từ Tanya, Đại Quân, cụm tập đoàn quân, Bộ Chỉ huy phương Bắc, Quân đội/Lục quân Đế quốc, Cộng hòa/Khối Thịnh vượng chung/Liên bang, “binh sĩ”). Không đọc bản dịch của batch khác.

## 1. Kết luận

- **Kết luận:** `pass_with_fixes`.
- **Mức nghiêm trọng:** serious = 0; moderate = 3 (M1–M3); minor = 12 (m1–m12).
- **next_action:** người giữ quyền sửa xử lý M1–M3, cân nhắc minor, chạy lại validator + `git diff --check`, rồi commit. Reviewer chỉ cần xác nhận nhanh p000145/p000147/p000152/p000154, p000160, p000161 sau khi sửa.
- Không có quyết định nào ảnh hưởng cốt truyện cần hỏi người dùng; cả năm thuật ngữ đều là đề xuất tạm.

## 2. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự ID | Đạt: 27 đoạn p000141–p000167, đúng thứ tự, khớp 1:1 với gói nguồn. |
| Hash gói nguồn | Đạt: `b0e1af62…7ae1` khớp handoff. |
| `source_sha256` mỗi record | Đạt: khớp handoff (`3ac53161…`). |
| `glossary_version` | Đạt: khớp handoff (`d5f19d64…`). |
| `status` / `notes` | `draft` toàn bộ; `notes` rỗng; không có ghi chú làm việc lọt vào translation. |
| Nhấn mạnh (DEC-P01-002) | Đạt: nguồn có 3 cụm nhấn mạnh (p000147, p000154, p000156) và bản dịch có đúng 3 cụm `*…*` ở cùng đoạn, đúng phạm vi. Các đoạn khác không có nhấn mạnh thừa. |
| Dấu thoại | Đạt: số dấu ngoặc kép khớp nguồn ở mọi đoạn (kể cả cặp “pháp sư tình nguyện” ở p000162). |
| Phủ định / logic | Không phát hiện đảo nghĩa hay mất phủ định (p000144 “không dung thứ”, p000145 “không yêu thích… không bị nghi ngờ”, p000159 “không thể chịu thêm”, p000167 “chẳng có gì đáng lo” đều đúng). |
| Người nói | Đạt: p000146, p000153, p000155 là lời Tanya; p000148–p000150 là lời thuộc hạ; p000163, p000167 là lời binh sĩ Viper; p000142 là lời thoại (người nói không rõ từ gói nguồn, không ảnh hưởng nghĩa). p000147 và p000154 là nội tâm in nghiêng, tách đúng khỏi thoại. |
| Thứ tự quốc gia ở p000161 | Đạt: Cộng hòa, Khối Thịnh vượng chung, Hợp chúng quốc, Liên bang giữ đúng thứ tự nguồn. |
| Chuyển cảnh | p000155 → p000156 chuyển từ Tanya sang Tiểu đoàn Viper; bản dịch giữ nguyên chuyển cảnh, không tự nối hai bên. |

## 3. Phát hiện moderate

**M1 — p000145, p000147, p000152, p000154: đại từ tự quy chiếu nội tâm dùng “tôi”, lệch lựa chọn tạm và DEC-P01-001.**
- Vấn đề: DEC-P01-001 và các mục ledger (`vol02-ch01-b01/b06 …-interior-self-reference`, `vol02-ch01-b09-tanya-narration`) chọn “mình” cho nội tâm tự quy chiếu của Tanya, giữ “tôi” cho hành động/lời nói thường. Bốn đoạn này là nội tâm ngôi thứ nhất của Tanya (“tôi vẫn phải vui vẻ ra chiến trường”, “người ta sẽ cho rằng tôi…”, “Thực ra tôi chẳng yêu thích…”, “vẻ mặt của tôi”, “tôi không cần lo lắng”, “Trông tôi có ra vẻ…”, “Tôi mỉm cười…”) nhưng dùng “tôi” suốt, nên giọng nội tâm lệch so với các batch trước. p000149–p000150 (lời thuộc hạ nói) giữ “tôi” là đúng.
- Đề xuất: đổi “tôi” → “mình” ở p000145, p000147, p000152, p000154 (ví dụ p000154 “Trông mình có ra vẻ… không nhỉ? Mình mỉm cười để khỏi buột miệng chửi thề.”). Nếu coordinator muốn dùng “tôi” cho ngôi thứ nhất kể chuyện của LN02, phải ghi thành lựa chọn thay thế trong ledger và đồng bộ lại các batch trước, không để lẫn. Độ tin cậy 0,7.

**M2 — p000161: “không mang nhãn hiệu” làm lệch nghĩa “unmarked”.**
- Vấn đề: nguồn nói quả cầu chính thức không mang dấu hiệu/phù hiệu nhận diện xuất xứ nhưng thực chất do các cường quốc cung cấp. “Nhãn hiệu” (trademark/thương hiệu) gợi chuyện thương mại, làm mất ý “che giấu nguồn cung cấp”, trong khi cả đoạn dựa vào sự đối lập giữa vẻ ngoài vô danh và nguồn thực.
- Đề xuất: “tuy chính thức không mang ký hiệu nào cho thấy xuất xứ” hoặc “chính thức không đánh dấu nguồn gốc”. Độ tin cậy 0,75.

**M3 — p000160: “thấp hơn hẳn” thêm mức độ và lược “in absolute terms”.**
- Vấn đề: nguồn nói tổng số pháp sư của Entente “ít hơn xét về số tuyệt đối” (nhượng bộ trước “nhưng họ có toàn quyền chủ động”). “Hẳn” biến thành chênh lệch rõ rệt, không có trong nguồn, và làm yếu nghịch lý ở p000164 (Đế quốc đông hơn “trên giấy” nhưng thua kém cục bộ).
- Đề xuất: “Dù về tổng quân số tuyệt đối, pháp sư Liên minh Entente ít hơn, họ hoàn toàn tự do chọn…” hoặc “tính tuyệt đối thì ít hơn”. Độ tin cậy 0,7.

## 4. Phát hiện minor

- **m1 — p000144:** “suy tàn” (decline) lệch khỏi “ruin” (thân bại danh liệt/gục ngã của cá nhân); “hình thức kỷ luật” lược sắc thái “reprisal” (trừng phạt trả đũa). Đề xuất “tránh cảnh thân bại danh liệt/gục ngã” và “một đòn kỷ luật trừng phạt nào đó”.
- **m2 — p000143:** “là điều đáng kể” gượng (đáng kể thường chỉ lượng); nguồn là “có ý nghĩa/đáng lưu ý”. Đề xuất “là điều đáng lưu ý”. “Ta” mở câu ba trong nội tâm hơi lệch so với “chúng ta” trước đó và lựa chọn “mình”; có thể dùng “chúng ta” cho nhất quán.
- **m3 — p000151:** “hùa theo” (go along) thêm sắc thái xu nịnh/a dua không có trong nguồn (style-guide cấm thêm phán xét). Đề xuất “làm theo”/“hưởng ứng”.
- **m4 — p000152:** “điều đang được yêu cầu ở mình” — “mình” ở đây là “họ” nhưng trùng với đại từ nội tâm của Tanya, dễ nhầm chủ thể. Đề xuất “ở họ”.
- **m5 — p000153, p000155:** (a) “các chiến hữu” gán tình đồng đội/thân mật không có trong nguồn (DEC-P01-001: không suy quan hệ); ledger đã có tiền lệ “các binh sĩ” cho “troops”. Đề xuất “các binh sĩ” hoặc “các anh”. (b) sắc thái “chuyến đi” (trip) mỉa mai bị lược ở “lên đường đến phương Bắc”; đề xuất “chuyến đi lên phương Bắc” để khớp “leo núi/trượt tuyết” ở p000142, p000149. (c) “Các anh” ở p000155 hợp lý; cần giữ nhất quán với nội tâm p000147 (cũng “Các anh”).
- **m6 — p000149:** “vừa định đi trượt tuyết” (was about to) khác “đúng lúc đang muốn đi trượt tuyết”. Đề xuất “Tôi đang muốn đi trượt tuyết đây.”
- **m7 — p000156:** “Tiểu đoàn Viper” là tên đơn vị mới chưa nằm trong năm đề xuất của handoff và chưa có mục ledger; đề xuất ghi vào ledger là “Tiểu đoàn Viper” (giữ nguyên Viper, thay thế “Tiểu đoàn Rắn lục”), độ tin cậy 0,5. Nguồn không nêu quan hệ giữa tiểu đoàn này và đơn vị của Tanya; không suy diễn.
- **m8 — p000157, p000165:** “Lục quân Đế quốc” (Imperial Army) là phương án thay thế trong ledger; mục `b06-imperial-army` ưu tiên “Quân đội Đế quốc”. Cần đồng bộ hoặc ghi lựa chọn mới vào ledger. Cũng p000157: “củng cố lực lượng” cho “recuperate” nên là “hồi sức/phục hồi lực lượng”.
- **m9 — p000158 và p000159:** “kho tiếp tế” (p000158) và “kho hàng” (p000159) cùng chỉ “depots”; nên thống nhất “kho tiếp tế”.
- **m10 — p000160:** “Cấp chỉ huy” cho “the brass” hơi trung tính; đề xuất “cấp trên/giới chỉ huy cấp cao”.
- **m11 — p000163:** “Khốn kiếp” nhẹ hơn lời chửi nặng của nguồn; đề xuất “Mẹ kiếp” hoặc giữ “Khốn kiếp” nếu coordinator muốn mức vừa.
- **m12 — p000167:** “Chúng đến” tự thêm chủ ngữ “chúng”; nguồn chỉ nói thời điểm sớm hơn dự tính. Đề xuất “Sớm hơn dự tính rồi!” hoặc “Sớm hơn ta nghĩ!”.

## 5. Đề xuất thuật ngữ tạm (không nâng canon)

| # | Thuật ngữ | Đoạn | Đề xuất của translator | Khuyến nghị tạm | Thay thế | Lý do | Độ tin cậy |
|---|---|---|---|---|---|---|---|
| 1 | Supreme Command | p000143 | Bộ Tư lệnh Tối cao | **Bộ Tư lệnh Tối cao** (giữ) | Bộ Chỉ huy Tối cao | “Tư lệnh tối cao” là cách dùng quân sự quen thuộc; còn giữ “Bộ Chỉ huy phương Bắc” (Northern Command) để phân biệt cơ quan tối cao với bộ chỉ huy khu vực. | 0,65 |
| 2 | Great Army | p000157 | Đại quân | **Đại Quân** (viết hoa Q) | Đại quân | Ledger Vol 1 đã thay mục “các sư đoàn Đại quân” bằng “các sư đoàn Đại Quân” và có mục `great-army` = “Đại Quân”; là tên riêng nên viết hoa. Cần coordinator đồng bộ với batch đã dùng “Đại quân”. | 0,6 |
| 3 | Northern Army Group | p000157 | Cụm Tập đoàn quân phương Bắc | **Cụm tập đoàn quân phương Bắc** (chỉ hạ “Tập đoàn quân”) | Cụm tập đoàn quân phía Bắc | Ledger dùng “cụm tập đoàn quân” viết thường (ch02-b04, ch01-b10); giữ “phương Bắc” để khớp “Bộ Chỉ huy phương Bắc” trong cùng đoạn. Nếu muốn khớp Eastern Army Group (“phía Đông”), cần đổi cả Command và Group cùng lúc. | 0,5 |
| 4 | voluntary mages | p000162 | pháp sư tình nguyện | **pháp sư tình nguyện** (giữ, giữ dấu ngoặc kép) | pháp sư xung phong | “Tình nguyện” khớp “quân tình nguyện”; “xung phong” gợi lao lên trước, không hợp nghĩa “mang quốc tịch không rõ, đến hỗ trợ”. Nguồn không nói quốc tịch nên giữ trung tính, không suy diễn. | 0,7 |
| 5 | Unified States | p000161 | Hợp chúng quốc | **Hợp chúng quốc** (giữ) | Các Quốc gia Hợp nhất | “Hợp chúng quốc” là cách dịch quen thuộc cho “United States”, ngắn và tự nhiên trong chuỗi bốn cường quốc; “Các Quốc gia Hợp nhất” gượng và dễ hiểu thành số nhiều. Không suy lore từ tên gọi. | 0,55 |
| (thêm) | Viper Battalion | p000156, p000159, p000160, p000165 | Tiểu đoàn Viper | **Tiểu đoàn Viper** | Tiểu đoàn Rắn lục | Tên đơn vị; giữ nguyên Viper để tránh suy diễn; ghi vào ledger. | 0,5 |

Ghi chú: cả năm là đề xuất tạm, không tự nâng thành canon; không ảnh hưởng cốt truyện nên không cần hỏi người dùng.

## 6. Rủi ro / cần theo dõi

- Đại từ nội tâm Tanya: “tôi” (b07) so với “mình” (ledger, các batch trước) — M1 cần coordinator chọn một quy ước cho cả Vol 2.
- “Đại quân” và “Đại Quân” đang tồn tại song song giữa ledger Vol 1 và b06/b07; cần đồng bộ trước khi nhiều batch dùng tiếp.
- “Quân đội Đế quốc” và “Lục quân Đế quốc” cùng được dùng; chọn một.
- Tên riêng mới “Tiểu đoàn Viper” chưa vào ledger; quan hệ với đơn vị của Tanya chưa rõ, chờ các batch sau.
- Địa danh/nước trong chuỗi bốn cường quốc: chỉ giữ theo tên gọi, không suy lore.

## 7. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-02-b07-review
state: done
reviewed_segments: 27
serious: 0
moderate: 3
minor: 12
review_path: reviews/prose/vol-02/ch-02-b07-claude.md
findings:
  - {severity: moderate, segment_ids: [p000145, p000147, p000152, p000154], issue: "Nội tâm Tanya dùng 'tôi' thay vì 'mình' theo DEC-P01-001/ledger", suggestion: "đổi sang 'mình' hoặc ghi lại quy ước"}
  - {severity: moderate, segment_ids: [p000161], issue: "'nhãn hiệu' lệch nghĩa 'unmarked'", suggestion: "ký hiệu/dấu hiệu xuất xứ"}
  - {severity: moderate, segment_ids: [p000160], issue: "'thấp hơn hẳn' thêm mức độ, lược 'in absolute terms'", suggestion: "ít hơn xét về tổng số tuyệt đối"}
  - {severity: minor, segment_ids: [p000144, p000143, p000151, p000152, p000153, p000155, p000149, p000156, p000157, p000165, p000158, p000159, p000160, p000163, p000167], issue: "xem mục 4 (m1–m12)"}
term_recommendations:
  - {source_term: Supreme Command, proposed_vi: "Bộ Tư lệnh Tối cao", alternatives: ["Bộ Chỉ huy Tối cao"], segment_ids: [p000143], confidence: 0.65}
  - {source_term: Great Army, proposed_vi: "Đại Quân", alternatives: ["Đại quân"], segment_ids: [p000157], confidence: 0.6}
  - {source_term: Northern Army Group, proposed_vi: "Cụm tập đoàn quân phương Bắc", alternatives: ["Cụm tập đoàn quân phía Bắc"], segment_ids: [p000157, p000158, p000159], confidence: 0.5}
  - {source_term: voluntary mages, proposed_vi: "pháp sư tình nguyện", alternatives: ["pháp sư xung phong"], segment_ids: [p000162], confidence: 0.7}
  - {source_term: Unified States, proposed_vi: "Hợp chúng quốc", alternatives: ["Các Quốc gia Hợp nhất"], segment_ids: [p000161], confidence: 0.55}
  - {source_term: Viper Battalion, proposed_vi: "Tiểu đoàn Viper", alternatives: ["Tiểu đoàn Rắn lục"], segment_ids: [p000156, p000159, p000160, p000165], confidence: 0.5}
unresolved_findings: [M1, M2, M3]
validator: not_run
diff_check: not_run
commit: null
next_action: translator_fix_M1_M3_then_validate_and_commit
```
