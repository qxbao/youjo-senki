# Final signoff — vol-02-ch-06-b13

```yaml
role: reviewer
task_id: vol-02-ch-06-b13-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-06-b13-final-signoff-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b13-final-signoff-codex.md
source_verification:
  path: work/vol-02/batches/ch-06-b13-source.jsonl
  expected_sha256: d2f3d4e413de55741c9c87520bc552ec12ee70ace95601d7fd73cdf966d59562
  actual_sha256: d2f3d4e413de55741c9c87520bc552ec12ee70ace95601d7fd73cdf966d59562
  result: pass
scope:
  segment_range:
    start: YS-LN02/Text/part0030.xhtml/p000382
    end: YS-LN02/Text/part0030.xhtml/p000417
  source_packages_read: [work/vol-02/batches/ch-06-b13-source.jsonl]
  assigned_inputs_read:
    - translations/vol-02/ch-06-b13.jsonl
    - reviews/semantic/vol-02/ch-06-b13-self-check.md
    - reviews/prose/vol-02/ch-06-b13-codex.md
    - handoffs/vol-02/ch-06-b13-final-signoff.yml
    - handoffs/vol-02/ch-06-b13-review-fixes.yml
    - handoffs/vol-02/ch-06-b13-review.yml
  canon_references:
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
  pending_references:
    path: work/run-state/pending-terms.yml
    entries: [chapter6_b13_translator_proposals, chapter6_b13_review_recommendations]
  epub_pdf_read: false
  translation_edited: false
  source_text_written: false
counts:
  assigned_ids: 36
  reviewed_ids: 36
  original_findings_checked: 7
  resolved_findings: 6
  partially_resolved_findings: 1
  serious: 0
  moderate: 1
  minor: 0
  unresolved_findings: 1
  new_findings: 0
  material_new_findings: 0
  provisional_recommendations_checked: 8
  provisional_recommendations_applied: 8
  source_emphasis_segments: 11
  source_emphasis_spans: 13
  translation_emphasis_spans: 13
  emphasis_segments_with_correct_boundaries: 10
validator: not_run
diff_check: not_run
commit: null
findings:
  - id: B13-R01
    severity: moderate
    status: partially_resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000416]
    issue: Phạm vi nhấn mạnh còn thiếu phần nối mở đầu câu tự vấn.
    evidence: >-
      Đối chiếu trực tiếp XHTML trong package cho thấy phần nối tương ứng
      với “Dẫu vậy,” thuộc cùng vùng nhấn mạnh với câu hỏi nội tâm.
      Bản dịch hiện đặt dấu sao mở sau phần nối này. Số vùng nhấn mạnh
      đã khớp nhưng ranh giới tại p000416 chưa khớp DEC-P01-002.
    resolution: >-
      Đưa dấu sao mở ra trước “Dẫu vậy,”, bao gồm phần nối và toàn bộ
      câu hỏi trong cùng một vùng nhấn mạnh; giữ dấu sao đóng sau dấu hỏi.
      Không cần đổi nội dung hoặc ngôi của câu hỏi.
    confidence: high
    severity_note: >-
      Giữ mức vừa của finding B13-R01 đang được xác minh; phần tồn đọng
      chỉ là ranh giới định dạng, không phải lỗi nghĩa mới.
finding_verification:
  - id: B13-R01
    status: partially_resolved
    correct_segments: [p000391, p000393, p000398, p000399, p000404, p000407, p000411, p000413, p000414]
    unresolved_segments: [p000416]
    assessment: >-
      Chín đoạn đã sửa giữ đúng ranh giới câu/cụm. Ba vùng riêng tại
      p000404 và dấu ba chấm tại p000411 đúng. Vùng có sẵn tại p000383
      vẫn đúng; các đoạn không có nhấn mạnh nguồn không bị thêm dấu.
  - id: B13-R02
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000387]
    assessment: Giữ tâm thế kích động và quan hệ nguyên nhân, không còn gán tính hấp tấp.
  - id: B13-R03
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000400]
    assessment: Câu hỏi hướng vào độ khó thực hiện; sự chưa hiểu của Grantz vẫn ở câu kể tiếp theo.
  - id: B13-R04
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000402, YS-LN02/Text/part0030.xhtml/p000403]
    assessment: >-
      Nhận xét thấy lạ được phục hồi theo điểm nhìn Grantz. Weiss được
      gọi rõ là người hít sâu để chuẩn bị tinh thần; câu hỏi tiếp nối
      giữ đối tượng của việc chuẩn bị. Quân hàm tạm không bị đổi hoặc
      diễn giải thành chức vụ.
  - id: B13-R05
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000401, YS-LN02/Text/part0030.xhtml/p000417]
    assessment: Phân biệt lính bổ sung với tân binh theo từng ngữ cảnh, không suy ra kinh nghiệm của toàn nhóm.
  - id: B13-R06
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000416]
    assessment: >-
      Cảm giác không ăn khớp được giữ, không gợi xung đột quan hệ.
      Câu hỏi tự quy chiếu của Grantz dùng mình/chúng ta; kiểm tra thiết bị
      và lý do bảo dưỡng còn đủ. Lỗi ranh giới nhấn mạnh được giữ riêng
      dưới B13-R01, không đếm trùng thành lỗi ngôi kể.
  - id: B13-R07
    status: resolved
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000405]
    assessment: Giữ việc được miễn trừ thuộc quy trình thông thường, không chỉ hành động xin miễn trừ.
unresolved_findings: [B13-R01]
term_disposition:
  status: pending
  non_canon: true
  all_eight_applied: true
  canon_promoted: false
  authoritative_provisional_entry: chapter6_b13_review_recommendations
  historical_entry_note: >-
    chapter6_b13_translator_proposals vẫn giữ đề xuất ban đầu của B13-T05;
    lựa chọn đã sửa trong review recommendations và fixes handoff được
    áp dụng tại p000401. Mục lịch sử không được coi là lựa chọn hiện hành.
term_recommendations:
  - id: B13-T01
    proposed_vi: mô thức / mô thức chiến trường
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000383]
    applied: true
    status: pending
    non_canon: true
    assessment: Giữ mô hình tư duy, không thêm mệnh lệnh cụ thể hoặc học thuyết chính thức.
  - id: B13-T02
    proposed_vi: Tiểu đoàn Pháp sư Trên không số 203
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000385]
    applied: true
    status: pending
    non_canon: true
    assessment: Giữ cấp đơn vị, số hiệu và vai trò trên không, không suy ra quân chủng.
  - id: B13-T03
    proposed_vi: xuất kích
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000387, YS-LN02/Text/part0030.xhtml/p000396, YS-LN02/Text/part0030.xhtml/p000409, YS-LN02/Text/part0030.xhtml/p000416]
    applied: true
    status: pending
    non_canon: true
    assessment: Nhất quán tại các vị trí được giao, không thêm số lượt bay.
  - id: B13-T04
    proposed_vi: quy tắc giao chiến
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000404, YS-LN02/Text/part0030.xhtml/p000405]
    applied: true
    status: pending
    non_canon: true
    assessment: >-
      Tên thuật ngữ tại p000405 giữ phạm vi quy định giao chiến;
      p000404 giữ nội dung quy định và không cần chèn thêm tên thuật ngữ.
  - id: B13-T05
    proposed_vi: lính bổ sung tại p000401; tân binh tại p000417
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000401, YS-LN02/Text/part0030.xhtml/p000417]
    applied: true
    status: pending
    non_canon: true
    assessment: Phân biệt theo ngữ cảnh được áp dụng, không khẳng định hai nhóm nhất thiết khác nhau.
  - id: B13-T06
    proposed_vi: chiếm đóng
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000384, YS-LN02/Text/part0030.xhtml/p000398, YS-LN02/Text/part0030.xhtml/p000399]
    applied: true
    status: pending
    non_canon: true
    assessment: Chiếm đóng và biến thể chiếm thành phố đúng ngữ cảnh, không thêm cơ chế cai trị.
  - id: B13-T07
    proposed_vi: người không tham chiến
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000404]
    applied: true
    status: pending
    non_canon: true
    assessment: Giữ phạm vi đối tượng và nhấn mạnh riêng, không đồng nhất với toàn bộ dân thường.
  - id: B13-T08
    proposed_vi: quả cầu tính toán
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000416]
    applied: true
    status: pending
    non_canon: true
    assessment: Giữ định danh thiết bị riêng với súng trường, không thêm cơ chế hoặc chức năng.
risks:
  - segment_ids: [YS-LN02/Text/part0030.xhtml/p000416]
    status: unresolved
    finding: B13-R01
    assessment: Self-check tuyên bố đã khớp nhấn mạnh nhưng bỏ sót ranh giới phần nối mở đầu tại đây.
  - segment_ids: [YS-LN02/Text/part0030.xhtml/p000389, YS-LN02/Text/part0030.xhtml/p000393, YS-LN02/Text/part0030.xhtml/p000395, YS-LN02/Text/part0030.xhtml/p000397, YS-LN02/Text/part0030.xhtml/p000405, YS-LN02/Text/part0030.xhtml/p000409]
    status: pending_non_canon
    assessment: >-
      Cô là lựa chọn cục bộ cho Tanya trong phạm vi b13, còn nhất quán
      và rõ chủ thể. Không mở rộng DEC-P01-001 sang giai đoạn này;
      tên Tanya hoặc lược chủ ngữ vẫn là phương án trung tính thay thế.
  - segment_ids: [YS-LN02/Text/part0030.xhtml/p000407, YS-LN02/Text/part0030.xhtml/p000416]
    status: pending_non_canon
    assessment: Mình trong nội tâm Grantz phù hợp ngữ cảnh; không tạo quy tắc xưng hô chung.
  - segment_ids: [YS-LN02/Text/part0030.xhtml/p000387, YS-LN02/Text/part0030.xhtml/p000402, YS-LN02/Text/part0030.xhtml/p000412, YS-LN02/Text/part0030.xhtml/p000414]
    status: pending_non_canon
    assessment: >-
      Các lựa chọn tâm thế, chuẩn bị tinh thần, sắc thái hơi phiền phức
      và cách gọi cấp trên còn có căn cứ cục bộ; không thêm cấp bậc,
      động cơ hoặc thông tin lore. Bất định không tạo lỗi nghĩa cần chặn mới.
coverage_notes:
  - Đã đối chiếu độc lập toàn bộ 36 đoạn; ID và thứ tự khớp package, không thiếu hoặc lặp đoạn.
  - >-
      Giữ điều kiện về bộ binh, khác biệt phạm vi binh sĩ/pháp sư, lệnh cấm
      và ngoại lệ tài sản, hai thời điểm cảnh báo, việc tạm ngừng giao chiến,
      điều kiện đầu hàng và kiểm tra trang bị. Không phát hiện lỗi mới
      nghiêm trọng, vừa hoặc có ảnh hưởng đáng kể trong phạm vi được giao.
  - >-
      Signoff chỉ đánh giá bản dịch và review được giao; validator,
      diff-check và commit chưa được thực hiện trong task này.
signoff: not_approved
signoff_criteria:
  all_B13_R01_R07_resolved: false
  emphasis_matches_source_and_DEC_P01_002: false
  no_open_serious_or_moderate: false
  no_material_new_issue: true
  eight_recommendations_applied_and_non_canon: true
next_action: >-
  Coordinator chuyển phần tồn đọng B13-R01 tại p000416 cho người giữ
  quyền sửa; đưa phần nối vào vùng nhấn mạnh, cập nhật self-check rồi
  đối chiếu lại ranh giới này trước khi duyệt signoff.
```
