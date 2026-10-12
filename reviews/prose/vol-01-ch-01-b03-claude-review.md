# Phản biện — vol-01 Chương 1, lô b03

Người phản biện: Claude. Task: `vol-01-ch-01-b03-review`. Phạm vi: 15 đoạn p000029–p000043, tiền tố đầy đủ `YS-LN01/Text/chapter003b.xhtml/`. Báo cáo không chép câu nguồn; chỉ dùng mã đoạn (`pNNNNNN`) và thuật ngữ nguyên gốc ngắn để nhận diện.

Đầu vào đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, handoff `review-ch-01-b03.yml`, gói nguồn b03 (đọc tại chỗ), bản dịch b03, `work/run-state/pending-terms.yml`, báo cáo quyết định tạm ch-00, báo cáo b02 follow-up, `canon/glossary-pending.yml`, `canon/style-guide.md`, `canon/decisions.md`, `canon/glossary.yml`, `canon/characters.yml` (hai file cuối vẫn rỗng).

**Tính chất:** mọi phương án dưới đây là đề xuất tạm theo AGENTS.md, không phải canon, không tự nâng thành quyết định. Không sửa bản dịch, canon, handoff hay sổ pending. Validator/diff_check: not_run; commit: null.

Thang tin cậy: cao ≥ 0,75; vừa 0,5–0,74; thấp < 0,5.

## 1. Kết luận

- Không có hard stop; không có điểm nào ảnh hưởng cốt truyện hay cần hỏi người dùng.
- Số phát hiện: nghiêm trọng 0, vừa 4 (p000033, p000034, p000031, p000043), nhẹ 14.
- 15/15 hàng khớp `source_sha256`; mã đoạn đủ và đúng thứ tự. Nhấn mạnh `*...*` đúng phạm vi ở p000030, p000031, p000032 (hai cặp), p000041, p000042; không có nhấn mạnh thừa. Dấu ngoặc kép p000037–p000040, p000042 giữ đúng.
- Đại từ Tanya: không dùng "cô"; lặp tên hoặc lược chủ ngữ, khớp quyết định b02 (`P01-tanya-narration-ch01`) và DEC-P01-001. Không phát hiện sai ở p000033, p000043.
- Nghĩa nhìn chung chính xác, văn phong tự nhiên. Vấn đề chính nằm ở sắc thái thuật ngữ chính trị–quân sự ("quan liêu", "sĩ quan cấp đại đội", "suicidal", "arbitrate") và vài chi tiết thêm/bớt nhỏ.

## 2. Phát hiện theo mã đoạn

