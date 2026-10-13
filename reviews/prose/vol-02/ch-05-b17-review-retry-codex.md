# Review — vol-02-ch-05-b17-review-retry

Hash package đã được xác nhận khớp cả handoff retry đã sửa và handoff batch gốc trước khi đối chiếu nội dung. Đã review đủ 26 đoạn p000404–p000429 trên package cục bộ và bản dịch hiện lưu. Lỗi đầu vào của lượt trước đã được giải quyết; đây là review hoàn tất, chưa phải xác nhận bản dịch đạt hoặc batch hoàn tất. Có 7 finding vừa và 3 finding nhẹ chưa được sửa.

Các lựa chọn thuật ngữ dưới đây đều tạm thời, không phải canon. Chọn cách trung tính khi thiếu chứng cứ; bất định thông thường không chặn review. Chỉ ghi báo cáo này; không mở sách gốc, không sửa bản dịch, ledger, handoff, canon, self-check hoặc checkpoint; không commit. Không chép câu nguồn.

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-05-b17-review-retry
state: done
review_path: reviews/prose/vol-02/ch-05-b17-review-retry-codex.md
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000404
  - YS-LN02/Text/part0026.xhtml/p000405
  - YS-LN02/Text/part0026.xhtml/p000406
  - YS-LN02/Text/part0026.xhtml/p000407
  - YS-LN02/Text/part0026.xhtml/p000408
  - YS-LN02/Text/part0026.xhtml/p000409
  - YS-LN02/Text/part0026.xhtml/p000410
  - YS-LN02/Text/part0026.xhtml/p000411
  - YS-LN02/Text/part0026.xhtml/p000412
  - YS-LN02/Text/part0026.xhtml/p000413
  - YS-LN02/Text/part0026.xhtml/p000414
  - YS-LN02/Text/part0026.xhtml/p000415
  - YS-LN02/Text/part0026.xhtml/p000416
  - YS-LN02/Text/part0026.xhtml/p000417
  - YS-LN02/Text/part0026.xhtml/p000418
  - YS-LN02/Text/part0026.xhtml/p000419
  - YS-LN02/Text/part0026.xhtml/p000420
  - YS-LN02/Text/part0026.xhtml/p000421
  - YS-LN02/Text/part0026.xhtml/p000422
  - YS-LN02/Text/part0026.xhtml/p000423
  - YS-LN02/Text/part0026.xhtml/p000424
  - YS-LN02/Text/part0026.xhtml/p000425
  - YS-LN02/Text/part0026.xhtml/p000426
  - YS-LN02/Text/part0026.xhtml/p000427
  - YS-LN02/Text/part0026.xhtml/p000428
  - YS-LN02/Text/part0026.xhtml/p000429
files_written: [reviews/prose/vol-02/ch-05-b17-review-retry-codex.md]
validator: not_run
diff_check: not_run
commit: null
inputs_read:
  - AGENTS.md
  - agents/shared.md
  - agents/reviewer.md
  - config/translation-pipeline.yml
  - handoffs/vol-02/ch-05-b17-review-retry.yml
  - handoffs/vol-02/ch-05-b17.yml
  - handoffs/vol-02/ch-05-b17-review.yml
  - reviews/prose/vol-02/ch-05-b17-codex.md
  - work/vol-02/batches/ch-05-b17-source.jsonl
  - canon/glossary.yml
  - canon/style-guide.md
  - canon/characters.yml
  - canon/decisions.md
  - canon/glossary-pending.yml
  - work/run-state/pending-terms.yml#chapter5_b17_translation_proposals
  - work/run-state/pending-terms.yml#chapter5_b13_reviewer_recommendations
  - work/run-state/pending-terms.yml#vol02-ch01-b02-lieutenant
  - work/run-state/pending-terms.yml#vol02-ch05-b04-lieutenant-serebryakov
  - reviews/prose/vol-02/ch-05-b04-pending-terms-codex.md
  - translations/vol-02/ch-05-b17.jsonl
  - reviews/semantic/vol-02/ch-05-b17-self-check.md
