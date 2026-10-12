# Báo cáo phản biện — vol-02-ch-01-b12

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon).
- Phạm vi: `p000299`–`p000326` (28 đoạn), gồm handoff b12, gói nguồn cục bộ, `translations/vol-02/ch-01-b12.jsonl`, canon và sổ pending.
- Kích hoạt: `even_batch`, `new_pending_terms`, `rank_map_conflict`.
- Báo cáo không trích câu nguồn. Thuật ngữ nguyên gốc ngắn và mã đoạn chỉ dùng để nhận diện. Mọi lựa chọn dưới đây là đề xuất tạm, không phải canon.

## 1. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự mã đoạn | 28/28, liên tục p000299→p000326, khớp 1–1 giữa nguồn và bản dịch |
| Hash gói nguồn | `8616a6c5…3f19` khớp `source_package_sha256` |
| Hash canon (5 tệp) | Khớp handoff (glossary, style-guide, characters, decisions, glossary-pending) |
| Số từ nguồn | 825 (theo regex của handoff), khớp |
| Nhấn mạnh (DEC-P01-002) | Nguồn có đúng 2 chỗ in nghiêng: một từ ở p000314 (đại từ ngôi thứ nhất) và từ nối đầu p000326. Bản dịch có `*Tôi*` (p000314) và `*Tuy nhiên*` (p000326). Không thừa, không thiếu. **Đạt.** |
| Dấu chú thích | p000305 có một dấu chú thích số 4; bản dịch giữ `⁴`, liên tục với `³` ở b07. Nội dung chú thích không nằm trong gói nên không đối chiếu được. |
| `notes` | Rỗng ở cả 28 đoạn |
| Đại từ Tanya (DEC-P01-001) | Trần thuật dùng "nó" (p000315, 317, 322, 324); nội tâm dùng "mình" (p000311, 312, 318, 319, 321). Khớp quy ước. |
| Phủ định / logic | Các phủ định ở p000299, p000302, p000305, p000310–311 và cấu trúc nhượng bộ ở p000324, p000326 đều giữ đúng. |

Nhìn chung bản dịch bám nghĩa tốt, giọng mỉa mai ở p000301 và p000305 được giữ. Không có lỗi nghiêm trọng.

## 2. Phát hiện

Đếm: **nghiêm trọng 0 · vừa 3 · nhẹ 12**.

### Mức vừa

**M1 — p000307: cấp bậc Weiss lệch bản đồ tạm hiện có.**
- Bản dịch dùng "Thiếu úy Weiss". Sổ pending b02, b06, b08 và b09 đều dùng Weiss = Trung úy, Serebryakov = Thiếu úy.
- Trong b12, nguồn chỉ có chức danh chung "Lieutenant" cho cả hai người, không có "Second"/"First". Vì vậy b12 không cung cấp bằng chứng mới để đổi bản đồ. Tiếng Anh vẫn bỏ "Second/First" khi gọi trực tiếp. Dịch Weiss thành "Thiếu úy" làm hai người cùng cấp, mâu thuẫn với các lô trước.
- Đề xuất: p000307 → "Trung úy Weiss". Các chỗ Serebryakov (p000299, 313, 318) đã đúng "Thiếu úy".
- Xem mục 3.1.

**M2 — p000307 (và p000320): đại từ "cô" mang giới tính.**
- p000307: "cô" chỉ Weiss. Trong b12 không có căn cứ nào về giới của Weiss. p000316 chỉ đối lập giọng "cứng rắn, đậm chất lính" với giọng của Serebryakov, và điều đó nói về giọng chứ không nói về giới. DEC-P01-001 cấm suy giới tính từ ngữ cảnh thiếu.
- p000320: "Cô" chỉ Serebryakov. Có dấu hiệu nghiêng về nữ ở p000318, vì lý do che đậy nhắc "một cô gái" và có thể chỉ Serebryakov. Nhưng đoạn đó là lời định nói sau này, chưa đủ để coi là xác nhận. Sổ pending b04 (`vol02-ch01-b04-serebryakov-address`) cũng ghi rõ "không dùng xưng hô có giới tính" khi Tanya gọi Serebryakov.
- Đề xuất:
  - p000307 → "…nhưng Trung úy đang nghĩ mọi chuyện hơi quá thẳng tuột đấy." (hoặc lược chủ ngữ).
  - p000320 → "Ừm, được thôi. Thiếu úy nói đúng, tôi nên làm vậy."
- Mức độ vừa vì sai giới tính nhân vật rất khó thu hồi nếu lan sang các lô sau.

