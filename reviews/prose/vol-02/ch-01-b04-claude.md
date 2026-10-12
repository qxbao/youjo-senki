# Báo cáo phản biện — vol-02-ch-01-b04 (Claude)

- Task: `vol-02-ch-01-b04-review`
- Phạm vi: `YS-LN02/Text/part0010.xhtml/p000060` → `p000087`, **28 đoạn**. Đã đối chiếu đủ 28/28; tập segment_id của bản dịch khớp hoàn toàn với source package (cùng thứ tự).
- Đầu vào đã dùng: handoff b04 (đã commit), source package cục bộ (sha256 `8d17042d…e53fe6b` khớp handoff; `source_sha256` mỗi đoạn `3ac53161…13ae0a` khớp), `canon/`, `work/run-state/pending-terms.yml`, `translations/vol-02/ch-01-b04.jsonl`. Không đọc batch khác, không sửa tệp nào ngoài báo cáo này.
- Metadata JSONL: 28/28 dòng có `glossary_version` (`d5f19d64…f5a41`, khớp `canon/glossary.yml`) và `source_sha256` đúng, `status: draft`, `notes: []`.
- Lưu ý đầu vào: handoff đã commit không nêu danh sách pending của translator; tôi dùng mục `chapter2_b04_translator_terms` trong sổ pending và danh sách thuật ngữ trong lệnh giao việc.
- Mọi chỗ dưới đây dẫn chứng bằng segment_id và mô tả ngắn, không chép câu nguồn. Các đề xuất tiếng Việt chỉ là **đề xuất, không phải canon**.

## Tóm tắt

Bản dịch đọc trôi chảy, giữ tốt giọng mỉa mai của Tanya, phủ định, trình tự (xuất phát → tiếp xúc tuần tra → thấy quân Dacia → ra lệnh → tấn công) và quy mô (ba trong bốn đại đội, ba sư đoàn). **Không có lỗi nghiêm trọng.** Có **7 lỗi vừa**, cần sửa trước khi commit:

1. Cấp bậc của Serebryakov lệch sổ pending (p000060, p000082, p000087).
2. Lời thoại của sĩ quan phụ tá bị dịch bằng đại từ nội tâm "Mình" (p000084).
3. Mất nhấn mạnh của nguồn (p000086).
4. Đại từ trần thuật "nó" cho Tanya, trái sổ pending (p000067, 068, 072, 073).
5. "các cô cậu" suy ra giới tính/tuổi, mâu thuẫn với "Các quý ông" ngay đoạn đó (p000069).
6. "human resources"/"human capital" bị gộp thành hai từ gần đồng nghĩa và không theo sổ (p000075).
7. "aerial mages" bị dịch "không chiến", sai nghĩa và lệch sổ (p000078).

Ngoài ra có 13 lỗi nhẹ. Bốn mục thuật ngữ trong bản dịch không khớp mục `chapter2_b04_translator_terms` của chính translator (xem phần đồng bộ sổ).

## Nhấn mạnh (emphasis parity)

Nguồn có **3** chỗ nhấn mạnh (`<em>`); bản dịch có **2** cặp `*...*`.

| segment_id | Nguồn | Bản dịch | Kết luận |
|---|---|---|---|
| p000067 | cả tiếng hô ngắn "đập cho nhừ tử" | `*Đánh chúng nhừ tử!*` | Khớp phạm vi |
| p000077 | một từ đơn: "chiến tranh" | `*chiến tranh*` | Khớp phạm vi |
| p000086 | cụm số lượng "ba sư đoàn" | không có `*` | **Thiếu** (M3). Bản dịch chỉ dùng "những" để tăng nghĩa, chưa đạt DEC-P01-002 |

25 đoạn còn lại không có nhấn mạnh ở nguồn và không có `*` thừa.

## Phát hiện

### Nghiêm trọng
Không có.

### Vừa

