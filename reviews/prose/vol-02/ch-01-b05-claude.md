# Báo cáo phản biện — vol-02-ch-01-b05 (Claude)

- Task: `vol-02-ch-01-b05-review`
- Phạm vi: `YS-LN02/Text/part0010.xhtml/p000088` → `p000118`, **31 đoạn**. Đã đối chiếu đủ 31/31; tập và thứ tự segment_id của bản dịch khớp hoàn toàn với source package.
- Đầu vào đã dùng: handoff b05 (đã commit, kể cả `review_coordination.provisional_choices`), source package cục bộ (sha256 `3debb214…c61e` khớp handoff; `source_sha256` mỗi đoạn `3ac53161…13ae0a` khớp), `canon/` (chỉ `glossary-pending.yml`, `decisions.md`, `style-guide.md` có nội dung; `glossary.yml` và `characters.yml` rỗng), `work/run-state/pending-terms.yml` (các mục `vol02-ch01-b01…b05` và `chapter2_b04_translator_terms`), `translations/vol-02/ch-01-b05.jsonl`. Không đọc batch khác, không sửa tệp nào ngoài báo cáo này.
- Metadata JSONL: 31/31 dòng có `glossary_version` `d5f19d64…f5a41` (khớp `canon/glossary.yml`), `source_sha256` đúng, `status: draft`, `notes: []`. Số từ nguồn tính lại bằng đúng regex của handoff = 883, khớp.
- Mọi chỗ dưới đây dẫn chứng bằng segment_id và mô tả ngắn, không chép câu nguồn. Các phương án tiếng Việt chỉ là **đề xuất tạm, không phải canon**.
- Giới hạn: tôi không đọc b01–b04 nên không kiểm được các batch ấy thực tế đã dùng gì; chỗ nào phụ thuộc điều đó được ghi rõ.

## Tóm tắt

Bản dịch đọc trôi chảy, giữ tốt giọng mỉa mai, phủ định, trình tự chiến đấu (bổ nhào → thả lựu đạn nổ trên không → hỗn loạn → địch xếp đội hình vuông) và logic "họ không biết chiến tranh là gì". **Không có lỗi nghiêm trọng.** Có **6 lỗi vừa**, nên sửa trước khi commit:

1. Cấp bậc của Serebryakov lệch sổ pending (p000089, p000092, p000118).
2. Mất nhấn mạnh của nguồn ở p000092.
3. Đại từ trần thuật "cô" cho Tanya (p000095), trái sổ b01/b02.
4. "sĩ quan tùy viên" thay vì "sĩ quan phụ tá" của sổ (p000088, p000115).
5. Đảo góc nhìn của câu so sánh đánh nhau tay không (p000109).
6. Tự quy chiếu nội tâm lúc "mình", lúc "tôi" trong cùng một mạch (p000088, p000105, p000110, p000115).

Cộng thêm 15 lỗi nhẹ. Bốn thuật ngữ pending được chọn ở phần `term_recommendations`: giữ ba (post-structuralist, anti-surface grenade, infantry square), **đổi một** (formula-fixed).

## Số lượng theo mức

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 6 |
| Nhẹ | 15 |

## Nhấn mạnh (emphasis parity, DEC-P01-002)

Nguồn có **1** chỗ nhấn mạnh (`<em>`); bản dịch có **0** cặp `*...*`.

| segment_id | Nguồn | Bản dịch | Kết luận |
|---|---|---|---|
| p000092 | nhấn cả một vế dài: nửa sau của câu thứ hai, từ phần khen sự chuẩn bị tinh thần của họ đến phần Tanya nhận lỗi vì gọi địch là "sư đoàn" | không có `*` | **Thiếu** (M2) |

30 đoạn còn lại không có nhấn mạnh ở nguồn và không có `*` thừa.

## Phát hiện

### Nghiêm trọng
Không có.

### Vừa

