# Quyết định tạm cho các mục pending — vol-01 Chapter 0 (b02–b05)

Người phản biện: Claude. Task: `vol-01-ch-00-pending-decisions-review`. Báo cáo không chép câu nguồn; chỉ dùng mã đoạn và thuật ngữ nguyên gốc ngắn để nhận diện. Mã đoạn viết tắt `pNNNNNN`, tiền tố đầy đủ `YS-LN01/Text/chapter001.xhtml/`.

Đầu vào đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, handoff, `work/run-state/pending-terms.yml`, `canon/*` (glossary và characters vẫn rỗng; decisions chỉ có DEC-P01-001/002), bốn báo cáo Claude liên quan, bản dịch b02–b05 và gói nguồn b02–b05 (đọc tại chỗ).

**Tính chất của báo cáo:** mọi lựa chọn dưới đây là **phương án tạm theo chính sách tự động hóa** (AGENTS.md), **không phải canon**, không tự nâng thành quyết định đã duyệt và không thay `canon/decisions.md`. Báo cáo không sửa bản dịch, canon, handoff hay sổ pending. Validator/diff_check: not_run; commit: null.

Thang tin cậy: **cao** ≥ 0,75; **vừa** 0,5–0,74; **thấp** < 0,5. Với mục thấp tôi chọn dạng trung tính/literal ít suy diễn nhất.

## 1. Tóm tắt

- Không có hard stop. Không mục nào làm đổi cốt truyện; mục gần nhất là tên gọi và vai trò của Being X, nhưng phương án tạm (giữ nguyên "Being X", không khẳng định bản chất thực thể) không thay đổi cốt truyện, nên không dừng.
- Chốt tạm 38 mục (xem mục 2 và 4). Cần chỉnh bản dịch ở 3 chỗ: p000086 (xưng hô), p000076 (xưng hô số nhiều), p000094 (reborn). Ngoài ra p000140 và chapter003b p000016 có mặt trong sổ pending nhưng nằm ngoài gói đầu vào được giao, tôi chưa đối chiếu.
- Mức độ: nghiêm trọng 0, vừa 1 (p000086), nhẹ 4 (p000076, p000094 reborn, thiếu tham chiếu ledger, thiếu mục pending cho lore nền).
- 9 mục "inherited, chưa liệt kê" trong sổ pending không thể dựng lại từ đầu vào được giao; tôi quyết định toàn bộ mục đã liệt kê cộng mục trong `canon/glossary-pending.yml` (mục 4). Coordinator nên đối soát 9 mục còn lại với mục 4 trước khi coi sổ đã đủ.

## 2. Bảng quyết định cho các mục ưu tiên

