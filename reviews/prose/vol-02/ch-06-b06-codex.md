# Review vol-02-ch-06-b06

- Vai trò: reviewer; task_id: `vol-02-ch-06-b06-review`.
- Đã đọc shared/persona reviewer, config, handoff, bản dịch, self-check, canon và các mục pending liên quan. Chỉ đối chiếu gói nguồn được giao; không mở EPUB/PDF hoặc gói nguồn khác.
- SHA-256 của `work/vol-02/batches/ch-06-b06-source.jsonl`: `1afb88d6570143a47f3950b1138107fe431183d677eceaecab40da5279606ede`, khớp handoff.
- Đã rà đủ 26 ID, nghĩa/văn phong/điểm nhìn/nhấn mạnh/thuật ngữ. Có 0 lỗi nghiêm trọng, 5 lỗi vừa, 4 lỗi nhẹ; tất cả còn mở vì reviewer không sửa đầu vào.
- Validator và diff_check: `not_run`. Không commit.

## Findings cần xử lý

### F01 — nhẹ — YS-LN02/Text/part0030.xhtml/p000174

“Ban hành lệnh chờ” thiếu rõ ràng trong tiếng Việt; “ngay khi nhận được tin” làm mờ tín hiệu ra lệnh hành động trong chuỗi chuẩn bị cơ động. Đề xuất “Ra lệnh sẵn sàng chờ lệnh. Bảo đảm chúng ta có thể cơ động ngay khi có lệnh.” Không cần suy thêm ai ban lệnh.

### F02 — vừa — YS-LN02/Text/part0030.xhtml/p000176

“Tổng tấn công” thêm quy mô/toàn diện mà nguồn tại ID chỉ xác nhận dấu hiệu một cuộc tiến công. Đề xuất “Dấu hiệu về một cuộc tiến công của phía Cộng hòa được xác nhận…”. Giữ nguyên việc xác nhận **dấu hiệu**, không chuyển thành xác nhận cuộc tiến công đã xảy ra.

### F03 — nhẹ — YS-LN02/Text/part0030.xhtml/p000178

“Đã gia nhập phe du kích” dễ bị hiểu là lực lượng tăng viện chuyển sang làm thành viên của một phe, trong khi nguồn và p000179 hỗ trợ việc hợp lực/hội quân. Đề xuất “lực lượng tăng viện của Quân đội Cộng hòa đã hội quân với lực lượng du kích”. Không thay đổi kết luận ưu tiên giữ phòng tuyến ở cuối đoạn.

### F04 — vừa — YS-LN02/Text/part0030.xhtml/p000179

“Tiếp tế đường không” tự thu hẹp đối tượng được đưa xuống thành vật tư. Ngay trong ID này, lực lượng được nhận diện là pháp sư và đang hội quân với quân nổi dậy; p000178 cũng đã nêu tăng viện. Đề xuất mở đầu “Đưa quân xuống bằng đường không ư?!”; phương án ngắn hơn là “Đổ quân đường không ư?!”. Không dùng “nhảy dù” khi package chưa nêu cơ chế dù.

“Chiến dịch đổ bộ đường không” ở vế sau có thể diễn đạt được việc đưa lực lượng vào khu vực bằng đường không, nên bản thân cụm này không phải lỗi nghĩa chắc chắn. Tuy nhiên, ledger có đề xuất tạm ở chương 3 ưu tiên “đột kích đường không” để phân biệt với hoạt động đổ bộ trên biển. Đề xuất tại đây: “Quân đội Cộng hòa đang tiến hành một chiến dịch đột kích đường không!”. Đây là lựa chọn tạm, không canon; điểm bắt buộc sửa là cách hiểu tiếp tế ở vế đầu. Giữ “Có vẻ” cho việc hội quân.

### F05 — nhẹ — YS-LN02/Text/part0030.xhtml/p000180

