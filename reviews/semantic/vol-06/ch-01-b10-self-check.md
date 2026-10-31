# Báo cáo tự kiểm dịch thuật — `vol-06-ch-01-b10`

- **Nhiệm vụ:** `vol-06-ch-01-b10` (Sign-off: `vol-06-ch-01-b10-translator-signoff`)
- **Tập / Chương:** `vol-06`, chương `1`
- **Phạm vi đoạn:** `YS-LN06/Text/part0008.html/p000354` → `YS-LN06/Text/part0008.html/p000394` (41 đoạn)
- **Tác tử dịch:** `argon-low`
- **Trạng thái dòng:** `reviewed` (41/41 dòng)

## 0. Xử lý Argon Review (`vol-06-ch-01-b10-argon-review`)
- **Finding đã xử lý:**
  - `YS-LN06/Text/part0008.html/p000371` (`moderate`): Bổ sung trạng từ `"một cách chủ quan"` vào cụm động từ để giữ trọn nghĩa và sắc thái tự trào/nghịch lý của nguyên văn: `"Hơn bất cứ điều gì, Tanya tự hào về khả năng nhìn nhận bản thân một cách chủ quan của mình."`
- **Kiểm tra `locked_choices` & `pending_term_recommendations`:** Toàn bộ 41 đoạn (`p000354`–`p000394`) tuân thủ đầy đủ các `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-06/ch-01-b10-argon-review.yml`.
- **Cập nhật trạng thái:** Đã chuyển `status` của toàn bộ 41/41 dòng trong `translations/vol-06/ch-01-b10.jsonl` từ `draft` sang `reviewed`.

## 1. Kiểm tra nghĩa, logic và mạch trần thuật
- Đảm bảo truyền tải đầy đủ tất cả chi tiết trong 41 đoạn từ `p000354` đến `p000394`, giữ nguyên các mệnh đề điều kiện, giả định, phủ định và quan hệ nhân quả:
  - Ở `p000354`–`p000368`: Thiếu tá Weiss nghiêm nghị nhận lệnh lập đơn vị với quyết tâm cao độ và hỏi về nhiệm vụ. Khi Tanya đáp gọn lỏn là đi cướp bóc, cả Weiss lẫn viên sĩ quan phụ tá Serebryakov (vốn im lặng từ nãy) đều sững sờ, hỏi lại bằng giọng the thé với gương mặt co giật biểu cảm như tranh vẽ. Tanya vội giải thích đó chỉ là câu đùa để làm dịu bầu không khí, nhưng nhìn Weiss vất vả cố thả lỏng và lời nhắc nhở thẳng thắn của hai cấp dưới, nó nhận ra khiếu hài hước và quan niệm thẩm mỹ của mình khác hẳn họ dù đã gắn bó lâu dài; nó khẳng định mình là người lính tuân thủ luật chiến tranh và điều lệnh quân sự, không có ý định đẩy tổ quốc vào thế đối đầu với tính hợp pháp hiện đại.
  - Ở `p000369`–`p000387`: Tanya lấy lại vẻ điềm tĩnh, tự nhủ cấp dưới dù thiếu khiếu hài hước nhưng vẫn làm việc chuyên nghiệp, đồng thời tự nhận bản thân quá nghiêm túc và việc tập pha trò chưa mấy tiến bộ nên có thể bị coi là cứng nhắc. Nó chuyển sang giọng công việc thực tế để phân tích tình hình với Weiss: mùa đông Liên bang đang làm tê liệt các tuyến tiếp vận gây ra hỗn loạn; dù Hội đồng Tự trị đã được thành lập nhờ sự dàn xếp của Tướng von Zettour và các trận đánh chống nổi dậy phối hợp ở hậu phương đạt kết quả khả quan giúp cải thiện hậu cần, tình hình vẫn chưa thể xoay chuyển ngay vì thiếu vật chất thực tế ngoài chiến trường—cụ thể là năng lực sản xuất trang bị chống rét không đáp ứng kịp nhu cầu. Cả Weiss và Serebryakov đều nắm bắt nhanh và gật đầu thấu hiểu bối cảnh Kampfgruppe Salamander đang bị nhu cầu hoàn tất chuẩn bị mùa đông thúc bách.
  - Ở `p000388`–`p000394`: Tanya suy ngẫm rằng ghét lãng phí và giảm thiểu rủi ro không loại trừ nhau, tiếc chút công sức mà làm tăng vọt nguy cơ sự cố chỉ là sự lười biếng đáng bị xử bắn, nên nó luôn tuân thủ quy trình. Nó nêu rõ nhu cầu phải kiếm được trang bị tối ưu để phát huy tối đa sức mạnh đơn vị; khi Weiss hỏi lấy ở đâu với vẻ bán tín bán nghi nhưng đã bắt trúng ẩn ý, Tanya dẫn chiếu luật chiến tranh và Quy tắc Chiến tranh trên Bộ mà nó từng học kỹ ở học viện (với phương châm lách luật chứ không phạm luật): dù Liên bang chưa phê chuẩn luật chiến tranh nhưng Lục quân Đế quốc vẫn tuân thủ quy tắc giao chiến về nguyên tắc, trong đó cho phép thu giữ tài sản quốc gia của địch bao gồm tiền mặt, ngân quỹ, chứng khoán có giá có thể chuyển nhượng thuộc diện động sản thuần túy của nhà nước, cùng kho vũ khí, phương tiện vận tải, kho tàng, vật tư tiếp tế và mọi tài sản nhà nước có thể dùng cho hoạt động quân sự.

