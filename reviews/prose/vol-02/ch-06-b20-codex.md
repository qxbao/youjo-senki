# Review độc lập — vol-02-ch-06-b20

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-06-b20-review
batch: vol-02-ch-06-b20
state: done
review_result: changes_requested
review_path: reviews/prose/vol-02/ch-06-b20-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b20-codex.md
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
  source_package: work/vol-02/batches/ch-06-b20-source.jsonl
  expected_sha256: 1214be418ef94f270ce38a9dfcc5ab091102dd1c54336935a01900f8bcd1d342
  actual_sha256: 1214be418ef94f270ce38a9dfcc5ab091102dd1c54336935a01900f8bcd1d342
  package_hash: match
  source_rows: 34
  translation_rows: 34
  ordered_segment_ids: match
  canon_reference_hashes: all_five_match_primary_handoff
  translation: translations/vol-02/ch-06-b20.jsonl
  self_check: reviews/semantic/vol-02/ch-06-b20-self-check.md
  review_handoff: handoffs/vol-02/ch-06-b20-review.yml
  primary_handoff: handoffs/vol-02/ch-06-b20.yml
  ledger_section: chapter6_b20_translator_proposals
  canon_read:
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
  scope: Chỉ gói b20 và đầu vào được giao; không mở EPUB/PDF hoặc gói nguồn khác.
counts:
  reviewed_rows: 34
  serious: 0
  moderate: 6
  minor: 4
  total_findings: 10
  unresolved_findings: 10
  pending_choices_assessed: 7
  canon_promotions: 0
