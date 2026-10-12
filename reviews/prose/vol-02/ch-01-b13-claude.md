# Báo cáo phản biện — vol-02-ch-01-b13

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon).
- Phạm vi: `p000327`–`p000369` (43 đoạn), gồm handoff b13, gói nguồn cục bộ, `translations/vol-02/ch-01-b13.jsonl`, canon và sổ pending.
- Kích hoạt: `new_pending_terms`, `meaning_style` (lỗi phát âm/văn phong ở p000330).
- Báo cáo không trích câu nguồn. Thuật ngữ nguyên gốc ngắn và mã đoạn chỉ dùng để nhận diện. Mọi lựa chọn dưới đây là đề xuất tạm, không phải canon, không nâng lên canon.
- Mã đoạn viết tắt `pNNNNNN` = `YS-LN02/Text/part0010.xhtml/pNNNNNN`.

## 1. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự | 43/43, liên tục p000327→p000369, khớp 1–1 giữa nguồn và bản dịch |
| Hash gói nguồn | `cca46a9e…05d1df7e` khớp `source_package_sha256`; `source_sha256` mọi đoạn khớp `3ac53161…` |
| Hash canon (5 tệp) | Khớp handoff (glossary, style-guide, characters, decisions, glossary-pending) |
| Trường bản dịch | `status: draft`, `glossary_version` khớp, `notes` rỗng ở cả 43 đoạn |
| Dấu chú thích | Không có ở nguồn lẫn bản dịch |
| Nhấn mạnh (DEC-P01-002) | Nguồn có 2 chỗ in nghiêng: toàn bộ câu nội tâm ở p000333 và một câu ngắn ở p000346. Bản dịch **không có `*…*` nào**. Xem M1. |
| Đại từ Tanya (DEC-P01-001) | Trần thuật dùng "cô" (không phải "nó"); p000337 còn dùng "mình" trong trần thuật. Lệch quy ước và lệch b11/b12. Xem M2. |
| Phủ định / logic | Các cấu trúc phủ định, nhượng bộ và điều kiện (p000328–329, 336, 355–356, 360) giữ đúng. |

Nhìn chung bản dịch bám nghĩa tốt, giọng mỉa mai ở p000328, 331, 344, 359 được giữ, thuật ngữ đã có (Tiểu đoàn Pháp sư Không quân 203, Type 95, Being X, quả cầu) dùng nhất quán với sổ pending. Không có lỗi nghiêm trọng.

## 2. Phát hiện

Đếm: **nghiêm trọng 0 · vừa 5 · nhẹ 14**.

### Mức vừa

**M1 — p000333, p000346: mất chữ nghiêng/nhấn mạnh (DEC-P01-002).**
- p000333: toàn bộ câu nội tâm của Visha in nghiêng ở nguồn; bản dịch bọc trong dấu ngoặc kép, không có `*…*`.
- p000346: câu thành ngữ ngắn (câu "đừng khơi chuyện") in nghiêng ở nguồn; bản dịch không đánh dấu.
- Đề xuất: p000333 → `…Không, suy nghĩ của cô là: *Thế này thì thấp kém quá đấy, thiếu tá.*` (bỏ ngoặc kép, dùng `*…*` cho đúng phạm vi nhấn mạnh). p000346 → bọc câu thành ngữ trong `*…*` (xem N6 về cách diễn đạt).

