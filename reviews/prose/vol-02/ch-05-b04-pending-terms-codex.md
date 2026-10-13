# Review bổ sung pending terms — vol-02-ch-05-b04

Đã đọc đúng mục `chapter5_b04_translation_proposals` và đối sánh đủ bốn ID chính thức với package, bản dịch và báo cáo ban đầu. Rủi ro thiếu bản đồ pending `B04-PENDING-MAP` có thể đóng về mặt chứng cứ review. Việc đóng rủi ro này không xác lập canon, không giải quyết quân hàm còn bất định và không đóng các finding bản dịch đang mở.

Không phát hiện lỗi nghiêm trọng/vừa mới ngoài báo cáo ban đầu trong lượt bổ sung này. Vấn đề xác định bậc cấp úy tại p000099 vẫn thuộc `B04-F05`, không tạo finding trùng. Ledger chỉ ghi lựa chọn tạm và độ tin cậy thấp; không cung cấp căn cứ mới để khẳng định Thiếu úy hoặc Trung úy. Tạm chọn cách gọi giữ cấp úy mà không gán bậc cụ thể để tiếp tục công việc.

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-05-b04
review_type: supplemental_pending_terms
state: done
review_path: reviews/prose/vol-02/ch-05-b04-pending-terms-codex.md
initial_review_path: reviews/prose/vol-02/ch-05-b04-codex.md
scope:
  segment_id_start: YS-LN02/Text/part0026.xhtml/p000076
  segment_id_end: YS-LN02/Text/part0026.xhtml/p000102
  ledger_section: chapter5_b04_translation_proposals
  inputs:
    - agents/shared.md
    - agents/reviewer.md
    - config/translation-pipeline.yml
    - handoffs/vol-02/ch-05-b04.yml
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
    - 'work/run-state/pending-terms.yml#chapter5_b04_translation_proposals'
    - work/vol-02/batches/ch-05-b04-source.jsonl
    - translations/vol-02/ch-05-b04.jsonl
    - reviews/prose/vol-02/ch-05-b04-codex.md
  other_batches_inspected: false
  target_segment_ids:
    - YS-LN02/Text/part0026.xhtml/p000081
    - YS-LN02/Text/part0026.xhtml/p000082
    - YS-LN02/Text/part0026.xhtml/p000083
    - YS-LN02/Text/part0026.xhtml/p000093
    - YS-LN02/Text/part0026.xhtml/p000096
    - YS-LN02/Text/part0026.xhtml/p000099
files_written: [reviews/prose/vol-02/ch-05-b04-pending-terms-codex.md]
validator: not_run
diff_check: not_run
commit: null
input_checks:
  package_sha256_matches_handoff: true
  canon_reference_hashes_match_handoff: true
  source_translation_unit_counts: [27, 27]
  source_translation_ids_match: true
  official_ledger_ids_matched: true
findings: []
existing_findings:
  - id: B04-F05
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000099
    official_ledger_id: vol02-ch05-b04-lieutenant-serebryakov
    status: unresolved
    issue: 'Bản dịch xác định Thiếu úy trong khi package không phân biệt bậc cấp úy.'
    evidence: 'Canon chưa chốt quân hàm nhân vật. Ledger b04 ghi chính lựa chọn này là pending, độ tin cậy 0.45 và cần ngữ cảnh quân hàm; đó là metadata đề xuất, không phải chứng cứ xác nhận cấp bậc.'
    resolution: 'Áp dụng phương án tạm Úy Serebryakov như đề xuất bên dưới; không tự đổi sang Trung úy, không suy ra thăng cấp hoặc giáng cấp.'
  - id: B04-F02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000083
    status: unresolved
    relation: 'Lỗi đại từ nội tâm trong đoạn chứa tên huy hiệu vẫn thuộc finding ban đầu; chọn tên huy hiệu không giải quyết lỗi này.'
  - id: B04-F09
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000099
    status: unresolved
    relation: 'Cách gọi diễn tập ứng phó pháo kích vẫn là đề xuất riêng của báo cáo ban đầu; không gộp nó vào vấn đề quân hàm.'
