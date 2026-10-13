# Final signoff — vol-02-ch-05-b17-final-signoff

Chưa duyệt: B17-F01 còn một lỗi vừa tại p000411 trong bản dịch đã lưu. Chín finding còn lại đã được giải quyết. Đã đối chiếu đủ 26 đoạn với package, kiểm tra nghĩa, văn phong, điểm nhìn, thuật ngữ và nhấn mạnh; không phát hiện lỗi mới độc lập. Self-check tuyên bố xử lý hết F01 nhưng chưa khớp bản lưu. Hash và thứ tự đoạn đạt; p000394 thuộc b16, vắng khỏi b17 và bản lưu b16 giống nguyên byte với HEAD.

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-05-b17-final-signoff
state: done
signoff_status: not_approved
review_path: reviews/prose/vol-02/ch-05-b17-final-signoff-codex.md
files_written: [reviews/prose/vol-02/ch-05-b17-final-signoff-codex.md]
validator: not_run
diff_check: not_run
commit: null
inputs_read:
  - AGENTS.md
  - agents/shared.md
  - agents/reviewer.md
  - config/translation-pipeline.yml
  - handoffs/vol-02/ch-05-b17-final-signoff.yml
  - handoffs/vol-02/ch-05-b17-review-retry.yml
  - reviews/prose/vol-02/ch-05-b17-review-retry-codex.md
  - reviews/prose/vol-02/ch-05-b17-codex.md
  - handoffs/vol-02/ch-05-b17-review-fixes.yml
  - handoffs/vol-02/ch-05-b17.yml
  - handoffs/vol-02/ch-05-b17-review.yml
  - reviews/semantic/vol-02/ch-05-b17-self-check.md
  - translations/vol-02/ch-05-b17.jsonl
  - work/vol-02/batches/ch-05-b17-source.jsonl
  - canon/glossary.yml
  - canon/style-guide.md
  - canon/characters.yml
  - canon/decisions.md
  - canon/glossary-pending.yml
  - work/run-state/pending-terms.yml#chapter5_b17_translation_proposals
  - work/run-state/pending-terms.yml#chapter5_b17_reviewer_recommendations
  - work/run-state/pending-terms.yml#chapter5_b13_reviewer_recommendations
  - work/run-state/pending-terms.yml#vol02-ch01-b02-lieutenant
  - work/run-state/pending-terms.yml#vol02-ch05-b04-lieutenant-serebryakov
  - translations/vol-02/ch-05-b16.jsonl
  - HEAD:translations/vol-02/ch-05-b16.jsonl
segment_range:
  start: YS-LN02/Text/part0026.xhtml/p000404
  end: YS-LN02/Text/part0026.xhtml/p000429
counts:
  segments_expected: 26
  segments_reviewed: 26
  serious: 0
  moderate: 1
  minor: 0
  findings_total: 1
  unresolved_findings: 1
  prior_findings_resolved: 9
  prior_findings_partially_resolved: 1
  new_findings: 0
  input_blockers: 0
hash_check:
  status: pass
  package_sha256_actual: 49cb1e17ffcdf82a282925db8d25fd7927b4cb06ce9751bb6176b4f40402be6e
  package_sha256_expected: 49cb1e17ffcdf82a282925db8d25fd7927b4cb06ce9751bb6176b4f40402be6e
  matches_final_signoff_handoff: true
  matches_corrected_review_retry_handoff: true
  matches_fix_handoff: true
  matches_original_batch_handoff: true
  original_blocked_review_handoff_sha256: 9f3cfaf76f20cf2795f1d7738c7e56cd5a1aed23d2f3ee9a1258e9aa1f2ee603
  B17-HASH: resolved_by_corrected_retry_handoff
  original_review_handoff_used_for_context_only: true
  canon_reference_hashes_match_batch_handoff: true
  source_sha256_metadata_consistent: true
  source_sha256_metadata: 3ac53161b6e093ba07203f284a400049cf902a3b0f51c0d3e40200867c13ae0a
  original_source_file_hash_recomputed: false
  note: 'Chỉ kiểm tra package và metadata tại chỗ; không mở EPUB/PDF gốc.'
