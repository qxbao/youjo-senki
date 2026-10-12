# Review b10 — vol-02-ch-02-b10-review

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích câu nguồn.
- **Phạm vi:** 37 đoạn `YS-LN02/Text/part0014.xhtml/p000221`–`p000257` (viết tắt `pNNNNNN`). Đã đọc: handoff b10, gói nguồn đã chuẩn bị, `translations/vol-02/ch-02-b10.jsonl`, `canon/` (glossary, characters, style-guide, decisions, glossary-pending), `work/run-state/pending-terms.yml` (mục `chapter2_b10_translation_proposals` và các mục b07–b09, ch01 liên quan đến đơn vị/chỉ huy/Trung ương). Không đọc batch dịch khác.
- **Kiểm tra cơ học:** 37/37 đoạn, thứ tự và `segment_id` khớp gói nguồn; `source_sha256` khớp từng đoạn. Chữ nghiêng (DEC-P01-002) khớp nguồn ở cả 11 đoạn có nhấn mạnh (p000226, p000229, p000232, p000235, p000237, p000239, p000243, p000251, p000253, p000256, p000257), kể cả phạm vi từng đoạn: p000226 (chỉ câu hỏi nội tâm), p000232 (chỉ một từ cảm thán), p000239 (câu đầu), p000253 (ba câu đầu, ba câu sau không nghiêng), p000257 (chỉ câu thứ hai). Không có nhấn mạnh thừa hay thiếu. Phủ định, số liệu (B-3) và thứ tự thông tin đều đúng.

## Kết luận: `needs_fixes` (serious 0, moderate 3, minor 12)

## Moderate

### MOD-1 — p000221: đổi quan hệ thời gian và dùng sai đại từ
- **Vấn đề:** nguồn nói sự việc xảy ra đúng lúc nhân vật vừa nghĩ đến nó (trùng hợp về thời điểm, nối ngay các đoạn thoại vô tuyến phía sau). Bản dịch thành "đoán không sai", tức là đánh giá dự đoán đúng/sai, không còn tính đồng thời; đồng thời có thể đọc như nhân vật đã dự đoán trước. Ngoài ra "Nó" là đại từ trần thuật theo DEC-P01-001 chỉ dành cho Tanya; chủ thể ở đây là người chỉ huy Viper (các đoạn kế tiếp dùng "anh"), nên không được áp dụng.
- **Đề xuất:** "Đúng lúc anh vừa nghĩ thế thì chuyện đó xảy ra." (hoặc "Ngay khi anh vừa nghĩ vậy thì…"). Dùng "anh" thống nhất với p000226, p000234, p000238.
- **Độ tin cậy:** 0,8 về đại từ; 0,7 về đổi nghĩa (nguồn ngắn, thiếu ngữ cảnh đoạn trước nên chưa thể chắc "chuyện đó" chỉ gì; giữ trung tính).

### MOD-2 — p000233: "cậu" cho người ở CP nói với Viper 02
- **Vấn đề:** người nói là nhân viên liên lạc ở CP (liền mạch p000231–p000232; p000228 cùng người dùng "các anh"). "Cậu" ngụ ý bề trên/thân mật, trái DEC-P01-001 (không suy ra quan hệ hoặc cấp bậc từ thiếu ngữ cảnh) và lệch với "các anh" ở p000228. Mục ledger `vol02-ch02-b08-tanya-address-to-viper02` là lời Tanya (p000175), không áp dụng cho nhân viên CP. Thêm "đi" biến "nên vui" thành lệnh, mạnh hơn nguồn.
- **Đề xuất:** "Và anh nên mừng đi." hoặc "Anh cũng nên vui lên. Chỉ huy của họ là một Named." (đồng bộ với p000228 "Mừng đi"). Nếu muốn trung lập hơn, bỏ đại từ: "Còn nữa, nên mừng đi."
- **Độ tin cậy:** 0,7.

### MOD-3 — p000235, p000237 (nội tâm Viper 02): "tôi" lệch ledger "mình"
- **Vấn đề:** ledger `vol02-ch02-b08-viper-interior-self-reference` đặt tạm "mình" (thay thế "tôi") cho nội tâm Viper 02. Ở b10, nội tâm dùng "tôi" (p000235 "tôi sẽ khui…", p000237 "Tôi muốn hô… / Tôi hiểu"), trong khi p000229 dùng "chúng ta". Lệch với checkpoint "pronouns" của handoff và gây hai biến thể cho cùng một chủ thể trong cả ba lượt b08–b10.
- **Đề xuất:** đổi sang "mình" ở các đoạn nội tâm (p000235, p000237) để khớp ledger; hoặc, nếu coordinator thấy "tôi" tự nhiên hơn, cập nhật ledger b08 thành "tôi" và áp dụng nhất quán. Đừng để hai biến thể cùng tồn tại. Cả hai đều chỉ là phương án tạm, không phải canon.
- **Độ tin cậy:** 0,6 (vấn đề nhất quán thật; độ ưu tiên giữa "mình"/"tôi" thấp).

