# Báo cáo tự kiểm dịch thuật (Semantic Self-Check) — `vol-01-ch-03-b18`

## 1. Thông tin chung
- **Task ID**: `vol-01-ch-03-b18`
- **Translator**: `argon-translator-v01-ch-03-b18`
- **Source batch**: `work/vol-01/batches/ch-03-b18-source.jsonl`
- **Output translation**: `translations/vol-01/ch-03-b18.jsonl`
- **Phạm vi đoạn**: `YS-LN01/Text/chapter007.xhtml/p000370` → `YS-LN01/Text/chapter007.xhtml/p000390` (21 đoạn, toàn bộ thuộc loại `story`)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`
- **Source SHA256**: `7698e1b80fc5d560020b8934f6243b3b7be1be9c911668455a069f857f3da528`

## 2. Kiểm tra tính đầy đủ và bảo toàn nghĩa
- **Đối chiếu 1:1 theo `segment_id`**: Đủ 21/21 dòng từ `p000370` đến `p000390`, giữ nguyên thứ tự, toàn bộ các dòng đều đặt `"status": "reviewed"` sau bước Translator Sign-off, không gộp đoạn, không tách đoạn, không bỏ sót bất kỳ mệnh đề hay câu thoại nào.
- **Bảo toàn phủ định, điều kiện, so sánh, suy đoán, câu hỏi, cấu trúc tăng tiến và chỉ số chú thích**:
  - `p000371`: Bảo toàn khả thể ở câu 3 (`Họ có thể ở yên an toàn bên trong một lô cốt...`) và cấu trúc phủ định giới hạn ở câu 4 (`một cái lô cốt nằm im bất động chẳng qua chỉ là một mục tiêu kiên cố mà thôi`).
  - `p000372`: Bảo toàn giả định phủ định trong suy nghĩ của Visha ở câu 2 (`đinh ninh rằng mình sẽ chẳng bao giờ sống sót rời khỏi đó`) và mệnh đề phủ định đối lập ở câu 3 (`trong khi chúng tôi lại thoát ra mà chẳng hề sứt mẻ lấy một mảy may`).
  - `p000373`: Kiểm tra kỹ cấu trúc tăng tiến phủ định `chẳng những... mà còn...` khi chủ thể hai vế thay đổi theo đúng `style-guide.md` (`chẳng những hầu như không có quả đạn pháo nào bay về phía chúng tôi, mà chúng tôi còn chẳng chịu bất kỳ tổn thất thực sự nào trước khi tiếp cận giao chiến với địch`).
  - `p000374`: Bảo toàn so sánh hơn ở câu 2, mệnh đề điều kiện phủ định ở câu 3 (`Chừng nào không vô tình đâm sầm vào một trận địa pháo phòng không...`) và mệnh đề nhượng bộ kết hợp cấu trúc `quá... để...` ở câu 4 (`Dù pháp sư chậm hơn máy bay, chúng tôi vẫn quá nhanh để pháo binh có thể thong thả ngắm bắn.`).
  - `p000375`: Bảo toàn câu điều kiện giả định kèm mức độ chắc chắn ở câu 1 (`Có lẽ sẽ là một câu chuyện khác nếu chúng tôi đột kích vào một trận địa hỏa lực hay một lô cốt...`) và cấu trúc tương quan tăng tiến ở câu 3 (`một pháp sư càng dày dạn kinh nghiệm bao nhiêu thì lại càng hoài nghi việc bảo vệ một vị trí cố định bấy nhiêu`).
  - `p000376`: Bảo toàn mệnh đề phủ định tuyệt đối ở câu 1 (`tuyệt đối không bao giờ được chọc giận`) và cấu trúc phủ định đi kèm điều kiện ngoại trừ ở câu 2 (`Sẽ chẳng thể nào sống sót nổi trừ phi biến vị thần này thành đồng minh của mình và học được cách né tránh chiếc búa sắt của ngài.`).
  - `p000377`–`p000378`: Bảo toàn câu suy đoán bỏ lửng ở đầu `p000377`, trình tự 3 danh ngữ khắc họa Tanya ở câu 2 `p000377`, câu hỏi nghi vấn mở đầu `p000378` (`Liệu những người lính, vốn bản chất là một tập hợp của những kẻ thực dụng, có thể tin vào Thượng đế hay không?`) và câu trả lời trích dẫn trong thư của Elya.
  - `p000382`: Bảo toàn giả định lý tưởng đối lập với thực tế ở câu 3 (`Lý tưởng nhất thì lẽ ra chúng tôi phải là cộng sự phối hợp cùng nhau, nhưng vị chỉ huy của chúng tôi chỉ bật cười và bảo rằng tôi vẫn cần phải rèn luyện thêm nhiều nữa.`).
  - `p000383`–`p000386`: Bảo toàn câu hỏi tu từ cảm thán ở cuối `p000383`, mệnh đề phủ định ở câu nội tâm `p000384` (`mà không bị âm thanh đó dọa cho phát hoảng lên thôi`), và sắc thái cầu nguyện tôn giáo cổ kính trong lời tung hô pháo binh ở `p000385`–`p000386`.
  - `p000387`–`p000390`: Bảo toàn mệnh đề nhượng bộ và phủ định bộ phận ở `p000387` (`không hoàn toàn sai`), mệnh đề điều kiện ở câu 1 `p000388`, chỉ số chú thích trên cao `¹⁵` tương ứng với `<html:sup>15</html:sup>` và mệnh đề phủ định ở cuối câu 2 `p000389` (`một thê đội địch¹⁵… và cả một loạt những chuyện mà tôi thực sự chẳng muốn nhớ lại chút nào đã xảy ra`), cùng mệnh đề điều kiện thời gian và suy đoán ở `p000390`.

## 3. Kiểm tra đại từ, điểm nhìn và giọng văn (`DEC-P01-001`)
- **Điểm nhìn tự sự ngôi thứ nhất của Hạ sĩ Viktoriya Ivanovna Serebryakov (Visha) (`p000370`–`p000390`)**:
  - Toàn bộ 21 đoạn tiếp nối trực tiếp mạch tự sự ngôi thứ nhất của Visha từ `ch-03-b16` (`p000347`–`p000348`) và `ch-03-b17` (`p000349`–`p000369`).
  - Tuân thủ nghiêm ngặt giới hạn chủ thể của `DEC-P01-001` (quy ước dùng `nó` trong trần thuật và `mình` làm đại từ độc thoại nội tâm chỉ áp dụng cho điểm nhìn của Tanya, tuyệt đối không mở rộng sang điểm nhìn của Visha):
    - Visha tự xưng `tôi` (kết hợp đại từ phản thân `mình`), dùng `chúng tôi` / `Chúng tôi` khi gộp mình với Thiếu úy Degurechaff hoặc toàn đại đội 205 (`p000370`, `p000372`–`p000375`, `p000379`–`p000382`, `p000384`, `p000387`–`p000389`), và dùng `chúng ta` trong nhận định đúc kết bài học chung trên chiến trường ở câu 1 `p000376`.
    - Quy chiếu cấp trên trực tiếp `Thiếu úy Degurechaff` (`Chỉ huy của tôi` ở `p000377`) ở ngôi thứ ba bằng `cô ấy` (`p000370`, `p000377`, `p000378` câu 2, `p000382` — đồng bộ hoàn toàn với `ch-03-b16` và `ch-03-b17`).
    - Quy chiếu người bạn thân thời huấn luyện `Elya` bằng `cậu ấy` (`p000378` câu 3–5, `p000380`; phương án khác: `cô ấy`) để vừa thể hiện tình cảm bạn bè đồng trang lứa vừa tách biệt hoàn toàn với đại từ `cô ấy` quy chiếu Thiếu úy Degurechaff ở câu 2 `p000378`; trong câu trích dẫn thư của Elya gửi Visha ở `p000378`, Elya tự xưng `tớ` đồng bộ với hệ xưng hô `tớ – cậu` ở `ch-03-b10` (`p000193`–`p000219`).
    - Tại `p000375` câu 3, do nguồn gộp chung danh từ cấp bậc số nhiều cho cả Schwarkopf và Degurechaff nhưng cấp bậc thực tế trong truyện của Schwarkopf là Trung úy và của Degurechaff là Thiếu úy (đồng bộ `ch-03-b11` `p000233`–`p000234`, `ch-03-b16` `p000347`–`p000348`, và `p000384` của chính lô này), dịch rõ là `Trung úy Schwarkopf và Thiếu úy Degurechaff`.
    - Quy chiếu hai học viên tình nguyện chuyển về tuyến sau ở `p000371` và các thành viên kỳ cựu của Trung đội 1 ở `p000387` bằng `Họ` / `họ`; quy chiếu đơn vị Quân đội Cộng hòa bằng `chúng` (`p000372`, `p000381`, `p000387`, `p000388`).
    - Tại các câu có đại từ ngôi thứ hai phiếm chỉ trong nguồn (`p000374` câu 3, `p000375` câu 3, `p000376` câu 2, `p000388` câu 2), lược đại từ phiếm chỉ hoặc chuyển sang cấu trúc chủ ngữ khái quát (`một pháp sư`, `người ta`) theo đúng quy ước `direct-address choice` (`work/run-state/pending-terms.yml`).
- **Lời thoại và lời cầu nguyện trong batch**:
  - Lời thoại của Trung úy Ihlen Schwarkopf (`p000383`) và các thành viên Trung đội 1 (`p000385`, `p000386`): Hào hứng ngợi ca pháo binh như `Thượng đế` / `Vị thần Chiến trường`; đặc biệt ở `p000386`, dùng cặp đại từ tôn kính mang âm hưởng kinh cầu nguyện `Ngài – chúng con` (phương án khác: `Người – chúng tôi`), và ở câu cầu nguyện thầm cuối `p000388` của Visha dùng `Thượng đế yêu dấu ơi, xin hãy ban cho con...`.

## 4. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002`)
- Đối chiếu toàn bộ thẻ `<html:em>` và `<html:i>` trong trường `xhtml` của 21 đoạn nguồn:
  - 19/21 đoạn (`p000370`–`p000383`, `p000385`–`p000387`, `p000389`–`p000390`): Không có thẻ nhấn mạnh trong `xhtml` nguồn → bản dịch hoàn toàn không chứa ký tự `*`.
  - Đoạn `p000384`: Có **1** thẻ `<html:em>` bọc trọn câu thứ hai → bảo toàn chính xác bằng dấu `*...*`: `*Gu âm nhạc của chúng tôi xem chừng có đôi chút khác biệt — tôi chỉ vừa đủ sức vượt qua những đợt pháo kích dữ dội này mà không bị âm thanh đó dọa cho phát hoảng lên thôi.*`
  - Đoạn `p000388`: Có **1** thẻ `<html:em>` bọc trọn câu thứ ba → bảo toàn chính xác bằng dấu `*...*`: `*Thượng đế yêu dấu ơi, xin hãy ban cho con sự chi viện của pháo binh.*`