**M2 — p000331, 332, 337, 338, 342, 343, 346, 348, 364: đại từ trần thuật Tanya lệch DEC-P01-001 và lệch b11/b12.**
- DEC-P01-001: trần thuật về Tanya dùng "nó", nội tâm tự quy chiếu dùng "mình". b11/b12 làm đúng thế. b13 dùng "cô" cho Tanya ở p000331, 332, 337 (ba lần), 338, 342 (hai lần), 343, 346, 348, 364.
- p000337: "tuổi của mình" nằm trong trần thuật, không phải nội tâm → phải là "nó/của nó" (hoặc lược).
- Rủi ro kéo theo: p000332–333 có cả Tanya và Visha. Nếu cả hai đều "cô", câu "suy nghĩ của cô" ở p000333 mơ hồ giữa hai người. Đổi Tanya thành "nó" sẽ giải ngay chỗ này ("cô" còn lại chỉ Visha).
- Nội tâm (p000331 "mình", p000345 "Mình") và lời nói (p000339 "mình" phản thân) đúng, giữ nguyên.
- Đề xuất: đổi "cô" chỉ Tanya thành "nó" ở các đoạn nêu trên (lược chủ ngữ khi tự nhiên). Giữ "cô" cho Visha (p000332–333). Giữ "anh" cho Weiss: nguồn dùng đại từ nam ở p000337, đây là căn cứ mới (xem mục 3.7).

**M3 — p000330: mất chi tiết phát âm trẻ con (xét riêng ở mục 4).**
- Nguồn cố ý viết sai âm ở hai từ (một từ thay âm l bằng w, một từ rụng âm tiết đầu). Bản dịch dịch cả câu sang tiếng Việt chuẩn. Style guide và quy tắc sau pilot-01 yêu cầu giữ chi tiết phát âm khi nguồn nêu. p000331 tiếp ngay đó nhắc "giọng nói nực cười" nên chi tiết này có chức năng truyền tải.
- Tiền lệ: b12 M3 (p000322, p000325) đã được xử lý bằng ngọng nhẹ ở từ chính ("cánh báo", kéo dài nguyên âm).
- Handoff ghi mức nhẹ; tôi nâng lên **vừa** để nhất quán với b12 M3 và vì vi phạm một quy tắc nêu rõ trong style guide. Tác động rất nhỏ (một đoạn, hai từ), sửa một dòng.
- Đề xuất: xem mục 4.

**M4 — p000351: bỏ mất đối tượng hô gọi "observers", lệch sổ pending.**
- Nguồn có hai mệnh lệnh: triển khai thuật thức và gọi nhóm quan sát phải nhìn kỹ. Bản dịch "Quan sát cho kỹ!" bỏ danh từ nhóm; người đọc không biết ai được gọi, và mục `vol02-ch01-b13-observers` trong sổ không có chỗ nào trong bản dịch để áp dụng.
- Đề xuất: p000351 → "Triển khai thuật thức! Các quan sát viên, nhìn cho kỹ!" (xem mục 3.3).

**M5 — p000335: "chị" trong lời Weiss gọi Thiếu tá.**
- "chị" mang giới tính và quan hệ tuổi tác/thân tộc. DEC-P01-001 không cho suy quan hệ hoặc giới từ ngữ cảnh thiếu căn cứ; b12 (`vol02-ch01-b12-address-to-lieutenants`) chọn gọi theo cấp bậc, tránh đại từ có giới/thân tộc. Ở đây nguồn chỉ có cấp bậc.
- Đề xuất: "Thiếu tá, Thiếu tá đã từng diễn xuất chưa?" hoặc lược: "Thiếu tá từng có kinh nghiệm diễn xuất chưa?" Không thêm "ạ" (nguồn không có từ lễ phép; xem b11 L9).
- Ghi chú: "cậu" ở p000336 (Tanya gọi Weiss) nay có căn cứ giới nam (p000337), nên chấp nhận được; xem mục 3.7.

### Mức nhẹ

| # | Đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| N1 | p000327 vs p000330 | Cùng một bản thông báo mà p000327 "chúng ta" (bao gồm người nghe), p000330 "chúng tôi" (loại trừ). Lời cảnh báo phát cho phía địch nên "chúng tôi" hợp hơn. | p000327 → "Ba mươi phút nữa chúng tôi sẽ bắt đầu diễn tập." |
| N2 | p000328 | "một đứa trẻ hiển nhiên như thế" gượng; nguồn nói đối tượng *hiển nhiên là* trẻ con. | "lời đe dọa của một người rõ ràng là trẻ con" |
| N3 | p000329 | "cau có" nặng/khác nghĩa; nguồn là cái nhíu mày *chê trách*. | "nhăn mặt chê trách rồi quay về ngủ" |
| N4 | p000331 | "sự hành xác tinh thần Tanya" thiếu "của", dễ hiểu nhầm; "Theo một nghĩa nào đó" thêm nhẹ. Thêm "cô" xem M2. | "sự hành xác tinh thần của Tanya" |
| N5 | p000337 | "rối bời" mạnh hơn "phức tạp" của nguồn; "vậy mà" thêm tương phản. | "tâm trạng phức tạp"; "nhưng ngay cả anh…" |
| N6 | p000340 | "với tư cách quân nhân" bị gắn sai vào vế "khắc sâu vào họ", trong khi thuộc về "huấn luyện"; "khắc sâu" làm nhẹ sắc thái bị nhồi/đóng vào bằng kỷ luật. | "trong quá trình huấn luyện làm quân nhân, có một điều đã bị nhồi vào đầu họ" |
| N7 | p000343 | "hăng máu" thêm sắc thái khát máu; nguồn chỉ nói có động lực (mỉa mai). | "Nó đang rất có động lực." / "…hăng hái" |
| N8 | p000346 | "rồi dựng lên" thêm quan hệ nối tiếp; nguồn nối hai hành động đồng thời. Câu thành ngữ dịch thành "người đang nổi giận" cụ thể hóa hơn nguồn. | "…khi thi triển… và dựng lên…"; câu in nghiêng: "*Đừng đánh thức con chó đang ngủ.*" (thay thế: "*Chớ khơi chuyện đã yên.*") |
| N9 | p000347 | "khai sáng" gần nghĩa "enlighten", va chạm với mục pending `P05-enlightenment`; nguồn là "educate". | "Hãy giáo huấn chúng nhân danh Chúa." (thay thế: "dạy cho chúng một bài học") |
| N10 | p000349 | Chuyển "Ta" cho Tanya: nguồn không có sắc thái chúa tể, và Tanya dùng "Tôi" ở p000336, p000344. | "Tôi sẽ khiến quyền năng của Chúa hiển hiện…" (giữ "Ta" nếu coordinator coi là giọng diễn có chủ ý; độ tin cậy 0,5) |
| N11 | p000342 | "phe Cộng hòa" thêm "phe"; sổ pending dùng "quân/lực lượng Cộng hòa" hoặc "Cộng hòa". | "nhận được sự hỗ trợ của Cộng hòa" |
| N12 | p000333 | "Thấp hèn" gán bình diện đạo đức/miệt thị không có trong nguồn (style guide cấm). Xem mục 3.8. | "Thế này thì thấp kém quá đấy, thiếu tá." |
| N13 | p000328, 333, 335, 338, 346 | Chức danh viết thường "thiếu tá"; b11/b12 viết hoa "Thiếu tá" khi dùng như danh xưng/gọi. | Thống nhất "Thiếu tá" |
| N14 | p000334, 359 | "chúng tôi": nguồn "we" ở p000334 có thể là giọng nội tâm của Tanya hoặc người kể gộp cả đơn vị; p000359 rất gần giọng nội tâm ("giải pháp tối ưu"). Ngôi "chúng tôi" hơi trang trọng cho nội tâm. | Giữ "chúng tôi" (an toàn); thay thế "bọn mình" nếu coordinator xác nhận đó là nội tâm. Độ tin cậy 0,4 — không sửa nếu chưa có căn cứ. |

