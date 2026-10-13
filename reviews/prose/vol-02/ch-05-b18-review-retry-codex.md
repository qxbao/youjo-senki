# Review retry — vol-02-ch-05-b18-review-retry

Đã kiểm tra hash **trước khi đọc nội dung package**: SHA-256 trong handoff retry gồm đúng 64 ký tự hex, khớp hash tính từ bytes package và handoff batch. Blocker hash của lần review cũ đã được khắc phục. Đã đọc báo cáo blocked để hiểu bối cảnh, rồi đối chiếu độc lập toàn bộ 35 đoạn p000430–p000464 với text/XHTML của package cục bộ, bản dịch, canon, ledger và self-check; không lấy các nhận xét cũ làm kết quả mặc định.

Review hoàn tất, bản dịch còn 9 lỗi vừa và 5 lỗi nhẹ; chưa đủ điều kiện signoff. Một finding về nhấn mạnh bao phủ sáu đoạn, được tính là một finding. Các lựa chọn thuật ngữ bên dưới đều là đề xuất tạm, không nâng thành canon. Không thấy ghi chú riêng của translator tại p000460 trong self-check; cả 35 trường notes đều rỗng. Vì vậy đánh giá trực tiếp câu dịch tại p000460, không suy đoán nội dung một ghi chú chưa được cung cấp.

Chỉ ghi báo cáo này. Không mở EPUB/PDF, không chép câu nguồn vào báo cáo, không sửa bản dịch, canon, ledger, handoff hay self-check. Không tạo graph/đầu ra phụ; quy trình graphify có bước ghi thêm tệp nên không áp dụng trong phạm vi chỉ được ghi một báo cáo. Không chạy validator hoặc diff-check; không commit.

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-05-b18-review-retry
state: done
review_path: reviews/prose/vol-02/ch-05-b18-review-retry-codex.md
files_written: [reviews/prose/vol-02/ch-05-b18-review-retry-codex.md]
validator: not_run
diff_check: not_run
commit: null
signoff: false
inputs_read:
  - AGENTS.md
  - agents/shared.md
  - agents/reviewer.md
  - config/translation-pipeline.yml
  - handoffs/vol-02/ch-05-b18-review-retry.yml
  - handoffs/vol-02/ch-05-b18.yml
  - reviews/prose/vol-02/ch-05-b18-codex.md
  - work/vol-02/batches/ch-05-b18-source.jsonl
  - canon/glossary.yml
  - canon/style-guide.md
  - canon/characters.yml
  - canon/decisions.md
  - canon/glossary-pending.yml
  - work/run-state/pending-terms.yml
  - translations/vol-02/ch-05-b18.jsonl
  - reviews/semantic/vol-02/ch-05-b18-self-check.md
hash_check:
  status: pass
  verified_before_package_content_review: true
  retry_hash_length: 64
  retry_hash_hex64: true
  package_sha256_actual: f32e7fecfce1d77df1322681680ba6cca9c96eeefc28b1ecc4a14b41ba92674c
  retry_handoff_expected: f32e7fecfce1d77df1322681680ba6cca9c96eeefc28b1ecc4a14b41ba92674c
  batch_handoff_expected: f32e7fecfce1d77df1322681680ba6cca9c96eeefc28b1ecc4a14b41ba92674c
  package_matches_retry_handoff: true
  package_matches_batch_handoff: true
  previous_hash_blocker_resolved: true
  canon_reference_hashes_match_batch_handoff: true
  canon_hashes_actual:
    canon/glossary.yml: d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41
    canon/style-guide.md: 64724c03b0b6ca29512cd3cea52fc104042429e96c2c676bbc721cba2243569c
    canon/characters.yml: 354f6573a8343bb94ce0a8cb95325777bd2bbbf2250c6d4efe1563f8cc93f3aa
    canon/decisions.md: 9f173f9c263ac6202bd9988d0b54be460ef993e1a3849cc36c09a667b8bf6044
    canon/glossary-pending.yml: 65458cca57c501b930e3797f84d5c8de2ee2211ac2c09682225e049fd932b3c1
  translation_sha256_actual: 4900bb6b104efff9faff69e2b89d3681cc0b89f551a44d9affceee4703879c9f
  translation_hash_is_snapshot_only: true
  source_sha256_metadata: 3ac53161b6e093ba07203f284a400049cf902a3b0f51c0d3e40200867c13ae0a
  source_metadata_matches_all_package_and_translation_rows: true
  original_epub_hash_recomputed: false
