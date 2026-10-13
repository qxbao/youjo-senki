# Review — vol-02-ch-05-b20-review

Đã đọc shared/reviewer, config, hai handoff đã sửa, package cục bộ, năm tệp canon, các mục ledger liên quan, bản dịch và self-check. Đã review đủ 39 đoạn về nghĩa, văn phong, điểm nhìn, thuật ngữ, tính nhất quán và nhấn mạnh. Không mở EPUB/PDF. Không chép câu nguồn; chỉ dùng thuật ngữ ngắn để nhận diện.

Package khớp cả hai handoff. Mọi đề xuất dưới đây còn pending, không phải canon. Review hoàn tất nhưng bản dịch cần sửa; không coi kết quả validator/diff của translator là kiểm tra do reviewer thực hiện.

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-05-b20-review
state: done
review_path: reviews/prose/vol-02/ch-05-b20-codex.md
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000496
  - YS-LN02/Text/part0026.xhtml/p000497
  - YS-LN02/Text/part0026.xhtml/p000498
  - YS-LN02/Text/part0026.xhtml/p000499
  - YS-LN02/Text/part0026.xhtml/p000500
  - YS-LN02/Text/part0026.xhtml/p000501
  - YS-LN02/Text/part0026.xhtml/p000502
  - YS-LN02/Text/part0026.xhtml/p000503
  - YS-LN02/Text/part0026.xhtml/p000504
  - YS-LN02/Text/part0026.xhtml/p000505
  - YS-LN02/Text/part0026.xhtml/p000506
  - YS-LN02/Text/part0026.xhtml/p000507
  - YS-LN02/Text/part0026.xhtml/p000508
  - YS-LN02/Text/part0026.xhtml/p000509
  - YS-LN02/Text/part0026.xhtml/p000510
  - YS-LN02/Text/part0026.xhtml/p000511
  - YS-LN02/Text/part0026.xhtml/p000512
  - YS-LN02/Text/part0026.xhtml/p000513
  - YS-LN02/Text/part0026.xhtml/p000514
  - YS-LN02/Text/part0026.xhtml/p000515
  - YS-LN02/Text/part0026.xhtml/p000516
  - YS-LN02/Text/part0026.xhtml/p000517
  - YS-LN02/Text/part0026.xhtml/p000518
  - YS-LN02/Text/part0026.xhtml/p000519
  - YS-LN02/Text/part0026.xhtml/p000520
  - YS-LN02/Text/part0026.xhtml/p000521
  - YS-LN02/Text/part0026.xhtml/p000522
  - YS-LN02/Text/part0026.xhtml/p000523
  - YS-LN02/Text/part0026.xhtml/p000524
  - YS-LN02/Text/part0026.xhtml/p000525
  - YS-LN02/Text/part0026.xhtml/p000526
  - YS-LN02/Text/part0026.xhtml/p000527
  - YS-LN02/Text/part0026.xhtml/p000528
  - YS-LN02/Text/part0026.xhtml/p000529
  - YS-LN02/Text/part0026.xhtml/p000530
  - YS-LN02/Text/part0026.xhtml/p000531
  - YS-LN02/Text/part0026.xhtml/p000532
  - YS-LN02/Text/part0026.xhtml/p000533
  - YS-LN02/Text/part0026.xhtml/p000534
files_written: [reviews/prose/vol-02/ch-05-b20-codex.md]
validator: not_run
diff_check: not_run
commit: null
hash_check:
  status: pass
  package_sha256_actual: 02bc6a96956258510c53df300780caad5fa8bdf46bd44a3ff258df8be4abc0fb
  batch_handoff_expected: 02bc6a96956258510c53df300780caad5fa8bdf46bd44a3ff258df8be4abc0fb
  review_handoff_expected: 02bc6a96956258510c53df300780caad5fa8bdf46bd44a3ff258df8be4abc0fb
  package_matches_batch_handoff: true
  package_matches_review_handoff: true
  original_source_file_hash_recomputed: false
order_check:
  status: pass
  source_units: 39
  translation_units: 39
  exact_expected_id_sequence: true
  source_translation_order_matches: true
  duplicates: 0
  missing_ids: 0
counts:
  reviewed_segments: 39
  serious: 0
  moderate: 3
  minor: 4
  total_findings: 7
  unresolved_findings: 7