unresolved_findings: [B04-F02, B04-F05, B04-F09]
initial_findings_disposition: 'Không đóng hay thay đổi trạng thái chín finding ban đầu; đây không phải lượt review sau sửa bản dịch.'
pending_map_disposition:
  id: B04-PENDING-MAP
  review_status: closed
  rationale: 'Đã đọc mục ledger b04 chính thức và đối sánh đủ bốn ID, từng mã đoạn, phương án hiện tại và lựa chọn thay thế.'
  state_file_updated: false
risks:
  - id: B04-RANK-UNCERTAINTY
    segment_id: YS-LN02/Text/part0026.xhtml/p000099
    status: residual_provisional
    description: 'Bậc cấp úy cụ thể vẫn chưa xác định. Dùng phương án trung tính để tiếp tục; không xem việc đóng pending-map là xác nhận Thiếu úy.'
  - 'Tên huy hiệu và tên đội hình chưa có canon; package chỉ cho nghĩa tại chỗ, không xác lập tên chính thức trong hệ thống huân thưởng hoặc học thuyết tác chiến.'
counts:
  context_segments_read: 27
  target_segments_reviewed: 6
  official_pending_ids_expected: 4
  official_pending_ids_reviewed: 4
  official_pending_ids_unresolved_mapping: 0
  new_findings_total: 0
  new_serious: 0
  new_moderate: 0
  new_minor: 0
  existing_findings_referenced: 3
  existing_moderate_referenced: 2
  existing_minor_referenced: 1
  pending_map_risks_closed_in_review: 1
  term_recommendations: 4
