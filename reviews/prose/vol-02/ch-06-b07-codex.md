# Review vol-02-ch-06-b07

- Task: `vol-02-ch-06-b07-review`; reviewer: Codex.
- Đã đọc agents/shared.md, agents/reviewer.md, config/translation-pipeline.yml, hai handoff b07/review, bản dịch, self-check, năm tài liệu canon được dẫn và riêng mục chapter6_b07_translation_proposals trong ledger.
- Chỉ đối chiếu gói cục bộ `work/vol-02/batches/ch-06-b07-source.jsonl`. SHA-256 thực tế khớp handoff: `f6e79df03b5320539229b74f06977d3069c11389c46d192ee3f688dd0ea1ff27`. Hash cả năm tài liệu canon cũng khớp handoff.
- Nguồn và bản dịch đều đủ 30 đơn vị, cùng ID và thứ tự p000194–p000223. Không mở EPUB/PDF hay gói khác. Không sửa đầu vào, ledger hoặc canon; không commit.
- Kết quả: **0 serious, 5 moderate, 3 minor**, tất cả còn chưa xử lý tại thời điểm review. Review hoàn tất; bản dịch cần sửa trước khi signoff. Validator/diff_check: not_run.

## Findings có thể hành động

### B07-R01 — moderate — mức chắc chắn

- ID: `YS-LN02/Text/part0030.xhtml/p000205`.
- Vấn đề: “phải tính đến khả năng” chỉ yêu cầu xét một khả thể; nguồn yêu cầu lấy việc còn đủ người duy trì thành phố làm giả định khi lập phương án. Bản dịch làm yếu tiền đề của lập luận tác chiến.
- Đề xuất: dùng “phải giả định rằng vẫn còn đủ người ở lại để duy trì hoạt động của thành phố”. Đồng thời “có vị trí như đầu mối giao thông” nên thành “đóng vai trò đầu mối giao thông” để giữ chức năng thực tế, tránh sắc thái so sánh.
- Căn cứ: nguồn tại ID này và quy tắc giữ mức độ chắc chắn trong style-guide. Độ tin cậy: cao.

### B07-R02 — moderate — mất cơ chế ép khuất phục

- IDs: `YS-LN02/Text/part0030.xhtml/p000212`, `YS-LN02/Text/part0030.xhtml/p000215`.
- Vấn đề: “cắt nguồn tiếp tế”/“thiếu tiếp tế” diễn đạt cơ chế bao vây chung, làm mờ chi tiết ép đối phương chịu đói đến khi khuất phục. Chi tiết này có ý nghĩa trong chính cuộc tranh luận về người không tham chiến; không nên làm nhẹ bằng cách chỉ nêu hậu cần.
- Đề xuất: p000212 dùng “bao vây, buộc họ chịu đói đến khi khuất phục”; p000215 nhắc lại nhất quán “bao vây và buộc họ khuất phục vì đói”. Giữ đại từ đối phương mở, không tự xác định ai trong thành phố chịu đói.
- Căn cứ: hai đoạn cùng nhắc một phương án, sau đó đánh giá khó khăn duy trì vòng vây. Độ tin cậy: cao về chi tiết đói; trung bình về phạm vi đại từ đối phương.

### B07-R03 — moderate — đại từ trần thuật Tanya

- IDs: `YS-LN02/Text/part0030.xhtml/p000214`, `YS-LN02/Text/part0030.xhtml/p000215`, `YS-LN02/Text/part0030.xhtml/p000217`.
- Vấn đề: các chỗ trần thuật dùng “cô” thay cho quy ước “nó” trong DEC-P01-001. Chủ thể p000214–p000215 có căn cứ liên tục: lời đề xuất p000212 được giải thích rồi nhắc lại; p000217 trực tiếp gắn chủ thể với Tanya.
- Đề xuất tạm có căn cứ tốt nhất: đọc chủ thể p000214–p000215 là Tanya, áp dụng “nó” nhất quán tại ba ID. Không đổi đại từ trong câu thoại thành “nó”.
- Phương án thay thế nếu muốn giảm độ suy luận ở p000214–p000215: lặp “Tanya”; tránh bỏ hẳn chủ thể hoặc gán lời cho người giảng bài. Độ bất định: thấp ở p000217, thấp–trung bình ở p000214–p000215 do gói chỉ có ngữ cảnh cục bộ. Đây là áp dụng quyết định hiện có, không xác lập quan hệ nhân vật mới.

