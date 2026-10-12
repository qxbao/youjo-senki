# Báo cáo duyệt gộp Claude — vol-01 Chapter 0, batch b03–b05 và 21 thuật ngữ pending P03/P04/P05

Người phản biện: Claude. Phạm vi đọc: `canon/` (glossary, glossary-pending, characters, decisions, style-guide), handoff b03–b05, `translations/vol-01/ch-00-b03..b05.jsonl`, các tự kiểm trong `reviews/semantic/`, báo cáo cũ `reviews/prose/vol-01-ch-00-b03-claude-review.md`, gói nguồn cục bộ `work/vol-01/batches/` và `work/vol-01/source.jsonl` (đọc tại chỗ, kể cả các chú thích cuối ¹ ²; dùng để kiểm tra cách thuật ngữ xuất hiện ở các chương sau). Báo cáo không chép câu nguồn và không sửa tệp nào khác.

Quy ước: mã đoạn viết tắt `pNNNNNN`, tiền tố đầy đủ `YS-LN01/Text/chapter001.xhtml/`. Đoạn không nêu tên có nghĩa là đã đối chiếu và không thấy lỗi có căn cứ. Trạng thái canon hiện tại: 21 mục vẫn `pending`; mọi đề xuất dưới đây chỉ là đề xuất, chỉ có hiệu lực sau khi được duyệt trong `canon/decisions.md`.

## 1. Tóm tắt

- **Nghiêm trọng:** không còn lỗi nghiêm trọng nào ở b03, b04, b05. Cả 2 lỗi nghiêm trọng cũ của b03 (p000043, p000053) đã được xử lý.
- **Điểm chạm tên/cấp bậc/quan hệ/xưng hô:** có 4 điểm, không điểm nào làm đổi cốt truyện nhưng đều cần ghi nhận hoặc quyết định (mục 4). Điều này khác với các tự kiểm b04 và b05, vốn ghi là không có.
- **Lore/lịch sử/ma pháp:** chưa thấy chỗ nào mơ hồ làm đổi cốt truyện. Nhưng nhóm từ lore nền (Thượng đế/Đấng Tạo Hóa/quỷ dữ/kẻ vô tín/đầu thai) chưa nằm trong pending dù sẽ lặp lại nhiều; nên bổ sung trước b06 (mục 5).
- **Hai cách hiểu làm đổi cốt truyện:** không có. Có ba chỗ hiểu được theo hai hướng nhưng không đổi cốt truyện: p000076, p000086, p000092 (mục 4).
- **Thuật ngữ:** đề nghị chốt 17/21 mục, giữ pending 4/21 mục (P03-rationality, P03-touchstone-award, P03-section-manager, P05-being-x) vì chưa đủ căn cứ hoặc cần người dùng quyết định (mục 2).
- Chú ý: 7 mục P01 trong `glossary-pending.yml` (sensibility… obedience to authority) thuộc b02, ngoài phạm vi báo cáo này, không đánh giá.

## 2. Đề nghị cho 21 thuật ngữ pending

### 2.1. Bảng tổng hợp