saved_verification:
  performed: true
  translation_sha256: 590e06b4b331ce52a60d47ad306bdf3ac9c28d7097c84f9bda321bd2c2daec9b
  source_units: 26
  translation_units: 26
  ordered_ids_equal: true
  contiguous_expected_range: true
  duplicate_or_missing_ids: false
  all_F01_to_F10_examined: true
  all_F01_to_F10_resolved: false
  emphasis_matches_package: true
  self_check_consistent: false
  self_check_issue: 'Tuyên bố đã xử lý F01 và giữ tôi trong thoại p000411/p000412, nhưng p000411 còn Tôi đã buột miệng nói ra nỗi lo ngoài thoại. Ghi chung với F01, không đếm thành finding mới.'
  p000394:
    segment_id: YS-LN02/Text/part0026.xhtml/p000394
    outside_b17: true
    absent_from_b17_package_and_translation: true
    file: translations/vol-02/ch-05-b16.jsonl
    saved_row_count: 1
    HEAD_row_count: 1
    saved_row_identical_to_HEAD: true
    entire_b16_file_identical_to_HEAD: true
    row_sha256_without_line_ending: 3cfbd911b5ecad74f7876007743a32fd7d3b32e67131397fbcd2d22a4c4fc4c5
    untouched: true
    evidence_limit: 'Xác nhận trạng thái đã lưu bằng so sánh byte với HEAD; không suy diễn lịch sử thao tác ngoài bằng chứng này.'
resolution_status:
  B17-F01:
    status: partially_resolved
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000404, YS-LN02/Text/part0026.xhtml/p000411, YS-LN02/Text/part0026.xhtml/p000425]
    evidence: 'p000404/p000425 đã dùng mình. p000411 giữ tôi đúng trong thoại, câu cuối đã dùng mình, nhưng câu tự thuật ngay sau thoại vẫn bắt đầu bằng Tôi.'
  B17-F02:
    status: resolved
    segment_id: YS-LN02/Text/part0026.xhtml/p000412
    evidence: 'Toàn bộ lời chống chế giả định được bọc Markdown chữ nghiêng; câu dẫn ở ngoài nhấn mạnh.'
  B17-F03:
    status: resolved
    segment_id: YS-LN02/Text/part0026.xhtml/p000414
    evidence: 'Daigongen đáng kính và Zusho giữ tên/kính ngữ trung tính, không thêm tuổi, thân tộc hoặc nhân thân.'
  B17-F04:
    status: resolved
    segment_id: YS-LN02/Text/part0026.xhtml/p000417
    evidence: 'Đã dùng nhóm làm nhiệm vụ trinh sát chiến đấu; không còn đặc tính luồn sâu được thêm vào.'
  B17-F05:
    status: resolved
    segment_id: YS-LN02/Text/part0026.xhtml/p000420
    evidence: 'Giữ vài phút chạy, điều kiện không thoát và hỏa lực dồn dập đáp lại tín hiệu cầu cứu; không thêm bên bắn hoặc loại vũ khí.'
  B17-F06:
    status: resolved
    segment_id: YS-LN02/Text/part0026.xhtml/p000423
    evidence: 'Đã khôi phục tiền đề Con người không thể thay thế và mỗi chúng ta đều độc nhất.'
  B17-F07:
    status: resolved
    segment_id: YS-LN02/Text/part0026.xhtml/p000428
    evidence: 'Đã dùng sĩ quan cấp úy Serebryakov, không phân tiểu cấp; ledger/handoff mapping đúng p000428, còn Thiếu tá tại p000429.'
  B17-F08:
    status: resolved
    segment_id: YS-LN02/Text/part0026.xhtml/p000405
    evidence: 'Đã có hành động mời lính gác sang kết bạn cho Tình báo trò chuyện; giữ ẩn dụ xã giao, không thêm phòng hoặc cách thẩm vấn.'
  B17-F09:
    status: resolved
    segment_id: YS-LN02/Text/part0026.xhtml/p000419
    evidence: 'Câu so sánh đã dùng Không có cách nào tốt hơn thuật thức bay; giữ quan hệ thả tín hiệu mana và tháo chạy, cùng lời tán thưởng cuối đoạn.'
  B17-F10:
    status: resolved
    segment_id: YS-LN02/Text/part0026.xhtml/p000424
    evidence: 'Đã dùng ca tụng quỷ dữ như Chúa trong vài phút để dốc toàn lực; giữ *nhất định*, không thêm phong thần hoặc giải thích thần học.'