**M3 — p000322, p000325: mất lối nói ngọng/trẻ con có chủ ý.**
- Nguồn cố ý viết sai âm ở một từ trong p000322 và một từ trong p000325. Nguồn còn nêu rõ ý định "nghe thật giống trẻ con" (p000320, p000322). Bản dịch dịch cả hai câu thành tiếng Việt chuẩn, nên chi tiết phát âm bị mất.
- Style guide ghi giữ chi tiết phát âm khi nguồn có nêu. Không tự thêm ghi chú vào bản dịch, nhưng nên có dấu hiệu ngọng tương đương.
- Đề xuất: dùng cùng một kiểu ngọng nhẹ, nhất quán ở cả hai đoạn, ví dụ thay một âm đầu ở từ chính của câu ("cảnh báo", "bắt đầu"). Các phương án và quy ước ghi tại mục 3.4. Cách này không đổi nghĩa.

### Mức nhẹ

| # | Đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| N1 | p000303 | "sai sót **của tôi**" thêm sở hữu. Nguồn chỉ nói "the error", không nêu rõ ai chịu lỗi. | "Xin thứ lỗi cho sai sót, thưa Thiếu tá." |
| N2 | p000312 | "đám cấp dưới" thêm sắc thái miệt thị không có trong nguồn (style guide cấm). "Đế quốc" viết hoa dù nguồn viết thường. "giọng điệu đĩnh đạc" thu hẹp "manner" thành giọng nói. | "những cấp dưới này"; "lính đế quốc"; "với vẻ đĩnh đạc" |
| N3 | p000314 | "phải làm" đổi câu hỏi ngạc nhiên ("muốn tôi làm sao?") thành nghĩa bị bắt buộc. | "Thiếu tá muốn *tôi* làm việc đó sao?" (giữ `*tôi*`) |
| N4 | p000313 | "Ra thông báo cảnh báo… Ra lệnh…" lặp "ra" và thừa "thông báo". | "Đưa ra cảnh báo. Ra lệnh sơ tán…" |
| N5 | p000301 | "quả thật… thật" lặp; "hơi… một chút" thừa; "luật tồi" mạnh hơn nghĩa "soạn thảo kém"; "hợp tình hợp lý phản đối" lệch trật tự. | "…mà chẳng ai có thể phản đối một cách hợp lý"; "luật được soạn vụng" |
| N6 | p000302 | "việc diễn giải **lại** khó khăn" và "khá đơn giản" thêm chữ không có. | "diễn giải khó khăn"; "xử lý đơn giản" |
| N7 | p000305 | "đặt **xưởng** làm giỏ bánh mì" thêm "xưởng". | "vì làm giỏ bánh mì trong một cơ sở…" |
| N8 | p000307 | "lo lắng" yếu hơn "fear" (nỗi sợ mất yếu tố bất ngờ). | "lo ngại" hoặc "e ngại" |
| N9 | p000316 | Bản dịch bỏ chức danh trước Serebryakov và Weiss trong trần thuật; "non nớt" nặng hơn "unsophisticated" (thiếu chải chuốt). | Khôi phục "Thiếu úy / Trung úy" nếu coordinator muốn giữ parity; "hơi ngây ngô" hoặc "chưa chải chuốt" |
| N10 | p000321 | "A!" đọc như ngạc nhiên, nguồn là bực bội. "lên mặt đạo đức" thêm bình diện đạo đức. | "Hừ!/Chậc!"; "ra vẻ cao siêu" |
| N11 | p000308 / 321 | "luật pháp quốc tế" và "luật quốc tế" lẫn nhau; p000304 "nhà máy sản xuất vũ khí" vs p000305 "nhà máy vũ khí". | Chọn một dạng cho cả chương |
| N12 | p000304 | "phát thông báo… phát trên kênh…" lặp "phát". | "Này, ra thông báo sơ tán đi — phát qua kênh…" |

## 3. Khuyến nghị thuật ngữ (đề xuất tạm, không phải canon)

### 3.1 Cấp bậc Serebryakov / Weiss — `vol02-ch01-b12-lieutenant-map`
- **Chọn tạm:** Serebryakov = **Thiếu úy**; Weiss = **Trung úy**; Tanya = **Thiếu tá**; "ma'am" → "thưa Thiếu tá" (p000303).
- **Phương án thay thế:** (a) Trung úy cho cả hai; (b) Thiếu úy cho cả hai (đề xuất gốc của translator, không khuyến nghị).
- **Độ tin cậy:** 0,55.
- **Căn cứ:** Chỉ có sổ pending (b02, b06, b08, b09, b11). b12 chỉ nêu "Lieutenant" chung, nên không có bằng chứng bác bản đồ hiện có.
- **Bất định:** Phụ thuộc chuỗi cấp bậc của nguồn mà b12 không cho thấy. Đây chỉ là chênh lệch cấp bậc, không ảnh hưởng cốt truyện, nên không cần hỏi người dùng.
- **Đoạn:** p000299, p000307, p000313, p000316 (và p000318 cho Serebryakov).
- **Việc coordinator:** cập nhật `proposed_vi` của mục b12 thành "Thiếu úy Serebryakov / Trung úy Weiss", hạ phương án (b) thành phương án thay thế.