| Mã | Phương án hiện tại | Kết luận | Đề nghị cuối |
| --- | --- | --- | --- |
| P03-paradigm-shift | chuyển đổi mô thức | Đề nghị chốt | giữ nguyên |
| P03-Chicago-school | trường phái Chicago | Đề nghị chốt, có chỉnh | **trường phái kinh tế Chicago** |
| P03-rationality | tính hợp lý | Chưa đủ căn cứ, giữ pending | xem 2.3 |
| P03-moratorium | quãng tạm hoãn | Đề nghị chốt (cục bộ) | giữ nguyên |
| P03-human-capital | vốn con người | Đề nghị chốt | giữ nguyên |
| P03-signaling-theory | lý thuyết tín hiệu | Đề nghị chốt | giữ nguyên |
| P03-touchstone-award | giải Touchstone | Chưa đủ căn cứ, giữ pending | xem 2.3 |
| P03-section-manager | trưởng phòng | Chưa đủ căn cứ, giữ pending, cần hỏi người dùng | xem 2.3 |
| P04-cost-performance | hiệu quả chi phí | Đề nghị chốt | giữ nguyên |
| P04-occupational-physician | bác sĩ y tế lao động | Đề nghị chốt | giữ nguyên |
| P04-cash-advance-loan | khoản vay ứng lương | Đề nghị chốt, có chỉnh | **khoản vay tiền mặt** |
| P04-pip | PIP | Đề nghị chốt | giữ nguyên viết tắt |
| P04-pink-slip | giấy thôi việc | Đề nghị chốt, có chỉnh | **giấy sa thải** |
| P05-delusion | ảo tưởng | Đề nghị chốt, kèm ghi chú phạm vi | giữ nguyên |
| P05-hallucination | ảo giác | Đề nghị chốt | giữ nguyên |
| P05-being-x | Being X | Chưa đủ căn cứ, cần hỏi người dùng | xem 2.3 |
| P05-enlightenment | giác ngộ | Đề nghị chốt | giữ nguyên |
| P05-rawls-theory-of-justice | lý thuyết công lý của Rawls | Đề nghị chốt | giữ nguyên |
| P05-haves-have-nots | người có của và người tay trắng | Đề nghị chốt, có chỉnh bản dịch | sửa p000092 cho khớp |
| P05-cycle-of-life-and-death | vòng sinh tử | Đề nghị chốt, có chỉnh bản dịch | dùng thống nhất ở p000094 và p000100 |
| P05-behavioral-economics | kinh tế học hành vi | Đề nghị chốt | giữ nguyên |

Đếm theo cột "Kết luận": **17 mục đề nghị chốt** (12 giữ nguyên phương án hiện tại hoặc chốt kèm ghi chú; 3 chốt có chỉnh phương án: P03-Chicago-school, P04-cash-advance-loan, P04-pink-slip; và 2 giữ phương án nhưng cần sửa bản dịch cho khớp: P05-haves-have-nots, P05-cycle-of-life-and-death) và **4 mục giữ pending** (P03-rationality, P03-touchstone-award, P03-section-manager, P05-being-x). Tổng 21.

### 2.2. Lý do cho các mục đề nghị chốt

