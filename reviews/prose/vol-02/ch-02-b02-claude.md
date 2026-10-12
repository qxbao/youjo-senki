# Báo cáo phản biện văn phong và ngữ nghĩa — vol-02-ch-02-b02 (batch chẵn)

- **Người phản biện:** Claude (reviewer, chỉ ghi báo cáo, không sửa bản dịch, handoff, canon, ledger hay run-state).
- **Phạm vi:** `handoffs/vol-02/ch-02-b02.yml`, `work/vol-02/batches/ch-02-b02-source.jsonl`, `translations/vol-02/ch-02-b02.jsonl`, `canon/*`, `work/run-state/pending-terms.yml` (mục `chapter2_b02_translation_proposals` và các mục b01/ch01 liên quan). Báo cáo không trích văn bản nguồn.
- **Mã đoạn:** viết tắt `pNNNNNN` = `YS-LN02/Text/part0014.xhtml/pNNNNNN`.

## 1. Kết luận

- **Kết luận:** `pass_with_fixes`.
- **Mức nghiêm trọng:** serious = 0; moderate = 3 (M1–M3); minor = 8 (m1–m8).
- **next_action:** người giữ quyền sửa xử lý M1–M3, cân nhắc các mục minor, chạy lại validator rồi commit. Chỉ cần reviewer xác nhận nhanh p000025, p000026, p000043 sau khi sửa.
- **Pending terms:** hai nhóm (nghị viên/chức danh; Grand Duchy) đều còn `provisional_non_canon`; khuyến nghị ở mục 4. Không nâng lên canon.

## 2. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự ID | Đạt: 19 đoạn, p000025–p000043, đúng thứ tự, khớp 1:1 với gói nguồn. |
| `source_sha256` mỗi record | Đạt: khớp hash trong handoff. |
| Hash gói nguồn | Đạt: `5b210418…ae1cc5ae034` khớp handoff. |
| `glossary_version` mỗi record | Đạt: khớp handoff. |
| Nhấn mạnh (DEC-P01-002) | **Chưa đạt:** nguồn có nhấn mạnh ở p000025 (câu mở đầu), p000029, p000041. Bản dịch có `*...*` ở p000029 và p000041 (đúng phạm vi) nhưng thiếu ở p000025 → M1. |
| Ghi chú làm việc lọt vào translation | Không có. `notes` rỗng dù có 2 nhóm pending (xem m8). |
| Thứ tự/người nói | Ổn: p000036 và p000037 là Abensoll; p000040 là Cazor (suy từ p000042 gọi tên Cazor); p000042 là Abensoll; p000043 là Cazor. |

## 3. Phát hiện

### Moderate

- **M1 — p000025: thiếu nhấn mạnh ở câu mở đầu.**
  Nguồn có nhấn mạnh (thẻ em) trên câu ngắn mở đầu đoạn; bản dịch viết “Khoan đã.” không có dấu. DEC-P01-002 yêu cầu `*...*` khi nguồn có nhấn mạnh tương ứng. Đề xuất: đánh dấu đúng phạm vi câu ngắn đó (`*Khoan đã.*`), không mở rộng ra phần sau. Độ tin cậy 0.9.

- **M2 — p000043 (và p000033): cùng một quốc gia bị gọi bằng hai tên và viết hoa không theo quy ước.**
  Nguồn tiếng Anh gọi Dacia là “Principality of Dacia” ở p000033 nhưng “Grand Duchy” ở p000043; ngữ cảnh (p000038, p000042–p000043: nói về việc nước này tham chiến để giảm gánh cho Liên minh, và Cazor bị “đối xử như Dacia thứ hai”) cho thấy gần như chắc là cùng chủ thể (độ tin cậy ~0.8; đây là suy luận từ ngữ cảnh, chưa phải xác nhận lore). Bản dịch dùng “Công quốc Dacia” rồi “Đại Công quốc”, người đọc dễ hiểu thành hai nhà nước khác nhau; ngoài ra “Đại Công quốc” viết hoa chữ “Công” giữa cụm, trái quy ước đang dùng (“Công quốc Dacia”, “Liên minh Entente”: chỉ viết hoa âm tiết đầu của danh từ loại). Đề xuất: xem mục 4.2; tối thiểu sửa thành “Đại công quốc” để theo quy ước viết hoa, và ghi trong ledger rằng đây có thể là Dacia. Không tự thêm “Dacia” vào p000043 khi nguồn không nêu.

