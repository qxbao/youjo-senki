# Review — vol-02-ch-05-b18-review

Đã đối chiếu đủ 35 đoạn p000430–p000464 về nghĩa, văn phong, điểm nhìn, thuật ngữ, tính nhất quán và nhấn mạnh. Package hiện có khớp hash bàn giao batch, số từ, thứ tự và metadata nguồn; hash bàn giao review chỉ có 48 ký tự và không khớp. Vì vậy các nhận xét dưới đây có căn cứ trên package khớp batch, nhưng chưa chứng nhận đúng đầu vào bàn giao review. Coordinator cần xử lý sai lệch metadata trước bước tiếp theo; reviewer không sửa handoff.

Đã đọc self-check như báo cáo translator. Self-check không chứa ghi chú riêng tại p000460 và trường notes của cả 35 đoạn đều rỗng; yêu cầu xét p000460 chỉ được nêu trong review handoff. Báo cáo vẫn xử lý trực tiếp câu dịch tại mã này, không giả định có một ghi chú chưa được cung cấp.

Mọi lựa chọn thuật ngữ/xưng hô dưới đây là đề xuất tạm, không phải canon. Không mở EPUB/PDF, không sao chép câu nguồn, không sửa translations/, canon, ledger, handoff hoặc self-check. Không tạo graph hay đầu ra phụ.

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-05-b18-review
state: blocked
review_path: reviews/prose/vol-02/ch-05-b18-codex.md
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000430
  - YS-LN02/Text/part0026.xhtml/p000431
  - YS-LN02/Text/part0026.xhtml/p000432
  - YS-LN02/Text/part0026.xhtml/p000433
  - YS-LN02/Text/part0026.xhtml/p000434
  - YS-LN02/Text/part0026.xhtml/p000435
  - YS-LN02/Text/part0026.xhtml/p000436
  - YS-LN02/Text/part0026.xhtml/p000437
  - YS-LN02/Text/part0026.xhtml/p000438
  - YS-LN02/Text/part0026.xhtml/p000439
  - YS-LN02/Text/part0026.xhtml/p000440
  - YS-LN02/Text/part0026.xhtml/p000441
  - YS-LN02/Text/part0026.xhtml/p000442
  - YS-LN02/Text/part0026.xhtml/p000443
  - YS-LN02/Text/part0026.xhtml/p000444
  - YS-LN02/Text/part0026.xhtml/p000445
  - YS-LN02/Text/part0026.xhtml/p000446
  - YS-LN02/Text/part0026.xhtml/p000447
  - YS-LN02/Text/part0026.xhtml/p000448
  - YS-LN02/Text/part0026.xhtml/p000449
  - YS-LN02/Text/part0026.xhtml/p000450
  - YS-LN02/Text/part0026.xhtml/p000451
  - YS-LN02/Text/part0026.xhtml/p000452
  - YS-LN02/Text/part0026.xhtml/p000453
  - YS-LN02/Text/part0026.xhtml/p000454
  - YS-LN02/Text/part0026.xhtml/p000455
  - YS-LN02/Text/part0026.xhtml/p000456
  - YS-LN02/Text/part0026.xhtml/p000457
  - YS-LN02/Text/part0026.xhtml/p000458
  - YS-LN02/Text/part0026.xhtml/p000459
  - YS-LN02/Text/part0026.xhtml/p000460
  - YS-LN02/Text/part0026.xhtml/p000461
  - YS-LN02/Text/part0026.xhtml/p000462
  - YS-LN02/Text/part0026.xhtml/p000463
  - YS-LN02/Text/part0026.xhtml/p000464
