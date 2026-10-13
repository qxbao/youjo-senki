# Review — vol-02-ch-05-b26-review

- Vai trò: reviewer; chỉ đối chiếu lô được giao, không sửa bản dịch.
- Đã đọc `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff review và handoff gốc b26, bản dịch b26, self-check b26, đúng năm tệp canon trong handoff gốc và mục `chapter5_b26_translation_proposals` trong ledger.
- Package: `work/vol-02/batches/ch-05-b26-source.jsonl`; SHA-256 thực tế và handoff cùng là `c29cd1ba4c44371ee2a0103097f9e2ecd6697fc4b3e4761b16516b0e7ffc0110`. Hash của cả năm tệp canon khớp handoff gốc.
- Package và bản dịch đều có 37 ID, cùng thứ tự, từ `YS-LN02/Text/part0028.xhtml/p000040` đến `YS-LN02/Text/part0028.xhtml/p000076`.
- Không mở EPUB/PDF hoặc package khác; không dùng lore hay tra cứu ngoài để lấp ngữ cảnh. Không tạo graph hoặc dữ liệu phụ vì phạm vi chỉ cho phép ghi báo cáo này.
- Validator: `not_run`; diff_check: `not_run`; commit: `null`.

## Kết quả và cách đếm

Chưa nên coi bản dịch đã xử lý xong review. Có **0 lỗi nghiêm trọng, 4 lỗi vừa, 6 lỗi nhẹ**, tất cả còn mở vì reviewer không sửa bản dịch. Đếm theo finding độc lập; một finding có thể bao phủ nhiều ID. Số unresolved nghiêm trọng/vừa: **0/4**. Bốn khuyến nghị thuật ngữ bên dưới đều là phương án tạm, không phải canon và không phải bốn lỗi bổ sung.

## Findings còn mở

### M01 — Vừa — Điểm nhìn và đại từ nội tâm

**ID:** `YS-LN02/Text/part0028.xhtml/p000048`, `YS-LN02/Text/part0028.xhtml/p000055`, `YS-LN02/Text/part0028.xhtml/p000056`, `YS-LN02/Text/part0028.xhtml/p000058`.

Sau chuyển cảnh p000044–p000045, chủ thể tự quy chiếu là Tanya: p000048 nối suy nghĩ về tiếp tế với lời kể gọi tên Tanya; p000055–p000058 nối việc nó kiểm tra thức ăn với cấp dưới và Weiss xuất hiện. Không có dấu chuyển lại Grantz trong package. “Tôi” ở các phần nội tâm này trái DEC-P01-001; p000056 và p000058 còn trộn “tôi”/“mình” ngay trong cùng đoạn. Đề nghị đổi các tự quy chiếu nội tâm ấy sang “mình”, kể cả “tôi sắp…” ở p000058. Giữ “tôi” của người kể đầu lô và trong thoại p000064/p000074; không đổi toàn bộ ngôi thứ nhất máy móc. Căn cứ điểm nhìn: mạnh; không suy rộng ra ngoài lô.

### M02 — Vừa — Mất toàn bộ bốn vị trí nhấn mạnh

**ID:** `YS-LN02/Text/part0028.xhtml/p000050`, `YS-LN02/Text/part0028.xhtml/p000051`, `YS-LN02/Text/part0028.xhtml/p000061`, `YS-LN02/Text/part0028.xhtml/p000072`.

XHTML trong package có dấu nhấn ở cả bốn đoạn, nhưng bản dịch không có Markdown tương ứng. Đây là mất thông tin theo DEC-P01-002, không phải lựa chọn biên tập tùy ý. Khôi phục đúng phạm vi:

- p000050: `*Chắc mình nên tránh ra ngoài một thời gian, nếu không cần thiết*`; lời dẫn Tanya nghĩ nằm ngoài dấu nhấn.
- p000051: `*Hôm nay chắc chắn sẽ có rắc rối.*`; phần trần thuật tiếp sau không nghiêng.
- p000061: chỉ `*không hài lòng*` hoặc cụm tương đương nếu sửa văn phong.
- p000072: chỉ liên từ `*và*` tương ứng với sự cộng thêm hai tính chất trong nhánh thứ hai; xem M04.

Không thêm chữ nghiêng vào những đoạn nội tâm khác vốn không được đánh dấu trong package. Căn cứ: trực tiếp, độ bất định thấp.

### M03 — Vừa — Thành ngữ bị dịch thành hành động vật lý

**ID:** `YS-LN02/Text/part0028.xhtml/p000049`.

“Không khuấy động mặt nước” không truyền đạt rõ quy tắc hành chính tránh xáo trộn, đi cùng việc tuân tiền lệ. Cách dịch hiện tại dễ thành hình ảnh vật lý không có chức năng trong lập luận. Đề nghị “những quy tắc sắt đá: tuân tiền lệ và tránh gây xáo trộn”. Phương án khác: “theo tiền lệ và giữ nguyên nếp cũ”; phương án này nhấn việc duy trì hiện trạng hơn, nên ưu tiên cách đầu trung tính. Giữ nhận xét ví chúng với hiện tượng tự nhiên; không thêm giải thích về tham nhũng hay động cơ của sĩ quan. Căn cứ thành ngữ và ngữ cảnh hành chính: mạnh.

### M04 — Vừa — Cấu trúc hai khả năng bị hỏng

**ID:** `YS-LN02/Text/part0028.xhtml/p000072`.

“Vừa ngu ngốc hoặc…” trộn cấu trúc cộng tính chất với cấu trúc lựa chọn, khiến hai khả năng khó phân biệt. Ý là nhánh thứ nhất ngu ngốc, nhánh thứ hai vừa hết sức phiền phức vừa ngu ngốc. Đề nghị: “Nói chung, chuyện này hoặc sẽ ngu ngốc, hoặc sẽ cực kỳ phiền phức *và* ngu ngốc.” Giữ sự lặp lại có chủ ý, giọng bực bội và dấu nhấn ở liên từ của nhánh thứ hai; không nhấn cả câu. Căn cứ: trực tiếp, độ bất định thấp. Phần thiếu dấu nhấn đã đếm ở M02, không đếm thêm.

### L01 — Nhẹ — Kết hợp từ chưa tự nhiên

**ID:** `YS-LN02/Text/part0028.xhtml/p000043`.

“Đã chấp nhận tôi cứng cáp hơn” dễ đọc như một cấu trúc thiếu từ nối. Đề nghị “đã công nhận tôi có phần cứng cáp hơn…” hoặc “đã xem tôi là người cứng cáp hơn đôi chút…”. Giữ hình ảnh chim non mới nở và mức độ tiến bộ nhỏ, không nâng thành sự công nhận hoàn toàn của tập thể.

### L02 — Nhẹ — Sắc thái chuẩn bị tinh thần

**ID:** `YS-LN02/Text/part0028.xhtml/p000051`.

“Tự trấn tĩnh” nhấn làm dịu cảm xúc, còn ngữ cảnh là Tanya chuẩn bị tinh thần đương đầu với rắc rối. Đề nghị “Tanya chuẩn bị tinh thần” hoặc “Tanya tự củng cố tinh thần”. Không suy ra nó đang hoảng loạn. Thuật ngữ cấp độ sẵn sàng trong cùng đoạn có thể giữ theo T04.

### L03 — Nhẹ — Cụm chính sách đối ngoại nặng và hơi mạnh nghĩa

**ID:** `YS-LN02/Text/part0028.xhtml/p000056`.

Đây là đánh giá cờ review về “cú hích”. Bản hiện tại giữ được phỏng đoán về tác động đã có thể xảy ra, việc đưa về hậu phương và điều kiện ngộ độc; chưa có căn cứ kết luận nó đảo nghĩa hoặc thay đổi quan hệ nhân quả. Tuy nhiên, “cú hích… tạo ra cho chính sách” vừa nặng cú pháp vừa dễ gợi một tác động thúc đẩy tích cực/mạnh hơn cần thiết. Đề nghị tạm “vì tác động nhỏ mà có lẽ mình đã gây ra đối với chính sách đối ngoại về Khối Thịnh vượng chung”. Có thể giữ “cú hích” nếu chỉnh thành “vì có lẽ mình đã tạo một cú hích cho…”; phương án này vẫn mang sắc thái thúc đẩy rõ hơn.

Không xác định chiều hướng chính sách, ý đồ của cấp trên hay tổ chức lịch sử ngoài đời. Không đổi phỏng đoán thành sự kiện đã chắc chắn xảy ra; giữ giả định ngộ độc và khả năng bị hy sinh ở câu sau. “Tôi tự hỏi” thuộc M01. Độ bất định về sắc thái tác động: vừa; về nội dung chính trị cụ thể: cao.

### L04 — Nhẹ — Tên vật/thông tin truyền tin cần trung tính và rõ hơn

**ID:** `YS-LN02/Text/part0028.xhtml/p000067`, `YS-LN02/Text/part0028.xhtml/p000071`.

Đây là đánh giá cờ review kỹ thuật. “Mật mã ngắn” là cách bám mặt chữ có thể hiểu được, nhưng có thể khiến người đọc nghĩ tới khóa/hệ mã hoặc mật khẩu thay vì thông tin được đưa cho Tanya. p000071 cho thấy nó là thứ dùng để truyền nội dung khi không cần hoặc không thể dùng điện tín. Đề nghị tạm “bản tin mã hóa ngắn”, áp dụng nhất quán cả hai ID, với giới hạn ở T03. Không có căn cứ xác định mã cụ thể, giấy/tấm thẻ, người giải mã hay phương tiện vận chuyển.

“Ống đựng điện tín” thu hẹp vật đựng thông điệp thành vật chỉ chứa điện tín. Ưu tiên “ống đựng thông điệp” ở p000067; lựa chọn khác là “ống đựng thư tín”. Giữ đối lập giữa hai dạng và phản ứng ngờ rắc rối. Không tự sửa mối liên hệ điện tín ở p000059: cách gọi bao quát ở đó và sự phân biệt ở p000067 cùng tồn tại trong package. Độ bất định: vừa đến cao đối với cách gọi kỹ thuật; không coi lựa chọn hiện tại là lỗi chuyên ngành đã được chứng minh.

### L05 — Nhẹ — Làm rõ người được đọc trước và chức năng thông tin

**ID:** `YS-LN02/Text/part0028.xhtml/p000070`.

“Không ai được đọc trước” lược đối tượng so sánh, dù người đọc có thể suy ra chỉ huy. “Điện báo viên” có thể phù hợp hệ thống điện tín trong đoạn trước, nhưng package tại ID này nhận diện người vận hành vô tuyến; chưa đủ căn cứ đồng nhất mọi chức danh. Đề nghị trung tính: “Miễn là điện đề tên người chỉ huy, ngoài nhân viên vô tuyến ra, không ai được đọc trước người chỉ huy.” Phương án “vô tuyến viên” gọn hơn; không suy thêm cấp bậc hay quy trình giải mã. Đây là làm rõ chi tiết, không kết luận bản hiện tại làm sai toàn bộ quy tắc bảo mật. Độ bất định thuật ngữ: vừa.

### L06 — Nhẹ — Thêm đánh giá thời lượng ngày

**ID:** `YS-LN02/Text/part0028.xhtml/p000075`.

“Một ngày dài” thêm đánh giá ngày kéo dài; ngữ cảnh đang than về một ngày tồi tệ và dự báo ở p000076. Đề nghị “Ôi, đúng là một ngày!” hoặc “Ôi, ngày gì thế này!” để giữ cảm thán mà không thêm thời lượng. Không cần giải thích hay tăng mức bi kịch.

## Bốn lựa chọn thuật ngữ tạm

| Mã | Thuật ngữ nhận diện | ID đầy đủ | Ưu tiên tạm | Phương án khác và lý do | Độ bất định / giới hạn |
| --- | --- | --- | --- | --- | --- |
| T01 | Commonwealth | YS-LN02/Text/part0028.xhtml/p000056 | Khối Thịnh vượng chung | Liên bang Thịnh vượng chung là lựa chọn trong ledger, nhưng tự gợi cấu trúc liên bang mà package không xác nhận. Giữ phương án đang dùng để nhất quán và ít thêm thông tin hơn. | Vừa–cao: chưa rõ cấu trúc chính trị; không đồng nhất với tổ chức ngoài đời. Pending, không canon. |
| T02 | magical interference formulas | YS-LN02/Text/part0028.xhtml/p000047 | thuật thức gây nhiễu | công thức gây nhiễu ma thuật bám cấu tạo từ hơn nhưng nặng và dễ gợi công thức toán. Trong package, thuật ngữ xuất hiện dưới dạng interference formulas, gắn với đạn để nạp; cách gọi ledger dài hơn không phải lý do thêm cơ chế. | Vừa: chức năng gây nhiễu được hỗ trợ, đối tượng/cơ chế gây nhiễu chưa rõ. Không đổi thành thuật thức chống phép hay nhiễu vô tuyến. Pending, không canon. |
| T03 | short cipher | YS-LN02/Text/part0028.xhtml/p000067; YS-LN02/Text/part0028.xhtml/p000071 | bản tin mã hóa ngắn | mật mã ngắn là phương án literal nếu cần tránh diễn giải danh từ; mật mã rút gọn trong ledger gợi thao tác rút gọn không được xác nhận. Ưu tiên bản tin vì thứ được trình và dùng để gửi nội dung trong p000067–p000071, không phải một hệ mật mã được mô tả. | Vừa–cao: package không xác định dạng vật lý hoặc kỹ thuật mã hóa; “bản tin” là suy luận chức năng tại chỗ. Nếu cần literal tối đa, dùng “bản mật mã ngắn”. Pending, không canon. |
| T04 | combat readiness level two | YS-LN02/Text/part0028.xhtml/p000051 | trạng thái sẵn sàng chiến đấu cấp độ hai | mức sẵn sàng chiến đấu hai là lựa chọn gọn cùng nghĩa. Cấp báo động chiến đấu hai trong ledger gợi một hệ thống báo động cụ thể hơn package cho phép. Giữ mức hai và trạng thái sẵn sàng phản ứng nhanh. | Thấp về cách diễn đạt literal; cao về định nghĩa của cấp hai và hệ thống cấp độ. Không ánh xạ sang hệ thống quân sự ngoài đời. Pending, không canon. |

Các lựa chọn này đủ để translator tiếp tục mà không cần chờ quyết định thông thường về thuật ngữ. Coordinator có thể ghi chúng dưới trạng thái đề xuất; reviewer không sửa ledger/canon. Cách gọi ngòi nổ tại p000047 vẫn là mô tả tạm: package không đủ để kết luận cơ chế kỹ thuật khác, nên không tạo thêm lỗi dựa trên giả định.

## Bao phủ đủ 37 ID

Mỗi dòng đã được đối chiếu nghĩa, văn phong, điểm nhìn, nhấn mạnh và thuật ngữ khi có. “Không thêm finding” có nghĩa không thấy vấn đề đủ căn cứ ngoài các mục đã nêu, không xác lập canon. Tiền tố cho toàn bộ ID là `YS-LN02/Text/part0028.xhtml/`.

| ID ổn định | Kết quả |
| --- | --- |
| YS-LN02/Text/part0028.xhtml/p000040 | Không thêm finding; giữ phỏng đoán của người kể về lần giết người đầu tiên. |
| YS-LN02/Text/part0028.xhtml/p000041 | Không thêm finding; giữ sự đối chiếu ký ức với trạng thái hiện tại. |
| YS-LN02/Text/part0028.xhtml/p000042 | Không thêm finding; chỉ dẫn sống sót và lời gọi Trung úy phù hợp đoạn. |
| YS-LN02/Text/part0028.xhtml/p000043 | L01; giữ hành động vỗ vai và ẩn dụ tiến bộ nhỏ. |
| YS-LN02/Text/part0028.xhtml/p000044 | Không thêm finding; giữ chuyển thời gian. |
| YS-LN02/Text/part0028.xhtml/p000045 | Không thêm finding; chuyển điểm nhìn Tanya, “nó” phù hợp. |
| YS-LN02/Text/part0028.xhtml/p000046 | Không thêm finding; giữ mức suôn sẻ bất thường và thời gian tiếp tế. |
| YS-LN02/Text/part0028.xhtml/p000047 | T02; không thêm finding về ngòi nổ khi thiếu bằng chứng kỹ thuật. |
| YS-LN02/Text/part0028.xhtml/p000048 | M01; nhận xét nội tâm thuộc Tanya, không phải quay lại người kể đầu lô. |
| YS-LN02/Text/part0028.xhtml/p000049 | M03; thành ngữ phải diễn đạt quy tắc tránh xáo trộn. |
| YS-LN02/Text/part0028.xhtml/p000050 | M02; “mình” và lời dẫn điểm nhìn đúng, thiếu dấu nhấn. |
| YS-LN02/Text/part0028.xhtml/p000051 | M02, L02, T04; giữ kế hoạch đề phòng và mức hai. |
| YS-LN02/Text/part0028.xhtml/p000052 | Không thêm finding; giữ bữa ăn thật và món tráng miệng. |
| YS-LN02/Text/part0028.xhtml/p000053 | Không thêm finding; giữ tuyến tiếp tế bất thường. |
| YS-LN02/Text/part0028.xhtml/p000054 | Không thêm finding; giữ đối lập cấp dưới ăn ngay/Tanya kiểm tra. |
| YS-LN02/Text/part0028.xhtml/p000055 | M01; không suy diễn chi tiết tình trạng liên quan khoai tây ngoài package. |
| YS-LN02/Text/part0028.xhtml/p000056 | M01, L03, T01; cờ chính sách được đánh giá riêng, giữ bất định và giả định. |
| YS-LN02/Text/part0028.xhtml/p000057 | Không thêm finding; chủ thể cấp dưới liên tục với Tanya. |
| YS-LN02/Text/part0028.xhtml/p000058 | M01; giữ điều kiện thức ăn không có vấn đề và khoảnh khắc bị ngắt. |
| YS-LN02/Text/part0028.xhtml/p000059 | Không thêm finding; Weiss xuất hiện làm lỡ cơ hội ăn. Quân hàm là cách gọi tạm theo package. |
| YS-LN02/Text/part0028.xhtml/p000060 | Không thêm finding; giữ lời gọi Thiếu tá và xuất xứ từ Bộ chỉ huy. |
| YS-LN02/Text/part0028.xhtml/p000061 | M02; hành động đáp lễ và sự không hài lòng được giữ. |
| YS-LN02/Text/part0028.xhtml/p000062 | Không thêm finding; “mình”, điều kiện phản thực và ý đuổi ngay phù hợp. |
| YS-LN02/Text/part0028.xhtml/p000063 | Không thêm finding; giữ bực bội và tự biết phản ứng theo cảm xúc. |
| YS-LN02/Text/part0028.xhtml/p000064 | Không thêm finding; “tôi” trong thoại hợp lệ, không thuộc M01. |
| YS-LN02/Text/part0028.xhtml/p000065 | Không thêm finding; giữ do dự thông thường và ngoại lệ không nhượng bộ. |
| YS-LN02/Text/part0028.xhtml/p000066 | Không thêm finding; giữ xin lỗi và tính khẩn cấp. |
| YS-LN02/Text/part0028.xhtml/p000067 | L04, T03; cờ kỹ thuật được đánh giá, không tự dựng cơ chế truyền tin. |
| YS-LN02/Text/part0028.xhtml/p000068 | Không thêm finding; câu hỏi vẫn phủ định việc đây là mệnh lệnh. |
| YS-LN02/Text/part0028.xhtml/p000069 | Không thêm finding; giữ phương thức truyền mệnh lệnh thông thường. |
| YS-LN02/Text/part0028.xhtml/p000070 | L05; làm rõ đọc trước chỉ huy và thuật ngữ nhân viên vô tuyến. |
| YS-LN02/Text/part0028.xhtml/p000071 | L04, T03; giữ hai trường hợp không cần/không thể truyền bằng điện tín. |
| YS-LN02/Text/part0028.xhtml/p000072 | M04, M02; sửa hai nhánh lựa chọn và nhấn liên từ. |
| YS-LN02/Text/part0028.xhtml/p000073 | Không thêm finding; giữ triệu tập trình diện ngay. “Cô” trong thoại xét riêng, không bị quy tắc “nó” cho trần thuật chi phối. |
| YS-LN02/Text/part0028.xhtml/p000074 | Không thêm finding; giữ nhắc lại lệnh triệu tập và xác nhận hiểu. |
| YS-LN02/Text/part0028.xhtml/p000075 | L06; bỏ suy diễn thời lượng ngày. |
| YS-LN02/Text/part0028.xhtml/p000076 | Không thêm finding; giữ dự báo điều tồi tệ sắp tới. |

## Rủi ro và bước xử lý

Phạm vi package đủ để chọn các phương án tạm trên; không đủ để xác nhận hệ thống quân hàm toàn truyện, cấu trúc Commonwealth hoặc cơ chế mã hóa/gây nhiễu. Self-check nhắc Serebryakov nhưng tên này không xuất hiện trong 37 đoạn được giao, nên không kiểm chứng quân hàm đó bằng package khác. Không có lỗi nghiêm trọng hoặc quyết định canon ảnh hưởng cốt truyện cần dừng từ bằng chứng của lô này.

Translator cần xử lý M01–M04 và cân nhắc L01–L06; sau đó coordinator thực hiện kiểm tra theo pipeline. Báo cáo chỉ hoàn tất việc review, không xác nhận batch đã đạt validator hoặc hoàn tất dịch.
