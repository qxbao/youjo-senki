```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-06-b22-final-signoff
batch: vol-02-ch-06-b22
state: done
review_path: reviews/prose/vol-02/ch-06-b22-final-signoff-codex.md
files_written: [reviews/prose/vol-02/ch-06-b22-final-signoff-codex.md]
source_package: work/vol-02/batches/ch-06-b22-source.jsonl
source_package_sha256: 934b216d2e43f95024350f9dde7b33cea51e64670f540d3a4f2b9f6d2ea2e94f
hash_check: match
segment_id_prefix: YS-LN02/Text/part0030.xhtml/
segment_ids: [p000673, p000674, p000675, p000676, p000677, p000678,
  p000679, p000680, p000681, p000682, p000683, p000684, p000685,
  p000686, p000687, p000688, p000689, p000690, p000691, p000692,
  p000693, p000694, p000695, p000696, p000697, p000698, p000699,
  p000700, p000701, p000702, p000703, p000704, p000705, p000706,
  p000707, p000708]
scope:
  read:
    - agents/shared.md
    - agents/reviewer.md
    - config/translation-pipeline.yml
    - handoffs/vol-02/ch-06-b22-final-signoff.yml
    - handoffs/vol-02/ch-06-b22.yml
    - handoffs/vol-02/ch-06-b22-translation.yml
    - handoffs/vol-02/ch-06-b22-review.yml
    - handoffs/vol-02/ch-06-b22-review-fixes.yml
    - work/vol-02/batches/ch-06-b22-source.jsonl
    - translations/vol-02/ch-06-b22.jsonl
    - reviews/semantic/vol-02/ch-06-b22-self-check.md
    - reviews/prose/vol-02/ch-06-b22-codex.md
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
    - work/run-state/pending-terms.yml#chapter6_b22_translator_proposals
    - work/run-state/pending-terms.yml#chapter6_b22_review_recommendations
  external_lookup: false
  epub_pdf_opened: false
  other_source_packages_opened: false
  source_sentence_quotes: false
  note: >-
    Đọc hướng dẫn skill graphify nhưng không chạy graphify, không đọc graph,
    không tạo dữ liệu graph và không dùng làm chứng cứ nội dung. Ledger được
    phân tích cục bộ, chỉ lấy hai section b22 được giao. Không sửa đầu vào.
counts:
  source_rows: 36
  translation_rows: 36
  reviewed_rows: 36
  missing_rows: 0
  duplicate_or_reordered_ids: 0
  findings_verified: 12
  resolved_findings: 11
  resolved_moderate: 5
  resolved_minor: 6
  serious: 0
  moderate: 1
  minor: 0
  unresolved_findings: 1
  new_material_findings: 0
  source_emphasis_spans: 2
  preserved_emphasis_spans: 2
  pending_proposal_groups_assessed: 8
  pending_non_canon_groups: 8
  proposal_groups_matching_translation: 7
  proposal_groups_partially_matching_translation: 1
findings:
  - id: B22-C01
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000683
    status: resolved
    evidence: Chỉ thán từ À được nghiêng; phần sau không nghiêng, khớp package và DEC-P01-002.
  - id: B22-C02
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000676
    related_segment_ids: [p000675, p000677, p000686, p000693, p000694, p000695]
    status: resolved
    evidence: >-
      Tự quy chiếu nội tâm ở các vị trí được nêu đã dùng mình. p000675 giữ
      tôi trong kể động tác, đổi phần tự xét phép tắc sang mình; lời chào
      không bị đổi đại từ hàng loạt. p000689 giữ tôi trong thoại.
      p000674 là kể hành động/nhận biết, không phải lỗi nội tâm còn sót.
  - id: B22-C03
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000688
    related_segment_ids: [p000676, p000678, p000690]
    status: unresolved
    issue: Cấp tổ chức đường sắt chưa được bỏ hết; self-check tuyên bố sửa xong không đúng bản dịch.
    evidence: >-
      p000688 vẫn dùng Bộ Đường sắt của quân đội. Package xác lập sở thuộc
      quân đội nhưng không đủ căn cứ cho cấp Bộ. p000676 đã dùng cơ quan
      đường sắt của quân đội; p000690 dùng Cơ quan đường sắt. Hậu cần ở
      p000676/p000678 đã dùng bộ phận/ngành, bỏ cấp Cục. Self-check ghi
      p000688 dùng cách gọi trung tính và cả C01–C12 đã áp dụng, trái thực tế.
    resolution: >-
      Người giữ lease đổi riêng tên cơ quan ở p000688 thành cơ quan đường
      sắt của quân đội theo T02, giữ nội dung yêu cầu vận chuyển và việc
      báo cáo. Cập nhật self-check để khớp bản thực tế; kiểm tra lại ba
      đoạn đường sắt trước khi đóng C03. Lựa chọn vẫn pending/non-canon.
  - id: B22-C04
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000689
    status: resolved
    evidence: Dùng một trong các sĩ quan được vận chuyển, giữ cùng lắm; không tự gán vai trò chiến trường hoặc nhóm quân hàm.
  - id: B22-C05
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000696
    status: resolved
    evidence: >-
      Cấp trên đang tính lùi chính phòng tuyến Rhine về phía sau; giữ mức
      nghe nói và dự định. p000697 vẫn là câu Tanya hỏi riêng về rút lui.
  - id: B22-C06
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000700
    status: resolved
    evidence: >-
      Dùng và nối lui quân với khiến địch đổ máu, giữ phỏng đoán; bỏ quan
      hệ đồng thời. Quan hệ mục đích ở p000701 vẫn thuộc phần Tanya diễn
      giải, không thêm chi tiết tác chiến hoặc biến phỏng đoán thành chắc chắn.
  - id: B22-C07
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000681
    status: resolved
    evidence: >-
      Bỏ hạn định chỉ; giữ họp đồng môn và thứ bậc tác động ở hậu cảnh
      đến việc sĩ quan tạo quan hệ. Mức thân hơn sơ giao phù hợp package;
      không thêm bảo trợ, bè phái hoặc quan hệ thân thuộc.
  - id: B22-C08
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000690
    status: resolved
    evidence: Dùng đại quân chữ thường, bỏ hùng mạnh; giữ con voi quá đồ sộ và chuỗi vận chuyển–cơ động–tập trung sức chiến đấu.
  - id: B22-C09
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000694
    status: resolved
    evidence: Dùng ra vẻ biết hơn người, giữ giọng tự xét và giới hạn vai trò chiến thuật.
  - id: B22-C10
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000703
    status: resolved
    evidence: >-
      Dùng dự án không sinh lời; giữ đối lập tiền đã bỏ ra và tổn thất
      tiếp theo, cùng tự châm biếm về óc kinh tế bị cùn. Không nhận diện
      thêm Concorde hoặc chèn giải thích chi phí chìm.
  - id: B22-C11
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000704
    status: resolved
    evidence: Hình ảnh tín đồ trung thành của tinh thần hiện đại, thực dụng đã rõ; ý định Being X vẫn là câu hỏi giả định.
  - id: B22-C12
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000706
    status: resolved
    evidence: Dùng Dù vậy… rút lui sao?, giữ phản vấn ngập ngừng, không hàm ý rút lui đã bắt đầu.
unresolved_findings: [B22-C03]
focus_checks:
  emphasis: pass
  internal_pronouns: pass
  neutral_organizations: fail_at_p000688
  relationship_wording: pass
  self_check_consistency: fail_for_B22-C03
  all_eight_pending_non_canon: pass
  all_eight_choices_applied_consistently: fail_for_T02
  notes:
    - p000707 giữ đúng phạm vi nghĩ được nhấn mạnh; phần dẫn Tanya thầm nghĩ không nghiêng. Không thêm chữ nghiêng ở p000699.
    - p000698 giữ tên Tanya và điểm nhìn ngôi ba; self-check hiện tại không còn tuyên bố dùng nó ở đây, không cần tự thêm đại từ.
    - Xưng hô thoại tôi/ông/cô vẫn là lựa chọn cục bộ; không xác lập hồ sơ quan hệ nhân vật.
term_recommendations:
  - id: T01
    source_term: Major / Lieutenant Colonel
    proposed_vi: Thiếu tá / trung tá
    segment_ids: [p000673, p000675, p000676, p000677, p000686]
    translation_match: true
    status: pending
    canon: false
    rationale: Giữ phân biệt quân hàm hiện tại và dự đoán thăng hàm; không đồng nhất nhóm sĩ quan cấp trung với một quân hàm cụ thể.
  - id: T02
    source_term: Railroad Department
    proposed_vi: cơ quan đường sắt của quân đội
    alternatives_vi: [bộ phận đường sắt, Cục Đường sắt]
    segment_ids: [p000676, p000688, p000690]
    translation_match: partial
    status: pending
    canon: false
    rationale: >-
      Reviewer recommendation là lựa chọn tạm được fix handoff yêu cầu;
      đề xuất Bộ Đường sắt ở section translator là dấu vết ban đầu, không
      phải canon hay căn cứ giữ cách gọi đó ở p000688. Sở thuộc quân đội
      có căn cứ; cấp hành chính chưa đủ căn cứ, nên ưu tiên cơ quan.
  - id: T03
    source_term: Logistics / General Staff
    proposed_vi: hậu cần / Bộ Tổng tham mưu
    segment_ids: [p000676, p000678]
    translation_match: true
    status: pending
    canon: false
    rationale: Bộ phận/ngành Hậu cần giữ trung tính; Bộ Tổng tham mưu là lựa chọn tạm đúng ledger, không xác lập hệ tổ chức canon. Viết hoa còn mở.
  - id: T04
    source_term: mage / Being X
    proposed_vi: pháp sư / Being X
    segment_ids: [p000694, p000704]
    translation_match: true
    status: pending
    canon: false
    rationale: Giữ loại nhân sự và định danh theo đề xuất; glossary-pending cũng chỉ để Being X ở trạng thái pending.
  - id: T05
    source_term: interior lines strategy
    proposed_vi: chiến lược nội tuyến
    segment_ids: [p000690]
    translation_match: true
    status: pending
    canon: false
    rationale: Phù hợp tạm với ngữ cảnh điều quân và tập trung sức chiến đấu; chưa xác minh danh pháp bên ngoài.
  - id: T06
    source_term: Concorde
    proposed_vi: Concorde
    segment_ids: [p000703]
    translation_match: true
    status: pending
    canon: false
    rationale: Giữ tên để bảo toàn ám chỉ; danh tính vẫn chưa được package xác lập.
  - id: additional-field-officers
    source_term: field officers
    proposed_vi: một trong các sĩ quan được vận chuyển
    alternatives_vi: [sĩ quan cấp tá]
    segment_ids: [p000689]
    translation_match: true
    status: pending
    canon: false
    rationale: Trung tính khi nghĩa nhóm quân hàm và nghĩa ngoài thực địa chưa được phân định chắc chắn.
  - id: additional-great-army
    source_term: Great Army
    proposed_vi: đại quân
    alternatives_vi: [Đại quân]
    segment_ids: [p000690]
    translation_match: true
    status: pending
    canon: false
    rationale: Giữ hình ảnh lực lượng lớn, không tự thêm tên lịch sử hoặc nhận diện lore.
pending_terms:
  policy: temporary_consistent_not_canon
  assessed_sections: [chapter6_b22_translator_proposals, chapter6_b22_review_recommendations]
  ledger_status_check: Tất cả sáu lựa chọn và hai đề xuất bổ sung của review đều status pending, canon false.
  canon_check: Glossary và characters chưa chốt mục nào; decisions chỉ duyệt quy tắc đại từ và nhấn mạnh, không duyệt tám nhóm đề xuất b22.
risks:
  - p000688 còn cấp Bộ không có căn cứ và không nhất quán với p000676/p000690; self-check hiện tại không thể làm bằng chứng đóng C03.
  - Package giới hạn không xác minh hệ quân hàm/tổ chức toàn tác phẩm, danh pháp nội tuyến hoặc danh tính Concorde; tám lựa chọn vẫn tạm, không canon.
  - Chưa chạy validator hoặc diff-check trong lượt reviewer này; không xác nhận lô đã đủ điều kiện hoàn tất pipeline hay commit.
signoff:
  status: withheld
  reason: Còn một finding mức vừa B22-C03; không thể xác nhận cả 12 mục đã giải quyết hoặc self-check hoàn toàn nhất quán.
validator: not_run
diff_check: not_run
commit: null
next_action: >-
  Coordinator giao người giữ lease sửa tên cơ quan ở p000688 theo T02 và
  cập nhật self-check; giữ cả tám lựa chọn pending/non-canon. Sau đó chạy
  validator b22 với package/handoff và diff-check, đối chiếu lại C03 cùng
  self-check rồi mới cấp final signoff và đóng lô theo pipeline.
```

