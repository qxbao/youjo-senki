# Final signoff b02 — Codex

```yaml
role: reviewer
task_id: vol-02-ch-07-b02-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-07-b02-final-signoff-codex.md
files_written: [reviews/prose/vol-02/ch-07-b02-final-signoff-codex.md]
scope:
  source_package: work/vol-02/batches/ch-07-b02-source.jsonl
  source_package_sha256: f0f3f21af108a2773fe799bcf53caaa91cf0b07bf40da350435589c613f9dfbe
  hash_verified: true
  translation: translations/vol-02/ch-07-b02.jsonl
  self_check: reviews/semantic/vol-02/ch-07-b02-self-check.md
  reports_and_handoffs:
    - reviews/prose/vol-02/ch-07-b02-codex.md
    - handoffs/vol-02/ch-07-b02.yml
    - handoffs/vol-02/ch-07-b02-review-fixes.yml
    - handoffs/vol-02/ch-07-b02-final-signoff.yml
  canon_read:
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
  canon_hashes_match_primary_handoff: true
  ledger_sections_read:
    - chapter7_b02_translator_proposals
    - chapter7_b02_review_recommendations
  source_and_translation_ids_match: true
  source_quotations: false
  other_packages_or_books_opened: false
segment_ids:
  - YS-LN02/Text/part0032.xhtml/p000026
  - YS-LN02/Text/part0032.xhtml/p000027
  - YS-LN02/Text/part0032.xhtml/p000028
  - YS-LN02/Text/part0032.xhtml/p000029
  - YS-LN02/Text/part0032.xhtml/p000030
  - YS-LN02/Text/part0032.xhtml/p000031
  - YS-LN02/Text/part0032.xhtml/p000032
  - YS-LN02/Text/part0032.xhtml/p000033
  - YS-LN02/Text/part0032.xhtml/p000034
  - YS-LN02/Text/part0032.xhtml/p000035
  - YS-LN02/Text/part0032.xhtml/p000036
  - YS-LN02/Text/part0032.xhtml/p000037
  - YS-LN02/Text/part0032.xhtml/p000038
  - YS-LN02/Text/part0032.xhtml/p000039
  - YS-LN02/Text/part0032.xhtml/p000040
  - YS-LN02/Text/part0032.xhtml/p000041
  - YS-LN02/Text/part0032.xhtml/p000042
  - YS-LN02/Text/part0032.xhtml/p000043
  - YS-LN02/Text/part0032.xhtml/p000044
  - YS-LN02/Text/part0032.xhtml/p000045
  - YS-LN02/Text/part0032.xhtml/p000046
  - YS-LN02/Text/part0032.xhtml/p000047
  - YS-LN02/Text/part0032.xhtml/p000048
  - YS-LN02/Text/part0032.xhtml/p000049
  - YS-LN02/Text/part0032.xhtml/p000050
  - YS-LN02/Text/part0032.xhtml/p000051
counts:
  rows_reviewed: 26
  findings_verified: 11
  original_moderate: 4
  original_minor: 7
  resolved: 10
  unresolved: 1
  serious: 0
  moderate: 1
  minor: 0
  new_findings: 0
  pending_groups_verified: 5
validator: not_run
diff_check: not_run
commit: null
signoff: withheld
findings:
  - id: B02-M01
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000038
    issue: "Cấp tổ chức chưa được sửa: bản dịch và self-check vẫn dùng tập đoàn quân."
    evidence: "Gói b02 phân biệt quy mô sư đoàn với army group. Báo cáo ban đầu xác định việc dùng tập đoàn quân làm mất cấp tổ chức cao hơn và đề xuất cụm tập đoàn quân. Handoff sửa lại ghi tập đoàn quân, trùng cách dùng bị phản biện; self-check chỉ xác nhận làm theo handoff nên chưa chứng minh đã xử lý nghĩa. Canon không chốt thuật ngữ này."
    resolution: "Đề xuất tạm cụm tập đoàn quân tại p000038, cập nhật self-check tương ứng; coordinator sửa mâu thuẫn trong chỉ dẫn trước khi giao translator. Giữ đối chiếu quy mô, không thêm biên chế."
    status: unresolved
verification:
  - id: B02-M01
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000038]
    result: unresolved
    note: "Đối chiếu quy mô còn nguyên nhưng tên cấp tổ chức vẫn là lựa chọn bị phản biện; không thể signoff theo lời tự xác nhận trong self-check. Cách nói kết quả sư đoàn chưa biết không thêm kết luận chắc chắn thất bại ở quy mô lớn."
  - id: B02-M02
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000042]
    result: resolved
    note: "Tướng von Zettour giữ quân hàm trung tính, không tự xác định cấp tướng; self-check khớp."
  - id: B02-M03
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000041, YS-LN02/Text/part0032.xhtml/p000049, YS-LN02/Text/part0032.xhtml/p000050, YS-LN02/Text/part0032.xhtml/p000051]
    result: resolved
    note: "Cả bốn chỗ đều dùng trinh sát bằng vũ lực. Giữ chức năng nghi binh, thâm nhập sâu, đánh chặn và phản ứng mắc câu; không thêm quy mô hay mục tiêu. Self-check liệt kê đủ bốn đoạn."
  - id: B02-M04
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000045]
    result: resolved
    note: "Vật tư và trang bị quân sự giữ phạm vi nhu cầu vật chất rộng; vật tư tiếp tế dùng riêng cho các chuyến tàu. Self-check phân biệt đúng hai phạm vi."
  - id: B02-L01
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000031]
    result: resolved
    note: "Hỏa lực được tổ chức bài bản và xuyên phá với tốc độ cao tự nhiên hơn; giữ điều kiện đã bị phát hiện nhưng chưa khóa mục tiêu và ẩn dụ tàng hình. Self-check khớp."
  - id: B02-L02
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000035]
    result: resolved
    note: "Chỉ vừa đủ trao đổi vài lời thể hiện hạn chế thực tế, nối được với nhiễu âm ở p000036; không còn hàm ý hạn mức được thiết kế. Self-check khớp."
  - id: B02-L03
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000037]
    result: resolved
    note: "Quan sát viên là người bị đánh lạc hướng; giữ thiếu thông tin đồng đội, lực lượng đoạn hậu và nhịp tự sửa. Không thêm đơn vị trinh sát. Self-check khớp."
  - id: B02-L04
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000040]
    result: resolved
    note: "Tiểu đoàn tăng cường và quân số thiếu hụt là hai thuộc tính riêng; không giới hạn tăng cường vào quân số. Self-check khớp."
  - id: B02-L05
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000042]
    result: resolved
    note: "Chính tôi cũng đã tin mất giữ xác quyết của hệ quả phản thực quá khứ; cuộc gặp ở thủ đô và công sức dựng chuyện được giữ. Self-check xử lý chung với M02."
  - id: B02-L06
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000046]
    result: resolved
    note: "Khống chế tình hình và ém đi bằng các lệnh cấm tiết lộ nghiêm ngặt đã xử lý hai cụm gượng. Những phần câu chuyện vẫn hiểu được trong mạch thông tin; giữ riêng lớp thừa nhận thất bại và lớp tin đồn đã kiểm soát để giữ thể diện. Self-check khớp."
  - id: B02-L07
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000050]
    result: resolved
    note: "Thể hiện sự nóng vội và nhiệm vụ trinh sát bằng vũ lực nhằm nghi binh đọc rõ hơn; trong mạch p000041–p000051 đây là hình ảnh cần diễn cho địch. Giữ bắt buộc thực hiện và bất chấp thương vong; self-check khớp."
unresolved_findings: [B02-M01]
term_recommendations:
  - source_term: high-density-interference factors
    proposed_vi: tác nhân gây nhiễu mật độ cao
    alternatives_vi: [các yếu tố gây nhiễu có mật độ cao]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000026]
    status: pending
    canon: false
    result: consistent
    rationale: "Bản dịch, self-check và ledger khuyến nghị dùng cùng lựa chọn chính; không đặt tên vật chất hay cơ chế. Phương án phụ trong self-check được rút gọn, không đổi lựa chọn áp dụng."
  - source_term: ECM
    proposed_vi: ECM
    alternatives_vi: [thiết bị đối kháng điện tử (ECM), thiết bị gây nhiễu điện tử (ECM)]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000026, YS-LN02/Text/part0032.xhtml/p000028]
    status: pending
    canon: false
    result: consistent
    rationale: "Giữ viết tắt trong cả hai đoạn và tham chiếu 24; self-check khớp ledger khuyến nghị. Đề xuất khai triển trong ledger translator là lịch sử trước review, được handoff thay bằng lựa chọn reviewer. Không xác nhận đồng nhất kỹ thuật."
  - source_term: orb
    proposed_vi: quả cầu
    alternatives_vi: [thiết bị dạng cầu]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000026, YS-LN02/Text/part0032.xhtml/p000035]
    status: pending
    canon: false
    result: consistent
    rationale: "Cùng cách dùng literal trong bản dịch, self-check và ledger; không suy ra tên khí tài chuyên dụng."
  - source_term: directional waves via orbs
    proposed_vi: sóng định hướng truyền qua các quả cầu
    alternatives_vi: [sóng định hướng thông qua các quả cầu]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000035]
    status: pending
    canon: false
    result: consistent
    rationale: "Lựa chọn chính khớp cả ba đầu vào; không thêm loại sóng, nơi phát hoặc kiến trúc truyền tin."
  - source_term: reconnaissance-in-force / recon-in-force
    proposed_vi: trinh sát bằng vũ lực
    alternatives_vi: [trinh sát chiến đấu, trinh sát có vũ trang]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000041, YS-LN02/Text/part0032.xhtml/p000049, YS-LN02/Text/part0032.xhtml/p000050, YS-LN02/Text/part0032.xhtml/p000051]
    status: pending
    canon: false
    result: consistent
    rationale: "Bốn lần dùng và self-check khớp ledger khuyến nghị; lựa chọn trinh sát có vũ trang trong ledger translator là lịch sử trước review. Handoff chỉ định rõ ưu tiên khuyến nghị reviewer, không nâng thành canon."
pending_terms: []
risks:
  - "B02-M01 còn lỗi vừa; handoff sửa và self-check lặp lựa chọn bị phản biện. Chưa đủ điều kiện signoff hoặc hoàn tất pipeline."
  - "Cả năm nhóm vẫn pending/non-canon; phần ledger translator giữ hai lựa chọn cũ, cần đọc cùng handoff ưu tiên khuyến nghị reviewer. Trạng thái pending_fixes của ledger không chứng minh sửa đã hoàn tất."
  - "Chú thích 24 không nằm trong gói; chưa xác minh khai triển ECM. Bản chất tác nhân, khí tài quả cầu và kỹ thuật truyền tin vẫn bất định."
  - "Không dùng ngữ cảnh ngoài b02 để chốt cấp tướng, địa lý hoặc đại từ Tanya; DEC-P01-001 không được tự mở rộng sang giai đoạn này."
  - "Validator và diff-check không chạy trong lượt reviewer; kết quả review không thay thế kiểm tra và commit của coordinator."
next_action: coordinator_corrects_M01_instruction_then_translator_revises_translation_and_self_check_then_reviewer_rechecks
```

