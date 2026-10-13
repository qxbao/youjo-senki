# Review — vol-02-ch-05-b15

```yaml
role: reviewer
task_id: vol-02-ch-05-b15-review
state: done
review_path: reviews/prose/vol-02/ch-05-b15-codex.md
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000358
  - YS-LN02/Text/part0026.xhtml/p000359
  - YS-LN02/Text/part0026.xhtml/p000360
  - YS-LN02/Text/part0026.xhtml/p000361
  - YS-LN02/Text/part0026.xhtml/p000362
  - YS-LN02/Text/part0026.xhtml/p000363
  - YS-LN02/Text/part0026.xhtml/p000364
  - YS-LN02/Text/part0026.xhtml/p000365
  - YS-LN02/Text/part0026.xhtml/p000366
  - YS-LN02/Text/part0026.xhtml/p000367
  - YS-LN02/Text/part0026.xhtml/p000368
  - YS-LN02/Text/part0026.xhtml/p000369
  - YS-LN02/Text/part0026.xhtml/p000370
  - YS-LN02/Text/part0026.xhtml/p000371
  - YS-LN02/Text/part0026.xhtml/p000372
  - YS-LN02/Text/part0026.xhtml/p000373
  - YS-LN02/Text/part0026.xhtml/p000374
  - YS-LN02/Text/part0026.xhtml/p000375
  - YS-LN02/Text/part0026.xhtml/p000376
  - YS-LN02/Text/part0026.xhtml/p000377
  - YS-LN02/Text/part0026.xhtml/p000378
  - YS-LN02/Text/part0026.xhtml/p000379
  - YS-LN02/Text/part0026.xhtml/p000380
  - YS-LN02/Text/part0026.xhtml/p000381
  - YS-LN02/Text/part0026.xhtml/p000382
files_written: [reviews/prose/vol-02/ch-05-b15-codex.md]
validator: not_run
diff_check: not_run
commit: null
package_hash_verification:
  path: work/vol-02/batches/ch-05-b15-source.jsonl
  algorithm: sha256
  expected: 38531306e5839281ec705606edef8cc4ec8af3166a6d7c41ab76644b2870443a
  actual: 38531306e5839281ec705606edef8cc4ec8af3166a6d7c41ab76644b2870443a
  result: pass
  matches: [review_handoff, batch_handoff]
  embedded_source_sha256: 3ac53161b6e093ba07203f284a400049cf902a3b0f51c0d3e40200867c13ae0a
  embedded_source_hash_consistency: pass
  note: Hash nhúng nhất quán với batch handoff và cả 25 dòng bản dịch; không mở sách gốc để tái tính hash sách.
segment_order_verification:
  result: pass
  source_count: 25
  translation_count: 25
  source_unique_ids: 25
  translation_unique_ids: 25
  exact_expected_order: true
  source_translation_order_match: true
  start: YS-LN02/Text/part0026.xhtml/p000358
  end: YS-LN02/Text/part0026.xhtml/p000382
  missing_ids: []
  extra_ids: []
counts:
  reviewed_segments: 25
  serious: 0
  moderate: 4
  minor: 6
  total_findings: 10
unresolved_findings: [R01, R02, R03, R04, R05, R06, R07, R08, R09, R10]
findings:
  - id: R01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000358
    issue: Bản dịch tự xác định cảnh báo là những hồi còi báo động.
    evidence: Package chỉ mô tả cảnh báo dễ được đưa ra, không xác định thiết bị hay âm thanh. Chi tiết còi khiến mô tả quy trình cảnh giới cụ thể hơn nguồn.
    resolution: Đề xuất thay bằng “Tân binh lẫn cựu binh đều phải đối phó với những cảnh báo được đưa ra chỉ vì một chuyện cỏn con.”
    status: open
  - id: R02
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000361
    issue: Cụm “thì đặc biệt khó chịu nổi” không tự nhiên và khiến câu thoại khó đọc.
    evidence: Nguồn đánh giá việc chứng kiến cách tác chiến ấy là rất khó chịu; ý này đã có nhưng kết hợp từ chưa thành câu tiếng Việt trôi chảy.
    resolution: Đề xuất “Đặc biệt, nhìn họ tác chiến trong những môi trường không thể dựa vào phép thuật thì thật khó mà chịu nổi.”
    status: open
  - id: R03
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000362
    issue: “Kết giới phòng thủ” đổi hình ảnh lớp vỏ và lệch lựa chọn tạm “lớp vỏ phòng ngự” đã có trong ledger.
    evidence: Package phân biệt hai biện pháp bảo vệ. Ledger ch01-b07 và ch04-b07 dùng lớp vỏ phòng ngự cho defensive shell; chưa có căn cứ trong lô này để đồng nhất với kết giới hoặc đổi tên cơ chế.
    resolution: Đề xuất dùng “màng bảo hộ” và “lớp vỏ phòng ngự”, giữ cả hai biện pháp; đây là lựa chọn tạm, không xác lập cơ chế hoặc canon.
    status: open
  - id: R04
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000364
    issue: Thiếu chữ nghiêng cho toàn bộ câu nhớ lại của Tanya.
    evidence: XHTML của package có một phần em từ lời chợt nhớ đến hết đoạn; trường translation không có dấu sao. Self-check ghi đã giữ dấu nhấn mạnh ở đoạn này nhưng tệp được giao không thể hiện điều đó.
    resolution: Bọc phần từ “À phải” đến dấu ba chấm cuối đoạn bằng *...*, giữ câu trần thuật mở đầu ngoài chữ nghiêng theo DEC-P01-002.
    status: open
  - id: R05
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000365
    issue: Thiếu chữ nghiêng cho câu kết luận nội tâm giữa đoạn.
    evidence: XHTML có một phần em cho lời nhận ra tác hại nhân lên từ lỗi cá nhân. Bản dịch hiện không có dấu sao dù self-check ghi đã giữ.
    resolution: Chỉ bọc câu từ “À, đúng là” đến “gấp bội.” bằng *...*; không nghiêng câu điều tra mở đầu hoặc phần trần thuật cuối đoạn.
    status: open
  - id: R06
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000368
    issue: “Vô tình bỏ qua” làm giảm nét thiếu cẩn trọng của các sĩ quan trong suy luận của Tanya.
    evidence: Nguồn mô tả việc bỏ sót do bất cẩn, không chỉ là không có chủ ý. Đây vẫn là suy đoán của Tanya, chưa phải kết luận khách quan của người kể.
    resolution: Đề xuất “một nguy cơ mà các sĩ quan khắp mặt trận đã sơ ý bỏ qua”; giữ “Hẳn” và phạm vi chữ nghiêng hiện có.
    status: open
  - id: R07
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000371
    issue: “Ai cũng cho rằng” thêm sự đồng thuận tuyệt đối; “cảnh xác người bị sản xuất hàng loạt” nặng cấu trúc bị động.
    evidence: Package chỉ nêu giả định đang được dùng, không khẳng định mọi người cùng tin. Ẩn dụ sản xuất xác người có trong nguồn và cần giữ độ lạnh lùng, nhưng không bắt buộc cấu trúc bị động hiện tại.
    resolution: Đề xuất phần nghiêng “Dù giả định hiện giờ là sẽ không nổ ra một trận đánh quy mô lớn…”; đổi cụm sau thành “việc sản xuất xác người hàng loạt”. Giữ nhận xét về người tử tế và sự đối lập với Tanya ở p000372.
    status: open
  - id: R08
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000374
    issue: “Sẽ trở thành” biến nguy cơ có thể gây thất bại thành dự báo chắc chắn; “quá sức chịu đựng” thêm ngưỡng chịu đựng không được xác định.
    evidence: Package thể hiện nỗi lo về khả năng tân binh phụ thuộc phép thuật là nhân tố lớn gây thất bại. Nhận định về thiệt hại chỉ nhấn mức quá lớn, không nói ai không chịu nổi.
    resolution: Đề xuất “thiệt hại thảm khốc—quá lớn” và “Nó lo rằng những tân binh không thể hoạt động nếu không dựa vào phép thuật có thể là một nhân tố lớn dẫn đến thất bại trong nhiệm vụ có rủi ro cao.”
    status: open
  - id: R09
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000380
    issue: “Ngài gọi tôi ạ?” đổi câu hỏi tiếp lời thành câu hỏi về việc được gọi.
    evidence: Đại tá vừa mở lời ở p000378; Tanya hỏi ông muốn nói việc gì. Package không nêu hành động gọi Tanya.
    resolution: Đề xuất “Vâng, có chuyện gì vậy, thưa ngài?”
    status: open
  - id: R10
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000382
    issue: “Kinh nghiệm được bảo vệ” gắn trạng thái được bảo vệ vào kinh nghiệm, tạo kết hợp từ khó hiểu.
    evidence: Nguồn đối chiếu việc tích lũy kinh nghiệm trong điều kiện được bảo vệ của một chiến dịch lớn với việc lặp lại và rút kinh nghiệm qua các trận nhỏ.
    resolution: Đề xuất “Điều họ cần hơn việc tích lũy kinh nghiệm dưới sự bảo vệ trong một chiến dịch lớn là luyện tập lặp đi lặp lại và ôn lại kỹ lưỡng qua những trận đánh quy mô nhỏ.” Không thêm người bảo vệ hay hình thức bảo vệ cụ thể.
    status: open
pending_terms:
  - source_term: Heinrich's Law
    proposed_vi: Định luật Heinrich
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000367]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: Murphy's Law
    proposed_vi: Định luật Murphy
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000367]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: protective films / defensive shells
    proposed_vi: màng bảo hộ / lớp vỏ phòng ngự
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000362]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: replacement troops
    proposed_vi: quân thay thế / lính thay thế
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000358, YS-LN02/Text/part0026.xhtml/p000365, YS-LN02/Text/part0026.xhtml/p000372]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: non-magic raid
    proposed_vi: đột kích không dùng phép thuật
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000382]
    volume: vol-02
    chapter: 5
    status: pending
term_recommendations:
  - id: vol02-ch05-b15-heinrichs-law
    source_term: Heinrich's Law
    proposed_vi: Định luật Heinrich
    alternatives_vi: [Luật Heinrich]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000367]
    status: pending
    canon: false
    rationale: Giữ tên Heinrich và cách đặt tên song song với Murphy trong suy luận về sai sót nhỏ dẫn tới hậu quả lớn; không thêm tỷ lệ tai nạn hay diễn giải học thuyết ngoài package.
  - id: vol02-ch05-b15-murphys-law
    source_term: Murphy's Law
    proposed_vi: Định luật Murphy
    alternatives_vi: [Luật Murphy]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000367]
    status: pending
    canon: false
    rationale: Giữ cách gọi hiện tại và cấu trúc song song với Heinrich. Ngữ cảnh là nguy cơ bỏ qua khả năng thất bại; không cần bổ sung lời giải thích hoặc một công thức của định luật.
  - id: vol02-ch05-b15-protective-films
    source_term: protective films / defensive shells
    proposed_vi: màng bảo hộ / lớp vỏ phòng ngự
    alternatives_vi: [lớp bảo vệ / lớp vỏ phòng thủ, màn chắn bảo hộ / kết giới phòng thủ]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000362]
    status: pending
    canon: false
    confidence: 0.65
    rationale: Màng và lớp vỏ giữ hai hình ảnh khác nhau, không suy diễn cấu tạo phép thuật. Lớp vỏ phòng ngự kế thừa ledger ch01-b07/ch04-b07; ch05-b04 cũng giữ hình ảnh lớp vỏ. Phương án kết giới ít literal hơn và chưa có căn cứ để coi là tên cơ chế.
  - id: vol02-ch05-b15-replacement-troops
    source_term: replacement troops
    proposed_vi: quân thay thế (tập thể hoặc đối tượng huấn luyện); lính thay thế (thành phần quân số)
    alternatives_vi: [quân bổ sung / lính bổ sung, binh sĩ thay thế]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000358, YS-LN02/Text/part0026.xhtml/p000360, YS-LN02/Text/part0026.xhtml/p000365, YS-LN02/Text/part0026.xhtml/p000372]
    status: pending
    canon: false
    rationale: Giữ gốc thay thế đang dùng trong lô; quân/lính là biến thể cú pháp có thể dùng nhất quán theo tập thể và quân số. Không đồng nhất thuật ngữ này với lực lượng tăng viện hay khẳng định họ thay riêng người tử trận.
    scope_note: p000360 nằm trong nhóm ledger nhưng package gọi người mới nhập ngũ; giữ “tân binh” ở đó, không buộc đổi thành quân thay thế. p000365 nói việc huấn luyện lực lượng thay thế; p000372 nói thành phần đơn vị.
  - id: vol02-ch05-b15-non-magic-raid
    source_term: non-magic raid
    proposed_vi: đột kích không dùng phép thuật
    alternatives_vi: [cuộc đột kích không sử dụng phép thuật, đột kích phi phép thuật]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000382]
    status: pending
    canon: false
    rationale: Tường minh việc không sử dụng phép thuật, khớp chuỗi huấn luyện ở p000361–p000375. Phi phép thuật kém tự nhiên và dễ hiểu như phân loại bản chất nhiệm vụ; không suy ra loại vũ khí hoặc thành phần lực lượng.
translator_observations:
  - segment_id: YS-LN02/Text/part0026.xhtml/p000364
    assessment: supported_no_mechanism_correction
    rationale: “Bị thổi bay” giữ hình ảnh hủy diệt mạnh của package; nguồn không chỉ rõ vũ khí hay cách đơn vị bị tiêu diệt. Không yêu cầu thêm bom, pháo hay cơ chế nổ. Lỗi có căn cứ tại đây là mất chữ nghiêng, đã ghi R04.
  - segment_id: YS-LN02/Text/part0026.xhtml/p000371
    assessment: supported_keep_metaphor
    rationale: Ẩn dụ sản xuất xác người hàng loạt có căn cứ và cần giữ. Đánh giá đạo đức thuộc sĩ quan tác chiến, đối lập với lo ngại hiệu năng của Tanya; không làm dịu ẩn dụ. Chỉ sửa lượng từ và câu chữ theo R07.
self_check_assessment:
  emphasis: Self-check không khớp bản dịch ở p000364/p000365. Các phần nhấn mạnh p000368/p000371/p000372/p000379 khớp phạm vi XHTML; những đoạn còn lại không có dấu nghiêng thêm.
  viewpoint: p000379 mở bằng nội tâm đại tá, được phần trần thuật liền sau xác định. “Tôi” ở đây có căn cứ; không đổi thành “mình” của Tanya. Nhận xét self-check về các suy luận của Tanya không được mở rộng sang phần này.
  modality: Các điều kiện ở p000368/p000369/p000371/p000373 và quyết định miễn cưỡng p000382 nhìn chung được giữ; p000374 cần khôi phục khả năng theo R08.
coverage:
  p000358: Đã xét cảnh giới, ban đêm/ban ngày, tính chưa quen và quân thay thế; R01.
  p000359: Lời đồng ý có dè dặt và việc suy nghĩ trước khi đáp được giữ; không phát hiện lỗi cần sửa.
  p000360: Giữ giả định chưa quen chiến hào và nhu cầu huấn luyện lại; tân binh không bắt buộc đổi theo nhóm replacement.
  p000361: Giữ hạn chế không thể dựa vào phép thuật; R02 về lời thoại.
  p000362: Giữ hai lớp bảo vệ, tự bảo vệ vô thức và hệ quả bị nhắm tới; R03 về thuật ngữ tạm.
  p000363: Giữ lệnh nghiêm cấm, tín hiệu vô ý lộ ra và việc bị địch phát hiện; không phát hiện lỗi cần sửa.
  p000364: Giữ ký ức đơn vị bị hủy diệt, lỗi cá nhân và thời điểm chuẩn bị; R04 về nhấn mạnh.
  p000365: Giữ câu hỏi sau điều tra, thiệt hại nhân lên và lối suy luận lệch của Tanya; R05 về nhấn mạnh.
  p000366: Giữ câu hỏi về cả trận nhỏ với tân binh huấn luyện thiếu; không phát hiện lỗi cần sửa.
  p000367: Giữ lập luận quản trị rủi ro và giọng coi con người là đồ ngốc; hai định luật vẫn là đề xuất.
  p000368: Giữ suy đoán của Tanya, sự kiêu ngạo và phạm vi nhấn mạnh; R06.
  p000369: Giữ góc nhìn nhân sự, giả định trận lớn và nguy cơ vấn đề nặng hơn; không phát hiện lỗi cần sửa.
  p000370: Giữ lời thoại bỏ lửng và đối chiếu quy mô giao tranh; không phát hiện lỗi cần sửa.
  p000371: Giữ quan tâm đạo đức của đại tá, thương vong và ẩn dụ; R07. Ban tác chiến phù hợp đề xuất chức năng ở ledger ch05-b08, chưa canon.
  p000372: Giữ đồng ý bề ngoài của Tanya, ít quan tâm thương vong và đánh giá đơn vị yếu; nhấn mạnh đúng phạm vi.
  p000373: Giữ xác suất trận lớn thấp nhưng sai sót hiện hữu tích lũy; không phát hiện lỗi cần sửa.
  p000374: Giữ lỗi cá nhân gây tổn thất lớn và nỗi lo phụ thuộc phép thuật; R08 về độ chắc chắn và mức thiệt hại.
  p000375: Giữ lời đại tá nhắc trải nghiệm Norden và việc không thể dựa vào phép thuật; không phát hiện lỗi nghĩa. “Ngài” là lựa chọn thoại tạm, không chứng minh quan hệ hoặc canon xưng hô.
  p000376: Giữ lời nhận thiếu sót và hứa lưu ý khi huấn luyện; không phát hiện lỗi cần sửa.
  p000377: Giữ tương phản dân sự/quân đội và cách Tanya diễn giải khẩu hiệu qua hậu quả lỗi cá nhân; không phát hiện lỗi cần sửa.
  p000378: Giữ lời mở chuyện bỏ lửng; không phát hiện lỗi cần sửa.
  p000379: Giữ nội tâm đại tá, sự hồ hởi và hiểu lầm do hai bên chỉ thấy chỗ đồng ý; chữ nghiêng đúng. Không gán nội tâm này cho Tanya.
  p000380: Đã xét mục đích câu hỏi tiếp lời; R09.
  p000381: Giữ yêu cầu cho lính có trải nghiệm; “thực tế” có căn cứ trực tiếp ở p000379, “cô” giữ là xưng hô tạm.
  p000382: Giữ ưu tiên luyện lại ở trận nhỏ và quyết định miễn cưỡng đột kích không dùng phép thuật; R10 về câu chữ.
risks:
  - Review đã hoàn tất nhưng bản dịch còn 4 finding vừa và 6 finding nhẹ chưa được người giữ quyền sửa xử lý.
  - Mọi khuyến nghị thuật ngữ là tạm, không nâng thành canon; không có quyết định canon ảnh hưởng cốt truyện cần dừng trong phạm vi lô này.
next_action: coordinator_handoff_to_translation_editor
```
