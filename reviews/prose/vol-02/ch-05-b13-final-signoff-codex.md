# Final signoff — vol-02-ch-05-b13

Đã đối chiếu toàn bộ 20 đoạn với package được giao, bản dịch đã sửa, self-check cập nhật, ba handoff, review gốc, canon và ledger pending. Hash package khớp cả handoff dịch và handoff review; mã đoạn đủ, duy nhất, đúng phạm vi và đúng thứ tự. R01–R06 đã được giải quyết. Không còn lỗi nghiêm trọng hoặc vừa; duyệt signoff với một lỗi nhẹ về chữ nghiêng ở p000321. Đây là kết luận review, không xác nhận validator, diff-check hoặc hoàn tất commit của batch.

```yaml
role: reviewer
task_id: vol-02-ch-05-b13-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-05-b13-final-signoff-codex.md
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000313
  - YS-LN02/Text/part0026.xhtml/p000314
  - YS-LN02/Text/part0026.xhtml/p000315
  - YS-LN02/Text/part0026.xhtml/p000316
  - YS-LN02/Text/part0026.xhtml/p000317
  - YS-LN02/Text/part0026.xhtml/p000318
  - YS-LN02/Text/part0026.xhtml/p000319
  - YS-LN02/Text/part0026.xhtml/p000320
  - YS-LN02/Text/part0026.xhtml/p000321
  - YS-LN02/Text/part0026.xhtml/p000322
  - YS-LN02/Text/part0026.xhtml/p000323
  - YS-LN02/Text/part0026.xhtml/p000324
  - YS-LN02/Text/part0026.xhtml/p000325
  - YS-LN02/Text/part0026.xhtml/p000326
  - YS-LN02/Text/part0026.xhtml/p000327
  - YS-LN02/Text/part0026.xhtml/p000328
  - YS-LN02/Text/part0026.xhtml/p000329
  - YS-LN02/Text/part0026.xhtml/p000330
  - YS-LN02/Text/part0026.xhtml/p000331
  - YS-LN02/Text/part0026.xhtml/p000332
files_written:
  - reviews/prose/vol-02/ch-05-b13-final-signoff-codex.md
source_package_hash: 2e7afecd8ca26f1cf031857ef3ac5d7bb0894db160111f9524e8bdd651b272a3
source_package_hash_verified: true
source_sha256: 3ac53161b6e093ba07203f284a400049cf902a3b0f51c0d3e40200867c13ae0a
segment_order_verified: true
counts:
  reviewed_segments: 20
  serious: 0
  moderate: 0
  minor: 1
  total: 1
  resolved_original_findings: 6
unresolved_findings: [R07]
findings:
  - id: R07
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000321
    issue: Thiếu chữ nghiêng cho câu nội tâm ở cuối đoạn.
    evidence: >-
      XHTML trong package đặt toàn bộ câu thứ hai trong thẻ em, nhưng trường
      translation không có dấu Markdown tương ứng. DEC-P01-002 yêu cầu giữ phạm vi
      nhấn mạnh của nguồn. Self-check chỉ xác nhận p000316, bỏ sót p000321.
      Nội dung câu vẫn giữ nghĩa; lỗi nằm ở biểu diễn nhấn mạnh.
    resolution: >-
      Đề nghị đặt toàn bộ câu tiếng Việt thứ hai, bắt đầu bằng “Tỷ lệ” và kết thúc
      bằng “kinh nghiệm.”, trong một cặp dấu *...*. Khi sửa, cập nhật self-check để
      ghi nhận cả p000316 và p000321. Reviewer chỉ báo cáo, không thực hiện sửa.
resolved_findings:
  - id: R01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000324
    resolution: >-
      Đã dùng Trung úy Serebryakov theo đề xuất tạm gần nhất b09–b10 và handoff sửa.
      Self-check cũng ghi đúng lựa chọn pending; không suy diễn một lần thăng cấp.
  - id: R02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000326
    resolution: >-
      Đã làm rõ Tanya ngầm cho khách thấy điều kiện tiền tuyến qua vị cà phê;
      không còn cách đọc về địa vị hay nghĩa vụ. Giữ tính hàm ý của lời nói.
  - id: R03
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000324
    resolution: >-
      Đã dùng cặn vôi và diễn đạt đun nước loại cặn vôi; bỏ cơ chế lắng/lọc tự thêm.
      Vị cà phê được diễn đạt bằng cảm nhận tạp chất khó chịu, phù hợp ngữ cảnh.
  - id: R04
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000324
    resolution: >-
      Đã dùng vị đại tá có vai vế ấy, thể hiện tầm quan trọng của khách tự nhiên,
      không thêm chức vụ hoặc nâng quân hàm.
  - id: R05
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000315
    resolution: Đã dùng vùng đất giữa hai chiến tuyến, giữ rõ vị trí quân sự.
  - id: R06
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000328
    resolution: >-
      Đã dùng tuyến đầu đúng ngữ cảnh điều kiện sinh hoạt sát địch. Self-check giới hạn
      lựa chọn cho lần xuất hiện này và không coi đề xuất riêng của b11 là canon.
term_recommendations:
  - source_term: circulating notice
    proposed_vi: thông báo lưu hành
    alternatives_vi: [công văn lưu chuyển]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000320, YS-LN02/Text/part0026.xhtml/p000321]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: Giữ ý văn bản được lưu hành, ít suy diễn loại công văn; hồi chỉ thông báo đã nhất quán.
  - source_term: gray camouflage of the trench dress code
    proposed_vi: lớp ngụy trang màu xám theo quy định trang phục trong chiến hào
    alternatives_vi: [trang phục ngụy trang màu xám theo quy định trong chiến hào]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000315]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: Giữ quan hệ màu sắc với ngụy trang và quy định với trang phục, không thêm loại quân phục.
  - source_term: 3D labor
    proposed_vi: lao động 3D (bẩn thỉu, nguy hiểm và hạ thấp phẩm giá)
    alternatives_vi: [công việc 3D (bẩn thỉu, nguy hiểm và làm mất phẩm giá)]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000316]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: Giữ đủ ba nét nghĩa được package giải thích, phù hợp nội tâm coi chiến tranh là công việc.
  - source_term: firing line
    proposed_vi: tuyến đầu
    alternatives_vi: [tuyến hỏa lực, tuyến bắn]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000328]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: >-
      Chỉ vị trí trực tiếp chiến đấu trong đoạn bàn về nước uống và đời sống chiến hào.
      Lần dùng p000281 ở b11 có ngữ cảnh riêng; không tự thống nhất hay hồi sửa lô đó.
  - source_term: Lieutenant Serebryakov
    proposed_vi: Trung úy Serebryakov
    alternatives_vi: [Sĩ quan cấp úy Serebryakov]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000324]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: >-
      Theo lựa chọn tạm gần nhất trong chương; package không phân biệt thêm cấp úy.
      Cấp bậc thực tế còn bất định, không suy diễn thay đổi quân hàm.
  - source_term: chalk
    proposed_vi: cặn vôi
    alternatives_vi: [chất vôi trong nước]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000324]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: Khớp ngữ cảnh nước pha cà phê; không khẳng định hóa học hoặc cơ chế xử lý cụ thể.
  - source_term: important colonel
    proposed_vi: vị đại tá có vai vế ấy
    alternatives_vi: [vị khách quan trọng mang quân hàm đại tá]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000324]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: Giữ tầm quan trọng của khách và giọng kể tự nhiên, không gán chức vụ.
  - source_term: no-man’s-land
    proposed_vi: vùng đất giữa hai chiến tuyến
    alternatives_vi: [vùng đất trống giữa hai chiến tuyến]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000315]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: Xác định rõ vị trí quân sự trong cảnh bò tiến dưới nguy cơ bắn tỉa.
pending_terms: []
risks:
  - R07 là lỗi nhẹ còn mở, không chặn signoff theo ngưỡng zero serious/moderate của task.
  - Mọi lựa chọn thuật ngữ và quân hàm nêu trên vẫn là đề xuất tạm, không được nâng thành canon.
signoff_status: approved
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_receive_signoff_and_minor_finding
```