“Sở chỉ huy” gán một dạng cơ quan cụ thể cho Control và làm mờ phân biệt với Command tại p000176. Ledger có các lựa chọn pending giữ nguyên Control, đồng thời cảnh báo không đồng nhất với Command; không đủ căn cứ trong package này để khai triển thành Norden Control hoặc Urban Control. Đề xuất tạm “Tiếng hét thất thanh từ Control.”; phương án Việt hóa trung tính “Tiếng hét thất thanh từ bộ phận kiểm soát.” Không xem đây là tên cơ quan đã chốt.

### F06 — vừa — YS-LN02/Text/part0030.xhtml/p000181

“Vẫn có khả năng … đủ sức xử lý” và “có lẽ có thể giải quyết” chuyển khả thể của phương án trước khi pháp sư tham chiến thành đánh giá còn mở ở hiện tại. Ngữ cảnh p000179–p000185 đã xác lập pháp sư tham chiến, nên cần giữ giả định đối lập đó và bình diện thời gian của khả thể. Đề xuất “Nếu họ chỉ là những kẻ nổi dậy có vũ trang mà không có pháp sư, thì dù khó dẹp yên, lực lượng cảnh sát vẫn có thể đã đủ sức xử lý. Hoặc có lẽ một sư đoàn bộ binh cũng đã có thể giải quyết.” Không biến giả định thành kết quả đã thực sự xảy ra.

### F07 — nhẹ — YS-LN02/Text/part0030.xhtml/p000182

“Có lời đồn rằng” thêm sắc thái tin đồn/chưa đáng tin. Nguồn chỉ dẫn một nhận định được truyền đạt, ít được công khai nhấn mạnh. Đề xuất “Điều này ít được nói công khai, nhưng người ta cho rằng pháp sư thực sự phát huy tốt nhất trong các trận đánh ở đô thị.” Giữ trạng thái nhận định gián tiếp, không biến thành sự thật được người kể xác quyết.

### F08 — vừa — YS-LN02/Text/part0030.xhtml/p000184

“Họ có lẽ đã trấn áp được đám đông” dễ thành phỏng đoán rằng việc trấn áp đã hoàn tất. Đây là khả thể quá khứ của phương án cảnh sát/Bộ Nội vụ trong lập luận đối chiếu với tình thế có pháp sư, không phải báo cáo kết quả. Đề xuất “Với nhân lực của cảnh sát và Bộ Nội vụ, họ có thể đã đủ sức trấn áp đám đông, dù phải đổ máu để làm được việc đó.” Giữ tính khả thể, không xác nhận kết quả.

### F09 — vừa — YS-LN02/Text/part0030.xhtml/p000190

Trường translation không có Markdown nhấn mạnh, trong khi XHTML tại ID có hai phạm vi riêng. Self-check nói đã giữ hai phạm vi nhưng không khớp bản dịch đang được review. Theo DEC-P01-002, đề xuất đoạn tương ứng: “*Chỉ vì lý do ấy thôi* chăng? Hay *chính vì thế?*—…”. Không in nghiêng “chăng?” hoặc “Hay”; giữ dấu hỏi bên trong phạm vi thứ hai. Coordinator/translator cần đối chiếu lại self-check sau sửa.

## Thuật ngữ tạm, không canon

### Feldgendarmerie — YS-LN02/Text/part0030.xhtml/p000171

- Đề xuất tốt nhất trong phạm vi được giao: **giữ nguyên Feldgendarmerie**.
- Phương án khác: **hiến binh dã chiến**.
- Căn cứ: p000169 nêu quân cảnh trong lực lượng kiểm soát khu vực; p000171 dùng một danh xưng riêng trong lời đánh giá về sự bất tài. Package đủ hỗ trợ quan hệ chức năng quân cảnh nhưng chưa xác lập cơ cấu, cấp tổ chức hay cách Việt hóa chính thức. Giữ nguyên cũng nhất quán với lựa chọn tạm của coordinator b04 và đề xuất b06 trong ledger.
- Độ bất định: thấp về việc giữ định danh hiện có; vừa về tương đương Việt hóa “hiến binh dã chiến”. Không suy cơ cấu hoặc lịch sử của tổ chức ngoài đời; không nâng thành canon. Không tính việc giữ nguyên hiện tại là lỗi. “Đám … bất tài” có căn cứ về giọng phê phán tại ID, không cần trung hòa.