validator: not_run
diff_check: not_run
commit: null
findings:
  - id: B20-CX-001
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000610
    category: emphasis
    issue: Mất cả hai vùng nhấn mạnh, gồm cách nhận diện nhóm người và câu hỏi nội tâm cuối đoạn.
    evidence: XHTML của gói có hai vùng em; bản dịch không có dấu sao nào. Trái DEC-P01-002.
    resolution: Đánh dấu cụm tương ứng với “chỉ là dân thường” hoặc phương án thay thế ở B20-CX-007, và đánh dấu riêng toàn bộ câu hỏi cuối đoạn; không in nghiêng cả đoạn.
    status: open
  - id: B20-CX-002
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000612
    category: emphasis
    issue: Hai câu hỏi nội tâm sau lời mô tả cảm xúc đều mất nhấn mạnh.
    evidence: Gói đánh dấu chung phần câu hỏi; bản dịch để toàn bộ đoạn ở dạng thường.
    resolution: Đặt dấu sao bao quanh phần từ “Thật sự định—?” đến hết câu hỏi kế tiếp, giữ trần thuật bên ngoài.
    status: open
  - id: B20-CX-003
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000627
    category: emphasis
    issue: Mất nhấn mạnh đối tượng mà chỉ huy gọi là kẻ thù, làm yếu điểm lập luận đáp lại Grantz.
    evidence: Gói chỉ đánh dấu danh ngữ đầu lời thoại, không đánh dấu cả lời thoại.
    resolution: Dùng “*Kẻ thù của Đế quốc* sẽ bị tiêu diệt. Tốt quá còn gì.” bên trong dấu thoại.
    status: open
  - id: B20-CX-004
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000633
    category: emphasis
    issue: In nghiêng toàn đoạn làm mất khoảng không nghiêng ở từ chỉ khả thể.
    evidence: XHTML có hai vùng em, ngắt tại could. Sự tương phản này gắn với việc giết người chỉ có khả năng trở thành địch.
    resolution: Dùng “*Vậy là cô bảo chúng ta giết họ sao? Cô đang bảo chúng ta giết những người* có thể *trở thành kẻ địch sao?*”; giữ “có thể” ngoài dấu sao.
    status: open
  - id: B20-CX-005
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000631
    related_segment_ids: [YS-LN02/Text/part0030.xhtml/p000626]
    category: rank
    issue: “Trung úy Grantz” tự xác định quân hàm khác với “thiếu úy” được nêu rõ cho cùng nhân vật năm đoạn trước.
    evidence: p000626 dùng second lieutenant; lời gọi Lieutenant ở p000631 không đủ căn cứ để xác lập việc đổi cấp bậc trong cùng cuộc đối thoại.
    resolution: Tạm dùng “Thiếu úy Grantz” ở p000631 theo căn cứ cụ thể tại p000626; cập nhật đề xuất ledger qua coordinator, không nâng thành canon. Phương án trung tính là chỉ gọi “Grantz”.
    status: open
  - id: B20-CX-006
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000639
    related_segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000640
      - YS-LN02/Text/part0030.xhtml/p000641
    category: viewpoint_metadata
    issue: Self-check gọi nội tâm p000639 là của Tanya; đây vẫn là điểm nhìn Grantz sau khi bị đánh và nhận lệnh.
    evidence: p000636–p000638 liên tục theo Grantz; p000639–p000640 đáp lại mệnh lệnh ấy. Dấu chuyển cảnh chỉ xuất hiện ở p000641.
    resolution: Sửa nhận định trong self-check thành nội tâm Grantz ở p000639–p000640. Tạm giữ “mình” tại p000639 vì tự quy chiếu tự nhiên, nhưng không viện DEC-P01-001 như canon cho Grantz. Với p000641–p000643, giữ giọng tự sự “mình”; gói này chưa nêu tên người kể ở cảnh tàu nên chỉ ghi nhận Tanya là suy đoán, không xác nhận bằng lore.
    status: open
  - id: B20-CX-007
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000610
    category: lexical_precision
    issue: “Dân thường” có căn cứ ngữ cảnh nhưng thu hẹp ý nhận ra những con người bình thường; “kiệt sức” chỉ diễn tả mệt mỏi, làm hẹp tình trạng tả tơi của các pháp sư.
    evidence: p000622 xác nhận nhóm sau là dân thường; riêng p000610 nhấn mạnh tính người và việc không thể hình dung họ chiến đấu. Mô tả beat-up không chỉ định riêng sự mệt mỏi.
    resolution: Tạm ưu tiên “chỉ là những người bình thường” và “các pháp sư tả tơi kia”; nhấn mạnh danh ngữ đầu theo B20-CX-001. Không thêm chi tiết thương tích cụ thể.
    alternatives: [Giữ “dân thường” nếu ưu tiên nhận diện nhóm, “các pháp sư rệu rã kia”]
    status: open
  - id: B20-CX-008
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000613
    category: prose
    issue: Chuỗi đồng vị dài khiến quan hệ mệnh lệnh–đối tượng khó đọc; “những kẻ” làm giọng kể có phần xa cách hơn cần thiết.
    evidence: Bản hiện tại vẫn giữ đúng cả Thiếu tá von Degurechaff lẫn pháo binh là hai mối đe dọa; không có lỗi đảo người bảo vệ và người được bảo vệ.
    resolution: Tạm sửa phần sau câu đầu thành “Mệnh lệnh quét sạch số địch còn lại—những người đang cố triển khai công thức bảo vệ để che chở dân chúng khỏi Thiếu tá von Degurechaff và pháo binh—chính là mệnh lệnh loại bỏ các pháp sư đang giúp dân chúng chạy thoát.”
    status: open
  - id: B20-CX-009
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000615
    category: radio_voice
    issue: “Hết. Xin hết.” lặp hai công thức kết thúc, làm mờ sự phân biệt giữa kết thúc nội dung và chuyển lượt liên lạc.
    evidence: p000620 còn có lời xác nhận của tiểu đoàn; không nên biến lượt trước thành hai lời đóng kênh liên tiếp.
    resolution: Tạm dùng “Bộ chỉ huy gọi Tiểu đoàn Pixie. Chỉ có vậy. Hết.”; lựa chọn tên cơ quan theo B20-T04, không tự đặt chuẩn thông tin vô tuyến toàn dự án.
    alternatives: [“Bộ chỉ huy gọi Tiểu đoàn Pixie. Chỉ có vậy. Mời trả lời.”]
    status: open
  - id: B20-CX-010
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000640
    category: profanity_voice
    issue: “Chết tiệt” giữ bực tức nhưng giảm độ thô của lời chửi ngắn trong cơn giằng xé của Grantz.
    evidence: Từ Fuck đứng thành một nhịp riêng giữa hai lần nhắc mệnh lệnh; gói không hướng lời chửi vào một người cụ thể.
    resolution: Tạm chọn “*Vì đó là mệnh lệnh. Đệch. Một mệnh lệnh…*” để giữ nhịp ngắn và độ thô, không thêm đối tượng bị chửi. Đây là đề xuất giọng cho đoạn này, không phải canon.
    alternatives:
      - “Địt.” — thô trực diện hơn nhưng dễ tạo nhịp tiếng Việt gượng ở lời cảm thán độc lập.
      - “Chết tiệt.” — dễ đọc hơn nhưng chấp nhận giảm độ thô.
    status: open
