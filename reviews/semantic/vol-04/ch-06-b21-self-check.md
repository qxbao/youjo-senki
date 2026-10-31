# Báo Cáo Tự Kiểm Dịch Thuật — Batch `vol-04-ch-06-b21`

- **Task ID**: `vol-04-ch-06-b21`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN04/Text/chapter001_v.xhtml/p000705` .. `YS-LN04/Text/chapter001_v.xhtml/p000752` (48 đoạn)
- **Tệp đích**: `translations/vol-04/ch-06-b21.jsonl`

---

## 1. Kiểm tra tính đầy đủ và toàn vẹn dữ liệu

- Đã dịch đầy đủ 48/48 đoạn theo đúng thứ tự `segment_id` từ `p000705` đến `p000752`.
- Toàn bộ các dòng đều khớp chính xác `source_sha256` (`d753e588b788516ce336d1cf80988217124eba4e9a380a1881bc8efb45e4467f`), `glossary_version` (`sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`), `translator` (`argon-low`), và đã được cập nhật lên `status: "reviewed"` sau khi xử lý Argon review.
- Không bỏ sót câu, mệnh đề phụ, từ phủ định, trạng từ chỉ mức độ hay bất kỳ chi tiết tu từ nào.

---

## 2. Kiểm tra nghĩa, logic và mạch cảnh

Batch này gồm hai phân cảnh nối tiếp nhau khép lại Chương 6 và toàn bộ Tập 4:

1. **Phân cảnh 1 (`p000705`–`p000738`) — Loria được Tổng Bí thư Josef phê chuẩn kế hoạch và trở về tổng hành dinh Bộ Nội vụ chỉ đạo cấp dưới**:
   - Tiếp nối mạch cuối `ch-06-b20`: Loria dốc hết quyết tâm khẩn cầu và được Tổng Bí thư Josef gật đầu cho phép (`p000705`–`p000709`).
   - Ngay khi tan họp, Loria nhảy lên xe lao về tổng hành dinh đang tái thiết, lòng lâng lâng phấn khích vì kế hoạch nhử `Kampfgruppe Salamander` vào sâu trong lãnh thổ Liên bang nhằm bắt giữ Tanya (`p000710`–`p000716`).
   - Loria triệu sĩ quan phụ trách tới hỏi về sĩ khí quân đội; khi nghe báo cáo nạn đào ngũ gia tăng, ông ta lập tức ra lệnh tăng cường `các đội đốc chiến` tuyển từ `Bộ Nội vụ`, đồng thời yêu cầu cải thiện điều kiện sinh hoạt tại `các trại tập trung` trong một tháng để đẩy tù nhân ra chiến trường làm bia đỡ đạn đối đầu với `Lục quân Đế quốc` (`p000717`–`p000738`). Sự tương phản châm biếm đen tối giữa góc nhìn tự coi mình là "nhà truyền giáo rao giảng hy vọng và ước mơ" với mệnh lệnh tàn nhẫn sử dụng tù nhân và đe dọa xử lý cả cấp dưới được giữ nguyên vẹn sắc thái lạnh lùng, bệnh hoạn.

2. **Phân cảnh 2 (`p000739`–`p000752`) — Mặt trận phía Đông ngày 18 tháng 7 năm Thống nhất 1926, độc thoại mở màn của Tanya và dòng kết Tập 4**:
   - Tiêu đề mốc thời gian - địa điểm (`p000739`): `NGÀY 18 THÁNG 7, NĂM THỐNG NHẤT 1926, CHIẾN TUYẾN PHÍA ĐÔNG`.
   - Từ `p000740` đến `p000751`, Tanya cất lời chào độc giả/khán giả bằng giọng điệu quảng cáo du lịch sinh thái giả tạo, mỉa mai sự cơ giới hóa đô thị để dẫn dắt sang công việc thực tế của mình là "dã ngoại có vũ trang" trên mặt đất lầy lội bằng mô tô và xe bọc thép nhằm tuần tra cảnh giới sườn cho `Cụm phương Bắc thuộc Cụm tập đoàn quân phía Đông của Đế quốc`.
   - Cuối cảnh (`p000750`–`p000751`), Tanya chủ quan tin rằng lực lượng dự bị của quân địch đã bị đánh bại ở `Trouncenberg` và `Bộ Tổng tham mưu` cũng không nghĩ địch sẽ tái xuất hiện, nên mong muốn biến nhiệm vụ thành trò bấm chuông cửa rồi bỏ chạy để có thể rút lui bất cứ lúc nào — tạo thế đối lập kịch tính trực tiếp với cái bẫy mà Loria vừa giăng ra ở phân cảnh trước.
   - Đoạn kết tập (`p000752`): `(Tanya Chiến Ký, Tập 4: Dabit Deus His Quoque Finem, Hết)`, đồng bộ cấu trúc với dòng kết ở `pending-terms-index.yml` và theo đúng khuyến nghị trong Argon review.

---

## 3. Kiểm tra đại từ và xưng hô (`DEC-P01-001`)

- **Tự sự ngôi thứ ba theo điểm nhìn Loria (`p000705`–`p000738`)**:
  - Dùng `Loria`, `ông ta`, phản thân `mình` nhất quán với `ch-06-b20`.
  - Độc thoại/lẩm bẩm một mình của Loria trên xe (`p000711`, `p000714`, `p000716`): Tự xưng `mình` (và `chúng ta` khi chỉ phía Liên bang), gọi Tanya là `con bé` (`p000711`) và `nàng tiên đó` (`p000738`), giữ sự liền mạch tuyệt đối với cuối `ch-06-b20`.
  - Độc thoại nội tâm của Loria hướng tới binh sĩ Liên bang (`p000736`) và khao khát cá nhân (`p000738`): Tự xưng `ta`, gọi binh sĩ là `các ngươi`.
- **Đối thoại giữa Tổng Bí thư Josef và Loria (`p000708`–`p000709`)**:
  - Josef nói với Loria (`p000708`): Xưng `tôi` – gọi `đồng chí`.
  - Loria đáp lời Josef (`p000709`): Xưng `tôi` – gọi `đồng chí`.
- **Đối thoại giữa Loria và sĩ quan cấp dưới thuộc Bộ Nội vụ (`p000718`–`p000737`)**:
  - Cấp dưới báo cáo và nhận lệnh (`p000718`, `p000722`, `p000726`, `p000731`, `p000734`): Xưng `chúng tôi` / `tôi`, đáp `Rõ.` / `Rõ, thưa đồng chí.` đúng chuẩn quân sự Liên bang.
  - Loria nói và nghĩ về cấp dưới (`p000728`, `p000730`, `p000732`, `p000735`): Gọi cấp dưới là `cậu`, xưng `chúng ta` khi nói về chính sách chung của cơ quan/quốc gia (`p000719`, `p000727`).
- **Độc thoại trực tiếp của Tanya (`p000740`–`p000751`)**:
  - Do đoạn này mang hình thức lời chào và diễn thuyết trực tiếp hướng tới người nghe/độc giả trước khi tự giới thiệu chức danh chính thức (`Trung tá Tanya von Degurechaff`), Tanya xưng `tôi` (và `chúng ta` / `chúng tôi` khi gộp người nghe hoặc đơn vị của mình), gọi người nghe là `mọi người` / `các bạn`.

---

## 4. Kiểm tra định dạng nhấn mạnh (`DEC-P01-002`)

Đã đối chiếu toàn bộ trường `xhtml` của 48 đoạn nguồn:
- Chỉ có đúng **3 đoạn** có thẻ nhấn mạnh trong nguồn và đã được bọc dấu `*...*` khớp chính xác phạm vi:
  - `p000728`: Chỉ bọc câu hỏi nội tâm đầu đoạn (`*Có chừng ấy thôi mà cậu cũng không hiểu sao?*`), phần trần thuật phía sau không bọc.
  - `p000736`: Chỉ bọc mệnh đề cầu khiến trước dấu phẩy (`*Vậy nên, hỡi các binh sĩ. Hãy mau chóng chứng minh cho ta thấy các ngươi làm được việc này đi*`), phần trần thuật sau dấu phẩy không bọc.
  - `p000738`: Bọc toàn bộ câu độc thoại nội tâm (`*Hãy mau chóng đưa nàng tiên đó đến cho ta.*`).
- Toàn bộ 45 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và hoàn toàn không chứa ký tự `*`.

---

## 5. Kiểm tra thuật ngữ và đối chiếu Canon / Pending Terms

Đã áp dụng nhất quán các thuật ngữ theo `canon/` và `work/run-state/pending-terms-index.yml`:
- `General Secretary` -> `Đồng chí Tổng Bí thư` (`p000711`)
- `Imperial Army` -> `Lục quân Đế quốc` (`p000714`, `p000727`)
- `Salamander Kampfgruppe` -> `Kampfgruppe Salamander` (`p000714`, `p000746`, `p000749`)
- `blocking units` -> `đội đốc chiến` (`p000719`)
- `Internal Affairs` -> `Bộ Nội vụ` (`p000719`)
- `concentration camps` -> `các trại tập trung` (`p000723`)
- `Unified Year 1926` -> `NĂM THỐNG NHẤT 1926` (`p000739`)
- `General Staff` -> `Bộ Tổng tham mưu` (`p000746`, `p000750`)
- `Lieutenant Colonel Tanya von Degurechaff` -> `Trung tá Tanya von Degurechaff` (`p000746`)
- `Imperial Eastern Army Group’s Northern Cluster` -> `Cụm phương Bắc thuộc Cụm tập đoàn quân phía Đông của Đế quốc` (`p000749`)
- `Trouncenberg` -> `Trouncenberg` (`p000750`)
- `The Saga of Tanya the Evil, Volume 4: Dabit Deus His Quoque Finem, fin` -> `Tanya Chiến Ký, Tập 4: Dabit Deus His Quoque Finem, Hết` (`p000752`)

Không phát sinh thuật ngữ mới gây mơ hồ cần bổ sung vào `notes`.

---

## 6. Xử lý Argon Review Sign-off (`vol-04-ch-06-b21-translator-signoff`)

Đã đối chiếu đầy đủ `reviews/prose/vol-04/ch-06-b21-argon-review.yml`:
- **`p000736` (minor)**: Tiếp nhận khuyến nghị, chỉnh cụm `"vừa vặn kìm nén sự giằng xé trong lòng"` thành `"chật vật kìm nén sự giằng xé trong lòng"` để tự nhiên hơn trong tiếng Việt mà vẫn giữ nguyên `locked_choices` (phạm vi bọc `*...*`).
- **`p000752` (minor & pending_term_recommendation)**: Tiếp nhận khuyến nghị và `proposed_vi`, cập nhật thành `"(Tanya Chiến Ký, Tập 4: Dabit Deus His Quoque Finem, Hết)"` để đồng bộ với sổ `pending-terms-index.yml` và vẫn giữ nguyên `locked_choices` (phụ đề Latinh `Dabit Deus His Quoque Finem` và nhãn `Hết`).
- Đã kiểm tra tuân thủ toàn bộ 48 mục `locked_choices` và 7 mục `pending_term_recommendations`.
- Đã cập nhật trường `status` của toàn bộ 48 dòng trong `translations/vol-04/ch-06-b21.jsonl` từ `"draft"` sang `"reviewed"`.
