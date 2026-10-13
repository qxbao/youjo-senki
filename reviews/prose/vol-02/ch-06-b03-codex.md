# Review — vol-02-ch-06-b03-review

- Vai trò: reviewer; chỉ báo cáo, không sửa bản dịch hoặc đầu vào.
- Đã đọc agents/shared.md, agents/reviewer.md, config/translation-pipeline.yml, handoff review và handoff gốc, translation, self-check, năm canon_references và riêng chapter6_b03_translation_proposals trong ledger.
- Package được giao: work/vol-02/batches/ch-06-b03-source.jsonl. SHA-256 thực tế khớp handoff: `65c888d732ceb171d6088586a60d67f294eac0110291225b6adec9ad03d50e5a`.
- Hash của cả năm file canon khớp handoff gốc. Package và translation có đủ 26 ID, cùng thứ tự, từ p000068 đến p000093.
- Chỉ dùng package được giao; không mở EPUB/PDF hoặc package khác. Không trích câu nguồn. Không chạy validator hoặc diff-check; không commit.

## Kết quả và cách đếm

Có **0 nghiêm trọng, 1 vừa, 6 nhẹ**, tất cả còn mở vì reviewer không sửa translation. Đếm theo finding; F01 là một lỗi hệ thống ảnh hưởng 18 ID, không phải 18 finding riêng. Số chưa giải quyết nghiêm trọng/vừa: **0/1**. Cần translator xử lý F01 trước khi coi lô đạt review. Bốn khuyến nghị thuật ngữ dưới đây đều là đề xuất tạm, không phải canon; chúng không tự tạo thêm finding mức vừa.

## Findings có thể hành động

### F01 — Vừa — Mất toàn bộ dấu nhấn mạnh được yêu cầu

ID: YS-LN02/Text/part0030.xhtml/p000068, YS-LN02/Text/part0030.xhtml/p000069, YS-LN02/Text/part0030.xhtml/p000070, YS-LN02/Text/part0030.xhtml/p000071, YS-LN02/Text/part0030.xhtml/p000072, YS-LN02/Text/part0030.xhtml/p000073, YS-LN02/Text/part0030.xhtml/p000074, YS-LN02/Text/part0030.xhtml/p000075, YS-LN02/Text/part0030.xhtml/p000076, YS-LN02/Text/part0030.xhtml/p000077, YS-LN02/Text/part0030.xhtml/p000078, YS-LN02/Text/part0030.xhtml/p000079, YS-LN02/Text/part0030.xhtml/p000080, YS-LN02/Text/part0030.xhtml/p000081, YS-LN02/Text/part0030.xhtml/p000084, YS-LN02/Text/part0030.xhtml/p000085, YS-LN02/Text/part0030.xhtml/p000086, YS-LN02/Text/part0030.xhtml/p000091.

Căn cứ: XHTML trong package có một vùng em bao toàn đoạn ở p000068–p000081 và p000084–p000086; p000091 có hai vùng em riêng. Translation tại cả 18 ID không có dấu sao. Điều này trái DEC-P01-002, làm mất tín hiệu phân biệt lời trích/tài liệu và nội tâm với trần thuật. Self-check khẳng định đã giữ những vùng này nhưng không khớp dữ liệu hiện tại.

Đề xuất: bao toàn nội dung translation của 17 đoạn được nhấn toàn đoạn bằng `*...*`; ở p000091 chỉ bao hai câu “Trong khi đó, kế hoạch của chúng ta đã thất bại hoàn toàn.” và “Đây thật sự là Quân đội Đế quốc của chúng ta sao?”. Không bao các câu trần thuật xen giữa; không thêm nhấn mạnh ở p000082–p000083 hoặc p000087–p000090, p000092–p000093. Translator cập nhật self-check sau sửa theo quyền được coordinator giao. Độ chắc chắn: cao.

### F02 — Nhẹ — YS-LN02/Text/part0030.xhtml/p000068

“nên vừa phải ổn định hậu phương” dùng “vừa” mà thiếu vế phối hợp, khiến yêu cầu đồng thời với thiếu quân tiền tuyến không rõ. Đề xuất sửa cụm này thành “nên yêu cầu đồng thời ổn định hậu phương gần như bất khả thi”. Giữ mức gần như không thể, không biến thành tuyệt đối không thể. Độ chắc chắn: cao.

