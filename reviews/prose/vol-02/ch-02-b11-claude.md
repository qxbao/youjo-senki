# Review b11 — vol-02-ch-02-b11-review

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích câu nguồn.
- **Phạm vi:** 42 đoạn `YS-LN02/Text/part0014.xhtml/p000258`–`p000299` (viết tắt `pNNNNNN`). Đã đọc: handoff b11, gói nguồn đã chuẩn bị, `translations/vol-02/ch-02-b11.jsonl`, `canon/` (glossary, characters, style-guide, decisions, glossary-pending), `work/run-state/pending-terms.yml` (mục `chapter2_b11_translation_proposals` và các mục b02–b10 liên quan đến đơn vị, công thức ma pháp, Named, Pixie, Viper, Bộ Tổng tham mưu, sở chỉ huy). Không đọc batch dịch khác.
- **Kiểm tra cơ học:** 42/42 đoạn, thứ tự và `segment_id` khớp gói nguồn; `source_sha256` khớp từng đoạn. Trường `notes` rỗng, không có ghi chú làm việc lẫn vào bản dịch. Chữ nghiêng (DEC-P01-002): nguồn có nhấn mạnh ở p000263, p000271, p000287; bản dịch chỉ có `*...*` ở p000287 (đúng phạm vi). p000263 và p000271 bị thiếu (xem MOD-3, MOD-4).

## Kết luận: `needs_fixes` (serious 0, moderate 7, minor 15)

## Moderate

### MOD-1 — p000258: "Pháp sư Không vận" sai tên đơn vị so với ledger
- **Vấn đề:** ledger `vol02-ch01-b06-aerial-mage-battalion` / `vol02-ch01-b10-aerial-mage-battalion` đặt tạm "Tiểu đoàn Pháp sư Không quân (203)". Bản dịch dùng "Không vận", nghĩa là vận tải đường không (airlift), đổi nghĩa đơn vị tác chiến thành đơn vị vận chuyển.
- **Đề xuất:** "Tiểu đoàn Pháp sư Không quân 203" (đồng bộ ledger).
- **Độ tin cậy:** 0,85.

### MOD-2 — p000258: sai dấu ngoặc đóng của lời thoại
- **Vấn đề:** nguồn là một lời thoại có trích dẫn lồng (hiệu gọi) rồi tiếng ngập ngừng của nhân viên điện đài nằm ngoài trích dẫn lồng. Bản dịch đóng bằng dấu nháy đơn, nên lời thoại ngoài không được đóng; ngoặc kép mở ở đầu đoạn bị bỏ lửng.
- **Đề xuất:** kết thúc bằng dấu nháy kép đóng sau "Ờ…" (giữ nháy đơn đóng sau "Pixie.").
- **Độ tin cậy:** 0,9.

### MOD-3 — p000263: thiếu toàn bộ chữ nghiêng của nguồn
- **Vấn đề:** nguồn nhấn mạnh ba phạm vi: (a) hai câu đầu (trích lại thông điệp và câu hỏi nội tâm), (b) từ "impressively", (c) từ "overly". Bản dịch không có `*...*` nào; mất cả cấu trúc đối lập "ấn tượng → quá mức". Vi phạm DEC-P01-002 và checkpoint `emphasis` của handoff.
- **Đề xuất:** nghiêng hai câu đầu; nghiêng từ tương ứng "ấn tượng" và "quá" ở câu cuối. Ví dụ câu cuối: "Mức độ tự tin này đã vượt qua mức *đáng nể* để thành *quá* tự tin." (xem thêm m3 về "tự phụ").
- **Độ tin cậy:** 0,9.

### MOD-4 — p000271: nhấn mạnh bị thay bằng dấu ngoặc kép
- **Vấn đề:** cụm "acting without permission" là chữ nghiêng trong nguồn (cụm bị nuốt lại, không nói ra). Bản dịch dùng “…” (dấu ngoặc kép) nên đọc như lời trích dẫn nhân vật, đồng thời mất `*...*` theo DEC-P01-002.
- **Đề xuất:** "Anh ta nuốt xuống những lời *tự ý hành động*, nhưng…".
- **Độ tin cậy:** 0,85.

