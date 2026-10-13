# Review vol-02-ch-05-b04

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-05-b04
state: done
review_path: reviews/prose/vol-02/ch-05-b04-codex.md
scope:
  segment_id_start: YS-LN02/Text/part0026.xhtml/p000076
  segment_id_end: YS-LN02/Text/part0026.xhtml/p000102
  units_reviewed: 27
  inputs: [agents/shared.md, agents/reviewer.md, config/translation-pipeline.yml, handoffs/vol-02/ch-05-b04.yml, canon/glossary.yml, canon/style-guide.md, canon/characters.yml, canon/decisions.md, canon/glossary-pending.yml, 'work/run-state/pending-terms.yml#chapter5_b03_translation_proposals', work/vol-02/batches/ch-05-b04-source.jsonl, translations/vol-02/ch-05-b04.jsonl]
  other_batches_inspected: false
files_written: [reviews/prose/vol-02/ch-05-b04-codex.md]
validator: not_run
diff_check: not_run
commit: null
input_checks:
  package_sha256_matches_handoff: true
  canon_reference_hashes_match_handoff: true
  source_and_translation_ids: 'Đủ 27 mã, đúng thứ tự p000076–p000102, không trùng hoặc thiếu.'
  source_hash_metadata_matches: true
  emphasis: 'p000076 giữ đúng phần nhấn mạnh bằng Markdown; không thấy thêm nhấn mạnh ở các đoạn khác.'
assessment:
  meaning: 'Cần sửa các điểm F01, F03 và F04.'
  omissions: 'Không thiếu đoạn hoặc lượt thoại; F01 mất nét nghĩa vô ý, F03 mất quan hệ không gian của hình ảnh so sánh.'
  logic: 'Giữ được yêu cầu yểm trợ năm phút, phản đối thời lượng quá ngắn, tiếp tục bắn khi đơn vị xông vào và phân công tấn công/yểm trợ trên không. F04 làm tăng độ chắc chắn của khả năng sống sót.'
  military_terms: 'Phần lớn dùng được tạm thời; cần bỏ bổ nghĩa trinh sát chưa có căn cứ và làm rõ nghĩa diễn tập tại F06/F09.'
  rank: 'Thiếu tá của Tanya có căn cứ trực tiếp trong package. Cấp úy cụ thể của Serebryakov chưa xác định được từ cách gọi tại p000099.'
  pronouns: 'Các đoạn tự suy nghĩ của Tanya cần áp dụng mình theo DEC-P01-001; đại từ nó trong trần thuật p000101–p000102 phù hợp.'
  pending_coverage: >-
    Handoff ghi bốn mục pending nhưng không cung cấp danh sách tên/ID hoặc phương án của chúng.
    Phần ledger được phép đọc là chapter5_b03_translation_proposals, không phải mục b04.
    Vì vậy không thể xác nhận đối sánh 4/4 ID chính thức. Báo cáo xét các thuật ngữ chưa chốt
    tại b04 và đưa phương án tạm để coordinator đối sánh; không tự gán danh tính cho bốn mục.
counts:
  segments_reviewed: 27
  findings_total: 9
  serious: 0
  moderate: 5
  minor: 4
  unresolved_findings: 9
  declared_pending_terms: 4
  declared_pending_ids_verified: 0
  term_recommendations: 8