term_recommendations:
  - id: vol02-ch05-b04-silver-wings-assault-badge
    source_term: Silver Wings Assault Badge
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000083]
    ledger_proposed_vi: Huy hiệu Tấn công Cánh bạc
    proposed_vi: Huy hiệu Tấn công Cánh bạc
    alternatives_vi: [Huy hiệu Xung kích Cánh bạc]
    status: proposed
    confidence: medium
    rationale: 'Giữ cách gọi hiện tại: huy hiệu đúng loại phần thưởng được nêu; các thành tố tên được bảo toàn. Tấn công là cách dịch rộng, ít giả định về tên một binh chủng hay hình thức khen thưởng.'
    alternative_rationale: 'Xung kích có sắc thái quân sự rõ hơn nhưng chưa có căn cứ rằng tên huy hiệu cần nghĩa hẹp ấy. Không đổi huy hiệu thành huân chương và không thêm cấp hạng.'
    existing_review_relation: 'Khớp B04-TR01; bản thân tên huy hiệu không có lỗi nghiêm trọng/vừa. B04-F02 về đại từ trong cùng đoạn vẫn mở.'
    translation_action: keep_term
  - id: vol02-ch05-b04-artillery-emplacement-suppressive-fire
    source_term: artillery emplacement / supporting suppressive fire
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000081, YS-LN02/Text/part0026.xhtml/p000082]
    ledger_proposed_vi: ổ pháo binh / hỏa lực chế áp yểm trợ
    proposed_vi: vị trí pháo binh / hỏa lực chế áp yểm trợ
    alternatives_vi: [ổ pháo binh / hỏa lực chế áp yểm trợ, vị trí pháo binh / hỏa lực yểm trợ chế áp]
    status: proposed
    confidence: high_for_local_meaning
    rationale: >-
      Vị trí pháo binh nhận diện nơi bố trí pháo địch mà không suy ra đơn vị khẩu đội,
      quân số hay cấu trúc công sự. Hỏa lực chế áp yểm trợ giữ cả chức năng chế áp
      lẫn mục đích hỗ trợ đơn vị tấn công. Bản dịch giữ đúng đối tượng Đại đội G/H,
      thời lượng năm phút, bắt đầu ngay và xử lý mục tiêu trong khoảng ấy.
    alternative_rationale: >-
      Ổ pháo binh hiện tại vẫn hiểu được, không đủ căn cứ coi là lỗi nghĩa vừa;
      vị trí pháo binh rõ và trung tính hơn. Đảo thứ tự thành hỏa lực yểm trợ chế áp
      không đổi nghĩa nhưng cần dùng nhất quán. Không thay chế áp bằng tiêu diệt:
      tiêu diệt mục tiêu thuộc nhiệm vụ của đơn vị xông vào, không phải kết quả
      được bảo đảm bởi yêu cầu hỏa lực yểm trợ.
    existing_review_relation: 'Báo cáo ban đầu chưa có đề xuất riêng cho ID này. Đây là bổ sung coverage, không phải finding lỗi mới; logic yểm trợ đã được đánh giá đúng trong assessment ban đầu.'
    translation_action: optional_wording_refinement
  - id: vol02-ch05-b04-anti-surface-assault-formation
    source_term: anti-surface assault formation
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000093, YS-LN02/Text/part0026.xhtml/p000096]
    ledger_proposed_vi: đội hình xung kích chống mục tiêu mặt đất
    proposed_vi: đội hình xung kích chống mục tiêu mặt đất
    alternatives_vi: [đội hình xung kích đối đất, đội hình tấn công mục tiêu trên mặt đất]
    contextual_vi:
      p000093: đội hình xung kích chống mục tiêu mặt đất
      p000096: đợt xung kích chống mục tiêu mặt đất
    status: proposed
    confidence: high_for_local_meaning
    rationale: >-
      Mục tiêu pháo binh và mô tả tấn công mặt đất ở p000101 xác lập nghĩa mặt đất
      trong batch này. p000093 nói về đội hình bay, còn p000096 nói về hoạt động
      xung kích và trách nhiệm cảnh giới phía trên; giữ đúng sự khác nhau ấy.
      Bản dịch hiện tại giữ được phân công một đơn vị đánh và một đơn vị yểm trợ trên không.
    alternative_rationale: 'Xung kích đối đất gọn hơn; tấn công mục tiêu trên mặt đất ít sắc thái thuật ngữ hơn. Không tự gọi đây là tên đội hình học thuyết đã chốt, không thêm đội hình cụ thể hoặc mục tiêu trên biển.'
    existing_review_relation: 'Khớp B04-TR04, nay gắn đúng ID ledger đầy đủ. Không có lỗi nghĩa nghiêm trọng/vừa mới ở hai đoạn này.'
    translation_action: keep_term_and_contextual_distinction
  - id: vol02-ch05-b04-lieutenant-serebryakov
    source_term: Lieutenant Serebryakov
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000099]
    ledger_proposed_vi: Thiếu úy Serebryakov
    proposed_vi: Úy Serebryakov
    alternatives_vi: [Sĩ quan cấp úy Serebryakov, Thiếu úy Serebryakov, Trung úy Serebryakov]
    status: proposed
    confidence: low_for_exact_rank_medium_for_neutral_wording
    rationale: >-
      Cách gọi tại chỗ không phân biệt bậc cụ thể; ledger không đưa chứng cứ bổ sung.
      Tạm giữ cấp úy trong lời gọi và tên riêng để tránh tự xác định thiếu úy/trung úy.
      Úy là giải pháp diễn đạt trung tính trong lúc thiếu căn cứ, không phải tên
      quân hàm chính thức được canon công nhận.
    alternative_rationale: >-
      Sĩ quan cấp úy rõ nghĩa hơn nhưng nặng trong lời thoại trực tiếp.
      Thiếu úy là phương án ledger hiện hành, Trung úy là phương án thay thế của ledger;
      cả hai đều cần căn cứ phân bậc mà package này không cung cấp.
      Không dùng lựa chọn dịch mặc định để suy ra lịch sử cấp bậc của nhân vật.
    existing_review_relation: 'Khớp B04-TR05 và lỗi vừa B04-F05. Bổ sung xác nhận ledger vẫn chỉ là đề xuất; không tạo finding trùng, không tăng mức nghiêm trọng.'
    translation_action: revise_provisionally_under_B04-F05
next_action: >-
  Coordinator ghi nhận coverage 4/4 và đóng B04-PENDING-MAP trong quy trình của mình,
  đồng thời giữ riêng bất định quân hàm. Ghi bốn lựa chọn tạm theo đúng ID ledger,
  không nâng canon; bàn giao người giữ quyền sửa áp dụng phương án quân hàm cho B04-F05
  và cân nhắc đổi ổ pháo binh thành vị trí pháo binh. Tiếp tục xử lý các finding
  ban đầu rồi chạy kiểm tra và review lại bản sửa theo pipeline; báo cáo này
  không công nhận batch đã hoàn tất.
```
