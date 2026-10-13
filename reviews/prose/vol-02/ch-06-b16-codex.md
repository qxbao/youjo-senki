# Review b16 — Codex

```yaml
role: reviewer
task_id: vol-02-ch-06-b16-review
state: done
review_path: reviews/prose/vol-02/ch-06-b16-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b16-codex.md
source_verification:
  path: work/vol-02/batches/ch-06-b16-source.jsonl
  expected_sha256: c4e7416296680421de9b4e6c93a90e7a5f5c7f25c299eec8804f1ca203d974ca
  actual_sha256: c4e7416296680421de9b4e6c93a90e7a5f5c7f25c299eec8804f1ca203d974ca
  result: pass
  units: 31
  only_source_text: assigned_package
runtime_policy: config/translation-pipeline.yml runtime.reviewer
scope:
  translation: translations/vol-02/ch-06-b16.jsonl
  self_check: reviews/semantic/vol-02/ch-06-b16-self-check.md
  primary_handoff: handoffs/vol-02/ch-06-b16.yml
  review_handoff: handoffs/vol-02/ch-06-b16-review.yml
  ledger: eight b16 entries in work/run-state/pending-terms.yml
  canon_references:
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
validator: not_run
diff_check: not_run
commit: null
counts:
  reviewed_ids: 31
  assessed_proposals: 8
  serious: 0
  moderate: 6
  minor: 3
  total_findings: 9
  unresolved_findings: 9
  ids_with_findings: 9
severity_mapping:
  serious: nghiêm trọng
  moderate: vừa
  minor: nhẹ
findings:
  - finding_id: B16-F01
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000479
    issue: Quy mô ngoài dự liệu bị cụ thể hóa thành lớn hơn dự kiến; cách nói về hỏa lực còn cứng.
    evidence: >-
      Gói nguồn xác nhận mọi người đã tránh được phản công và đội hình bị xáo trộn;
      quy mô không được dự liệu, nhưng không trực tiếp so sánh lớn/nhỏ với dự kiến.
      Tính có tổ chức thuộc việc bắn của quân Cộng hòa.
    resolution: >-
      Tạm dùng “đợt phản công có quy mô ngoài dự liệu” và “hỏa lực được tổ chức
      bài bản của quân Cộng hòa”. Giữ kết quả né đòn đã xảy ra và nhận định rằng
      tốc độ cùng cơ động phân tán đơn thuần sẽ không đủ vượt các vị trí hỏa lực.
    confidence: 0.85
    status: open
  - finding_id: B16-F02
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000480
    issue: Mất nhấn mạnh của toàn bộ đoạn nội tâm.
    evidence: XHTML trong package đánh dấu toàn bộ đoạn bằng em; translation không có dấu sao.
    resolution: Bọc toàn bộ translation bằng *...* theo DEC-P01-002; giữ tính giả định và mức có thể gặp rắc rối.
    confidence: 1.0
    status: open
  - finding_id: B16-F03
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000481
    issue: Tự thêm dạng bào chế và đơn vị dùng “một viên”.
    evidence: Nguồn chỉ yêu cầu tonic; không xác định thuốc dạng viên hay liều lượng.
    resolution: >-
      Dùng “Cho tôi xin ít thuốc bổ được không?” hoặc “Cho tôi xin thuốc bổ được
      không?”. Có thể sửa “tự nhiên tôi thấy mệt” thành “tôi thấy mệt lạ thường”
      để làm rõ mức mệt bất thường thay vì chỉ thời điểm xuất hiện.
    confidence: 0.94
    status: open
  - finding_id: B16-F04
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000482
    issue: Quan hệ đồng thời bị đổi thành xác nhận một dự đoán.
    evidence: >-
      Đầu đoạn đặt tiếng Weiss vang lên trong lúc Tanya suy nghĩ; bản dịch
      “Đúng như nó nghĩ” gán cho Tanya một dự đoán đã được xác nhận. Câu hỏi
      tiếp theo thể hiện sự bất ngờ trước việc Weiss mệt.
    resolution: >-
      Đổi mở đoạn thành “Trong lúc nó đang suy nghĩ, giọng nói mệt mỏi của
      Trung úy Weiss vang lên qua radio…”. Giữ “mình” trong phần tự vấn về
      phó chỉ huy, không tự thêm chữ nghiêng vì đoạn này không có em.
    confidence: 0.98
    status: open
  - finding_id: B16-F05
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000493
    issue: Hai lần dùng “cô” trong trần thuật về Tanya trái với phương án tạm của chính b16.
    evidence: >-
      Đoạn này là trần thuật ngôi ba. Self-check chọn “nó” cho Tanya ở phạm vi
      hiện tại, nhưng translation dùng “thuộc hạ của cô” và “mặt bằng chung của cô”.
      DEC-P01-001 chỉ đã duyệt trong giai đoạn pilot, không tự xác lập canon cho LN02.
    resolution: >-
      Áp dụng nhất quán đề xuất tạm b16: “thuộc hạ của nó” và “một pháp sư có
      năng lực trên mức trung bình trong đơn vị của nó”. Giữ “anh” cho Weiss;
      giữ tính dường như của suy nghĩ về chiến dịch và khả năng đạt đẳng cấp,
      không biến thành thành tích Ace of Aces đã được xác nhận.
    confidence: 0.97
    status: open
  - finding_id: B16-F06
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000505
    issue: “Xét về con người” và “xét theo lý lẽ” thiếu tự nhiên, làm mờ hai bình diện tự biện hộ.
    evidence: >-
      Tanya đối chiếu đánh giá với tư cách một con người và tính thuận tiện theo
      logic; sau đó tự nhận lòng nhân ái. Đây là lời tự đánh giá của nhân vật.
    resolution: >-
      Tạm dùng “Với tư cách một con người, làm vậy chẳng hay ho gì. Xét về mặt
      logic, tiêu diệt họ sẽ dễ hơn…”. Giữ lời tự nhận nhân ái và ý tránh liên
      lụy người vô tội; không thêm lời kể xác nhận hoặc phủ nhận phẩm chất ấy.
    confidence: 0.9
    status: open
  - finding_id: B16-F07
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000507
    issue: Mất nhấn mạnh ở câu tự vấn cuối đoạn.
    evidence: Chỉ câu cuối được đánh dấu em trong package.
    resolution: >-
      Bọc riêng “Trời ạ, cậu ghét tham gia một cuộc thảm sát đến thế sao?” bằng
      *...*, không bọc cả đoạn. Đề xuất tạm đổi “cậu” thành “anh” để thống nhất
      đối tượng Weiss với p000503; đây là nội tâm hướng tới anh, không phải thoại phát ra.
    confidence: 1.0
    status: open
  - finding_id: B16-F08
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000508
    issue: Mất hai vùng nhấn mạnh phân cách bởi lời trần thuật.
    evidence: >-
      Package đánh dấu phần tự nhận không thích và phần nhận định về cái chết;
      lời kể tự giễu ở giữa không được nhấn mạnh.
    resolution: >-
      Dạng đề xuất: “*Chà, mình không thích chuyện này*, nó tự giễu,
      *nhưng hoàn cảnh đòi hỏi phe thân Cộng hòa ở Arene phải chết.*”. Giữ
      riêng hai vùng nhấn mạnh và ranh giới giữa nội tâm với trần thuật.
    confidence: 1.0
    status: open
  - finding_id: B16-F09
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000509
    issue: Không làm gì bị diễn giải thành chủ động làm ngơ.
    evidence: >-
      Lập luận tự biện hộ phủ nhận hành động trực tiếp rồi mới viện hình ảnh
      ba con khỉ. Bản dịch nhập kết luận làm ngơ vào mệnh đề trước hình ảnh đó.
    resolution: >-
      Đổi thành “Mình chỉ tham gia theo nghĩa rộng thôi. Mình chỉ chẳng làm gì,
      như ba con khỉ thông thái kia: không thấy điều ác, không nghe điều ác,
      không nói điều ác.” Giữ giọng tự miễn trách nhiệm và đủ ba hành vi.
    confidence: 0.93
    status: open
unresolved_findings:
  - B16-F01
  - B16-F02
  - B16-F03
  - B16-F04
  - B16-F05
  - B16-F06
  - B16-F07
  - B16-F08
  - B16-F09
term_recommendations:
  - source_term: tonic
    proposed_vi: thuốc bổ
    alternatives_vi: [thuốc tăng lực, thuốc bồi bổ]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000481]
    rationale: Nghĩa rộng phù hợp yêu cầu khi mệt; không đủ căn cứ xác định dạng bào chế hoặc chất kích thích.
    confidence: 0.82
    status: pending
    canon: false
  - source_term: soldier fuel
    proposed_vi: nhiên liệu của người lính
    alternatives_vi: [nhiên liệu cho lính, thứ tiếp sức cho người lính]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000483]
    rationale: Giữ ẩn dụ về rượu và sắc thái đùa cợt; không thêm công dụng y tế.
    confidence: 0.93
    status: pending
    canon: false
  - source_term: war addict(s)
    proposed_vi: đám nghiện chiến tranh
    alternatives_vi: [đám mê chiến trận, những kẻ nghiện chiến tranh]
    segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000487
      - YS-LN02/Text/part0030.xhtml/p000488
    rationale: >-
      Dùng ở p000488 để giữ cường điệu trong nội tâm. p000487 dùng hình ảnh
      berserkers, nên giữ “kẻ cuồng chiến”, không thay cả hai bằng một nhãn.
      Không coi cách gọi của Tanya là chẩn đoán khách quan.
    confidence: 0.94
    status: pending
    canon: false
  - source_term: Ace of Aces
    proposed_vi: Ace of Aces
    alternatives_vi: [bậc ace hàng đầu, át chủ bài trong các át chủ bài]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000493]
    rationale: >-
      Giữ định danh tạm trong cấu trúc “đẳng cấp Ace of Aces”. Package cho biết
      đây là mức năng lực có thể đạt, chưa cho biết tiêu chuẩn, danh hiệu chính
      thức hay số chiến công; không tự bổ sung thông tin lore.
    confidence: 0.78
    status: pending
    canon: false
  - source_term: modern individuals
    proposed_vi: những con người hiện đại
    alternatives_vi: [những cá nhân hiện đại]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000499]
    rationale: Giữ nghĩa rộng gắn với lý trí và thị trường; không tự đổi thành tầng lớp doanh nhân hoặc hệ tư tưởng cụ thể.
    confidence: 0.92
    status: pending
    canon: false
  - source_term: three wise monkeys
    proposed_vi: ba con khỉ thông thái
    alternatives_vi: [ba con khỉ tam không]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000509]
    rationale: Giữ hình ảnh đếm được và đủ ba hành vi; chỉ dùng “tam không” sẽ làm mất hình ảnh con khỉ.
    confidence: 0.95
    status: pending
    canon: false
  - source_term: Lieutenant / First Lieutenant / Major
    proposed_vi: Trung úy / Thượng úy / Thiếu tá
    alternatives_vi: [giữ tên quân hàm tiếng Anh khi cần đối chiếu]
    segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000481
      - YS-LN02/Text/part0030.xhtml/p000482
      - YS-LN02/Text/part0030.xhtml/p000484
      - YS-LN02/Text/part0030.xhtml/p000490
      - YS-LN02/Text/part0030.xhtml/p000493
      - YS-LN02/Text/part0030.xhtml/p000495
    rationale: >-
      Tạm giữ ánh xạ của b16. Nguồn gọi Weiss bằng dạng rút gọn ở p000482,
      p000484 và dạng đầy đủ ở p000493; chưa có căn cứ kết luận anh đổi cấp
      hoặc tự sửa mọi lời gọi thành Thượng úy. p000490 không có quân hàm,
      nên không thêm dù ledger và self-check gắn cờ ID này.
    confidence: 0.72
    status: pending
    canon: false
  - source_term: viewpoint pronouns Tanya/Weiss
    proposed_vi: Tanya trần thuật “nó”, nội tâm “mình”; Weiss trần thuật “anh”; thoại dùng chức danh hoặc lược đại từ khi phù hợp
    alternatives_vi: [lặp tên Tanya ở chỗ cần phân biệt chủ thể, dùng tên hoặc quân hàm khi chưa đủ căn cứ xưng hô]
    segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000482
      - YS-LN02/Text/part0030.xhtml/p000483
      - YS-LN02/Text/part0030.xhtml/p000487
      - YS-LN02/Text/part0030.xhtml/p000488
      - YS-LN02/Text/part0030.xhtml/p000492
      - YS-LN02/Text/part0030.xhtml/p000493
      - YS-LN02/Text/part0030.xhtml/p000502
      - YS-LN02/Text/part0030.xhtml/p000507
      - YS-LN02/Text/part0030.xhtml/p000508
      - YS-LN02/Text/part0030.xhtml/p000509
    rationale: >-
      Giữ phương án nội bộ b16 đã nêu trong self-check. Giới hạn của DEC-P01-001
      không cho tự nâng cách gọi LN02 thành canon. Package hỗ trợ chủ thể
      Weiss và Serebryakov ở các đoạn có đại từ; “cô ấy” cho Serebryakov trong
      trần thuật không chứng minh quan hệ tuổi tác hoặc thân thuộc. p000483
      “của mình” là phản thân trong trần thuật, không tự biến cả câu thành nội tâm.
      p000502 có thể dùng “Rõ… Chúc may mắn.” để tránh thêm cách gọi “cô”;
      p000507 chọn “anh” tạm cho người được Tanya hướng ý nghĩ tới.
    confidence: 0.87
    status: pending
    canon: false
meaning_recommendations:
  - segment_id: YS-LN02/Text/part0030.xhtml/p000508
    proposed_vi: hoàn cảnh đòi hỏi phe thân Cộng hòa ở Arene phải chết
    alternatives_vi: [hoàn cảnh đòi hỏi những người du kích ở Arene phải chết]
    rationale: >-
      Đối tượng phải chết là nhóm partisan, không phải Tanya, Weiss hoặc toàn
      bộ cư dân. p000504 hỗ trợ liên hệ với phe thân Cộng hòa cố thủ ở Arene.
      “Du kích” là cách hiểu từ vựng có thể có, nhưng gói này chưa xác lập
      chiến thuật hay tổ chức du kích; dùng “phe thân Cộng hòa” trung tính hơn.
      Không chuyển thành khẳng định mọi người vô tội đều thuộc nhóm này, cũng
      không suy ra trong nhóm tuyệt đối không có dân thường. “Phải chết” giữ
      kết quả được hoàn cảnh đòi hỏi mà không tự thêm chủ thể ra tay giết.
    confidence: 0.84
    status: pending
    canon: false
coverage:
  id_prefix: YS-LN02/Text/part0030.xhtml/
  checked_dimensions: [meaning, prose, viewpoint_pronouns, emphasis, ranks, terminology]
  per_id:
    p000479: B16-F01; né phản công là kết quả thực tế, không phải kết quả giả định.
    p000480: B16-F02; giữ điều kiện tương lai và khả năng gặp rắc rối.
    p000481: B16-F03; thuật ngữ và quân hàm tạm như đề xuất.
    p000482: B16-F04; Tanya trần thuật chuyển sang nội tâm tự vấn đúng chủ thể.
    p000483: Không có lỗi bắt buộc; rượu được đưa cho phụ tá và Serebryakov đi kiểm tra.
    p000484: Không có lỗi bắt buộc; người bị bắn là Weiss, giữ mệnh lệnh cầm máu.
    p000485: Không có lỗi bắt buộc; phản ứng ngắn được giữ.
    p000486: Không có lỗi bắt buộc; giữ việc không nhận ra thương tích và yêu cầu garô.
    p000487: Không có lỗi bắt buộc; người nói đúng là Serebryakov, không phải Weiss.
    p000488: Không có lỗi bắt buộc; phủ định việc đã cho dùng meth và thế lưỡng nan đều còn.
    p000489: Không có lỗi bắt buộc; câu hỏi về tình trạng Weiss, không đổi thành hỏi vị trí.
    p000490: Không có lỗi bắt buộc; không nguy hiểm tính mạng nhưng khó tiếp tục chiến đấu, không thêm quân hàm.
    p000491: Không có lỗi bắt buộc; lệnh rút lui và sự miễn cưỡng được giữ.
    p000492: Không có lỗi bắt buộc; lo mất phụ tá và chuyển sang cân nhắc vấn đề về sau được giữ.
    p000493: B16-F05; đề xuất giữ Ace of Aces và phân biệt quân hàm rút gọn/đầy đủ.
    p000494: Không có lỗi bắt buộc; điều kiện không phải ngẫu nhiên và năng lực đánh chặn được giữ.
    p000495: Không có lỗi bắt buộc; lời phản đối ngắt giữa chừng, Major tạm là Thiếu tá.
    p000496: Không có lỗi bắt buộc; Weiss tập hợp người bị thương để về căn cứ, không cho cả đơn vị rút.
    p000497: Không có lỗi bắt buộc; lời tự nhận sáng suốt thuộc điểm nhìn Tanya.
    p000498: Không có lỗi bắt buộc; kiệt sức dự kiến và giá trị nhân sự sáng suốt được giữ.
    p000499: Không có lỗi bắt buộc; lý trí, thị trường và xã hội tư bản tương lai được giữ.
    p000500: Không có lỗi bắt buộc; câu hỏi về kinh tế hậu chiến vẫn là điều kiện.
    p000501: Không có lỗi bắt buộc; câu hỏi đổi lương thành vàng/hàng hóa và dự cảm thắng/thua đều còn.
    p000502: Không có lỗi bắt buộc; đề xuất lược “cô” để giữ lời chúc trung tính.
    p000503: Không có lỗi bắt buộc; lời trách do dự và đe dọa xử lý khi quay về đều còn.
    p000504: Không có lỗi bắt buộc; cần sống sót và nhiệm vụ đánh phe thân Cộng hòa được giữ.
    p000505: B16-F06; giữ lập luận nhân quyền và lời tự nhận nhân ái, không diễn giải lore.
    p000506: Không có lỗi bắt buộc; nhận định pháp lý thuộc ý nghĩ nhân vật, do dự dẫn đến bị bắn.
    p000507: B16-F07; giả định đặt mình vào vị trí Weiss và ghen tị vì tránh trách nhiệm được giữ.
    p000508: B16-F08; xem meaning_recommendations về phạm vi đối tượng và cách gọi trung tính.
    p000509: B16-F09; giữ tự biện hộ về không hành động và hình ảnh ba con khỉ.
risks:
  - >-
    p000479 và p000480 thuộc hai bình diện thời gian: né được phản công đã xảy ra,
    còn nguy cơ khi gặp quân Đỏ là giả định. Không sửa đoạn đầu thành khả năng
    chưa xảy ra, cũng không biến đoạn sau thành thất bại chắc chắn.
  - >-
    Các ánh xạ quân hàm và đại từ LN02 chỉ là đề xuất tạm. Không xác nhận cấp
    bậc toàn dự án hoặc mở rộng phạm vi canon pilot từ báo cáo này.
  - >-
    p000505–p000509 giữ góc nhìn tự biện hộ của Tanya. Không xem lời nhận định
    pháp lý/đạo đức trong nội tâm là kết luận khách quan của reviewer.
  - >-
    p000508 chưa đủ căn cứ xác lập thành phần dân sự hay chiến thuật du kích
    của phe ở Arene. Chọn cách gọi trung tính và tiếp tục; không cần quyết
    định canon ảnh hưởng cốt truyện để xử lý lô này.
limitations:
  - Không mở EPUB/PDF hoặc package khác; không kiểm chứng sự nhất quán thực tế với b14/b15.
  - Bản dịch chưa được sửa; findings còn mở cho người giữ quyền sửa tiếp nhận.
next_action: translator_revision_then_targeted_recheck
```
