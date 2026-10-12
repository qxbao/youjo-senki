# Sign-off sửa lỗi — vol-02-ch-01-b11-fixes-signoff

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon).
- Phạm vi: `p000276`, `p000277`, `p000293`, `p000296` và p000287 làm tham chiếu cấp bậc. Căn cứ: báo cáo b11 gốc, handoff b11, `translations/vol-02/ch-01-b11.jsonl`, gói nguồn b11 cục bộ.
- Không trích câu nguồn. Mọi lựa chọn bên dưới vẫn là đề xuất tạm, không phải canon.

## 1. Kết quả từng mục

| Mục | Đoạn | Kết quả | Ghi chú |
|---|---|---|---|
| M1 | p000293 (tham chiếu p000287) | **Đạt** | Bản dịch dùng "Trung úy Weiss", khớp bản đồ cấp bậc tạm và p000287 ("Trung úy"). Không còn "Thượng úy". |
| M2 | p000277 | **Đạt** | "khái niệm cấm ánh sáng ban đêm" — không còn nghĩa sự cố mất điện; khớp mạch đèn có thể là mồi nhử và lựa chọn tạm trong handoff. |
| M3 | p000276, p000277 | **Đạt** | p000276 và các mệnh đề nội tâm của p000277 dùng "mình". Mệnh đề trần thuật cuối p000277 giữ "nó", đúng việc nguồn đổi ngôi ngay trong đoạn. Lời thoại không bị ảnh hưởng. |
| M4 | p000296 | **Đạt** | Đã bỏ "bản thân"; "dù thiếu kinh nghiệm" không chốt chủ thể là phó chỉ huy hay cấp trên, giữ độ mở của nguồn. |
| Khai sáng | p000277 | **Đạt** | "được khai sáng" khớp lựa chọn pending (confidence 0,5) và khớp "Khai sáng" ở p000293; giữ được trò chơi chữ ánh sáng. |

## 2. Còn lại

- Nghiêm trọng: **0**
- Vừa: **0**
- Nhẹ: **1 trong phạm vi sign-off**, không chặn commit.
  - p000296: "quả có mắt nhìn người" vẫn khẳng định mạnh hơn sắc thái dè dặt của nguồn (L2 trong báo cáo gốc). Có thể đổi "có vẻ có mắt nhìn người" nếu tiện.
- Các mục nhẹ L3–L9 ngoài phạm vi sign-off này (p000278, p000280, p000281, p000294, p000298…) không được kiểm lại ở đây; trạng thái giữ như báo cáo gốc.

## 3. Rủi ro

- p000287: "Lieutenant" trần, người nhận có thể là Weiss hoặc Serebryakov (bất định khoảng 40%). "Trung úy" chỉ chắc nếu là Weiss; giữ tạm và đã ghi ở sổ pending.
- p000296: chủ thể của "thiếu kinh nghiệm" vẫn mơ hồ theo nguồn; bản dịch hiện giữ mơ hồ, không cần xử lý thêm.
- Handoff có khóa `provisional_review_choices` bị lặp hai lần (nội dung gần như trùng, khác chỉ ở lời giải thích). Nên coordinator dọn thành một khối khi ghi ledger; không ảnh hưởng bản dịch.
- Mọi lựa chọn (Trung úy, cấm ánh sáng ban đêm, mình, bỏ bản thân, được khai sáng) vẫn là pending non-canon. Không cần hỏi người dùng.

## 4. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-01-b11-fixes-signoff
state: done
review_path: reviews/prose/vol-02/ch-01-b11-fixes-signoff-claude.md
segment_ids: [p000276, p000277, p000293, p000296, p000287(ref)]
fixes_pass: true
confirmed: {M1: pass, M2: pass, M3: pass, M4: pass, enlightened_p000277: pass}
remaining: {serious: 0, moderate: 0, minor: 1}
risks:
  - "p000287 người nhận Lieutenant chưa chắc là Weiss"
  - "p000296 chủ thể mơ hồ giữ nguyên theo nguồn"
  - "handoff lặp khóa provisional_review_choices"
pending_status: provisional_non_canon
files_written: [reviews/prose/vol-02/ch-01-b11-fixes-signoff-claude.md]
next_action: "Coordinator dọn handoff, ghi lựa chọn tạm vào ledger rồi commit b11; mục nhẹ L2 tùy chọn."
```