- **P03-paradigm-shift** (p000043). Chỉ xuất hiện một lần trong b03; từ "paradigm" còn xuất hiện ở chương sau (chapter009b p000105, ngữ cảnh chiến lược quốc phòng). "Mô thức" dùng được cho cả hai, tránh "hệ hình" vì nghe học thuật (Kuhn) hơn ngữ cảnh đời thường của p000043.
- **P03-Chicago-school** (p000046). Chú thích ¹ trong nguồn nói rõ đây là trường phái kinh tế; chương sau cũng ghi rõ "of economics" (chapter007b p000211). Bản dịch hiện chỉ có "trường phái Chicago", người đọc Việt dễ hiểu sang kiến trúc, xã hội học hoặc văn học. Đề nghị lần đầu dùng "trường phái kinh tế Chicago" kèm dấu ¹, các lần nhắc lại ở chương sau có thể rút gọn thành "trường phái Chicago" khi mạch đã rõ là kinh tế. Cần sửa p000046 (xem mục 3.1).
- **P03-moratorium** (p000047). Một lần duy nhất; câu đã tự giải thích ("cho đến khi bước ra đời") nên "quãng tạm hoãn" đủ hiểu. Không cần đưa vào canon toàn cục; có thể đóng pending bằng quyết định cục bộ. Không đủ căn cứ để khẳng định nghĩa chuyên ngành tâm lý–xã hội, nên không nâng thành thuật ngữ cố định.
- **P03-human-capital** (p000047). Còn lặp lại ở chapter007 (p000428, p000429) và chapter009 (p000150), và ở p000428 xuất hiện cùng "human resources" trong một câu. "Vốn con người" giữ được sự phân biệt với "nguồn nhân lực"; "vốn nhân lực" dễ lẫn.
- **P03-signaling-theory** (p000047). Lặp lại ở chapter009 p000150 (dùng cùng human capital). "Lý thuyết tín hiệu" là cách gọi phổ biến, nhất quán với cụm sau.
- **P04-cost-performance** (p000060, p000069). Hai lần đều là so sánh hiệu quả/chi phí của nhân sự; "hiệu quả chi phí" dùng nhất quán ở cả hai nơi và đúng nghĩa.
- **P04-occupational-physician** (p000060). Một lần; "bác sĩ y tế lao động" tự nhiên. Có thể chấp nhận "bác sĩ y học lao động" như phương án tương đương, không cần đổi.
- **P04-pip** (p000062). Nguồn chỉ dùng chữ viết tắt (nhiều lần trong cùng đoạn) và không khai triển; không nên tự mở rộng. Nếu muốn giúp người đọc thì cần quyết định chú thích riêng theo style-guide, không tự chèn vào bản dịch.
- **P04-cash-advance-loan** (p000060), chốt có chỉnh: "ứng lương" khẳng định khoản tiền gắn với lương (thường hiểu là công ty ứng trước), trong khi cụm nguồn thường chỉ khoản vay tiền mặt ngắn hạn (tín dụng/cho vay tiêu dùng). Phương án trung tính "khoản vay tiền mặt" không khẳng định nguồn tiền. Chỉ có một lần xuất hiện nên chưa đủ căn cứ để đặt tên chuyên biệt hơn.
- **P04-pink-slip** (p000073), chốt có chỉnh: "thôi việc" bao gồm cả tự nguyện, mà chính cảnh p000062 đối lập "từ chức tự nguyện" với "sa thải kỷ luật". "Giấy sa thải" không gây nhầm. Mức độ nhẹ, một lần.
- **P05-delusion / P05-hallucination** (p000080). Cặp "ảo tưởng"/"ảo giác" phân biệt rõ niềm tin sai và tri giác sai, đúng với cấu trúc "hoặc… hoặc…". Chương sau còn "mass hallucinations" (chapter005b p000262–263) nên "ảo giác" có thể dùng chung. Với delusion, thuật ngữ tâm thần học chặt chẽ là "hoang tưởng" nhưng mang sắc thái paranoia trong tiếng Việt thường ngày; nên giữ "ảo tưởng" cho p000080 và ghi chú rằng "delusional" ở chapter007/009 (p000032, p000122, p000205) là dùng nghĩa thường, xét theo ngữ cảnh chứ không ép về cùng một từ.
- **P05-enlightenment** (p000090, p000100; thêm p000131). Cả ba lần đều là nghĩa tâm linh (giải thoát khỏi ràng buộc trần thế, thoát vòng sinh tử); chữ viết thường, không phải "Enlightenment" thời Khai sáng. "Giác ngộ" phù hợp; nên bỏ cách hiểu "khai sáng" cho các đoạn này.
- **P05-rawls-theory-of-justice** (p000092). Chú thích ² xác nhận đây là lý thuyết triết học chính trị. "Lý thuyết công lý của Rawls" ổn, giữ dấu ².
- **P05-haves-have-nots** (p000092). Giữ phương án pending; sửa bản dịch p000092 từ "kẻ tay trắng" thành "người tay trắng" (xem 3.3).
- **P05-cycle-of-life-and-death** (p000094). "Vòng sinh tử" sát nghĩa đen và không áp giáo lý riêng; thống nhất với p000100 (xem 3.3).
- **P05-behavioral-economics** (p000096). Tên ngành chuẩn, một lần.

### 2.3. Mục chưa đủ căn cứ (giữ pending)