order_check:
  status: pass
  source_units: 35
  translation_units: 35
  exact_expected_id_sequence: true
  source_translation_order_matches: true
  source_word_count_actual: 879
  source_word_count_expected: 879
  method: 'Đếm theo regex của handoff; đối chiếu ID và metadata trực tiếp, không chạy validator.'
counts:
  reviewed_segments: 35
  serious: 0
  moderate: 9
  minor: 5
  total_findings: 14
  translation_findings: 14
  handoff_findings: 0
  missing_emphasis_spans: 6
findings:
  - id: B18R-F01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000438
    issue: 'Tanya tự quy chiếu tôi trong nội tâm, lệch mình ở p000442 và DEC-P01-001.'
    evidence: 'Đoạn không phải thoại; nó bình luận phương án quân sự giữa các mục tổng kết, cùng điểm nhìn với câu hỏi chọn pháp sư ở p000442.'
    resolution: 'Đổi tôi thành mình tại p000438. Giữ tôi trong lời thoại; không áp quy ước Tanya cho Grantz.'
  - id: B18R-F02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000443
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000443
      - YS-LN02/Text/part0026.xhtml/p000451
      - YS-LN02/Text/part0026.xhtml/p000454
      - YS-LN02/Text/part0026.xhtml/p000458
      - YS-LN02/Text/part0026.xhtml/p000461
      - YS-LN02/Text/part0026.xhtml/p000462
    issue: 'Thiếu toàn bộ sáu span nhấn mạnh trong XHTML, trái DEC-P01-002.'
    evidence: 'Mỗi đoạn liệt kê có một phần tử em; tất cả translation đều không có dấu Markdown nhấn mạnh.'
    resolution: 'Dùng *...*: p000443 từ Pháp sư thường được đãi ngộ tốt đến hết đoạn; p000451 chỉ câu Cô ta đúng là đáng sợ; p000454 chỉ Có lẽ mình làm được!; p000458 chỉ câu điều kiện Nếu tôi mắc lỗi...; p000461 chỉ cụm trách nhiệm tập thể; p000462 chỉ hai câu đầu về được nghỉ và ngủ sớm. Giữ phần kể ngoài span; không thêm nghiêng vào các câu nội tâm khác.'
  - id: B18R-F03
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000431
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000431, YS-LN02/Text/part0026.xhtml/p000440]
    issue: 'Thiếu úy của Serebryakov quay lại mapping cũ dù lựa chọn tạm gần nhất b17 đã trung tính hóa cấp úy.'
    evidence: 'Package chỉ nêu Lieutenant. Ledger có các mapping cũ mâu thuẫn; cả translator và reviewer b17 chọn sĩ quan cấp úy Serebryakov khi chưa phân tiểu cấp.'
    resolution: 'Tạm dùng Cô với tôi... ở p000431 để tránh lời gọi quân hàm gượng; dùng Sĩ quan cấp úy Serebryakov ở p000440. Không kết luận nhân vật được thăng/giáng cấp; Grantz tại p000444 có bậc Second rõ nên vẫn dùng thiếu úy ma pháp.'
  - id: B18R-F04
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000456
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000456, YS-LN02/Text/part0026.xhtml/p000463]
    issue: 'Không quân gán nghĩa quân chủng cho Aerial và lệch tên tạm Trên không trong ledger b03.'
    evidence: 'Hai tên ở nguồn có/không có yếu tố Assault; không có căn cứ trong lô để xác lập trực thuộc quân chủng Không quân.'
    resolution: 'Tạm dùng Tiểu đoàn Pháp sư Xung kích Trên không số 203 ở p000456; Tiểu đoàn Pháp sư Trên không số 203 ở p000463. Giữ khác biệt tên dài/tên rút gọn, không thêm Xung kích vào p000463.'
  - id: B18R-F05
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000460
    issue: 'Thường là phe an toàn hơn thêm tần suất, gợi phe phái và làm mờ nhóm tương đối ít đáng lo hơn đối với Grantz.'
    evidence: 'p000460 phân biệt người lấy khả năng của đứa trẻ làm động lực với người xem nhẹ Tanya; p000461 nối sang nỗi lo họ gây chuyện và trách nhiệm tập thể. Đây không phải nhận xét xác suất sống sót của một phe.'
    resolution: 'Tạm dùng Những người nghĩ rằng nếu đứa trẻ bé xíu ấy đương đầu được với chiến tranh thì mình cũng làm được vẫn còn thuộc nhóm ít đáng lo hơn. Phương án literal hơn: ...vẫn còn thuộc nhóm an toàn hơn. Bỏ thường; giữ tính tương đối, không thêm hành vi chống lệnh hoặc nguy cơ chắc chắn. Không có ghi chú translator riêng để xét ngoài câu dịch này.'
  - id: B18R-F06
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000440
    issue: 'Tiến thân qua các cấp bậc chỉ nói thăng cấp, làm mất ý tiến lên từ hàng ngũ binh lính.'
    evidence: 'Đường trưởng thành từ hàng ngũ là căn cứ cho khả năng hỗ trợ lính mới, không phải chỉ việc sĩ quan từng trải qua các cấp quân hàm.'
    resolution: 'Tạm dùng Sĩ quan cấp úy Serebryakov cùng những người khác trưởng thành từ hàng ngũ binh lính có lẽ sẽ làm tốt việc đó. Giữ phỏng đoán; không bổ sung lịch sử nhập ngũ/thăng cấp cụ thể.'
  - id: B18R-F07
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000451
    issue: 'Học viên năm hai tự xác định niên khóa từ nhãn second-class student.'
    evidence: 'Package không giải thích nhãn này là năm học, lớp hay hạng; canon chưa xác lập hệ phân loại học viện.'
    resolution: 'Tạm dùng một học viên thuộc lớp thứ hai, giữ nhãn literal với độ tin cậy thấp. Năm hai chỉ là phương án thay thế khi có thêm chứng cứ; không đổi sang hạng hai với hàm ý năng lực kém. Coordinator lưu bất định, không dừng chờ người dùng.'
  - id: B18R-F08
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000453
    issue: 'Trước khi nhận nhiệm vụ thu hẹp assignment thành nhiệm vụ thay vì việc phân công sau huấn luyện.'
    evidence: 'Chuỗi p000452–453 nói về phân về đơn vị huấn luyện, tái huấn luyện quân bổ sung và làm quen tiền tuyến trước việc phân công; chưa nêu một nhiệm vụ cụ thể.'
    resolution: 'Dùng trước khi được phân công; không tự nêu đơn vị đích hoặc nhiệm vụ tác chiến.'
  - id: B18R-F09
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000431
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000431, YS-LN02/Text/part0026.xhtml/p000440, YS-LN02/Text/part0026.xhtml/p000446, YS-LN02/Text/part0026.xhtml/p000447]
    issue: 'Tự thêm sông vào Rhine trong các ngữ cảnh chiến trường/khu vực điều quân.'
    evidence: 'p000447 xác định khu vực Rhine trên đường ra tiền tuyến; p000455 gọi rõ mặt trận. Ledger b03/b08 đã giữ địa danh không tự phân loại hoặc dùng mặt trận khi ngữ cảnh xác lập.'
    resolution: 'p000431/p000440/p000446 dùng mặt trận Rhine theo ngữ cảnh quân sự; p000447 dùng khu vực Rhine. Không suy vị trí chiến đấu ngay trên sông hoặc đổi tên riêng.'
  - id: B18R-F10
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000452
    issue: 'Đơn vị huấn luyện viên gượng và lệch cách gọi chức năng trong ledger b10/b12/b16.'
    evidence: 'Đoạn nói đơn vị nhận quân để huấn luyện lại, không xác lập một biên chế gồm toàn huấn luyện viên.'
    resolution: 'Dùng đơn vị huấn luyện; phương án khác: đơn vị phụ trách huấn luyện.'
  - id: B18R-F11
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000450
    issue: 'Lính già dễ nhấn tuổi tác thay vì kinh nghiệm của old stagers.'
    evidence: 'Đoạn đối chiếu tập quán của người quen đi tàu ra mặt trận với Grantz; không nêu tuổi.'
    resolution: 'Cân nhắc những người lính lâu năm hoặc lính kỳ cựu; giữ ba cách giết thời gian.'
  - id: B18R-F12
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000458
    issue: 'Kiêm cố vấn làm phẳng sắc thái oái oăm trong lời than của Grantz.'
    evidence: 'Việc người huấn luyện đáng sợ ấy lại còn là cố vấn làm tăng cảm giác bị đe dọa, nối với câu muốn khóc ở p000459.'
    resolution: 'Cân nhắc ...người huấn luyện ấy, oái oăm thay, lại còn là cố vấn của tôi. Giữ câu đầu là điều Grantz sẽ tin nếu nghe kể, không biến chuyện làm hại học viên thành sự kiện đã được xác nhận.'
  - id: B18R-F13
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000445
    issue: 'Lưỡi anh không đến nỗi chê bai là kết hợp từ gượng.'
    evidence: 'Đoạn chỉ nhận xét món ăn đáp ứng cơn đói và chấp nhận được về vị, trước khi chuyển sang sự chán nản do bị điều ra chiến trường.'
    resolution: 'Cân nhắc Ít ra nó cũng làm dịu cơn đói, và cũng không đến nỗi khó nuốt. Không đổi thành thức ăn ngon hoặc khiến anh hết chán nản.'
  - id: B18R-F14
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000444
    issue: 'Mới được phong sĩ quan bỏ sắc thái cuối cùng cũng của việc nhận quân hàm.'
    evidence: 'Nguồn vừa đánh dấu mới nhận quân hàm vừa gợi sự chờ đợi đến thời điểm đó; bản dịch chỉ giữ tính mới.'
    resolution: 'Cân nhắc người cuối cùng cũng vừa được phong sĩ quan; giữ tên và bậc quân hàm, không tự thêm tuổi hoặc thời gian đào tạo.'