- **M3 — p000025 / p000026 / p000027: “homeland” và “fatherland” không còn được phân biệt.**
  p000025 dịch “homeland” là “quê hương” rồi “fatherland” là “Tổ quốc”; p000026 lại dịch “homeland” (nguồn dùng từ này, không phải “fatherland”) thành “Tổ quốc” và dịch “home” thành “quê nhà”. Ledger b01 đã gán fatherland → Tổ quốc (alt: quê hương). Hậu quả: câu chủ đề của đoạn (homeland vs. home trong tim người dân) bị nhập vào từ vựng của “fatherland”, và hai đoạn kề nhau dùng hai từ cho cùng một từ nguồn. Đề xuất: p000026 dùng “Quê hương không chỉ là lãnh thổ; chừng nào mái nhà còn hiện hữu trong trái tim người dân…” (hoặc “quê nhà” cho “home” như hiện tại) để khớp p000025 (homeland → quê hương), giữ “Tổ quốc” riêng cho “fatherland” (p000025 cuối, p000027, p000029, p000032). Độ tin cậy 0.7; phương án thay thế: đổi cả p000025 sang “Tổ quốc”, nhưng sẽ trùng với “fatherland” cùng đoạn.

### Minor

- **m1 — p000030: “wife and daughter” → “vợ con”.** Nguồn nêu cụ thể con gái; bản dịch khái quát. Đề xuất “vợ và con gái” (khớp câu trước “bên con mấy”, nên giữ “con” số ít ở đó).
- **m2 — p000030: “immodest” → “tự phụ”.** “Tự phụ” nặng hơn nguồn (thiếu khiêm tốn/không đúng mực), vi phạm hướng dẫn không thêm sắc thái đạo đức. Đề xuất “Dù có phần thiếu khiêm tốn” hoặc “Dẫu hơi ngượng”.
- **m3 — p000029: “Ta … ngươi, hỡi Tổ quốc” so với nội tâm “mình”.** Giọng thề cổ phù hợp “thee/O Fatherland”, nhưng ledger b01 đặt nội tâm của Sue là “mình”; “Ta” là đại từ khác. Chấp nhận được vì là lời thề trang trọng; nên ghi vào ledger để giữ nhất quán ở các batch sau.
- **m4 — p000038: mất liên kết hệ quả “to the point that”.** Nguồn: thái độ xấu đi nhanh *đến mức* Cộng hòa gần như không tiếp. Bản dịch tách hai câu, liên kết thành chuỗi thời gian (“Sau khi Dacia can dự”). Đề xuất nối bằng “đến mức”. Cũng nên giữ nguyên mơ hồ “Dacia can dự” như nguồn (đừng làm rõ thêm).
- **m5 — p000041: “cho mình” gây mơ hồ.** Trong suy nghĩ có “chúng ta”, “cho mình” có thể bị đọc là “cho chúng ta”. Đề xuất “cho chính họ” hoặc “cho phía họ”.
- **m6 — p000043: “wretched” bị làm nhẹ thành “chẳng dễ chịu chút nào”.** Nguồn là cảm thán mỉa/khó chịu mạnh hơn; đề xuất “nghe thật tệ hại” hoặc “nghe thật khó nuốt”.
- **m7 — p000033: cụm “warrior’s fanfare”.** “Màn phô trương binh đao” đúng hướng; “thứ nghe chẳng khác nào khúc nhạc vui” hơi lạc điệu so với “music to the ears” (nghe vui tai/hả dạ với nghị viên). Có thể “nghe như nhạc êm tai đối với các nghị viên”. Mức độ nhẹ.
- **m8 — Ghi chú/ledger.** `notes` rỗng nhưng ledger đã có hai nhóm pending; nên cân nhắc ghi nhóm “homeland vs fatherland” (M3) và đại từ lời thề của Sue (m3) vào ledger.

## 4. Phản biện đề xuất thuật ngữ (tạm thời, không canon)

### 4.1 “councilor / councilor titles”

