# Báo cáo review vol-01-ch-01-b08 (Claude, reviewer)

- Task: `vol-01-ch-01-b08`; 15 đoạn `YS-LN01/Text/chapter003b.xhtml/p000129`–`p000143`. Dưới đây viết tắt mã đoạn là `pNNNNNN`.
- Đầu vào đã đọc: source package cục bộ (sha256 khớp `source_package_sha256` trong handoff: 03851ec2…fd12e), `translations/vol-01/ch-01-b08.jsonl`, `handoffs/vol-01/ch-01-b08.yml`, canon (glossary và characters còn rỗng; `decisions.md` có DEC-P01-001/002; style-guide), `canon/glossary-pending.yml`, `work/run-state/pending-terms.yml` (mục b08-* và các mục b01–b07 liên quan), bản dịch b01–b07 để đối chiếu nhất quán.
- Đối chiếu cấu trúc: đủ 15/15 đoạn, đúng thứ tự, `source_sha256` mỗi dòng khớp handoff, không đoạn thiếu/thừa/gộp. Gói nguồn không có thẻ nhấn mạnh (`em`, `i`, `span`, `sup`) ở đoạn nào; bản dịch không có `*…*` nào → đúng DEC-P01-002.
- Không dùng EPUB/PDF, không đọc `footnote.xhtml` (ngoài phạm vi).

## Kết luận

Không có lỗi nghiêm trọng. Bản dịch bám nghĩa, chronology, phủ định và giọng nội tâm khá tốt. Có **7 lỗi vừa** (chủ yếu thuật ngữ quân sự và nhất quán liên lô: p129/p136/p139/p143, p130 ×2, p132, p133, p136, p137) và **13 lỗi nhẹ**. Cả 5 thuật ngữ translator đề xuất (mục `b08-*`) đều cần chỉnh hoặc đối chiếu; xem mục 2.

## 1. Phát hiện

### Vừa

**M1 — p129, p136, p139, p143: "Đài kiểm soát Norden" lệch với 5 lô trước (b01, b05 dùng nguyên "Norden Control").**
- Vấn đề: b01–b05 giữ nguyên "Norden Control" trong cả trần thuật lẫn thoại vô tuyến (≥ 20 lần). Lô này đổi sang "Đài kiểm soát Norden" ở 4 đoạn. Cùng một đơn vị có hai tên trong cùng chương.
- Căn cứ: ledger `P01-norden-control` (đề xuất "Norden Control", phương án khác "Đài kiểm soát Norden") và `b05-norden-control` (đề xuất "Norden Control"); lô này không có chứng cứ mới để đổi.
- Đề xuất: dùng "Norden Control" ở cả 4 đoạn (không dịch tên/hô hiệu trong thoại vô tuyến). Nếu coordinator muốn đổi tên thì phải đổi đồng loạt cả chương. Độ tin cậy: 0.8.

**M2 — p130: "khai hỏa trên không" sai nghĩa "air burst".**
- Vấn đề: "air burst" là kiểu nổ của đạn (đạn nổ trên không trung), không phải việc pháo binh khai hỏa "trên không". Bản dịch biến thành hành động bắn của pháo binh và làm mất ý đạn nổ trên cao.
- Căn cứ: ledger `b08-air-burst` đề xuất "đạn nổ trên không" nhưng câu dịch không dùng; p142 sau đó mô tả đạn rơi và nổ.
- Đề xuất: "…quan sát pháo binh Đế quốc dùng đạn nổ trên không và các loạt bắn …". Phương án khác: "bắn nổ trên không", "đạn nổ cao". Độ tin cậy: 0.75.

**M3 — p130: "bắn đồng thời theo thời gian mục tiêu" là dịch từng chữ, khó hiểu.**
- Vấn đề: "time on target" là kỹ thuật bắn nhiều khẩu/đơn vị sao cho đạn cùng rơi trúng mục tiêu một lúc. Cụm "theo thời gian mục tiêu" không có nghĩa trong tiếng Việt; cụm "thực hiện các loạt bắn đồng thời" cũng nghiêng về "bắn cùng lúc" (thời điểm khai hỏa) thay vì "cùng rơi".
- Căn cứ: nghĩa kỹ thuật của thuật ngữ; không có mục canon. Nghĩa này không ảnh hưởng cốt truyện.
- Đề xuất tạm (ít suy diễn nhất): "các loạt bắn cho đạn cùng rơi trúng mục tiêu một lúc" (không chèn chú thích làm việc vào bản dịch). Phương án khác: "bắn đồng loạt theo thời điểm đạn rơi", "bắn TOT". Độ tin cậy: 0.55.

