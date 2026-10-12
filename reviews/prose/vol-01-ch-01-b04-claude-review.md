# Phản biện — vol-01 Chương 1, lô b04

Người phản biện: Claude. Task: `vol-01-ch-01-b04-review`. Phạm vi: 11 đoạn p000044–p000054, tiền tố đầy đủ `YS-LN01/Text/chapter003b.xhtml/`. Báo cáo không chép câu nguồn; chỉ dùng mã đoạn (`pNNNNNN`) và thuật ngữ nguyên gốc ngắn để nhận diện.

Đầu vào đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, handoff `review-ch-01-b04.yml` và `ch-01-b04.yml`, gói nguồn b04 (đọc tại chỗ), bản dịch b04, `work/run-state/pending-terms.yml`, `canon/style-guide.md`, `canon/decisions.md`, `canon/glossary-pending.yml`; `canon/glossary.yml` và `canon/characters.yml` vẫn rỗng.

**Tính chất:** mọi phương án dưới đây là đề xuất tạm theo AGENTS.md, không phải canon, không tự nâng thành quyết định. Không sửa bản dịch, canon, handoff hay sổ pending. Validator/diff_check: not_run; commit: null.

Thang tin cậy: cao ≥ 0,75; vừa 0,5–0,74; thấp < 0,5.

## 1. Kết luận

- Không có hard stop; không có điểm ảnh hưởng cốt truyện cần hỏi người dùng.
- Số phát hiện: nghiêm trọng 0, vừa 3 (p000044, p000051, chính sách đại từ toàn lô), nhẹ 9.
- 11/11 hàng đủ mã đoạn, đúng thứ tự, `source_sha256` khớp giá trị trong handoff; `glossary_version` khớp. (Không tính lại hash gói nguồn trong task này.)
- Nguồn b04 không có chữ nghiêng nào; bản dịch không thêm `*...*` nào: đúng DEC-P01-002. Ngoặc kép giữ đúng ở p000045, p000049, p000050 (hai cụm), p000052.
- Nghĩa nhìn chung chính xác, văn phong tự nhiên. Vấn đề chủ yếu: thì giả định ở p000044, một từ lệch sắc thái ở p000051, và nhất quán đại từ "nó" so với b02–b03.
- Điểm nhìn p000054 (và cùng kiểu ở p000051): cách xử lý hiện tại chấp nhận được, không gán người nói; xem mục 3.

## 2. Phát hiện theo mã đoạn

