# Báo cáo review — vol-02-ch-04-b04 (Claude)

- Task: `vol-02-ch-04-b04`; checkpoint_generation: 715; phạm vi: 33 đoạn, từ `YS-LN02/Text/part0022.xhtml/p000063` đến `p000095` (dưới đây viết tắt là pNNNNNN).
- Đầu vào đã đọc: shared.md, reviewer.md, config/translation-pipeline.yml, handoff b04, canon (style-guide, decisions, glossary-pending, glossary, characters), các mục liên quan trong `work/run-state/pending-terms.yml` (`chapter4_b04_translation_proposals` và các mục Operations / Northern Sea Fleet / orderly / Officer of the Week / computation orb / General Staff / mobilize), gói nguồn b04 và `translations/vol-02/ch-04-b04.jsonl`. Báo cáo b03 chỉ được xem để lấy định dạng.
- Không mở EPUB/PDF, gói nguồn hay bản dịch khác; không sửa bản dịch, handoff, ledger, canon, run-state. Báo cáo không trích câu nguồn; mọi đề xuất là phương án tạm, không phải canon.
- Đối chiếu kỹ thuật: sha256 gói nguồn khớp handoff (`a247d7ac…0240`); 33/33 mã đoạn khớp và cùng thứ tự; status `draft`; `notes` rỗng ở mọi đoạn (handoff nhắc "2 ghi chú thuật ngữ mức nhẹ" nhưng chúng không có trong JSONL nên không đánh giá được). Chữ nghiêng: p000090, p000091 có `<em>` bao toàn đoạn ở nguồn và bản dịch dùng `*...*` bao toàn đoạn đúng DEC-P01-002; không có nhấn mạnh thừa/thiếu ở đoạn khác.

## Số lượng

| Mức | Số |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 6 |
| Nhẹ | 16 |

Không bỏ sót đoạn, không đảo phủ định, không thêm ý lớn. Các lỗi vừa nằm ở: đại từ gây nhầm đối tượng (p000074), lệch chức danh/thuật ngữ so với ledger (p000078, p000092, p000093), phạm vi "mọi người" (p000087) và đại từ nội tâm trong lời kể ngôi ba (p000079).

## Phát hiện mức vừa

**M1 — p000074: "mình" trong câu hỏi nội tâm bị hiểu thành Tanya, trong khi nguồn chỉ những người khác.**
- Căn cứ: câu hỏi hỏi liệu các quý ông kia có thầm mừng vì người bị đẩy ra trận không phải là chính họ. Bản dịch viết "người gặp chuyện không phải là mình"; theo DEC-P01-001, "mình" trong nội tâm quy chiếu Tanya, nên người đọc hiểu "mừng vì người gặp chuyện không phải là Tanya", đảo đối tượng của câu hỏi (vi phạm quy tắc giữ nguyên đối tượng câu hỏi nội tâm).
- Đề xuất tạm: "…không ai trong số họ đang thầm mừng vì người gặp chuyện không phải là họ không?"
- Thay thế: "…không ai trong số họ đang thầm thấy may vì kẻ phải ra trận không phải là họ không?" Tránh mọi cách viết dùng "mình" cho họ, vì "mình" theo DEC-P01-001 luôn có thể bị hiểu là Tanya. Độ chắc chắn về lỗi: cao; về từ thay thế: trung bình.

**M2 — p000078: "sĩ quan tùy viên" cho orderly (lệch ledger, đổi cấp/vai) và mất "xe/lái".**
- Căn cứ: ledger `vol02-ch03-b09-orderly` đang tạm dùng "lính phục vụ" (thay thế: "lính liên lạc"), tức binh sĩ, không phải sĩ quan; "sĩ quan tùy viên" thêm cấp bậc/vai không có căn cứ (vi phạm giới hạn suy luận về cấp bậc). Ngoài ra câu "xe đã chờ sẵn với cấp dưới cầm lái" bị rút thành "cấp dưới … chờ sẵn bên ghế lái": mất "xe đang chờ" và "bên ghế lái" gần với "ngồi cạnh tay lái", không phải "đang cầm lái".
- Đề xuất tạm: "Hẳn người phục vụ chu đáo kia đã báo cho lính phục vụ ở phòng chờ. Chiếc xe có cấp dưới của nó ngồi sau tay lái đã chờ sẵn."
- Thay thế: "lính liên lạc"; "đang chờ sẵn, cấp dưới của nó ở vị trí lái". Giữ pending.

