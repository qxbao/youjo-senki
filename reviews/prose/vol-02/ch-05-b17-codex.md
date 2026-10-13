# Review — vol-02-ch-05-b17-review

Đã đối chiếu nội dung đủ 26 đoạn trong package hiện có với bản dịch và self-check. Báo cáo này là đánh giá trên package khớp bàn giao batch; chưa thể xác nhận đây là đầu vào được bàn giao review vì hash của hai handoff khác nhau. Trạng thái blocked chỉ áp dụng cho việc xác nhận đầu vào/hoàn tất task; các nhận xét dưới đây vẫn có căn cứ trực tiếp trên package đã đọc. Không mở EPUB/PDF, không sửa bản dịch, ledger hay handoff; không chép câu nguồn.

Hai ghi chú của translator được giải quyết bằng đề xuất tạm: giữ nguyên Daigongen và Zusho, dùng kính ngữ “đáng kính”; dùng “hỏa lực đáp lại tín hiệu cầu cứu” tại p000420, chưa xác định loại vũ khí hoặc bên khai hỏa. Quân hàm Serebryakov tạm diễn đạt “Sĩ quan cấp úy Serebryakov” vì đoạn nguồn không phân bậc. Các lựa chọn này đều pending, không phải canon.

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-05-b17-review
state: blocked
review_path: reviews/prose/vol-02/ch-05-b17-codex.md
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
files_written: [reviews/prose/vol-02/ch-05-b17-codex.md]
validator: not_run
diff_check: not_run
commit: null
inputs_read:
  - AGENTS.md
  - agents/shared.md
  - agents/reviewer.md
  - config/translation-pipeline.yml
  - handoffs/vol-02/ch-05-b17.yml
  - handoffs/vol-02/ch-05-b17-review.yml
  - work/vol-02/batches/ch-05-b17-source.jsonl
  - canon/glossary.yml
  - canon/style-guide.md
  - canon/characters.yml
  - canon/decisions.md
  - canon/glossary-pending.yml
  - work/run-state/pending-terms.yml#chapter5_b17_translation_proposals
  - work/run-state/pending-terms.yml#chapter5_b13_reviewer_recommendations
  - translations/vol-02/ch-05-b17.jsonl
  - reviews/semantic/vol-02/ch-05-b17-self-check.md
  - reviews/prose/vol-02/ch-05-b04-pending-terms-codex.md
hash_check:
  status: fail
  package_sha256_actual: 49cb1e17ffcdf82a282925db8d25fd7927b4cb06ce9751bb6176b4f40402be6e
  batch_handoff_expected: 49cb1e17ffcdf82a282925db8d25fd7927b4cb06ce9751bb6176b4f40402be6e
  review_handoff_expected: 9f3cfaf76f20cf2795f1d7738c7e56cd5a1aed23d2f3ee9a1258e9aa1f2ee603
  package_matches_batch_handoff: true
  package_matches_review_handoff: false
  canon_reference_hashes_match_batch_handoff: true
  source_sha256_metadata_consistent: true
  source_sha256_metadata: 3ac53161b6e093ba07203f284a400049cf902a3b0f51c0d3e40200867c13ae0a
  original_source_file_hash_recomputed: false
  source_units: 26
  translation_units: 26
  ordered_ids_equal: true
  contiguous_expected_range: true
  duplicate_or_missing_ids: false
  interpretation: 'Hash package chỉ xác nhận khớp bàn giao batch. Metadata source_sha256 không thay thế việc kiểm tra file sách; reviewer không được mở sách gốc.'
counts:
  segments_expected: 26
  segments_reviewed: 26
  serious: 0
  moderate: 7
  minor: 3
  findings_total: 10
  unresolved_findings: 10
  input_blockers: 1
  official_pending_entries_reviewed: 6
  term_recommendations: 10
input_blockers:
  - id: B17-HASH
    issue: 'Hash package trong review handoff không khớp file hiện có, dù batch handoff khớp.'
    resolution: 'Coordinator xác minh package nào được giao và sửa metadata bàn giao hoặc cung cấp đúng package trong lượt tiếp theo. Không tự đổi hash hay mặc định review handoff sai.'