| Mức | Mã đoạn | Vấn đề | Căn cứ / đề xuất |
|---|---|---|---|
| vừa | p000044 | Nguồn là giả định phản thực tại về quá khứ (nếu đã được nói tự do thì có lẽ đã mô tả như vậy); bản dịch "Nếu được nói thẳng… có lẽ nó sẽ mô tả" biến thành giả định hiện tại/tương lai. Ngoài ra "nó" ở vế sau dễ đọc nhầm là chỉ "chuyện này"; "tự tìm đến cái chết" thêm tính chủ động, nặng hơn "death wish". | Style guide (quy tắc giữ thời gian của giả định). Đề xuất: "Nếu có thể nói thẳng, có lẽ Tanya đã mô tả… như khoảnh khắc chứng kiến khát vọng chết thành hình" (0,7); thay thế "ý muốn chết". Giữ tính phỏng đoán, không diễn giải thành hành động tự sát cụ thể (ghi chú đã nêu đúng ý này). |
| vừa | p000051 | "thấy ái ngại" cho phản ứng với gương mặt như búp bê: trong tiếng Việt "ái ngại" nghiêng về thương cảm/e ngại, trong khi nguồn là cảm giác khó chịu/không thiện cảm ngay cả với chính mình. Đổi bình diện cảm xúc. | Đề xuất: "thấy không mấy thiện cảm"/"thấy khó chịu" (0,6); thay thế "thấy chùn lòng". |
| vừa | p000044–p000054 (toàn lô) | Bản dịch dùng "nó" cho Tanya xuyên suốt (trần thuật) kèm "mình" (nội tâm), đúng DEC-P01-001 (đã duyệt). Nhưng b02–b03 dùng lặp tên/lược chủ ngữ theo mục `P01-tanya-narration-ch01` trong sổ pending (tránh "cô"); b04 chuyển sang "nó" khiến giọng kể đổi giữa các lô cùng chương. DEC-P01-001 ghi "ở giai đoạn này" nhưng không nói rõ có phủ Chương 1 hay không. | Không phải lỗi bản dịch: là mâu thuẫn quy ước. Đề xuất tạm: giữ "nó"/"mình" ở b04 theo canon đã duyệt, coordinator ghi vào sổ pending và giao rà soát đồng bộ b02–b03 sau (hoặc ghi quyết định ngược lại). Độ tin cậy 0,55. Không ảnh hưởng cốt truyện. |
| nhẹ | p000045 | (a) "Chỉ mới ít phút trước" thêm đơn vị thời gian cụ thể; nguồn chỉ nói vừa mới xảy ra. (b) "tin giao tranh nổ ra ở một số khu vực": "đã" của "đã nhận được" làm lệch sắc thái "đã nổ ra". (c) Tên "Liên minh Entente Regadonia" lần đầu có tên đầy đủ; thứ tự từ và nhất quán với "Liên minh Entente" ở b03 chưa có canon. | (a) "Vừa mới đây"; (b) "Chúng tôi nhận được tin giao tranh đã nổ ra ở một số khu vực"; (c) giữ, ghi pending (0,6), thay thế "Liên minh Regadonia Entente". |
| nhẹ | p000046 | "bên dưới nó": "nó" đứng sau "quân ta", dễ hiểu nhầm là chỉ lực lượng thiết giáp thay vì Tanya. "quân ta" là lựa chọn điểm nhìn của Tanya (ghi chú đã nêu). | "bên dưới Tanya" hoặc "phía dưới chỗ Tanya"; giữ "quân ta" (0,6), thay thế "quân bạn". |
| nhẹ | p000047 | Mất "vastly" (vượt trội hẳn/vượt xa) ở quốc lực, công nghệ, vũ trang. "chiêu quảng bá" cho publicity stunt khá nhẹ, mất sắc thái màn trình diễn gây chú ý. | "vượt trội hẳn"/"vượt xa"; "màn quảng bá"/"chiêu gây chú ý" (0,5). |
| nhẹ | p000048 | (a) "giới chỉ huy" cho "the brass" thấp hơn một bậc so với ý "cấp cao"; b03 dùng "lãnh đạo quân đội" cho military leaders. (b) "lý do chính đáng" cho legitimate justification: cùng trục nghĩa với "danh nghĩa chính đáng" đã dùng ở p000043 (b03), nên đồng bộ để giữ liên kết văn bản. | (a) "giới chỉ huy cấp cao"/"cấp trên" (0,5); (b) "danh nghĩa chính đáng" (0,55). Cả hai tùy chọn. |
| nhẹ | p000049 | (a) "các người" (số nhiều) cho đối tượng là nhà nước: chấp nhận, nhưng chưa có quyết định xưng hô. (b) "người tốt bụng" hẹp hơn "người tốt, tử tế"; nguồn không nhấn mạnh lòng tốt theo nghĩa thương người. | (a) giữ, ghi pending (0,5), thay thế "cái đất nước này"/bỏ đại từ; (b) "một người tốt, tử tế" (0,6). |
| nhẹ | p000050 | (a) "hài lòng" mạnh hơn "hoàn toàn không phiền/chấp nhận hoàn toàn". (b) "một vụ chẳng tệ": "vụ" gợi nghĩa vụ việc; "deal" là món lợi/thương vụ. (c) "ngàn năm có một" thay "một phần triệu": thành ngữ chấp nhận được. (d) "Lãnh thổ Norden": cần đồng bộ với "mặt trận Norden" (P01-norden-theater). | (a) "hoàn toàn không phản đối"; (b) "một món hời chẳng tệ"; (c) giữ; (d) giữ (0,6), thay thế "vùng Norden". |
| nhẹ | p000051 | "mà để những điều kiện vốn bất lợi càng thêm tệ": "để" mang nghĩa mục đích, có thể đảo quan hệ logic (nguồn chỉ nói điều kiện còn tệ hơn vì ngoại hình). "Ở đó không dễ lập nhiều thành tích": "nhiều" là thêm nhẹ. | "Ở đó vốn đã khó lập thành tích, mà điều kiện còn tệ hơn vì dù muốn hay không, Tanya… vẫn mang vóc dáng…" (0,6). |
| nhẹ | p000052 | "được bổ nhiệm làm sĩ quan" cho commissioned: "bổ nhiệm" thiên về chức vụ; ngữ cảnh quân sự thường là "được phong quân hàm sĩ quan". Không suy ra quân hàm cụ thể. | "kể từ khi nó nhận quân hàm sĩ quan" (0,55); thay thế giữ nguyên. |
| nhẹ | p000054 | (a) Điểm nhìn: xem mục 3; giữ. (b) "giành nhiều vinh dự và được tuyên dương" cho honors and commendations: "vinh dự" nghiêng về đặc ân hơn là danh hiệu được ghi nhận. | (b) "được vinh danh và khen thưởng" (0,5). Không suy thành huân chương cụ thể. |

