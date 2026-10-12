# Báo cáo phản biện — vol-02-ch-02-b16 (Claude)

- Task: `vol-02-ch-02-b16`; checkpoint_generation 410; vai trò: reviewer (nghĩa, văn phong, thuật ngữ).
- Phạm vi: 28 đoạn `YS-LN02/Text/part0014.xhtml/p000417`–`p000444`.
- Đầu vào đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b16, gói nguồn b16, `translations/vol-02/ch-02-b16.jsonl`, `canon/` (decisions, style-guide, glossary, characters, glossary-pending) và các mục pending liên quan trong `work/run-state/pending-terms.yml`. Không đọc gói nguồn hay bản dịch của lô khác.
- Kiểm tra hash: SHA-256 gói nguồn tính được `7175e710…1952a` **khớp** handoff. 28/28 đoạn có đủ, đúng thứ tự; `source_sha256` và `glossary_version` trong bản dịch khớp handoff. Không thiếu/thừa đoạn.
- Nhấn mạnh (DEC-P01-002): nguồn không có vùng nhấn mạnh nào (không có thẻ em/i); bản dịch không có dấu `*`. Đạt. Dấu ngoặc lặp ở `p000427` (bốn lớp) và `p000443` (ba lớp) được giữ đúng số lớp.
- Đại từ (DEC-P01-001): nội tâm tự quy chiếu của Tanya dùng "mình" nhất quán; thoại dùng "tôi". Lô không có câu trần thuật ngôi thứ ba về Tanya nên không phát sinh vấn đề "nó". Đạt.
- Tóm tắt: không có lỗi nghiêm trọng; không bỏ sót hay thêm ý lớn. Có 3 vấn đề mức vừa (thì giả định ở `p000422`; chênh lệch giữa bản dịch và ledger ở `p000425`; mất ẩn dụ tài chính ở `p000434`) và 10 mục nhẹ.

## Phát hiện

### Mức vừa

**F01 — `p000422`: câu giả định quá khứ bị biến thành khả năng/suy đoán.**
- Vấn đề: nguồn dùng giả định quá khứ kép (hắn *có thể đã* trở thành… và *sẽ đã* mãi gây chiến). Bản dịch "Hắn hẳn có thể trở thành… suốt đời gây chiến…" ghép "hẳn" (suy đoán chắc chắn) với "có thể" (khả năng) và bỏ dấu hiệu "đã/lẽ ra", nên đọc như khả năng còn mở hoặc suy đoán về quá khứ, không còn là phản thực tế đối chiếu với con đường thật của Tsuji. Vế "suốt đời gây chiến" cũng mất bản chất điều kiện (nếu đi theo hướng đó).
- Căn cứ: `style-guide.md`, mục "Giữ đồng thời tính giả định, mức chắc chắn và thời gian của giả định; không biến khả thể quá khứ thành khả năng ở hiện tại hoặc phỏng đoán".
- Đề xuất: "Lẽ ra hắn đã có thể trở thành một chiến binh công sở, cả đời gây chiến nội bộ trong công ty bằng tham vọng thăng tiến điên cuồng." Phương án thay thế: "Hắn đã có thể là… và sẽ cả đời…". Độ bất định thấp (ngữ pháp rõ), nhưng cách chọn trạng từ là vấn đề văn phong.