### B07-R04 — moderate — thêm loại hình lực lượng

- ID: `YS-LN02/Text/part0030.xhtml/p000222`.
- Vấn đề: “lực lượng dự bị” gán tư cách quân sự cụ thể cho lực lượng dư ra/khả dụng; nguồn không xác định đây là quân dự bị. Điều này có thể khiến người đọc hiểu sai cơ cấu quân đang bị ghìm chân.
- Đề xuất: “phần lớn lực lượng dư ra” hoặc “phần lớn lực lượng có thể dành cho các chiến trường khác”; ưu tiên phương án đầu vì ít diễn giải hơn.
- Căn cứ: lập luận về quân lực bị giữ ở bắc/tây và thiếu khả năng dốc sức cho chiến tranh lớn. Độ tin cậy: cao về việc không đủ căn cứ cho “dự bị”; trung bình về cách diễn đạt Việt tự nhiên nhất.

### B07-R05 — moderate — phạm vi nhấn mạnh

- ID: `YS-LN02/Text/part0030.xhtml/p000222`.
- Vấn đề: nguồn nhấn mạnh yếu tố chỉ tình cảnh hiện tại; bản dịch chuyển nhấn mạnh sang “vẫn”, tức tính tiếp diễn. Có dấu Markdown chưa đồng nghĩa với giữ đúng phạm vi nhấn mạnh theo DEC-P01-002.
- Đề xuất: giữ câu nhưng chuyển dấu nhấn sang yếu tố chỉ tình cảnh, ví dụ “vậy mà vẫn lâm vào *tình cảnh này*”. Không in nghiêng toàn câu.
- Căn cứ: cấu trúc em trong XHTML gói đã xác minh. Độ tin cậy: cao.

### B07-R06 — minor — ghi chú văn phong p000214

- ID: `YS-LN02/Text/part0030.xhtml/p000214`.
- Đánh giá ghi chú translator: tự kiểm đúng khi yêu cầu rà lại văn phong. Lời phản đối gián tiếp và phần nhấn mạnh được giữ; việc dồn sức ép chính trị vào câu giữa vẫn giữ quan hệ nguyên nhân. Tuy nhiên, “đủ hiểu ... để nguyền rủa” gượng, giảm cường độ nguyền rủa; “Đó là tất cả những gì có thể làm” làm nhạt việc chỉ còn có thể kêu ca/phản đối như vậy.
- Đề xuất: chỉnh cụm đầu theo hướng “hiểu quá rõ tầm quan trọng chiến lược của yêu cầu ấy, đến mức chỉ muốn nguyền rủa”; câu cuối nêu rõ “Dưới sức ép chính trị, họ chỉ có thể kêu ca như vậy.” Cân nhắc “nguyền rủa xuống địa ngục” nếu cần giữ hình ảnh mạnh hơn; phương án này sát hình ảnh nhưng kém tự nhiên hơn trong tiếng Việt. Không biến lời gián tiếp thành lời phản đối đã được nói thẳng.
- Độ bất định: trung bình về mức khẩu ngữ của lời nguyền; thấp về việc nên giữ sắc thái kêu ca. Sửa đại từ theo R03. Không cần quyết định canon mới.

### B07-R07 — minor — đối tượng hành động chưa rõ

- ID: `YS-LN02/Text/part0030.xhtml/p000211`.
- Vấn đề: “giữ chân họ” có thể hiểu là ghìm quân đối phương, trong khi đoạn đang nói trì hoãn việc các cường quốc can thiệp. Ngữ cảnh p000210 giúp suy ra nhưng câu riêng chưa rõ.
- Đề xuất: “Vậy nên ta nên cố trì hoãn việc họ can thiệp thêm một thời gian nữa.” “Nên” cũng giữ mức khuyến nghị tốt hơn “phải”.
- Độ tin cậy: cao.

