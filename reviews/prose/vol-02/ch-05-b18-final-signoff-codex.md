# Final signoff — vol-02-ch-05-b18-final-signoff

**Chưa duyệt bản dịch đã lưu:** còn 2 lỗi vừa, không có lỗi nghiêm trọng hoặc nhẹ. Đã mở lại JSONL và self-check trên đĩa, đối chiếu độc lập đủ 35 đoạn với text/XHTML trong package. Trong 14 finding của retry, 13 đã xử lý đầy đủ; B18R-F03 mới xử lý một phần. Phát hiện thêm một lỗi nghĩa tại p000458, vốn chưa được retry nêu riêng. Sáu span nhấn mạnh đều đúng và không có span thừa.

Self-check nói p000431 đã dùng “Cô với tôi”, nhưng JSONL thực tế vẫn mở đầu bằng “Thiếu úy, cô với tôi”. Kết luận này dựa trên tệp đã lưu, không dựa vào lời xác nhận sửa. Pending terms vẫn không chặn signoff và không trở thành canon; lỗi p000431 là việc còn gán tiểu cấp khi nguồn chưa phân biệt, không phải việc thuật ngữ còn pending.

Đã đọc AGENTS.md, agents/shared.md, agents/reviewer.md, config/translation-pipeline.yml; handoff batch, review ban đầu, review retry, review-fixes và final-signoff; báo cáo retry, báo cáo cũ để hiểu blocker đã được thay thế; bản dịch, self-check, package; toàn bộ các tệp canon và mục khuyến nghị B18 trong pending ledger. Không mở EPUB/PDF. Không chép câu nguồn vào báo cáo. Chỉ ghi báo cáo này; không sửa bất kỳ đầu vào nào.

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-05-b18-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-05-b18-final-signoff-codex.md
files_written: [reviews/prose/vol-02/ch-05-b18-final-signoff-codex.md]
validator: not_run
diff_check: not_run
commit: null
signoff: false
signoff_status: changes_required
saved_verification:
  translation_reopened_from_disk: true
  self_check_reopened_from_disk: true
  all_segments_compared_with_package_text_and_xhtml: true
  all_retry_findings_independently_checked: true
  all_emphasis_spans_independently_checked: true
  self_check_fully_agrees_with_saved_translation: false
  self_check_discrepancy: 'p000431 vẫn có lời gọi Thiếu úy; self-check mô tả đã trung tính hóa.'
hash_check:
  status: pass
  expected_package_hash_hex64: true
  package_sha256_actual: f32e7fecfce1d77df1322681680ba6cca9c96eeefc28b1ecc4a14b41ba92674c
  package_matches_final_batch_retry_and_fix_handoffs: true
  translation_sha256_actual: 71b5fca640d70bb1b3bece72e3cc056ef976b64dc9e35a371fbfe178dd4dc2e6
  self_check_sha256_actual: 3f6c4a255cb068677838214cf9ebb346ecd9a98bd1da11f0ba897382972a4407
  saved_hashes_are_review_snapshots: true
  source_sha256_metadata: 3ac53161b6e093ba07203f284a400049cf902a3b0f51c0d3e40200867c13ae0a
  all_package_and_translation_source_metadata_match: true
  all_translation_glossary_version_metadata_match_batch: true
  all_five_canon_reference_hashes_match_batch: true
  original_epub_hash_recomputed: false
order_check:
  status: pass
  source_units: 35
  translation_units: 35
  unique_translation_ids: 35
  segment_id_start: YS-LN02/Text/part0026.xhtml/p000430
  segment_id_end: YS-LN02/Text/part0026.xhtml/p000464
  exact_expected_contiguous_id_sequence: true
  source_translation_order_matches: true
  source_word_count_actual: 879
  source_word_count_expected: 879
  method: 'Đọc JSONL, đối chiếu ID/metadata và đếm theo regex handoff; không chạy validator.'
counts:
  reviewed_segments: 35
  prior_findings_checked: 14
  prior_findings_fully_resolved: 13
  prior_findings_partially_resolved: 1
  prior_findings_unresolved: 1
  serious: 0
  moderate: 2
  minor: 0
  total_findings: 2
  new_findings: 1
  source_emphasis_spans: 6
  saved_translation_emphasis_spans: 6
  correctly_scoped_emphasis_spans: 6
  missing_emphasis_spans: 0
  extra_emphasis_spans: 0
