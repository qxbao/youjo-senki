# Báo cáo phản biện — vol-02-ch-01-b11

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon).
- Phạm vi: `p000276`–`p000298` (23 đoạn), gồm handoff b11, gói nguồn cục bộ, `translations/vol-02/ch-01-b11.jsonl`, canon và sổ pending.
- Kích hoạt: `new_pending_terms`.
- Báo cáo không trích câu nguồn. Thuật ngữ nguyên gốc ngắn và mã đoạn chỉ dùng để nhận diện.

## 1. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự mã đoạn | 23/23, liên tục từ p000276 đến p000298, khớp nguồn và bản dịch |
| Hash gói nguồn | khớp `source_package_sha256` trong handoff |
| Số từ nguồn | 872, khớp handoff |
| Nhấn mạnh (DEC-P01-002) | Nguồn chỉ nhấn mạnh câu đầu p000283. Bản dịch chỉ đánh `*...*` đúng phạm vi đó. Không có nhấn mạnh thừa hay thiếu ở đoạn khác. **Đạt.** |
| `notes` trong bản dịch | Rỗng ở cả 23 đoạn; không có ghi chú làm việc lẫn vào văn bản |

Nhìn chung bản dịch bám nghĩa và phủ định tốt. Các logic "nếu… thì sao lại…", "dù… vẫn…" và phép so sánh ở p000276, p000282, p000289, p000290 đều được giữ. Không có lỗi nghiêm trọng.

## 2. Phát hiện

Đếm: **nghiêm trọng 0 · vừa 4 · nhẹ 9**.

### Mức vừa

**M1 — p000293 (liên quan p000287): cấp bậc "Thượng úy" lệch bản đồ cấp bậc tạm.**
- Bản dịch dùng "Thượng úy Weiss". Sổ pending b02/b06/b08 dùng Weiss = Trung úy, và b09 (p000219, đã sửa theo review b09) chốt tạm "Trung úy Weiss".
- Trong cùng lô, p000287 gọi người đối thoại là "Trung úy". Nếu người đó là Weiss thì cùng một nhân vật bị gọi hai cấp khác nhau trong 17 đoạn.
- Căn cứ: First Lieutenant xếp trên Second Lieutenant (Thiếu úy) và dưới Captain theo thang Anh–Mỹ, tương ứng Trung úy. "Thượng úy" là bậc nằm giữa trung úy và đại úy trong hệ Việt Nam, nên đây là lựa chọn lệch thang.
- Đề xuất: p000293 → "Trung úy Weiss". Giữ p000287 là "Trung úy".
- Xem mục 3.2.

**M2 — p000277: "khái niệm mất điện" lệch nghĩa so với blackout.**
- Trong bối cảnh chiến trường, blackout là việc chủ động tắt/che đèn để tránh bị phát hiện, chứ không phải sự cố "mất điện". Cả đoạn nói về việc thành phố sáng rực, đèn có thể là mồi nhử và sự chủ quan trước không kích, nên nghĩa "tắt đèn phòng không" mới đúng mạch.
- Đề xuất: "khái niệm tắt đèn phòng không" hoặc "khái niệm cấm ánh sáng ban đêm". Cách thứ hai trung tính hơn; chọn một và dùng nhất quán nếu từ này xuất hiện lại.

**M3 — p000276, p000277: đại từ nội tâm "tôi" lệch DEC-P01-001.**
- DEC-P01-001: nội tâm tự quy chiếu của Tanya dùng "mình". Cùng lô, p000278, p000282, p000283, p000284, p000290 và p000298 đều dùng "mình".
- Riêng p000276 ("tôi không thể tưởng tượng nổi") và nửa đầu p000277 ("khiến tôi tin chắc", "tôi tự hỏi") dùng "tôi" trong đoạn độc thoại nội tâm.
- b10 dùng "mình" cho nội tâm cùng giai đoạn, nên b11 là ngoại lệ. "Tôi" trong thoại trực tiếp (p000251, p000288, p000289, p000295) là đúng.
- Đề xuất: đổi "tôi" thành "mình" ở p000276 và nửa đầu p000277. Nửa sau p000277 giữ "nó" cho trần thuật theo nguồn, vì nguồn chuyển ngôi ngay trong đoạn.