## 5. Thuật ngữ, danh từ riêng và lựa chọn kế thừa / đề xuất tạm
- **Đã khóa trong `canon/`**:
  - `pháp sư`, `pháo binh`, `trung đội`, `đại đội`, `tiểu đoàn`, `tiền tuyến`.
- **Kế thừa từ `work/run-state/pending-terms.yml` và các batch trước**:
  - `Thiếu úy Degurechaff` (`b02-second-lieutenant`, `ch-03-b11`–`b17`)
  - `Trung úy Schwarkopf` (`ch-03-b16` `p000348`, `ch-04-b07` `p000145`)
  - `học viên thiếu sinh quân` (`ch-03-b10` `p000185`, `ch-03-b17` `p000353`)
  - `tuyến sau` (`ch-03-b15` `p000304`, `ch-03-b17` `p000369`)
  - `lô cốt` (`vol-04-ch-01-b15` `p000075`)
  - `lực lượng dự bị` (`ch-03-b13` `p000263`, `ch-03-b14` `p000298`)
  - `cuộc phản công` / `phản công` (`ch-03-b14` `p000294`, `ch-03-b15` `p000306`, `p000310`)
  - `Cộng hòa` / `Quân đội Cộng hòa` (`ch-03-b17` `p000367`, `vol-04-ch-04-b04`)
  - `phòng tuyến` (`ch-03-b13`–`b16`)
  - `hỏa lực áp chế` (`pending-terms.yml` dòng 1254, 1418)
  - `pháo hạng nặng` (`ch-01-b06` `p000077`, `ch-04-b21` `p000230`)
  - `súng máy` (`ch-03-b14` `p000299`)
  - `pháo phòng không` (`pending-terms.yml` dòng 6960)
  - `trận địa hỏa lực` (`ch-04-b21` `p000227`, `p000230`)
  - `đồng minh` (`ch-03-b11` `p000234`, `ch-03-b16` `p000345`)
  - `tác chiến cơ động` (`vol-04-ch-01-b16` `p000095`; phương án khác: `chiến tranh cơ động`)
  - `Thượng đế` (`review-God`, `ch-03-b10`, `ch-03-b17` `p000357`)
  - `Elya` (`ch-03-b09`, `ch-03-b10`, `ch-03-b17` `p000351`, `p000357`)
  - `chiến hào` (`ch-03-b14`–`b17`)
  - `quan sát viên` (`chapter1_b01_pending_terms`: `quan sát viên pháo binh`)
  - `lính mới` (`ch-03-b10` `p000188`, `ch-03-b12` `p000247`, `ch-03-b16` `p000325`)
  - `cầm chân kẻ địch` (`ch-03-b12` `p000261`)
