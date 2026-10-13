# Signoff followup — vol-02-ch-06-b17

```yaml
role: reviewer
task_id: vol-02-ch-06-b17-final-signoff-followup
state: done
review_path: reviews/prose/vol-02/ch-06-b17-final-signoff-followup-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b17-final-signoff-followup-codex.md
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
  scope: Gói b17 đã giao, handoff b17, bản dịch, self-check, hai báo cáo review b17 và đúng mục ledger được chỉ định; hướng dẫn shared/reviewer và config pipeline.
  excluded_inputs_opened: false
  note: Không mở EPUB/PDF, gói khác hoặc canon ngoài phạm vi; lựa chọn kế thừa được đánh giá qua hồ sơ b17, không xác nhận lại canon.
counts:
  assigned_findings: 13
  resolved_assigned_findings: 13
  prior_closed_findings_rechecked: 12
  reopened_findings: 0
  followup_items_resolved: 2
  serious: 0
  moderate: 0
  minor: 0
  unresolved: 0
  material_new_issues: 0
  pending_term_groups: 7
  pending_local_choices: 5
validator: not_run
diff_check: not_run
commit: null
findings:
  - id: B17-F02
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000521, YS-LN02/Text/part0030.xhtml/p000525, YS-LN02/Text/part0030.xhtml/p000514]
    evidence: p000521 và p000525 dùng chúng ta cho nhiệm vụ chung trong nội tâm; p000514 giữ tôi trong lời xin lỗi thành tiếng. Sáu vị trí tự quy chiếu đã được review vẫn dùng mình, và self-check đã đồng bộ.
  - id: B17-S01
    status: resolved
    evidence: Khóa cấp cao nhất chapter6_b17_review_recommendations tồn tại; term_choices chứa đúng B17-T01–T07, local_choices chứa đúng B17-L01–L05. Cả 12 mục đều status pending và canon false; trạng thái nhóm là provisional_non_canon_apply_consistently. Bản dịch áp dụng nhất quán các lựa chọn hoặc phương án thay thế được cho phép.
prior_closed_findings:
  - {id: B17-F01, status: resolved, segments: [p000510], evidence: Giữ khái niệm không hành động rộng và tách câu xét nghĩa vụ báo cáo.}
  - {id: B17-F03, status: resolved, segments: [p000516], evidence: Nhấn mạnh tiếng hô tương ứng thẻ em duy nhất trong package; self-check ghi đúng.}
  - {id: B17-F04, status: resolved, segments: [p000519], evidence: Bỏ xưng hô thân mật thiếu căn cứ; giữ bản tính và chuyển quyền chỉ huy.}
  - {id: B17-F05, status: resolved, segments: [p000521], evidence: Quyết định sắp xếp chỉ huy không gợi hành động trái quyền hạn.}
  - {id: B17-F06, status: resolved, segments: [p000528, p000529], evidence: Chủ thể lực lượng Tanya và hướng đẩy lùi rõ; giữ điều kiện ngăn địch tiếp cận máy bay hoặc pháo binh.}
  - {id: B17-F07, status: resolved, segments: [p000532], evidence: Câu hỏi giữ do dự và kính ngữ cấp dưới; không gán giới hoặc tuổi.}
  - {id: B17-F08, status: resolved, segments: [p000533], evidence: Truy quét giữ nghĩa tác chiến; không suy thêm trạng thái tàn quân.}
  - {id: B17-F09, status: resolved, segments: [p000539], evidence: Kìm lời phản đối trong lòng không gợi thất hứa.}
  - {id: B17-F10, status: resolved, segments: [p000542], evidence: Oanh kích không giới hạn riêng pháo binh; giữ đủ hai nhánh đầu hàng và không đầu hàng.}
  - {id: B17-F11, status: resolved, segments: [p000546], evidence: Đại đội 2 nhận nhiệm vụ yểm trợ trực tiếp; không suy giới hoặc bên được yểm trợ.}
  - {id: B17-F12, status: resolved, segments: [p000547], evidence: Giữ điều kiện hành xử hợp lý và khả năng đầu hàng khác không; giả định phiên tòa và mục đích biện hộ rõ.}
  - {id: B17-F13, status: resolved, segments: [p000551], evidence: Giữ tầng chỉ huy cấp cao và phương án cho khả năng đầu hàng; không thêm nghĩa vụ pháp lý hoặc kế hoạch giam giữ.}
unresolved_findings: []
ledger_verification:
  path: work/run-state/pending-terms.yml
  top_level_key: chapter6_b17_review_recommendations
  exists: true
  term_ids: [B17-T01, B17-T02, B17-T03, B17-T04, B17-T05, B17-T06, B17-T07]
  local_ids: [B17-L01, B17-L02, B17-L03, B17-L04, B17-L05]
  all_pending: true
  all_non_canon: true
  applied_consistently: true
  note: Áp dụng được kiểm chứng từ bản dịch; ledger không cần trường applied riêng. B17-L03 dùng phương án giữ bản hiện tại đã được ledger và review cho phép. signoff_followup ghi đúng lựa chọn đại từ tại ba đoạn cần kiểm tra.
term_recommendations:
  - {id: B17-T01, proposed_vi: hành vi không hành động, segments: [p000510], status: pending, canon: false, application: verified}
  - {id: B17-T02, proposed_vi: xuất kích, segments: [p000511, p000525], status: pending, canon: false, application: verified}
  - {id: B17-T03, proposed_vi: Thưa thiếu tá / Trung úy / chỉ huy, segments: [p000514, p000519, p000524, p000530], status: pending, canon: false, application: verified}
  - {id: B17-T04, proposed_vi: Đại đội 2, segments: [p000546], status: pending, canon: false, application: verified}
  - {id: B17-T05, proposed_vi: giới chỉ huy cấp cao, segments: [p000551], status: pending, canon: false, application: verified}
  - {id: B17-T06, proposed_vi: tác chiến đô thị, segments: [p000534], status: pending, canon: false, application: verified}
  - {id: B17-T07, proposed_vi: truy quét, segments: [p000533], status: pending, canon: false, application: verified}
local_recommendations:
  - {id: B17-L01, segments: [p000519], status: pending, canon: false, application: verified}
  - {id: B17-L02, segments: [p000532], status: pending, canon: false, application: verified}
  - {id: B17-L03, segments: [p000544], status: pending, canon: false, application: verified_allowed_alternative}
  - {id: B17-L04, segments: [p000546], status: pending, canon: false, application: verified}
  - {id: B17-L05, segments: [p000551], status: pending, canon: false, application: verified}
risks:
  - Thiếu tá tại p000514 là lựa chọn tạm kế thừa; cách gọi trong nguồn tự nó không xác lập quân hàm. Không nâng thành canon.
  - Người nhận câu hỏi p000545 và bên được yểm trợ p000546 vẫn bất định; bản dịch hiện tại giữ trung tính, không cản signoff.
  - Signoff chỉ xác nhận review b17; validator và diff_check không chạy trong task này, không xác nhận commit hoặc hoàn tất pipeline.
signoff:
  decision: approved
  pronoun_followup_pass: true
  all_B17_F01_F13_resolved: true
  prior_12_findings_remain_closed: true
  ledger_inventory_verified: true
  seven_term_groups_and_five_local_choices_pending_non_canon: true
  no_material_new_issue: true
  reason: Cả hai mục tồn dư của signoff trước đã được xử lý; 12 finding đã đóng vẫn đạt sau đối chiếu đủ 44 đoạn.
next_action: Coordinator tiếp nhận signoff và xử lý các điều kiện hoàn tất pipeline thuộc thẩm quyền.
```