### MOD-5 — p000265: "Họ định…" đổi nghĩa "be supposed to"
- **Vấn đề:** nguồn là câu hỏi phẫn nộ về việc bị yêu cầu/được mong đợi phải đặt đơn vị dưới quyền một chỉ huy không hiểu tình hình. "Họ định đặt" biến thành ý định của bên khác và làm mờ yếu tố nghĩa vụ/áp đặt. Câu sau ("tuyệt đối không thể chấp nhận") càng cho thấy nhân vật là bên bị buộc phải làm.
- **Đề xuất:** "Phải đặt các đơn vị dưới quyền một chỉ huy không hiểu điều đó sao?" hoặc "Họ buộc phải giao các đơn vị cho một chỉ huy không hiểu điều đó sao?". Chủ thể "họ" giữ mơ hồ vì nguồn không nói rõ ai ra lệnh.
- **Độ tin cậy:** 0,65.

### MOD-6 — p000297: "công thức giao thoa" lệch ledger
- **Vấn đề:** ledger đặt tạm "thuật thức" cho "formulas" (`vol02-ch02-b09-formulas`) và "thuật thức gây nhiễu ma pháp" cho "magical interference formulas" (`b02-magical-interference-formulas`). Bản dịch dùng "công thức giao thoa", lệch cả thuật ngữ chính lẫn bổ ngữ (giao thoa ≠ gây nhiễu), nên cùng một khái niệm có hai tên trong cùng chương.
- **Đề xuất:** "Kẻ có thể dùng những thuật thức gây nhiễu mạnh đến mức làm biến dạng không gian." Nếu coordinator muốn giữ "interference = giao thoa" thì phải cập nhật cả ledger b02/b09 và áp dụng nhất quán, không để hai biến thể cùng tồn tại.
- **Độ tin cậy:** 0,65. Chỉ là phương án tạm, không phải canon.

### MOD-7 — p000264: "hành quân cưỡng bức" gợi hành quân bộ
- **Vấn đề:** ledger `vol02-ch02-b06-long-range-maneuver` chọn từ cơ động tương thích hàng không, ghi rõ "không phải hành quân bộ". Đoạn này nói về tiểu đoàn pháp sư bay tới. "Hành quân cưỡng bức" là thuật ngữ bộ binh (đi bộ cường độ cao). Ngoài ra "Rõ ràng… khó lòng" đẩy mức chắc chắn lên cao hơn nguồn (nguồn dùng "dường như không", mức suy đoán); và "lại đang tấn công" đọc như đang diễn ra, trong khi nguồn mô tả loại tiểu đoàn.
- **Đề xuất:** "Rõ ràng một tiểu đoàn xung kích vừa trải qua chặng cơ động gấp rút…" hoặc "Có vẻ không thể tự mình xử lý nổi chuyện đó khi một tiểu đoàn tấn công vừa tới sau chặng cơ động cấp tốc." Dùng "dường như/có vẻ" thay "Rõ ràng".
- **Độ tin cậy:** 0,6.

## Minor (không chặn, nên sửa cùng lượt nếu tiện)

