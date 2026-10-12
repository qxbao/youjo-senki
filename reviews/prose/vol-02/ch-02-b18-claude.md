# Báo cáo phản biện — vol-02-ch-02-b18 (Claude)

- **Task:** vol-02-ch-02-b18; checkpoint_generation 426.
- **Phạm vi:** 33 đoạn, từ `YS-LN02/Text/part0014.xhtml/p000480` đến `.../p000512`.
- **Đầu vào đã đọc:** `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b18, source package b18, `translations/vol-02/ch-02-b18.jsonl`, `canon/` (style-guide, decisions, glossary, characters, glossary-pending), `work/run-state/pending-terms.yml` (mục b18 và các mục thuật ngữ liên quan ở batch khác, chỉ đọc sổ pending).
- **Xác minh package:** SHA-256 của `work/vol-02/batches/ch-02-b18-source.jsonl` là `8e0a34a6…415576f`, khớp `source_package_sha256` trong handoff. Có đủ 33 đoạn nguồn và 33 đoạn dịch, mã đoạn khớp một–một.
- **Không** mở batch dịch hay package nguồn nào khác; không mở EPUB/PDF; không sửa bản dịch, handoff, ledger, canon hay run-state. Báo cáo không trích câu nguồn.
- **Kết luận:** không có lỗi nghiêm trọng. Có 3 lỗi vừa (một đoạn mất nhấn mạnh, một chỗ có nguy cơ thu hẹp đối tượng, một nhóm đại từ trần thuật lệch lựa chọn đã ghi) và 11 góp ý nhẹ. Bản dịch nhìn chung sát nghĩa, không thấy bỏ sót hay thêm ý đáng kể; các lỗi vừa nên được người giữ quyền sửa xử lý trước khi tính hoàn tất.

## 1. Lỗi vừa

### M1 — p000509: mất nhấn mạnh của câu một từ
- **Căn cứ:** XHTML nguồn có thẻ `em` quanh câu ngắn đầu tiên của lời “tuyệt vời”; bản dịch để chữ thường, không có `*...*`. Các đoạn p000512 (hai chỗ nhấn mạnh) đã được giữ đúng. DEC-P01-002 và checkpoint `emphasis` của handoff yêu cầu giữ đúng phạm vi nhấn mạnh có trong nguồn.
- **Đề xuất:** bọc đúng câu một từ tương ứng bằng `*...*`; không nhấn mạnh thêm chỗ khác trong đoạn.

### M2 — p000498: “cách xưng hô chuẩn mực” có nguy cơ thu hẹp đối tượng
- **Căn cứ:** danh từ nguồn chỉ “lời nói/phát biểu được trình bày chỉn chu”, không nhất thiết là lời xưng hô. Lời ở p000497 không chứa danh xưng hay cấp bậc nào, nên “xưng hô” khó có chỗ bám trong đoạn kề trước; khả năng hợp lý hơn là Tanya hài lòng vì lần này lời gọi/đề nghị đúng quy trình, rõ ràng (đối lập với việc bị quở ở p000491–p000493). Style guide yêu cầu không thu hẹp đối tượng của nhận định.
- **Độ bất định:** vừa phải; chưa đối chiếu được bản gốc ngôn ngữ khác nên chưa chắc 100% nguồn trỏ đến lời ở p000497 hay thủ tục gọi ở p000494–p000496.
- **Đề xuất:** dùng cách nói trung tính, ví dụ “mỉm cười trước lời trình bày chỉn chu/chuẩn mực ấy”; tránh “xưng hô”.

### M3 — p000498, p000500, p000501, p000505: đại từ trần thuật về Tanya dùng “cô”
- **Căn cứ:** DEC-P01-001 (đã duyệt) chọn “nó” cho trần thuật về Tanya ở giai đoạn này; sổ pending Vol 2 (`vol02-ch02-b06-tanya-narration`, `vol02-ch01-b14-tanya-narration`) tạm chọn lặp tên hoặc bỏ chủ ngữ để tránh đại từ có giới tính, “cô” chỉ là phương án thay thế. Bản dịch dùng “cô” ở bốn đoạn, trong khi p000504 và p000512 dùng “Tanya”. Ngoài ra p000501 dùng “mình” ở câu trần thuật ngôi ba (“hơn mình tưởng”), trộn với “mình” nội tâm ngôi nhất.
- **Đề xuất:** thay “cô” bằng “Tanya” hoặc bỏ chủ ngữ; ở p000501 dùng “hơn dự tính/hơn Tanya tưởng”. Nếu coordinator muốn dùng “nó” theo DEC-P01-001 thì áp dụng nhất quán cho cả batch. Đây là chọn lựa tạm, không phải canon.

## 2. Góp ý nhẹ

- **L1 — p000497 (thuật ngữ rear guard, xem mục 3):** “Ta điều họ làm hậu quân nhé?” — “Ta” mang sắc thái người trên/cổ; người nói chưa rõ cấp bậc. Đề xuất cách nói trung tính, ví dụ “Có nên cho họ làm … không?” hoặc “Chúng tôi xin điều họ làm … được chứ?” (chỉ dùng nếu coordinator chấp nhận suy luận về quan hệ).
- **L2 — p000493 (Heinrich’s Law, xem mục 3):** bản dịch dùng “Định luật … quy tắc kinh nghiệm” liền nhau; hơi nặng, vì nguồn tự mô tả đây là quy tắc kinh nghiệm. Chấp nhận được; xem mục 3.
- **L3 — p000490:** “kẻ cẩu thả” thêm sắc thái miệt thị và “cẩu thả” (làm ẩu) lệch nhẹ so với “bất cẩn”. Đề xuất “những người bất cẩn”. “nội quy, quy định” thiên về nội quy cơ quan; nguồn dùng cặp từ chung chung — cân nhắc “quy tắc, quy định”.
- **L4 — p000492:** “điều lệnh” là thuật ngữ cụ thể (điều lệnh đội ngũ/nội vụ); nguồn dùng từ chung “regulations” như ở p000490/p000493. Để nhất quán, cân nhắc “kỷ luật và quy định của quân đội”.
- **L5 — p000485:** “thiết bị dò nhiệt” thêm từ “thiết bị”; nguồn nêu phương thức dò nhiệt đối lập với radar. Cân nhắc “dò nhiệt hoặc radar”.
- **L6 — p000495:** “Có người nghe giọng điệu có vẻ là nhân vật quan trọng lên sóng” vụng cú pháp. Đề xuất “Một người nghe có vẻ là nhân vật quan trọng vừa lên sóng”.
- **L7 — p000506, p000511:** “các anh” (506) và “anh” số ít (511) cho đối tượng là tiểu đoàn; ledger (`vol02-ch01-b04-address-to-unit`) tạm dùng “mọi người” để tránh suy diễn giới tính/tuổi. Đối tượng của p000511 không rõ (cả tiểu đoàn hay một người). Đề xuất “mọi người” cho cả hai, hoặc “các anh” nhất quán nếu coordinator chấp nhận.
- **L8 — p000504, 508, 510:** “quân chi viện”, “đơn vị tiếp viện”, “quân tiếp viện” dùng lẫn lộn cho cùng khái niệm reinforcements. Đề xuất chọn một cách và áp dụng nhất quán trong batch. p000508 “Một số đơn vị” thêm chữ “đơn vị”, và “Vui lên nào” nghiêng về “cheer up” hơn “rejoice” (cân nhắc “Mừng đi”).
- **L9 — p000509:** “điện báo viên” thường chỉ người điện báo (telegraph); radio operator nên là “báo vụ viên” hoặc “nhân viên vô tuyến”. Chưa có mục ledger cho thuật ngữ này.
- **L10 — p000505:** “quân ta” thêm lập trường sở hữu; nguồn chỉ nói đại từ ngôi ba. Đề xuất “phía mình/họ” hoặc bỏ chủ ngữ. “nóng lòng” đúng ý “couldn’t wait”.
- **L11 — p000503:** “Cảm ơn” hơi mỏng so với câu cảm ơn trang trọng; cân nhắc “Xin cảm ơn”. “Hết” cho “Over” khớp ledger (`b05-radio-over`), giữ nguyên.

## 3. Thuật ngữ đề xuất (không nâng canon)

### rear guard — p000497 (ledger `vol02-ch02-b18-rear-guard`)
- **Bằng chứng trong ngữ cảnh:** (a) đề nghị dùng các đơn vị đã tái tổ chức và vừa rút lui; (b) p000500 mong họ làm “lá chắn”/quân tốt; (c) p000507 nêu lợi ích là chiến đấu mà không phải lo phía sau. Nghĩa vì thế nghiêng về lực lượng yểm trợ/bảo vệ phía sau đội hình đang giao chiến, không phải lực lượng phục vụ khu vực hậu phương. Chưa thấy chứng cứ nói đây là cuộc rút lui, nên tránh “đoạn hậu” (hàm ý yểm trợ rút lui).
- **Khuyến nghị tạm:** “đơn vị hậu vệ” (đúng thuật ngữ hành quân “tiền vệ/hậu vệ” trong tiếng Việt quân sự; thêm “đơn vị” để tránh nghĩa hậu vệ bóng đá). Độ tin cậy ~0.5.
- **Phương án khác:** “hậu quân” (giữ của translator; gọn, nhưng cổ, dễ hiểu là một phần trong bố trí tiền/trung/hậu quân thời xưa hay “lực lượng hậu phương”); “lực lượng bảo vệ phía sau” (an toàn nghĩa nhưng mất tính thuật ngữ).
- **Bất định:** tôi chưa kiểm tra được cách dùng trong các bản dịch quân sự hiện đại; không ảnh hưởng cốt truyện. Không cần hỏi người dùng; coordinator ghi lựa chọn vào ledger/handoff.

### Heinrich’s Law — p000493 (ledger `vol02-ch02-b18-heinrichs-law`)
- **Bằng chứng:** nguồn gọi đây là quy tắc kinh nghiệm do một người làm bảo hiểm tìm ra khi thống kê, và dùng nó để chứng minh lỗi nhỏ tích tụ thành tai nạn lớn. Đây là tên riêng của nguyên lý an toàn lao động có thật; không thêm số liệu hay chi tiết không có trong nguồn.
- **Khuyến nghị tạm:** giữ “Định luật Heinrich” (độ tin cậy ~0.55): cách gọi này phổ biến trong tài liệu an toàn lao động tiếng Việt theo hiểu biết của tôi, nhưng chưa tra lại.
- **Phương án khác:** “Quy luật Heinrich” (trung tính hơn, hợp với “quy tắc kinh nghiệm”); “Quy tắc Heinrich” (nếu đổi cụm đi sau thành “nguyên tắc kinh nghiệm” để tránh lặp). Chọn phương án nào cũng phải nhất quán toàn tập.
- **Bất định:** “định luật” gợi sắc thái chặt chẽ hơn “rule of thumb”; mức độ này nhẹ và không đổi nghĩa.

### Đề xuất bổ sung (chưa có trong ledger)
| source_term | proposed_vi | phương án khác | đoạn | ghi chú |
|---|---|---|---|---|
| radio operator | báo vụ viên | nhân viên vô tuyến; điện báo viên | p000509 | tránh nghĩa telegraph; độ tin cậy ~0.5 |
| reinforcements / backup | quân tiếp viện (thống nhất một cách gọi) | quân chi viện | p000498, 504, 508, 510, 512 | chỉ cần nhất quán; độ tin cậy ~0.5 |
| well-made address (nhận định về lời nói) | lời trình bày chỉn chu | lời báo cáo chuẩn mực | p000498 | tránh thu hẹp thành “xưng hô”; chưa chắc về đối tượng chính xác |

## 4. Kiểm tra theo tiêu chí
- **Nghĩa/thiếu sót/thêm ý:** không bỏ sót hay thêm ý đáng kể ngoài các chỗ ghi ở trên (L3, L5, L8, L10).
- **Đại từ:** nội tâm dùng “mình” đúng DEC-P01-001; trần thuật lệch ở M3. “mình” trong thoại trực tiếp ở p000481 và p000483 chấp nhận được (tự nói); không suy diễn quan hệ.
- **Nhấn mạnh:** p000512 đúng (hai chỗ); p000509 thiếu (M1). Các đoạn khác không có nhấn mạnh trong nguồn và bản dịch cũng không thêm.
- **Văn phong:** nhìn chung tự nhiên; chỗ cần chỉnh ở L6. Giọng giả vờ vui của Tanya ở p000499 hơi cộc nhưng chấp nhận được.
- **Thuật ngữ khớp ledger:** Tiểu đoàn Viper, Cụm tập đoàn quân phương Bắc, hiệu gọi, Pixie, “Hết” cho Over.

## 5. Phạm vi không có quyết định
Không có mục nào ảnh hưởng cốt truyện; không cần hỏi người dùng. Mọi lựa chọn trên là đề xuất tạm, chưa nâng thành canon.