| # | Mục | Phương án tạm chọn | Tin cậy | Phương án thay thế | Mã đoạn |
|---|---|---|---|---|---|
| 1 | Người nói + xưng hô p000086 | Người nói là **Being X**; đổi "Ông" thành **"Ngươi"** | cao (0,8) | giữ "Ông" (người kể nói) | p000084, p000085, p000086, p000087 |
| 2 | Ngôi ba cho người đàn ông trưởng thành | **"anh"** (tự sự ngôi ba), **"tôi"** (ngôi một, b04) | cao (0,8) | "ông ấy" / "người ấy" | p000043, p000045, p000046, p000055 (+ p000044, p000047–p000054) |
| 3 | rationality | Nghĩa kinh tế: họ **"hợp lý"** (tính hợp lý / hợp lý / bất hợp lý); nghĩa phẩm chất cá nhân ở b02: **"lý trí"** | vừa (0,55) | một từ duy nhất "tính duy lý / duy lý / phi duy lý" cho cả ba | p000029, p000046, p000096 |
| 4 | Chicago school | **"trường phái kinh tế Chicago"** (lần đầu, kèm ¹); nhắc lại có thể rút gọn "trường phái Chicago" | cao (0,8) | "trường phái Chicago" | p000046 |
| 5 | section manager | **"trưởng phòng"**, kèm quy tắc kèm theo (mục 3.5) | vừa (0,5) | "trưởng bộ phận", "quản lý bộ phận" | p000055 (+ p000069, p000073, p000146) |
| 6 | touchstone award | **"giải Touchstone"**, giữ nguyên tên, không giải nghĩa | vừa (0,55) | "giải thưởng “Touchstone”" (ngoặc kép) | p000055 |
| 7 | Being X: tên | Giữ **"Being X"** (không Việt hóa) | cao (0,8) | "Thực thể X", "Tồn tại X" | p000087, p000094, p000101 (+ p000083, p000098, p000100) |
| 8 | Being X: giọng | Thoại: **ta / ngươi / các ngươi**; người kể gọi **"ông ta"**; người kể nói với Being X: **"tôi – ông"** | vừa-cao (0,7) | "tôi / ông" hai chiều (bỏ giọng trịch thượng) | p000082, p000086, p000088, p000090, p000094, p000097, p000100 |
| 9 | cash advance loan | **"vay tiền mặt"** (động từ), **"khoản vay tiền mặt"** (danh từ); không dùng "ứng lương" | vừa (0,6) | "khoản vay ứng lương" | p000060 |
| 10 | PIP | Giữ **"PIP"**, không khai triển, không tự chèn chú thích | cao (0,8) | "chương trình cải thiện hiệu suất" kèm chú thích | p000062 |
| 11 | pink slip | **"giấy sa thải"** | vừa (0,65) | "giấy thôi việc", "thông báo sa thải" | p000073 |
| 12 | God | **"Thượng đế"**, đại từ **"ngài"** khi chủ ngữ là God trong lập luận | vừa (0,65) | "Chúa", "Trời" | p000087, p000094, p000101 |
| 13 | Creator | **"Đấng Tạo Hóa"** | vừa (0,6) | "Đấng Sáng Tạo" | p000088 (+ p000094, p000101; p000138 ngoài gói) |
| 14 | devil | **"quỷ dữ"** | vừa (0,6) | "ác quỷ" | p000085, p000087 |
| 15 | disbelievers | **"kẻ vô tín"** (số nhiều: "những kẻ vô tín") | vừa (0,6) | "kẻ không có đức tin" | p000084, p000088, p000089 |
| 16 | reborn | **"tái sinh"** | vừa (0,55) | "đầu thai" (đang dùng) | p000094 (+ p000140, chapter003b p000016 ngoài gói) |

## 3. Chi tiết, căn cứ và lựa chọn thay thế

### 3.1. p000086 — người nói và xưng hô (mục 1, 8)

- **Chọn:** người nói là Being X; chuyển đại từ ngôi hai thành "ngươi". Chỉ đổi đại từ mở đầu, phần còn lại giữ nguyên.
- **Căn cứ (chỉ từ gói nguồn):**
  1. p000083 nêu rằng Being X đọc được suy nghĩ; p000084 là lời Being X xác nhận. p000085 là câu người kể nói thành lời (trong ngoặc kép) về việc quỷ dữ có thật. p000086 là lượt luân phiên kế tiếp, tức vị trí của Being X, và có dạng phản ứng bác bỏ/chê ý nghĩ vừa được nói ra.
  2. p000087 sau đó là lập luận nội tâm của người kể dẫn tới kết luận "Being X là quỷ dữ" và không có lời dẫn nào chuyển người nói của p000086 sang người kể.
  3. Giọng Being X đã nhất quán "ta/ngươi" ở p000088, p000090, p000094, p000097, p000100 sau lượt sửa b05.
- **Thay thế:** nếu người nói là người kể thì "ông" đúng. Cách này kém phù hợp vì bắt người kể bác bỏ chính điều mình vừa nói thành lời.
- **Bất định còn lại:** nguồn không có nhãn người nói; tôi không có bản đối chiếu bên ngoài. Tin cậy 0,8.
- **Kết quả:** coordinator có thể đóng mục `speaker-attribution-p000086` với trạng thái "tạm chọn Being X, đề xuất, chưa canon".

### 3.2. "anh" ngôi ba cho người đàn ông trưởng thành (mục 2)