hash_check:
  status: pass
  verified_before_content_review: true
  package_sha256_actual: 49cb1e17ffcdf82a282925db8d25fd7927b4cb06ce9751bb6176b4f40402be6e
  corrected_review_retry_handoff_expected: 49cb1e17ffcdf82a282925db8d25fd7927b4cb06ce9751bb6176b4f40402be6e
  original_batch_handoff_expected: 49cb1e17ffcdf82a282925db8d25fd7927b4cb06ce9751bb6176b4f40402be6e
  package_matches_corrected_review_retry_handoff: true
  package_matches_original_batch_handoff: true
  original_review_handoff_expected: 9f3cfaf76f20cf2795f1d7738c7e56cd5a1aed23d2f3ee9a1258e9aa1f2ee603
  previous_blocker: B17-HASH
  previous_blocker_disposition: resolved_by_corrected_retry_handoff
  original_review_handoff_used_for_context_only: true
  canon_reference_hashes_match_batch_handoff: true
  source_sha256_metadata_consistent: true
  source_sha256_metadata: 3ac53161b6e093ba07203f284a400049cf902a3b0f51c0d3e40200867c13ae0a
  original_source_file_hash_recomputed: false
  source_units: 26
  translation_units: 26
  ordered_ids_equal: true
  contiguous_expected_range: true
  duplicate_or_missing_ids: false
  interpretation: 'Hash package xác nhận đúng đầu vào retry và batch. Metadata source_sha256 nhất quán nhưng không phải phép kiểm tra lại file sách; reviewer không mở sách gốc.'
counts:
  segments_expected: 26
  segments_reviewed: 26
  serious: 0
  moderate: 7
  minor: 3
  findings_total: 10
  unresolved_findings: 10
  input_blockers: 0
  official_pending_entries_reviewed: 6
  term_recommendations: 10
