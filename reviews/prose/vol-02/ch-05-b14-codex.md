# Review — vol-02-ch-05-b14

```yaml
role: reviewer
task_id: vol-02-ch-05-b14-review
state: done
review_path: reviews/prose/vol-02/ch-05-b14-codex.md
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000333
  - YS-LN02/Text/part0026.xhtml/p000334
  - YS-LN02/Text/part0026.xhtml/p000335
  - YS-LN02/Text/part0026.xhtml/p000336
  - YS-LN02/Text/part0026.xhtml/p000337
  - YS-LN02/Text/part0026.xhtml/p000338
  - YS-LN02/Text/part0026.xhtml/p000339
  - YS-LN02/Text/part0026.xhtml/p000340
  - YS-LN02/Text/part0026.xhtml/p000341
  - YS-LN02/Text/part0026.xhtml/p000342
  - YS-LN02/Text/part0026.xhtml/p000343
  - YS-LN02/Text/part0026.xhtml/p000344
  - YS-LN02/Text/part0026.xhtml/p000345
  - YS-LN02/Text/part0026.xhtml/p000346
  - YS-LN02/Text/part0026.xhtml/p000347
  - YS-LN02/Text/part0026.xhtml/p000348
  - YS-LN02/Text/part0026.xhtml/p000349
  - YS-LN02/Text/part0026.xhtml/p000350
  - YS-LN02/Text/part0026.xhtml/p000351
  - YS-LN02/Text/part0026.xhtml/p000352
  - YS-LN02/Text/part0026.xhtml/p000353
  - YS-LN02/Text/part0026.xhtml/p000354
  - YS-LN02/Text/part0026.xhtml/p000355
  - YS-LN02/Text/part0026.xhtml/p000356
  - YS-LN02/Text/part0026.xhtml/p000357
files_written:
  - reviews/prose/vol-02/ch-05-b14-codex.md
counts:
  reviewed_segments: 25
  serious: 0
  moderate: 2
  minor: 4
  total: 6
unresolved_findings: [R01, R02, R03, R04, R05, R06]
package_hash_verification:
  algorithm: sha256
  path: work/vol-02/batches/ch-05-b14-source.jsonl
  expected: 1b686a564fa130ce8d390bebad653222ec131bbd66ab5ba619c905d7b2ab1453
  actual: 1b686a564fa130ce8d390bebad653222ec131bbd66ab5ba619c905d7b2ab1453
  result: pass
  matches_review_handoff: true
  matches_batch_handoff: true
  source_units: 25
  translation_units: 25
  segment_ids_match_in_order: true
validator: not_run
diff_check: not_run
findings:
  - id: R01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000337
    related_segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000343
      - YS-LN02/Text/part0026.xhtml/p000353
    issue: Nội tâm tự quy chiếu của Tanya dùng “tôi”, lệch lựa chọn tạm “mình” trong ledger LN02.
    evidence: >-
      Hai câu đầu p000337 là suy nghĩ của Tanya trước khi chuyển sang trần thuật;
      p000343 là nội tâm về người sẽ chết; câu nói về đơn vị của bản thân ở
      p000353 cũng nằm ngoài thoại. Ledger ch05-b12 tiếp tục đề xuất “mình”
      cho nội tâm. Self-check chưa phát hiện các trường hợp này.
      DEC-P01-001 có giới hạn giai đoạn; căn cứ áp dụng tại LN02 là ledger
      tạm, không phải tự mở rộng canon.
    resolution: >-
      Đề nghị đổi các lần tự quy chiếu đó thành “mình”, gồm cả hai lần ở
      p000343 và “đơn vị mình” ở p000353; giữ “tôi” trong lời thoại.
    status: unresolved
  - id: R02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000350
    issue: Thêm ý cuộc tập kích làm nạn nhân “chết sớm hơn”.
    evidence: >-
      Nguồn giới hạn nhóm bị giết là những người mà Tanya cho rằng đằng nào
      cũng sẽ chết; không xác định cuộc tập kích đẩy thời điểm chết lên sớm.
      Bản dịch chuyển nhận định về đối tượng thành nhận định về thời gian.
    resolution: >-
      Đề nghị dùng “cũng chỉ giết những người đằng nào rồi cũng sẽ chết”,
      giữ giới hạn “cùng lắm” và thái độ xem nhẹ của người nói.
    status: unresolved
  - id: R03
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000353
    issue: Cách nói về lượng kinh nghiệm và tỷ lệ tổn thất chưa tự nhiên, hơi thu hẹp nghĩa.
    evidence: >-
      “Số trận chiến” quy lượng trải nghiệm thực chiến về số lần tham chiến,
      trong khi nguồn không chỉ định thước đo đó. “Thấp nhất vượt xa” ghép
      hướng so sánh cao và thấp gây vấp; “bị thương, dù chỉ từ từ” cũng khó đọc.
    resolution: >-
      Đề nghị “mức độ từng trải trong thực chiến”, “tỷ lệ tổn thất của đơn vị
      mình thấp hơn hẳn các đơn vị khác” và “binh sĩ bổ sung từ các đơn vị khác
      cũng bắt đầu lần lượt bị thương”. Giữ tiến trình chậm, không thêm tốc độ
      hay số lượng cụ thể.
    status: unresolved
  - id: R04
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000356
    issue: Phạm vi nhấn mạnh thứ hai thiếu từ nối hệ quả.
    evidence: >-
      XHTML đặt cả quan hệ hệ quả vào phần nhấn mạnh thứ hai;
      bản dịch để “nên” ngoài dấu sao. Lời cảnh báo thứ nhất giữ đúng phạm vi.
    resolution: Đề nghị đặt dấu sao bao trọn “nên đừng có chui hết vào cùng một chỗ!” theo DEC-P01-002.
    status: unresolved
  - id: R05
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000335
    issue: Lược mức chắc chắn của Tanya về sự thay đổi sau hai tháng sống sót.
    evidence: >-
      Điều kiện sống sót và thời lượng được giữ, nhưng lời xác quyết chủ quan
      của người nói chỉ còn “Dĩ nhiên ... lại là chuyện khác”.
    resolution: >-
      Đề nghị “Dĩ nhiên, tôi chắc rằng nếu họ sống sót được hai tháng ở Rhine
      thì lại là chuyện khác”; đây là thoại nên “tôi” phù hợp.
    status: unresolved
  - id: R06
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000357
    issue: “Cách viết thật sự” diễn đạt gượng, làm mờ yêu cầu thực sự hướng dẫn thao tác viết.
    evidence: >-
      Nguồn yêu cầu đi từng bước theo bảng chữ cái và thực sự dạy cách viết;
      bản dịch khiến “thật sự” giống thuộc tính của một kiểu viết.
    resolution: >-
      Đề nghị “Nếu không đi từng bước A-B-C và thực sự dạy họ cách viết từng
      chữ thì chẳng ích gì”. Giữ nhận ra thiếu hụt trải nghiệm của tiểu đoàn
      ở câu sau, không thêm nội dung huấn luyện cụ thể.
    status: unresolved
pending_terms:
  - source_term: infant military careers
    proposed_vi: mới chập chững vào đời binh nghiệp
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000335]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: field guns
    proposed_vi: pháo dã chiến
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000356]
    volume: vol-02
    chapter: 5
    status: pending
term_recommendations:
  - source_term: infant military careers
    proposed_vi: mới chập chững vào đời binh nghiệp
    alternatives_vi: [mới bắt đầu sự nghiệp quân ngũ, mới vào quân ngũ]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000335]
    status: pending
    confidence: 0.9
    rationale: >-
      Câu trước nói đến tuổi nhỏ của Tanya nhưng câu này chuyển tiêu chí sang
      thâm niên quân ngũ, rồi kiểm chứng bằng khả năng sống sót hai tháng.
      “Chập chững” giữ ẩn dụ non trẻ và giọng coi thường lính chưa từng trải,
      không biến họ thành trẻ em theo tuổi sinh học. Phương án trung tính
      làm rõ nghĩa nhưng giảm nét chơi trên hai bình diện tuổi và kinh nghiệm.
      Giữ lựa chọn ledger hiện tại như đề xuất tạm, không canon.
  - source_term: field guns
    proposed_vi: pháo dã chiến
    alternatives_vi: [pháo chiến trường]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000356]
    status: pending
    confidence: 0.85
    rationale: >-
      Ngữ cảnh phân biệt loại pháo mà chiến hào giúp giảm hiệu quả với pháo
      hạng nặng cỡ lớn bắn tập trung đủ sức phá bê tông cốt thép. “Pháo dã chiến”
      giữ nhãn loại vũ khí gọn và nhất quán ledger; “pháo chiến trường” rộng
      hơn, làm yếu sự phân biệt. Không suy thêm cỡ nòng, kiểu nòng hay
      mẫu pháo. Phạm vi kỹ thuật chính xác còn bất định; lựa chọn vẫn pending.
risks:
  - Chưa thể sign off bản dịch khi R01 và R02 còn mở; báo cáo hoàn tất không đồng nghĩa lô đã đạt.
  - Tên gọi, quân hàm và ánh xạ giọng LN02 vẫn là đề xuất; glossary và characters chính thức chưa chốt mục nào.
commit: null
next_action: coordinator_assign_translation_fixes
```

Đã đối chiếu đủ p000333–p000357 về nghĩa, văn phong, thuật ngữ, điểm nhìn,
tính nhất quán và nhấn mạnh. Các đoạn không nêu finding riêng vẫn đã được
kiểm tra. Trình tự trao đổi, sự khác biệt giữa quan điểm tiêu hao nhân lực của
Tanya và lo ngại tinh thần binh sĩ của đại tá được giữ. Các giới hạn quy mô
tập kích ở p000351, điều kiện nhận lệnh ở p000355 và cảnh chết ngạt trong
lô cốt ở p000356 không có lỗi nghĩa đáng kể khác.

p000341 giữ nhấn mạnh nhan đề theo XHTML; cách nối nhan đề với sự im ắng
giữ được ý mỉa mai. p000349 giữ đúng đối lập giữa chuẩn đánh giá của Tanya
và người bình thường. Các lựa chọn Thiếu tá, đại tá, pháp sư, Đế quốc,
Rhine và Dacia không mâu thuẫn với căn cứ tạm đã đọc; không xác lập thêm
địa hình, định danh hay canon. Báo cáo chỉ đề nghị sửa, chưa finding nào
được xử lý trong bản dịch.
