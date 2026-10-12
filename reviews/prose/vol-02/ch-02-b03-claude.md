# Báo cáo phản biện văn phong và ngữ nghĩa — vol-02-ch-02-b03 (batch lẻ, có cờ new_pending_terms)

- **Người phản biện:** Claude (reviewer; chỉ ghi báo cáo, không sửa bản dịch, handoff, canon, ledger hay run-state). Báo cáo không trích văn bản nguồn.
- **Phạm vi:** 28 đoạn p000044–p000071 (`YS-LN02/Text/part0014.xhtml/…`, viết tắt `pNNNNNN`). Đã đọc: `agents/shared.md`, `config/translation-pipeline.yml`, handoff b03, gói nguồn b03, bản dịch b03, `canon/*`, `work/run-state/pending-terms.yml` (mục b03/b02 và các mục rank, army group, Tanya narration), báo cáo b02 và signoff b02 (chỉ phần quyết định “councilor”). Không xem batch dịch khác; chỉ đối chiếu chuỗi thuật ngữ qua ledger.

## 1. Kết luận

- **Kết luận:** `pass_with_fixes`.
- **Mức nghiêm trọng:** serious = 0; moderate = 4 (M1–M4); minor = 9 (m1–m9).
- **next_action:** người giữ quyền sửa xử lý M1–M4, cân nhắc minor, chạy lại validator rồi commit. Cần reviewer xác nhận nhanh p000044, p000046, p000047, p000049, p000053, p000059, p000062, p000069 sau khi sửa.

## 2. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự ID | Đạt: 28 đoạn, p000044–p000071, đúng thứ tự, khớp 1:1 với gói nguồn. |
| Hash gói nguồn | Đạt: `ae04ab9f…cb5eda` khớp handoff. |
| `source_sha256` mỗi record | Đạt: khớp gói nguồn. |
| `glossary_version` | Đạt: khớp handoff. |
| `status` / `notes` | `draft` toàn bộ; `notes` rỗng (xem m9). Không có ghi chú làm việc lọt vào translation. |
| Nhấn mạnh (DEC-P01-002) | Đạt: nguồn chỉ có nhấn mạnh ở p000065 (toàn bộ đoạn); bản dịch có `*…*` đúng và chỉ ở đó. Không đánh dấu thừa. |
| Định dạng thoại | Đạt: dấu ngoặc kép giữ đúng ở các đoạn thoại và đoạn hỗn hợp (p000053, p000059). |
| Người nói | Không phát hiện lỗi. p000060 là lời trực tiếp của phía Entente (xưng “chúng ta”), p000061 là tường thuật lại việc Abensoll cảnh báo; p000062 là một nghị viên khác nói với Abensoll. |

## 3. Phát hiện

### Moderate

- **M1 — Chức danh “councilor” lệch quyết định tạm của b02 (p000044, p000046, p000053, p000059, p000062).**
  Bản dịch dùng “Ủy viên hội đồng” (p000044, p000062, p000046 dạng thường, p000053), “Ủy viên Hội đồng Đối ngoại” (p000046, p000059), trong khi ledger `vol02-ch02-b02-councilor` (đã áp dụng cho b02; handoff b03 ghi rõ dùng lựa chọn b02) là **“Nghị viên”**, “Nghị viên Ngoại giao” và dạng chung viết thường. Ngoài ra: (a) “Đối ngoại” khác “Ngoại giao” đã dùng ở b02 cho cùng chức vụ của Abensoll; (b) “Hội đồng” viết hoa giữa chức danh không theo quy ước viết hoa của dự án (chỉ viết hoa chức danh/bộ phận ngắn); (c) p000053 dùng cụm miêu tả dài “phụ trách nội vụ” thay vì dạng chức danh như b02. Hậu quả: cùng một người (Abensoll) bị gọi bằng hai chức danh khác nhau giữa b02 và b03.
  Đề xuất (áp dụng đồng loạt, độ tin cậy 0.8 cho việc đồng bộ):
  - p000044, p000062 (xưng hô trực tiếp): “Nghị viên Abensoll”.
  - p000046, p000059: “Nghị viên Ngoại giao Abensoll”.
  - p000046 (người không tên): “một nghị viên” (xem m1 về “lớn tuổi hơn”).
  - p000053: “Nghị viên Nội vụ” (hoặc “vị nghị viên Nội vụ”) thay cho “ủy viên hội đồng phụ trách nội vụ”.
  Xem mục 4.1 về việc có nên đổi thuật ngữ gốc hay không.

