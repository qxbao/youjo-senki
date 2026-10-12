# Báo cáo phản biện văn phong và ngữ nghĩa — vol-02-ch-02-b06-review (batch chẵn, cờ new_pending_terms)

- **Người phản biện:** Claude (reviewer; chỉ ghi báo cáo này, không sửa bản dịch, handoff, canon, ledger hay run-state). Báo cáo không trích văn bản nguồn.
- **Phạm vi:** 23 đoạn p000118–p000140 (`YS-LN02/Text/part0014.xhtml/…`, viết tắt `pNNNNNN`). Đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, handoff b06, gói nguồn b06, bản dịch b06, `canon/*` (glossary rỗng; characters rỗng; style-guide; decisions DEC-P01-001/002), `canon/glossary-pending.yml` và các mục liên quan trong `work/run-state/pending-terms.yml` (mục `chapter2_b06_translation_proposals` cùng tiền lệ: Entente, Cộng hòa, Khối Thịnh vượng chung, Liên bang, Cục Tác chiến, Bộ Tổng tham mưu, cụm tập đoàn quân, quân hàm Serebryakov/Weiss, giới tính Weiss, đại từ Tanya, “Các vị”). Không đọc bản dịch của batch khác.

## 1. Kết luận

- **Kết luận:** `pass_with_fixes`.
- **Mức nghiêm trọng:** serious = 0; moderate = 3 (M1–M3); minor = 9 (m1–m9).
- **next_action:** người giữ quyền sửa xử lý M1–M3, cân nhắc minor, chạy lại validator + `git diff --check`, rồi commit. Reviewer chỉ cần xác nhận nhanh p000122, p000132, p000135 sau khi sửa.

## 2. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự ID | Đạt: 23 đoạn p000118–p000140, đúng thứ tự, khớp 1:1 với gói nguồn. |
| Hash gói nguồn | Đạt: `0cad57b9…4e30` khớp handoff. |
| `source_sha256` mỗi record | Đạt: khớp handoff (`3ac53161…`). |
| `glossary_version` | Đạt: khớp handoff (`d5f19d64…`). |
| `status` / `notes` | `draft` toàn bộ; `notes` rỗng; không có ghi chú làm việc lọt vào translation. |
| Nhấn mạnh (DEC-P01-002) | Đạt: nguồn không có thẻ nhấn mạnh ở đoạn nào; bản dịch không có `*…*`. |
| Dấu thoại | Đạt: số dấu ngoặc kép mở/đóng khớp nguồn ở mọi đoạn. |
| Chú thích | p000122: nguồn có chỉ số chú thích gắn vào mốc giờ; bản dịch giữ “⁶” đúng vị trí. Không kiểm được nội dung chú thích (ngoài phạm vi batch). |
| Phủ định / logic | Không phát hiện đảo nghĩa hay mất phủ định. |
| Người nói | Đạt: p000122 là lời Weiss (sau cái gật đầu ở p000121); p000126, p000128, p000133, p000136, p000138 là lời Tanya; p000134 là Weiss. Không lẫn thoại với nội tâm. |
| Thuật ngữ đã có tiền lệ | Nhất quán với ledger: Liên minh Entente, Cộng hòa, Khối Thịnh vượng chung, Liên bang, Cục Tác chiến, Bộ Tổng tham mưu, cụm tập đoàn quân, Trung úy Weiss, “Thưa các vị”, anh (Weiss, tạm theo ledger giới tính). |

## 3. Phát hiện moderate

**M1 — p000135 (kèm p000120, p000121): đại từ chỉ Tanya trong trần thuật không nhất quán và trái lựa chọn tạm.**
- Vấn đề: p000135 dùng “cô ấy” cho Tanya (“ý cô ấy”), trong khi p000120–p000121 dùng “nó” và p000125/p000132/p000135/p000137 lặp “Tanya”. Ledger Vol 2 (`vol02-ch01-b06-tanya-narration` và các mục trước) chọn “lặp Tanya hoặc lược chủ ngữ”, “nó/cô” chỉ là phương án thay thế; DEC-P01-001 chỉ chuẩn hóa “nó” cho giai đoạn pilot và cấm mở rộng sang giai đoạn khác. “Cô ấy” còn gán giới tính, trái nguyên tắc tránh suy diễn.
- Đề xuất: p000135 → “Hẳn anh đã đoán được phần nào điều Tanya định nói.” (hoặc lược chủ ngữ). p000120 → “Tanya chẳng nói nhiều với ai” giữ, nhưng “thời gian nó phục vụ” → “thời gian phục vụ của Tanya”. p000121 → “Dù sao, bộc lộ sự bực bội cũng chẳng giúp ích gì cho Tanya. Tanya gật đầu … với Trung úy Weiss, người đang nhìn Tanya chờ cho phép” hoặc lược chủ ngữ cho đỡ lặp. Nếu coordinator muốn giữ “nó” theo DEC-P01-001 thì phải dùng đồng bộ cho cả batch (đổi “cô ấy” ở p000135 và các lần lặp tên) và ghi rõ trong ledger.

