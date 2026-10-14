# Kiểm tra ký duyệt cuối b04 — Codex

Đã đối chiếu độc lập 28/28 đoạn p000076–p000103 với package b04. Tám sửa đổi B04-C01–B04-C08 đều đã có trong translation và được ghi nhận trong phần tiếp nhận phản biện của self-check. Chưa ký duyệt cuối: p000083 phát sinh vấn đề chủ thể khi bỏ lời gọi, và hồ sơ lựa chọn còn chưa đồng bộ. Không coi việc làm đúng đề xuất của reviewer trước là bằng chứng tự thân rằng câu sửa giữ đúng nghĩa.

Mã rút gọn pNNNNNN trong báo cáo luôn mang tiền tố `YS-LN02/Text/part0032.xhtml/`. Không trích câu nguồn. Chỉ đọc các chỉ dẫn được giao, package/translation/self-check b04, báo cáo và handoff b04, năm tài liệu canon được primary handoff nêu và hai mục ledger được chỉ định. Không mở EPUB/PDF, package khác hay nội dung nguồn ngoài phạm vi. Không chạy graphify vì việc đó vượt phạm vi đọc/ghi được giao.

```yaml
role: reviewer
task_id: vol-02-ch-07-b04-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-07-b04-final-signoff-codex.md
segment_ids:
  - YS-LN02/Text/part0032.xhtml/p000076–p000103
files_written:
  - reviews/prose/vol-02/ch-07-b04-final-signoff-codex.md
coverage:
  checked_rows: 28
  total_rows: 28
  source_package_sha256: bbe4ad2e636962ef2d554ae815a8bbbed9f026b02a5ab93c3d6c14bc38729d46
  source_package_hash: pass
  segment_alignment: pass
  segment_uniqueness: pass
  source_hash_metadata: pass
  canon_reference_hashes: pass
  original_findings_verified: 8
  original_findings_resolved_in_translation: 8
  original_findings_recorded_in_self_check_addendum: 8
  base_choices_reviewed: 11
  additional_choices_reviewed: 5
  base_ledger_choices_present: 11
  additional_ledger_section_present: false
counts:
  serious: 0
  moderate: 1
  minor: 2
  total: 3
resolved_findings: [B04-C01, B04-C02, B04-C03, B04-C04, B04-C05, B04-C06, B04-C07, B04-C08]
unresolved_findings: [B04-FS01, B04-FS02, B04-FS03]
signoff: withheld
translation_signoff: withheld
validator: not_run
diff_check: not_run
commit: null
pending_terms: []
term_recommendations:
  count_existing_groups: 11
  count_additional_choices: 5
  status: proposed
  canon: false
  consistency: incomplete
  dialogue_address: Giữ rõ người được tin là có khả năng thực hiện nhiệm vụ; tạm dùng người nhận lệnh trong câu p000083.
findings:
  - id: B04-FS01
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000083
    issue: Bỏ lời gọi làm mờ hoặc đổi chủ thể có khả năng thực hiện nhiệm vụ trong lời cấp trên được nhắc lại.
    resolution: Đề xuất tôi biết người nhận lệnh có thể làm được; giữ câu hỏi mỉa mai và không tự thêm giới tính. Chưa áp dụng.
  - id: B04-FS02
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000082
    related_segment_ids: [YS-LN02/Text/part0032.xhtml/p000103]
    issue: Các mục đầu self-check vẫn ghi đội đoạn hậu và dán nhãn sai như lựa chọn đang dùng, trái với phần tiếp nhận và translation cuối.
    resolution: Người giữ quyền sửa cập nhật các mục cũ hoặc đánh dấu rõ đã được thay thế; không chỉ nối thêm phần tiếp nhận. Chưa áp dụng.
  - id: B04-FS03
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000082
    related_segment_ids: [YS-LN02/Text/part0032.xhtml/p000081, YS-LN02/Text/part0032.xhtml/p000083, YS-LN02/Text/part0032.xhtml/p000084, YS-LN02/Text/part0032.xhtml/p000092, YS-LN02/Text/part0032.xhtml/p000098, YS-LN02/Text/part0032.xhtml/p000103]
    issue: Base ledger vẫn đề xuất đội đoạn hậu cho p000082; mục chapter7_b04_review_recommendations được handoff viện dẫn không tồn tại.
    resolution: Coordinator đồng bộ mục rear guard và ghi đủ năm lựa chọn bổ sung với mã đoạn, căn cứ, bất định và trạng thái pending/non-canon; tiếp nhận sửa chủ thể FS01. Chưa áp dụng.
risks:
  - p000083 còn vấn đề chủ thể mức vừa nên chưa đạt điều kiện ký duyệt.
  - Hồ sơ self-check và ledger cũ có thể khiến lần sửa sau tái áp dụng lựa chọn đã thay thế.
  - Năm lựa chọn bổ sung chưa có mục ledger được handoff chỉ định; không thể xác nhận 16 lựa chọn đã đồng bộ giữa mọi đầu vào.
  - Package b04 không đủ để chốt cơ chế phép thuật, hệ thống cấp hàm hoặc quan hệ nhân vật liên chương.
  - Chỉ tiêu p000101 chưa được định danh; giữ độ mở, không suy ra số mục tiêu hoặc số người.
  - Không chạy validator hoặc diff-check; kiểm tra hash và JSONL ở đây không thay thế các điều kiện hoàn tất pipeline.
next_action: translator_fix_FS01_and_self_check_then_coordinator_sync_ledger_and_required_checks
```

