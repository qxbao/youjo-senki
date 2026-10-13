# Sign-off F01–F08 — vol-02-ch-04-b28

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-04-b28
state: done
signoff: changes_required
review_path: reviews/prose/vol-02/ch-04-b28-fixes-signoff-codex.md
scope: >-
  Chỉ xác minh F01–F08 của p000502–p000528 và kiểm tra lỗi nghiêm trọng/vừa
  mới trên các đoạn bị tác động; không thực hiện review mới toàn bộ lô.
segment_ids:
  - YS-LN02/Text/part0024.xhtml/p000502
  - YS-LN02/Text/part0024.xhtml/p000503
  - YS-LN02/Text/part0024.xhtml/p000504
  - YS-LN02/Text/part0024.xhtml/p000507
  - YS-LN02/Text/part0024.xhtml/p000508
  - YS-LN02/Text/part0024.xhtml/p000526
  - YS-LN02/Text/part0024.xhtml/p000527
  - YS-LN02/Text/part0024.xhtml/p000528
input_checks:
  source_package_sha256: cbac478639ed500387b1b528a0c99d9302fd5854ddc63e33f530baf12f3941f4
  package_hash_matches_handoff: true
  listed_canon_hashes_match_handoff: true
  source_units: 27
  translation_units: 27
  pending_scope: chapter4_b28_translation_proposals
  basis: >-
    agents/shared.md, agents/reviewer.md, config/translation-pipeline.yml,
    handoff đúng lô, năm canon references của handoff, riêng nhóm pending được
    chỉ định, package chuẩn bị, bản dịch hiện tại và báo cáo ch-04-b28-codex.md.
  other_batch_inputs_inspected: false
findings:
  - id: F01
    severity: nghiêm trọng
    segment_id: YS-LN02/Text/part0024.xhtml/p000527
    status: resolved
    evidence: >-
      Bản dịch dùng hình ảnh máy bay bị ví như bật lửa một phát; không còn
      xác định tác nhân là xà lan hoặc thêm giới hạn chỉ khai hỏa một lần.
      Ví dụ tiếp tục phục vụ lập luận về sức mạnh trên không và chiến hạm.
    qualification: Chấp nhận phương án tạm của coordinator; không xác minh lore hoặc nâng thành canon.
  - id: F02
    severity: vừa
    segment_id: YS-LN02/Text/part0024.xhtml/p000507
    status: resolved
    evidence: >-
      Đã dùng khuôn mẫu nhận thức, tránh sắc thái phán xét của định kiến;
      giữ giới hạn tiếp nhận chủ quan, tính nghịch lý và khả năng mở rộng trí tuệ.
  - id: F03
    severity: vừa
    segment_id: YS-LN02/Text/part0024.xhtml/p000526
    status: resolved
    evidence: >-
      Đã dùng tác chiến bằng hỏa lực, không giới hạn quan điểm vào pháo binh;
      vẫn giữ vế coi trọng pháo chiến hạm vì khả năng yểm trợ.
  - id: F04
    severity: vừa
    segment_id: YS-LN02/Text/part0024.xhtml/p000526
    related_segment_ids: [YS-LN02/Text/part0024.xhtml/p000528]
    status: resolved
    evidence: >-
      Lực lượng tác chiến trên không ở p000526 và học thuyết lấy sức mạnh
      trên không làm trung tâm ở p000528 giữ hướng chuyển học thuyết của
      hải quân; không chuyển chủ thể thành một quân chủng độc lập.
  - id: F05
    severity: vừa
    segment_id: YS-LN02/Text/part0024.xhtml/p000528
    status: resolved
    evidence: >-
      Đã xác định trọng tâm hiện tại là tác chiến bằng chiến hạm, làm rõ
      đối lập với sức mạnh trên không; giữ điều kiện chưa có sự kiện tương tự
      thì khó thuyết phục hải quân.
  - id: F06
    severity: vừa
    segment_id: YS-LN02/Text/part0024.xhtml/p000502
    related_segment_ids: [YS-LN02/Text/part0024.xhtml/p000504]
    status: unresolved
    fix_progress: partially_resolved
    issue: Từ nối Hơn nữa ở đầu p000502 vẫn chưa có dấu nhấn mạnh.
    evidence: >-
      XHTML của p000502 đánh dấu hai vùng riêng. Bản dịch hiện tại chỉ đặt
      Markdown quanh phần nội tâm sau lời dẫn; từ nối đầu đoạn vẫn để phẳng.
      Phần nội tâm không bao gồm lời dẫn, và vùng chưa biết chuyện đó ở
      p000504 đã đúng. Vì vậy F06 chưa đạt đầy đủ DEC-P01-002.
    resolution: >-
      Người giữ quyền sửa đặt riêng *Hơn nữa* ở đầu p000502; giữ nguyên
      ranh giới nhấn mạnh nội tâm và vùng đã sửa ở p000504.
  - id: F07
    severity: nhẹ
    segment_id: YS-LN02/Text/part0024.xhtml/p000503
    related_segment_ids:
      - YS-LN02/Text/part0024.xhtml/p000508
      - YS-LN02/Text/part0024.xhtml/p000527
    status: resolved
    evidence: >-
      Basel ở p000503/p000508 và hai tên tàu ở p000527 đều có Markdown
      chữ nghiêng đúng vị trí; câu hỏi nghiêng riêng ở p000508 vẫn được giữ.
  - id: F08
    severity: nhẹ
    segment_id: YS-LN02/Text/part0024.xhtml/p000527
    status: resolved
    evidence: >-
      Đã mô tả Repulse được cải tạo cho phù hợp với thời hiện đại và
      Prince of Wales tối tân thời bấy giờ; không còn chuyển quá trình
      cải tạo thành thiết kế lại hoặc thêm mức tối tân bậc nhất. Hình ảnh
      xuống làm bạn với rong biển giữ kết quả đánh chìm và giọng ví von.
