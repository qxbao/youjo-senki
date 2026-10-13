# Sign-off sau sửa — vol-02-ch-05-b04

Chấp nhận chín sửa đổi B04-F01–F09 trong bản dịch hiện tại. Không phát hiện lỗi nghiêm trọng/vừa mới khi đối chiếu 27 đoạn p000076–p000102, gồm các đoạn đã sửa và ngữ cảnh trong cùng b04. B04-PENDING-MAP được xác nhận đóng về đối sánh: đủ bốn ID chính thức và năm ID đề xuất bổ sung, đúng mục ledger, mã đoạn và lựa chọn đang áp dụng. Cả chín thuật ngữ vẫn pending, không được nâng thành canon.

Sign-off này xác nhận nghĩa/văn phong và đối sánh pending của bản hiện tại; không xác nhận batch đã hoàn tất pipeline hoặc đã commit. Validator/diff_check của lượt này không chạy. Kết quả pass trong handoff là kết quả translator đã báo, không phải kiểm tra do reviewer thực hiện.

## Phạm vi và đầu vào

- `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, `handoffs/vol-02/ch-05-b04.yml` và quy tắc `AGENTS.md`.
- Hai báo cáo: `reviews/prose/vol-02/ch-05-b04-codex.md`, `reviews/prose/vol-02/ch-05-b04-pending-terms-codex.md`.
- Năm canon reference trong handoff: `canon/glossary.yml`, `canon/style-guide.md`, `canon/characters.yml`, `canon/decisions.md`, `canon/glossary-pending.yml`.
- Chỉ hai mục ledger: `work/run-state/pending-terms.yml#chapter5_b04_translation_proposals` và `#chapter5_b04_reviewer_suggestions`; không sử dụng mục b03 hay mục khác.
- Package `work/vol-02/batches/ch-05-b04-source.jsonl` và bản dịch `translations/vol-02/ch-05-b04.jsonl`.

Không đọc nội dung source/translation/review của batch khác, không mở EPUB/PDF, không chạy worker. Chỉ ghi báo cáo này; không sửa translation, handoff, ledger, canon hay run-state. Không chạy graphify vì quy trình của skill vượt phạm vi đọc/ghi được giao.

Package SHA-256 khớp handoff: `2a85f82ace6d10aef1b96b241e8cbbfa48db1185ee976355b51b7c9d4bebe63b`. Cả năm hash canon reference cũng khớp. Package và bản dịch đều có đủ 27 mã theo đúng thứ tự, không thiếu/trùng; metadata source hash và glossary version khớp handoff. Nhấn mạnh ở p000076 giữ đúng phạm vi; không thêm nhấn mạnh ở đoạn khác. Đây là kiểm tra đầu vào trực tiếp, không thay validator/diff_check.

## Chín sửa đổi

Mã đoạn dưới đây có tiền tố `YS-LN02/Text/part0026.xhtml/`.

| ID | Mức ban đầu | Đoạn | Kết quả đối chiếu bản hiện tại |
| --- | --- | --- | --- |
| B04-F01 | vừa | p000076 | Resolved. Cách nói lỡ ném bom giữ tính vô ý cùng giọng mỉa mai; không còn biến thành tùy ý có chủ đích. |
| B04-F02 | vừa | p000076, p000079, p000083, p000085–p000089, p000097, p000101 | Resolved. Nội tâm tự quy chiếu dùng mình theo DEC-P01-001. Tôi trong thoại p000082/p000099 và chúng tôi được giữ đúng phạm vi; mình trong tiểu đoàn mình ở p000099 là cách sở hữu tự nhiên trong thoại, không phải áp dụng máy móc đại từ nội tâm. p000101 giữ cô ấy làm đối tượng lời bình về giới tính và nó trong trần thuật; p000102 cũng dùng nó. |
| B04-F03 | vừa | p000086 | Resolved. Đã giữ quan hệ tàu ngầm chìm xuống nhà vệ sinh hỏng, không biến nhà vệ sinh thành trang bị trên tàu. Hình ảnh lạ là đặc điểm của package; không tự sửa bằng suy luận ngoài phạm vi. |
| B04-F04 | vừa | p000094 | Resolved. Điều kiện trúng đạn và từ có lẽ giới hạn dự đoán tránh thương tích chí mạng; không còn bảo đảm sống sót. Cách nói có lẽ sẽ giúp đủ giữ độ bất định dù không dùng nguyên phương án hẳn vẫn có thể của review. |
| B04-F05 | vừa | p000099 | Resolved về lỗi tự xác định bậc quân hàm. Úy Serebryakov khớp lựa chọn tạm trong ledger/handoff; bậc cụ thể vẫn chưa xác định. |
| B04-F06 | nhẹ | p000092 | Resolved. Tiểu đội quan sát bỏ chức năng trinh sát suy diễn; giữ việc dẫn đường và quan sát điểm đạn rơi. |
| B04-F07 | nhẹ | p000091 | Resolved. Tương đối an toàn ở tiền tuyến mô tả mức rủi ro của nhiệm vụ, không còn gợi rằng nhiệm vụ làm tiền tuyến an toàn hơn. |
| B04-F08 | nhẹ | p000085 | Resolved. Mùa xuân đầu tiên giữ thứ tự mùa; không còn thêm thông tin mùa vừa bắt đầu. |
| B04-F09 | nhẹ | p000099 | Resolved. Diễn tập ứng phó pháo kích giữ hoạt động huấn luyện tránh đạn, phù hợp p000094 và nguy cơ đạn quân mình; không gợi tiểu đoàn luyện bắn pháo. |