- **M2 — p000069: đại từ “Cô” cho Tanya trong trần thuật, trái DEC-P01-001 và ledger.**
  DEC-P01-001 (đã duyệt): trần thuật về Tanya dùng “nó”, không suy diễn thêm; ledger các batch ch01 (b05–b09, ví dụ `vol02-ch01-b09`…) tiếp tục “nó” hoặc lặp tên/lược chủ ngữ, ghi rõ “tránh cô”. Câu cuối p000069 dùng “Cô bước lên bục…”, đồng thời đoạn này còn hai chủ thể khác (Weiss và binh sĩ) nên cần tránh nhầm. Đề xuất: “Tanya bước lên bục ở chính giữa…” (lặp tên, an toàn nhất) hoặc “Nó bước lên bục…”. Độ tin cậy 0.85.

- **M3 — p000047: “quyết định là bên đầu tiên tham chiến” làm lệch nghĩa.**
  Nguồn nói Khối Thịnh vượng chung đã quyết định *bước đầu tiên tiến tới* việc tham chiến (một bước khởi đầu/chuẩn bị can dự). Bản dịch thành “bên đầu tiên tham chiến”: (a) biến bước khởi đầu thành việc đã/sẽ tham chiến; (b) thêm hàm ý xếp thứ tự trước các nước khác, mâu thuẫn với câu liền trước (Cộng hòa đã giao chiến). Đề xuất: “nên đã quyết định đi bước đầu tiên để tiến tới việc tham chiến”. Độ tin cậy 0.8.

- **M4 — p000049: câu về “một nửa lời đề nghị như một sự sỉ nhục” mơ hồ/gần như vô nghĩa.**
  Nguồn nói về cách giới lãnh đạo Entente hiểu động cơ của Khối Thịnh vượng chung khi đề nghị giúp: một phần (một nửa) của lời đề nghị mang ý sỉ nhục, dựa trên việc họ đã phá hiệp ước. Bản dịch “chỉ đưa ra một nửa lời đề nghị như một sự sỉ nhục” có thể bị đọc là chỉ đề nghị một nửa phạm vi viện trợ (nghĩa số lượng), khác ý. Đề xuất bám nguồn nhưng giữ độ mở: “Khối Thịnh vượng chung đưa ra lời đề nghị này, một nửa là để sỉ nhục họ” (chỉ đổi “nửa” sang vị trí động cơ, không thêm chủ thể). Độ tin cậy 0.55 vì nguồn tiếng Anh vốn cô đọng; nếu coordinator có đối chiếu bản gốc khác, nên xác nhận lại. Không ảnh hưởng cốt truyện.

### Minor

- **m1 — p000046: “lớn tuổi hơn”.** Nguồn chỉ nói một nghị viên lớn tuổi; “hơn” gợi so sánh với Abensoll, thêm quan hệ. Đề xuất “một nghị viên cao tuổi” hoặc “một nghị viên lớn tuổi”.
- **m2 — p000054: “tập đoàn quân” cho “army group”.** Ledger ch01 (b02, b10) dùng “cụm tập đoàn quân” cho army group. Đề xuất “một cụm tập đoàn quân của Đế quốc” để nhất quán (tạm thời, không canon). Độ tin cậy 0.6.
- **m3 — p000055: mất mức độ giả định “should”.** “Ít nhất, họ cũng có thể xử lý phần lớn tình huống” khẳng định hơn nguồn (dự đoán). Đề xuất “hẳn ít nhất cũng xử lý được phần lớn tình huống”.
- **m4 — p000062: “thiết giáp hạm” cho “capital ships”.** “Thiết giáp hạm” là loại tàu cụ thể (battleship), hẹp hơn “capital ship”. Đề xuất “chiến hạm chủ lực” (hoặc “tàu chủ lực”); đồng thời dấu “?” sau “thôi đấy” làm câu lủng củng, nên đổi thành “…chỉ có hai chiến hạm chủ lực thôi, ông nhớ chứ?” hoặc câu hỏi nhẹ hơn. Độ tin cậy 0.6; người nói là người phía Entente nói về hải quân nước mình (xưng “chúng ta”), nên không vướng Hải quân Cộng hòa.
- **m5 — p000064: “Chuyện này được giữ bí mật”.** Nguồn là lời báo trước thông tin mật (“đây là chuyện mật”), không phải mô tả tình trạng chung. Đề xuất “Đây là chuyện mật, nhưng…”.
- **m6 — p000052: “chỉ coi đây như một mặt trận phụ”.** “Đây” mơ hồ (Entente hay cuộc chiến); nguồn là “dự án phụ”. Đề xuất “chỉ coi đó như một việc phụ” hoặc “một mặt trận phụ” kèm chủ ngữ rõ (“coi họ…”). Mức nhẹ.
- **m7 — p000063: “cố tìm được chút hy vọng”.** “Cố” và “tìm được” mâu thuẫn nhẹ; nguồn là vẫn xoay xở cảm thấy có hy vọng. Đề xuất “Dù vậy ông vẫn xoay xở cảm thấy chút hy vọng.”
- **m8 — p000056: “mình có thể ngăn chặn” (đại từ).** Trần thuật về giới lãnh đạo, không phải nội tâm Tanya; “mình” tự quy chiếu tập thể hơi lệch giọng. Đề xuất “họ có thể ngăn chặn”. Mức nhẹ.
- **m9 — Ledger/notes.** `notes` rỗng nhưng có bốn nhóm pending (translator báo 4). Nên cân nhắc ghi vào ledger: “cụm tập đoàn quân” (p000054), “capital ship” (p000062), “Chiến tranh Dacia” (p000051) cho các batch sau; cũng ghi rằng p000048 “mới là” nhấn nhẹ thay cho nhấn mạnh nguồn không có (rất nhẹ, có thể bỏ “mới”).