| ID | Đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| m1 | p000259 | "danh hiệu liên lạc" là một cách gọi mới cho callsign; ledger chưa có mục; có thể lệch với "hiệu gọi" dùng ở batch khác. | Chọn "hiệu gọi" hoặc "tín hiệu gọi" cho toàn bộ chương; ghi ledger (xem thuật ngữ pending). |
| m2 | p000262 | "Yêu cầu… lập tức rút lui" nhẹ hơn một chỉ thị; p000271 gọi nội dung này là mệnh lệnh. | "Hãy cho Tiểu đoàn Viper lập tức rút lui." (hoặc "Cho Tiểu đoàn Viper rút lui ngay.") |
| m3 | p000263 | "quá tự phụ" thêm phán xét tính cách; nguồn chỉ nói mức tự tin quá mức. | "quá tự tin" (xem MOD-3). |
| m4 | p000266 | "Ta" làm lời nói của sĩ quan tham mưu nghe như người bề trên; nguồn trung tính. | "Chúng ta có thể… phải không?" hoặc "Có thể… đúng không?". "Điều động" hơi hành chính; "cho cất cánh khẩn cấp" sát "scramble" hơn. |
| m5 | p000270 | "họ" chọn người làm chủ thể của "use them" (Pixie hay Viper), trong khi vật được dùng cũng có thể là tiêm kích ở p000266–p000268. Ngữ cảnh không đủ để khẳng định. | Giữ nguyên nếu coordinator muốn; hoặc dùng "Chẳng phải nên dùng đến chúng sao?" nếu hiểu là tiêm kích (0,4). Ghi độ bất định. |
| m6 | p000272, p000276, p000281, p000290 | "sĩ quan tham mưu" thêm thuộc tính cấp bậc cho "staff members / staffer" ở p000272 ("staff members' authority", "staffer"). Nguồn p000276/p000290 có "staff officers" nên đúng. | p000272: "nhân viên tham mưu / người làm tham mưu" cho "staff members/staffer". |
| m7 | p000276 | Dùng lẫn "tiếp viện" (reinforcements, p000259) và "chi viện" (assistance, backup, p000262, p000276). Hai từ cùng chỉ một lực lượng ở các đoạn gần. | Thống nhất từ cho "backup" thành "tiếp viện" hoặc ghi rõ ledger chỉ dùng "chi viện" cho "assistance". |
| m8 | p000280 | "Có thể dữ liệu ghi kỷ lục là…" đọc như khả năng dữ liệu nói gì; nguồn là nhượng bộ (dù dữ liệu ghi kỷ lục…). "hợp lý" cho "commonsense" hơi yếu. | "Dữ liệu có thể ghi nhận kỷ lục là tám nghìn, nhưng…"; "giới hạn theo lẽ thường". |
| m9 | p000282 | "khiêm nhường" là tự giữ thái độ; nguồn là bị làm cho phải khiêm tốn (humbled). | "họ chẳng còn cách nào khác ngoài việc phải cúi đầu / thấy mình nhỏ bé trước điều đang chứng kiến". |
| m10 | p000291 | "quân bài chủ lực" không phải thành ngữ tự nhiên; tương đương của trump card là "át chủ bài". | "…có một dị thường làm át chủ bài." |
| m11 | p000294 | "Đã xác nhận một Named!" thêm sắc thái báo cáo chính thức; nguồn là lời kêu lên nhận ra. "Named mà họ còn chẳng chắc…" thiếu từ chỉ định, hơi cụt. | "Là Named! Có một Named được phát hiện ở phía tây!"; câu cuối: "Named mà họ còn chẳng chắc có tồn tại hay không đã xuất hiện." |
| m12 | p000295, p000296, p000297 | "Kẻ" mở ba câu tiêu ngữ thêm sắc thái hạ thấp; nguồn dùng "the one" trung tính. "vùng chết chóc" biến danh từ riêng/khái niệm "death zone" thành tính từ. | "Người…" hoặc "Kẻ" chỉ khi coordinator chọn thống nhất (0,45); "vùng chết" hoặc "vùng tử địa" cho death zone. |
| m13 | p000298 | "cười nhạo" nặng hơn "laughed it off" (gạt đi bằng tiếng cười). "đang say rượu" khẳng định đang say; nguồn chỉ nói anh ta đã uống. | "họ chỉ cười xòa…", "hơn nữa anh ta còn uống rượu". |
| m14 | p000299 | "cô" cho người được đề cập ở đây: DEC-P01-001 chỉ chốt "nó" cho trần thuật về Tanya, và nguồn đoạn này là điểm nhìn của bên khác; không suy rộng. Phương án "cô" hợp với "she" nhưng là chọn tạm. "kính trọng… thẳng thừng phủ nhận" ổn. | Giữ "cô" làm lựa chọn tạm (0,55); ghi ledger; không nâng canon. Thay thế: "người ấy". |
| m15 | p000273, p000288, p000289 | "Đơn vị điều khiển" cho "control unit" là thuật ngữ mới chưa có ledger; "điều khiển" dễ hiểu là điều khiển thiết bị. Nhân viên đơn vị này là người được hỏi "anh" ở p000279. | Ghi pending; tạm giữ, thay thế "đơn vị kiểm soát/đơn vị điều hành". |