files_written: [reviews/prose/vol-02/ch-05-b18-codex.md]
validator: not_run
diff_check: not_run
commit: null
inputs_read:
  - AGENTS.md
  - agents/shared.md
  - agents/reviewer.md
  - config/translation-pipeline.yml
  - handoffs/vol-02/ch-05-b18.yml
  - handoffs/vol-02/ch-05-b18-review.yml
  - work/vol-02/batches/ch-05-b18-source.jsonl
  - segments/vol-02/manifest.yml
  - canon/glossary.yml
  - canon/style-guide.md
  - canon/characters.yml
  - canon/decisions.md
  - canon/glossary-pending.yml
  - work/run-state/pending-terms.yml
  - reviews/semantic/vol-02/ch-05-b18-self-check.md
  - translations/vol-02/ch-05-b18.jsonl
  - reviews/prose/vol-02/ch-05-b17-codex.md
hash_check:
  status: fail
  package_sha256_actual: f32e7fecfce1d77df1322681680ba6cca9c96eeefc28b1ecc4a14b41ba92674c
  batch_handoff_expected: f32e7fecfce1d77df1322681680ba6cca9c96eeefc28b1ecc4a14b41ba92674c
  review_handoff_expected: 6b81f3f3974cdefb5f9faffaf0d996b0ba8e8cfabfe181f0
  review_handoff_hash_length: 48
  package_matches_batch_handoff: true
  package_matches_review_handoff: false
  canon_reference_hashes_match_batch_handoff: true
  source_sha256_metadata_consistent: true
  source_sha256_metadata: 3ac53161b6e093ba07203f284a400049cf902a3b0f51c0d3e40200867c13ae0a
  original_source_file_hash_recomputed: false
order_check:
  status: pass
  source_units: 35
  translation_units: 35
  exact_expected_id_sequence: true
  source_translation_order_matches: true
  source_word_count_actual: 879
  source_word_count_expected: 879
counts:
  reviewed_segments: 35
  serious: 0
  moderate: 9
  minor: 3
  total_findings: 12
  translation_findings: 11
  handoff_findings: 1
  missing_emphasis_spans: 6
