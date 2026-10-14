# Review nghĩa và văn phong — vol-02 ch-07 b05

```yaml
role: reviewer
task_id: vol-02-ch-07-b05-review
batch: vol-02-ch-07-b05
state: done
review_path: reviews/prose/vol-02/ch-07-b05-codex.md
files_written: [reviews/prose/vol-02/ch-07-b05-codex.md]
counts:
  rows_reviewed: 28
  serious: 0
  moderate: 1
  minor: 3
  term_proposals_reviewed: 5
  name_callsign_choices_reviewed: 2
unresolved_findings: [B05-R01, B05-R02, B05-R03, B05-R04]
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_receive_review_then_translator_fix
```

## Phạm vi và căn cứ

Chỉ đọc hướng dẫn được giao, cấu hình pipeline, handoff review và handoff chính b05, package b05, bản dịch b05, self-check b05, năm tệp canon được handoff chính nêu và section `chapter7_b05_translator_proposals` của ledger. Không mở EPUB/PDF, chú thích gốc hoặc package khác; không tra cứu ngoài. Không dùng nhận định về lore làm căn cứ.

Hash SHA-256 của package khớp `6644770cd31ca1c5d2bfff29bb96bd181e047e2b4bed40044e6f5b17986b6b46`; hash của cả năm tệp canon khớp handoff. Có đủ 28 dòng, mã đoạn nguồn/bản dịch khớp từng dòng theo thứ tự p000104–p000131. Đây là kiểm tra đầu vào thủ công, không thay cho validator hoặc diff-check.

Các mã rút gọn trong bảng dưới đều có tiền tố `YS-LN02/Text/part0032.xhtml/`. Các góp ý chỉ mô tả căn cứ bằng tiếng Việt, không trích câu nguồn. Các lựa chọn thuật ngữ/tên gọi bên dưới đều **pending, không phải canon**.

## Findings

### B05-R01 — nhẹ — YS-LN02/Text/part0032.xhtml/p000114

**Vấn đề:** “vô tư đáp” thiên về tâm thế thản nhiên hoặc không lo lắng, trong khi điểm nhấn là đáp lệnh mà không suy nghĩ. Điều này làm nhạt đánh giá về mức độ cân nhắc của đối phương.

**Căn cứ:** p000114 phủ định việc đối phương chỉ phục tùng một cách thiếu suy xét; p000115–p000116 tiếp tục đánh giá đây là lực lượng tuyển chọn cần được coi trọng. Không có căn cứ để thêm việc họ bất tuân hoặc sợ Tanya.

**Đề xuất:** thay cụm này bằng “đáp … mà chẳng suy nghĩ” hoặc “không cần suy nghĩ đã đáp …”, giữ nguyên phủ định và lời đáp quân sự. Không đổi thành đánh giá lòng can đảm.

### B05-R02 — nhẹ — YS-LN02/Text/part0032.xhtml/p000115

**Vấn đề:** “được điều động từ mặt đất lên” giữ hướng xuất phát nhưng chưa thể hiện tính khẩn trương của việc xuất kích đánh chặn.

**Căn cứ:** package mô tả một tiểu đoàn xuất kích từ mặt đất để cản nhiệm vụ; p000109 xác nhận lực lượng này đang áp sát nhanh. Chỉ thêm sắc thái khẩn trương đã có, không suy ra phương tiện vận chuyển.

**Đề xuất:** “một tiểu đoàn được lệnh khẩn trương xuất kích từ mặt đất để cản trở nhiệm vụ trinh sát của chúng ta”. Nếu muốn giữ câu hiện tại, có thể thêm “khẩn trương” trước “điều động”.

### B05-R03 — vừa — YS-LN02/Text/part0032.xhtml/p000123

**Vấn đề:** “mình đã không trải qua huấn luyện một cách vô ích” chuyển trọng tâm từ việc huấn luyện có lý do/mục đích sang việc huấn luyện không vô ích, tức đánh giá kết quả hoặc hiệu quả.

