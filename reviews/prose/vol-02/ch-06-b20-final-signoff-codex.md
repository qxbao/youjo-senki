# Final signoff độc lập — vol-02-ch-06-b20

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-06-b20-final-signoff
batch: vol-02-ch-06-b20
state: done
review_result: signoff
signoff: pass_with_provisional_choices
review_path: reviews/prose/vol-02/ch-06-b20-final-signoff-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b20-final-signoff-codex.md
segment_ids:
  - YS-LN02/Text/part0030.xhtml/p000610
  - YS-LN02/Text/part0030.xhtml/p000611
  - YS-LN02/Text/part0030.xhtml/p000612
  - YS-LN02/Text/part0030.xhtml/p000613
  - YS-LN02/Text/part0030.xhtml/p000614
  - YS-LN02/Text/part0030.xhtml/p000615
  - YS-LN02/Text/part0030.xhtml/p000616
  - YS-LN02/Text/part0030.xhtml/p000617
  - YS-LN02/Text/part0030.xhtml/p000618
  - YS-LN02/Text/part0030.xhtml/p000619
  - YS-LN02/Text/part0030.xhtml/p000620
  - YS-LN02/Text/part0030.xhtml/p000621
  - YS-LN02/Text/part0030.xhtml/p000622
  - YS-LN02/Text/part0030.xhtml/p000623
  - YS-LN02/Text/part0030.xhtml/p000624
  - YS-LN02/Text/part0030.xhtml/p000625
  - YS-LN02/Text/part0030.xhtml/p000626
  - YS-LN02/Text/part0030.xhtml/p000627
  - YS-LN02/Text/part0030.xhtml/p000628
  - YS-LN02/Text/part0030.xhtml/p000629
  - YS-LN02/Text/part0030.xhtml/p000630
  - YS-LN02/Text/part0030.xhtml/p000631
  - YS-LN02/Text/part0030.xhtml/p000632
  - YS-LN02/Text/part0030.xhtml/p000633
  - YS-LN02/Text/part0030.xhtml/p000634
  - YS-LN02/Text/part0030.xhtml/p000635
  - YS-LN02/Text/part0030.xhtml/p000636
  - YS-LN02/Text/part0030.xhtml/p000637
  - YS-LN02/Text/part0030.xhtml/p000638
  - YS-LN02/Text/part0030.xhtml/p000639
  - YS-LN02/Text/part0030.xhtml/p000640
  - YS-LN02/Text/part0030.xhtml/p000641
  - YS-LN02/Text/part0030.xhtml/p000642
  - YS-LN02/Text/part0030.xhtml/p000643
input_verification:
  instructions_read: [agents/shared.md, agents/reviewer.md, config/translation-pipeline.yml]
  source_package: work/vol-02/batches/ch-06-b20-source.jsonl
  expected_sha256: 1214be418ef94f270ce38a9dfcc5ab091102dd1c54336935a01900f8bcd1d342
  actual_sha256: 1214be418ef94f270ce38a9dfcc5ab091102dd1c54336935a01900f8bcd1d342
  package_hash: match
  source_rows: 34
  translation_rows: 34
  ordered_segment_ids: match
  per_row_source_hashes: all_match
  canon_reference_hashes: all_five_match_primary_handoff
  translation: translations/vol-02/ch-06-b20.jsonl
  self_check: reviews/semantic/vol-02/ch-06-b20-self-check.md
  initial_review: reviews/prose/vol-02/ch-06-b20-codex.md
  handoffs_read:
    - handoffs/vol-02/ch-06-b20.yml
    - handoffs/vol-02/ch-06-b20-translation.yml
    - handoffs/vol-02/ch-06-b20-review.yml
    - handoffs/vol-02/ch-06-b20-review-fixes.yml
    - handoffs/vol-02/ch-06-b20-final-signoff.yml
  canon_read:
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
  pending_ledger_sections_read:
    - chapter6_b20_translator_proposals
    - chapter6_b20_review_recommendations
  scope: Chỉ đầu vào b20 được giao và canon được nêu tên; không mở EPUB/PDF, gói nguồn khác hoặc dùng graph làm chứng cứ. Không chép câu nguồn.