findings:
  - id: B18-HASH
    severity: moderate
    segment_id: null
    issue: 'Hash bàn giao review không phải SHA-256 đầy đủ và không khớp package.'
    evidence: 'Giá trị review chỉ có 48 ký tự; hash thực tế đủ 64 ký tự khớp bàn giao batch. Cả 35 mã đoạn và 879 từ đúng phạm vi.'
    resolution: 'Coordinator xác minh rồi sửa metadata bàn giao review trong phạm vi của mình. Chưa chứng nhận đầu vào review hoặc công nhận batch hoàn tất; không sửa package để khớp một hash lỗi.'
  - id: B18-F01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000438
    issue: 'Tôi trong tự quy chiếu nội tâm Tanya lệch DEC-P01-001 và mình ở p000442.'
    evidence: 'Đây là suy nghĩ xen giữa các mục tổng kết, không có dấu thoại; p000442 tiếp tục cùng điểm nhìn trước khi chuyển sang Grantz ở p000443–444.'
    resolution: 'Đổi tôi thành mình tại p000438. Giữ tôi trong lời thoại p000431–432/p000441. Không áp quy ước Tanya cho Grantz.'
  - id: B18-F02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000443
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000443
      - YS-LN02/Text/part0026.xhtml/p000451
      - YS-LN02/Text/part0026.xhtml/p000454
      - YS-LN02/Text/part0026.xhtml/p000458
      - YS-LN02/Text/part0026.xhtml/p000461
      - YS-LN02/Text/part0026.xhtml/p000462
    issue: 'Mất cả sáu span nhấn mạnh của nguồn, trái DEC-P01-002.'
    evidence: 'XHTML có một em ở mỗi mã trên; bản dịch không có dấu Markdown tương ứng. Dấu ngoặc kép ở p000461 không thay cho chữ nghiêng.'
    resolution: 'Đánh *...* cho phần từ Pháp sư thường được đãi ngộ tốt đến hết p000443; câu Cô ta đúng là đáng sợ ở p000451; câu Có lẽ mình làm được! ở p000454; câu điều kiện Nếu tôi mắc lỗi... ở p000458; chỉ cụm trách nhiệm tập thể ở p000461; hai câu đầu Tối nay.../Nên đi ngủ... ở p000462. Giữ phần kể còn lại ngoài dấu nhấn mạnh; không tự thêm chữ nghiêng ở p000442 hoặc p000456–460.'
  - id: B18-F03
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000431
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000431, YS-LN02/Text/part0026.xhtml/p000440]
    issue: 'Thiếu úy gán bậc cụ thể cho Serebryakov dù package chỉ nêu Lieutenant và ledger b17 đã chọn cách trung tính.'
    evidence: 'Hai mục chapter5_b17_translation_proposals và chapter5_b17_reviewer_recommendations đều dùng sĩ quan cấp úy Serebryakov; các bậc cũ khác nhau còn pending. Không có chứng cứ nhân vật đổi quân hàm.'
    resolution: 'Tạm dùng Cô với tôi... ở đầu thoại p000431 để tránh câu gọi cứng và không gán bậc; dùng Sĩ quan cấp úy Serebryakov trong trần thuật p000440. Cô là lựa chọn giao tiếp tại chỗ, không canon; Magic Second Lieutenant của Grantz ở p000444 vẫn giữ thiếu úy ma pháp vì nguồn phân bậc rõ.'
  - id: B18-F04
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000456
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000456, YS-LN02/Text/part0026.xhtml/p000463]
    issue: 'Không quân khiến Aerial dễ bị hiểu thành tên quân chủng và lệch lựa chọn Trên không trong ledger chương này.'
    evidence: 'chapter5_b03_translation_proposals chọn Trên không để không gán đơn vị vào Air Force. Hai tên ở batch này khác nhau vì nguồn có/không có yếu tố xung kích; khác biệt đó cần được giữ.'
    resolution: 'Tạm dùng Tiểu đoàn Pháp sư Xung kích Trên không số 203 ở p000456 và Tiểu đoàn Pháp sư Trên không số 203 ở p000463; không tự thêm Xung kích vào tên rút gọn. Đây là đề xuất tên đơn vị, không chốt cơ cấu quân đội.'
  - id: B18-F05
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000460
    issue: 'Thường là phe an toàn hơn thêm tần suất, gợi phe phái và làm mờ so sánh tương đối giữa những người coi nhẹ Tanya.'
    evidence: 'Nguồn phân biệt những người lấy khả năng của đứa trẻ làm động lực với những người xem thường Tanya có thể gây chuyện ở p000461. Chưa mô tả một phe hay một nguy cơ cụ thể sẽ xảy ra.'
    resolution: 'Tạm dùng Những người nghĩ rằng nếu đứa trẻ bé xíu ấy đương đầu được với chiến tranh thì mình cũng làm được vẫn còn thuộc nhóm ít đáng lo hơn. Bỏ thường; giữ so sánh tương đối, không nói họ chắc chắn an toàn hoặc nhóm còn lại chắc chắn sẽ chống lệnh. Phương án ít diễn giải hơn: ...vẫn còn thuộc nhóm an toàn hơn.'
  - id: B18-F06
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000440
    issue: 'Tiến thân qua các cấp bậc làm mất xuất thân từ hàng ngũ binh lính của các sĩ quan được nhắc.'
    evidence: 'Cụm come up through the ranks nhấn đường tiến lên từ hàng ngũ, không chỉ việc từng thăng cấp. Nó giải thích sự tin cậy khi giao họ hỗ trợ tân binh.'
    resolution: 'Tạm dùng Sĩ quan cấp úy Serebryakov cùng những người khác trưởng thành từ hàng ngũ binh lính có lẽ sẽ làm tốt việc đó. Giữ mức suy đoán, không thêm hồ sơ nhập ngũ hoặc lịch sử thăng cấp cụ thể.'
  - id: B18-F07
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000451
    issue: 'Học viên năm hai tự xác định năm học từ nhãn second-class student khi package không xác lập hệ phân lớp.'
    evidence: 'Trong phạm vi được giao không có thông tin để quyết định đây là niên khóa, lớp hay phân hạng. Canon characters/glossary chưa chốt.'
    resolution: 'Tạm dùng một học viên lớp hai, ghi độ bất định về hệ phân lớp; không gọi là năm hai hoặc học viên kém chỉ từ nhãn này. Coordinator lưu lựa chọn pending, không cần dừng để hỏi người dùng.'
  - id: B18-F08
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000452
    issue: 'Đơn vị huấn luyện viên gượng và khác cách gọi chức năng đơn vị huấn luyện đang dùng trong ledger.'
    evidence: 'chapter5_b10, b12 và b16 đã lặp lựa chọn đơn vị huấn luyện; không cần suy thêm biên chế gồm toàn huấn luyện viên.'
    resolution: 'Dùng đơn vị huấn luyện hoặc đơn vị phụ trách huấn luyện. Ở p000456/p000458 có thể gọi cá nhân là người huấn luyện để hợp giọng quân sự, nhưng không tự thêm chức vụ.'
  - id: B18-F09
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000453
    issue: 'Trước khi nhận nhiệm vụ thu hẹp assignment thành nhiệm vụ tác chiến thay vì việc phân công sau huấn luyện bổ sung.'
    evidence: 'p000452–453 mô tả được đưa về đơn vị huấn luyện, huấn luyện lại rồi mới phân công; chưa nói nhận một nhiệm vụ cụ thể.'
    resolution: 'Tạm dùng trước khi được phân công, anh sẽ được huấn luyện lại với tư cách quân bổ sung. Không tự thêm đơn vị đích hoặc thời hạn điều quân.'
  - id: B18-F10
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000450
    issue: 'Những lính già dễ chỉ tuổi tác, trong khi old stagers nhấn kinh nghiệm.'
    evidence: 'Đoạn đối chiếu tập quán của người quen cảnh đi tàu ra mặt trận với Grantz mới tới; không nêu tuổi.'
    resolution: 'Cân nhắc những người lính lâu năm; giữ ba cách giết thời gian và việc Grantz xen kẽ chợp mắt/trò chuyện.'
  - id: B18-F11
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000458
    issue: 'Huấn luyện viên kiêm cố vấn làm phẳng sắc thái oái oăm vì người đáng sợ ấy lại còn là cố vấn của Grantz.'
    evidence: 'Nguồn không chỉ liệt kê hai chức năng; giọng Grantz đang than thở trước câu muốn khóc ở p000459.'
    resolution: 'Cân nhắc ...người huấn luyện ấy, oái oăm thay, lại còn là cố vấn của tôi. Giữ câu đầu ở dạng tôi sẽ tin nếu được kể, không biến chuyện làm hại học viên thành sự kiện đã xác nhận.'
