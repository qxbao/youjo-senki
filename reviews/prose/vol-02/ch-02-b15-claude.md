# Báo cáo phản biện — vol-02-ch-02-b15 (Claude)

- Task: `vol-02-ch-02-b15`; checkpoint_generation 397; vai trò: reviewer (nghĩa, văn phong, thuật ngữ).
- Phạm vi: 25 đoạn `YS-LN02/Text/part0014.xhtml/p000392`–`p000416`.
- Đầu vào đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b15, gói nguồn b15, `translations/vol-02/ch-02-b15.jsonl`, `canon/` (decisions, style-guide, glossary, characters, glossary-pending) và các mục pending liên quan trong `work/run-state/pending-terms.yml`. Không đọc gói nguồn hay bản dịch của lô khác.
- Kiểm tra hash: SHA-256 gói nguồn tính được `8828a7b9…1d7` **khớp** handoff. 25/25 đoạn có đủ, đúng thứ tự, `source_sha256` và `glossary_version` trong bản dịch khớp handoff. Không thiếu/thừa đoạn.
- Nhấn mạnh (DEC-P01-002): nguồn chỉ có một vùng nhấn mạnh (`p000408`); bản dịch dùng `*...*` đúng một lần ở đoạn này, đúng phạm vi. Không có dấu `*` thừa. Đạt.
- Tóm tắt: không có lỗi nghiêm trọng; không bỏ sót hay thêm ý lớn; thoại và chuỗi kế hoạch tác chiến (p000406, p000413–p000416) giữ đúng logic. Có 2 vấn đề mức vừa (nhất quán thuật ngữ "Control"; đại từ/tự xưng theo DEC-P01-001) và 10 mục nhẹ.

## Phát hiện

### Mức vừa

**F01 — `p000393`, `p000394`, `p000395` (và đối chiếu `p000396`, `p000397`, `p000398`, `p000400`): dạng rút gọn "Control" bị dịch thành "Bộ chỉ huy".**
- Vấn đề: `p000393` giữ tên riêng "Norden Control", nhưng ngay câu sau và ở `p000394`–`p000395` dạng rút gọn "Control" (cả của ta lẫn "Enemy Control") được dịch là "Bộ chỉ huy / Bộ chỉ huy địch". Người đọc khó nhận ra đây vẫn là cùng thực thể với Norden Control. Cùng lúc, cụm "Bộ chỉ huy" còn là phương án tạm cho "Command" (radio address) ở ledger b06, và "bộ chỉ huy địch" (chữ thường, nghĩa chung) ở `p000400`, "hệ thống chỉ huy" ở `p000396`; "CP" giữ nguyên ở `p000397`–`p000398`. Năm khái niệm nguồn khác nhau bị dồn vào một hoặc hai từ Việt.
- Căn cứ: ledger b05 (dạng rút gọn "Control" → "Norden Control", lý do tránh nhầm với thuật ngữ kiểm soát không phận), ledger b08 (độ tin cậy 0.8, nhất quán với chương trước), ledger b06 (Command → Bộ chỉ huy). Chưa canon.
- Đề xuất (tạm): ở `p000393`–`p000395` dùng nhất quán "Control" khi là dạng rút gọn (ví dụ "một cuộc chiến không có Control", "Control của địch đã bị loại bỏ"); giữ "bộ chỉ huy địch" (chữ thường, nghĩa chung) ở `p000400` vì nguồn dùng chữ thường; giữ "CP" ở `p000397`–`p000398`. Phương án thay thế: giữ "Bộ chỉ huy" nhưng khi đó nên ghi rõ trong ledger rằng nó ánh xạ cả Control lẫn Command và chấp nhận mất liên kết với tên "Norden Control". Độ bất định: nguồn tự dùng cả "Control" lẫn "CP" cho chức năng gần nhau; không đủ căn cứ để hợp nhất chúng.