| Mức | Mã đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| vừa | p000033 | "bộ máy quan liêu" cho bureaucracy: trong tiếng Việt "quan liêu" mang nghĩa chê (bệnh quan liêu), trong khi nguồn khen bộ máy "được tinh chỉnh kỹ lưỡng". Vi phạm quy tắc không thêm sắc thái phán xét. | "bộ máy hành chính" (0,7); thay thế "hệ thống quan chức". |
| vừa | p000034 | "suicidal advance" dịch "bước tiến liều lĩnh": giảm từ tự hủy diệt xuống mức liều lĩnh, mất lý do khiến Commonwealth/Republic phải can thiệp. | "bước tiến tự sát" hoặc "cuộc tiến quân tự sát" (0,65); thay thế "liều lĩnh đến mức tự sát". |
| vừa | p000031 | "sĩ quan cấp đại đội thấp kém như Tanya": (a) "thấp kém" nặng hơn "lowly", hàm ý chất lượng kém thay vì cấp thấp; (b) "như Tanya" là phần thêm, nguồn dùng cách nói chung từ điểm nhìn của Tanya. Ngoài ra "company officer" ở Việt ngữ quân sự thường là "sĩ quan cấp úy". | "một sĩ quan cấp úy quèn", bỏ "như Tanya" (0,6); thay thế "sĩ quan cấp đại đội quèn". |
| vừa | p000043 | "gã khổng lồ quân sự": "gã" thêm sắc thái miệt thị/nam tính cho Đế quốc, không có trong nguồn. | "người khổng lồ quân sự" hoặc "khổng lồ quân sự" (0,7); thay thế "cường quốc quân sự". |
| nhẹ | p000029 | "liên tục truyền về" thêm tính liên tục; nguồn chỉ nói tin báo dồn dập đến. Bỏ "positions". | "dồn dập truyền về"; "các đồn an ninh" giữ. |
| nhẹ | p000030 | (a) "rải truyền đơn" xác định hình thức phát hành; nguồn chỉ nói rải thông báo. (b) "Chẳng mấy chốc" khác "trước khi họ kịp nhận ra". (c) "cả Quân đội Đế quốc" làm mất "mọi người trong quân đội", cấu trúc "không chỉ… mà cả" đổi chủ thể từ người sang tổ chức. (d) "bộ máy lãnh đạo" cho "executives" hơi rộng. | (a) "rải thông báo" hoặc "rải thông cáo"; (b) "Trước khi kịp nhận ra"; (c) "mà cả những người trong Quân đội Đế quốc"; (d) "giới lãnh đạo". |
| nhẹ | p000032 | "không chịu đối diện" (couldn't) biến thành không muốn; "tồi tệ nhất" (superlative) cho "all the wrong reasons"; "Bọn họ" thêm chút khinh. | "không thể đối diện" hoặc "không dám nhìn thẳng vào thực tế"; "những lý do chẳng hay ho gì"; "Họ ngu ngốc thật sao?". |
| nhẹ | p000033 | (a) "chỉ chủ yếu" tự mâu thuẫn. (b) "đường hướng" cho "agenda" lệch: agenda là ý đồ/toan tính. (c) "tuyên truyền trong nước" tạm được nhưng thuật ngữ chính trị chuẩn là "đối nội". | (a) "phần lớn chỉ nhằm…"; (b) "ý đồ hay mục tiêu"; (c) "tuyên truyền đối nội" (0,6), thay thế "trong nước". |
| nhẹ | p000034 | "Dù sao thì" cho "After all" đổi quan hệ lý lẽ (anyway thay vì suy cho cùng). | "Suy cho cùng," hoặc "Xét cho cùng,". Lưu ý p000034 đã dùng "Suy cho cùng" ở câu cuối; chọn "Dù gì" hoặc "Vả lại". |
| nhẹ | p000035 | (a) "làm trung gian" cho arbitrate trùng khái niệm "hòa giải" ở p000034; arbitrate nghiêng về phân xử. (b) "hai bên đối địch" mạnh hơn "opposing". (c) "chẳng có cửa" khẩu ngữ, chấp nhận được. | (a) "đứng ra phân xử" (0,6), thay thế "làm trung gian" (giữ cũng được); (b) "hai bên đang đối đầu". |
| nhẹ | p000036 | "vào thời điểm ấy" đổi mốc: "in this day and age" là thời đại của người kể (đồng bộ với "much later" ở p000039). | "trong thời đại này" hoặc "thời nay". |
| nhẹ | p000037 | Đạt. Chỉ ghi chú: "đang tiến quân" tạm được; nguồn không có nhãn người nói/phương tiện, bản dịch đã không suy ra. | Giữ. |
| nhẹ | p000038 | "bán tín bán nghi" cho incredulous: từ này nghĩa là nửa tin nửa ngờ; incredulous là không thể tin nổi. "chấn động" cho "shocking" mạnh hơn "gây sốc". | "trong tâm thế không thể tin nổi" (0,6); "gây sốc" (thay thế "chấn động" nếu muốn bớt hoa mỹ). |
| nhẹ | p000039 | Trong ngoặc: "Chúng ta… của ta" lẫn hai kiểu xưng; cấu trúc "đến mức nghi rằng … còn hợp lý hơn" khó đọc; "lãnh đạo quân đội" tạm ổn. Không thêm quân hàm cho Lergen: đúng. | "của chúng ta" hoặc "của phía mình"; "đến mức việc nghi ngờ… còn hợp lý hơn". |
| nhẹ | p000040 | (a) "tập kết vật tư" và "tập kết bằng đường sắt" trùng từ cho hai việc khác nhau (amass supplies / assemble divisions). (b) "đường hướng" cho agenda (xem p000033). (c) "điềm tĩnh" cho soberly chấp nhận được. (d) "Đại quân" viết thường: nguồn viết hoa tên riêng, và "đại quân" là danh từ chung (lực lượng lớn). | (a) "tích trữ/dự trữ vật tư" cho amass; (b) "ý đồ"; (d) "Đại Quân" hoặc "Đại quân" có nhấn tên riêng, nhất quán toàn tập (0,5). |
| nhẹ | p000041 | (a) "trong nội bộ" là phần thêm; chủ thể gốc là chính Đế quốc. (b) "dai dẳng một chút hoài nghi" kết hợp lệch (dai dẳng + một chút). (c) "mobilize troops" Việt ngữ quân sự là "động viên" (không "huy động" chung). (d) "thu mua" cho procure hơi lệch sang mua bán. | (a)(b) "vẫn bị một phần hoài nghi đeo bám"; (c) "thậm chí đã động viên quân"; (d) "mua sắm" hoặc "tích trữ" (0,5). |
| nhẹ | p000042 | (a) "dưới danh nghĩa" cho under the pretext yếu hơn, mất sắc thái lấy cớ. (b) "Quân đoàn được huy động bổ sung" mơ hồ số ít/nhiều ("corps" là số ít/nhiều đồng dạng). (c) "Để phục vụ chiến tranh thông tin" mạnh hơn "with in mind". | (a) "lấy cớ tuần tra thường lệ"; (b) "Các quân đoàn được huy động bổ sung" hoặc giữ nếu muốn trung tính; (c) "Có tính đến chiến tranh thông tin". |
| nhẹ | p000043 | (a) "vô cớ" bớt mất "without any semblance of justification". (b) "chưa từng mơ" hơi sát chữ, khó nghe với "lại". | (a) "chẳng có chút danh nghĩa chính đáng nào"; (b) "chưa bao giờ ngờ rằng". |

Các đoạn p000029, p000036, p000037 không có lỗi nghĩa. p000035, p000038 chỉ có điểm nhẹ.

## 3. Thuật ngữ mới — đề xuất tạm ưu tiên

| Mục | Hiện tại | Đề xuất ưu tiên | Thay thế | Tin cậy | Mã đoạn |
|---|---|---|---|---|---|
| security outpost | đồn an ninh | giữ "đồn an ninh" | tiền đồn cảnh giới, trạm gác biên giới | 0,6 | p000029 |
| cross-border operation | chiến dịch xuyên biên giới | giữ | cuộc tấn công vượt biên | 0,7 | p000029, p000040 |
| policy direction | định hướng chính sách | giữ | đường lối chính sách | 0,7 | p000030 |
| doctrine | học thuyết | giữ "học thuyết" (không thêm "quân sự", vì nguồn chưa nêu rõ) | học thuyết quân sự | 0,55 | p000030 |
| declaration of war | lời tuyên chiến | giữ | — | 0,8 | p000030 |
| company officer | sĩ quan cấp đại đội | "sĩ quan cấp úy" | sĩ quan cấp đại đội | 0,6 | p000031 |
| full-blown military engagement | giao chiến toàn diện | giữ | chiến tranh toàn diện | 0,65 | p000031 |
| Entente Alliance Army | Quân đội Liên minh Entente | giữ, nhất quán với "Quân đội Đế quốc" | Lục quân Liên minh Entente | 0,6 | p000037 |
| Great Army divisions | các sư đoàn Đại quân | "các sư đoàn Đại Quân" (viết hoa tên riêng), chưa suy luận quan hệ với Imperial Army | các sư đoàn thuộc Đại Quân | 0,5 | p000040 |
| Central | Central | giữ nguyên, không dịch ("Trung ương" chỉ khi có căn cứ về cơ quan), kiểm tra các đoạn sau | Trung ương; vùng trung tâm | 0,5 | p000040 |
| corps-sized garrison | lực lượng đồn trú quy mô quân đoàn | giữ | quân đoàn đồn trú | 0,65 | p000042 |
| information warfare | chiến tranh thông tin | giữ | — | 0,85 | p000042 |
| organizational victory | chiến thắng về tổ chức | giữ | thắng lợi về mặt tổ chức | 0,65 | p000040 |
| agenda | đường hướng | "ý đồ" (đổi trong cả p000033 và p000040) | toan tính | 0,6 | p000033, p000040 |
| internal propaganda | tuyên truyền trong nước | "tuyên truyền đối nội" | trong nước | 0,6 | p000033 |
| mobilize troops | huy động binh sĩ | "động viên quân" | huy động binh sĩ | 0,5 | p000041 |
| arbitrate | đứng ra làm trung gian | "đứng ra phân xử" | làm trung gian (chấp nhận được) | 0,6 | p000035 |
| incredulous | bán tín bán nghi | "không thể tin nổi" | hoài nghi | 0,6 | p000038 |
| military titan | gã khổng lồ quân sự | "người khổng lồ quân sự" | cường quốc quân sự | 0,7 | p000043 |

### Mục chưa có trong sổ pending (nên bổ sung)

| Source term | Đề xuất tạm | Thay thế | Tin cậy | Mã đoạn |
|---|---|---|---|---|
| the Federation | Liên bang | — | 0,65 | p000034 |
| the Commonwealth | Khối Thịnh vượng chung (hiện dùng ở bản dịch) | Thịnh vượng chung (bỏ "Khối" cho gọn) | 0,5 | p000034 |
| the Republic | Cộng hòa (viết hoa như tên riêng) | nước Cộng hòa | 0,55 | p000034 |
| Lergen | Lergen (giữ nguyên tên, chưa canon) | — | 0,8 | p000039 |
| Imperial Army General Staff | Bộ Tổng Tham mưu Quân đội Đế quốc (theo b01 follow-up) | — | 0,65 | p000039 |
| military folk / military leaders | người trong quân đội / lãnh đạo quân đội | giới quân sự / giới chỉ huy | 0,55 | p000034, p000039 |

Ghi chú: "Liên bang", "Khối Thịnh vượng chung", "Cộng hòa" chưa xuất hiện ở ch-00 hay ch-01 b01–b02, nên đây là lần đầu; nếu về sau tên đổi, sẽ cần sửa ở p000034. Ghi chú trong bản dịch p000034 chỉ nêu "Commonwealth" nhưng chưa ghi "Federation" và "Republic".

## 4. Việc cần làm sau báo cáo (đề xuất)

1. Translator (khi nhận quyền sửa): xử lý bốn mục vừa (p000031, p000033, p000034, p000043); các mục nhẹ tùy chọn, ưu tiên "ý đồ" (p000033/p000040), "động viên" (p000041), "đối nội" (p000033), "phân xử" (p000035).
2. Coordinator: đồng bộ ledger — thêm `Federation`, `Commonwealth`, `Republic`, `Lergen`, `agenda`, `mobilize`, `arbitrate`, `incredulous`, `military titan`; cập nhật `company officer` và `Great Army divisions` theo mục 3. Ghi tất cả là đề xuất, chưa canon.
3. Translator làm mới trường `notes` ở p000030, p000031, p000034, p000040, p000042 để khớp bản dịch sau sửa.
4. Chạy validator và `git diff --check` sau khi sửa, trước khi commit.

## 5. Rủi ro và bất định

- "Great Army" và "Central" tin cậy thấp (0,5): chưa rõ đây là tên đơn vị riêng hay chức năng và có thể đổi khi các đoạn sau làm rõ.
- "Sĩ quan cấp úy" dựa vào quy ước quân hàm Việt Nam; nguồn chỉ nói "company officer" nên không suy ra quân hàm cụ thể của Tanya.
- Tên "Liên bang/Khối Thịnh vượng chung/Cộng hòa" dựa vào quy ước chung cho các bản dịch cùng thể loại; chưa có canon.
- Không đối chiếu được nguồn ngoài gói b03 (EPUB/PDF không được mở); chưa chạy validator và diff-check.

```yaml
role: reviewer
task_id: vol-01-ch-01-b03-review
state: done
review_path: reviews/prose/vol-01-ch-01-b03-claude-review.md
segment_ids: [p000029, p000030, p000031, p000032, p000033, p000034, p000035, p000036, p000037, p000038, p000039, p000040, p000041, p000042, p000043]
files_written: [reviews/prose/vol-01-ch-01-b03-claude-review.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 4, minor: 14}
unresolved_findings: [p000031, p000033, p000034, p000043]
term_recommendations: [company officer → sĩ quan cấp úy, agenda → ý đồ, internal propaganda → tuyên truyền đối nội, mobilize → động viên, arbitrate → phân xử, incredulous → không thể tin nổi, military titan → người khổng lồ quân sự, Great Army → Đại Quân]
risks: [Great Army và Central tin cậy thấp, Federation/Commonwealth/Republic chưa có trong ledger, chưa chạy validator]
commit: null
next_action: coordinator đồng bộ ledger và giao translator sửa bốn mục vừa; sau đó chạy validator và diff-check
```