**F02 — `p000425`: "power harassment" — bản dịch lệch ledger; thuật ngữ chưa ổn định.**
- Vấn đề (a): ledger b16 (`vol02-ch02-b16-power-harassment`) ghi `proposed_vi: lạm quyền chèn ép cấp dưới`, phương án thay thế "quấy rối bằng quyền lực" (độ tin cậy 0.45). Bản dịch lại dùng "quấy rối quyền lực" — không trùng phương án chính, cũng không trùng đúng phương án thay thế. Cần đồng bộ ledger và bản dịch.
- Vấn đề (b): nội dung thuật ngữ. Nguồn dùng khái niệm quấy rối/lạm dụng thế thượng của cấp trên với cấp dưới trong công sở (thuật ngữ vay mượn, ngữ cảnh cho thấy ranh giới "vừa chạm ngưỡng" khi sếp bắt cấp dưới trả tiền). Hai điểm yếu của "quấy rối quyền lực": (i) trong tiếng Việt "quấy rối" thường gợi quấy rối tình dục, dễ gây hiểu lầm; (ii) "quyền lực" đứng sau "quấy rối" là kiểu dịch từng chữ, người đọc không quen thuật ngữ này có thể không hiểu ngay. Phương án chính của ledger tránh được cả hai nhưng dài và lặp "cấp dưới" khi ngay trước đó đã có "tiền của cấp dưới", đồng thời "lạm quyền" nghiêng về nghĩa pháp lý/hành chính hơn nguồn.
- (c) Chữ "nhưng" ở đầu vế sau ("—nhưng chỉ sát dưới ngưỡng…") không có trong nguồn: nguồn nối bằng quan hệ "vậy nên… sát dưới ngưỡng", không đối lập. Nên bỏ "nhưng" hoặc đổi thành quan hệ bổ sung.
- Đề xuất tạm (không canon; độ tin cậy ~0.5): giữ khái niệm "chèn ép bằng quyền lực" rút gọn thành "lạm quyền chèn ép" trong cụm "sát dưới ngưỡng lạm quyền chèn ép". Phương án thay thế: (1) "quấy rối quyền lực" (hiện tại, ~0.4; dùng rộng trong bản dịch từ tiếng Nhật nhưng mơ hồ với quấy rối tình dục); (2) "bắt nạt bằng quyền lực nơi công sở" (~0.35; rõ nghĩa nhưng dài và hơi nghiêng về bắt nạt); (3) giữ nguyên "power harassment" kèm giải thích trong ledger nếu về sau thống nhất giữ thuật ngữ Anh. Phân tích: tính hài hước của đoạn nằm ở việc dùng thuật ngữ công sở hiện đại; phương án thay thế (3) giữ được sắc thái hiện đại hóa nhưng ngoài văn bản đang dịch sang tiếng Việt thì ít tự nhiên. Độ bất định cao: chưa có thêm lần xuất hiện nào trong phạm vi được phép để so sánh nhất quán; không có gì ở đây ảnh hưởng cốt truyện.

**F03 — `p000434`: mất ẩn dụ tài chính "limit up".**
- Vấn đề: nguồn kết bằng ẩn dụ chứng khoán — mua (tức gây ra) mối thù của kẻ địch ở mức giá trần. Bản dịch "khiến kẻ thù căm ghét mình hết mức" chỉ giữ ý tăng tối đa, bỏ "mua" và hình ảnh giá trần. Đây là mạch ẩn dụ kinh doanh xuyên suốt lô (chẳng hạn phá sản ở `p000423`, công ty/điều kiện lao động ở `p000430`), nên mất mạch giọng.
- Căn cứ: `style-guide.md` (không lược bỏ chi tiết), mạch ẩn dụ công sở/tài chính của nội tâm trong chính lô này.
- Đề xuất: "Nói gọn lại, mình đang mua mối thù của kẻ địch ở mức giá trần." Phương án thay thế: "…mua lòng căm thù của kẻ địch với giá tăng trần" hoặc giữ diễn giải hiện tại nếu coi ẩn dụ khó dịch. Độ bất định: trung bình — "tăng trần" quen thuộc với người đọc chứng khoán Việt, nhưng "mua mối thù" có thể hơi lạ.

### Mức nhẹ

**F04 — `p000420`, `p000428`: xưng hô số nhiều không thống nhất với ledger.** `p000420` dùng "các anh" và `p000428` dùng "các quý ông", trong khi ledger b04 (`vol02-ch02-b04-plural-address`, 0.7) đề xuất "Các vị" trung tính giới và tránh suy diễn giới tính/thân mật. "các quý ông" còn mang sắc thái trang trọng/giới tính chưa có trong nguồn ngoài từ "gentlemen". Đề xuất tạm: `p000428` → "các vị"; `p000420` → "các vị" hoặc giữ "các anh" nếu coi người nghe là đội ngũ nam đã xác định (chưa có căn cứ trong lô). Không canon.

**F05 — `p000423`: "một chai vang" thêm đơn vị.** Nguồn nói "some" rượu vang hai mươi lăm năm; không nêu số lượng. Đề xuất "mấy chai/ít rượu vang" hoặc "rượu vang hai mươi lăm năm tuổi" không có lượng từ. Cũng cân nhắc "Ngoài ra" → "Còn nữa" cho giọng khẩu ngữ.

