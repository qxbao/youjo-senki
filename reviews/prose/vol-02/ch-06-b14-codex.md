# Review — vol-02-ch-06-b14

```yaml
role: reviewer
task_id: vol-02-ch-06-b14-review
state: done
review_path: reviews/prose/vol-02/ch-06-b14-codex.md
files_written: [reviews/prose/vol-02/ch-06-b14-codex.md]
validator: not_run
diff_check: not_run
commit: null
source_verification:
  path: work/vol-02/batches/ch-06-b14-source.jsonl
  sha256: fa68024cca38b1f862f4b696c787aa41f3e4fcac36e9564ca36701b26d654578
  result: pass
  canon_hashes_match_handoff: true
  stable_ids_and_order_match: true
counts:
  source_units: 33
  translation_units: 33
  reviewed: 33
  ledger_proposals_assessed: 8
  findings: 11
  serious: 0
  moderate: 5
  minor: 6
  counting_rule: Đếm theo finding; finding có thể liên quan nhiều mã đoạn.
segment_ids:
  - YS-LN02/Text/part0030.xhtml/p000418
  - YS-LN02/Text/part0030.xhtml/p000419
  - YS-LN02/Text/part0030.xhtml/p000420
  - YS-LN02/Text/part0030.xhtml/p000421
  - YS-LN02/Text/part0030.xhtml/p000422
  - YS-LN02/Text/part0030.xhtml/p000423
  - YS-LN02/Text/part0030.xhtml/p000424
  - YS-LN02/Text/part0030.xhtml/p000425
  - YS-LN02/Text/part0030.xhtml/p000426
  - YS-LN02/Text/part0030.xhtml/p000427
  - YS-LN02/Text/part0030.xhtml/p000428
  - YS-LN02/Text/part0030.xhtml/p000429
  - YS-LN02/Text/part0030.xhtml/p000430
  - YS-LN02/Text/part0030.xhtml/p000431
  - YS-LN02/Text/part0030.xhtml/p000432
  - YS-LN02/Text/part0030.xhtml/p000433
  - YS-LN02/Text/part0030.xhtml/p000434
  - YS-LN02/Text/part0030.xhtml/p000435
  - YS-LN02/Text/part0030.xhtml/p000436
  - YS-LN02/Text/part0030.xhtml/p000437
  - YS-LN02/Text/part0030.xhtml/p000438
  - YS-LN02/Text/part0030.xhtml/p000439
  - YS-LN02/Text/part0030.xhtml/p000440
  - YS-LN02/Text/part0030.xhtml/p000441
  - YS-LN02/Text/part0030.xhtml/p000442
  - YS-LN02/Text/part0030.xhtml/p000443
  - YS-LN02/Text/part0030.xhtml/p000444
  - YS-LN02/Text/part0030.xhtml/p000445
  - YS-LN02/Text/part0030.xhtml/p000446
  - YS-LN02/Text/part0030.xhtml/p000447
  - YS-LN02/Text/part0030.xhtml/p000448
  - YS-LN02/Text/part0030.xhtml/p000449
  - YS-LN02/Text/part0030.xhtml/p000450
coverage:
  dimensions: [meaning, prose, viewpoint, pronouns, emphasis, terminology, ranks]
  assessment: Đã đối chiếu từng mã trong danh sách trên ở mọi chiều; mã không nằm trong findings không có lỗi cần sửa được xác lập từ phạm vi b14.
  emphasis_preserved: [p000426, p000427, p000441]
  emphasis_missing: [p000420, p000421, p000434, p000448, p000450]
  self_check_corrections:
    - Danh sách nhấn mạnh trong self-check thiếu năm đoạn; kết luận bảo toàn nhấn mạnh chưa đúng.
    - p000421 đang dùng đổ bộ đường không, p000423 không dùng chiếm đóng; mô tả lựa chọn b13 trong self-check không phản ánh văn bản b14. Chỉ đánh giá bản hiện tại, không truy cập b13.
    - p000430 không có từ mage; các mã trong ledger là ngữ cảnh tham chiếu, không phải mọi mã đều có thuật ngữ nguyên văn.
    - p000430 không nói về đại từ của Vianto; p000448 chỉ gọi Vianto bằng tên trong bản dịch hiện tại.
findings:
  - id: B14-F01
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000420, YS-LN02/Text/part0030.xhtml/p000421, YS-LN02/Text/part0030.xhtml/p000434, YS-LN02/Text/part0030.xhtml/p000448, YS-LN02/Text/part0030.xhtml/p000450]
    issue: Mất nhấn mạnh của nguồn và dấu chuyển sang nội tâm.
    evidence: XHTML trong gói b14 có thẻ em ở cả năm đoạn; bản dịch không có dấu Markdown tương ứng.
    resolution: Bao *...* quanh câu cuối p000420, toàn bộ p000421, câu bắt đầu Giá mà ở p000434, câu bắt đầu Thế này thì ở p000448, và câu đầu p000450. Giữ các câu trần thuật ngoài phạm vi này ở dạng thường.
  - id: B14-F02
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000429]
    issue: Tính trước bước tiếp theo biến sự tính toán thành quả khi chưa đạt được thành lập kế hoạch bình thường; mất sắc thái mỉa mai.
    evidence: Thành ngữ ví việc tính trước kết quả chưa chắc xảy ra; đoạn nhấn nghịch lý rằng cách tính ấy lại có tác dụng trong lý lẽ quốc gia.
    resolution: Đổi vế đầu thành Nhưng xem ra, khi nói đến raison d’état, tính chuyện hưởng thành quả từ khi chưa đạt được lại có tác dụng. Dùng rời khỏi các tuyến chính ở vế sau; không tự gắn loại tuyến cụ thể.
  - id: B14-F03
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000432]
    issue: Dùng một Named để đánh lạc hướng đơn vị tạo thêm tác nhân đối địch; phần người có thể nhắm vào điểm yếu bị treo và đảo quy chiếu họ.
    evidence: p000430–p000431 mô tả chính đơn vị Đế quốc có Named chỉ huy bị kéo khỏi tiền tuyến. Cấu trúc p000432 có thể đọc là đơn vị có Named, không đủ căn cứ để đưa thêm một Named làm công cụ của phe Cộng hòa.
    resolution: Tạm dùng Việc kéo đơn vị này cùng một Named lão luyện có khả năng đánh vào điểm yếu của phía Cộng hòa ra khỏi tiền tuyến đã tạo ra tác động quan trọng trên chiến trường, không thể đo đếm bằng con số. Đây là cách đọc có căn cứ ngữ cảnh tốt nhất, vẫn pending; không xác lập lore hay danh tính khác.
    confidence: 0.86
    alternative: Nếu cần giảm xác định chủ thể bị đánh vào điểm yếu, dùng có khả năng đánh vào những điểm yếu của đối phương trong cùng cấu trúc đơn vị này cùng một Named.
  - id: B14-F04
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000434, YS-LN02/Text/part0030.xhtml/p000450]
    issue: Bộ binh thu hẹp lực lượng mặt đất thành một binh chủng.
    evidence: Nguồn chỉ phân biệt quân mặt đất với pháp sư, không xác định mọi quân tăng viện là bộ binh.
    resolution: Dùng vài sư đoàn quân mặt đất ở p000434 và lực lượng mặt đất đông hơn nhiều so với dự kiến ở p000450; giữ cả số lượng tăng mạnh và thời điểm đến sớm hơn nhiều.
  - id: B14-F05
    severity: moderate
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000430]
    issue: Cơ động ở cường độ cao tự thêm cường độ giao chiến.
    evidence: Từ high bổ nghĩa khả năng/mức cơ động; b14 không đưa thông tin về cường độ tác chiến.
    resolution: Tạm dùng tác chiến có tính cơ động cao, giữ riêng khả năng bắn tầm xa.
  - id: B14-F06
    severity: minor
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000445]
    issue: Bắn trả thêm quan hệ đáp trả hỏa lực trước đó.
    evidence: p000444 chỉ xác định phía ẩn trong các tòa nhà bắt đầu bắn quấy nhiễu; p000445 nói không thể bỏ việc ấy.
    resolution: Đổi bỏ qua việc bắn trả thành bỏ việc bắn quấy nhiễu; không gán ai đã nổ súng trước ngoài thông tin nguồn.
  - id: B14-F07
    severity: minor
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000425]
    issue: Tiếng nói của một cường quốc bỏ quan hệ sở hữu của Cộng hòa và kết hợp đặt tiếng nói vào vòng nguy hiểm nặng cấu trúc dịch.
    evidence: Đối tượng bị đe dọa là tiếng nói của chính Cộng hòa trong tư cách cường quốc.
    resolution: Dùng Nhận thấy nguy cơ mất tiếng nói của mình với tư cách cường quốc nghiêm trọng đến mức nào, Cộng hòa cảm thấy cần tự giải quyết tình hình hết mức có thể. Không đổi thành mất địa vị cường quốc, vốn mạnh hơn nguồn.
  - id: B14-F08
    severity: minor
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000430]
    issue: Toán quân đáng ghét chuyển bất tiện tác chiến sang cảm xúc ghét bỏ.
    evidence: Điểm nhìn phe Cộng hòa đánh giá đối thủ cơ động khó đối phó, không thêm phán xét đạo đức.
    resolution: Dùng một toán quân phiền toái hoặc một lực lượng khó chịu; ưu tiên phiền toái trong câu hiện tại.
  - id: B14-F09
    severity: minor
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000435]
    issue: Tuyến tiếp tế cạn kiệt gắn trạng thái của hàng tiếp tế vào tuyến đường, khiến câu khó hiểu.
    evidence: Giữ đầu mối vận tải sẽ khiến tuyến không còn cung cấp được tiếp tế trong chưa đầy một tuần; điều kiện chưa được khẳng định đã xảy ra.
    resolution: Dùng nếu giữ được đầu mối giao thông này, các tuyến tiếp tế của Đế quốc sẽ không còn đưa được hàng tiếp tế tới trong chưa đầy một tuần. Giữ điều kiện và kết quả chắc chắn ở câu kế tiếp.
  - id: B14-F10
    severity: minor
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000441]
    issue: Kiệt sức tăng mức độ suy kiệt so với mục tiêu gây mệt do né tránh.
    evidence: Chuỗi mục tiêu là buộc né, gây mệt và phá đội hình để trì hoãn; không nói đã hoặc phải kiệt sức hoàn toàn.
    resolution: Dùng làm chúng mệt mỏi; giữ toàn đoạn trong dấu nhấn mạnh.
  - id: B14-F11
    severity: minor
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000436]
    issue: Các anh tự xác định giới tính người ở đầu dây Combat Control.
    evidence: Nguồn chỉ có ngôi thứ hai; nhân viên điều phối không được xác định giới tính trong b14.
    resolution: Dùng Ý là chúng tôi phải giao chiến với tiểu đoàn đó từ xa sao? Giữ chúng tôi theo phía phát thoại, lược ngôi thứ hai để tránh suy diễn.
unresolved_findings: [B14-F01, B14-F02, B14-F03, B14-F04, B14-F05, B14-F06, B14-F07, B14-F08, B14-F09, B14-F10, B14-F11]
term_recommendations:
  - proposal: 1
    source_term: Named
    status: pending
    proposed_vi: Giữ Named; dùng một Named hoặc Named ấy theo cú pháp.
    alternative: người được gọi là Named
    rationale: Viết hoa cho thấy định danh đặc biệt nhưng chưa giải thích bản chất. Mang danh hiệu tự gắn cơ chế danh hiệu chưa được nguồn xác nhận; bỏ phần diễn giải này ở p000429–p000430.
    confidence: 0.91
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000419, YS-LN02/Text/part0030.xhtml/p000429, YS-LN02/Text/part0030.xhtml/p000430, YS-LN02/Text/part0030.xhtml/p000431, YS-LN02/Text/part0030.xhtml/p000432, YS-LN02/Text/part0030.xhtml/p000445]
    note: p000431 là ngữ cảnh đơn vị, không có từ Named trực tiếp.
  - proposal: 2
    source_term: raison d’état
    status: pending
    proposed_vi: raison d’état
    alternative: lý lẽ lợi ích quốc gia
    rationale: Giữ dạng đang dùng theo ledger; trong đoạn đây là lý lẽ biện minh hành động vì quốc gia, không chỉ mục tiêu quyền lợi chung. Không tự thêm chú giải vào bản dịch.
    confidence: 0.85
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000427, YS-LN02/Text/part0030.xhtml/p000429]
  - proposal: 3
    source_term: Commonwealth
    status: pending
    proposed_vi: Khối Thịnh vượng chung
    alternative: Commonwealth
    rationale: Giữ lựa chọn dự án đang đề xuất để nhất quán; b14 không chứng minh đây là một khối nhiều nước hay một quốc gia. Không suy ra chính thể từ cách gọi tạm.
    confidence: 0.65
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000424, YS-LN02/Text/part0030.xhtml/p000426]
  - proposal: 4
    source_term: mage / mage battalion
    status: pending
    proposed_vi: pháp sư / tiểu đoàn pháp sư
    alternative: pháp sư chiến đấu / tiểu đoàn pháp sư chiến đấu
    rationale: Dạng rộng đủ cho ngữ cảnh quân sự; chưa cần gắn Không quân hoặc quân chủng riêng. Mage Second Company tạm là Đại đội Pháp sư số Hai.
    confidence: 0.94
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000420, YS-LN02/Text/part0030.xhtml/p000422, YS-LN02/Text/part0030.xhtml/p000430, YS-LN02/Text/part0030.xhtml/p000431, YS-LN02/Text/part0030.xhtml/p000436, YS-LN02/Text/part0030.xhtml/p000444, YS-LN02/Text/part0030.xhtml/p000447, YS-LN02/Text/part0030.xhtml/p000450]
    note: p000430 và p000436 là ngữ cảnh quy chiếu đơn vị, không có từ mage trực tiếp.
  - proposal: 5
    source_term: high-maneuver warfare
    status: pending
    proposed_vi: tác chiến có tính cơ động cao
    alternative: tác chiến cơ động cao
    rationale: Giữ mức cơ động, không thêm cường độ giao chiến hoặc tên học thuyết. Thay đề xuất hiện tại theo B14-F05.
    confidence: 0.93
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000430]
  - proposal: 6
    source_term: transport terminal
    status: pending
    proposed_vi: đầu mối giao thông
    alternative: đầu mối vận tải
    rationale: Đủ rộng khi nguồn chưa xác định loại cơ sở; tránh nhà ga trung chuyển vì tự thêm loại hình và chức năng trung chuyển. Có thể giữ bản hiện tại.
    confidence: 0.80
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000435]
  - proposal: 7
    source_term: Major / Lieutenant Colonel
    status: pending
    proposed_vi: Thiếu tá von Degurechaff / Trung tá Vianto
    alternative: Giữ Major / Lieutenant Colonel nếu sau này dự án quyết định bảo toàn tên quân hàm gốc.
    rationale: Hai danh xưng nguồn rõ ràng và cách quy đổi hiện tại không mâu thuẫn nhau; không có căn cứ đổi sang quân hàm khác. Đây là đề xuất cục bộ, không lập bảng quân hàm canon.
    confidence: 0.97
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000418, YS-LN02/Text/part0030.xhtml/p000422]
  - proposal: 8
    source_term: pronouns/forms of address for Vianto
    status: pending
    proposed_vi: Giữ anh cho Vianto trong trần thuật p000422 và p000450; lặp Vianto khi cần rõ quy chiếu. Thoại dùng tôi/chúng tôi; nội tâm tập thể dùng chúng ta.
    alternative: Lặp Vianto hoặc lược chủ ngữ ở chỗ trần thuật có thể gây mơ hồ.
    rationale: Nguồn xác định giới tính Vianto nhưng không xác định tuổi hay quan hệ thân sơ; anh là lựa chọn hiện hành chấp nhận được, không tự đổi sang ông. p000430 là Named nữ, không phải Vianto; p000433 chỉ cần tôi. Lược người nhận ở p000436 theo B14-F11.
    confidence: 0.84
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000422, YS-LN02/Text/part0030.xhtml/p000430, YS-LN02/Text/part0030.xhtml/p000433, YS-LN02/Text/part0030.xhtml/p000436, YS-LN02/Text/part0030.xhtml/p000448, YS-LN02/Text/part0030.xhtml/p000450]
additional_recommendations:
  - source_term: she at p000430
    status: pending
    proposed_vi: Named ấy cùng đơn vị tinh nhuệ dưới quyền đều giỏi…
    alternative: Named ấy cùng đơn vị tinh nhuệ do cô chỉ huy đều giỏi…
    rationale: she có căn cứ giới tính trực tiếp, nên cô không phải lỗi suy ra giới tính. Tuy nhiên danh tính Tanya không được xác nhận bằng tên trong phạm vi này; cách dưới quyền tránh cả suy diễn danh tính và xung đột quy ước nó nếu coordinator xác nhận sau đó. Không mở rộng DEC-P01-001 sang một Named chưa định danh.
    confidence: 0.92
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000430]
  - source_term: ground forces / ground troops
    status: pending
    proposed_vi: quân mặt đất / lực lượng mặt đất
    alternative: lực lượng tác chiến trên bộ
    rationale: Giữ phạm vi rộng hơn bộ binh, xem B14-F04.
    confidence: 0.97
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000434, YS-LN02/Text/part0030.xhtml/p000450]
  - source_term: main lines
    status: pending
    proposed_vi: các tuyến chính
    alternative: các tuyến tiền phương chính
    rationale: p000431 xác nhận hướng tiền tuyến, nhưng chưa đủ căn cứ tự xác định tuyến chủ lực hay tuyến phòng thủ. Dụ được giữ ý kéo lực lượng ra khỏi vị trí; không cần đổi thành rút quân tự nguyện.
    confidence: 0.84
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000429, YS-LN02/Text/part0030.xhtml/p000431]
  - source_term: sniping / breaking
    status: pending
    proposed_vi: bắn tỉa / tản ra
    alternative: hỏa lực bắn tỉa / tách đội hình
    rationale: p000441 và p000448 hỗ trợ việc đội hình tản để né hỏa lực, không phải tan vỡ tinh thần hay tháo chạy. Không suy ra vũ khí hoặc phương thức ngắm bắn. Đòn bắn tỉa hiện tại chấp nhận được.
    confidence: 0.90
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000447]
  - source_term: disciplined fire
    status: pending
    proposed_vi: bắn có kỷ luật
    alternative: hỏa lực được kiểm soát chặt chẽ
    rationale: Giữ phẩm chất kiểm soát hỏa lực; không tự đổi sang bắn loạt đồng bộ hoặc khẳng định độ chính xác tuyệt đối.
    confidence: 0.85
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000446]
  - source_term: Bravo Leader / Charlie Leader / Combat Control
    status: pending
    proposed_vi: Đội trưởng Bravo / Đội trưởng Charlie / Trung tâm Điều phối Tác chiến
    alternative: Chỉ huy Bravo / Chỉ huy Charlie / Điều phối Tác chiến
    rationale: Có thể giữ nhãn liên lạc hiện tại nhất quán; đây là vai trò và đầu mối liên lạc, không xác lập cấp đơn vị hay quân hàm. Phương án thay thế giảm giả định về cơ cấu tổ chức khi cần.
    confidence: 0.72
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000419, YS-LN02/Text/part0030.xhtml/p000436]
  - source_term: line of distracting fire
    status: pending
    proposed_vi: một loạt đạn bắn quấy nhiễu
    alternative: một tuyến hỏa lực quấy nhiễu
    rationale: B14 không xác định bố trí không gian của hỏa lực. Giữ dạng hiện hành theo mục tiêu gây né tránh, không tự thêm màn hỏa lực hoặc công sự; chỉ sửa mức độ gây mệt theo B14-F10.
    confidence: 0.64
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000441]
wording_concerns:
  p000442:
    assessment: Giữ nguyên hai lớp ngoặc kép và Rõ.
    rationale: Cả text và XHTML đều có cấu trúc này; chưa có quyết định canon cho phép chuẩn hóa dấu thoại. Không thêm đồng thanh hoặc số lượng người đáp vì nguồn không xác nhận trực tiếp.
    alternative: Một lớp ngoặc kép chỉ khi dự án sau này có quyết định định dạng rõ ràng.
    confidence: 0.99
  p000430: Đại từ cô có căn cứ giới tính; khuyến nghị dưới quyền là phương án trung tính để tránh gán danh tính. Cần sửa cơ động ở cường độ cao và đáng ghét theo findings.
  p000425: Giữ tiếng nói theo nghĩa ảnh hưởng của chính Cộng hòa với tư cách cường quốc; sửa kết hợp từ và sở hữu theo B14-F07.
  p000429: Vấn đề chính là thành ngữ, không phải động từ dụ. Giữ các tuyến chính trung tính và bỏ diễn giải mang danh hiệu.
risks:
  - Chưa sửa bản dịch; năm findings mức vừa vẫn mở, batch chưa đủ điều kiện nghiệm thu.
  - p000432 có cấu trúc Anh ngữ dễ đọc theo hai cách; lựa chọn tạm dựa vào mạch p000430–p000431, không xác lập thêm một Named thuộc phe Cộng hòa.
  - Named, tên chính thể, quân hàm, cách gọi đơn vị và đại từ đều giữ pending; không có đề xuất nâng canon hoặc quyết định lore ảnh hưởng cốt truyện.
  - Chỉ b14 đủ căn cứ cho đánh giá này; không khẳng định danh tính Named nữ, người nói không ghi tên hoặc cơ cấu Combat Control.
next_action: Coordinator chuyển findings và lựa chọn tạm vào bàn giao/ledger theo quyền hạn; giao translator sửa b14, cập nhật self-check rồi chạy validator/diff-check và kiểm tra lại các findings mở trước khi nghiệm thu.
```