**M1 — p000060, p000082, p000087 — cấp bậc/chủ thể.** Bản dịch gọi Serebryakov là "Trung úy" ở cả ba chỗ (p000087 là "Trung úy Serebryakov"). Sổ `vol02-ch01-b02-lieutenant` đề xuất Serebryakov = "Thiếu úy" (căn cứ cấp bậc nêu rõ ở p000051), Weiss = "Trung úy"; phương án thay thế duy nhất là "Trung úy" cho cả hai nếu không có căn cứ phân biệt. Batch này không có nguồn nêu cấp bậc đầy đủ, nên không có lý do bỏ ánh xạ của sổ; dùng "Trung úy" làm người đọc tưởng đổi cấp hoặc hai nhân vật.
→ Sửa: p000060 "Cảm ơn, Thiếu úy."; p000082 "…, Thiếu úy."; p000087 "Thiếu úy Serebryakov". Nếu coordinator chốt "Trung úy" cho cả hai thì đồng bộ ở mọi đoạn (kể cả p000051–p000058 của batch khác).

**M2 — p000084 — người nói/đại từ.** Đoạn là lời thoại của sĩ quan phụ tá, nhưng bản dịch dùng "Mình". Căn cứ: p000085 là câu đáp của Tanya hỏi lại vì người kia "lo lắng"; p000086 cùng người nói xưng với "Thiếu tá"; p000082 Tanya đã gọi cấp bậc của người này nên người nói p000084 không phải Tanya. "Mình" là đại từ nội tâm tự quy chiếu của Tanya theo DEC-P01-001 (không mở rộng sang chủ thể khác) và lệch giọng thuộc cấp–cấp trên (p000086 dùng "Tôi… ngài").
→ Sửa: "…Tôi đã chuẩn bị tinh thần cho một trận chiến cam go."

**M3 — p000086 — nhấn mạnh.** Xem bảng trên. Nguồn nhấn vào con số ba sư đoàn (đối lập với cách Tanya xem nhẹ ở p000085); bản dịch mất dấu `*`.
→ Sửa: "Ý tôi là, Thiếu tá… có *ba sư đoàn* cơ mà." (hoặc giữ "có những" nhưng bọc `*ba sư đoàn*`). Giữ phạm vi nhấn là cụm số lượng, không mở rộng.

**M4 — p000067 (×2), p000068, p000072, p000073 — đại từ trần thuật về Tanya.** Bản dịch dùng "nó" cho Tanya trong trần thuật LN02. DEC-P01-001 chỉ duyệt "nó" cho giai đoạn pilot LN01 ch001 và cấm tự mở rộng; sổ `vol02-ch01-b01-tanya-narration` và `vol02-ch01-b02-tanya-narration` đề xuất lặp tên Tanya hoặc lược chủ ngữ, "nó" chỉ là phương án thay thế. Cùng đoạn p000061, p000073, p000083 đã dùng tên "Tanya", nên "nó" còn tạo cảm giác chủ thể luân phiên.
→ Sửa: p000067 "Vì thế Tanya nắm chặt tay…" và "ý định của Tanya"; p000068 "…nên Tanya ra lệnh cho họ…"; p000072 "…khiến Tanya vô cùng hài lòng"; p000073 "Chẳng bao lâu sau, Tanya liên lạc được…". Nếu coordinator quyết giữ "nó" cho LN02 thì áp dụng đồng loạt và ghi vào sổ (tôi không đọc b01–b03 nên không xác nhận được các batch ấy dùng gì).

**M5 — p000069 — xưng hô.** "các cô cậu" suy ra tuổi/giới tính của cả tiểu đoàn, trong khi cùng đoạn nguồn gọi thính giả là "quý ông" (bản dịch cũng dịch "Các quý ông") nên hai cách gọi mâu thuẫn. Vi phạm DEC-P01-001 (không suy giới tính/quan hệ khi thiếu căn cứ); không có mục sổ nào cho "cô cậu".
→ Sửa trung tính: "Tôi không nghĩ ai trong số mọi người ngu đến mức để bị bắn hạ…" (khớp "mọi người" ở p000060, p000066).