findings:
  - id: B20-F01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000497
    issue: "Giả định quá khứ bị chuyển thành điều kiện hiện tại/tương lai."
    evidence: "Người kể hồi tưởng tình huống đã được mệnh lệnh và huấn luyện giải cứu ở p000499; bản dịch dùng Nếu cứ để mặc và sẽ xảy ra."
    resolution: "Dùng Nếu lúc ấy tôi bị bỏ mặc như thế, không biết chuyện gì đã có thể xảy ra với tôi. Giữ tính giả định, không xác nhận hậu quả đã xảy ra."
  - id: B20-F02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000508
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000508, YS-LN02/Text/part0026.xhtml/p000509, YS-LN02/Text/part0026.xhtml/p000510, YS-LN02/Text/part0026.xhtml/p000511, YS-LN02/Text/part0026.xhtml/p000529]
    issue: "Cô trong trần thuật Tanya lệch phương án tạm cùng chương."
    evidence: "Ledger chapter5_b12_reviewer_recommendations đề xuất nó hoặc lặp tên/lược chủ ngữ; bản dịch chuyển sang cô sau p000505 và ở phần kể sau nội tâm p000529. DEC-P01-001 giới hạn phạm vi, nên không tự mở rộng nó thành canon LN02."
    resolution: "Ưu tiên lặp Tanya khi cần xác định chủ thể rồi lược đại từ ở các câu liền nhau. Giữ mình trong nội tâm p000527–529, tôi trong thư và lời kể ngôi thứ nhất p000530–534 theo ledger riêng về lời kể Tanya; không áp mình cho người kể p000496–504."
  - id: B20-F03
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000534
    issue: "Đổi người cười và đối tượng bị cười nhạo."
    evidence: "Nguồn hướng tiếng cười của người khác vào sĩ quan mất quân vì khoai tây; bản dịch khiến chính sĩ quan cười cho qua. Điều này làm lệch sự tự giễu trước câu phủ nhận tính buồn cười."
    resolution: "Dùng Ý tôi là, một sĩ quan để mất binh sĩ vì khoai tây hỏng thì người ta chỉ có thể cười nhạo thôi. Giữ câu kết Không, chẳng buồn cười chút nào."
  - id: B20-F04
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000514
    issue: "Thêm cấp trên trực tiếp khi quan hệ trực tiếp chưa được nêu."
    evidence: "Nguồn chỉ xác lập cấp trên; chức danh chỉ huy ở chữ ký cũng không xác lập tầng quản lý trực tiếp."
    resolution: "Bỏ trực tiếp, dùng cấp trên của anh ấy."
  - id: B20-F05
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000516
    issue: "Chiến dịch định quy mô hoạt động cụ thể hơn căn cứ hiện có."
    evidence: "Thư nói hoạt động quân sự; p000530 cho biết có đột kích ban đêm và đổ bệnh khi trở về. Không có căn cứ coi đây là phẫu thuật, cũng chưa xác định quy mô chiến dịch."
    resolution: "Tạm dùng trong một nhiệm vụ tác chiến; phương án khác là trong một hoạt động quân sự. Giữ đột nhiên đổ bệnh và nhận định khó phục vụ dài hạn; không sửa thư thành tường thuật nguyên nhân khoai tây."
  - id: B20-F06
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000514
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000514, YS-LN02/Text/part0026.xhtml/p000526]
    issue: "Magic Major đổi từ phương án Thiếu tá Pháp sư của reviewer b12 sang Thiếu tá ma pháp mà chưa có lựa chọn thay thế được ghi."
    evidence: "Ledger b12 có phương án translator và reviewer cùng dùng Thiếu tá Pháp sư; mục b20 chỉ là đề xuất mới, chưa chứng minh đã thay phương án trước."
    resolution: "Đề xuất trở lại Thiếu tá Pháp sư ở cả hai đoạn để nhất quán trong chương; coordinator ghi lựa chọn tạm vào ledger/handoff. Thiếu tá ma pháp vẫn là phương án thay thế, không phải sai quân hàm."
  - id: B20-F07
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000530
    issue: "Màng bảo hộ khác màn bảo hộ đã được reviewer b15 đề xuất cho cùng thuật ngữ."
    evidence: "Ledger chapter5_b15_reviewer_recommendations chọn màn bảo hộ, phân biệt với lớp vỏ phòng ngự; b20 dùng màng bảo hộ."
    resolution: "Tạm dùng màn bảo hộ theo ledger hiện có; nếu coordinator chọn màng bảo hộ thì ghi rõ và đồng bộ các lần dùng trước. Không bổ sung cơ chế phòng vệ."