unresolved_findings:
  - B20-CX-001
  - B20-CX-002
  - B20-CX-003
  - B20-CX-004
  - B20-CX-005
  - B20-CX-006
  - B20-CX-007
  - B20-CX-008
  - B20-CX-009
  - B20-CX-010
translator_flags:
  p000610: Dân thường được p000622 hỗ trợ; ưu tiên phương án ít thu hẹp hơn ở B20-CX-007 và khôi phục nhấn mạnh ở B20-CX-001.
  p000613: Nghĩa hai mối đe dọa đúng; đề nghị làm rõ cấu trúc tại B20-CX-008.
  p000640: Chọn tạm “Đệch”, với phương án thay thế và giới hạn ở B20-CX-010; người nghĩ là Grantz.
term_recommendations:
  - id: B20-T01
    source_term: protective formula
    proposed_vi: công thức bảo vệ
    alternatives_vi: [công thức phòng hộ]
    segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000613
      - YS-LN02/Text/part0030.xhtml/p000618
    contextual_segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000610
      - YS-LN02/Text/part0030.xhtml/p000619
    rationale: Giữ lựa chọn literal, thống nhất với hệ từ “công thức”; chức năng là bảo vệ dân chúng. Không tự thêm mô tả cơ chế phép.
    ledger_note: p000610 và p000619 chỉ nhắc sự bảo vệ/tấm khiên theo ngữ cảnh, không có chính thuật ngữ này; coordinator nên phân biệt tham chiếu ngữ cảnh với lần xuất hiện trực tiếp.
    uncertainty: low
    volume: vol-02
    chapter: 6
    status: pending
    canon: false
  - id: B20-T02
    source_term: rear guard
    proposed_vi: đội hậu vệ
    alternatives_vi: [lực lượng đoạn hậu]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000611]
    rationale: Đúng vai trò nhóm ở lại bảo vệ phía sau cuộc rút lui; không suy ra quy mô đơn vị chính thức.
    uncertainty: low
    volume: vol-02
    chapter: 6
    status: pending
    canon: false
  - id: B20-T03
    source_term: Pixie Battalion
    proposed_vi: Tiểu đoàn Pixie
    alternatives_vi: [Tiểu đoàn mang mật danh Pixie]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000615, YS-LN02/Text/part0030.xhtml/p000620]
    rationale: Giữ định danh Pixie và quy mô tiểu đoàn có trong lời liên lạc; không Việt hóa sang một loài sinh vật hoặc xác quyết đây là tên chính thức. Phương án thêm “mật danh” chỉ dùng khi có căn cứ bổ sung, hiện chưa ưu tiên.
    uncertainty: medium
    volume: vol-02
    chapter: 6
    status: pending
    canon: false
  - id: B20-T04
    source_term: HQ
    proposed_vi: Bộ chỉ huy
    replaces_proposed_vi: Đại bản doanh
    alternatives_vi: [Sở chỉ huy, Đại bản doanh]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000615]
    rationale: Trong lời vô tuyến đây là đầu mối chỉ huy ra lệnh; gói chưa xác định cấp chiến lược hay quy mô để ưu tiên “Đại bản doanh”. “Bộ chỉ huy” trung tính và nhất quán với Command trong cùng mạch, không xác lập hai tên là một cơ quan trong canon.
    uncertainty: medium
    volume: vol-02
    chapter: 6
    status: pending
    canon: false
  - id: B20-T05
    source_term: second lieutenant
    proposed_vi: thiếu úy
    alternatives_vi: [sĩ quan cấp thấp]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000626]
    rationale: Nguồn nêu quân hàm cụ thể; giữ “thiếu úy”. Phương án mô tả trung tính làm mất độ chính xác nên không ưu tiên.
    uncertainty: low
    volume: vol-02
    chapter: 6
    status: pending
    canon: false
  - id: B20-T06
    source_term: Lieutenant
    proposed_vi: Thiếu úy Grantz
    replaces_proposed_vi: Trung úy Grantz
    alternatives_vi: [Grantz]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000631]
    evidence_segment_ids: [YS-LN02/Text/part0030.xhtml/p000626]
    rationale: Lời gọi rút gọn chỉ cùng Grantz; quân hàm cụ thể tại p000626 là căn cứ tốt hơn việc ánh xạ từ riêng lẻ sang “trung úy”. Lựa chọn chỉ áp dụng lần gọi này, không thiết lập quy tắc dịch Lieutenant toàn truyện.
    uncertainty: low_within_batch
    volume: vol-02
    chapter: 6
    status: pending
    canon: false
  - id: B20-T07
    source_term: Command
    proposed_vi: Bộ chỉ huy
    alternatives_vi: [cấp chỉ huy, Sở chỉ huy]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000612, YS-LN02/Text/part0030.xhtml/p000626]
    rationale: Chủ thể ra và truyền xuống mệnh lệnh được dùng như đầu mối chỉ huy; không có căn cứ thêm cấp “tối cao” hoặc tên tổ chức.
    uncertainty: medium
    volume: vol-02
    chapter: 6
    status: pending
    canon: false