- **Đề xuất tạm mới trong batch (đã ghi rõ trong `notes` từng dòng, không tự nâng thành canon)**:
  - `p000370`: `đồng đội bắt cặp` (đồng bộ với `ghép cặp` ở `ch-03-b17` `p000359`; phương án khác: `cộng sự`).
  - `p000371`: `thăng vượt hai cấp` (phương án khác: `thăng liền hai cấp` / `đặc cách thăng hai cấp`).
  - `p000372`: `đánh bọc sườn` (đồng bộ với `tấn công vào mạn sườn` ở `p000381`; phương án khác: `tập kích mạn sườn`).
  - `p000375`: `hỏa lực bắn chặn theo khu vực dữ dội` (phương án khác: `hỏa lực phong tỏa khu vực dày đặc`), `vị trí cố định` (đồng bộ với `lực lượng đóng chốt cố định` ở `ch-03-b16` `p000330`).
  - `p000377`: `tín đồ cuồng nhiệt đến tận xương tủy của hỏa lực`, `hiện thân hoàn hảo cho học thuyết tác chiến cơ động không khoan nhượng`.
  - `p000378`: `những kẻ thực dụng` (phương án khác: `những người theo chủ nghĩa hiện thực`), `nữ thần chiến tranh nắm giữ ý chỉ thần thánh` (phương án khác: `nữ thần chiến tranh phụ trách ý nguyện của thần linh`).
  - `p000379`: `những tín đồ sùng đạo`, `các ổ súng` (phương án khác: `các hỏa điểm`), `những mặc khải thần thánh từ pháo binh` (phương án khác: `những lời sấm truyền thần thánh của pháo binh`).
  - `p000381`: `đợt đột kích đường không` (phương án khác: `cuộc xung kích trên không`), `hỏa lực yểm trợ từ pháo binh`.
  - `p000385`–`p000387`: `Vị thần Chiến trường` (phương án khác: `Chúa tể Chiến trường`), `đấng cứu rỗi` (phương án khác: `vị cứu tinh`), `Trung đội 1` (đồng bộ quy ước chữ số với `Trung đội 3` ở `ch-03-b11` `p000224`, `p000233`), `những tay lính kỳ cựu` (tránh dùng `cựu binh` cho quân nhân đang tại ngũ).
  - `p000388`: `đám ô hợp` (phương án khác: `đám tàn quân hỗn tạp`).
  - `p000389`: `Màn pháo kích chuẩn bị` (phương án khác: `Đợt bắn pháo dọn đường`), `thê đội địch¹⁵`.


## 6. Translator Sign-off (`vol-01-ch-03-b18-translator-signoff`)
- **Task ID**: `vol-01-ch-03-b18-translator-signoff`
- **Review report**: `reviews/prose/vol-01/ch-03-b18-argon-review.yml` (`status: approved_for_polish`, `serious: 0`, `moderate: 0`, `minor: 0`, `findings: []`)
- **Xử lý findings**: Không có finding cần sửa (`findings_to_process: []`). Giữ nguyên toàn bộ các lựa chọn đã khóa (`locked_choices`) từ `p000370` đến `p000390` và các đề xuất thuật ngữ tạm trong `pending_term_recommendations`.
- **Cập nhật trạng thái**: Đã chuyển `status` của toàn bộ 21/21 dòng trong `translations/vol-01/ch-03-b18.jsonl` từ `"draft"` sang `"reviewed"`.
