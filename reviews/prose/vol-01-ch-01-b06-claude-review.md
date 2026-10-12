# Báo cáo phản biện — vol-01-ch-01-b06

- Task: `vol-01-ch-01-b06-review` (reviewer: Claude)
- Phạm vi: 25 đoạn `YS-LN01/Text/chapter003b.xhtml/p000076`–`p000100` (viết tắt `pNNNNNN` bên dưới).
- Đầu vào đã đọc: source package cục bộ, `translations/vol-01/ch-01-b06.jsonl`, handoff dịch, `canon/*`, `work/run-state/pending-terms.yml`, `agents/*`, `config/translation-pipeline.yml`.
- Kiểm tra toàn vẹn: sha256 source package khớp handoff (`fdf507c3…18ce9`); `source_sha256` mỗi đoạn khớp (`7698e1b8…`); 25/25 đoạn có bản dịch, đúng thứ tự mã đoạn, `status: draft`.
- Không chép câu nguồn; chỉ dùng thuật ngữ ngắn và mã đoạn để nhận diện. Mọi thuật ngữ bên dưới là đề xuất, không phải canon.

## 1. Tổng quan

Bản dịch bám nghĩa tốt, giọng văn tự nhiên, giữ đúng ranh giới đoạn và các dấu hiệu định dạng: chữ nghiêng ở p000077 (cụm mở đầu nội tâm) và p000084 (từ "soldiers") khớp với nguồn; dấu chú thích ⁶ ở p000084 khớp quy ước ⁴/⁵ của các lô trước. Không phát hiện lỗi nghiêm trọng, không có quyết định canon ảnh hưởng cốt truyện cần hỏi người dùng.

Có **4 lỗi mức vừa** cần translator xử lý (tên địa danh bị đổi so với nguồn, hai thuật ngữ chính trị làm lệch lập luận, và một uyển ngữ bị làm mất tính mỉa mai) và **15 lỗi nhẹ**.

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 4 |
| Nhẹ | 15 |

## 2. Phát hiện mức vừa

**M1 — p000076 — địa danh bị đổi so với nguồn.** Dòng tiêu đề của nguồn ghi tên *Nordland* (đúng chính tả đó, xuất hiện trong package), nhưng bản dịch ghi "Norden". Ghi chú của translator nói dùng lại cách gọi "Norden" từ các đoạn trước, nghĩa là đã hài hòa hóa ngầm. Ledger chỉ có "mặt trận Norden", "Lãnh thổ Norden", "Norden Control"; chưa có mục nào ghi *Nordland = Norden*.
- Căn cứ: so sánh trực tiếp package b06; style-guide yêu cầu không tự đổi chi tiết, và tiền lệ Goliath-07 trong ledger là giữ nguyên chênh lệch nguồn, không hài hòa hóa.
- Đề xuất: giữ dạng nguồn "Nordland" (hoặc ghi rõ trong ledger là nghi vấn chênh lệch nguồn) cho đến khi coordinator đối chiếu với nguồn ở các lô trước (ngoài phạm vi review này). Không khẳng định hai tên là một.
- Độ tin cậy: 0,7 (chưa kiểm được các lô khác).

**M2 — p000084 — "pseudo-border" → "đường ranh giả" kèm "thực chất".** Có hai vấn đề.
1. "Đường ranh giả" đọc là "đường kẻ giả/không có thật". Nhưng p000089 khẳng định khu phi quân sự tạm thời *trên thực tế là biên giới quốc gia*. Hai đoạn tạo mâu thuẫn bề mặt. Ghi chú translator còn nói ý là "không phải đường biên thực chất", ngược với p000089.
2. "Thực chất là" ở đầu câu là chữ thêm, khẳng định mạnh hơn nguồn, nhấn đúng chiều đang gây mâu thuẫn ở trên.
3. Ngoài ra "đường ranh" tách khỏi "biên giới" ngay câu trước, làm mất liên hệ chữ nghĩa với từ "border".
- Đề xuất: bỏ "thực chất"; chọn cách gọi giữ hạt nhân "biên giới" và sắc thái "gần như/không chính thức", ví dụ "một dạng ‘biên giới’ không chính thức" (độ tin cậy 0,5). Phương án "biên giới trên danh nghĩa" của translator cũng ngược chiều với p000089 (danh nghĩa ≠ thực tế), nên không khuyến nghị. Không suy ra gì về lore ngoài nhận xét logic giữa p000084 và p000089.