## Điểm đã kiểm tra, không có lỗi
- **Người nói và chủ thể:** p000258–p000262 (nhân viên điện đài ↔ sĩ quan tham mưu), p000266–p000271 (hai sĩ quan tham mưu), p000273–p000289 (đơn vị điều khiển ↔ tham mưu) và p000294 (quan sát viên) nhất quán; không phát hiện lẫn người nói. Đây là phía Đế quốc (sở chỉ huy), và Named ở p000294–p000299 là người được phe Cộng hòa mô tả; chưa có xác nhận trong batch rằng đó là Tanya, nên không suy ra.
- **Số liệu và phủ định:** 48 tín hiệu, 250 km/h (p000274), 300 (p000284), 6.000/8.000 feet (p000280, p000283) đúng; 7.500 giữ không đơn vị đúng nguồn (p000277). "Không cần chi viện" và các phủ định ở p000279, p000289 đúng.
- **Thuật ngữ khớp ledger:** "Tiểu đoàn Viper", "Pixie" (hiệu gọi/biệt danh, giữ nguyên), "Named" (giữ nguyên, viết hoa), "Bộ Tổng tham mưu Trung ương", "Quân đội Cộng hòa/phe Cộng hòa", "Đế quốc".
- **Văn phong:** nhìn chung tự nhiên, nhịp tốt; p000281–p000282 và p000286–p000287 giữ được lập luận.

## Thuật ngữ pending

### 1. Đơn vị và hiệu gọi (p000258, p000259, p000262–p000264, p000273, p000283, p000286)
- **Tiểu đoàn Pháp sư Không quân 203:** đề xuất tạm theo ledger b06/b10, sửa "Không vận" (MOD-1). Độ tin cậy 0,85 cho việc loại "Không vận"; 0,65 cho tên đầy đủ. Thay thế: "Tiểu đoàn Pháp sư Không quân số 203".
- **Pixie (Tiểu đoàn Pixie / các Pixie):** giữ nguyên, như `vol02-ch02-b10-pixie-callsign` (0,7). Là hiệu gọi vô tuyến và biệt danh đơn vị; dạng "các Pixie" ở p000272 là cách gọi tập thể, không suy ra sở hữu hay quan hệ với đơn vị 203. Thay thế: "Tiểu đoàn Tiên nữ" (loại, 0,05; không dùng nghĩa đen khi nguồn dùng như tên gọi).
- **Viper (Tiểu đoàn Viper):** giữ nguyên, theo `vol02-ch02-b07-viper-battalion` (0,5). Thay thế: "Tiểu đoàn Rắn lục". Không suy ra quan hệ giữa Viper và Pixie.
- **Callsign:** đề xuất "hiệu gọi" (0,5); bản dịch dùng "danh hiệu liên lạc" (p000259). Thay thế: "tín hiệu gọi", "danh hiệu liên lạc". Không ảnh hưởng cốt truyện.
- **Control unit:** tạm "đơn vị điều khiển" (0,45); thay thế "đơn vị kiểm soát", "đơn vị điều hành". Cần giữ nhất quán p000273, p000288, p000289.

### 2. Quy ước đơn vị đo độ cao nguồn (feet/foot) — p000277, p000280, p000283, p000286
- **Đề xuất tạm:** giữ đơn vị gốc, không quy đổi sang mét. Viết "feet" (không biến đổi theo số) thay cho "foot": "sáu nghìn feet", "tám nghìn feet". Số không kèm đơn vị trong nguồn (p000277 "7.500", p000273 "độ cao…") giữ không đơn vị; không tự thêm "feet" vào đó. Tốc độ nguồn dùng kilômét một giờ (p000274) thì giữ "kilômét một giờ"; các số trần ở p000273, p000284 giữ trần.
- **Lý do:** (1) quy đổi sẽ tạo số lẻ như 1.829 m, 2.438 m, làm mất so sánh số liệu với giới hạn kinh nghiệm và với số trần chưa có đơn vị; (2) nguồn đã trộn feet với km/h nên việc thống nhất đơn vị là can thiệp của biên tập chứ không phải việc của người dịch; (3) "foot" số ít với số lớn đọc như lỗi chính tả hơn "feet"; (4) "bộ" mơ hồ nghĩa với các nghĩa khác.
- **Phương án thay thế:** (a) "foot" như bản dịch hiện tại (0,3; chấp nhận được nhưng lạ); (b) "bộ" (0,15); (c) quy đổi sang mét (0,1; loại trừ vì lý do 1–2); (d) viết tắt "ft" (0,2; ít hợp văn xuôi).
- **Độ tin cậy:** 0,55 cho "giữ feet"; 0,8 cho "không quy đổi".
- **Rủi ro:** thấp, không ảnh hưởng cốt truyện. Nếu coordinator chọn quy ước đo lường toàn bộ truyện, cần ghi một mục ledger duy nhất. Không đụng canon.

