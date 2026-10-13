# Báo cáo review vol-02-ch-04-b22 (Claude)

- Phạm vi: 40 đoạn, từ `YS-LN02/Text/part0024.xhtml/p000312` đến `p000351`. Mã đoạn dưới đây viết tắt `pNNNNNN`.
- Đầu vào đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b22, source package b22 (sha256 khớp handoff: `bb7ae685…`), canon (`style-guide.md`, `decisions.md` DEC-P01-001/002, `glossary.yml`, `characters.yml`, `glossary-pending.yml`), `work/run-state/pending-terms.yml` (chỉ để tra mục áp dụng cho b22), bản dịch b22.
- Không đọc package hay bản dịch của lô khác, nên chưa đối chiếu được độ nhất quán xuyên lô. Trong `pending-terms.yml` chưa có mục `chapter4_b22_*`.
- `glossary.yml` và `characters.yml` đang trống. Mọi thuật ngữ, xưng hô và cấp bậc dưới đây là đề xuất, không phải canon.
- Validator/diff-check: not_run. Commit: null.

## Kết luận tổng

- Không có lỗi nghiêm trọng.
- Có 1 lỗi vừa (M1: thiếu toàn bộ dấu nhấn mạnh `*...*`). Cần translator sửa trước khi ký duyệt lô chẵn.
- Có 12 lỗi nhẹ, không chặn lô.
- Số đoạn khớp 40/40, mã đoạn và thứ tự đúng. Không phát hiện đoạn bị bỏ sót hay thêm ý lớn. Các câu hỏi nội tâm giữ đúng đối tượng; không có đảo phủ định hay đảo chủ thể.
- Chưa đạt tiêu chí ký duyệt lô chẵn vì còn 1 lỗi vừa mở.

## Lỗi vừa

### M1 — p000328, p000329, p000332, p000333, p000337, p000347, p000350: thiếu toàn bộ dấu nhấn mạnh
- Vấn đề: theo `xhtml` của package, nguồn có chữ nghiêng ở 7 đoạn. Bản dịch không có dấu `*...*` nào (0/7), trái DEC-P01-002.
- Phạm vi nghiêng cần giữ:
  - p000328: chỉ câu hỏi cuối ("Cô cầu toàn đến mức nào nữa đây?").
  - p000329: chỉ câu hỏi cuối ("Phải dạy một đứa trẻ thế nào…").
  - p000332: toàn đoạn (nội tâm Lergen).
  - p000333: toàn đoạn.
  - p000337: hai vùng riêng: "Nhưng, nhưng…" và câu cuối "Con quái vật trước mặt anh…". Câu giữa ("ở một góc nào đó…") không nghiêng.
  - p000347: chỉ câu hỏi giữa ("Chừng nào mũi giáo… thì có gì phải sợ?").
  - p000350: chỉ phần sau dấu hai chấm ("Mình vừa thoát nạn trong gang tấc.").
- Hậu quả: p000332–p000333 là hai đoạn nội tâm của Lergen liền nhau. Thiếu dấu nghiêng thì lẫn vào lời kể. Ở p000337 mất ranh giới giữa lời kể và giọng lý trí đang cảnh báo.
- Đề xuất: thêm `*...*` đúng phạm vi trên, không đánh dấu thêm chỗ khác.

## Lỗi nhẹ