**M3 — p000087: "kể cả" đổi phạm vi của "mọi người".**
- Căn cứ: nguồn nói gọi mọi người quay về từ kỳ nghỉ phép nửa ngày (mọi người đều đang nghỉ nửa ngày). Bản dịch "gọi mọi người quay về, kể cả những người đang nghỉ phép nửa ngày" ngụ ý còn nhóm khác ngoài nhóm nghỉ nửa ngày, làm sai phạm vi (vi phạm quy tắc giữ phạm vi/quan hệ logic).
- Đề xuất tạm: "…Vâng, đã rõ, lệnh động viên. Tôi sẽ gọi mọi người đang nghỉ phép nửa ngày quay về."
- Thay thế: "Tôi sẽ triệu hồi mọi người khỏi kỳ nghỉ nửa ngày."

**M4 — p000092: "Ban Tác chiến" lệch ledger ("Cục Tác chiến" / "phía Tác chiến").**
- Căn cứ: ledger `vol02-ch01-b15-operations`, `vol02-ch03-b10-operations-division`, `vol02-ch03-b04-logistics-operations-staff` thống nhất "Cục Tác chiến" (hoặc "phía Tác chiến" khi chỉ chức năng); "Ban Tác chiến" chỉ là phương án thay thế bị xếp sau. Cùng đoạn có phần lệch phụ: "đích thân" bị đặt sang "lấy cớ thanh tra" (nguồn nhấn việc ông ta có mặt tại Norden; xem N15).
- Đề xuất tạm: "…Tướng von Rudersdorf bên Cục Tác chiến lại đích thân có mặt ở Norden với cớ thanh tra?"
- Thay thế: "phía Tác chiến" (nếu muốn giữ mức chức năng rộng). Đây là lựa chọn nhất quán, không phải canon.

**M5 — p000093: "Hạm đội Bắc Hải" lệch đề xuất tạm của chính batch (ledger ghi "Hạm đội Biển Bắc").**
- Căn cứ: `chapter4_b04_translation_proposals` / `vol02-ch04-b04-northern-sea-fleet` chọn "Hạm đội Biển Bắc" theo b19 chương 3 (reviewer đã ưu tiên dạng đó); "Bắc Hải" là đề xuất cũ của b12. Hai dạng cùng tồn tại sẽ làm tên đơn vị trôi trong cùng chương. Độ tin của ledger chỉ 0,5, nên đây là lỗi nhất quán, không phải lỗi nghĩa.
- Đề xuất tạm: "Điện tín từ Bộ chỉ huy Hạm đội Biển Bắc của Hải quân Đế quốc!" (p000095 dùng "hạm đội" chung, không cần đổi.)
- Thay thế: giữ "Hạm đội Bắc Hải" nhưng khi đó coordinator phải đổi ledger b04 để khớp.

**M6 — p000079: đại từ nội tâm "mình" trong lời kể ngôi ba.**
- Căn cứ: nguồn ở p000079 là trần thuật ngôi ba ("she"), cả câu đầu lẫn câu sau; bản dịch dùng "nó" ở câu đầu rồi "mình" ở câu sau ("Đúng là mình đã không tiếc tiền boa…"). DEC-P01-001: trần thuật dùng "nó", "mình" chỉ cho nội tâm tự quy chiếu; không có chỉ dấu ngôi nhất ở đây. b03 đã sửa lỗi tương tự (đại từ nội tâm không nhất quán) ở mức vừa.
- Đề xuất tạm: "Nó đã đúng khi không keo kiệt tiền boa cho những người phục vụ."
- Thay thế (nếu coordinator coi đây là lời nghĩ tự do): giữ "mình" nhưng thêm dấu nội tâm rõ hơn. Độ chắc chắn: trung bình (có thể coi là cách chuyển giọng chủ ý).

## Phát hiện mức nhẹ