- **P03-rationality** (p000046; liên quan p000029 ở b02 và p000096 ở b05). Cùng một thuật ngữ nguồn đang có hai cách dịch trong bản nháp: "lý trí" (b02 p000029, trong bộ ba cùng sensibility/personality, thuộc P01) và "tính hợp lý" (b03 p000046), cộng "hợp lý/bất hợp lý" cho hai kiểu người (b05 p000096). Có ít nhất ba nghĩa cần phân định: phẩm chất cá nhân (p000029), tính duy lý kinh tế (p000046), kiểu người trong kinh tế học hành vi (p000096). Chưa đủ căn cứ để chọn một từ cho cả ba. Đề nghị tạm thời: nghĩa kinh tế (p000046, p000096) thống nhất họ "hợp lý"; nghĩa phẩm chất cá nhân (p000029) giữ "lý trí"; ghi rõ hai nghĩa trong pending và không đưa vào glossary chung cho đến khi chốt P01. Nếu người dùng muốn một từ duy nhất, cần xét luôn "duy lý/phi duy lý". Rủi ro hiện tại: nhẹ, không đổi cốt truyện.
- **P03-touchstone-award** (p000055). Nguồn viết thường "touchstone award", chỉ xuất hiện một lần, không có chú thích. Bản dịch "giải Touchstone" viết hoa như tên riêng, tức là khẳng định một điều chưa có căn cứ (có thể là tên riêng, cũng có thể là cách mô tả nghĩa "thước đo"). Chưa thể chốt. Cần người dùng quyết định: giữ nguyên "Touchstone" như tên giải, hoặc đặt trong ngoặc kép và thêm ghi chú; không nên tự dịch nghĩa.
- **P03-section-manager** (p000055). Chức danh một lần, nhưng chạm cấp bậc và liên quan hệ thống chức danh sẽ gặp lại: "department" (bộ phận nhân sự, p000055), "director of human resources" (p000069, p000073, và p000146 xác nhận "the director" ở cảnh ga cũng là giám đốc nhân sự), "supervisor" (p000060), và ở chapter003b có "section/division/personnel division" trong bối cảnh quân đội. Trong tiếng Việt "phòng" thường ở cấp department; "section" thấp hơn. Bản dịch đang dùng "bộ phận nhân sự" cho department và "trưởng phòng" cho section manager, có nguy cơ đảo thứ bậc nhìn thấy. Cần người dùng chốt bảng chức danh: ví dụ department → phòng, section → bộ phận hoặc tổ, nên section manager → trưởng bộ phận (hoặc giữ trưởng phòng và đổi department thành phòng/ban cho khớp). Chưa đủ căn cứ để tự chọn.
- **P05-being-x** (p000087, p000094, p000101). Đây là tên thực thể chính, xuất hiện ít nhất 25 lần trong tập 1; thuộc phạm vi `characters.yml` hơn là glossary. Nguồn dùng như nhãn do người kể đặt ("X" là ẩn số). Tạm giữ "Being X" là an toàn vì dễ thay hàng loạt về sau; nhưng việc Việt hóa (ví dụ "Tồn tại X", "Thực thể X") là quyết định tên gọi, cần người dùng duyệt trước khi dịch tiếp. Kèm theo cần quyết định giọng nhân vật (xem 4.2).

## 3. Lỗi còn lại theo batch

### 3.1. b03 (p000043–p000057)

**Nghiêm trọng:** không.

**Vừa**
- **p000046** — "trường phái Chicago" thiếu lĩnh vực. Căn cứ: chú thích ¹ và chapter007b ghi rõ kinh tế. Đề xuất: "trường phái kinh tế Chicago¹".
- **p000046** (liên đoạn p000029, p000096) — "rationality" đang có ba cách dịch khác nhau giữa các batch. Căn cứ: so sánh bản dịch b02/b03/b05. Đề xuất: xử lý theo 2.3, tối thiểu ghi chú đối chiếu trong pending.
- **p000055** — "section manager" gây nhầm thứ bậc với "bộ phận nhân sự" (xem 2.3 và 4.1). Đề xuất: chờ quyết định bảng chức danh.