**M2 — p000132: “cầm chân Đại quân” lệch nghĩa quân sự.**
- Vấn đề: nguồn nói quân Entente có khả năng đẩy lùi/chặn được Đại quân trong khi vẫn trụ vững trước áp lực của cụm tập đoàn quân Đế quốc. “Cầm chân” nghĩa là kéo chân, khiến đối phương không tiến hay rút được, ít hàm ý đẩy lùi; đồng thời văn cảnh là Đại quân đã rút (p000128), nên “cầm chân” còn mâu thuẫn với trạng thái đã rút đi. Nghĩa kết quả bị suy yếu: lập luận “phải có viện trợ” dựa vào việc họ chống đỡ thành công.
- Đề xuất: “Khả năng quân đội họ chặn đứng được Đại quân, đồng thời vẫn đứng vững trước áp lực từ cụm tập đoàn quân Đế quốc trong khu vực, …” (phương án: “chống đỡ/đẩy lùi”). Độ tin cậy 0,75.

**M3 — p000122: “hành quân đường dài” không hợp với chuyển động trên không (đề xuất 1).**
- Vấn đề: “hành quân” mặc định là di chuyển bộ/đường bộ; câu kế tiếp bàn “kế hoạch bay” và đơn vị là pháp sư không quân, nên người đọc hiểu “hành quân” và “bay” như hai việc tách rời. Từ nguồn là “maneuver” (cơ động), cùng họ với mục tiền lệ “chiến tranh cơ động” trong ledger.
- Đề xuất: xem mục 5. Sửa thành “cuộc cơ động đường dài hướng về kho tiếp tế” hoặc “chuyển quân đường dài bằng đường không” nếu muốn rõ (không khuyến nghị, thêm chi tiết nguồn không nêu).

## 4. Phát hiện minor

- **m1 — p000122 (đề xuất 2):** “lộ trình bay” hẹp hơn “kế hoạch bay”; cuộc họp đại đội trưởng quyết định cả tuyến, độ cao, thời điểm, đội hình. Đề xuất “kế hoạch bay” (xem mục 5).
- **m2 — p000139 (đề xuất 4):** “những con vật chính trị” nghe như lời chửi và lạ tai; xem mục 5 (đề xuất “động vật chính trị”). Không phải lỗi nghĩa nên xếp minor.
- **m3 — p000120:** “mình chỉ nghĩ rằng” làm nhẹ “chỉ có thể nghĩ là” (mức chắc chắn: không còn cách giải thích nào khác). Đề xuất “mình chỉ có thể nghĩ rằng”. Cũng: “bị buộc” (forced) ở câu thử đi thử lại bị lược; “chiến thuật mới” cho cụm gốc thiên về “kế/mưu lược mới” — chấp nhận được. Thuật ngữ “Cục Công nghệ” và “đơn vị huấn luyện” (đơn vị giáo quan) chưa thấy trong ledger — xem rủi ro.
- **m4 — p000121:** “với vẻ nhân từ với” lặp “với” và “nhân từ” hơi nặng (bố thí, từ bi). Đề xuất “gật đầu rộng lượng với Trung úy Weiss…” hoặc “gật đầu ra vẻ khoan dung”.
- **m5 — p000125:** “cho ra hồn” thêm đánh giá chất lượng; nguồn chỉ nói “một dạng lời khuyên nào đó” (hàm ý hời hợt/tạm bợ). Đề xuất “cố gắng chắp vài lời khuyên đại loại”.
- **m6 — p000130:** “đáng kể” yếu hơn “đáng gờm/hùng hậu” (formidable). Đề xuất “đã chìa tay giúp đỡ đáng gờm”/“hết sức đáng kể”.
- **m7 — p000139:** (a) giữ nguyên “raison d’état” bằng tiếng Pháp ổn nhưng người đọc Việt có thể cần cách đọc quen thuộc; cân nhắc “lý do quốc gia (raison d’état)”, thuộc thuật ngữ mới cần ghi vào ledger; (b) “kẻ bốc đồng gây chiến” biến Entente thành một người, trong khi nguồn là mệnh đề quan hệ về quốc gia; đề xuất “…Liên minh Entente, bên gây chiến vì bốc đồng, …”; (c) “Hẳn người dân … có thể yên tâm” đúng ý mỉa mai, giữ.
- **m8 — p000140:** kéo dài âm “soooo” (nhấn mạnh khẩu ngữ) bị mất; đề xuất “yêu thích nó đến mê mẩn”/“yêu lắm lắm”. “xúi nó đối đầu” thêm sắc thái xúi giục; “cho nó đấu với Đế quốc” sát hơn.
- **m9 — p000118, p000123:** (p000118) dấu ba chấm mở đầu thoại bị lược; cân nhắc ““… Vậy nên …”. (p000123) “tương tác được nghi thức hóa” cứng; đề xuất “những buổi trao đổi mang tính nghi thức như thế này”.

