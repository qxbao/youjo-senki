# Báo cáo phản biện vol-02-ch-01-b10 (lô chẵn)

- Người phản biện: Claude (reviewer). Chỉ đọc: handoff b10, `work/vol-02/batches/ch-01-b10-source.jsonl`, `translations/vol-02/ch-01-b10.jsonl`, canon, sổ pending. Không đọc bản dịch/nguồn lô khác; không sửa tệp nào ngoài báo cáo này.
- Hash gói nguồn khớp handoff (`af1f7fc9…c6d99`). 32/32 `segment_id` khớp nguồn đúng thứ tự p000244–p000275; `source_sha256` từng dòng khớp; mọi dòng `status: draft`.
- Quy ước đối chiếu: không chép câu nguồn; chỉ dùng thuật ngữ gốc ngắn và mã đoạn (rút gọn `pNNNNNN` = `YS-LN02/Text/part0010.xhtml/pNNNNNN`).

## 1. Kết luận

Nghĩa, phủ định, chủ thể thoại, cấp bậc và logic nhìn chung trung thành; không có lỗi nghiêm trọng. Có **2 lỗi mức vừa** (một chỗ thiếu nhấn mạnh so với nguồn, một chỗ lệch đại từ so với DEC-P01-001) và một số lỗi nhẹ. Cần sửa 2 mục vừa trước khi commit.

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 2 |
| Nhẹ | 11 |

## 2. Phát hiện cần xử lý

### Mức vừa

**V1 — p000264: thiếu nhấn mạnh ở cụm cuối (DEC-P01-002).**
Nguồn (XHTML) có hai vùng `<em>`: câu nội tâm về "bonus level" và cặp câu hô tiến lên ở cuối đoạn. Bản dịch chỉ bọc `*…*` vùng đầu; vùng sau ("Tiến lên nào! Cứ tiến lên mãi!") để phẳng. Đề xuất: bọc `*Tiến lên nào! Cứ tiến lên mãi!*`; giữ nguyên vùng nghiêng đầu. Các nhấn mạnh còn lại khớp: p000267 chỉ một chữ "couldn't" → `*chẳng*` đúng phạm vi; không đoạn nào khác có `<em>` nên không có nhấn mạnh thừa.

**V2 — p000274: dùng "cô" cho Tanya trong trần thuật, trái DEC-P01-001.**
DEC-P01-001 (đã duyệt) quy định trần thuật về Tanya dùng "nó"; các đoạn p000254, p000264, p000275 trong lô đều theo "nó", riêng p000274 dùng "cô" bốn lần ("ngắm nhìn… cô", "hợp với cô", "Cô lướt đi", "trong lòng cô"). Hệ quả: đổi đại từ giữa hai đoạn liền nhau; thêm sắc thái nữ tính/thiện cảm không có căn cứ trong DEC; đồng thời "hẳn nó sẽ chứng minh" dùng "nó" chỉ bức ảnh, dễ nhầm với "nó" = Tanya ở p000275. Đề xuất: đổi "cô" → "nó" (hoặc lặp "Tanya" ở chỗ cần rõ), và đổi "nó" chỉ bức ảnh thành "bức ảnh ấy". Nếu cố ý dùng "cô" để tách vẻ ngoài khỏi nội tâm thì đó là quyết định canon cần ghi, không tự áp dụng trong lô.

### Mức nhẹ