unresolved_findings: [B20-F01, B20-F02, B20-F03, B20-F04, B20-F05, B20-F06, B20-F07]
term_recommendations:
  - source_term: computation orb
    proposed_vi: quả cầu tính toán
    alternatives_vi: [cầu tính toán]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000500]
    status: pending
    rationale: "Giữ lựa chọn lặp lại trong ledger; quả cầu rõ hình dạng, dạng rút gọn kém tự nhiên hơn. Không thêm tên mẫu hay chức năng ngoài đoạn."
  - source_term: Magic Major
    proposed_vi: Thiếu tá Pháp sư
    alternatives_vi: [Thiếu tá ma pháp, Thiếu tá ma thuật]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000514, YS-LN02/Text/part0026.xhtml/p000526]
    status: pending
    rationale: "Ưu tiên lựa chọn reviewer b12 để nhất quán; giữ bậc Thiếu tá, không xác lập hệ quân hàm canon."
  - source_term: Warrant Officer
    proposed_vi: Chuẩn úy
    alternatives_vi: [Sĩ quan chuẩn úy, Warrant Officer]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000513]
    status: pending
    confidence: medium
    rationale: "Chấp nhận ánh xạ tạm b20; phương án có Sĩ quan dài hơn, giữ nguyên tiếng Anh ít diễn giải hơn nhưng khó đọc. Không suy ra đây là cấp tương đương chính xác trong quân đội thực."
  - source_term: Field Service Badge First Class
    proposed_vi: Huy hiệu Phục vụ Chiến trường Hạng Nhất
    alternatives_vi: [Huy hiệu Dã chiến Hạng Nhất]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000523]
    status: pending
    rationale: "Giữ tên hiện tại vì bảo toàn ý phục vụ và hạng; Dã chiến gọn nhưng lược ý phục vụ. Không đổi huy hiệu thành huân chương hoặc khẳng định đã trao: nguồn chỉ nói đề cử được chấp thuận."
  - source_term: Disability Medal
    proposed_vi: Huân chương Thương tật
    alternatives_vi: [Huy chương Thương tật, Huân chương Tàn tật]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000523]
    status: pending
    confidence: medium
    rationale: "Giữ lựa chọn ledger, không suy thành bị thương do chiến đấu; huy chương sát loại medal hơn và có thể được chọn nếu thống nhất hệ khen thưởng. Tàn tật nặng sắc thái hơn, không ưu tiên. Tên loại phần thưởng chưa canon."
  - source_term: NBC weapon
    proposed_vi: vũ khí NBC
    alternatives_vi: [vũ khí hạt nhân, sinh học, hóa học]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000530]
    status: pending
    rationale: "Giữ chữ viết tắt đúng package và ledger, không khai triển vào bản dịch khi nguồn không khai triển. Giữ đây là suy đoán của người kể đã được chẩn đoán ngộ độc ở p000531 bác bỏ; không xác nhận có vũ khí mới."
  - source_term: surgeon
    proposed_vi: bác sĩ quân y
    alternatives_vi: [bác sĩ phẫu thuật, quân y sĩ]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000516, YS-LN02/Text/part0026.xhtml/p000531]
    status: pending
    confidence: medium
    rationale: "Đề xuất cách gọi theo vai trò khám và đánh giá khả năng phục vụ trong bối cảnh quân đội; không có cảnh phẫu thuật. Bác sĩ phẫu thuật là cách literal hiện tại và chưa đủ căn cứ để kết luận sai chuyên khoa. Quân y sĩ có thể gợi trình độ khác, không ưu tiên."
  - source_term: Personnel Division / Personnel
    proposed_vi: Cục Nhân sự
    alternatives_vi: [bộ phận Nhân sự, Phòng Nhân sự]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000518, YS-LN02/Text/part0026.xhtml/p000533]
    status: pending
    confidence: medium
    rationale: "Giữ cách gọi tạm hiện tại ở hai đoạn; chưa xác lập cấp tổ chức Cục. Bộ phận Nhân sự trung tính hơn nếu coordinator đồng bộ các lần dùng; không đổi riêng một đoạn."
  - source_term: protective films
    proposed_vi: màn bảo hộ
    alternatives_vi: [màng bảo hộ, lớp bảo vệ]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000530]
    status: pending
    rationale: "Theo lựa chọn reviewer b15; không đồng nhất với lớp vỏ phòng ngự hoặc tự xác lập cơ chế."
  - source_term: medical formula
    proposed_vi: thuật thức trị liệu
    alternatives_vi: [thuật thức y thuật, công thức trị liệu]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000530]
    status: pending
    rationale: "Chấp nhận cách gọi hiện tại theo công dụng trong đoạn; giữ tác dụng chỉ làm dịu đau, không biến thành chữa khỏi."
focus_assessments:
  p000516: "Ngữ cảnh quân sự có căn cứ trong batch; không hiểu operation là ca mổ. Cần thu hẹp mức suy diễn về quy mô theo B20-F05. Chuyên khoa surgeon còn bất định, xử lý bằng đề xuất tạm riêng."
  p000526: "Giữ [xxx] đúng package, đúng vị trí đầu chữ ký và trong phạm vi chữ nghiêng. Đây là placeholder nguồn, không phải lỗi bỏ sót translator. Không đoán số đơn vị hoặc thay bằng tên đơn vị từ lore."
  emphasis: "Đã đối chiếu XHTML từng đoạn: 16 span chữ nghiêng, ở p000513–526 và phần nội tâm p000528–529; bản dịch giữ tương ứng. p000527 và p000530–534 không có nhấn mạnh nguồn, không tự thêm chữ nghiêng."
  self_check: "Hai điểm self-check nêu đã được xử lý trực tiếp; p000526 được chấp nhận, p000516 có đề xuất chỉnh. Self-check chưa phát hiện các lỗi nghĩa p000497/p000534 và các điểm nhất quán nêu trên."