Các quan hệ liên quan vẫn được giữ: mục tiêu pháo địch đang đánh Đại đội G/H, yêu cầu yểm trợ bắt đầu ngay trong năm phút, phản đối thời lượng ngắn, tiếp tục bắn khi đơn vị xông vào, phân công tấn công/yểm trợ trên không, rồi tăng độ cao. Không thấy sửa đổi tạo sai chủ thể, phủ định, thời gian hay mức chắc chắn nghiêm trọng/vừa mới.

## Đối sánh thuật ngữ

Mọi hàng dưới đây có trạng thái `pending`, thuộc nhóm `provisional_non_canon`. Các lựa chọn thay thế chỉ để xét về sau, không yêu cầu thay bản dịch hiện tại.

| Nhóm / ID đầy đủ | Đoạn | Lựa chọn đã kiểm chứng | Căn cứ và phương án thay thế |
| --- | --- | --- | --- |
| Chính thức: vol02-ch05-b04-silver-wings-assault-badge | p000083 | Huy hiệu Tấn công Cánh bạc | Giữ loại phần thưởng và các thành tố tên; chưa xác lập tên canon. Thay thế: Huy hiệu Xung kích Cánh bạc. |
| Chính thức: vol02-ch05-b04-artillery-emplacement-suppressive-fire | p000081–p000082 | vị trí pháo binh / hỏa lực chế áp yểm trợ | Đã áp dụng cách gọi trung tính cho nơi bố trí pháo, giữ chức năng chế áp và yểm trợ; không suy ra khẩu đội/công sự hoặc bảo đảm tiêu diệt bằng pháo yểm trợ. Thay thế: ổ pháo binh / hỏa lực chế áp yểm trợ; vị trí pháo binh / hỏa lực yểm trợ chế áp. |
| Chính thức: vol02-ch05-b04-anti-surface-assault-formation | p000093, p000096 | đội hình xung kích chống mục tiêu mặt đất / đợt xung kích chống mục tiêu mặt đất | Phân biệt đội hình ở p000093 với hoạt động ở p000096; mục tiêu mặt đất có căn cứ tại chỗ. Dạng contextual ở p000096 khớp review bổ sung, không phải thiếu từ đội hình. Thay thế: đội hình tấn công mục tiêu trên mặt đất; review cũng đề xuất đội hình xung kích đối đất. |
| Chính thức: vol02-ch05-b04-lieutenant-serebryakov | p000099 | Úy Serebryakov | Tránh tự chọn bậc cụ thể theo DEC-P01-001. Thay thế: Sĩ quan cấp úy Serebryakov; Thiếu úy/Trung úy chỉ xét khi có chứng cứ phân bậc. Độ tin cậy bậc cụ thể thấp; Úy chưa là quân hàm canon. |
| Bổ sung: vol02-ch05-b04-observation-squad | p000092 | tiểu đội quan sát | Giữ loại đơn vị và chức năng quan sát; không thêm trinh sát hay quân số. Thay thế: tổ quan sát, đội quan sát. |
| Bổ sung: vol02-ch05-b04-mage-outer-shells | p000093 | lớp vỏ ngoài của pháp sư | Giữ cách gọi literal; chưa có chứng cứ chốt cơ chế. Thay thế: lớp vỏ bảo vệ của pháp sư, lớp bảo vệ ngoài của pháp sư. Không tự gọi là kết giới/giáp. |
| Bổ sung: vol02-ch05-b04-direct-support | p000097 | lực lượng yểm trợ trực tiếp | Khớp phân công bay/yểm trợ trong p000096–p000097; không nhận diện tên đơn vị chính thức hay đổi thành pháo yểm trợ. Thay thế: bộ phận yểm trợ trực tiếp, yểm trợ trực tiếp. |
| Bổ sung: vol02-ch05-b04-orb | p000094 | quả cầu | Giữ tên thiết bị rút gọn tại chỗ, không thêm model/cơ chế. Thay thế: quả cầu tính toán, chỉ là đề xuất. |
| Bổ sung: vol02-ch05-b04-cp-pixie | p000080–p000081 | CP / Pixie | Giữ định danh vô tuyến, không khai triển CP thiếu căn cứ. Thay thế: sở chỉ huy / Pixie. |

