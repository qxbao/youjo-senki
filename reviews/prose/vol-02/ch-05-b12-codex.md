# Review — vol-02-ch-05-b12

## Phạm vi và đối chiếu đầu vào

Đã đọc agents/shared.md, agents/reviewer.md, config/translation-pipeline.yml, handoff, source package được giao, năm tệp canon, ledger pending, bản dịch và semantic self-check. Chỉ rà 29 đoạn p000284–p000312 của batch này. Không mở EPUB/PDF, không dùng dịch vụ ngoài để tra nguồn.

SHA-256 của source package: `cb717af0caf5d3b156dbdd48c71741359a4cdf815be6138462682897ed579509`, khớp `source_package_sha256` trong handoff. Đã đối chiếu mã đoạn và nội dung tại chỗ; đây không phải lượt chạy validator hay diff-check.

## Findings còn mở

### F01

- segment_id: `YS-LN02/Text/part0026.xhtml/p000296`
- severity: serious
- issue: Biến việc các sĩ quan cấp trên tử trận/được điều đi thành sự lo ngại về những khả năng ấy.
- evidence/reasoning: Nguồn mô tả các sĩ quan cấp trên có mặt lúc Tanya đến đang lần lượt được truy thăng sau khi chết hoặc, nếu may mắn, được điều chuyển/đưa về hậu phương. Bản dịch thêm “đang lo chuyện”, khiến những biến động nhân sự thực tế thành tâm trạng dự phòng. Điều này làm mất nguyên nhân trực tiếp khiến Tanya bất ngờ ở gần đỉnh cơ cấu chỉ huy tại p000297. Self-check khẳng định giữ logic tổn thất và truy thăng nhưng chưa phát hiện sai lệch này.
- recommended correction: “Mình chỉ là Thiếu tá, nhưng các sĩ quan cấp trên có mặt ở đây khi mình mới đến đều lần lượt được truy thăng hai cấp sau khi chết, hoặc nếu may mắn thì được điều chuyển hay đưa về hậu phương.” Giữ giọng mỉa mai; không thêm số người chết hoặc nguyên nhân điều chuyển.
- resolution: unresolved

### F02

- segment_id: `YS-LN02/Text/part0026.xhtml/p000286`
- related_segment_ids: `YS-LN02/Text/part0026.xhtml/p000288`, `YS-LN02/Text/part0026.xhtml/p000289`, `YS-LN02/Text/part0026.xhtml/p000294`
- severity: moderate
- issue: Đại từ nội tâm và đại từ trần thuật về Tanya chưa nhất quán với lựa chọn đang dùng trong dự án.
- evidence/reasoning: p000286 dùng “tôi tưởng” trong nhận xét ngôi thứ nhất, trong khi p000284, p000292 và các đoạn nội tâm sau dùng “mình”. p000288–p000289 và p000294 dùng “cô” ở trần thuật. DEC-P01-001 giới hạn quyết định theo giai đoạn, nên không tự tuyên bố “nó” là canon cho mọi LN02; tuy vậy ledger đã đề xuất tiếp tục “nó”/lặp tên/lược chủ ngữ cho trần thuật LN02 và “mình” cho nội tâm. Batch không đưa căn cứ cho việc đổi giọng này. Self-check nói đã giữ “mình” nhưng bỏ sót p000286.
- recommended correction: Đổi “tôi tưởng” thành “mình tưởng” tại p000286; tạm dùng “nó”, hoặc lặp Tanya/lược chủ ngữ khi thuận câu, thay “cô” ở ba đoạn liên quan. Giữ “tôi” trong lời thoại của Tanya. Lựa chọn áp dụng cho LN02 vẫn là đề xuất tạm theo ledger.
- resolution: unresolved

### F03

- segment_id: `YS-LN02/Text/part0026.xhtml/p000292`
- severity: moderate
- issue: “Cục Nghiên cứu Kỹ thuật” tự xác định cấp tổ chức chưa được nguồn batch chứng minh.
- evidence/reasoning: Định danh ngắn Tech Research cho biết chức năng nghiên cứu kỹ thuật, không xác lập đơn vị ở cấp cục. Ledger và self-check đều thừa nhận chưa rõ cấp tổ chức. Đây là thông tin thêm cụ thể, không chỉ là việc thuật ngữ còn pending.
- recommended correction: Tạm dùng “bộ phận nghiên cứu kỹ thuật” trong câu này; phương án giữ định danh là “Nghiên cứu Kỹ thuật”. Không thêm cấp tổ chức hoặc nâng thành canon.
- resolution: unresolved