findings:
  - id: B04-F01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000076
    issue: 'Muốn ném bom chỗ nào thì ném biến tính vô ý thành hành động tùy ý có chủ đích.'
    evidence: 'Nguồn nối tai nạn quân sự với sự châm biếm về việc được dung thứ cho ném bom nhầm; bản dịch bỏ đặc tính vô ý ở câu thứ hai.'
    resolution: 'Đề xuất: Chỉ có Hoa Kỳ mới được phép lỡ ném bom bất cứ chỗ quái quỷ nào. Giữ nét mỉa mai và phần nhấn mạnh hiện có.'
  - id: B04-F02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000076
    related_segment_ids: [YS-LN02/Text/part0026.xhtml/p000079, YS-LN02/Text/part0026.xhtml/p000083, YS-LN02/Text/part0026.xhtml/p000085, YS-LN02/Text/part0026.xhtml/p000086, YS-LN02/Text/part0026.xhtml/p000087, YS-LN02/Text/part0026.xhtml/p000088, YS-LN02/Text/part0026.xhtml/p000089, YS-LN02/Text/part0026.xhtml/p000097, YS-LN02/Text/part0026.xhtml/p000101]
    issue: 'Tự quy chiếu trong nội tâm Tanya dùng tôi thay vì mình theo DEC-P01-001.'
    evidence: 'Các đoạn này là lời tự đánh giá, hồi tưởng hoặc mong muốn của Tanya, khác với lời thoại vô tuyến. p000101 còn chuyển rõ từ tự bình luận sang trần thuật về nó.'
    resolution: 'Dùng mình cho ngôi thứ nhất số ít trong các phần nội tâm nêu trên. Không thay hàng loạt đại từ trong lời thoại hoặc chúng tôi. Giữ cô ấy ở p000101 như đối tượng của lời bình về đại từ giới tính, và giữ nó trong phần trần thuật.'
  - id: B04-F03
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000086
    issue: 'Hình ảnh tàu ngầm chìm vào nhà vệ sinh hỏng bị đổi thành tàu ngầm đang chìm có nhà vệ sinh hỏng.'
    evidence: 'Nguồn gắn chuyển động chìm với nhà vệ sinh như đích đến của hình ảnh so sánh. Bản dịch biến nhà vệ sinh thành trang bị trên tàu, làm yếu mức ghê tởm của môi trường.'
    resolution: 'Tạm giữ hình ảnh literal: Tệ chẳng khác nào ở trên một chiếc tàu ngầm đang chìm xuống một nhà vệ sinh hỏng. Hình ảnh vốn lạ; không tự sửa nghĩa nguồn theo giả định về tàu ngầm thực tế.'
  - id: B04-F04
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000094
    issue: 'Sẽ giúp tránh thương tích chí mạng làm dự đoán có điều kiện thành bảo đảm.'
    evidence: 'Nguồn chỉ đánh giá rằng có lẽ có thể tránh thương tích chí mạng nhờ mẫu thiết bị mới khi trúng trực tiếp; không bảo đảm kết quả.'
    resolution: 'Đề xuất: Nếu có trúng đạn trực tiếp do một sự trùng hợp hi hữu nào đó, nhờ mẫu quả cầu mới, chúng tôi hẳn vẫn có thể tránh bị thương chí mạng. Giữ mức dự đoán hẳn/có lẽ và khả năng có thể.'
  - id: B04-F05
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000099
    issue: 'Thiếu úy Serebryakov xác định một cấp cụ thể khi package chỉ cho cách gọi cấp úy chưa phân biệt bậc.'
    evidence: 'Canon nhân vật chưa có cấp bậc đã duyệt. Package này không có thêm định ngữ phân biệt thiếu úy/trung úy; mục ledger b03 được phép đọc cũng không xác lập cấp của Serebryakov.'
    resolution: 'Tạm dùng Úy Serebryakov để giữ dấu hiệu quân hàm mà không tự chọn bậc. Phương án diễn giải rõ hơn là Sĩ quan cấp úy Serebryakov nhưng kém tự nhiên trong thoại. Thiếu úy hoặc Trung úy chỉ là lựa chọn thay thế chưa đủ căn cứ trong phạm vi này.'
  - id: B04-F06
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000092
    issue: 'Đội trinh sát quan sát thêm chức năng trinh sát chưa được nguồn xác lập.'
    evidence: 'Vai trò được nêu tại chỗ là quan sát điểm đạn rơi và dẫn đường cho đơn vị tấn công; không xác định đây là đơn vị trinh sát.'
    resolution: 'Dùng tiểu đội quan sát; có thể dùng tổ quan sát nếu chưa muốn xác định cấp tổ chức. Giữ quan sát viên tiền tuyến ở câu sau. Không thêm trinh sát.'
  - id: B04-F07
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000091
    issue: 'Tương đối an toàn đối với tiền tuyến dễ bị hiểu là nhiệm vụ làm tiền tuyến an toàn hơn.'
    evidence: 'Đoạn đánh giá rủi ro đối với người thực hiện một loại nhiệm vụ tương đối an toàn trong môi trường tiền tuyến.'
    resolution: 'Đề xuất: Ngay cả một nhiệm vụ không kích, vốn thuộc loại tương đối an toàn ở tiền tuyến, cũng buộc ta phải chấp nhận những rủi ro khá tệ hại.'
  - id: B04-F08
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000085
    issue: 'Mới chỉ bắt đầu thêm thông tin về thời điểm trong mùa xuân.'
    evidence: 'Nguồn chỉ xác định đây là mùa xuân đầu tiên, không nói mùa ấy vừa bắt đầu.'
    resolution: 'Dùng Đây mới chỉ là mùa xuân đầu tiên của chúng tôi; không thêm mốc đầu mùa.'
  - id: B04-F09
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000099
    issue: 'Diễn tập pháo kích dễ bị hiểu là tiểu đoàn được huấn luyện bắn pháo.'
    evidence: 'p000094 nêu huấn luyện phòng tránh pháo kích; p000099 dùng các buổi tập làm căn cứ để tin quân mình tránh được đạn pháo yểm trợ.'
    resolution: 'Dùng Sau tất cả những buổi diễn tập ứng phó với pháo kích mà chúng ta đã trải qua. Cách diễn đạt này giữ hoạt động luyện tập và quan hệ với việc tránh đạn quân mình.'