- **Mã đoạn:** p000031, p000035, p000037, p000041, p000042, p000043 (ledger liệt kê 5 mã, thiếu p000041 vì dùng “mười nghị viên”).
- **Khuyến nghị tạm:** giữ **“nghị viên”** cho “councilor”; chức danh viết hoa khi đi kèm tên: **“Nghị viên Ngoại giao Abensoll”**, **“Nghị viên Lục quân Cazor”**, **“Nghị viên Cazor”**; dạng chung viết thường (“các nghị viên”, “nghị viên mới”). Bản dịch hiện đã áp dụng đúng và nhất quán trong batch.
- **Độ tin cậy:** 0.6.
- **Lý do:** ngắn, tự nhiên, dùng được làm tiền tố trước tên, bám sát nghĩa “thành viên của một hội đồng”, không hứa hẹn nhiều hơn nguồn. Batch này cho thấy một hội đồng gồm mười người, có phân công theo lĩnh vực (ngoại giao, lục quân), nhưng chưa xác lập hội đồng này mang tính lập pháp hay hành pháp; lựa chọn trung tính này tránh tự quyết điều đó.
- **Phương án thay thế:** (a) “ủy viên hội đồng” / “Ủy viên Ngoại giao”, “Ủy viên Lục quân”: sát hơn nếu hội đồng là cơ quan hành pháp theo lĩnh vực, nhưng dài hơn và dễ gợi sắc thái chính trị hiện thực của tiếng Việt; (b) “thành viên hội đồng”: quá chung, khó dùng làm chức danh trước tên; (c) “bộ trưởng”: tự suy diễn chức năng, không dùng.
- **Điều kiện xem lại:** nếu batch/volume sau mô tả rõ quyền hạn hội đồng (lập pháp hay nội các), cân nhắc đổi sang “ủy viên” và thay đồng loạt. Không ảnh hưởng cốt truyện nên không cần hỏi người dùng.
- **Ghi chú ledger:** nên ghi thêm quy tắc viết hoa chức danh trước tên và thêm mã p000041.

### 4.2 “Grand Duchy”

- **Mã đoạn:** p000043 (liên quan p000033, p000038, p000042 về nhận diện chủ thể).
- **Khuyến nghị tạm:** **“Đại công quốc”** (chỉ viết hoa âm tiết đầu khi là tên riêng dạng rút gọn, giống “Công quốc Dacia”, “Liên minh Entente”), dùng làm từ chỉ chính quốc gia mà batch này gọi là Dacia. Độ tin cậy 0.6.
- **Lý do:** dịch sát nghĩa “Grand Duchy”, là cách gọi phổ biến trong tiếng Việt cho thể chế này, không thêm tên riêng mà nguồn không nêu ở p000043, và đúng quy ước viết hoa đang dùng. Dạng “Đại Công quốc” trong bản dịch chỉ khác về viết hoa (xem M2).
- **Phương án thay thế:** (a) “Công quốc” — thống nhất với “Principality” của ch01 và p000033, nhưng mất “Đại”, tức che đi chỗ nguồn tự đổi tên; độ tin cậy 0.35; (b) “Đại công quốc Dacia” — rõ chủ thể nhưng thêm tên không có trong p000043; chỉ cân nhắc nếu coordinator xác nhận nguồn/volume sau gọi Dacia là Grand Duchy; (c) giữ “Đại Công quốc” như hiện tại — chấp nhận được, mức viết hoa không theo quy ước.
- **Bất định:** việc nguồn tiếng Anh dùng hai danh xưng cho Dacia là sự thật của nguồn; việc hai danh xưng cùng chỉ một nước là suy luận từ ngữ cảnh (~0.8). Không dùng làm căn cứ lore; nếu các batch sau gọi nước này rõ là “Grand Duchy of Dacia”, coordinator nên rà lại ch01 để quyết định thống nhất (không ảnh hưởng cốt truyện).

### 4.3 Thuật ngữ cần ghi thêm (đề xuất, tùy coordinator)

- “homeland” → “quê hương”; “fatherland” → “Tổ quốc” (nhất quán với ledger b01; xem M3). Độ tin cậy 0.65.
- “Rhine front” → “mặt trận Rhine”: khớp ch01-b04 và các batch trước; p000040. Không có vấn đề.

## 5. Rủi ro

- Nhận diện Grand Duchy = Dacia dựa trên suy luận ngữ cảnh; nếu sai (một nước thứ ba), M2 chỉ còn ý nghĩa viết hoa.
- Người nói p000040 là Cazor suy từ p000042; nếu bản gốc khác thì chỉ đổi người đối thoại, không đổi bản dịch.
- Các batch sau (b03 trở đi) sẽ dùng “Nghị viên” dày đặc; đổi thuật ngữ về sau sẽ tốn công sửa hàng loạt.