**M1 — p000089, p000092, p000118 — cấp bậc/chủ thể.** Bản dịch gọi Serebryakov là "Trung úy" ở p000089, p000092 và p000118. Sổ `vol02-ch01-b02-lieutenant` (và `vol02-ch01-b04-serebryakov-address`) đề xuất Serebryakov = "Thiếu úy" theo cấp bậc nêu rõ ở p000051, Weiss = "Trung úy"; phương án thay thế duy nhất là "Trung úy" cho cả hai nếu không có căn cứ phân biệt. Batch này không có căn cứ mới để bỏ ánh xạ của sổ; dùng "Trung úy" khiến người đọc tưởng đổi cấp hoặc hai nhân vật.
→ Sửa: p000089 "Thiếu úy Serebryakov", p000092 "Thiếu úy Serebryakov", p000118 "Thiếu úy Serebryakov". Nếu coordinator chốt "Trung úy" cho cả hai thì đồng bộ ở mọi batch.

**M2 — p000092 — nhấn mạnh.** Xem bảng trên. Phạm vi nhấn là cả vế "họ chuẩn bị tinh thần … đáng khen; nhưng chính tôi đã sai khi gọi … là sư đoàn", không phải một từ. Bản dịch còn thêm "chính" ("chính tôi đã sai") như một cách nhấn thay thế không có dấu `*`, nên mất dấu cấu trúc theo DEC-P01-002.
→ Sửa: bọc nguyên vế đó bằng `*...*` (từ "Họ có thể chuẩn bị tinh thần…" đến "…là “sư đoàn”.") và bỏ "chính" thừa, hoặc giữ "chính" nhưng vẫn bọc `*`. Không mở rộng nhấn sang câu đầu hay câu cuối đoạn.

**M3 — p000095 (×2) — đại từ trần thuật về Tanya.** Bản dịch dùng "cô" ("Bởi thế cô mới tự hỏi…", "khiến cô thấy hơi buồn cười"). Sổ `vol02-ch01-b01-tanya-narration` và `b02-tanya-narration` đề xuất lặp tên "Tanya" hoặc lược chủ ngữ; "nó" và "cô" chỉ là phương án thay thế vì "cô" mang giới tính/giai đoạn cụ thể (DEC-P01-001 không cho mở rộng). Chính batch này đã dùng "Tanya" ở p000092, p000112, nên "cô" tạo cảm giác chủ thể luân phiên.
→ Sửa: "Bởi thế Tanya mới tự hỏi…" và "…bắt đầu khiến Tanya thấy hơi buồn cười." (hoặc lược chủ ngữ ở vế sau).

**M4 — p000088, p000115 — thuật ngữ chức danh.** Bản dịch dùng "sĩ quan tùy viên" cho "adjutant". Sổ `vol02-ch01-b03-adjutant` ghi "sĩ quan phụ tá" (thay thế: trợ tá, sĩ quan tùy tùng). "Tùy viên" trong tiếng Việt quân sự thường gợi attaché (tùy viên quân sự), lệch nghĩa với người phụ tá chỉ huy trực tiếp. Không có mục sổ nào cho "tùy viên".
→ Sửa: "sĩ quan phụ tá" ở cả hai chỗ. (Nếu b04 đã dùng một dạng khác, đồng bộ theo sổ; tôi không đọc b04.)

**M5 — p000109 — góc nhìn/chủ thể.** Nguồn nói về người *ra đòn*: đấm ai thì phải đoán trước bị đáp trả. Bản dịch viết "bị đấm cũng phải biết đấm trả", chuyển sang nghĩa vụ của người *bị đánh*. Hai câu khác nhau về chủ thể và hàm ý, và câu gốc mới khớp mạch p000107 (Dacia đánh mà tưởng không bị đánh lại).
→ Sửa: "Đánh nhau tay không thì đấm người ta cũng phải lường trước bị đấm trả." (hoặc tương đương, giữ chủ thể là kẻ ra đòn).

