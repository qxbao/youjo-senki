# Báo cáo tự kiểm dịch thuật (Semantic Self-Check) — `vol-01-ch-03-b17`

## 1. Thông tin chung
- **Task ID**: `vol-01-ch-03-b17`
- **Translator**: `argon-translator-v01-ch-03-b17`
- **Source batch**: `work/vol-01/batches/ch-03-b17-source.jsonl`
- **Output translation**: `translations/vol-01/ch-03-b17.jsonl`
- **Phạm vi đoạn**: `YS-LN01/Text/chapter007.xhtml/p000349` → `YS-LN01/Text/chapter007.xhtml/p000369` (21 đoạn, toàn bộ thuộc loại `story`)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`
- **Source SHA256**: `7698e1b80fc5d560020b8934f6243b3b7be1be9c911668455a069f857f3da528`

## 2. Kiểm tra tính đầy đủ và bảo toàn nghĩa
- **Đối chiếu 1:1 theo `segment_id`**: Đủ 21/21 dòng từ `p000349` đến `p000369`, giữ nguyên thứ tự, toàn bộ các dòng đều đặt `"status": "reviewed"` sau bước Translator Sign-off, không gộp đoạn, không tách đoạn, không bỏ sót bất kỳ mệnh đề hay câu thoại nào.
- **Bảo toàn phủ định, điều kiện, so sánh, suy đoán, câu hỏi và dấu câu đặc thù**:
  - `p000349`: Bảo toàn cấu trúc phủ định ở cả hai câu (`chẳng thấy có gì bất thường...`, `không tài nào giải thích rõ được, nhưng cảm giác cứ như thể cô ấy hoàn toàn thuộc về nơi này vậy`).
  - `p000350`: Bảo toàn cấu trúc so sánh giả định ở câu 1 (`như thể chúng tôi là những món đồ đang chờ được định giá`) và khả năng giả định kèm ẩn dụ ở câu 2 (`Người ta có thể cười nhạo tôi... gợi cho tôi nhớ đến ánh nhìn của một con mèo khi đang vờn chuột`).
  - `p000351`: Bảo toàn cấu trúc nhấn mạnh thành tích (`mà nổi bật không kém phần chính là Huy hiệu Xung kích Cánh Bạc`) và câu danh ngữ miêu tả ngoại hình cuối đoạn (`Đôi mắt xanh vô hồn, mái tóc vàng pha sắc xám sẫm.`).
  - `p000352`: Bảo toàn mệnh đề suy đoán phủ định ở vế đầu (`Có lẽ một phần là vì chúng tôi chẳng mấy khi thấy ánh nắng ở mặt trận Rhine...`).
  - `p000353`: Bảo toàn mệnh đề phủ định bổ nghĩa cho giọng điệu (`không chừa chỗ cho bất kỳ sự hiểu lầm nào`), cụm chêm giảm nhẹ (`— chỉ một chút xíu thôi —`) và mệnh đề giả định nhượng bộ ở câu 3 (`sẽ chẳng thể nào có cùng tần số, ngay cả khi được huấn luyện cùng nhau`).
  - `p000355`–`p000356`, `p000358`: Bảo toàn sự đối lập dấu câu cuối lời báo cáo điều lệnh — dấu chấm than dõng dạc của hai học viên tình nguyện ở `p000355`–`p000356` đối lập với dấu chấm trầm xuống của Visha ở `p000358`.
  - `p000357`: Bảo toàn cấu trúc phủ định giảm nhẹ ở câu 2 (`Cũng không hẳn là tôi ước gì mình đã đi tình nguyện, nhưng...`), hai mệnh đề phủ định liên tiếp ở câu 3 (`Tôi không thể cứ thế mà phớt lờ chẳng bận tâm như Elya được; da mặt tôi chưa đủ dày để có thể cười xòa cho qua chuyện.`) và câu hỏi than thở ở câu 4 (`Ôi, Thượng đế ơi, sao ngài cứ phải hành hạ tôi thế này?`).
  - `p000359`–`p000360`: Bảo toàn câu điều kiện giả định theo thông lệ ở `p000359` (`Nếu chúng tôi làm theo thông lệ, điều đó có nghĩa là... sẽ lập thành một cặp, còn tôi sẽ được ghép cặp với trung đội trưởng.`) và ước muốn phủ định trong lúc báo cáo ở `p000360` (`thầm mong sao mình đừng bị mắng xối xả...`).
  - `p000362`: Bảo toàn cấu trúc câu tỉnh lược mở đầu kèm gạch ngang dài và so sánh hơn hết (`hơn bất kỳ ai tôi từng gặp`) cùng mệnh đề phủ định ở câu 2 (`không hiểu chuyện gì vừa xảy ra`).
  - `p000364`: Bảo toàn mệnh lệnh cảnh cáo phủ định ở câu 1 (`Đã tình nguyện đi lính thì các anh liệu hồn mà đừng có chết sau Hạ sĩ Serebryakov và tôi.`), các câu phủ định ở câu 2, 3, 6 (`vẫn không hề thay đổi`, `chẳng hề cao giọng`, `không có thời gian hay nguồn lực...`) và giả định ở câu 7 (`làm vậy chỉ tổ phản tác dụng`).
  - `p000366`: Bảo toàn câu điều kiện giả định trái thực tế đối lập với thực tại ở câu 1 (`Sẽ là một câu chuyện khác nếu các anh bị ép phải phục vụ trái với ý muốn vì đất nước cần đến mình, đằng này chính các anh là những kẻ đã xếp hàng...`) và câu điều kiện mệnh lệnh ở câu 2 (`Còn nếu các anh bất tài đến mức không làm nổi việc đó, thì chết quách đi.`).
  - `p000367`–`p000369`: Bảo toàn sắc thái suy đoán (`Ắt hẳn cô ấy đã nói hết...`), mệnh đề nhượng bộ (`dù vừa mới chân ướt chân ráo tới nơi`), dấu ngoặc kép châm biếm ở `p000367` (`“quà chuyển phát”`) và `p000369` (`“chỉnh đốn”`), cấu trúc tăng tiến phủ định ở `p000368` (`chẳng những không đáng đồng lương đang nhận, mà còn tệ hơn cả rác rưởi`) và hai cấu trúc phủ định ở `p000369` (`không bị kỷ luật thẳng tay`, `không thể trông nom nổi hai người đó ở ngoài tiền tuyến`).

## 3. Kiểm tra đại từ, điểm nhìn và giọng văn (`DEC-P01-001`)
- **Điểm nhìn tự sự ngôi thứ nhất của Hạ sĩ Viktoriya Ivanovna Serebryakov (Visha) (`p000349`–`p000369`)**:
  - Toàn bộ 21 đoạn tiếp nối trực tiếp mạch tự sự ngôi thứ nhất của Visha từ cuối `ch-03-b16` (`p000347`–`p000348`).
  - Tuân thủ nghiêm ngặt giới hạn của `DEC-P01-001` (quy ước dùng `nó` trong trần thuật và `mình` làm đại từ độc thoại nội tâm chỉ áp dụng cho điểm nhìn của Tanya, tuyệt đối không mở rộng sang điểm nhìn của chủ thể khác):
    - Visha tự xưng `tôi` / `Tôi` (kết hợp đại từ phản thân `mình`), và dùng `chúng tôi` / `Chúng tôi` khi gộp nhóm ba tân binh mới về trung đội (`p000349`, `p000350`, `p000353`, `p000359`, `p000367`, `p000368`).
    - Dưới góc nhìn của người lính cấp dưới đối với vị trung đội trưởng trực tiếp mới gặp, Visha quy chiếu Thiếu úy Tanya Degurechaff ở ngôi thứ ba bằng `Thiếu úy Degurechaff`, `vị thiếu úy`, và đại từ `cô ấy` / `Cô ấy` (đồng bộ hoàn toàn với `ch-03-b16` `p000347`–`p000348`).
    - Quy chiếu `đại đội trưởng` (Trung úy Schwarkopf) ở `p000349`, `p000367`, `p000369`; quy chiếu người bạn `Elya` ở `p000351`, `p000357`; quy chiếu hai người đồng đội cùng trung đội `Hạ sĩ Kurst von Walhorf` và `Hạ sĩ Harald von Vist` bằng `họ`, `hai anh chàng... kia`, `hai người đó`, `cặp đôi ấy` (`p000354`–`p000359`, `p000369`). Ở `p000369` câu 2, phân biệt rõ chủ ngữ `họ` (đại đội trưởng và vị thiếu úy) với tân ngữ `hai người đó` / `cặp đôi ấy` (Kurst và Harald) để câu văn tiếng Việt hoàn toàn tường minh.
    - Ở `p000357`, trong câu cảm thán hướng tới `Thượng đế` (`review-God`), gọi bằng `ngài` và tự xưng `tôi` (`Ôi, Thượng đế ơi, sao ngài cứ phải hành hạ tôi thế này?`).
    - Ở `p000359`, lược bỏ đại từ ngôi thứ hai phiếm chỉ đầu câu theo `direct-address choice` (`Có thể nói là tôi cảm thấy hơi lạc lõng...`).
- **Lời thoại trực tiếp trong batch**:
  - Báo cáo điều lệnh của ba hạ sĩ tân binh (`p000355`, `p000356`, `p000358`): Ngắn gọn, chuẩn mực điều lệnh quân đội.
  - Lời thoại của Thiếu úy Tanya Degurechaff với Hạ sĩ Visha (`p000361`): Tự xưng `Tôi`, gọi cấp dưới bằng `cô` đi kèm cấp bậc và họ tên đầy đủ `Hạ sĩ Viktoriya Ivanovna Serebryakov` kết hợp phản thân `mình`.
  - Lời thoại của Thiếu úy Tanya Degurechaff với hai nam hạ sĩ tình nguyện Kurst và Harald (`p000364`, `p000366`): Tự xưng `tôi`, gọi hai cấp dưới nam giới ở ngôi thứ hai số nhiều là `mấy anh bạn` / `các anh`, và nhắc đến Visha cùng bản thân là `Hạ sĩ Serebryakov và tôi`; giữ giọng điệu điềm tĩnh, lạnh lùng nhưng sắc lẹm và tàn nhẫn.

## 4. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002`)
- Đối chiếu toàn bộ thẻ `<html:em>` và `<html:i>` trong trường `xhtml` của 21 đoạn nguồn:
  - Các đoạn `p000349`–`p000368` (20 đoạn): Không có thẻ nhấn mạnh trong `xhtml` nguồn → bản dịch hoàn toàn không chứa ký tự `*`.
  - Đoạn `p000369`: Có **1** cụm `<html:em>` trong `xhtml` nguồn → bảo toàn chính xác bằng dấu `*...*` tại `*thẳng tay*` (`...nhưng họ không bị kỷ luật thẳng tay — từ khóa ở đây là *thẳng tay*.`).

