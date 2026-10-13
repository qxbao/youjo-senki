# Review — vol-02-ch-05-b16

```yaml
role: reviewer
task_id: vol-02-ch-05-b16-review
state: done
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000383
  - YS-LN02/Text/part0026.xhtml/p000384
  - YS-LN02/Text/part0026.xhtml/p000385
  - YS-LN02/Text/part0026.xhtml/p000386
  - YS-LN02/Text/part0026.xhtml/p000387
  - YS-LN02/Text/part0026.xhtml/p000388
  - YS-LN02/Text/part0026.xhtml/p000389
  - YS-LN02/Text/part0026.xhtml/p000390
  - YS-LN02/Text/part0026.xhtml/p000391
  - YS-LN02/Text/part0026.xhtml/p000392
  - YS-LN02/Text/part0026.xhtml/p000393
  - YS-LN02/Text/part0026.xhtml/p000394
  - YS-LN02/Text/part0026.xhtml/p000395
  - YS-LN02/Text/part0026.xhtml/p000396
  - YS-LN02/Text/part0026.xhtml/p000397
  - YS-LN02/Text/part0026.xhtml/p000398
  - YS-LN02/Text/part0026.xhtml/p000399
  - YS-LN02/Text/part0026.xhtml/p000400
  - YS-LN02/Text/part0026.xhtml/p000401
  - YS-LN02/Text/part0026.xhtml/p000402
  - YS-LN02/Text/part0026.xhtml/p000403
files_written: [reviews/prose/vol-02/ch-05-b16-codex.md]
review_path: reviews/prose/vol-02/ch-05-b16-codex.md
counts:
  reviewed_segments: 21
  serious: 0
  moderate: 5
  minor: 3
  unresolved_findings: 8
package_hash_verification:
  algorithm: sha256
  expected: d1c4792e7a846a626620b61d23c7310e956ee283e703192a41c83fcb5fd24c22
  actual: d1c4792e7a846a626620b61d23c7310e956ee283e703192a41c83fcb5fd24c22
  result: pass
  source_units: 21
  translation_units: 21
  segment_order: pass
  source_translation_ids_match: true
  contiguous_range: p000383-p000403
validator: not_run
diff_check: not_run
findings:
  - id: F01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000388
    related_segment_ids: [YS-LN02/Text/part0026.xhtml/p000389, YS-LN02/Text/part0026.xhtml/p000394, YS-LN02/Text/part0026.xhtml/p000395, YS-LN02/Text/part0026.xhtml/p000397]
    issue: Giọng trần thuật về Tanya chuyển giữa mình, nó và cô mà không có căn cứ thay đổi quy ước.
    evidence: Câu mở p000388 là trần thuật ngôi ba nhưng dùng mình; phần dẫn suy nghĩ và trần thuật tiếp theo ở các đoạn liên quan dùng cô. Ledger LN02 đề xuất nó hoặc lặp tên/lược chủ ngữ; DEC-P01-001 giới hạn mình ở nội tâm tự quy chiếu.
    resolution: Đề xuất tạm dùng Tanya/lược chủ ngữ hoặc nó ở trần thuật; giữ mình trong nội tâm. Không tự đổi cô trong lời thoại p000387/p000391, vốn là xưng hô riêng.
  - id: F02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000394
    issue: Đổi người thực hiện việc trao đổi với chỉ huy tân binh.
    evidence: Hai hành động chuẩn bị và trao đổi cùng phụ thuộc vào cấu trúc sai khiến với các đại đội trưởng; bản dịch gán hành động thứ hai cho Tanya.
    resolution: Đề xuất giao cho các đại đội trưởng dưới quyền chuẩn bị đánh đêm và trao đổi với người chỉ huy nhóm tân binh.
  - id: F03
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000395
    issue: Khổ hẹp xác định thêm thông số đường ray mà package không nêu rõ.
    evidence: light railway chỉ được mô tả về tải vận chuyển; package không cho khổ đường ray. Không đủ chứng cứ để xem hai tên gọi là tương đương chắc chắn.
    resolution: Tạm dùng đường sắt nhẹ, giữ ý gần hết công suất; khổ hẹp là phương án thay thế chờ căn cứ.
  - id: F04
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000398
    related_segment_ids: [YS-LN02/Text/part0026.xhtml/p000401]
    issue: Công thức gây nhiễu không kế thừa đề xuất đã có cho chính thuật ngữ này.
    evidence: Ledger vol02-ch02-b11-interference-formulas dùng thuật thức gây nhiễu; nhiều mục formula sau đó giữ gốc thuật thức. Ledger cũng có công thức ở ch05-b03, nên đây là bất nhất trong các đề xuất, không phải vi phạm một thuật ngữ canon.
    resolution: Ưu tiên tạm thuật thức gây nhiễu ở cả hai đoạn; coordinator ghi lựa chọn và bất nhất ledger. Không suy thêm loại nhiễu hoặc cơ chế liên lạc.
  - id: F05
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000401
    issue: Vế cả khu vực sẽ bị pháo kích có thể bị đọc như kết quả chắc chắn.
    evidence: Khả thể trong nguồn bao trùm cả việc địch rút lui và toàn khu vực bị oanh kích, không chỉ việc rút lui.
    resolution: Đề xuất có thể xảy ra chuyện đối phương rút lui rồi cả khu vực bị oanh kích bừa bãi; tránh sẽ độc lập. Oanh kích giữ độ mở về phương tiện hơn pháo kích khi package không xác định loại vũ khí.
  - id: F06
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000402
    issue: Cứ đón hỏa lực súng máy kiềm chế tối nghĩa và làm nhẹ sắc thái phải chịu hỏa lực đối phương.
    evidence: Trong chuỗi giả định p000401-p000403, đây là một nguy cơ thay thế cho oanh kích; take chỉ phía nhận/chịu hỏa lực. checking bổ nghĩa chức năng ngăn chặn của hỏa lực, không phải hành động kiểm tra súng.
    resolution: Đề xuất À, hoặc ta có thể chỉ phải hứng hỏa lực ngăn chặn của súng máy. Giữ khả thể và giọng tự cân nhắc ngắn, không thêm ý chủ động chấp nhận tổn thất.
  - id: F07
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000391
    issue: Lược số nhiều của phía đang trông cậy vào Tanya.
    evidence: Chủ thể nguồn là số nhiều; bản dịch bỏ chủ thể ngay sau câu người nói tự xưng tôi, dễ khiến lời trông cậy bị hiểu là cá nhân.
    resolution: Đề xuất nhưng chúng tôi trông cậy vào cô đấy; không suy thành tên một cơ quan.
  - id: F08
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000403
    issue: Bốn hướng thay cho bốn địa điểm làm hẹp mô tả bố trí tấn công.
    evidence: Nguồn xác định vị trí khác nhau, không xác định hướng hoặc phương vị.
    resolution: Đề xuất tấn công từ bốn vị trí hoàn toàn khác nhau; giữ đủ nghi binh, bốn đại đội và việc không còn lực lượng dự bị.
unresolved_findings: [F01, F02, F03, F04, F05, F06, F07, F08]
pending_terms:
  - source_term: interference formulas
    proposed_vi: thuật thức gây nhiễu
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000398, YS-LN02/Text/part0026.xhtml/p000401]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: light railway
    proposed_vi: đường sắt nhẹ
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000395]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: batman
    proposed_vi: lính hầu
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000394]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: checking machine-gun fire
    proposed_vi: hỏa lực ngăn chặn của súng máy
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000402]
    volume: vol-02
    chapter: 5
    status: pending
term_recommendations:
  - source_term: interference formulas
    proposed_vi: thuật thức gây nhiễu
    alternatives_vi: [công thức gây nhiễu, thuật thức giao thoa]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000398, YS-LN02/Text/part0026.xhtml/p000401]
    status: pending
    confidence: 0.65
    rationale: Kế thừa đề xuất cho cùng cụm ở ledger; gây nhiễu giữ nghĩa chức năng trực tiếp. Chưa đủ căn cứ cho cơ chế giao thoa cụ thể.
  - source_term: light railway
    proposed_vi: đường sắt nhẹ
    alternatives_vi: [đường sắt khổ hẹp]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000395]
    status: pending
    confidence: 0.55
    rationale: Literal ít bổ sung nhất khi chỉ có ngữ cảnh vận tải; khổ hẹp có thể phù hợp nhưng chưa được package chứng minh.
  - source_term: batman
    proposed_vi: lính hầu
    alternatives_vi: [quân hầu, lính phục vụ sĩ quan]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000394]
    status: pending
    confidence: 0.75
    rationale: Vai trò phục vụ cá nhân trong quân đội phù hợp cảnh bữa ăn; không nâng thành sĩ quan tùy tùng hay phó quan.
  - source_term: checking machine-gun fire
    proposed_vi: hỏa lực ngăn chặn của súng máy
    alternatives_vi: [hỏa lực kiềm chế của súng máy, hỏa lực súng máy nhằm cản bước]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000402]
    status: pending
    confidence: 0.65
    rationale: Chọn nghĩa ngăn/cản theo cấu trúc và chuỗi nguy cơ chiến thuật; không tự gán một học thuyết hỏa lực. Không chọn khai hỏa súng máy để kiểm tra vì đảo phía chịu hỏa lực thành phía bắn; bắn áp chế là cách đọc chuyên biệt hơn chưa đủ căn cứ.
  - source_term: instructor unit
    proposed_vi: đơn vị huấn luyện
    alternatives_vi: [đơn vị phụ trách huấn luyện]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000388]
    status: pending
    confidence: 0.75
    rationale: Giữ lựa chọn chức năng hiện có ở ch05-b10/b12, không đặt thêm cấp tổ chức.
  - source_term: new recruits / fresh recruits
    proposed_vi: tân binh
    alternatives_vi: [lính mới]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000388, YS-LN02/Text/part0026.xhtml/p000394, YS-LN02/Text/part0026.xhtml/p000398]
    status: pending
    confidence: 0.8
    rationale: Giữ đúng người mới và nhất quán ledger; lính mới phù hợp giọng nội tâm p000386, không đồng nhất mọi quân thay thế với tân binh.
  - source_term: no-man’s-land
    proposed_vi: vùng đất giữa hai chiến tuyến
    alternatives_vi: [vùng đất trống giữa hai chiến tuyến]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000398]
    status: pending
    confidence: 0.8
    rationale: Kế thừa đề xuất ch05-b13; có thể viết ngay giữa vùng đất giữa hai chiến tuyến để tránh lặp giữa trong cùng cấu trúc.
risks:
  - Các lựa chọn trên đều tạm thời, không nâng thành canon; không cần dừng chờ quyết định thuật ngữ.
  - Nghĩa chuyên biệt của checking còn bất định; lựa chọn ngăn chặn đủ dùng trong phạm vi package, không xác nhận lore hoặc học thuyết quân sự.
commit: null
next_action: coordinator_accept_report_then_translator_revision
```

