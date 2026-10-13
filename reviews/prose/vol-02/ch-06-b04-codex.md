# Review vol-02-ch-06-b04-review

Vai trò: reviewer (Codex). Đã đối chiếu đủ 38 ID về nghĩa, văn phong, điểm nhìn, nhấn mạnh và thuật ngữ. Báo cáo hoàn tất; bản dịch cần sửa trước khi sign-off. Không sửa đầu vào, không commit, không chạy validator hoặc diff-check.

## Đầu vào và giới hạn

- Đã đọc `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff review và handoff nền `handoffs/vol-02/ch-06-b04.yml`.
- Chỉ đối chiếu nguồn từ `work/vol-02/batches/ch-06-b04-source.jsonl`; SHA-256 khớp `f667b42079f2a4e86e9c9461ac282ffbba00b3399f95fbf2f69e5bc798dd9308`. Không mở EPUB/PDF hoặc gói nguồn khác.
- Đã đọc `translations/vol-02/ch-06-b04.jsonl`, self-check tương ứng, cả năm tài liệu canon được handoff nền chỉ định và bốn mục `chapter6_b04_translation_proposals` trong ledger. Hash của cả năm tài liệu canon khớp handoff nền.
- Danh sách ID nguồn và bản dịch đều khớp 38 ID được giao, đúng thứ tự. Đây là kiểm tra đầu vào cho review, không thay thế validator.
- Canon glossary và characters chưa có mục chốt. Áp dụng DEC-P01-001 trong đúng giới hạn Tanya; không áp đại từ của Tanya sang vị tư lệnh ở lô này. Áp dụng DEC-P01-002 cho phạm vi chữ nghiêng.
- Self-check báo giữ đủ nhấn mạnh, nhưng đối chiếu XHTML trong package cho thấy p000097 bị mất một vùng chữ nghiêng. Kết quả validator/diff-check ghi trong self-check không được coi là do reviewer chạy.

## Findings theo mức độ và ID

### Nghiêm trọng — S01

**YS-LN02/Text/part0030.xhtml/p000129 — Đổi đối tượng của điều kiện pháp lý thành không còn người nào.**

Bản dịch kết thúc bằng “đảm bảo rằng không còn ai”. Đối tượng bị phủ định trong nguồn là người không tham chiến, không phải toàn bộ người trong thành phố. Nguồn giữ sự nhập nhằng giữa thủ thuật pháp lý và hậu quả thực tế; câu hỏi về giết tất cả ở p000130 là phản ứng tiếp theo của người nghe. Bản dịch hiện tại khẳng định trước một cách tuyệt đối rằng không còn bất kỳ ai, làm sai logic của kế hoạch vốn vẫn giả định có lực lượng địch.

Đề nghị thay phần kết bằng “vậy thì ta chỉ cần bảo đảm rằng không còn người không tham chiến nào”, đồng thời dùng cùng cách gọi ở p000123. Giữ lời về lừa dối và tính hợp lệ; không tự giải thích thủ tục, sơ tán hay cách tái phân loại người dân. Căn cứ cao về đối tượng ngữ pháp; cơ chế cụ thể chưa được package này xác lập. Chưa xử lý.

### Vừa — M01

**YS-LN02/Text/part0030.xhtml/p000094 — Thu hẹp việc cắt đứt địch thành cắt đường lui.**

“Cắt đứt đường lui” gán riêng hướng rút quân cho hành động mà nguồn chỉ mô tả là cắt đứt/cô lập địch phía bắc. Trong đoạn đang bàn hậu cần, lựa chọn này làm mất độ mở của quan hệ chiến lược. Không đủ căn cứ trong package để khẳng định đó là đường rút lui hoặc riêng đường tiếp tế.

Đề nghị tạm dùng “nhất là sau khi đã cô lập kẻ địch ở phía bắc”. Phương án khác: “cắt đứt liên lạc của kẻ địch ở phía bắc”, nhưng cách này vẫn bổ sung loại liên hệ cụ thể nên kém trung tính hơn. Chưa xử lý.

### Vừa — M02

**YS-LN02/Text/part0030.xhtml/p000097 — Mất nhấn mạnh câu nội tâm.**

XHTML nguồn đánh dấu riêng câu giữa về thói quen ngủ trưa và đuổi về quê. Bản dịch bỏ toàn bộ dấu đánh dấu ở câu này, trái DEC-P01-002 và làm yếu ranh giới giữa lời kể với lời rủa thầm. Đề nghị bọc đúng câu “Nếu có thói quen ngủ trưa thì xéo về quê mà ngủ.” bằng `*...*`; không bọc cả đoạn. Giữ giọng giận dữ và hành động cuối đoạn. Chưa xử lý.

### Vừa — M03

**YS-LN02/Text/part0030.xhtml/p000103 — Tự xác lập cơ quan cấp Cục.**

“Cục Tác chiến” thêm cấp tổ chức chưa được định danh trong package hay canon. Lời thoại chỉ gọi phía/bộ phận tác chiến trình bày trước các chỉ huy và tham mưu. Chọn tạm “bộ phận tác chiến” hoặc “bên tác chiến” để giữ chức năng, không thêm cấp hành chính. Đề nghị “Xin mời bộ phận tác chiến trình bày.” Không suy ra người cụ thể hay cấp bậc. Chưa xử lý.

### Vừa — M04

**YS-LN02/Text/part0030.xhtml/p000123 — Thu hẹp nhóm người không tham chiến thành thường dân.**

Nguồn đặt điều kiện về người không tham chiến, rồi p000125–126 nói riêng về lính địch, thường dân và dân quân. “Thường dân” không giữ nguyên tiêu chí tham chiến, đặc biệt khi đoạn tiếp theo nhắc dân quân. Đây là điều kiện then chốt của lập luận pháp lý trong truyện, cần giữ đúng lớp nghĩa mà không suy diễn quy định pháp luật ngoài đời.

Đề nghị dùng “người không tham chiến” tại đây và p000129; vẫn giữ “thường dân” ở p000126. Phương án “người phi chiến đấu” cũng giữ độ rộng nhưng kém tự nhiên hơn. Chưa xử lý; không cần quyết định canon để sửa nghĩa tại chỗ.

### Nhẹ — L01

**YS-LN02/Text/part0030.xhtml/p000101 — Kết hợp từ gượng.** “Điều chuyển mặt trận” khiến mặt trận thành đối tượng điều động như đơn vị quân. Tạm dùng “dịch chuyển mặt trận” để giữ độ mở, không tự chọn rút quân hay đổi hướng tiến công. Phạm vi chữ nghiêng, mối lo Cộng hòa phản ứng và điều kiện gián đoạn tiếp tế đều được giữ. Chưa xử lý.

### Nhẹ — L02

**YS-LN02/Text/part0030.xhtml/p000104 — Tăng nhẹ mức chắc chắn.** “Sẽ giúp” khẳng định tác dụng mạnh hơn khả năng trợ giúp mà nguồn nêu. Đề nghị “có thể giúp ta xử lý vấn đề”. Không cần đổi chủ thể hay ý về chuẩn bị trước. Chưa xử lý.

### Nhẹ — L03

**YS-LN02/Text/part0030.xhtml/p000121 — Thành ngữ dịch sát gây gượng.** “Chẳng còn lấy một giây để mất” khó hiểu tự nhiên trong tiếng Việt. Đề nghị “chúng ta không thể phí thêm dù chỉ một giây”. Giữ toàn bộ đoạn trong chữ nghiêng và giọng sốt ruột, không tăng thành mệnh lệnh đã nói ra. Chưa xử lý.

### Nhẹ — L04

**YS-LN02/Text/part0030.xhtml/p000126 — Chủ thể câu không tự nhiên.** “Thành phố phần lớn là thường dân” đồng nhất địa điểm với người. Đề nghị “Cư dân thành phố phần lớn là thường dân”. Không đổi chi tiết dân quân xen lẫn hoặc việc đã xác nhận dân cư khi chiếm Arene. Chưa xử lý.

## Bốn lựa chọn pending — đều là đề xuất tạm, không canon

| Mục / ID | Chọn tạm | Phương án khác | Căn cứ và bất định |
| --- | --- | --- | --- |
| Worms Convention — YS-LN02/Text/part0030.xhtml/p000117 | Công ước Worms | Hiệp ước Worms; WTN | Tên đầy đủ hiện diện trực tiếp trong package; “Công ước” giữ loại tên gọi, Worms giữ tên riêng. “Hiệp ước” rộng hơn và phù hợp câu mô tả sau, nhưng không cần thay tên. WTN không có trong package nên không dùng để thay tên tại ID này. Tin cậy cao về cách dịch tại chỗ; không xác lập hiệp ước ngoài đời hoặc lore. |
| Feldgendarmerie — YS-LN02/Text/part0030.xhtml/p000095, YS-LN02/Text/part0030.xhtml/p000097 | Giữ Feldgendarmerie | hiến binh dã chiến | Package xác định liên hệ với quân cảnh nhưng không giải thích đủ cơ cấu, loại đơn vị hay tên riêng. Giữ dạng đã dùng nhất quán tránh gán thêm cơ cấu. “Hiến binh dã chiến” là phương án dịch chức năng có thể cân nhắc sau, chưa được xác nhận chỉ bằng hai ID này. Tin cậy vừa về lựa chọn bảo thủ; mức Việt hóa còn pending. |
| war college — YS-LN02/Text/part0030.xhtml/p000113, YS-LN02/Text/part0030.xhtml/p000114 | Giữ Học viện Quân sự cho lô này | học viện chiến tranh; trường đào tạo sĩ quan cao cấp | Ủy ban nghiên cứu chiến lược hỗ trợ cách gọi học viện có chức năng quân sự. Bản hiện tại nhất quán và không thêm riêng cấp học hay đối tượng đào tạo. “Học viện chiến tranh” literal hơn nhưng chưa cần đổi trong lô; “trường đào tạo sĩ quan cao cấp” thêm thông tin người học chưa được chứng minh. Tin cậy vừa; cách gọi và viết hoa vẫn là đề xuất, không tên chính thức. |
| WTN (term expansion unresolved) — YS-LN02/Text/part0030.xhtml/p000117 | Dùng Công ước Worms ở ID này; để quan hệ WTN ↔ tên đầy đủ chưa xác minh | Giữ WTN nếu một nguồn được giao về sau chỉ có chữ viết tắt | Không có WTN trong text hoặc XHTML của package. Tên đầy đủ đủ căn cứ cho bản dịch tại đây, nhưng không chứng minh nó là khai triển của WTN. Không ghi quan hệ đồng nghĩa/khai triển là đã xác nhận. Tin cậy cao về lựa chọn tại ID, thấp/chưa đủ căn cứ về quan hệ viết tắt. Tiếp tục bằng tên đầy đủ có nguồn; không cần chờ người dùng. |

Đối với WTN, mục ledger là đề xuất cần thẩm định, không phải chứng cứ nguồn. Coordinator có thể ghi lại giới hạn này khi tiếp nhận; reviewer không sửa ledger. Các sửa nghĩa ở p000123/p000129 và cách gọi bộ phận ở p000103 cũng chỉ là lựa chọn phù hợp đoạn, không bổ sung canon.

## Bao phủ từng ID

Mọi ID trong bảng đã được rà cả năm tiêu chí. “Đạt” nghĩa là không phát hiện lỗi có căn cứ cần ghi nhận trong phạm vi package; không phải sign-off cả lô. Các ghi chú pending không tự tính thành lỗi.

| Segment ID | Kết quả / ghi chú trọng tâm |
| --- | --- |
| YS-LN02/Text/part0030.xhtml/p000094 | M01; giữ chi tiết tuyến nhánh, đầu mối đường sắt và phản ứng nhân viên. |
| YS-LN02/Text/part0030.xhtml/p000095 | Đạt; Feldgendarmerie pending, giữ quan hệ lỗi không dập nổi loạn. |
| YS-LN02/Text/part0030.xhtml/p000096 | Đạt; đúng phủ định không chỉ tư lệnh và giọng mỉa mai. |
| YS-LN02/Text/part0030.xhtml/p000097 | M02; giữ lời rủa thầm khác với hành động rên rỉ/nhổ xuống đất. |
| YS-LN02/Text/part0030.xhtml/p000098 | Đạt; giữ giả định trái thực tế trong quá khứ và đại đội pháp sư. |
| YS-LN02/Text/part0030.xhtml/p000099 | Đạt; đúng diễn biến xấu và nỗi lo, không biến nỗi lo thành sự kiện. |
| YS-LN02/Text/part0030.xhtml/p000100 | Đạt; giữ nguyên nhân các đơn vị bị kẹt. |
| YS-LN02/Text/part0030.xhtml/p000101 | L01; nhấn mạnh đúng câu hỏi, giữ logic quân/tiếp tế. |
| YS-LN02/Text/part0030.xhtml/p000102 | Đạt; đúng mục tiêu và việc pháp sư Cộng hòa đã tham gia. |
| YS-LN02/Text/part0030.xhtml/p000103 | M03; giữ lời mời trình bày, bỏ cấp tổ chức suy diễn. |
| YS-LN02/Text/part0030.xhtml/p000104 | L02; tổng hợp phân tích và vai trò kế hoạch vẫn rõ. |
| YS-LN02/Text/part0030.xhtml/p000105 | Đạt; giữ mục tiêu hạn chế, góc nhìn quân sự và nghiên cứu chiến lược. |
| YS-LN02/Text/part0030.xhtml/p000106 | Đạt; đúng câu hỏi khả năng sử dụng. |
| YS-LN02/Text/part0030.xhtml/p000107 | Đạt; đúng vấn đề duy nhất. |
| YS-LN02/Text/part0030.xhtml/p000108 | Đạt; giữ bác kế hoạch nửa vời và điều kiện giải quyết trong một lần. |
| YS-LN02/Text/part0030.xhtml/p000109 | Đạt; vẫn là đánh giá của tư lệnh, không khẳng định thất bại. |
| YS-LN02/Text/part0030.xhtml/p000110 | Đạt; giữ độ chắc chắn kết quả và sự ngập ngừng. |
| YS-LN02/Text/part0030.xhtml/p000111 | Đạt; đúng phạm vi chữ nghiêng và việc tự kìm không quát. |
| YS-LN02/Text/part0030.xhtml/p000112 | Đạt; lời thoại thúc giục giữ đúng đối tượng. |
| YS-LN02/Text/part0030.xhtml/p000113 | Đạt; học viện pending; giữ pháp sư trong nhóm mục tiêu, thời gian cực ngắn. |
| YS-LN02/Text/part0030.xhtml/p000114 | Đạt; giữ điểm nhìn hoài nghi và các điều kiện suy luận. |
| YS-LN02/Text/part0030.xhtml/p000115 | Đạt trong phạm vi này; không đủ căn cứ tự quy đổi cấp tổ chức của các lực lượng nhận kế hoạch. |
| YS-LN02/Text/part0030.xhtml/p000116 | Đạt; chữ nghiêng toàn câu đúng, vẫn là câu hỏi nội tâm. |
| YS-LN02/Text/part0030.xhtml/p000117 | Đạt; giữ “có lẽ” và câu hỏi vi phạm; hai mục tên/WTN pending đã đánh giá riêng. |
| YS-LN02/Text/part0030.xhtml/p000118 | Đạt; giữ giả định về khí độc/pháo và mức “có lẽ” của kế hoạch phòng thủ. |
| YS-LN02/Text/part0030.xhtml/p000119 | Đạt; nhận định pháp lý vẫn do chuyên gia trong truyện đưa ra. |
| YS-LN02/Text/part0030.xhtml/p000120 | Đạt; phản ứng và câu hỏi đúng. |
| YS-LN02/Text/part0030.xhtml/p000121 | L03; phạm vi chữ nghiêng và chủ thể “chúng ta” đúng. |
| YS-LN02/Text/part0030.xhtml/p000122 | Đạt; giữ bực tức, đập bàn và thúc giục bằng ánh mắt. |
| YS-LN02/Text/part0030.xhtml/p000123 | M04; giả định vẫn là giả định, cần sửa nhóm người bị phủ định. |
| YS-LN02/Text/part0030.xhtml/p000124 | Đạt; giữ phản đối giả định khó tin bằng câu hỏi. |
| YS-LN02/Text/part0030.xhtml/p000125 | Đạt; giữ “suýt” và sự phân biệt lính địch/cư dân thành phố. |
| YS-LN02/Text/part0030.xhtml/p000126 | L04; giữ thường dân khác dân quân và căn cứ đã xác nhận. |
| YS-LN02/Text/part0030.xhtml/p000127 | Đạt; thủ tục pháp lý là phương tiện tạo điều kiện, chưa giải thích cơ chế. |
| YS-LN02/Text/part0030.xhtml/p000128 | Đạt; cả hai che cảm xúc bằng giọng đều đều. |
| YS-LN02/Text/part0030.xhtml/p000129 | S01; áp dụng cách gọi người không tham chiến theo M04. |
| YS-LN02/Text/part0030.xhtml/p000130 | Đạt; giữ câu hỏi suy ra giết tất cả, không biến thành mệnh lệnh. |
| YS-LN02/Text/part0030.xhtml/p000131 | Đạt; giữ nhận thức tập thể, thảm sát đội lốt chiến đấu và điều kiện cuối. Cụm đánh giá pháp lý trong nguồn còn trừu tượng; không suy diễn thêm cơ chế hay kết luận pháp luật. |

## Tổng số và bàn giao

- Findings: nghiêm trọng 1, vừa 4, nhẹ 4; tổng 9.
- Chưa xử lý: nghiêm trọng 1, vừa 4, nhẹ 4. Lô chưa đủ điều kiện sign-off; lỗi nghiêm trọng là hard stop trước bước nâng bản chuẩn.
- Bốn mục pending đều có lựa chọn tạm, phương án thay thế và độ bất định; không mục nào được nâng thành canon. Quan hệ khai triển WTN vẫn chưa có chứng cứ, nhưng không cản dùng tên đầy đủ có trong nguồn tại p000117.
- Người giữ quyền sửa xử lý S01, M01–M04 và cân nhắc L01–L04; sau đó review lại các ID sửa. Không yêu cầu người dùng quyết định thuật ngữ thông thường.
- Chỉ ghi `reviews/prose/vol-02/ch-06-b04-codex.md`. `validator: not_run`; `diff_check: not_run`; `commit: null`.