- **Chọn:** giữ "anh" cho tự sự ngôi ba ở b03 (p000043–p000055), và "tôi" cho cùng nhân vật khi kể ngôi một ở b04 (p000067–p000073). Nguồn dùng đại từ nam ở ngôi ba nên không phải suy diễn giới tính; đại từ này không áp lên Tanya (vẫn theo DEC-P01-001: "nó"/"mình").
- **Ranh giới:** quy ước chỉ áp dụng cho nhân vật này, trong đoạn tự sự về đời trước. Không suy ra tuổi, quan hệ hay cấp bậc từ "anh"; không dùng "anh" cho các nhân vật khác (giám đốc ở p000073 gọi "ông ấy" theo đại từ nam của nguồn).
- **Thay thế:** "ông ấy"/"người ấy". "Hắn" hay "gã" thêm sắc thái khinh, không chọn.
- **Tin cậy:** 0,8.

### 3.3. rationality — nhất quán (mục 3)

- **Vấn đề:** cùng một thuật ngữ nguồn đang được dịch khác nhau ("lý trí" ở b02 p000029; "tính hợp lý" ở b03 p000046; "hợp lý/bất hợp lý" ở b05 p000096).
- **Chọn:**
  - Nghĩa **kinh tế/lựa chọn duy lý** (p000046, p000096): họ "hợp lý": danh từ "tính hợp lý", tính từ "hợp lý" / "bất hợp lý". Đúng cho cả p000046 (áp dụng vào quan hệ quy tắc–tự do) và p000096 (hai kiểu người trong kinh tế học hành vi).
  - Nghĩa **phẩm chất của một con người** trong bộ ba cùng sensibility và personality (p000029): "lý trí".
- **Căn cứ:** hai ngữ vực khác nhau (thí nghiệm tâm lý–xã hội so với kinh tế học); gộp một từ buộc phải chọn giữa "lý trí" (lạ trong p000046, p000096) và "tính hợp lý" (lạ trong bộ ba tính cách). Tách theo nghĩa giữ được tính tự nhiên và vẫn nhất quán trong từng nghĩa.
- **Quy tắc đi kèm:** không dùng "lý trí" cho "logic" ở p000073 (đang dùng "lý lẽ", giữ nguyên); không dùng "tính hợp lý" cho bộ ba ở p000029.
- **Thay thế:** một từ duy nhất "tính duy lý / duy lý / phi duy lý" cho cả ba chỗ (cần sửa p000029, p000046, p000096).
- **Tin cậy:** 0,55. Rủi ro nhẹ, không đổi cốt truyện. Ghi trong ledger rằng đây là hai nghĩa tách, để translator ở b06+ không nhầm.

### 3.4. Chicago school (mục 4)

- **Chọn:** "trường phái kinh tế Chicago" ở lần đầu (p000046, đã khớp bản dịch), kèm dấu ¹. Các lần nhắc lại có thể rút gọn "trường phái Chicago" khi mạch đã rõ là kinh tế.
- **Căn cứ:** chú thích ¹ trong nguồn xác định đây là trường phái kinh tế; báo cáo gộp ghi nhận chapter sau cũng nêu rõ lĩnh vực. Bản dịch hiện tại khớp phương án này. Lưu ý: `canon/glossary-pending.yml` vẫn ghi "trường phái Chicago" (phương án cũ), còn ledger `pending-terms.yml` ghi dạng mới; đề nghị đồng bộ ghi chú, không đổi bản dịch.
- **Tin cậy:** 0,8.

### 3.5. section manager và hệ chức danh (mục 5)

- **Chọn:** "trưởng phòng" cho "section manager" (p000055). Giữ "giám đốc nhân sự" cho "director of human resources" (p000069, p000073, p000146), với p000073 "the director" là cùng người theo báo cáo gộp.
- **Căn cứ:** thứ bậc trong nguồn: nhân viên → section manager (p000055) → director of HR (p000069 coi đó là mức thăng tiến kế tiếp). "Trưởng phòng" là cách dịch phổ biến cho cấp quản lý trung gian này và thấp hơn "giám đốc".
- **Quy tắc đi kèm để tránh đảo bậc:** (a) "department" ở p000055 vẫn dịch "bộ phận nhân sự", không dịch "phòng nhân sự"; (b) "restructuring departments" ở p000069 dịch chung "phòng ban"; (c) không dùng "trưởng bộ phận" cho bất kỳ chức danh nào khác trong cảnh này; (d) "supervisor" (p000060) là "cấp trên trực tiếp" như hiện tại.
- **Thay thế:** "trưởng bộ phận" (cần đổi "bộ phận nhân sự" thành "phòng nhân sự"); "quản lý bộ phận".
- **Tin cậy:** 0,5. Không đổi cốt truyện. Nếu sau này xuất hiện thêm "division", "department head", cần bảng chức danh riêng, chưa có đủ căn cứ ở chương này.