### B07-R08 — minor — phạm vi vật tư

- ID: `YS-LN02/Text/part0030.xhtml/p000223`.
- Vấn đề: “khí tài” dễ chỉ trang bị kỹ thuật/vũ khí, hẹp hơn vật tư quân sự nói chung trong đoạn bàn nền công nghiệp và nguồn cung. Các hình ảnh tuyến tiếp tế kêu gào, nhân viên hậu cần cuống cuồng đã được giữ tốt.
- Đề xuất: cân nhắc “vật tư quân sự” thay cho “khí tài”; giữ nguyên thực phẩm và vật tư tiêu hao ở vế sau.
- Độ bất định: trung bình do cách dùng “khí tài” có thể rộng tùy văn phong; không coi đây là lỗi cốt truyện.

## Hai thuật ngữ pending

| Thuật ngữ | IDs | Lựa chọn tạm | Phương án thay thế và lý do | Độ bất định |
| --- | --- | --- | --- | --- |
| law of war | `YS-LN02/Text/part0030.xhtml/p000208` | **luật chiến tranh** | “luật về chiến tranh” dễ hiểu nhưng dài hơn và không thêm độ chính xác; “luật nhân đạo quốc tế” áp khung pháp lý chuyên biệt chưa được gói xác lập nên không chọn. Giữ cách literal có sẵn trong đề xuất b07. | Thấp về nghĩa tại đoạn; trung bình về tên lĩnh vực pháp lý dùng thống nhất lâu dài. |
| noncombatants | `YS-LN02/Text/part0030.xhtml/p000208`, `YS-LN02/Text/part0030.xhtml/p000212` | **người không tham chiến** | “người không trực tiếp tham chiến” bổ sung tiêu chí chưa được nguồn nói rõ; “dân thường” tự thu hẹp nhóm và xóa phân biệt với cách gọi thường dân ở p000205, p000220–p000222. Giữ tiêu chí tham chiến là phương án ít suy diễn nhất. | Thấp về cách dịch tại lô; trung bình về thành phần cụ thể của nhóm. |

Cả hai lựa chọn đều là **provisional/pending, không phải canon**. Không phát hiện quyết định thuật ngữ cần người dùng chốt để tiếp tục. Việc tồn tại điều khoản chế tài chỉ là thông tin chưa xác thực trong điểm nhìn nhân vật, không phải khẳng định về luật ngoài đời; bản dịch đã giữ điểm này. Không tra cứu ngoài gói. Riêng “ngành Hậu cần” tại p000215 có thể giữ tạm vì không gán cấp cục/bộ; cấp tổ chức vẫn chưa xác lập.

## Đối chiếu đủ 30 ID

Mỗi hàng đã được rà nghĩa, điểm nhìn, mức chắc chắn, văn phong, thuật ngữ và nhấn mạnh; “đạt” chỉ nghĩa là chưa thấy lỗi có căn cứ trong gói này.