unresolved_findings: [B18-HASH, B18-F01, B18-F02, B18-F03, B18-F04, B18-F05, B18-F06, B18-F07, B18-F08, B18-F09, B18-F10, B18-F11]
coverage:
  p000430: 'Giữ hai nguyên nhân làm lộ tiếp cận và sắc thái tên ngốc; tín hiệu mana phù hợp lựa chọn tạm.'
  p000431: 'Giữ sự ngán ngẩm và câu hỏi khả năng xử lý; quân hàm cần F03. Không diễn giải xử lý thành trừng phạt cụ thể.'
  p000432: 'Giữ điều kiện nếu cần và cố hỗ trợ để tránh phải xử lý; Thiếu tá/tôi trong thoại phù hợp đề xuất tạm.'
  p000433: 'Giữ hành động điểm lại ý kiến; thoại tự nhiên.'
  p000434: 'Giữ ý tổng kết các kết luận hợp lý nhất; không tự đánh chữ nghiêng.'
  p000435: 'Giữ số thứ tự và mức làm mọi cách để tránh giao chiến.'
  p000436: 'Giữ giọng ủng hộ hòa bình ngắn, hơi mỉa mai.'
  p000437: 'Giữ điều đơn vị mạnh nhất, không đổi thành đội đông nhất.'
  p000438: 'Giữ bực mình nhưng chấp thuận vì thận trọng; tự quy chiếu cần F01.'
  p000439: 'Giữ điều kiện chưa bị phát hiện và phân biệt tiếp cận/rút lui nguy hiểm.'
  p000440: 'Giữ kế hoạch an toàn có điều kiện, hỗ trợ khi tân binh làm hỏng việc và sĩ quan/hạ sĩ quan; F03/F06.'
  p000441: 'Giữ người nói sẽ thông báo kế hoạch; tôi trong thoại được giữ.'
  p000442: 'Giữ câu hỏi chọn tân pháp sư, mình và ẩn dụ dã ngoại; nguồn không có em nên không thêm nghiêng.'
  p000443: 'Giữ thực đơn, hậu phương/tiền tuyến, lời nghe kể và suy đoán hậu cần; chuyển sang điểm nhìn Grantz; F02.'
  p000444: 'Giữ tên, quân hàm phân bậc, ăn nhanh và so sánh khẩu phần thao trường. Có thể thêm cuối cùng cũng vừa để giữ sắc thái chờ tới lúc được phong sĩ quan; không thêm năm/tuổi.'
  p000445: 'Giữ ăn được nhưng chán nản mấy ngày vì bị đưa tới nơi giao tranh ác liệt. Lưỡi anh không đến nỗi chê bai hơi gượng; có thể dùng cũng không đến nỗi khó nuốt.'
  p000446: 'Giữ hồi tưởng phấn khích, ý muốn lập công và trở thành anh hùng; không hiểu run vì sợ.'
  p000447: 'Giữ nhiệt tình giảm dần khi tàu tới gần khu vực Rhine.'
  p000448: 'Giữ cảnh cháy xám, mùi hăng, suy sụp và pháo có lẽ của Đế quốc; không xác nhận nguồn âm thanh.'
  p000449: 'Giữ sự bồn chồn không tự nhận ra và nhận ra nhiều người cũng lo âu.'
  p000450: 'Giữ tin đồn, ngủ/chơi bài, trò chuyện theo nhịp tàu và tin từng biết; F10.'
  p000451: 'Giữ lời đồn là lời đồn và trình diện Bộ chỉ huy; F02/F07. Cô ta nằm trong suy nghĩ Grantz, không tự đổi thành nó theo quy ước trần thuật Tanya.'
  p000452: 'Giữ nghe tin về đơn vị và cảm giác nhẹ nhõm; F08.'
  p000453: 'Giữ huấn luyện lại cho quân bổ sung và làm quen tiền tuyến; F09.'
  p000454: 'Giữ có lẽ, dấu cảm thán và suy nghĩ từ vài ngày trước; F02.'
  p000455: 'Giữ lời chào quân nhân và mặt trận Rhine; các anh là lựa chọn thoại tại chỗ.'
  p000456: 'Giữ giả định quỷ dữ, huấn luyện viên là chỉ huy và tên von Degurechaff; F04. Ngôi chúng tôi mở phần kể của Grantz, không phải tự quy chiếu Tanya.'
  p000457: 'Giữ ba nhịp ngắn, so sánh giòi bọ và vẻ khát máu chỉ là cảm nhận; cô ta tiếp tục điểm nhìn Grantz.'
  p000458: 'Giữ mức sẽ tin chuyện chưa xác nhận, điều kiện mắc lỗi và sự sợ hãi chủ quan; F02/F11.'
  p000459: 'Giữ câu muốn khóc khẩu ngữ và dấu lửng; không tự thêm chữ nghiêng.'
  p000460: 'Giữ Grantz là người duy nhất qua học viện và hai phản ứng với lời đồn; F05 xử lý nhóm ít đáng lo hơn, không tạo phe phái.'
  p000461: 'Giữ lo về hành động có thể xảy ra và ghét trách nhiệm tập thể; F02. Không thêm cơ chế hình phạt.'
  p000462: 'Giữ tối nay được nghỉ, định ngủ sớm rồi bị gián đoạn ngay; F02.'
  p000463: 'Giữ triệu tập, theo trung đội, phòng hội ý và hạn ba phút; F04. Không tự thêm Xung kích từ tên dài ở p000456.'
  p000464: 'Giữ hai mệnh lệnh ngắn, cấp bách; không cần làm dịu giọng.'