## Minor (không chặn, nên sửa cùng lượt nếu tiện)

| ID | Đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| m1 | p000222, p000236, p000246 | "roger" dịch ba kiểu: "Rõ", "nghe rõ", "Rõ". p000236 là phản hồi bằng hiệu gọi nên "nghe rõ" hợp lý nhưng tạo hai biến thể. | Chọn một dạng cho cả batch ("Rõ" hoặc "Nghe rõ"). |
| m2 | p000232, p000244 | Cùng một người: "Trực ban viên" rồi "nhân viên điện đài". Nguồn có hai danh xưng khác nhau (operator / radio operator) nên chấp nhận được, nhưng người đọc dễ tưởng hai người. | Thống nhất ("nhân viên điện đài" cho cả hai) hoặc ghi ledger. |
| m3 | p000224 | Gọi CP lặp hai lần ở nguồn, bản dịch bỏ lần hai ("Có chuyện gì vậy?"), mất nhịp gọi dồn. | "Sở chỉ huy? Sở chỉ huy, có chuyện gì vậy?" |
| m4 | p000230 | "sao giờ mới điều đến?" thu hẹp câu hỏi thành chuyện thời điểm; nguồn hỏi vì sao chờ đợi/không dùng lực lượng dự bị khi đã có. | "Nếu còn quân tăng viện thì còn chờ gì nữa?" |
| m5 | p000241 | Câu bị động ẩn tác nhân; "Họ nhận định" thêm chủ thể xác định (dễ hiểu là CP hoặc chính tiêm kích). Ẩn tác nhân là điểm tác giả cố ý. | "…Đã được đánh giá là không cần thiết." |
| m6 | p000236 | "xịn sò" quá khẩu ngữ/hiện đại cho đối thoại vô tuyến quân sự; nguồn mỉa mai nhưng ở sắc thái quân đội. | "Viện binh quả là hạng sang." hoặc "Viện binh thật là…", mức mỉa mai tương đương. Độ tin cậy 0,4. |
| m7 | p000247 | "Sở chỉ huy" cho Northern Army Group Headquarters trùng với "Sở chỉ huy" của CP (Command Post), dù ledger `vol02-ch01-b08-command-post-headquarters` cho "tổng hành dinh" tùy ngữ cảnh. "Các sĩ quan" thêm thuộc tính cấp bậc cho "staff". | "Tổng hành dinh Cụm tập đoàn quân phương Bắc" (hoặc "Bộ chỉ huy…"); "các nhân viên/cán bộ tham mưu" thay cho "các sĩ quan". |
| m8 | p000253 | "Central Army" → "Tập đoàn quân Trung ương": "tập đoàn quân" trùng loại đơn vị với "Cụm tập đoàn quân" ở các đoạn khác và là thuật ngữ mới chưa có trong ledger. | Ghi pending mới; tạm "Quân Trung ương" (trung lập về cấp đơn vị). |
| m9 | p000248 | "chúng" cho Bộ Tổng tham mưu thêm sắc thái khinh miệt nặng hơn "they" của nguồn (đã có "chết tiệt" cho sự giận dữ). | "Sao họ nghĩ họ có thể…". |
| m10 | p000255 | "Đúng là gan thật" dễ đọc thành khen; nguồn là chê trơ trẽn ("có gan đấy mà"). | "Đúng là to gan." hoặc "Cũng gan thật đấy." |
| m11 | p000256, p000257 | "miền Bắc" (kho/đường tiếp tế) lệch với "phương Bắc" dùng cho Cụm tập đoàn quân/Bộ chỉ huy. | Thống nhất "phương Bắc". |
| m12 | p000235 | "mang theo món quà" đổi chủ thể; nguồn là "chúng ta nhận được món quà tuyệt vời này". | "…lại còn nhận được món quà tuyệt vời này vậy." |
| m13 | p000249, p000253, p000257 | Nhóm lệch nhỏ: p000249 "vừa mới nghĩ" thêm tính vừa xảy ra; "lẽ thường tình" bị thay bằng "đương nhiên". p000253 "Dù không muốn buộc tội" (nguồn: chưa đến mức buộc tội). p000257 bỏ "thậm chí"; "mọi người kinh ngạc" thêm "mọi người" (nguồn: tin gây kinh ngạc, không nêu đối tượng). | Sửa: "đã nghĩ", "đó cũng là lẽ thường tình", "dù chưa đến mức buộc tội", "Có thể thậm chí gọi…", "tin còn gây sững sờ hơn nữa". |