pending_terms: [B20-T01, B20-T02, B20-T03, B20-T04, B20-T05, B20-T06, B20-T07]
row_review:
  p000610: Nghĩa cảm xúc và câu hỏi giữ được; xem B20-CX-001 và B20-CX-007.
  p000611: Giữ trình tự tiêu diệt hậu vệ rồi pháo binh xử lý, giới hạn không quá mười phút; thuật ngữ tạm B20-T02.
  p000612: Giữ xung đột lý trí–cảm xúc và câu hỏi bị ngắt; xem B20-CX-002. “Trong đầu Grantz hiểu” hơi gượng, có thể dùng “Về lý trí, Grantz hiểu”.
  p000613: Không mất mối đe dọa nào, giữ vai trò che chở dân chúng; xem B20-CX-008.
  p000614: Giữ tự thuyết phục và nhấn mạnh đúng; “cô ấy” trong ý nghĩ Grantz là lựa chọn theo điểm nhìn, chưa canon.
  p000615: Giữ các bên liên lạc; xem B20-CX-009 và B20-T03/B20-T04.
  p000616: Giữ giới hạn nội dung mong muốn của cấp trên; không thêm động cơ.
  p000617: Giữ mệnh lệnh giết và phạm vi nhấn mạnh riêng phần mệnh lệnh.
  p000618: Giữ chuỗi mất bảo vệ–pháo kích, sự không biết của pháo binh và lời tự trấn an; nhấn mạnh đúng.
  p000619: Giữ chuyển từ đoán sang biết chắc và ẩn dụ tấm khiên; nhấn mạnh đúng.
  p000620: Giữ lời xác nhận và cam kết cố gắng; chưa biến thành bảo đảm kết quả.
  p000621: Giữ điều kiện, pháo kích tập trung và thiếu vật che chắn; không khẳng định nhóm đã chết.
  p000622: Giữ câu hỏi vì sao nã vào dân thường và sự thiếu kỹ năng sống sót; nhấn mạnh đúng.
  p000623: Giữ lời xin cân nhắc, ngập ngừng và điều kiện chưa nói hết.
  p000624: Giữ tính bất ngờ của việc nêu ý kiến với cấp trên.
  p000625: Giữ biểu hiện tái mét và cảm nhận của Grantz.
  p000626: Giữ mức gần như chống lệnh, cấp bậc thấp và quan hệ cấp trên; thiếu úy là đề xuất B20-T05.
  p000627: Giữ lời tán thành lạnh lùng; mất nhấn mạnh tại B20-CX-003.
  p000628: Giữ phản đối bị ngắt, không hoàn tất ý thay nhân vật.
  p000629: Giữ phỏng đoán nguyên nhân chần chừ và việc vẫn phản đối.
  p000630: Giữ bối rối và cố ngăn chỉ huy, không biến thành đã ngăn được.
  p000631: Giữ khả năng cầm súng trở lại và mục tiêu bắn phe mình; quân hàm cần sửa B20-CX-005. “Cô” trong trần thuật bám điểm nhìn Grantz là tạm, không tự mở rộng canon LN01 sang LN02.
  p000632: Giữ lời thừa nhận khả thể rồi sự chắc chắn lặp lại về tân binh và ý chí chiến đấu; nhấn mạnh đúng.
  p000633: Giữ câu hỏi về người có thể trở thành địch; khoảng nhấn mạnh cần sửa B20-CX-004. “Cô” là lời hướng tới chỉ huy trong ý nghĩ, xét riêng với trần thuật.
  p000634: Giữ hai khả năng về lý do nói thêm; chưa xác quyết chỉ huy đọc được nội tâm Grantz.
  p000635: Giữ điều kiện bị bắn, nghĩa vụ nổ súng đến khi được bảo dừng và lý do mệnh lệnh.
  p000636: Giữ bị đánh ngã bất ngờ và tự đính chính đất thành bùn.
  p000637: Giữ đau, trạng thái lờ mờ và giả thuyết về lòng tốt; không biến giả thuyết thành động cơ chắc chắn.
  p000638: Giữ đủ giả vờ chưa nghe, mệnh lệnh, nhặt súng và làm việc; giọng dứt khoát phù hợp.
  p000639: Bản dịch tự quy chiếu và nhấn mạnh phù hợp; chủ thể trong self-check sai tại B20-CX-006.
  p000640: Giữ nhịp lặp mệnh lệnh và chữ nghiêng; mức thô cần cân nhắc theo B20-CX-010.
  p000641: Gói có dấu chuyển cảnh; giọng chào và than phiền về tàu phù hợp, giữ ưu tiên quân sự và lịch trình lệch. Không xác định danh tính người kể chỉ từ gói này.
  p000642: Giữ tài liệu/cà phê nguội, bảo mật, gây nhiễu và hạn chế rời toa; cấu trúc tăng tiến hai chủ thể rõ, câu hỏi không bị thu hẹp.
  p000643: Giữ đánh giá đồ ăn tương đối tốt, nguồn cung từ tàu và tâm trạng khó thư thái; nhấn mạnh đúng.
risks:
  - Self-check khẳng định đã giữ đủ nhấn mạnh nhưng còn bốn đoạn sai; không dùng tự kiểm thay cho đối chiếu XHTML.
  - Không xác lập danh tính người kể cảnh tàu hoặc phạm vi đại từ canon của LN02 khi gói chưa đủ chứng cứ; tiếp tục bằng cách tự quy chiếu trung tính đã có.
  - Các lựa chọn thuật ngữ, lời gọi, đại từ theo điểm nhìn và mức tục đều tạm; không tự nâng thành canon.
  - Chưa chạy validator/diff-check; review hoàn tất không đồng nghĩa lô đạt điều kiện hoàn tất pipeline.
  - Reviewer chưa áp dụng sửa; cả mười phát hiện còn mở, không có lỗi serious được nhận diện trong phạm vi này.
next_action: Coordinator tiếp nhận báo cáo, ghi các đề xuất tạm và giới hạn vào ledger/handoff; giao người giữ lease sửa bản dịch và self-check, rồi đối chiếu lại các finding và chạy validator/diff-check theo pipeline trước khi chốt lô.
```