## Final correction addendum — B22-C03

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-06-b22-final-signoff
addendum: final_correction_B22-C03
state: done
review_path: reviews/prose/vol-02/ch-06-b22-final-signoff-codex.md
files_written: [reviews/prose/vol-02/ch-06-b22-final-signoff-codex.md]
supersedes: >-
  Trạng thái withheld, finding B22-C03 unresolved, các focus check thất bại
  tại p000688/self-check và T02 translation_match partial trong báo cáo trên.
  Giữ nguyên kết luận resolved của mười một finding còn lại và các giới hạn
  chứng cứ, pending/non-canon của báo cáo trước.
source_package: work/vol-02/batches/ch-06-b22-source.jsonl
source_package_sha256: 934b216d2e43f95024350f9dde7b33cea51e64670f540d3a4f2b9f6d2ea2e94f
hash_check: match
scope:
  semantic_recheck: [B22-C03]
  segment_id_prefix: YS-LN02/Text/part0030.xhtml/
  source_segments_rechecked: [p000676, p000688, p000690]
  retained_checks: >-
    Đối chiếu kết luận của mười một finding đã resolved với bản dịch và
    self-check hiện tại; kiểm tra lại hai section ledger b22 đã giao.
    Không mở rộng đối chiếu nguồn sang finding khác.
  external_lookup: false
  epub_pdf_opened: false
  other_source_packages_opened: false
  source_sentence_quotes: false
  graph_used: false
