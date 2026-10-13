# Review độc lập — vol-02-ch-06-b21

```yaml
role: reviewer
task_id: vol-02-ch-06-b21-review
state: done
review_path: reviews/prose/vol-02/ch-06-b21-codex.md
files_written: [reviews/prose/vol-02/ch-06-b21-codex.md]
segment_id_prefix: YS-LN02/Text/part0030.xhtml/
segment_ids: [p000644, p000645, p000646, p000647, p000648, p000649, p000650, p000651, p000652, p000653, p000654, p000655, p000656, p000657, p000658, p000659, p000660, p000661, p000662, p000663, p000664, p000665, p000666, p000667, p000668, p000669, p000670, p000671, p000672]
id_convention: Mọi mã p trong báo cáo nối với segment_id_prefix để thành mã đoạn đầy đủ, ổn định.
input_verification:
  source_package: work/vol-02/batches/ch-06-b21-source.jsonl
  source_package_sha256: 7cbc9cfc8f06bae5e818fddda061f1a6ca05b00c014e96bb6c75140fb8ad29e8
  hash_match: true
  source_rows: 29
  translation_rows: 29
  ordered_ids_match: true
  canon_reference_hashes_match_primary_handoff: true
  read_scope:
    - agents/shared.md
    - agents/reviewer.md
    - config/translation-pipeline.yml
    - handoffs/vol-02/ch-06-b21-review.yml
    - handoffs/vol-02/ch-06-b21.yml
    - work/vol-02/batches/ch-06-b21-source.jsonl
    - translations/vol-02/ch-06-b21.jsonl
    - reviews/semantic/vol-02/ch-06-b21-self-check.md
    - work/run-state/pending-terms.yml#chapter6_b21_translator_proposals
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
  epub_pdf_opened: false
  other_packages_opened: false
  source_sentences_in_report: false
counts:
  rows_reviewed: 29
  rows_with_findings: 10
  rows_without_findings: 19
  serious: 0
  moderate: 6
  minor: 4
  total_findings: 10
  unresolved_findings: 10
  pending_groups_assessed: 8
  pending_groups_remaining_non_canon: 8
findings:
  - id: B21-R01
    severity: moderate
    segment_id: p000644
    issue: “Chẳng hợp thời” chuyển sự thiếu nhạy cảm với hoàn cảnh thành chuyện hợp thời đại hoặc thời thượng.
    evidence: Ngữ cảnh p000645–p000646 nói về cảm giác ăn thịt sau khi chứng kiến chiến trường, không bàn sự lỗi thời của thực đơn.
    resolution: Đổi thành “chẳng hợp hoàn cảnh chút nào” hoặc “thật vô tâm khi chọn món ấy”.
    alternatives: ['món chính lại là bò hầm, thật chẳng đúng lúc chút nào']
    status: unresolved
  - id: B21-R02
    severity: moderate
    segment_ids: [p000644, p000645, p000646]
    issue: Mất chữ nghiêng có sẵn trong XHTML nguồn.
    evidence: p000644 và p000645 có em bao toàn đoạn; p000646 có hai vùng em, chỉ tên món doria nằm giữa chúng không nghiêng. Bản dịch ba đoạn đều không đánh dấu.
    resolution: Theo DEC-P01-002, bọc toàn p000644 và p000645 bằng dấu sao. Ở p000646 đánh dấu hai vùng nghĩa tương ứng; giữ phần dịch tên món “cơm đút lò” ngoài chữ nghiêng và giữ phần nghĩa “thịt” trong chữ nghiêng khi sắp lại từ.
    alternatives: [Giữ tên món doria không nghiêng giữa hai vùng dịch nghiêng nếu cần bảo toàn ranh giới dễ đối chiếu hơn; vẫn chỉ là đề xuất cách gọi món.]
    status: unresolved
  - id: B21-R03
    severity: moderate
    segment_id: p000646
    issue: Câu cuối chưa giữ rõ giả định nhìn lại bữa ăn vừa diễn ra.
    evidence: Nguồn dùng cấu trúc giả định hoàn thành; “chắc ... chẳng ... nổi đâu” dễ thành dự đoán cho hiện tại hoặc tương lai.
    resolution: Dùng “Ừ, nếu lúc nãy là món cơm đút lò thịt thì chắc mình cũng đã chẳng nuốt nổi.” Kết hợp sửa chữ nghiêng theo B21-R02.
    alternatives: ['Ừ, giả sử lúc ấy ăn cơm đút lò thịt thì mình nghĩ mình cũng đã chẳng nuốt nổi.']
    status: unresolved
  - id: B21-R04
    severity: moderate
    segment_id: p000651
    issue: “Binh lính” mở rộng đối tượng đang được lập luận trực tiếp từ chi phí đào tạo pháp sư.
    evidence: Đại từ số nhiều nối ngay sau việc đào tạo một pháp sư; cách đọc gần nhất là những pháp sư ấy, không phải mọi binh lính nói chung.
    resolution: Dùng “đâu thể để các pháp sư cứ ngã xuống la liệt trên chiến trường như vậy”.
    alternatives: ['đâu thể để những người ấy ngã xuống la liệt trên chiến trường như vậy — nếu muốn tránh giải đại từ quá cụ thể.']
    status: unresolved
  - id: B21-R05
    severity: moderate
    segment_id: p000652
    issue: Biến trạng thái đóng quân kéo dài đến gần đây thành sự kiện bị điều ra tiền tuyến đúng hôm kia.
    evidence: Nguồn có mốc kết thúc hoặc giới hạn của trạng thái đóng quân; không xác định ngày điều động, cũng không chốt chính xác hai ngày trước.
    resolution: Dùng “cho đến tận mới đây, ... vẫn còn đóng quân ở tiền tuyến”. Giữ nguyên giả định bất cân xứng vũ khí ở phần sau.
    alternatives: ['mãi đến mấy hôm trước, ... vẫn còn ở tiền tuyến']
    status: unresolved
  - id: B21-R06
    severity: moderate
    segment_id: p000654
    issue: Mất mốc quá khứ của nhận định không chắc chắn về khả năng làm quân nhân của Einstein.
    evidence: Nguồn đặt khả năng đó trong quá khứ; “có thể chẳng giỏi” không giữ rõ mốc này. Không có cơ sở chuyển sang khẳng định lịch sử hoặc giả định Einstein thực sự phục vụ quân đội.
    resolution: Dùng “Tiến sĩ Einstein có thể đã chẳng giỏi làm quân nhân, nhưng ông ấy đã cống hiến cho đất nước ...”.
    alternatives: ['Có thể trước đây Tiến sĩ Einstein không giỏi làm quân nhân, nhưng ...']
    status: unresolved
  - id: B21-R07
    severity: minor
    segment_id: p000655
    issue: “Tuyến đầu tiên” dễ được hiểu là thứ tự tuyến thay vì vị trí tiền tuyến xa nhất về phía trước.
    evidence: So sánh nhấn vị trí trực tiếp ở tuyến trước cùng để minh họa việc dùng nhân lực sai chỗ.
    resolution: Đổi thành “đặt Nobel ngay ở tuyến đầu”.
    alternatives: ['đưa Nobel ra tận tuyến trước cùng']
    status: unresolved
  - id: B21-R08
    severity: minor
    segment_id: p000659
    issue: “Lãng phí ... hoang phí” lặp nghĩa và làm câu nội tâm vấp.
    evidence: Cần giữ mức phung phí nhưng không cần hai lần cùng một động tác trong câu hỏi.
    resolution: Dùng “A, sao lại phung phí vốn con người đến thế?”.
    alternatives: ['A, sao lại lãng phí vốn con người đến mức ấy?']
    status: unresolved
  - id: B21-R09
    severity: minor
    segment_id: p000667
    issue: Thêm lượng “nhiều” khi nguồn không lượng hóa số mạng người được cứu.
    evidence: Nghĩa cứu mạng được nêu không kèm mức độ nhiều; chữ nghiêng chỉ ở từ nối đã được giữ đúng bằng *và*.
    resolution: Dùng “Đúng là chúng ta đã cứu được mạng người *và* tiêu diệt các pháp sư địch.”
    alternatives: ['Đúng là chúng ta đã cứu người *và* tiêu diệt các pháp sư địch.']
    status: unresolved
  - id: B21-R10
    severity: minor
    segment_id: p000671
    issue: Cấu trúc “không nhận nhiều hơn số người mà bốn mươi tám người có thể quản lý” khó đọc; cách gọi nguồn tin thêm mục đích bắt người hơi cụ thể.
    evidence: Cú pháp gần nhất đặt nhóm 48 người làm chủ thể có năng lực xử lý, với tù binh là đối tượng ngầm từ mạch trước. Nguồn xác định người bị bắt là nguồn tin, không nói riêng rằng mục đích ban đầu của việc bắt là khai thác tin tức.
    resolution: Dùng “đơn vị mình chỉ nhận số tù binh trong khả năng quản lý của bốn mươi tám người”; gọi nhóm nguồn tin là “những người bị bắt làm nguồn tin”. Đây là diễn đạt tạm, không xác lập tổng quân số hoặc chính sách bắt giữ.
    alternatives:
      - “đơn vị mình không nhận quá khả năng xử lý của bốn mươi tám người” để giữ đối tượng ngầm rộng hơn.
      - “những nguồn tin bị bắt giữ” nếu ưu tiên giữ giọng công cụ hóa con người của lời kể.
    status: unresolved
focused_checks:
  p000667:
    emphasis: pass
    evidence: XHTML chỉ đặt em ở từ nối; bản dịch chỉ đặt dấu sao ở “và”.
    meaning: Cứu mạng và tiêu diệt pháp sư địch là hai thành tích cùng chủ thể; giữ quan hệ cộng thêm, chỉ bỏ lượng thêm theo B21-R09.
  p000671:
    preferred_reading: 48 người là chủ thể của năng lực quản lý hoặc xử lý; tù binh là đối tượng ngầm được ngữ cảnh hỗ trợ tốt nhất.
    confidence: medium_high
    current_rendering: Giữ đúng cách đọc chủ thể gần nhất, nhưng đã giải đối tượng ngầm thành số người được nhận; không hoàn toàn bảo toàn mọi độ mở của động tác xử lý.
    rejected_as_default: Mức trần tuyệt đối 48 tù binh; cú pháp không đặt con số trực tiếp vào giới hạn tù binh.
    remaining_uncertainty: Không đủ dữ liệu b21 để khẳng định 48 người là toàn bộ quân số đơn vị, hay giới hạn xử lý gồm những hoạt động cụ thể nào.
    temporary_choice: Áp dụng B21-R10; nếu cần literal hơn, chọn phương án “không nhận quá khả năng xử lý của bốn mươi tám người”. Không dừng chờ canon.
  pronouns:
    result: Nội tâm tự quy chiếu dùng “mình” nhất quán với DEC-P01-001; p000647 dùng tên Tanya, không tạo đại từ trần thuật mới.
    notes: “Ông ấy” ở p000654 và p000655 có tiền ngữ Einstein và Nobel rõ; p000670 hiểu đối tượng quản lý là cấp dưới là đúng, không phải bản báo cáo. “Chúng mình” ở p000671 hiểu được nhưng “đơn vị mình” hoặc “chúng ta” có thể hợp giọng quân sự hơn; không xác lập quy tắc đại từ tập thể mới.
row_checks:
  p000644: B21-R01, B21-R02.
  p000645: Nghĩa và thái độ không muốn ăn đúng; B21-R02.
  p000646: Quan hệ cảnh chiến trường và khó ăn, cùng tên món được chuyển nghĩa hợp lý; B21-R02, B21-R03.
  p000647: Giữ chuyển sang trần thuật và giọng càu nhàu đùa cợt.
  p000648: Giữ phân biệt tranh luận với thực thi, câu hỏi phản bác và các lý lẽ phủ nhận dân thường; không xác nhận các lý lẽ ấy là sự thật.
  p000649: Giữ điều thường không xảy ra, hai yếu tố cùng tồn tại và phán xét về thời đại.
  p000650: Giữ giả định sử dụng khôn ngoan, phán xét lãng phí và tự đính chính sang việc phớt lờ. “Người thân” là cách literal khả dụng của kin, nhưng không dùng nó để suy ra quan hệ gia đình cụ thể trong truyện.
  p000651: Giữ câu hỏi đầu tư và chi phí đào tạo; B21-R04.
  p000652: Giữ học vị, hệ quả bỏ bê khoa học và giả định địch có vũ khí mà ta không có; B21-R05; P-B21-03.
  p000653: Giữ giả định Manhattan, đối lập phe và ngoại lệ nhà khoa học điên; không tự xác định danh tính người này.
  p000654: Giữ so sánh giá trị đóng góp và đối lập súng với bút chì; B21-R06; P-B21-04.
  p000655: Giữ so sánh, nghiên cứu nitroglycerin và mục đích tránh lãng phí; B21-R07.
  p000656: Giữ kết luận vì tương lai nhân loại.
  p000657: Giữ lời dẫn theo Wiki như một phần lời kể, cùng đối lập hiệu quả; không kiểm chứng hoặc biến nó thành khẳng định ngoài truyện.
  p000658: Giữ điều muốn thêm nếu là người kể và đối tượng bảo vệ vốn con người.
  p000659: Giữ điều kiện nhiều vị trí thiếu tài năng và giải pháp rút người khỏi tiền tuyến; B21-R08.
  p000660: Giữ độ chắc chắn nghe nói và việc đang chấn chỉnh.
  p000661: Giữ giới hạn chỉ có thể làm và việc viết lại để nộp.
  p000662: Giữ tàu, hoàn cảnh chiến tranh và cảm giác chán.
  p000663: Giữ việc đã bị triệu và thái độ chịu đựng.
  p000664: Giữ khả thể thảnh thơi, nghỉ phép đã được cho và bố trí quân trong tương lai; không cần suy diễn thời điểm mới.
  p000665: Giữ câu hỏi vì sao chỉ mình phải trình diện và thủ đô; P-B21-05.
  p000666: Giữ tự kiểm điểm nghiêm túc, lý do có thể bị triệu và phủ định đã mắc lỗi.
  p000667: Phạm vi nhấn mạnh đúng; B21-R09.
  p000668: Giữ mốc trước đó, Rhine, thành tích và hình thức trao thưởng giản dị; P-B21-06 không xác định loại hoặc hạng huân chương.
  p000669: Giữ phủ định có hành vi đáng ngại.
  p000670: Giữ kiểm soát cấp dưới, quy định tiểu đoàn, tránh tòa án quân sự và dấu chú thích 22; không mở chú thích ngoài package.
  p000671: Giữ phủ định ngược đãi và tra tấn, tần suất hiếm, đối lập với đám nghiệp dư, gánh nặng nuôi người và mức dễ hơn chỉ đôi chút; B21-R10 và focused_checks.
  p000672: Giữ hai phẩm chất cùng một đơn vị, ít phiền toái và câu hỏi vì sao bị triệu; P-B21-08.
term_recommendations:
  - id: P-B21-01
    source_term: human capital
    proposed_vi: vốn con người
    alternatives_vi: [vốn nhân lực]
    segment_ids: [p000651, p000655, p000658, p000659]
    rationale: Nhất quán P03-human-capital trong glossary-pending; mạch đầu tư, đào tạo, bảo vệ và lãng phí cho thấy cách nhìn con người như vốn.
    uncertainty: low
    status: pending
    canon: false
  - id: P-B21-02
    source_term: mage
    proposed_vi: pháp sư
    alternatives_vi: [ma pháp sư]
    segment_ids: [p000651, p000667]
    rationale: Cách gọi trung tính, nhất quán hai lần xuất hiện; nguồn cho thấy người được đào tạo và chiến đấu, chưa nêu phân loại hoặc cấp bậc chuyên biệt.
    uncertainty: low
    status: pending
    canon: false
  - id: P-B21-03
    source_term: VT fuses
    proposed_vi: ngòi nổ VT
    alternatives_vi: [ngòi nổ cận đích VT, ngòi nổ tiệm cận VT]
    segment_ids: [p000652]
    rationale: Package chỉ nêu ký hiệu, không giải thích cơ chế. Chọn cách literal ít suy diễn nhất trong phạm vi đọc được phép; không suy từ radar rằng ngòi nổ dùng cùng một cơ chế.
    uncertainty: medium
    note: Các phương án khai triển có thể được xét riêng khi có căn cứ kỹ thuật được phép; không coi sự thiếu giải thích trong package là bằng chứng bản hiện tại sai cơ chế.
    status: pending
    canon: false
  - id: P-B21-04
    source_term: rank-and-file soldier
    proposed_vi: người lính bình thường
    alternatives_vi: [binh lính thông thường, người lính trong hàng ngũ]
    segment_ids: [p000654]
    rationale: Đối chiếu đóng góp của nhà khoa học với người lính thông thường; tránh tự gán quân hàm binh nhì hoặc đánh giá chất lượng yếu kém.
    uncertainty: low
    status: pending
    canon: false
  - id: P-B21-05
    source_term: General Staff Office
    proposed_vi: Bộ Tổng tham mưu
    alternatives_vi: [cơ quan Tổng tham mưu]
    segment_ids: [p000665]
    rationale: Địa điểm trình diện của cơ quan tham mưu cấp trung ương ở thủ đô; giữ đề xuất hiện có như tên gọi tạm. Phương án cơ quan Tổng tham mưu trung tính hơn nếu tránh xác lập danh xưng tổ chức.
    uncertainty: medium
    note: Không chốt cơ cấu tổ chức, cấp bậc hoặc tên canon từ một lần xuất hiện.
    status: pending
    canon: false
  - id: P-B21-06
    source_term: decoration
    proposed_vi: huân chương
    alternatives_vi: [phần thưởng quân sự, huân huy chương]
    segment_ids: [p000668]
    rationale: Trao thưởng cho chiến công trong bối cảnh quân sự hỗ trợ cách gọi hiện có; không thêm tên, hạng hoặc chất liệu. “Phần thưởng quân sự” là lựa chọn rộng hơn nếu loại vật phẩm chưa đủ rõ.
    uncertainty: medium
    status: pending
    canon: false
  - id: P-B21-07
    source_term: prisoners / captured information sources
    proposed_vi: tù binh / những người bị bắt làm nguồn tin
    alternatives_vi: ['người bị bắt / những nguồn tin bị bắt giữ', 'tù binh / những người bị bắt để khai thác tin tức']
    segment_ids: [p000671]
    rationale: Mạch bắt giữ của đơn vị quân sự và nuôi tù binh hỗ trợ “tù binh”; vế nguồn tin giữ vai trò khai thác thông tin mà giảm việc gán mục đích ban đầu của việc bắt người. Giữ độ lạnh và tính công cụ của lời kể, không thêm kết luận pháp lý về đối tượng.
    uncertainty: medium
    note: Nếu cần tránh gán tư cách tù binh cho mọi người bị bắt, dùng phương án rộng “người bị bắt”; không quyết định canon hoặc diễn giải lore.
    status: pending
    canon: false
  - id: P-B21-08
    source_term: international laws
    proposed_vi: luật pháp quốc tế
    alternatives_vi: [luật quốc tế]
    segment_ids: [p000672]
    rationale: Giữ phạm vi rộng của cách gọi trong lời kể; không thu hẹp thành luật nhân đạo quốc tế hoặc tự thêm tên công ước.
    uncertainty: low
    status: pending
    canon: false
pending_choices: Các tám mục term_recommendations là khuyến nghị áp dụng tạm; coordinator ghi ledger và handoff, không nâng thành canon.
unresolved_findings: [B21-R01, B21-R02, B21-R03, B21-R04, B21-R05, B21-R06, B21-R07, B21-R08, B21-R09, B21-R10]
risks:
  - Self-check chưa phát hiện mất chữ nghiêng ở p000644–p000646; phải đối chiếu XHTML chứ không chỉ trường text.
  - p000671 có thể bị sửa quá tay thành trần 48 tù binh hoặc khẳng định tổng quân số đơn vị; tránh cả hai.
  - VT chưa được giải nghĩa bằng tài liệu trong phạm vi; đề xuất literal vẫn đủ để tiếp tục, không cần dừng chờ quyết định thuật ngữ.
  - Tên cơ quan, loại phần thưởng và tư cách người bị bắt chỉ là đề xuất theo b21; không suy ra lore hoặc hệ thống pháp lý ngoài package.
  - Sáu lỗi mức vừa còn mở; lô chưa đủ điều kiện hoàn tất pipeline dù review này đã xong.
validator: not_run
diff_check: not_run
commit: null
next_action: Coordinator tiếp nhận khuyến nghị pending vào ledger và handoff; giao người giữ lease translations sửa B21-R01–R10, rồi đối chiếu lại các mã bị sửa và chạy validator cùng diff-check trước khi hoàn tất lô.
```