findings:
  - id: B18R-F03
    severity: moderate
    status: partially_resolved
    segment_id: YS-LN02/Text/part0026.xhtml/p000431
    related_segment_ids: [YS-LN02/Text/part0026.xhtml/p000440]
    issue: 'Lời gọi Thiếu úy còn nguyên ở p000431, tiếp tục gán tiểu cấp chưa được package xác định.'
    evidence: 'Nguồn chỉ có nhãn Lieutenant; fix handoff và ledger chọn cách gọi trung tính. JSONL đã lưu vẫn chứa Thiếu úy, cô với tôi, dù p000440 đã đổi sang Sĩ quan cấp úy Serebryakov.'
    resolution: 'Bỏ lời gọi Thiếu úy để câu mở bằng Cô với tôi như handoff; giữ phần còn lại. Không suy thăng/giáng cấp và không thay thiếu úy ma pháp ở p000444, nơi Second được nêu rõ.'
  - id: B18FS-F01
    severity: moderate
    status: open
    segment_id: YS-LN02/Text/part0026.xhtml/p000458
    issue: 'Từng định giết hạ một hành vi đã thử thực hiện xuống mức ý định.'
    evidence: 'Trong mệnh đề mà Grantz nói mình sẽ tin, package dùng hành vi cố thực hiện việc giết hoặc đập vỡ sọ học viên. Bản dịch giữ khung giả định nhưng chỉ diễn đạt định giết, làm yếu nội dung bạo lực được hình dung. Đây không phải sự kiện được người kể xác nhận.'
    resolution: 'Đổi từng định giết thành từng tìm cách giết hoặc từng cố giết. Giữ khung Tôi tin ngay nếu có người bảo, đối tượng học viên khóa dưới, nhánh đập vỡ sọ và span nhấn mạnh của câu kế tiếp; không biến chuyện giả định thành sự kiện có thật.'
unresolved_findings: [B18R-F03, B18FS-F01]
pending_terms_policy: temporary_consistent_not_canon_nonblocking
pending_terms: []
term_recommendations:
  - source_term: Lieutenant Serebryakov
    proposed_vi: 'Cô với tôi ở p000431; sĩ quan cấp úy Serebryakov ở p000440'
    alternatives_vi: [Trung úy Serebryakov]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000431, YS-LN02/Text/part0026.xhtml/p000440]
    status: pending
    rationale: 'Kế thừa lựa chọn tạm trong fix handoff/ledger, tránh gán tiểu cấp; phương án thay thế cần thêm chứng cứ. Không nâng thành canon.'
risks:
  - 'Self-check chưa phản ánh đúng lời gọi còn sót ở p000431; không dùng self-check làm chứng cứ thay cho JSONL.'
  - 'Nhãn học viên thuộc lớp thứ hai vẫn có độ tin cậy thấp; không suy niên khóa hoặc thứ hạng, không chặn vì pending.'