**M4 — p000296: chủ thể của "thiếu kinh nghiệm" bị chốt một chiều.**
- Nguồn dùng đại từ sở hữu trung tính "their", có thể chỉ phó chỉ huy hoặc cấp trên (Tanya). Ngữ cảnh p000298 (Tanya chỉ qua huấn luyện sĩ quan ngắn hạn) làm cách đọc "cấp trên" cũng hợp lý.
- Bản dịch dùng "bản thân thiếu kinh nghiệm", thường được đọc là phó chỉ huy và bỏ mất cách đọc còn lại.
- Đề xuất: "dù thiếu kinh nghiệm", bỏ "bản thân", để giữ độ mở của chủ thể. Tôi không khẳng định nguồn nghiêng về bên nào; đây là rủi ro chủ thể (xem mục 4).

### Mức nhẹ

- **L1 — p000277, "giác ngộ" cho "enlightened":** mang sắc thái tôn giáo và làm mất trò chơi chữ ánh sáng với thành phố sáng đèn. Đề xuất "tự thấy mình được khai sáng đôi chút", khớp "Khai sáng" ở p000293 và bắt được hai tầng nghĩa. Ghi chú: sổ pending hiện chỉ ghi p000293 cho enlightenment b11, chưa ghi p000277; mục P05-enlightenment (vol-01, "giác ngộ") là ngữ cảnh khác, không ràng buộc ở đây.
- **L2 — p000296, "quả có mắt nhìn người":** nguồn có sắc thái dè dặt ("seems"), bản dịch khẳng định. Đề xuất: "có vẻ có mắt nhìn người".
- **L3 — p000298, "luật lệ của nó":** trong đoạn "nó" còn chỉ Tanya (DEC-P01-001). Đề xuất: "luật lệ của chiến tranh".
- **L4 — p000294, "anh":** gán xưng hô thân mật cho Weiss, trong khi DEC-P01-001 giới hạn suy luận quan hệ và b09 đã nêu lỗi tương tự (L4 của b09). Đề xuất dùng tên: "Nhận ra Weiss đang cố hết sức…" và "giao nhiệm vụ cho Weiss".
- **L5 — p000278, "đá đít chúng":** "chúng" có thể bị đọc là "những cảm xúc ấy". Đề xuất "đá đít lũ địch/bọn chúng". Ngoài ra "satisfaction" bị dịch thành "cảm giác"; có thể dùng "cảm giác thỏa mãn" để giữ sắc thái.
- **L6 — p000281, "chiến dịch tinh vi":** nguồn đang tiếp mạch ẩn dụ làm thuê thu phí (p000279–p000280), còn "chiến dịch" kéo về quân sự. Đề xuất "thương vụ/dự án tinh vi".
- **L7 — p000280, "cố vấn chính phủ nước ngoài":** có thể bị đọc là cố vấn của chính phủ nước ngoài. Đề xuất "cố vấn nước ngoài của chính phủ thời Minh Trị".
- **L8 — các chỗ lệch nhỏ về từ nối và mức độ:**
  - p000289: "rồi khịt mũi" mất quan hệ nhượng bộ ("dù… vẫn khịt mũi"); nên là "dù khịt mũi khi tiếp lời".
  - p000283: "nếu mình bắn" đổi "khi" thành điều kiện; nên là "khi mình bắn".
  - p000295: "thuận lợi" yếu hơn "dễ dàng/nhẹ nhàng".
  - p000284: "vung nó" có thể trỏ nhầm Tanya vì "nó" đang là đại từ trần thuật; dùng "vung đèn" hoặc "xoay vòng".
- **L9 — p000297, "Ta ra tay chứ?":** lời cấp dưới (suy ra là Serebryakov từ p000298) nói với cấp trên. "Ta" nghe trên vai. Đề xuất "Chúng ta ra tay chứ?". Không thêm "ạ" vì nguồn không có từ lễ phép này.