### 3.6. Touchstone (mục 6)

- **Chọn:** giữ "giải Touchstone", không giải nghĩa thành "đá thử vàng" hay "thước đo".
- **Căn cứ:** xuất hiện một lần, không có chú thích; nguồn viết thường. Dịch nghĩa sẽ khẳng định điều chưa có căn cứ. Giữ nguyên thuật ngữ và không bổ sung thông tin là phương án ít suy diễn nhất, mặc dù viết hoa mặc định đây là tên riêng (đây là điểm bất định còn lại).
- **Thay thế:** "giải thưởng “Touchstone”" trong ngoặc kép.
- **Tin cậy:** 0,55.

### 3.7. Being X: tên và giọng (mục 7, 8)

- **Tên:** giữ "Being X". Việt hóa là quyết định tên gọi; "X" là nhãn do người kể đặt (p000087). Giữ nguyên Latin có chi phí thay thế thấp và không khẳng định bản chất. Không thêm bản dịch như "Thực thể X" trừ khi có quyết định canon.
- **Giọng:** thoại của Being X dùng ta/ngươi/các ngươi (p000082, p000086, p000088, p000090, p000094, p000097, p000100). Người kể gọi "ông ta" trong lời kể (p000083, p000089, p000094, p000098, p000100) và "kẻ tự xưng" ở p000094, p000101. Người kể nói trực tiếp với Being X dùng "tôi – ông" (p000077, p000085, p000091, p000095).
- **Giới hạn suy diễn:** không dùng giọng "ta/ngươi" để gán thêm nghĩa thần thánh hay cấp bậc; người kể gọi "kẻ tự xưng là Thượng đế" là điểm nhìn của người kể, không phải xác nhận.
- **Thay thế:** xưng hô hai chiều "tôi – ông".
- **Tin cậy:** 0,8 (tên), 0,7 (giọng).

### 3.8. cash advance, PIP, pink slip (mục 9, 10, 11) và xưng hô trực tiếp ở b04

- **cash advance loan (p000060):** chọn "vay tiền mặt", không khẳng định nguồn tiền hay quan hệ với lương. Hiện `canon/glossary-pending.yml` ghi "khoản vay ứng lương" và ledger ghi "khoản vay tiền mặt"; đồng bộ cả hai theo phương án này (và dùng "khoản vay tiền mặt" khi cần danh từ). Tin cậy 0,6.
- **PIP (p000062):** giữ nguyên, không khai triển. Tin cậy 0,8.
- **pink slip (p000073):** chọn "giấy sa thải". "Thôi việc" bao cả tự nguyện, trong khi p000062 đối lập "tự nguyện xin nghỉ" với "sa thải kỷ luật". Tin cậy 0,65.
- **Xưng hô trực tiếp với nhân viên bị sa thải (p000060, p000061, p000062, p000065, p000066):** giữ cấu trúc trung tính ("nhân viên", lược chủ ngữ, "chúng tôi"); không dùng "anh/chị" vì nguồn chỉ có "you" và nhân viên bị sa thải không có căn cứ về giới tính hay quan hệ. Tin cậy 0,75. Mục `direct-address choice` trong ledger nên bỏ p000073 (không có xưng hô trực tiếp).

### 3.9. God, Creator, devil, disbelievers, reborn (mục 12–16)

Ngữ cảnh chung: lập luận của người kể (p000087) về Thượng đế/quỷ dữ và lời than của Being X (p000088, p000090, p000094, p000100) có tính triết học/thần học tổng quát, không gắn riêng tôn giáo nào.