## Điểm đã kiểm tra, không có lỗi
- **Người nói và chủ thể:** p000224–p000231 là hội thoại Viper 02 ↔ CP nhất quán; p000234–p000239 nội tâm và trần thuật của người chỉ huy Viper dùng "anh"/nội tâm; p000247–p000257 chuyển sang Bộ chỉ huy phương Bắc (chuyển cảnh rõ ở p000247). Không phát hiện lẫn người nói. Rủi ro: do không đọc batch khác, không xác nhận được người chỉ huy Viper ở đây là Viper 02 như ledger b08; trong batch này cách đọc là hợp lý (p000236 tự xưng Viper 02).
- **Logic và giả định:** p000232 (điều kiện về đơn vị trung ương và khả năng đã đến sớm), p000238–p000239 (nhận ra sự đòi hỏi, ước tính tiêm kích), p000251 và p000256 (suy luận của bên Bắc) giữ đúng mức chắc chắn. Số liệu "B-3" chính xác. Phủ định ở p000245, p000247 ("đừng động vào") đúng.
- **Thuật ngữ khớp ledger:** "Tiểu đoàn Viper", "Đại Quân", "Cụm tập đoàn quân phương Bắc", "Bộ chỉ huy phương Bắc", "Cục Tác chiến", "Bộ Tổng tham mưu", "Trung ương", "pháp sư không quân" (tương thích "Tiểu đoàn Pháp sư Không quân"). "Pixie" giữ nguyên hiệu gọi là hợp lý.
- **Văn phong:** nhìn chung tự nhiên, nhịp tốt; thành ngữ "xó xỉnh nào" ở p000229 đúng sắc thái.

## Thuật ngữ pending

### Named (p000233, p000235) — đề xuất tạm: giữ nguyên "Named"
- **Chứng cứ trong phạm vi batch:** chữ hoa; dùng như danh từ chỉ người/loại ("chỉ huy của họ là một Named", "một tiểu đoàn viện binh và một Named"); đối đáp thể hiện đây là địa vị được coi trọng và khiến nhân vật huýt sáo kinh ngạc; không có định nghĩa nào trong batch. Vì vậy là nhãn/danh hiệu, không phải tính từ "được đặt tên" hay tên riêng cho cá nhân. Không dùng phỏng đoán lore để định nghĩa thêm.
- **Phương án tạm:** giữ nguyên "Named", viết hoa, không dấu ngoặc kép, không kèm chú giải trong bản dịch. Dùng "một Named", "các Named" (không biến đổi hình thái), áp dụng thống nhất khi gặp lại. Độ tin cậy 0,6.
- **Lý do:** (1) tránh tự khẳng định nghĩa chưa có trong batch; (2) cấu trúc "là một Named" vẫn đọc tự nhiên; (3) nghĩa "được đặt tên" ("là được đặt tên", "một được đặt tên") sai ngữ pháp/nghĩa khi dùng như danh từ; (4) giữ khả năng đổi sang phương án dịch sau khi có giải thích trong truyện mà không phải sửa nhiều chỗ.
- **Phương án thay thế:** (a) "người có danh hiệu" (rõ nghĩa hơn nhưng khẳng định nghĩa "danh hiệu" chưa có căn cứ trong batch; độ tin cậy 0,3); (b) "Kẻ Có Tên"/"Người Có Danh" (gần nghĩa đen nhưng lạ tai; 0,25); (c) "được đặt tên" (loại, 0,05).
- **Rủi ro/ảnh hưởng cốt truyện:** thuật ngữ có thể gắn với hệ thống danh hiệu/biệt danh ở các tập sau; không chặn batch nhưng khi có giải thích trong truyện cần rà lại. Nếu ledger đã có "White Silver" (Bạch Ngân) là biệt danh ở ch01 b10, không suy luận quan hệ giữa hai mục khi thiếu nguồn.
- **Thao tác cho coordinator:** cập nhật mục `vol02-ch02-b10-named` thành `proposed_vi: Named` (giữ nguyên), confidence 0,6, alternatives như trên; không nâng canon.

### Các mục mới nên thêm vào ledger (đề xuất, không canon)
- `Central Army` → "Quân Trung ương" (thay thế: "Tập đoàn quân Trung ương"), p000253, confidence 0,45 (xem m8).
- `Pixie` (hiệu gọi) → giữ nguyên "Pixie", p000231, confidence 0,7; không suy ra đơn vị này thuộc ai.
- `Sector B-3` → "Khu vực B-3", p000228, confidence 0,65.
- `Viper 02 interior self-reference`: ghi nhận lệch tại p000235, p000237 (xem MOD-3).

## Khuyến nghị
Translator/người giữ quyền sửa áp dụng MOD-1..3 (bắt buộc trước commit theo `review_coordination`), nên sửa m1–m13 cùng lượt nếu tiện; sau đó coordinator cập nhật ledger. Validator/diff_check: not_run. Commit: null.
