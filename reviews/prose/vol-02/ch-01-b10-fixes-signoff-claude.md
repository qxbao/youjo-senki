# Signoff sửa lỗi vol-02-ch-01-b10 (task vol-02-ch-01-b10-fixes-signoff)

- Người phản biện: Claude (reviewer). Chỉ đọc: báo cáo b10 gốc, `handoffs/vol-02/ch-01-b10.yml`, `translations/vol-02/ch-01-b10.jsonl`, `work/vol-02/batches/ch-01-b10-source.jsonl`. Không sửa tệp nào ngoài báo cáo này.
- Phạm vi: p000244, p000254–p000265, p000267, p000268, p000274 (rút gọn `pNNNNNN` = `YS-LN02/Text/part0010.xhtml/pNNNNNN`). Không dẫn nguồn; thuật ngữ vẫn là đề xuất tạm, không canon.
- Kiểm tra toàn vẹn: hash gói nguồn khớp handoff (`af1f7fc9…c6d99`); 32 mã đoạn bản dịch trùng 32 mã nguồn, không trùng lặp; `source_sha256` từng dòng khớp; các đoạn trong phạm vi đều `status: draft`.

## 1. Kết luận

**fixes_pass: true.** Cả hai phát hiện mức vừa đã được sửa đúng. Các thuật ngữ đã áp dụng không làm đổi nghĩa. Không còn lỗi nghiêm trọng hay mức vừa.

## 2. Xác nhận hai phát hiện mức vừa

**V1 — p000264: ĐÃ SỬA.** Nguồn có đúng hai vùng `<em>` (câu nội tâm về bonus level; cặp câu hô tiến lên ở cuối). Bản dịch hiện bọc `*…*` cả hai vùng, gồm `*Tiến lên nào! Cứ tiến lên mãi!*` ở cuối. Phạm vi khớp từng vùng, không bọc thừa phần trần thuật ở giữa (DEC-P01-002 thỏa). Không đoạn nào khác trong phạm vi có `<em>` ngoài p000267, và p000267 vẫn đúng với `*chẳng*`.

**V2 — p000274: ĐÃ SỬA.** Không còn "cô" nào. Tanya trong trần thuật dùng "nó" (“Nó lướt đi…”, “trong lòng nó…”) và tên riêng ở chỗ cần rõ; bức ảnh gọi bằng "bức ảnh" / "bức ảnh ấy", không còn "nó" chỉ bức ảnh. Nhất quán với "nó" ở p000254, p000264 (DEC-P01-001). Câu “Nó lướt đi…” đứng ngay sau danh từ cuối là Tanya nên không còn mơ hồ.

## 3. Kiểm tra nghĩa của các thuật ngữ đã áp dụng (đề xuất tạm, không canon)

| Thuật ngữ nguồn | Bản dịch hiện tại | Mã đoạn | Đánh giá |
|---|---|---|---|
| air fleet / Seventh Air Fleet | "đội bay" / "đội bay số 7" | p000244, p000267 | Giữ nghĩa là lực lượng không trung tách biệt với tiểu đoàn pháp sư; p000267 không thêm số hiệu (đúng nguồn). Chưa xác định cấp tổ chức. |
| Aerial Mage Battalion | "Tiểu đoàn Pháp sư Không quân 203" | p000265, p000267 | Giữ để nhất quán liên tập; không đổi nghĩa so với lựa chọn tạm trước. Rủi ro "Không quân" như binh chủng đã được ghi ở báo cáo gốc 4.2. |
| White Silver | "Bạch Ngân" | p000274 | Ổn, đặt trong ngoặc kép, nghĩa giữ nguyên; tránh "Bạch Kim". |
| bonus level | "màn chơi thưởng thêm" | p000264 | Giữ nghĩa và nhấn mạnh. |
| Eastern Army Group | "Cụm tập đoàn quân phía Đông" | p000267 | Đúng nghĩa; tránh được "Phương Đông" văn hóa. |
| Seventeenth Army | "Tập đoàn quân số 17" | p000267 | Đúng. |
| Dacian Army | "Quân đội Dacia" | p000267 | Đúng. |
| strategic reserves | "lực lượng dự bị chiến lược" | p000267 | Đúng. |
| Principality of Dacia | "Công quốc Dacia" | p000268 | Đúng. |

Không đảo/mất phủ định, số liệu (hai nghìn; sáu trăm nghìn / bảy mươi nghìn), cấp bậc (Đại tá, Trung úy, Chỉ huy Tiểu đoàn) hay quan hệ "bên ra đòn trước / trước khi đội bay tới" trong các đoạn đã đối chiếu.

## 4. Còn lại

- **Nghiêm trọng:** 0.
- **Vừa:** 0.
- **Nhẹ (còn trong phạm vi, chưa sửa, không chặn commit):**
  - p000255: "khí thế" vs "mood" (N3 cũ).
  - p000260: "lương tri" (N4 cũ).
  - p000261: lặp "rồi" (N5 cũ).
  - p000267: "nghiền nát" dùng hai lần cho hai ý khác nhau (N6 cũ).
  - p000244/p000267: cách ghi số lẫn lộn ("số 7", "số 17", "Đại đội Bốn", "203") (N11 cũ).
  - p000264 (mới): “Nó cười toe toét” đứng ngay sau “Đại tá von Lergen lạnh sống lưng” nên có thể đọc nhầm "Nó" là Đại tá. Gợi ý: lặp "Tanya" ở đây. Mức nhẹ.
  - p000274 (mới, rất nhẹ): "Tanya" lặp hai lần trong câu đầu; có thể chấp nhận.
- Các mục N1, N2, N7–N10 nằm ngoài phạm vi signoff này; không đánh giá.

## 5. Rủi ro

- `handoffs/vol-02/ch-01-b10.yml` có **khóa `provisional_review_choices` xuất hiện hai lần** trong `review_coordination` (bản cũ dùng "nó or Tanya", bản mới dùng "nó"). YAML trùng khóa có thể bị parser báo lỗi hoặc ghi đè im lặng; cần coordinator xóa khối cũ. Đây là lỗi tệp handoff, không phải bản dịch (reviewer không sửa).
- Tôi không chạy lại validator/diff_check (không thuộc quyền reviewer); chỉ dựa vào `validator: pass`, `diff_check: pass` do handoff ghi.
- Thuật ngữ vẫn tạm; đổi sau này (đặc biệt "Không quân", "đội bay") phải đổi đồng loạt giữa các lô.

## 6. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-01-b10-fixes-signoff
state: done
review_path: reviews/prose/vol-02/ch-01-b10-fixes-signoff-claude.md
files_written: [reviews/prose/vol-02/ch-01-b10-fixes-signoff-claude.md]
segment_ids: [p000244, p000254..p000265, p000267, p000268, p000274]
fixes_pass: true
v1_p000264: fixed        # cả hai vùng nhấn mạnh, gồm cụm cuối
v2_p000274: fixed        # nó/Tanya cho Tanya; bức ảnh ấy cho ảnh
counts: {serious: 0, moderate: 0, minor: 7}
term_meaning_changes: none
validator: not_run
diff_check: not_run
risks:
  - handoff có khóa provisional_review_choices trùng
  - thuật ngữ tạm, cần nhất quán liên lô
next_action: coordinator_dedupe_handoff_key_then_commit_b10   # minor tùy chọn: lặp "Tanya" ở p000264
```