**M6 — p000075 — human resources / human capital.** Nguồn dùng hai từ khác nhau trong hai câu liền nhau (câu thứ nhất là "tài nguyên" bị lãng phí, câu thứ hai là "vốn" đáng lẽ sinh lời). Bản dịch dịch "nhân lực" và "nguồn nhân lực", gần như đồng nghĩa nên mất khác biệt; lại ngược sổ: sổ b04 đề xuất human resources = "nguồn nhân lực", human capital = "vốn con người" (P03-human-capital). Bản dịch thực tế đã đưa "nguồn nhân lực" vào chỗ của human capital.
→ Xem khuyến nghị thuật ngữ T4/T5. Sửa câu cuối: "Có vốn con người dồi dào đến thế mà hoàn toàn không biết tận dụng."; câu trước giữ "núi nhân lực".

**M7 — p000078 — aerial mages.** Bản dịch dùng "pháp sư không chiến". "Không chiến" nghĩa là chiến đấu trên không (giao tranh phi cơ), trong khi đoạn nói rõ các pháp sư này đối đầu lực lượng **mặt đất**; đồng thời lệch mục sổ b04 ("pháp sư không quân") và mục vol-01 `b06-aerial-mage`. Xem T3.
→ Sửa: "pháp sư không quân".

### Nhẹ

| # | segment_id | Vấn đề và căn cứ | Đề xuất |
|---|---|---|---|
| m1 | p000065 | "thảm sát một chiều" thêm sắc thái hành vi tàn bạo/đạo đức hơn thành ngữ gốc (bắn hạ dễ dàng, không phản kháng) và lặp ý với "tàn sát" ngay câu trước; "thoải mái tàn sát" biến trạng thái "không bị cản trở" thành thái độ. Không khớp mục sổ (`cuộc bắn áp đảo`). Xem T1 | "…khi chúng ta tàn sát họ từ trên trời mà không bị cản trở. Đây sẽ còn là một cuộc bắn gà tây lớn hơn cả ở quần đảo Mariana." |
| m2 | p000070 | "săn lùng" gợi truy bắt kẻ chạy trốn; nguồn nhấn "đúng nghĩa đen" và ngay sau là "môn thể thao" nên nghĩa là săn người như trò chơi. Xem T2 | "đây đúng là cuộc săn người" |
| m3 | p000071 | "khiến… cũng phải lu mờ" nói câu chuyện át cả Don Quixote; nguồn chỉ nói đủ sức sánh ngang/không kém cạnh | "một câu chuyện đủ sức sánh ngang hiệp sĩ huyền thoại Don Quixote" |
| m4 | p000069 | "sẽ bắn trả" bỏ mất mức chắc chắn "lẽ ra phải"; "tiếp tục diễn tập" bỏ nghĩa **bắt đầu lại**; "trò chơi bắt đầu" là lời tuyên bố chứ nguồn là lời mời/lệnh cho bắt đầu | "đáng lẽ sẽ bắn trả… trên lý thuyết"; "ta bắt đầu lại buổi diễn tập"; "Các quý ông, bắt đầu trò chơi nào." |
| m5 | p000068 | "nghiền nát nghĩa đen" câu cú sai; nghĩa là "theo đúng nghĩa đen" | "nghiền nát đội tiên phong quân Dacia theo đúng nghĩa đen" |
| m6 | p000072 | (a) "trở thành đơn vị ứng phó nhanh nhất" biến "xuất phát với tư cách" thành thành tích đạt được; (b) "nhân viên hậu phương" gợi nhân viên dân sự, lệch mục sổ `command-personnel` (nhân sự); (c) "đến thăm trấn giữ" khó tách vai hai vế | (a) "lên đường với tư cách đơn vị ứng phó nhanh nhất"; (b) "nhân sự tuyến sau"; (c) "…từ Bộ Tổng tham mưu đang thăm đơn vị, trấn giữ cứ điểm" |
| m7 | p000073 | "càng thêm tin chắc" thêm so sánh (đã tin từ trước) không có ở nguồn | "Tanya tin chắc" |
| m8 | p000076 | "đám thanh niên" thêm khinh miệt; "ngu xuẩn" mạnh hơn "foolish"; mất liên từ nhân quả "vậy nên" (nhiệm vụ của quân đội → chia buồn để chính phủ Dacia lo) | "những thanh niên này"; "ngu ngốc"; "Vậy nên chuyện chia buồn… xin để chính phủ ngu ngốc của Công quốc Dacia lo liệu" |
| m9 | p000078 | "dự bị" không có ở nguồn (chỉ "còn thừa"; "backup" chỉ xuất hiện ở p000081); "dễ đoán" lệch nghĩa so với "hiển nhiên đến mức giáo khoa" | "còn lại một đại đội"; "cực kỳ hiển nhiên" |
| m10 | p000079 | "mọi người" mở rộng người nghe từ các đại đội trưởng ra cả tiểu đoàn; mất "cho tôi thấy" | "Các đại đội trưởng, tôi trông đợi các anh tuân theo mệnh lệnh và cho tôi thấy kết quả tốt!" hoặc lặp "các đại đội trưởng" |
| m11 | p000081 | "không bắn nổi" đổi "không thu hút hỏa lực" thành không đủ khả năng; "giáng tai họa" mất "tàn phá"; "toàn bộ binh lính" biến "chỉ còn biết" thành định lượng | "đến nỗi chẳng thu hút nổi phát phòng không nào"; "tàn phá chúng từ trên trời"; "bọn lính mặt đất của địch dường như chỉ còn biết hoảng loạn" |
| m12 | p000085 | "Cô" suy giới tính/tuổi người nghe, trái DEC-P01-001 (sổ b03 cũng chỉ liệt "cô" làm phương án thay thế); "hành quân" thu hẹp "xông bừa/hoành hành" | "Thiếu úy lo lắng trước…"; "một cuộc tấn công liều lĩnh, nửa vời" |
| m13 | p000061 | "nụ cười rạng rỡ niềm vui thuần khiết" lủng củng; lặp tên Tanya hai lần trong một câu | "nụ cười thuần khiết niềm vui… gần như hát lên cho mọi người nghe mình vui đến thế nào" (hoặc lược chủ ngữ) |

