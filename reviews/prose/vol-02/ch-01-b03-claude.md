# Báo cáo phản biện — vol-02-ch-01-b03 (Claude)

- Task: `vol-02-ch-01-b03-review`
- Phạm vi: `YS-LN02/Text/part0010.xhtml/p000026` → `p000059`, tức **34 đoạn** (không phải 59: số 59 chỉ là số thứ tự đoạn cuối). Đã đối chiếu đủ 34/34; tập segment_id của bản dịch khớp hoàn toàn với source package.
- Đầu vào đã dùng: handoff b03, source package cục bộ (sha256 `a3f3f763…1b86` khớp handoff), `canon/`, `work/run-state/pending-terms.yml`, `translations/vol-02/ch-01-b03.jsonl`. Không đọc batch khác, không sửa bất kỳ tệp nào ngoài báo cáo này.
- Lưu ý đầu vào: handoff đã commit không có khối `review_coordination`/`provisional_choices`; khối này chỉ có ở bản sửa chưa commit của handoff (và trong lệnh giao việc). Tôi dùng nó như metadata do coordinator cung cấp.
- Metadata JSONL: 34/34 dòng có `source_sha256` và `glossary_version` đúng, `status: draft`.

## Tóm tắt

Bản dịch nhìn chung chính xác về nghĩa, phủ định, chủ thể và trình tự thời gian; giọng nội tâm ("mình") và thoại nhất quán. **Không có lỗi nghiêm trọng.** Có **3 lỗi vừa** (cấp bậc ở p000052 và p000058; đại từ trần thuật "nó" lệch sổ pending ở p000054, p000056) và một số lỗi nhẹ. Nên sửa các lỗi vừa trước khi commit.

## Nhấn mạnh (emphasis parity)

Nguồn có đúng **2** chỗ nhấn mạnh (thẻ `<em>`), bản dịch có đúng 2 cặp `*...*`:

| segment_id | Nguồn | Bản dịch | Kết luận |
|---|---|---|---|
| p000054 | một từ đơn (nhấn vào vị ngữ "trơn tru") | `*trơn tru*` | Khớp phạm vi |
| p000056 | cả cụm lời tuyên bố của Tanya gửi đại tá | `*Cứ giao cho tôi.*` | Khớp phạm vi; dấu chấm nằm trong cặp `*` vì là lời thoại tưởng tượng, chấp nhận được |

32 đoạn còn lại không có nhấn mạnh ở nguồn và không có dấu `*` thừa trong bản dịch. Đạt DEC-P01-002. Việc để nguyên "conquistador" không có `*` là đúng (nguồn không in nghiêng).

## Phát hiện

### Nghiêm trọng
Không có.

### Vừa

**M1 — p000052 — cấp bậc/chủ thể.** Tanya gọi sĩ quan phụ tá là "Trung úy", trong khi đoạn ngay trước (p000051) tự xưng "Thiếu úy Serebryakov". Trong cùng đoạn hội thoại, người đọc sẽ hiểu là hai người hoặc có thăng cấp ngầm. Cách gọi rút gọn "Lieutenant" ở nguồn là gọi tắt cấp của chính Serebryakov.
→ Sửa: "Thiếu úy" (có thể thêm "Này"/"Thiếu úy Serebryakov" nếu cần rõ). Căn cứ: p000051; sổ `vol02-ch01-b02-lieutenant` (phương án thay thế Thiếu úy) và nguyên tắc không tự nâng cấp bậc.

**M2 — p000058 — thuật ngữ cấp bậc.** "Trung úy nhất" là dạng mới, không có trong sổ pending và không phải cấp bậc tiếng Việt thông dụng. Cùng nhân vật Weiss ở p000053 là "Trung úy Weiss"; sổ `b06-first-lieutenant` đề xuất "trung úy" cho First Lieutenant. Hiện cùng một người bị hai cách gọi.
→ Sửa: "Trung úy Weiss" (khớp p000053 và sổ vol-01). Nếu sau này canon chọn cách phân biệt Lieutenant/First Lieutenant thì đồng bộ lại cả p000052, p000053, p000058; hiện chưa đủ căn cứ để phân biệt.

**M3 — p000054, p000056 — đại từ trần thuật về Tanya.** Bản dịch dùng "nó" (p000054 một lần, p000056 hai lần), còn p000054 còn lẫn "hai má mình" ngay cạnh "nó" trong cùng câu. Sổ `vol02-ch01-b01-tanya-narration` (provisional, 0.6) đề xuất lặp tên Tanya hoặc lược chủ ngữ; DEC-P01-001 cũng chỉ duyệt "nó" cho giai đoạn LN01 ch001 và cấm tự mở rộng sang giai đoạn khác. Chọn "nó" ở LN02 là mở rộng quy ước ngoài phạm vi và có thể không nhất quán với b01–b02.
→ Sửa: p000054 "Tanya thậm chí còn cảm thấy hai má giãn ra… nhưng cố ép chúng giữ căng"; p000056 "…Tanya hài lòng gật đầu rồi nện nắm tay bé xíu vào ngực…". Nếu coordinator có quyết định giữ "nó" cho LN02 thì áp dụng đồng loạt và ghi vào ledger. (Tôi không đọc b01/b02 nên không xác nhận được chúng dùng gì.)