next_action: 'Coordinator giao người giữ quyền sửa xử lý hai finding và đồng bộ self-check, sau đó thực hiện validator/diff-check và review lại bản đã lưu. Reviewer không sửa hoặc commit.'
```

Đối chiếu toàn bộ B18R-F01–F14 dưới đây dùng mã đoạn rút gọn; tiền tố chung là `YS-LN02/Text/part0026.xhtml/`.

| Finding | Đoạn | Kết quả trên bản đã lưu |
| --- | --- | --- |
| B18R-F01 | p000438 | Đã xử lý: Tanya tự quy chiếu “mình”; thoại vẫn dùng “tôi”, không áp quy ước Tanya cho Grantz. |
| B18R-F02 | p000443, p000451, p000454, p000458, p000461, p000462 | Đã xử lý: đủ sáu span, đúng phạm vi XHTML; không thêm nhấn mạnh ở 29 đoạn còn lại. |
| B18R-F03 | p000431, p000440 | Một phần: p000440 trung tính đúng; p000431 vẫn còn “Thiếu úy”. |
| B18R-F04 | p000456, p000463 | Đã xử lý: tên dài có “Xung kích Trên không số 203”; tên ngắn chỉ “Trên không số 203”, không gán quân chủng. |
| B18R-F05 | p000460 | Đã xử lý: “có lẽ là nhóm ít đáng lo hơn”, bỏ tần suất và phe phái; giữ so sánh tương đối trong mạch lo trách nhiệm tập thể. |
| B18R-F06 | p000440 | Đã xử lý: “trưởng thành từ hàng ngũ” thay cho chỉ thăng qua các cấp; giữ tính phỏng đoán, không thêm lịch sử phục vụ. |
| B18R-F07 | p000451 | Đã xử lý: “học viên thuộc lớp thứ hai”, nhãn literal tạm; không gán năm học hoặc năng lực. |
| B18R-F08 | p000453 | Đã xử lý: “trước khi được phân công”; giữ tái huấn luyện quân bổ sung và làm quen tiền tuyến. |
| B18R-F09 | p000431, p000440, p000446, p000447 | Đã xử lý: ba ngữ cảnh quân sự dùng “mặt trận Rhine”, p000447 dùng “khu vực Rhine”; không thêm sông. |
| B18R-F10 | p000452 | Đã xử lý: “đơn vị huấn luyện”; giữ cảm giác nhẹ nhõm khi nghe tin phân về đơn vị. |
| B18R-F11 | p000450 | Đã xử lý: “những người lính lâu năm”; giữ ngủ, chơi bài và truyền tin đồn. |
| B18R-F12 | p000458 | Đã xử lý sắc thái riêng của finding: “oái oăm thay, lại còn là cố vấn”; khung giả định vẫn còn. Lỗi mức hành động là B18FS-F01 riêng. |
| B18R-F13 | p000445 | Đã xử lý: làm dịu cơn đói, không đến nỗi khó nuốt; không biến thành khen ngon tuyệt hoặc hết chán nản. |
| B18R-F14 | p000444 | Đã xử lý: giữ “cuối cùng cũng vừa được phong sĩ quan”, không thêm tuổi hoặc thời lượng đào tạo. |

Kiểm tra phạm vi nhấn mạnh theo phần tử `em` của package, không dựa trên self-check:

| Đoạn | Phạm vi tiếng Việt đã xác minh | Phần ngoài span |
| --- | --- | --- |
| p000443 | Từ câu về đãi ngộ pháp sư đến hết đoạn, bao gồm suy nghĩ hậu phương/tiền tuyến và Hậu cần | Ba câu thông tin khẩu phần trước đó không nghiêng. |
| p000451 | Chỉ “Cô ta đúng là đáng sợ.” | Lời đồn và lời kể trình diện không nghiêng. |
| p000454 | Chỉ “Có lẽ mình làm được!” | Câu kể về vài ngày trước không nghiêng. |
| p000458 | Chỉ câu điều kiện về mắc lỗi trên chiến trường và bị giết | Câu giả định đầu và cảm giác bị đe dọa/cố vấn không nghiêng. |
| p000461 | Chỉ “trách nhiệm tập thể” | Hai câu bao quanh và dấu câu ngoài cụm không bị mở rộng nhấn mạnh. |
| p000462 | Hai câu đầu về tối nay được nghỉ và ngủ sớm | Câu kể sự việc xảy ra không nghiêng. |

Rà soát mới bao phủ cả 35 đoạn: p000430–442 giữ điều kiện tiếp cận/rút lui, hai nguyên nhân lộ vị trí, kế hoạch có phỏng đoán và điểm nhìn Tanya; p000443–454 giữ chuyển điểm nhìn Grantz, khẩu phần, hồi tưởng phấn khích rồi suy sụp, lời đồn và trình tự phân công/huấn luyện; p000455–464 giữ chuyển ngôi thứ nhất, cảm nhận chủ quan về người huấn luyện, hai nhóm phản ứng với lời đồn, trách nhiệm tập thể, nghỉ tối bị gián đoạn và lệnh tập hợp theo trung đội trong ba phút. Ngoài hai finding nêu trên, không phát hiện thêm lỗi nghiêm trọng, vừa hoặc nhẹ có căn cứ. Đây là kết quả review; validator và diff-check vẫn `not_run`, commit vẫn `null`.