findings:
  - id: B17-F01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000404
    related_segment_ids: [YS-LN02/Text/part0026.xhtml/p000411, YS-LN02/Text/part0026.xhtml/p000425]
    issue: 'Tự quy chiếu ngoài lời thoại chuyển sang tôi, trái quy ước nội tâm mình và không nhất quán trong lô.'
    evidence: 'p000404 là suy nghĩ về kế hoạch; sau lời thoại p000411 là tự thuật trong cùng điểm nhìn. p000425 không có dấu thoại trong XHTML và tiếp tục suy nghĩ về sống sót/rút lui.'
    resolution: 'Dùng mình trong câu đầu p000404, phần tự thuật sau lời thoại p000411 và các lần tôi ở p000425. Giữ tôi trong lời thoại trực tiếp p000411 và câu nói giả định p000412.'
  - id: B17-F02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000412
    issue: 'Thiếu chữ nghiêng dù self-check nói đã đối chiếu nhấn mạnh.'
    evidence: 'XHTML có em bao trọn lời chống chế; translation chỉ có dấu ngoặc kép. p000424 đã có nhấn mạnh tương ứng, không có dấu nhấn mạnh nguồn khác trong lô.'
    resolution: 'Bọc toàn bộ lời chống chế tiếng Việt bằng *...* theo DEC-P01-002; dấu ngoặc kép có thể giữ nhưng không thay thế chữ nghiêng.'
  - id: B17-F03
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000414
    issue: 'Cụ Đại Ngongen tự Việt hóa và tách tên Daigongen khi canon chưa có tên tương ứng.'
    evidence: 'Package chỉ cung cấp Daigongen, Zusho và kính ngữ. Không có căn cứ trong phạm vi này để gán nhân thân, quan hệ tuổi tác hay diễn giải điển tích.'
    resolution: 'Tạm dùng Daigongen đáng kính và Zusho; giữ câu về sự hữu dụng của hai tên gọi, không thêm chú giải hoặc định danh nhân vật lịch sử.'
  - id: B17-F04
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000417
    issue: 'Trinh sát luồn sâu thêm đặc tính độ sâu/luồn vào mà thuật ngữ tại chỗ không xác lập.'
    evidence: 'Nguồn dùng force recon và nhấn vào lực lượng hạn chế của nhóm so với đơn vị phản công; không mô tả một nhiệm vụ deep recon.'
    resolution: 'Tạm dùng nhóm làm nhiệm vụ trinh sát chiến đấu, giữ ý chỉ có sức chiến đấu của nhóm này. Đây là đề xuất theo nghĩa tại chỗ, không xác lập tên học thuyết hay binh chủng.'
  - id: B17-F05
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000420
    issue: 'Làn đạn cấp cứu khó hiểu và gợi nghĩa y tế, làm mờ quan hệ giữa cầu cứu và hỏa lực.'
    evidence: 'p000417 đã nêu báo động, p000419–420 nêu rút lui và nguy cơ bị nổ tung. SOS fire chỉ cho phép chọn nghĩa hỏa lực gắn với cầu cứu; chưa xác lập loại súng/pháo, quy trình gọi bắn hoặc bên khai hỏa.'
    resolution: 'Tạm dùng bị nổ tung dưới hỏa lực dồn dập đáp lại tín hiệu cầu cứu; giữ điều kiện không thoát được và vài phút chạy thoát thân. Không thêm pháo binh hoặc hỏa lực quân mình.'
  - id: B17-F06
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000423
    issue: 'Vô giá đổi ý không thể thay thế thành đánh giá giá trị.'
    evidence: 'Lập luận nối tính độc nhất với ý không có người thay thế ở p000424; bản dịch p000423 làm mất tiền đề này.'
    resolution: 'Dùng Con người không thể thay thế; mỗi chúng ta đều độc nhất. Giữ điều kiện tin vào tương lai và sắc thái diễn thuyết hơi khoa trương.'
  - id: B17-F07
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000428
    issue: 'Thiếu úy Serebryakov không khớp lựa chọn tạm gần nhất trong ledger, đồng thời package không xác định bậc cấp úy.'
    evidence: 'Canon characters/glossary chưa chốt. Ledger b17 đề xuất Trung úy, có phương án trung tính; self-check lại nói Thiếu úy theo dự án. Hai ánh xạ đều chưa phải chứng cứ về bậc cụ thể.'
    resolution: 'Tạm dùng Sĩ quan cấp úy Serebryakov trong trần thuật này; coordinator ghi lựa chọn và bất định vào ledger. Không suy ra thăng/giáng cấp và không tự đổi sang Trung úy như một sự thật.'
  - id: B17-F08
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000405
    issue: 'Kết thân làm yếu hình ảnh mời lính gác về làm khách và lệch mạch ẩn dụ ở p000409/p000417.'
    evidence: 'Nguồn đang nói bắt người để Tình báo trò chuyện, dùng giọng xã giao mỉa mai; bản dịch còn hiểu được nhờ câu đầu nhưng không giữ đủ hành động mời.'
    resolution: 'Cân nhắc mời lính gác địch ở chiến hào cảnh giới về kết bạn, để Tình báo trò chuyện với họ; không đổi trò chuyện thành tra tấn hoặc thêm phương thức thẩm vấn.'
  - id: B17-F09
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000419
    issue: 'Không gì giúp để lộ... tốt hơn là kết hợp từ gượng.'
    evidence: 'Đoạn giữ được thứ tự che giấu mana trước đó rồi ưu tiên tốc độ và rút lui; vấn đề ở cách nối câu tiếng Việt.'
    resolution: 'Cân nhắc Không có cách nào tốt hơn thuật thức bay để thả tín hiệu mana ra rồi tháo chạy khỏi chiến tuyến. Giữ giọng tán thưởng ở cuối, không thêm chữ nghiêng.'
  - id: B17-F10
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000424
    issue: 'Tôn quỷ dữ lên làm Chúa hơi nghiêng sang hành động phong thần, thay vì lời ca tụng đổi lấy khả năng dốc toàn lực.'
    evidence: 'Nguồn nêu sự sẵn sàng ca tụng quỷ dữ như Chúa trong vài phút để sống sót; không nói thay đổi địa vị thực thể.'
    resolution: 'Cân nhắc mình sẵn sàng ca tụng cả quỷ dữ như Chúa trong vài phút ấy để dốc toàn lực. Giữ *nhất định* ở lời quyết sống sót.'
