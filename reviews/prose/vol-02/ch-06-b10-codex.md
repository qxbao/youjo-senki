# Review b10 — Codex

```yaml
role: reviewer
task_id: vol-02-ch-06-b10-review
state: done
review_result: changes_requested
review_path: reviews/prose/vol-02/ch-06-b10-codex.md
coverage: 46/46
segment_id_start: YS-LN02/Text/part0030.xhtml/p000285
segment_id_end: YS-LN02/Text/part0030.xhtml/p000330
source_package: work/vol-02/batches/ch-06-b10-source.jsonl
source_package_sha256: 2aa9e83e70ceb04bd458066e5a6621374f1ff1c60bdaa2682b8a5bc56ac5199c
hash_verified: true
counts:
  serious: 0
  moderate: 23
  minor: 8
  total: 31
count_unit: finding_record
unresolved_findings: [F01, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, L01, L02, L03, L04, L05, L06, L07, L08]
validator: not_run
diff_check: not_run
commit: null
```

Review đã hoàn tất; bản dịch cần sửa, chưa phải signoff. Số đếm là số finding riêng trong hai bảng bên dưới, không phải số ID: một ID có thể có nhiều lỗi độc lập. Có 15 finding lặp nội dung, 5 finding đại từ trần thuật và 3 finding nghĩa khác ở mức vừa. Các đề xuất thuật ngữ không tự được tính thành lỗi và đều chưa canon.

## Đầu vào và giới hạn

