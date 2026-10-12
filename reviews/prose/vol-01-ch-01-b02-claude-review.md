# Phản biện ngữ nghĩa và văn phong — vol-01 Chương 1, lô b02

Người phản biện: Claude. Task: `vol-01-ch-01-b02-review`. Phạm vi: 17 đoạn `pNNNNNN` (p000012–p000028), tiền tố đầy đủ `YS-LN01/Text/chapter003b.xhtml/`. Báo cáo không chép câu nguồn; chỉ dùng mã đoạn và thuật ngữ nguyên gốc ngắn để nhận diện.

Đầu vào đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, handoff `review-ch-01-b02.yml`, gói nguồn b02 (đọc tại chỗ), bản dịch b02, `work/run-state/pending-terms.yml`, báo cáo quyết định tạm ch-00, `canon/*` (glossary và characters vẫn rỗng; decisions có DEC-P01-001/002), bản dịch b01 để đối chiếu nhất quán.

**Tính chất:** mọi phương án dưới đây là **đề xuất tạm theo chính sách tự động hóa (AGENTS.md)**, không phải canon, không thay `canon/decisions.md`. Báo cáo không sửa bản dịch, canon, handoff hay sổ pending. Validator/diff_check: not_run; commit: null. Thang tin cậy: cao ≥ 0,75; vừa 0,5–0,74; thấp < 0,5.

## 1. Tóm tắt

- Không có hard stop và không có lỗi nghiêm trọng. Không mục nào làm đổi cốt truyện.
- Số phát hiện: nghiêm trọng 0, vừa 6, nhẹ 13.
- Đoạn sạch hoặc chỉ có vấn đề rất nhỏ: p000017, p000020.
- Các vấn đề vừa đáng sửa trước khi nâng lô: (1) đại từ "cô" cho Tanya lệch DEC-P01-001; (2) mất dấu chú thích ở p000021; (3) dấu nhấn mạnh ở p000027 đặt sai từ; (4) p000027 hiểu sai sắc thái "obnoxiously" và "really"; (5) p000028 dịch "gone on duty" thành "nhận nhiệm vụ"; (6) "fire for effect" nên dùng thuật ngữ pháo binh chuẩn.
- Nhìn chung bản dịch giữ tốt nghĩa, nhịp độc thoại nội tâm và các lựa chọn tạm đã có (tái sinh, quả cầu tính toán, thuật thức, hô hiệu). Không thấy thêm ý hay lược ý lớn.

## 2. Phát hiện vừa

| # | Mã đoạn | Vấn đề | Đề xuất | Tin cậy |
|---|---|---|---|---|
| M1 | p000013, p000026, p000027 | Trần thuật về Tanya dùng "cô" (nhiều chỗ ở p000026, p000027, một chỗ ở p000013). DEC-P01-001 (đã duyệt) quy định trần thuật Tanya dùng "nó", nội tâm dùng "mình"; b01 né đại từ bằng cách lặp tên hoặc lược chủ ngữ. Dùng "cô" cũng gán thêm giới tính/quan hệ mà quyết định cấm suy ra. | Ưu tiên phương án trung tính nhất quán với b01: lặp "Tanya" hoặc lược chủ ngữ. Nếu coordinator xác nhận phạm vi "giai đoạn này" của DEC-P01-001 bao trùm Chương 1 thì dùng "nó". Không giữ "cô". | 0,7 |
| M2 | p000021 | Nguồn có đánh dấu chú thích 4 sau "ICBM"; bản dịch bỏ mất dấu. Quy ước hiện có trong ch-00 là chèn ký tự chỉ số trên (¹ ² ³). | Thêm "⁴" ngay sau cụm dịch của ICBM ở lần xuất hiện đầu. Lần nhắc lại không cần dấu. | 0,85 |
| M3 | p000027 | Nguồn nhấn mạnh từ "young". Bản dịch lại đánh dấu `*cực kỳ*`, tức nhấn mạnh trạng từ, không phải từ được nhấn. Trái DEC-P01-002 (giữ đúng phạm vi nhấn mạnh). | "…một đứa trẻ cực kỳ *nhỏ tuổi*" (hoặc "*bé* xíu" nếu muốn khẩu ngữ hơn, nhưng không nên đổi trọng tâm). | 0,8 |
| M4 | p000027 | Hai chỗ lệch sắc thái ở cùng đoạn. (a) "obnoxiously" là đánh giá của người kể về cách người ta ví von; "người ta đang khó chịu mà ví cô…" đọc thành người ta đang khó chịu, mơ hồ chủ thể. (b) "really" nằm giữa hai dấu gạch là lời nhấn "thật đấy", không phải tự sửa; "—không, một đứa trẻ…" biến nó thành lời phủ định và sửa lại. | (a) "Rõ ràng, người ta cứ ví Tanya với tiên nữ một cách đáng ghét." (b) "…đứa nhóc còi cọc—thật đấy—một đứa trẻ cực kỳ *nhỏ tuổi*." | 0,7 |
| M5 | p000028 | "Gone on duty twenty-four hours ago" dịch thành "nhận nhiệm vụ từ hai mươi tư giờ trước": nhận nhiệm vụ không phải vào ca trực, và "từ … giờ trước" đọc như mốc kéo dài. "Suited up" dịch thành "mặc quân phục" thu hẹp việc mặc trang bị. | "…miễn cưỡng mặc trang bị rồi vào ca trực cách đây hai mươi tư giờ." Nếu bản dịch muốn giữ quân phục thì "mặc quân trang". | 0,75 |
| M6 | p000012, p000014 | "Fire for effect" dịch "bắn hiệu quả". Trong pháo binh tiếng Việt cặp thuật ngữ quen dùng là bắn điều chỉnh (hiệu chỉnh) và **bắn hiệu lực**. "Hiệu quả" nghe như tính từ đánh giá, không phải lệnh. | Mệnh lệnh ở p000014: "Bắn hiệu lực." Giữ "bắn hiệu chỉnh" cho calibration fire. Cặp này thống nhất để dùng cho các cảnh pháo sau. | 0,7 |