**M4 — p132: đại từ "tôi" trong nội tâm vi phạm DEC-P01-001.**
- Vấn đề: p132 là độc thoại nội tâm của Tanya (cùng mạch với p133, p134 đang dùng "mình"). Câu cuối p132 dùng "tôi"; DEC-P01-001 quy định nội tâm tự quy chiếu dùng "mình".
- Căn cứ: DEC-P01-001 (đã duyệt); cách dùng "mình" ở p130, p133–p135, p138, p141, p142.
- Đề xuất: "Nếu mình báo cho …". Độ tin cậy: 0.85.

**M5 — p133: "Lễ duyệt binh hỏa lực Fuji" sai loại sự kiện và lệch b05.**
- Vấn đề: b05 (p000056) đã dịch cùng sự kiện là "buổi trình diễn hỏa lực Fuji" (có chú thích ⁵). Lô này đổi sang "Lễ duyệt binh", là parade (diễu hành), khác hẳn buổi diễn tập bắn. "Nhỏ bé" cũng bỏ sắc thái "dễ thương/trẻ con" của nguồn (xem m5).
- Căn cứ: ledger `b05-fuji-firepower-review` (đề xuất "buổi trình diễn hỏa lực Fuji", phương án khác "cuộc thao diễn hỏa lực Fuji").
- Đề xuất: "buổi trình diễn hỏa lực Fuji" (hoặc "cuộc thao diễn hỏa lực Fuji" nếu b05 đổi). Độ tin cậy: 0.8.

**M6 — p136: "bắn hiệu chỉnh theo quan sát" trùng thuật ngữ với "calibration fire" và gây lệch logic với p137.**
- Vấn đề: b02 (p000012) dùng "bắn hiệu chỉnh" cho "calibration fire". Ở đây "observed fire" (bắn có quan sát viên) cũng dịch "bắn hiệu chỉnh", rồi p137 báo "không cần chỉnh làn bắn", dễ đọc như hai bước mâu thuẫn ("hiệu chỉnh" rồi "không cần chỉnh").
- Đề xuất: "Pháo binh bắt đầu bắn có quan sát." (phương án khác: "bắn theo quan sát"). Tránh dùng "hiệu chỉnh" cho "observed". Độ tin cậy: 0.6.

**M7 — p137: "Bắt đầu bắn tiêu diệt mục tiêu" lệch ledger và thêm kết quả không có trong nguồn.**
- Vấn đề: "fire for effect" đã có đề xuất "bắn hiệu lực" (b05, b02). "Bắn tiêu diệt" khẳng định mục đích/kết quả (tiêu diệt) mà lệnh chỉ nêu giai đoạn bắn.
- Căn cứ: sổ pending (`fire for effect / good effect → bắn hiệu lực`); b05 báo cáo Claude yêu cầu thống nhất.
- Đề xuất: "Bắt đầu bắn hiệu lực." Độ tin cậy: 0.8.

### Nhẹ

**m1 — p129: "binh chủng pháo binh" không áp dụng; "nhân viên" trơ.** Bản dịch dùng "pháo binh" còn ledger ghi "binh chủng pháo binh" (lệch ledger, không lệch nghĩa). "Một nhân viên ở … đưa ra các mệnh lệnh" cho "operator" (người vận hành/trực máy) hơi chung chung. Đề xuất: giữ "kíp pháo binh", sửa ledger; "nhân viên điều hành" hoặc "điều hành viên". 0.4.