### 3.2 Kênh phát thông báo — `vol02-ch01-b12-international-distress-channel`
- **Chọn tạm:** **kênh báo nguy quốc tế** (giữ phương án của translator).
- **Phương án thay thế:** "kênh cấp cứu quốc tế"; "kênh cứu nạn quốc tế"; "tần số báo nguy quốc tế".
- **Độ tin cậy:** 0,6.
- **Căn cứ:** Đây là kênh vô tuyến (p000304 "phát", p000322 có ống nghe, p000326 nói về radio) dùng để phát thông báo sơ tán theo quy định. Dịch sát chữ "distress" bằng "báo nguy" ít suy diễn nhất. Hai đoạn p000304 và p000324 nhất quán.
- **Bất định:** Tiếng Việt có thể có tên gọi chuẩn hơn ("cấp cứu/cứu nạn") theo thông lệ hàng hải hoặc hàng không, nhưng b12 không xác định. Chưa có căn cứ đổi.

### 3.3 Cách gọi trực tiếp Serebryakov/Weiss — mục mới đề xuất
- **Chọn tạm:** gọi theo cấp bậc ("Thiếu úy", "Trung úy"), tránh "cô/anh" khi nguồn không nêu giới.
- **Phương án thay thế:** "cô" cho Serebryakov (nếu về sau có căn cứ rõ hơn p000318).
- **Độ tin cậy:** 0,6.
- **Đoạn:** p000307, p000320.
- **Bất định:** p000318 gợi ý nghiêng nữ cho Serebryakov nhưng chưa chắc; không có dữ liệu gì cho Weiss trong b12.

### 3.4 Lối nói ngọng trẻ con — mục mới đề xuất
- **Chọn tạm:** ngọng nhẹ, nhất quán ở p000322 và p000325, chỉ ở từ chính của câu, không kéo dài cả đoạn.
- **Phương án thay thế:** giữ văn bản chuẩn nhưng thêm dấu hiệu bằng động từ chỉ tiếng nói ("giọng non choẹt"), nhưng cách này không dùng được vì không thêm chi tiết ngoài nguồn.
- **Độ tin cậy:** 0,5.
- **Bất định:** cách gõ âm ngọng tiếng Việt tương đương là lựa chọn dịch thuật, không phải sự kiện của nguồn.

## 4. Rủi ro còn lại

- Nếu M1 không sửa, "Thiếu úy Weiss" sẽ lan sang các lô sau và tạo hai bản đồ cấp bậc song song.
- M2 là rủi ro giới tính: "cô" cho Weiss chưa có căn cứ.
- M3 là mất chi tiết văn phong mà người dịch sau dễ bỏ qua.
- Không phát hiện quyết định ảnh hưởng cốt truyện. Không cần hỏi người dùng.

## 5. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-01-b12
state: done
segment_ids: [YS-LN02/Text/part0010.xhtml/p000299, YS-LN02/Text/part0010.xhtml/p000326] # 28 đoạn liên tục
files_written: [reviews/prose/vol-02/ch-01-b12-claude.md]
review_path: reviews/prose/vol-02/ch-01-b12-claude.md
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 3, minor: 12}
unresolved_findings: [M1, M2, M3, N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12]
term_recommendations:
  - id: vol02-ch01-b12-lieutenant-map
    proposed_vi: "Thiếu úy Serebryakov / Trung úy Weiss"
    alternatives_vi: ["Trung úy cho cả hai", "Thiếu úy cho cả hai"]
    segment_ids: [p000299, p000307, p000313, p000316]
    confidence: 0.55
    status: pending
  - id: vol02-ch01-b12-international-distress-channel
    proposed_vi: "kênh báo nguy quốc tế"
    alternatives_vi: ["kênh cấp cứu quốc tế", "kênh cứu nạn quốc tế", "tần số báo nguy quốc tế"]
    segment_ids: [p000304, p000324]
    confidence: 0.6
    status: pending
  - id: vol02-ch01-b12-address-to-lieutenants
    proposed_vi: "gọi theo cấp bậc, tránh cô/anh"
    alternatives_vi: ["cô cho Serebryakov nếu có căn cứ thêm"]
    segment_ids: [p000307, p000320]
    confidence: 0.6
    status: pending
  - id: vol02-ch01-b12-childish-speech
    proposed_vi: "ngọng nhẹ nhất quán ở từ chính"
    alternatives_vi: []
    segment_ids: [p000322, p000325]
    confidence: 0.5
    status: pending
risks: [rank_map_divergence, gendered_pronoun_unsupported, lost_mispronunciation]
commit: null
next_action: translator_fix_M1_M2_M3_then_reviewer_signoff
```