Các điểm đã kiểm và chấp nhận: p000332 (giữ nghĩa, Visha là chủ thể của "emotions"), p000336 (Tanya nói "họ" = địch), p000337 (Weiss là người thấy, "anh"), p000341 (câu "vì thế… họ hiểu" giữ được quan hệ nhân quả), p000355–356 (điều kiện/tương phản), p000359 (con số 48 và "tối ưu"), p000362–363 (trúng đích, nhận xét), p000364 ("nhà máy" thay cho "it", chấp nhận được; **không** dùng "nó" vì trùng với đại từ của Tanya), p000366 ("bừng tỉnh" hơi chủ động hơn "bị đánh thức" nhưng chấp nhận được).

## 3. Khuyến nghị thuật ngữ (đề xuất tạm, không phải canon)

### 3.1 formula / formulas — `vol02-ch01-b13-formula`
- **Chọn tạm:** **thuật thức** (giữ).
- **Phương án thay thế:** công thức.
- **Độ tin cậy:** 0,6 (sổ ghi 0,6; tôi giữ).
- **Căn cứ:** nhất quán với `P01-formulas`, `b02-magical-interference-formulas`, `vol02-ch01-b05-formula-fixed`; "công thức" dễ nhầm với công thức toán học, trong khi nguồn dùng với động từ phóng/thi triển/khai hỏa. Bản dịch b13 dùng đồng nhất.
- **Đoạn thực tế có thuật ngữ:** p000346 (hai lần, gồm projection formula), p000351, 352, 354, 355, 357, 359, 361, 363. **Sổ ghi sai danh sách đoạn:** liệt kê p000331, 342, 353, 356, 358 (không có thuật ngữ này) và thiếu p000359. Cần coordinator sửa `segment_ids`.
- **Bất định:** vẫn chưa rõ "formula" là thuật ngữ quân sự hay kỹ thuật ma pháp trong thế giới truyện; không ảnh hưởng cốt truyện.

### 3.2 projection formula — `vol02-ch01-b13-projection-formula`
- **Chọn tạm:** **thuật thức phóng chiếu** (tầm xa).
- **Phương án thay thế:** công thức phóng chiếu; thuật thức phóng tầm xa (độ tin cậy thấp, 0,3).
- **Độ tin cậy:** 0,55.
- **Căn cứ:** nguồn đứng cạnh "extra-large yet precise formula" và định ngữ "long-range"; bản dịch nghĩa đen giữ được phân biệt hai thuật thức. Không đủ căn cứ cho cách hiểu cơ chế cụ thể (đẩy, dẫn hướng, hay mở rộng tầm).
- **Đoạn:** p000346.

### 3.3 observers — `vol02-ch01-b13-observers`
- **Chọn tạm:** **quan sát viên** (đổi từ "người quan sát").
- **Phương án thay thế:** người quan sát; pháp sư quan sát (chỉ nếu xác nhận cùng nhóm với "observer mage").
- **Độ tin cậy:** 0,55.
- **Căn cứ:** tiền lệ b07 `b07-artillery-observer` dùng "quan sát viên pháo binh" là nhãn vai trò; "quan sát viên" giữ cùng gốc nhưng không thêm "pháp sư"/"pháo binh" khi p000351 không nêu. "Người quan sát" nghe như nhãn trung tính nhưng lỏng hơn khi dùng làm đối tượng hô gọi.
- **Bất định:** chưa rõ nhóm này có trùng với "pháp sư quan sát" (`b07-observer-mage`) hay không; không ảnh hưởng cốt truyện. Cũng không rõ người hô p000351 là ai (không có nhãn người nói), nên giữ lời hô trung tính.
- **Đoạn:** p000351.

