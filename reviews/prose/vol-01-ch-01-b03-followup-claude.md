# Phản biện follow-up — vol-01 Chương 1, lô b03

Người phản biện: Claude. Task: `vol-01-ch-01-b03-review-followup-review`. Phạm vi: 15 đoạn p000029–p000043, tiền tố đầy đủ `YS-LN01/Text/chapter003b.xhtml/`. Báo cáo không chép câu nguồn; chỉ dùng mã đoạn và thuật ngữ nguyên gốc ngắn để nhận diện.

Đầu vào đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, handoffs `review-ch-01-b03-followup.yml` và `revision-ch-01-b03.yml`, gói nguồn b03 (đọc tại chỗ), bản dịch b03 hiện tại, báo cáo b03 ban đầu, `work/run-state/pending-terms.yml`. Mọi lựa chọn dưới đây là đề xuất tạm, không phải canon. Validator/diff_check: not_run; commit: null.

## 1. Kết luận

- Bốn phát hiện mức vừa trước đây (p000031, p000033, p000034, p000043) đều đã được xử lý đúng và không làm phát sinh lỗi mới.
- Không còn lỗi nghiêm trọng hay vừa. Còn 5 điểm nhẹ (3 về bản dịch, 2 về sổ pending), không chặn commit.
- 15/15 hàng giữ nguyên `segment_id`, thứ tự, `source_sha256` và `glossary_version`; nhấn mạnh `*...*` ở p000030, p000031, p000032, p000041, p000042 vẫn đúng phạm vi; ngoặc kép p000037–p000040 giữ nguyên.
- Tanya: không dùng "cô" ở p000033, p000043; khớp `P01-tanya-narration-ch01`.
- Không có điểm ảnh hưởng cốt truyện; không cần hỏi người dùng.

## 2. Xác nhận bốn phát hiện vừa cũ

| Mã đoạn | Kết quả | Căn cứ |
|---|---|---|
| p000031 | Đã sửa | "sĩ quan cấp úy quèn": hết "thấp kém", bỏ phần thêm "như Tanya"; khớp đề xuất b03-company-officer và hệ thống quân hàm b02 (thiếu úy, chuẩn úy). Không suy ra quân hàm cụ thể. |
| p000033 | Đã sửa | "bộ máy hành chính" thay "bộ máy quan liêu", hết sắc thái chê. Kèm sửa các mục nhẹ: "ý đồ hay mục tiêu", "tuyên truyền đối nội", "phần lớn chỉ nhằm" (hết mâu thuẫn "chỉ chủ yếu"). |
| p000034 | Đã sửa | "bước tiến tự sát" thay "liều lĩnh", giữ lý do các bên phải can thiệp. "Người trong quân đội" khớp ghi chú. |
| p000043 | Đã sửa | "người khổng lồ quân sự" thay "gã khổng lồ", bỏ sắc thái miệt thị; kèm "chẳng có chút danh nghĩa chính đáng nào" và "chưa bao giờ ngờ". |

## 3. Các mục nhẹ khác: đã áp dụng

p000029 (dồn dập), p000030 (rải thông báo, Trước khi kịp nhận ra, "những người trong Quân đội Đế quốc"), p000032 (không thể đối diện, chẳng hay ho gì, "Họ ngu ngốc thật sao?"), p000035 (phân xử, hai bên đang đối đầu), p000036 (thời đại này), p000038 (không thể tin nổi), p000039 (xưng hô "chúng ta" nhất quán, cấu trúc câu rõ hơn), p000040 (tích trữ vật tư, ý đồ, Đại Quân, "tập kết" chỉ còn cho sư đoàn), p000041 (bỏ "trong nội bộ", động viên quân, hoài nghi đeo bám), p000042 (lấy cớ, "Các quân đoàn", "Có tính đến"). Nghĩa khớp nguồn; không phát hiện thêm/bớt nghĩa.

## 4. Phát hiện còn lại (nhẹ)