| # | Mã đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| N1 | p000247 | "trọng dụng" hàm ý tin cậy/đề bạt; nguồn chỉ là "dùng cho tốt" mang tính thực dụng. | "tận dụng cho đúng chỗ" / "dùng cho ra dùng". |
| N2 | p000253 | "cuối cùng mình cũng phải thừa nhận" biến việc *sớm muộn sẽ phải* thừa nhận (tương lai) thành đã xảy ra. | "rồi cũng phải thừa nhận" / "sớm muộn gì cũng phải thừa nhận". |
| N3 | p000255 | "khí thế" (sĩ khí/đà tiến) lệch với "mood" (không khí). | "làm mất không khí/làm cụt hứng mọi người". |
| N4 | p000260 | "lương tri" thường là lương tâm → thêm nét đạo đức; nguồn là "common sense" mang tính thực tế (cố ý tránh sắc thái phán xét theo style-guide). | "chút lẽ thường/óc thực tế". |
| N5 | p000261 | "…tiến xa hơn rồi" lặp "rồi" sau "Được rồi". | Bỏ một "rồi". |
| N6 | p000267 | "Nghiền nát" dùng cho cả "demolished" và "run them over" trong một đoạn; mất sự phân biệt. | Đổi một trong hai (vd. "cán bẹp"/"nghiền" cho lời huênh hoang). |
| N7 | p000269 | "chút phấn khích" thu nhỏ độ lớn; nguồn là "một thứ phấn khích nào đó" (không nói ít). | "một thứ phấn khích nào đó". |
| N8 | p000272 | Lời thoại độc lập này giữ dấu ngoặc kép ngoài, trong khi các đoạn thoại độc lập khác trong lô (p000244–p000263 …) bỏ dấu ngoặc. | Thống nhất theo quy ước đang dùng trong lô (bỏ ngoặc ngoài) hoặc đối chiếu quy ước JSONL hiện hành; không có DEC riêng nên chỉ báo là lệch nội bộ lô. |
| N9 | p000275 | "không hề áp dụng chế độ tắt đèn" mạnh hơn nguồn (hiện trạng "chưa"). | "chưa áp dụng". |
| N10 | p000275 | "không có máy bay hay pháp sư nào đánh chặn" cụ thể hóa "aerial or magical interception" thành loại phương tiện. | "không có lực lượng đánh chặn trên không hay bằng pháp thuật" (giữ trung tính). |
| N11 | p000244, p000257, p000267 | Cách ghi số thứ tự lẫn nhau trong lô: "Đệ Thất", "số Mười bảy", "Đại đội Bốn", "203". | Chọn một kiểu (vd. chữ số: "số 7", "số 17", "Đại đội 4", "203") và ghi vào ledger như đề xuất. |

Ghi chú không tính lỗi: p000246/p000249/p000262 dịch "ma'am" thành "Thiếu tá" — được hỗ trợ trong lô bởi p000273 (Thiếu tá Tanya) và p000265 (Trung úy Weiss); xưng hô cặp Tanya–Weiss trong lô nhất quán (Tanya: "tôi/anh"; Weiss: "tôi/Thiếu tá"). Nên ghi đây là lựa chọn tạm, chưa canon (DEC-P01-001 giới hạn suy luận về xưng hô).

## 3. Kiểm tra theo tiêu chí

- **Nghĩa/phủ định:** đúng ở các điểm dễ sai — p000251 (không ai bị thương dù nhẹ), p000253 (không cho rằng có thương vong), p000267 (câu hỏi tu từ phủ định, giữ đúng hướng "ai cũng làm được"), p000270 (khói vẫn tan). Không phát hiện đảo/mất phủ định.
- **Chủ thể/người nói:** p000244 (không rõ người báo; dịch trung tính), p000245–p000263 phân vai Tanya/Weiss đúng; p000258 Tanya, p000257 Weiss. p000266 "họ" chỉ binh sĩ — chấp nhận được.
- **Giọng/đại từ:** nội tâm "mình" và trần thuật "nó" đúng DEC ngoài ngoại lệ V2. p000250 "cảm thấy mình" là phản thân trong câu, không vi phạm.
- **Cấp bậc:** Thiếu tá/Trung úy/Đại tá nhất quán; "Chỉ huy Tiểu đoàn" (p000267) và "chỉ huy tiểu đoàn" (p000273) cùng một cách hiểu. Không đổi cấp.
- **Nhấn mạnh:** xem V1; p000267 đúng.
- **Thời gian/giả định:** p000274 giả định "nếu có ảnh" giữ đúng; riêng p000253 xem N2.