## 3. Đánh giá lựa chọn pending (tạm thời, không phải canon)

### 3.1 Enlightenment — p000293
- **Chọn tạm:** "Khai sáng" trong "các nhà tư tưởng thời Khai sáng" (giữ bản dịch hiện tại).
- **Phương án thay:** "Thời kỳ Khai sáng"; "thế kỷ Ánh sáng" (không khuyến nghị: thêm chi tiết thời gian không có trong nguồn).
- **Độ tin cậy:** 0,7.
- **Bất định:** câu có sắc thái mỉa mai về công nghiệp hóa, kết nối nhẹ với chủ đề ánh sáng ở p000277. Mối liên hệ này chưa chắc là cố ý; không khẳng định. Không gộp với P05 vol-01 ("giác ngộ").
- **Mã đoạn:** p000293 (liên quan p000277).

### 3.2 First Lieutenant — p000293 (xung đột với lựa chọn pending hiện có)
- **Chọn tạm:** "Trung úy" (Weiss), khớp lựa chọn b09 (p000219), ledger b02/b06/b08 và p000287.
- **Phương án thay:** "Thượng úy" (lệch thang, độ tin cậy thấp), "Trung úy nhất" (không khuyến nghị, đã bị loại ở b09).
- **Độ tin cậy:** 0,55.
- **Bản đồ cấp bậc tạm đề xuất cho cả tập:** Second Lieutenant = Thiếu úy; First Lieutenant = Trung úy; Major = Thiếu tá (sổ hiện có). Đây là bản đồ thang Anh–Mỹ; nếu chủ đề cấp bậc được xét lại, xét toàn tập một lần chứ không đổi riêng b11.
- **Bất định:** cách gọi trần "Lieutenant" ở p000287 không nêu First hay Second nên chưa chắc người nhận là Weiss (xem mục 4). Với Weiss, "Trung úy" vẫn đúng cho cả hai cách gọi.
- **Xung đột đã nêu:** mục `vol02-ch01-b11-first-lieutenant` (Thượng úy) mâu thuẫn mục `vol02-ch01-b09-first-lieutenant` (Trung úy). Khuyến nghị coordinator giữ "Trung úy" làm giá trị tạm duy nhất.
- **Mã đoạn:** p000293, p000287.

### 3.3 Second Lieutenant — p000298
- **Chọn tạm:** "Thiếu úy" (Serebryakov), không thêm "ma pháp".
- **Phương án thay:** "Thiếu úy ma pháp" (chỉ khi nguồn khác xác nhận đây là cấp bậc ma pháp; b11 không có chứng cứ như vậy).
- **Độ tin cậy:** 0,6.
- **Bất định:** thấp; nhất quán với p000051 và b02/b05/b06/b08.
- **Mã đoạn:** p000298.

### 3.4 Principality — p000281
- **Chọn tạm:** "Công quốc" ("Công quốc tội nghiệp ấy"), chỉ Dacia.
- **Phương án thay:** "lãnh địa công tước" (không khuyến nghị: sai bậc thể chế và lệch dùng ở b09 p000235, b10 p000268).
- **Độ tin cậy:** 0,75.
- **Bất định:** thấp; nhất quán với "Công quốc Dacia" ở b10. Cách dịch "poor" thành "tội nghiệp" là ổn.
- **Mã đoạn:** p000281.

## 4. Rủi ro chủ thể/người nói (không chốt, chuyển vào sổ pending)

