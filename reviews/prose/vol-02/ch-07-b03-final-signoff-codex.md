# Phản biện ký duyệt cuối — vol-02-ch-07-b03

```yaml
role: reviewer
task_id: vol-02-ch-07-b03-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-07-b03-final-signoff-codex.md
files_written: [reviews/prose/vol-02/ch-07-b03-final-signoff-codex.md]
validator: not_run
diff_check: not_run
commit: null
signoff: withheld
next_action: coordinator_assign_translation_revision
scope:
  source_package: work/vol-02/batches/ch-07-b03-source.jsonl
  expected_sha256: 12607922a93b34fd2af9d60c983b49e735829c3c44963023755abee473e372e6
  actual_sha256: 12607922a93b34fd2af9d60c983b49e735829c3c44963023755abee473e372e6
  hash_check: pass
  source_rows: 24
  translation_rows: 24
  ids_and_order_match: true
  source_metadata_match: true
  segment_id_prefix: YS-LN02/Text/part0032.xhtml/
  segment_range: p000052–p000075
  canon_hashes_match_primary_handoff: true
  input_paths:
    - agents/shared.md
    - agents/reviewer.md
    - config/translation-pipeline.yml
    - handoffs/vol-02/ch-07-b03-final-signoff.yml
    - handoffs/vol-02/ch-07-b03-review-fixes.yml
    - handoffs/vol-02/ch-07-b03-review.yml
    - handoffs/vol-02/ch-07-b03.yml
    - reviews/prose/vol-02/ch-07-b03-codex.md
    - reviews/semantic/vol-02/ch-07-b03-self-check.md
    - translations/vol-02/ch-07-b03.jsonl
    - work/vol-02/batches/ch-07-b03-source.jsonl
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
  ledger_path: work/run-state/pending-terms.yml
  ledger_sections_read: [chapter7_b03_translator_proposals, chapter7_b03_review_recommendations]
  evidence_policy: Đối chiếu độc lập tại chỗ; không đọc EPUB/PDF hoặc package khác, không trích câu nguồn.
counts:
  reviewed_rows: 24
  prior_findings_verified: 11
  prior_findings_resolved: 11
  prior_findings_unresolved: 0
  prior_severity_counts: {serious: 0, moderate: 6, minor: 5}
  new_findings: 1
  serious: 0
  moderate: 1
  minor: 0
  unresolved_findings: 1
  pending_groups_checked: 4
  pending_groups_matching_active_recommendations: 4
  pending_groups_non_canon: 4
counting_method: Các mức hiện tại đếm finding còn mở; 11 finding cũ đã sửa được đếm riêng. Pending không tự động là lỗi.
unresolved_findings: [B03-F01]
findings:
  - id: B03-F01
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000060
    status: open
    issue: Bản dịch giữ trạng thái radar bị làm mù nhưng bỏ chủ thể phía Tanya duy trì trạng thái đó.
    evidence: >-
      Package gắn điều kiện hạn chế hỏa lực đối phương với hành động của phía người kể.
      Bản dịch hiện dùng điều kiện bị động, chỉ còn radar của địch bị làm mù, nên mất
      thông tin bên nào thực hiện/duy trì việc làm mù. Đây là quan hệ tác chiến có căn cứ
      trực tiếp, không phải cơ chế kỹ thuật cần suy đoán. Bao phủ p000060 của báo cáo
      đầu cũng đã lưu ý giữ rõ chủ thể phía Tanya; self-check hiện chưa xét phần này.
    resolution: >-
      Giữ điều kiện và dùng chủ thể số nhiều trong nội tâm, chẳng hạn “miễn là bọn mình
      giữ cho radar của địch bị làm mù”; giữ “khai hỏa có kiểm soát”. Không thêm cơ chế,
      thiết bị, đội hình hoặc cấp bậc. Cập nhật self-check để xác nhận chủ thể và quan hệ
      duy trì điều kiện, rồi đối chiếu lại p000060 với package.
    related_prior_findings: [B03-C01, B03-C04]
term_recommendations:
  - group: recon-in-force
    proposed_vi: trinh sát chiến đấu
    alternatives_vi: [trinh sát bằng vũ lực, trinh sát có vũ trang]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000053, YS-LN02/Text/part0032.xhtml/p000056, YS-LN02/Text/part0032.xhtml/p000058]
    contextual_segment_ids: [YS-LN02/Text/part0032.xhtml/p000057]
    matches_translation_and_self_check: true
    status: pending
    canon: false
    rationale: Giữ cả mục đích thu thập tình báo lẫn giao chiến thăm dò; không chèn thuật ngữ vào p000057 chỉ để khớp liên kết ngữ cảnh.
  - group: battalion_name
    proposed_vi: Tiểu đoàn Pháp sư Trên không số 203
    alternatives_vi: [Tiểu đoàn Pháp sư Không chiến số 203]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000054]
    matches_translation_and_self_check: true
    status: pending
    canon: false
    rationale: Giữ cấp tiểu đoàn, số hiệu 203 và yếu tố trên không; không tự xác lập tên chính thức hoặc tiền lệ ngoài b03.
  - group: radar_and_visual_combat
    proposed_vi: trắc thủ radar / tác chiến bằng quan sát trực tiếp
    alternatives_vi: [quan sát viên radar / tác chiến bằng mắt thường, trắc thủ radar / không chiến bằng mắt thường]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000061, YS-LN02/Text/part0032.xhtml/p000062]
    contextual_segment_ids: [YS-LN02/Text/part0032.xhtml/p000060]
    matches_translation_and_self_check: true
    status: pending
    canon: false
    rationale: Giữ chức năng dẫn hướng hỏa lực và đối lập radar với quan sát trực tiếp; không suy ra chức danh chính thức, kíp radar hay dụng cụ ngắm bắn.
  - group: game_theory_and_zero_sum
    proposed_vi: lý thuyết trò chơi / trò chơi tổng bằng không
    alternatives_vi: [lý thuyết trò chơi / tình thế tổng bằng không, lý thuyết trò chơi / tổng bằng không]
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000075]
    matches_translation_and_self_check: true
    status: pending
    canon: false
    rationale: Giữ lập luận chủ quan của Tanya và phủ định tổng bằng không; không biến cơ hội an toàn thành bảo đảm sống sót hoặc kết luận mọi bên đều thắng.
pending_terms: []
risks:
  - B03-F01 còn mở ở mức vừa; chưa đủ điều kiện ký duyệt nội dung cuối.
  - Bốn lựa chọn chỉ khớp bộ khuyến nghị đang được handoff giao áp dụng; ledger đề xuất ban đầu được giữ như lịch sử, không phải bộ lựa chọn hiện hành.
  - Tên đơn vị, chức danh radar và thuật ngữ tác chiến vẫn tạm thời; không có quyết định canon mới trong các đầu vào được phép.
  - Validator và diff-check không chạy trong lượt reviewer; kết quả đối chiếu thủ công/hash không thay thế các điều kiện hoàn tất pipeline.
```