## 4. Nhóm pending của translator

Tất cả ở dạng đề xuất tạm, không canon, không dựa vào lô khác; căn cứ chỉ trong b10.

### 4.1 air fleet / Air Fleet (p000244, p000267)

- Hiện trạng: "không hạm đội" (độ tin cậy translator 0.3).
- Đánh giá: "hạm" gợi tàu thủy/đội tàu, "không hạm" là tạo từ chưa quen thuộc và dễ đọc thành "đội tàu bay/khinh khí cầu". Căn cứ trong lô chỉ cho biết đây là lực lượng khác với tiểu đoàn pháp sư (p000267 đặt hai bên cạnh nhau; p000244 báo "đang trên đường tới"), đủ để chọn cách nói trung tính nhưng chưa đủ để chốt cấp tổ chức.
- **Đề xuất tạm:** "Hạm đội Không quân" (số hiệu theo kiểu chọn ở N11, vd. "Hạm đội Không quân số 7" ở p000244). Độ tin cậy 0.4.
- **Phương án thay thế:** "không hạm đội" (hiện tại; chấp nhận được nếu giữ nhất quán), "đội bay", "phi đội".
- **Bất định:** cấp tổ chức; "fleet" có thể là một đơn vị trên không lớn hơn phi đội, có thể không liên quan hải quân. p000267 viết hoa "Air Fleet" trong cụm "Army and Air Fleet" nhưng không nêu số hiệu; không nên mặc định đồng nhất với "Seventh" ở p000244 trong bản dịch (hiện dịch đúng khi không thêm số hiệu ở p000267).
- Phụ thuộc cốt truyện: không.

### 4.2 Aerial Mage Battalion (p000265, p000267, p000271)

- Hiện trạng: "Tiểu đoàn Pháp sư Không quân 203" (0.65, dùng lại thuật ngữ tạm đã có).
- Đánh giá: phần "Tiểu đoàn … 203" và "Pháp sư" đúng. Vấn đề là "Không quân" (binh chủng air force) cho "aerial" — trong lô, tiểu đoàn được đặt tương phản với "air fleet" như hai lực lượng khác nhau (p000267), nên "Không quân" có thể ngầm đặt tiểu đoàn vào một binh chủng mà nguồn không nêu. "Aerial" chỉ môi trường hoạt động.
- **Đề xuất tạm:** "Tiểu đoàn Pháp sư Không trung 203"; độ tin cậy 0.5.
- **Phương án thay thế:** "Tiểu đoàn Pháp sư trên không 203" (trung tính nhất), "Tiểu đoàn Pháp sư Không quân 203" (hiện tại).
- **Bất định:** nếu coordinator ưu tiên nhất quán với thuật ngữ tạm đã dùng ở lô trước, có thể giữ nguyên hiện tại; không đủ nghiêm trọng để chặn. Nếu đổi thì phải đổi đồng loạt ở cả ba mã đoạn và ở lô khác (ngoài phạm vi phản biện này).
- Phụ thuộc cốt truyện: không (tên đơn vị), nhưng nên ghi vào ledger là đề xuất.

### 4.3 White Silver (p000274)

- Hiện trạng: "Bạch Ngân" (0.4).
- Đánh giá: trong b10 chỉ có một căn cứ ngữ cảnh — biệt hiệu hợp với vẻ dịu dàng, tao nhã của nhân vật khi nhìn thành phố. "Bạch Ngân" (Hán-Việt) giữ được sắc thái trang nhã/lạnh sáng, đọc tự nhiên như biệt hiệu; "Bạc Trắng" sát nghĩa nhưng nghe như mô tả vật liệu; "Bạch Kim" nghĩa là bạch kim (platinum), lệch nghĩa.
- **Đề xuất tạm:** giữ "Bạch Ngân" (đặt trong ngoặc kép như hiện tại); độ tin cậy 0.5.
- **Phương án thay thế:** "Bạc Trắng"; tránh "Bạch Kim".
- **Bất định:** trong lô không có căn cứ nói biệt hiệu này đến từ ngoại hình hay từ nguồn gốc khác (lore); không phỏng đoán.
- Phụ thuộc cốt truyện: có thể (biệt hiệu nhân vật chính) → chỉ ghi đề xuất, không nâng canon.

