```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-06-b22-review
batch: vol-02-ch-06-b22
state: done
review_path: reviews/prose/vol-02/ch-06-b22-codex.md
files_written: [reviews/prose/vol-02/ch-06-b22-codex.md]
source_package: work/vol-02/batches/ch-06-b22-source.jsonl
source_package_sha256: 934b216d2e43f95024350f9dde7b33cea51e64670f540d3a4f2b9f6d2ea2e94f
hash_check: match
segment_id_prefix: YS-LN02/Text/part0030.xhtml/
segment_ids:
  - YS-LN02/Text/part0030.xhtml/p000673
  - YS-LN02/Text/part0030.xhtml/p000674
  - YS-LN02/Text/part0030.xhtml/p000675
  - YS-LN02/Text/part0030.xhtml/p000676
  - YS-LN02/Text/part0030.xhtml/p000677
  - YS-LN02/Text/part0030.xhtml/p000678
  - YS-LN02/Text/part0030.xhtml/p000679
  - YS-LN02/Text/part0030.xhtml/p000680
  - YS-LN02/Text/part0030.xhtml/p000681
  - YS-LN02/Text/part0030.xhtml/p000682
  - YS-LN02/Text/part0030.xhtml/p000683
  - YS-LN02/Text/part0030.xhtml/p000684
  - YS-LN02/Text/part0030.xhtml/p000685
  - YS-LN02/Text/part0030.xhtml/p000686
  - YS-LN02/Text/part0030.xhtml/p000687
  - YS-LN02/Text/part0030.xhtml/p000688
  - YS-LN02/Text/part0030.xhtml/p000689
  - YS-LN02/Text/part0030.xhtml/p000690
  - YS-LN02/Text/part0030.xhtml/p000691
  - YS-LN02/Text/part0030.xhtml/p000692
  - YS-LN02/Text/part0030.xhtml/p000693
  - YS-LN02/Text/part0030.xhtml/p000694
  - YS-LN02/Text/part0030.xhtml/p000695
  - YS-LN02/Text/part0030.xhtml/p000696
  - YS-LN02/Text/part0030.xhtml/p000697
  - YS-LN02/Text/part0030.xhtml/p000698
  - YS-LN02/Text/part0030.xhtml/p000699
  - YS-LN02/Text/part0030.xhtml/p000700
  - YS-LN02/Text/part0030.xhtml/p000701
  - YS-LN02/Text/part0030.xhtml/p000702
  - YS-LN02/Text/part0030.xhtml/p000703
  - YS-LN02/Text/part0030.xhtml/p000704
  - YS-LN02/Text/part0030.xhtml/p000705
  - YS-LN02/Text/part0030.xhtml/p000706
  - YS-LN02/Text/part0030.xhtml/p000707
  - YS-LN02/Text/part0030.xhtml/p000708
scope:
  read:
    - agents/shared.md
    - agents/reviewer.md
    - config/translation-pipeline.yml
    - work/vol-02/batches/ch-06-b22-source.jsonl
    - translations/vol-02/ch-06-b22.jsonl
    - reviews/semantic/vol-02/ch-06-b22-self-check.md
    - handoffs/vol-02/ch-06-b22.yml
    - handoffs/vol-02/ch-06-b22-review.yml
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
    - work/run-state/pending-terms.yml#chapter6_b22_translator_proposals
  external_lookup: false
  other_source_packages_opened: false
  epub_pdf_opened: false
  note: >-
    Có đọc hướng dẫn skill graphify ngoài đầu vào nội dung; không chạy graphify,
    không đọc graph hoặc mở rộng corpus. Ledger được phân tích cục bộ để lấy
    đúng section b22; không dùng các section khác làm căn cứ.
counts:
  source_rows: 36
  translation_rows: 36
  reviewed_rows: 36
  missing_rows: 0
  duplicate_or_reordered_ids: 0
  serious: 0
  moderate: 6
  minor: 6
  findings_total: 12
  unresolved_findings: 12
  pending_proposal_groups_assessed: 6
  source_emphasis_spans: 2
  preserved_emphasis_spans: 1
findings:
  - id: B22-C01
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000683
    issue: Mất chữ nghiêng ở thán từ mở đầu.
    evidence: XHTML trong package chỉ nhấn thán từ; bản dịch không có dấu Markdown ở đây.
    resolution: Đổi thán từ tương ứng thành '*À*'; giữ phần sau không nghiêng theo DEC-P01-002.
    status: unresolved
  - id: B22-C02
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000676
    related_segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000675
      - YS-LN02/Text/part0030.xhtml/p000677
      - YS-LN02/Text/part0030.xhtml/p000686
      - YS-LN02/Text/part0030.xhtml/p000693
      - YS-LN02/Text/part0030.xhtml/p000694
      - YS-LN02/Text/part0030.xhtml/p000695
    issue: Nội tâm tự quy chiếu còn dùng tôi, không nhất quán với DEC-P01-001 và p000703–p000705.
    evidence: >-
      Đây là các đoạn nhớ lại, suy đoán hoặc tự hỏi không đặt trong lời thoại.
      p000675 có cả thoại, hành động và phần tự xét phép tắc; phải phân biệt từng phần.
    resolution: >-
      Dùng mình cho tự quy chiếu trong nội tâm; tại p000675 giữ tôi trong thoại,
      xét riêng phần kể hành động và đổi tự quy chiếu ở phần nghĩ về phép tắc.
      Không đổi hàng loạt tôi trong thoại hoặc coi mọi ngôi thứ nhất là nội tâm.
    status: unresolved
  - id: B22-C03
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000676
    related_segment_ids:
      - YS-LN02/Text/part0030.xhtml/p000678
      - YS-LN02/Text/part0030.xhtml/p000688
      - YS-LN02/Text/part0030.xhtml/p000690
    issue: Bộ Đường sắt và Cục Hậu cần tự xác định cấp tổ chức khi package chưa xác lập.
    evidence: >-
      Cơ quan đường sắt được đặt trong quân đội; Logistics không kèm cấp tổ chức.
      p000676 dùng Cục Hậu cần, nhưng p000678 dùng ngành Hậu cần;
      self-check chỉ khai báo lựa chọn Hậu cần.
    resolution: >-
      Tạm dùng cơ quan đường sắt của quân đội hoặc cơ quan đường sắt theo ngữ cảnh,
      và bộ phận hậu cần/ngành hậu cần; bỏ cấp Bộ/Cục chưa có căn cứ.
      Coordinator ghi phương án tạm, không nâng thành canon.
    status: unresolved
  - id: B22-C04
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000689
    issue: Sĩ quan chiến trường thu hẹp một cụm có thể chỉ nhóm quân hàm.
    evidence: >-
      field officers có khả năng là cách gọi nhóm sĩ quan theo cấp bậc;
      package đặt người nói trong bối cảnh thiếu tá và chỉ huy tiểu đoàn,
      nhưng chưa đủ để chốt hệ quy đổi hoặc loại trừ nghĩa phục vụ ngoài thực địa.
    resolution: >-
      Tạm dùng một trong các sĩ quan được vận chuyển. Phương án sĩ quan cấp tá
      cần được giữ pending nếu chọn; không mặc định là sĩ quan chiến trường.
    status: unresolved
  - id: B22-C05
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000696
    issue: Rút lui khỏi phòng tuyến làm mờ ý lùi vị trí của chính phòng tuyến.
    evidence: >-
      Đối tượng dịch chuyển trong lời Uger là phòng tuyến Rhine;
      p000697 mới là câu Tanya hỏi lại về rút lui. Bản dịch đã nhập hai mức diễn đạt.
    resolution: Tạm dùng 'Nghe nói cấp trên đang tính lùi phòng tuyến Rhine về phía sau.'
    status: unresolved
  - id: B22-C06
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000700
    issue: Vừa...vừa... thêm quan hệ đồng thời giữa lui quân và gây tổn thất.
    evidence: >-
      Package nối hai hành động nhưng không chốt chúng xảy ra đồng thời;
      p000701 diễn giải việc lùi quân như một cách gây tổn thất cho địch.
    resolution: >-
      Tạm dùng 'Có lẽ họ định lùi quân và khiến địch đổ máu.'
      Nếu dùng để thì coi đó là diễn giải theo p000701, không thêm tác chiến cụ thể.
    status: unresolved
  - id: B22-C07
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000681
    issue: Chỉ đóng vai trò ngầm thêm mức hạn định; gắn kết dễ thiên về tình cảm.
    evidence: >-
      Package mô tả ảnh hưởng hậu cảnh của họp đồng môn và thứ bậc quân hàm
      lên các quan hệ sĩ quan. Ngữ cảnh p000678/p000687 thiên về mạng lưới có ích.
      Không có căn cứ đảo quan hệ thành đồng môn xóa bỏ thứ bậc.
    resolution: >-
      Bỏ chỉ; tạm diễn đạt rằng các cuộc họp mặt đồng môn và thứ bậc quân hàm
      tuy tác động ở hậu cảnh vẫn thúc đẩy sĩ quan tạo quan hệ với nhau.
      Có thể giữ mối quan hệ quen biết; không tự thêm bè phái hoặc bảo trợ.
    status: unresolved
  - id: B22-C08
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000690
    issue: Đại quân hùng mạnh thêm đánh giá và có thể gợi một tên quân đội đã xác lập.
    evidence: >-
      Package dùng Great Army, không phải Grand Army; không xác lập danh tính
      lịch sử hoặc lore. Hình ảnh con voi quá đồ sộ và chuỗi thiếu vận chuyển,
      không tập trung được sức chiến đấu đã được giữ đúng.
    resolution: >-
      Tạm dùng đại quân, bỏ hùng mạnh; nếu giữ viết hoa Đại quân thì ghi là
      lựa chọn biên tập pending. Không thêm tên lịch sử hay giải thích ẩn dụ.
    status: unresolved
  - id: B22-C09
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000694
    issue: Láu cá gợi sự ranh mãnh thay vì thái độ tỏ ra khôn hoặc nói xấc.
    evidence: Người nói đang tự hạn định vai trò chiến thuật, không nhận mình dùng mưu mẹo.
    resolution: Tạm dùng 'Mình không có ý ra vẻ biết hơn người'; giữ giọng tự xét.
    status: unresolved
  - id: B22-C10
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000703
    issue: Doanh nghiệp thua lỗ thu hẹp enterprise vào một tổ chức kinh doanh cụ thể.
    evidence: >-
      Đoạn đối chiếu tiền đã đầu tư với tổn thất tiếp theo và tự chê óc kinh tế
      bị cùn. Logic chi phí chìm và sắc thái tự châm biếm cơ bản được giữ;
      không có đảo ý thành phải tiếp tục đầu tư. Package không nhận diện Concorde.
    resolution: >-
      Tạm dùng công cuộc không sinh lời hoặc dự án không sinh lời;
      giữ đối lập đừng tiếc tiền đã bỏ ra/hãy tiếc tổn thất phát sinh thêm.
      Không chèn giải thích chi phí chìm hoặc xác định Concorde vào bản dịch.
    status: unresolved
  - id: B22-C11
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000704
    issue: Kẻ tin tưởng trung thành này của tinh thần... là kết hợp từ gượng và mờ đối tượng tin tưởng.
    evidence: >-
      Tanya tự ví mình như tín đồ của tinh thần hiện đại, thực dụng;
      câu hỏi vẫn là nghi vấn về ý định Being X, không phải xác nhận âm mưu.
    resolution: Tạm dùng 'Hay Being X định hủy diệt tín đồ trung thành của tinh thần hiện đại, thực dụng này?'
    status: unresolved
  - id: B22-C12
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000706
    issue: Vẫn... rút lui sao dễ gợi một cuộc rút lui đang tiếp diễn.
    evidence: >-
      Lời thoại trở lại sự khó chấp nhận ý tưởng rút lui sau phần tự kiểm điểm;
      package chưa nói cuộc rút lui đã bắt đầu.
    resolution: Tạm dùng 'Dù vậy… rút lui sao?' để giữ sắc thái ngập ngừng phản vấn.
    status: unresolved
unresolved_findings:
  - B22-C01
  - B22-C02
  - B22-C03
  - B22-C04
  - B22-C05
  - B22-C06
  - B22-C07
  - B22-C08
  - B22-C09
  - B22-C10
  - B22-C11
  - B22-C12
row_audit:
  p000673: Đạt nghĩa chào hỏi; Thiếu tá là đề xuất tạm.
  p000674: Giữ nhận diện giọng, áo sĩ quan cấp trung, vị trí cửa khoang; tôi trong kể hành động cần phân biệt với nội tâm.
  p000675: Giữ lời đáp, động tác và khả thể về phép tắc; xem C02.
  p000676: Giữ ký ức chưa chắc chắn và hai khả năng nơi công tác; xem C02/C03.
  p000677: Giữ trình tự thăng hàm và dự đoán trung tá; cấp trung không tự đổi thành một quân hàm; xem C02.
  p000678: Giữ hai hướng công tác và động cơ duy trì quan hệ; xem C03.
  p000679: Giữ người được hỏi và thông tin Arene; không thêm sự kiện.
  p000680: Giữ lý do không tiết lộ chi tiết.
  p000681: Quan hệ đồng môn, thứ bậc và mạng lưới cơ bản đúng; xem C07.
  p000682: Giữ việc được Zettour sai đi và câu hỏi đáp lại; Tướng quân chỉ là cách gọi tạm, không chốt cấp tướng cụ thể.
  p000683: Giữ suy đoán vai trò đưa tin; mất nhấn mạnh, xem C01.
  p000684: Giữ đối tượng hỏi là Tanya; không đủ căn cứ để kết luận lỗi phân vai.
  p000685: Cách xưng cô phù hợp tạm với Uger nói tiếp trước khi tiết lộ ở p000688; không ép thành lời Tanya.
  p000686: Giữ hoài nghi khả năng giữ bí mật và sự tin cậy; xem C02.
  p000687: Giữ bộ ba quan hệ, ảnh hưởng, mạng lưới.
  p000688: Giữ yêu cầu lên kế hoạch vận chuyển khẩn cấp và đi báo cáo; xem C03.
  p000689: Giữ câu hỏi và giới hạn cùng lắm; xem C04.
  p000690: Giữ chuỗi vận chuyển–cơ động–tập trung sức chiến đấu và ẩn dụ con voi; xem C03/C08 và T05.
  p000691: Giữ mức phỏng đoán và tần suất.
  p000692: Cũng phải chấp nhận được trong mạch tự xét điều vừa nêu.
  p000693: Giữ câu hỏi về liên hệ với lý do triệu tập; xem C02.
  p000694: Giữ pháp sư, chỉ huy tiểu đoàn, giới hạn chiến thuật và hai cách di chuyển; xem C02/C09.
  p000695: Giữ ý không thấy lý do triệu về thủ đô; xem C02.
  p000696: Giữ thông tin còn qua lời nghe; phạm vi rút phòng tuyến cần sửa, xem C05.
  p000697: Giữ câu hỏi xác nhận rút lui và người được hỏi.
  p000698: Giữ chuyển sang ngôi ba và độ trễ vì sốc; dùng tên Tanya hợp lệ, không buộc thêm nó.
  p000699: Giữ phản vấn về công sức tiến quân; không tự thêm chữ nghiêng.
  p000700: Giữ phỏng đoán chủ ý cấp trên và địch là bên chịu tổn thất; xem C06.
  p000701: Giữ diễn giải và ngạc nhiên về quy mô Cannae; không suy ra chi tiết chiến thuật ngoài package.
  p000702: Giữ bất ngờ, mức quyết liệt và đánh giá thú vị; táo bạo chấp nhận được trong ngữ cảnh.
  p000703: Giữ tự châm biếm, đối lập chi phí đã bỏ ra/tổn thất tiếp theo và mất sắc sảo; xem C10/T06.
  p000704: Giữ nghi vấn về Being X, bối cảnh và suýt tê liệt cảm nhận; xem C11.
  p000705: Giữ mong thoát chiến tranh và đề nghị thay bằng chiến tranh kinh tế.
  p000706: Xem C12 về sắc thái nối lại lời thoại.
  p000707: Giữ đúng phạm vi chữ nghiêng, phần dẫn nghĩ không nghiêng; mức ngưỡng mộ đúng.
  p000708: Giữ so sánh thương vong có điều kiện, chỉnh phòng tuyến và khả năng đối đầu; không tự thêm bao vây.
term_recommendations:
  - id: T01
    source_term: Major / Lieutenant Colonel
    proposed_vi: Thiếu tá / trung tá
    alternatives_vi: [giữ nguyên tên quân hàm tiếng Anh]
    segment_ids: [p000673, p000675, p000676, p000677, p000686]
    rationale: >-
      Package phân biệt cấp đang mang với cấp có thể được thăng;
      hai cách dịch giữ được phân biệt đó. Không dùng sĩ quan cấp trung thay
      cho quân hàm nêu rõ, cũng không suy ngược middle ranks thành thiếu tá.
    uncertainty: Chưa có bảng quân hàm canon; đại úy ở p000677 cũng chỉ là lựa chọn tạm.
    status: pending
    canon: false
  - id: T02
    source_term: Railroad Department
    proposed_vi: cơ quan đường sắt của quân đội
    alternatives_vi: [bộ phận đường sắt, Cục Đường sắt]
    segment_ids: [p000676, p000688, p000690]
    rationale: >-
      Quan hệ thuộc quân đội có trong package; cấp Bộ hoặc Cục chưa được xác lập.
      Có thể rút còn cơ quan đường sắt khi sở thuộc đã rõ. Cục ít gợi bộ dân sự
      hơn Bộ, nhưng vẫn cần chứng cứ tổ chức nên chưa ưu tiên.
    uncertainty: Không chốt tên riêng và cấp hành chính của cơ quan.
    status: pending
    canon: false
  - id: T03
    source_term: Logistics / General Staff
    proposed_vi: hậu cần / Bộ Tổng tham mưu
    alternatives_vi: [bộ phận hậu cần / cơ quan tổng tham mưu]
    segment_ids: [p000676, p000678]
    rationale: >-
      Logistics chỉ lĩnh vực hoặc nơi công tác, không đủ căn cứ cho Cục.
      Ngành hậu cần thích hợp ở p000678; bộ phận hậu cần thích hợp ở p000676.
      Bộ Tổng tham mưu giữ chức năng và đối lập với vị trí giảng viên,
      nhưng chưa xác lập quan hệ với tên cơ quan ở lô khác.
    uncertainty: Không dùng lời self-check về đề xuất lô trước làm chứng cứ đã duyệt.
    status: pending
    canon: false
  - id: T04
    source_term: mage / Being X
    proposed_vi: pháp sư / Being X
    alternatives_vi: [thuật sĩ / Thực thể X]
    segment_ids: [p000694, p000704]
    rationale: >-
      Pháp sư giữ loại nhân sự có khả năng bay mà không tự thêm cấp chuyên môn;
      package chưa phân biệt các hệ phép. Being X khớp đề xuất P05-being-x
      trong canon/glossary-pending.yml; Thực thể X là phương án Việt hóa còn mở.
    uncertainty: Canon được đọc không chốt mage; b22 ledger cho phép lựa chọn tạm này.
    status: pending
    canon: false
  - id: T05
    source_term: interior lines strategy
    proposed_vi: chiến lược nội tuyến
    alternatives_vi: [chiến lược hoạt động theo tuyến trong]
    segment_ids: [p000690]
    rationale: >-
      Có thể giữ tạm cách gọi gọn hiện tại: package gắn chiến lược với đường sắt,
      điều chuyển lực lượng và tập trung sức chiến đấu. Phương án tuyến trong
      dễ đọc hơn nhưng kém gọn. Không đồng nhất với phòng thủ thuần túy,
      chiến đấu trong nội địa hoặc đường dây bí mật.
    uncertainty: Đánh giá từ ngữ cảnh package; chưa xác minh danh pháp quân sự bên ngoài.
    status: pending
    canon: false
  - id: T06
    source_term: Concorde
    proposed_vi: Concorde
    alternatives_vi: [giữ Concorde và hoãn nhận diện đối tượng]
    segment_ids: [p000703]
    rationale: >-
      Package chỉ nhắc tên và thất bại trong mạch tự xét về khoản đã đầu tư;
      giữ tên bảo toàn ám chỉ mà không tự gán loại vật thể hoặc dự án.
      Không thêm máy bay, quốc gia, mốc lịch sử hay chú giải trong bản dịch.
    uncertainty: Chưa nhận diện Concorde; không cần dừng để giải quyết danh tính.
    status: pending
    canon: false
pending_terms:
  policy: temporary_consistent_not_canon
  assessed_ledger_section: chapter6_b22_translator_proposals
  choices: [T01, T02, T03, T04, T05, T06]
  additional_proposals:
    - source_term: field officers
      proposed_vi: các sĩ quan
      alternatives_vi: [sĩ quan cấp tá]
      segment_ids: [YS-LN02/Text/part0030.xhtml/p000689]
      rationale: Trung tính khi nghĩa nhóm quân hàm và nghĩa ngoài thực địa chưa phân định chắc chắn.
      status: pending
      canon: false
    - source_term: Great Army
      proposed_vi: đại quân
      alternatives_vi: [Đại quân]
      segment_ids: [YS-LN02/Text/part0030.xhtml/p000690]
      rationale: Giữ hình ảnh lực lượng lớn; viết hoa vẫn là lựa chọn biên tập chưa chốt.
      status: pending
      canon: false
risks:
  - >-
    Self-check không khớp bản dịch ở p000683 về nhấn mạnh và p000698 về việc dùng nó;
    p000698 thực tế chỉ dùng tên Tanya, không phải lỗi cần tự thêm đại từ.
  - >-
    Các quan hệ xưng hô tôi/ông/cô trong thoại là lựa chọn tạm dựa trên package;
    không suy ra thân thuộc hay tạo hồ sơ nhân vật canon.
  - >-
    Giới hạn package không cho phép xác minh lore, danh tính Concorde hoặc
    hệ tổ chức/quân hàm toàn bộ tác phẩm; các lựa chọn trên đều không canon.
  - >-
    Chưa sửa bản dịch và chưa chạy validator; lô chưa đủ điều kiện hoàn tất
    khi còn sáu finding mức vừa. Không có lỗi nghiêm trọng hoặc quyết định canon
    ảnh hưởng cốt truyện được xác lập trong phạm vi này.
validator: not_run
diff_check: not_run
commit: null
next_action: >-
  Coordinator ghi sáu lựa chọn tạm và hai đề xuất bổ sung vào ledger/handoff;
  giao người giữ lease sửa các finding, cập nhật self-check cho đúng bản thực tế,
  rồi chạy validator và diff-check, đối chiếu lại các finding trước khi đóng b22.
```
