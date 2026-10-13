# Phản biện b11 — vol-02, ch-06

```yaml
role: reviewer
task_id: vol-02-ch-06-b11-review
state: done
review_result: revisions_required
segment_ids:
- YS-LN02/Text/part0030.xhtml/p000331
- YS-LN02/Text/part0030.xhtml/p000332
- YS-LN02/Text/part0030.xhtml/p000333
- YS-LN02/Text/part0030.xhtml/p000334
- YS-LN02/Text/part0030.xhtml/p000335
- YS-LN02/Text/part0030.xhtml/p000336
- YS-LN02/Text/part0030.xhtml/p000337
- YS-LN02/Text/part0030.xhtml/p000338
- YS-LN02/Text/part0030.xhtml/p000339
- YS-LN02/Text/part0030.xhtml/p000340
- YS-LN02/Text/part0030.xhtml/p000341
- YS-LN02/Text/part0030.xhtml/p000342
- YS-LN02/Text/part0030.xhtml/p000343
- YS-LN02/Text/part0030.xhtml/p000344
- YS-LN02/Text/part0030.xhtml/p000345
- YS-LN02/Text/part0030.xhtml/p000346
- YS-LN02/Text/part0030.xhtml/p000347
- YS-LN02/Text/part0030.xhtml/p000348
- YS-LN02/Text/part0030.xhtml/p000349
- YS-LN02/Text/part0030.xhtml/p000350
- YS-LN02/Text/part0030.xhtml/p000351
- YS-LN02/Text/part0030.xhtml/p000352
- YS-LN02/Text/part0030.xhtml/p000353
- YS-LN02/Text/part0030.xhtml/p000354
- YS-LN02/Text/part0030.xhtml/p000355
- YS-LN02/Text/part0030.xhtml/p000356
- YS-LN02/Text/part0030.xhtml/p000357
- YS-LN02/Text/part0030.xhtml/p000358
files_written:
- reviews/prose/vol-02/ch-06-b11-codex.md
review_path: reviews/prose/vol-02/ch-06-b11-codex.md
source_package: work/vol-02/batches/ch-06-b11-source.jsonl
source_package_sha256: c1dfda6756f791aad672a6f89a87de0017104fd7be57d0cc8a123f631b5d0831
hash_verification: pass
coverage: 28/28
counts:
  serious: 0
  moderate: 4
  minor: 3
counting_method: Đếm phát hiện, không đếm số ID; F02 bao gồm hai ID.
unresolved_findings: [F01, F02, F03, F04, F05, F06, F07]
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_receive_review_then_translator_revise
```

## Đầu vào và giới hạn