### F03 — Nhẹ — YS-LN02/Text/part0030.xhtml/p000070

“phong trào ly khai độc lập” ghép hai bổ nghĩa khá cứng và không thể hiện rõ độc lập là mục tiêu của phong trào. Đề xuất “phong trào ly khai đòi độc lập” theo T02. Không suy thành tên tổ chức hoặc quy kết tính chính đáng. Hỏa lực và lựa chọn trấn áp còn được giữ; không cần nâng thành lỗi nghĩa mức vừa. Độ chắc chắn: khá cao về diễn đạt, vừa về tên gọi chính trị.

### F04 — Nhẹ — YS-LN02/Text/part0030.xhtml/p000071

Hai lần “họ” dễ đổi chủ thể: lần đầu có thể là bên điều quân, lần sau dễ bị đọc thành chính đơn vị được điều đi. Căn cứ p000069–p000070 cho phép làm rõ đây là lựa chọn sử dụng lực lượng của Đế quốc/Bộ chỉ huy. Đề xuất “nếu điều động các đơn vị ấy đến đây, Đế quốc sẽ không thể dùng lực lượng đó để chống đỡ một cuộc xâm lược”. Không đặt thêm tên người chỉ huy hoặc định danh cuộc xâm lược. Độ chắc chắn: cao.

### F05 — Nhẹ — YS-LN02/Text/part0030.xhtml/p000087

Sau giải mã JSON, translation bắt đầu bằng hai ký tự gạch chéo ngược rồi một dấu sao. Package chỉ có dấu sao chú thích, không có vùng em. Hai gạch chéo có thể để lại ký tự thừa khi dựng Markdown. Đề xuất giữ một dấu sao literal; nếu dùng escape Markdown thì chuỗi giải mã chỉ cần một gạch chéo trước dấu sao, được JSON escape đúng một lần. Không biến chú thích thành chữ nghiêng. Độ chắc chắn: cao về khác biệt ký tự; cách hiển thị cuối phụ thuộc renderer chưa được chạy.

### F06 — Nhẹ — YS-LN02/Text/part0030.xhtml/p000088

“vị chỉ huy quân đoàn rộng lượng giả vờ hỏi” đọc như lời đánh giá tính cách, làm câu khựng. Ngữ cảnh p000089 cho thấy cơn giận được kiềm lại; nét rộng lượng ở đây gắn với cách hỏi giả bộ nhã nhặn. Đề xuất “vị chỉ huy quân đoàn giả vờ hỏi bằng vẻ độ lượng”, giữ tiếp chi tiết cố giấu giọng run. Giữ “tham mưu trưởng”, “chỉ huy quân đoàn”, “ngài”; không suy thêm quân hàm. Độ chắc chắn: vừa; không nâng vẻ độ lượng thành thái độ thật.

### F07 — Nhẹ — YS-LN02/Text/part0030.xhtml/p000093

“bị gián đoạn trên thực tế” chuyển sắc thái gián đoạn vật chất của tuyến vận chuyển thành lời xác nhận tính thực tế, hơi mơ hồ. Đề xuất “tuyến vận chuyển ... sẽ bị đứt đoạn” để gắn trực tiếp với đoàn tàu tê liệt; không thêm cầu bị phá, đường ray bị hủy hoặc lượng hàng theo ngày. Các con số hàng chục nghìn tấn, tối thiểu 500 và nếu có thể 1.000 tấn cho mỗi sư đoàn đều được giữ đúng. Độ chắc chắn: khá cao.

## Khuyến nghị thuật ngữ tạm — không canon