Mọi mã rút gọn bên dưới có tiền tố `YS-LN02/Text/part0032.xhtml/`. Đã đọc độc lập cả 24 cặp đoạn nguồn–dịch và đối chiếu self-check, thay vì chỉ kiểm tra câu sửa có giống đề xuất hay không.

| Finding | Mã đoạn | Kết quả trong bản dịch và self-check |
|---|---|---|
| B03-C01 | p000055, p000058, p000060, p000063, p000065, p000066, p000068–p000070, p000074–p000075 | Đã sửa đại từ nội tâm thành “mình” và chủ thể đơn vị thành “bọn mình”; “tôi” chỉ xuất hiện trong thoại p000059/p000067. p000057 giữ “nó” cho Tanya trong trần thuật. Ở p000075, chủ thể lược của điều kiện chấp nhận rủi ro được hiểu là Tanya từ điểm nhìn nội tâm và mạch p000070/p000074; nhóm rút lui là bên có cơ hội an toàn. Self-check nêu đúng quy tắc. Việc bỏ chủ thể tác chiến ở p000060 được tách thành F01, không tính lặp lỗi đại từ cũ. |
| B03-C02 | p000052 | Đã giữ nhượng bộ về chức vụ sĩ quan tham mưu, không biến thành phỏng đoán chức vụ và không thêm quân hàm; nỗi ám ảnh Being X còn nguyên. Self-check xác nhận đúng. |
| B03-C03 | p000056 | Đã dùng cuộc tiến công lớn sắp diễn ra; giữ trinh sát tìm hiểu chuẩn bị phòng thủ/vị trí, dẫn tới che giấu quân và hạn chế điều động dự bị. Self-check đúng. |
| B03-C04 | p000060, p000062 | Đã dùng khai hỏa/hỏa lực có kiểm soát, bỏ đội hình không có căn cứ; đối lập với bắn nhiều nhưng ngắm kém vẫn rõ ở p000063–p000064. Self-check đúng về sửa thuật ngữ này; F01 là mất chủ thể trong điều kiện kế cận. |
| B03-C05 | p000067, p000074 | Cả mệnh lệnh vô tuyến lẫn nội tâm đều là hai phát, không còn hai loạt. Self-check ghi đúng lượng và đơn vị bắn. |
| B03-C06 | p000074 | Khói từ đạn nổ và ánh đèn pha là hai yếu tố che lấp, không còn quan hệ đèn pha tạo khói. Hai thuộc cấp cùng người bị thương thành ba người; Tanya bắn hai phát yểm trợ. Self-check khớp. |
| B03-C07 | p000058 | Khôi phục tiếp đón nồng nhiệt mang giọng mỉa mai; không thêm chữ nghiêng. Self-check khớp. |
| B03-C08 | p000059 | Thông báo trúng đạn rồi dự định rút lui, không khẳng định đã rút; p000067 tiếp tục giao yểm trợ và lui trong thời gian hai phát bắn. Mã gọi và thoại gọn được giữ. Self-check khớp. |
| B03-C09 | p000069 | Lời tự tán thưởng về tinh thần xây dựng hướng tới tương lai tự nhiên hơn, giữ giọng tự biện hộ và câu thái độ tích cực; không thêm phán xét đạo đức. Self-check khớp. |
| B03-C10 | p000072 | Khôi phục khả thể người nghiệp dư có lý khi nhận thấy nguy cơ; vẫn giới hạn đánh giá của họ. Self-check khớp về mức chắc chắn, dù bản dịch không dùng toàn bộ câu ví dụ trong báo cáo. |
| B03-C11 | p000075 | Chuyển ý tăng tiến bằng “Thậm chí”; giữ hai người hỗ trợ làm mồi nhử, hút chú ý khi rút và cơ hội về nơi an toàn. Self-check khớp. |