### 4.4 Thuật ngữ chưa vào nhóm pending nhưng nên ghi vào ledger (đề xuất, không canon)

- p000267: Eastern Army Group → "Cụm tập đoàn quân Phương Đông" ("Phương Đông" nghe như phương Đông địa lý-văn hóa; xét "Cụm tập đoàn quân Đông"/"phía Đông"); Seventeenth Army → "Tập đoàn quân số Mười bảy"; Dacian Army → "Quân đội Dacia"; strategic reserves → "lực lượng dự bị chiến lược".
- p000268: Principality of Dacia → "Công quốc Dacia".
- p000254–p000265: bonus level → "màn chơi thưởng thêm" (nội tâm Tanya, giữ nguyên nhấn mạnh).
- Cách xưng hô Tanya–Weiss và dịch "ma'am" thành chức danh (xem ghi chú phần 2).

## 5. Rủi ro

- Sửa V2 (đổi "cô" → "nó") và V1 (nhấn mạnh) là thay đổi nhỏ, không ảnh hưởng nghĩa; rủi ro thấp.
- Nếu đổi thuật ngữ ở 4.1/4.2, cần giữ nhất quán giữa các lô; chỉ coordinator quyết định ledger.
- Chưa xác minh `validator`/`diff_check` (không thuộc quyền reviewer).

## 6. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-01-b10
state: done
segment_ids: [p000244..p000275]   # 32 mã, thứ tự đúng
review_path: reviews/prose/vol-02/ch-01-b10-claude.md
files_written: [reviews/prose/vol-02/ch-01-b10-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 2, minor: 11}
unresolved_findings:
  - {severity: moderate, segment_id: p000264, issue: thiếu nhấn mạnh cụm cuối (DEC-P01-002), resolution: bọc *...* cụm "tiến lên"}
  - {severity: moderate, segment_id: p000274, issue: dùng "cô" thay "nó" cho Tanya (DEC-P01-001), resolution: đổi sang "nó"/tên, tách "nó" chỉ bức ảnh}
  - {severity: minor, segment_id: "p000247,p000253,p000255,p000260,p000261,p000267,p000269,p000272,p000275,p000244/p000257/p000267", issue: xem N1–N11, resolution: xem bảng}
term_recommendations:
  - {source_term: air fleet / Air Fleet, proposed_vi: "Hạm đội Không quân", alternatives_vi: [không hạm đội, đội bay, phi đội], segment_ids: [p000244, p000267], confidence: 0.4, status: pending}
  - {source_term: Aerial Mage Battalion, proposed_vi: "Tiểu đoàn Pháp sư Không trung 203", alternatives_vi: ["Tiểu đoàn Pháp sư trên không", "Tiểu đoàn Pháp sư Không quân (hiện tại)"], segment_ids: [p000265, p000267, p000271], confidence: 0.5, status: pending}
  - {source_term: White Silver, proposed_vi: "Bạch Ngân", alternatives_vi: ["Bạc Trắng"], segment_ids: [p000274], confidence: 0.5, status: pending, note: tránh "Bạch Kim"}
risks: [thuật ngữ đơn vị cần nhất quán liên lô, biệt hiệu có thể ảnh hưởng lore — không nâng canon]
commit: null
next_action: translator_fix_v1_v2_then_signoff   # coordinator ghi ledger các đề xuất
```