## Tám findings ban đầu

| Finding | Đoạn | Kết quả độc lập trong translation và self-check |
| --- | --- | --- |
| B04-C01 | p000076 | Đã sửa. Lợi ích riêng đi cùng sự quan tâm tới cấp dưới; không còn tự thêm sự giả vờ. Việc dùng cớ hỗ trợ người rút lui và cơ hội cứu người đều còn. Self-check ghi nhận đúng. |
| B04-C02 | p000081–p000082, p000088 | Đã sửa. “tướng” giữ danh xưng chung; “Thiếu tướng” ở p000088 giữ cấp cụ thể. Không tự suy ra cấp khác; chữ hoa ở p000088 không làm thay đổi cấp hàm. Self-check phân biệt hai trường hợp đúng. |
| B04-C03 | p000082 | Đã sửa trong translation: “đảm nhiệm việc đoạn hậu” phù hợp chủ thể cá nhân. Phần tiếp nhận self-check đúng, nhưng danh sách pending cũ chưa cập nhật: FS02/FS03. |
| B04-C04 | p000085 | Đã sửa. Ông ta là người dùng lời để ép người khác im miệng; Tanya vẫn thừa nhận khả năng hiểu lầm. Self-check đúng. |
| B04-C05 | p000092 | Đã sửa. 01 gọi hai bên nhận 06 và 09; không còn dải số. Màn chắn là cách giải thích tạm có căn cứ từ p000089–p000093, không nhập với sức cầm cự của nghi binh. Self-check đúng. |
| B04-C06 | p000098 | Đã sửa. Lời chửi giữ hình ảnh tục, không thành lời nguyền chết, vẫn là nội tâm có chữ nghiêng. Self-check đúng. |
| B04-C07 | p000101–p000102 | Đã sửa. Một nửa ngừng tham chiến, không gán tử vong hoặc nguyên nhân; “chúng tôi” nhất quán trong báo cáo. Đoạn sau vẫn phủ định tử vong và giữ phỏng đoán về trở lại chiến tuyến. Self-check đúng. |
| B04-C08 | p000103 | Đã sửa trong translation. Cấu trúc nếu–thì coi như giữ hệ quả giả định; “ghi nhãn sai” giữ liên hệ nhãn–quảng cáo–lòng tin. Phần tiếp nhận self-check đúng, nhưng mục Findings cũ còn “dán nhãn sai”: FS02. |

Bốn vùng nhấn mạnh được giữ đúng: hai vùng tại p000087, một tại p000094 và một tại p000098. Trần thuật về Tanya tại p000081 và phần giữa p000087 dùng “nó”; nội tâm tự quy chiếu dùng “mình”, phù hợp DEC-P01-001. Lời thoại được xét riêng. Không thấy lỗi nghiêm trọng hoặc lỗi vừa khác ngoài FS01 khi đối chiếu đủ 28 đoạn.

## Vấn đề mới và hồ sơ chưa đồng bộ