| Mã / thuật ngữ nhận diện | ID | Khuyến nghị tạm | Phương án khác | Căn cứ và bất định |
| --- | --- | --- | --- | --- |
| T01 — intercepting mage unit | YS-LN02/Text/part0030.xhtml/p000069 | đơn vị pháp sư đánh chặn | đơn vị pháp sư ngăn chặn | Giữ chức năng đánh chặn và cấp gọi chung là đơn vị; p000070–p000073 đặt lực lượng này trong dự bị và khả năng chống địch ở mặt trận. “Ngăn chặn” rộng hơn, kém đặc trưng về nhiệm vụ. Tin cậy khá cao về chức năng; chưa biết biên chế, đối tượng đánh chặn hoặc đây có phải tên chính thức. Không thêm “không quân” hay “tiểu đoàn”. |
| T02 — separatist independent movement | YS-LN02/Text/part0030.xhtml/p000070 | phong trào ly khai đòi độc lập | phong trào ly khai giành độc lập; phong trào ly khai độc lập | Kết hợp tính ly khai với mục tiêu độc lập bằng tiếng Việt rõ hơn. “Đòi” tránh hàm ý mục tiêu đã đạt; “giành” nhấn hành động đấu tranh mạnh hơn mức cần thiết. Phương án ledger hiện tại giữ các thành tố nhưng cứng. Tin cậy khá cao về ý nghĩa, vừa về sắc thái chính trị; chưa xác lập danh xưng chính thức hoặc tư cách tổ chức. |
| T03 — suppression unit | YS-LN02/Text/part0030.xhtml/p000092 | đơn vị trấn áp | đơn vị dẹp loạn | Giữ chức năng của lực lượng được hứa điều đến, phù hợp việc dẹp nổi dậy đã nêu trong package. “Dẹp loạn” cụ thể và mang đánh giá về bên nổi dậy hơn; không cần tăng sắc thái. Tin cậy cao về chức năng, chưa rõ cấp tổ chức và không đủ căn cứ đồng nhất đơn vị này với T01. |
| T04 — Railroad Department | YS-LN02/Text/part0030.xhtml/p000092 | Bộ phận Đường sắt | Phòng Đường sắt; Cục Đường sắt | Package xác nhận cơ quan phụ trách quản lý lịch trình, không xác nhận cấp phòng/cục. Chọn cách gọi trung tính “Bộ phận” để tiếp tục mà không gán cấp tổ chức. “Phòng” là đề xuất ledger có thể dùng khi thêm căn cứ; “Cục” khẳng định cấp cao hơn và chưa có hỗ trợ. Tin cậy cao về lĩnh vực, thấp về cấp/tên chính thức; cách viết hoa cũng chỉ tạm. Không phải lỗi nghĩa mức vừa của lựa chọn “Phòng” hiện tại. |

Coordinator tiếp nhận các lựa chọn này vào ledger/handoff theo quyền của mình, translator áp dụng nhất quán; reviewer không sửa các file đó. Không có lựa chọn nào trong bốn mục cần dừng chờ người dùng theo chứng cứ được giao.

## Bao phủ đủ 26 ID

Mỗi dòng đã được xét nghĩa, văn phong, điểm nhìn, nhấn mạnh và thuật ngữ. “Không thêm finding” chỉ áp dụng trong package hiện tại.