affected_segment_check:
  reviewed_segments: 8
  new_serious: 0
  new_moderate: 0
  observation: >-
    Không phát hiện lỗi nghiêm trọng/vừa mới về nghĩa, chủ thể, điều kiện,
    logic hoặc phạm vi nhấn mạnh trên các đoạn bị tác động. F06 là phần
    còn sót của lỗi đã giao, không tính thành lỗi mới.
term_recommendations:
  status: provisional_non_canon
  disposition: >-
    Giữ các lựa chọn tạm đã ghi cho khuôn mẫu nhận thức, tác chiến bằng hỏa lực,
    pháo cao xạ và hình ảnh máy bay ở các đoạn bị tác động; không đề xuất
    thay đổi canon hoặc cập nhật ledger trong lượt sign-off này.
files_written: [reviews/prose/vol-02/ch-04-b28-fixes-signoff-codex.md]
commit: null
resolved_findings: [F01, F02, F03, F04, F05, F07, F08]
unresolved_findings: [F06]
counts:
  assigned_total: 8
  assigned_severity: {serious: 1, moderate: 5, minor: 2}
  resolved_total: 7
  resolved_severity: {serious: 1, moderate: 4, minor: 2}
  unresolved_total: 1
  unresolved_severity: {serious: 0, moderate: 1, minor: 0}
  new_serious: 0
  new_moderate: 0
risks:
  - F06 còn mở ở mức vừa; chưa đủ điều kiện hoàn tất review bắt buộc hoặc xác nhận lô đã duyệt.
  - Hình ảnh máy bay ở p000527 là suy luận ngữ cảnh được coordinator chọn tạm; không xác nhận loại phương tiện, lịch sử hoặc cơ chế cụ thể.
  - Các lựa chọn thuật ngữ vẫn pending, không trở thành canon qua sign-off này.
  - Kết luận giới hạn ở tám đoạn bị tác động; không xác nhận toàn bộ lô hay các lô khác.
  - Validator và diff_check của fix_report là kết quả được handoff ghi lại; reviewer không chạy lại hoặc xác nhận chúng bằng công cụ.
validator: not_run
diff_check: not_run
next_action: >-
  Coordinator giao người giữ quyền sửa bổ sung riêng chữ nghiêng cho Hơn nữa
  tại p000502, rồi kiểm tra lại F06 và thực hiện validator/diff_check theo
  pipeline trước khi xác nhận hoàn tất. Reviewer không sửa bản dịch, handoff,
  canon, ledger, run-state và không chạy worker.
```