**Căn cứ:** câu này nằm trong lời tự khẳng định không phải tay mơ, có tư duy hợp lý và đầu óc kinh tế. Phủ định ở nguồn áp vào việc trải qua huấn luyện mà không có lý do; không trực tiếp khẳng định hiệu quả của khóa huấn luyện.

**Đề xuất:** “mình trải qua huấn luyện đâu phải không có lý do”. Cách này giữ lập luận về lý do, giọng nội tâm và phủ định mà không thêm mục đích cụ thể. Giữ nguyên Being X và đúng phạm vi chữ nghiêng ở tên loài.

### B05-R04 — nhẹ — YS-LN02/Text/part0032.xhtml/p000128

**Vấn đề:** “Kế hoạch này chỉ có một vấn đề” biến một mệnh đề có điều kiện thành khẳng định chỉ tồn tại một vấn đề. Cụm “dù phải bị tiêu diệt sạch” cũng có chủ thể lược dễ vướng vào “phía ra lệnh” ở đầu câu.

**Căn cứ:** phần tự bình luận xác định vấn đề từ vị trí người nhận lệnh, không lập danh sách đầy đủ mọi nhược điểm của kế hoạch. Nhóm chịu nguy cơ bị tiêu diệt là lực lượng đoạn hậu, còn việc cấp trên ra lệnh vẫn ở mức phỏng đoán.

**Đề xuất:** “Nếu kế hoạch này có vấn đề gì, thì đó là mình đang ở phía nhận lệnh.” Với câu trước, dùng “dù lực lượng ấy có phải bị tiêu diệt sạch theo đúng nghĩa đen”. Giữ “có lẽ”, mức tổn thất, sự đổi từ trần thuật về Tanya sang nội tâm “mình”, và lời chửi cuối đoạn.

## Đối chiếu đủ 28 dòng