p000053: không có lỗi nghĩa. p000045 là lời phát thanh của phóng viên, giọng khẩn cấp và trình tự sự kiện được giữ tốt.

## 3. Điểm nhìn p000054 (và p000051)

- Nguồn p000054 có một câu chuyển sang ngôi thứ nhất ("I also want her…") trong khi đối tượng vẫn là Tanya. Cùng kiểu xảy ra ở câu cuối p000051. Nguồn không có nhãn người nói, không có dấu nhấn mạnh hay ngoặc kép giúp xác định.
- Bản dịch xử lý: "mình" cho ngôi thứ nhất, "nó" cho Tanya, ở cả p000051 và p000054 — nhất quán, giữ nguyên sự chuyển ngôi, không nói rõ ai đang nghĩ, không thêm chú thích về người nói.
- Rủi ro còn lại: "mình" theo DEC-P01-001 là đại từ nội tâm tự quy chiếu của Tanya; dùng trong ngữ cảnh có "nó" chỉ Tanya khiến người đọc có thể hiểu là Tanya tự nói về mình. Điều này nghiêng nhẹ về một cách hiểu mà nguồn không khẳng định. Đề xuất giữ nguyên (0,55). Phương án thay thế trung tính hơn: "tôi" (0,4), nhưng nó lại gợi người kể tách khỏi Tanya; cả hai đều là suy diễn, nên giữ lựa chọn hiện tại và ghi bất định.
- Không suy luận người nói là Tanya, người kể, hay nhân vật khác; không đối chiếu với giọng "tôi/anh" của Chương 0 vì không đủ căn cứ. Cách xử lý này cần được xét lại nếu các đoạn sau làm rõ.
- Ghi chú p000051 và p000054 đã nêu đúng rủi ro (độ tin cậy 0,55); đề nghị thêm tên mục này vào sổ pending.

## 4. Thuật ngữ — đề xuất tạm ưu tiên

Hiện sổ pending chưa có mục nào cho b04.

