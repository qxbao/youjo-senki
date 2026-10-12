# Signoff sửa lỗi — vol-02-ch-01-b09-fixes-signoff (Claude)

- Phạm vi: 11 đoạn đã sửa của b09 (`YS-LN02/Text/part0010.xhtml/`): p000219, 221, 224, 225, 227, 230, 234, 235, 238, 242, 243.
- Đã đọc: báo cáo gốc `ch-01-b09-claude.md`, handoff b09, `translations/vol-02/ch-01-b09.jsonl`, `work/vol-02/batches/ch-01-b09-source.jsonl`, mục b09 trong `work/run-state/pending-terms.yml`. Không đọc lô khác. Không sửa bản dịch, handoff, ledger hay canon. Không chép văn bản nguồn; mọi thuật ngữ là đề xuất tạm, **không phải canon**.

## 1. Xác nhận M1–M4

| Mã | Kết quả | Căn cứ |
|---|---|---|
| M1 — đại từ Tanya | **Đã sửa.** | Không còn “cô” trong toàn b09. Trần thuật dùng “nó”, lặp “Tanya” hoặc lược chủ ngữ ở nơi “nó” dễ nhầm (p000221, p000225: “của Tanya”, p000243). Nội tâm ngôi nhất p000234 dùng “mình”. Khớp DEC-P01-001 và ledger. |
| M2 — súng ngắn | **Đã sửa.** | p000225 nay là “chỉ với súng ngắn…”, thể hiện giới hạn vũ khí thay cho lượng. Hơi mạnh hơn nguồn một chút (nguồn: gần như chỉ có súng ngắn) nhưng chấp nhận được, không đổi ý. |
| M3 — biệt danh -guchi | **Đã sửa.** | p000238: “gã Khốn-guchi ở Imphal” giữ hậu tố chơi chữ, giữ cấu trúc “tiền tố chửi + hậu tố”, giữ Imphal, không thêm lore/chú thích. Mức tục đã nhẹ hơn nguồn; ghi nhận là lựa chọn tạm (độ tin cậy 0,5), không cần sửa. |
| M4 — First Lieutenant | **Đã sửa.** | p000219: “Trung úy Weiss”, khớp bản đồ cấp bậc tạm của tập và p000239. |

## 2. Thuật ngữ tạm trên các đoạn đã sửa (không canon)

| Thuật ngữ | Đoạn | Bản dịch hiện tại | Đánh giá |
|---|---|---|---|
| booby trap | p000227 / p000230 | “Đặt bẫy đi.” / “gài bẫy nổ vào một cái xác” | Khớp ledger; “bẫy nổ” có căn cứ từ ngữ cảnh p000230, không suy diễn thành “mìn”. Chấp nhận. |
| aerial mage | p000235 | “Tiểu đoàn Pháp sư Không quân 203” | Nhất quán với các lô trước; giữ, ghi rủi ro toàn cục ở mục 5. |
| blitzkrieg tactics | p000238 | “chiến thuật chiến tranh chớp nhoáng” | Khớp đề xuất; ít suy diễn. Chấp nhận. |
| air fleet | p000242 | “Đội bay của chúng ta…” | Trung tính, độ tin cậy 0,4; không gây hiểu sai trong ngữ cảnh. Chấp nhận như pending. |

Không phát hiện chỗ nào tự nâng thuật ngữ thành canon.

## 3. Nhấn mạnh và thay đổi nghĩa ngoài ý muốn

- Nhấn mạnh (DEC-P01-002): b09 vẫn chỉ có `*…*` ở p000219 và p000241; các đoạn đã sửa không thêm/bớt dấu nhấn mạnh. Đạt.
- Không phát hiện đảo phủ định, đổi chủ thể, đổi đối tượng hay thay đổi logic điều kiện trong 11 đoạn. Quan hệ “anh ta” (p000243, Weiss) và “nó” (Tanya) không gây nhầm.
- p000221: câu cuối vẫn giữ đúng ý “theo góc nhìn của chính Tanya”.

## 4. Còn lại sau sửa

- **Nghiêm trọng: 0.**
- **Vừa: 0.** Cả bốn mục M1–M4 đã giải quyết.
- **Nhẹ (không chặn commit, tùy chọn):**
  - p000225: câu “kết cục … sách giáo khoa Dacia … đã thành hiện thực” vẫn hơi lủng củng (L6 cũ).
  - p000230: dấu chấm phẩy làm câu hơi gãy (L10 cũ).
  - p000234: “Tình hình căng thẳng thấp” sát chữ, dễ đọc lệch; “cảnh cáo” hơi nặng (L2 cũ).
  - p000235: “thành hàng dọc” thêm ý “cột dọc”; “cổ đại” hơi cực đoan (L3 cũ).
  - p000238: mức tục của biệt danh nhẹ hơn nguồn (đã ghi nhận ở M3).

## 5. Rủi ro

- Biệt danh p000238 và “đội bay” p000242 là lựa chọn tạm độ tin cậy thấp; nếu xuất hiện lại ở lô sau cần áp dụng nhất quán theo ledger.
- “Pháp sư không quân” có thể gợi binh chủng; chỉ nên xét lại toàn cục, không đổi riêng trong b09.
- Đoạn p000232 (xưng hô, chủ thể không rõ) ngoài phạm vi signoff này, không đánh giá lại.

## 6. Kết luận (YAML)

```yaml
role: reviewer
task_id: vol-02-ch-01-b09-fixes-signoff
state: done
segment_ids: [p000219, p000221, p000224, p000225, p000227, p000230, p000234, p000235, p000238, p000242, p000243]
review_path: reviews/prose/vol-02/ch-01-b09-fixes-signoff-claude.md
files_written: [reviews/prose/vol-02/ch-01-b09-fixes-signoff-claude.md]
m1_m4: {M1: resolved, M2: resolved, M3: resolved, M4: resolved}
remaining: {serious: 0, moderate: 0, minor: 5}
fixes_pass: true
pending_status: provisional_non_canon
risks:
  - "p000238 biệt danh và p000242 'đội bay' độ tin cậy thấp; áp dụng nhất quán nếu lặp lại"
  - "'pháp sư không quân' chỉ nên xét lại toàn cục"
next_action: coordinator_may_commit_b09   # lỗi nhẹ tùy chọn, không chặn
```