**F02 — `p000396` ("cô"), `p000401` ("Theo tôi thấy"), `p000414` ("tôi" xuyên suốt): đại từ/tự xưng lệch DEC-P01-001.**
- `p000396`: trần thuật dùng "cô" cho "she". Nếu chủ thể là Tanya (rất có khả năng: đoạn liền sau lời báo cáo "Pixie 01"), DEC-P01-001 yêu cầu "nó" trong trần thuật, như `p000405`. Trong lô này không có ngữ cảnh khẳng định chủ thể của câu, nên giữ độ bất định: nếu là Tanya → "nó"; nếu là người khác thì không suy diễn quan hệ.
- `p000401` ("I've noticed") và `p000414` (cả đoạn, kể cả câu cuối): nội tâm tự quy chiếu của Tanya dịch là "tôi", trong khi `p000402`–`p000403`, `p000407`–`p000412`, `p000416` dùng "mình". Cùng một mạch nội tâm đổi tự xưng giữa chừng.
- Đề xuất: `p000396` → "nó" (nếu xác nhận chủ thể); `p000401`, `p000414` → "mình". Không thay đổi các đoạn thoại (`p000395`, `p000398`, `p000406`, `p000413`, `p000415`).

### Mức nhẹ

**F03 — `p000393`.** (a) "crude dogfight" dịch "màn quần thảo thô bạo": "thô bạo" gợi bạo lực/hung hãn; nguồn nói về sự sơ sài, thiếu tổ chức → "thô sơ"/"lộn xộn". (b) "vẫn nhận được" thêm "vẫn" không có trong nguồn (nguồn chỉ nói đang nhận chỉ đạo tối thiểu); bỏ "vẫn".

**F04 — `p000396`.** "ném bom dồn dập" cho đợt tấn công bằng pháo kích/thuật thức của pháp sư: "ném bom" gợi thả bom từ máy bay, dễ nhầm với máy bay ném bom ở `p000399`–`p000403`. Đề xuất "dội/tung ra một đợt pháo kích" hoặc "oanh tạc" (trung tính); không tự suy diễn phương thức cụ thể ngoài nguồn.

**F05 — `p000405`.** (a) Nguồn nói Tanya sẵn lòng *giữ giả thuyết* rằng Being X là ác; "vẫn cho rằng" biến giả thuyết thành niềm tin → "vẫn giữ giả thuyết rằng…". (b) "blue ocean" được diễn giải thành "không có đối thủ cạnh tranh": đúng nghĩa thuật ngữ kinh doanh nhưng mất phép ẩn dụ; cân nhắc "đại dương xanh" hoặc giữ cách diễn giải hiện tại nếu coi là phương án tạm (đề xuất, không bắt buộc). (c) "Hiếm khi" cho "For once" khá gần; có thể "lần này hiếm hoi".

**F06 — `p000407`.** "Chúng ta có lý do chính đáng để hành động" đổi câu phủ định kép ("không thiếu lý do cần thiết") và thêm sắc thái chính đáng/đạo lý (style-guide: không thêm sắc thái đạo đức). Đề xuất: "Chúng ta không thiếu lý do cần thiết để hành động." Cũng lưu ý "Chúng ta" lẫn trong mạch "mình"; có thể giữ vì nguồn dùng "we".

**F07 — `p000410`.** "thuế má tuy cũng là một thứ tội ác": "tội ác" mạnh hơn "evil" và mang nghĩa phạm pháp; mạch sau là "chuộc lỗi" (atone) nên cần giữ phép nói quá nhẹ. Đề xuất: "một dạng điều ác/điều xấu".

**F08 — Đại từ chỉ địch và lời gọi.** `p000399` ("Hai đại đội đang bảo vệ họ") và `p000414` ("xem họ đối phó với cấp dưới của mình") dùng "họ" cho địch, trong khi `p000399` câu sau, `p000401` dùng "chúng"; ở `p000414` "họ" dễ bị đọc nhầm là cấp dưới. Đề xuất "chúng"/"bọn chúng" nhất quán. `p000398`: "các anh" gán giới/quan hệ cho nhân viên CP khi nguồn không nêu; theo DEC-P01-001 và mục ledger "control-address" (omit vocative / neutral address) nên bỏ vocative: "Báo cáo tình hình số địch đã phát hiện."

**F09 — `p000413`.** "rồi gọng kìm hai tiểu đoàn đó" dùng danh từ làm động từ, gượng. Đề xuất "rồi kẹp gọng kìm hai tiểu đoàn đó" hoặc "bao vây gọng kìm".

**F10 — `p000415`.** "thưa các quý ông" lệch ledger b04 (Gentlemen → "Các vị", thay thế "Các anh", chưa canon) và nghe như dịch từ tiếng Anh. Đề xuất "Các vị…" cho đồng nhất, vẫn là phương án tạm. Giữ dấu lửng.

