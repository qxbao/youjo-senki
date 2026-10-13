# Final signoff độc lập — vol-02-ch-06-b21

```yaml
role: reviewer
task_id: vol-02-ch-06-b21-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-06-b21-final-signoff-codex.md
files_written: [reviews/prose/vol-02/ch-06-b21-final-signoff-codex.md]
segment_id_prefix: YS-LN02/Text/part0030.xhtml/
segment_ids: [p000644, p000645, p000646, p000647, p000648, p000649, p000650, p000651, p000652, p000653, p000654, p000655, p000656, p000657, p000658, p000659, p000660, p000661, p000662, p000663, p000664, p000665, p000666, p000667, p000668, p000669, p000670, p000671, p000672]
id_convention: Mọi mã p nối với segment_id_prefix để thành mã đoạn đầy đủ.
input_verification:
  source_package: work/vol-02/batches/ch-06-b21-source.jsonl
  source_package_sha256: 7cbc9cfc8f06bae5e818fddda061f1a6ca05b00c014e96bb6c75140fb8ad29e8
  hash_match: true
  source_rows: 29
  translation_rows: 29
  ordered_ids_match: true
  canon_reference_hashes_match_primary_handoff: true
  review_inputs:
    - agents/shared.md
    - agents/reviewer.md
    - config/translation-pipeline.yml
    - handoffs/vol-02/ch-06-b21-final-signoff.yml
    - handoffs/vol-02/ch-06-b21.yml
    - handoffs/vol-02/ch-06-b21-review.yml
    - handoffs/vol-02/ch-06-b21-review-fixes.yml
    - work/vol-02/batches/ch-06-b21-source.jsonl
    - translations/vol-02/ch-06-b21.jsonl
    - reviews/semantic/vol-02/ch-06-b21-self-check.md
    - reviews/prose/vol-02/ch-06-b21-codex.md
    - work/run-state/pending-terms.yml#chapter6_b21_translator_proposals
    - work/run-state/pending-terms.yml#chapter6_b21_review_recommendations
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
  epub_pdf_opened: false
  other_packages_opened: false
  source_sentences_in_report: false
counts:
  rows_reviewed: 29
  findings_rechecked: 10
  original_serious: 0
  original_moderate: 6
  original_minor: 4
  findings_resolved: 10
  serious: 0
  moderate: 0
  minor: 0
  new_findings: 0
  unresolved_findings: 0
  proposals_verified: 8
  proposals_accurate_as_temporary_choices: 8
  proposals_pending_non_canon: 8
findings: []
resolution_checks:
  - id: B21-R01
    original_severity: moderate
    segment_ids: [p000644]
    status: resolved
    translation_check: Cách nói chẳng hợp hoàn cảnh giữ sự thiếu nhạy cảm của lựa chọn món ăn, không còn nghĩa hợp thời hoặc thời thượng.
    self_check: Đã ghi đúng việc sửa bình diện đánh giá ở p000644–p000646.
  - id: B21-R02
    original_severity: moderate
    segment_ids: [p000644, p000645, p000646]
    status: resolved
    translation_check: p000644 và p000645 nghiêng toàn đoạn. p000646 có hai vùng nghiêng, chỉ cơm đút lò ở ngoài; nghĩa thịt vẫn nằm trong vùng nghiêng sau khi đổi trật tự từ. Khớp phạm vi nghĩa của các vùng em trong XHTML package và DEC-P01-002.
    self_check: Ghi đúng việc khôi phục vùng nhấn mạnh và để tên món ngoài chữ nghiêng.
  - id: B21-R03
    original_severity: moderate
    segment_ids: [p000646]
    status: resolved
    translation_check: Cấu trúc nếu lúc nãy kết hợp cũng đã chẳng nuốt nổi giữ giả định nhìn lại bữa ăn vừa qua; không chuyển thành dự đoán tương lai hoặc khẳng định đã ăn món thay thế.
    self_check: Nhận diện đúng giả định về bữa ăn vừa qua.
  - id: B21-R04
    original_severity: moderate
    segment_ids: [p000651]
    status: resolved
    translation_check: Đối tượng ngã xuống là các pháp sư, nối trực tiếp với chi phí và thời gian đào tạo một pháp sư; không mở rộng lập luận trực tiếp sang toàn bộ binh lính.
    self_check: Ghi đúng giới hạn lập luận về pháp sư.
  - id: B21-R05
    original_severity: moderate
    segment_ids: [p000652]
    status: resolved
    translation_check: Cho đến tận mới đây và vẫn còn đóng quân giữ trạng thái kéo dài đến gần đây; không gán ngày điều động hoặc mốc đúng hai ngày trước. Tình huống địch có radar/ngòi nổ VT còn ta không có vẫn là giả định.
    self_check: Ghi đúng thời gian, trạng thái đóng quân và bất cân xứng vũ khí giả định; chọn ngòi nổ VT đúng handoff sửa.
  - id: B21-R06
    original_severity: moderate
    segment_ids: [p000654]
    status: resolved
    translation_check: Có thể đã chẳng giỏi giữ bất định và mốc quá khứ của khả năng quân sự; không khẳng định Einstein từng phục vụ quân đội. Đối lập giá trị đóng góp, súng/bút chì và ngoại lệ nhà khoa học điên còn nguyên.
    self_check: Nhãn phản thực được hiểu là nhận định giả định/bất định về năng lực trong quá khứ, không phải kết luận lịch sử; bản dịch không thêm sự kiện phục vụ quân đội.
  - id: B21-R07
    original_severity: minor
    segment_ids: [p000655]
    status: resolved
    translation_check: Ngay ở tuyến đầu diễn đạt vị trí tiền tuyến, không còn gợi số thứ tự tuyến. So sánh hiệu quả nghiên cứu và tránh lãng phí được giữ.
    self_check: Ghi đúng vị trí Nobel ở tuyến đầu.
  - id: B21-R08
    original_severity: minor
    segment_ids: [p000659]
    status: resolved
    translation_check: Phung phí vốn con người đến thế giữ mức độ lãng phí, bỏ lặp cùng nghĩa; điều kiện thiếu tài năng và giải pháp điều khỏi tiền tuyến còn nguyên.
    self_check: Ghi đúng việc bỏ lặp nghĩa.
  - id: B21-R09
    original_severity: minor
    segment_ids: [p000667]
    status: resolved
    translation_check: Không còn lượng nhiều gán cho số mạng được cứu; chỉ từ nối và được nghiêng. Hai thành tích cùng chủ thể và quan hệ cộng thêm được giữ.
    self_check: Ghi đúng cả việc bỏ lượng thêm và phạm vi nhấn mạnh.
  - id: B21-R10
    original_severity: minor
    segment_ids: [p000671]
    status: resolved
    translation_check: Số tù binh được nhận phụ thuộc khả năng quản lý của bốn mươi tám người; 48 là nhóm có năng lực xử lý, không phải trần tuyệt đối số tù binh. Những người bị bắt làm nguồn tin là lựa chọn tạm theo handoff, không thêm mục đích ban đầu của việc bắt người. Câu không xác định tổng quân số đơn vị hoặc chính sách bắt giữ.
    self_check: Ghi đúng cách dịch tạm và cả hai giới hạn không suy ra tổng quân số/không áp trần 48 tù binh.
focused_checks:
  emphasis:
    result: pass
    segment_ids: [p000644, p000645, p000646, p000667]
    basis: Đối chiếu trực tiếp XHTML của package với dấu sao trong translation, không dựa riêng trường text hoặc lời xác nhận của self-check.
  chronology_scope:
    result: pass
    segment_ids: [p000646, p000651, p000652, p000653, p000654, p000664, p000668]
    notes: Giữ giả định bữa ăn quá khứ, đối tượng pháp sư, trạng thái đóng quân đến gần đây, giả định Manhattan và bất định quá khứ về Einstein. Phần nghỉ phép/bố trí quân không thêm ngày mới; thành tích Rhine vẫn có mốc trước đó.
  p000671_ambiguity:
    result: pass_with_explicit_limits
    confidence: medium_high
    preferred_reading: Nhóm 48 người là chủ thể năng lực quản lý; tù binh là đối tượng ngầm được mạch bắt giữ và nuôi người hỗ trợ.
    retained_uncertainty: Không biết đây có phải toàn bộ quân số đơn vị hay năng lực xử lý bao gồm cụ thể những việc nào. Quản lý tù binh là cách giải ngữ cảnh tạm, không bảo toàn mọi độ mở từ vựng của động tác xử lý.
    rejected_inferences: [trần tuyệt đối 48 tù binh, xác nhận tổng quân số đơn vị là 48, chính sách bắt người chỉ để khai thác tin tức]
    alternative_if_more_literal_needed: đơn vị mình không nhận quá khả năng xử lý của bốn mươi tám người
    remaining_content: Giữ không dung thứ ngược đãi, hiếm có tù binh, phủ định tra tấn/ngược đãi, đối lập đám nghiệp dư, gánh nặng nuôi người và mức dễ hơn đôi chút.
  other_rows:
    result: Không phát hiện vấn đề mới có ý nghĩa vật chất trong 29 đoạn; giữ phủ định, câu hỏi nội tâm, chuyển điểm nhìn ở p000647, tự đính chính ở p000650 và dấu chú thích 22 ở p000670. Không mở nội dung chú thích ngoài package.
term_recommendations:
  - id: P-B21-01
    source_term: human capital
    proposed_vi: vốn con người
    segment_ids: [p000651, p000655, p000658, p000659]
    assessment: Dùng nhất quán trong translation/self-check; khớp reviewer ledger và P03-human-capital đang pending. Phù hợp mạch đầu tư, bảo vệ và lãng phí.
    alternative: vốn nhân lực
    status: pending
    canon: false
  - id: P-B21-02
    source_term: mage
    proposed_vi: pháp sư
    segment_ids: [p000651, p000667]
    assessment: Nhất quán với ledger và self-check; giữ người được đào tạo/chiến đấu, không thêm phân loại hoặc quân hàm.
    alternative: ma pháp sư
    status: pending
    canon: false
  - id: P-B21-03
    source_term: VT fuses
    proposed_vi: ngòi nổ VT
    segment_ids: [p000652]
    assessment: Khớp reviewer ledger, handoff sửa và self-check; giữ ký hiệu, không tự giải cơ chế. Đề xuất ban đầu ngòi nổ cận đích VT trong translator ledger được lưu như lịch sử, không phải lựa chọn áp dụng cuối.
    alternatives: [ngòi nổ cận đích VT, ngòi nổ tiệm cận VT]
    uncertainty: medium
    status: pending
    canon: false
  - id: P-B21-04
    source_term: rank-and-file soldier
    proposed_vi: người lính bình thường
    segment_ids: [p000654]
    assessment: Khớp hai ledger và self-check; diễn đạt người lính thông thường, không gán quân hàm binh nhì hoặc đánh giá yếu kém.
    alternatives: [binh lính thông thường, người lính trong hàng ngũ]
    status: pending
    canon: false
  - id: P-B21-05
    source_term: General Staff Office
    proposed_vi: Bộ Tổng tham mưu
    segment_ids: [p000665]
    assessment: Khớp ledger và self-check, dùng tạm cho cơ quan trình diện ở thủ đô; không xác lập tên canon, cơ cấu hay cấp bậc.
    alternative: cơ quan Tổng tham mưu
    uncertainty: medium
    status: pending
    canon: false
  - id: P-B21-06
    source_term: decoration
    proposed_vi: huân chương
    segment_ids: [p000668]
    assessment: Khớp lựa chọn chính trong ledger và self-check; bối cảnh trao thưởng chiến công hỗ trợ cách dùng tạm, không thêm loại, hạng hoặc chất liệu.
    alternatives: [phần thưởng quân sự, huân huy chương]
    ledger_note: Reviewer ledger ghi các phương án huy chương/phần thưởng, khác cách ghi alternatives ở initial review; lựa chọn chính vẫn khớp. Đây là phương án dự phòng, không phải sai lệch trong bản dịch cuối.
    uncertainty: medium
    status: pending
    canon: false
  - id: P-B21-07
    source_term: prisoners / captured information sources
    proposed_vi: tù binh / những người bị bắt làm nguồn tin
    segment_ids: [p000671]
    assessment: Khớp reviewer ledger, handoff sửa và self-check. Translator ledger còn cách gọi ban đầu để khai thác tin tức như lịch sử; bản cuối áp dụng đúng khuyến nghị mới, không tự xác lập mục đích bắt giữ hoặc tư cách pháp lý của mọi người bị bắt.
    alternative: người bị bắt / những nguồn tin bị bắt giữ
    uncertainty: medium
    status: pending
    canon: false
  - id: P-B21-08
    source_term: international laws
    proposed_vi: luật pháp quốc tế
    segment_ids: [p000672]
    assessment: Khớp ledger và self-check; giữ phạm vi rộng trong lời kể, không tự thu hẹp sang luật nhân đạo quốc tế hoặc tên công ước.
    alternative: luật quốc tế
    status: pending
    canon: false
ledger_status_check:
  translator_section: Cả 8 mục có status pending và canon false; giữ đề xuất ban đầu.
  reviewer_section: Cả 8 mục có status pending và canon false; 8 lựa chọn chính đều khớp translation cuối và self-check.
  selection_authority: Handoff review-fixes chỉ định áp dụng chapter6_b21_review_recommendations; khác biệt lịch sử ở P-B21-03/P-B21-07 không phải lỗi chưa sửa.
  canon_check: glossary và characters chưa có mục đã chốt; decisions chỉ duyệt đại từ/nhấn mạnh, không duyệt 8 thuật ngữ này. P03-human-capital trong glossary-pending cũng còn pending.
unresolved_findings: []
full_signoff: true
signoff_scope: Toàn bộ review nghĩa/văn phong của b21 được thông qua; B21-R01–R10 đã xử lý trong translation và self-check, không còn lỗi nghiêm trọng/vừa/nhẹ hoặc vấn đề mới có ý nghĩa vật chất. Đây không phải xác nhận hoàn tất pipeline hoặc duyệt canon.
risks:
  - p000671 vẫn có độ mở về quân số, phạm vi xử lý và tư cách người bị bắt; các lượt sau phải giữ giới hạn nêu trên.
  - VT, tên cơ quan và loại phần thưởng chỉ là lựa chọn cục bộ có căn cứ trong b21, chưa đủ để chốt cơ chế kỹ thuật hoặc lore.
  - Hai phần ledger có chức năng lưu đề xuất ban đầu và khuyến nghị sửa; không lấy lại P-B21-03/P-B21-07 cũ thay cho lựa chọn đã áp dụng theo handoff.
  - Validator và diff-check không được chạy trong lượt reviewer này; việc đạt điều kiện hoàn tất pipeline còn cần coordinator xác nhận kiểm tra và commit.
validator: not_run
diff_check: not_run
commit: null
next_action: Coordinator tiếp nhận full signoff, xác nhận hoặc chạy validator với primary b21 handoff/package cùng diff-check, rồi commit lô khi các kiểm tra bắt buộc đạt; giữ cả 8 lựa chọn pending/non-canon, không cần lượt sửa dịch thêm từ review này.
```