## 4. Thuật ngữ pending: lựa chọn tạm thời (không canon)

### 4.1 Councilor / chức danh

- **Mã đoạn:** p000044, p000046, p000053, p000059, p000062 (và p000061 chỉ nhắc “đồng nghiệp”, không có chức danh).
- **Lựa chọn tạm:** **“Nghị viên”**; chức danh gắn tên viết hoa (“Nghị viên Ngoại giao Abensoll”, “Nghị viên Abensoll”); dạng chung viết thường (“một nghị viên”). Giữ đúng lựa chọn của b02 (ledger `vol02-ch02-b02-councilor`, độ tin cậy 0.6).
- **Độ tin cậy:** 0.55–0.6.
- **Lý do:** (1) Nhất quán với b01/b02; đổi chiều ngược ở b03 làm cùng một nhân vật mang hai chức danh. (2) “Nghị viên” ngắn, dùng được trước tên và trong lời xưng hô trực tiếp (p000044, p000062). (3) Chi phí đổi hàng loạt sau này thấp hơn nếu giữ từ sớm. (4) Không ảnh hưởng cốt truyện.
- **Phương án thay thế:** “Ủy viên hội đồng / Ủy viên Ngoại giao / Ủy viên Nội vụ” (độ tin cậy ~0.4). Batch này thêm căn cứ cho phương án “ủy viên”: các thành viên hội đồng có phân công theo lĩnh vực (ngoại giao, nội vụ), họ tham gia hoạch định chính sách đối ngoại và quân sự, nghiêng về hội đồng hành pháp hơn là nghị viện lập pháp; “nghị viên” trong tiếng Việt thường gợi nghị viện. Tuy nhiên “ủy viên” dài hơn, gợi sắc thái bộ máy chính thức, và chưa có đoạn nào xác lập cơ chế bầu cử/quyền hạn. Vì vậy tạm giữ “Nghị viên”.
- **Điều kiện xem lại:** nếu batch/volume sau xác lập rõ hội đồng là cơ quan hành pháp theo bộ phận (nội các), nên đổi đồng loạt sang “Ủy viên …” và rà lại b02/b03 cùng lúc; ghi trong ledger là đổi theo nhóm, không đổi lẻ.
- **Ghi chú ledger:** thêm mã p000044, p000046, p000053, p000059, p000062 cho nhóm b03 (ledger `vol02-ch02-b02-councilor` đã liệt kê các mã này trước khi b03 được dịch; cần xác nhận lại sau khi sửa M1).

### 4.2 Commonwealth