unresolved_findings: [B17-F01, B17-F02, B17-F03, B17-F04, B17-F05, B17-F06, B17-F07, B17-F08, B17-F09, B17-F10]
coverage:
  p000404: 'Kế hoạch, đơn vị chủ công, không dự bị và nghi binh giữ đúng; F01.'
  p000405: 'Mục tiêu bắt sống và trò chuyện của Tình báo giữ đúng; F08.'
  p000406: 'Giữ đối tượng câu hỏi và mức tránh giao chiến; không phát hiện lỗi riêng.'
  p000407: 'Giữ lời xác nhận, chức danh chỉ huy và nhận định không thể chiến đấu với tân binh.'
  p000408: 'Giữ mệnh lệnh tạo kinh nghiệm đánh đêm và giọng cộc ở cuối; không thêm nhấn mạnh.'
  p000409: 'Thành ngữ phù hợp, giữ ẩn dụ xã giao và mỉa mai của cuộc bắt người.'
  p000410: 'Giữ tự sửa ý và độ dè dặt khi đánh giá tốt/xấu.'
  p000411: 'Giữ ưu tiên tốc độ/rút lui và trách nhiệm chỉ huy; F01.'
  p000412: 'Giữ nghĩa lời chống chế; thiếu nhấn mạnh, F02.'
  p000413: 'Giữ hai điều kiện đối lập và hai hậu quả; không biến giả định thành sự kiện.'
  p000414: 'Giữ không giết mà đánh bất tỉnh, huấn luyện và giọng đen tối; tên/kính ngữ cần F03.'
  p000415: 'Giữ đối lập lính/nông dân và tự sửa sang thường dân; không thêm phán xét đạo đức.'
  p000416: 'Giữ phân biệt cạnh xẻng/mặt phẳng và ý gần như muốn cho tân binh chỉ mang xẻng.'
  p000417: 'Giữ báo động, đánh hoặc chạy, mục tiêu tù binh và nguy cơ lỡ rút lui; F04.'
  p000418: 'Giữ ví von công việc/về nhà và câu ngắn.'
  p000419: 'Giữ trình tự che giấu rồi bộc lộ mana, tốc độ và tán thưởng thuật thức bay; F09.'
  p000420: 'Giữ vài phút, điều kiện không thoát và nguy cơ bị nổ tung; thuật ngữ cần F05.'
  p000421: 'Phát chí mạng phù hợp suy nghĩ chết nhanh để khỏi đau trong ngữ cảnh; không tự thêm vũ khí.'
  p000422: 'Giữ chuyển ý sang mong muốn tận hưởng cuộc sống.'
  p000423: 'Giữ ý không sinh ra đã muốn tự sát và điều kiện tin tương lai; F06.'
  p000424: 'Giữ tự quy chiếu mình, quyết tâm sống sót và phạm vi nhấn mạnh; F10.'
  p000425: 'Giữ hỗ trợ nhau nhưng không dừng, may bị bắt/xui chết trận; F01.'
  p000426: 'Lo lắng đúng mức giữ sắc thái phản ứng khiến Tanya ngạc nhiên; cô là đề xuất xưng hô tại chỗ, chưa canon.'
  p000427: 'Giữ lặp lo lắng đúng mức, giọng bất bình và câu hỏi về việc tập hợp người nghiện chiến tranh.'
  p000428: 'Giữ nhu cầu giãn ra/tìm ý kiến bình thường và hành động giơ tay; quân hàm cần F07.'
  p000429: 'Giữ mấy phút cuối nguy hiểm và việc hỗ trợ tân binh trên đường đến đó; Thiếu tá là pending.'