**F06 — `p000424`: "chi tiếp khách" và "kiểm toán".** (a) Nguồn nói về chi phí giao tế với cấp dưới, không phải khách hàng; "tiếp khách" dễ hiểu thành khách bên ngoài → "chi phí giao tế/liên hoan". (b) "audited" với "kiểm toán chi tiêu" nặng chất kế toán độc lập; "soi/kiểm tra chi tiêu vô cớ" tự nhiên hơn. Đề xuất, không bắt buộc.

**F07 — `p000426`: "nước mắt mình cứ trào ra".** Nguồn: nghĩ đến chuyện đó khiến mắt rưng rưng/nước mắt dâng; "cứ trào ra" thêm tính liên tục và cường độ. Đề xuất "mắt mình rưng rưng" hoặc "nước mắt chực trào". Phần còn lại (chiến hữu, nhắm mắt cho qua) đạt.

**F08 — `p000432`: ba chỗ nhỏ.** (a) "chẳng ai đời nào muốn nhận" sai trật tự thành ngữ → "đời nào có ai muốn nhận" hoặc "chẳng đời nào ai muốn nhận". (b) "tự do tín ngưỡng" thu hẹp nghĩa về tôn giáo; "freedom of belief" trong ngữ cảnh hoạt động cánh tả có thể rộng hơn (niềm tin/tư tưởng). Đề xuất tạm "tự do tín ngưỡng" giữ nếu muốn sát chữ; thay thế "tự do tư tưởng" nếu muốn bao trùm — độ bất định cao, không đủ căn cứ để chọn chắc. (c) "kẻ tố giác" cho "whistle-blower" thêm sắc thái miệt thị "kẻ"; "người tố giác" trung tính hơn (nguồn có hàm ý nghi ngờ nhưng bình diện đạo đức không được nêu trực tiếp).

**F09 — `p000433`: "Xét cho hợp lý".** Nguồn là "nghĩ một cách logic/xét theo lý trí"; "xét cho hợp lý" nghe như xin thông cảm. Đề xuất "Suy nghĩ một cách logic" hoặc "Xét theo lý trí". Phần "sau khi đã giết nhiều người… khó tự bảo vệ" đạt.

**F10 — `p000437`: quan hệ nhân quả bị đổi.** Nguồn: họ hết thuốc chữa nếu bỏ qua cân bằng giữa việc công và tự do cá nhân *bằng cách* gây rắc rối cho người khác. Bản dịch tách thành hai vế song song ("gây rắc rối… mà chẳng màng cân bằng…"), làm yếu quan hệ phương tiện. Đề xuất: "Nếu họ phớt lờ cân bằng giữa việc công và tự do cá nhân bằng cách gây rắc rối cho người khác thì hết thuốc chữa." Mức nghĩa vẫn đúng đại thể nên chỉ nhẹ.

**F11 — `p000440`: chơi chữ về "slug" mất.** Nguồn là câu cửa miệng "người khôn" chơi chữ giữa đạn và hành động đấm mạnh. "Đạn được gọi là viên chì vì nó nện đau điếng" chỉ giữ lý do, không còn tương ứng từ. Không tìm được cặp chữ Việt tương đương; đề xuất giữ nguyên hoặc ghi vào `notes` của dòng JSONL (hiện rỗng) để đối chiếu, không chèn ghi chú vào văn bản dịch (theo `style-guide.md`).

**F12 — `p000443`: "Vì vinh quang" lệch nghĩa.** "Glory to…" là lời tung hô ("Vinh quang thuộc về…"), không phải "vì" (hiến thân vì). Đề xuất "Vinh quang thuộc về Tổ quốc và chỉ huy của chúng ta!" hoặc "Vinh quang cho Tổ quốc…". "Rõ!" cho "Roger" khớp ledger (`b08-radio-terms`); lưu ý `p000427` ("Understood") cũng là "Rõ!", chấp nhận được, hoặc "Đã rõ!" nếu muốn giữ khác biệt.

**F13 — `p000422` (vế sau): "chẳng dễ sống".** "rather impossible" là gần như không sống nổi; "chẳng dễ sống" yếu hơn. Đề xuất "quả thật khó mà sống nổi". Các chi tiết "công dân tốt", "biết xấu hổ và có lương tâm" đạt.

