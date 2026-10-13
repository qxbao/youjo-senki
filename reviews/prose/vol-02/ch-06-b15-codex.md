# Review — vol-02-ch-06-b15

```yaml
role: reviewer
task_id: vol-02-ch-06-b15-review
state: done
review_path: reviews/prose/vol-02/ch-06-b15-codex.md
files_written: [reviews/prose/vol-02/ch-06-b15-codex.md]
configured_runtime:
  launcher_alias: codex-personal
  via: ai-isolator
  model: gpt-6.1-sol
  effort: medium
  note: Cấu hình đọc từ config; không khởi chạy thêm worker hoặc tự xác nhận thông tin launcher của phiên hiện tại.
source_verification:
  path: work/vol-02/batches/ch-06-b15-source.jsonl
  expected_sha256: 6aa446a5ca911955f226bd56f344b3066c3adfd28b77dd2b07ffd4a1bcb87cdd
  actual_sha256: 6aa446a5ca911955f226bd56f344b3066c3adfd28b77dd2b07ffd4a1bcb87cdd
  result: pass
  units: 28
  ids_order_and_alignment: pass
scope:
  source: Chỉ gói b15 được giao; không mở EPUB/PDF hoặc nguồn lô khác.
  canon: [canon/glossary.yml, canon/style-guide.md, canon/characters.yml, canon/decisions.md, canon/glossary-pending.yml]
  pending_basis: Các lựa chọn b15 và lựa chọn kế thừa b14 liên quan; không lấy lore làm căn cứ.
  proposal_count_note: Sáu mục của ledger b15 gồm hai mục tái dùng và bốn mục còn lại; self-check có thêm đề xuất về tuyến, đơn vị, tăng cường, mana và hỏa lực. Đã xét cả hai nhóm.
counts:
  reviewed: 28
  serious: 0
  moderate: 4
  minor: 5
  total: 9
  unresolved: 9
  ledger_proposals_assessed: 6
  term_recommendations: 15
  emphasis_mismatches: 0
validator: not_run
diff_check: not_run
commit: null
segment_ids:
  - YS-LN02/Text/part0030.xhtml/p000451
  - YS-LN02/Text/part0030.xhtml/p000452
  - YS-LN02/Text/part0030.xhtml/p000453
  - YS-LN02/Text/part0030.xhtml/p000454
  - YS-LN02/Text/part0030.xhtml/p000455
  - YS-LN02/Text/part0030.xhtml/p000456
  - YS-LN02/Text/part0030.xhtml/p000457
  - YS-LN02/Text/part0030.xhtml/p000458
  - YS-LN02/Text/part0030.xhtml/p000459
  - YS-LN02/Text/part0030.xhtml/p000460
  - YS-LN02/Text/part0030.xhtml/p000461
  - YS-LN02/Text/part0030.xhtml/p000462
  - YS-LN02/Text/part0030.xhtml/p000463
  - YS-LN02/Text/part0030.xhtml/p000464
  - YS-LN02/Text/part0030.xhtml/p000465
  - YS-LN02/Text/part0030.xhtml/p000466
  - YS-LN02/Text/part0030.xhtml/p000467
  - YS-LN02/Text/part0030.xhtml/p000468
  - YS-LN02/Text/part0030.xhtml/p000469
  - YS-LN02/Text/part0030.xhtml/p000470
  - YS-LN02/Text/part0030.xhtml/p000471
  - YS-LN02/Text/part0030.xhtml/p000472
  - YS-LN02/Text/part0030.xhtml/p000473
  - YS-LN02/Text/part0030.xhtml/p000474
  - YS-LN02/Text/part0030.xhtml/p000475
  - YS-LN02/Text/part0030.xhtml/p000476
  - YS-LN02/Text/part0030.xhtml/p000477
  - YS-LN02/Text/part0030.xhtml/p000478
findings:
  - id: B15-F01
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000451
    issue: Thêm chức năng phòng thủ cho các tuyến mà nguồn chưa xác định.
    evidence: Từ lines không tự xác lập tuyến phòng thủ; lựa chọn kế thừa về các tuyến ở b14 cũng tránh bổ nghĩa này. Tính giả định và mức bất lợi còn giữ đúng.
    resolution: Đổi cụm thành “rút khỏi các tuyến”; có thể dùng “rút khỏi chiến tuyến” nếu cần tự nhiên hơn. Không suy diễn mục đích điều quân.
    confidence: 0.93
  - id: B15-F02
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000453
    issue: “của hắn” lệch đại từ Vianto và dễ làm phụ tá bị hiểu là thuộc Ác quỷ sông Rhine.
    evidence: Đoạn đặt chủ thể phía Vianto và phụ tá; đại từ sở hữu ngay sau danh hiệu đối phương làm tham chiếu mơ hồ. Hắn còn thêm sắc thái xa cách/miệt thị không có căn cứ, trong khi ledger đề xuất anh cho Vianto.
    resolution: Dùng “nhưng sĩ quan phụ tá của Vianto không nói điều vô lý”; sau khi chủ thể rõ có thể dùng “phụ tá của anh”.
    confidence: 0.93
  - id: B15-F03
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000456
    issue: “được tăng viện” gợi sự kiện bổ sung quân cụ thể; “quyết tâm đến cùng” tăng mức tuyệt đối.
    evidence: Nguồn chỉ xác định tiểu đoàn được tăng cường sức mạnh và quyết tâm của đối phương, không nói cách tăng cường hoặc cam kết đến cùng.
    resolution: Dùng “cả một tiểu đoàn tăng cường” và “thì rõ ràng kẻ địch rất quyết tâm”. Giữ điều kiện đối đầu đột ngột và quy mô đại đội/tiểu đoàn.
    confidence: 0.91
  - id: B15-F04
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000458
    issue: “sẽ có thể” làm kỳ vọng khả năng đột phá chắc chắn hơn sắc thái dự tính trong nguồn.
    evidence: Nhận định quân có khả năng chọc thủng còn mang mức trông đợi; lời đáp p000459 bác bỏ tính lạc quan ấy. Đây không phải kết quả bảo đảm sau khi cắt tiếp tế.
    resolution: Dùng “quân ta hẳn sẽ có thể chọc thủng các vị trí phòng thủ của chúng khi nguồn tiếp tế bị cắt, anh nghĩ sao?”. Giữ chuỗi phản công, giảm áp lực rồi điều kiện cắt tiếp tế.
    confidence: 0.88
  - id: B15-F05
    severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000460
    issue: “đã bắt liên lạc” hạ việc gặp/hội hợp với dân quân thành chỉ thiết lập liên lạc.
    evidence: Nguồn xác nhận đã gặp lực lượng dân quân; không chỉ nói có kênh liên lạc. Cũng cần làm rõ Họ ở câu sau là quân mặt đất địch.
    resolution: Dùng “đã gặp dân quân du kích”; “đã hội hợp với dân quân du kích” là lựa chọn khác nếu muốn nhấn việc gặp lực lượng. Đổi “Họ sẽ có” thành “Quân mặt đất ấy sẽ có” để phân biệt với phía đang thiếu đạn.
    confidence: 0.94
  - id: B15-F06
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000464
    issue: “một nghề mục ruỗng” không tự nhiên và dễ chuyển lời chán ghét cảnh làm lính sang cáo buộc thể chế suy đồi.
    evidence: Lời thoại đánh giá việc làm người lính là tồi tệ trong hoàn cảnh dùng dân thường làm lá chắn; không xác lập sự mục ruỗng của nghề nghiệp.
    resolution: Dùng “Dù thế nào đi nữa, làm lính cũng thật tồi tệ.”
    confidence: 0.88
  - id: B15-F07
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000474
    issue: “loạt đạn tầm xa có kỷ luật” gán kỷ luật cho đạn và thu hẹp fire thành một loạt đạn.
    evidence: Nguồn nói hỏa lực được điều khiển có kỷ luật; p000475 mô tả luồng sáng, nên không cần xác định đạn vật lý hoặc loạt bắn đồng bộ.
    resolution: Dùng “hỏa lực tầm xa được kiểm soát chặt chẽ mà Lục quân Cộng hòa rất tự hào”. Giữ giả vờ bất bình, né tránh khéo léo và đại từ nó.
    confidence: 0.95
  - id: B15-F08
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000476
    issue: “né chúng khá quyết liệt” tăng sắc thái hành động mạnh bạo thay vì mức nghiêm túc/cẩn trọng.
    evidence: Tanya vẫn coi việc né tránh là cần thiết vì có nguy cơ bị xuyên bảo hộ; nguồn không mô tả thao tác dữ dội. Khả thể xuyên thủng, ngần ngại và lựa chọn né tránh đã giữ đúng.
    resolution: Dùng “Dù vậy, mình vẫn khá nghiêm túc trong việc né tránh chúng” hoặc “mình vẫn phải né chúng thật cẩn thận”.
    confidence: 0.9
  - id: B15-F09
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000478
    issue: “thắng cả trăm trận trong một trăm trận” lặp cấu trúc thiếu tự nhiên.
    evidence: Nguồn dùng so sánh về khó khăn của chiến thắng tuyệt đối để dẫn sang khó đột phá nguyên vẹn; logic và hậu quả kinh nghiệm gặp đối thủ yếu đã được giữ.
    resolution: Dùng “cũng như khó lòng trăm trận trăm thắng”; có thể dùng “đột phá mà không bị tổn hại” để sát tình trạng nguyên vẹn hơn “không tổn thất”.
    confidence: 0.94
unresolved_findings: [B15-F01, B15-F02, B15-F03, B15-F04, B15-F05, B15-F06, B15-F07, B15-F08, B15-F09]
term_recommendations:
  - id: B15-T01
    source_term: Named
    ledger_proposal: true
    proposed_vi: một Named
    alternatives_vi: [một người được gọi là Named]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000457]
    status: pending
    confidence: 0.96
    rationale: Giữ định danh đã dùng tạm trong ledger; không suy tên riêng, quân hàm hay thân phận từ danh hiệu.
  - id: B15-T02
    source_term: raison d’état
    ledger_proposal: true
    proposed_vi: raison d’état
    alternatives_vi: [lý lẽ lợi ích quốc gia]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000462]
    status: pending
    confidence: 0.9
    rationale: Kế thừa cách giữ tiếng Pháp; đoạn nói tính toán vì quốc gia, không cần thêm chú giải hoặc đổi canon.
  - id: B15-T03
    source_term: Air Defense Identification Zone
    ledger_proposal: true
    proposed_vi: vùng nhận dạng phòng không
    alternatives_vi: [Vùng Nhận dạng Phòng không, Air Defense Identification Zone]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000467]
    status: pending
    confidence: 0.96
    rationale: Giữ đủ nhận dạng, phòng không và phạm vi vùng; chữ thường tự nhiên cho tên loại khu vực. Bản hiện tại đúng nghĩa; không biến thành vùng cấm bay hoặc tự mở rộng thành cơ chế radar.
  - id: B15-T04
    source_term: Commander
    ledger_proposal: true
    proposed_vi: Thưa chỉ huy, vậy chúng ta nên—
    alternatives_vi: [Chỉ huy, vậy chúng ta nên—]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000469]
    status: pending
    confidence: 0.95
    rationale: Lời gọi cấp chỉ huy phù hợp ngữ cảnh hỏi lệnh; thưa làm thoại tự nhiên. Không chuyển sang quân hàm cụ thể; p000470 là lời đáp không có Commander.
  - id: B15-T05
    source_term: organic resource recovery unit
    ledger_proposal: true
    proposed_vi: đơn vị thu hồi tài nguyên hữu cơ
    alternatives_vi: [bộ phận thu hồi tài nguyên hữu cơ]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000475]
    status: pending
    confidence: 0.78
    rationale: Cách literal ít suy diễn nhất; unit chưa xác định là tổ chức hay thiết bị. Không chọn tái chế tài nguyên sinh học vì đổi recovery và organic; không gán tên tác phẩm, robot hoặc chủng loài cho liên tưởng.
  - id: B15-T06
    source_term: Type 95
    ledger_proposal: true
    proposed_vi: Type 95
    alternatives_vi: [Kiểu 95]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000476]
    status: pending
    confidence: 0.96
    rationale: Giữ nhãn thiết bị tạm để không tự dựng tên kỹ thuật; ngữ cảnh chỉ cho biết có thể truyền mana vào nó.
  - id: B15-T07
    source_term: withdraw from the lines
    proposed_vi: rút khỏi các tuyến
    alternatives_vi: [rút khỏi chiến tuyến]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000451]
    status: pending
    confidence: 0.93
    rationale: Chưa đủ bằng chứng về chức năng phòng thủ; giữ cách trung tính tương thích lựa chọn các tuyến ở ledger kế thừa.
  - id: B15-T08
    source_term: company / battalion
    proposed_vi: đại đội / tiểu đoàn
    alternatives_vi: [giữ company / battalion nếu chính sách toàn dự án sau này yêu cầu]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000452, YS-LN02/Text/part0030.xhtml/p000453, YS-LN02/Text/part0030.xhtml/p000456]
    status: pending
    confidence: 0.98
    rationale: Giữ tương quan quy mô đơn vị và số lượng; đây là cấp đơn vị, không phải quân hàm. Không thêm biên chế, số hiệu hoặc quân chủng.
  - id: B15-T09
    source_term: augmented battalion
    proposed_vi: tiểu đoàn tăng cường
    alternatives_vi: [tiểu đoàn được tăng cường lực lượng]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000456]
    status: pending
    confidence: 0.94
    rationale: Tăng cường đủ rộng để không tự xác định cách tăng sức mạnh; tăng viện gợi một sự kiện bổ sung quân chưa được xác nhận.
  - id: B15-T10
    source_term: mana
    proposed_vi: mana
    alternatives_vi: [ma lực]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000476]
    status: pending
    confidence: 0.87
    rationale: Tạm giữ nhãn cùng Type 95; nguồn chỉ cho thấy đây là thứ truyền vào thiết bị. Không tự xây dựng hệ thuật ngữ phép thuật.
  - id: B15-T11
    source_term: disciplined fire
    proposed_vi: hỏa lực được kiểm soát chặt chẽ
    alternatives_vi: [hỏa lực bắn có kỷ luật]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000474]
    status: pending
    confidence: 0.95
    rationale: Chọn phương án thay thế đã có trong ledger để hợp danh ngữ ở đây; không tự thêm tính đồng bộ, độ chính xác tuyệt đối hoặc dạng đạn.
  - id: B15-T12
    source_term: Vianto pronouns / his adjutant
    proposed_vi: Vianto tại p000453; anh trong trần thuật p000466, p000468, p000471
    alternatives_vi: [lặp Vianto khi mơ hồ, lược chủ ngữ nếu đã rõ]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000453, YS-LN02/Text/part0030.xhtml/p000466, YS-LN02/Text/part0030.xhtml/p000468, YS-LN02/Text/part0030.xhtml/p000471]
    status: pending
    confidence: 0.94
    rationale: Giữ lựa chọn địa phương đã ghi; lặp tên ở câu có danh hiệu đối phương để khóa tham chiếu. Không suy tuổi, sự thân mật hay mở rộng DEC-P01-001 sang Vianto.
  - id: B15-T13
    source_term: viewpoint pronouns in speech and thought
    proposed_vi: tôi/chúng ta trong thoại; ta hoặc chúng ta cho nội tâm tập thể; bạn cho câu hỏi khái quát của Tanya
    alternatives_vi: [lược anh ở câu hỏi p000458, dùng chúng ta nhất quán ở nội tâm tập thể]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000452, YS-LN02/Text/part0030.xhtml/p000458, YS-LN02/Text/part0030.xhtml/p000459, YS-LN02/Text/part0030.xhtml/p000460, YS-LN02/Text/part0030.xhtml/p000461, YS-LN02/Text/part0030.xhtml/p000463, YS-LN02/Text/part0030.xhtml/p000464, YS-LN02/Text/part0030.xhtml/p000469, YS-LN02/Text/part0030.xhtml/p000470, YS-LN02/Text/part0030.xhtml/p000472]
    status: pending
    confidence: 0.86
    rationale: Lời bàn và suy nghĩ là phía Vianto; bạn ở p000472 là câu hỏi khái quát chứ không xác lập người đối thoại. Anh ở p000458 có thể giữ cục bộ, không coi là quan hệ thân thiết đã chốt.
  - id: B15-T14
    source_term: raison d’être
    proposed_vi: raison d’être
    alternatives_vi: [lẽ tồn tại]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000466]
    status: pending
    confidence: 0.87
    rationale: Có thể giữ tiếng Pháp như bản hiện tại; nghĩa về lý do tồn tại của người lính khác lợi ích quốc gia ở p000462, không được đồng nhất hai cụm.
  - id: B15-T15
    source_term: humans spotting
    proposed_vi: việc quan sát xác định mục tiêu do con người đảm nhiệm
    alternatives_vi: [người ngắm bắn là con người]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000475]
    status: pending
    confidence: 0.8
    rationale: Spotting nhấn vào quan sát mục tiêu; bản hiện tại giữ yếu tố con người nhưng gộp sang ngắm bắn. Phương án trung tính tránh tự thêm một tổ quan sát pháo binh riêng; đây là khuyến nghị làm rõ, không tính thành lỗi nghĩa riêng khi ngữ cảnh còn hạn chế.
coverage:
  note: Tất cả ID dưới đây đã được xét nghĩa, văn phong, điểm nhìn/đại từ, nhấn mạnh và thuật ngữ/cấp bậc; các mục pass không có lỗi có căn cứ cần sửa.
  per_segment:
    p000451: B15-F01; điều kiện và khả thể giữ đúng; nhấn mạnh đúng phạm vi.
    p000452: pass; hai đại đội và câu hỏi bế tắc giữ đúng.
    p000453: B15-F02; nhiệm vụ đặc biệt và một trong các mục tiêu giữ đúng.
    p000454: pass; tác chiến đô thị và không trụ nổi hai tuần giữ đúng.
    p000455: pass; giữ giả định địch tập trung nhiều hơn dự tính.
    p000456: B15-F03; giữ tăng quy mô đột ngột và đơn vị.
    p000457: pass; Named và việc sẵn sàng tung vào trận giữ đúng.
    p000458: B15-F04; trình tự tác chiến giữ đúng, nên làm rõ mức kỳ vọng.
    p000459: pass; lời bác bỏ lạc quan và mong thành công giữ đúng.
    p000460: B15-F05; nhấn mạnh đúng, tương quan hỏa lực và giới hạn đạn giữ đúng.
    p000461: pass; giữ tổn thất, xác suất dùng lá chắn và sự hổ thẹn; nhấn mạnh đúng.
    p000462: pass; giữ tính toán vắt kiệt du kích để câu giờ và đánh giá mặt xấu.
    p000463: pass; giữ câu hỏi phương án xấu nhất và tối đa thiệt hại.
    p000464: B15-F06; giữ lựa chọn duy nhất, nên sửa sắc thái nghề nghiệp.
    p000465: pass; nhiệm vụ dùng dân thường và lý do không có lựa chọn giữ đúng; không thêm cơ chế ra lệnh.
    p000466: pass; Vianto tự chất vấn lẽ tồn tại, nghịch lý bảo vệ Cộng hòa nhưng để công dân chết giữ đúng.
    p000467: pass; cảnh báo tiền đội và tốc độ áp sát giữ đúng; tên vùng chỉ là đề xuất.
    p000468: pass; giữ thời điểm suy nghĩ và giả định đã chết từ lâu nếu không hiểu.
    p000469: pass; lời gọi chức năng và câu nói bị ngắt giữ đúng, thưa là cải thiện tùy chọn.
    p000470: pass; lời đáp và lệnh chuẩn bị phục kích giữ đúng.
    p000471: pass; ưu tiên sống sót trước rồi mới hối tiếc giữ đúng.
    p000472: pass; chuyển sang Tanya, câu hỏi khái quát và mình giữ đúng; nhấn mạnh toàn đoạn đúng.
    p000473: pass; giọng tự đánh giá và muốn làm việc cho ra trò giữ đúng; nhấn mạnh toàn đoạn đúng.
    p000474: B15-F07; nó theo DEC-P01-001; giả vờ và đồng thời né tránh giữ đúng.
    p000475: pass với B15-T05/B15-T15; giữ so sánh sức mạnh và tỷ lệ trúng thấp do yếu tố con người, không suy lore.
    p000476: B15-F08; mình đúng điểm nhìn; nguồn không nhấn mạnh nên không thêm chữ nghiêng; nguy cơ và né tránh giữ đúng.
    p000477: pass; lệnh giao chiến và đối phương nhanh/thành thạo giữ đúng; “Rành việc thật!” có thể giữ giọng gấp.
    p000478: B15-F09; giữ hỏa lực dày và hậu quả kinh nghiệm gặp lực lượng hạng hai; họ là phía Tanya.
risks:
  - segment_id: YS-LN02/Text/part0030.xhtml/p000451
    assessment: Cần sửa B15-F01; chưa đủ căn cứ chọn tuyến phòng thủ hoặc tự giải thích mục đích rút quân.
    temporary_choice: rút khỏi các tuyến
    confidence: 0.93
  - segment_id: YS-LN02/Text/part0030.xhtml/p000467
    assessment: Đúng nghĩa, không có lỗi mức vừa; viết hoa là lựa chọn biên tập tạm, không xác lập tên riêng canon.
    temporary_choice: vùng nhận dạng phòng không
    confidence: 0.96
  - segment_id: YS-LN02/Text/part0030.xhtml/p000469
    assessment: Commander là lời gọi chức năng ở đây; chưa đủ căn cứ dịch thành quân hàm. Self-check gán p000470 là phạm vi thuật ngữ quá rộng, nhưng p000470 không sai bản dịch.
    temporary_choice: Thưa chỉ huy
    confidence: 0.95
  - segment_id: YS-LN02/Text/part0030.xhtml/p000474
    assessment: Đại từ nó đúng quy tắc đã duyệt; cần sửa kết hợp từ hỏa lực. Giữ sắc thái giả vờ thay vì biến thành bất bình thật.
    temporary_choice: hỏa lực tầm xa được kiểm soát chặt chẽ
    confidence: 0.95
  - segment_id: YS-LN02/Text/part0030.xhtml/p000475
    assessment: Liên tưởng đơn vị thù địch chưa đủ để xác lập thiết bị/tác phẩm cụ thể; giữ literal, không bổ sung lore.
    temporary_choice: đơn vị thu hồi tài nguyên hữu cơ
    confidence: 0.78
  - segment_id: YS-LN02/Text/part0030.xhtml/p000476
    assessment: Không có quyết định canon cho mana/Type 95; không suy diễn cơ chế khiến dùng thiết bị có hại tinh thần.
    temporary_choice: giữ mana và Type 95
    confidence: 0.87
next_action: Coordinator ghi lựa chọn tạm vào ledger/handoff; người giữ quyền sửa áp dụng B15-F01–F09 và khuyến nghị đã chọn, rồi kiểm tra lại b15. Chưa sign-off vì còn bốn lỗi mức vừa. Không cần hỏi người dùng cho các mục ordinary pending này.
```
