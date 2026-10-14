# Phản biện độc lập — vol-02-ch-07-b03

```yaml
role: reviewer
task_id: vol-02-ch-07-b03-review
state: done
review_path: reviews/prose/vol-02/ch-07-b03-codex.md
files_written: [reviews/prose/vol-02/ch-07-b03-codex.md]
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_assign_translation_revision
scope:
  source_package: work/vol-02/batches/ch-07-b03-source.jsonl
  expected_sha256: 12607922a93b34fd2af9d60c983b49e735829c3c44963023755abee473e372e6
  actual_sha256: 12607922a93b34fd2af9d60c983b49e735829c3c44963023755abee473e372e6
  hash_check: pass
  source_rows: 24
  translation_rows: 24
  ids_and_order_match: true
  segment_id_prefix: YS-LN02/Text/part0032.xhtml/
  segment_range: p000052–p000075
  reviewed_dimensions: [meaning, tactical_terminology, emphasis, viewpoint]
  input_paths:
    - agents/shared.md
    - agents/reviewer.md
    - config/translation-pipeline.yml
    - handoffs/vol-02/ch-07-b03-review.yml
    - handoffs/vol-02/ch-07-b03.yml
    - reviews/semantic/vol-02/ch-07-b03-self-check.md
    - translations/vol-02/ch-07-b03.jsonl
    - work/vol-02/batches/ch-07-b03-source.jsonl
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
  ledger_section_read: work/run-state/pending-terms.yml#chapter7_b03_translator_proposals
  evidence_policy: Đối chiếu tại chỗ; không trích câu nguồn, không đọc EPUB/PDF hoặc package khác.
counts:
  reviewed_rows: 24
  serious: 0
  moderate: 6
  minor: 5
  total_findings: 11
  unresolved_findings: 11
  pending_groups_assessed: 4
counting_method: Đếm theo finding, không đếm số đoạn bị ảnh hưởng; pending không tự động được tính là lỗi.
findings:
  - id: B03-C01
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000055
    affected_segment_ids:
      - YS-LN02/Text/part0032.xhtml/p000055
      - YS-LN02/Text/part0032.xhtml/p000058
      - YS-LN02/Text/part0032.xhtml/p000060
      - YS-LN02/Text/part0032.xhtml/p000063
      - YS-LN02/Text/part0032.xhtml/p000065
      - YS-LN02/Text/part0032.xhtml/p000066
      - YS-LN02/Text/part0032.xhtml/p000068
      - YS-LN02/Text/part0032.xhtml/p000069
      - YS-LN02/Text/part0032.xhtml/p000070
      - YS-LN02/Text/part0032.xhtml/p000074
      - YS-LN02/Text/part0032.xhtml/p000075
    issue: Nội tâm tự quy chiếu dùng “tôi” hoặc “chúng tôi/bọn tôi”, chưa nhất quán với DEC-P01-001.
    evidence: >-
      Các đoạn này là suy nghĩ ngôi thứ nhất của Tanya, xen với trần thuật về Tanya ở
      p000052/p000057 và thoại vô tuyến ở p000059/p000067. Quyết định đã duyệt yêu cầu
      “mình” cho nội tâm; self-check chỉ xác nhận ngôi thứ nhất nên bỏ sót yêu cầu này.
    resolution: >-
      Dùng “mình” khi Tanya tự quy chiếu; dùng “bọn mình/chúng mình” khi chủ thể là cả đơn vị,
      không biến chủ thể số nhiều thành riêng Tanya. Giữ “tôi” trong thoại vô tuyến.
      p000075 cần giữ rõ Tanya là người chấp nhận rủi ro và tránh nguy hiểm, còn nhóm ba người
      là bên rút lui và có cơ hội tới nơi an toàn; có thể nêu “mình” để tránh chủ thể bị lửng.
    status: open
  - id: B03-C02
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000052
    issue: “Dù có thể đang làm sĩ quan tham mưu” biến nhượng bộ về chức vụ thành sự chưa chắc chắn về chức vụ.
    evidence: >-
      Câu đặt vị thế sĩ quan tham mưu đối lập với thực tế phải chiến đấu để sống sót;
      không đưa ra hai khả năng về việc Tanya có giữ chức vụ ấy hay không.
    resolution: Dùng “Dù là sĩ quan tham mưu, Tanya vẫn…”; giữ nỗi ám ảnh về Being X và không bổ sung chức danh/cấp bậc.
    status: open
  - id: B03-C03
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000056
    issue: “Tổng tấn công” nâng quy mô/hình thức của cuộc tiến công quá mức chứng cứ.
    evidence: >-
      Lập luận chỉ cần dấu hiệu một cuộc tiến công lớn sắp diễn ra để giải thích việc
      đối phương giấu quân và hạn chế điều động dự bị; không xác định đó là tổng tấn công.
    resolution: >-
      Dùng “một cuộc tiến công lớn sắp diễn ra”. Có thể dùng “những cuộc trinh sát chiến đấu
      nhằm thăm dò” để giữ sắc thái dò tìm ở đầu đoạn. Giữ đúng hướng nhân quả và hành vi dự bị.
    status: open
  - id: B03-C04
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000060
    affected_segment_ids: [YS-LN02/Text/part0032.xhtml/p000060, YS-LN02/Text/part0032.xhtml/p000062]
    issue: “Bắn theo đội hình có kỷ luật” tự thêm đội hình; “hỏa lực có kỷ luật” ở p000062 chưa rõ nghĩa tác chiến.
    evidence: >-
      p000060–p000064 đối lập hỏa lực được tổ chức/kiểm soát với bắn nhiều nhưng ngắm kém.
      Việc radar bị làm mù ảnh hưởng điều khiển hỏa lực; nguồn không xác định đội hình bắn.
    resolution: >-
      Tạm dùng “khai hỏa có kiểm soát” ở p000060 và “hỏa lực có kiểm soát của các pháp sư”
      ở p000062. Không tự thêm bắn đồng loạt, tập trung, theo đội hình hay cơ chế kỹ thuật.
      Đây là diễn đạt tạm từ ngữ cảnh, chưa phải thuật ngữ canon.
    status: open
  - id: B03-C05
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000067
    affected_segment_ids: [YS-LN02/Text/part0032.xhtml/p000067, YS-LN02/Text/part0032.xhtml/p000074]
    issue: “Hai loạt” thay đổi đơn vị bắn và không khớp “hai phát” trong lời giải thích kế tiếp.
    evidence: >-
      Lệnh vô tuyến và suy nghĩ ở p000074 cùng nói tới hai lần bắn yểm trợ;
      package không cho căn cứ đổi thành hai loạt gồm nhiều phát.
    resolution: Dùng “Tôi sẽ bắn hai phát…” trong thoại; giữ “hai phát yểm trợ” tại p000074.
    status: open
  - id: B03-C06
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000074
    issue: “Khói mù từ những quả đạn nổ và đèn pha” khiến đèn pha thành nguồn sinh khói.
    evidence: >-
      Lý do vài phát bắn khó bị nhận ra là bầu trời đã đầy khói đạn nổ cùng ánh đèn pha;
      hai yếu tố cùng che lấp dấu hiệu bắn, không có quan hệ đèn pha tạo ra khói.
    resolution: Dùng “bầu trời vẫn đầy khói từ đạn nổ cùng ánh đèn pha”; giữ ba người rút lui và hai phát yểm trợ.
    status: open
  - id: B03-C07
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000058
    issue: Bỏ sắc thái chào đón nhiệt tình làm yếu giọng mỉa mai.
    evidence: Hỏa lực phòng không được trình bày như sự tiếp đón nhiệt tình của địch; đây là mỉa mai trong nội tâm Tanya.
    resolution: Dùng “nồng nhiệt chào đón bọn mình bằng…”; không thêm nhấn mạnh bằng chữ nghiêng.
    status: open
  - id: B03-C08
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000059
    issue: “Đang rút lui” đẩy thông báo dự định sang hành động đã bắt đầu.
    evidence: Fairy 08 thông báo bị trúng đạn và sẽ lui; p000067 tiếp đó giao yểm trợ và thời điểm lui.
    resolution: Tạm dùng “Sẽ rút lui” hoặc “Tôi sẽ lui lại”, giữ giọng vô tuyến gọn và mã gọi.
    status: open
  - id: B03-C09
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000069
    issue: “Định hướng xây dựng của tôi về tương lai” là kết hợp từ cứng, làm mờ lời tự tán thưởng có tính mỉa mai.
    evidence: Tanya chuyển từ tiếc khoản đầu tư sang tự khẳng định thái độ tích cực; không nói tới một định hướng xây dựng cụ thể.
    resolution: Tạm dùng “Đấy, mình hướng tới tương lai với tinh thần xây dựng như thế đó”; giữ nét tự biện hộ và không thêm bình luận đạo đức.
    status: open
  - id: B03-C10
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000072
    issue: “Quả thật có nguy cơ” làm lời thừa nhận dè dặt trở thành xác nhận chắc chắn.
    evidence: Tanya thừa nhận cách cảm nhận nguy hiểm của người nghiệp dư có thể đúng, rồi bác tính đầy đủ của lối suy nghĩ ấy.
    resolution: Dùng “Đúng là họ có thể có lý khi nhận thấy nguy cơ ở đó”; giữ sự nhượng bộ và giới hạn đánh giá.
    status: open
  - id: B03-C11
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000075
    issue: “Nếu có gì thì” không diễn đạt tự nhiên quan hệ chuyển ý và tăng sức khẳng định.
    evidence: Tanya bổ sung lợi thế của việc nhóm yểm trợ thu hút chú ý đối phương; không đặt điều kiện có sự việc nào xảy ra.
    resolution: Dùng “Thậm chí, mình còn có thể kỳ vọng…”; giữ tác dụng mồi nhử và cơ hội sống sót của nhóm rút lui.
    status: open
unresolved_findings: [B03-C01, B03-C02, B03-C03, B03-C04, B03-C05, B03-C06, B03-C07, B03-C08, B03-C09, B03-C10, B03-C11]
term_recommendations:
  - group: recon-in-force
    source_term: recon-in-force
    proposed_vi: trinh sát chiến đấu
    alternatives_vi: [trinh sát bằng vũ lực, trinh sát có vũ trang]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000053, YS-LN02/Text/part0032.xhtml/p000056, YS-LN02/Text/part0032.xhtml/p000058]
    contextual_segment_ids: [YS-LN02/Text/part0032.xhtml/p000057]
    status: pending
    canon: false
    confidence: medium
    rationale: >-
      Mục tiêu là dùng giao chiến thăm dò chuẩn bị phòng thủ/vị trí địch, chấp nhận thương vong,
      đồng thời làm địch tin rằng tiến công lớn sắp tới. “Trinh sát chiến đấu” diễn đạt gọn cả
      thu thập tình báo và giao chiến. “Trinh sát bằng vũ lực” vẫn hiểu được và không phải lỗi
      nghĩa bắt buộc sửa. “Trinh sát có vũ trang” chỉ nêu trang bị, dễ làm nhẹ tính giao chiến.
    uncertainty: Không xác lập tên thuật ngữ quân sự chuẩn từ package này; đây là đề xuất ngữ cảnh.
    ledger_note: p000057 chỉ diễn giải nhiệm vụ, không có thuật ngữ trực tiếp; không chèn thuật ngữ để khớp ledger.
  - group: battalion_name
    source_term: 203rd Aerial Mage Battalion
    proposed_vi: Tiểu đoàn Pháp sư Trên không số 203
    alternatives_vi: [Tiểu đoàn Pháp sư Không chiến số 203]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000054]
    status: pending
    canon: false
    confidence: medium
    rationale: >-
      Giữ tên tạm hiện dùng vì sát yếu tố trên không, đúng cấp tiểu đoàn và số hiệu 203;
      phù hợp việc đơn vị trải dọc tiền tuyến làm mồi nhử/hậu vệ. “Không chiến” tự nhiên hơn
      khi nhấn chức năng chiến đấu nhưng thu hẹp yếu tố trên không thành tác chiến trên không.
      Không cần đổi tên chỉ để sửa văn phong trong b03.
    uncertainty: Không kiểm chứng tiền lệ b01 ngoài phạm vi; canon tên/thuật ngữ hiện chưa chốt tên đơn vị này.
  - group: radar_and_visual_combat
    source_term: radar observers / visual combat
    proposed_vi: trắc thủ radar / tác chiến bằng quan sát trực tiếp
    alternatives_vi: [quan sát viên radar / tác chiến bằng mắt thường, trắc thủ radar / không chiến bằng mắt thường]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000061, YS-LN02/Text/part0032.xhtml/p000062]
    contextual_segment_ids: [YS-LN02/Text/part0032.xhtml/p000060]
    status: pending
    canon: false
    confidence: medium
    rationale: >-
      p000061 xác định nhân sự radar dẫn hướng hỏa lực, nên “trắc thủ radar” có căn cứ chức năng
      tốt hơn “quan sát viên radar”, dù chức danh chính thức chưa xác định. p000062 đối lập lệ
      thuộc dẫn hướng radar với giao chiến dựa trên quan sát trực tiếp; phương án này tránh hiểu
      “mắt thường” là khẳng định không dùng bất kỳ dụng cụ quang học nào. “Tác chiến bằng mắt
      thường” vẫn là lựa chọn tạm chấp nhận được. “Không chiến” thu hẹp phạm vi trong khi đoạn
      cũng bàn hỏa lực phòng không từ mặt đất, nên chưa ưu tiên.
    uncertainty: Không suy ra cấu trúc kíp radar hoặc phương thức ngắm bắn cụ thể.
    ledger_note: p000056 không chứa hai thuật ngữ này; cần sửa liên kết ở ledger khi coordinator tiếp nhận, không sửa báo cáo nguồn/ledger tại lượt review.
    related_finding: B03-C04
  - group: game_theory_and_zero_sum
    source_term: game theory / zero-sum
    proposed_vi: lý thuyết trò chơi / trò chơi tổng bằng không
    alternatives_vi: [lý thuyết trò chơi / tình thế tổng bằng không, lý thuyết trò chơi / tổng bằng không]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000075]
    status: pending
    canon: false
    confidence: high_for_local_meaning
    rationale: >-
      Giữ lựa chọn hiện dùng: lập luận nối lợi ích của Tanya với cơ hội nhóm rút lui tới nơi an
      toàn, phủ nhận việc một bên chỉ được lợi bằng mất mát tương ứng của bên kia. “Tình thế
      tổng bằng không” hoặc chỉ “tổng bằng không” giảm danh từ bổ sung và vẫn giữ phủ định;
      “trò chơi” có căn cứ ngay trong bình diện lý thuyết của câu trước.
    uncertainty: Đây là cách Tanya đánh giá tình huống, không phải kết luận khách quan về mọi bên tham chiến; không thêm khẳng định tất cả đều thắng.
pending_terms:
  - {source_term: recon-in-force, proposed_vi: trinh sát chiến đấu, segment_ids: [YS-LN02/Text/part0032.xhtml/p000053, YS-LN02/Text/part0032.xhtml/p000056, YS-LN02/Text/part0032.xhtml/p000058], volume: vol-02, chapter: 7, status: pending}
  - {source_term: 203rd Aerial Mage Battalion, proposed_vi: Tiểu đoàn Pháp sư Trên không số 203, segment_ids: [YS-LN02/Text/part0032.xhtml/p000054], volume: vol-02, chapter: 7, status: pending}
  - {source_term: radar observers / visual combat, proposed_vi: trắc thủ radar / tác chiến bằng quan sát trực tiếp, segment_ids: [YS-LN02/Text/part0032.xhtml/p000061, YS-LN02/Text/part0032.xhtml/p000062], volume: vol-02, chapter: 7, status: pending}
  - {source_term: game theory / zero-sum, proposed_vi: lý thuyết trò chơi / trò chơi tổng bằng không, segment_ids: [YS-LN02/Text/part0032.xhtml/p000075], volume: vol-02, chapter: 7, status: pending}
risks:
  - Sáu finding mức vừa còn mở; review hoàn tất không đồng nghĩa batch đủ điều kiện hoàn tất pipeline.
  - Self-check chưa nhận ra yêu cầu đại từ nội tâm đã chốt, hai phát/hai loạt và đội hình bị thêm.
  - Ledger b03 gắn recon-in-force vào p000057 theo ngữ cảnh và radar/visual vào p000056 không có thuật ngữ tương ứng; coordinator cần phân biệt liên kết trực tiếp với ngữ cảnh.
  - Cơ chế làm mù radar và chức danh radar chưa đủ căn cứ; dùng diễn đạt trung tính, không chốt lore hoặc canon.
  - Mọi đề xuất thuật ngữ ở báo cáo vẫn non-canon; không cần chờ người dùng để áp dụng tạm nhất quán trong phạm vi này.
```