unresolved_findings: [B18R-F01, B18R-F02, B18R-F03, B18R-F04, B18R-F05, B18R-F06, B18R-F07, B18R-F08, B18R-F09, B18R-F10, B18R-F11, B18R-F12, B18R-F13, B18R-F14]
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000430
  - YS-LN02/Text/part0026.xhtml/p000431
  - YS-LN02/Text/part0026.xhtml/p000432
  - YS-LN02/Text/part0026.xhtml/p000433
  - YS-LN02/Text/part0026.xhtml/p000434
  - YS-LN02/Text/part0026.xhtml/p000435
  - YS-LN02/Text/part0026.xhtml/p000436
  - YS-LN02/Text/part0026.xhtml/p000437
  - YS-LN02/Text/part0026.xhtml/p000438
  - YS-LN02/Text/part0026.xhtml/p000439
  - YS-LN02/Text/part0026.xhtml/p000440
  - YS-LN02/Text/part0026.xhtml/p000441
  - YS-LN02/Text/part0026.xhtml/p000442
  - YS-LN02/Text/part0026.xhtml/p000443
  - YS-LN02/Text/part0026.xhtml/p000444
  - YS-LN02/Text/part0026.xhtml/p000445
  - YS-LN02/Text/part0026.xhtml/p000446
  - YS-LN02/Text/part0026.xhtml/p000447
  - YS-LN02/Text/part0026.xhtml/p000448
  - YS-LN02/Text/part0026.xhtml/p000449
  - YS-LN02/Text/part0026.xhtml/p000450
  - YS-LN02/Text/part0026.xhtml/p000451
  - YS-LN02/Text/part0026.xhtml/p000452
  - YS-LN02/Text/part0026.xhtml/p000453
  - YS-LN02/Text/part0026.xhtml/p000454
  - YS-LN02/Text/part0026.xhtml/p000455
  - YS-LN02/Text/part0026.xhtml/p000456
  - YS-LN02/Text/part0026.xhtml/p000457
  - YS-LN02/Text/part0026.xhtml/p000458
  - YS-LN02/Text/part0026.xhtml/p000459
  - YS-LN02/Text/part0026.xhtml/p000460
  - YS-LN02/Text/part0026.xhtml/p000461
  - YS-LN02/Text/part0026.xhtml/p000462
  - YS-LN02/Text/part0026.xhtml/p000463
  - YS-LN02/Text/part0026.xhtml/p000464