- **L1 — p000314: "vì nhầm nó là tàu khả nghi"**. Nguồn nói cô đánh chìm tàu ngầm như một tàu khả nghi, còn điều cô không nhận ra là nó thuộc nước trung lập. "Nhầm" làm lệch chỗ sai: thành nhầm về tính khả nghi. Kèm "Dù không biết…" ngay trước nên câu hơi lặp. Đề xuất: "vì coi nó là tàu khả nghi", hoặc "không nhận ra đó là tàu của nước trung lập nên đã đánh chìm tàu ngầm … như một tàu khả nghi". Cũng nên đổi "chỉ có hình thức" thành "chỉ là hình thức".
- **L2 — p000314: "Bộ Chỉ huy Trung ương"**. Nguồn chỉ nêu "Central" (địa điểm hoặc cơ quan trung ương). "Bộ Chỉ huy" là phần thêm. Đề xuất tạm: "Trung ương", ghi pending.
- **L3 — p000318: "thiếu tá quèn"**. Nguồn là "mere major" (chỉ là một thiếu tá), không miệt thị. "Quèn" thêm sắc thái hạ thấp, trái quy tắc style-guide về phán xét không có trong nguồn. Đề xuất: "Chỉ là một thiếu tá mà phải chịu trách nhiệm về mọi thứ."
- **L4 — p000321: "không nói suông"**. Nguồn đối lập giữa lời can thiệp vô hiệu và việc lời đó không chỉ để làm màu. "Nói suông" là lời không đi kèm hành động. Lệch nhẹ sang bình diện khác. Đề xuất: "nhưng đó không phải lời nói cho có". "Lời bênh vực" cho "intercession" chấp nhận được; có thể dùng "lời can thiệp".
- **L5 — p000328: "ở mức vừa đủ"**. Nguồn là "merely satisfactory", tức đạt yêu cầu. "Vừa đủ" gợi sát ngưỡng. Đề xuất "chỉ ở mức đạt yêu cầu".
- **L6 — p000332: nhất quán nội tâm Lergen**. Đoạn dùng "Mình" rồi "chúng tôi" cho "tôi và cô ấy". Đề xuất "hai người". "Quả cầu điên loạn" (ball of insanity) đọc lạ; có thể "khối điên loạn". Lưu ý: DEC-P01-001 chỉ chốt "mình" cho nội tâm Tanya, không mở sang chủ thể khác. Dùng "mình" cho Lergen là đề xuất tạm, ghi pending xưng hô.
- **L7 — p000333: "con người bình thường"**. Nguồn là "mere person" (chỉ là một con người). "Bình thường" thêm nghĩa "ordinary". Đề xuất "một con người thông thường" hoặc "một con người thôi".
- **L8 — p000334: cấu trúc điều kiện**. "Nếu nền tảng … không lệch lạc, thì … là điều không thể có" tương đương về logic nhưng khó đọc. Đề xuất: "Trừ phi nền tảng làm người của cô đã lệch lạc, nếu không thì mức bất tương xứng này là không thể."
- **L9 — p000335: "không có ý kiến gì"**. Nguồn là không ai có vấn đề, tức không phản đối. "Không có ý kiến" dễ hiểu là không bình luận. Đề xuất: "không ai ở Bộ Tổng tham mưu có điều gì phàn nàn về hành động của cô".
- **L10 — p000336: "chỉ thể hiện" và "lời chúc mừng năm mới"**. "Chỉ" là phần thêm. "Season's greetings" là lời chúc theo mùa lễ nói chung; "năm mới" thu hẹp. Đề xuất bỏ "chỉ", dùng "lời chúc theo mùa" hoặc "lời chúc dịp lễ".
- **L11 — p000341, p000347**. p000341 "cân nhắc cho cô" nghe như suy tính; nguồn là sự chiếu cố trong giới hạn quyền hạn. Đề xuất "anh chiếu cố cô hết mức quyền hạn cho phép". p000347 "theo phép lịch sự" lệch khỏi "dutifully/required" (vì bổn phận). Đề xuất "đúng theo bổn phận". "chưa chĩa" làm điều kiện hóa thành "chưa tới lúc"; nguồn là "không chĩa". Đề xuất "chừng nào … không chĩa vào".
- **L12 — p000349–p000351: danh xưng và đại từ**.
  - p000349: nguồn chỉ nêu "Major von Degurechaff"; bản dịch thêm "Pháp sư" và "Tanya". Đề xuất "Thiếu tá von Degurechaff". "Dù có biết hay không khi cúi chào" mơ hồ về phạm vi; đề xuất đặt "khi cúi chào" lên đầu câu.
  - p000350 dùng "Mình", p000351 dùng "Tôi" cho cùng giọng Tanya. DEC-P01-001 phân biệt lời kể ngôi ba và nội tâm, chưa quy định lời kể ngôi nhất. Đề xuất tạm: giữ "tôi" cho p000351 (kể ngôi nhất, không nghiêng) và ghi pending, hoặc dùng "mình" cho nhất quán. Nên có người duyệt xác nhận.
  - p000351: "Đại tá von Lergen" theo nguồn. Chưa đối chiếu được cấp bậc ở các lô khác (b21 từng ghi nghi vấn Trung tá/Đại tá).

## Nhận xét tốt (không cần sửa)

- p000318, p000337: hai "luồng khí" và "lý trí cảnh báo" giữ đúng điểm nhìn Lergen.
- p000323, p000326: giữ được "chỉ một người" và hình ảnh búp bê.
- p000331: "Không để sót một con tàu nào" nhất quán với hướng đã đề xuất ở b21.
- p000342: "hạm đội" được nêu rõ đúng chủ thể của "it".
- Xưng hô: Tanya gọi Lergen "ngài", Lergen gọi Tanya "cô" nhất quán trong lô. Không suy ra thêm quan hệ.

## Thuật ngữ và đề xuất (chưa canon)

| Thuật ngữ nguồn | Bản dịch hiện tại | Khuyến nghị | Ghi chú |
|---|---|---|---|
| Central (p000314) | Bộ Chỉ huy Trung ương | "Trung ương", pending | Không đủ căn cứ để thêm "Bộ Chỉ huy". |
| marine mages (p000322) | pháp sư hải quân | giữ tạm "pháp sư hải quân"; thay thế "pháp sư hải chiến" | Mục mới, ghi vào ledger. |
| Commonwealth (p000314) | Khối Thịnh vượng chung | giữ tạm | Cần nhất quán với b21. |
| General Staff Office / General Staff (p000335, p000351) | Bộ Tổng tham mưu | giữ tạm | Hai cách gọi nguồn cùng một bản dịch, chấp nhận được. |
| war game (p000342) | diễn tập chiến tranh | giữ tạm; thay thế "diễn tập quân sự" | Mục mới. |
| Northern Sea, Rhine (p000342) | Biển Bắc, Rhine | giữ tạm; "Rhine" có thể là mặt trận, không thêm | Cần khớp với "Hạm đội Biển Bắc" của b21. |
| Colonel von Lergen (p000351) | Đại tá von Lergen | giữ literal, ghi uncertainty | Cấp bậc theo nguồn; kiểm tra xuyên lô. |
| Magic Major (p000349–p000350) | Thiếu tá Pháp sư | giữ tạm ở p000350; p000349 bỏ "Pháp sư" và "Tanya" | Theo nguồn từng đoạn. |

## Tiêu chí ký duyệt lô chẵn

- Nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic: đạt, chỉ còn lỗi nhẹ.
- Đại từ (DEC-P01-001): đạt có ghi chú pending ở L6 và L12.
- Nhấn mạnh (DEC-P01-002): chưa đạt (M1).
- Thuật ngữ pending: không có mục mới bắt buộc chặn; cần ghi 3 đề xuất mới.
- Kết luận: chưa ký duyệt. Cần translator sửa M1 (nên sửa luôn L1, L3, L9, L11, L12), rồi review lại phần đã sửa.