**B04-FS01 — vừa — p000083.** Câu cuối hiện là “Nhiệm vụ ác liệt đấy, nhưng tôi biết làm được” kèm “ư?”. Trong ngữ cảnh đây là lời cấp trên được Tanya nhắc lại, “tôi” là cấp trên, còn người được đánh giá có khả năng thực hiện nhiệm vụ là người nhận lệnh. “Tôi biết làm được” thường được hiểu là người nói biết cách hoặc biết mình làm được; việc bỏ đối tượng làm mất quan hệ giữa người tin tưởng và người thực hiện. Đề xuất cục bộ: “Nhiệm vụ ác liệt đấy, nhưng tôi biết người nhận lệnh có thể làm được” kèm “ư?”. Phương án tự nhiên hơn “tôi biết người được giao nhiệm vụ sẽ làm được” cũng trung tính nhưng hơi tăng độ chắc chắn; ưu tiên phương án có “có thể”. Chưa chọn đại từ giới tính hoặc quy tắc xưng hô liên chương. p000084 cũng đã bỏ đối tượng kỳ vọng, nhưng mạch ngay cạnh còn cho phép hiểu Tanya là đối tượng; có thể bổ sung “ở người nhận lệnh” nếu cần đồng bộ. Không tính p000084 thành một lỗi vừa riêng.

**B04-FS02 — nhẹ — p000082/p000103.** Self-check có phần tiếp nhận đầy đủ, nhưng các mục cũ vẫn mô tả “đội đoạn hậu” và “dán nhãn sai” ở thì hiện tại. Câu cuối còn khẳng định các lựa chọn pending trong bảng trên giữ nguyên. Vì không đánh dấu mục cũ là lịch sử đã thay thế, không thể xác nhận toàn bộ self-check nhất quán với bản cuối. Đề xuất thay mục rear guard thành “đoạn hậu”, dùng trong câu “đảm nhiệm việc đoạn hậu”, và mục mislabeling thành “ghi nhãn sai”; giữ nhãn đề xuất/non-canon.

**B04-FS03 — nhẹ — hồ sơ ledger b04.** Parse YAML xác nhận mục base có đủ 11 lựa chọn, tất cả `status: pending`, `canon: false`; tuy nhiên rear guard vẫn là “đội đoạn hậu” với đúng mã p000082. Không tìm thấy khóa `chapter7_b04_review_recommendations` trong cấu trúc YAML, dù fix handoff và final-signoff handoff đều viện dẫn nó. Năm lựa chọn bổ sung có trong báo cáo ban đầu và phần tiếp nhận self-check, không phải hoàn toàn thiếu chứng cứ; nhưng chưa có sổ ledger được chỉ định để xác nhận đồng bộ. Coordinator cần cập nhật hồ sơ theo quyền, không cần hỏi người dùng chốt canon. Reviewer không sửa ledger/handoff.

## Đủ 11 nhóm gốc và năm lựa chọn bổ sung

Mọi lựa chọn dưới đây còn là đề xuất, không canon. Canon glossary và characters đều chưa có mục đã chốt; decisions chỉ duyệt đại từ trần thuật/nội tâm và biểu diễn nhấn mạnh. Năm hash canon đều khớp primary handoff. Việc tham chiếu đề xuất lô trước trong hồ sơ không được dùng làm chứng cứ đã đọc các lô đó.