**M3 — p000089 — "dominion" và "sovereignty" cùng thành "chủ quyền".** "Claim of dominion" ở p000089 và "sovereignty" ở p000091 đều được dịch "chủ quyền", làm mất phân biệt hai khái niệm trong cùng đoạn lập luận pháp lý–chính trị. Ở p000089 điều đó còn khiến người đọc hiểu hiệp ước *thừa nhận* chủ quyền Entente, trong khi câu nói hiệp ước chỉ "thể hiện tôn trọng tạm thời" (nhằm đến sự nhường nhịn). Cùng đoạn đã dùng "quyền quản lý" cho administrative rights nên có cơ sở tách bậc.
- Đề xuất: giữ "chủ quyền" riêng cho p000091 (sovereignty); ở p000089 dùng "quyền cai trị"/"quyền thống trị/cai quản" (độ tin cậy 0,55; phương án "quyền cai trị" đã có trong ledger).

**M4 — p000094 (so với p000090/p000092) — uyển ngữ "hiking" bị quân sự hóa.** p000090 và p000092 giữ "đi bộ đường dài" (đúng ý mỉa mai: hoạt động giải trí). Nhưng p000094 dịch thành "cuộc hành quân đi bộ đường dài", thêm "hành quân" không có trong nguồn, khiến lời phát ngôn viên gần với sự thật hơn và làm yếu tính uyển ngữ mà cả cụm p000090–p000094 dựa vào. Ghi chú nói "giữ nhất quán", nhưng thực tế có thêm từ. Từ "exercise" đứng cạnh "hiking" cũng chưa được dịch rõ ràng (bài tập/diễn tập).
- Đề xuất: "cuộc đi bộ đường dài có tổ chức chặt chẽ" hoặc "buổi diễn tập đi bộ đường dài…", giữ cụm "trong điều kiện áp lực" thống nhất ba chỗ. Tin cậy 0,7.
- Ghi chú thêm: "trong điều kiện áp lực" là cách dịch từng chữ của "under pressure", đọc gượng nhưng nhất quán; chưa đủ căn cứ để đổi (nghĩa gốc là "dưới áp lực" hay "trong tình huống căng thẳng" chưa rõ). Nên ghi vào ledger như thuật ngữ cần giữ thống nhất.

## 3. Phát hiện mức nhẹ