findings:
  - id: B22-C03
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000688
    related_segment_ids: [p000676, p000690]
    status: resolved
    evidence: >-
      p000688 hiện dùng Cơ quan đường sắt của quân đội, cùng cách gọi
      trung tính với p000676 và dạng rút gọn Cơ quan đường sắt ở p000690.
      Viết hoa đầu câu không xác lập cấp tổ chức. Sở thuộc quân đội được
      giữ; không còn tự đặt cấp Bộ/Cục. Yêu cầu lên kế hoạch vận chuyển
      khẩn cấp vào vùng chiến sự và lời báo cáo vẫn đúng package.
    self_check: >-
      Mục Railroad Department và mục B22-C03 nay mô tả đúng ba đoạn
      đường sắt; tuyên bố áp dụng C01–C12 không còn bị p000688 phủ định.
      Có lệch mô tả từ ngữ nhỏ đã có ở p000678: self-check ghi bộ phận
      Hậu cần, bản dịch dùng ngành Hậu cần. Cả hai đều trung tính; đây
      không phải cấp Bộ/Cục còn sót hoặc finding mức vừa, và không làm
      mất hiệu lực kết luận C03. Không xác nhận self-check khớp từng chữ.
prior_resolved_findings:
  ids: [B22-C01, B22-C02, B22-C04, B22-C05, B22-C06, B22-C07,
    B22-C08, B22-C09, B22-C10, B22-C11, B22-C12]
  status: remain_valid
  evidence: >-
    Bản dịch hiện tại vẫn thể hiện các sửa chữa đã ghi trong báo cáo:
    phạm vi chữ nghiêng và đại từ, cách gọi sĩ quan trung tính, quan hệ
    p000696/p000700, họp đồng môn, đại quân, tự xét ở p000694, dự án
    không sinh lời, hình ảnh tín đồ và phản vấn ở p000706. Không thấy
    điểm nào phủ định mười một kết luận trước trong kiểm tra kế thừa này.