## 5. Thuật ngữ, danh từ riêng và lựa chọn kế thừa / đề xuất tạm
- **Đã khóa trong `canon/`**:
  - `Đế quốc`, `pháp sư`, `sĩ quan`, `trung đội`, `đại đội`, `tiền tuyến`, `Viktoriya Ivanovna Serebryakov`.
- **Kế thừa từ `work/run-state/pending-terms.yml` và các batch trước**:
  - `Thiếu úy Degurechaff` / `vị thiếu úy` (`b02-second-lieutenant`, `ch-03-b11`–`b16`)
  - `đại đội trưởng` (`ch-03-b11` `p000232`, `ch-03-b15` `p000319`)
  - `Elya` (`ch-03-b10` `p000199`–`p000220`)
  - `át chủ bài` (`ch-02-b02` `p000018`, `ch-03-b11` `p000227`; mở rộng thành `át chủ bài kỳ cựu` ở `p000351`)
  - `huân chương` (`ch-01-b15` `p000270`, `ch-03-b11` `p000229`)
  - `Huy hiệu Xung kích Cánh Bạc` (`ch-01-b17`, `ch-03-b08`–`b12`)
  - `như búp bê` (`ch-01-b04` `p000051`)
  - `mặt trận Rhine` (`ch-03-b01` `p000016`, `ch-03-b10` `p000204`)
  - `ma cà rồng` (`ch-03-b16` `p000347`)
  - `bằng một giọng điệu điềm tĩnh, đậm chất công vụ` (`P01-matter-of-fact-register`, `ch-03-b12` `p000249`)
  - `Trường Thiếu sinh quân` (`ch-03-b09` `p000182`, `ch-03-b10` `p000185`, `ch-03-b12` `p000246`, `ch-03-b16` `p000325`, `p000348`)
  - `học viên` (`ch-03-b16` `p000348`), `học viện` (`ch-03-b11` `p000225`, `ch-03-b16` `p000330`)
  - `Hạ sĩ` (`ch-01-b04`–`b06`, `ch-03-b09` `p000180`)
  - `Thượng đế` (`review-God`)
  - `trung đội trưởng` (`ch-03-b11`–`b16`)
  - `ý chí tự do` (`ch-01-b13` `p000222`, `ch-02-b13` `p000143`, `ch-03-b16` `p000340`)
  - `bất tài` (`ch-03-b11` `p000226`, `ch-03-b16` `p000330`)
  - `các trung sĩ huấn luyện` (`ch-03-b10` `p000185`)
  - `lính Đế quốc` (`ch-03-b10` `p000191`)
  - `quân phục` (`ch-03-b16` `p000348`), `tổ quốc` (`ch-03-b10` `p000189`, `ch-03-b14` `p000295`)
  - `tân binh` (`ch-03-b11` `p000226`), `chiến hào` (`ch-03-b14`–`b15`)
  - `Quân đội Cộng hòa` (`ch-03-b05` `p000090`, `vol-04-ch-04-b04`)
  - `tuyến sau` (`ch-03-b01` `p000018`, `ch-03-b11` `p000222`)