**M6 — p000088, p000105, p000110, p000115 — tự quy chiếu nội tâm.** p000088 dùng "mình" (ba lần); p000105, p000110, p000115 cũng là độc thoại nội tâm của Tanya nhưng dùng "tôi" ("tôi suýt tự hỏi", "người khổ sở nhất chính là tôi", "sĩ quan … của tôi"). Sổ `vol02-ch01-b01-interior-self-reference` đề xuất "mình" (0.8), thay thế "tôi"; DEC-P01-001 áp dụng "mình" cho nội tâm tự quy chiếu. Đoạn p000093–p000099, p000118 là tường thuật hành động ngôi thứ nhất với "chúng tôi", khác bình diện, nên "tôi/chúng tôi" ở đó chấp nhận được.
→ Đề xuất tạm (không canon): các đoạn tư duy một chủ thể (p000088, p000105, p000110, p000115) dùng "mình" nhất quán, ví dụ p000110 "Mình bị kẹt trong cuộc chiến…, rõ ràng người khổ sở nhất chính là mình"; "chúng tôi" giữ cho hành động tập thể. Phương án thay thế: "tôi" cho toàn bộ, sửa p000088 (ba chỗ). Độ bất định: nếu b01–b04 đã đi theo hướng "tôi" cho tường thuật nội tâm dài thì chọn thay thế để đồng bộ; không dừng pipeline vì chuyện này.

### Nhẹ

- **L1 — p000088:** "phân tích giải cấu trúc" thừa "phân tích" (giải cấu trúc đã là hành động); và "đúng là đã xem nhẹ" đánh rơi ý "mình sai khi…" của vế đầu (nguồn nêu rõ là lỗi, có chút e dè). Gợi ý: "Hình như lỗi của mình là đã xem nhẹ một người theo chủ nghĩa hậu cấu trúc… Mình phải giải cấu trúc chuyện này và sửa sai."
- **L2 — p000091:** "đám đông" yếu hơn "mob" (gợi tập hợp ô hợp, thiếu tổ chức). Gợi ý "đám ô hợp năm vạn người". "năm vạn" có sắc thái Hán Việt; kiểm tra đồng bộ với cách ghi số lượng ở batch trước.
- **L3 — p000097:** "bia ghim" không phải hình ảnh tiếng Việt có sẵn; nguồn là ví von đầu bị cắm đầy mảnh như gối cắm kim. Gợi ý "đầu chúng bị ghim đầy mảnh như cái gối cắm kim".
- **L4 — p000097:** "đồng loạt" thêm ý đồng thời không có ở nguồn (chỉ nói khai hỏa hết công suất sau khi chuẩn bị và chọn vị trí). Bỏ "đồng loạt".
- **L5 — p000097:** "gắn thuật thức" đánh rơi nghĩa "fixed" và thêm nghĩa "gắn vào". Xử lý theo T2.
- **L6 — p000098:** "quét sạch" vượt nghĩa "blow away" (đánh bật/thổi bay), và mâu thuẫn ngay câu sau (binh lính vẫn chạy tán loạn, có bắn trả). Gợi ý "đánh tan/thổi bay".
- **L7 — p000099 so với p000112:** cùng thuật ngữ anti-air nhưng bản dịch dịch "chống máy bay" (p000099) và "phòng không" (p000112). Thống nhất "phòng không" (kể cả "chiến thuật phòng không sơ sài").
- **L8 — p000105:** mất "almost" của "fought almost too passionately": "hăng máu quá mức" khẳng định hơn nguồn. Gợi ý "hăng máu đến mức gần như quá đà".
- **L9 — p000106:** "chính họ cũng tuyên chiến" thêm "cũng" (ngầm so sánh với bên khác) không có ở nguồn; nguồn nhấn họ là bên tuyên chiến. Gợi ý "chính họ là bên tuyên chiến".
- **L10 — p000109:** "thể diện" (face) lệch với "dignity"; gợi ý "tư cách/phẩm cách tối thiểu". "Friedrich Đại đế" là dạng tên mới, không có trong sổ; chấp nhận, nên ghi vào sổ (T8).
- **L11 — p000110:** "bình thường đến mức nhàm chán" thêm "nhàm chán" không có ở nguồn (ultra-ordinary chỉ là cực kỳ bình thường). Gợi ý "cực kỳ bình thường". "tên Being X độc ác": "tên" thêm sắc thái khinh miệt nhẹ; chấp nhận theo giọng Tanya nhưng có thể bỏ.
- **L12 — p000115:** mất "actually" (nghịch với nhận định của người phụ tá): thiếu "thực ra" trước "mấy người trông giống sĩ quan … đang ra lệnh".
- **L13 — p000118:** "các đợt không kích ma pháp" đổi "ground attack" thành "air strike" và thêm số nhiều "đợt". Gợi ý "các đợt tấn công mặt đất bằng ma pháp" (khớp "mặt đất" ở p000097/p000098).
- **L14 — p000090, p000101:** "thiếu tá" viết thường làm xưng hô trực tiếp, trong khi "Trung úy Serebryakov" viết hoa; sổ ghi "Thiếu tá". Thống nhất viết hoa khi dùng làm lời gọi. p000090: "Dạ" là tiếng đáp, trong khi nguồn là tiếng ngập ngừng ("Er"); gợi ý "Ơ… thưa Thiếu tá?".
- **L15 — p000089:** "cô" gọi Serebryakov suy ra giới tính chỉ từ trước đó ("her" ở p000088). Có căn cứ trong batch nên chấp nhận được, nhưng lời gọi theo sổ b04 là "Thiếu úy"; gợi ý "Có vẻ Thiếu úy nói đúng."