**Nhẹ**
- **p000046** — "kẻ mọt sách" thêm sắc thái khinh; nguồn chỉ là kiểu người mọt sách. Đề xuất: "một anh mọt sách" hoặc "người mọt sách".
- **p000045** — "ý chí con người" thu hẹp "tinh thần con người" (spirit) sang ý chí (will). Tự kiểm có ghi giữ vì chưa đủ căn cứ; tôi cho rằng căn cứ đủ để đổi sang "tinh thần con người".
- **p000055** — "Touchstone" viết hoa như tên riêng (xem 2.3); "bước sang tuổi ba mươi" nghiêng về "vừa tròn ba mươi", trong khi nguồn là đã ở độ tuổi ba mươi. Đề xuất: "bước vào độ tuổi ba mươi".
- **p000043–p000055** — người đàn ông trưởng thành được gọi "anh" ở ngôi ba; DEC-P01-001 chỉ quy định Tanya ("nó"/"mình"). Đây là lựa chọn nhất quán, không sai, nhưng chưa có quyết định canon (xem 4.1).

### 3.2. b04 (p000058–p000074)

**Nghiêm trọng:** không.

**Vừa**
- **p000060, p000062, p000066** — nhân viên bị sa thải được gọi "anh", tức mặc định giới tính nam, trong khi nguồn tiếng Anh dùng "you". DEC-P01-001 dặn không suy giới tính hay quan hệ khi thiếu căn cứ. Đề xuất: ghi quyết định xưng hô cho cảnh này (tôi–anh là mặc định tạm hay đổi), xem 4.1. Tự kiểm b04 không nêu điểm này.
- **p000060** — "vay ứng lương" (xem 2.2). Đề xuất: "vay tiền mặt".
- **p000069** — "tôi sẽ thăng tiến… ngồi vào ghế giám đốc nhân sự" bỏ sắc thái dự đoán/kỳ vọng (should) thành khẳng định chắc chắn. Ở đây mức chắc chắn là chi tiết quan trọng vì p000070–p000071 ngay sau đó lặp lại kiểu "đáng lẽ". Đề xuất: "hẳn tôi sẽ thăng tiến vùn vụt…" hoặc "đáng lẽ từ đây tôi sẽ…" tùy giọng.

**Nhẹ**
- **p000058** — bỏ "AD" khi ghi ngày; chấp nhận được nhưng ghi nhận.
- **p000064** — "liên quan gì đến đào tạo" yếu hơn "tính là đào tạo thế nào được"; mất giọng chất vấn.
- **p000066** — "tay sai của sếp" thêm sắc thái kẻ làm việc bẩn; nguồn nghiêng về "cưng/cún của sếp". "Người máy" cho "cyborg" tạm ổn.
- **p000071** — mất dấu "…" mở đầu (ngập ngừng).
- **p000073** — "giấy thôi việc" (xem 2.2); "kẻ", "đám" thêm khinh thị; "lý trí" cho "logic" lẫn với "lý trí" của rationality ở b02.
- **p000073** — "Giám đốc" nhất quán với "giám đốc nhân sự" ở p000069; chapter001 p000146 xác nhận cùng người. Không cần sửa, nhưng nên thêm "director of human resources" vào pending (mục 5).

### 3.3. b05 (p000075–p000101)

**Nghiêm trọng:** không.

**Vừa**
- **p000097** — lời của Being X được dịch "Tôi hết chịu nổi", trong khi cùng nhân vật dùng "ta/ngươi" ở p000088, p000090, p000094, p000100. Người nói là Being X (p000098 xác nhận). Đề xuất: "Ta hết chịu nổi rồi."
- **p000082** — Being X nói "các người", trong khi các nơi khác là "các ngươi". Đề xuất: thống nhất giọng (xem 4.2).
- **p000086** — "Ông…" ngầm gán người nói là nhân vật chính xưng hô với Being X; theo mạch, đây nhiều khả năng là Being X đáp lại, khi đó phải là "ngươi". Hai cách hiểu, không đổi cốt truyện, nhưng đổi xưng hô. Đề xuất: người dùng/biên tập xác nhận người nói rồi sửa cho khớp.
- **p000100 và p000094** — cùng một vòng nhưng dịch "vòng luân hồi" và "vòng sinh tử"; "luân hồi" còn áp khái niệm nhà Phật. Đề xuất: thống nhất "vòng sinh tử".

