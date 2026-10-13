# Review b18 — nghĩa, văn phong, điểm nhìn và pending

```yaml
role: reviewer
task_id: vol-02-ch-06-b18-review
state: done
review_path: reviews/prose/vol-02/ch-06-b18-codex.md
files_written: [reviews/prose/vol-02/ch-06-b18-codex.md]
runtime_config:
  reviewer_launcher: codex-personal
  reviewer_model: gpt-6.1-sol
  reviewer_effort: medium
  note: Đọc cấu hình reviewer hiện hành; không khởi chạy worker khác.
source_verification:
  path: work/vol-02/batches/ch-06-b18-source.jsonl
  expected_sha256: 1f6116310c3d403849cb4ba575d10a8bf521a4ea1fc4e6ad08dffe8554685d92
  actual_sha256: 1f6116310c3d403849cb4ba575d10a8bf521a4ea1fc4e6ad08dffe8554685d92
  result: pass
  only_source_text: true
  ordered_ids_match: true
  source_units: 30
  translation_units: 30
scope:
  start: YS-LN02/Text/part0030.xhtml/p000554
  end: YS-LN02/Text/part0030.xhtml/p000583
  examined: [meaning, prose, viewpoint, pronouns, emphasis, terms, ranks]
  canon_reference: canon/glossary-pending.yml — P03-human-capital
  ledger_section: chapter6_b18_translator_proposals
  scope_note: >-
    Không mở EPUB/PDF, package khác hoặc bản dịch khác. Một truy vấn tìm vị trí
    section ledger đã trả về vài dòng metadata của section khác; không dùng các
    dòng ấy làm căn cứ. Sau đó chỉ đọc section b18. Không đọc đoạn nguồn được
    viện dẫn ngoài b18, không suy ra sự nhất quán xuyên lô từ self-check.
validator: not_run
diff_check: not_run
commit: null
counts:
  reviewed_ids: 30
  ids_with_findings: 8
  ids_without_actionable_findings: 22
  serious: 0
  moderate: 2
  minor: 7
  findings_total: 9
  unresolved_findings: 9
  pending_groups_assessed: 8
  canon_promotions: 0
findings:
  - finding_id: B18-M01
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000582
    category: meaning_modality
    issue: >-
      “không còn bị xếp vào nhóm phi chiến đấu” biến việc không còn cần phân loại
      thường dân là người không tham chiến thành một thay đổi phân loại đã xảy ra;
      chữ “bị” còn tạo sắc thái bất lợi không có căn cứ. “Xét về kỹ thuật” cũng dễ
      bị hiểu theo nghĩa kỹ thuật tác chiến thay vì khía cạnh thủ tục.
    evidence: >-
      Câu giữa là suy đoán về công dụng của thủ tục, còn câu cuối mô tả thời điểm
      Đế quốc tấn công sau khi không còn cần coi thường dân là người không tham
      chiến. Package không xác định cơ chế pháp luật hoặc chủ thể ra quyết định.
    resolution: >-
      Đề xuất câu giữa: “*Xét về mặt thủ tục, có lẽ đó là một bước để có thể coi
      thường dân là dân quân.*” Đề xuất câu cuối: “Dù sao, ngay khi không còn cần
      phân loại thường dân là người không tham chiến, Đế quốc đã bắt đầu tấn công
      thành phố không chút khoan nhượng.” Giữ “có lẽ”, không thêm căn cứ luật,
      quyết định chính thức hoặc tính hợp pháp của cuộc tấn công.
    confidence: 0.95
    status: open
  - finding_id: B18-M02
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000580
    category: sensory_meaning
    issue: >-
      “vừa cháy sém” làm nhẹ mức cháy của xác; “nồng mùi protein” thay cảm giác
      không khí dính/bết bởi protein bằng một mùi riêng của protein, đồng thời
      thêm “bốc lên”. Cả hai làm thay đổi hình ảnh thân thể gây buồn nôn.
    evidence: >-
      Đoạn nguồn mô tả xác mới bị cháy đến mức hóa than và tính chất dính của
      không khí; không chỉ tả bề mặt bị sém hoặc mùi protein.
    resolution: >-
      Dùng “Một xác chết vừa bị thiêu cháy thành than, mùi khét chưa bị mùi thối
      rữa che lấp. Không khí quánh dính vì protein, hôi thối khủng khiếp.” Có thể
      thay “quánh dính” bằng “dính bết”; không giải thích cơ chế sinh học.
    confidence: 0.93
    status: open
  - finding_id: B18-L01
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000573
    category: emphasis
    issue: Câu châm ngôn không có dấu nghiêng; dấu ngoặc kép không thay thế nhấn mạnh nguồn.
    resolution: >-
      Chỉ in nghiêng “Điều tốt mình làm cho người khác rồi sẽ quay lại với mình”.
      Giữ phần dẫn và nhận xét ngoài dấu nghiêng. Self-check cần được worker có
      quyền cập nhật sau sửa vì hiện tuyên bố đã giữ nhấn mạnh này.
    confidence: 1.0
    status: open
  - finding_id: B18-L02
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000582
    category: emphasis
    issue: Mất nhấn mạnh toàn bộ câu suy đoán ở giữa đoạn.
    resolution: In nghiêng riêng câu giữa như đề xuất B18-M01; không in nghiêng hai câu còn lại.
    confidence: 1.0
    status: open
  - finding_id: B18-L03
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000567
    category: prose
    issue: “Chính nghĩa công bằng đến tuyệt vời của việc” chồng danh từ và tính từ, khó đọc và làm yếu giọng tự biện hộ đắc ý.
    resolution: >-
      Đề xuất “Ngay trước mắt mình là một lý do chính đáng tuyệt vời: bảo vệ đồng
      bào.” Nếu muốn giữ “chính nghĩa”, dùng “Bảo vệ đồng bào — một chính nghĩa
      tuyệt vời — đang ở ngay trước mắt mình.”
    confidence: 0.88
    status: open
  - finding_id: B18-L04
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000570
    category: modality_prose
    issue: “cũng nên là” dễ thành lời khuyên về điều nên làm thay vì kỳ vọng rằng lý do này có thể dùng để biện minh.
    resolution: Đề xuất “Ít nhất thì đó cũng hẳn là một lý do để biện minh.” Giữ sắc thái tự trấn an, không khẳng định được miễn tội.
    confidence: 0.86
    status: open
  - finding_id: B18-L05
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000574
    category: meaning_prose
    issue: “cô hiểu sự tình” thiên về biết tình hình; căn cứ của phản ứng khá hơn là Visha đã thạo việc/có kinh nghiệm.
    resolution: >-
      Thay bằng “vì cô đã có kinh nghiệm” hoặc “vì cô đã thạo việc”. Giữ mức
      “khá hơn một chút” và câu về nguy hiểm khi chần chừ; không bổ sung lai lịch.
    confidence: 0.9
    status: open
  - finding_id: B18-L06
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000583
    category: terms_viewpoint
    issue: “đồng minh” dễ bị hiểu là lực lượng của một quốc gia liên minh; đoạn chỉ đủ căn cứ cho phía mình/những người cùng phe.
    resolution: >-
      Đề xuất “Anh thấy lạ khi Thiếu tá von Degurechaff quan tâm đến người phía
      mình hơn kẻ địch...” Giữ đây là cảm nhận của Grantz, rồi tan ngay, và giữ
      “Có lẽ” ở câu giải thích; không biến thành động cơ khách quan của Tanya.
    confidence: 0.85
    status: open
  - finding_id: B18-L07
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000556
    category: meaning_precision
    issue: “bị đánh chết” chỉ giữ cách gây chết, bỏ nét hành hình tự phát bởi đám đông; đồng thời thu hẹp vào đánh đập.
    resolution: >-
      Đề xuất “Có lẽ họ đã bị giết hoặc bị đám đông hành hình ngay khi cuộc nổi
      dậy bắt đầu.” Không xác định hình thức hành hình, thủ phạm cụ thể hoặc
      mức chắc chắn cao hơn.
    confidence: 0.87
    status: open
unresolved_findings: [B18-M01, B18-M02, B18-L01, B18-L02, B18-L03, B18-L04, B18-L05, B18-L06, B18-L07]
term_recommendations:
  - group: 1
    source_term: Rules of War on Land
    proposed_vi: Quy tắc Chiến tranh trên bộ
    alternatives_vi: [Luật Chiến tranh trên bộ, giữ tên tiếng Anh]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000554]
    rationale: Giữ tên mô tả và viện dẫn Điều 26, Khoản 3; không đủ căn cứ đồng nhất với một văn kiện ngoài đời.
    confidence: 0.88
    status: pending
    canon: false
  - group: 2
    source_term: Second Lieutenant
    proposed_vi: Thiếu úy
    alternatives_vi: [giữ cấp bậc tiếng Anh]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000581]
    rationale: Tương ứng dịch thuật thông thường và không mâu thuẫn package; chưa xác nhận hệ quy đổi cấp bậc xuyên tác phẩm.
    confidence: 0.95
    status: pending
    canon: false
  - group: 3
    source_term: Major
    proposed_vi: Thiếu tá
    alternatives_vi: [giữ cấp bậc tiếng Anh]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000583]
    rationale: Tương ứng dịch thuật thông thường; giữ nguyên von Degurechaff, không suy diễn cấp bậc từ lore hoặc volume khác.
    confidence: 0.95
    status: pending
    canon: false
  - group: 4
    source_term: cleanup / mopping up
    proposed_vi: truy quét
    alternatives_vi: [quét sạch lực lượng còn lại, dọn dẹp chiến trường]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000574, YS-LN02/Text/part0030.xhtml/p000576]
    rationale: >-
      Mệnh lệnh vẫn là tác chiến chống Quân đội Cộng hòa, không phải công tác
      hậu chiến. Dùng cùng một gốc từ cho cách tô vẽ cuộc thảm sát ở p000574;
      “dọn dẹp chiến trường” dễ làm nhẹ nghĩa. Không kiểm chứng p000533 ngoài phạm vi.
    confidence: 0.92
    status: pending
    canon: false
  - group: 5
    source_term: extermination / annihilation
    proposed_vi: cuộc tiêu diệt / giai đoạn tiêu diệt toàn bộ
    alternatives_vi: [cuộc tận diệt / giai đoạn tận diệt, tiêu diệt sạch]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000566, YS-LN02/Text/part0030.xhtml/p000568]
    rationale: >-
      Giữ tính triệt để và giọng tính toán của Tanya; chưa cần thay lựa chọn hiện
      tại. Không tự thêm “dân thường”, “cả thành phố” hay “diệt chủng” làm đối tượng.
    confidence: 0.86
    status: pending
    canon: false
  - group: 6
    source_term: prisoner rescue mission
    proposed_vi: nhiệm vụ giải cứu những người bị giam giữ
    alternatives_vi: [nhiệm vụ giải cứu tù binh, nhiệm vụ giải cứu người bị bắt]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000583]
    rationale: >-
      Package nói đến binh lính lẫn nhân viên dân sự quân đội và công dân bị bắt,
      chưa xác lập toàn bộ người được cứu có tư cách tù binh. Cách trung tính giữ
      tình trạng bị giữ mà không thêm địa vị pháp lý. “Tù binh” là phương án hẹp
      hơn còn pending; bản hiện tại chưa đủ căn cứ để kết luận sai chắc chắn.
    confidence: 0.8
    status: pending
    canon: false
  - group: 7
    source_term: Tanya/Grantz pronouns by viewpoint
    proposed_vi: >-
      Nội tâm Tanya dùng mình hoặc lược chủ ngữ; Grantz trần thuật dùng anh,
      nội tâm p000579 dùng mình; Visha dùng cô; Tanya trong cảm nhận Grantz
      ở p000583 dùng cô hoặc lặp tên/cấp bậc.
    alternatives_vi: [lặp tên hoặc lược đại từ khi mơ hồ, tôi trong nội tâm nếu coordinator đổi đồng bộ]
    segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000556
      - YS-LN02/Text/part0030.xhtml/p000557
      - YS-LN02/Text/part0030.xhtml/p000565
      - YS-LN02/Text/part0030.xhtml/p000566
      - YS-LN02/Text/part0030.xhtml/p000567
      - YS-LN02/Text/part0030.xhtml/p000568
      - YS-LN02/Text/part0030.xhtml/p000569
      - YS-LN02/Text/part0030.xhtml/p000570
      - YS-LN02/Text/part0030.xhtml/p000573
      - YS-LN02/Text/part0030.xhtml/p000574
      - YS-LN02/Text/part0030.xhtml/p000577
      - YS-LN02/Text/part0030.xhtml/p000579
      - YS-LN02/Text/part0030.xhtml/p000580
      - YS-LN02/Text/part0030.xhtml/p000581
      - YS-LN02/Text/part0030.xhtml/p000582
      - YS-LN02/Text/part0030.xhtml/p000583
    rationale: >-
      p000574 chuyển sang Grantz/Visha; p000578–p000579 neo rõ nội tâm Grantz,
      và p000582 tiếp tục suy đoán trong mạch ấy. “Chúng ta” ở p000565 hợp nghĩa
      nghĩa vụ chung; “mình” ở p000569 quy chiếu hợp mạch động cơ cá nhân. Không
      áp “nó” từ ledger lên p000583: đây là Tanya qua cảm nhận Grantz. B18 không
      có chỗ trần thuật Tanya độc lập đủ để phê chuẩn quy tắc “nó” toàn cục.
    confidence: 0.94
    status: pending
    canon: false
  - group: 8
    source_term: forms of address for locals/enemy
    proposed_vi: đồng bào / lũ Đế quốc khốn kiếp
    alternatives_vi: [người cùng nước / lũ người Đế quốc khốn kiếp, thường dân của nước mình ở p000568]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000561, YS-LN02/Text/part0030.xhtml/p000567, YS-LN02/Text/part0030.xhtml/p000568, YS-LN02/Text/part0030.xhtml/p000569]
    rationale: >-
      “Đồng bào” phù hợp quan hệ cùng quốc gia trong nội tâm tự biện hộ, không
      khẳng định cùng dân tộc. Câu chửi là Tanya đoán lời dân quân; phải giữ “có
      lẽ” và “Đại loại thế”, không biến thành lời nghe được chắc chắn. p000568
      giữ “thường dân của chính phe mình” được; “của nước mình” rõ nghĩa hơn.
    confidence: 0.92
    status: pending
    canon: false
additional_recommendations:
  - segment_id: YS-LN02/Text/part0030.xhtml/p000563
    subject: human capital
    proposed_vi: vốn con người
    alternative_vi: vốn nhân lực
    rationale: >-
      P03-human-capital trong canon/glossary-pending.yml đang đề xuất “vốn con
      người”, trong khi bản dịch dùng “vốn nhân lực”. Cả hai phù hợp khái niệm;
      ưu tiên phương án đã ghi ở tài liệu pending được phép đọc để nhất quán.
      Coordinator có thể giữ “vốn nhân lực” nếu ghi rõ lựa chọn tạm cho b18.
    confidence: 0.82
    status: pending
    canon: false
legal_ambiguity:
  segment_id: YS-LN02/Text/part0030.xhtml/p000582
  assessment: >-
    Câu giữa là phỏng đoán về việc thủ tục tạo khả năng coi thường dân là dân
    quân; không chứng minh thường dân thật sự tham chiến. Câu cuối nói không
    còn cần phân loại họ là người không tham chiến, không xác nhận một quyết
    định pháp lý chính thức. Đại từ chỉ người thực hiện không đủ rõ để thêm
    “Đế quốc” hoặc “bộ chỉ huy” vào câu giữa; giữ cấu trúc vô chủ thể.
  temporary_wording: Xét về mặt thủ tục, có lẽ đó là một bước để có thể coi thường dân là dân quân.
  alternative_vi: Xét về hình thức, có lẽ đó là thủ tục để có thể coi thường dân là dân quân.
  confidence: 0.88
  residual_uncertainty: Quan hệ pháp lý và chủ thể phân loại chưa được package xác lập.
  status: pending
  canon: false
  user_question_required: false
coverage:
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000554, result: acceptable, note: Giữ lời yêu cầu và viện dẫn; tên văn kiện pending.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000555, result: acceptable, note: Giữ tính danh nghĩa và giới hạn công dân có mặt.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000556, result: revise, findings: [B18-L07]}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000557, result: acceptable, note: Giữ ngạc nhiên và ví dụ chiến tranh hạt nhân; không tự giải đại từ họ.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000558, result: acceptable, note: Lược đại từ hợp lời hỏi ngắn; chưa đủ căn cứ thêm chức danh.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000559, result: acceptable, note: Báo bắn người nhưng chưa khẳng định chết.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000560, result: acceptable, note: Giữ bắn chết và lập luận quân chính quy/dân quân trong giọng Tanya.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000561, result: acceptable, note: Giữ câu chửi là lời đoán.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000562, result: acceptable, note: Giữ điều kiện thiếu huấn luyện và kết luận có mức dè dặt.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000563, result: acceptable_with_pending_alignment, note: Nghĩa đúng; cân nhắc vốn con người theo P03.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000564, result: acceptable, note: Giữ xin phép và tính tức thời của giải cứu.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000565, result: acceptable, note: Chúng ta giữ nghĩa vụ chung; cảnh báo mới hoàn thành trên danh nghĩa.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000566, result: acceptable, note: Giữ động cơ chính trị và tự biện hộ; tiêu diệt pending.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000567, result: revise, findings: [B18-L03]}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000568, result: acceptable, note: Giữ phân biệt ý nghĩa chính trị/quân sự và tính triệt để.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000569, result: acceptable, note: Tấm bùa miễn tội là ẩn dụ trong tự biện hộ; không xác nhận miễn trách nhiệm thật.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000570, result: revise, findings: [B18-L04]}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000571, result: acceptable, note: Giữ xác nhận và lệnh tiến hành; cách gọi vô tuyến không cần tự thêm chủ thể.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000572, result: acceptable, note: Giữ Pixie 01 và lời đáp thực hiện ngay.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000573, result: revise, findings: [B18-L01]}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000574, result: revise, findings: [B18-L05]}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000575, result: acceptable, note: Giữ luyện ngục/địa ngục và điểm nhìn Grantz.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000576, result: acceptable, note: Giữ tính mệnh lệnh và đối tượng Quân đội Cộng hòa.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000577, result: acceptable, note: Giữ cảm giác phân tâm và giọng vô tuyến đều đến phi thực.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000578, result: acceptable, note: Giữ nhịp lặp mệnh lệnh và Grantz cá nhân.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000579, result: acceptable, note: Toàn đoạn nghiêng đúng; mình là Grantz và giữ bước nhận ra đã giết người.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000580, result: revise, findings: [B18-M02]}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000581, result: acceptable, note: Giữ phản ứng nôn và mức có lẽ đang quen chiến đấu; Thiếu úy pending.}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000582, result: revise, findings: [B18-M01, B18-L02]}
  - {segment_id: YS-LN02/Text/part0030.xhtml/p000583, result: revise, findings: [B18-L06], note: Có khuyến nghị trung tính cho người bị giam giữ; Thiếu tá pending.}
risks:
  - Hai lỗi mức vừa vẫn mở; chưa đủ điều kiện nâng thành bản chuẩn.
  - Self-check tuyên bố giữ nhấn mạnh nhưng bản dịch thiếu ở p000573 và p000582.
  - Tám nhóm thuật ngữ/cấp bậc/xưng hô còn pending; không xác nhận canon hoặc sự nhất quán ngoài b18.
  - Cách hiểu p000582 không đủ căn cứ để phán quyết tính hợp pháp hoặc lore; áp dụng cách trung tính rồi tiếp tục.
  - Chưa kiểm tra validator hoặc diff-check; reviewer chỉ đọc và viết báo cáo.
next_action: >-
  Coordinator ghi nhận lựa chọn pending và giao translator đang giữ quyền sửa
  xử lý chín finding, cân nhắc hai khuyến nghị về người bị giam giữ và vốn con
  người, cập nhật self-check. Sau đó kiểm tra lại p000580, p000582 và phạm vi
  nhấn mạnh p000573/p000579/p000582, chạy validator/diff-check theo pipeline;
  không nâng bản chuẩn khi hai lỗi mức vừa chưa được giải quyết.
```