## 3. Phát hiện nhẹ

| # | Mã đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| m1 | p000012 | "Base piece" → "khẩu pháo cơ sở" ít quen; khẩu pháo dùng làm chuẩn để hiệu chỉnh thường gọi là khẩu chuẩn. | "khẩu pháo chuẩn" (0,55); giữ "cơ sở" nếu muốn literal. |
| m2 | p000015 | Mất "now" ở lệnh bắt đầu. Thoại vô tuyến ngắn nên không nghiêm trọng. | "Bắt đầu nhiệm vụ bắn pháo ngay." Giữ "nhiệm vụ bắn pháo" cho fire mission (0,6). |
| m3 | p000013, p000026, p000027 | Viết hoa quân hàm không đồng nhất: "Thiếu úy"/"Chuẩn úy" trước tên, "phong Thiếu úy" khi đứng riêng, trong khi b01 viết thường "thiếu úy ma pháp". | Viết thường khi đứng riêng ("được phong thiếu úy"). Trước tên chọn một kiểu và dùng cả chương. |
| m4 | p000016 | "Nhìn xuống dưới" thừa. "Mang giới tính trái ngược" làm mất chủ thể bị biến đổi và "fighting" mờ đi. | "…nhìn xuống bên dưới", "giới tính đối lập", "phải đi đánh trận". Nhẹ, chấp nhận được nếu giữ nguyên. |
| m5 | p000018 | "Partner" khi đấu tập dịch "đối thủ"; đây là bạn tập, sắc thái đối kháng không có trong nguồn. | "bạn tập" hoặc "người tập cùng". |
| m6 | p000019 | "Realm of numbers" → "miền số học" dễ hiểu thành toán số học; "bò sấp" lạ. | "miền con số" (hoặc "thế giới số"); "bò lết bằng bụng". Giữ "ba vectơ số", "thuật thức gây nhiễu ma pháp" (xem mục 4). |
| m7 | p000021 | "Drills" → "huấn luyện" gần trùng nghĩa với nội dung đào tạo; trong bối cảnh duy trì khí tài thì nghiêng về diễn tập. "Make provisions" → "dự trù" ổn. | "diễn tập". |
| m8 | p000022, p000023 | "Xung đột trong các cuộc đụng độ" lặp ý; "trường chính trị quốc tế" lạ; "áp đảo" nhấn hơn "incredible powerhouse". | "giằng co với những vụ đụng độ biên giới không chính thức"; "chính trường quốc tế"; "mạnh khủng khiếp". |
| m9 | p000024 | "Thì quá khứ" là calque ngữ pháp tiếng Anh; tiếng Việt không có thì. Nghĩa vẫn truyền được. | "…phải nhắc đến nó như chuyện đã qua." |
| m10 | p000025 | "Đấu súng" gợi quyết đấu tay đôi; "firefights" là giao tranh nhỏ. | "đọ súng" hoặc "giao tranh lẻ tẻ". |
| m11 | p000026 | (a) "Thường sẽ" thay cho "bình thường thì" (nguồn nói điều hợp lẽ). (b) "Trường sĩ quan" ở p000026 nhưng "học viện" ở p000027 cho cùng cơ sở "academy", đồng thời dễ nhầm với "trường đào tạo sĩ quan ma pháp" ở p000028, vốn là nơi khác. (c) Xem mục 4 về tên cơ quan. | (a) "thì bình thường cô sẽ được điều về…" (đổi đại từ theo M1). (b) Thống nhất một tên cho academy, ví dụ "học viện quân sự", để tách với trường sĩ quan ma pháp. |
| m12 | p000027 | "Thanks to them" mỉa mai nhưng dịch "Vì họ". "Did start to seem" mất "bắt đầu". | "Nhờ họ" ; "hô hiệu ấy bắt đầu có vẻ hợp thật". |
| m13 | p000028 | (a) "Administrative unit" → "đơn vị hành chính" dễ hiểu thành đơn vị lãnh thổ. (b) "New transfer" → "lính mới" trùng bản dịch của "greenhorn" ở p000026 trong khi Tanya là sĩ quan. (c) "Border army" → "quân đội biên phòng" gợi lực lượng biên phòng hiện đại và lệch "lục quân" ở p000027. (d) "The brass" → "cấp trên" mất sắc thái khẩu ngữ. | (a) "đơn vị biên chế" (0,5). (b) "người mới chuyển đến". (c) "lục quân biên giới" hoặc giữ "quân biên phòng" kèm ghi chú, tin cậy 0,5. (d) "cấp chỉ huy cao" hoặc "các sếp lớn" tùy giọng. |