### Kiểm tra đã đạt (không có lỗi)
- **Phủ định và logic:** p000065 (không có cơ hội), p000069 (chưa nhận xác nhận; không nghĩ ai ngu đến mức), p000081 (không thấy cần/giữ lại làm dự phòng; không bị bắn phòng không), p000083 (không phải hiếu chiến/nghiện việc nhưng lo bị đánh giá), p000086–087 giữ đúng.
- **Chronology:** thứ tự p000072 (để lại hậu cứ → dẫn đi) → p000073 (tiếp xúc tuần tra) → p000074 (thấy khối người) → p000077 (ra lệnh) → p000078–081 (tấn công) đúng. "Hai tháng kể từ khi thành lập tiểu đoàn" (p000083) giữ đúng mốc. Quy mô "ba trong bốn đại đội / còn một" (p000078) và "ba sư đoàn" đúng.
- **Chủ thể:** p000060 và p000082 là lời Tanya nói với sĩ quan phụ tá; p000084 và p000086 là lời sĩ quan phụ tá (lỗi chỉ ở đại từ p000084, xem M2); p000085 là lời Tanya. Các đoạn nội tâm (p000063, 065, 070, 071, 074–076, 078, 081, 083, 087) dùng "mình" nhất quán theo DEC-P01-001.
- **Thuật ngữ quân sự khác:** tiểu đoàn/đại đội/sư đoàn, Công quốc Dacia, Quân đội Đế quốc, đơn vị tuần tra biên giới khớp sổ. "Bộ Tổng tham mưu" (viết thường "tham") khớp mục LN02 b02, nhưng khác cách viết hoa ở các mục vol-01 ("Bộ Tổng Tham mưu"); chỉ là vấn đề đồng bộ chính tả, coordinator quyết khi gộp sổ.

## Khuyến nghị thuật ngữ (đề xuất tạm, không canon)