Đã đọc shared/reviewer, config, cả hai handoff, package được giao, toàn bộ bản dịch và self-check, các tệp canon và các mục ledger liên quan. Chỉ đọc nguồn trong package cục bộ; không mở EPUB/PDF, không tra cứu hay truyền nguồn ra ngoài. Kiểm tra hash và thứ tự là kiểm tra đầu vào riêng, không phải chạy validator hoặc diff-check của pipeline.

Đã đối chiếu toàn bộ 21 đoạn về nghĩa, văn phong, giọng, thuật ngữ và nhấn mạnh. p000383–p000387 giữ lập luận kinh nghiệm/huấn luyện và sự tự trách; p000384 có thể trau chuốt lời đáp nhưng không có lỗi đáng yêu cầu sửa. p000388–p000390 giữ đủ ba vùng nhấn mạnh ở p000388 và một vùng ở p000389; p000390 không có nhấn mạnh trong nguồn và bản dịch cũng không thêm. “Ảo tưởng mục nát” hơi gượng nhưng giữ được hình ảnh cùng sắc thái tiêu cực, không phải lỗi nghĩa bắt buộc sửa. p000389 giữ câu hỏi phản đối chưa nói thành lời và sự tự nhận ra hấp tấp/thiển cận.

p000390–p000393 giữ tương phản giữa lời nhận nhiệm vụ và hai cách nhìn mâu thuẫn; sửa số nhiều ở p000391 theo F07. p000394–p000397 giữ mạch thực phẩm, tải vận chuyển, định mức năng lượng và lời mỉa mai về khẩu phần tàu ngầm; các điểm cần sửa là F01–F03. p000398–p000403 giữ nguy cơ lộ vị trí, thiếu vô tuyến cá nhân, so sánh hỏa lực, khả năng hỗn loạn, bố trí bốn đại đội và động cơ muốn ở hậu phương. Các câu giả định cần xử lý F05–F06. Tên Eagle Claw/Iran được giữ nguyên; không thêm kiến thức lịch sử ngoài package. Phạm vi batch không có quân hàm cần quyết định mới.

Self-check đúng về số đoạn và nhấn mạnh nhưng chưa nhận ra các vấn đề chủ thể, giọng trần thuật và phạm vi khả thể nêu trên. Báo cáo hoàn tất; tám finding vẫn mở vì reviewer không sửa bản dịch.
