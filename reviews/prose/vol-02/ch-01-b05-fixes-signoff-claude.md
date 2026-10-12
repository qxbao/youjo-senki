# Signoff sửa lỗi — vol-02-ch-01-b05 (Claude)

- Task: `vol-02-ch-01-b05-fixes-signoff`
- Đối chiếu: `reviews/prose/vol-02/ch-01-b05-claude.md` (M1–M6, L1–L15, T1–T4), `handoffs/vol-02/ch-01-b05.yml` (working tree, chưa commit), `translations/vol-02/ch-01-b05.jsonl`, source package cục bộ `work/vol-02/batches/ch-01-b05-source.jsonl` (bị Git bỏ qua, chỉ đọc tại chỗ).
- Phạm vi: đúng 16 segment được giao (p000088, 089, 090, 091, 092, 095, 097, 098, 099, 101, 105, 106, 109, 110, 115, 118). Không đọc batch khác; không sửa bản dịch, handoff, ledger hay canon.
- Mọi lựa chọn dưới đây là **đề xuất tạm, không phải canon**. Báo cáo không trích văn bản nguồn.

## Kết luận

**Cả 6 lỗi vừa M1–M6 đều đã được xử lý đạt.** Không còn lỗi nghiêm trọng hay lỗi vừa. Còn một vài lỗi nhẹ không chặn commit và một điểm bất đồng bộ ở handoff (xem bên dưới).

| Mức | Số lượng còn lại |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 0 |
| Nhẹ (hành động được) | 3 (N1–N3) |

## Kiểm tra từng lỗi vừa

| Mã | Segment | Kết quả | Ghi chú |
|---|---|---|---|
| M1 | p000089, p000092, p000095, p000118 | **Đạt** | Serebryakov nhất quán "Thiếu úy" ở mọi chỗ trong phạm vi; khớp lựa chọn tạm `serebryakov_rank`. Không có đổi nhân vật hay cấp. |
| M2 | p000092 | **Đạt** | Đã bọc `*...*` đúng vế mà nguồn nhấn (từ phần khen sự chuẩn bị đến phần nhận lỗi gọi "sư đoàn"), không tràn sang câu đầu/cuối; từ "chính" thừa đã bỏ. Nguồn 1 chỗ nhấn, bản dịch 1 cặp `*`; 15 đoạn còn lại trong phạm vi không có `*` thừa. |
| M3 | p000095 | **Đạt** | Cả hai chỗ "cô" đã đổi thành "Tanya"; chủ thể nhất quán với p000092. Ý chuỗi "chặt đầu → thổi bay tàn quân" giữ nguyên. |
| M4 | p000088, p000115 | **Đạt** | Cả hai dùng "sĩ quan phụ tá", khớp sổ `vol02-ch01-b03-adjutant`. |
| M5 | p000109 | **Đạt** | Chủ thể trở lại là kẻ ra đòn (phải lường trước bị đánh trả); hợp mạch p000107. Nghĩa, hàm ý không còn đảo. "phẩm cách tối thiểu" cũng sửa được L10 một phần. |
| M6 | p000088, p000105, p000110, p000115 | **Đạt** | Độc thoại nội tâm một chủ thể dùng "mình" nhất quán (p000088, 105, 110, 115); "chúng tôi/tôi" chỉ còn ở trần thuật hành động tập thể (p000091, 097, 098, 099, 118) và lời thoại (p000091), khác bình diện, chấp nhận được. |

Giọng mỉa mai, phủ định, trình tự chiến đấu, logic "họ không biết chiến tranh là gì" và chủ thể lời thoại không bị ảnh hưởng bởi các lần sửa.

## Lỗi nhẹ trước đó (đối chiếu)

Đã xử lý: L1 (p000088), L2 (p000091 "đám ô hợp"), L3 (p000097 "gối cắm kim"), L4 ("đồng loạt" đã bỏ), L5/T2 (p000097 "đã cố định thuật thức"), L6 (p000098 "đánh tan"), L7 (p000099 "phòng không"), L8 (p000105), L9 (p000106), L10 (p000109 "phẩm cách"), L11 (p000110), L12 (p000115 "thực ra"), L13 (p000118 "tấn công mặt đất bằng ma pháp"), L14 (p000090, p000101 "Thiếu tá" viết hoa), L15 (p000089 "Thiếu úy").