pending_terms_policy: 'Đề xuất tạm, không canon; coordinator ghi ledger/handoff, người giữ quyền sửa áp dụng. Reviewer không ghi ledger.'
pending_terms: []
term_recommendations:
  - source_term: mana signal
    proposed_vi: tín hiệu mana
    alternatives_vi: [dấu hiệu mana, tín hiệu ma lực]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000430]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ lựa chọn b17 và mana trong ledger; ma lực dễ hiểu hơn nhưng chưa được chọn thống nhất. Không gán đây là tín hiệu cầu cứu.'
  - source_term: Lieutenant Serebryakov
    proposed_vi: 'Cô trong câu gọi tại p000431; Sĩ quan cấp úy Serebryakov tại p000440'
    alternatives_vi: [Úy Serebryakov, Trung úy Serebryakov, Thiếu úy Serebryakov]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000431, YS-LN02/Text/part0026.xhtml/p000440]
    volume: vol-02
    chapter: 5
    status: pending
    confidence: low_for_exact_rank
    rationale: 'Theo lựa chọn trung tính b17 khi nguồn không phân bậc; cô hợp thoại đang có. Úy ngắn nhưng gượng; hai bậc cụ thể chưa có đủ chứng cứ.'
  - source_term: Magic Second Lieutenant
    proposed_vi: thiếu úy ma pháp
    alternatives_vi: [thiếu úy pháp sư]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000444]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Nguồn phân Second rõ, phù hợp lựa chọn chapter1_b01 trong ledger; không đánh đồng với Lieutenant không phân bậc của Serebryakov.'
  - source_term: Major von Degurechaff
    proposed_vi: Thiếu tá von Degurechaff
    alternatives_vi: [Major von Degurechaff]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000432, YS-LN02/Text/part0026.xhtml/p000456]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ ánh xạ quân hàm hiện hành và tên nguyên dạng, chưa chốt hệ cấp bậc canon.'
  - source_term: 203rd Aerial Mage Assault Battalion
    proposed_vi: Tiểu đoàn Pháp sư Xung kích Trên không số 203
    alternatives_vi: [Tiểu đoàn Pháp sư Xung kích Không quân 203]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000456]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ chức năng xung kích và lựa chọn Trên không từ b03; Không quân có nguy cơ gán quân chủng chưa được xác lập.'
  - source_term: 203rd Aerial Mage Battalion
    proposed_vi: Tiểu đoàn Pháp sư Trên không số 203
    alternatives_vi: [Tiểu đoàn Pháp sư Bay số 203, Tiểu đoàn Pháp sư Không quân 203]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000463]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Theo b03; Bay kém tự nhiên cho tên đơn vị, Không quân dễ bị hiểu là quân chủng. Không bổ sung Xung kích vào tên nguồn rút gọn.'
  - source_term: Great Army
    proposed_vi: Đại quân
    alternatives_vi: [Great Army]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000443]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ cách dùng b08 và bản dịch; chưa đủ chứng cứ để đổi thành một cấp biên chế cụ thể.'
  - source_term: Logistics
    proposed_vi: bộ phận Hậu cần
    alternatives_vi: [bộ phận hậu cần, ngành hậu cần]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000443]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ cách gọi chức năng hiện có; chưa chốt là cơ quan chính thức hay quân chủng. Không suy lên Cục/Bộ Hậu cần; cách viết thường là phương án nếu sau này xác định chỉ là chức năng.'
  - source_term: instructor unit
    proposed_vi: đơn vị huấn luyện
    alternatives_vi: [đơn vị phụ trách huấn luyện, đơn vị huấn luyện viên]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000452]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Nhất quán ledger b10/b12/b16 và mô tả chức năng. Phụ trách huấn luyện rõ hơn nhưng dài; huấn luyện viên hợp người hơn đơn vị.'
  - source_term: second-class student
    proposed_vi: học viên lớp hai
    alternatives_vi: [học viên năm hai, học viên hạng hai]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000451]
    volume: vol-02
    chapter: 5
    status: pending
    confidence: low
    rationale: 'Giữ nhãn lớp theo nghĩa literal khi chưa biết hệ phân loại của học viện. Năm hai gán niên khóa; hạng hai dễ gán chất lượng. Không xác lập lore hoặc hệ giáo dục.'
  - source_term: picnic
    proposed_vi: dã ngoại
    alternatives_vi: [chuyến đi chơi]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000442]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ ví von mỉa mai của Tanya về chuyến đi tác chiến đầu tiên, không đổi thành tên nhiệm vụ trinh sát. Đi chơi khẩu ngữ hơn nhưng mất hình ảnh cụ thể.'
  - source_term: collective responsibility
    proposed_vi: trách nhiệm tập thể
    alternatives_vi: [trách nhiệm chung, liên đới chịu trách nhiệm]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000461]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Giữ thuật ngữ và nhấn mạnh đúng phạm vi; trách nhiệm chung loãng hơn, liên đới nêu cơ chế rõ hơn nhưng không cần thêm. Không đổi thành trừng phạt tập thể.'
  - source_term: railway gun
    proposed_vi: pháo đường sắt
    alternatives_vi: [pháo đặt trên đường sắt]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000448]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Nhất quán ledger b10; giữ có lẽ cho việc nhận diện khẩu pháo. Không bổ sung cỡ nòng hoặc cơ chế vận hành.'
  - source_term: pronoun choices
    proposed_vi: 'Tanya tự quy chiếu mình ở p000438/p000442; Grantz anh trong trần thuật, mình trong ý nghĩ p000443/p000454, tôi/chúng tôi trong đoạn kể ngôi thứ nhất p000456–463; cô ta khi Grantz nghĩ về Tanya.'
    alternatives_vi: ['Lược đại từ tại chỗ khi không mất chủ thể; dùng mình cho các câu suy nghĩ trực tiếp của Grantz nếu được coordinator thống nhất toàn chương.']
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000438, YS-LN02/Text/part0026.xhtml/p000442, YS-LN02/Text/part0026.xhtml/p000443, YS-LN02/Text/part0026.xhtml/p000451, YS-LN02/Text/part0026.xhtml/p000454, YS-LN02/Text/part0026.xhtml/p000456, YS-LN02/Text/part0026.xhtml/p000457, YS-LN02/Text/part0026.xhtml/p000458, YS-LN02/Text/part0026.xhtml/p000460, YS-LN02/Text/part0026.xhtml/p000461, YS-LN02/Text/part0026.xhtml/p000462, YS-LN02/Text/part0026.xhtml/p000463]
    volume: vol-02
    chapter: 5
    status: pending
    rationale: 'Chỉ tự quy chiếu Tanya đã có DEC-P01-001. Các đại từ Grantz là đề xuất theo chuyển điểm nhìn tại p000443–444 và chuyển ngôi thứ nhất ở p000456. Không ép cô ta trong lời kể Grantz thành nó hoặc áp mình của Tanya cho mọi nhân vật.'
risks:
  - 'Sai hash review chặn chứng nhận đầu vào, dù package khớp batch; cần coordinator xử lý metadata trước bước tiếp theo.'
  - 'Các lỗi vừa còn mở và sáu span nhấn mạnh cần người giữ quyền sửa xử lý; báo cáo không phải signoff bản dịch.'
  - 'Không thấy ghi chú translator riêng tại p000460 trong self-check/notes; đã xử lý vấn đề qua bản dịch và yêu cầu handoff, không dựng thêm nội dung ghi chú.'
  - 'Bậc cụ thể Serebryakov và nhãn second-class vẫn bất định; phương án trung tính cho phép tiếp tục sau khi xử lý hash, không cần chờ quyết định canon.'
next_action: 'Coordinator xác minh/sửa hash bàn giao review, ghi các lựa chọn pending vào ledger/handoff; giao người giữ quyền sửa xử lý findings, chạy validator/diff-check rồi review lại. Reviewer dừng sau báo cáo; không commit.'
```
