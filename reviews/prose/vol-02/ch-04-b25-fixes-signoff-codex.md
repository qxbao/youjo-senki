# Sign-off sửa lỗi vol-02-ch-04-b25

Kết quả: xác nhận đã xử lý B25-F01, B25-F06, B25-F07, B25-F08 và B25-F09. Không phát hiện lỗi nghiêm trọng/vừa mới trong chín đoạn chịu ảnh hưởng của năm finding và lựa chọn marine mages. Đây là sign-off giới hạn cho các mục được giao, không phải lượt review mới toàn lô.

Đầu vào: agents/shared.md, agents/reviewer.md, config/translation-pipeline.yml, handoff b25, năm canon reference được handoff liệt kê, riêng chapter4_b25_translation_proposals, package nguồn b25 đã chuẩn bị, bản dịch b25 và báo cáo prose b25 ban đầu. Hash package và năm canon reference khớp handoff; metadata hash nguồn khớp và 34 mã đoạn nguồn/bản dịch tương ứng. Chỉ dùng ngữ cảnh p000413–p000446; không mở lô khác, EPUB/PDF hoặc chạy worker.

| ID | Đoạn (YS-LN02/Text/part0024.xhtml/) | Kết quả đối chiếu |
| --- | --- | --- |
| B25-F01 | p000416, p000417, p000419, p000420 | Đã dùng “nó” cho trần thuật về Tanya, “mình” cho nội tâm tự quy chiếu; việc lược đại từ ở đầu p000417 không đổi chủ thể. Giữ “tôi” trong khẩu lệnh p000418 phù hợp giới hạn DEC-P01-001. Dấu nhấn mạnh p000416 vẫn đúng phạm vi. |
| B25-F06 | p000427 | Va chạm được xác định đã xảy ra; mức xấp xỉ gắn với hướng trực diện. Giữ khí thế của Tiểu đoàn 203 và liên hệ với việc không giảm tốc p000424. |
| B25-F07 | p000431 | Lính thủy đánh bộ là nòng cốt của đội xung kích, phù hợp thành phần đội phản kích p000432. Giữ mục tiêu chiếm lại đài chỉ huy thứ hai. |
| B25-F08 | p000437 | Đã phân biệt bộ phận tiên phong với các thành viên phía sau, không gán thành hậu phương; động tác cơ động trên không giữ bình diện chiến đấu. Giữ khả thể ở nhóm tiên phong và mục đích khắc phục điểm yếu của huấn luyện. |
| B25-F09 | p000446 | Đã khôi phục cấp lữ đoàn và tính lâm thời, giữ thành phần sĩ quan/hạ sĩ quan được huy động cùng nhiệm vụ tăng viện cho lính thủy đánh bộ. Không thêm quân số hoặc biên chế đầy đủ. |

Tại p000433, “pháp sư tác chiến trên biển” khớp đề xuất vol02-ch04-b25-marine-mages trong mục pending được phép đọc. Cách gọi trung tính giữ bối cảnh tác chiến cùng lính thủy đánh bộ bên trong tàu, không khẳng định nhánh quân. Chấp nhận để tiếp tục dưới trạng thái pending/provisional, không nâng canon. Các phương án “pháp sư hải quân” và “pháp sư thủy quân lục chiến” vẫn cần căn cứ biên chế mà phạm vi này chưa cung cấp. Độ chắc chắn thấp về nhánh quân; đủ căn cứ để giữ cách diễn đạt tạm hiện tại.

B25-F02–B25-F05 không được đánh giá lại hoặc giải quyết trong lượt này; giữ deferred theo yêu cầu. Không đưa ra kết luận mới về các mục đó hoặc thuật ngữ magazine. Ghi chú trong bản dịch p000433 có dẫn đề xuất lô khác; không kiểm tra tham chiếu ấy và không dùng nó làm căn cứ sign-off.

```yaml
role: reviewer
task_id: vol-02-ch-04-b25
state: done
review_path: reviews/prose/vol-02/ch-04-b25-fixes-signoff-codex.md
files_written: [reviews/prose/vol-02/ch-04-b25-fixes-signoff-codex.md]
segment_ids:
  - YS-LN02/Text/part0024.xhtml/p000416
  - YS-LN02/Text/part0024.xhtml/p000417
  - YS-LN02/Text/part0024.xhtml/p000419
  - YS-LN02/Text/part0024.xhtml/p000420
  - YS-LN02/Text/part0024.xhtml/p000427
  - YS-LN02/Text/part0024.xhtml/p000431
  - YS-LN02/Text/part0024.xhtml/p000433
  - YS-LN02/Text/part0024.xhtml/p000437
  - YS-LN02/Text/part0024.xhtml/p000446
resolved_findings: [B25-F01, B25-F06, B25-F07, B25-F08, B25-F09]
unresolved_in_scope: []
unresolved_findings: [B25-F02, B25-F03, B25-F04, B25-F05]
deferred_findings: [B25-F02, B25-F03, B25-F04, B25-F05]
counts:
  affected_segments_checked: 9
  fixes_verified: 5
  resolved: 5
  unresolved_in_scope: 0
  serious: 0
  moderate: 0
  new_serious: 0
  new_moderate: 0
  minor_reviewed: 0
  minor_deferred: 4
  unresolved_total_including_deferred: 4
  provisional_choices_verified: 1
findings: []
term_recommendations:
  - id: vol02-ch04-b25-marine-mages
    proposed_vi: pháp sư tác chiến trên biển
    segment_ids: [YS-LN02/Text/part0024.xhtml/p000433]
    status: pending
    action: retain_provisional
    canon_promotion: false
risks:
  - Nhánh quân của pháp sư p000433 chưa được xác nhận; lựa chọn vẫn là đề xuất.
  - Cách dịch cấp lữ đoàn p000446 chưa là canon; không suy ra quân số hoặc biên chế.
  - F02–F05 còn deferred và không được đánh giá lại trong lượt này.
  - Sign-off chỉ bao phủ các mục được giao; không xác minh tính nhất quán giữa các lô hoặc tham chiếu lô khác trong notes.
input_hash_check: pass
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_record_scoped_signoff_keep_F02_F05_deferred_and_marine_mages_provisional
```