| Nhóm | Đoạn | Kiểm tra bản cuối và trạng thái hồ sơ |
| --- | --- | --- |
| rear guard | p000082 | “đảm nhiệm việc đoạn hậu” đúng ngữ cảnh cá nhân; self-check cũ/base ledger còn “đội đoạn hậu”. Đề xuất đồng bộ thành “đoạn hậu”; giữ “lực lượng đoạn hậu” chỉ cho ngữ cảnh tập thể có căn cứ. |
| Major General(s) | p000088 | “Thiếu tướng” khớp base ledger và self-check; cấp cụ thể chỉ dùng nơi package nêu cụ thể. Pending/non-canon. |
| mage(s) | p000102 | “pháp sư” khớp hồ sơ; “thuật sĩ” vẫn là phương án khác, chưa cần thay. Pending/non-canon. |
| orb / computation orb | p000089 | “quả cầu tính toán” khớp tên đầy đủ; không tạo lần gọi rút gọn chỉ để dùng cả hai biến thể trong ledger. Pending/non-canon. |
| interference formula | p000089–p000090 | “công thức gây nhiễu” nhất quán hai lần. “Công thức can thiệp” là phương án trung tính hơn nhưng cứng; phương án điện tử trong hồ sơ chưa có căn cứ trong b04, không được xem là đồng nghĩa đã chốt. Pending/non-canon. |
| protective film / defensive shell | p000089, p000097 | “màn chắn bảo hộ / lớp vỏ phòng thủ” giữ hai cách gọi và lớp vỏ nhất quán; không kết luận hai cơ chế đồng nhất hay độc lập. Pending/non-canon. |
| Elinium Type 95 | p000097 | Giữ tên và số hiệu đúng hồ sơ; “Elinium loại 95” vẫn chỉ là phương án khác. Pending/non-canon. |
| General Staff | p000086 | “Bộ Tổng tham mưu” nhất quán với hồ sơ, phân biệt với sĩ quan tham mưu. Pending/non-canon. |
| Being X | p000098 | Giữ định danh, khớp P05-being-x còn pending; không tự đồng nhất với mọi danh xưng thần linh. Non-canon. |
| Lord | p000096–p000097 | “Chúa” nhất quán lời cầu và lời tự trách; “Thượng đế” là phương án khác. Không chốt quan hệ với Being X. Pending/non-canon. |
| CP / Fairy | p000100–p000101 | Giữ ký hiệu và Fairy 01; hai hướng gọi khớp package, không khai triển chữ viết tắt. Pending/non-canon. |
| General — bổ sung | p000081–p000082 | “tướng” được áp dụng và self-check ghi đúng; phương án gọi thiếu tướng ở mọi lần cụ thể hóa quá mức. Chưa có mục ledger bổ sung, vẫn không canon. |
| dialogue_address — bổ sung | p000083–p000084, p000096–p000097 | Đã bỏ “cô”, giữ “tôi” của người nói và “các cậu” với lính dưới quyền; p000083 cần FS01 để giữ chủ thể. “Mọi người” là phương án khác cho lính dưới quyền. Chưa có mục ledger bổ sung, không canon. |
| radio_route — bổ sung | p000092, p000100–p000101 | Đã áp dụng “gọi”, giữ đúng bên gửi/nhận; p000092 không thêm CP/Fairy. Chưa có mục ledger bổ sung, không canon. |
| profanity — bổ sung | p000098 | Đã áp dụng lời chửi có hình ảnh tục, giữ nhấn mạnh; cách chửi chung giảm độ cụ thể, không ưu tiên. Chưa có mục ledger bổ sung, không canon. |
| mislabeling — bổ sung | p000103 | “ghi nhãn sai” đã áp dụng; “gắn nhãn sai” là phương án khác. Self-check đầu còn lựa chọn cũ, chưa có mục ledger bổ sung. Không canon. |

Kết quả: xác nhận trạng thái non-canon của đủ 16 nhóm qua hồ sơ cho phép, nhưng không xác nhận chúng đã nhất quán toàn bộ. Mười nhóm base khớp lựa chọn đang dùng; nhóm rear guard cần đồng bộ. Cả năm lựa chọn bổ sung được ghi nhận trong báo cáo/self-check, bốn lựa chọn không có lỗi dịch mới; lựa chọn xưng hô cần sửa chủ thể. Final signoff bị giữ lại cho đến khi lỗi vừa FS01 được xử lý, hồ sơ được đồng bộ và coordinator thực hiện các kiểm tra bắt buộc. Không có quyết định canon ảnh hưởng cốt truyện cần dừng chờ người dùng trong phạm vi b04.

## Correction addendum — tái kiểm ba residuals (2026-10-14)

**Full signoff: granted.** B04-FS01, B04-FS02 và B04-FS03 đều đã được xử lý. Kết luận addendum này thay thế trạng thái withheld và danh sách unresolved của lần kiểm trước; không lặp lại việc kiểm toàn bộ 28 đoạn hoặc tám findings ban đầu.

