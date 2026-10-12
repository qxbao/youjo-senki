# Signoff sửa lỗi — vol-02-ch-01-b08-fixes-signoff (Claude)

- Phạm vi: 24 đoạn `YS-LN02/Text/part0010.xhtml/` p000179, 182, 183, 184, 185, 186, 190, 191, 192, 194, 197, 199, 200, 202, 206, 209, 210, 211, 212, 213, 214, 216, 217, 218. Đã đối chiếu 24/24.
- Đầu vào đã đọc: báo cáo phản biện gốc `reviews/prose/vol-02/ch-01-b08-claude.md`, handoff b08, `translations/vol-02/ch-01-b08.jsonl` hiện tại, source package b08 (`work/vol-02/batches/ch-01-b08-source.jsonl`). Không đọc bản dịch lô khác, không đọc nguồn ngoài package b08.
- Không chép câu nguồn. Mọi thuật ngữ là **đề xuất tạm, không phải canon**. Không sửa bản dịch, handoff, sổ pending hay canon.
- Các nhận định của báo cáo gốc cần chứng cứ ngoài b08 (bản đồ cấp bậc b04–b06, tiền lệ b01–b07, nguồn tập cho Type 97/95) được coi là **chưa kiểm chứng** ở đây; việc sign-off dựa trên tính nhất quán nội bộ b08, handoff và package b08. Lệch phạm vi của phản biện gốc (đọc nguồn ngoài package, tham chiếu lô khác) đã được handoff ghi nhận (`review_scope_note`); chỉ nhắc ở đây vì M1 và M2 gốc dựa vào đối chiếu b04–b07. Cả hai bản sửa trùng với `provisional_review_choices` trong handoff nên vẫn chấp nhận được.

## 1. Ba lỗi vừa gốc

| Mã | Đoạn | Kết quả | Ghi chú |
|---|---|---|---|
| M1 | p000200 | **Đã xử lý** | Weiss = Trung úy, Serebryakov = Thiếu úy; hai người hết cùng cấp. Khớp lựa chọn tạm trong handoff. p000202 vẫn “Trung úy Weiss” (nhất quán). Nghĩa lệnh (Weiss yểm trợ, Serebryakov tập hợp đại đội rồi theo) giữ nguyên. |
| M2 | p000202 | **Đã xử lý** | “lớp phòng hộ” → “lớp vỏ phòng ngự”, khớp handoff. Không đổi nghĩa; “chủ động tăng cường” giữ ý chủ ý làm dày lớp phòng ngự trước loạt bắn đoán trước. |
| M3 | p000210 | **Đã xử lý (còn một tồn đọng nhẹ, xem L-a)** | Ngữ pháp cụm nhấn mạnh đã sửa (“tốt hơn cả dự tính”). Vế kế hoạch đã được viết lại thành “trong chiến tranh, việc không diễn ra đúng kế hoạch vốn là chuyện thường”: đúng chiều, đúng mức khẳng định của nguồn (điều hiển nhiên), không còn bị yếu đi. Nghĩa “suôn sẻ thì tốt, không phải bàn” và “chưa từng mơ” giữ nguyên. |

## 2. Nhất quán thuật ngữ trong các lần xuất hiện được liệt kê

| Nhóm | Kết quả | Chi tiết |
|---|---|---|
| Sở chỉ huy / tổng hành dinh / sở chỉ huy dã chiến | Nhất quán | *command post* → “sở chỉ huy” (p000179, 184, 185 — cấp sư/lữ đoàn); *headquarters* → “tổng hành dinh” (p000186, 192, 197, 206, 211); *field HQ* → “tổng hành dinh dã chiến” (p000216), giữ liên hệ với “tổng hành dinh” ở p000186/211 theo đề xuất của phản biện gốc. p000182 “bộ chỉ huy”/“đầu não” là chuỗi chỉ huy chứ không phải địa điểm nên chấp nhận được. Chưa kiểm chứng được việc đây là cùng một địa điểm (nguồn không nói rõ) — vẫn là rủi ro đọc hiểu đã biết. |
| Cấp bậc / xưng hô | Nhất quán | Thiếu tá (p000183, 213); Trung úy Weiss (p000200, 202); Thiếu úy Serebryakov (p000200); “thưa Thiếu tá” (p000213); “Các vị” (p000209, 217); “cậu” (p000200); “cô” (p000194). Không phát hiện lệch chéo giữa các đoạn trong b08. |
| Chiến thuật trên không | Nhất quán | “ưu thế trên không”, “chiến thuật chặt đầu bộ chỉ huy” (p000182); “cơ động trên không để trinh sát bằng lực lượng” (p000202). Cách đọc “trinh sát bằng lực lượng” tránh sắc thái bạo lực của “bằng vũ lực”. |
| Liên lạc / tin đánh lừa | Nhất quán | “không mã hóa” (p000191, 192, 199), “không bảo mật” (p000197) tách đúng theo hai từ nguồn khác nhau; “tin đánh lừa” (p000192). Không còn “nghi binh”. |
| Type 97 / Type 95 | Nhất quán | Giữ nguyên tên mẫu, chỉ ở p000202; không thêm đối tượng suy diễn. |
| Nhập cảnh / Tuần tra biên giới | Nhất quán | “cơ quan quản lý nhập cảnh” (p000214), “kiểm tra nhập cảnh” (p000218), “Đội Tuần tra Biên giới của Quân đội Đế quốc” (p000217, viết hoa, đọc như đơn vị). Hết “xuất nhập cảnh”. |
| Quả cầu | Nhất quán | “quả cầu của mình” (p000199), duy nhất một lần trong danh sách. |
| Quân đội Dacia | Gần như nhất quán | “Quân đội Dacia” (p000197, 211). p000218 dùng “người Dacia” — xem L-c. |

