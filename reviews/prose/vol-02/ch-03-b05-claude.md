# Báo cáo review vol-02-ch-03-b05 (Claude)

- task_id: `vol-02-ch-03-b05`; checkpoint_generation: 484; vai trò: Claude reviewer.
- Phạm vi: 20 đoạn `YS-LN02/Text/part0016.xhtml/p000100`–`p000119` (đọc đủ 20/20).
- Đầu vào đã dùng: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b05, source package b05, `translations/vol-02/ch-03-b05.jsonl`, `canon/` (style-guide, decisions, glossary-pending, characters, glossary) và mục ledger `chapter3_b05_translation_proposals` cùng các mục pending liên quan của chính các thuật ngữ trong lô.
- Hash source package: `d2c7aac1e7262e2cc0da1e03f4771ffc9933ea01dcf3c39fa688da52714bd9d3` — khớp handoff (đã kiểm bằng sha256sum). Không mở lô khác, EPUB/PDF, không sửa tệp nào ngoài báo cáo này.
- Báo cáo không chép câu nguồn; chỉ dùng thuật ngữ ngắn và mã đoạn để nhận diện.

## Tóm tắt

Bản dịch nhìn chung chính xác và đọc tự nhiên. Không có lỗi nghiêm trọng, không có đoạn bị bỏ sót hoặc thêm cả mệnh đề. Nhấn mạnh duy nhất của nguồn (p000105) được giữ đúng bằng `*...*`, không có nhấn mạnh thừa (DEC-P01-002). Còn **5 lỗi mức vừa** (p000102, p000111, p000112, p000118, p000119) nên sửa trước khi nâng trạng thái lô; còn lại là lỗi nhẹ. Các đoạn p000105, p000109, p000115, p000116 không có vấn đề cần sửa.

## Lỗi mức vừa

**F01 — p000102 — thêm/thu hẹp nghĩa của “lines”.**
- Vấn đề: nguồn nói thu hẹp “lines” nói chung; bản dịch chọn “tuyến phòng thủ”. Trong đoạn này “lines” có thể là chiến tuyến hoặc tuyến tiếp tế (lời mở đầu đoạn nêu lý do là hậu cần không kham nổi); bản dịch chốt thành “phòng thủ”, một chi tiết nguồn không nêu, và có thể lệch so với p000101 (chờ thời cơ) lẫn p000108 (tuyến tiếp tế).
- Căn cứ: quy tắc “không tự thêm giải thích”, và quy tắc giữ độ mở của đối tượng (style-guide, bổ sung sau pilot-01).
- Đề xuất: “thu hẹp tuyến”/“thu hẹp chiến tuyến”, không gắn “phòng thủ”. Chưa đủ căn cứ để quyết “chiến tuyến” hay “tuyến tiếp tế” — giữ trung tính.

**F02 — p000111 — thêm cơ quan và không nhất quán với p000118.**
- Vấn đề: nguồn chỉ nói “Central officers”; bản dịch thêm “Bộ Chỉ huy”, trong khi p000118 dịch “Central Army” là “Lục quân Trung ương”. Cùng một nhóm sĩ quan (Tanya và những người cùng phía) mang hai tên khác nhau trong cùng lô; cả hai cũng khác ledger (“Quân Trung ương”, conf. 0.45, hoặc giữ nguyên “Central”).
- Đề xuất tạm: “các sĩ quan Trung ương” cho p000111; p000118 dùng “Quân Trung ương” theo ledger (xem T03). Không thêm “Bộ Chỉ huy”, vì echelon chưa được xác lập.

**F03 — p000112 — đại từ “Anh” gọi nhầm người nghe.**
- Vấn đề: câu mở đầu lời thoại dịch “Anh nói cũng có lý”, nhưng ngay sau đó cùng người nói gọi người nghe là “cô” (người đạt chiến thắng khi quân ta chỉ bằng một nửa đối phương, tức Degurechaff). Cùng một người nghe bị gọi “anh” rồi “cô” trong một lời thoại → lỗi đại từ, và ngầm gán giới tính khác (DEC-P01-001 yêu cầu không suy ra giới tính từ đoạn thiếu ngữ cảnh).
- Đề xuất: “Cô nói cũng có lý”. Người nói (chưa nêu tên trong đoạn) vẫn là điểm bất định; chỉ sửa đại từ cho khớp người nghe.