**Nhẹ**
- **p000092** — "kẻ tay trắng" khác phương án pending và thêm sắc thái xấu; đề xuất "người tay trắng". "Trong hiện tại" mất "đời này" (đối lập với đời sau, liên hệ p000093 và p000096); đề xuất "ngay trong đời này". "Có ích gì chứ" lệch khỏi "có quan trọng gì". Không đổi cốt truyện.
- **p000093** — "có lý lẽ" cho "constructively" (có tính xây dựng); đề xuất "một cách xây dựng".
- **p000090** — "Nhân loại tiến bộ rồi" chuyển tiến trình thành hoàn tất; đề xuất "khi nhân loại ngày càng tiến bộ".
- **p000094** — "gã tự xưng" (thêm khinh) khác "kẻ tự xưng" ở p000101; mất "chỉ việc" (just) ở "Ta sẽ ném…". "Đầu thai" là một chọn lựa hợp lý cho "reborn", nhưng thu hẹp theo dân gian; nên đưa vào pending (mục 5).
- **p000076** — "Các người" vừa giả định số nhiều vừa thô hơn "Xin lỗi, ông là ai?" ở p000077. Chưa đủ căn cứ để sửa; ghi nhận.
- **p000101** — "anime" dịch "phim hoạt hình" mất nghĩa riêng của thể loại; đề xuất giữ "anime".

### 3.4. Xác nhận các lỗi cũ của b03 đã được xử lý

Đã đối chiếu từng mục trong báo cáo cũ (2 nghiêm trọng, 10 vừa, 7 nhẹ) với bản dịch hiện tại:

- **Nghiêm trọng, đã sửa:** p000043 (vị ngữ cuối lặp lại động từ thích nghi), p000053 (phạm vi "chỉ… lúc đầu", nối với "theo thời gian quen dần").
- **Vừa, đã sửa:** p000043 (bỏ "Hãy", ba câu in nghiêng đúng phạm vi nguồn), p000045 ("những người mê thể thao"), p000046 ("lý tính" → "tính hợp lý"; Chicago ghi pending), p000047 ("kỹ năng ngôn ngữ"), p000049 ("để có lợi cho anh"), p000050 ("công ty này công ty nọ"), p000055 (giữ "Touchstone", không tự diễn giải), p000056 ("đang cư xử… lịch thiệp"), p000057 ("một điều chợt ập đến với nó", giữ độ mở).
- **Nhẹ, đã sửa:** p000043, p000045 ("lải nhải"), p000048, p000052, p000055 ("leo dần các bậc thăng tiến"), p000056 ("xuống họng", "Tanya, thân mến"), p000057 ("Càng lúc càng sốt ruột").
- Xác nhận thêm: markdown `*...*` theo DEC-P01-002 khớp phạm vi nhấn mạnh của nguồn ở p000043 (ba câu), p000056 (cả đoạn), p000061 (một câu hỏi), p000071, p000072, p000074 (chỉ từ mở đầu). Đại từ "nó"/"mình" tại p000056–p000057 đúng DEC-P01-001. Không mất phủ định hay mất đoạn ở b03–b05.
- Tự kiểm b03 ghi "đã sửa 2/2 nghiêm trọng và 10/10 vừa": **đồng ý**. Điều tự kiểm chưa nêu: một số thuật ngữ được sửa nay để lộ vấn đề liên batch (rationality, Chicago).

## 4. Điểm chạm tên, cấp bậc, quan hệ, xưng hô, lore, cách hiểu kép

1. **Xưng hô / giới tính (chạm quy tắc DEC-P01-001).**
   - b03: người đàn ông trưởng thành gọi "anh" ở ngôi ba. Chưa có quyết định canon (DEC chỉ nói về Tanya). Nguồn có "he", nên không phải suy diễn sai; đề nghị ghi vào `decisions.md` như quy ước giai đoạn trưởng thành.
   - b04: nhân viên bị sa thải gọi "anh" dù nguồn chỉ có "you"; cặp "tôi–anh" giữa quản lý và nhân viên cũng là chọn lựa quan hệ chưa ghi. Đề nghị ghi rõ là tạm thời, không dùng làm căn cứ giới tính, hoặc người dùng chọn cách xưng hô trung tính hơn nếu có.