- **Đề xuất tạm mới trong batch (đã ghi rõ trong `notes` từng dòng, không tự nâng thành canon)**:
  - `p000353`–`p000360`: `lính tình nguyện` / `lính nghĩa vụ` / `bị gọi nhập ngũ` (phương án khác: `đi nghĩa vụ` / `tân binh nghĩa vụ`), `nghĩa vụ quân sự bắt buộc` (phương án khác: `thời hạn phục vụ bắt buộc`), `Tiểu đoàn C` / `Tiểu đoàn D`.
  - `p000355`–`p000356`, `p000358`: Tên riêng giữ nguyên `Kurst von Walhorf`, `Harald von Vist`, `Idal-Stein`; phiên hiệu đơn vị huấn luyện dịch là `Đại đội 1, Tiểu đoàn C Idal-Stein` và `Đại đội 3, Tiểu đoàn D Idal-Stein` (phương án khác giữ nguyên trật tự nguồn: `Tiểu đoàn C Idal-Stein, Đại đội 1` / `Tiểu đoàn D Idal-Stein, Đại đội 3`).
  - `p000364`: `ứng viên sĩ quan` (phương án khác: `học viên dự nguồn sĩ quan`).
  - `p000367`: `những đợt “quà chuyển phát” định kỳ` (phương án khác: `những kiện hàng “giao tận nơi” định kỳ`).
  - `p000369`: `“chỉnh đốn”` (phương án khác: `“uốn nắn”`) và `thẳng tay — từ khóa ở đây là *thẳng tay*` (phương án khác: `trực tiếp — từ khóa ở đây là *trực tiếp*`).


## 6. Translator Sign-off (`vol-01-ch-03-b17-translator-signoff`)
- **Task ID**: `vol-01-ch-03-b17-translator-signoff`
- **Review report**: `reviews/prose/vol-01/ch-03-b17-argon-review.yml` (`status: approved_for_polish`, `serious: 0`, `moderate: 0`, `minor: 0`, `findings: []`)
- **Xử lý findings**: Không có finding cần sửa (`findings_to_process: []`). Giữ nguyên toàn bộ các lựa chọn đã khóa (`locked_choices`) từ `p000349` đến `p000369` và các đề xuất thuật ngữ tạm trong `pending_term_recommendations`.
- **Cập nhật trạng thái**: Đã chuyển `status` của toàn bộ 21/21 dòng trong `translations/vol-01/ch-03-b17.jsonl` từ `"draft"` sang `"reviewed"`.