- **N1 — p000065**: "những người địa phương này" làm mất sắc thái "nhân vật có tên tuổi"; "tưởng rằng đó là tin tốt" thêm ý hiểu lầm, nguồn chỉ nói số tiền là tín hiệu rằng tin là điều may mắn. Gợi ý: "những người có máu mặt ở địa phương", "lại là tín hiệu cho thấy đó là tin may mắn".
- **N2 — p000067**: "cau mày vụng về" lệch "unrefined" (thô, không được che giấu). Gợi ý: "cau mày không giấu nổi" / "cau mày thô".
- **N3 — p000068**: "Vậy thì…" mang nghĩa điều kiện ("nếu thế thì"), trong khi nguồn là câu bỏ lửng cảm thán. Gợi ý: "Ôi! Chuyện đó thì…" / "Ôi! Thế là…".
- **N4 — p000069**: "Dù sao" làm yếu sắc thái mỉa nhẹ của "Well". Gợi ý: "Chà, họ có thiện ý của những kẻ không phải ra chiến trường mà."
- **N5 — p000070**: "tập kích" thu hẹp "assault" (cuộc tấn công); "khó xử" không đúng "phức tạp". Gợi ý: "đợt tấn công"; "chuyện này thật phức tạp, nhưng đành chịu vậy". (Ledger chưa có mục "assault" chung.)
- **N6 — p000071**: "Cốt lõi của con người là động vật chính trị" ngữ pháp gượng. Gợi ý: "Về bản chất, con người là động vật chính trị, nhưng đồng thời cũng là động vật xã hội."
- **N7 — p000073**: "thượng lộ bình an" thay lời chúc chung bằng lời chúc đường đi (suy ra từ ngữ cảnh); "cô" cạnh "Thiếu tá" thừa và suy ra xưng hô khi chưa có căn cứ quan hệ (DEC-P01-001). Gợi ý: "…Chúc Thiếu tá mọi điều tốt lành." Biên giới mức vừa; giữ nhẹ vì tác động nhỏ.
- **N8 — p000076**: "Bộ quân phục khiến nó trông rất chỉnh tề" đổi câu nêu trang phục thành quan hệ nhân quả. Gợi ý: "Nó ăn mặc chỉnh tề, tức là quân phục."
- **N9 — p000077**: "chỉ để làm thời trang" thêm "chỉ" (tính loại trừ) không có ở nguồn. Gợi ý: "mặc áo măng tô như một thứ thời trang". "Áo măng tô" cho trench coat là phương án tạm; "áo trench" là thay thế.
- **N10 — p000078**: "chu đáo" lặp hai lần cho hai từ nguồn khác nhau (thoughtful / efficient). Gợi ý: "cách sắp xếp gọn gàng, hiệu quả".
- **N11 — p000081**: "cậu" cho Hạ sĩ là phỏng định xưng hô thoại khi chưa có canon; giữ pending. Thay thế: "anh".
- **N12 — p000082**: "thưa Thiếu tá" thêm cấp bậc không có trong nguồn; ledger `vol02-ch02-b04-maam-neutral-rank` đang tạm dùng "thưa chỉ huy" (thay thế: "thưa Thiếu tá"). Nhẹ vì thay thế ledger cho phép.
- **N13 — p000083**: "cho xe chạy nhanh" thêm ý "nhanh"; "kết nối với đồn trú" gượng (garrison). Gợi ý: "Hạ sĩ cho xe chạy"; "kết nối với nơi đồn trú / doanh trại". Phần còn lại ổn (chuông thứ hai, "quả cầu tính toán" theo ledger).
- **N14 — p000088**: "coi như cho nghỉ" làm nhạt "nominal" (trên danh nghĩa); "chợt nghĩ" thêm tính bất ngờ. Gợi ý: "với danh nghĩa cho nghỉ"; "nghĩ đến".
- **N15 — p000092**: "đích thân" xuất hiện hai lần ở chỗ không khớp: "đích thân chọn nó" (nguồn là "chỉ định riêng nó") và "đích thân lấy cớ thanh tra" (nguồn nhấn ông ta có mặt tại chỗ). Gợi ý: "Việc họ chỉ định riêng nó để truyền lệnh…"
- **N16 — p000095**: "nhìn nhau ngơ ngác" thêm hành động "nhìn nhau" (nguồn chỉ nói vẻ mặt bối rối); "cũng tự hỏi như" hơi yếu so với "chung câu hỏi". Gợi ý: "chung câu hỏi ẩn sau vẻ mặt ngơ ngác của các sĩ quan…". "Chúng ta" tạm ổn trong nội tâm.

Các đoạn không có lỗi đáng ghi: p000063, p000066, p000072, p000075, p000080, p000084–p000086, p000089–p000091, p000094. (p000064 dùng "Tin tốt chứ" thích hợp.)

## Đánh giá thuật ngữ và ghi chú đang pending