### 3. Named (p000294, p000299) — đề xuất tạm: giữ nguyên "Named"
- Theo `vol02-ch02-b10-named`: nhãn viết hoa, giữ nguyên, không ngoặc kép, không chú giải. Chứng cứ trong batch này tăng hơn: "Named" được dùng như danh từ chỉ người ("một Named", "Named này"), được xác nhận qua đối chiếu cá nhân với biệt danh. Vẫn không có định nghĩa trong batch. Độ tin cậy 0,6. Thay thế: "người có danh hiệu", "Người Có Danh". Không suy lore thêm.

### 4. Devil of the Rhine (p000294) — đề xuất: "Ác quỷ sông Rhine"
- Giữ như bản dịch (0,55). Viết hoa chữ đầu "Ác" (như một biệt danh), "sông Rhine" thường. Thay thế: "Ác quỷ Rhine" (0,3; gọn nhưng mất danh từ chỉ vị trí), "Ác quỷ vùng Rhine" (0,2; đổi nghĩa địa lý), "Ác Quỷ sông Rhine" viết hoa kiểu tiêu đề (0,3, nếu coordinator muốn các biệt danh viết hoa từng chữ như "Bạch Ngân"). Cần xác nhận cách viết hoa biệt danh theo ledger `vol02-ch01-b10-white-silver`.
- **Rủi ro:** biệt danh có thể xuất hiện trong nhiều batch về sau; ghi một mục ledger duy nhất. Đây là tên riêng thật sự, nên không dịch sang dạng khác nếu chưa có căn cứ.

### 5. Deviation (p000291, p000292) — đề xuất: giữ "dị thường"
- Chứng cứ: ở p000291 "deviation" là danh từ (một kẻ/sự vật làm quân bài chủ lực), p000292 lặp lại như tính chất ("Deviation is right"); p000289 dùng "bất thường" cho "abnormalities". Vì vậy "dị thường" tách khỏi "bất thường" (đúng) và dùng được cả hai vị trí. Độ tin cậy 0,5.
- Thay thế: "ngoại lệ" (0,25; mất ý lệch chuẩn), "sự lệch chuẩn" (0,2; nặng thuật ngữ), "độ lệch" (0,05; như đại lượng, loại). Không dịch thành tên người/loại người, vì nguồn không nêu.
- **Thao tác:** nếu giữ "dị thường", chỉnh danh từ cho tự nhiên ("một kẻ dị thường" chỉ khi coordinator chấp nhận suy ra đó là người; mặc định 0,4 giữ không suy diễn).

### 6. Các mục mới nên thêm vào ledger (đề xuất, không canon)
| Mục | Đề xuất | Thay thế | Độ tin cậy | Đoạn |
|---|---|---|---|---|
| interference formulas | thuật thức gây nhiễu | thuật thức giao thoa | 0,6 | p000297 |
| death zone | vùng chết | vùng tử địa | 0,5 | p000295 |
| height unit | feet (không quy đổi) | foot; bộ | 0,55 | p000280, p000283 |
| control unit | đơn vị điều khiển | đơn vị kiểm soát | 0,45 | p000273, p000288, p000289 |
| call sign | hiệu gọi | danh hiệu liên lạc | 0,5 | p000259 |
| Quân đội Cộng hòa (contact) | đầu mối trong Quân đội Cộng hòa | người liên lạc | 0,6 | p000298 |
| Named reference to Tanya, "she" | cô (tạm) | người ấy | 0,55 | p000299 |

## Rủi ro
- p000258–p000263: 3 lỗi định dạng/nhấn mạnh (MOD-2, 3, 4) có thể khiến validator hoặc bước dựng EPUB sai; cần sửa trước khi commit.
- Đại từ "cô" (p000299) và biệt danh "Ác quỷ sông Rhine" liên quan danh tính Tanya; batch không xác nhận nên không suy diễn. Không phải hard stop.
- Quy ước feet/foot cần ghi vào ledger để các batch sau không đổi sang mét hoặc từ khác.
- p000270 ("họ" so với "chúng") là điểm mơ hồ; nếu chọn sai chỉ ảnh hưởng nhẹ, không chặn.
- Không có phát hiện serious; batch chưa đạt hoàn tất theo `completion` vì còn 7 moderate.

## Đề xuất bước tiếp theo
Người giữ quyền sửa áp dụng MOD-1 đến MOD-7 và các minor nên sửa, cập nhật ledger theo mục pending ở trên (coordinator ghi), chạy lại validator/diff-check, rồi cho Claude ký xác nhận sau sửa (fixes signoff) trước khi commit.