## 3. Kiểm tra thay đổi nghĩa ngoài ý muốn

Không phát hiện thay đổi nghĩa ngoài ý muốn trong các bản sửa. Các đoạn có chỉnh sửa đều giữ đúng phủ định, đối tượng, người nói và logic. Nhấn mạnh `*...*` ở p000185, p000190, p000210: p000185 và p000190 đúng phạm vi nguồn (cả câu); p000210 xem L-a. Đại từ: “nó” cho Tanya trần thuật (p000217), “tôi” ở các đoạn ngôi nhất, “mình” ở p000185/p000199 giữ theo DEC-P01-001.

## 4. Tồn đọng

### Nghiêm trọng: 0
### Vừa: 0
### Nhẹ: 3 (đều là điều chỉnh tùy chọn, không chặn commit)

- **L-a — p000210, độ rộng cụm nhấn mạnh:** nguồn in nghiêng chỉ một cụm ngắn tương ứng “tốt hơn cả”; bản dịch hiện đưa cả “dự tính” vào `*...*`. Gợi ý: `*tốt hơn cả* dự tính` để đúng phạm vi DEC-P01-002 và đúng handoff (“keep the source emphasis span”). Rủi ro đọc hiểu thấp.
- **L-b — p000216, “lá cờ của nó”:** “nó” là đại từ quy ước cho Tanya (p000217), trong câu có Tanya nên dễ đọc nhầm; “lá cờ của sở chỉ huy ấy/lá cờ treo ở đó” rõ hơn (L13 gốc, chưa áp dụng).
- **L-c — p000218, “người Dacia”:** khác “Quân đội Dacia” ở p000197/211; chấp nhận được vì ngữ cảnh trò giả khách tham quan. Nếu coordinator muốn đồng bộ: “phía Dacia”/“quân Dacia”. Cũng còn các lỗi nhẹ L1–L15 gốc khác chưa áp dụng (ví dụ p000192 “điện báo viên”, p000197 “để Quân đội Đế quốc nghe được”); không nằm trong yêu cầu sign-off này và không ảnh hưởng nghĩa chính.

## 5. Báo cáo coordinator

```yaml
role: reviewer
task_id: vol-02-ch-01-b08-fixes-signoff
state: done
segment_ids_reviewed: 24   # p000179, 182, 183, 184, 185, 186, 190, 191, 192, 194, 197, 199, 200, 202, 206, 209, 210, 211, 212, 213, 214, 216, 217, 218
files_written:
  - reviews/prose/vol-02/ch-01-b08-fixes-signoff-claude.md
original_moderate_resolved: {M1_p000200: true, M2_p000202: true, M3_p000210: true}
fixes_pass: true
counts:
  checked_segments: 24
  original_moderate: 3
  resolved: 3
  remaining_serious: 0
  remaining_moderate: 0
  remaining_minor: 3   # L-a p000210 độ rộng nhấn mạnh, L-b p000216 "của nó", L-c p000218 "người Dacia"
risks:
  - "p000210: cụm nhấn mạnh rộng hơn nguồn một chút (từ 'dự tính'); tùy chọn thu hẹp."
  - "p000186/211/216: 'tổng hành dinh' vs 'tổng hành dinh dã chiến' có thể bị đọc thành hai nơi; nguồn không nói rõ."
  - "p000216: 'của nó' có thể bị đọc nhầm là của Tanya."
  - "M1/M2 dựa một phần vào bản đồ b04–b07 từ báo cáo gốc (chưa kiểm chứng ngoài b08); chấp nhận vì khớp lựa chọn tạm trong handoff."
  - "Mọi thuật ngữ pending vẫn là đề xuất tạm, không canon."
next_action: "Có thể commit b08. Tùy chọn trước khi commit: thu hẹp nhấn mạnh p000210 và làm rõ 'của nó' p000216; coordinator giữ các thuật ngữ trong pending-terms.yml ở trạng thái provisional_non_canon."
```