**m2 — p130: quan hệ "không chỉ tin… mà còn tuân theo" bị mờ.** "đã vượt qua niềm tin vào ưu thế hỏa lực để xem việc tuân theo ưu thế ấy như học thuyết" — "tuân theo ưu thế" gượng và "vượt qua niềm tin" nghe như từ bỏ niềm tin. Nguồn: họ đã đi xa hơn việc tin, và coi tuân theo nó là học thuyết hiển nhiên. Đề xuất: "…không chỉ tin vào ưu thế hỏa lực mà còn coi việc tuân theo nó là học thuyết được thừa nhận." 0.6.

**m3 — p131: "mà nguồn lực cũng vậy" và "còn là" làm mờ quan hệ.** "Nhưng neither do resources" tức nguồn lực cũng không nói dối; "mà … cũng vậy" dễ đọc thành khẳng định khác. "As well" ở câu sau là "đối với Tanya cũng vậy" (cùng quan điểm với Đế quốc); "còn là" nghiêng sang tăng tiến. Đề xuất: "…nhưng nguồn lực cũng không" / "Với một người như Tanya cũng vậy, đó là những vị thần tuyệt đối hơn hẳn …". 0.5. Ghi chú: "Thượng đế tối cao" nhất quán với b06 (p000077); không ảnh hưởng thuật ngữ b07 "Chúa" (nhân vật khác).

**m4 — p132: thêm "của đối phương"; "air supremacy" dịch như "air superiority".** "Chống pháp sư không quân của đối phương" thêm chủ thể không có trong nguồn (nguồn ngắn gọn, mơ hồ giữa "pháp sư phòng không" và "chống pháp sư trên không"). "Ưu thế trên không" cho "supremacy" yếu hơn; ledger b05 dùng "kiểm soát không phận"/"ưu thế" cho thuật ngữ gần. Đề xuất: bỏ "của đối phương"; "duy trì quyền kiểm soát trên không" hoặc giữ "ưu thế trên không" và ghi mức độ chưa chắc. Độ bất định: 0.45.

**m5 — p133: "nhỏ bé" bỏ sắc thái "cute".** Nguồn dùng từ đáng yêu/trẻ con (mỉa mai Fuji là "dễ thương" so với cảnh này). Đề xuất: "trông như trò trẻ con" hoặc "trông thật dễ thương". 0.5.

**m6 — p134: "Bọn pháp sư", "Xin chúc mừng… dàn dựng".** "Bọn" thêm sắc thái xem thường mà "us mages" không có (cần cân với giọng mỉa của Tanya). "Cheers to" là nâng cốc/tán thưởng, "chúc mừng" ổn nhưng "dàn dựng" gợi dàn cảnh. "Đột kích sâu" cho "deep penetration" có thể thành "thọc sâu". Đề xuất: "Các pháp sư chúng ta…"; "Xin nâng cốc mừng Bộ Tổng Tham mưu đã sắp xếp mọi chuyện tuyệt vời đến thế"; "thọc sâu". 0.45.

**m7 — p135: "Đại tướng Lee" gắn cấp bậc; "ngày càng mê đắm" đổi "too fond".** Cấp bậc "General" ở đây là danh xưng người nổi tiếng; "Đại tướng" áp một bậc cụ thể (AGENTS.md: không tự chốt cấp bậc). "Quá yêu thích" (too fond) bị đổi thành quá trình ("ngày càng"). Đề xuất: "Tướng Lee"; "…nếu không chúng ta sẽ quá yêu thích nó." 0.55.

**m8 — p137: "chỉnh làn bắn" dùng "làn".** "Adjust fire" là hiệu chỉnh việc bắn; "làn" gợi làn đạn. Đề xuất: "chỉnh bắn"/"hiệu chỉnh bắn" (thống nhất với M6). 0.4.

**m9 — p138: "cấp quân đoàn dã chiến" chưa chắc.** Ledger `b08-field-corps-integration`. "Field corps" có thể chỉ quân đoàn dã chiến hoặc quân đoàn ngoài mặt trận (khác "Quân đoàn Lâm thời" của b01–b05). Không đủ căn cứ để kết luận; giữ literal "pháo binh được tích hợp ở cấp quân đoàn dã chiến" là chấp nhận được; phương án khác: "pháo binh phối thuộc cấp quân đoàn". 0.45.