### 3.4 augmented mage battalion — `vol02-ch01-b13-augmented-mage-battalion`
- **Chọn tạm:** **tiểu đoàn pháp sư tăng cường** (giữ).
- **Phương án thay thế:** tiểu đoàn pháp sư được tăng viện; tiểu đoàn pháp sư biên chế mở rộng.
- **Độ tin cậy:** 0,5.
- **Căn cứ:** "tăng cường" trong quân sự tiếng Việt chấp nhận cả nghĩa biên chế bổ sung lẫn lực lượng phối thuộc, nên không buộc nghĩa cụ thể; số 48 trong nguồn ở cùng đoạn cho thấy đây là quân số thực tế của đơn vị, và "gồm bốn mươi tám người" trong bản dịch giữ được dữ kiện này.
- **Bất định:** không đủ căn cứ để quyết "augmented" nói về biên chế hay về tăng viện; **không** suy diễn quy mô biên chế chuẩn. Không ảnh hưởng cốt truyện.
- **Đoạn:** p000359. Cần bảo đảm tên "Tiểu đoàn Pháp sư Không quân 203" (p000342) không bị lẫn với cách gọi này: đã nhất quán.

### 3.5 anti-magic artillery — `vol02-ch01-b13-anti-magic-artillery`
- **Chọn tạm:** **pháo chống ma pháp** (giữ).
- **Phương án thay thế:** pháo kháng ma pháp; pháo bắn pháp sư (diễn giải, không khuyến nghị).
- **Độ tin cậy:** 0,55.
- **Căn cứ:** sát nghĩa "anti-"; tương tự `vol02-ch01-b07-anti-air-positions`, `anti-surface strikes`. "Kháng" gợi sức đề kháng, lệch hơn. Đoạn nói pháo hoạt động chống pháp sư đang thi triển, và "chống" bao được cả hai cách hiểu.
- **Bất định:** chưa rõ đây là loại pháo đặc biệt hay chức năng của pháo thường; không ảnh hưởng cốt truyện.
- **Đoạn:** p000355.

### 3.6 orb — `vol02-ch01-b13-orb`
- **Chọn tạm:** **quả cầu** (giữ).
- **Phương án thay thế:** quả cầu tính toán.
- **Độ tin cậy:** 0,7.
- **Căn cứ:** tiền lệ `vol02-ch01-b08-computation-orb`; nguồn dùng số nhiều, tiếng Việt không đánh dấu số nên không cần đổi. Ở p000341 đi cạnh "súng trường", dạng ngắn đọc ổn. Nếu coordinator muốn giảm mơ hồ ở lần đầu của một tiểu chương, dùng "quả cầu tính toán".
- **Đoạn:** p000341.

### 3.7 Mục mới đề xuất bổ sung vào sổ (chưa có trong 6 nhóm)

- **Carberius Arms Foundry** (p000352). Tạm: "Nhà máy Vũ khí Carberius" (độ tin cậy 0,5); thay thế "Xưởng đúc vũ khí Carberius". "Foundry" nghiêng xưởng đúc, còn p000342 gọi cùng mục tiêu là "munitions factory" nên "nhà máy" an toàn hơn. Tên riêng Carberius giữ nguyên. Không thấy mục này trong sổ.
- **Tamaya (tiếng hô khi xem pháo hoa), p000369.** Tạm: giữ nguyên phiên âm "Tamayaaa!" (độ tin cậy 0,8); không thêm chú thích trong bản dịch. Nếu về sau cần chú thích thì theo quy tắc chú thích của dự án, không do translator tự thêm.
- **Cách gọi Weiss / Tanya trong lời nói.** Nguồn ở p000337 dùng đại từ nam cho Weiss, giúp xác định giới của Weiss; sổ b12 (`vol02-ch01-b12-address-to-lieutenants`) đang ghi "chưa xác định". Đề xuất coordinator ghi nhận "Weiss: nam theo p000337" cho mục này (vẫn là đề xuất tạm). Với Serebryakov vẫn chưa có thêm căn cứ.
- **Tanya gọi Weiss là "cậu"** (p000336): chấp nhận được với căn cứ trên; độ tin cậy 0,6, thay thế "Trung úy" (gọi theo cấp bậc).