unresolved_findings: [B04-F01, B04-F02, B04-F03, B04-F04, B04-F05, B04-F06, B04-F07, B04-F08, B04-F09]
unresolved_ids:
  findings: [B04-F01, B04-F02, B04-F03, B04-F04, B04-F05, B04-F06, B04-F07, B04-F08, B04-F09]
  metadata: [B04-PENDING-MAP]
term_recommendations:
  - id: B04-TR01
    source_term: Silver Wings Assault Badge
    proposed_vi: Huy hiệu Tấn công Cánh bạc
    alternatives_vi: [Huy hiệu Xung kích Cánh bạc]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000083]
    status: proposed
    confidence: medium
    rationale: 'Có thể giữ cách gọi hiện tại vì bám các thành tố tên huy hiệu. Xung kích sát sắc thái quân sự hơn nhưng chưa có căn cứ canon để đổi tên; không gọi đây là huân chương.'
  - id: B04-TR02
    source_term: observation squad
    proposed_vi: tiểu đội quan sát
    alternatives_vi: [tổ quan sát, đội quan sát]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000092]
    status: proposed
    confidence: medium
    rationale: 'Giữ loại đơn vị và chức năng quan sát, không thêm trinh sát. Tổ quan sát là phương án trung tính hơn nếu cấp tổ chức còn bất định; không tự suy ra quân số.'
  - id: B04-TR03
    source_term: mage’s outer shells
    proposed_vi: lớp vỏ ngoài của pháp sư
    alternatives_vi: [lớp vỏ bảo vệ của pháp sư, lớp bảo vệ ngoài của pháp sư]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000093]
    status: proposed
    confidence: medium
    rationale: 'Giữ cách gọi literal hiện tại. Ngữ cảnh cho thấy tác dụng bảo vệ trước hỏa lực nhưng chưa xác lập cơ chế; phương án có bảo vệ dễ hiểu hơn, song không nên tự gọi là kết giới, giáp hay lá chắn năng lượng.'
  - id: B04-TR04
    source_term: anti-surface assault
    proposed_vi: xung kích chống mục tiêu mặt đất
    alternatives_vi: [xung kích đối đất, tấn công mục tiêu mặt đất]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000093, YS-LN02/Text/part0026.xhtml/p000096]
    status: proposed
    confidence: high
    rationale: 'Mục tiêu pháo binh và p000101 xác lập mặt đất trong batch này. Giữ đội hình ở p000093 và đợt tấn công ở p000096; không dùng thuật ngữ gợi tác chiến mặt biển. Xung kích đối đất gọn hơn nhưng cần nhất quán trước khi thay.'
  - id: B04-TR05
    source_term: Lieutenant Serebryakov
    proposed_vi: Úy Serebryakov
    alternatives_vi: [Sĩ quan cấp úy Serebryakov, Thiếu úy Serebryakov, Trung úy Serebryakov]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000099]
    status: proposed
    confidence: low
    rationale: 'Cách gọi nguồn không phân biệt bậc cấp úy trong package. Tạm chọn dạng giữ cấp úy, ít suy diễn nhất. Hai cấp cụ thể là phương án để xét khi có căn cứ được phép, không phải kết luận quân hàm.'
  - id: B04-TR06
    source_term: direct support
    proposed_vi: lực lượng yểm trợ trực tiếp
    alternatives_vi: [bộ phận yểm trợ trực tiếp, yểm trợ trực tiếp]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000097]
    status: proposed
    confidence: medium
    rationale: 'Phân công ở p000096 và việc được tăng độ cao ở p000097 ủng hộ cách hiểu Tanya bay cùng bộ phận yểm trợ. Có thể giữ bản hiện tại; không tự đổi thành hỏa lực pháo binh hoặc khẳng định tên một đơn vị chính thức.'
  - id: B04-TR07
    source_term: orb
    proposed_vi: quả cầu
    alternatives_vi: [quả cầu tính toán]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000094]
    status: proposed
    confidence: medium
    rationale: 'Giữ dạng rút gọn của thiết bị tại chỗ, tương thích với đề xuất quả cầu tính toán trong ledger b03. Không thêm cơ chế tác dụng hoặc tên model.'
  - id: B04-TR08
    source_term: CP / Pixie
    proposed_vi: CP / Pixie
    alternatives_vi: [sở chỉ huy / Pixie]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000080, YS-LN02/Text/part0026.xhtml/p000081]
    status: proposed
    confidence: medium
    rationale: 'Giữ định danh vô tuyến; Pixie tương thích với đề xuất hô hiệu ở b03. Package không khai triển CP nên giữ chữ viết tắt là lựa chọn ít suy diễn; không đưa phần giải thích hô hiệu vào lời thoại.'