### Các lựa chọn liên quan khác

- p000179: airdrop → “đưa quân xuống bằng đường không”; alternative “đổ quân đường không”; bất định về cơ chế vận chuyển/thả quân, không tự thêm dù. airborne operation → “chiến dịch đột kích đường không”; alternative “chiến dịch đổ bộ đường không”; ưu tiên lựa chọn ledger, không xem alternative là lỗi nghĩa tự thân.
- p000180: Control → giữ nguyên Control; alternative “bộ phận kiểm soát”; chưa biết tên đầy đủ/cấp cơ quan. Không áp dụng tên riêng của địa bàn khác.
- p000175: giữ “đám cháy” như hình ảnh tình hình tự lắng xuống; không bắt buộc đổi thành thuật ngữ pending “bão lửa” của ngữ cảnh khác.

## Bao phủ toàn bộ ID

Mọi ID dưới đây mang tiền tố `YS-LN02/Text/part0030.xhtml/`; “không phát hiện lỗi” chỉ là kết quả review trong package được giao.

| ID | Kết quả |
|---|---|
| p000168 | Không phát hiện lỗi; câu hỏi giữ độ mở về tình hình. |
| p000169 | Không phát hiện lỗi; giữ lực lượng phối hợp và mức chắc chắn. |
| p000170 | Không phát hiện lỗi. |
| p000171 | Không phát hiện lỗi cần sửa; giữ hai nguy cơ hậu phương/tiền tuyến; khuyến nghị Feldgendarmerie ở trên. |
| p000172 | Không phát hiện lỗi; giữ mức dự báo thảm họa và nguy cơ vỡ phòng tuyến. |
| p000173 | Không phát hiện lỗi. |
| p000174 | F01, nhẹ. |
| p000175 | Không phát hiện lỗi; giữ nội tâm “mình” và hình ảnh đám cháy. |
| p000176 | F02, vừa. |
| p000177 | Không phát hiện lỗi. |
| p000178 | F03, nhẹ. |
| p000179 | F04, vừa; đã đánh giá riêng thuật ngữ đột kích/đổ bộ đường không. |
| p000180 | F05, nhẹ. |
| p000181 | F06, vừa. |
| p000182 | F07, nhẹ. |
| p000183 | Không phát hiện lỗi. |
| p000184 | F08, vừa. |
| p000185 | Không phát hiện lỗi; giữ yêu cầu đánh chiếm từng khu và bất chấp thiệt hại. |
| p000186 | Không phát hiện lỗi; giữ điểm yếu không chiến và mạng phòng không 360 độ dưới dạng kế hoạch đáng lẽ có. |
| p000187 | Không phát hiện lỗi đủ rõ để yêu cầu sửa; không suy danh tính lực lượng. |
| p000188 | Không phát hiện lỗi cần sửa; giữ chênh lệch kế hoạch/thực trạng và thiếu lực lượng luân phiên. |
| p000189 | Không phát hiện lỗi cần sửa; giữ chuỗi nhiệm vụ tăng ngoài dự kiến và nhận thức về kiểm soát bầu trời. |
| p000190 | F09, vừa; hai phạm vi nhấn mạnh bị mất. |
| p000191 | Không phát hiện lỗi; giữ mức ưu thế có giới hạn và đảo vai công/thủ. |
| p000192 | Không phát hiện lỗi. |
| p000193 | Không phát hiện lỗi; giữ câu hỏi về đối phương đã sẵn sàng. |

## Bàn giao

Review đã hoàn tất; bản dịch chưa đạt điều kiện không còn lỗi vừa. Coordinator chuyển F01–F09 cho translator đang giữ quyền sửa và ghi các khuyến nghị thuật ngữ dưới trạng thái pending. Reviewer không sửa translation, self-check, ledger hoặc canon; không cần chờ người dùng cho các lựa chọn tạm này.