## 2. Kiểm tra đại từ và xưng hô (`DEC-P01-001`)
- **Trần thuật ngôi thứ ba về Tanya:** Dùng nhất quán tên gọi `Tanya` hoặc đại từ `nó` (`p000355`, `p000360`, `p000361`, `p000369`, `p000372`, `p000374`, `p000375`, `p000386`, `p000392`, `p000393`).
- **Nội tâm tự quy chiếu của Tanya:** Dùng `mình` cho ngôi thứ nhất số ít (`p000363`, `p000367`, `p000371`, `p000372`, `p000374`, `p000380`), `chúng tôi` khi nhắc tới khoảng thời gian gắn bó giữa mình và hai cấp dưới (`p000367`), và `bạn` cho chủ ngữ khái quát chỉ người sĩ quan nói chung (`p000384`).
- **Đối thoại giữa Tanya với Thiếu tá Weiss và Trung úy Serebryakov:**
  - Tanya xưng `tôi` / `chúng ta`, gọi hai cấp dưới là `hai người` (`p000362`, `p000366`, `p000370`, `p000376`, `p000381`, `p000383`, `p000387`, `p000390`, `p000394`).
  - Weiss và Serebryakov xưng `tôi` / `chúng tôi` / `chúng ta`, gọi Tanya là `Trung tá` (`Colonel` / `ma’am`) kèm sắc thái lễ phép (`p000354`, `p000356`, `p000358`, `p000359`, `p000364`, `p000365`, `p000382`, `p000391`), và Weiss gọi Serebryakov là `Trung úy` (`p000365`).

## 3. Kiểm tra nhấn mạnh / chữ nghiêng (`DEC-P01-002`)
- Đối chiếu chính xác thẻ `<html:em>` từ dữ liệu nguồn:
  - `p000361`: `*Dù chưa sánh được với bức* Tiếng Thét*, họ vẫn khắc họa được sự bàng hoàng giỏi hơn bất kỳ họa sĩ xoàng xĩnh nào.*` (phần tên tác phẩm nằm ngoài thẻ `<html:em>` trong nguồn nên để chữ đứng, hai phần trước và sau nằm trong thẻ `<html:em>` nên đặt trong `*...*`).
  - `p000369`: `*Dù sao thì…*`
  - `p000381`: `*vật chất*`
  - `p000391`: `*Trung tá không thể nào nói thật được.*`
  - `p000393`: `*Luật pháp sinh ra không phải để bị phá vỡ mà là để lách qua.*`
- Không tự ý thêm `*...*` vào các đoạn khác không có thẻ nhấn mạnh trong nguồn.

## 4. Thuật ngữ và mục chờ xét (`pending_terms`)
- Áp dụng nhất quán các phương án tạm đã có trong `canon/glossary-pending.yml` và `work/run-state/pending-terms-index.yml`:
  - `ma’am` / `Colonel` (gọi Tanya): thưa Trung tá / Trung tá (`p000354`, `p000359`, `p000364`, `p000391`)
  - `adjutant`: viên sĩ quan phụ tá / sĩ quan phụ tá (`p000361`, `p000384`)
  - `Weiss`: Weiss (`p000363`, `p000375`, `p000379`, `p000391`)
  - `the lieutenant` (chỉ Serebryakov): Trung úy (`p000365`)
  - `law of war`: luật chiến tranh (`p000366`, `p000392`, `p000393`, `p000394`)
  - `fatherland`: tổ quốc (`p000366`)
  - `Federation`: Liên bang (`p000370`, `p000393`)
  - `Council for Self-Government`: Hội đồng Tự trị (`p000376`, `p000381`)
  - `General von Zettour`: Tướng von Zettour (`p000376`)
  - `the rear`: hậu phương (`p000377`, `p000381`)
  - `counterinsurgency battles`: các trận đánh chống nổi dậy (`p000381`)
  - `cold-weather gear`: trang bị chống rét (`p000383`)
  - `Imperial Army`: Lục quân Đế quốc (`p000384`, `p000393`)
  - `Serebryakov`: Serebryakov (`p000384`)
  - `Salamander Kampfgruppe`: Kampfgruppe Salamander (`p000387`)
- Ghi nhận thuật ngữ đề xuất mới trong mục `pending_terms` của báo cáo:
  - `Rules of War on Land`: Quy tắc Chiến tranh trên Bộ (`p000393`)
  - `realizable securities`: các chứng khoán có giá có thể chuyển nhượng (`p000394`)