pending_terms: []
risks:
  - id: B04-PENDING-MAP
    description: 'Chưa thể xác nhận bốn mục pending chính thức đã được đối sánh đầy đủ vì đầu vào được phép không có danh sách tên/ID b04. Tám đề xuất trên bao quát các điểm chưa chốt nhìn thấy tại chỗ; coordinator cần đối sánh với ledger hiện có.'
  - 'Quân hàm cụ thể của Serebryakov vẫn bất định; phương án tạm giữ cấp úy cho phép tiếp tục mà không suy ra lịch sử thăng cấp.'
  - 'Hình ảnh p000086 có cấu trúc bất thường; đề xuất literal giữ quan hệ nguồn, không tự sửa theo hiểu biết ngoài phạm vi.'
  - 'Chưa có sửa bản dịch hay review lại; năm lỗi vừa vẫn mở. state done chỉ chỉ việc hoàn tất báo cáo, không phải chấp nhận batch.'
  - 'Mọi lựa chọn thuật ngữ đều là đề xuất, không nâng thành canon. Không thấy quyết định canon ảnh hưởng cốt truyện cần dừng trong phạm vi này.'
next_action: >-
  Coordinator đối sánh các đề xuất với bốn ID pending b04 trong ledger hiện có,
  ghi lựa chọn tạm và bàn giao cho người giữ quyền sửa translations/.
  Translator sửa chín finding trong đúng batch; sau đó chạy các kiểm tra bắt buộc
  và review lại những đoạn đã sửa trước khi công nhận hoàn tất.
```