## Kiểm tra các hạng mục khác (không phát hiện lỗi)

- **Nghĩa/phủ định/thời gian:** p000092 (khen sự chuẩn bị nhưng nhận lỗi gọi "sư đoàn"), p000095 (chuỗi mục tiêu: chặt đầu → thổi bay tàn quân), p000104 (tưởng mình bị tấn công, nhưng…), p000105–p000106 (Entente vượt biên không định đánh vs Công quốc tuyên chiến nhưng không biết chiến tranh) đều giữ đúng. "Công quốc" khớp `vol02-ch01-b02-principality`; "Dacia" khớp `b03-dacia-country`.
- **Chủ thể lời thoại:** p000094–p000117 phân vai hợp lý (Tanya ra lệnh, các đại đội trưởng báo cáo, Serebryakov ngạc nhiên ở p000117); không có đảo người nói.
- **Quân sự:** "đội hình vuông" ở p000113 (dạng số nhiều chung) khớp p000116/p000118; "bổ nhào", "khai hỏa", "lớp vỏ phòng ngự", "xung phong kỵ binh" đều hợp ngữ cảnh.
- **Pending chưa có trong sổ cần thêm:** "Command Company" → "Đại đội chỉ huy" (p000094) và "Friedrich Đại đế" (p000109); xem T6, T8.

## term_recommendations

Mọi mục là đề xuất tạm, status `pending`, không tự nâng thành canon.

### T1 — post-structuralist (p000088)
- **Chọn:** giữ "người theo chủ nghĩa hậu cấu trúc". Độ chắc 0.65.
- **Căn cứ:** nguồn dùng như danh từ chỉ người ("a post-structuralist") để đùa Serebryakov bắt bẻ từ ngữ; "người theo chủ nghĩa …" là dạng danh từ chỉ người quen thuộc, trang trọng đủ cho giọng tự trào của Tanya, và đi cặp tự nhiên với "giải cấu trúc" (deconstruct) cùng đoạn. Đây là sự pha trộn thuật ngữ triết học vào độc thoại, không liên quan cốt truyện.
- **Thay thế:** "nhà hậu cấu trúc luận" (hơi học thuật nặng), "một tay hậu cấu trúc" (khẩu ngữ, thêm sắc thái miệt thị không có ở nguồn).
- **Bất định:** không rõ tác giả có chủ ý phê phán trường phái hay chỉ dùng như nhãn hài hước; không dịch mở rộng. Không suy ra giới tính từ danh từ này.

### T2 — formula-fixed (p000097) — ĐỔI
- **Chọn:** "đã cố định thuật thức", ví dụ "lựu đạn chống mục tiêu mặt đất đã cố định thuật thức". Độ chắc 0.5.
- **Căn cứ:** "formula" khớp "thuật thức" của sổ (`P01-formulas`) và của chính p000097 ("chuẩn bị thuật thức"); "fixed" nên dịch sát là "cố định". Đối lập hợp lý: lựu đạn có thuật thức đã cố định, còn đại đội "chuẩn bị thuật thức" ngay trên không. "gắn" là bản dịch thoát ý, thêm hình ảnh "gắn vào" không có ở nguồn nên không chọn; "sẵn" cũng không thêm vì suy ra thời điểm.
- **Thay thế (theo thứ tự):** "thuật thức cố định" làm tính từ ghép ("lựu đạn thuật thức cố định chống mục tiêu mặt đất"), "gắn sẵn thuật thức" (suy diễn thời điểm), "cố định công thức" (dùng "công thức" thay thuật thức, lệch sổ).
- **Bất định:** cách dùng quân sự không rõ: có thể là thuật thức đã được viết sẵn vào quả lựu đạn, hoặc quả lựu đạn có thuật thức không thay đổi trên đường bay. Không đủ căn cứ để chọn nghĩa thứ nhất nên dùng cách diễn đạt trung tính.