## 4. Thuật ngữ mới: phương án tạm ưu tiên (không canon)

Tin cậy tính cho phương án ưu tiên; phương án thay thế là lựa chọn dự phòng.

| Thuật ngữ nguồn | Bản dịch hiện tại | Phương án tạm ưu tiên | Tin cậy | Ghi chú / thay thế |
|---|---|---|---|---|
| base piece | khẩu pháo cơ sở | khẩu pháo chuẩn | 0,55 | giữ "cơ sở" được |
| calibration fire | bắn hiệu chỉnh | bắn hiệu chỉnh | 0,65 | alt: bắn điều chỉnh |
| fire for effect | bắn hiệu quả | bắn hiệu lực | 0,7 | thuật ngữ pháo binh quen dùng |
| fire mission | nhiệm vụ bắn pháo | nhiệm vụ bắn pháo | 0,6 | alt: nhiệm vụ bắn |
| Second Lieutenant | thiếu úy | thiếu úy (viết thường khi đứng riêng) | 0,8 | khớp "thiếu úy ma pháp" b01 |
| Warrant Officer | chuẩn úy | chuẩn úy | 0,65 | cấp thấp hơn thiếu úy; không suy thêm về hệ cấp bậc |
| Technical Arsenal | Kho Vũ khí Kỹ thuật | Xưởng Vũ khí Kỹ thuật | 0,5 | "Kho" thu hẹp thành nơi chứa; "arsenal" có thể gồm cả chế tạo. Giữ "Kho" nếu coordinator muốn literal |
| Logistical Command | Bộ Chỉ huy Hậu cần | Bộ Tư lệnh Hậu cần | 0,5 | "Bộ Chỉ huy" cũng dùng được; chọn một kiểu cho mọi "Command" về sau |
| semi-war | bán chiến tranh | tình trạng "bán chiến tranh" | 0,6 | giữ ngoặc kép như nguồn |
| brinkmanship diplomacy | ngoại giao bên miệng hố chiến tranh | giữ nguyên | 0,7 | khớp cách gọi quen thuộc của brinkmanship |
| magic officer training school | trường đào tạo sĩ quan ma pháp | giữ nguyên | 0,65 | tách khỏi "học viện quân sự" |
| three numeric vectors | ba vectơ số | giữ nguyên | 0,6 | giữ literal, không suy diễn thành "vectơ ba chiều" |
| magical interference formulas | thuật thức gây nhiễu ma pháp | giữ nguyên | 0,6 | theo P01-formulas |
| ICBM | tên lửa đạn đạo liên lục địa | giữ nguyên + "⁴" ở lần đầu | 0,65 | nhắc lại có thể dùng cùng dạng; cân nhắc "ICBM" nếu chú thích đã giải thích |
| call sign | hô hiệu | giữ nguyên | 0,7 | khớp b01 và P01-call-sign |
| border army | quân đội biên phòng | lục quân biên giới | 0,5 | hoặc giữ nếu chấp nhận sắc thái biên phòng |
| administrative unit | đơn vị hành chính | đơn vị biên chế | 0,5 | tránh hiểu nhầm đơn vị lãnh thổ |

