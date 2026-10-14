# Review b05 — nghĩa và giọng văn

```yaml
role: reviewer
task_id: vol-02-ch-07-b05-review
batch: vol-02-ch-07-b05
state: done
review_path: reviews/prose/vol-02/ch-07-b05-codex.md
files_written:
  - reviews/prose/vol-02/ch-07-b05-codex.md
segment_ids:
  - YS-LN02/Text/part0032.xhtml/p000104
  - YS-LN02/Text/part0032.xhtml/p000105
  - YS-LN02/Text/part0032.xhtml/p000106
  - YS-LN02/Text/part0032.xhtml/p000107
  - YS-LN02/Text/part0032.xhtml/p000108
  - YS-LN02/Text/part0032.xhtml/p000109
  - YS-LN02/Text/part0032.xhtml/p000110
  - YS-LN02/Text/part0032.xhtml/p000111
  - YS-LN02/Text/part0032.xhtml/p000112
  - YS-LN02/Text/part0032.xhtml/p000113
  - YS-LN02/Text/part0032.xhtml/p000114
  - YS-LN02/Text/part0032.xhtml/p000115
  - YS-LN02/Text/part0032.xhtml/p000116
  - YS-LN02/Text/part0032.xhtml/p000117
  - YS-LN02/Text/part0032.xhtml/p000118
  - YS-LN02/Text/part0032.xhtml/p000119
  - YS-LN02/Text/part0032.xhtml/p000120
  - YS-LN02/Text/part0032.xhtml/p000121
  - YS-LN02/Text/part0032.xhtml/p000122
  - YS-LN02/Text/part0032.xhtml/p000123
  - YS-LN02/Text/part0032.xhtml/p000124
  - YS-LN02/Text/part0032.xhtml/p000125
  - YS-LN02/Text/part0032.xhtml/p000126
  - YS-LN02/Text/part0032.xhtml/p000127
  - YS-LN02/Text/part0032.xhtml/p000128
  - YS-LN02/Text/part0032.xhtml/p000129
  - YS-LN02/Text/part0032.xhtml/p000130
  - YS-LN02/Text/part0032.xhtml/p000131
counts:
  source_rows: 28
  translation_rows: 28
  reviewed_rows: 28
  serious: 0
  moderate: 3
  minor: 3
  unresolved_findings: 6
  pending_choices_assessed: 7
input_checks:
  package_sha256: 6644770cd31ca1c5d2bfff29bb96bd181e047e2b4bed40044e6f5b17986b6b46
  package_hash_matches_handoff: true
  segment_ids_match: true
  row_source_hashes_match_primary_handoff: true
  five_named_canon_hashes_match: true
  ledger_section: chapter7_b05_translator_proposals
validator: not_run
diff_check: not_run
commit: null
findings:
  - id: B05-C01
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000104
    issue: Cấu trúc “hễ có ai ... thì ... cũng làm được” đổi trọng tâm của lời đánh giá năng lực.
    evidence: >-
      Nguồn nhấn mạnh niềm tin rằng 203 là đơn vị có khả năng làm việc đó nếu có
      bất cứ đơn vị nào làm nổi; bản dịch biến thành so sánh với thành tích của
      một người hoặc đơn vị khác. Cụm “vì chỉ vì” còn làm câu vấp.
    resolution: >-
      Đề xuất đổi vế cuối thành “ai nấy đều tin chắc rằng nếu có đơn vị nào đủ sức
      phá hủy kho đạn của địch thì đó chính là Tiểu đoàn Pháp sư Trên không số 203”,
      đồng thời bỏ một chữ “vì”. Giữ câu hỏi tự giễu và nguyên nhân từ vụ Dacia.
    status: open
  - id: B05-C02
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000112
    issue: “Trận địa pháo” tự xác định loại hỏa lực.
    evidence: >-
      Package chỉ xác định các vị trí khai hỏa dưới vùng trời giao chiến, không
      xác định đó là pháo. Chi tiết thêm này thu hẹp hình dung chiến thuật.
    resolution: >-
      Tạm dùng “các vị trí khai hỏa” hoặc “các trận địa hỏa lực”; giữ ý đối phương
      ở sân nhà và vẫn có nguy cơ vô tình bị bắn trúng. Không tự chỉ ra bên bắn
      hay loại vũ khí.
    status: open
  - id: B05-C03
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000126
    issue: “Bộ binh” thu hẹp lực lượng rút lui; “cố thủ” gợi thế phòng thủ cố định quá cụ thể.
    evidence: >-
      Nguồn nói lực lượng trên mặt đất nói chung và yêu cầu đoạn hậu trụ lại để
      câu giờ. Package không giới hạn thành phần quân rút lui vào bộ binh hoặc
      yêu cầu giữ một vị trí cố định.
    resolution: >-
      Đề xuất “lực lượng trên mặt đất” thay “bộ binh” và “cầm cự” thay “cố thủ”.
      Giữ chuỗi nghi binh thất bại, đoạn hậu phải câu giờ, rút lui mất trật tự và
      nguy cơ bị giẫm đạp; không tự xác định ai gây ra nguy cơ cuối.
    status: open
  - id: B05-C04
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000106
    issue: Mất dấu gọi chú thích 25 cạnh Matsusheeta.
    evidence: >-
      XHTML trong package có liên kết chú thích và số mũ; bản dịch bỏ hẳn dấu
      nhận diện. Nội dung chú thích không nằm trong phạm vi được giao.
    resolution: >-
      Đề xuất phục hồi dấu ²⁵ cạnh tên để giữ liên hệ chú thích, hoặc coordinator
      xác nhận cơ chế bảo toàn liên kết khi dựng bản xuất. Không thêm nội dung
      chú thích và không mở tệp đích. Đây là đề xuất định dạng, chưa phải canon.
    status: open
  - id: B05-C05
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000110
    issue: “Chỉ vừa đủ giữ được giọng điệu công việc” thiếu tự nhiên và làm mờ vẻ chuyên nghiệp gượng giữ.
    evidence: >-
      Tanya đang nén giận để lời đáp vẫn có vẻ chuyên nghiệp; “giọng điệu công
      việc” là kết hợp từ cứng, còn “vừa đủ” nghiêng sang đánh giá mức đạt yêu cầu.
    resolution: >-
      Đề xuất “mình chật vật giữ giọng chuyên nghiệp”. Giữ cơn giận đang dâng và
      lời bình chua chát về sự nhẹ tênh của cấp trên.
    status: open
  - id: B05-C06
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000130
    issue: Chuỗi phủ định dài làm lời tự khẳng định của Tanya khó đọc.
    evidence: >-
      Nghĩa về sự dại dột khi bỏ đầu tư vì một rủi ro nhỏ vẫn đúng, nhưng cấu trúc
      “không phải kiểu người không hiểu rằng chẳng đầu tư” làm giọng phân tích vấp.
    resolution: >-
      Đề xuất “Mình hiểu rõ việc không đầu tư chỉ vì sợ một rủi ro nhỏ là dại dột”.
      Giữ “lợi nhuận” ở câu sau để bảo toàn phép so sánh kinh tế.
    status: open
unresolved_findings: [B05-C01, B05-C02, B05-C03, B05-C04, B05-C05, B05-C06]
term_recommendations:
  - source_term: 203rd Aerial Mage Battalion
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000104]
    proposed_vi: Tiểu đoàn Pháp sư Trên không số 203
    alternatives_vi: [Tiểu đoàn Pháp sư Không chiến số 203]
    status: provisional_non_canon
    canon: false
    rationale: >-
      Giữ lựa chọn của ledger; cách gọi trên không sát nhãn đơn vị và không tự
      giới hạn nhiệm vụ vào không chiến. Phương án không chiến dễ đọc nhưng hẹp
      hơn. Chưa có thuật ngữ được duyệt trong glossary.
  - source_term: interdiction combat
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000110, YS-LN02/Text/part0032.xhtml/p000111, YS-LN02/Text/part0032.xhtml/p000119]
    proposed_vi: tác chiến ngăn chặn
    alternatives_vi: [tác chiến kiềm chế]
    status: provisional_non_canon
    canon: false
    rationale: >-
      Giữ lựa chọn ledger vì mệnh lệnh tại p000109 là cầm chân đối phương đến hết
      giai đoạn ba. Kiềm chế diễn tả tác dụng tại chỗ nhưng kém sát nhãn nhiệm vụ.
      Không đồng nhất với “đánh chặn”, vốn chỉ hoạt động của phía đối phương trong lô.
  - source_term: recon-in-force
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000111, YS-LN02/Text/part0032.xhtml/p000117, YS-LN02/Text/part0032.xhtml/p000125, YS-LN02/Text/part0032.xhtml/p000126]
    proposed_vi: trinh sát chiến đấu
    alternatives_vi: [trinh sát bằng vũ lực, trinh sát có vũ trang]
    status: provisional_non_canon
    canon: false
    rationale: >-
      Giữ lựa chọn ledger: p000125 nêu thăm dò năng lực đánh chặn, p000111 có lực
      lượng hai đại đội xuyên vị trí phòng thủ. “Bằng vũ lực” làm rõ yếu tố giao
      chiến nhưng thô; “có vũ trang” chỉ nói trang bị, chưa thể hiện thăm dò bằng
      tác chiến. Đây là đánh giá theo package, không khẳng định chuẩn học thuyết.
  - source_term: rear guard
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000126, YS-LN02/Text/part0032.xhtml/p000128]
    proposed_vi: lực lượng đoạn hậu
    alternatives_vi: [lực lượng hậu vệ]
    status: provisional_non_canon
    canon: false
    rationale: >-
      Giữ lựa chọn ledger vì vai trò là cầm cự để bảo vệ cuộc rút lui và câu giờ,
      kể cả chịu tiêu diệt sạch. Hậu vệ là phương án khả dụng nhưng kém rõ chức
      năng trong cuộc rút lui. Không tự suy ra cấp tổ chức của lực lượng này.
  - source_term: Rhine lines/front
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000109, YS-LN02/Text/part0032.xhtml/p000129]
    proposed_vi: phòng tuyến Rhine / mặt trận Rhine
    alternatives_vi: [tuyến phòng thủ Rhine / mặt trận Rhine]
    status: provisional_non_canon
    canon: false
    rationale: >-
      Giữ phân biệt tuyến phòng thủ bị áp sát ở p000109 với phạm vi mặt trận có
      nhiều đơn vị ở p000129. Không gộp thành một tên chiến dịch hoặc Việt hóa địa
      danh khi package chưa có căn cứ.
  - source_term: Matsusheeta
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000106]
    proposed_vi: Matsusheeta
    alternatives_vi: [Matsusheeta kèm dấu gọi chú thích ²⁵]
    status: provisional_non_canon
    canon: false
    rationale: >-
      Giữ đúng dạng tên trong package. Phương án khác chỉ phục hồi dấu chú thích,
      không chuẩn hóa tên thành một nhân vật ngoài đời. Không đủ căn cứ cục bộ
      để đề xuất một cách viết tên khác có trách nhiệm.
  - source_term: CP / Fairy 01
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000105, YS-LN02/Text/part0032.xhtml/p000110]
    proposed_vi: CP / Fairy 01
    alternatives_vi: [CP / Tiên 01]
    status: provisional_non_canon
    canon: false
    rationale: >-
      Ưu tiên giữ nguyên định danh vô tuyến trong ledger; không khai triển CP và
      giữ “01” khi nguồn dùng dạng rút gọn ở p000105. “Tiên 01” là lựa chọn dịch
      nghĩa có thể xét nhưng dễ bị hiểu thành tên hoặc loại sinh vật; chưa có
      quyết định cho phép thay đồng bộ định danh vô tuyến nên không khuyến nghị áp dụng.
recommendations:
  - Translator có lease xử lý B05-C01 đến B05-C03 trước khi coordinator tính lô hoàn tất.
  - Xử lý ba mục nhẹ; mục chú thích cần ghi rõ cách bảo toàn dấu gọi trong phạm vi được phép.
  - Coordinator ghi bảy đề xuất và lựa chọn thay thế vào ledger/handoff, giữ trạng thái non-canon.
  - Sau sửa, đối chiếu lại các dòng liên quan rồi chạy validator và diff-check của pipeline.
risks:
  - Ba lỗi vừa còn mở; báo cáo hoàn tất không đồng nghĩa lô dịch được duyệt hoàn tất.
  - Chỉ kiểm tra package b05; chưa có căn cứ về nội dung chú thích 25 hoặc chuẩn hóa tên Matsusheeta.
  - Tính nhất quán với các lô trước chỉ dựa trên self-check và ledger được giao, không kiểm tra lô khác.
  - Bảy lựa chọn vẫn là đề xuất; không có quyết định canon ảnh hưởng cốt truyện cần dừng trong phạm vi này.
next_action: translator_revision
```