pending_terms_policy: 'Mọi mục dưới đây là đề xuất tạm; không nâng canon. Reviewer chỉ ghi báo cáo, coordinator cập nhật ledger/handoff.'
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
    rationale: 'Giữ lựa chọn ledger và bản dịch, không suy thêm cơ cấu tổ chức.'
  - id: vol02-ch05-b17-flight-formula
    source_term: flight formula
    proposed_vi: thuật thức bay
    alternatives_vi: [công thức bay]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000419]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ cách dùng thuật thức hiện có, không bổ sung cơ chế ma thuật.'
  - id: vol02-ch05-b17-major-rank
    source_term: Major
    proposed_vi: Thiếu tá
    alternatives_vi: [Major]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000429]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ ánh xạ tạm hiện hành; ledger gắn nhầm p000428, vị trí thực tế là p000429. Chưa xác lập hệ cấp bậc canon.'
  - id: vol02-ch05-b17-lieutenant-serebryakov
    source_term: Lieutenant Serebryakov
    proposed_vi: Sĩ quan cấp úy Serebryakov
    alternatives_vi: [Úy Serebryakov, Trung úy Serebryakov, Thiếu úy Serebryakov]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000428]
    volume: vol-02
    chapter: 5
    status: pending
    confidence: low_for_exact_rank
    rationale: 'Cách trung tính rõ nghĩa và hợp trần thuật hơn Úy; hai bậc cụ thể đều cần thêm chứng cứ. Ledger gắn nhầm p000429; không coi lệch với ledger là bằng chứng nhân vật đổi quân hàm.'
  - id: vol02-ch05-b17-venerable-daigongen
    source_term: venerable Daigongen
    proposed_vi: Daigongen đáng kính
    alternatives_vi: [ngài Daigongen, Cụ Daigongen]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000414]
    volume: vol-02
    chapter: 5
    status: pending
    confidence: medium_for_wording_low_for_identity
    rationale: 'Giữ cách viết nguồn và sắc thái kính ngữ; không xác định tuổi, danh tính lịch sử hoặc Việt hóa thành Đại Ngongen.'
    alternative_rationale: 'Ngài cũng mang kính ngữ nhưng giả định cách gọi người; Cụ thêm sắc thái tuổi tác nên ít trung tính hơn.'
  - id: vol02-ch05-b17-sos-fire
    source_term: SOS fire
    proposed_vi: hỏa lực đáp lại tín hiệu cầu cứu
    alternatives_vi: [hỏa lực yểm trợ khẩn cấp, hỏa lực cầu cứu, hỏa lực SOS]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000420]
    volume: vol-02
    chapter: 5
    status: pending
    confidence: medium_for_context_low_for_tactical_definition
    rationale: 'Liên hệ báo động và truy kích trong package ủng hộ hỏa lực gắn với cầu cứu. Chọn diễn đạt theo chức năng, giữ bất định về bên bắn và loại vũ khí.'
    alternative_rationale: 'Yểm trợ khẩn cấp rõ hơn nhưng gán chức năng yểm trợ; cầu cứu quá cô đọng và dễ hiểu thành hỏa lực tự phát tín hiệu; SOS giữ bất định nhưng kém tự nhiên. Không tự dùng một tên học thuyết pháo binh.'
  - id: B17-TR07
    source_term: Zusho
    proposed_vi: Zusho
    alternatives_vi: []
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000414]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ tên nguồn; phạm vi này không đủ để định danh hoặc thêm chú thích.'
  - id: B17-TR08
    source_term: warning trench
    proposed_vi: chiến hào cảnh giới
    alternatives_vi: [chiến hào tiền tiêu]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000405, YS-LN02/Text/part0026.xhtml/p000417]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ thống nhất hai lần và chức năng cảnh báo; tiền tiêu thêm giả định về vị trí.'
  - id: B17-TR09
    source_term: force recon
    proposed_vi: trinh sát chiến đấu
    alternatives_vi: [trinh sát bằng lực lượng]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000417]
    volume: vol-02
    chapter: 5
    status: pending
    confidence: medium_for_local_wording
    rationale: 'Diễn đạt tạm cho nhiệm vụ trinh sát có lực lượng chiến đấu; không thêm luồn sâu hoặc coi là tên đơn vị chuyên biệt. Chưa có căn cứ để chốt thuật ngữ học thuyết.'
  - id: B17-TR10
    source_term: mana signal
    proposed_vi: tín hiệu mana
    alternatives_vi: [dấu hiệu mana]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000419]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ cách dùng của bản dịch; không đồng nhất việc để lộ mana với phát tín hiệu cầu cứu tại đoạn sau.'
risks:
  - 'B17-HASH chặn xác nhận đúng đầu vào review; không công nhận batch hoàn tất.'
  - 'Ledger b17 đảo vị trí Major/Serebryakov giữa p000428 và p000429; có khóa status/rationale lặp ở mục SOS fire. Reviewer không sửa hoặc diễn giải khóa lặp như quyết định đã duyệt.'
  - 'Self-check tuyên bố đã đối chiếu nhấn mạnh và nhất quán mình nhưng bản dịch vẫn có F01/F02; cần kiểm tra lại sau sửa.'
  - 'Danh tính Daigongen/Zusho, định nghĩa chiến thuật SOS fire và bậc cụ thể Serebryakov vẫn bất định. Các đề xuất trung tính cho phép tiếp tục sau khi giải quyết hash, không xác lập lore.'
next_action: 'Coordinator giải quyết B17-HASH trước bước tiếp theo, ghi nhận các đề xuất pending và sửa mapping mã đoạn trong phạm vi của mình; bàn giao người giữ quyền sửa xử lý findings, chạy validator/diff-check rồi review lại bản sửa. Reviewer dừng sau báo cáo, không commit.'
```
