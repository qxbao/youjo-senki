# Final signoff — vol-02-ch-06-b07

Đã đọc persona/shared, config, handoff final-signoff/review/review-fixes, báo cáo review, bản dịch hiện tại, self-check, canon và riêng các mục chapter6_b07 trong pending ledger. Chỉ đối chiếu gói nguồn cục bộ được giao; không mở EPUB/PDF hoặc gói khác. SHA-256 gói khớp handoff: `f6e79df03b5320539229b74f06977d3069c11389c46d192ee3f688dd0ea1ff27`.

Nguồn và bản dịch có đủ 30 đơn vị p000194–p000223, cùng ID và thứ tự. Đã rà cả lô và kiểm lại từng finding. Kết quả: **7/8 resolved; 1/8 partially resolved**. Còn **0 serious, 0 moderate, 1 minor**; không phát hiện finding mới. Đếm theo finding, không đếm lặp theo đoạn.

| Finding | Severity ban đầu | IDs (tiền tố YS-LN02/Text/part0030.xhtml/) | Kết quả kiểm lại |
| --- | --- | --- | --- |
| B07-R01 | moderate | p000205 | Resolved: giữ giả định đủ người duy trì thành phố và chức năng đầu mối giao thông. |
| B07-R02 | moderate | p000212, p000215 | Resolved: giữ bao vây, bỏ đói đến khi khuất phục; không định danh nhóm đối phương. |
| B07-R03 | moderate | p000214, p000215, p000217 | Resolved: trần thuật Tanya dùng đại từ theo DEC-P01-001; thoại giữ riêng. |
| B07-R04 | moderate | p000222 | Resolved: lực lượng dư ra, không gán tư cách quân dự bị. |
| B07-R05 | moderate | p000222 | Resolved: nhấn mạnh đúng yếu tố chỉ tình cảnh, theo DEC-P01-002. |
| B07-R06 | minor | p000214 | Partially resolved: cụm nguyền rủa đã tự nhiên hơn; câu kết vẫn khái quát hóa giới hạn chỉ còn có thể than phiền. |
| B07-R07 | minor | p000211 | Resolved: trì hoãn can thiệp, giữ sắc thái khuyến nghị. |
| B07-R08 | minor | p000223 | Resolved: vật tư quân sự giữ phạm vi rộng. |

## Finding còn lại

**B07-R06 — minor — YS-LN02/Text/part0030.xhtml/p000214**

Câu cuối chỉ nói đó là tất cả những gì có thể làm; chưa giữ rõ hành động than phiền/kêu ca là giới hạn dưới sức ép chính trị. Câu trước đã giữ lời phản đối gián tiếp và sức ép, nên lỗi còn lại nhỏ, không làm đảo nghĩa lập luận. Căn cứ: đối chiếu đoạn được giao và yêu cầu R06 trong báo cáo/handoff sửa; độ tin cậy cao. Đề xuất sửa câu cuối thành: “Dưới sức ép chính trị, họ chỉ có thể than phiền như vậy.” Đây là đề xuất tiếng Việt, không phải trích nguồn. Self-check và handoff hiện đánh dấu R06 đã xử lý; đánh giá đó chưa đầy đủ ở chi tiết này.

## Thuật ngữ và giới hạn signoff

`law of war` tiếp tục đề xuất **luật chiến tranh**, tại p000208; phương án thay thế **luật về chiến tranh**. Cách literal có căn cứ trong gói; không thêm khung pháp lý chuyên biệt. Độ bất định thấp về nghĩa trong lô, trung bình về tên gọi chuẩn dài hạn.

`noncombatants` tiếp tục đề xuất **người không tham chiến**, tại p000208/p000212; phương án thay thế **người không trực tiếp tham chiến** bổ sung tiêu chí chưa được xác lập nên không ưu tiên. Không thu hẹp thành thường dân hoặc định danh thành phần nhóm. Độ bất định thấp về cách dịch trong lô, trung bình về thành phần cụ thể.

Cả hai mục có trạng thái **pending**, nhóm coordinator choices có trạng thái **provisional_non_canon**, và không có quyết định duyệt tương ứng trong canon. Bản dịch giữ lời truyền chưa xác thực về chế tài ở p000208; không suy diễn luật ngoài đời. Không cần chờ quyết định thuật ngữ để tiếp tục. Cấp tổ chức Hậu cần vẫn chưa xác lập; nhận diện chủ thể p000214–p000215 dựa trên ngữ cảnh gói cục bộ.

Không xác nhận toàn bộ R01–R08 đã đóng. Review hoàn tất với một minor còn lại; coordinator có thể bàn giao người giữ quyền sửa xử lý R06. Không sửa bản dịch, self-check, handoff, ledger hoặc canon; không commit. Validator/diff_check trong lượt signoff này không chạy; kết quả pass ở handoff sửa là kết quả được báo cáo từ lượt trước.

```yaml
role: reviewer
task_id: vol-02-ch-06-b07-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-06-b07-final-signoff-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b07-final-signoff-codex.md
counts:
  reviewed_segments: 30
  findings_checked: 8
  resolved: 7
  partially_resolved: 1
  new_findings: 0
  serious: 0
  moderate: 0
  minor: 1
unresolved_findings:
  - id: B07-R06
    severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000214
    issue: Câu kết chưa giữ rõ giới hạn chỉ có thể than phiền dưới sức ép chính trị.
    resolution: Dưới sức ép chính trị, họ chỉ có thể than phiền như vậy.
term_recommendations:
  - source_term: law of war
    proposed_vi: luật chiến tranh
    alternative_vi: luật về chiến tranh
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000208]
    status: pending
    canon: false
  - source_term: noncombatants
    proposed_vi: người không tham chiến
    alternative_vi: người không trực tiếp tham chiến
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000208, YS-LN02/Text/part0030.xhtml/p000212]
    status: pending
    canon: false
risks:
  - Handoff và self-check đánh dấu R06 resolved nhưng còn thiếu chi tiết than phiền ở câu kết.
  - Chủ thể p000214–p000215 dựa trên ngữ cảnh cục bộ; cấp tổ chức Hậu cần chưa xác lập.
  - Hai thuật ngữ pháp lý còn pending/non-canon; không suy diễn khung pháp lý.
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_assign_R06_fix
```