| Mã đoạn | Kết quả nghĩa, điểm nhìn, diễn tiến và văn phong |
|---|---|
| p000104 | Đạt: câu hỏi tự giễu, vụ Dacia và việc suy rộng năng lực đơn vị 203 đều còn; tên đơn vị vẫn là đề xuất. |
| p000105 | Đạt: xác nhận vô tuyến rồi báo tin xấu; lược người nghe không làm mất CP hoặc 01. |
| p000106 | Đạt: không khẳng định tin vào may mắn; giữ tính nghe kể, thời điểm trước khi đến thế giới này và dấu chú thích ²⁵. |
| p000107 | Đạt: chuyển từ chưa hiểu sang hiểu, nhưng vẫn giữ khả thể liên quan lý thuyết xác suất. |
| p000108 | Đạt: câu hỏi mở về tin được báo, không tự thu hẹp nội dung. |
| p000109 | Đạt: quy mô cấp tiểu đoàn, rìa tầm radar, hướng áp sát và mốc hết giai đoạn ba đều giữ. |
| p000110 | Đạt: đổi nhiệm vụ, hỏi tiếp, nén giận và chật vật giữ giọng chuyên nghiệp; Fairy 01 không bị khai triển. |
| p000111 | Đạt: sức mạnh tương đương hai đại đội, đội hình không chặt và hao sức khi qua vị trí phòng thủ; phân biệt hai loại nhiệm vụ. |
| p000112 | Đạt: tương phản sung sức/hao sức, lợi thế sân nhà và điều kiện không vô tình bị bắn trúng; không tự chỉ bên bắn hoặc vũ khí. |
| p000113 | Đạt: suy luận về mức căng thẳng tinh thần, giữ mức chắc chắn suy đoán. |
| p000114 | B05-R01: cần đổi sắc thái “vô tư” về hành động thiếu suy nghĩ; phủ định còn đúng. |
| p000115 | B05-R02: giữ quy mô, hướng xuất phát và mục tiêu; nên phục hồi sắc thái xuất kích khẩn trương. |
| p000116 | Đạt: lực lượng tuyển chọn, tránh đánh giá địch là ngốc và chuẩn bị theo hướng bi quan; không thêm lore. |
| p000117 | Đạt: cho phép hủy ngay, không biến thành lệnh bắt buộc hủy. |
| p000118 | Đạt: phản ứng ngập ngừng rồi thấy việc được phép ấy đáng chú ý; không thêm dấu nghiêng. |
| p000119 | Đạt: sự hiếm có của quyền hủy và điều kiện cuộc rút lui đúng kế hoạch; lợi ích chỉ là hạn chế tổn thất thêm. |
| p000120 | Đạt: cấp trên có vẻ hợp lý nhưng Tanya không rút; giữ bước tự xét lại và hình ảnh cái bẫy. |
| p000121 | Đạt: thiện ý vẫn có thể dẫn xuống địa ngục; lối rẽ qua hoang địa an toàn hơn, không đổi chiều so sánh. |
| p000122 | Đạt: mong không cần đến lựa chọn ấy; lược đại từ không gán quan hệ người nói/người nghe. |
| p000123 | B05-R03: cần trả trọng tâm về lý do huấn luyện; phần kinh tế, Being X, tiến hóa và phạm vi nghiêng còn giữ. |
| p000124 | Đạt: hai câu hỏi nối tiếp về điều vừa nói, không gán giới tính/cấp bậc. |
| p000125 | Đạt: mục đích khảo sát đánh chặn và nguy cơ lộ mục đích đánh lừa nếu hủy ngay; không nói nguy cơ đã xảy ra. |
| p000126 | Đạt: mưu che rút lui thất bại thì đoạn hậu phải cầm cự; không câu giờ được thì rút lui trật tự có nguy cơ hóa hỗn loạn. Giữ sự không rõ tác nhân giẫm đạp. |
| p000127 | Đạt: dè dặt truyền cuộc trao đổi kể cả khi mã hóa, không biến mã hóa thành bảo đảm an toàn. |
| p000128 | B05-R04: giữ chuyển điểm nhìn và giả định vai người ra lệnh; chỉnh điều kiện và làm rõ chủ thể chịu tổn thất. |
| p000129 | Đạt: né tiểu đoàn hiện tại nhưng bị toàn bộ đơn vị Cộng hòa trên mặt trận truy đuổi là phương án tệ hơn. |
| p000130 | Đạt: ở lại là lựa chọn duy nhất xét rủi ro; giữ phép ví đầu tư và lợi nhuận, phủ định đã được rút gọn đúng. |
| p000131 | Đạt: không được lộ trước khi giai đoạn ba kết thúc; loại bỏ đơn vị đánh chặn rồi tiếp tục nhiệm vụ, không đảo thứ tự. |

## Bảy khuyến nghị tạm