input_blockers: []
findings:
  - id: B17-F01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000404
    related_segment_ids: [YS-LN02/Text/part0026.xhtml/p000411, YS-LN02/Text/part0026.xhtml/p000425]
    issue: 'Tự quy chiếu ngoài lời thoại dùng tôi xen mình, trái DEC-P01-001 tại p000404 và phần tự thuật p000411.'
    evidence: 'p000404 trình bày kế hoạch trong điểm nhìn Tanya; p000411 phân biệt rõ lời nói với phần tự thuật sau đó. p000425 không có dấu thoại trong XHTML và nằm trong chuỗi suy nghĩ về sống sót, nhưng cấu trúc trình bày ý và lời đáp p000426 cũng cho phép hiểu là lời được thuật lại.'
    resolution: 'Đổi tự quy chiếu thành mình ở câu đầu p000404 và sau lời thoại p000411. Tạm dùng mình tại hai vị trí tôi trong p000425 theo điểm nhìn liên tục; giữ chúng ta cho tập thể. Giữ tôi trong lời thoại p000411 và lời chống chế giả định p000412.'
    alternatives: 'Nếu chọn p000425 là lời nói được thuật lại, có thể giữ tôi tại riêng đoạn đó và ghi rõ lý do; không tự thêm dấu thoại hoặc coi cách đọc này đã được nguồn xác nhận.'
  - id: B17-F02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000412
    issue: 'Thiếu nhấn mạnh trong bản dịch, dù self-check nói đã đối chiếu XHTML.'
    evidence: 'em bao trọn lời chống chế giả định; bản dịch chỉ có ngoặc kép. Trong lô, nguồn có em tại p000412 và p000424; dấu *nhất định* ở p000424 giữ được nhấn mạnh quyết tâm.'
    resolution: 'Bọc toàn bộ lời chống chế tiếng Việt bằng *...* theo DEC-P01-002. Có thể giữ ngoặc kép, nhưng không dùng chúng thay cho chữ nghiêng; không nghiêng cả câu dẫn.'
  - id: B17-F03
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000414
    issue: 'Cụ Đại Ngongen tự tách/Việt hóa tên Daigongen và thêm sắc thái tuổi tác khi chưa có canon.'
    evidence: 'Package có tên Daigongen, Zusho và kính ngữ; không cung cấp định danh lịch sử hay quan hệ thân tộc. Ledger cũng chỉ là đề xuất, không xác nhận dạng tên Việt.'
    resolution: 'Tạm dùng Daigongen đáng kính và giữ Zusho. Giữ giọng đen tối của lời nhận xét về sự hữu dụng; không thêm chú giải điển tích hoặc gán nhân thân.'
  - id: B17-F04
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000417
    issue: 'Trinh sát luồn sâu chuyển loại nhiệm vụ sang đặc tính độ sâu mà package không xác lập.'
    evidence: 'force recon bổ nghĩa cho nhiệm vụ của nhóm; lập luận so sức chiến đấu hạn chế của nhóm với đơn vị phản công trong chiến hào. Không có mô tả độ sâu hoặc tên một đơn vị đặc nhiệm cụ thể.'
    resolution: 'Tạm dùng nhóm làm nhiệm vụ trinh sát chiến đấu; giữ ý chỉ có sức chiến đấu của nhóm ấy, mục tiêu bắt tù binh và yêu cầu rút lui ngay. Đây là cách diễn đạt tại chỗ, chưa chốt thuật ngữ học thuyết.'
  - id: B17-F05
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000420
    issue: 'Làn đạn cấp cứu gợi nghĩa y tế và không làm rõ hỏa lực gắn với cầu cứu.'
    evidence: 'p000417 nêu báo động, p000419–420 chuyển sang rút lui và nguy cơ bị nổ tung. SOS fire chưa xác định loại vũ khí, bên khai hỏa hoặc quy trình gọi bắn; không được đồng nhất với việc bộc lộ mana ở p000419.'
    resolution: 'Tạm dùng bị nổ tung dưới hỏa lực dồn dập đáp lại tín hiệu cầu cứu. Giữ vài phút chạy thoát thân và điều kiện không thoát được; không thêm pháo binh, quân mình hoặc quân địch.'
  - id: B17-F06
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000423
    issue: 'Vô giá đổi ý không thể thay thế thành đánh giá giá trị.'
    evidence: 'Lập luận nối tính độc nhất với việc không có người thay thế tại p000424. Bản dịch hiện tại làm mất tiền đề không thể thay thế dù vẫn giữ độc nhất.'
    resolution: 'Dùng Con người không thể thay thế; mỗi chúng ta đều độc nhất. Giữ điều kiện còn tin vào tương lai và giọng diễn thuyết khoa trương.'
  - id: B17-F07
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000428
    issue: 'Thiếu úy Serebryakov lệch đề xuất Trung úy gần nhất trong chương, trong khi nguồn tại chỗ không phân bậc cấp úy.'
    evidence: 'Ledger lịch sử từng đề xuất Thiếu úy dựa trên đoạn khác, nhưng b13/b17 đề xuất Trung úy; b04 từng chọn cấp úy trung tính. Đây là lịch sử đề xuất mâu thuẫn, không phải chứng cứ đã kiểm tra về thay đổi quân hàm. Canon glossary/characters chưa chốt.'
    resolution: 'Tạm dùng sĩ quan cấp úy Serebryakov trong trần thuật p000428 để không phân bậc. Giữ tên Serebryakov; không suy ra thăng hoặc giáng cấp. Coordinator ghi lý do chọn trung tính và mã đoạn đúng, không tự nâng canon.'
  - id: B17-F08
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000405
    issue: 'Kết thân giữ ý xã giao nhưng làm mờ hành động mời lính gác về làm khách, yếu hơn mạch mỉa mai p000409/p000417.'
    evidence: 'Mục tiêu bắt sống đã có ở câu đầu; hình ảnh mời và trò chuyện cố ý giảm nhẹ cuộc bắt người.'
    resolution: 'Cân nhắc mời lính gác địch ở chiến hào cảnh giới về kết bạn, để Tình báo trò chuyện với họ. Không thêm tra tấn hoặc phương thức thẩm vấn.'
  - id: B17-F09
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000419
    issue: 'Không gì giúp để lộ... tốt hơn là kết hợp từ gượng.'
    evidence: 'Nghĩa cơ bản và trình tự che giấu mana trước đó rồi ưu tiên tốc độ/rút lui được giữ; lỗi nằm ở cách nối câu tiếng Việt.'
    resolution: 'Cân nhắc Không có cách nào tốt hơn thuật thức bay để thả tín hiệu mana ra rồi tháo chạy khỏi chiến tuyến. Giữ lời tán thưởng cuối đoạn; không thêm chữ nghiêng.'
  - id: B17-F10
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000424
    issue: 'Tôn quỷ dữ lên làm Chúa nghiêng sang phong thần, trong khi hành động tại chỗ là ca tụng.'
    evidence: 'Lời sẵn sàng ca tụng trong vài phút gắn với dốc toàn lực để sống sót; chưa nói thay đổi địa vị thực thể.'
    resolution: 'Cân nhắc mình sẵn sàng ca tụng cả quỷ dữ như Chúa trong vài phút ấy để dốc toàn lực. Giữ nhấn mạnh *nhất định* và không thêm diễn giải tôn giáo.'