Nhất quán với lựa chọn đã có: "tái sinh" ở p000016 khớp review-reborn; "quả cầu tính toán" và "thuật thức" khớp b01.

## 5. Kiểm tra nhất quán và nhấn mạnh

- Dấu nhấn mạnh: nguồn chỉ có một chỗ nhấn mạnh (p000027). Bản dịch có đánh dấu nhưng sai từ (M3). Không có nhấn mạnh thừa ở đoạn khác.
- Chú thích: nguồn có một dấu (p000021); bản dịch thiếu (M2).
- Xưng hô: các câu nội tâm dùng "mình" ổn và khớp DEC-P01-001. Vấn đề chỉ nằm ở trần thuật ngôi ba (M1). Đại từ "anh ta" cho bạn tập ở p000018 chỉ là đại từ nam theo nguồn, không phải xưng hô thân mật.
- Số liệu: mười mét, bốn mươi tám giờ, hai mươi tư giờ, Fairy 08, Goliath 07 đều giữ đúng.
- Ghi chú của translator ở các đoạn dùng chung ghi lặp cả danh sách thuật ngữ cho nhiều đoạn (p000013, p000014, p000015, p000026–p000028) không liên quan nội dung từng đoạn; không ảnh hưởng bản dịch xuất bản nhưng nên gọn hơn khi tổng hợp.
- Điểm bất định về nguồn: người nói ở p000012 và p000015 suy từ mã gọi (Goliath 07 tự xưng) khớp cách b01 dùng; không có nhãn người nói tường minh. Tin cậy 0,7; giữ nguyên bản dịch.

## 6. Rủi ro

- M1 phụ thuộc phạm vi "giai đoạn này" của DEC-P01-001; nếu coordinator giải thích rộng hơn, "nó" thay cho tên lặp.
- Tên cơ quan (Technical Arsenal, Logistical Command) và "border army" chỉ dựa vào ngữ cảnh một đoạn; có thể phải đổi khi các đoạn sau mô tả rõ chức năng.
- "Bán chiến tranh" và "ngoại giao bên miệng hố chiến tranh" là calque dễ hiểu nhưng chưa có đối chiếu bên ngoài.
- Mọi lựa chọn trên vẫn là đề xuất, chưa canon.

```yaml
role: reviewer
task_id: vol-01-ch-01-b02-review
state: done
review_path: reviews/prose/vol-01-ch-01-b02-claude-review.md
segment_ids: [p000012, p000013, p000014, p000015, p000016, p000017, p000018, p000019, p000020, p000021, p000022, p000023, p000024, p000025, p000026, p000027, p000028]
files_written: [reviews/prose/vol-01-ch-01-b02-claude-review.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 6, minor: 13}
unresolved_findings: [M1 đại từ cô, M2 dấu chú thích p000021, M3 nhấn mạnh p000027, M4 sắc thái p000027, M5 p000028 vào ca trực, M6 bắn hiệu lực]
term_recommendations: [fire-for-effect→bắn hiệu lực, base-piece→khẩu pháo chuẩn, Technical-Arsenal→Xưởng Vũ khí Kỹ thuật, Logistical-Command→Bộ Tư lệnh Hậu cần, border-army→lục quân biên giới, administrative-unit→đơn vị biên chế]
risks: [phạm vi DEC-P01-001, tên cơ quan chỉ dựa một đoạn, không có nhãn người nói ở p000012/p000015]
commit: null
next_action: coordinator ghi lựa chọn vào ledger/handoff; giao translator áp dụng M1–M6 và các mục nhẹ được chọn; chạy validator và diff-check
```