**m10 — p139, p140: "đã rõ" khác "rõ" của b01/b05; "Over"/"Out" cùng "Hết".** b01 p003, p006 và b05 dùng "rõ" cho "roger"; lô này dùng "đã rõ". Ledger `b05-radio-over` đã đề xuất "Hết" cho "Over" nhưng b01 p006 cũng dùng "Hết" cho "Out", nên p139 "Over" và p140 "Out" không phân biệt. Đề xuất: đổi "đã rõ" → "rõ"; giữ "Hết" cho "Over" (đã có tiền lệ), cân nhắc "Kết thúc" cho "Out" (p140) và sửa b01 p006 nếu đồng ý. 0.4. Ngoài ra, hai đoạn này theo mẫu "tên, rõ" như b01 nên có thể bị đọc ngược người nói (nội dung p139 là của phía pháo/đài, p140 của Fairy 08); nguồn mơ hồ, giữ literal, không thêm nhãn người nói. Độ bất định: 0.5.

**m11 — p141: "thảm họa", "chỉ có thể".** "Outrageous" là "quá vô lý/không thể chấp nhận", không phải thảm họa; "chỉ có thể đứng nhìn" thêm tính bất lực. Đề xuất: "thì thật vô lý" / "còn mình thì nhìn mà ghen tị". 0.4.

**m12 — p142: "xa xa mình thấy".** "As far as I can see" là phạm vi tầm nhìn (khắp tầm mắt), không phải "ở xa". Đề xuất: "Từ vị trí trên không, trong tầm mắt mình thấy…" / "khắp tầm mắt". 0.5. (Chronology "ngay khi quầng lửa tan" đúng.)

**m13 — p143: "Xin nhắc lại" và "trúng mục tiêu".** "Repeat" trong thoại vô tuyến pháo binh có thể là "lặp lại việc bắn/lệnh", không nhất thiết "nhắc lại thông tin" (khác "I say again" ở p137). "Impact confirmed" chỉ "đã xác nhận điểm đạn rơi", không nêu "trúng mục tiêu". Chứng cứ chưa đủ; đề xuất trung tính: "Đã xác nhận điểm đạn rơi của nhiệm vụ hỏa lực. Lặp lại." Độ bất định: 0.45.

### Không có vấn đề (đã đối chiếu)
- p129 (các phần còn lại), p131, p134 (trình tự pháo → bộ binh/xe bọc thép), p138 (đoạn còn lại): giữ nghĩa, giọng và chronology.
- p135: lời xin lỗi "bất kính" và khẳng định thích chiến tranh giữ nguyên, không phủ định sai.
- p141, p142: chuyển động (bay về phía tây, lên cao) và chronology (nổ → mảnh thân thể bay) đúng.
- Nhấn mạnh: không có nhấn mạnh trong nguồn lô này; bản dịch không thêm → đúng DEC-P01-002.

## 2. Khuyến nghị thuật ngữ (chỉ là đề xuất, không phải quyết định canon)