unresolved_findings: [B17-F01, B17-F02, B17-F03, B17-F04, B17-F05, B17-F06, B17-F07, B17-F08, B17-F09, B17-F10]
previous_review_disposition:
  B17-HASH: 'Đã giải quyết bằng hash của handoff retry; không còn chặn review.'
  B17-F01: 'Còn mở; bổ sung bất định tại riêng p000425, không khẳng định dấu thoại thiếu đồng nghĩa tuyệt đối với không được thuật lại lời nói.'
  B17-F02_to_F10: 'Đã đối chiếu lại trên bản dịch hiện lưu, còn mở; giữ ID để không đếm trùng với báo cáo cũ.'
  metadata_note: 'Không lặp nhận xét khóa status/rationale của SOS fire bị trùng trong báo cáo cũ: mục b17 hiện đọc có một cặp khóa này.'
coverage:
  p000404: 'Giữ kế hoạch, đơn vị chủ công, không dự bị, nghi binh; F01.'
  p000405: 'Giữ mục tiêu bắt sống và trò chuyện của Tình báo; F08.'
  p000406: 'Giữ đối tượng câu hỏi và mức tránh giao chiến; không có finding riêng.'
  p000407: 'Giữ lời xác nhận, cách gọi chỉ huy và khó chiến đấu khi có tân binh đi cùng.'
  p000408: 'Giữ chỉ dẫn cho kinh nghiệm đánh đêm và giọng cộc ở cuối; không tự thêm nhấn mạnh.'
  p000409: 'Giữ thành ngữ, xã giao mỉa mai và lời mời binh lính địch sang chơi.'
  p000410: 'Giữ tự sửa ý và sự dè dặt trước đánh giá tốt/xấu.'
  p000411: 'Giữ ưu tiên tốc độ/rút lui và trách nhiệm chỉ huy; phần tự thuật có F01.'
  p000412: 'Giữ nghĩa chống chế; thiếu em tương ứng, F02.'
  p000413: 'Giữ hai điều kiện đối lập và hậu quả; không biến giả định thành sự kiện.'
  p000414: 'Giữ không giết mà đánh bất tỉnh, trải nghiệm huấn luyện, sống dở chết dở; tên/kính ngữ có F03.'
  p000415: 'Giữ lính/nông dân và tự sửa sang thường dân; không thêm phán xét đạo đức.'
  p000416: 'Giữ phân biệt cạnh/mặt phẳng xẻng và ý gần như muốn tân binh chỉ mang xẻng.'
  p000417: 'Giữ báo động, đánh/chạy, tù binh, tiêu hao vô vọng và lỡ rút lui; loại nhiệm vụ có F04.'
  p000418: 'Giữ ví von xong việc/về nhà và câu ngắn.'
  p000419: 'Giữ mana đã che giấu đến lúc ấy, sau đó ưu tiên tốc độ và bay thoát; F09 về prose.'
  p000420: 'Giữ vài phút và điều kiện không thoát; F05, chọn cách trung tính không xác định bên bắn.'
  p000421: 'Phát chí mạng phù hợp ý chết nhanh khỏi đau; không thêm loại vũ khí.'
  p000422: 'Giữ chuyển ý sang mong muốn tận hưởng cuộc sống.'
  p000423: 'Giữ ý không sinh ra đã muốn tự sát và điều kiện tin tương lai; F06.'
  p000424: 'Giữ mình, không có người thay thế và quyết tâm sống sót; nhấn mạnh đúng; F10.'
  p000425: 'Giữ hỗ trợ lẫn nhau nhưng không dừng, may bị bắt/xui chết trận; lựa chọn điểm nhìn tạm tại F01.'
  p000426: 'Giữ phản ứng lo lắng đúng mức; cô là lựa chọn thoại tạm, không xác lập canon về quan hệ.'
  p000427: 'Giữ lặp lo lắng đúng mức, giọng bất bình và câu hỏi về việc tập hợp người nghiện chiến tranh.'
  p000428: 'Giữ tìm ý kiến bình thường và Serebryakov giơ tay; quân hàm có F07.'
  p000429: 'Giữ mấy phút cuối nguy hiểm và hỗ trợ tân binh trên đường đến đó; Thiếu tá tạm phù hợp, chưa canon.'