### Nhẹ

| # | segment_id | Vấn đề và căn cứ | Đề xuất |
|---|---|---|---|
| m1 | p000041 | "tàn sát giả dạng" đảo chiều: nguồn là việc **trông giống** tàn sát nhưng thực chất chỉ là diễn tập; bản dịch đọc như tàn sát thật đội lốt diễn tập. | "một màn gần như tàn sát, chỉ có thể gọi là diễn tập bắn đạn thật" |
| m2 | p000038 | "lính bộ binh chân đất" thêm sắc thái nghèo/lạc hậu (đi chân đất) không có ở nguồn (chỉ là bộ binh đi bộ thông thường); còn thừa lặp "lính bộ binh". | "toàn bộ binh đi bộ thuần túy" |
| m3 | p000056 | "ông ta" (ở câu đánh giá quá cao) mang sắc thái xa cách/miệt thị, vi phạm quy tắc không thêm phán xét; sổ `vol02-ch01-b01-lergen-reference` đề xuất lặp tên hoặc lược chủ ngữ. Cách gọi "ông" ở câu sau cũng suy ra tuổi/vai vế. | "Đại tá" / "Đại tá von Lergen", hoặc lược chủ ngữ |
| m4 | p000035, p000041 | "Quân conquistador" biến một danh từ chung số nhiều thành "quân", thêm hàm ý đội quân có tổ chức. | p000041: "Các conquistador có ngựa và súng…" (xem khuyến nghị thuật ngữ) |
| m5 | p000031 | "Chỉ vậy thôi cũng đủ…" thu hẹp tham chiếu của "That" (cả bối cảnh vừa nêu) thành "chỉ riêng việc đó"; "giáng… xuống đầu" thêm chi tiết hướng. | "Điều đó cũng cho ngài thấy…"; "giáng chiếc búa sắt của văn minh xuống bọn man rợ này" |
| m6 | p000029 | "cũng tiện thể xếp thành hàng" mất tính mỉa mai "tử tế đến mức chịu xếp hàng sẵn"; "tiện thể" nghe như việc phụ. | "lại còn tử tế xếp hàng cho ta dễ ngắm bắn" |
| m7 | p000049 | Cấu trúc "đang… thì… khi…" ba liên từ chồng nhau, lủng củng; "đang" làm đổi thể. | "Mình nghĩ ngợi như vậy, nhưng mọi ý nghĩ tan biến khi sĩ quan phụ tá chạy lon ton tới." |
| m8 | p000057 | "quân trang huấn luyện" = quân phục, lệch khỏi "trang bị dùng khi huấn luyện"; "vừa được phát" thêm mốc thời gian. | "trang bị huấn luyện cùng số đạn thật đã phát" |
| m9 | p000036, p000045, p000051 | Lời gọi "Cô" (đại tá → Tanya; sĩ quan phụ tá → Tanya) suy ra quan hệ/tuổi, trái giới hạn của DEC-P01-001 ("cách gọi trong thoại phải xét riêng"). Sổ b01 chỉ liệt "cô" là phương án thay thế, chưa chốt. | Phương án trung tính: lặp cấp bậc ("Thiếu tá biết là…", "Thiếu tá gọi tôi ạ?"). Tạm chấp nhận hiện trạng nếu b01–b02 đã dùng "cô" nhất quán |
| m10 | p000046 | "bài học giáo dục" mất yếu tố "chỉ dẫn/kèm cặp" của lối nói ẩn dụ; vẫn đọc được. | "một buổi chỉ dạy mang tính giáo dục" |
| m11 | p000048 | "bầu trời Dacia ôn hòa ở phía đông nam" gắn "ôn hòa" vào bầu trời thay vì vùng đông nam. | "bầu trời Dacia ở vùng đông nam ôn hòa" |
| m12 | p000058 | "Chỉ thị từ chỉ huy!" bỏ "our"; lời hô trước đội hình nên giữ tính sở hữu. | "Chỉ thị từ chỉ huy của chúng ta!" hoặc "Chỉ huy ra chỉ thị!" |