| Stable ID | Kết quả |
| --- | --- |
| YS-LN02/Text/part0030.xhtml/p000194 | Đạt; quan hệ thời gian và mức xấu đi giữ đúng. |
| YS-LN02/Text/part0030.xhtml/p000195 | Đạt; ước lượng pháp sư và quan hệ với chiến thuật tiên phong được giữ. |
| YS-LN02/Text/part0030.xhtml/p000196 | Đạt; lời triệu tập, tên và cấp bậc không thêm quan hệ mới. |
| YS-LN02/Text/part0030.xhtml/p000197 | Đạt; giữ câu chuyển đoạn ngắn. |
| YS-LN02/Text/part0030.xhtml/p000198 | Đạt; không có quyết định dứt khoát. |
| YS-LN02/Text/part0030.xhtml/p000199 | Đạt; ý tính toán sai lầm giữ đúng, có thể làm mượt sau. |
| YS-LN02/Text/part0030.xhtml/p000200 | Đạt; xác suất giao chiến tăng rất cao, vẫn là dự báo. |
| YS-LN02/Text/part0030.xhtml/p000201 | Đạt theo ngữ cảnh p000202; Đế quốc dần phục hồi thế trận. |
| YS-LN02/Text/part0030.xhtml/p000202 | Đạt; đối lập tiến chậm và bước chuyển lớn được giữ. |
| YS-LN02/Text/part0030.xhtml/p000203 | Đạt; điểm nhìn Tanya, tính khả thi và phạm vi nhấn mạnh đúng. |
| YS-LN02/Text/part0030.xhtml/p000204 | Đạt; dự báo chiến tranh đô thị. |
| YS-LN02/Text/part0030.xhtml/p000205 | R01 moderate. |
| YS-LN02/Text/part0030.xhtml/p000206 | Đạt; nhiệm vụ do Bộ Tổng tham mưu giao; tên gọi tạm. |
| YS-LN02/Text/part0030.xhtml/p000207 | Đạt; dự đoán Tanya và loại nhiệm vụ đúng. |
| YS-LN02/Text/part0030.xhtml/p000208 | Đạt với hai đề xuất thuật ngữ; giữ lời truyền chưa xác thực và điều kiện cố ý. |
| YS-LN02/Text/part0030.xhtml/p000209 | Đạt; quyền viện dẫn từng nước và lý do yêu cầu giữ đúng. |
| YS-LN02/Text/part0030.xhtml/p000210 | Đạt; chỉ câu giờ, vẫn có lý do địa chính trị để can thiệp. |
| YS-LN02/Text/part0030.xhtml/p000211 | R07 minor. |
| YS-LN02/Text/part0030.xhtml/p000212 | R02 moderate; điều kiện và tính duy nhất của phương án được giữ. |
| YS-LN02/Text/part0030.xhtml/p000213 | Đạt; nhận thức chung về yêu cầu phi thực tế. |
| YS-LN02/Text/part0030.xhtml/p000214 | R03 moderate; R06 minor; phần em đúng. |
| YS-LN02/Text/part0030.xhtml/p000215 | R02, R03 moderate; tỷ lệ ba lần và khó duy trì vòng vây đúng. |
| YS-LN02/Text/part0030.xhtml/p000216 | Đạt; giữ phòng thủ đến khi đối phương không chịu nổi. |
| YS-LN02/Text/part0030.xhtml/p000217 | R03 moderate; hai vị trí em đúng, không tự in nghiêng phần kể. |
| YS-LN02/Text/part0030.xhtml/p000218 | Đạt; không tự làm rõ hành động được nhắc lại khi nguồn để mở. |
| YS-LN02/Text/part0030.xhtml/p000219 | Đạt; ưu thế và hệ quả ghìm quân giữ đúng, hướng bắc phù hợp p000222. |
| YS-LN02/Text/part0030.xhtml/p000220 | Đạt; giữ điểm nhìn Tanya và đối chiếu Quân đội Mỹ, không tự xác lập lore. |
| YS-LN02/Text/part0030.xhtml/p000221 | Đạt; tính không còn lựa chọn được giữ. |
| YS-LN02/Text/part0030.xhtml/p000222 | R04, R05 moderate; còn lại giữ áp lực tiếp tế, điều kiện dốc toàn lực và nhận định của Tanya. “Mình” trong câu nói về ưu thế quốc gia có thể hiểu là tự quy chiếu tập thể, không kết luận là Tanya có quân lực/dân số riêng. |
| YS-LN02/Text/part0030.xhtml/p000223 | R08 minor; áp lực hậu cần và nguy cơ thiếu vật tư giữ đúng. |

## Bàn giao kết quả

- Unresolved serious: **0**; unresolved moderate: **5**; unresolved minor: **3**. Đếm theo finding R01–R08, không đếm lặp mỗi ID bị ảnh hưởng.
- Người giữ quyền sửa translations/ xử lý R01–R05 trước signoff, cân nhắc R06–R08; coordinator ghi lựa chọn thuật ngữ vào ledger/handoff theo quyền của mình.
- Rủi ro còn lại: giới hạn ngữ cảnh cục bộ khi nhận diện chủ thể p000214–p000215; thuật ngữ và cấp tổ chức chưa canon. Các điểm này đã có phương án tạm để tiếp tục, không yêu cầu chờ người dùng.