- **God → "Thượng đế":** trung tính hơn "Chúa" (gắn Kitô giáo) và hơn "Trời" (gắn dân gian). Đại từ "ngài" khi God là chủ ngữ (p000087). Tin cậy 0,65.
- **Creator → "Đấng Tạo Hóa":** viết hoa như danh xưng, đi cùng God. Ở p000088, "Creator của các ngươi" có vẻ chỉ chính người nói, nhưng chưa đủ căn cứ để xác định; giữ literal "Đấng Tạo Hóa của các ngươi" và không nêu ai là Đấng Tạo Hóa. Tin cậy 0,6.
- **devil → "quỷ dữ":** nghĩa chung. Các chương sau có danh xưng riêng chứa "devil"; không khóa chung với danh xưng đó, quyết định riêng khi gặp. Tin cậy 0,6.
- **disbelievers → "kẻ vô tín":** giữ sắc thái từ ngữ cực đoan của Being X, khớp "không có đức tin" ở p000100. p000089 dựa vào số nhiều: giữ "những kẻ vô tín". Tin cậy 0,6.
- **reborn → "tái sinh":** literal hơn "đầu thai" (thu hẹp theo tín ngưỡng dân gian, và chỉ rõ quá trình vào bụng mẹ). Phù hợp "vòng sinh tử" và "kiếp sau" (p000096). **Cần đổi p000094 từ "đầu thai" sang "tái sinh"**. Nếu coordinator không muốn đổi bản dịch đã có, "đầu thai" là phương án thay thế chấp nhận được miễn là dùng nhất quán. Tin cậy 0,55.
- **Ledger:** các mục `review-God`, `review-Creator`, `review-devil`, `review-disbelievers`, `review-reborn` đã có; đề nghị cập nhật `proposed_vi` của `review-reborn` thành "tái sinh".

## 4. Các mục còn lại trong ledger và `glossary-pending.yml`

| Mã | Phương án tạm | Tin cậy | Thay thế | Mã đoạn |
|---|---|---|---|---|
| P03-paradigm-shift | chuyển đổi mô thức | vừa (0,65) | thay đổi hệ hình | p000043 |
| P03-moratorium | quãng tạm hoãn | vừa (0,5) | giai đoạn chờ trước khi vào đời | p000047 |
| P03-human-capital | vốn con người | cao (0,8) | vốn nhân lực | p000047 |
| P03-signaling-theory | lý thuyết tín hiệu | cao (0,8) | — | p000047 |
| P04-cost-performance | hiệu quả chi phí | vừa (0,7) | — | p000060, p000069 |
| P04-occupational-physician | bác sĩ y tế lao động | vừa (0,65) | bác sĩ y học lao động | p000060 |
| review-director-of-human-resources | giám đốc nhân sự | cao (0,75) | — | p000069, p000073, p000146 |
| P05-delusion | ảo tưởng (nghĩa thường, không ép về thuật ngữ tâm thần học) | vừa (0,6) | hoang tưởng | p000080 |
| P05-hallucination | ảo giác | vừa-cao (0,7) | — | p000080 |
| P05-enlightenment | giác ngộ | vừa (0,7) | khai sáng (loại: nghĩa tâm linh) | p000090, p000100 |
| P05-rawls-theory-of-justice | lý thuyết công lý của Rawls (giữ ²) | cao (0,8) | — | p000092 |
| P05-haves-have-nots | người có của và người tay trắng | vừa (0,65) | — | p000092 |
| P05-cycle-of-life-and-death | vòng sinh tử (thống nhất p000094, p000100; tránh "luân hồi") | vừa (0,7) | vòng luân hồi | p000094, p000100 |
| P05-behavioral-economics | kinh tế học hành vi | cao (0,85) | — | p000096 |
| P01-authority | quyền uy | vừa (0,55) | thẩm quyền | p000029 |
| P01-obedience-to-authority | sự phục tùng quyền uy | vừa (0,55) | sự tuân phục quyền uy | p000029 |
| P01-sensibility | khả năng cảm nhận (literal, tránh "cảm tính" vì thêm sắc thái) | thấp (0,45) | cảm tính | p000029 |
| P01-personality | tính cách | vừa (0,6) | — | p000029, p000030 |
| P01-individual-disposition | khuynh hướng cá nhân | vừa (0,55) | khuynh hướng riêng | p000029, p000030 |
| P01-moral-character | phẩm chất đạo đức | vừa (0,65) | — | p000029–p000031 |
| P01-deindividuation | sự phi cá nhân hóa | vừa (0,5) | sự mất cá tính | p000029 |