### Kiểm tra đã đạt (không có lỗi)
- **Phủ định và logic:** p000028 (không), p000040, p000041, p000055 (không ai… cùng chia sẻ), p000039 giữ đúng.
- **Thời gian giả định/chronology:** p000026 (điều kiện "đã được giao"), p000029 (giả định phản thực "nếu đó là… sẽ…"), p000044 (khả năng "nếu… vô tình… thì có thể…"), p000048 ("vẫn còn là tháng Chín"), p000057 (trình tự tập hợp → phát đạn) đều giữ đúng.
- **Chủ thể:** chuyển điểm nhìn p000054 (ngôi ba) → p000055 (ngôi nhất) → p000056 được giữ; người nói trong các thoại p000027–p000046 khớp ngữ cảnh (Tanya ↔ đại tá).
- **Số liệu:** sáu trăm nghìn (p000029, p000056), ba sư đoàn (p000036, p000037, p000041), bốn mươi lăm độ (p000058).

## Khuyến nghị thuật ngữ (tạm thời, không canon)

### 1. Dacian
- Khuyến nghị: **"quân Dacia"** khi chỉ lực lượng vũ trang (p000027, p000037, p000056); **"Dacia"** khi chỉ quốc gia/lãnh thổ (p000046, p000048). "người Dacia" chưa cần ở batch này; giữ làm phương án khi chỉ dân thường.
- Lý do: p000027 và p000037 nói về lực lượng vượt biên/mũi tiến công; p000056 là con số quân (sáu trăm nghìn), trùng với cùng con số "troops" ở p000029, nên nhất quán với "quân".
- Thay thế: "phía Dacia" (trung tính hơn nếu muốn tránh phân biệt), "lính Dacia" cho p000056.
- Độ bất định: ~0.6. Không ảnh hưởng cốt truyện.
- Sửa ledger: p000029 và p000048 trong mục `vol02-ch01-b03-dacian` không chứa "Dacian" (p000029 nói về Federal/Republican; p000048 chỉ có tên nước). Mã đoạn đúng cho "Dacian": **p000027, p000037, p000056**; tên nước "Dacia": p000046, p000048.

### 2. Federal / Republican forces
- Khuyến nghị: **"quân Liên bang hoặc quân Cộng hòa"** (p000029); bản dịch hiện "quân Liên bang hoặc Cộng hòa" dùng được, thêm "quân" lần hai là phương án an toàn hơn về cú pháp.
- Lý do: hai tính từ tương ứng với `b03-federation` → Liên bang và `b03-republic` → Cộng hòa của vol-01 (p000034 chương 003b); ngữ cảnh chỉ nêu họ như các đối thủ có không quân, nên không cần thêm nhãn nào khác.
- Thay thế: "lực lượng Liên bang/Cộng hòa" (nhấn tính tổ chức); "quân đội Liên bang/Cộng hòa".
- Độ bất định: ~0.55–0.6; chưa chắc "Republican" chỉ cùng một chính thể với `b03-republic` hay chỉ là tính từ chung. Không nâng thành canon.
- Mã đoạn: **p000029**.

### 3. Conquistador
- Khuyến nghị: **giữ mượn từ "conquistador"** (viết thường, không in nghiêng vì nguồn không in nghiêng), số nhiều dùng "các conquistador" thay cho "quân conquistador".
- Lý do: ngữ cảnh p000035 là nói về "kiểu đánh" gắn với lịch sử; p000041 nêu ngựa và súng, nên chỉ cần đủ để nhận ra ám chỉ lịch sử. Thêm "Tây Ban Nha" hoặc tên chiến dịch là bổ sung không có căn cứ trong đoạn. "Kẻ chinh phục" dễ trùng với "chinh phục bầu trời" ở p000032 (cố ý hay không chưa rõ) và mất nghĩa riêng của từ.
- Thay thế: "kẻ chinh phục" (nếu muốn thuần Việt), "nhà chinh phục Tây Ban Nha" (không khuyến nghị; thêm quốc tịch).
- Độ bất định: ~0.6. Không ảnh hưởng cốt truyện.
- Mã đoạn: **p000035, p000041**.

### 4. Thuật ngữ mới cần ghi vào sổ pending
- Sĩ quan phụ tá (adjutant), p000049, p000056, p000057: hiện dùng nhất quán trong batch; chưa có trong sổ. Ghi nhận là đề xuất, độ chắc ~0.55; thay thế: "trợ tá", "sĩ quan tùy tùng".
- Thiếu úy / Trung úy (Second Lieutenant / Lieutenant / First Lieutenant): xem M1, M2; cần ghi cặp ánh xạ vào `vol02-ch01-b02-lieutenant`.

## Rủi ro
- Hệ cấp bậc (Thiếu úy/Trung úy) và đại từ trần thuật Tanya là hai điểm dễ lệch xuyên batch; cần coordinator đối chiếu với b01–b02 (đã ngoài phạm vi đọc của tôi).
- "Cô" trong thoại chưa được canon; nếu sau này đổi cần sửa đồng loạt.
- Handoff đã commit thiếu khối `review_coordination`; coordinator nên commit cùng handoff cập nhật để task có đủ căn cứ.