Các đoạn không có finding riêng vẫn giữ nghĩa và mạch lập luận: p000053–p000054 về nghi binh/hậu vệ; p000055 về pháo rút trước bộ binh, bẫy đã bố trí và dự kiến vài giờ; p000057 về mệnh lệnh câu giờ; p000061 về khả thể quá khứ đánh chặn tốt hơn; p000063–p000066 về lượng đạn, cổ phiếu và khoản đầu tư; p000068–p000071/p000073 về bài học, yểm trợ và mất cơ hội hành động. XHTML của toàn bộ package không có dấu nhấn mạnh tương ứng cần chuyển sang Markdown; bản dịch không thêm dấu sao.

Cả bốn nhóm khớp đồng thời bản dịch, self-check, báo cáo đầu và `chapter7_b03_review_recommendations`, đúng lựa chọn được fix handoff giao áp dụng. `chapter7_b03_translator_proposals` vẫn giữ phương án cũ cho trinh sát và quan sát trực tiếp, cùng liên kết đoạn rộng hơn; đây là lịch sử đề xuất, không phải bằng chứng bản dịch phải quay lại phương án cũ. Bộ khuyến nghị hiện hành đã phân biệt p000057/p000060 là ngữ cảnh và không gắn radar/visual vào p000056. Tất cả mục trong hai phần ledger vẫn `pending`, `canon: false`; glossary và characters chưa có mục đã chốt, decisions chỉ duyệt quy tắc đại từ/nhấn mạnh. Không phát hiện việc nâng bốn nhóm thành canon. Không đề xuất thêm nhóm thuật ngữ mới.

Ký duyệt nội dung cuối **chưa đạt** do F01. Coordinator có thể giao sửa p000060 và cập nhật self-check trong phạm vi b03, rồi yêu cầu đối chiếu lại; không cần quyết định canon để khôi phục chủ thể đã có căn cứ trong package.

## Phụ lục sửa cuối — B03-F01 tại p000060

Phụ lục này thay thế kết luận giữ lại ký duyệt ở trên. Chỉ đối chiếu lại B03-F01 tại `YS-LN02/Text/part0032.xhtml/p000060` trong package b03 được giao, bản dịch cuối và self-check tương ứng; không mở EPUB/PDF hoặc package khác. SHA-256 của package vẫn là `12607922a93b34fd2af9d60c983b49e735829c3c44963023755abee473e372e6`, khớp handoff và lần ký duyệt trước.

Bản dịch hiện ghi: “miễn là bọn mình giữ cho radar của địch bị làm mù, họ không thể nào khai hỏa có kiểm soát.” “Bọn mình” nêu rõ phía Tanya là chủ thể duy trì trạng thái radar địch bị làm mù; điều kiện và quan hệ hạn chế khả năng khai hỏa của đối phương khớp package. Câu giữ “khai hỏa có kiểm soát”, không thêm thiết bị, cơ chế kỹ thuật hoặc đội hình. Self-check tại B03-C04 đã xác nhận đúng chủ thể, trạng thái được duy trì và cách diễn đạt hỏa lực này.

B03-F01 **đã giải quyết**. B03-C01–B03-C11 tiếp tục **đóng** theo kết quả đối chiếu trước trong báo cáo này; lượt kiểm tra giới hạn này không mở lại các finding đó. Sửa tại p000060 giữ quy tắc đại từ của C01 và cách diễn đạt hỏa lực của C04. Bốn nhóm thuật ngữ tiếp tục là đề xuất pending, non-canon.

**Ký duyệt đầy đủ về nội dung cho vol-02-ch-07-b03: đạt.** Không còn finding chưa giải quyết. Đây là kết luận phản biện nội dung; không xác nhận thay cho validator của pipeline.

```yaml
addendum: final_correction
role: reviewer
scope: B03-F01_only
segment_id: YS-LN02/Text/part0032.xhtml/p000060
source_package_hash_check: pass
finding_status: {B03-F01: resolved}
prior_findings_closed: 11
prior_findings_reopened: 0
unresolved_findings: []
signoff: full
validator: not_run
files_written: [reviews/prose/vol-02/ch-07-b03-final-signoff-codex.md]
commit: null
```
