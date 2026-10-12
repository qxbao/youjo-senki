# Signoff thuật ngữ b07 — vol-02-ch-02-b07-term-signoff

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa file khác). Không trích văn bản nguồn.
- **Phạm vi:** chỉ p000158, p000159, đối chiếu MOD-1 trong `ch-02-b07-fixes-signoff-claude.md`, handoff b07, gói nguồn đã chuẩn bị, bản dịch b07 và ledger `work/run-state/pending-terms.yml`. Không đọc batch khác.

## Kết luận: `pass` (serious 0, moderate 0)

## MOD-1 đã giải quyết
- p000158 và p000159 nay dùng "Cụm tập đoàn quân phương Bắc" (hạ chữ "tập đoàn quân"), trùng p000157 và ledger `vol02-ch02-b07-northern-army-group`.
- Handoff ghi `army_group_consistency_followup` với changed_segments đúng p000158, p000159; validator và diff_check đều pass.

## Đối chiếu nghĩa (nguồn ↔ bản dịch)
- **p000158:** giữ ý các cuộc tập kích liên tục vào kho tiếp tế, điều kiện "một khi bị buộc dàn mỏng quân lực", rồi pháp sư không quân địch tấn công. Chủ thể và trình tự không đổi.
- **p000159:** giữ ý đã trúng đòn hai lần, vừa đủ duy trì tiếp tế, không chịu nổi thêm gián đoạn lớn, phải chặn các cuộc tập kích kho, và nhiệm vụ bảo vệ tuyến tiếp tế của Tiểu đoàn Viper. Không thêm hay mất ý.
- Đại từ "Họ" trong p000159 chỉ rõ cụm tập đoàn quân, không mơ hồ.

## Minor (không chặn)
- Ledger `vol02-ch02-b07-northern-army-group` chỉ liệt kê p000157 trong `segment_ids`. Nên bổ sung p000158, p000159 vào danh sách để truy vết, nhưng không ảnh hưởng bản dịch.

## Rủi ro
- Thuật ngữ vẫn là đề xuất tạm (`pending`, confidence 0.5), chưa phải canon. Ba đoạn nay nhất quán nên đổi sau này chỉ cần thay đồng loạt.

## YAML
```yaml
task_id: vol-02-ch-02-b07-term-signoff
state: done
reviewed_segments: 2
serious: 0
moderate: 0
findings:
  - {severity: minor, segment_ids: [p000158, p000159], issue: "ledger northern-army-group chỉ liệt kê p000157", suggestion: "bổ sung segment_ids"}
risks: [thuật ngữ vẫn là đề xuất tạm, chưa canon]
next_action: coordinator có thể nâng b07 theo quy trình; tùy chọn bổ sung segment_ids vào ledger
```