**F04 — p000118 — thời/thể của giả định và sắc thái “cô ta”.**
- Vấn đề (1): nguồn là câu giả định phản thực (would have … if she weren’t). Bản dịch “đã đuổi cô ta đi ngay lập tức nếu cô không phải…” dễ đọc thành sự việc đã xảy ra (ông đã đuổi), trái quy tắc giữ tính giả định và thời của giả định.
- Vấn đề (2): “cô ta” thêm sắc thái miệt thị không có trong nguồn (style-guide: không thêm sắc thái phán xét); toàn lô còn lại dùng “cô”.
- Đề xuất: “… rằng ông hẳn đã đuổi cô ra ngoài ngay lập tức, nếu cô không phải là đại diện cho quan điểm của Quân Trung ương” (hoặc “nếu không vì cô là đại diện…”). “Cô” thay cho “cô ta”.

**F05 — p000119 — chủ thể của “kiệt sức” bị chốt mơ hồ và thêm “chính”.**
- Vấn đề: nguồn nói hai tiểu đoàn bị làm cho mệt mỏi/kiệt quệ bởi nỗ lực của đồng đội. Bản dịch “kiệt sức vì nỗ lực của chính đồng đội mình” (a) bỏ thể bị động nên không rõ ai kiệt sức, người đọc dễ hiểu là tiểu đoàn phe ta, và (b) thêm “chính” nhấn mạnh không có trong nguồn. Hướng đúng (tiểu đoàn địch bị đồng đội làm kiệt quệ, hay ngược lại) phụ thuộc ngữ cảnh ngoài phạm vi lô — **chưa đủ căn cứ để chốt**.
- Đề xuất: giữ độ mở của nguồn, ví dụ “hai tiểu đoàn bị bào mòn bởi nỗ lực của các đồng đội chúng ta”; bỏ “chính”. Nếu coordinator có ngữ cảnh p000120 trở đi thì xác nhận sau.

## Lỗi mức nhẹ

- **F06 — p000100/p000102/…** — “cô” dùng cho Degurechaff theo điểm nhìn các sĩ quan (nguồn dùng “her/she”). Hợp lý và không vi phạm DEC-P01-001 (quyết định này chỉ ràng buộc “nó/mình” cho trần thuật/nội tâm của Tanya ở giai đoạn đã nêu). Ledger lại ghi các phương án “nó / lặp Tanya / lược chủ ngữ” cho trần thuật về Tanya; coordinator cần ghi rõ “cô” là lựa chọn tạm cho điểm nhìn bên ngoài (Schreise/sĩ quan) trong lô này, để tránh xung đột với các lô trần thuật nội tâm. Không sửa bản dịch.
- **F07 — p000101** — “mọi việc” thêm phạm vi (nguồn chỉ “nó”, tức vấn đề/cuộc chiến đang bàn). Đề xuất: “giải quyết dứt điểm bằng một đòn quyết định” hoặc “giải quyết chuyện này…”.
- **F08 — p000102** — “chẳng buồn lắng nghe lấy một lời” dịch thành thái độ không thèm, trong khi nguồn là “không thể nghe lọt tai”; đổi sắc thái từ khả năng sang thái độ. Đề xuất: “không thể lọt tai nổi dù chỉ một lời”.
- **F09 — p000103** — “các anh” (lời Tanya nói với sĩ quan Tác chiến): gán giới tính và có thể quá thân/ngang vai khi quan hệ cấp bậc chưa chốt. Đề xuất trung tính: “các vị”. Mức bất định cao; chấp nhận được nếu coordinator giữ nhất quán.
- **F10 — p000104** — “cau có nhìn chằm chằm” là cách diễn đạt cảm xúc; nguồn là nhìn trừng/lườm. Đề xuất: “trừng mắt nhìn”.
- **F11 — p000106** — “dư sức đảm đương” mạnh hơn “không thành vấn đề”; “thu gom” có sắc thái gom nhặt, “mọi thứ cần thiết” rộng hơn “provisions” (lương thảo/vật phẩm). Đề xuất: “hoàn toàn đáp ứng được”; “đã bảo đảm gần đủ vật tư cho mặt trận”.
- **F12 — p000107/p000117** — “Tập đoàn quân Phương Bắc” (p000117, viết hoa P) và “tập đoàn quân” (p000107) khác ledger “cụm tập đoàn quân phương Bắc” (conf. 0.5–0.8). Đề xuất: “Cụm tập đoàn quân phương Bắc”, “cụm tập đoàn quân”.
- **F13 — p000108** — “đầy ẩn ý” cho tiếng thở dài: “pointed” là cố ý để người khác nghe thấy, không hẳn là ẩn ý. Đề xuất: “thở dài một tiếng thật rõ”. Ngoài ra “chọc thủng phòng tuyến” thêm tân ngữ “phòng tuyến” (chấp nhận được vì ngữ cảnh kháng cự).
- **F14 — p000110/p000117** — “ngoan cố” hàm ý khăng khăng sai trái, mạnh hơn “stubborn”; style-guide yêu cầu không thêm sắc thái đạo đức/miệt thị. Đề xuất: “cứng đầu/bướng bỉnh”, thống nhất ở hai đoạn.
- **F15 — p000111** — (a) “giữ vững quan điểm” dịch cụm “keep holding out”; cụm này mơ hồ (kiên trì/cầm cự), dịch thành “quan điểm” đã thu hẹp; đề xuất “vẫn sẽ kiên trì”. (b) “chỉ tổ vướng chân” = cản trở, nguồn là gây phiền toái/bực mình; đề xuất “chỉ tổ gây phiền”. Chưa chắc ý (a); giữ độ mở.
- **F16 — p000113** — bỏ liên từ mở đoạn mang nghĩa giải thích (“xét cho cùng”), làm đoạn mất quan hệ lý do với p000112. Đề xuất: “Xét cho cùng, xét cả tổn thất pháp sư…”.
- **F17 — p000114** — “thuyết phục” mất sắc thái dỗ dành/khuyên nhủ nhẹ; đề xuất “khuyên nhủ”/“dỗ”. “lãnh thổ” thêm vào “Chiếm toàn bộ lãnh thổ Liên minh Entente” — chấp nhận được, ghi nhận.
- **F18 — p000117** — “bờ bên kia” thêm yếu tố địa lý (bờ/sông) không có trong nguồn. Đề xuất: “phía đối diện”/“bên kia”.