coverage:
  p000496: "Cảm giác va đập và đối chiếu độ giật được giữ."
  p000497: B20-F01
  p000498: "Lệnh, vai trò, mốc 30 giây và đồng bộ đồng hồ được giữ."
  p000499: "Huấn luyện và mệnh lệnh giúp trở lại thực tại; giữ quan hệ nhân quả."
  p000500: "Đúng thời điểm, công suất và cất cánh; thuật ngữ pending."
  p000501: "Giữ đường về, thời lượng, sợ hãi và đau khi thở."
  p000502: "Giữ cảm giác xa lạ với bản thân vì sợ."
  p000503: "Giữ tránh bị bắn nhầm, hướng về hậu phương rồi kiệt sức."
  p000504: "Giữ câu hỏi kinh ngạc, không tự thêm dấu nghiêng."
  p000505: "Giữ chuyển cảnh, lịch buổi sáng và vẻ quyết tâm."
  p000506: "Giữ khả năng thư thông qua căn cứ hậu phương."
  p000507: "Giữ khả năng chậm trễ nhưng nhìn chung gửi nhận bình thường."
  p000508: B20-F02
  p000509: B20-F02
  p000510: B20-F02
  p000511: B20-F02
  p000512: "Giữ nhận xét việc viết thư khó khăn là bình thường."
  p000513: "Giữ người nhận, tên và nhấn mạnh; quân hàm pending."
  p000514: "B20-F04 và B20-F06; tôi là tự xưng trong thư, được chấp nhận."
  p000515: "Giữ thông báo giải ngũ vì tình trạng thương tật, không dịch thành báo tử; có thể trau chuốt cậu con trai duy nhất thân yêu thành người con trai trẻ tuổi duy nhất để giữ nét tuổi trẻ."
  p000516: B20-F05
  p000517: "Giữ xác suất, thời gian dưỡng bệnh dài và hai nơi hồi phục."
  p000518: "Giữ chấp thuận kế hoạch; tên cơ quan pending."
  p000519: "Giữ cả yêu cầu trò chuyện và bảo đảm dưỡng bệnh yên tĩnh."
  p000520: "Giữ lời xin tha thứ, không suy thành tử vong."
  p000521: "Giữ tài năng, tình đồng đội, dũng cảm và sự tin cậy."
  p000522: "Giữ mất người khỏi hàng ngũ, được hiểu qua giải ngũ."
  p000523: "Giữ hai phần thưởng, hạng và việc đề cử được chấp thuận; tên pending."
  p000524: "Giữ mong hồi phục hoàn toàn."
  p000525: "Lời kết thư và chữ nghiêng phù hợp."
  p000526: "Placeholder đạt; B20-F06 về nhất quán quân hàm."
  p000527: "Giữ khoai tây hỏng và tham chiếu phi công như nội dung nhân vật, không xác minh hay thêm lore; mình phù hợp tự quy chiếu."
  p000528: "Giữ nhấn mạnh riêng phần suy nghĩ và bực bội về hậu cần."
  p000529: "Giữ trách nhiệm gửi thư và tâm trạng khó nguôi; B20-F02 về phần kể."
  p000530: "Giữ trình tự ăn/đột kích/trở về, suy đoán NBC, giảm đau và nỗi lo vũ khí mới; B20-F07 về thuật ngữ."
  p000531: "Giữ chẩn đoán ngộ độc cấp tính, chỉ một người mắc; surgeon pending."
  p000532: "Giữ tức giận, đánh giá năng lực và bất ngờ phải đưa quân rời tiền tuyến."
  p000533: "Giữ phân loại tình trạng, lương hưu, danh dự và hồ sơ sĩ quan; không xác nhận mất danh dự thật."
  p000534: B20-F03
risks:
  - "Ba lỗi vừa còn mở; cần người giữ quyền sửa xử lý rồi kiểm tra lại."
  - "Quân hàm, cơ quan, phần thưởng và tên ma pháp là đề xuất tạm; coordinator ghi lựa chọn nhất quán, không tự nâng canon."
  - "Placeholder có thật trong package, giữ nguyên để tiếp tục; không cần chờ người dùng để đoán nội dung."
next_action: "Coordinator ghi lựa chọn tạm vào ledger/handoff; giao người giữ quyền sửa xử lý findings, chạy validator/diff-check và review lại các chỗ sửa. Reviewer không commit."
```