| Source term | Hiện tại | Đề xuất ưu tiên | Thay thế | Tin cậy | Mã đoạn |
|---|---|---|---|---|---|
| Regadonia Entente Alliance | Liên minh Entente Regadonia | giữ | Liên minh Regadonia Entente | 0,6 | p000045 |
| Gulf War | Chiến tranh Vùng Vịnh | giữ | — | 0,8 | p000050 |
| Norden Territory | Lãnh thổ Norden | giữ; đồng bộ với "mặt trận Norden" | vùng Norden | 0,6 | p000050 |
| the brass | giới chỉ huy | "giới chỉ huy cấp cao" | cấp trên, lãnh đạo quân đội | 0,5 | p000048, p000050 |
| publicity stunt | chiêu quảng bá | "màn quảng bá" | chiêu gây chú ý | 0,5 | p000047 |
| legitimate justification | lý do chính đáng | "danh nghĩa chính đáng" (đồng bộ b03 p000043) | lý do chính đáng | 0,55 | p000048 |
| field training | huấn luyện thực địa | giữ | huấn luyện dã chiến | 0,65 | p000049 |
| military state | nhà nước quân sự | giữ | quốc gia quân phiệt (không dùng, thêm sắc thái) | 0,6 | p000049 |
| pay grade | bậc lương | giữ | ngạch lương | 0,65 | p000052 |
| commissioned | được bổ nhiệm làm sĩ quan | "nhận quân hàm sĩ quan" | giữ | 0,55 | p000052 |
| little girl mage | pháp sư bé gái | giữ | | 0,6 | p000052 |
| armored forces | lực lượng thiết giáp | giữ | | 0,7 | p000046 |
| war correspondents | phóng viên chiến trường | giữ | | 0,75 | p000046 |
| mass media | truyền thông đại chúng | giữ (đồng bộ b03) | | 0,7 | p000048 |
| honors and commendations | vinh dự và được tuyên dương | "được vinh danh và khen thưởng" | | 0,5 | p000054 |
| Being X | Being X | giữ (đồng bộ ch-00) | | 0,7 | p000049 |
| narration pronoun (Tanya) | nó / mình | giữ theo DEC-P01-001; cần đồng bộ b02–b03 | lặp tên/lược chủ ngữ | 0,55 | p000044–p000054 |

## 5. Việc cần làm sau báo cáo (đề xuất)

1. Coordinator: quyết định tạm về đại từ Tanya xuyên Chương 1 (xem mục vừa thứ ba), ghi vào sổ pending và handoff; thêm các mục thuật ngữ mục 4 và mục điểm nhìn p000051/p000054 (độ tin cậy 0,55).
2. Translator (khi nhận quyền sửa): xử lý ba mục vừa (p000044, p000051 "ái ngại", đại từ theo quyết định coordinator); các mục nhẹ tùy chọn, ưu tiên p000051 (logic "để"), p000048 ("danh nghĩa chính đáng"), p000045, p000046.
3. Translator làm mới `notes` ở các đoạn sửa để khớp bản dịch sau sửa.
4. Chạy validator và `git diff --check` sau khi sửa, trước khi commit.

## 6. Rủi ro và bất định

- Điểm nhìn p000051/p000054: bất định về người nói, độ tin cậy 0,55; không phải lỗi bản dịch.
- Đại từ "nó" so với b02–b03: cần quyết định của coordinator; không ảnh hưởng cốt truyện.
- p000044 mở đầu một phần ngắt cảnh (đoạn có lớp ngắt khoảng trắng trong nguồn); JSONL không biểu diễn ngắt cảnh, cần giữ khi dựng bản. Không phải lỗi bản dịch.
- Chưa chạy validator và diff-check; chưa tính lại hash gói nguồn; chưa mở EPUB/PDF.

```yaml
role: reviewer
task_id: vol-01-ch-01-b04-review
state: done
review_path: reviews/prose/vol-01-ch-01-b04-claude-review.md
segment_ids: [p000044, p000045, p000046, p000047, p000048, p000049, p000050, p000051, p000052, p000053, p000054]
files_written: [reviews/prose/vol-01-ch-01-b04-claude-review.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 3, minor: 9}
unresolved_findings: [p000044, p000051, "narration-pronoun-policy p000044-p000054"]
term_recommendations: [giới chỉ huy → giới chỉ huy cấp cao, legitimate justification → danh nghĩa chính đáng, commissioned → nhận quân hàm sĩ quan, honors and commendations → được vinh danh và khen thưởng, publicity stunt → màn quảng bá, Gulf War → Chiến tranh Vùng Vịnh giữ, Norden Territory → Lãnh thổ Norden giữ, Tanya narration → nó/mình giữ theo DEC-P01-001 và đồng bộ b02-b03]
risks: [điểm nhìn p000051/p000054 chưa rõ người nói (0,55), đại từ "nó" lệch quy ước b02-b03, ngắt cảnh trước p000044 không biểu diễn trong JSONL, chưa chạy validator]
commit: null
next_action: coordinator ghi quyết định đại từ và thuật ngữ vào sổ pending, giao translator sửa ba mục vừa; sau đó chạy validator và diff-check
```