Quy trình (không gán đoạn): translator báo `pending_term_count: 1`, nhưng bản dịch có thêm các lựa chọn thuật ngữ chưa vào ledger: “Lục quân Trung ương”, “Bộ Chỉ huy Trung ương”, “Tập đoàn quân Phương Bắc”, “công binh dã chiến”, “pháp sư biệt kích”, “nhiên liệu đa dụng”, “đại đội tăng cường”, “Bộ phận Tác chiến/Tình báo” (xem T01–T05). Ledger không cần coi các mục này là lỗi mức vừa, nhưng coordinator nên ghi nhận.

## Kiểm tra theo hạng mục

- **Nghĩa/thiếu–thừa:** không bỏ đoạn; các thêm/bớt đáng kể nằm ở F01, F02, F05, F16, F18. Các con số (hai mươi kilômét, ba tuần, một tuần, hai trận đánh, hai tiểu đoàn, hai đối một ≈ “một nửa đối phương”) đều đúng.
- **Đại từ:** F03, F04 (mức vừa), F09 (nhẹ). “ông” cho Schreise nhất quán. Tanya xưng “Tôi” trong thoại, hợp lý.
- **Nhấn mạnh:** p000105 `*có sẵn*` đúng; không đánh dấu thừa ở nơi khác.
- **Văn phong:** tự nhiên, nhịp tốt; “Trớ trêu thay”, “Thật lãng phí thời gian biết bao” giữ giọng châm biếm của Schreise. Điểm cần chỉnh nằm ở các từ gán sắc thái (F10, F14, F15, F17).
- **Cấu trúc “không chỉ… mà còn…”:** p000116 đúng phạm vi tăng tiến (vũ khí/đạn dược → lương thực).

## Đánh giá “light-rail” (p000108, p000111) — khuyến nghị tạm, không nâng canon

