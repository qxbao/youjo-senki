# Review prose/meaning — vol-02-ch-06-b08

```yaml
role: reviewer
task_id: vol-02-ch-06-b08-review
state: done
review_path: reviews/prose/vol-02/ch-06-b08-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b08-codex.md
coverage:
  start: YS-LN02/Text/part0030.xhtml/p000224
  end: YS-LN02/Text/part0030.xhtml/p000256
  assessed: 33
  missing: 0
  duplicate: 0
source_package_sha256: 6e96135ab00ea6d1f8262ab5a89b7e4365ac618fb8e32f21112226ad7b7e68dd
source_package_hash: pass
canon_reference_hashes: pass_all_five
counts:
  serious: 0
  moderate: 6
  minor: 2
count_method: Mỗi finding tính một lần; các vấn đề cùng mức tại cùng ID được gộp.
unresolved_findings: [B08-M01, B08-M02, B08-M03, B08-M04, B08-M05, B08-M06, B08-L01, B08-L02]
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_handoff_to_translator_for_fixes_then_recheck
```

Đã đọc `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, hai handoff b08, package được giao, bản dịch, self-check, năm tham chiếu canon và đề xuất b08 trong ledger. Hash package và cả năm hash canon đều khớp handoff. Đối chiếu từng ID, văn bản và XHTML trong đúng package; không mở EPUB/PDF hoặc package khác. Chỉ ghi báo cáo này; không sửa bản dịch, self-check, ledger hay canon.

Canon được đối chiếu: `canon/glossary.yml`, `canon/style-guide.md`, `canon/characters.yml`, `canon/decisions.md`, `canon/glossary-pending.yml`. Glossary và characters chính thức còn rỗng. DEC-P01-002 quy định giữ đúng phạm vi nhấn mạnh. DEC-P01-001 phân biệt nội tâm/trần thuật nhưng giới hạn theo giai đoạn; không mặc nhiên nâng quy ước đại từ pilot thành quy tắc cho mọi giai đoạn của tập 2.

## Findings cần xử lý

### B08-M01 — moderate — YS-LN02/Text/part0030.xhtml/p000232

- **Vấn đề:** Mất nhấn mạnh ở từ chỉ toàn bộ mọi người. Self-check kết luận package không có nhấn mạnh là sai.
- **Căn cứ:** XHTML tại ID này có một thẻ `em`, giới hạn vào lượng từ chỉ mọi người; DEC-P01-002 yêu cầu giữ phạm vi tương ứng.
- **Sửa:** Đánh dấu `*ai cũng*` trong câu cuối, không nghiêng cả câu hoặc cả đoạn. Coordinator giao translator sửa nhận định về nhấn mạnh trong self-check.

### B08-M02 — moderate — YS-LN02/Text/part0030.xhtml/p000238

- **Vấn đề:** Mất nhấn mạnh ở trọng tâm hỏi cách tiến hành trận đánh.
- **Căn cứ:** XHTML nhấn riêng từ nghi vấn về cách thức, phân biệt với việc có giao chiến hay không.
- **Sửa:** Dùng `*như thế nào*` ở cuối câu hỏi; không đánh dấu toàn bộ câu hỏi. Ý nghĩa và mức dè dặt của phần đầu có thể giữ.

### B08-M03 — moderate — YS-LN02/Text/part0030.xhtml/p000242

- **Vấn đề:** Mất hai vùng nhấn mạnh độc lập, làm mờ chuyển tiếp từ lời kể sang nội tâm trực tiếp. Vùng nhận ra khả năng san phẳng phố còn thiếu liên từ chuyển hướng ở đầu ý nghĩ.
- **Căn cứ:** XHTML có hai thẻ `em`: toàn bộ ý nghĩ giả định về Warsaw, và toàn bộ ý nghĩ cuối về chiến tranh tổng lực. Ý nghĩ thứ nhất đối lập với sự từ chối thực hiện vừa nêu.
- **Sửa:** Khôi phục hai vùng Markdown riêng: từ `Nhưng nếu...` đến `...dễ như trở bàn tay.`, và từ `Bước vào...` đến `...một khả năng.` Giữ lời kể về Tanya và việc bắt đầu tính toán ngoài hai vùng. Thêm `Nhưng` trước giả định để giữ bước tự phản biện. Giữ giả định ở mức khả thể, không biến việc tàn phá thành sự kiện đã xảy ra ở hiện tại.
- **Đại từ tạm:** Ở lời tự quy chiếu về Iraq/Afghanistan, đề xuất `mình` thay `tôi`, theo phân biệt nội tâm mà handoff dẫn DEC-P01-001. Đây là đề xuất áp dụng tại ID, không mở rộng canon theo giai đoạn. Không thêm chữ nghiêng cho phần này vì nguồn không đánh dấu nó.

### B08-M04 — moderate — YS-LN02/Text/part0030.xhtml/p000245

- **Vấn đề:** `vị thống soái của nền văn minh` thêm hình tượng chỉ huy quân sự và nhân cách hóa mạnh hơn căn cứ tại chỗ. Cụm kết `cơ hội ... quả thật rất vui` cũng gượng về chủ thể cảm nhận.
- **Căn cứ:** Đoạn nói về niềm vui học luật và vai trò của luật đối với văn minh, không chỉ ra chức năng chỉ huy quân sự. Style guide cấm thêm sắc thái hoặc giải thích không có căn cứ.
- **Sửa tạm:** Dùng cụm đồng vị `thứ chi phối nền văn minh`; diễn đạt kết câu theo hướng `được học luật ... quả thật là một niềm vui`. Không biến phép ví von thành lời giải thích dài.
- **Đại từ tạm:** Hai chỗ `tôi` trong hồi tưởng học tập là nội tâm tự quy chiếu của cùng người vừa được xác định qua p242–p246; đề xuất `mình`, với giới hạn áp dụng như B08-M03.
- **Lựa chọn khác và bất định:** Xem T01 dưới đây. Không kết luận nghĩa ví von này đã được canon hóa.

### B08-M05 — moderate — YS-LN02/Text/part0030.xhtml/p000249

- **Vấn đề:** Trong ví dụ quốc đảo, bản dịch bỏ đối tượng được trang bị vũ khí. Câu hiện tại chỉ nói quốc gia trang bị vũ khí, làm yếu nghịch lý tuy phủ nhận quân đội nhưng vẫn trang bị chính quân đội ấy.
- **Căn cứ:** Quan hệ đại từ trong package gắn việc trang bị với quân đội vừa được phủ nhận; đây là chi tiết phục vụ ví dụ về phạm vi diễn giải luật.
- **Sửa:** Nêu rõ `nhưng lại trang bị cho quân đội ấy đủ loại vũ khí...`. Giữ quốc đảo ở dạng không nêu tên như nguồn; không tự thêm tên quốc gia, lực lượng hay điều khoản ngoài đời.

### B08-M06 — moderate — YS-LN02/Text/part0030.xhtml/p000256

- **Vấn đề:** `hầm trú ẩn` thu hẹp nơi trú ẩn thành cấu trúc hầm, trong khi package không xác định loại công trình.
- **Căn cứ:** Từ chỉ nơi trú ẩn tại ID này không tự xác nhận vị trí ngầm; không có chi tiết bổ sung trong package b08 cho phép thu hẹp.
- **Sửa:** Dùng `những người trong các nơi trú ẩn` hoặc `những người ở các chỗ trú ẩn`. Giữ riêng nhóm người sơ tán, điều kiện không đưa họ đi rồi rút lui, và kết luận chỉ là cách diễn giải khả dĩ về thường dân.

### B08-L01 — minor — YS-LN02/Text/part0030.xhtml/p000236

- **Vấn đề:** `có chút học vấn trí thức` là kết hợp từ gượng, đồng thời dễ khiến sắc thái dè dặt về phẩm chất nền giáo dục thành nhận xét đơn thuần về lượng học vấn ít ỏi.
- **Căn cứ:** Đoạn tiếp tục lập luận về trách nhiệm xem xét mọi khả năng của người được đào tạo trí thức; có sắc thái hạ nhẹ giá trị của nền đào tạo đó.
- **Sửa tạm:** `Với một người đã được đào tạo ít nhiều theo kiểu trí thức, đó sẽ là sai lầm không thể tha thứ.` Có thể chọn `được coi là đã qua đào tạo trí thức` nếu muốn giữ sắc thái hoài nghi rõ hơn. Không thêm đánh giá đạo đức về nhân vật.

### B08-L02 — minor — YS-LN02/Text/part0030.xhtml/p000249

- **Vấn đề:** `thị trường lý tính` và `kẻ cơ hội pháp lý` nặng cấu trúc dịch sát; `đám khốn kiếp` đẩy giọng chê bai lên mức chửi mạnh.
- **Căn cứ:** Mạch nội tâm châm biếm việc lợi dụng khoảng diễn giải luật để kiếm lợi; không đủ căn cứ coi cụm về thị trường là tên một mô hình kinh tế chuyên biệt.
- **Sửa tạm:** Dùng T02 cho thị trường; thay `kẻ cơ hội pháp lý` bằng `những kẻ lợi dụng luật pháp để kiếm lợi`. Cân nhắc `đám đáng ghét` thay `đám khốn kiếp` để giữ giọng khinh ghét mà giảm mức tục. Không làm sạch hoàn toàn thái độ châm biếm.

## Đề xuất tạm về thuật ngữ và giọng kể

| Mã | ID | Lựa chọn tạm tốt nhất | Lựa chọn khác | Lý do / bất định |
|---|---|---|---|---|
| T01 | YS-LN02/Text/part0030.xhtml/p000245 | `thứ chi phối nền văn minh` | `thước đo của nền văn minh`; `kẻ cai quản nền văn minh` | Cụm ngắn nhận diện: `ruler`. Ngữ cảnh vai trò của luật và mạch diễn giải sau đó nghiêng về sự chi phối. Phương án chọn giảm phần nghĩa quân sự mà `thống soái` tự thêm. Nghĩa công cụ đo vẫn là khả năng khác của từ, nhưng package không có hình ảnh đo lường hỗ trợ; phương án cai quản nhân cách hóa mạnh hơn. Độ tin cậy trung bình; không tuyên bố đã giải quyết dứt điểm phép ví von. |
| T02 | YS-LN02/Text/part0030.xhtml/p000249 | `thị trường vận hành hợp lý` | `thị trường lý tính`; `thị trường vận hành theo lý trí` | Cụm nhận diện: `rational marketplace`. Đã xét đề xuất ledger `thị trường lý tính` và phương án `thị trường hợp lý`, cùng phương án trong self-check. Thêm `vận hành` giúp tính chất hợp lý gắn với hoạt động thị trường, tự nhiên hơn mô tả thị trường như một thực thể có lý trí. Không thêm nghĩa cạnh tranh hoàn hảo, thị trường hiệu quả hay học thuyết cụ thể. Độ tin cậy trung bình; đây là lựa chọn diễn đạt tại đoạn, chưa phải thuật ngữ chuyên ngành đã chốt. |
| T03 | YS-LN02/Text/part0030.xhtml/p000242; YS-LN02/Text/part0030.xhtml/p000245 | `mình` trong nội tâm tự quy chiếu | Giữ `tôi` nếu coordinator có quy ước giai đoạn hiện tại được chứng minh | Handoff dẫn DEC-P01-001 và hai đoạn đủ căn cứ nhận diện người nghĩ là Tanya. Chọn tạm `mình` theo phân biệt điểm nhìn đó. Không coi canon pilot tự động áp dụng toàn bộ tập 2. Với lời kể tại p225, p232, p238, p242, p246, giữ `cô` như bản hiện tại; nếu cần tránh lựa chọn đại từ chưa chốt, dùng `Tanya` tại chỗ. Không tự đổi đồng loạt thành `nó` khi thiếu căn cứ về phạm vi giai đoạn. |

T01–T03 đều là **proposed**, không phải canon. Reviewer đã chọn phương án tạm để translator tiếp tục, không cần chờ người dùng cho các lựa chọn thông thường. Coordinator ghi đề xuất và độ bất định vào ledger/handoff trong lượt của mình; reviewer không sửa các tệp đó.

## Đối chiếu đủ 33 ID

Mỗi dòng dưới là một ID đã xét nghĩa, văn phong, điểm nhìn, sắc thái, thuật ngữ và dấu nhấn trong XHTML. “Giữ” nghĩa là không thấy lỗi cần sửa trên căn cứ package này, không phải duyệt canon.

| Segment ID | Kết quả |
|---|---|
| YS-LN02/Text/part0030.xhtml/p000224 | Giữ; câu hỏi về sự cần thiết và thái độ dè dặt còn nguyên. |
| YS-LN02/Text/part0030.xhtml/p000225 | Giữ; ngắt lời, tự ý thức và giọng cố ý đều được bảo toàn; đại từ trần thuật xem T03. |
| YS-LN02/Text/part0030.xhtml/p000226 | Giữ; phân biệt phản ứng thông thường với dự đoán của Tanya. |
| YS-LN02/Text/part0030.xhtml/p000227 | Giữ; yêu cầu giải thích rõ vẫn còn, không đổi thành hành động khác. |
| YS-LN02/Text/part0030.xhtml/p000228 | Giữ; chiến thuật chậm rãi và mốc thời kỳ còn nguyên. |
| YS-LN02/Text/part0030.xhtml/p000229 | Giữ; hai ví dụ lịch sử và chi tiết chưa có đường sắt còn nguyên. |
| YS-LN02/Text/part0030.xhtml/p000230 | Giữ; lời khuyên không đánh vẫn là hệ quả có điều kiện. |
| YS-LN02/Text/part0030.xhtml/p000231 | Giữ; lời thoại bỏ lửng. |
| YS-LN02/Text/part0030.xhtml/p000232 | B08-M01; nội dung ít phương án thực tế đúng, thiếu nhấn mạnh. |
| YS-LN02/Text/part0030.xhtml/p000233 | Giữ; phủ định mục đích cuộc thảo luận đúng. |
| YS-LN02/Text/part0030.xhtml/p000234 | Giữ; điều kiện và đề xuất tìm kẽ hở đúng. |
| YS-LN02/Text/part0030.xhtml/p000235 | Giữ; gác khả thi riêng với nghĩa vụ xét mọi khả năng. |
| YS-LN02/Text/part0030.xhtml/p000236 | B08-L01; cần làm tự nhiên cụm học vấn và giữ sắc thái dè dặt. |
| YS-LN02/Text/part0030.xhtml/p000237 | Giữ; mức tin chắc, nhượng bộ và đề nghị đổi cách tiếp cận đúng. |
| YS-LN02/Text/part0030.xhtml/p000238 | B08-M02; trọng tâm cách tiến hành thiếu nhấn mạnh. |
| YS-LN02/Text/part0030.xhtml/p000239 | Giữ; câu hỏi đề nghị tìm cách giao chiến hợp pháp phù hợp mạch diễn giải. |
| YS-LN02/Text/part0030.xhtml/p000240 | Giữ; câu hỏi nội tâm, luật chơi và ví dụ thương lượng còn nguyên. |
| YS-LN02/Text/part0030.xhtml/p000241 | Giữ; đảo thế thương lượng và phủ định khả năng thắng đúng. |
| YS-LN02/Text/part0030.xhtml/p000242 | B08-M03, T03; giả định và mức khả thể đúng, thiếu dấu nhấn và liên từ chuyển hướng. |
| YS-LN02/Text/part0030.xhtml/p000243 | Giữ tạm `luật chiến tranh`; cách sắp từ bất thường ở nguồn được đọc theo hỏi môn học và p244–p245, không tự biến thành học thuyết mới. |
| YS-LN02/Text/part0030.xhtml/p000244 | Giữ; học xong môn và thái độ hứng thú đúng. |
| YS-LN02/Text/part0030.xhtml/p000245 | B08-M04, T01, T03; các môn và hồi tưởng thời sinh viên còn nguyên, ví von và kết câu cần sửa. |
| YS-LN02/Text/part0030.xhtml/p000246 | Giữ; tự tin về căn cứ pháp lý vẫn là nhận định gắn với ý tưởng của Tanya. |
| YS-LN02/Text/part0030.xhtml/p000247 | Giữ; câu hỏi về kinh nghiệm làm căn cứ. |
| YS-LN02/Text/part0030.xhtml/p000248 | Giữ tạm `thưa giảng viên`; không tự gán quân hàm hoặc quan hệ thân thuộc. |
| YS-LN02/Text/part0030.xhtml/p000249 | B08-M05, B08-L02, T02; logic diễn giải còn nguyên, cần khôi phục đối tượng trang bị và chỉnh cụm diễn đạt. |
| YS-LN02/Text/part0030.xhtml/p000250 | Giữ; lặp ý nghiêm túc phục vụ giọng tự biện hộ, không nên tự xóa. |
| YS-LN02/Text/part0030.xhtml/p000251 | Giữ; khác biệt luật trong nước/quốc tế và hình ảnh xám/trắng còn nguyên; không thay bằng diễn giải đạo đức. |
| YS-LN02/Text/part0030.xhtml/p000252 | Giữ; phạm vi không cấm rõ ràng và giới hạn tùy cách diễn giải đúng. |
| YS-LN02/Text/part0030.xhtml/p000253 | Giữ; yêu cầu ví dụ cụ thể. |
| YS-LN02/Text/part0030.xhtml/p000254 | Giữ; không mất tiêu chí tấn công bừa bãi hoặc người không tham chiến. |
| YS-LN02/Text/part0030.xhtml/p000255 | Giữ; suy xét có vẻ bất khả thi và đổi góc nhìn không biến thành khẳng định tuyệt đối. |
| YS-LN02/Text/part0030.xhtml/p000256 | B08-M06; điều kiện, công/thủ và kết luận diễn giải khả dĩ đúng; loại nơi trú ẩn bị thu hẹp. |

## Rủi ro và trạng thái bàn giao

- Review đã hoàn tất; bản dịch chưa sign-off vì còn 6 finding vừa và 2 finding nhẹ chưa được translator xử lý.
- Self-check phủ nhận mọi nhấn mạnh trong package, dù có bốn vùng `em` ở ba ID. Cần sửa nhận định này cùng bản dịch để tránh lặp mất dấu.
- Phép ví von p245, cách gọi thị trường p249 và phạm vi đại từ theo giai đoạn còn bất định như T01–T03; đã có phương án tạm, không cần mở rộng nguồn hoặc đợi người dùng.
- Phần bàn về luật là lập luận của nhân vật trong package. Không xem nó là xác nhận luật thực tế, không thêm giải thích quốc gia/công ước ngoài nguồn.
- Validator/diff-check theo pipeline chưa chạy trong vai reviewer. Hash và độ phủ ID đã kiểm tra riêng; không dùng kết quả đó thay cho validator hoặc tuyên bố batch hoàn tất.