## Bao phủ từng đoạn

Mã rút gọn dưới đây đều có tiền tố `YS-LN02/Text/part0032.xhtml/`. Cả bốn bình diện đã được kiểm tra ở từng dòng. Không dòng nguồn nào có đánh dấu nhấn mạnh trong XHTML được cung cấp; bản dịch không thêm chữ nghiêng, phù hợp DEC-P01-002. Những lỗi sắc thái nhấn mạnh bằng lời được ghi riêng, không đề nghị dùng định dạng để bù.

| Mã đoạn | Nghĩa và thuật ngữ tác chiến | Điểm nhìn và sắc thái | Kết quả |
|---|---|---|---|
| p000052 | Cần giữ nhượng bộ về chức vụ; Being X giữ tên tạm trong pending canon. | Trần thuật về Tanya, nỗi ám ảnh còn nguyên. | C02 |
| p000053 | Giữ nghi binh, bị buộc thực hiện, bất chấp tổn thất; thuật ngữ đề xuất G1. | Giọng trần thuật, không thêm phán xét. | Không có lỗi bắt buộc riêng. |
| p000054 | Đúng cấp/số hiệu, trải dọc tiền tuyến, cả mồi nhử và hậu vệ để che rút quân; G2. | Trần thuật, không suy ra đội hình mới. | Không có lỗi bắt buộc riêng. |
| p000055 | Giữ thứ tự pháo → bộ binh, bẫy đã bố trí, dự kiến vài giờ và câu giờ. | Nội tâm; mức phỏng đoán còn nhận diện được. | C01 |
| p000056 | Giữ dò chuẩn bị/vị trí và logic che quân/dự bị; quy mô tiến công bị nâng; G1. | Phân tích khái quát, không cần thêm đại từ. | C03 |
| p000057 | Giữ điều kiện mua thời gian cho quân rút và nghĩa vụ theo lệnh. | “Nó” về Tanya đúng DEC-P01-001. | Không có lỗi bắt buộc riêng. |
| p000058 | Giữ thu thập tình báo, phòng không dày, đánh chặn từ căn cứ sâu và thương vong; G1. | Nội tâm; mỉa mai tiếp đón bị làm nhẹ. | C01, C07 |
| p000059 | Đúng mã gọi và báo trúng đạn; thời điểm rút cần chỉnh. | Thoại vô tuyến, “tôi” được giữ. | C08 |
| p000060 | Giữ mất khả năng chiến đấu và radar bị làm mù; không có căn cứ thêm đội hình. | Nội tâm; chủ thể làm mù là phía Tanya, nên giữ rõ nếu viết lại. | C01, C04 |
| p000061 | Đúng radar dẫn hướng và khả thể đánh chặn hiệu quả hơn; G3. | Dè dặt, giữ giả định quá khứ. | Không có lỗi bắt buộc riêng. |
| p000062 | Đúng đối lập radar/hỏa lực pháp sư với quan sát trực tiếp; cần làm rõ hỏa lực; G3. | Giữ đánh giá rất kém của Tanya. | C04 |
| p000063 | Giữ nguyên nhân chủ yếu là lượng đạn lớn và hình ảnh sắt thép. | Nội tâm, không đổi sang nguyên nhân duy nhất. | C01 |
| p000064 | Giữ bắn nhiều vẫn trúng dù ngắm kém. | Câu cảm thán và đánh giá tiêu cực còn nguyên. | Không có lỗi bắt buộc riêng. |
| p000065 | Giữ tiếc cơ hội đầu tư cổ phiếu đạn dược trước cảnh phung phí. | Nội tâm và giọng tính toán/mỉa mai; cần thống nhất tự quy chiếu. | C01 |
| p000066 | Giữ giá đơn vị/lợi nhuận thấp đối lập doanh số lớn, tiền lương đã đầu tư và khả năng sai lầm. | Nội tâm; “tài nguyên thiên nhiên” hợp ngữ cảnh, không suy ra công ty/ngành cụ thể. | C01 |
| p000067 | Giữ 06/09 yểm trợ người trúng đạn và lui trong thời gian Tanya bắn; hai phát bị đổi thành hai loạt. | Thoại mệnh lệnh, “tôi” giữ nguyên. | C05 |
| p000068 | Giữ không đảo ngược quá khứ, xem lại kết luận và áp dụng bài học về sau. | Nội tâm có cả “mình” và “tôi”, cần nhất quán. | C01 |
| p000069 | Giữ tự khẳng định thái độ tích cực, cần diễn đạt tự nhiên. | Nội tâm và giọng tự tán thưởng. | C01, C09 |
| p000070 | Giữ bù chỗ trống, muốn tránh nguy hiểm và bác bỏ không yểm trợ vì sợ. | Câu hỏi mở đúng đối tượng; nội tâm. | C01 |
| p000071 | Giữ sợ nguy cơ nhìn thấy → sợ hành động → bất động. | Phân tích khái quát về người nghiệp dư. | Không có lỗi bắt buộc riêng. |
| p000072 | Giữ nguy cơ lộ vị trí; cần khôi phục mức chắc chắn của nhượng bộ. | Đánh giá tư duy nghiệp dư, không thêm phán xét đạo đức. | C10 |
| p000073 | Giữ không hành động là mất cơ hội hành động. | Câu khái quát ngắn, giữ trọng tâm. | Không có lỗi bắt buộc riêng. |
| p000074 | Đúng hai thuộc cấp + người bị thương = ba người, hai phát và khó nhận ra; sửa khói/ánh đèn. | Nội tâm, tính lợi ích của việc yểm trợ còn nguyên. | C01, C06 |
| p000075 | Đúng hút chú ý khi rút, rủi ro nhỏ để tránh nguy hiểm, cơ hội an toàn và phủ định tổng bằng không; G4. | Cần rõ chủ thể Tanya/nhóm rút và sửa câu chuyển ý. | C01, C11 |

G1–G4 lần lượt là bốn nhóm trong `term_recommendations`. Các lựa chọn tạm đủ căn cứ để coordinator tiếp nhận và translator áp dụng; không có yêu cầu quyết định canon ảnh hưởng cốt truyện trong phạm vi review này. Reviewer không sửa bản dịch, ledger, handoff hoặc self-check.