counts:
  reviewed_rows: 34
  findings_verified: 10
  resolved_findings: 10
  resolved_by_original_severity: {serious: 0, moderate: 6, minor: 4}
  serious: 0
  moderate: 0
  minor: 0
  new_findings: 0
  unresolved_findings: 0
  emphasis_fixes_verified: 4
  pending_choices_assessed: 7
  pending_ledger_entries_assessed: 14
  canon_promotions: 0
validator: not_run
diff_check: not_run
commit: null
findings:
  - id: B20-CX-001
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000610
    status: resolved
    verification: Đối chiếu XHTML xác nhận hai vùng nhấn mạnh riêng. Bản dịch nhấn cụm “chỉ là những người bình thường” và riêng câu hỏi cuối; phần trần thuật giữa hai vùng không nghiêng, đúng DEC-P01-002.
  - id: B20-CX-002
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000612
    status: resolved
    verification: Hai câu hỏi nội tâm liên tiếp nằm chung một vùng nghiêng đúng ranh giới XHTML; trần thuật và lời dẫn cảm xúc bên ngoài. Câu bị ngắt vẫn được giữ; “Về lý trí” cũng đã làm câu dẫn tự nhiên hơn.
  - id: B20-CX-003
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000627
    status: resolved
    verification: Chỉ “Kẻ thù của Đế quốc” được nhấn trong lời thoại; vị ngữ và câu tán thành ngoài vùng nghiêng, đúng đối tượng nhấn trong gói.
  - id: B20-CX-004
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000633
    status: resolved
    verification: Hai vùng nghiêng giữ khoảng ngắt ở “có thể”; từ chỉ khả thể nằm ngoài nhấn mạnh. Vẫn là câu hỏi về người có khả năng trở thành địch, chưa biến thành địch đã xác định.
  - id: B20-CX-005
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000631
    related_segment_ids: [YS-LN02/Text/part0030.xhtml/p000626]
    status: resolved
    verification: Bản dịch dùng “Thiếu úy Grantz”, phù hợp quân hàm cụ thể ở p000626 và tính liên tục của cùng cuộc đối thoại. Self-check và cả hai mục ledger dùng lựa chọn này; B20-T06 giữ “Grantz” làm phương án thay thế. Đây là lời gọi tạm tại đoạn này, không là quy tắc chung cho Lieutenant.
  - id: B20-CX-006
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000639
    related_segment_ids: [YS-LN02/Text/part0030.xhtml/p000640, YS-LN02/Text/part0030.xhtml/p000641]
    status: resolved
    verification: Chuỗi p000636–p000638 tiếp tục theo Grantz; p000639–p000640 là phản ứng nội tâm của anh với lệnh vừa nhận. Self-check đã xác định đúng Grantz và không viện DEC-P01-001 cho anh. “Mình” là tự quy chiếu cục bộ. Dấu chuyển cảnh tại p000641 chỉ hỗ trợ tách cảnh tàu, chưa xác nhận danh tính người kể p000641–p000643; self-check giữ đúng giới hạn này.
  - id: B20-CX-007
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000610
    status: resolved
    verification: “Chỉ là những người bình thường” giữ nhận thức về tính người và khả năng chiến đấu; “các pháp sư tả tơi kia” giữ trạng thái rộng hơn sự mệt mỏi. Không thêm thương tích cụ thể. Self-check ghi nhận đúng hai thay đổi.
  - id: B20-CX-008
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000613
    status: resolved
    verification: Cụm giải thích được tách bằng gạch ngang, quan hệ mệnh lệnh–đối tượng rõ hơn. Pháp sư vẫn triển khai công thức để bảo vệ dân chúng khỏi cả Thiếu tá von Degurechaff và pháo binh, giúp dân chúng chạy thoát; không đảo vai hay bỏ một mối đe dọa.
  - id: B20-CX-009
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000615
    status: resolved
    verification: “Bộ chỉ huy gọi Tiểu đoàn Pixie. Chỉ có vậy. Hết.” giữ bên gọi/bên nhận, kết nội dung và một công thức kết lượt; đã bỏ lặp “Hết. Xin hết.”. p000620 vẫn là lời xác nhận và cam kết cố gắng của tiểu đoàn. Công thức vô tuyến này là lựa chọn cục bộ theo handoff, chưa thành chuẩn toàn dự án.
  - id: B20-CX-010
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000640
    status: resolved
    verification: “Đệch” đứng riêng giữa hai nhịp nhắc mệnh lệnh, giữ độ thô và nhịp giằng xé của Grantz. Toàn đoạn vẫn nghiêng đúng XHTML; không thêm đối tượng bị chửi. Self-check gọi rõ đây là lựa chọn giọng cục bộ chưa canon.