| Mục | Đánh giá | Khuyến nghị tạm |
|---|---|---|
| Tiểu đoàn Pháp sư Không quân 203 (p000088, p000095) | Khớp ledger | Giữ; thay thế "…trên không". |
| sĩ quan trực ban tuần (p000083) | Khớp ledger b09; "trực ban" là trực hằng ngày nên lai "tuần" hơi gượng | Giữ tạm; thay thế "sĩ quan trực tuần". Tin cậy thấp. |
| Hạm đội Biển Bắc / Bắc Hải (p000093) | Bản dịch lệch ledger b04 | Dùng "Biển Bắc" (M5) hoặc cập nhật ledger. |
| Norden (p000092) | Giữ nguyên đã hợp lý | Giữ nguyên dạng nguồn; phiên âm là thay thế. |
| orderly (p000078) | Bản dịch lệch ledger | "lính phục vụ" (M2). |
| Operations (p000092) | Bản dịch lệch ledger | "Cục Tác chiến" (M4). |
| quả cầu tính toán (p000083), Bộ Tổng Tham mưu (p000090, p000092), lệnh động viên (p000086, p000087), Hạ sĩ (p000081) | Khớp ledger/lẽ thường | Giữ; "lệnh động viên" tương thích mục "động viên quân". |
| Mục "General (address)" b03 trong ledger b04 | Không áp dụng cho b04 (không có thoại gọi Tướng) | Không đổi. |

Không có điểm nào ảnh hưởng cốt truyện cần hỏi người dùng. Mọi lựa chọn giữ pending, không nâng thành canon.

## Báo cáo coordinator

```yaml
role: reviewer
task_id: vol-02-ch-04-b04
state: done
segment_ids:
  - YS-LN02/Text/part0022.xhtml/p000063..p000095
files_written:
  - reviews/prose/vol-02/ch-04-b04-claude.md
validator: not_run
diff_check: not_run
findings:
  - {severity: moderate, segment_id: YS-LN02/Text/part0022.xhtml/p000074, issue: "'mình' trong câu hỏi nội tâm bị hiểu là Tanya, đảo đối tượng (người bị đưa đi là họ)", resolution: "vì người gặp chuyện không phải là họ"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0022.xhtml/p000078, issue: "'sĩ quan tùy viên' lệch ledger orderly, đổi cấp; mất 'xe chờ/cầm lái'", resolution: "lính phục vụ; xe có cấp dưới ngồi sau tay lái đã chờ sẵn"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0022.xhtml/p000087, issue: "'kể cả' đổi phạm vi 'mọi người' đang nghỉ nửa ngày", resolution: "gọi mọi người đang nghỉ phép nửa ngày quay về"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0022.xhtml/p000092, issue: "'Ban Tác chiến' lệch ledger; 'đích thân' đặt sai chỗ", resolution: "Cục Tác chiến; đích thân có mặt ở Norden"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0022.xhtml/p000093, issue: "'Hạm đội Bắc Hải' lệch đề xuất b04 'Hạm đội Biển Bắc'", resolution: "Hạm đội Biển Bắc hoặc cập nhật ledger"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0022.xhtml/p000079, issue: "'mình' trong trần thuật ngôi ba, trái DEC-P01-001", resolution: "Nó đã đúng khi không keo kiệt tiền boa"}
review_path: reviews/prose/vol-02/ch-04-b04-claude.md
counts: {serious: 0, moderate: 6, light: 16}
unresolved_findings: 6
term_recommendations:
  - {source_term: "Northern Sea Fleet", proposed_vi: "Hạm đội Biển Bắc", segment_ids: [YS-LN02/Text/part0022.xhtml/p000093], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "orderly", proposed_vi: "lính phục vụ", segment_ids: [YS-LN02/Text/part0022.xhtml/p000078], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "Operations (named staff body)", proposed_vi: "Cục Tác chiến", segment_ids: [YS-LN02/Text/part0022.xhtml/p000092], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "Officer of the Week", proposed_vi: "sĩ quan trực ban tuần", segment_ids: [YS-LN02/Text/part0022.xhtml/p000083], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "Norden", proposed_vi: "Norden", segment_ids: [YS-LN02/Text/part0022.xhtml/p000092], volume: vol-02, chapter: 4, status: pending}
  - {source_term: "aerial mage / Aerial Mage Battalion", proposed_vi: "pháp sư không quân / Tiểu đoàn Pháp sư Không quân", segment_ids: [YS-LN02/Text/part0022.xhtml/p000088, YS-LN02/Text/part0022.xhtml/p000095], volume: vol-02, chapter: 4, status: pending}
risks:
  - "6 lỗi mức vừa chưa xử lý; cần translator sửa rồi re-review hoặc signoff."
  - "Ledger b04 (Biển Bắc) và bản dịch (Bắc Hải) chưa khớp; coordinator cần chọn một dạng trước khi sửa."
  - "M6 (p000079) là lựa chọn giọng có thể chủ ý; độ chắc chắn trung bình."
commit: null
next_action: translator_fix_then_signoff
```