pending_terms_policy: 'Các đề xuất chỉ áp dụng tạm; coordinator ghi ledger/handoff và translator áp dụng nhất quán. Không chờ người dùng cho bất định thông thường, không nâng canon.'
pending_terms: []
term_recommendations:
  - id: vol02-ch05-b17-first-company
    source_term: First Company
    proposed_vi: Đại đội Một
    alternatives_vi: [Đại đội thứ nhất]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000404]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ tên đơn vị gọn của ledger/bản dịch; không suy thêm cơ cấu tổ chức.'
    alternative_rationale: 'Đại đội thứ nhất cùng nghĩa nhưng khác quy ước tên; chưa có lý do đổi riêng ở lô này.'
  - id: vol02-ch05-b17-flight-formula
    source_term: flight formula
    proposed_vi: thuật thức bay
    alternatives_vi: [công thức bay]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000419]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ cách gọi thuật thức hiện có và ba lần lặp; không bổ sung cơ chế ma thuật.'
    alternative_rationale: 'Công thức bay sát hình thức từ nhưng dễ gợi công thức tính toán; chưa có căn cứ buộc đổi.'
  - id: vol02-ch05-b17-major-rank
    source_term: Major
    proposed_vi: Thiếu tá
    alternatives_vi: [Major]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000429]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ ánh xạ tạm hiện hành; nguồn tại p000429 có lời gọi quân hàm này. Ledger b17 ghi nhầm p000428.'
    alternative_rationale: 'Giữ Major tránh Việt hóa hệ quân hàm nhưng kém tự nhiên trong lời thoại; không cần đổi lựa chọn tạm hiện có.'
  - id: vol02-ch05-b17-lieutenant-serebryakov
    source_term: Lieutenant Serebryakov
    proposed_vi: sĩ quan cấp úy Serebryakov
    alternatives_vi: [Úy Serebryakov, Trung úy Serebryakov, Thiếu úy Serebryakov]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000428]
    volume: vol-02
    chapter: 5
    status: pending
    confidence: medium_for_neutral_wording_low_for_exact_rank
    rationale: 'Trung tính giữa các đề xuất lịch sử mâu thuẫn; rõ nghĩa trong trần thuật, không xác lập bậc cụ thể. Ledger b17 ghi nhầm p000429.'
    alternative_rationale: 'Úy gọn nhưng thiếu tự nhiên và không phải tên quân hàm chính thức đã chốt; Trung úy theo b13/b17 và Thiếu úy theo lịch sử cũ đều thiếu chứng cứ phân bậc được kiểm tra trong phạm vi task.'
  - id: vol02-ch05-b17-venerable-daigongen
    source_term: venerable Daigongen
    proposed_vi: Daigongen đáng kính
    alternatives_vi: [ngài Daigongen, Cụ Daigongen]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000414]
    volume: vol-02
    chapter: 5
    status: pending
    confidence: medium_for_wording_low_for_identity
    rationale: 'Giữ chính tả tên và kính ngữ, không đoán nhân thân, tuổi hoặc dạng Hán Việt.'
    alternative_rationale: 'Ngài giữ kính ngữ nhưng thêm cách gọi cá nhân; Cụ thêm tuổi tác nên kém trung tính. Không dùng Đại Ngongen khi chưa có chứng cứ cho cách tách tên.'
  - id: vol02-ch05-b17-sos-fire
    source_term: SOS fire
    proposed_vi: hỏa lực đáp lại tín hiệu cầu cứu
    alternatives_vi: [hỏa lực cầu cứu, hỏa lực SOS, hỏa lực yểm trợ khẩn cấp]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000420]
    volume: vol-02
    chapter: 5
    status: pending
    confidence: medium_for_context_low_for_tactical_definition
    rationale: 'Diễn đạt chức năng gắn với cầu cứu trong ngữ cảnh báo động/rút lui; không xác định bên bắn, loại vũ khí hoặc quy trình. Quan hệ đáp lại là cách đọc tạm có căn cứ ngữ cảnh, chưa phải định nghĩa học thuyết.'
    alternative_rationale: 'Hỏa lực cầu cứu quá gọn, dễ hiểu là dùng đạn phát tín hiệu; hỏa lực SOS giữ bất định nhưng cần người đọc hiểu SOS; yểm trợ khẩn cấp thêm chức năng yểm trợ. Làn đạn cấp cứu không rõ nghĩa.'
  - id: B17-TR07
    source_term: Zusho
    proposed_vi: Zusho
    alternatives_vi: []
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000414]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ tên nguyên dạng; chưa đủ chứng cứ cho nhân thân hoặc phiên âm Việt khác.'
    alternative_rationale: 'Chờ thêm ngữ cảnh chỉ áp dụng định danh, không chặn dịch; không có phương án tên Việt khác có căn cứ trong package này.'
  - id: B17-TR08
    source_term: warning trench
    proposed_vi: chiến hào cảnh giới
    alternatives_vi: [chiến hào tiền tiêu]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000405, YS-LN02/Text/part0026.xhtml/p000417]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ chức năng cảnh báo và nhất quán hai lần trong bản dịch.'
    alternative_rationale: 'Tiền tiêu thêm thông tin vị trí; cảnh giới ít suy diễn hơn.'
  - id: B17-TR09
    source_term: force recon
    proposed_vi: trinh sát chiến đấu
    alternatives_vi: [trinh sát bằng lực lượng]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000417]
    volume: vol-02
    chapter: 5
    status: pending
    confidence: medium_for_local_wording_low_for_doctrine
    rationale: 'Giữ loại nhiệm vụ trinh sát có sức chiến đấu, không thêm luồn sâu hoặc xác lập tên binh chủng. Dùng nhóm làm nhiệm vụ để giữ quan hệ nhóm/nhiệm vụ của nguồn.'
    alternative_rationale: 'Trinh sát bằng lực lượng sát hình thức nhưng gượng; trinh sát luồn sâu thêm chiều sâu không được xác lập. Chưa đủ chứng cứ gọi đây là thuật ngữ học thuyết chính thức.'
  - id: B17-TR10
    source_term: mana signal
    proposed_vi: tín hiệu mana
    alternatives_vi: [dấu hiệu mana]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000419]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ cách dùng bản dịch và thời điểm thôi che giấu khi rút lui; không đồng nhất với tín hiệu cầu cứu tại p000420.'
    alternative_rationale: 'Dấu hiệu mana ít gợi phát tín hiệu chủ động nhưng yếu sắc thái signal; chưa cần thay lựa chọn nhất quán hiện có.'
risks:
  - 'B17-F01–F10 còn mở: state done chỉ xác nhận reviewer hoàn tất nhiệm vụ, không xác nhận batch đạt điều kiện completion.'
  - 'Ledger b17 đảo mã đoạn Major/Serebryakov; coordinator cần ghi đúng p000429/p000428 trong phạm vi quyền của mình.'
  - 'Self-check tuyên bố nhất quán mình và đã kiểm tra p000412 nhưng bản dịch còn F01/F02; cần đối chiếu lại sau sửa.'
  - 'Daigongen/Zusho, loại nhiệm vụ force recon, SOS fire và bậc cụ thể Serebryakov còn bất định; đã chọn phương án tạm, không có yêu cầu dừng chờ quyết định canon.'
  - 'p000425 có thể được đọc là lời nói được thuật lại; đề xuất mình là lựa chọn điểm nhìn tạm, không xác nhận cách đọc duy nhất.'
next_action: 'Coordinator tiếp nhận báo cáo, ghi đề xuất và mapping pending đúng mã đoạn; bàn giao người giữ quyền sửa xử lý findings, rồi chạy validator/diff-check và review bản sửa theo pipeline. Reviewer dừng sau báo cáo, không thực hiện các bước đó và không commit.'
```