- **m1 — p000077.** Ba lệch nhỏ: (a) "cầu khẩn" mạnh hơn nghĩa "hỏi" trời cao; (b) "rám nắng" mất ý "snow-tanned" (rám/sạm vì tuyết); (c) "bộ binh mềm yếu" chuyển nghĩa vật lý "mềm, không giáp" (song song với xe không bọc giáp) sang đánh giá "yếu" — ghi chú nói giữ sắc thái khinh miệt nhưng nguồn chưa đến mức đó. Đề xuất: "hỏi trời cao"; "sạm nắng tuyết"; "bộ binh trần/không giáp". Tin cậy 0,6.
- **m2 — p000077, p000084, p000097.** "Imperial Army" dịch "Lục quân Đế quốc", trong khi ledger b03 dùng "Quân đội Đế quốc" (Bộ Tổng Tham mưu Quân đội Đế quốc, Quân đội Liên minh Entente). Chênh lệch tên cơ quan giữa các lô; "lục quân" còn gợi ngầm phân biệt với không quân. Đề xuất coordinator chọn một dạng cho cả chương; tin cậy 0,6.
- **m3 — p000078.** Câu đầu của lời thoại nghĩa là "điều này khác với những gì chúng tôi được báo", bản dịch thành "không ai báo chuyện này", chuyển từ bị báo sai sang không được báo. Đề xuất: "Chuyện này đâu giống những gì bọn tôi được nghe!" Tin cậy 0,6.
- **m4 — p000084.** (a) "waltz over" = bước qua thản nhiên/chủ quan, bản dịch "ngang nhiên" (ngạo mạn); (b) "ever-diligent" = chuyên cần, bản dịch "luôn cảnh giác"; (c) "they should have known" → "họ phải biết" mất tính phản thực tế (lẽ ra phải lường trước), trái quy tắc giữ giả định/thời gian của style-guide. Đề xuất: "cứ thản nhiên bước qua", "vốn luôn cần mẫn", "lẽ ra họ phải lường trước". Tin cậy 0,6.
- **m5 — p000085.** "Bureaucrats" → "Đồ quan liêu": "quan liêu" thường là tính từ/danh từ trừu tượng, còn ở p000088 "officials" → "quan chức". Chấp nhận được về khẩu ngữ nhưng nên đồng bộ: "Lũ công chức/quan chức chết tiệt…". Tin cậy 0,5.
- **m6 — p000086.** (a) "gap between classes" → "khoảng cách giai cấp" mang sắc thái Marx-xít không có trong nguồn; nên "khoảng cách giữa các tầng lớp"; (b) "các lực hướng tâm gây bất ổn" đọc như thuật ngữ vật lý và logic "lực hướng tâm → bất ổn" khó theo (xem mục thuật ngữ 4). Giữ nghĩa đen là chấp nhận được.
- **m7 — p000088.** Mất từ "mistake" ("lên án họ đã tiếp tục…" → thiếu "sai lầm"). Đề xuất: "lên án sai lầm của họ khi tiếp tục thổi bùng…". "Nguyền rủa" cho "curses" hơi nặng chất bùa chú, "chửi rủa" tự nhiên hơn.
- **m8 — p000089.** (a) "nhằm lưu tâm đến" biến "out of consideration for" (vì nể/vì chiếu cố) thành mục đích + "lưu tâm", nên "vì nể/chiếu cố đến yêu sách…"; (b) "buộc hai bên" suy ra đối tượng "them"; nguồn mơ hồ, nên cân nhắc giữ ngang mức mơ hồ.
- **m9 — p000091.** "Sore losers" → "kẻ thua cuộc" mất sắc thái cay cú; "chẳng ai coi họ là nghiêm túc" là calque, nên "chẳng ai thèm xem họ là nghiêm túc/coi trọng". "Dreamers" → "kẻ mơ mộng" nhẹ hơn nghĩa mỉa mai (cân nhắc "kẻ mơ mộng hão huyền").
- **m10 — p000094.** "Salary thief" → "tên ăn lương" mất ý "kẻ ăn lương mà vô dụng" (mất "thief/ăn hại"); "appallingly thoughtless" → "ngu xuẩn đến không thể chấp nhận" nặng hơn "thiếu suy nghĩ" và lặp "ngu xuẩn" của p000097. Đề xuất: "kẻ ăn hại lương" / "thiếu suy nghĩ đến mức kinh người".
- **m11 — p000097.** "Vượt biên" trong tiếng Việt thường chỉ việc trốn ra nước ngoài; với quân đội nên "vượt qua biên giới".
- **m12 — p000098.** (a) Viết hoa "Bộ phận Kiểm soát Không phận" khác dạng chữ thường của b01 ("bộ phận kiểm soát không phận"); nguồn viết hoa nhưng không có chữ "section/department", nên "Bộ phận" là phần thêm, và "Bộ" dễ đọc như cấp bộ; (b) "Combat Direction Center" → "Trung tâm Chỉ huy Tác chiến" làm "direction" thành "chỉ huy", trùng với "sở chỉ huy" (command centers) ngay trong câu; xem mục thuật ngữ 7–8.
- **m13 — p000099.** "Đường dây" gợi dây dẫn/điện thoại, trong khi ngữ cảnh là liên lạc vô tuyến; nên "đường liên lạc/kênh liên lạc". "Chưa được phân đúng tần số" (mới chưa) khác một chút so với "không được phân" (đã không). Tin cậy 0,5.
- **m14 — p000100.** "Cựu binh lão luyện" gợi người đã giải ngũ; ở đây là người đang tại ngũ. Dùng "lão luyện/kỳ cựu của bầu trời" (đã dùng "kỳ cựu" ở câu trước, tránh lặp "cựu binh").
- **m15 — p000077, p000088, p000098, p000096, p000100 — xưng hô chưa vào ledger.** Bản dịch dùng "ông" (trần thuật về Sue), "anh" (Sue gọi Cunningham ở p000098) và "ngài" (Cunningham gọi Sue ở p000096). Các lựa chọn hợp lý nhưng chưa có mục ledger/ghi chú; "ông" ngầm suy ra tuổi. Đề xuất coordinator ghi như lựa chọn tạm, không nâng canon; phương án trung tính: lặp "Sue" hoặc lược chủ ngữ. Tin cậy 0,6. Cũng nên ghi "Command" gọi ở p000083 → "Bộ chỉ huy" là cách gọi tạm.

