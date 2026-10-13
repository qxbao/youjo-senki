role: reviewer
task_id: vol-02-ch-06-b12-final-signoff
state: done
signoff: approved
review_path: reviews/prose/vol-02/ch-06-b12-final-signoff-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b12-final-signoff-codex.md
source_verification:
  package: work/vol-02/batches/ch-06-b12-source.jsonl
  expected_sha256: 900b06e047c5e7cf8aee3289ff795a590bdd541038bfdbfaf9597e0a26027e6d
  actual_sha256: 900b06e047c5e7cf8aee3289ff795a590bdd541038bfdbfaf9597e0a26027e6d
  result: pass
  only_source_text: true
scope:
  batch: vol-02-ch-06-b12
  segments_reviewed: 23
  first_segment_id: YS-LN02/Text/part0030.xhtml/p000359
  last_segment_id: YS-LN02/Text/part0030.xhtml/p000381
  method: Đối chiếu độc lập toàn bộ b12 với package đã xác minh, rồi kiểm tra từng sửa theo báo cáo ban đầu và fixes handoff.
segment_ids:
  - YS-LN02/Text/part0030.xhtml/p000369
  - YS-LN02/Text/part0030.xhtml/p000370
  - YS-LN02/Text/part0030.xhtml/p000373
  - YS-LN02/Text/part0030.xhtml/p000378
  - YS-LN02/Text/part0030.xhtml/p000379
counts:
  before_fix: {serious: 0, moderate: 4, minor: 3, unresolved: 7}
  resolved: {serious: 0, moderate: 4, minor: 3, total: 7}
  remaining: {serious: 0, moderate: 0, minor: 0, unresolved: 0}
  new_findings: {serious: 0, moderate: 0, minor: 0}
findings:
  - id: F01
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000373]
    status: resolved
    resolution: Cả đơn vị là đối tượng được tập hợp; Grantz chỉ chạy đến để khỏi muộn. Cấu trúc bị động không thêm người tổ chức hay người ra lệnh. Mức sẵn sàng hai không bị diễn giải thành hệ thống báo động.
  - id: F02
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000373, YS-LN02/Text/part0030.xhtml/p000378]
    status: resolved
    resolution: Đại từ trần thuật về Tanya đã theo DEC-P01-001; Grantz vẫn được gọi theo ngữ cảnh riêng. Các vị trí Tanya trong phần còn lại của b12 cũng nhất quán; self-check phản ánh đúng bản dịch.
  - id: F03
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000378]
    status: resolved
    resolution: Giữ giả định nhượng bộ về việc lường trước và tác động vẫn sẽ xảy ra; không biến thành khẳng định Grantz đã chuẩn bị tinh thần. Hệ quả nản lòng không còn bị tăng thành mất hết tinh thần.
  - id: F04
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000370]
    status: resolved
    resolution: Giữ đánh giá về khả năng tận hưởng cuộc sống hậu chiến của Rudel; không còn suy ra sự sung túc vật chất.
  - id: F05
    severity: minor
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000370]
    status: resolved
    resolution: Hình ảnh bê tông cốt thép gắn trực tiếp với cả hai lập trường chính trị, giữ phép cường điệu trong nội tâm. Không thêm dấu nghiêng khi nguồn không có.
  - id: F06
    severity: minor
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000369]
    status: resolved
    resolution: Cách gọi huân chương đã tự nhiên và thể hiện thái độ coi nhẹ; không thêm kết luận phần thưởng giả hoặc người nhận không xứng đáng. Self-check ghi lựa chọn này là pending.
  - id: F07
    severity: minor
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000379]
    status: resolved
    resolution: Dùng điểm trung chuyển tiếp tế lớn, giữ việc thất thủ; không thêm tính chất phòng thủ. Ngữ cảnh hậu cần ở p000380 hỗ trợ cách diễn đạt này.
unresolved_findings: []
term_disposition:
  status: provisional_non_canon
  consistency: pass
  basis: Glossary và characters chưa có mục đã chốt; DEC-P01-001 và DEC-P01-002 chỉ chốt quy ước đại từ và nhấn mạnh. Fixes handoff và self-check đều giữ các lựa chọn thuật ngữ ở trạng thái tạm.
  canon_promotions: 0
term_recommendations:
  - id: P01
    source_term: sortie / sortie readiness
    proposed_vi: xuất kích / trạng thái sẵn sàng xuất kích
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000366, YS-LN02/Text/part0030.xhtml/p000367]
    status: pending
    applied_consistently: true
    rationale: Phân biệt hành động tác chiến và trạng thái chuẩn bị; không thêm phương thức triển khai.
    alternatives_vi: [xuất quân / trạng thái sẵn sàng xuất quân]
  - id: P02
    source_term: parallel pursuit
    proposed_vi: truy kích song song
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000375]
    status: pending
    applied_consistently: true
    rationale: Giữ tên gọi chiến thuật mà không suy diễn đội hình hoặc cơ chế bao vây.
    alternatives_vi: [truy đuổi song song]
  - id: P03
    source_term: supply relay point
    proposed_vi: điểm trung chuyển tiếp tế
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000379]
    status: pending
    applied_consistently: true
    rationale: Giữ chức năng hậu cần và độ mở về loại cơ sở; không thêm tính chất cứ điểm.
    alternatives_vi: [đầu mối trung chuyển tiếp tế]
  - id: P04
    source_term: readiness level two
    proposed_vi: mức sẵn sàng hai
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000373]
    status: pending
    applied_consistently: true
    rationale: Diễn đạt trung tính mức chuẩn bị, không đoán quy trình hoặc hệ thống báo động.
    alternatives_vi: [cấp độ sẵn sàng hai]
  - id: F06-wording
    source_term: superficial decoration
    proposed_vi: huân chương chỉ mang tính hình thức
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000369]
    status: pending
    rationale: Giữ thái độ coi nhẹ mà không kết luận về tính xác thực hoặc sự xứng đáng.
    alternatives_vi: [huân chương hào nhoáng bề ngoài]
additional_provisional_choices:
  - proposed_vi: bị bắt giam
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000369]
    status: provisional_non_canon
  - proposed_vi: Thiếu úy Grantz / Thiếu tá von Degurechaff
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000371, YS-LN02/Text/part0030.xhtml/p000381]
    status: provisional_non_canon
cross_checks:
  self_check_consistent_with_translation: true
  conditional_relations_and_viewpoint: pass
  emphasis_DEC_P01_002: pass
  material_new_issue: false
risks:
  - Thuật ngữ chiến thuật, mức sẵn sàng, cách gọi huân chương và quân hàm vẫn là lựa chọn tạm; package không đủ để xác lập tên gọi kỹ thuật hoặc canon toàn tác phẩm.
  - Các lựa chọn khẩu ngữ tại p000362 và p000366 vẫn nằm trong sắc thái nguồn; không phát hiện vấn đề mới cần sửa ở mức nghiêm trọng, vừa hoặc nhẹ.
  - Signoff này xác nhận nội dung b12 trong đầu vào hiện tại; không thay thế validator, kiểm tra diff hoặc bước commit của coordinator.
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_validation_and_commit