| Mục và mã đoạn | Phương án đề xuất | Căn cứ trong phạm vi và phương án khác |
|---|---|---|
| 203rd Aerial Mage Battalion — p000104 | Giữ “Tiểu đoàn Pháp sư Trên không số 203”. | Giữ cấp đơn vị, số hiệu và đặc tính hoạt động trên không. Ledger b05 đang dùng cách này; không kiểm tra tính nhất quán ở lô khác. “Tiểu đoàn Pháp sư Không chiến số 203” là phương án khác, nhưng nhấn vào chức năng chiến đấu hơn tên mô tả hiện có. |
| interdiction combat — p000110, p000111, p000119 | Giữ “tác chiến ngăn chặn”. | p000109 giao việc cầm chân lực lượng áp sát; p000110 chuyển nhiệm vụ, p000111 đối chiếu với trinh sát, p000119 xét quyền hủy. Cách gọi này phân biệt được với năng lực/đơn vị “đánh chặn” ở p000125, p000131. “Tác chiến cản bước” là phương án diễn nghĩa, nhưng kém thuận làm tên nhiệm vụ. Không suy ra đây là nhiệm vụ đánh đường tiếp tế. |
| recon-in-force — p000111, p000117, p000125, p000126 | Giữ “trinh sát chiến đấu”. | p000125 xác định khảo sát năng lực đánh chặn; p000126 dùng nhiệm vụ làm vỏ bọc che rút lui. Cách này giữ tính trinh sát và yếu tố đối đầu. “Trinh sát bằng vũ lực” là phương án literal; “trinh sát có vũ trang” dễ chỉ còn ý mang vũ khí, chưa thể hiện việc thăm dò bằng đối đầu. Không gọi đây là chuẩn thuật ngữ quân sự đã xác minh. |
| rear guard — p000126, p000128 | Giữ “lực lượng đoạn hậu”. | Nhóm này ở lại cầm cự/câu giờ để bảo đảm rút lui, có thể bị tiêu diệt; cách gọi thể hiện đúng vai trò và không thêm biên chế. “Lực lượng hậu vệ” là phương án khác nhưng ít rõ việc bảo vệ đoàn quân rút. Không đổi thành hậu phương hay hậu cần. |
| Rhine lines/front — p000109, p000129 | Giữ “phòng tuyến Rhine” / “mặt trận Rhine” theo từng chỗ. | p000109 là tuyến đang bị áp sát; p000129 là phạm vi mặt trận chứa các đơn vị truy đuổi. Không đồng nhất hai phạm vi. “Các tuyến phòng thủ Rhine” ở p000109 và “chiến tuyến Rhine” ở p000129 là phương án khác; chưa đủ căn cứ thêm vị trí dọc sông hoặc tên chiến dịch. |
| Matsusheeta — p000106 | Giữ Matsusheeta²⁵. | Package cung cấp dạng tên này và dấu gọi chú thích; phạm vi không cho mở chú thích để xác minh danh tính. Phương án khác là chuẩn hóa tên sau khi có nguồn được phép xác nhận, hiện chưa đề xuất dạng thay thế cụ thể. Không tự sửa chính tả hay nhận diện người thật. |
| CP / Fairy 01 — p000105, p000110 | Giữ CP, 01 và Fairy 01 theo đúng từng lượt thoại. | Cấu trúc vô tuyến cho phép nhận diện nhãn gọi, nhưng không đủ chứng cứ khai triển CP hoặc Việt hóa Fairy. p000105 dùng 01 rút gọn; p000110 dùng Fairy 01 đầy đủ. Phương án khác chỉ là khai triển/Việt hóa sau khi có chứng cứ được phép; không tự thêm nghĩa hoặc chữ số. |

Canon glossary và characters chưa chốt thuật ngữ/tên. DEC-P01-001 và DEC-P01-002 chỉ cung cấp chuẩn đại từ và biểu diễn nhấn mạnh; không phê duyệt bảy mục trên. Being X ở p000123 phù hợp cách giữ nguyên đang pending trong canon/glossary-pending.yml, không mở thêm một quyết định thứ tám.

## Pending và rủi ro còn lại

- Cả bảy lựa chọn vẫn pending/non-canon; đủ căn cứ để dùng tạm nhất quán trong b05, không cần dừng chờ quyết định. Coordinator tiếp nhận khuyến nghị vào ledger/handoff; reviewer không sửa các tệp đó.
- B05-R03 là lỗi vừa còn mở; cần translator sửa trước khi coi review này đã được xử lý. Ba góp ý nhẹ cũng chưa được áp dụng.
- Chưa xác minh danh tính Matsusheeta, nội dung chú thích ²⁵, nghĩa khai triển CP hoặc bản dịch Fairy. Giữ nguyên là phương án ít suy diễn nhất với phạm vi được giao.
- Không xác minh tính nhất quán liên lô hay chuẩn thuật ngữ quân sự bên ngoài; các khuyến nghị dựa vào package b05 và canon được phép đọc.
- Các điểm self-check tiếp nhận ở p000104, p000112, p000126, dấu chú thích p000106, giọng nén giận p000110 và lập luận p000130 đã hiện diện trong bản dịch đang đọc. Không tuyên bố đã đọc báo cáo phản biện trước đó hoặc đã kiểm tra validator.
- Không phát hiện lỗi nghiêm trọng, quyết định canon ảnh hưởng cốt truyện hoặc căn cứ cần mở rộng phạm vi. Validator và diff-check chưa chạy; reviewer không sửa bản dịch và không commit.