B04-PENDING-MAP đóng về chứng cứ review: bốn ID chính thức nằm đúng mục translation_proposals, năm đề xuất nằm riêng trong reviewer_suggestions, đều đúng task và phạm vi đoạn. Ledger hiện tại đã thay hai lựa chọn cũ bằng vị trí pháo binh và Úy Serebryakov, khớp coordinator_provisional_choices và bản dịch. Handoff giữ coverage chính thức 4/4, không gộp năm bổ sung thành chín pending chính thức. Không thấy sai lệch đối sánh còn mở; không sửa trạng thái trong tệp điều phối.

## Kết quả bàn giao

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-05-b04
review_type: fixes_signoff
state: done
review_path: reviews/prose/vol-02/ch-05-b04-fixes-signoff-codex.md
signoff: accepted_for_reviewed_fixes_and_pending_reconciliation
scope:
  segment_id_start: YS-LN02/Text/part0026.xhtml/p000076
  segment_id_end: YS-LN02/Text/part0026.xhtml/p000102
  other_batches_inspected: false
files_written: [reviews/prose/vol-02/ch-05-b04-fixes-signoff-codex.md]
resolved_ids:
  findings: [B04-F01, B04-F02, B04-F03, B04-F04, B04-F05, B04-F06, B04-F07, B04-F08, B04-F09]
  metadata: [B04-PENDING-MAP]
unresolved_ids:
  findings: []
  metadata: []
unresolved_findings: []
findings: []
term_recommendations:
  official_pending_ids_verified: 4
  supplementary_ids_verified: 5
  choices: as_documented_in_term_table
  all_status: pending
  canon_promotion: false
  pending_status_resolved_by_signoff: false
counts:
  segments_reviewed: 27
  original_findings_verified: 9
  resolved_moderate: 5
  resolved_minor: 4
  unresolved_serious: 0
  unresolved_moderate: 0
  unresolved_minor: 0
  new_findings_total: 0
  new_serious: 0
  new_moderate: 0
  new_minor: 0
  official_pending_ids: 4
  supplementary_pending_ids: 5
  pending_terms_remaining: 9
  unresolved_mapping_ids: 0
risks:
  - 'Bậc cấp úy của Serebryakov còn bất định; Úy là lựa chọn tạm, không xác nhận Thiếu úy/Trung úy hoặc lịch sử cấp bậc.'
  - 'Tên huy hiệu, tên đội hình, cấp tổ chức quan sát và cơ chế lớp vỏ/thiết bị chưa được canon xác lập; giữ chín mục pending.'
  - 'Hình ảnh p000086 bất thường nhưng bản hiện tại giữ quan hệ nguồn; không suy diễn để làm hợp thực tế.'
  - 'Không có quyết định canon ảnh hưởng cốt truyện cần dừng trong phạm vi được đọc.'
  - 'Không xác nhận commit hoặc hoàn tất pipeline; không kiểm tra diff lịch sử. Sign-off dựa trên bản hiện tại và đầu vào b04.'
validator: not_run
diff_check: not_run
commit: null
next_action: >-
  Coordinator ghi nhận chín finding đã resolved và B04-PENDING-MAP đã reconciled,
  giữ bốn pending chính thức và năm đề xuất bổ sung ở trạng thái không canon.
  Coordinator xác nhận các kiểm tra bắt buộc áp dụng cho đúng bản đã sign-off
  và commit theo pipeline trước khi công nhận batch hoàn tất; không cần worker
  sửa thêm theo báo cáo này.
```