- **p000279, p000292:** lời thoại không gắn người nói. Bản dịch không gán đại từ, nên an toàn. Có thể là Tanya.
- **p000286, p000288:** người nói chưa gắn; có thể là Weiss hoặc Serebryakov. Bản dịch dùng "Ngài… ạ… thiếu tá" cho p000286, chỉ nên giữ nếu không đổi nghĩa; không suy thêm.
- **p000287:** "Lieutenant" có thể là Weiss hoặc Serebryakov. "Trung úy" chỉ đúng nếu là Weiss. Nếu là Serebryakov thì cách gọi là Thiếu úy. Độ bất định khoảng 40%; cách xử lý tạm: giữ "Trung úy", báo coordinator.
- **p000297:** suy ra người nói là Serebryakov từ mạch p000298 ("cùng lúc đó"). Độ tin cậy khoảng 0,65.
- **p000296:** xem M4.

## 5. Điểm tốt đáng giữ

- Cấu trúc giễu nhại giáo dục/văn minh p000278–p000283 được giữ giọng. Giọng mỉa mai và sự thô tục có kiểm soát ở p000278 hợp nhân vật.
- p000283 giữ đúng phạm vi nhấn mạnh và tách lớp nội tâm khỏi trần thuật.
- p000289–p000291: ẩn dụ "hai chiều/phẳng" nhất quán.
- Không thêm sắc thái phán xét ngoài nguồn.

## 6. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-01-b11
state: done
review_path: reviews/prose/vol-02/ch-01-b11-claude.md
segment_ids: [YS-LN02/Text/part0010.xhtml/p000276 .. p000298]
files_written: [reviews/prose/vol-02/ch-01-b11-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 4, light: 9}
findings:
  - {severity: moderate, segment_id: p000293, issue: "Thượng úy lệch bản đồ cấp bậc tạm và p000287", resolution: "Trung úy Weiss"}
  - {severity: moderate, segment_id: p000277, issue: "blackout dịch thành mất điện", resolution: "tắt đèn phòng không / cấm ánh sáng ban đêm"}
  - {severity: moderate, segment_id: "p000276, p000277", issue: "tôi trong nội tâm lệch DEC-P01-001", resolution: "mình"}
  - {severity: moderate, segment_id: p000296, issue: "chủ thể thiếu kinh nghiệm bị chốt một chiều", resolution: "dù thiếu kinh nghiệm"}
  - {severity: light, segment_ids: [p000277, p000296, p000298, p000294, p000278, p000281, p000280, "p000289/p000283/p000295/p000284", p000297], issue: "L1–L9 xem mục 2"}
unresolved_findings: [M1, M2, M3, M4]
term_recommendations:
  - {source_term: Enlightenment, proposed_vi: "Khai sáng", alternatives_vi: ["Thời kỳ Khai sáng"], segment_ids: [p000293], confidence: 0.7, status: pending}
  - {source_term: First Lieutenant, proposed_vi: "Trung úy", alternatives_vi: ["Thượng úy"], segment_ids: [p000293], confidence: 0.55, status: pending}
  - {source_term: Second Lieutenant, proposed_vi: "Thiếu úy", alternatives_vi: ["Thiếu úy ma pháp (chưa có chứng cứ)"], segment_ids: [p000298], confidence: 0.6, status: pending}
  - {source_term: Principality, proposed_vi: "Công quốc", alternatives_vi: ["lãnh địa công tước"], segment_ids: [p000281], confidence: 0.75, status: pending}
  - {source_term: enlightened (lowercase), proposed_vi: "được khai sáng", segment_ids: [p000277], confidence: 0.5, status: pending}
risks:
  - "p000287: người nhận 'Lieutenant' có thể là Weiss hoặc Serebryakov"
  - "p000286, p000288, p000292, p000297: người nói không gắn trong nguồn"
  - "p000296: chủ thể của 'thiếu kinh nghiệm' mơ hồ trong nguồn"
  - "Xung đột ledger First Lieutenant (b09 Trung úy so với b11 Thượng úy)"
  - "Không có lựa chọn nào ở đây ảnh hưởng cốt truyện; không cần hỏi người dùng"
commit: null
next_action: "Coordinator ghi lựa chọn tạm vào ledger/handoff (giữ Trung úy làm giá trị duy nhất), translator (người giữ quyền sửa) sửa M1–M4 và các mục nhẹ khả thi; sau đó xin sign-off ngắn trước khi commit b11."
```