| segment_id | Kết quả |
| --- | --- |
| YS-LN02/Text/part0030.xhtml/p000068 | F01, F02; giữ tình thế thiếu quân và yêu cầu đồng thời. |
| YS-LN02/Text/part0030.xhtml/p000069 | F01; T01. Giữ đối lập giữa lợi thế và khả năng tai hại. |
| YS-LN02/Text/part0030.xhtml/p000070 | F01, F03; T02. Giữ lực lượng dự bị và khả năng lựa chọn trấn áp. |
| YS-LN02/Text/part0030.xhtml/p000071 | F01, F04; giữ điều kiện và mất khả năng dùng cùng lực lượng. |
| YS-LN02/Text/part0030.xhtml/p000072 | F01; giữ lo ngại mặt trận sụp đổ và giới hạn tác dụng khi chiếm thành phố. |
| YS-LN02/Text/part0030.xhtml/p000073 | F01; giữ đối lập với tiền tuyến và hai khả năng tiêu diệt/đánh bật. |
| YS-LN02/Text/part0030.xhtml/p000074 | F01; chuỗi điều kiện và tổn thất tiêu hao được giữ, không biến dự báo thành việc đã xảy ra. |
| YS-LN02/Text/part0030.xhtml/p000075 | F01; giữ lựa chọn dự bị duy nhất, sa lầy, đột phá và sinh mạng mất uổng phí. |
| YS-LN02/Text/part0030.xhtml/p000076 | F01; mức bảo đảm thành công và lợi ích bất kể lựa chọn được giữ. |
| YS-LN02/Text/part0030.xhtml/p000077 | F01; sắc thái lên án có căn cứ trong lời người phát biểu. |
| YS-LN02/Text/part0030.xhtml/p000078 | F01; giữ thiếu thông tin về cả người ra lệnh và thi hành. |
| YS-LN02/Text/part0030.xhtml/p000079 | F01; giữ đồng thời tài năng quân sự và sự ô nhục. |
| YS-LN02/Text/part0030.xhtml/p000080 | F01; “tôi” là người phát biểu hậu chiến, không áp đại từ Tanya. |
| YS-LN02/Text/part0030.xhtml/p000081 | F01; giữ phân biệt kết quả cứu phòng tuyến với không tán thành phương pháp. |
| YS-LN02/Text/part0030.xhtml/p000082 | Không thêm finding; tên Walter Halbom được giữ, không có nhấn mạnh. |
| YS-LN02/Text/part0030.xhtml/p000083 | Không thêm finding; giữ chuyển video và tài liệu nội bộ. |
| YS-LN02/Text/part0030.xhtml/p000084 | F01; giữ khả thể và dấu trích trong nhận xét về tính thực dụng. Chủ thể nữ chưa được định danh chắc chắn. |
| YS-LN02/Text/part0030.xhtml/p000085 | F01; chuyển giữa ngôi ba và ngôi một có trong tài liệu nguồn. Giữ “cô/tôi” tạm, không tự quy về Tanya hoặc áp DEC-P01-001 sang tài liệu này. |
| YS-LN02/Text/part0030.xhtml/p000086 | F01; giữ câu hỏi trách nhiệm, ẩn dụ con thú và quy trách nhiệm cho người đưa vật hiến tế. |
| YS-LN02/Text/part0030.xhtml/p000087 | F05; đây là chú thích về ghi chú, không có vùng em. |
| YS-LN02/Text/part0030.xhtml/p000088 | F06; giữ vai trò người hỏi/người được hỏi, chưa suy tên hoặc quân hàm. |
| YS-LN02/Text/part0030.xhtml/p000089 | Không thêm finding; giữ bề ngoài kiềm chế và bên trong giận dữ của người chỉ huy. |
| YS-LN02/Text/part0030.xhtml/p000090 | Không thêm finding; giữ lượng tiếp viện nhỏ và thông tin trái dự tính; không thêm đơn vị/biên chế. |
| YS-LN02/Text/part0030.xhtml/p000091 | F01; hai câu ngôi một là nội tâm, xen trần thuật ngôi ba. Giữ xác suất phòng thủ mạnh lên và phán xét về quân đội. |
| YS-LN02/Text/part0030.xhtml/p000092 | T03, T04; giữ chậm trễ và cơn giận hướng tới cơ quan quản lý lịch trình. |
| YS-LN02/Text/part0030.xhtml/p000093 | F07; giữ điều kiện tê liệt chỉ một ngày, các lượng quân nhu và hệ quả quân số hao hụt. |

## Giới hạn và rủi ro

- Không đủ căn cứ định danh chủ thể nữ trong ghi chú p000084–p000086. Dùng “cô/tôi” là khuyến nghị bảo toàn ngôi và tránh suy diễn, không là quyết định canon về Tanya. Không gán người viết ghi chú.
- Cấp tổ chức của các đơn vị và cơ quan đường sắt vẫn chưa rõ. Các tên quân đội, Bộ Tổng tham mưu và Arene chỉ được đánh giá theo package và canon hiện có, không xác thực lore ngoài phạm vi.
- Self-check mô tả nhấn mạnh không phản ánh translation hiện tại; cần xác nhận lại sau sửa. Chưa chạy renderer để kiểm tra dấu chú thích F05.
- Chỉ một finding mức vừa còn mở: F01. Không có finding nghiêm trọng; không phát hiện quyết định canon ảnh hưởng cốt truyện cần escalation trong phạm vi này.