**F11 — `p000416`.** Viết hoa "Cụm Tập đoàn quân" khác khuyến nghị ledger b07 (loại đơn vị viết thường). Xem mục thuật ngữ bên dưới.

**F12 — Nhỏ về văn phong.** `p000392`: "thầm cảm thấy" thêm "thầm" (nguồn không nêu); `p000400`: "những gì ta thấy" dùng "ta" lạc giữa chuỗi "mình"/"chúng ta"; có thể "đúng như vẻ ngoài của nó"; `p000412`: "phải không?" biến câu khẳng định "you know" thành câu hỏi, có thể "mà, ai cũng biết thế". Đều không đổi nghĩa lớn.

## Khuyến nghị thuật ngữ (tạm, không canon)

### Norden Control — `p000393` (mục `vol02-ch02-b15-norden-control`)
- Khuyến nghị tạm: **giữ "Norden Control"** (dạng tên riêng giữ nguyên).
- Căn cứ: nhất quán với ledger P01, b05, b08 (độ tin cậy 0.8) và với chương 1; "Đài kiểm soát Norden" dễ gợi đài kiểm soát không lưu, xung đột với thuật ngữ "Airspace Control/control of the air" ở ledger b05–b06; nguồn dùng "Norden Control" như danh xưng của một cơ quan chỉ đạo/dẫn đường, nên giữ nguyên tránh chọn nghĩa cụ thể.
- Phương án thay thế: "Đài kiểm soát Norden" (đã có trong ledger); "Trung tâm Control Norden" (chưa có tiền lệ, không khuyến nghị).
- Độ bất định: trung bình (khoảng 0.6). Còn cần một quyết định chung về dạng rút gọn "Control" (xem F01) và quan hệ với "CP"; không ảnh hưởng cốt truyện nên không cần hỏi người dùng. Không nâng canon.

### Northern Army Group — `p000416` (mục `vol02-ch02-b15-northern-army-group`)
- Khuyến nghị tạm: **"Cụm tập đoàn quân phương Bắc"** (loại đơn vị viết thường, chỉ viết hoa "Bắc" nếu quy ước tên riêng sau này yêu cầu).
- Căn cứ: ledger b07 (ba đoạn `p000157`–`p000159`, khuyến nghị chữ thường và "phương Bắc" để khớp "Bộ chỉ huy phương Bắc"), ledger b04 (army group → cụm tập đoàn quân), ledger b12 (Western Army Group → "phương Tây" cùng kiểu). Bản b15 đã trùng cấu trúc với b07, chỉ khác viết hoa "Tập" (F11).
- Phương án thay thế: "Cụm tập đoàn quân phía Bắc" (khớp "Cụm tập đoàn quân phía Đông" của ledger vol-02 ch-01 b10 và nghe trung tính hơn "phương Bắc", vốn mang sắc thái địa–lịch sử); "Cụm tập đoàn quân phương Bắc" viết hoa toàn bộ nếu sau này coi đây là tên riêng.
- Độ bất định: trung bình (khoảng 0.5). Ledger hiện chia hai kiểu ("phía Đông" so với "phương Bắc/Tây"); cần một lượt hài hòa về sau, nên lưu thành mục cần thống nhất, không tự đổi các lô đã commit. Nguồn không cho biết quan hệ giữa cụm tập đoàn quân này và "Northern Command"; không suy diễn. Không ảnh hưởng cốt truyện trực tiếp ở đoạn này; không nâng canon.

### Mục khác (theo dõi, không phải thuật ngữ mới)
- "CP" giữ nguyên (`p000397`–`p000398`): chấp nhận; xem F01.
- "Being X" (`p000405`) giữ nguyên theo ledger P05; "Pixie 01" theo ledger b10; "Dacia" giữ nguyên.
- Đơn vị "6.500 feet" giữ nguyên; không quy đổi: chấp nhận.

## Kết luận
Bản dịch bám nghĩa tốt, không bỏ sót hay thêm ý đáng kể, nhấn mạnh đúng DEC-P01-002. Cần người giữ quyền sửa xử lý F01–F02 (mức vừa) trước khi coi lô đạt; F03–F12 sửa nếu thuận tiện. Các đề xuất thuật ngữ chỉ là tạm thời, coordinator ghi vào ledger/handoff.