### 3.8 "That's so low" — p000333
- **Chọn tạm:** "Thế này thì thấp kém quá đấy, thiếu tá."
- **Phương án thay thế:** "nhỏ nhen quá"; "hạ cấp quá".
- **Độ tin cậy:** 0,45.
- **Căn cứ:** p000345 sau đó Tanya tự nhận đang xả giận lên địch, nên "low" có thể là "nhỏ nhen/hạ thấp mình". "Thấp hèn" đặt bình diện đạo đức/miệt thị mạnh hơn nguồn.
- **Bất định:** chưa rõ "low" là về đạo đức, phẩm cách hay chiến thuật; chọn cách trung tính nhất.

## 4. Đánh giá riêng vấn đề phát âm/văn phong ở p000330

**Hiện trạng.** Nguồn có hai từ bị phát âm sai có chủ ý (một từ thay âm l bằng w, một từ rụng âm tiết đầu). Bản dịch chuẩn hóa hoàn toàn.

**Phân tích.**
- Đây là chi tiết do nguồn nêu, không phải suy diễn; quy tắc sau pilot-01 yêu cầu giữ. Đoạn kế tiếp (p000331) dựa vào "giọng nực cười", và p000332–334 (phản ứng của đơn vị, "giọng phù hợp trẻ con") cũng dựa vào nó.
- Nếu giữ chuẩn hóa, hiệu ứng hài/mỉa mai chung của đoạn vẫn còn nhờ lời dẫn, nhưng hai điểm phát âm đóng vai trò chữ ký giọng, bị mất.
- Tiền lệ b12 đã chọn ngọng nhẹ ở từ chính, không kéo dài cả đoạn. Nên cùng một quy ước cho b13.
- Tránh phát minh kiểu ngọng khác với b12 (vd. đổi cả một loạt âm), vì sẽ làm giọng Tanya không nhất quán giữa các lô.

**Đề xuất tạm** (độ tin cậy 0,5): tối đa hai thay đổi nhỏ, trùng với hai từ nguồn bị sai: một từ chính ở vế đầu, một từ ở vế sau.
- Ví dụ: "Chúng tôi **chân chọng** thề—mọi **nười** đều thề sẽ chiến đấu công bằng, đúng theo luật pháp quốc tế." (tr→ch ở "trân trọng"; "người"→"nười").
- Phương án thay thế A: chỉ ngọng một từ ("chân chọng") và giữ phần còn lại chuẩn (ít rủi ro đọc hiểu nhất).
- Phương án thay thế B: giữ văn bản chuẩn, ghi vào handoff rằng chi tiết phát âm bị bỏ có chủ ý (không khuyến nghị vì trái quy tắc).
- Không thêm chú thích hoặc lời dẫn vào bản dịch.

**Về "fair and square":** "công bằng" đủ nghĩa; thành ngữ nguồn thêm sắc "đường hoàng, minh bạch" nhưng không bắt buộc (nhẹ, không lập thành phát hiện).

**Mức độ:** vừa (M3); không ảnh hưởng cốt truyện; coordinator không cần hỏi người dùng.

## 5. Rủi ro còn lại

- M2 (đại từ Tanya) có thể lan sang các lô sau nếu coordinator dùng b13 làm mẫu; ảnh hưởng toàn chương.
- M1 là một lỗi cấu trúc nhỏ nhưng validator không bắt (validator pass vẫn có thể bỏ qua nhấn mạnh thiếu `*…*`).
- Sổ pending sai danh sách đoạn cho `formula` và thiếu hai mục (Carberius, Tamaya); nếu không sửa, truy vết thuật ngữ về sau sai.
- Chỗ dùng "nó" thay cho "cô" làm tăng nguy cơ nhầm với "nó" chỉ vật; cần kiểm lại p000332, 333, 337, 346, 364 sau khi sửa.
- Chi tiết N14 (ngôi "chúng tôi"/"bọn mình") là bất định thật sự; không nên sửa nếu không có căn cứ.
- Không phát hiện quyết định ảnh hưởng cốt truyện. Không cần hỏi người dùng.