### T3 — anti-surface grenade (p000097)
- **Chọn:** giữ "lựu đạn chống mục tiêu mặt đất". Độ chắc 0.6.
- **Căn cứ:** nguồn nói "surface", không nói người/lực lượng. Dù p000098 cho thấy mục tiêu thực tế là bộ binh, "lực lượng mặt đất" thu hẹp nghĩa ra ngoài nguồn. "mục tiêu mặt đất" còn khớp "mặt đất" ở p000098 và p000118 (L13).
- **Thay thế:** "lựu đạn chống lực lượng mặt đất" (thu hẹp theo ngữ cảnh), "lựu đạn đối đất" (ngắn, nhưng hơi lạ).
- **Bất định:** chưa biết nguyên tác muốn nhấn mạnh đối đất hay chống sát thương. Thống nhất phần anti-air bằng "phòng không" (L7) để cặp đối lập khớp.

### T4 — infantry square (p000116, p000118)
- **Chọn:** giữ "đội hình vuông bộ binh". Độ chắc 0.65.
- **Căn cứ:** p000117 ("thời đại kỵ binh qua rồi") và p000118 cho thấy đây là đội hình chống kỵ binh; "đội hình vuông" là cách gọi tự nhiên, dễ hiểu, và "bộ binh" giữ danh từ của nguồn. p000113 đã dùng "đội hình vuông" ở dạng chung nên cách gọi nhất quán trong batch.
- **Thay thế:** "đội hình ô vuông của bộ binh" (đọc như lưới ô), "khối vuông bộ binh" (hơi sách vở).
- **Bất định:** thấp. Không thêm chú giải trong bản dịch (không có chú thích nguồn). Nếu về sau Tanya nói rõ hướng mặt/rỗng ruột thì mới xét lại.

### Các mục khác nên ghi vào sổ
- **T5 — adjutant:** dùng "sĩ quan phụ tá" theo `vol02-ch01-b03-adjutant` (M4).
- **T6 — Command Company (p000094):** giữ "Đại đội chỉ huy" (sát chữ, 0.5); thay thế "đại đội bộ chỉ huy". Chưa rõ đây có phải tên đơn vị chính thức hay chỉ mô tả; tránh dùng "Bộ chỉ huy" của `b01-command-hq` vì khác đối tượng.
- **T7 — Serebryakov rank / Tanya narration / interior self-reference:** theo M1, M3, M6; chờ coordinator chốt ledger.
- **T8 — Friedrich Đại đế (p000109):** chấp nhận cách phiên theo Phổ; đề xuất ghi sổ (0.7). Thay thế "Frederick Đại đế".

## Rủi ro

- **R1:** M1/M3/M4/M6 phụ thuộc cách b01–b04 đã áp dụng sổ; tôi không đọc các batch đó nên đồng bộ chéo cần coordinator rà. Nếu b04 dùng "Trung úy"/"nó"/"tùy viên" thì phải xử lý theo quyền sửa riêng, không để lệch trong cùng chương.
- **R2:** T2 (formula-fixed) độ chắc thấp (0.5). Nếu các batch sau mô tả lại cơ chế lựu đạn, cần xem lại; lúc đó chỉ sửa p000097 và các lần nhắc lại.
- **R3:** L6 ("quét sạch") và L13 ("không kích") thay đổi nhẹ mức độ/trường tác chiến; nếu coordinator giữ nguyên thì cần ghi rõ lựa chọn chủ ý.
- **R4:** Không có quyết định ảnh hưởng cốt truyện; không cần hỏi người dùng. Tất cả vẫn là đề xuất, không tự nâng canon.

## next_action