| # | source_term | Lựa chọn tạm tốt nhất | Lý do | Phương án thay thế | segment_id | Độ tin cậy |
|---|---|---|---|---|---|---|
| T1 | turkey shoot | **cuộc bắn gà tây** (kèm "ở quần đảo Mariana" như bản dịch) | Nguồn dùng thành ngữ và nêu ngay tên địa danh Mariana, tức quy chiếu đến một sự kiện cụ thể mang tên này; giữ hình ảnh gốc là phương án literal ít suy diễn nhất, đồng thời tránh sắc thái thảm sát/đạo đức của "cuộc thảm sát". Tôi chưa kiểm chứng nguồn ngoài để biết tiếng Việt có dùng cách gọi này không; nếu coordinator muốn bản đọc không phụ thuộc kiến thức nền thì dùng phương án thay thế trung tính | "cuộc bắn hạ một chiều" (trung tính, không giữ hình ảnh); "cuộc tàn sát một chiều" (ý nghĩa gần, nhưng lặp với "tàn sát" cùng đoạn); loại "cuộc thảm sát một chiều" (bản dịch hiện tại), cũng ngược sổ "cuộc bắn áp đảo" | p000065 | 0.45 |
| T2 | manhunt | **cuộc săn người** | Nguồn tự nhấn "đúng nghĩa đen" và nối với "môn thể thao", tức nghĩa là săn con người như thú vui; "săn người" là cách nói tự nhiên, ngắn, đủ literal. "Truy lùng" mang nghĩa truy bắt, mất sắc thái thể thao nên không chọn | "cuộc săn lùng con người" (bản dịch/sổ hiện tại, chấp nhận được); "cuộc truy lùng" (không khuyến nghị) | p000070 | 0.6 |
| T3 | aerial mages | **pháp sư không quân** | Khớp mục sổ vol-01 (`b06-aerial-mage`, mục kế thừa `aerial mage`) và mục b04; ưu tiên nhất quán vì chưa có căn cứ mới để đổi. "Không chiến" bị loại (sai nghĩa: xem M7). Rủi ro: gợi một binh chủng không quân, có thể lẫn với "Hạm đội Không quân 7" (sổ b02) dù đoạn này nói rõ họ thuộc Quân đội Đế quốc. Nếu coordinator muốn tránh hàm ý binh chủng thì chọn "trên không" cho toàn bộ | "pháp sư trên không" (trung tính, literal); loại "pháp sư không chiến" | p000078 | 0.65 |
| T4 | human resources | **nhân lực** (cụm "núi nhân lực bị lãng phí") | Cách nói tự nhiên với "núi", giữ nghĩa tài nguyên/lực lượng bị hoang phí, và khác rõ với "vốn con người" ở câu sau. Sổ b04 nêu "nguồn nhân lực" là chính, "nhân lực" là phương án thay thế; tôi đề xuất đảo vì "núi nguồn nhân lực" nặng nề. Nếu coordinator muốn theo đúng sổ thì dùng "nguồn nhân lực" ở đây và khi đó **bắt buộc** đổi capital sang "vốn con người" | "nguồn nhân lực" (sổ hiện tại); "sức người" | p000075 | 0.55 |
| T5 | human capital | **vốn con người** | Khớp P03-human-capital (glossary-pending, vol-01 giọng kinh tế học của Tanya); nguồn dùng hai từ khác nhau liền kề nên cần hai từ Việt khác nhau, và "vốn" khớp ý "không biết đưa vào sử dụng hiệu quả". Dùng "nguồn nhân lực" cho cả hai là mất khác biệt | "vốn nhân lực" (thuật ngữ kinh tế phổ biến, đồng nghĩa); "nguồn nhân lực" (loại, trùng T4) | p000075 | 0.7 |
| T6 | Aconitum 01 | **giữ nguyên "Aconitum 01"** | Là hô hiệu vô tuyến mở đầu thông báo cho toàn đơn vị (p000077), dạng chữ Latinh + số thứ tự; dịch tên cây sẽ biến hô hiệu thành từ thường và có nguy cơ mất tính định danh. Bản dịch hiện tại đã đúng. Trong phạm vi batch chỉ có một lần xuất hiện nên không đủ để kết luận "01" là gì (ví dụ chỉ cá nhân hay đơn vị); không suy diễn | không có phương án nào tốt hơn (dịch nghĩa bị loại) | p000077 | 0.8 |

Đồng bộ sổ (cho coordinator): bản dịch hiện tại lệch mục `chapter2_b04_translator_terms` ở T1 (sổ: "cuộc bắn áp đảo"; bản dịch: "cuộc thảm sát một chiều"), T3 (sổ: "pháp sư không quân"; bản dịch: "không chiến"), T4 (sổ: "nguồn nhân lực"; bản dịch: "nhân lực"), T5 (sổ: "vốn con người"; bản dịch: "nguồn nhân lực"). T2 và T6 khớp sổ. Các mục quân hàm/đại từ trần thuật (M1, M4) cũng đã có sẵn trong sổ b01–b02 và chỉ cần áp dụng.

