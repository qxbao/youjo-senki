# Final signoff — vol-02-ch-05-b15

```yaml
role: reviewer
task_id: vol-02-ch-05-b15-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-05-b15-final-signoff-codex.md
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000358
  - YS-LN02/Text/part0026.xhtml/p000359
  - YS-LN02/Text/part0026.xhtml/p000360
  - YS-LN02/Text/part0026.xhtml/p000361
  - YS-LN02/Text/part0026.xhtml/p000362
  - YS-LN02/Text/part0026.xhtml/p000363
  - YS-LN02/Text/part0026.xhtml/p000364
  - YS-LN02/Text/part0026.xhtml/p000365
  - YS-LN02/Text/part0026.xhtml/p000366
  - YS-LN02/Text/part0026.xhtml/p000367
  - YS-LN02/Text/part0026.xhtml/p000368
  - YS-LN02/Text/part0026.xhtml/p000369
  - YS-LN02/Text/part0026.xhtml/p000370
  - YS-LN02/Text/part0026.xhtml/p000371
  - YS-LN02/Text/part0026.xhtml/p000372
  - YS-LN02/Text/part0026.xhtml/p000373
  - YS-LN02/Text/part0026.xhtml/p000374
  - YS-LN02/Text/part0026.xhtml/p000375
  - YS-LN02/Text/part0026.xhtml/p000376
  - YS-LN02/Text/part0026.xhtml/p000377
  - YS-LN02/Text/part0026.xhtml/p000378
  - YS-LN02/Text/part0026.xhtml/p000379
  - YS-LN02/Text/part0026.xhtml/p000380
  - YS-LN02/Text/part0026.xhtml/p000381
  - YS-LN02/Text/part0026.xhtml/p000382
files_written: [reviews/prose/vol-02/ch-05-b15-final-signoff-codex.md]
validator: not_run
diff_check: not_run
commit: null
source_sha256: 3ac53161b6e093ba07203f284a400049cf902a3b0f51c0d3e40200867c13ae0a
package_hash_verification:
  path: work/vol-02/batches/ch-05-b15-source.jsonl
  algorithm: sha256
  expected: 38531306e5839281ec705606edef8cc4ec8af3166a6d7c41ab76644b2870443a
  actual: 38531306e5839281ec705606edef8cc4ec8af3166a6d7c41ab76644b2870443a
  result: pass
  matches: [batch_handoff, review_handoff]
  embedded_source_hash_consistency: pass
  note: Hash nhúng khớp batch handoff và cả 25 dòng nguồn/bản dịch; không mở EPUB/PDF để tái tính hash sách.
segment_order_verification:
  result: pass
  source_count: 25
  translation_count: 25
  source_unique_ids: 25
  translation_unique_ids: 25
  exact_expected_order: true
  source_translation_order_match: true
  start: YS-LN02/Text/part0026.xhtml/p000358
  end: YS-LN02/Text/part0026.xhtml/p000382
  missing_ids: []
  extra_ids: []
counts:
  reviewed_segments: 25
  serious: 0
  moderate: 4
  minor: 6
  total_findings: 10
  resolved: 0
  unresolved: 10
  new_serious: 0
  new_moderate: 0
  new_minor: 0
signoff_status: changes_requested
signoff_reason: Bản dịch được giao vẫn chứa toàn bộ R01–R10; còn 4 lỗi vừa nên chưa đủ điều kiện duyệt. Self-check đã cập nhật nhưng không khớp nội dung translation thực tế.
resolved_findings: []
unresolved_findings: [R01, R02, R03, R04, R05, R06, R07, R08, R09, R10]
new_findings: []
findings:
  - id: R01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000358
    issue: Vẫn thêm thiết bị/âm thanh cảnh báo không có căn cứ.
    evidence: Translation vẫn dùng “những hồi còi báo động vang lên”; package chỉ xác định cảnh báo được đưa ra dễ dàng, không xác định còi.
    resolution: Bỏ chi tiết còi và âm thanh; dùng “những cảnh báo được đưa ra chỉ vì một chuyện cỏn con”.
    status: open
  - id: R02
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000361
    issue: Kết hợp từ khó đọc chưa được sửa.
    evidence: Translation vẫn kết câu bằng “thì đặc biệt khó chịu nổi”.
    resolution: Diễn đạt tự nhiên việc nhìn họ tác chiến khi không thể dựa vào phép thuật là rất khó chịu, chẳng hạn “thì thật khó mà chịu nổi”.
    status: open
  - id: R03
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000362
    issue: Chưa áp dụng cặp thuật ngữ tạm được coordinator chọn; hình ảnh lớp vỏ vẫn bị đổi thành kết giới.
    evidence: Translation vẫn dùng “màn chắn bảo hộ lẫn kết giới phòng thủ”; handoff sửa và nhóm reviewer trong ledger chọn màn bảo hộ / lớp vỏ phòng ngự.
    resolution: Dùng “màn bảo hộ” và “lớp vỏ phòng ngự” cho hai biện pháp riêng biệt; giữ trạng thái pending, không xác lập cơ chế.
    status: open
  - id: R04
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000364
    issue: Vẫn thiếu chữ nghiêng cho phần nhớ lại.
    evidence: XHTML có một phần em tương ứng lời chợt nhớ; translation không có dấu sao nào ở đoạn này.
    resolution: Bọc từ “À phải” qua dấu ba chấm cuối đoạn bằng *...*; câu trần thuật mở đầu nằm ngoài theo DEC-P01-002.
    status: open
  - id: R05
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000365
    issue: Vẫn thiếu chữ nghiêng cho kết luận nội tâm giữa đoạn.
    evidence: XHTML có một phần em cho lời nhận ra hậu quả nhân lên; translation không có dấu sao nào ở đoạn này.
    resolution: Chỉ bọc từ “À, đúng là” đến “gấp bội.” bằng *...*; giữ hai phần trần thuật bên ngoài.
    status: open
  - id: R06
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000368
    issue: Nét bất cẩn của sĩ quan vẫn bị giảm thành không chủ ý.
    evidence: Translation còn “vô tình bỏ qua”, trong khi package mô tả bỏ sót vì thiếu cẩn trọng. Tính suy đoán và hai phạm vi nghiêng hiện có vẫn đúng.
    resolution: Dùng “sơ ý bỏ qua”; giữ “Hẳn” để đây vẫn là suy luận của Tanya.
    status: open
  - id: R07
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000371
    issue: Vẫn thêm đồng thuận tuyệt đối và giữ cấu trúc ẩn dụ nặng bị động.
    evidence: Translation còn “ai cũng cho rằng” và “cảnh xác người bị sản xuất hàng loạt”; package không khẳng định mọi người cùng tin.
    resolution: Dùng giả định hiện giờ thay cho “ai cũng”; diễn đạt “việc sản xuất xác người hàng loạt”, giữ độ lạnh của ẩn dụ và nhận xét đạo đức thuộc đại tá.
    status: open
  - id: R08
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000374
    issue: Vẫn tăng độ chắc chắn và thêm ngưỡng chịu đựng không xác định.
    evidence: Translation còn “sẽ trở thành” và “quá sức chịu đựng”; package nêu khả năng gây thất bại cùng mức thiệt hại quá lớn.
    resolution: Khôi phục “có thể là một nhân tố lớn dẫn đến thất bại”; diễn đạt thiệt hại “thảm khốc—quá lớn” mà không thêm chủ thể hay ngưỡng chịu đựng.
    status: open
  - id: R09
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000380
    issue: Vẫn đổi câu hỏi tiếp lời thành câu hỏi về việc được gọi.
    evidence: Translation còn “ngài gọi tôi ạ?”; ngữ cảnh p000378 và package xác định Tanya hỏi đại tá muốn nói việc gì.
    resolution: Dùng “Vâng, có chuyện gì vậy, thưa ngài?” hoặc câu hỏi tiếp lời tương đương.
    status: open
  - id: R10
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000382
    issue: Vẫn gắn sự bảo vệ vào kinh nghiệm và chưa làm rõ việc luyện tập lặp lại.
    evidence: Translation còn “kinh nghiệm được bảo vệ” và “luyện tập và ôn tập”; ý nguồn là tích lũy kinh nghiệm trong điều kiện được bảo vệ, đối chiếu với lặp lại và rút kinh nghiệm qua trận nhỏ.
    resolution: Làm rõ “tích lũy kinh nghiệm dưới sự bảo vệ trong một chiến dịch lớn” và “luyện tập lặp đi lặp lại và ôn lại kỹ lưỡng” qua các trận nhỏ; không thêm người bảo vệ.
    status: open
self_check_assessment:
  result: inconsistent_with_translation
  issue: Self-check ghi đã áp dụng R01–R10 và khôi phục chữ nghiêng p000364/p000365, nhưng các trường translation thực tế vẫn thể hiện toàn bộ vấn đề cũ.
  action: Sau khi thực sự sửa translation, người giữ quyền sửa cần đối chiếu và cập nhật self-check theo tệp đã lưu trước khi giao review lại.
  counting_note: Sự không khớp của self-check được ghi riêng; không đếm lại thành finding dịch mới trùng với R01–R10.
  viewpoint_note: Nội tâm mở đầu p000379 là của đại tá, được trần thuật kế tiếp xác định; nhận xét về suy luận của Tanya không được áp dụng sang phần này.
reassessment:
  coverage: Đã đọc lại toàn bộ 25 đoạn theo cặp nguồn/bản dịch, xét nghĩa, văn phong, giọng, chủ thể, phủ định, điều kiện, độ chắc chắn, thuật ngữ và phạm vi em trong XHTML.
  new_translation_errors: Không phát hiện lỗi nghiêm trọng/vừa/nhẹ mới ngoài R01–R10.
  emphasis: p000368/p000371/p000372/p000379 giữ đúng phạm vi nhấn mạnh; p000364/p000365 vẫn thiếu theo R04/R05. Không thấy nhấn mạnh thêm ở đoạn khác.
  observations: p000364 giữ hình ảnh đơn vị bị hủy diệt mà không thêm cơ chế; p000371 cần giữ ẩn dụ lạnh lùng. Hai quan sát này không đòi thêm sửa nghĩa ngoài findings đã nêu.
pending_terms:
  - source_term: Heinrich's Law
    proposed_vi: Định luật Heinrich
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000367]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: Murphy's Law
    proposed_vi: Định luật Murphy
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000367]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: protective films / defensive shells
    proposed_vi: màn bảo hộ / lớp vỏ phòng ngự
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000362]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: replacement troops
    proposed_vi: quân thay thế / lính thay thế
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000358, YS-LN02/Text/part0026.xhtml/p000365, YS-LN02/Text/part0026.xhtml/p000372]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: non-magic raid
    proposed_vi: đột kích không dùng phép thuật
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000382]
    volume: vol-02
    chapter: 5
    status: pending
term_recommendations:
  - source_term: Heinrich's Law
    proposed_vi: Định luật Heinrich
    alternatives_vi: [Luật Heinrich]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000367]
    status: pending
    canon: false
    rationale: Giữ tên và cấu trúc song song với Murphy; không thêm tỷ lệ tai nạn hoặc học thuyết ngoài package.
  - source_term: Murphy's Law
    proposed_vi: Định luật Murphy
    alternatives_vi: [Luật Murphy]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000367]
    status: pending
    canon: false
    rationale: Nhất quán với Heinrich và lập luận về khả năng thất bại, không bổ sung công thức.
  - source_term: protective films / defensive shells
    proposed_vi: màn bảo hộ / lớp vỏ phòng ngự
    alternatives_vi: [màng bảo hộ / lớp vỏ phòng ngự, lớp bảo vệ / lớp vỏ phòng thủ]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000362]
    status: pending
    canon: false
    rationale: Theo lựa chọn tạm của coordinator và nhóm reviewer mới hơn trong ledger; giữ hai hình ảnh riêng và kế thừa lớp vỏ ở ch01-b07/ch04-b07, không suy cơ chế. Màng bảo hộ là phương án literal thay thế, không phải yêu cầu đổi lựa chọn đã giao.
  - source_term: replacement troops
    proposed_vi: quân thay thế / lính thay thế
    alternatives_vi: [quân bổ sung / lính bổ sung, binh sĩ thay thế]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000358, YS-LN02/Text/part0026.xhtml/p000360, YS-LN02/Text/part0026.xhtml/p000365, YS-LN02/Text/part0026.xhtml/p000372]
    status: pending
    canon: false
    rationale: Chọn quân/lính theo cú pháp tập thể hoặc quân số; p000360 giữ tân binh theo định danh package. Không đồng nhất với tăng viện hay chỉ người thay lính tử trận.
  - source_term: non-magic raid
    proposed_vi: đột kích không dùng phép thuật
    alternatives_vi: [cuộc đột kích không sử dụng phép thuật]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000382]
    status: pending
    canon: false
    rationale: Tường minh việc không dùng phép thuật và tự nhiên trong chuỗi huấn luyện; không thêm chiến thuật hoặc vũ khí.
risks:
  - Self-check không phải bằng chứng rằng các sửa đổi đã có trong translation; cần giao lại bản dịch thực sự sửa và self-check khớp.
  - Pending không cản signoff; mọi lựa chọn thuật ngữ vẫn chưa canon. Lý do chưa duyệt là các lỗi vừa còn nguyên.
next_action: coordinator_handoff_to_translation_editor
```