Ghi chú: các mục P01 tôi chỉ đánh giá theo b02 p000029–p000031 đã đọc; không đào sâu ngoài phạm vi.

## 5. Việc cần làm sau báo cáo (đề xuất cho coordinator/translator)

1. Translator (khi nhận quyền sửa): p000086 đổi "Ông" thành "Ngươi"; p000076 xem lại "các người" theo đề xuất bên dưới; p000094 đổi "đầu thai" thành "tái sinh" (nếu áp dụng mục 3.9). Các đoạn đã sửa quay về `draft`.
2. **p000076 (nhẹ):** nguồn là ngôi hai số nhiều, nội dung hỏi bản chất; "các người" thô hơn so với "ông" ở p000077. Đề xuất tạm trung tính: "các vị". Thay thế: lược đại từ, hoặc giữ "các người". Tin cậy 0,45 (thấp); nếu coordinator ngại sửa, giữ nguyên vì không đổi cốt truyện.
3. Coordinator cập nhật ledger: bổ sung p000100 cho `P05-enlightenment` và `P05-cycle-of-life-and-death`; thêm `P03-rationality` ghi chú hai nghĩa; đồng bộ `P03-Chicago-school`, `P04-cash-advance-loan`, `P04-pink-slip` giữa `pending-terms.yml` và `glossary-pending.yml`; bỏ p000073 khỏi `direct-address choice`; chốt `speaker-attribution-p000086` theo mục 3.1. Đối soát 9 mục inherited chưa liệt kê.
4. Không đưa mục nào vào `glossary.yml` hay `characters.yml`; các lựa chọn vẫn là đề xuất, đến khi có quyết định ghi vào `canon/decisions.md`.
5. Chạy validator và `git diff --check` sau khi translator sửa, trước khi commit.

## 6. Rủi ro và bất định

- Căn cứ của p000086 chỉ dựa vào mạch trong gói nguồn; không có nhãn người nói tường minh.
- "Section manager" và "touchstone award" là hai mục tin cậy thấp nhất (0,5–0,55); nếu sau này có thêm chức danh hoặc chú thích, cần xét lại.
- P000138, p000140, p000146, p000131 và chapter003b p000016 xuất hiện trong ledger hoặc báo cáo cũ nhưng nằm ngoài gói đầu vào này; các quyết định áp dụng cho chúng chỉ dựa trên báo cáo cũ và chưa được đối chiếu trực tiếp.

```yaml
role: reviewer
task_id: vol-01-ch-00-pending-decisions-review
state: done
review_path: reviews/prose/vol-01-ch-00-pending-decisions-claude.md
segment_ids: [p000029, p000030, p000031, p000043, p000045, p000046, p000047, p000055, p000060, p000061, p000062, p000065, p000066, p000069, p000073, p000076, p000080, p000083, p000084, p000085, p000086, p000087, p000088, p000089, p000090, p000092, p000094, p000096, p000097, p000100, p000101]
files_written: [reviews/prose/vol-01-ch-00-pending-decisions-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 1, minor: 4}
unresolved_findings: [p000086 xưng hô chờ translator áp dụng, p000076 "các người" (tin cậy thấp), p000094 reborn "đầu thai" thành "tái sinh", ledger thiếu tham chiếu p000100, 9 mục inherited chưa liệt kê]
term_recommendations: [P03-rationality, P03-Chicago-school, P03-section-manager, P03-touchstone-award, P05-being-x, P04-cash-advance-loan, P04-pip, P04-pink-slip, review-God, review-Creator, review-devil, review-disbelievers, review-reborn, speaker-attribution-p000086, choice-adult-male-third-person]
risks: [section manager và touchstone tin cậy thấp, không có nhãn người nói ở p000086, một số đoạn ledger nằm ngoài gói đầu vào]
commit: null
next_action: coordinator cập nhật ledger và giao translator áp dụng các chỉnh sửa; sau đó chạy validator
```