Mục mới nên ghi vào sổ (đề xuất): `vol02-ch01-b04-address-to-unit` (cách gọi cả tiểu đoàn: "mọi người", tránh "cô cậu", p000069/p000079); `vol02-ch01-b04-serebryakov-address` (xưng hô Tanya ↔ phụ tá: cấp bậc lặp, tránh "Cô", p000060/p000082/p000085/p000087). Cả hai chưa phải canon.

## Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-01-b04-review
state: done
segment_ids: [YS-LN02/Text/part0010.xhtml/p000060 .. YS-LN02/Text/part0010.xhtml/p000087]  # 28 đoạn
files_written: [reviews/prose/vol-02/ch-01-b04-claude.md]
validator: not_run
diff_check: not_run
review_path: reviews/prose/vol-02/ch-01-b04-claude.md
counts: {serious: 0, moderate: 7, minor: 13}
findings:
  - {severity: moderate, segment_id: p000060/p000082/p000087, issue: cấp bậc Serebryakov lệch sổ, resolution: Thiếu úy}
  - {severity: moderate, segment_id: p000084, issue: lời thoại phụ tá dùng đại từ nội tâm "Mình", resolution: "Tôi"}
  - {severity: moderate, segment_id: p000086, issue: mất nhấn mạnh "ba sư đoàn", resolution: thêm *...*}
  - {severity: moderate, segment_id: p000067/p000068/p000072/p000073, issue: "nó" cho Tanya trái sổ, resolution: lặp tên/lược chủ ngữ}
  - {severity: moderate, segment_id: p000069, issue: "các cô cậu" suy giới tính/mâu thuẫn "quý ông", resolution: "mọi người"}
  - {severity: moderate, segment_id: p000075, issue: human resources/capital gộp, lệch sổ, resolution: nhân lực / vốn con người}
  - {severity: moderate, segment_id: p000078, issue: "không chiến" sai nghĩa, lệch sổ, resolution: pháp sư không quân}
  - {severity: minor, segment_id: "p000061,065,068,069,070,071,072,073,076,078,079,081,085", issue: xem bảng nhẹ m1–m13, resolution: xem bảng}
unresolved_findings: 20   # 7 vừa + 13 nhẹ, chờ translator sửa
term_recommendations:
  - {source_term: turkey shoot, proposed_vi: cuộc bắn gà tây, alternatives_vi: [cuộc bắn hạ một chiều, cuộc tàn sát một chiều], segment_ids: [p000065], status: pending, confidence: 0.45}
  - {source_term: manhunt, proposed_vi: cuộc săn người, alternatives_vi: [cuộc săn lùng con người, cuộc truy lùng], segment_ids: [p000070], status: pending, confidence: 0.6}
  - {source_term: aerial mages, proposed_vi: pháp sư không quân, alternatives_vi: [pháp sư trên không], segment_ids: [p000078], status: pending, confidence: 0.65}
  - {source_term: human resources, proposed_vi: nhân lực, alternatives_vi: [nguồn nhân lực, sức người], segment_ids: [p000075], status: pending, confidence: 0.55}
  - {source_term: human capital, proposed_vi: vốn con người, alternatives_vi: [vốn nhân lực], segment_ids: [p000075], status: pending, confidence: 0.7}
  - {source_term: Aconitum 01, proposed_vi: giữ nguyên Aconitum 01, alternatives_vi: [], segment_ids: [p000077], status: pending, confidence: 0.8}
pending_terms: []   # thuật ngữ mới ngoài danh sách trên: không có; hai mục xưng hô nêu ở phần đồng bộ sổ
risks: [meaning, new_pending_terms, emphasis]   # validator_warning: không có thông tin (not_run)
commit: null
next_action: translator_fix_moderate_then_followup_review   # coordinator ghi lựa chọn tạm vào ledger/handoff; không có hard stop
```