Đã đọc `AGENTS.md`, `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, hai handoff `handoffs/vol-02/ch-06-b10-review.yml` và `handoffs/vol-02/ch-06-b10.yml`; package được giao; `translations/vol-02/ch-06-b10.jsonl`; `reviews/semantic/vol-02/ch-06-b10-self-check.md`; năm tài liệu canon được handoff dẫn; các mục pending liên quan trong `work/run-state/pending-terms.yml`.

SHA-256 package khớp handoff. Hash hiện tại của cả năm tài liệu canon cũng khớp các giá trị trong handoff. Package có 46 đơn vị, bản dịch có 46 dòng, ID và thứ tự khớp hoàn toàn, từ p000285 đến p000330. Đã đối chiếu cả nội dung và phạm vi nhấn mạnh từ trường XHTML của đúng package này. Không mở EPUB/PDF, không đọc package khác. Các dẫn chiếu batch trước dưới đây chỉ dựa vào ledger pending đã được phép đọc, không phải kiểm tra lại bản dịch hay nguồn của batch đó.

Chỉ viết báo cáo này. Không sửa bản dịch, self-check, canon, ledger, handoff hoặc trạng thái pipeline. Không chạy validator/diff-check thay coordinator. Không chép câu nguồn vào báo cáo.

Self-check bỏ sót 15 ID lặp nội dung và hai chỗ mở rộng phạm vi chữ nghiêng. Nhận xét của self-check rằng p000306 đã chuyển câu hỏi tu từ thành lời bình cũng không khớp bản dịch hiện tại: câu hỏi vẫn còn. Self-check còn cho phép “cô/cô ta” trong trần thuật, trong khi handoff dẫn DEC-P01-001 và ledger ngay trước b10 đang đề xuất “nó”.

## Finding mức vừa

Mọi ID rút gọn trong các bảng là hậu tố của `YS-LN02/Text/part0030.xhtml/`. Các lỗi lặp bên dưới có độ chắc chắn cao: trường nội dung và XHTML của package chỉ thể hiện mỗi ý một lần; bản dịch có một bản trong dấu nhấn mạnh và một bản thường được thêm ở cuối. Xóa bản thường thừa, giữ bản dịch đúng một lần ở đúng vị trí; không xóa phần trần thuật hợp lệ nằm sau nội tâm.

| Finding | ID | Mức | Vấn đề, căn cứ và sửa đề xuất |
| --- | --- | --- | --- |
| F01 | p000287 | vừa | Thêm câu “Không còn cách nào khác.” ở cuối, lặp phần điều kiện đã dịch. Xóa câu thêm; vẫn giữ tính điều kiện của câu chính. |
| F02 | p000294 | vừa | Thêm lại ý không đốt thành phố thì tốt hơn sau phần nói về pháo binh/không quân. Xóa câu cuối thừa. |
| F03 | p000295 | vừa | Câu hỏi nội tâm xuất hiện hai lần, lần thứ hai sau câu về ý chí chiến đấu. Xóa bản thường cuối đoạn, giữ câu hỏi nghiêng ở đầu. |
| F04 | p000300 | vừa | Lặp toàn bộ câu nội tâm. Chỉ giữ một câu nghiêng. |
| F05 | p000306 | vừa | Cuối đoạn thêm một từ “chỉ” rời và lặp hai câu nội tâm, sau câu về chiến tuyến Rhine. Xóa toàn bộ phần thêm đó, giữ hai vùng nhấn mạnh tại vị trí ban đầu. |
| F06 | p000308 | vừa | Thêm lại “kẻ địch” thành mảnh câu cuối đoạn. Xóa mảnh thừa; giữ từ được nhấn mạnh trong câu chính. |
| F07 | p000312 | vừa | Lặp toàn bộ câu nội tâm. Chỉ giữ một câu nghiêng. |
| F08 | p000313 | vừa | Lặp câu hỏi nội tâm ở cuối. Giữ phần trần thuật đầu và một câu hỏi nghiêng. |
| F09 | p000314 | vừa | Lặp toàn bộ hai câu nội tâm. Chỉ giữ một bản nghiêng. |
| F10 | p000316 | vừa | Lặp chuỗi suy nghĩ về lời đồn sau câu đánh giá vô nhân tính. Xóa chuỗi thường cuối đoạn; giữ nội tâm nghiêng rồi đến câu đánh giá thường. |
| F11 | p000320 | vừa | Lặp toàn bộ ba câu nội tâm. Chỉ giữ một bản nghiêng. |
| F12 | p000321 | vừa | Lặp toàn bộ ba câu nội tâm. Chỉ giữ một bản nghiêng. |
| F13 | p000323 | vừa | Lặp câu hỏi về nụ cười. Chỉ giữ một câu nghiêng. |
| F14 | p000324 | vừa | Lặp toàn bộ chuỗi câu hỏi và lời gọi ma cà rồng. Chỉ giữ một bản nghiêng; không coi hình ảnh này là xác nhận lore. |
| F15 | p000330 | vừa | Lặp câu hỏi nội tâm sau các câu kể. Xóa câu cuối thừa, giữ câu hỏi ở đầu và các câu kể ở sau. |
| F16 | p000289 | vừa | Hai đại từ trần thuật về Tanya dùng “cô”. Handoff và lựa chọn pending sát b10 hỗ trợ “nó”; đề xuất “Nó được tin tưởng giao việc đến mức sẽ tham gia hỗ trợ. Chà, nó quả là có năng lực đáng sợ.” Có thể lặp tên Tanya nếu cần tránh đại từ. Chắc chắn cao về chủ thể trong chuỗi p000289–p000299; lựa chọn áp dụng tại LN02 vẫn ghi là tạm, không mở rộng quyết định sang mọi giai đoạn. |
| F17 | p000299 | vừa | Đại từ trong trần thuật về Tanya dùng “cô”. Đề xuất đổi thành “nó”, hoặc nhắc tên Tanya. Giữ đánh giá về bộ óc và mức độ dự liệu; không thay đại từ của người tư lệnh trong nội tâm. |
| F18 | p000306 | vừa | Đại từ trần thuật “cô” chưa theo lựa chọn hiện hành. Đề xuất “Đúng vậy, nó *chỉ* đang kiểm tra…”. Câu hỏi nghiêng sau đó là suy nghĩ của người tư lệnh; không áp đại từ trần thuật vào lời thoại hoặc tự quy chiếu. |
| F19 | p000308 | vừa | Đại từ trần thuật “cô” chưa theo lựa chọn hiện hành. Đề xuất “Nhưng ông hiểu vì sao nó phải xác nhận lại định nghĩa.” Phần sau vẫn nhấn đúng thuật ngữ kẻ địch. |
| F20 | p000316 | vừa | Câu thường đánh giá Tanya dùng “Cô ta”. Đề xuất “Nó đúng là vô nhân tính.” Giữ “cô ta” trong phần nội tâm trước đó: đó là cách người tư lệnh nghĩ về Tanya, không phải tự quy chiếu của Tanya. Mức chắc chắn khá cao; không thay máy móc cả đoạn. |
| F21 | p000295 | vừa | “Cớ ngoại phạm” dễ gợi chứng minh không có mặt tại hiện trường, trong khi chuỗi lập luận nói về dùng cảnh báo đầu hàng để biện minh cho việc tiếp theo. “Ra lệnh đầu hàng” cũng làm mờ chức năng cảnh báo. Đề xuất câu nội tâm: “*Vậy họ định đưa ra lời cảnh báo buộc đầu hàng sau khi Tiểu đoàn Pháp sư Trên không số 203 tiêu diệt các pháp sư, chỉ để có cớ biện minh sao?*” Phương án khác: “để có lý lẽ tự bào chữa”. Giữ đây là câu hỏi suy đoán, không biến thành kết luận về chủ ý đã được xác nhận. Chắc chắn cao về nghĩa cảnh báo; khá cao về cách dùng alibi theo ngữ cảnh. |
| F22 | p000320 | vừa | “Người lính của cỗ máy chiến tranh này” biến hình ảnh người lính như cỗ máy thành quan hệ thuộc về một cỗ máy/hệ thống. Ngữ cảnh người tư lệnh đang đánh giá cá nhân Tanya, người chỉ cần được cho phép và có mệnh lệnh. Đề xuất “Dù sao thì người lính như một cỗ máy chiến tranh này chỉ cần được cho phép và nhận mệnh lệnh là đủ.” Phương án khác: “người lính chẳng khác nào cỗ máy chiến tranh này”. Chắc chắn khá cao; cụm danh từ nguồn nén nghĩa, nên dùng phép so sánh để tránh tự khẳng định một thuộc tính lore. |
| F23 | p000330 | vừa | “Chẳng còn gì phải lo ư?” hỏi lại tính đúng/sai của lời trấn an, làm mất câu hỏi về đối tượng: cụ thể không phải lo chuyện gì. Đề xuất “*Không phải lo chuyện gì cơ?*” hoặc “*Chẳng còn gì phải lo về chuyện gì?*”; ưu tiên phương án đầu tự nhiên hơn. Giữ các câu kể về muốn hỏi/kìm lại/không muốn biết. Chắc chắn cao; style-guide yêu cầu giữ đối tượng và độ mở câu hỏi. |

## Finding mức nhẹ

| Finding | ID | Mức | Vấn đề và đề xuất |
| --- | --- | --- | --- |
| L01 | p000287 | nhẹ | Dấu nghiêng bao cả “nếu”, trong khi XHTML chỉ nhấn phần không còn cách nào khác. Đề xuất “Xem ra, nếu *không còn cách nào khác*, …”. Độc lập với việc xóa câu lặp F01. Chắc chắn cao. |
| L02 | p000294 | nhẹ | Nhấn cả phương án không đốt thành phố, trong khi XHTML chỉ nhấn phần đánh giá tối ưu. Đề xuất “Hẳn họ nghĩ rằng giải quyết mọi chuyện mà không thiêu rụi thành phố *là tốt nhất*.” Giữ suy đoán của người kể. Chắc chắn cao. |
| L03 | p000297 | nhẹ | “Đã trở thành thương vong” là kết hợp từ gượng. Đề xuất “Nhiều cư dân Arene đã bị thương hoặc thiệt mạng.” Phương án khác: “Cư dân Arene đã chịu nhiều thương vong.” Ưu tiên phương án đầu giữ chủ thể và độ mở, không tự thu hẹp thành chỉ chết. Chắc chắn cao. |
| L04 | p000303 | nhẹ | “Chim chóc thì thầm” kém tự nhiên và đổi hình ảnh một chú chim thành số nhiều. Phải giữ cả cách ám chỉ tin nghe được và trò đối đáp về thính giác ở p000304. Đề xuất “À phải, tôi tình cờ nghe một chú chim mách nhỏ chuyện du kích…”. Phương án khác: “tôi nghe một chú chim líu lo chuyện du kích…”. Không chỉ sửa thành “nghe đồn” rồi bỏ hình ảnh, vì sẽ làm yếu câu đáp kế tiếp. Độ chắc chắn vừa về lựa chọn văn phong; không phải lỗi chủ thể du kích. |
| L05 | p000309 | nhẹ | “Phô trương sức mạnh” dễ nghiêng về biểu diễn/răn đe hơn là có dịp dùng sức thực sự; “đến mức chí mạng” cũng gượng. Đề xuất “Vậy là chúng ta có dịp trổ sức. Ý ngài là ta phải vui vẻ câu giờ dù địch đông áp đảo đến mức có thể mất mạng sao?” Phương án khác: “có dịp ra tay”. Giữ giọng mỉa và yêu cầu câu giờ, không thêm ý tự sát chắc chắn. Độ chắc chắn vừa. |
| L06 | p000312 | nhẹ | Nội tâm người tư lệnh dùng “tôi”, trong khi p000300–p000302, p000316, p000320 và p000326 dùng “mình”. Đề xuất “*Ừ, mình hiểu vì sao người ta có thể diễn giải theo hướng đó.*” sau khi bỏ bản lặp. “Tôi” vẫn là phương án hợp lệ nếu coordinator chọn nhất quán cho nội tâm người tư lệnh; DEC-P01-001 không tự quy định nội tâm của người này. Độ chắc chắn vừa, vấn đề nhất quán giọng. |
| L07 | p000326 | nhẹ | “Vừa giật mình” có thể chỉ cảm giác bất ngờ, làm nhạt phản ứng cơ thể mà ông lo người khác nhìn thấy. Đề xuất “*Mong là không ai nhận ra mình vừa giật nảy người*, viên tư lệnh quân đoàn nghĩ thầm, nhận rõ rằng ông sợ cô ta.” Phương án khác: “vừa co rúm lại”. Chưa đủ chi tiết để chọn động tác lớn; “giật nảy người” là đề xuất, có thể giữ “giật mình” nếu muốn ít suy diễn hơn. Độ chắc chắn vừa. |
| L08 | p000327 | nhẹ | “Cả khu phố” có thể đọc như một khu duy nhất; nguồn cho phép tàn phá nguyên các khu phố. Đề xuất “Vậy ta có thể san phẳng nguyên các khu phố chứ?” hoặc “san phẳng từng khu phố chứ?”. Phương án đầu giữ số nhiều mà không thêm kế hoạch tuần tự. Độ chắc chắn khá cao; không tự mở rộng thành toàn thành phố. |

## Năm passage được gắn cờ

- **p000293:** Vai trò tiên phong, số hiệu 203, cấp tiểu đoàn, đối tượng pháp sư và mục đích gỡ cản trở trấn áp đều được giữ. Không có lỗi nghĩa nghiêm trọng/vừa riêng tại ID này. Tên đơn vị cần đề xuất thống nhất theo T02 bên dưới.
- **p000295:** F03 và F21 cần sửa. Câu nội tâm là câu hỏi của người tư lệnh, chưa chứng minh động cơ thật của giới chỉ huy. Giữ thứ tự tiêu diệt pháp sư → cảnh báo đầu hàng → nếu ý chí chiến đấu không suy giảm thì quân đội không còn lựa chọn. Không diễn giải thành dân đã chắc chắn đầu hàng hoặc chắc chắn bị giết. Tên đơn vị dùng T02.
- **p000298:** Chủ thể thiếu tá pháp sư là Tanya trong mạch local; đánh giá về quan điểm và luật quốc tế được giữ. “Trường sĩ quan tham mưu” là phương án có thể dùng nhưng chuyên biệt hóa loại cơ sở; package không tự xác lập tên chính thức. Khuyến nghị tạm T03, không tính một nghi vấn chưa đủ chứng cứ thành lỗi nghĩa đã xác định. Áp dụng cùng lựa chọn ở p000315.
- **p000306:** Bản hiện tại giữ câu hỏi tu từ, không chuyển thành lời bình như self-check mô tả. Chỉ cần F05/F18; giữ hai vùng nghiêng riêng: từ hạn định và chuỗi nội tâm. Phần về chiến tuyến Rhine là trần thuật thường. Câu hỏi thể hiện sự khó hiểu của người tư lệnh trước việc Tanya xác nhận định nghĩa; không phải Tanya tự chất vấn mình.
- **p000326:** Package tự nêu chức vụ tư lệnh quân đoàn và đại từ nam của chủ thể nội tâm; “ông” có căn cứ, không phải suy ra từ chức vụ. Ông là người sợ Tanya, không phải ngược lại. Nội tâm dùng “mình” có thể giữ tạm để nhất quán; đây không phải áp dụng quy tắc Tanya. L07 chỉ là tinh chỉnh sắc thái phản ứng cơ thể. Không suy tên riêng hay quân hàm từ chức vụ này.

## Đề xuất thuật ngữ và lựa chọn tạm

Tất cả mục sau là **proposed/pending**, không được nâng thành canon. Coordinator tiếp nhận vào ledger/handoff trong quyền của mình; reviewer không sửa các tệp đó. Không có mục nào cần chờ người dùng trong phạm vi review này.

| Mục | Thuật ngữ / ID | Lựa chọn tạm tốt nhất | Phương án khác, lý do và độ bất định |
| --- | --- | --- | --- |
| T01 | the brass; p000286, cùng cụm chỉ cấp trên ở p000294/p000319 | “giới chỉ huy cấp cao” tại p000286; “cấp trên” tại p000294 và lời thoại p000319 | Giữ như bản hiện tại. Ba vị trí liên quan về nghĩa nhưng không phải đều dùng đúng một từ nguồn. “Lãnh đạo quân đội” cũng có thể dùng; “bộ chỉ huy cấp cao” dễ gợi một cơ quan xác định, còn “đám chỉ huy” tăng sắc thái coi thường mà local không buộc phải có. Chắc chắn cao về tập thể chỉ huy; chưa xác định cơ quan/quân hàm cụ thể. |
| T02 | 203rd Aerial Mage Battalion; p000293, p000295 | “Tiểu đoàn Pháp sư Trên không số 203” | Kế thừa đề xuất vol02-ch05-b03 trong ledger và mục cùng tên sau đó; giữ đầy đủ loại đơn vị, pháp sư, tính trên không, số hiệu. “Tiểu đoàn Pháp sư Không chiến 203” vẫn hiểu được nhưng đổi cách gọi pending và nhấn chức năng chiến đấu; “Tiểu đoàn Pháp sư Bay số 203” là phương án tự nhiên hơn nhưng hẹp về thao tác bay. “Không quân” có nguy cơ suy quân chủng, nên chưa chọn. Độ tin cậy khá cao về cấu tạo, vừa về tên tiếng Việt/cách viết hoa; không tuyên bố tên chính thức. |
| T03 | war college; p000298, p000315 | “trường quân sự cao cấp” | Tạm ưu tiên cách gọi rộng, không khẳng định đây là trường đào tạo sĩ quan tham mưu. “Trường sĩ quan tham mưu” có thể giữ nếu coordinator cần kế thừa tên pending, nhưng phải ghi chưa xác minh cơ cấu; “học viện quân sự” cũng có thể dùng nhưng ngầm chọn loại cơ sở. Local chỉ cho biết cơ sở gắn với quan điểm/diễn giải luật, chưa đủ để chốt tên riêng. Độ tin cậy vừa; dùng cùng một lựa chọn ở cả hai ID. |
| T04 | alibi; p000295 | “cớ biện minh” | “Lý lẽ tự bào chữa” giữ chức năng né trách nhiệm nhưng dài hơn. Tránh “cớ ngoại phạm” vì dễ hiểu là chứng minh vắng mặt. Căn cứ từ cảnh báo đầu hàng và chuỗi diễn giải pháp lý trong local. Khá chắc; vẫn giữ dấu hỏi về động cơ, không chốt sự kiện cốt truyện. |
| T05 | army corps commander; p000285, p000326 | “tư lệnh quân đoàn”; trần thuật “ông” | “Chỉ huy quân đoàn” ít tính danh xưng hơn. Package đủ căn cứ cho cấp tổ chức quân đoàn và chủ thể nam, nhưng không cho tên riêng/quân hàm cụ thể. Độ tin cậy cao cho chức vụ và chủ thể; giữ pending về cách gọi. |
| T06 | Đại từ Tanya trong trần thuật; p000289, p000299, p000306, p000308, phần thường p000316 | “nó” theo handoff và lựa chọn pending gần nhất | Có thể nhắc tên Tanya. DEC-P01-001 có giới hạn giai đoạn, nên đây là kế thừa tạm trong phạm vi b10 theo chỉ dẫn handoff, không quy tắc canon mới cho cả LN02. Không đổi “cô/cô ta” trong thoại hoặc nội tâm của người tư lệnh ở p000300/p000316/p000321/p000323/p000324/p000326/p000330. Khá chắc về chủ thể; chưa chốt hệ xưng hô ngoài phạm vi. |
| T07 | Tự quy chiếu người tư lệnh; p000300–p000302, p000312, p000316, p000320, p000326 | “mình” trong nội tâm | Giữ nhất quán với đa số vị trí hiện tại, sửa riêng p000312 nếu coordinator chọn phương án này. “Tôi” là lựa chọn thay thế nhất quán; không viện DEC-P01-001 để bắt buộc cho nhân vật này. Độ tin cậy vừa về giọng, cao về chủ thể; không nhầm các nội tâm này là của Tanya. |

Các cách gọi “thiếu tá/pháp sư”, “dân quân”, “người không tham chiến”, “Công ước Chiến tranh trên bộ”, “Bộ Hậu cần”, tên von Zettour/von Degurechaff, Arene, Rhine và Valhalla chưa có mục canon chốt tên trong tài liệu được giao. Bản hiện tại không phát sinh mâu thuẫn nghĩa có căn cứ tại các vị trí đó; giữ tạm, không tự đổi quân hàm, khai triển tên cơ quan hay xác định một công ước ngoài đời. Không mở nguồn ngoài để xử lý các nhãn này.

## Sổ đối chiếu đủ 46 ID

“Đạt local” nghĩa là không có finding riêng sau đối chiếu nghĩa, phủ định, điều kiện, thời gian, điểm nhìn, nhấn mạnh và văn phong trong package b10; không phải signoff toàn batch. Các ID có T chỉ là khuyến nghị tạm. Những finding khác nhau tại cùng ID được giữ riêng để số đếm kiểm tra được.

| ID | Kết quả |
| --- | --- |
| YS-LN02/Text/part0030.xhtml/p000285 | Đạt local; hậu cần bị cắt → đói, kết luận tự giễu; T05. |
| YS-LN02/Text/part0030.xhtml/p000286 | Đạt local; giữ suy đoán và quyết tâm thể hiện qua mệnh lệnh; T01. |
| YS-LN02/Text/part0030.xhtml/p000287 | F01, L01; giữ điều kiện không còn cách khác. |
| YS-LN02/Text/part0030.xhtml/p000288 | Đạt local; sơ tán/giới nghiêm đã ban, hai điều kiện và cách nói tránh được giữ. |
| YS-LN02/Text/part0030.xhtml/p000289 | F16. |
| YS-LN02/Text/part0030.xhtml/p000290 | Đạt local; lời mời đặt câu hỏi. |
| YS-LN02/Text/part0030.xhtml/p000291 | Đạt local; hỏi quy mô lực lượng dự kiến. |
| YS-LN02/Text/part0030.xhtml/p000292 | Đạt local; giữ giới hạn ít nhất một tiểu đoàn. |
| YS-LN02/Text/part0030.xhtml/p000293 | Đạt nghĩa local; passage gắn cờ, T02. |
| YS-LN02/Text/part0030.xhtml/p000294 | F02, L02; T01. |
| YS-LN02/Text/part0030.xhtml/p000295 | F03, F21; passage gắn cờ, T02/T04. |
| YS-LN02/Text/part0030.xhtml/p000296 | Đạt local; câu hỏi về loại quân. |
| YS-LN02/Text/part0030.xhtml/p000297 | L03; phân biệt số ít pháp sư và dân quân được giữ. |
| YS-LN02/Text/part0030.xhtml/p000298 | Đạt nghĩa local; passage gắn cờ, T03. |
| YS-LN02/Text/part0030.xhtml/p000299 | F17; giữ giới hạn đánh giá cường điệu. |
| YS-LN02/Text/part0030.xhtml/p000300 | F04; nội tâm người tư lệnh, T07. |
| YS-LN02/Text/part0030.xhtml/p000301 | Đạt local; người tư lệnh đã được cho biết chi tiết và hối hận; T07. |
| YS-LN02/Text/part0030.xhtml/p000302 | Đạt local; lời chửi trong nội tâm người tư lệnh, không tự chuyển chủ thể sang Tanya; T07. |
| YS-LN02/Text/part0030.xhtml/p000303 | L04; lời ám chỉ về du kích và hình ảnh chim. |
| YS-LN02/Text/part0030.xhtml/p000304 | Đạt local; giữ câu đáp về nghe quá rõ/nhầm âm thanh. |
| YS-LN02/Text/part0030.xhtml/p000305 | Đạt local; câu hỏi xác nhận quân địch. |
| YS-LN02/Text/part0030.xhtml/p000306 | F05, F18; passage gắn cờ. |
| YS-LN02/Text/part0030.xhtml/p000307 | Đạt local; lời thoại về công ước và bảo vệ người không tham chiến. |
| YS-LN02/Text/part0030.xhtml/p000308 | F06, F19. |
| YS-LN02/Text/part0030.xhtml/p000309 | L05; giữ câu hỏi về câu giờ và nguy cơ từ quân số áp đảo. |
| YS-LN02/Text/part0030.xhtml/p000310 | Đạt local; giữ hai lựa chọn chiến thắng/Valhalla và giọng đáp. |
| YS-LN02/Text/part0030.xhtml/p000311 | Đạt local; câu hỏi diễn giải mệnh lệnh, chưa biến thành lệnh mới. |
| YS-LN02/Text/part0030.xhtml/p000312 | F07, L06; T07. |
| YS-LN02/Text/part0030.xhtml/p000313 | F08; giữ giới hạn về lý thuyết của pháp lý. |
| YS-LN02/Text/part0030.xhtml/p000314 | F09; giữ so sánh và dự báo không có giao tranh. |
| YS-LN02/Text/part0030.xhtml/p000315 | Đạt nghĩa local; giả định diễn giải luật đúng vẫn không xóa đánh giá thảm sát; T03. |
| YS-LN02/Text/part0030.xhtml/p000316 | F10, F20; không nâng lời đồn thành sự kiện chắc chắn. |
| YS-LN02/Text/part0030.xhtml/p000317 | Đạt local; hôm qua 11 giờ và giả định pháp lý về chiếm thành phố được giữ. |
| YS-LN02/Text/part0030.xhtml/p000318 | Đạt local; hỏi hệ quả/ý nghĩa. |
| YS-LN02/Text/part0030.xhtml/p000319 | Đạt local; mệnh lệnh tiêu diệt và giới hạn “xét về mặt pháp lý”; T01. |
| YS-LN02/Text/part0030.xhtml/p000320 | F11, F22; T07. |
| YS-LN02/Text/part0030.xhtml/p000321 | F12; các đại từ là trong nội tâm người tư lệnh, không thay theo T06. |
| YS-LN02/Text/part0030.xhtml/p000322 | Đạt local; câu thoại và cách nói lạnh lùng được giữ. |
| YS-LN02/Text/part0030.xhtml/p000323 | F13; câu hỏi nội tâm người tư lệnh. |
| YS-LN02/Text/part0030.xhtml/p000324 | F14; hình ảnh nanh/ma cà rồng thuộc đánh giá nội tâm. |
| YS-LN02/Text/part0030.xhtml/p000325 | Đạt local; giữ cuộc đua với thời gian. |
| YS-LN02/Text/part0030.xhtml/p000326 | L07; passage gắn cờ, T05/T07. |
| YS-LN02/Text/part0030.xhtml/p000327 | L08; giữ điều kiện thành phố đã do địch kiểm soát. |
| YS-LN02/Text/part0030.xhtml/p000328 | Đạt local; lời gọi thiếu tá ngắn, giữ ngắt mạch. |
| YS-LN02/Text/part0030.xhtml/p000329 | Đạt local; giữ hai điều kiện về thường dân và thành phố đã bị chiếm. |
| YS-LN02/Text/part0030.xhtml/p000330 | F15, F23; câu hỏi và tự kiềm chế của người tư lệnh. |

## Chuyển tiếp và rủi ro

Coordinator giao người giữ quyền sửa xử lý 23 finding mức vừa và cân nhắc 8 finding nhẹ; áp dụng tên đơn vị, tên trường và đại từ được chọn tạm nhất quán. Sau sửa, cần đối chiếu lại các ID liên quan và chạy kiểm tra bắt buộc của pipeline. Không coi trạng thái `done` của reviewer là hoàn tất batch hoặc cho phép commit bản dịch chưa sửa.

Rủi ro chính: nội dung thường lặp lại sau phần nghiêng, self-check chưa phản ánh bản hiện tại; đổi đại từ máy móc có thể nhầm nội tâm người tư lệnh với Tanya; tên trường/quân chủng chưa đủ chứng cứ để chốt; câu hỏi về động cơ ở p000295 và suy đoán lời đồn ở p000316 không được nâng thành sự thật cốt truyện. Không còn thiếu đầu vào, không có quyết định canon ảnh hưởng cốt truyện cần dừng chờ người dùng. Mọi finding hiện còn mở vì reviewer không được sửa bản dịch.