## 6. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-01-b13
state: done
segment_ids: [YS-LN02/Text/part0010.xhtml/p000327, YS-LN02/Text/part0010.xhtml/p000369] # 43 đoạn liên tục
files_written: [reviews/prose/vol-02/ch-01-b13-claude.md]
review_path: reviews/prose/vol-02/ch-01-b13-claude.md
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 5, minor: 14}
unresolved_findings: [M1, M2, M3, M4, M5, N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14]
findings:
  - {severity: moderate, id: M1, segment_id: p000333/p000346, issue: thiếu *…* theo DEC-P01-002}
  - {severity: moderate, id: M2, segment_id: p000331/332/337/338/342/343/346/348/364, issue: đại từ trần thuật Tanya "cô"/"mình" lệch DEC-P01-001}
  - {severity: moderate, id: M3, segment_id: p000330, issue: mất chi tiết phát âm trẻ con}
  - {severity: moderate, id: M4, segment_id: p000351, issue: bỏ đối tượng hô gọi observers}
  - {severity: moderate, id: M5, segment_id: p000335, issue: "chị" có giới/thân tộc, nên gọi theo cấp bậc}
term_recommendations:
  - {id: vol02-ch01-b13-formula, proposed_vi: thuật thức, alternatives_vi: [công thức], confidence: 0.6, segment_ids: [p000346, p000351, p000352, p000354, p000355, p000357, p000359, p000361, p000363], status: pending, note: sổ ghi sai danh sách đoạn}
  - {id: vol02-ch01-b13-projection-formula, proposed_vi: thuật thức phóng chiếu, alternatives_vi: [công thức phóng chiếu, thuật thức phóng tầm xa], confidence: 0.55, segment_ids: [p000346], status: pending}
  - {id: vol02-ch01-b13-observers, proposed_vi: quan sát viên, alternatives_vi: [người quan sát, pháp sư quan sát], confidence: 0.55, segment_ids: [p000351], status: pending}
  - {id: vol02-ch01-b13-augmented-mage-battalion, proposed_vi: tiểu đoàn pháp sư tăng cường, alternatives_vi: [tiểu đoàn pháp sư được tăng viện, tiểu đoàn pháp sư biên chế mở rộng], confidence: 0.5, segment_ids: [p000359], status: pending}
  - {id: vol02-ch01-b13-anti-magic-artillery, proposed_vi: pháo chống ma pháp, alternatives_vi: [pháo kháng ma pháp], confidence: 0.55, segment_ids: [p000355], status: pending}
  - {id: vol02-ch01-b13-orb, proposed_vi: quả cầu, alternatives_vi: [quả cầu tính toán], confidence: 0.7, segment_ids: [p000341], status: pending}
  - {id: vol02-ch01-b13-carberius-foundry, proposed_vi: Nhà máy Vũ khí Carberius, alternatives_vi: [Xưởng đúc vũ khí Carberius], confidence: 0.5, segment_ids: [p000352], status: pending, note: mục mới}
  - {id: vol02-ch01-b13-tamaya, proposed_vi: giữ nguyên phiên âm, alternatives_vi: [], confidence: 0.8, segment_ids: [p000369], status: pending, note: mục mới}
  - {id: vol02-ch01-b13-childish-pronunciation, proposed_vi: ngọng nhẹ ở từ chính, trùng quy ước b12, alternatives_vi: [chỉ một từ, văn bản chuẩn], confidence: 0.5, segment_ids: [p000330], status: pending}
risks: [lan truyền đại từ Tanya sang lô sau, validator không bắt thiếu nhấn mạnh, sổ pending sai segment_ids và thiếu mục, N14 bất định]
commit: null
next_action: translator_fix_then_reviewer_signoff # M1–M5 cần sửa; coordinator cập nhật sổ pending; không hỏi người dùng
```