## 5. Đề xuất thuật ngữ tạm (không nâng canon)

| # | Thuật ngữ | Đoạn | Đề xuất của translator | Khuyến nghị tạm | Thay thế | Lý do | Độ tin cậy |
|---|---|---|---|---|---|---|---|
| 1 | long-range maneuver | p000122 | cuộc hành quân đường dài | **cuộc cơ động đường dài** | cuộc hành quân đường dài (nếu coordinator muốn giữ) | Nguồn là cơ động; cuộc di chuyển liên quan đến bay (pháp sư không quân) nên “hành quân” gợi bộ binh/đường bộ. “Cơ động” trung tính, khớp tiền lệ “chiến tranh cơ động” và “thao trường”. | 0,6 |
| 2 | flight plan | p000122 | lộ trình bay | **kế hoạch bay** | lộ trình bay | “Kế hoạch bay” là cách gọi chuẩn trong hàng không; cuộc họp quyết định nhiều hơn tuyến bay. | 0,7 |
| 3 | total war | p000132 | chiến tranh tổng lực | **chiến tranh tổng lực** (giữ) | chiến tranh toàn diện | Cách dùng phổ biến trong văn lịch sử quân sự tiếng Việt; “tổng chiến” không có tiền lệ và dễ gây khó hiểu. Giữ nguyên ý “dồn toàn bộ sức mạnh quốc gia”. | 0,7 |
| 4 | political animals | p000139 | những con vật chính trị | **động vật chính trị** (“những động vật chính trị đúng nghĩa”) | những kẻ làm chính trị thứ thiệt (nếu ưu tiên tự nhiên, nhưng mất hình ảnh động vật); con vật chính trị | “Động vật chính trị” gợi tương ứng với cụm triết học quen thuộc và giữ hình ảnh động vật để song song với “chó chọi” ở p000140. “Con vật” nghe như xúc phạm. | 0,55 |

Ghi chú: cả bốn chỉ là đề xuất tạm, không tự nâng thành canon; không ảnh hưởng cốt truyện nên không cần hỏi người dùng. Đề xuất 1 và 2 nên đồng bộ với nhau (cơ động đường dài + kế hoạch bay) trong p000122.

## 6. Rủi ro / cần theo dõi

- Đại từ Tanya trong trần thuật: ledger Vol 2 và DEC-P01-001 chưa thống nhất; M1 cần coordinator chọn một quy ước cho cả Vol 2 để các batch sau không lẫn “nó/cô/lặp tên”.
- Thuật ngữ chưa có mục ledger riêng: “Cục Công nghệ” (Technology), “đơn vị huấn luyện” (instructor unit), “Đại quân” (chỉ có mục “các sư đoàn Đại quân”), “kho tiếp tế”, “chỉ huy” khi Weiss gọi Tanya (p000134), “raison d’état”. Nên ghi vào ledger như đề xuất.
- Cách gọi “Chỉ huy” (p000134) có thể cần đồng bộ với cách gọi Tanya của các đơn vị khác; thiếu căn cứ để kết luận trong batch này.
- Giới tính Weiss (“anh”) dựa vào đại từ nguồn ở batch khác trong ledger; giữ nhất quán.

## 7. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-02-b06-review
state: done
reviewed_segments: 23
serious: 0
moderate: 3
minor: 9
review_path: reviews/prose/vol-02/ch-02-b06-claude.md
unresolved_findings: [M1, M2, M3]
validator: not_run
diff_check: not_run
commit: null
next_action: translator_fix_then_commit
```