findings:
  - id: B17-F01
    severity: moderate
    status: partially_resolved
    segment_id: YS-LN02/Text/part0026.xhtml/p000411
    issue: 'Tự quy chiếu trong phần tự thuật vẫn dùng Tôi ngoài thoại, khiến lựa chọn ngôi chưa nhất quán và trái yêu cầu sửa F01.'
    evidence: 'Bản lưu có Tôi đã buột miệng nói ra nỗi lo sau dấu đóng thoại. Package phân biệt lời nói với câu thuật lại việc vừa lên tiếng; câu sau đó trong cùng đoạn đã dùng mình. Fix handoff yêu cầu mình trong phần này, theo DEC-P01-001.'
    resolution: 'Đổi câu tự thuật thành Mình đã buột miệng nói ra nỗi lo. Giữ Tôi trong câu thoại trước đó. Đối chiếu và cập nhật self-check theo bản thực lưu trước lượt signoff tiếp theo.'
unresolved_findings: [B17-F01]
input_blockers: []
new_findings: []
pending_terms_policy: temporary_consistent_not_canon
pending_terms: []
term_recommendations:
  - source_term: venerable Daigongen
    proposed_vi: Daigongen đáng kính
    alternatives_vi: [Daigongen tôn kính]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000414]
    status: pending
    rationale: 'Giữ tên nguyên dạng và kính ngữ; danh tính vẫn chưa xác lập. Đề xuất cũ trong ledger được giữ như lịch sử, đề xuất reviewer mới khớp bản lưu.'
  - source_term: SOS fire
    proposed_vi: hỏa lực đáp lại tín hiệu cầu cứu
    alternatives_vi: [hỏa lực yểm trợ khẩn cấp]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000420]
    status: pending
    rationale: 'Cách đọc chức năng được ngữ cảnh báo động/rút lui hỗ trợ; chưa xác lập bên bắn, vũ khí hoặc học thuyết. Phương án thay thế gán rõ chức năng yểm trợ hơn.'
  - source_term: force recon
    proposed_vi: nhóm làm nhiệm vụ trinh sát chiến đấu
    alternatives_vi: [trinh sát chiến đấu]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000417]
    status: pending
    rationale: 'Giữ quan hệ nhóm/nhiệm vụ và không thêm chiều sâu xâm nhập; chưa chốt thuật ngữ học thuyết.'
  - source_term: Lieutenant Serebryakov
    proposed_vi: sĩ quan cấp úy Serebryakov
    alternatives_vi: [Trung úy Serebryakov, Thiếu úy Serebryakov]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000428]
    status: pending
    rationale: 'Trung tính trước các đề xuất lịch sử mâu thuẫn; đoạn tại chỗ không xác định tiểu cấp. Không suy ra thay đổi quân hàm.'
  - source_term: Major
    proposed_vi: Thiếu tá
    alternatives_vi: [Major]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000429]
    status: pending
    rationale: 'Giữ ánh xạ tạm và mapping đã sửa; chưa canon.'
  - source_term: Zusho
    proposed_vi: Zusho
    alternatives_vi: []
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000414]
    status: pending
    rationale: 'Giữ tên nguyên dạng; không đủ căn cứ cho định danh hoặc cách Việt hóa khác.'
retained_pending_choices:
  First_Company: Đại đội Một
  flight_formula: thuật thức bay
  warning_trench: chiến hào cảnh giới
  mana_signal: tín hiệu mana
  p000425_viewpoint: 'Tạm dùng mình theo điểm nhìn liên tục; cách đọc lời nói được thuật lại vẫn là phương án khác, không khẳng định đây là cách đọc duy nhất.'
  p000426_address: 'cô trong thoại vẫn là đề xuất tại chỗ, không xác lập quan hệ nhân vật.'
risks:
  - 'Một lỗi vừa còn lại không đáp ứng điều kiện duyệt; state done chỉ xác nhận reviewer đã hoàn tất nhiệm vụ.'
  - 'Không nâng bất kỳ tên gọi, quân hàm hoặc thuật ngữ pending nào thành canon. Quy ước nội tâm mình và nhấn mạnh đã được duyệt riêng trong decisions.md.'
next_action: 'Coordinator bàn giao sửa phần F01 còn lại và self-check, rồi kiểm tra lại bản lưu; reviewer dừng tại báo cáo này.'
```