2. **Giọng Being X (b05).** "Ta/ngươi/các ngươi" ở p000088, p000090, p000094, p000100, nhưng "các người" ở p000082 và "Tôi" ở p000097; p000086 chưa rõ người nói. Người kể gọi lúc "ông ta", lúc "gã", lúc "kẻ". Cần ghi giọng chuẩn trong `characters.yml` khi người dùng chốt tên gọi.
3. **Cấp bậc / chức danh (b03–b04).** "Section manager", "department", "director of human resources", "supervisor", "executives" cần một bảng thứ bậc thống nhất (2.3). Không có lỗi cốt truyện nhưng dễ trôi nếu không chốt trước khi gặp thêm chức danh ở chương sau.
4. **Tên gọi (b05).** "Being X" là tên thực thể chính, cần quyết định (2.3).
5. **Hai cách hiểu, không đổi cốt truyện:** p000076 (số nhiều/thô hơn mức cần), p000086 (ai nói), p000092 ("đời này" hay "hiện tại"). p000057 ("it hit him", đã giữ độ mở) và p000074 (không xác định ai va vào) được giữ đúng; tôi đồng ý với cách xử lý của tự kiểm.
6. **Lore, lịch sử, ma pháp:** chuỗi lập luận ở p000087 (chỉ Thượng đế hoặc quỷ dữ phá được quy luật, không có Thượng đế nên Being X là quỷ dữ) được giữ đúng thành lập luận của nhân vật, không xác nhận sự thật khách quan. Chưa thấy chỗ nào làm đổi cốt truyện, ma pháp hay lịch sử (không có yếu tố ma pháp hay lịch sử thế giới Tanya trong 3 batch này).

## 5. Đề nghị bổ sung vào pending (chưa nằm trong 21 mục)

Các từ dưới đây là lore nền, lặp lại nhiều, nên đưa vào pending trước b06 để khỏi trôi:

- **God** (67 lần trong tập 1; p000087, p000094…) và **Creator** (p000088, p000138): hiện "Thượng đế", "Đấng Tạo Hóa"; cần chọn giữa Thượng đế/Chúa/Trời cho thống nhất.
- **devil** (p000085, p000087 và nhiều đoạn sau): hiện "quỷ dữ"; lưu ý có cụm danh xưng riêng có "devil" ở các chương sau (6 đoạn), nên cân nhắc chung với tên danh xưng đó để không trùng nghĩa.
- **disbelievers** (p000084, p000088, p000089): hiện "kẻ vô tín"; đoạn p000089 dựa trên số nhiều nên cần giữ phân biệt số ít/số nhiều.
- **reborn** (p000094, p000140; chapter003b p000016): hiện "đầu thai"; cân nhắc "tái sinh".
- **director of human resources** (p000069, p000073, p000146): "giám đốc nhân sự"; ghi chú cùng một người khi dùng "the director".

## 6. Khuyến nghị xử lý

1. Người giữ quyền sửa: sửa p000046, p000060, p000073, p000092, p000097, p000100 theo mục 3 sau khi người dùng duyệt quyết định thuật ngữ; đưa các đoạn bị ảnh hưởng về `draft` theo README bản dịch.
2. Người dùng quyết định: P03-section-manager (bảng chức danh), P05-being-x (tên gọi), P03-touchstone-award, P03-rationality, giọng Being X, xưng hô "anh" cho nhân vật nhân viên.
3. Ghi quyết định cho 17 mục đề nghị chốt vào `canon/decisions.md` (có thể gộp một mã `DEC-...`), rồi cập nhật `glossary.yml`; không chuyển bằng cách chép trực tiếp từ pending.
4. Không xử lý b06 trước khi hoàn tất mục 5 và hai điểm xưng hô ở mục 4.