| Mục ledger | Hiện tại | Khuyến nghị | Độ tin cậy | Ghi chú |
|---|---|---|---|---|
| b08-norden-control (p129, p136, p139, p143) | Đài kiểm soát Norden | Đổi về "Norden Control" (nhất quán b01–b05; ledger P01-norden-control, b05-norden-control). Phương án khác: "Đài kiểm soát Norden" (nếu đổi đồng loạt toàn chương). | 0.8 | Không ảnh hưởng cốt truyện. |
| b08-air-burst (p130) | đạn nổ trên không (ledger) / "khai hỏa trên không" (câu dịch) | Giữ ledger; sửa câu dịch theo M2. Phương án khác: "bắn nổ trên không", "đạn nổ cao". | 0.75 | Câu dịch phải khớp ledger. |
| b08-time-on-target (p130) | bắn đồng thời theo thời gian mục tiêu | Đổi sang "bắn cho đạn cùng rơi trúng mục tiêu một lúc". Phương án khác: "bắn TOT", "bắn đồng loạt theo thời điểm đạn rơi". | 0.55 | Thiếu căn cứ để chốt thuật ngữ cố định; chọn diễn giải gần nghĩa kỹ thuật nhất, ít suy diễn nhất. |
| b08-artillery-arm (p129) | binh chủng pháo binh (ledger) / "pháo binh" (câu dịch) | Giữ "pháo binh" trong câu dịch; sửa ledger cho khớp. Phương án khác: "binh chủng pháo binh". | 0.6 | Câu dịch tự nhiên hơn, nghĩa không đổi. |
| b08-field-corps-integration (p138) | pháo binh được tích hợp ở cấp quân đoàn dã chiến | Giữ tạm; phương án khác "pháo binh phối thuộc cấp quân đoàn". | 0.45 | Chưa rõ "field corps" là tên đơn vị hay loại hình; bất định cao, cần đối chiếu các lô sau. |
| (đề xuất thêm) fire for effect (p137) | bắn tiêu diệt mục tiêu | "bắn hiệu lực" (theo ledger b05/b02). | 0.8 | Thống nhất liên lô. |
| (đề xuất thêm) observed fire (p136) | bắn hiệu chỉnh theo quan sát | "bắn có quan sát"; không dùng "hiệu chỉnh" (đã dành cho calibration fire, b02). | 0.6 | Phương án khác: "bắn theo quan sát". |
| (đề xuất thêm) Fuji Firepower Review (p133) | Lễ duyệt binh hỏa lực Fuji | "buổi trình diễn hỏa lực Fuji" (b05). | 0.8 | Phương án khác: "cuộc thao diễn hỏa lực Fuji". |
| (đề xuất thêm) radio Over/Out (p139, p140) | Hết / Hết | "Over → Hết" giữ; "Out" cân nhắc "Kết thúc"; "roger → rõ". | 0.4 | Cần chốt cho cả chương; chưa đủ căn cứ để tách. |
| (đề xuất thêm) General Lee (p135) | Đại tướng Lee | "Tướng Lee". | 0.55 | Tránh gán cấp bậc. |
| gods of war (p131, p132) | thần chiến tranh | Giữ tạm, nhất quán; thêm vào ledger nếu muốn theo dõi. | 0.6 | Không có chứng cứ thay đổi. |
| mixed fighter-bomber squadron (p134) | phi đội hỗn hợp tiêm kích-ném bom | Giữ tạm; phương án khác "phi đội hỗn hợp tiêm kích - cường kích". | 0.4 | Bất định về loại máy bay/chức năng. |

Không có mục nào cần hỏi người dùng theo hướng ảnh hưởng cốt truyện. Theo AGENTS.md, các lựa chọn trên là phương án tạm để coordinator ghi vào ledger và handoff, không tự nâng thành canon.

## 3. Rủi ro còn lại

1. Nhất quán liên lô của hộ hiệu Norden Control (M1) và thuật ngữ vô tuyến (m10); cần đồng bộ cả chương.
2. Thuật ngữ pháo binh (air burst, TOT, observed fire, fire for effect) chưa có canon; nên chốt một bảng tạm cho chương 1.
3. "Field corps" và "mixed fighter-bomber squadron" thiếu căn cứ (m9, bảng 2).
4. Xưng hô/nội tâm: "mình" (nội tâm) và "ta/chúng ta" (trần thuật hướng về phe mình) hiện nhất quán trừ p132 (M4).

## 4. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-01-ch-01-b08
state: done
segment_ids: [p000129..p000143, 15 đoạn theo handoff]
files_written:
  - reviews/prose/vol-01-ch-01-b08-claude.md
review_path: reviews/prose/vol-01-ch-01-b08-claude.md
validator: not_run
diff_check: not_run
counts:
  serious: 0
  moderate: 7
  minor: 13