- **Ngữ cảnh trong lô:** (a) p000108 đo khoảng cách “hơn hai mươi km khỏi light-rail” và nối trực tiếp với việc duy trì tuyến tiếp tế bằng sức người khi quân đi xa → nó là một tuyến cố định mà tiếp tế dựa vào, không phải phương tiện; (b) p000111 “công binh dã chiến tu sửa đường và đặt thêm light-rail” → công trình quân sự có thể đặt thêm ở vùng chiến sự, dùng để cải thiện hậu cần. Cả hai nghiêng mạnh về “hệ thống đường ray hạng nhẹ/dã chiến”, loại trừ “phương tiện” và “giao thông đô thị”.
- **Phương án:**
  1. **đường sắt nhẹ** (đề xuất của translator; đang dùng): sát nghĩa, đọc tự nhiên, trung tính về khổ ray và nguồn động lực; giữ được tính “đặt thêm” (p000111). Nhược điểm: người đọc Việt ít quen, có thể hiểu mơ hồ “nhẹ” ở đâu.
  2. **đường sắt khổ hẹp**: thêm khẳng định kỹ thuật về khổ ray mà nguồn không nêu → loại, trừ khi có chứng cứ.
  3. **đường sắt dã chiến**: sát với vai trò (công binh dã chiến đặt) nhưng thêm “dã chiến” không có trong nguồn; có thể là phương án thay thế nếu về sau thấy từ “nhẹ” gây khó hiểu.
  4. **đường sắt đô thị / tàu điện nhẹ** (hai phương án thay thế trong ledger): **không phù hợp** — “đô thị” gán bối cảnh không có; “tàu điện nhẹ” chỉ phương tiện/đường tàu điện hiện đại, mâu thuẫn việc đo khoảng cách từ đường ray và việc công binh đặt thêm ở tiền tuyến mùa đông. Khuyến nghị bỏ khỏi danh sách phương án.
- **Khuyến nghị tạm:** giữ **“đường sắt nhẹ”** cho cả hai đoạn; sửa nhỏ để nhất quán: p000108 giữ “tuyến đường sắt nhẹ”; p000111 có thể “đặt thêm đường sắt nhẹ” (nguồn là danh từ không đếm được, “tuyến” đang thêm khái niệm tuyến mới). Độ tin cậy: ~0.65 (tăng từ 0.5 của translator).
- **Bất định còn lại:** (1) chưa đối chiếu được từ gốc ngôn ngữ nguồn — chỉ có bản tiếng Anh, nên không thể xác nhận đây là hệ thống đường sắt hạng nhẹ/dã chiến có tên riêng; (2) chưa biết các lô sau có dùng lại thuật ngữ này (ví dụ gắn với đầu máy/toa xe) hay không; (3) chưa có căn cứ về khổ ray hay động lực. Nếu các lô sau cho thấy nghĩa khác thì sửa; cho tới đó đây chỉ là đề xuất tạm, **không nâng canon** và không ảnh hưởng cốt truyện nên không phải hard stop.

## Đề xuất thuật ngữ (đều pending, không phải canon)

| Mã | Nguồn | Đề xuất tạm | Phương án khác | Đoạn | Độ tin cậy | Ghi chú |
|---|---|---|---|---|---|---|
| T01 | light-rail | đường sắt nhẹ | đường sắt dã chiến | p000108, p000111 | 0.65 | Xem phần đánh giá; bỏ “đường sắt đô thị”, “tàu điện nhẹ” |
| T02 | Operations / Logistics / Intelligence (tên bộ phận) | phía Tác chiến / phía Hậu cần / phía Tình báo (tên cơ quan: Cục …) | Bộ phận … | p000100, p000102, p000104, p000107, p000116 | 0.5 | Translator dùng “Bộ phận”, “các sĩ quan …”; nên khớp ledger b04 |
| T03 | Central (officers / Army) | Trung ương (sĩ quan Trung ương; “Quân Trung ương”) | Lục quân Trung ương | p000111, p000118 | 0.45 | Không thêm “Bộ Chỉ huy”; echelon chưa rõ |
| T04 | Northern Army Group / army group | Cụm tập đoàn quân phương Bắc / cụm tập đoàn quân | Tập đoàn quân … | p000107, p000117 | 0.6 | Theo ledger hiện có |
| T05 | field engineers; mage commandos; general-purpose fuel; augmented company | công binh dã chiến; pháp sư biệt kích; nhiên liệu thông dụng; đại đội tăng cường | nhiên liệu đa dụng | p000107, p000110, p000111, p000119 | 0.5 | “Augmented” có thể chỉ quy mô hoặc thành phần (khớp ghi chú ledger cho “augmented unit”) |
| T06 | Tanya (narration, external POV) | cô (điểm nhìn Schreise/sĩ quan) | lặp tên; “nó” cho điểm nhìn Tanya | cả lô | 0.6 | Ghi rõ để không xung đột DEC-P01-001 |

## Rủi ro và tiếp nhận

- Không có hard stop; không có quyết định ảnh hưởng cốt truyện. Điểm bất định nhất là F05 (chủ thể p000119) và người nói của p000112 — cần xác nhận khi có ngữ cảnh rộng hơn, cho tới đó dùng cách diễn đạt trung tính.
- Người giữ quyền sửa tiếp nhận F01–F05 (bắt buộc) và F06–F18 (nên sửa/ghi chú). Reviewer không sửa bản dịch, handoff, ledger hay canon.