- **Mã đoạn:** p000045, p000047, p000049, p000057, p000059, p000064.
- **Lựa chọn tạm:** **“Khối Thịnh vượng chung”**.
- **Độ tin cậy:** 0.65.
- **Lý do:** (1) Tên chính thể có chữ “Commonwealth” có cách dịch tiếng Việt thông dụng là “Khối Thịnh vượng chung”; nhất quán với ledger vol-01 (`b03-commonwealth`, 0.6) và ch01 (`vol02-ch01-b14-commonwealth`). (2) Batch này mô tả đây là một cường quốc hải quân, trung lập có thiện cảm, đã bước đầu can dự để cân bằng quyền lực, nên không có căn cứ coi là “liên bang” (tránh trùng với “Federation/Liên bang” ở vol-01). (3) Không có đoạn nào cho biết cấu trúc nội bộ để cân nhắc thêm.
- **Phương án thay thế:** “Thịnh vượng chung” (rút gọn, 0.2; tự nhiên hơn khi lặp nhiều nhưng dễ đọc như danh từ chung); “Liên bang” (0.1; trùng với Federation, loại).
- **Bất định:** thấp. Nếu về sau nguồn cho thấy “Commonwealth” là một liên minh nhiều thực thể, “Khối” vẫn phù hợp.

### 4.3 Entente Alliance

- **Mã đoạn:** p000047, p000049, p000052, p000054, p000056, p000061.
- **Lựa chọn tạm:** **“Liên minh Entente”**; dạng rút gọn “Liên minh” có thể dùng khi ngữ cảnh rõ, nhưng hiện nên giữ đầy đủ để tránh nhầm với “alliance” chung.
- **Độ tin cậy:** 0.7.
- **Lý do:** (1) Nhất quán với ledger vol-01 và ch01–ch02 (b02 đã dùng); nguồn lặp “Entente Alliance” như một tên riêng ổn định (không có “alliance” làm mô tả chung riêng biệt trong 28 đoạn này). (2) Giữ “Entente” nguyên vẹn tránh tự quy ước nghĩa “Hiệp ước”. (3) Nhất quán với “Hiệp ước Londinium” (p000048) là một thực thể khác (hiệp ước, không phải liên minh).
- **Phương án thay thế:** “Liên minh Hiệp ước Entente” (0.15; dài, trùng nghĩa “entente = hiệp ước”); “Liên minh Entente Regadonia” khi có tên đầy đủ (đã có ledger vol-01 `b04-regadonia-entente`, chỉ dùng khi nguồn nêu đủ).
- **Bất định:** thấp.

### 4.4 First Lieutenant

- **Mã đoạn:** p000069 (Weiss, chỉ huy Đại đội Hai).
- **Lựa chọn tạm:** **“Trung úy”**.
- **Độ tin cậy:** 0.6.
- **Lý do:** (1) Nhất quán với ledger ch01 (`vol02-ch01-b02-lieutenant`, `vol02-ch01-b12-lieutenant-map`): Weiss = Trung úy, Serebryakov = Thiếu úy; bản dịch ch01 đã dùng “Trung úy” xuyên suốt cho Weiss (b02, b03, b06–b12). (2) Chuỗi cấp bậc theo ánh xạ phổ biến: Second Lieutenant = Thiếu úy, First Lieutenant = Trung úy, Lieutenant Colonel = Trung tá (p000071 dùng “Trung tá von Lergen”, đã nhất quán). (3) Chưa có căn cứ trong nguồn để xây hệ cấp bậc khác.
- **Phương án thay thế:** “Thượng úy” (0.25; chỉ phù hợp nếu hệ cấp bậc của sách có bậc giữa “Trung úy” và “Đại úy” và nguồn phân biệt); “Trung úy nhất” (0.1; nghe lạ, không dùng).
- **Bất định:** vừa; không ảnh hưởng cốt truyện.

## 5. Rủi ro

- Việc đổi “Ủy viên” → “Nghị viên” ở b03 phải đồng bộ với hai batch khác và các batch sau; nếu coordinator sau này đổi sang “Ủy viên”, phải đổi đồng loạt các batch đã duyệt (b02, b03 và sau).
- M4 (p000049) phụ thuộc cách đọc cụm từ cô đọng của nguồn; nếu coordinator có bản gốc cho thấy nghĩa khác, chỉ cần điều chỉnh câu đó.
- Giọng nội tâm p000071 dùng “mình” là phù hợp DEC-P01-001; không phát hiện lỗi, nhưng cuối đoạn “Thật không khỏi sửng sốt” hơi cứng — mức rất nhẹ, không liệt kê.
- Toàn bộ lựa chọn thuật ngữ ở mục 4 vẫn là đề xuất, không nâng canon.