Đã đọc `AGENTS.md`, `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, hai handoff `handoffs/vol-02/ch-06-b11.yml` và `handoffs/vol-02/ch-06-b11-review.yml`, package b11, bản dịch `translations/vol-02/ch-06-b11.jsonl`, self-check `reviews/semantic/vol-02/ch-06-b11-self-check.md`, cùng năm file canon được handoff dẫn: glossary, style-guide, characters, decisions và glossary-pending. Đọc các lựa chọn/đề xuất liên quan trong ledger `work/run-state/pending-terms.yml`, đặc biệt các lựa chọn chương 6 về dân quân, tư lệnh quân đoàn, đại từ và năm đề xuất b11. Không mở báo cáo hay package của batch khác; không mở EPUB/PDF, chú thích ngoài package hoặc dịch vụ ngoài.

SHA-256 package khớp handoff; SHA-256 của cả năm file canon cũng khớp. Package và bản dịch đều có 28 ID, đúng thứ tự p000331–p000358. Glossary chính thức và danh sách nhân vật chưa chốt mục nào. Áp dụng DEC-P01-001 và DEC-P01-002; các tên gọi/thuật ngữ khác chỉ là phương án tạm.

Nhận định dưới đây chỉ đối chiếu bản dịch với package được giao. Những lập luận về chiến tranh, hồi tố và trách nhiệm pháp lý là suy nghĩ của nhân vật, không phải xác nhận luật hoặc lịch sử. Không chép câu nguồn vào báo cáo.

## Phát hiện cần xử lý

### F01 — moderate — YS-LN02/Text/part0030.xhtml/p000331

- **Vấn đề:** Mất cặp dấu ngoặc thoại, làm lời nói thành câu kể. Đây là thay đổi tầng phát ngôn, ngay trước lượt đáp ở p000334.
- **Căn cứ:** Text và XHTML của p000331 đều có dấu thoại; đây không phải câu nhấn mạnh/nội tâm.
- **Đề nghị:** Giữ bản dịch hiện có nhưng bọc bằng dấu thoại: “Nhưng chuyện này thật sự đáng tiếc.”
- **Bất định:** Thấp về lỗi dấu thoại; package không đủ căn cứ để ghi tên người nói. Không thêm người nói hoặc đại từ.

### F02 — moderate — YS-LN02/Text/part0030.xhtml/p000332; YS-LN02/Text/part0030.xhtml/p000333

- **Vấn đề:** “Sự đã rồi” giữ tính không thể quay lại, nhưng “kết cục” ở đoạn sau xóa hình ảnh xúc xắc được lặp có chủ ý. Nó cũng dễ gợi một kết quả đã hoàn tất, trong khi chuỗi này nói về bước quyết định và nỗi ghê sợ của người gánh trách nhiệm.
- **Căn cứ:** Từ ngắn `die` xuất hiện ở cả hai ID, lần đầu trong thành ngữ, lần sau nối lại hình ảnh ấy. Dấu nhấn mạnh chỉ bao trọn p000332; p000333 không nghiêng.
- **Đề nghị tạm:** p000332: *Vậy là xúc xắc đã gieo.* p000333: “Với người phải chịu trách nhiệm, có lẽ chẳng có con xúc xắc nào khiến người ta buồn nôn hơn.” Đây là đề xuất để translator cân lại độ tự nhiên, không phải bản dịch đã chốt.
- **Phương án khác:** “Ván đã đóng thuyền” / “ván cược ấy” giữ cảm giác quyết định nhưng thay đổi hình ảnh; “sự đã rồi” / “quyết định ấy” rõ nghĩa hơn nhưng mất lặp hình tượng. Không dùng “ván đã đóng” đứng riêng như trong ledger.
- **Bất định:** Thấp về sự lặp hình ảnh, vừa về cách Việt hóa tự nhiên. Không tự thêm người gieo xúc xắc hoặc diễn giải thành kết cục chắc chắn.

### F03 — moderate — YS-LN02/Text/part0030.xhtml/p000350

- **Vấn đề:** “Ném bom chiến lược bừa bãi” thu hẹp `bombardment` thành hành động thả bom. p000352–p000354 ngay trong package phân biệt bom với pháo binh, nên sự thu hẹp này có thể làm lệch đối tượng Tanya đang lo ngại. “Bừa bãi” còn dễ gợi làm ẩu thay vì không phân biệt mục tiêu.
- **Đề nghị tạm:** “...khả năng oanh kích chiến lược không phân biệt mục tiêu?” Giữ dạng câu hỏi và mức ám chỉ, không khẳng định đã có mệnh lệnh giết dân thường.
- **Phương án khác:** “bắn phá chiến lược không phân biệt mục tiêu” bao quát, nhưng hơi nghiêng về pháo binh; “oanh tạc chiến lược không phân biệt mục tiêu” dễ lại gợi riêng không kích.
- **Bất định:** Vừa về thuật ngữ bao quát; thấp về việc cần giữ khả năng bao gồm pháo binh. Đây là lựa chọn ngôn ngữ tạm, không định nghĩa pháp lý.

### F04 — moderate — YS-LN02/Text/part0030.xhtml/p000355

- **Vấn đề:** Mạch đối lập nước bại trận/bên thắng và nỗi sợ bị quy là tội phạm chiến tranh được giữ. Tuy nhiên, “bị kết án” thêm một kết quả tố tụng cụ thể vào mệnh đề khó hiểu chứa `written off`; package không đủ để chắc rằng đây là kết án chính thức. “Bị xướng tên thành tội phạm chiến tranh” cũng không tự nhiên và dễ gợi một danh hiệu.
- **Đề nghị tạm:** Giữ đối lập hiện tại; đổi vế cuối của lập luận thành “...chứ đừng nói đến việc bị lên án sau những cuộc chất vấn vốn chẳng hề diễn ra.” Đổi nguy cơ cá nhân thành “Chỉ cần một bước đi sai lầm, mình có thể bị quy là tội phạm chiến tranh.”
- **Phương án khác:** “bị đánh giá là sai trái” trung tính hơn cho vế bên thắng; “bị coi là tội phạm chiến tranh” nhẹ hơn “bị quy là”. Không ưu tiên cách hiểu miễn trách nhiệm hoặc hợp pháp hóa, vì sẽ đảo hướng lập luận trong package.
- **Lý do:** Đây là độc thoại lo trách nhiệm và tiêu chuẩn bên thắng/bên thua. Cách tạm trên giữ hướng phê phán nhưng giảm mức suy diễn về phán quyết.
- **Bất định:** Vừa đến cao ở `written off`; thấp về đối lập hai bên và điều kiện tự bảo toàn. Không cần chờ quyết định thuật ngữ thông thường; coordinator có thể ghi cách trung tính vào ledger, vẫn để pending. Không sửa câu này thành một kết luận khách quan về luật.

### F05 — minor — YS-LN02/Text/part0030.xhtml/p000341

- **Vấn đề:** “Thấy như ở nhà giữa địa ngục” bám cấu trúc thành ngữ, hơi cứng trong tiếng Việt.
- **Đề nghị tạm:** “Có lẽ cô cảm thấy quen thuộc như ở nhà giữa địa ngục nơi Mặt trận Rhine.” Phương án khác: “Có lẽ cô thấy thoải mái giữa địa ngục nơi Mặt trận Rhine”; phương án này trôi hơn nhưng bớt hình ảnh nhà.
- **Bất định:** Thấp về nghĩa thành ngữ; vừa về “cô”. Lời hướng đến Tanya trong nội tâm không phải đại từ trần thuật; không thay máy móc bằng “nó”.

### F06 — minor — YS-LN02/Text/part0030.xhtml/p000342

- **Vấn đề:** “Hầm trú quân dự bị” dễ bị hiểu là hầm của lực lượng dự bị thay vì nơi chờ lệnh; “tuyến đầu” giảm sắc thái tuyến trước cùng; “an toàn hơn” thêm so sánh vào mô tả hầm chỉ huy an toàn.
- **Đề nghị tạm:** “...khỏi hầm trú quân nơi mình chờ lệnh ở tuyến trước cùng, đến hầm chỉ huy an toàn ở phía sau...” Giữ phần còn lại, gồm mệnh lệnh ưu tiên cao nhất và nhiệm vụ diệt pháp sư.
- **Phương án khác:** “hầm chờ lệnh ở tuyến đầu tiên”; “hầm trú quân ở vị trí tiền tiêu” tự nhiên nhưng gợi loại vị trí quân sự cụ thể hơn.
- **Bất định:** Vừa về cách gọi hầm; thấp về việc không nên gán “dự bị” cho quân số hoặc thêm so sánh.

### F07 — minor — YS-LN02/Text/part0030.xhtml/p000354

- **Vấn đề:** “Nằm trong phạm vi thông thường” cứng và làm lời tự trấn an thành văn giải thích.
- **Đề nghị tạm:** “...chuyện này *vẫn* thuộc loại thường thấy.” Phương án khác: “...chuyện này *quả là* thuộc loại thông thường.”
- **Lý do:** Nhấn sự khẳng định của Tanya rằng thủ đoạn này không khác tiền lệ thông thường, sau khi đã gọi nó là thảm sát. Giữ nhấn mạnh hẹp tương ứng với vị trí khẳng định trong nguồn, không nghiêng cả câu.
- **Bất định:** Vừa về từ mang nhấn mạnh tiếng Việt. Bản hiện tại không mắc lỗi thêm nhấn mạnh; đây là sửa độ tự nhiên, không giảm mức “thảm sát” hoặc biến thông thường thành hợp pháp.

## Rà đủ 28 ID

Mỗi hàng đã xét nghĩa, văn phong, điểm nhìn, nhấn mạnh và thuật ngữ. “Đạt” nghĩa là không có lỗi cần sửa được chứng minh trong phạm vi package; các lựa chọn tạm vẫn cần được quản lý là pending.

| Stable ID | Nghĩa / văn phong | Điểm nhìn | Nhấn mạnh | Thuật ngữ / kết luận |
|---|---|---|---|---|
| YS-LN02/Text/part0030.xhtml/p000331 | Nghĩa đạt; mất dấu thoại, F01 | Phải là lời nói | Không nghiêng, đúng | Không thêm người nói |
| YS-LN02/Text/part0030.xhtml/p000332 | Không thể đảo ngược được giữ; mất hình ảnh, F02 | Nội tâm không tự gán chủ thể | Nghiêng toàn đoạn, đúng | Thành ngữ pending, xét cùng p333 |
| YS-LN02/Text/part0030.xhtml/p000333 | Giữ có lẽ và buồn nôn; “kết cục” lệch hình ảnh, F02 | Trần thuật về người gánh trách nhiệm, chưa định danh | Không nghiêng, đúng | Đề nghị giữ xúc xắc |
| YS-LN02/Text/part0030.xhtml/p000334 | Đạt: mệnh lệnh có điều kiện, vẫn thiêu thành phố đẹp | Thoại, chúng ta là binh lính | Nhấn cụm tăng cường, đúng | Arene tạm giữ nguyên |
| YS-LN02/Text/part0030.xhtml/p000335 | Đạt: lời rủa và đánh giá độc ác | Nội tâm, không gán người bị gọi quỷ sứ ngoài căn cứ | Nghiêng toàn đoạn, đúng | Zettour/Rudersdorf giữ nguyên, chưa canon |
| YS-LN02/Text/part0030.xhtml/p000336 | Đạt: suy đoán và lặp ý bất chấp thủ đoạn | Nội tâm về họ | Nghiêng toàn đoạn, đúng | Chưa cần thêm giải thích |
| YS-LN02/Text/part0030.xhtml/p000337 | Đạt: bằng mọi giá và phát rồ | Nội tâm đánh giá binh lính | Nghiêng toàn đoạn, đúng | Không suy thành chẩn đoán |
| YS-LN02/Text/part0030.xhtml/p000338 | Đạt: khuyên không ai làm lính; giọng chán chường | Thoại, không gán người nói | Không nghiêng, đúng | Không có term mới |
| YS-LN02/Text/part0030.xhtml/p000339 | Đạt: không phải ai cũng được sống theo ý muốn | “Cậu” chỉ là cách gọi tạm trong thoại | Không nghiêng, đúng | Có thể bỏ xưng hô nếu cần trung tính |
| YS-LN02/Text/part0030.xhtml/p000340 | Đạt: lời xác nhận hướng đến Degurechaff | Nội tâm hướng đến người khác | Nghiêng toàn đoạn, đúng | Thiếu tá Pháp sư tạm giữ; chưa chốt hệ quân hàm |
| YS-LN02/Text/part0030.xhtml/p000341 | Giữ hai mức có lẽ; thành ngữ cứng, F05 | “Cô” không thuộc quy ước “nó” trong trần thuật | Nghiêng toàn đoạn, đúng | Rhine tạm giữ nguyên |
| YS-LN02/Text/part0030.xhtml/p000342 | Nhiệm vụ/ưu tiên đạt; chi tiết hầm/tuyến cần làm rõ, F06 | Chuyển tự quy chiếu “mình”, đúng | Không tự nghiêng nội tâm, đúng | Chờ lệnh khác quân dự bị |
| YS-LN02/Text/part0030.xhtml/p000343 | Đạt: nút đường sắt, tốc độ, ba tầng cấp trên | “Mình”, “chúng ta” đúng phạm vi | Chỉ nghiêng chỉ thị, đúng | Chiến trường trong ngoặc, Arene/Đế quốc tạm |
| YS-LN02/Text/part0030.xhtml/p000344 | Đạt: hiểu theo cách riêng và so sánh đàn áp | “Nó” trong trần thuật, đúng | Không nghiêng, đúng | Mùa xuân Praha tạm; không thêm lịch sử |
| YS-LN02/Text/part0030.xhtml/p000345 | Đạt: có vẻ, quy mô tiểu đoàn, pháo binh; xe tăng là ví von pháp sư | Trần thuật đánh giá tình hình | Không nghiêng, đúng | Dân quân tạm giữ; không thêm xe tăng thật |
| YS-LN02/Text/part0030.xhtml/p000346 | Đạt: điều kiện, chán, nhưng tiếp tế khiến nhiệm vụ quan trọng | Tanya/nó, đúng | Không nghiêng, đúng | Không giảm mức nguy hiểm tiếp tế |
| YS-LN02/Text/part0030.xhtml/p000347 | Đạt: vì ngạc nhiên nên kiểm tra nhiều lần | “Nó”, sĩ quan tiền tuyến, đúng | Không nghiêng, đúng | Tư lệnh quân đoàn tạm giữ, không đoán cấp bậc |
| YS-LN02/Text/part0030.xhtml/p000348 | Đạt: gần bật cười, cơ hội rời tiền tuyến | Trần thuật rồi nội tâm, giữ ranh giới | Chỉ hai câu nội tâm nghiêng, đúng | Không thêm tính chắc chắn |
| YS-LN02/Text/part0030.xhtml/p000349 | Đạt: chạy tới sở chỉ huy để chuẩn bị cách đây chưa lâu | “Nó”, đúng | Không nghiêng, đúng | Sở chỉ huy tiểu đoàn tạm |
| YS-LN02/Text/part0030.xhtml/p000350 | Giữ thắc mắc và ám chỉ; thu hẹp bắn phá thành thả bom, F03 | “Mình”; pháp lý là tự đánh giá | Không nghiêng, đúng | Oanh kích không phân biệt mục tiêu tạm |
| YS-LN02/Text/part0030.xhtml/p000351 | Đạt: điều kiện không đầu hàng, bật suy nghĩ và khả năng bị lịch sử lên án | Xen nội tâm/chúng ta với Tanya/nó, đúng | Không nghiêng, đúng | WTO giữ nguyên; chú thích 20 thiếu nội dung, ghi rủi ro |
| YS-LN02/Text/part0030.xhtml/p000352 | Đạt: phá đá tối đa để lộ phần dễ cháy, đánh giá quân sự | Giọng phân tích, không thêm đạo đức | Không nghiêng, đúng | Công thức gây nổ tạm; khác thuốc nổ mạnh |
| YS-LN02/Text/part0030.xhtml/p000353 | Đạt: tự sửa suy đoán bom cháy sang đạn pháo, điều kiện tập trung hỏa lực | Câu hỏi suy tính, không biến thành lệnh | Không nghiêng, đúng | Dresden/Lục quân/đạn hẹn giờ tạm, không thêm cơ chế |
| YS-LN02/Text/part0030.xhtml/p000354 | Giữ thảm sát và tiền lệ; câu kết cứng, F07 | Lời tự trấn an, không phải phán quyết | Nhấn hẹp, đúng; đề nghị từ Việt rõ hơn | Ném bom rải thảm tạm giữ |
| YS-LN02/Text/part0030.xhtml/p000355 | Đối lập chính đạt; “kết án” quá cụ thể và “xướng tên thành” cứng, F04 | “Mình”, nỗi lo tự bảo toàn | Không nghiêng, đúng | Vùng xám/lên án/quy là đều tạm |
| YS-LN02/Text/part0030.xhtml/p000356 | Đạt: chỉ nếu thua; giả sử không thua; từ chối lúc này sẽ bị bắn | “Mình/chúng ta”, đúng | Không nghiêng, đúng | Bất tuân/bỏ chạy không thêm danh tội mới |
| YS-LN02/Text/part0030.xhtml/p000357 | Đạt: lúc này, không có căn cứ từ chối, có thể không còn thời gian | Tự bào chữa của “mình”, không khái quát khách quan | Không nghiêng, đúng | Không cần sửa thuật ngữ |
| YS-LN02/Text/part0030.xhtml/p000358 | Đạt: hồi tố, cần nhân đạo, bị buộc tội sau này, giả vờ tử tế | Độc thoại tự bảo toàn; giữ hai câu hỏi | Không nghiêng, đúng | Tòa án Quân sự Viễn Đông tạm giữ |

## Khuyến nghị thuật ngữ tạm

Tất cả mục sau có trạng thái **pending / provisional_non_canon**. Coordinator ghi lựa chọn và bất định vào ledger/handoff; reviewer không sửa những file đó.

| Term / ID áp dụng | Phương án tạm ưu tiên | Phương án khác | Lý do và bất định |
|---|---|---|---|
| die is cast — p000332–p000333 | Xúc xắc đã gieo / con xúc xắc | Sự đã rồi / quyết định ấy; ván đã đóng thuyền / ván cược ấy | Giữ liên kết hình ảnh hai đoạn, F02. Chắc về liên kết; vừa về độ tự nhiên. |
| WTO — p000351 | Giữ WTO, không khai triển | “WTO, bên đã...” để giảm lặp “tổ chức”; diễn đạt bằng “họ” chỉ sau khi đã nêu WTO | Package không cung cấp định danh hay nội dung chú thích 20. Chắc về giữ viết tắt, bất định cao về tên đầy đủ. Không tự thay bằng tổ chức khác. |
| explosion formulas — p000352 | Công thức gây nổ | Thuật thức gây nổ; công thức phát nổ | Giữ cách literal đang dùng, phân biệt với thuốc nổ mạnh. Bất định vừa về cơ chế; “thuật thức” có thể hợp vai pháp sư nhưng package chưa xác lập. Không chọn “công thức thuốc nổ”, vì dễ biến thành công thức pha chế cùng loại vật liệu đứng trước. |
| carpet-bombing — p000354 | Ném bom rải thảm | Oanh tạc rải thảm | Diễn đạt rõ thủ đoạn được thay bằng pháo binh. Bất định thấp về nghĩa tại đây, vẫn chưa canon. |
| Military Tribunal for the Far East — p000358 | Tòa án Quân sự Viễn Đông | Tòa án Quân sự vùng Viễn Đông | Giữ cấu tạo tên trong package. Bất định thấp về nghĩa literal, vừa về danh xưng chuẩn; không thêm “Quốc tế”, địa điểm hay định danh lịch sử ngoài nguồn được giao. |
| bombardment — p000350 | Oanh kích chiến lược không phân biệt mục tiêu | Bắn phá chiến lược không phân biệt mục tiêu | Bao quát khả năng dùng pháo binh, F03; bất định vừa về lựa chọn từ Việt. |
| militia — p000345 | Dân quân / lực lượng dân quân | Đội dân quân | Kế thừa lựa chọn chương 6 trong ledger; quy mô cấp tiểu đoàn khác danh nghĩa một tiểu đoàn chính quy. Bất định thấp tại đây. |
| army corps commander — p000347 | Tư lệnh quân đoàn | Chỉ huy quân đoàn | Kế thừa lựa chọn tạm chương 6; không thêm quân hàm cá nhân. Bất định thấp về cấp đơn vị. |
| Prague Spring — p000344, p000351 | Mùa xuân Praha | Mùa xuân Prague | Giữ nhất quán bản dịch; package chỉ đủ cho so sánh của nhân vật, không cho chú giải lịch sử. Bất định thấp về đối tượng, vừa về quy ước tên Việt chưa canon. |
| Magic Major — p000340 | Thiếu tá Pháp sư | Thiếu tá pháp sư | Chuyển tải quân hàm và vai trò, chỉ khác quy ước viết hoa. Bất định vừa về chuẩn danh xưng chưa chốt; không biến thành chức vụ chỉ huy cụ thể. |
| Tanya narration/self-reference — p000342–p000358 khi tương ứng | Nó trong trần thuật, mình trong tự quy chiếu | Dùng Tanya thay đại từ nếu cần rõ chủ thể | Đây là áp dụng DEC-P01-001, không đề xuất canon mới; không dùng cho lời hướng đến Tanya ở p000341. |
| you — p000339, p000341 | Tạm giữ cậu trong thoại và cô trong nội tâm hướng đến Tanya | Bỏ xưng hô p339; dùng “Thiếu tá” p341 | Package không xác lập quan hệ hay người nói bằng tên. Không đủ căn cứ để kết luận bản hiện tại sai; ưu tiên cách trung tính nếu coordinator muốn giảm suy diễn. Bất định vừa. |
| humane / nice — p000358 | Hành xử nhân đạo / giả vờ tử tế | Đối xử nhân đạo / ra vẻ tử tế | Phân biệt yêu cầu hành xử với vẻ ngoài để tránh cáo buộc. Bản hiện tại giữ đúng sắc thái tự bảo toàn, không cần thay. Bất định thấp trong package. |

## Đánh giá self-check và rủi ro còn lại

- **p000333:** Self-check đã nhận diện việc thay hình ảnh bằng “kết cục”; rủi ro này có căn cứ và cần xử lý cùng p000332 (F02).
- **p000355:** Self-check giữ được đối lập bên thắng/bên thua nhưng diễn giải thành “kết án” quá cụ thể. Dùng cách trung tính nêu ở F04; còn bất định về cụm khó hiểu, không cần dừng chờ thuật ngữ.
- **p000351:** Giữ WTO là đúng giới hạn. Package có mốc chú thích 20 nhưng không có nội dung; bản dịch không giữ mốc này. Ghi là rủi ro truy vết chú thích cho coordinator vì canon chưa quy định cách xuất chú thích. Không mở mục chú thích ngoài package, không tự bổ sung giải nghĩa, không tính là lỗi nghĩa đã xác minh.
- **p000352:** “Công thức gây nổ” chấp nhận tạm; “công thức thuốc nổ” trong self-check là phương án kém ưu tiên vì có thể nhập hai phương tiện làm một. Không khẳng định lore/cơ chế phép thuật từ tên term.
- **p000358:** “Hành xử nhân đạo” phù hợp trong mạch tự bảo toàn và vẫn đối lập với “giả vờ tử tế”. Không thấy lỗi cần sửa; nhận định về hồi tố vẫn là suy luận của Tanya.
- **Điểm nhìn:** Giữ “nó” trong trần thuật về Tanya và “mình” ở tự quy chiếu; không ép cậu/cô thành nó. Không xác nhận danh tính người nói ở đầu package từ ngữ cảnh ngoài phạm vi.
- **Nhấn mạnh:** Tất cả vị trí nghiêng khớp phạm vi XHTML; F07 chỉ đề nghị diễn đạt từ mang nhấn mạnh rõ hơn. Không thêm nghiêng cho p000342 hoặc p000350–p000358 chỉ vì là độc thoại.
- **Trạng thái xử lý:** Review hoàn tất, bản dịch cần sửa bốn phát hiện vừa và cân nhắc ba phát hiện nhẹ. Không có lỗi nghiêm trọng được xác minh; không sign-off, không nâng thuật ngữ thành canon, không commit.