pending_terms:
  assessed_sections: [chapter6_b22_translator_proposals, chapter6_b22_review_recommendations]
  policy: temporary_consistent_not_canon
  proposal_groups_assessed: 8
  proposal_groups_matching_translation: 8
  all_pending: true
  all_canon_false: true
  T02_translation_match: true
  evidence: >-
    Sáu lựa chọn T01–T06 và hai đề xuất field officers/Great Army trong
    section review vẫn pending, canon false và khớp bản dịch hiện tại.
    Sáu đề xuất ban đầu của translator cũng còn pending/non-canon;
    Bộ Đường sắt ở section đó là dấu vết đề xuất ban đầu, không ghi đè
    lựa chọn trung tính T02 đã được handoff final-correction yêu cầu.
    Không sửa ledger hoặc tự nâng bất kỳ lựa chọn nào thành canon.
effective_counts:
  resolved_findings: 12
  resolved_moderate: 6
  resolved_minor: 6
  serious: 0
  moderate: 0
  minor: 0
  unresolved_findings: 0
  new_material_findings: 0
unresolved_findings: []
focus_checks:
  neutral_organizations: pass
  self_check_consistency_for_B22-C03: pass
  prior_eleven_resolutions: pass
  all_eight_pending_non_canon: pass
  all_eight_choices_applied_consistently: pass
signoff:
  status: granted
  scope: full_reviewer_signoff_for_b22
  reason: >-
    C03 đã giải quyết; mười một finding và các kiểm tra pending trước
    vẫn có hiệu lực. Không còn finding nghiêm trọng/vừa hoặc lỗi mới
    có ảnh hưởng thực chất trong phạm vi recheck được giao.
risks:
  - Tám lựa chọn vẫn là đề xuất cục bộ pending/non-canon; giữ giới hạn chứng cứ của báo cáo trước.
  - Signoff reviewer không xác nhận validator, commit hoặc việc hoàn tất toàn bộ pipeline.
validator: not_run
diff_check: not_run
commit: null
next_action: Coordinator xác nhận các kiểm tra pipeline bắt buộc và commit trước khi đóng lô.
```