coverage:
  p000430: 'Giữ hai nguyên nhân lộ tiếp cận, phủ định và sắc thái tên ngốc; tín hiệu mana phù hợp lựa chọn tạm b17.'
  p000431: 'Giữ ngán ngẩm, hai người cùng chứng kiến và câu hỏi xử lý lính mới; F03/F09.'
  p000432: 'Giữ điều kiện nếu cần, lời gọi Thiếu tá và nỗ lực hỗ trợ để khỏi phải xử lý; tôi là đại từ thoại.'
  p000433: 'Giữ hành động điểm lại ý kiến, giọng thoại ngắn.'
  p000434: 'Giữ tổng kết các kết luận hợp lý nhất; không có em để thêm chữ nghiêng.'
  p000435: 'Giữ số thứ tự và mức làm mọi cách tránh giao chiến.'
  p000436: 'Giữ bình luận ngắn về hòa bình và không phản đối, hợp giọng Tanya.'
  p000437: 'Giữ đơn vị mạnh nhất, không đổi thành đông nhất.'
  p000438: 'Giữ khó chịu nhưng chấp nhận sự thận trọng quân sự; F01.'
  p000439: 'Giữ điều kiện chưa bị phát hiện, khả năng tiếp cận và nguy cơ rút lui.'
  p000440: 'Giữ kế hoạch có điều kiện, tiến quân/rút lui, sĩ quan và hạ sĩ quan hỗ trợ; F03/F06/F09. Không coi hẳn sẽ là cam kết chắc chắn.'
  p000441: 'Giữ người nói sẽ thông báo kế hoạch; tôi trong thoại phù hợp.'
  p000442: 'Giữ câu hỏi chọn pháp sư mới, mình và ví von dã ngoại; không thêm chữ nghiêng.'
  p000443: 'Giữ khẩu phần, hậu phương/tiền tuyến, nghe kể về Đại quân và phỏng đoán hậu cần; điểm nhìn Grantz được xác nhận ở p000444; F02.'
  p000444: 'Giữ tên Warren Grantz, bậc thiếu úy ma pháp, ăn nhanh và so sánh khẩu phần thao trường; F14.'
  p000445: 'Giữ ăn được nhưng vẫn chán nản mấy ngày do bị điều tới nơi giao tranh ác liệt nhất; F13.'
  p000446: 'Giữ hồi tưởng run vì phấn khích, mong lập chiến công và thành anh hùng; F09.'
  p000447: 'Giữ háo hức tắt dần khi tàu tới gần khu vực chiến trường; F09.'
  p000448: 'Giữ cảnh hố pháo/cháy/xám, mùi hăng, tinh thần sa sút và có lẽ pháo của Đế quốc; không xác nhận nguồn tiếng pháo.'
  p000449: 'Giữ bồn chồn trước lúc tự nhận ra và nhìn thấy đồng đội cũng lo âu.'
  p000450: 'Giữ tin đồn, ngủ/chơi bài, chợp mắt xen trò chuyện và lời đồn từng biết; F11.'
  p000451: 'Giữ tính lời đồn, lời đánh giá đáng sợ và trình diện Bộ chỉ huy; F02/F07. Cô ta thuộc điểm nhìn Grantz.'
  p000452: 'Giữ việc nghe thông báo phân về đơn vị và cảm giác nhẹ nhõm; F10.'
  p000453: 'Giữ tái huấn luyện với tư cách quân bổ sung và làm quen tiền tuyến; F08.'
  p000454: 'Giữ có lẽ, dấu cảm thán và ý nghĩ cách đó vài ngày; F02.'
  p000455: 'Giữ lời chào quân nhân và mặt trận Rhine; các anh là đề xuất thoại tại chỗ.'
  p000456: 'Giữ điều kiện quỷ dữ, người huấn luyện là chỉ huy, Thiếu tá von Degurechaff; chuyển sang lời kể ngôi thứ nhất của Grantz; F04.'
  p000457: 'Giữ ba nhịp ngắn, giòi bọ và vẻ khát máu như cảm nhận; cô ta không phải trần thuật trung tính về Tanya.'
  p000458: 'Giữ điều Grantz sẽ tin nếu nghe kể, điều kiện mắc lỗi và nỗi sợ chủ quan; F02/F12.'
  p000459: 'Giữ muốn khóc và dấu lửng; nguồn không có em.'
  p000460: 'Giữ Grantz là người duy nhất qua học viện và hai phản ứng với lời đồn; F05 sửa so sánh nhóm tương đối ít đáng lo, không dựng phe phái.'
  p000461: 'Giữ lo về điều người xem thường Tanya có thể làm, đau bụng và ghét trách nhiệm tập thể; F02. Không thêm hình phạt cụ thể.'
  p000462: 'Giữ tối nay được nghỉ, ý định ngủ sớm và sự việc xảy ra ngay khi nghĩ thế; F02.'
  p000463: 'Giữ bị triệu tập, tập hợp theo trung đội, phòng hội ý và hạn ba phút; F04.'
  p000464: 'Giữ hai mệnh lệnh cấp bách, ngắn và trực tiếp.'