Coordinator giao cho translator (người đang giữ quyền sửa `translations/vol-02/ch-01-b05.jsonl`) sửa 6 lỗi vừa M1–M6 và xem xét các lỗi nhẹ L1–L15, áp dụng T1–T4 như trên, ghi các mục T5–T8 vào ledger. Sau đó chạy validator/diff-check, rồi một vòng signoff ngắn chỉ cho các đoạn đã sửa (p000088, p000089, p000090, p000092, p000095, p000097, p000098, p000105, p000109, p000110, p000115, p000118) trước khi commit.

## YAML báo cáo

```yaml
role: reviewer
task_id: vol-02-ch-01-b05
state: done
segment_ids:
  - YS-LN02/Text/part0010.xhtml/p000088
  - YS-LN02/Text/part0010.xhtml/p000089
  - YS-LN02/Text/part0010.xhtml/p000090
  - YS-LN02/Text/part0010.xhtml/p000091
  - YS-LN02/Text/part0010.xhtml/p000092
  - YS-LN02/Text/part0010.xhtml/p000093
  - YS-LN02/Text/part0010.xhtml/p000094
  - YS-LN02/Text/part0010.xhtml/p000095
  - YS-LN02/Text/part0010.xhtml/p000096
  - YS-LN02/Text/part0010.xhtml/p000097
  - YS-LN02/Text/part0010.xhtml/p000098
  - YS-LN02/Text/part0010.xhtml/p000099
  - YS-LN02/Text/part0010.xhtml/p000100
  - YS-LN02/Text/part0010.xhtml/p000101
  - YS-LN02/Text/part0010.xhtml/p000102
  - YS-LN02/Text/part0010.xhtml/p000103
  - YS-LN02/Text/part0010.xhtml/p000104
  - YS-LN02/Text/part0010.xhtml/p000105
  - YS-LN02/Text/part0010.xhtml/p000106
  - YS-LN02/Text/part0010.xhtml/p000107
  - YS-LN02/Text/part0010.xhtml/p000108
  - YS-LN02/Text/part0010.xhtml/p000109
  - YS-LN02/Text/part0010.xhtml/p000110
  - YS-LN02/Text/part0010.xhtml/p000111
  - YS-LN02/Text/part0010.xhtml/p000112
  - YS-LN02/Text/part0010.xhtml/p000113
  - YS-LN02/Text/part0010.xhtml/p000114
  - YS-LN02/Text/part0010.xhtml/p000115
  - YS-LN02/Text/part0010.xhtml/p000116
  - YS-LN02/Text/part0010.xhtml/p000117
  - YS-LN02/Text/part0010.xhtml/p000118
files_written:
  - reviews/prose/vol-02/ch-01-b05-claude.md
review_path: reviews/prose/vol-02/ch-01-b05-claude.md
validator: not_run
diff_check: not_run
counts:
  serious: 0
  moderate: 6
  minor: 15
findings:
  - {severity: moderate, segment_id: "p000089,p000092,p000118", issue: "Serebryakov bị gọi Trung úy, lệch sổ vol02-ch01-b02-lieutenant (Thiếu úy)", resolution: "đổi thành Thiếu úy hoặc coordinator chốt Trung úy cho cả hai và đồng bộ toàn chương"}
  - {severity: moderate, segment_id: p000092, issue: "mất nhấn mạnh <em> của nguồn (cả một vế); thêm 'chính' thay vì *...*", resolution: "bọc vế đó bằng *...* theo DEC-P01-002"}
  - {severity: moderate, segment_id: p000095, issue: "đại từ trần thuật 'cô' cho Tanya, trái sổ b01/b02 (lặp tên/lược chủ ngữ)", resolution: "dùng 'Tanya' hoặc lược chủ ngữ"}
  - {severity: moderate, segment_id: "p000088,p000115", issue: "'sĩ quan tùy viên' lệch sổ b03-adjutant ('sĩ quan phụ tá'), 'tùy viên' gợi attaché", resolution: "dùng 'sĩ quan phụ tá'"}
  - {severity: moderate, segment_id: p000109, issue: "đảo góc nhìn: người ra đòn bị thành người bị đánh", resolution: "giữ chủ thể là kẻ ra đòn phải lường trước bị đáp trả"}
  - {severity: moderate, segment_id: "p000088,p000105,p000110,p000115", issue: "tự quy chiếu nội tâm lúc 'mình', lúc 'tôi'", resolution: "dùng 'mình' nhất quán cho độc thoại một chủ thể (hoặc 'tôi' cho tất cả); coordinator đồng bộ với b01–b04"}
pending_terms:
  - {source_term: post-structuralist, proposed_vi: người theo chủ nghĩa hậu cấu trúc, segment_ids: [YS-LN02/Text/part0010.xhtml/p000088], volume: vol-02, chapter: 1, status: pending}
  - {source_term: formula-fixed, proposed_vi: đã cố định thuật thức, segment_ids: [YS-LN02/Text/part0010.xhtml/p000097], volume: vol-02, chapter: 1, status: pending}
  - {source_term: anti-surface grenade, proposed_vi: lựu đạn chống mục tiêu mặt đất, segment_ids: [YS-LN02/Text/part0010.xhtml/p000097], volume: vol-02, chapter: 1, status: pending}
  - {source_term: infantry square, proposed_vi: đội hình vuông bộ binh, segment_ids: [YS-LN02/Text/part0010.xhtml/p000116, YS-LN02/Text/part0010.xhtml/p000118], volume: vol-02, chapter: 1, status: pending}
  - {source_term: Command Company, proposed_vi: Đại đội chỉ huy, segment_ids: [YS-LN02/Text/part0010.xhtml/p000094], volume: vol-02, chapter: 1, status: pending}
  - {source_term: Frederick the Great, proposed_vi: Friedrich Đại đế, segment_ids: [YS-LN02/Text/part0010.xhtml/p000109], volume: vol-02, chapter: 1, status: pending}
unresolved_findings: 6
term_recommendations:
  - {term_id: vol02-ch01-b05-post-structuralist, decision: keep, proposed_vi: người theo chủ nghĩa hậu cấu trúc, alternatives: [nhà hậu cấu trúc luận, một tay hậu cấu trúc], segment_ids: [YS-LN02/Text/part0010.xhtml/p000088], confidence: 0.65, uncertainty: "ý đồ phê phán trường phái của nguồn không rõ; không ảnh hưởng cốt truyện", status: pending}
  - {term_id: vol02-ch01-b05-formula-fixed, decision: change, proposed_vi: đã cố định thuật thức, alternatives: [thuật thức cố định, gắn sẵn thuật thức, cố định công thức], segment_ids: [YS-LN02/Text/part0010.xhtml/p000097], confidence: 0.5, uncertainty: "cách dùng quân sự không rõ; tránh 'gắn' và 'sẵn' vì suy diễn", status: pending}
  - {term_id: vol02-ch01-b05-anti-surface-grenade, decision: keep, proposed_vi: lựu đạn chống mục tiêu mặt đất, alternatives: [lựu đạn chống lực lượng mặt đất, lựu đạn đối đất], segment_ids: [YS-LN02/Text/part0010.xhtml/p000097], confidence: 0.6, uncertainty: "chưa rõ nguyên tác nhấn đối đất hay chống sát thương; thống nhất phòng không ở p000099/p000112", status: pending}
  - {term_id: vol02-ch01-b05-infantry-square, decision: keep, proposed_vi: đội hình vuông bộ binh, alternatives: [đội hình ô vuông của bộ binh, khối vuông bộ binh], segment_ids: [YS-LN02/Text/part0010.xhtml/p000116, YS-LN02/Text/part0010.xhtml/p000118], confidence: 0.65, uncertainty: thấp, status: pending}
risks:
  - "Đồng bộ chéo b01–b04 về cấp bậc Serebryakov, đại từ trần thuật Tanya, 'sĩ quan phụ tá' và tự quy chiếu nội tâm chưa kiểm được (không đọc các batch đó)."
  - "formula-fixed độ chắc thấp (0.5); xem lại nếu batch sau giải thích cơ chế lựu đạn."
  - "Không có quyết định ảnh hưởng cốt truyện; không cần hỏi người dùng. Mọi lựa chọn là đề xuất, không canon."
commit: null
next_action: "translator sửa M1–M6 và xem xét L1–L15, áp dụng T1–T4, coordinator ghi T5–T8 vào ledger; sau đó validator/diff-check và signoff ngắn cho các đoạn đã sửa trước khi commit"
```