| Mức | Mã đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| nhẹ | p000034 | Mở đầu mất từ nối nghĩa "suy cho cùng" của câu đầu; hiện lập luận nối với câu sau kém liền mạch. "Suy cho cùng" chỉ còn ở câu cuối. | Thêm "Dù gì" hoặc "Vả lại" ở đầu đoạn (tránh trùng "Suy cho cùng" ở câu cuối). Tùy chọn. |
| nhẹ | p000030 | "bộ máy lãnh đạo" (executives) còn hơi rộng; đề xuất cũ "giới lãnh đạo" chưa áp dụng. | Tùy chọn: "giới lãnh đạo". Giữ nguyên cũng chấp nhận được. |
| nhẹ | p000040, p000041 | "tích trữ" dùng cho cả amass supplies (p000040) lẫn procure supplies (p000041); khác nghĩa nhẹ (thu mua vs dự trữ). | Tùy chọn: p000041 dùng "mua sắm"/"trang bị đủ" (độ tin cậy 0,5). Không ảnh hưởng nghĩa. |
| nhẹ | sổ pending | `chapter1_b03_pending_terms` còn hai mục cũ chưa đánh dấu superseded: company officer → "sĩ quan cấp đại đội" (p000031), Great Army divisions → "các sư đoàn Đại quân" (p000040); mâu thuẫn bản dịch và `chapter1_b03_followup_terms`. | Coordinator ghi `superseded_by` cho hai mục này. |
| nhẹ | sổ pending | (a) `b03-military-folk` ghi preferred "giới quân sự/giới chỉ huy" nhưng bản dịch (p000034 "người trong quân đội", p000039 "lãnh đạo quân đội") và báo cáo b03 chọn phương án kia; `followup_terms` không có mục này, cũng không có Lergen, Bộ Tổng Tham mưu Quân đội Đế quốc. (b) Mục `Great Army`/`Central` (tin cậy 0,5) và Federation/Commonwealth/Republic (0,5–0,65) chưa ghi `confidence`/ghi chú bất định. | Coordinator đảo preferred/alternative cho military-folk (hoặc ghi rõ lý do), thêm mục thiếu, ghi confidence. Đây là việc ledger, không sửa bản dịch. |

## 5. Nhất quán thuật ngữ và ghi chú

- Notes p000030, p000031, p000034, p000040, p000042 đã khớp nội dung hàng và lựa chọn tạm: "đồn an ninh", "bộ máy hành chính", "ý đồ", "tuyên truyền đối nội", "bước tiến tự sát", "các sư đoàn Đại Quân", "các quân đoàn được huy động", "người khổng lồ quân sự". Không chứa câu nguồn; đều ghi "tạm, chưa phải canon".
- Nhất quán liên đoạn: "ý đồ" (p000033, p000040), "chiến dịch xuyên biên giới" (p000029, p000040), "quỷ dữ" (p000029; khớp `review-devil`), "Quân đội Đế quốc/Liên minh Entente", "Central" giữ nguyên.
- Bất định còn ghi: Great Army/Central (chưa rõ tên đơn vị hay chức năng), tên Liên bang/Khối Thịnh vượng chung/Cộng hòa chưa canon; không có chênh lệch nguồn mới trong b03. Chênh lệch nguồn Goliath-07 (b01) không thuộc phạm vi này và vẫn được giữ trong sổ.

## 6. Rủi ro

- "Đại Quân" và "Central" có thể phải đổi khi các đoạn sau làm rõ; cần quét lại p000040 khi có thêm ngữ cảnh.
- "Khối Thịnh vượng chung", "Liên bang", "Cộng hòa" chưa có canon.
- Chưa chạy validator/diff-check trong task này; chưa đối chiếu nguồn ngoài gói b03.

```yaml
role: reviewer
task_id: vol-01-ch-01-b03-review-followup-review
state: done
review_path: reviews/prose/vol-01-ch-01-b03-followup-claude.md
segment_ids: [p000029, p000030, p000031, p000032, p000033, p000034, p000035, p000036, p000037, p000038, p000039, p000040, p000041, p000042, p000043]
files_written: [reviews/prose/vol-01-ch-01-b03-followup-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 0, minor: 5}
unresolved_findings: []
commit: null
```