unresolved_findings: []
term_recommendations:
  - {id: B20-T01, proposed_vi: công thức bảo vệ, status: pending, canon: false, assessment: consistent}
  - {id: B20-T02, proposed_vi: đội hậu vệ, status: pending, canon: false, assessment: consistent}
  - {id: B20-T03, proposed_vi: Tiểu đoàn Pixie, status: pending, canon: false, assessment: consistent}
  - {id: B20-T04, proposed_vi: Bộ chỉ huy, status: pending, canon: false, assessment: consistent}
  - {id: B20-T05, proposed_vi: thiếu úy, status: pending, canon: false, assessment: consistent}
  - {id: B20-T06, proposed_vi: Thiếu úy Grantz, status: pending, canon: false, assessment: consistent}
  - {id: B20-T07, proposed_vi: Bộ chỉ huy, status: pending, canon: false, assessment: consistent}
pending_ledger_verification:
  result: accurate_provisional_local_recommendations
  all_fourteen_entries: status_pending_and_canon_false
  alternatives: B20-T01–B20-T07 giữ các phương án thay thế của review; lựa chọn áp dụng và giới hạn được hỗ trợ bởi lý do trong initial review và fix handoff.
  replacement_history: Mục translator giữ initial_proposed_vi cho HQ và Lieutenant; proposed_vi hiện tại đã theo B20-T04/B20-T06, không còn yêu cầu dùng lựa chọn cũ.
  occurrence_precision: Mục review B20-T01 phân biệt đúng lần xuất hiện trực tiếp p000613/p000618 với tham chiếu ngữ cảnh p000610/p000619. Danh sách rộng hơn trong mục translator và self-check được đọc là phạm vi ngữ cảnh, không phải bốn lần xuất hiện nguyên thuật ngữ.
  scope_limits: Không xác lập Pixie là tên chính thức hay mật danh; không đồng nhất HQ và Command thành một cơ quan canon; không thêm cấp chỉ huy hoặc cơ chế phép. Quân hàm và lời gọi chỉ được chọn theo bằng chứng trong lô.
  prose_and_voice: Các thay đổi từ vựng, vô tuyến, đại từ và mức tục là lựa chọn cục bộ được ghi trong review/handoff/self-check, không phải các mục canon mới.
  canon_check: glossary.yml và characters.yml chưa chốt mục nào; decisions.md chỉ có DEC-P01-001/002, không phê duyệt các đề xuất B20. Các hash canon vẫn khớp handoff.
additional_review:
  result: Không nhận diện lỗi mới có tính vật chất khi đối chiếu toàn bộ 34 đoạn.
  coverage: Giữ trình tự diệt hậu vệ–mất bảo vệ–pháo kích, giới hạn mười phút, điều kiện và độ chắc chắn, phản đối bị ngắt, giả thuyết về chỉ huy, mệnh lệnh và chuyển cảnh tàu. Các vùng nhấn mạnh còn lại cũng khớp nội dung và ranh giới tương ứng; số vùng nhấn khớp ở cả 34 đoạn.
risks:
  - Danh tính người kể cảnh tàu p000641–p000643 chưa được gói này xác nhận; tiếp tục giữ tự quy chiếu trung tính, không suy đoán từ lore.
  - Thuật ngữ, lời gọi quân hàm, xưng hô, công thức vô tuyến và mức tục vẫn là đề xuất cục bộ; signoff này không nâng chúng thành canon.
  - Trạng thái tiêu đề hai mục ledger vẫn phản ánh giai đoạn pending_review/pending_fixes; coordinator có thể cập nhật tiến độ sau khi tiếp nhận signoff, nhưng phải giữ pending/non-canon cho lựa chọn.
  - Validator và diff-check không chạy trong nhiệm vụ reviewer; không xác nhận lô đã đáp ứng điều kiện commit/hoàn tất pipeline.
next_action: Coordinator tiếp nhận signoff, xác nhận hoặc chạy validator và diff-check trên bản cuối theo primary handoff, cập nhật trạng thái xử lý review rồi commit lô nếu các điều kiện pipeline đạt; giữ mọi lựa chọn B20 là pending/non-canon.
```