pending_terms_policy: 'Tất cả khuyến nghị sau là pending/non-canon. Coordinator ghi ledger/handoff, người giữ quyền sửa áp dụng; reviewer không sửa ledger.'
pending_terms: []
term_recommendations:
  - source_term: mana signal
    proposed_vi: tín hiệu mana
    alternatives_vi: [dấu hiệu mana, tín hiệu ma lực]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000430]
    status: pending
    rationale: 'Theo b17 và cách giữ mana trong ledger; không đồng nhất với tín hiệu cầu cứu. Ma lực dễ hiểu nhưng cần thống nhất trước khi thay.'
  - source_term: Lieutenant Serebryakov
    proposed_vi: 'Cô trong câu gọi p000431; sĩ quan cấp úy Serebryakov ở p000440'
    alternatives_vi: [Úy Serebryakov, Trung úy Serebryakov, Thiếu úy Serebryakov]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000431, YS-LN02/Text/part0026.xhtml/p000440]
    status: pending
    confidence: low_for_exact_rank
    rationale: 'Theo lựa chọn trung tính gần nhất b17; mapping cũ mâu thuẫn. Cô là lựa chọn thoại hiện có, không quyết định canon về giới/quan hệ.'
  - source_term: Magic Second Lieutenant
    proposed_vi: thiếu úy ma pháp
    alternatives_vi: [thiếu úy pháp sư]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000444]
    status: pending
    rationale: 'Bậc Second được phân rõ; kế thừa chapter1_b01. Pháp sư gần cách gọi người hơn nhưng chưa thay cấu trúc danh xưng thống nhất.'
  - source_term: Major von Degurechaff
    proposed_vi: Thiếu tá von Degurechaff
    alternatives_vi: [Major von Degurechaff]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000432, YS-LN02/Text/part0026.xhtml/p000456]
    status: pending
    rationale: 'Giữ ánh xạ Major ở b17, tên von Degurechaff nguyên dạng; không thêm Magic khi lần nguồn chỉ nêu Major.'
  - source_term: 203rd Aerial Mage Assault Battalion
    proposed_vi: Tiểu đoàn Pháp sư Xung kích Trên không số 203
    alternatives_vi: [Tiểu đoàn Pháp sư Xung kích Không quân 203]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000456]
    status: pending
    rationale: 'Kế thừa Trên không b03, giữ Assault; phương án Không quân có nguy cơ gán trực thuộc quân chủng.'
  - source_term: 203rd Aerial Mage Battalion
    proposed_vi: Tiểu đoàn Pháp sư Trên không số 203
    alternatives_vi: [Tiểu đoàn Pháp sư Bay số 203, Tiểu đoàn Pháp sư Không quân 203]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000463]
    status: pending
    rationale: 'Theo tên tạm b03; Bay kém tự nhiên, Không quân dễ gán quân chủng. Không tự thêm Xung kích.'
  - source_term: Great Army
    proposed_vi: Đại quân
    alternatives_vi: [Great Army]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000443]
    status: pending
    rationale: 'Giữ đề xuất b08; không đổi thành cấp biên chế cụ thể khi nguồn lô này chưa giải thích.'
  - source_term: Logistics
    proposed_vi: bộ phận Hậu cần
    alternatives_vi: [phía Hậu cần, bộ phận hậu cần]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000443]
    status: pending
    rationale: 'Tương thích các lựa chọn chức năng trong ledger và self-check; không nâng thành Cục/Bộ. Viết hoa vẫn là đề xuất, không khẳng định tên cơ quan.'
  - source_term: instructor unit / instructor / advisor
    proposed_vi: đơn vị huấn luyện / người huấn luyện / cố vấn
    alternatives_vi: [đơn vị phụ trách huấn luyện / huấn luyện viên / người hướng dẫn]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000452, YS-LN02/Text/part0026.xhtml/p000456, YS-LN02/Text/part0026.xhtml/p000458]
    status: pending
    rationale: 'Đơn vị theo chức năng b10/b12/b16; phân biệt người huấn luyện với vai trò cố vấn, giữ sắc thái oái oăm khi một người kiêm hai vai trò.'
  - source_term: second-class student
    proposed_vi: học viên thuộc lớp thứ hai
    alternatives_vi: [học viên lớp hai, học viên năm hai, học viên hạng hai]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000451]
    status: pending
    confidence: low
    rationale: 'Giữ nhãn literal, chưa xác lập niên khóa hay phân hạng. Năm hai cần chứng cứ; hạng hai dễ gợi chất lượng thấp. Bất định cần coordinator ghi ledger.'
  - source_term: picnic
    proposed_vi: dã ngoại
    alternatives_vi: [chuyến đi chơi]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000442]
    status: pending
    rationale: 'Giữ hình ảnh mỉa mai trong kế hoạch tác chiến; đi chơi khẩu ngữ hơn nhưng loãng hình ảnh. Không biến thành tên nhiệm vụ.'
  - source_term: collective responsibility
    proposed_vi: trách nhiệm tập thể
    alternatives_vi: [trách nhiệm chung, liên đới chịu trách nhiệm]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000461]
    status: pending
    rationale: 'Giữ thuật ngữ và đúng span nhấn mạnh; không suy thành một hình phạt tập thể cụ thể.'
  - source_term: railway gun
    proposed_vi: pháo đường sắt
    alternatives_vi: [pháo đặt trên đường sắt]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000448]
    status: pending
    rationale: 'Theo b10, gọn và không thêm cơ chế/cỡ nòng; giữ có lẽ khi Grantz nhận diện.'
  - source_term: Rhine / Rhine Command / Rhine front
    proposed_vi: 'Rhine; mặt trận Rhine trong ngữ cảnh chiến đấu; khu vực Rhine ở p000447; Bộ chỉ huy Rhine ở p000451/p000453'
    alternatives_vi: [chiến tuyến Rhine, bộ chỉ huy mặt trận Rhine]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000431, YS-LN02/Text/part0026.xhtml/p000440, YS-LN02/Text/part0026.xhtml/p000446, YS-LN02/Text/part0026.xhtml/p000447, YS-LN02/Text/part0026.xhtml/p000451, YS-LN02/Text/part0026.xhtml/p000453, YS-LN02/Text/part0026.xhtml/p000455]
    status: pending
    rationale: 'Theo b03/b08, không thêm sông. Bộ chỉ huy là lựa chọn chức năng, tên/chữ hoa chưa canon; không tự định cấp tổ chức.'
  - source_term: replacement / replacements
    proposed_vi: quân bổ sung
    alternatives_vi: [quân thay thế, lính thay thế]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000453, YS-LN02/Text/part0026.xhtml/p000460]
    status: pending
    rationale: 'Giữ cách dùng nhất quán trong lô, là phương án thay thế được b15 ghi nhận; quân thay thế gần nhãn nguồn hơn và có thể thống nhất ở lượt sửa. Không hiểu là tăng viện hoặc chỉ thay người tử trận; không đồng nhất mọi người với tân binh.'
  - source_term: Warren Grantz / Cadet Degurechaff / NCOs
    proposed_vi: Warren Grantz / Học viên Degurechaff / hạ sĩ quan
    alternatives_vi: [Grantz khi gọi ngắn / học viên sĩ quan Degurechaff / NCO]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000440, YS-LN02/Text/part0026.xhtml/p000444, YS-LN02/Text/part0026.xhtml/p000450, YS-LN02/Text/part0026.xhtml/p000451]
    status: pending
    rationale: 'Giữ tên nguyên dạng và vai trò ở thời điểm lời đồn; không tự thêm von vào nhãn Cadet của nguồn. Hạ sĩ quan giữ khác biệt với sĩ quan, không suy quân hàm cá nhân.'
  - source_term: pronoun choices
    proposed_vi: 'Tanya mình trong nội tâm p000438/p000442; tôi trong thoại. Grantz anh ở trần thuật, mình trong suy nghĩ p000443/p000454, tôi/chúng tôi khi chuyển ngôi thứ nhất p000456–463; cô ta khi Grantz đánh giá Tanya. Các anh ở lời chào p000455.'
    alternatives_vi: ['Lược đại từ khi rõ chủ thể; dùng mình cho suy nghĩ trực tiếp Grantz nếu thống nhất toàn chương.']
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000431, YS-LN02/Text/part0026.xhtml/p000432, YS-LN02/Text/part0026.xhtml/p000438, YS-LN02/Text/part0026.xhtml/p000441, YS-LN02/Text/part0026.xhtml/p000442, YS-LN02/Text/part0026.xhtml/p000443, YS-LN02/Text/part0026.xhtml/p000444, YS-LN02/Text/part0026.xhtml/p000451, YS-LN02/Text/part0026.xhtml/p000454, YS-LN02/Text/part0026.xhtml/p000455, YS-LN02/Text/part0026.xhtml/p000456, YS-LN02/Text/part0026.xhtml/p000457, YS-LN02/Text/part0026.xhtml/p000458, YS-LN02/Text/part0026.xhtml/p000460, YS-LN02/Text/part0026.xhtml/p000461, YS-LN02/Text/part0026.xhtml/p000462, YS-LN02/Text/part0026.xhtml/p000463]
    status: pending
    rationale: 'Phân biệt điểm nhìn và ngôi kể thay đổi trong package; không áp nó/mình của Tanya cho mọi nhân vật. Các lựa chọn ngoài phạm vi DEC-P01-001 vẫn tạm, không xác lập tuổi/quan hệ.'
risks:
  - 'Không còn blocker hash đầu vào retry; đây là hoàn tất review, không phải công nhận batch hoàn tất.'
  - 'Chín lỗi vừa còn mở, gồm sáu span nhấn mạnh; người giữ quyền sửa cần xử lý rồi được review lại.'
  - 'Bậc cụ thể Serebryakov và hệ phân lớp học viện chưa đủ chứng cứ; dùng phương án trung tính tạm, coordinator ghi bất định vào ledger.'
  - 'Không có ghi chú riêng p000460 trong các đầu vào; kết luận dựa trên câu dịch và ngữ cảnh p000461.'
next_action: 'Coordinator tiếp nhận báo cáo, ghi các lựa chọn tạm và bất định vào ledger/handoff, giao người giữ quyền sửa xử lý findings; sau đó chạy validator/diff-check và review lại. Reviewer dừng sau báo cáo, không commit.'
```