Thuật ngữ T1, T3, T4 giữ như đề xuất: "người theo chủ nghĩa hậu cấu trúc" (p000088), "lựu đạn chống mục tiêu mặt đất" (p000097), "đội hình vuông bộ binh" (p000118). T2 đã đổi sang "đã cố định thuật thức" theo đề xuất.

## Lỗi nhẹ còn lại (không chặn commit)

- **N1 — handoff lệch bản dịch (p000097):** `review_coordination.provisional_choices` trong handoff vẫn ghi `formula-fixed` = "gắn thuật thức" (độ chắc 0.45) trong khi bản dịch và `provisional_review_choices` cùng handoff đã dùng "đã cố định thuật thức". Coordinator nên đồng bộ mục này (và ledger/`pending-terms.yml`) khi ghi lại; đây vẫn chỉ là đề xuất pending.
- **N2 — p000091:** "năm vạn" mang sắc thái Hán Việt hơn "50.000"; không sai nghĩa, chỉ cần coordinator kiểm đồng bộ cách ghi số lượng với b01–b04 (tôi không đọc các batch ấy).
- **N3 — p000099:** vế "với bộ binh bị buộc phải dùng vũ khí cơ bản để phòng không…" hơi dài, dễ đọc vấp; chỉ là gợi ý tách câu nếu translator muốn, không bắt buộc.

## Xác nhận validator / diff-check

Không chạy lại (đúng phạm vi). Handoff có ghi `status: fixes_reported_validator_pass`, nhưng đó là lời khai của translator/coordinator; trong dữ liệu được cấp tôi **không thấy** đầu ra validator hay diff-check để tự xác nhận. Việc tôi đã kiểm trực tiếp: nội dung 16 segment khớp mô tả sửa, không có `*` thừa, không còn mốc "Trung úy/cô/tùy viên" nào trong phạm vi.

## Rủi ro

- Đồng bộ chéo với b01–b04 (Serebryakov, "mình/tôi", "sĩ quan phụ tá") chưa kiểm được; coordinator rà theo ledger.
- Không có quyết định ảnh hưởng cốt truyện; không cần hỏi người dùng.

## next_action

Coordinator xem N1 (đồng bộ ghi chú handoff/ledger cho formula-fixed), chạy validator/diff-check cuối cùng nếu chưa có đầu ra lưu lại, rồi có thể commit batch b05. Không cần thêm vòng phản biện.

## YAML tóm tắt

```yaml
role: reviewer
task_id: vol-02-ch-01-b05-fixes-signoff
state: done
review_of: reviews/prose/vol-02/ch-01-b05-claude.md
scope_segments: [p000088, p000089, p000090, p000091, p000092, p000095, p000097, p000098, p000099, p000101, p000105, p000106, p000109, p000110, p000115, p000118]
files_written:
  - reviews/prose/vol-02/ch-01-b05-fixes-signoff-claude.md
counts:
  serious: 0
  moderate: 0
  minor_remaining: 3
moderate_fixes:
  M1: pass
  M2: pass
  M3: pass
  M4: pass
  M5: pass
  M6: pass
all_moderate_fixes_pass: true
unresolved_serious_or_moderate: 0
minors:
  - {id: N1, segment_id: p000097, issue: "handoff provisional_choices còn ghi phương án formula-fixed cũ, lệch bản dịch", action: "coordinator đồng bộ handoff/ledger"}
  - {id: N2, segment_id: p000091, issue: "sắc thái Hán Việt của cách ghi số lượng", action: "kiểm đồng bộ với b01-b04"}
  - {id: N3, segment_id: p000099, issue: "câu dài, tùy chọn tách", action: optional}
validator: not_run_not_evidenced
diff_check: not_run_not_evidenced
pending_status: provisional_not_canon
commit: null
next_action: "coordinator xử lý N1, xác nhận validator/diff-check rồi commit b05; không cần vòng phản biện thêm"
```
