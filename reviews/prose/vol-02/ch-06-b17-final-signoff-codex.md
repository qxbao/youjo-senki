# Final signoff — vol-02-ch-06-b17

```yaml
role: reviewer
task_id: vol-02-ch-06-b17-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-06-b17-final-signoff-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b17-final-signoff-codex.md
runtime:
  configured_launcher: codex-personal
  configured_via: ai-isolator
  configured_model: gpt-6.1-sol
  configured_effort: medium
  execution: current_assigned_reviewer
  note: Không khởi chạy worker khác; các trường configured ghi cấu hình, không phải kiểm chứng launcher của tiến trình hiện tại.
source_verification:
  path: work/vol-02/batches/ch-06-b17-source.jsonl
  expected_sha256: 3d43967ca2b146408635d3eac527634fc11cb8f20212f5baf6c97505141df8ed
  actual_sha256: 3d43967ca2b146408635d3eac527634fc11cb8f20212f5baf6c97505141df8ed
  hash_match: true
  source_units: 44
  translation_units: 44
  ordered_ids_match: true
  row_source_hashes_match: true
coverage:
  segment_id_start: YS-LN02/Text/part0030.xhtml/p000510
  segment_id_end: YS-LN02/Text/part0030.xhtml/p000553
  reviewed: 44
  dimensions: [meaning, prose, viewpoint, pronouns, emphasis, ranks, pending_terms]
  canon_reference_hashes_match: true
  source_scope: Chỉ đọc gói nguồn b17 đã giao; không mở EPUB/PDF hoặc gói nguồn khác.
counts:
  assigned_findings: 13
  resolved_assigned_findings: 12
  partially_resolved_assigned_findings: 1
  serious: 0
  moderate: 0
  minor: 2
  unresolved: 2
  material_new_semantic_issues: 0
  pending_term_groups: 7
  pending_local_recommendations: 5
validator: not_run
diff_check: not_run
commit: null
findings:
  - id: B17-F01
    original_severity: moderate
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000510]
    evidence: Khái niệm không hành động được giữ rộng; nghĩa vụ báo cáo nằm ở câu riêng, không đặt tên tội hay xác quyết hệ thống luật hiện tại.
  - id: B17-F02
    original_severity: moderate
    residual_severity: minor
    status: partially_resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000510, YS-LN02/Text/part0030.xhtml/p000515, YS-LN02/Text/part0030.xhtml/p000516, YS-LN02/Text/part0030.xhtml/p000521, YS-LN02/Text/part0030.xhtml/p000543, YS-LN02/Text/part0030.xhtml/p000551]
    evidence: Tất cả sáu vị trí tự quy chiếu đã dùng mình; lời xin lỗi p000514 giữ tôi đúng. Tuy nhiên p000521 vẫn dùng chúng tôi cho nhiệm vụ chung, trái lựa chọn chúng ta mà handoff sửa và self-check xác nhận. p000525 cũng còn chúng tôi trong cùng mạch nội tâm.
    resolution: Translator đổi chúng tôi thành chúng ta tại p000521 và p000525, rồi đồng bộ self-check. Không sửa tôi trong lời thoại p000514.
    rationale: Lỗi còn lại là nhất quán lựa chọn đã giao, không phải đảo chủ thể hay sai nghĩa nghiêm trọng. Chúng tôi tự nó không chứng minh dịch sai; vì vậy hạ mức phần tồn dư xuống nhẹ, nhưng không xác nhận F02 hoàn tất toàn bộ.
  - id: B17-F03
    original_severity: moderate
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000516]
    evidence: Dấu nhấn mạnh Markdown bao đúng tiếng hô tương ứng thẻ em trong package; self-check đã ghi đúng. Phù hợp DEC-P01-002.
  - id: B17-F04
    original_severity: minor
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000519]
    evidence: Đã bỏ cách gọi thân mật chưa có căn cứ; giữ ý khó làm khác bản tính và chuyển quyền chỉ huy giữa hai sĩ quan.
  - id: B17-F05
    original_severity: minor
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000521]
    evidence: Việc sắp xếp lại chỉ huy được diễn đạt như quyết định của người có quyền, không còn hàm ý tự ý trái quyền hạn.
  - id: B17-F06
    original_severity: minor
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000528, YS-LN02/Text/part0030.xhtml/p000529]
    evidence: Lực lượng Tanya là bên đẩy địch khỏi vùng có thể tấn công; lực lượng ấy nối đúng chủ thể, giữ điều kiện và mục tiêu ngăn địch tiếp cận máy bay hoặc pháo binh, không thêm tiêu diệt hay giải cứu.
  - id: B17-F07
    original_severity: moderate
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000532]
    evidence: Câu hỏi giữ do dự và kính ngữ cấp dưới, không gán giới tính hoặc tuổi cho chỉ huy.
  - id: B17-F08
    original_severity: moderate
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000533]
    evidence: Truy quét giữ nghĩa tác chiến; không còn nghĩa thu dọn vật chất hoặc suy thêm tình trạng tàn quân.
  - id: B17-F09
    original_severity: minor
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000539]
    evidence: Giữ lời muốn nói trong lòng thể hiện kìm phản đối, không gợi thất hứa; phạm vi nhận xét tốt hay xấu rõ.
  - id: B17-F10
    original_severity: moderate
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000542]
    evidence: Oanh kích không thu hẹp riêng pháo binh trong ngữ cảnh có cả máy bay ném bom; giữ đủ hai nhánh đầu hàng và không đầu hàng.
  - id: B17-F11
    original_severity: minor
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000546]
    evidence: Giao Đại đội 2 nhiệm vụ yểm trợ trực tiếp, không thêm giới tính hoặc bên được yểm trợ.
  - id: B17-F12
    original_severity: minor
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000547]
    evidence: Điều kiện hành xử hợp lý và khả năng đầu hàng khác không được diễn đạt tự nhiên; giữ giả định phiên tòa và mục đích tự biện hộ.
  - id: B17-F13
    original_severity: moderate
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000551]
    evidence: Tầng chỉ huy cấp cao được tách rõ khỏi Tanya; phương án dự phòng hướng đến khả năng đầu hàng. Không thêm kế hoạch giam giữ, nghĩa vụ pháp lý hoặc chi tiết hậu cần ngoài thông tin package đã có.
  - id: B17-S01
    severity: minor
    status: open
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000510, YS-LN02/Text/part0030.xhtml/p000533, YS-LN02/Text/part0030.xhtml/p000551]
    issue: Handoff dẫn ledger chapter6_b17_review_recommendations nhưng không tìm thấy khóa này; mục chapter6_b17_translator_proposals còn giữ các lựa chọn cũ cho omission, mopping up và the brass.
    evidence: Review ban đầu và self-check ghi đầy đủ 12 đề xuất pending/non-canon; bản dịch áp dụng các lựa chọn sau review, nhưng ledger chưa phản ánh inventory reviewer được handoff dẫn.
    resolution: Coordinator ghi đủ B17-T01–T07 và B17-L01–L05 vào mục ledger được handoff chỉ định, giữ lịch sử đề xuất cũ và trạng thái pending/non-canon.
unresolved_findings: [B17-F02, B17-S01]
term_disposition:
  status: pending
  canon: false
  applied_consistently: true
  ledger_inventory_verified: false
  canon_promotion_found: false
  note: Bảy nhóm và năm lựa chọn cục bộ được xác nhận trong review, handoff và self-check; không có quyết định canon tương ứng. B17-L03 giữ bản hiện tại là phương án thay thế đã được review cho phép.
term_recommendations:
  - {id: B17-T01, proposed_vi: hành vi không hành động, segment_ids: [YS-LN02/Text/part0030.xhtml/p000510], status: pending, canon: false, application: verified}
  - {id: B17-T02, proposed_vi: xuất kích, segment_ids: [YS-LN02/Text/part0030.xhtml/p000511, YS-LN02/Text/part0030.xhtml/p000525], status: pending, canon: false, application: verified}
  - {id: B17-T03, proposed_vi: "Thưa thiếu tá / Trung úy / chỉ huy", segment_ids: [YS-LN02/Text/part0030.xhtml/p000514, YS-LN02/Text/part0030.xhtml/p000519, YS-LN02/Text/part0030.xhtml/p000524, YS-LN02/Text/part0030.xhtml/p000530], status: pending, canon: false, application: verified}
  - {id: B17-T04, proposed_vi: Đại đội 2, segment_ids: [YS-LN02/Text/part0030.xhtml/p000546], status: pending, canon: false, application: verified}
  - {id: B17-T05, proposed_vi: giới chỉ huy cấp cao, segment_ids: [YS-LN02/Text/part0030.xhtml/p000551], status: pending, canon: false, application: verified}
  - {id: B17-T06, proposed_vi: tác chiến đô thị, segment_ids: [YS-LN02/Text/part0030.xhtml/p000534], status: pending, canon: false, application: verified}
  - {id: B17-T07, proposed_vi: truy quét, segment_ids: [YS-LN02/Text/part0030.xhtml/p000533], status: pending, canon: false, application: verified}
local_recommendations:
  - {id: B17-L01, choice: Bỏ đại từ ở câu trấn an và giữ tên/cấp bậc khi phân công, segment_ids: [YS-LN02/Text/part0030.xhtml/p000519], status: pending, canon: false, application: verified}
  - {id: B17-L02, choice: "…Chắc chứ ạ?", segment_ids: [YS-LN02/Text/part0030.xhtml/p000532], status: pending, canon: false, application: verified}
  - {id: B17-L03, choice: Giữ bản hiện tại với họ chỉ đối phương và cái cớ biện minh trong nội tâm, segment_ids: [YS-LN02/Text/part0030.xhtml/p000544], status: pending, canon: false, application: verified_allowed_alternative}
  - {id: B17-L04, choice: Đại đội 2 đảm nhiệm yểm trợ trực tiếp, segment_ids: [YS-LN02/Text/part0030.xhtml/p000546], status: pending, canon: false, application: verified}
  - {id: B17-L05, choice: Giới chỉ huy cấp cao và chừa phương án cho khả năng đầu hàng, segment_ids: [YS-LN02/Text/part0030.xhtml/p000551], status: pending, canon: false, application: verified}
risks:
  - Ma’am không xác lập quân hàm; thiếu tá chỉ là lựa chọn tạm kế thừa trong phạm vi được giao, không được xác nhận bằng batch khác.
  - Chủ thể người nhận ở p000545 và bên được yểm trợ ở p000546 còn bất định; cách diễn đạt trung tính hiện tại phù hợp.
  - Ledger còn phương án cũ có thể khiến lượt sau kế thừa sai dù cả 12 đề xuất vẫn pending/non-canon.
  - Một truy vấn ledger dùng điều kiện b17 quá rộng đã trả thêm metadata đề xuất của chương khác. Đây là sai lệch phạm vi đọc; không dùng các mục đó làm căn cứ và không mở nguồn hoặc bản dịch tương ứng.
  - Reviewer không chạy validator hoặc diff-check; báo cáo không xác nhận điều kiện commit hay hoàn tất pipeline.
signoff:
  decision: withheld
  all_B17_F01_F13_resolved: false
  no_serious_or_moderate_remaining: true
  no_material_new_semantic_issue: true
  seven_term_groups_and_five_local_choices_pending_non_canon: true
  reason: F02 còn tồn dư nhẹ và mục ledger reviewer được dẫn chưa tồn tại; chưa thể ký xác nhận tất cả finding đã xử lý đầy đủ.
next_action: Coordinator giao translator đang giữ lease sửa hai đại từ số nhiều và đồng bộ self-check; coordinator bổ sung inventory pending vào ledger. Sau đó đối chiếu lại F02 và B17-S01 trong b17.
```