## 4. Đánh giá chín thuật ngữ tạm

Mọi mục dưới đây khớp ghi chú translator và `pending-terms.yml`; đều là đề xuất, không canon, và không có mục nào cần hỏi người dùng.

| # | Thuật ngữ | Hiện tại | Khuyến nghị tạm | Tin cậy | Ghi chú |
|---|---|---|---|---|---|
| 1 | aerial mage (p000077) | pháp sư không quân | Giữ; thay thế "pháp sư trên không" | 0,65 | Nhất quán với b01/p000004. Rủi ro: "không quân" gợi một quân chủng riêng; nên ghi vào ledger để rà khi có ngữ cảnh tổ chức. |
| 2 | smoke screen (p000080) | màn khói | Giữ | 0,8 | Chuẩn quân sự; "dựng" chấp nhận được, có thể "tung/thả màn khói". |
| 3 | pseudo-border (p000084) | đường ranh giả | **Đổi** (xem M2): "một dạng ‘biên giới’ không chính thức" | 0,5 | Phải tương thích với p000089; tránh "giả/danh nghĩa" nếu p000089 giữ "trên thực tế". |
| 4 | centripetal forces (p000086) | các lực hướng tâm | Giữ nghĩa đen; thay thế "lực kéo về trung tâm" | 0,55 | Ẩn dụ chính trị (hướng tâm vừa gây bất ổn) khó theo với người Việt; nguồn dùng đúng từ này nên không sửa nghĩa. Nếu cần xác minh ý tác giả phải có nguồn được phép, chưa suy diễn ở đây. |
| 5 | exclusionism (p000086) | chủ nghĩa bài ngoại | Giữ; thay thế "chủ nghĩa loại trừ" | 0,6 | Hợp ngữ cảnh đối đầu với Đế quốc; nhưng có thể hẹp hơn nghĩa gốc (loại trừ nhóm khác). |
| 6 | dominion (p000089) | chủ quyền | **Đổi** (xem M3): "quyền cai trị/thống trị" | 0,55 | Giữ "chủ quyền" cho sovereignty (p000091). |
| 7 | Airspace Control (p000098) | Bộ phận Kiểm soát Không phận | Giữ chức năng; đồng bộ chữ hoa/thường với b01, cân nhắc bỏ "Bộ phận" | 0,6 | Tên chức năng, chưa rõ có phải đơn vị cố định không. |
| 8 | Combat Direction Center (p000098) | Trung tâm Chỉ huy Tác chiến | Tạm giữ hoặc "Trung tâm Điều hành Tác chiến"; thay thế của translator "Điều hành Chiến đấu" | 0,5 | Phương án có "Điều hành" giữ "direction" và tránh trùng "chỉ huy" với "command centers". Chưa đủ căn cứ để chọn dứt khoát. |
| 9 | First Lieutenant (p000100) | trung úy | **Giữ**; không dùng "thiếu úy" | 0,85 | "Thiếu úy" đã dùng cho Second Lieutenant (b01/b02); "trung úy" cho First Lieutenant, "trung tá" cho Lieutenant Colonel cho thang cấp bậc nhất quán, không va chạm. Không ảnh hưởng cốt truyện; vẫn chỉ là đề xuất. |

Các ẩn dụ/chính trị p000084–p000089: ngoài các điểm M2/M3, "khu phi quân sự tạm thời" nhất quán giữa p000084 và p000089, "Khối Thịnh vượng chung" khớp b03, "quan chức/chính khách/phát ngôn viên" phân biệt được. Đề xuất ghi vào ledger thêm: "Hiệp ước Londinium", "khu phi quân sự tạm thời", "đi bộ đường dài trong điều kiện áp lực", Nordland/Norden (M1).

## 5. Rủi ro còn lại

- M1 phụ thuộc đối chiếu nguồn ở các lô trước (ngoài phạm vi), cần coordinator.
- M2–M4 cần translator (người giữ quyền sửa) áp dụng; sau đó nên chạy validator.
- Dùng "Lục quân Đế quốc" khác ledger b03; cần chốt tên cơ quan nhất quán trước các lô sau.
- Chưa thể xác nhận nghĩa nguyên bản của "centripetal" vì không có tài liệu ngoài nguồn; giữ nghĩa đen là lựa chọn ít suy diễn nhất.
- Validator và diff_check: **chưa chạy** (not_run). Commit: null.