## Final correction addendum — B02-M01

```yaml
role: reviewer
task_id: vol-02-ch-07-b02-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-07-b02-final-signoff-codex.md
files_written: [reviews/prose/vol-02/ch-07-b02-final-signoff-codex.md]
segment_ids: [YS-LN02/Text/part0032.xhtml/p000038]
source_package_sha256: f0f3f21af108a2773fe799bcf53caaa91cf0b07bf40da350435589c613f9dfbe
hash_verified: true
findings:
  - id: B02-M01
    status: resolved
    resolution: "Bản dịch hiện dùng cụm tập đoàn quân cho army group, đúng handoff ch-07-b02-final-correction.yml và khuyến nghị reviewer. Giữ đối chiếu với sư đoàn, không hạ xuống cấp army, không thêm biên chế hay kết luận chắc chắn thất bại. Dòng xử lý M01 trong self-check khớp và ghi rõ pending/non-canon."
term_recommendations:
  - source_term: army group
    proposed_vi: cụm tập đoàn quân
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000038]
    status: pending
    canon: false
    rationale: "Giữ cấp tổ chức và phép đối chiếu quy mô của gói b02; tập đoàn quân là lựa chọn đã bị phản biện."
counts: {rows_reviewed: 1, resolved_total: 11, serious: 0, moderate: 0, minor: 0, new_findings: 0}
unresolved_findings: []
prior_signoff_findings: "Giữ nguyên kết luận đã xác minh cho 10 finding khác và năm nhóm thuật ngữ; lượt này chỉ tái kiểm M01."
risks:
  - "Dòng rủi ro cũ trong self-check còn ghi tập đoàn quân; dòng xử lý M01 cập nhật và bản dịch thống nhất cụm tập đoàn quân, nên đây là dấu vết ghi chép cũ, không còn lỗi nghĩa."
  - "Mục chapter7_b02_review_recommendations thực tế chỉ có năm nhóm thuật ngữ đã ghi ở trên, chưa có dòng army group dù handoff nói ledger đã sửa. Không xác nhận một mục ledger không hiện diện; lựa chọn M01 vẫn là đề xuất pending/non-canon theo handoff và self-check."
  - "Các giới hạn chứng cứ trước đây vẫn giữ nguyên; signoff không thay thế validator, diff-check và commit của coordinator."
validator: not_run
diff_check: not_run
commit: null
signoff: granted
signoff_scope: full_b02_review
supersedes: "Kết luận withheld, B02-M01 unresolved và yêu cầu sửa M01 trong phần báo cáo trước."
next_action: coordinator_completes_pipeline_checks_and_commit
```