Chỉ đọc hướng dẫn được giao, báo cáo/handoff b04, package b04, bốn dòng translation p000082–p000084/p000103, self-check b04 và hai mục ledger `chapter7_b04_translator_proposals`, `chapter7_b04_review_recommendations`. SHA-256 package vẫn khớp `bbe4ad2e636962ef2d554ae815a8bbbed9f026b02a5ab93c3d6c14bc38729d46`. Không mở EPUB/PDF hay package khác, không chạy graphify, không trích câu nguồn. Chỉ bổ sung báo cáo này.

| Residual | Kết quả tái kiểm |
| --- | --- |
| B04-FS01 — p000083–p000084 | p000083 hiện có “tôi biết người nhận lệnh có thể làm được”: “tôi” vẫn là người nói lời cấp trên được nhắc lại, người có khả năng thực hiện nhiệm vụ được nêu riêng và trung tính. p000084 có “kỳ vọng rất nhiều ở người nhận lệnh”, giữ đúng đối tượng kỳ vọng. Cả hai vẫn kết thúc bằng “ư?”, không thêm giới tính hay quy tắc xưng hô liên chương. Cách gọi hơi hành chính nhưng rõ nghĩa và phù hợp phương án tạm đã đề xuất; không còn lỗi chủ thể mức vừa. |
| B04-FS02 — p000082/p000103 | Translation dùng “đảm nhiệm việc đoạn hậu” cho cá nhân và “ghi nhãn sai”. Mục pending đầu self-check đã dùng “đoạn hậu”; mục Findings về p000103 đã dùng “ghi nhãn sai”. Các cách dùng cũ “đội đoạn hậu”/“dán nhãn sai” được đánh dấu lịch sử đã thay thế, nhất quán với phần tiếp nhận phản biện và câu xác nhận cuối. Mọi lựa chọn vẫn là đề xuất, không canon. |
| B04-FS03 — hai mục ledger b04 | Parse YAML xác nhận mục base tồn tại với 11 lựa chọn; rear guard hiện là “đoạn hậu”, usage “đảm nhiệm việc đoạn hậu”, còn wording cũ là lịch sử. Mục reviewer bổ sung thực sự tồn tại: có B04-RG-01 đồng bộ rear guard và đủ B04-ADD-01–B04-ADD-05 cho General, dialogue address, radio route, profanity, mislabeling, kèm mã đoạn và phương án khác. B04-ADD-02 ghi rõ giữ “tôi” của người nói và nêu trung tính “người nhận lệnh” ở p000083–p000084; B04-ADD-05 dùng “ghi nhãn sai”. Căn cứ lựa chọn cục bộ được ghi ở nguồn báo cáo/rationale của mục và rationale xưng hô; không thiết lập quy tắc liên chương. Cả 11 mục base và sáu bản ghi reviewer đều có `status: pending`, `canon: false`. Không còn việc handoff viện dẫn một mục ledger chưa tồn tại. |

```yaml
role: reviewer
task_id: vol-02-ch-07-b04-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-07-b04-final-signoff-codex.md
files_written:
  - reviews/prose/vol-02/ch-07-b04-final-signoff-codex.md
segment_ids:
  - YS-LN02/Text/part0032.xhtml/p000082
  - YS-LN02/Text/part0032.xhtml/p000083
  - YS-LN02/Text/part0032.xhtml/p000084
  - YS-LN02/Text/part0032.xhtml/p000103
coverage:
  scope: residual_correction_recheck_only
  source_package_hash: pass
  evaluated_recipient_explicit_neutral: pass
  speaker_toi_retained: pass
  self_check_current_choices_consistent: pass
  base_ledger_rear_guard_consistent: pass
  additional_ledger_section_present: true
  additional_choices_present: 5
  all_checked_ledger_choices_pending_non_canon: true
counts:
  serious: 0
  moderate: 0
  minor: 0
  total: 0
resolved_findings: [B04-FS01, B04-FS02, B04-FS03]
unresolved_findings: []
signoff: granted
translation_signoff: granted
validator: not_run
diff_check: not_run
commit: null
pending_terms: []
term_recommendations:
  status: proposed
  canon: false
  consistency: complete_for_residual_scope
risks:
  - Signoff là kết luận review; không thay thế validator, diff-check hoặc commit bắt buộc của coordinator.
next_action: coordinator_complete_required_pipeline_checks_and_record_signoff
```
