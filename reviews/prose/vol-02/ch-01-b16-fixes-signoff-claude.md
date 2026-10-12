# Signoff sửa lỗi — vol-02-ch-01-b16-fixes-signoff

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon).
- Phạm vi: chỉ `p000053` và `p000054` của `YS-LN02/Text/part0012.xhtml`, đối chiếu báo cáo `reviews/prose/vol-02/ch-01-b16-claude.md`, `handoffs/vol-02/ch-01-b16.yml`, `translations/vol-02/ch-01-b16.jsonl` và gói nguồn cục bộ b16.
- Không trích câu nguồn. Thuật ngữ vẫn là đề xuất tạm, không phải canon.

## 1. Xác nhận từng mục

| Mục | Kết quả | Căn cứ |
|---|---|---|
| M1 (p000054) | **Đã sửa** | Bản dịch hiện dùng "Xưởng Vũ khí Kỹ thuật", khớp mục `b02-technical-arsenal` (preferred_vi) trong `work/run-state/pending-terms.yml` và mục b16 `vol02-ch01-b16-technical-arsenal`. Không còn "Xưởng kỹ thuật". Handoff ghi `provisional_review_choices.technical_arsenal` cùng dạng. |
| M2 (p000053) | **Đã sửa** | Bản dịch hiện là "Ông chịu được chứ?". Đây là câu hỏi về mức sẵn lòng/chịu đựng việc dùng đơn vị khó trị, khớp phần nguồn hỏi "có chấp nhận được không". Không còn hỏi về độ chắc chắn. Khớp `provisional_review_choices.p000053_question` trong handoff. |

## 2. Kiểm tra nghĩa

- p000053: giữ đủ hai vế (đơn vị/tiểu đoàn khó trị + câu hỏi xác nhận), dấu ngoặc kép và dấu hỏi đúng; không thêm/bớt ý. "Tiểu đoàn đó" khớp nguồn.
- p000054: giữ đủ các ý: đơn vị tác chiến gan lì; chiến tranh cơ động hoàn hảo ở Dacia; từng ném bom nhà máy vũ khí; đơn vị tăng cường có khí tài tối tân từ cơ quan kỹ thuật; Trung tá von Lergen báo cáo huấn luyện, khẳng định kèm vẻ kinh ngạc không giấu nổi rằng Đế quốc không đơn vị nào sánh bằng. Phủ định, so sánh và thứ tự câu đúng. Chỉ thay đổi duy nhất so với lần review trước là nhãn M1; không phát sinh lỗi mới.
- Mã đoạn, trường `status`, `glossary_version`, `source_sha256` của hai đoạn không đổi so với b16 gốc; `notes` rỗng.

## 3. Kết quả

```yaml
role: reviewer
task_id: vol-02-ch-01-b16-fixes-signoff
state: done
segment_ids: [YS-LN02/Text/part0012.xhtml/p000053, YS-LN02/Text/part0012.xhtml/p000054]
files_written: [reviews/prose/vol-02/ch-01-b16-fixes-signoff-claude.md]
fixes_pass: true
M1: confirmed_fixed
M2: confirmed_fixed
remaining:
  serious: 0
  moderate: 0
  minor_in_scope:
    - {segment_id: p000054, issue: "'gan lì' nghiêng về ương bướng so với 'dauntless'; 'túi Zettour' có thể 'túi của Zettour' (m8 cũ, không bắt buộc)"}
  minor_out_of_scope_not_rechecked: "m1–m7, m9 cũ không thuộc phạm vi signoff này; không xét lại"
risks:
  - "T7 (đơn vị tăng cường) vẫn pending, độ chắc 0.5; giữ đồng bộ b13–b16, không nâng canon."
  - "Mục pending b16 cho Technical Arsenal ghi confidence 0.5 với alternatives Kho Vũ khí Kỹ thuật; cùng nhãn với b02 nên không còn lệch hai lô."
validator: not_run
diff_check: not_run
commit: null
next_action: proceed_to_commit_b16  # M1/M2 đã đóng; không còn mục nghiêm trọng hoặc vừa; coordinator quyết định có xử lý các mục nhẹ trước khi commit hay không. Không có hard stop.
```