Đã đối chiếu riêng từng dòng về nghĩa, điểm nhìn, sắc thái và markup. Mã đầy đủ của các dòng dưới đây là `YS-LN02/Text/part0032.xhtml/` cộng mã dòng.

| Dòng | Kết quả nghĩa và giọng văn |
| --- | --- |
| p000104 | B05-C01; cần giữ lời đánh giá 203 là đơn vị có thể làm nổi nhiệm vụ, giọng than phiền tự giễu. |
| p000105 | Lời vô tuyến ngắn gọn; lược người nghe không mất thông tin hoặc thêm quan hệ. |
| p000106 | Nghĩa về may mắn, tuyển người và thời điểm trước khi bị đưa sang thế giới này được giữ; B05-C04 về dấu chú thích. |
| p000107 | Giữ bước chuyển từ không hiểu sang hiểu và mức khả thể về xác suất. |
| p000108 | Câu hỏi về tình hình vẫn mở, không đổi thành hỏi địa điểm. |
| p000109 | Giữ quy mô cấp tiểu đoàn, rìa tầm radar, hướng áp sát và hạn cầm chân đến hết giai đoạn ba. |
| p000110 | Lời nhận lệnh đối lập với cơn giận nội tâm; B05-C05 về cách thể hiện giọng chuyên nghiệp. |
| p000111 | Giữ chênh lệch nhiệm vụ và lực lượng hai đại đội, đội hình phân tán và sự hao sức. |
| p000112 | Giữ đối lập sung sức/sân nhà/nguy cơ bị bắn trúng; B05-C02 về loại hỏa lực bị thêm. |
| p000113 | Giữ suy đoán chắc cao về mức căng thẳng tinh thần của đối phương. |
| p000114 | Giữ phủ định nhận định đối phương phục tùng vô tư, không biến thành khinh địch. |
| p000115 | Giữ tiểu đoàn được điều động từ mặt đất lên cản trinh sát. |
| p000116 | Giữ lực lượng tuyển chọn, phản đối hy vọng ngây thơ và nguyên tắc chuẩn bị bi quan. |
| p000117 | Giữ quyền hủy ngay nhiệm vụ trinh sát; không biến thành mệnh lệnh phải hủy. |
| p000118 | Giữ phản ứng ngập ngừng, thấy việc được cấp quyền hủy là thú vị. |
| p000119 | Giữ tính hiếm của quyền hủy và điều kiện rút lui đúng kế hoạch mới hạn chế thêm tổn thất. |
| p000120 | Giữ logic cấp trên có lý nhưng Tanya không rút, cùng hình ảnh tính thực dụng là cái bẫy. |
| p000121 | Giữ ví dụ đường nhựa xuống địa ngục, ý tốt và lựa chọn rẽ qua hoang địa. Đại từ “bạn” mang nghĩa khái quát. |
| p000122 | Lược đại từ hợp lý; vẫn là mong không cần dùng tới lựa chọn vừa nêu. |
| p000123 | Giữ tự khẳng định không phải tay mơ, tư duy kinh tế, huấn luyện, Being X và phép thề về tiến hóa; chỉ tên loài được in nghiêng đúng markup. |
| p000124 | Hai câu hỏi ngắn giữ sự ngạc nhiên và yêu cầu giải thích, không tự thêm xưng hô. |
| p000125 | Giữ thăm dò năng lực đánh chặn và nguy cơ lộ mục đích đánh lừa khi hủy sớm. |
| p000126 | Chuỗi nguyên nhân và nguy cơ vẫn rõ; B05-C03 về thành phần lực lượng và thế cầm cự. |
| p000127 | Giữ lý do dè chừng trao đổi vô tuyến ngay cả khi đã mã hóa. |
| p000128 | Giữ chuyển từ gọi tên Tanya sang nội tâm “mình”, giả định vai ra lệnh, khả năng hy sinh đoạn hậu và tiếng chửi cuối. Không cần thay tên riêng bằng đại từ. |
| p000129 | Giữ so sánh né một tiểu đoàn với bị mọi đơn vị Cộng hòa trên mặt trận truy đuổi. |
| p000130 | Nghĩa phép so sánh đầu tư và lợi nhuận đúng; B05-C06 về chuỗi phủ định. |
| p000131 | Giữ giới hạn bí mật trước khi giai đoạn ba kết thúc, loại bỏ đơn vị đánh chặn rồi tiếp tục nhiệm vụ. |

Self-check đúng về nội tâm “mình”, giới hạn chữ nghiêng và chuỗi quyền hủy–không thể rút–câu giờ đến hết giai đoạn ba. Các nhận xét ấy chưa phát hiện ba lỗi vừa ở trên. Báo cáo không chép câu nguồn, không mở EPUB/PDF, package khác hay nội dung chú thích; không sửa bản dịch, canon hoặc trạng thái pipeline.