findings:
  - {severity: moderate, segment_id: p000129/p000136/p000139/p000143, issue: 'Đài kiểm soát Norden lệch Norden Control của b01-b05', resolution: 'dùng Norden Control'}
  - {severity: moderate, segment_id: p000130, issue: 'khai hỏa trên không sai nghĩa air burst', resolution: 'dùng đạn nổ trên không'}
  - {severity: moderate, segment_id: p000130, issue: 'time on target dịch từng chữ', resolution: 'bắn cho đạn cùng rơi trúng mục tiêu một lúc'}
  - {severity: moderate, segment_id: p000132, issue: 'tôi trong nội tâm vi phạm DEC-P01-001', resolution: 'dùng mình'}
  - {severity: moderate, segment_id: p000133, issue: 'Lễ duyệt binh sai loại sự kiện và lệch b05', resolution: 'buổi trình diễn hỏa lực Fuji'}
  - {severity: moderate, segment_id: p000136, issue: 'observed fire trùng thuật ngữ calibration fire', resolution: 'bắn có quan sát'}
  - {severity: moderate, segment_id: p000137, issue: 'bắn tiêu diệt mục tiêu lệch ledger bắn hiệu lực', resolution: 'bắn hiệu lực'}
unresolved_findings:
  - {severity: moderate, segment_ids: [p000129, p000136, p000139, p000143], issue: 'M1 Norden Control'}
  - {severity: moderate, segment_id: p000130, issue: 'M2 air burst'}
  - {severity: moderate, segment_id: p000130, issue: 'M3 time on target'}
  - {severity: moderate, segment_id: p000132, issue: 'M4 đại từ tôi'}
  - {severity: moderate, segment_id: p000133, issue: 'M5 Fuji'}
  - {severity: moderate, segment_id: p000136, issue: 'M6 observed fire'}
  - {severity: moderate, segment_id: p000137, issue: 'M7 fire for effect'}
  - {severity: minor, segment_ids: [p000129, p000130, p000131, p000132, p000133, p000134, p000135, p000137, p000138, p000139, p000140, p000141, p000142, p000143], issue: 'm1-m13 như mục 1'}
term_recommendations:
  - {id: b08-norden-control, keep_provisional: true, proposed_vi: 'Norden Control', alternatives: ['Đài kiểm soát Norden'], confidence: 0.8}
  - {id: b08-air-burst, keep_provisional: true, proposed_vi: 'đạn nổ trên không', alternatives: ['bắn nổ trên không', 'đạn nổ cao'], confidence: 0.75, note: 'sửa câu dịch cho khớp'}
  - {id: b08-time-on-target, keep_provisional: true, proposed_vi: 'bắn cho đạn cùng rơi trúng mục tiêu một lúc', alternatives: ['bắn TOT', 'bắn đồng loạt theo thời điểm đạn rơi'], confidence: 0.55, uncertainty: 'chưa đủ căn cứ để chốt'}
  - {id: b08-artillery-arm, keep_provisional: true, proposed_vi: 'pháo binh', alternatives: ['binh chủng pháo binh'], confidence: 0.6}
  - {id: b08-field-corps-integration, keep_provisional: true, proposed_vi: 'pháo binh được tích hợp ở cấp quân đoàn dã chiến', alternatives: ['pháo binh phối thuộc cấp quân đoàn'], confidence: 0.45, uncertainty: 'bất định cao'}
  - {id: fire-for-effect, add_pending: true, proposed_vi: 'bắn hiệu lực', segment_ids: [p000137], confidence: 0.8}
  - {id: observed-fire, add_pending: true, proposed_vi: 'bắn có quan sát', alternatives: ['bắn theo quan sát'], segment_ids: [p000136], confidence: 0.6}
  - {id: fuji-firepower-review, keep_provisional: true, proposed_vi: 'buổi trình diễn hỏa lực Fuji', segment_ids: [p000133], confidence: 0.8}
  - {id: radio-over-out-roger, add_pending: true, proposed_vi: 'Over=Hết; Out=Kết thúc (cân nhắc); roger=rõ', segment_ids: [p000139, p000140], confidence: 0.4}
  - {id: general-lee-title, add_pending: true, proposed_vi: 'Tướng Lee', segment_ids: [p000135], confidence: 0.55}
risks:
  - 'Nhất quán Norden Control và thuật ngữ vô tuyến trong chương'
  - 'Thuật ngữ pháo binh chưa có canon'
  - 'field corps / mixed fighter-bomber squadron thiếu căn cứ'
commit: null
next_action: translator sửa M1–M7 và các lỗi nhẹ được chấp nhận; coordinator cập nhật ledger và handoff
```
