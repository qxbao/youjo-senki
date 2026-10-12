# Signoff sửa lỗi — vol-02-ch-01-b07-fixes-signoff (Claude)

- Phạm vi: 8 đoạn đã sửa `p000155, p000157, p000159, p000160, p000162, p000165, p000168, p000173` (tiền tố `YS-LN02/Text/part0010.xhtml/`).
- Đầu vào: `reviews/prose/vol-02/ch-01-b07-claude.md`, `handoffs/vol-02/ch-01-b07.yml`, `translations/vol-02/ch-01-b07.jsonl` hiện tại, `work/vol-02/batches/ch-01-b07-source.jsonl`, mục b07 trong `work/run-state/pending-terms.yml` (chỉ đọc). Không đọc bản dịch batch khác; không sửa tệp nào ngoài báo cáo này. Không chép văn bản nguồn. Mọi thuật ngữ vẫn là **đề xuất tạm, không phải canon**.

## 1. Ba lỗi vừa

| Mã | Đoạn | Kết quả | Ghi chú |
|---|---|---|---|
| M1 | p000160 | **Đã sửa** | "súng ngắn" đã đổi thành "vũ khí cá nhân bên ta": nghĩa rộng, đúng loại vũ khí mang theo, không thu hẹp thành một loại súng. Khớp mục ledger `sidearms`. |
| M2 | p000159 | **Đã sửa** | "kết giới phòng ngự" đã đổi thành "lớp vỏ phòng ngự", khớp b05 và ledger `defensive-shell`. |
| M3 | p000165 | **Đã sửa** | Bỏ "điều khiển nó"; chủ thể "Tanya" đứng rõ trước "nạp… rồi lượn xuống gọn ghẽ". Không còn mơ hồ đối tượng. Weiss vẫn được tách bằng "anh". |

## 2. Kiểm tra riêng p000157 (có phải "defensive shell" không)

**Kết luận: không.** Đối chiếu source package: p000157 không chứa khái niệm lớp vỏ/phòng ngự. Cụm in nghiêng (bản dịch: `*thứ đó*`) là đại từ chỉ vào đội hình/thế bắn của địch ở p000155–p000156; vế sau nói pháp sư bị bắn hạ bởi thứ đó. Khái niệm "defensive shell" chỉ nằm ở p000159. Do đó:

- Bản dịch p000157 đúng như translator giải thích; không cần đổi sang "lớp vỏ phòng ngự". Nghĩa, người nói (Tanya gọi Weiss là Trung úy), nhấn mạnh `*...*` đúng một chỗ, phạm vi đúng DEC-P01-002 đều đạt.
- Ledger `vol02-ch01-b07-defensive-shell` chỉ liệt kê p000159 là **đúng**. Khuyến nghị trước đây của tôi (ghi cả p000157 trong `term_recommendations` và M2) là **nhầm**; xin coi là rút lại. Đây là sai sót của báo cáo review gốc, không phải của bản dịch hay coordinator.

## 3. Năm thay đổi nhẹ — kiểm tra nghĩa ngoài ý muốn

- **p000155 (formation wording):** "thế bắn theo đội hình khép sát" — khớp đề xuất T3. Người nói vẫn là Weiss, "ra lệnh cho đại đội tránh họ" đúng. Không lệch nghĩa. Pass.
- **p000160 (tercio + tone):** "đâm sầm vào đội hình tercio với giáo dài và súng hỏa mai" sát nguồn hơn bản cũ (kỵ binh bị đâm vào, phủ định "có phải… đâu" còn nguyên). "đáng cười mà tàn khốc" thay cho "khốc liệt đến nực cười" khớp sắc thái mỉa mai, không khuếch đại. "đội hình vuông bộ binh", mặt trận Rhine, Viễn Đông, Akitsushima và Liên bang giữ nguyên. Pass.
- **p000159 (nickname):** "ngài Lẽ Thường" khớp mục ledger `mr-common-sense`; vẫn đối lập "ngài" / "cậu", vẫn một lần giải thích. Không đổi nghĩa. Pass.
- **p000162:** "gỡ lại danh dự" thay "gỡ tội" — bỏ hàm ý tội danh; "phóng một thuật thức thẳng vào giữa đội hình" giữ nguyên. Pass.
- **p000168:** "quân địch" thay "chúng" đã bỏ sắc thái khinh miệt; mệnh đề nhượng bộ, "binh sĩ Dacia", "bị nổ tung" đúng. Pass. Ghi chú không bắt buộc: câu đầu của đoạn dùng "họ" cho phía Đế quốc, câu sau dùng "họ" cho địch (đứng sau cụm "quân địch" nên đọc được). Không cần sửa.
- **p000173:** đã bỏ "vừa"; không còn suy diễn thời điểm. Dấu chú thích ² được giữ; "nó" trần thuật cho Tanya theo quy ước, nội dung không đổi. Pass.

## 4. Còn lại sau sửa

- Nghiêm trọng: **0**. Vừa: **0**. Nhẹ cần sửa (actionable): **0**.
- Nhẹ còn ngoài phạm vi signoff này, không chặn: L6 (p000177 "Tướng quân"/"Bộ Tổng tham mưu"), L8 (p000178 hơi nặng chữ), L9 (p000172 "đơn vị", p000166 lược chủ ngữ). Không nằm trong 8 đoạn; không kiểm lại ở đây. Coordinator tự quyết có áp dụng hay không.

## 5. Rủi ro

- **R1:** "lớp vỏ phòng ngự" vẫn là đề xuất tạm; nếu canon sau này chọn thuật ngữ khác cho phòng ngự ma pháp thì cần đồng bộ cả chương.
- **R2:** L6 và R3 của báo cáo gốc cần đối chiếu chéo với batch khác (tôi không đọc).
- **R3:** Confidence của tercio khác nhẹ giữa báo cáo gốc (0.6) và ledger (0.55); không ảnh hưởng nghĩa.
- **R4:** "Quân đoàn Công vụ" (p000177) vẫn bất định cao; ngoài phạm vi signoff này.

## 6. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-01-b07-fixes-signoff
state: done
segment_ids: [p000155, p000157, p000159, p000160, p000162, p000165, p000168, p000173]
review_path: reviews/prose/vol-02/ch-01-b07-fixes-signoff-claude.md
files_written: [reviews/prose/vol-02/ch-01-b07-fixes-signoff-claude.md]
fixes_pass: true
counts: {serious: 0, moderate: 0, minor_actionable: 0}
verified:
  M1_p000160_sidearms: fixed
  M2_p000159_defensive_shell: fixed
  M3_p000165_subject: fixed
  p000157_defensive_shell: not_applicable  # chỉ thứ đó/đội hình địch; ledger chỉ p000159 là đúng; rút lại khuyến nghị cũ
minor_changes_checked: [p000155, p000160, p000159_nickname, p000162, p000168, p000173]  # không đổi nghĩa ngoài ý muốn
term_status: provisional_non_canon
risks: [R1, R2, R3, R4]
commit: null
next_action: coordinator_accept_b07_fixes_and_proceed  # không cần sửa thêm trong 8 đoạn; L6/L8/L9 tùy chọn
```