### F04

- segment_id: `YS-LN02/Text/part0026.xhtml/p000290`
- severity: minor
- issue: “Làm bia cho cối xay thịt” trộn hai hình ảnh, khiến ẩn dụ thịt kém tự nhiên.
- evidence/reasoning: Hình ảnh nguồn là tân binh làm nguyên liệu cho cối xay thịt, tiếp nối khối thịt tươi, băm thịt và bít tết. “Bia” thuộc hình ảnh mục tiêu bị bắn, không kết hợp tự nhiên với cối xay. Phần “nhào nặn”/bít tết trong self-check vẫn giữ được ý giễu cợt; vấn đề nằm ở cụm trước đó.
- recommended correction: Đổi thành “chỉ có ích làm nguyên liệu cho cối xay thịt”. Giữ phạm vi chữ nghiêng của hai mệnh lệnh cuối đoạn.
- resolution: unresolved

### F05

- segment_id: `YS-LN02/Text/part0026.xhtml/p000294`
- severity: minor
- issue: Đổi lời nhận ra nguyên nhân của nhiệm vụ huấn luyện thành câu hỏi tu từ.
- evidence/reasoning: Cuối đoạn nguồn khẳng định sau khi nghĩ lại, chính tình trạng tân binh ấy giải thích vì sao nhiệm vụ huấn luyện được đặt ra. “Chẳng phải … sao?” làm thay đổi hình thức và độ trực tiếp của kết luận dù vẫn có thể hiểu đúng ý.
- recommended correction: “Nhưng nghĩ lại, chính vì thế mà có người nghĩ ra nhiệm vụ huấn luyện này để biến họ thành một lực lượng chiến đấu đúng nghĩa.”
- resolution: unresolved

### F06

- segment_id: `YS-LN02/Text/part0026.xhtml/p000293`
- severity: minor
- issue: “Nói đúng hơn” biến dấu hiệu nói ví von thành lời đính chính chính xác hơn.
- evidence/reasoning: Nguồn dùng dấu hiệu chỉ cách nói hình tượng khi gọi Rhine là nghĩa địa. Bản dịch lại đặt nghĩa địa như một nhận định chính xác hơn địa ngục. Cần giữ sắc thái ví von trong lời cảnh báo.
- recommended correction: “Như các anh biết, Rhine là địa ngục. Có thể ví nó như một nghĩa địa.”
- resolution: unresolved

### F07

- segment_id: `YS-LN02/Text/part0026.xhtml/p000310`
- severity: minor
- issue: “Cực kỳ rẻ để sản xuất hàng loạt” làm mờ quan hệ chi phí chế tạo thấp dẫn đến phù hợp sản xuất hàng loạt.
- evidence/reasoning: Nguồn nêu riêng đặc tính chế tạo rất rẻ, rồi suy ra sự phù hợp với sản xuất đại trà. Cụm hiện tại vừa gượng tiếng Việt vừa gộp hai ý thành chi phí của riêng việc sản xuất hàng loạt.
- recommended correction: “Hơn nữa, chi phí chế tạo xẻng cực kỳ thấp nên rất thích hợp để sản xuất hàng loạt.” Các so sánh trước đó và mức lo ngại về tâm trí cần được giữ nguyên về nghĩa; không suy diễn cơ chế gây hại.
- resolution: unresolved

### F08

- segment_id: `YS-LN02/Text/part0026.xhtml/p000312`
- severity: minor
- issue: “Không để lộ tung tích” mở rộng tính bí mật lúc hạ sát thành việc không để lại dấu vết/không bị truy ra.
- evidence/reasoning: Nguồn nói ưu thế hạ sát lén lút của công cụ không dựa vào ma thuật, với đối tượng lệ thuộc dò quét ma thuật. Nguồn không bảo đảm việc che giấu tung tích sau hành động.
- recommended correction: “Trên hết, nó không phụ thuộc vào ma thuật nên rất lý tưởng để lặng lẽ hạ sát.” Giữ lời “giáo dục” giễu cợt và chữ nghiêng của tiếng động.
- resolution: unresolved

