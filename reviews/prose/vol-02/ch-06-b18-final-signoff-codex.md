# Final signoff — vol-02-ch-06-b18

```yaml
role: reviewer
task_id: vol-02-ch-06-b18-final-signoff
state: done
signoff: pass
review_path: reviews/prose/vol-02/ch-06-b18-final-signoff-codex.md
files_written: [reviews/prose/vol-02/ch-06-b18-final-signoff-codex.md]
runtime_config:
  reviewer_launcher: codex-personal
  reviewer_model: gpt-6.1-sol
  reviewer_effort: medium
  note: Đọc cấu hình reviewer hiện hành; thực hiện trong worker được giao, không dispatch worker khác.
source_verification:
  path: work/vol-02/batches/ch-06-b18-source.jsonl
  expected_sha256: 1f6116310c3d403849cb4ba575d10a8bf521a4ea1fc4e6ad08dffe8554685d92
  actual_sha256: 1f6116310c3d403849cb4ba575d10a8bf521a4ea1fc4e6ad08dffe8554685d92
  result: pass
  only_source_package: true
  source_units: 30
  translation_units: 30
  ordered_ids_match: true
scope:
  start: YS-LN02/Text/part0030.xhtml/p000554
  end: YS-LN02/Text/part0030.xhtml/p000583
  translation: translations/vol-02/ch-06-b18.jsonl
  self_check: reviews/semantic/vol-02/ch-06-b18-self-check.md
  initial_review: reviews/prose/vol-02/ch-06-b18-codex.md
  handoffs:
    - handoffs/vol-02/ch-06-b18-final-signoff.yml
    - handoffs/vol-02/ch-06-b18-review-fixes.yml
    - handoffs/vol-02/ch-06-b18-review.yml
  canon_reference: canon/glossary-pending.yml — P03-human-capital
  ledger_section: chapter6_b18_review_recommendations
  note: >-
    Đối chiếu độc lập cả 30 đoạn với đúng package đã xác minh và kiểm tra phạm vi
    nhấn mạnh từ XHTML trong package. Không mở EPUB/PDF, package khác hoặc đoạn
    được P03 viện dẫn ngoài b18. Chỉ dùng section ledger được giao làm căn cứ.
validator: not_run
diff_check: not_run
commit: null
counts:
  reviewed_ids: 30
  prior_findings: 9
  resolved_findings: 9
  serious: 0
  moderate: 0
  minor: 0
  new_findings: 0
  material_new_issues: 0
  unresolved_findings: 0
  pending_main_groups: 8
  additional_pending_choices: 1
  pending_total: 9
  canon_promotions: 0
findings:
  - finding_id: B18-F01
    original_id: B18-M01
    original_severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000582
    status: resolved
    verification: >-
      Giữ suy đoán có lẽ về công dụng thủ tục và việc không còn cần phân loại
      thường dân là người không tham chiến. Không còn khẳng định thay đổi phân
      loại đã xảy ra; không thêm chủ thể quyết định, căn cứ luật hay tính hợp pháp.
  - finding_id: B18-F02
    original_id: B18-M02
    original_severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000580
    status: resolved
    verification: Giữ mức cháy thành than, quan hệ mùi khét/thối rữa và cảm giác không khí quánh dính vì protein; không thêm cơ chế sinh học.
  - finding_id: B18-F03
    original_id: B18-L01
    original_severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000573
    status: resolved
    verification: Chỉ câu châm ngôn được in nghiêng; phần dẫn, ngoặc kép và nhận xét nằm ngoài nhấn mạnh, đúng phạm vi nguồn.
  - finding_id: B18-F04
    original_id: B18-L02
    original_severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000582
    status: resolved
    verification: Toàn bộ câu suy đoán giữa đoạn được in nghiêng, kể cả dấu kết câu; hai câu còn lại không nghiêng.
  - finding_id: B18-F05
    original_id: B18-L03
    original_severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000567
    status: resolved
    verification: Dùng phương án lý do chính đáng trước mắt theo reviewer; câu rõ, giữ giọng tự biện hộ và bảo vệ đồng bào.
  - finding_id: B18-F06
    original_id: B18-L04
    original_severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000570
    status: resolved
    verification: Hẳn là giữ kỳ vọng tự trấn an về lý do biện minh, không còn sắc thái lời khuyên và không xác nhận miễn tội thực tế.
  - finding_id: B18-F07
    original_id: B18-L05
    original_severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000574
    status: resolved
    verification: Visha có kinh nghiệm, phản ứng khá hơn một chút và hiểu nguy hiểm khi chần chừ; không bổ sung lai lịch.
  - finding_id: B18-F08
    original_id: B18-L06
    original_severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000583
    status: resolved
    verification: Người phía mình giữ nghĩa cùng phe; cảm nhận thuộc Grantz rồi vụt tan, câu giải thích giữ Có lẽ và không biến động cơ Tanya thành sự thật.
  - finding_id: B18-F09
    original_id: B18-L07
    original_severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000556
    status: resolved
    verification: Giữ khả năng bị giết hoặc bị đám đông hành hình, cùng mức phỏng đoán; không thu hẹp phương thức hay thêm thủ phạm cụ thể.
unresolved_findings: []
emphasis:
  result: pass
  p000573: chỉ câu châm ngôn
  p000579: toàn đoạn, giữ nội tâm Grantz
  p000582: chỉ toàn câu suy đoán giữa đoạn
  additional_emphasis: none
self_check_assessment: >-
  Những mô tả về sửa nghĩa, điểm nhìn, phạm vi nghiêng và human capital khớp bản
  dịch hiện tại. Chỗ diễn giải lập luận về vốn nhân lực trong mục kiểm tra không
  phải lựa chọn thuật ngữ mới; mục pending xác nhận rõ vốn con người là cách dùng
  hiện tại và vốn nhân lực là phương án thay thế.
term_recommendations:
  - {id: B18-T01, proposed_vi: Quy tắc Chiến tranh trên bộ, segments: [p000554], application: consistent, status: pending, canon: false}
  - {id: B18-T02, proposed_vi: Thiếu úy, segments: [p000581], application: consistent, status: pending, canon: false}
  - {id: B18-T03, proposed_vi: Thiếu tá, segments: [p000583], application: consistent, status: pending, canon: false}
  - {id: B18-T04, proposed_vi: truy quét, segments: [p000574, p000576], application: consistent, status: pending, canon: false}
  - {id: B18-T05, proposed_vi: cuộc tiêu diệt / giai đoạn tiêu diệt toàn bộ, segments: [p000566, p000568], application: consistent, status: pending, canon: false}
  - {id: B18-T06, proposed_vi: nhiệm vụ giải cứu những người bị giam giữ, segments: [p000583], application: consistent, status: pending, canon: false}
  - id: B18-T07
    proposed_vi: Tanya nội tâm mình hoặc lược chủ ngữ; Grantz trần thuật anh và nội tâm mình; Visha cô; Tanya qua cảm nhận Grantz cô.
    application: consistent_with_local_viewpoint
    status: pending
    canon: false
    note: >-
      Không áp máy móc nó ở p000583. Ledger yêu cầu áp theo điểm nhìn cục bộ;
      initial review giải thích rõ cô ở đây. B18 không đủ căn cứ phê chuẩn nó
      cho trần thuật Tanya độc lập hoặc bất kỳ quy tắc đại từ toàn cục nào.
  - {id: B18-T08, proposed_vi: đồng bào / lũ Đế quốc khốn kiếp, segments: [p000561, p000567, p000568, p000569], application: consistent_with_review_accepted_variant_at_p000568, status: pending, canon: false}
  - id: B18-HC01
    source_term: human capital
    segment_id: YS-LN02/Text/part0030.xhtml/p000563
    proposed_vi: vốn con người
    alternative_vi: vốn nhân lực
    application: applied
    rationale: Khớp lựa chọn reviewer và đề xuất P03-human-capital; phù hợp lập luận về huấn luyện và giá trị con người trong kinh tế học ở b18.
    status: pending
    canon: false
    disposition_note: >-
      Section ledger được giao có tám nhóm B18-T01–T08. B18-HC01 được ghi riêng
      trong handoff final-signoff và được self-check xác nhận cùng phương án thay
      thế; không tuyên bố HC01 có entry trong section ledger này. P03 vẫn pending.
risks:
  - Chín lựa chọn vẫn tạm thời, không phải canon; không xác nhận sự nhất quán ngoài b18.
  - p000582 vẫn không xác lập chủ thể phân loại hoặc cơ chế pháp lý; cách dịch hiện tại giữ bất định đó và không cần dừng review.
  - Signoff chỉ xác nhận review nghĩa/văn phong; validator và diff_check chưa chạy trong task này, không xác nhận hoàn tất các cổng pipeline hoặc commit.
next_action: Coordinator tiếp tục các cổng pipeline theo thẩm quyền; không cần vòng sửa thêm từ review này.
```