## Đoạn không có vấn đề đáng kể

`p000417`, `p000418`, `p000419` (giọng miệt thị với Tsuji là của nguồn, "tên/hắn/gã" thay đổi hợp lý), `p000429`, `p000430`, `p000431`, `p000435`, `p000436`, `p000438`, `p000439`, `p000441`, `p000442`, `p000444`.

## Phân tích điểm chú ý theo yêu cầu

### `p000421` — "Tsuji doctrine"

- Bản dịch: "học thuyết Tsuji". Ledger: `vol02-ch02-b16-tsuji-doctrine`, đề xuất giữ, thay thế "học thuyết của Tsuji" (0.55).
- Chứng cứ trong ngữ cảnh: (1) Tsuji đã được nêu tên ở `p000419` là kẻ ba hoa, vùi dập nhân tài rồi vẫn được thăng chức; (2) `p000421` mô tả "doctrine" là thứ Tanya dùng để tự bảo vệ, dựa trên việc "gã đó" tránh được truy tố tội ác chiến tranh sau Thế chiến thứ Hai, và nói rõ có điều học được dù không bắt chước nổi sự trơ trẽn; (3) `p000424`–`p000425` tiếp tục nêu điều học từ Tsuji (kiểm tra chi tiêu để tìm điểm yếu, quân đội và công ty không khác mấy). Như vậy "doctrine" ở đây là cách ứng xử/phương châm thực dụng gắn với một người, cách gọi nửa đùa, không phải một học thuyết được hệ thống hóa.
- Đánh giá: "học thuyết Tsuji" chấp nhận được và giữ được giọng trịnh trọng mỉa mai; nhược điểm là "học thuyết" nghe như hệ tư tưởng chính thức. Phương án thay thế: "học thuyết của Tsuji" (nhấn quan hệ sở hữu), "cách làm kiểu Tsuji", "đạo Tsuji" (đùa hơn, nhưng thêm sắc thái tôn giáo), "phương châm Tsuji".
- Đề xuất tạm: giữ "học thuyết Tsuji" (~0.55–0.6) và dùng nhất quán nếu thuật ngữ này xuất hiện lại. Độ bất định: không rõ nguồn có định nghĩa chính thức ở nơi khác; không tự khẳng định Tsuji có phải nhân vật lịch sử hay không (nguồn chỉ nêu "gã đó"/bối cảnh Thế chiến thứ Hai); không đưa vào canon; không ảnh hưởng cốt truyện theo chứng cứ hiện có.

### `p000425` — "power harassment"

Xem F02. Tóm tắt: lệch ledger, "quấy rối" gợi quấy rối tình dục, cần chốt một phương án trong ledger. Đề xuất tạm "lạm quyền chèn ép", thay thế "quấy rối quyền lực", "bắt nạt bằng quyền lực nơi công sở". Tất cả là đề xuất, không canon.

## Đề xuất thuật ngữ (tạm, không canon)

| Thuật ngữ | Đề xuất | Thay thế | Mã đoạn | Độ tin cậy |
|---|---|---|---|---|
| power harassment | lạm quyền chèn ép (trong cụm "ngưỡng lạm quyền chèn ép") | quấy rối quyền lực; bắt nạt bằng quyền lực nơi công sở | p000425 | 0.5 |
| Tsuji doctrine | học thuyết Tsuji | học thuyết của Tsuji; cách làm kiểu Tsuji; phương châm Tsuji | p000421 | 0.55 |
| limit up | (giá) trần/tăng trần | giữ diễn giải "hết mức" | p000434 | 0.5 |
| gentlemen (xưng hô số nhiều) | các vị (theo ledger b04) | các anh; các quý ông | p000420, p000428 | 0.65 |
| freedom of belief | tự do tín ngưỡng (giữ tạm) | tự do tư tưởng | p000432 | 0.45 |

## Ghi chú pending

Các mục `work/run-state/pending-terms.yml#chapter2_b16_translation_proposals` cho p000421 và p000425 cần coordinator đồng bộ lại: ghi "quấy rối quyền lực" vào ledger nếu giữ bản dịch hiện tại, hoặc để translator sửa theo F02. Fatherland → "Tổ quốc" (b01) và Entente Alliance → "Liên minh Entente" (b03) được áp dụng nhất quán, không có đề xuất mới.