## Kết luận
Cần người giữ quyền sửa áp dụng M1–M3 (và nên sửa m1–m3); sau đó có thể kiểm tra lại nhanh p000052, p000054, p000056, p000058 rồi chạy validator.

```yaml
role: reviewer
task_id: vol-02-ch-01-b03-review
state: done
segment_ids: [p000026..p000059 của YS-LN02/Text/part0010.xhtml, 34 đoạn]
files_written:
  - reviews/prose/vol-02/ch-01-b03-claude.md
validator: not_run
diff_check: not_run
review_path: reviews/prose/vol-02/ch-01-b03-claude.md
counts: {serious: 0, moderate: 3, minor: 12}
findings:
  - {severity: moderate, segment_id: YS-LN02/Text/part0010.xhtml/p000052, issue: gọi Thiếu úy Serebryakov là Trung úy, lệch p000051, resolution: sửa thành Thiếu úy}
  - {severity: moderate, segment_id: YS-LN02/Text/part0010.xhtml/p000058, issue: "Trung úy nhất" là cấp bậc mới, lệch p000053 và sổ pending, resolution: dùng Trung úy Weiss}
  - {severity: moderate, segment_id: "YS-LN02/Text/part0010.xhtml/p000054, YS-LN02/Text/part0010.xhtml/p000056", issue: dùng "nó" cho Tanya trái sổ vol02 (lặp tên/lược chủ ngữ) và lẫn "mình" cùng câu, resolution: lặp tên Tanya hoặc lược chủ ngữ, hoặc coordinator chốt "nó" cho LN02}
  - {severity: minor, segment_id: YS-LN02/Text/part0010.xhtml/p000041, issue: "tàn sát giả dạng" đảo chiều nghĩa, resolution: gần như tàn sát / diễn tập}
  - {severity: minor, segment_id: YS-LN02/Text/part0010.xhtml/p000038, issue: "chân đất" thêm sắc thái, resolution: bỏ}
  - {severity: minor, segment_id: YS-LN02/Text/part0010.xhtml/p000056, issue: "ông ta" thêm sắc thái xa cách, resolution: lặp Đại tá/lược chủ ngữ}
  - {severity: minor, segment_id: "YS-LN02/Text/part0010.xhtml/p000035, YS-LN02/Text/part0010.xhtml/p000041", issue: "Quân conquistador" thêm hàm ý đội quân, resolution: "các conquistador"}
  - {severity: minor, segment_id: "p000029, p000031, p000046, p000048, p000049, p000057, p000058", issue: các điểm văn phong/độ sát nhỏ, resolution: xem bảng m5–m12 trong báo cáo}
  - {severity: minor, segment_id: "p000036, p000045, p000051", issue: lời gọi "Cô" chưa canon, resolution: lặp cấp bậc nếu muốn trung tính}
pending_terms:
  - {source_term: Dacian, proposed_vi: "quân Dacia (lực lượng) / Dacia (quốc gia)", segment_ids: [p000027, p000037, p000056], volume: vol-02, chapter: 1, status: pending}
  - {source_term: Federal / Republican forces, proposed_vi: "quân Liên bang / quân Cộng hòa", segment_ids: [p000029], volume: vol-02, chapter: 1, status: pending}
  - {source_term: conquistador, proposed_vi: "giữ mượn từ conquistador; số nhiều: các conquistador", segment_ids: [p000035, p000041], volume: vol-02, chapter: 1, status: pending}
  - {source_term: adjutant, proposed_vi: sĩ quan phụ tá, segment_ids: [p000049, p000056, p000057], volume: vol-02, chapter: 1, status: pending}
  - {source_term: "Second Lieutenant / Lieutenant / First Lieutenant (Serebryakov, Weiss)", proposed_vi: "Thiếu úy / theo người được gọi / Trung úy", segment_ids: [p000051, p000052, p000053, p000058], volume: vol-02, chapter: 1, status: pending}
unresolved_findings: 15  # 3 vừa + 12 nhẹ, chờ người giữ quyền sửa
term_recommendations: xem mục "Khuyến nghị thuật ngữ"
risks:
  - cấp bậc và đại từ Tanya có thể lệch xuyên batch (chưa đối chiếu b01–b02 do giới hạn phạm vi)
  - lời gọi "Cô" chưa canon
  - handoff đã commit thiếu review_coordination
  - lệnh giao nêu 59 đoạn, thực tế batch có 34 đoạn (p000026–p000059)
commit: null
next_action: translator áp dụng M1–M3 (và nên sửa m1–m3), sau đó recheck p000052/p000054/p000056/p000058 và chạy validator
```