## Nhận xét về self-check và phần đã đạt

Hai phạm vi nhấn mạnh ở p000290 và p000312 khớp XHTML theo DEC-P01-002. Quan hệ giữa xử lý nhanh của Bộ chỉ huy và dự cảm rắc rối ở p000286–p000287 được giữ. Các câu hỏi về Darwin ở p000298 vẫn giữ hai khả năng và đối tượng lập luận; không có lỗi actionable riêng cho phần đó. Hình ảnh tán tụng xẻng cùng giọng mỉa mai nhìn chung được chuyển rõ.

Chấp nhận tạm quân hàm và tên mẫu được self-check đề xuất, với giới hạn non-canon. Không coi sự chưa chắc chắn thông thường của các tên/thuật ngữ ấy là lý do dừng. F01 là lỗi nghĩa nghiêm trọng còn mở nên cần coordinator giao translator sửa trước khi xét thông qua batch; reviewer dừng sau báo cáo.

## YAML báo cáo

```yaml
role: reviewer
task_id: vol-02-ch-05-b12
state: done
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000284
  - YS-LN02/Text/part0026.xhtml/p000285
  - YS-LN02/Text/part0026.xhtml/p000286
  - YS-LN02/Text/part0026.xhtml/p000287
  - YS-LN02/Text/part0026.xhtml/p000288
  - YS-LN02/Text/part0026.xhtml/p000289
  - YS-LN02/Text/part0026.xhtml/p000290
  - YS-LN02/Text/part0026.xhtml/p000291
  - YS-LN02/Text/part0026.xhtml/p000292
  - YS-LN02/Text/part0026.xhtml/p000293
  - YS-LN02/Text/part0026.xhtml/p000294
  - YS-LN02/Text/part0026.xhtml/p000295
  - YS-LN02/Text/part0026.xhtml/p000296
  - YS-LN02/Text/part0026.xhtml/p000297
  - YS-LN02/Text/part0026.xhtml/p000298
  - YS-LN02/Text/part0026.xhtml/p000299
  - YS-LN02/Text/part0026.xhtml/p000300
  - YS-LN02/Text/part0026.xhtml/p000301
  - YS-LN02/Text/part0026.xhtml/p000302
  - YS-LN02/Text/part0026.xhtml/p000303
  - YS-LN02/Text/part0026.xhtml/p000304
  - YS-LN02/Text/part0026.xhtml/p000305
  - YS-LN02/Text/part0026.xhtml/p000306
  - YS-LN02/Text/part0026.xhtml/p000307
  - YS-LN02/Text/part0026.xhtml/p000308
  - YS-LN02/Text/part0026.xhtml/p000309
  - YS-LN02/Text/part0026.xhtml/p000310
  - YS-LN02/Text/part0026.xhtml/p000311
  - YS-LN02/Text/part0026.xhtml/p000312
files_written:
  - reviews/prose/vol-02/ch-05-b12-codex.md
review_path: reviews/prose/vol-02/ch-05-b12-codex.md
source_package_hash: pass
counts: {serious: 1, moderate: 2, minor: 5}
unresolved_findings:
  serious: 1
  moderate: 2
  minor: 5
  serious_or_moderate: 3
  ids: [F01, F02, F03, F04, F05, F06, F07, F08]
findings:
  - {id: F01, severity: serious, segment_id: YS-LN02/Text/part0026.xhtml/p000296, issue: Biến biến động nhân sự thực tế thành lo ngại, resolution: unresolved}
  - {id: F02, severity: moderate, segment_id: YS-LN02/Text/part0026.xhtml/p000286, issue: Đại từ nội tâm và trần thuật chưa nhất quán, resolution: unresolved}
  - {id: F03, severity: moderate, segment_id: YS-LN02/Text/part0026.xhtml/p000292, issue: Tự xác định cấp cục cho Tech Research, resolution: unresolved}
  - {id: F04, severity: minor, segment_id: YS-LN02/Text/part0026.xhtml/p000290, issue: Kết hợp hình ảnh bia và cối xay thịt, resolution: unresolved}
  - {id: F05, severity: minor, segment_id: YS-LN02/Text/part0026.xhtml/p000294, issue: Đổi kết luận thành câu hỏi tu từ, resolution: unresolved}
  - {id: F06, severity: minor, segment_id: YS-LN02/Text/part0026.xhtml/p000293, issue: Đổi sắc thái ví von thành đính chính, resolution: unresolved}
  - {id: F07, severity: minor, segment_id: YS-LN02/Text/part0026.xhtml/p000310, issue: Mờ quan hệ chi phí thấp và sản xuất hàng loạt, resolution: unresolved}
  - {id: F08, severity: minor, segment_id: YS-LN02/Text/part0026.xhtml/p000312, issue: Mở rộng hạ sát lén lút thành che giấu tung tích, resolution: unresolved}
pending_terms: []
term_recommendations:
  - source_term: Magic Major / major
    proposed_vi: Thiếu tá Pháp sư / Thiếu tá
    alternative_vi: Thiếu tá ma thuật / Major
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000291, YS-LN02/Text/part0026.xhtml/p000296, YS-LN02/Text/part0026.xhtml/p000297]
    status: pending
    rationale: Tiếp tục ánh xạ Thiếu tá của b08 và đề xuất pháp sư trong ledger; cấu trúc danh xưng chưa canon, không coi phương án khác là lỗi tự thân.
  - source_term: Lieutenant Weiss
    proposed_vi: Trung úy Weiss
    alternative_vi: Sĩ quan cấp úy Weiss
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000289]
    status: pending
    rationale: Ledger đã có ánh xạ tạm riêng cho Weiss; giữ nhất quán, không suy cấp cụ thể chỉ từ từ Lieutenant ở đoạn này.
  - source_term: Tech Research
    proposed_vi: bộ phận nghiên cứu kỹ thuật
    alternative_vi: Nghiên cứu Kỹ thuật
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000292]
    status: pending
    rationale: Giữ chức năng được định danh nhưng tránh thêm cấp cục chưa xác nhận; phương án thay thế giữ tính tên gọi.
  - source_term: Central
    proposed_vi: Central
    alternative_vi: Trung ương
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000292]
    status: pending
    rationale: Ledger có đề xuất cạnh tranh; mục b12 giữ nguyên tên, và batch chưa xác lập đây là địa danh hay nhãn cơ quan. Tạm giữ để ít suy diễn.
  - source_term: Elinium Type 95
    proposed_vi: Elinium Type 95
    alternative_vi: Elinium loại 95
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000292]
    status: pending
    rationale: Giữ nguyên định danh mẫu theo ledger b12; không tự bổ sung loại thiết bị hoặc bản chất Elinium.
  - source_term: magic scanning
    proposed_vi: dò quét ma thuật
    alternative_vi: quét ma thuật
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000312]
    status: pending
    rationale: Phương án hiện tại diễn đạt rõ thao tác phát hiện trong ngữ cảnh lệ thuộc cảm nhận ma thuật, không thêm cơ chế; phương án ngắn cũng chấp nhận được.
  - source_term: instructor unit
    proposed_vi: đơn vị huấn luyện
    alternative_vi: đơn vị phụ trách huấn luyện
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000292]
    status: pending
    rationale: Giữ lựa chọn chức năng tạm của b10; không tự xác định biên chế hoặc cấp đơn vị.
  - source_term: Tanya third-person narration / interior self-reference
    proposed_vi: nó hoặc lặp Tanya/lược chủ ngữ ở trần thuật; mình ở nội tâm
    alternative_vi: Lặp Tanya/lược chủ ngữ ở trần thuật; giữ mình ở nội tâm
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000286, YS-LN02/Text/part0026.xhtml/p000288, YS-LN02/Text/part0026.xhtml/p000289, YS-LN02/Text/part0026.xhtml/p000294]
    status: pending
    rationale: Tiếp tục đề xuất giọng LN02 trong ledger, phân biệt với tôi trong thoại; không tự mở rộng phạm vi canon của DEC-P01-001.
risks:
  - F01 là lỗi serious còn mở; chưa thể thông qua batch trước khi sửa.
  - Các lựa chọn thuật ngữ và giọng LN02 vẫn là đề xuất tạm, không canon và không tự chặn vì bất định thông thường.
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_assign_translator_fixes
```
