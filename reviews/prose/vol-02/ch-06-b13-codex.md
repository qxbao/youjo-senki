# Review — vol-02-ch-06-b13

```yaml
role: reviewer
task_id: vol-02-ch-06-b13-review
state: done
review_path: reviews/prose/vol-02/ch-06-b13-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b13-codex.md
source_verification:
  path: work/vol-02/batches/ch-06-b13-source.jsonl
  expected_sha256: d2f3d4e413de55741c9c87520bc552ec12ee70ace95601d7fd73cdf966d59562
  actual_sha256: d2f3d4e413de55741c9c87520bc552ec12ee70ace95601d7fd73cdf966d59562
  result: pass
  only_source_text: true
scope:
  reviewed_dimensions: [meaning, prose, viewpoint, pronouns, emphasis, terminology, rank]
  canon_read:
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
  pending_ledger_read: entries_for_this_batch_only
  source_packages_read: [work/vol-02/batches/ch-06-b13-source.jsonl]
  epub_pdf_read: false
  translation_edited: false
segment_ids:
  - YS-LN02/Text/part0030.xhtml/p000382
  - YS-LN02/Text/part0030.xhtml/p000383
  - YS-LN02/Text/part0030.xhtml/p000384
  - YS-LN02/Text/part0030.xhtml/p000385
  - YS-LN02/Text/part0030.xhtml/p000386
  - YS-LN02/Text/part0030.xhtml/p000387
  - YS-LN02/Text/part0030.xhtml/p000388
  - YS-LN02/Text/part0030.xhtml/p000389
  - YS-LN02/Text/part0030.xhtml/p000390
  - YS-LN02/Text/part0030.xhtml/p000391
  - YS-LN02/Text/part0030.xhtml/p000392
  - YS-LN02/Text/part0030.xhtml/p000393
  - YS-LN02/Text/part0030.xhtml/p000394
  - YS-LN02/Text/part0030.xhtml/p000395
  - YS-LN02/Text/part0030.xhtml/p000396
  - YS-LN02/Text/part0030.xhtml/p000397
  - YS-LN02/Text/part0030.xhtml/p000398
  - YS-LN02/Text/part0030.xhtml/p000399
  - YS-LN02/Text/part0030.xhtml/p000400
  - YS-LN02/Text/part0030.xhtml/p000401
  - YS-LN02/Text/part0030.xhtml/p000402
  - YS-LN02/Text/part0030.xhtml/p000403
  - YS-LN02/Text/part0030.xhtml/p000404
  - YS-LN02/Text/part0030.xhtml/p000405
  - YS-LN02/Text/part0030.xhtml/p000406
  - YS-LN02/Text/part0030.xhtml/p000407
  - YS-LN02/Text/part0030.xhtml/p000408
  - YS-LN02/Text/part0030.xhtml/p000409
  - YS-LN02/Text/part0030.xhtml/p000410
  - YS-LN02/Text/part0030.xhtml/p000411
  - YS-LN02/Text/part0030.xhtml/p000412
  - YS-LN02/Text/part0030.xhtml/p000413
  - YS-LN02/Text/part0030.xhtml/p000414
  - YS-LN02/Text/part0030.xhtml/p000415
  - YS-LN02/Text/part0030.xhtml/p000416
  - YS-LN02/Text/part0030.xhtml/p000417
counts:
  assigned_ids: 36
  reviewed_ids: 36
  findings: 7
  serious: 0
  moderate: 6
  minor: 1
  unresolved_findings: 7
  provisional_proposals_assessed: 8
  stated_risk_ids_assessed: 5
validator: not_run
diff_check: not_run
commit: null
findings:
  - id: B13-R01
    severity: moderate
    segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000391
      - YS-LN02/Text/part0030.xhtml/p000393
      - YS-LN02/Text/part0030.xhtml/p000398
      - YS-LN02/Text/part0030.xhtml/p000399
      - YS-LN02/Text/part0030.xhtml/p000404
      - YS-LN02/Text/part0030.xhtml/p000407
      - YS-LN02/Text/part0030.xhtml/p000411
      - YS-LN02/Text/part0030.xhtml/p000413
      - YS-LN02/Text/part0030.xhtml/p000414
      - YS-LN02/Text/part0030.xhtml/p000416
    issue: Thiếu dấu nhấn mạnh nguồn ở mười đoạn, trái DEC-P01-002.
    evidence: >-
      XHTML trong package đánh dấu phần nội tâm, lượng từ của mệnh lệnh,
      ba cụm trong quy định giao chiến và điều kiện chuyển sang tiêu diệt.
      Bản dịch chỉ giữ dấu tương ứng ở p000383.
    resolution:
      p000391: Bọc câu hỏi mở đầu bằng dấu sao đơn.
      p000393: Bọc toàn bộ câu thứ hai bằng dấu sao đơn.
      p000398: Chỉ bọc cụm “toàn bộ”.
      p000399: Bọc toàn bộ đoạn.
      p000404: Bọc riêng “người không tham chiến”, “được phép” và “thiệt hại tài sản”; không bọc cả mệnh đề.
      p000407: Chỉ bọc câu hỏi nội tâm mở đầu.
      p000411: Bọc toàn bộ đoạn, gồm dấu ba chấm.
      p000413: Chỉ bọc câu điều kiện thứ hai về từ chối và chuyển sang tiêu diệt.
      p000414: Chỉ bọc câu cuối về đầu hàng.
      p000416: Bọc câu hỏi nội tâm sau khi sửa ngôi kể theo B13-R06.
    confidence: high
    status: open
  - id: B13-R02
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000387]
    issue: “Suy nghĩ nóng vội” gán thêm tính hấp tấp cho Grantz và Tanya.
    evidence: >-
      Mô tả tâm thế ở đây nhấn vào sự kích động; package không đủ căn cứ
      để xác định hai người thiếu kiên nhẫn hoặc quyết định quá nhanh.
      Câu còn nối tâm thế đó với việc xem tấn công là đương nhiên.
    resolution: >-
      Đổi thành “Cả Grantz lẫn Tanya đều có khuynh hướng suy nghĩ trong
      trạng thái kích động, nên họ thấy tấn công là việc đương nhiên
      phải làm trên chiến trường.” Giữ nguyên quan hệ nguyên nhân.
      Có thể làm mượt câu đầu thành “Ngay khi nói vậy, chính Tanya
      cũng tin rằng tái chiếm là lựa chọn duy nhất, một kết luận đủ hợp lý.”
    alternative: “Cả Grantz lẫn Tanya đều có lối suy nghĩ dễ bị kích động”.
    confidence: medium
    status: open
  - id: B13-R03
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000400]
    issue: “Có gì khó hiểu đâu?” đổi đối tượng câu hỏi từ độ khó của nhiệm vụ sang độ khó hiểu.
    evidence: >-
      Sau lập luận chiến thuật ở p000399, Grantz tự hỏi việc đó có khó
      thực hiện hay không; lời kể tiếp theo mới mô tả anh chưa hiểu
      sự do dự. Bản dịch hiện gộp hai bình diện này.
    resolution: “Liệu việc đó có khó đến thế không? Grantz vẫn chưa thực sự hiểu.”
    alternative: “Chuyện đó có khó gì đâu? Grantz vẫn chưa hiểu.”
    confidence: high
    status: open
  - id: B13-R04
    severity: moderate
    segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000402
      - YS-LN02/Text/part0030.xhtml/p000403
    issue: >-
      p000402 mất nhận xét rằng biểu hiện của Weiss kỳ lạ; động tác chuẩn bị
      tinh thần bị đổi thành lấy lại bình tĩnh. Đại từ cuối đoạn dễ bị
      hiểu lại thành Grantz.
    evidence: >-
      Package có một nhận xét độc lập của người quan sát trước khi mô tả
      Weiss lo lắng, dao động. Hơi thở là động tác tự làm mình vững vàng
      để đối diện điều sắp tới, cũng là điều câu hỏi p000403 tiếp nối.
    resolution: >-
      Ở p000402 dùng “Gương mặt viên trung úy chỉ hơi căng lại.
      Grantz thấy điều đó thật lạ. Weiss rõ ràng đang lo lắng và dao động.
      Rồi Weiss hít sâu một hơi, như thể cố chuẩn bị tinh thần.”
      Ở p000403 đổi câu mở đầu thành “Chuẩn bị tinh thần để đối mặt với điều gì?”
      Giữ phần câu hỏi còn lại.
    alternative: Dùng “cố làm mình vững tâm” ở p000402 và “Vững tâm trước chuyện gì?” ở p000403.
    confidence: high
    status: open
  - id: B13-R05
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000401]
    issue: “Tân binh” thu hẹp nhóm quân bổ sung thành người mới nhập ngũ.
    evidence: >-
      Vai trò bổ sung quân số được nêu ở p000401; p000417 gọi nhóm người
      mới đang học thích nghi với chiến tranh. Việc hai nhóm có thể trùng nhau
      không đủ để xóa khác biệt giữa hai cách gọi trong nguồn.
    resolution: >-
      Dùng “hầu hết lính bổ sung” ở p000401; giữ “tân binh” ở p000417.
      Áp dụng đề xuất pending B13-T05, không tạo kết luận về kinh nghiệm
      của mọi quân nhân được bổ sung.
    alternative: “Hầu hết quân bổ sung”.
    confidence: high
    status: open
  - id: B13-R06
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000416]
    issue: Câu tự vấn ngôi thứ nhất thành câu kể về “anh”; “sự bất hòa” gợi xung đột quan hệ ngoài căn cứ.
    evidence: >-
      Câu hỏi được đánh dấu nội tâm, tự quy chiếu từ Grantz sang bản thân
      và việc đơn vị sắp xuất kích. Cảm giác trước đó là sự không ăn khớp,
      không xác định bất hòa giữa người với người.
    resolution: >-
      Đổi phần đầu thành “Nếu phải nói rõ, anh đành thừa nhận có điều gì đó
      khác thường. Anh cảm thấy có gì đó không ăn khớp, không ổn.
      Dẫu vậy, mình có thật sự nên để tâm trí bị phân tán ngay trước khi
      chúng ta xuất kích không?” Bọc riêng câu cuối bằng dấu sao đơn.
      Giữ các thao tác kiểm tra thiết bị và so sánh về bảo dưỡng phía sau.
    alternative: Dùng “có điều gì đó lệch nhịp” cho cảm giác không ăn khớp.
    confidence: high
    status: open
  - id: B13-R07
    severity: minor
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000405]
    issue: “Xin miễn trừ” chỉ hành động yêu cầu, chưa giữ việc đạt được miễn trừ.
    evidence: >-
      Câu cuối mô tả việc có được miễn trừ thuộc quy trình bình thường,
      tiếp nối tình trạng đã được miễn trách nhiệm ở câu trước.
    resolution: “Nhưng ngay cả việc được miễn trừ đó cũng thuộc quy trình thông thường.”
    alternative: “Nhưng ngay cả việc đạt được sự miễn trừ ấy cũng thuộc thủ tục thông thường.”
    confidence: high
    status: open
unresolved_findings: [B13-R01, B13-R02, B13-R03, B13-R04, B13-R05, B13-R06, B13-R07]
term_recommendations:
  - id: B13-T01
    source_term: paradigm / battlefield paradigm
    proposed_vi: mô thức / mô thức chiến trường
    status: pending
    non_canon: true
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000383]
    rationale: >-
      Giữ cách gọi mô hình tư duy chi phối hành động, phù hợp đề xuất
      về mô thức trong canon/glossary-pending.yml. Không biến thành học thuyết
      hay quy định chính thức. Tránh khiến từ “mệnh lệnh” thêm vào trong bản
      dịch bị hiểu là một mệnh lệnh cụ thể đã được ban ra.
    alternative: mô hình tư duy chiến trường
    suggested_context: “Theo mô thức chiến trường, họ chẳng cần nghĩ gì xa hơn việc *tiêu diệt kẻ địch*.”
    confidence: high
  - id: B13-T02
    source_term: 203rd Aerial Mage Battalion
    proposed_vi: Tiểu đoàn Pháp sư Trên không số 203
    status: pending
    non_canon: true
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000385]
    rationale: >-
      Giữ số hiệu, cấp tiểu đoàn và hoạt động trên không. Package không
      xác định quân chủng; chọn “Không quân” sẽ thêm thông tin tổ chức.
      Giữ lựa chọn ledger để nhất quán tạm thời, không xác nhận các lô khác.
    alternative: Tiểu đoàn Pháp sư Không chiến số 203
    confidence: high
  - id: B13-T03
    source_term: sortie
    proposed_vi: xuất kích
    status: pending
    non_canon: true
    segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000387
      - YS-LN02/Text/part0030.xhtml/p000396
      - YS-LN02/Text/part0030.xhtml/p000409
      - YS-LN02/Text/part0030.xhtml/p000416
    rationale: Phù hợp việc triển khai đơn vị pháp sư trên không và kiểm tra trước nhiệm vụ; không thêm số lượt bay.
    alternative: xuất quân
    confidence: high
  - id: B13-T04
    source_term: rules of engagement / ROE
    proposed_vi: quy tắc giao chiến
    status: pending
    non_canon: true
    segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000404
      - YS-LN02/Text/part0030.xhtml/p000405
    rationale: >-
      Bao quát giới hạn nổ súng, thiệt hại tài sản và các chỉ dẫn tác chiến;
      “khai hỏa” hẹp hơn. p000405 có thuật ngữ đầy đủ rồi tên viết tắt,
      nên việc lặp “quy tắc giao chiến” hiện tại chấp nhận được.
      p000404 là ngữ cảnh quy định, không có tên thuật ngữ cần chèn thêm.
    alternative: quy định giao chiến
    confidence: high
  - id: B13-T05
    source_term: replacement(s)
    proposed_vi: lính bổ sung
    status: pending
    non_canon: true
    segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000401
      - YS-LN02/Text/part0030.xhtml/p000417
    rationale: >-
      Ở p000401 ưu tiên vai trò bổ sung quân số, không suy diễn mức huấn luyện
      hay kinh nghiệm. p000417 dùng cách gọi người mới khác, nên giữ “tân binh”
      tại đó; đây là phân biệt theo từng đoạn, không buộc hai nhóm phải khác nhau.
    alternative: quân bổ sung
    contextual_wording:
      p000401: lính bổ sung
      p000417: tân binh
    confidence: high
  - id: B13-T06
    source_term: occupation
    proposed_vi: chiếm đóng
    status: pending
    non_canon: true
    segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000384
      - YS-LN02/Text/part0030.xhtml/p000399
      - YS-LN02/Text/part0030.xhtml/p000398
    rationale: >-
      Giữ nghĩa kiểm soát thành phố bằng lực lượng quân sự, không tự thêm
      cơ chế cai trị. p000384 nói khả năng duy trì sự chiếm đóng;
      p000399 diễn đạt hành động chiếm thành phố, còn p000398 là trạng thái
      đang bị chiếm đóng. Các biến thể hiện có không tạo mâu thuẫn.
    alternative: chiếm giữ
    confidence: high
  - id: B13-T07
    source_term: noncombatants
    proposed_vi: người không tham chiến
    status: pending
    non_canon: true
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000404]
    rationale: >-
      Giữ phạm vi đối tượng theo tình trạng tham chiến; không đồng nhất
      với toàn bộ dân thường hoặc suy ra ai được xem là quân địch.
      Phải giữ dấu nhấn mạnh của cụm này.
    alternative: người không tham gia chiến đấu
    confidence: high
  - id: B13-T08
    source_term: computation orb
    proposed_vi: quả cầu tính toán
    status: pending
    non_canon: true
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000416]
    rationale: >-
      Giữ định danh thiết bị riêng với súng trường, bám cấu tạo tên gọi
      và lựa chọn ledger. Package không giải thích hình dạng hay cơ chế,
      nên không thêm chức năng hoặc chuyển thành loại trang bị suy đoán.
    alternative: cầu tính toán
    confidence: medium
risks:
  - segment_ids: [YS-LN02/Text/part0030.xhtml/p000387]
    assessment: needs_revision
    recommended_temporary_wording: khuynh hướng suy nghĩ trong trạng thái kích động
    rationale: Giữ tâm thế, tránh gán thêm tính hấp tấp; không diễn giải ẩn ý về lập trường hay đạo đức.
    alternative: lối suy nghĩ dễ bị kích động
    confidence: medium
    finding: B13-R02
    status: pending_non_canon
  - segment_ids: [YS-LN02/Text/part0030.xhtml/p000402]
    assessment: needs_revision
    recommended_temporary_wording: Weiss hít sâu một hơi, như thể cố chuẩn bị tinh thần.
    rationale: >-
      Người hít thở là Weiss; gọi lại tên tránh nhập với Grantz.
      Giữ “trung úy” tạm thời cho quân hàm ghi trong package,
      không tự đổi thành cấp khác hoặc suy ra chức vụ.
    alternative: Weiss hít sâu một hơi, như thể cố làm mình vững tâm.
    rank_alternative: trung úy Weiss
    confidence: high
    finding: B13-R04
    status: pending_non_canon
  - segment_ids: [YS-LN02/Text/part0030.xhtml/p000407]
    assessment: wording_acceptable_emphasis_missing
    recommended_temporary_wording: “*Mình… mình đang bỏ sót điều gì sao?*”
    rationale: >-
      Ngữ cảnh xác định tự vấn của Grantz. Dùng “mình” là lựa chọn cục bộ,
      không mở rộng DEC-P01-001 của Tanya thành quy tắc canon cho Grantz.
      “Nỗi lo mơ hồ, khó gọi tên” chấp nhận được, không cần thêm nguyên nhân.
    alternative: “*Mình… mình chưa nhận ra điều gì sao?*”
    confidence: high
    finding: B13-R01
    status: pending_non_canon
  - segment_ids: [YS-LN02/Text/part0030.xhtml/p000412]
    assessment: acceptable
    recommended_temporary_wording: một trận đánh hơi phiền phức để quét sạch họ
    rationale: >-
      Giữ sắc thái đánh giá nhẹ trong suy nghĩ của Grantz; không thêm
      khó khăn chiến thuật hoặc phán xét đạo đức. Đối tượng được để
      trung tính là “họ”, không suy rộng sang cư dân hay dân quân.
    alternative: một trận đánh khá phiền phức để tiêu diệt họ
    confidence: medium
    status: pending_non_canon
  - segment_ids: [YS-LN02/Text/part0030.xhtml/p000414]
    assessment: term_acceptable_emphasis_missing
    recommended_temporary_wording: cấp trên của anh
    rationale: >-
      Giữ quan hệ chỉ huy nhìn từ Grantz, không thêm quân hàm hay chức danh.
      Có thể làm mượt “giọng cấp trên của anh phẳng lặng tuyệt đối”
      thành “giọng cấp trên của anh hoàn toàn đều đều”.
      Câu cuối cần dấu nhấn mạnh theo B13-R01.
    alternative: người chỉ huy của anh
    confidence: high
    finding: B13-R01
    status: pending_non_canon
  - segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000389
      - YS-LN02/Text/part0030.xhtml/p000393
      - YS-LN02/Text/part0030.xhtml/p000395
      - YS-LN02/Text/part0030.xhtml/p000397
      - YS-LN02/Text/part0030.xhtml/p000405
      - YS-LN02/Text/part0030.xhtml/p000409
    assessment: pronoun_scope_uncertain_use_local_neutral_wording
    recommended_temporary_wording: Tanya ở chỗ cần nhắc lại chủ thể; “cô” chỉ là phương án cục bộ đang dùng.
    rationale: >-
      DEC-P01-001 giới hạn cách gọi Tanya vào giai đoạn đã duyệt và cấm
      tự mở rộng. Handoff không xác nhận áp dụng “nó” cho giai đoạn vol-02;
      characters.yml chưa có quy ước. Không báo lỗi canon chỉ vì các đoạn
      này dùng “cô”, cũng không nâng “cô” thành canon. Nếu cần loại bỏ
      bất định, dùng tên Tanya và lược chủ ngữ ở chỗ rõ chủ thể.
    alternative: giữ “cô” nhất quán cục bộ, với trạng thái pending
    confidence: medium
    status: pending_non_canon
coverage_notes:
  - Đã rà toàn bộ 36 ID; các ID không có finding không phát hiện lỗi cần sửa có căn cứ trong phạm vi package.
  - >-
      p000384 giữ điều kiện thiếu bộ binh và giới hạn khả năng của dân quân.
      p000385 giữ hình tượng đơn vị trưởng thành trong chiến tranh;
      có thể làm mượt “là những đứa con” thành “là đứa con” để giữ
      hình tượng tập thể, nhưng không coi đây là lỗi nghĩa cần chặn.
  - >-
      p000398 giữ mục tiêu toàn bộ binh sĩ Cộng hòa; p000399 và p000410
      giữ cách hiểu hẹp của Grantz về pháp sư. Không đồng nhất hai phạm vi
      hoặc giải thích trước điều mà nhân vật chưa hiểu.
  - >-
      p000404–p000406 và p000408 giữ lệnh cấm, ngoại lệ về tài sản,
      hai thời điểm phát cảnh báo và tạm ngừng chiến đấu.
      Không tự suy ra người nhận cảnh báo sau khi pháp sư bị tiêu diệt,
      và không đưa nhận định pháp lý ngoài package vào báo cáo.
  - >-
      p000411 giữ độ mở của suy nghĩ dè dặt; p000413–p000415 giữ điều kiện
      đầu hàng hoặc chuyển sang tiêu diệt. p000416–p000417 giữ mục tiêu
      kiểm tra trang bị và thích nghi để sống sót.
  - >-
      Self-check chưa bao quát đúng dấu nhấn mạnh và bỏ sót các thay đổi
      nghĩa nêu trên. Reviewer không sửa self-check; translator nên cập nhật
      theo quy trình sau khi nhận báo cáo.
next_action: >-
  Coordinator chuyển B13-R01–B13-R07 cho người giữ quyền sửa translation;
  ghi tám lựa chọn tạm và các đánh giá rủi ro vào ledger/handoff theo quyền
  của coordinator, vẫn pending/non-canon. Translator sửa đúng ID, cập nhật
  tự kiểm theo phân công; sau đó chạy validator/diff-check và đối chiếu lại
  các finding. Review đã hoàn tất, batch còn sáu finding vừa chưa xử lý;
  chưa đủ điều kiện hoàn tất batch.
```
