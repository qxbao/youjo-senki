# Review b12 — vol-02-ch-02-b12-review

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích câu nguồn.
- **Phạm vi:** 29 đoạn `YS-LN02/Text/part0014.xhtml/p000300`–`p000328` (viết tắt `pNNNNNN`). Đã đọc: handoff b12, gói nguồn đã chuẩn bị, `translations/vol-02/ch-02-b12.jsonl`, `canon/` (glossary, characters, style-guide, decisions, glossary-pending) và `work/run-state/pending-terms.yml` (mục `chapter2_b12_translation_proposals` cùng các mục liên quan đến đơn vị, Named, Commonwealth/Entente/Republic, control unit, Cụm tập đoàn quân). Không đọc batch dịch khác.
- **Kiểm tra cơ học:** 29/29 đoạn; thứ tự p000300→p000328 liên tục; `segment_id` khớp gói nguồn; `source_sha256` từng đoạn khớp; `glossary_version` khớp handoff; `notes` rỗng, không có ghi chú làm việc lẫn vào bản dịch. Chữ nghiêng (DEC-P01-002): nguồn chỉ nhấn mạnh ở p000311 và p000324; bản dịch có `*...*` đúng hai chỗ này, phạm vi khớp, không thêm thừa. Dấu thoại không có lỗi đóng/mở.

## Kết luận: `needs_fixes` (serious 0, moderate 3, minor 13)

Chất lượng nhìn chung tốt: phủ định, logic điều kiện, chuỗi suy luận về nhận diện và chú ý "ý đồ khẩu khí" được giữ chắc. Ba lỗi moderate đều nhỏ và sửa nhanh. Không có hard stop.

## Moderate

### MOD-1 — p000301: thêm sắc thái miệt thị/phán xét không có trong nguồn
- **Vấn đề:** "bọn Cộng hòa" thêm sắc thái khinh miệt; "mơ mộng hão huyền" thêm đánh giá "viển vông". Nguồn chỉ là nghi ngờ nhẹ rằng phía Cộng hòa đang mơ màng/tưởng tượng. Style guide: không thêm sắc thái phán xét/miệt thị. Ledger dùng "quân Cộng hòa" / "Cộng hòa".
- **Đề xuất:** "Cô ấy có thật sao? Tôi cứ tưởng phía Cộng hòa chỉ đang mơ mộng thôi." (hoặc "quân Cộng hòa").
- **Độ tin cậy:** 0,7.

### MOD-2 — p000310: quan hệ "nên" có nguy cơ vô lý do cách hiểu "bên đó" chỉ nơi chốn
- **Vấn đề:** câu nguồn mơ hồ giữa (a) giao tranh ở đó đã phần lớn kết thúc và (b) giao tranh phần lớn diễn ra ở đó. Bản dịch chọn (b) ("diễn ra bên đó"), rồi nối bằng "nên … có thể điều quân đi nơi khác", nên lập luận tự mâu thuẫn. Ngữ cảnh ủng hộ (a): p000311 nói "khi rảnh tay" mới điều đi; p000318 nói Dacia đã thất thủ nhanh. "đều" và "điều quân" (thay cho "chuyển đơn vị đó") cũng là thêm nhẹ.
- **Đề xuất:** "Giao tranh bên đó phần lớn đã xong rồi, nên có lẽ họ đủ sức điều đơn vị ấy đi nơi khác." Nếu coordinator muốn giữ mơ hồ: dùng cách nói trung lập "Phần lớn giao tranh nằm ở phía đó" chỉ khi bỏ liên từ "nên" (không khuyến nghị).
- **Độ tin cậy:** 0,6 cho (a). Không ảnh hưởng cốt truyện lớn; không hard stop.

### MOD-3 — p000311, p000314, p000317, p000318: đại từ chỉ viên sĩ quan tình báo không nhất quán và có suy diễn tuổi/vai vế
- **Vấn đề:** p000311 dùng "Anh ta", còn p000314/317/318 dùng "ông". Nguồn dùng cùng đại từ nam; không có thông tin tuổi hoặc cấp bậc. "ông" suy ra người lớn tuổi/cao vai vế, trái giới hạn suy luận của DEC-P01-001. Nếu đây là cùng một nhân vật (p000312–p000313 là lời của viên sĩ quan tình báo; p000314 gọi nhân vật này bằng chức danh) thì hai cách gọi gây hiểu thành hai người.
- **Đề xuất:** thống nhất "anh ta" (hoặc lặp "viên sĩ quan tình báo" ở chỗ cần rõ). Không dùng "ông" khi chưa có căn cứ.
- **Độ tin cậy:** 0,6.

## Minor

- **m1 — p000300, p000301, p000304, p000305 ("cô ta"):** ledger b11 đề xuất "cô" cho "she" chỉ Tanya (0,55). "cô ta" nghiêng về xa cách/khinh thường hơn nguồn. Đề xuất "cô ấy" hoặc "cô" nhất quán cả batch. Alternative: giữ "cô ta" nếu coordinator muốn góc nhìn kẻ thù. Độ tin cậy 0,5. Không suy diễn danh tính Tanya.
- **m2 — p000300:** "a nice cup" mất "nice": "tách trà ngon" sát hơn. Độ tin cậy 0,5.
- **m3 — p000302:** "máy liên lạc" gán chức năng cho từ trung tính ("machines"); p000303 dùng "ống nghe" cho receivers. Đề xuất "máy" / "thiết bị". Độ tin cậy 0,4.
- **m4 — p000303:** "cấp chỉ huy tối cao" nghe như bộ tư lệnh tối cao; "high command" nên là "bộ chỉ huy cấp cao" / "thượng cấp". Độ tin cậy 0,45.
- **m5 — p000305:** "nửa phần tin rằng nó chẳng có thật" đổi "nửa hồ nghi liệu nó có thật không" thành niềm tin phủ định. Đề xuất: "nhập mẫu tín hiệu vào với nửa ngờ rằng liệu nó có thật không". Độ tin cậy 0,6.
- **m6 — p000309:** "quá nhiều sức ép" nặng hơn "so much"; đề xuất "nhiều sức ép đến vậy". Chủ thể gây sức ép (Đế quốc) bị bị động hóa; chấp nhận được. Độ tin cậy 0,4.
- **m7 — p000311:** "mấy cậu Hướng đạo sinh" thêm "cậu" (thân mật); "cuộc càn quét" cho "rampage" mang nghĩa quân sự "quét sạch", nên "cuộc tung hoành/quậy phá". "ngạo mạn" chấp nhận được (alternative "xấc xược"). Độ tin cậy 0,4.
- **m8 — p000312, p000322:** "Ta" đứng đầu lời thoại có thể bị đọc là "tôi" cổ/vị thế trên; p000323 dùng "chúng ta". Đề xuất "Chúng ta" nhất quán. Độ tin cậy 0,4.
- **m9 — p000314:** "có thể đang trò chuyện" biến nhượng bộ ("dù đang trò chuyện") thành phỏng đoán không chắc. Đề xuất "Viên sĩ quan tình báo tuy đang trò chuyện, nhưng suốt lúc đó…". Độ tin cậy 0,5.
- **m10 — p000315:** "liên lạc vô tuyến" thêm "vô tuyến"; nguồn dùng từ trung tính cho truyền tin. Đề xuất "truyền tin"/"liên lạc". Độ tin cậy 0,4.
- **m11 — p000316:** "Chúng" xuất hiện hai lần với hai đối tượng khác nhau (kẻ địch, rồi mật mã/giao thức), và "chúng" chỉ người mang sắc thái miệt thị nhẹ. Đề xuất: "Đối phương dùng… Ít nhất thì mật mã và giao thức ấy không có trong thư viện dữ liệu." Độ tin cậy 0,55.
- **m12 — p000325:** bỏ so sánh "calmer" (bình tĩnh hơn các sĩ quan vừa nói) → "bình tĩnh hơn". Hình ảnh bệnh nhân rồi chuyển sang "họ sẽ lên cơn co giật": nên lặp "Liên minh" hoặc dùng "nó"/"người bệnh" để giữ liền mạch ẩn dụ. Độ tin cậy 0,5.
- **m13 — p000328:** thiếu "consciously" (chủ ý gạt bỏ). Đề xuất "cố ý gạt những ý nghĩ ấy". Độ tin cậy 0,55.

(Ghi nhận không phải lỗi: p000304 "tín hiệu đặc trưng" cho signature, p000305 "mẫu tín hiệu" cho pattern, p000313 "hắn" cho Named bị gọi là nam, p000300–p000305 "cô ta" cho Tanya — giữ khác biệt giới trong lời kẻ quan sát, không hòa giải.)

## Thuật ngữ đề xuất của translator — đề xuất tạm (không canon)

### 1. mana inclination — p000307, p000314 (xuất hiện thêm khái niệm đối chiếu ở p000304, p000308, p000316, p000319)
- **Phân tích:** ngữ cảnh không ngụ ý năng khiếu bẩm sinh. "Inclination" là đặc điểm/mẫu của tín hiệu mana được so với "hồ sơ" và "thư viện" (p000307 so sánh với hồ sơ hiện có; p000314 ông chưa từng thấy; p000319 hầu như không có điểm tương đồng). Nguồn tách khái niệm này khỏi "signature" (p000304) và "pattern" (p000305), nên không nên gộp.
- **Đề xuất tạm:** giữ **"khuynh hướng mana"** (0,5): sát từ gốc, ít suy diễn lore, đọc được như một đặc điểm của tín hiệu.
- **Thay thế:** "thiên hướng mana" (0,15; gợi năng khiếu/thiên bẩm, loại); "đặc tính mana" (0,25; tự nhiên hơn nhưng diễn giải thêm); "đặc trưng mana" (0,1; trùng "tín hiệu đặc trưng" ở p000304). Khuyến nghị coordinator ghi thêm các đoạn đối chiếu để batch sau nhất quán.
- **Lưu ý:** "mana" tự thân không có mục ledger riêng trong những gì tôi đọc; coordinator nên kiểm tra các batch trước (tôi không đọc) để chắc "mana" so với "ma lực" nhất quán.

### 2. augmented battalion — p000307
- **Phân tích:** nguồn đối lập "tiểu đoàn" với "tiểu đoàn được/ có thể được tăng cường", tức một tiểu đoàn mang thêm lực lượng/biên chế hơn chuẩn; modifier mô tả loại biên chế hơn là trạng thái tạm thời. "tiểu đoàn tăng cường" là cách nói quân sự quen thuộc trong tiếng Việt và khớp ledger `augmented mage battalion` ("tiểu đoàn pháp sư tăng cường") và `augmented unit` ("đơn vị tăng cường").
- **Đề xuất tạm:** giữ **"tiểu đoàn tăng cường"** (0,65).
- **Thay thế:** "tiểu đoàn được tăng cường" (0,25; nhấn trạng thái); "tiểu đoàn tăng viện" (0,1; dễ lẫn "viện binh" ở p000306, loại).

### 3. Mục nên thêm vào ledger (đề xuất, không canon)
| Mục | Đề xuất | Thay thế | Độ tin cậy | Đoạn |
|---|---|---|---|---|
| Western Army Group | Cụm tập đoàn quân phương Tây | phía Tây | 0,55 | p000319 |
| high command | bộ chỉ huy cấp cao | thượng cấp | 0,45 | p000303 |
| library (record library) | thư viện dữ liệu | kho hồ sơ | 0,5 | p000308, p000316 |
| intelligence officer (pronoun) | anh ta | viên sĩ quan tình báo | 0,55 | p000311, p000314, p000317, p000318 |
| Republicans (casual) | quân Cộng hòa / phía Cộng hòa | Cộng hòa | 0,6 | p000301 |
| control unit — bổ sung chứng cứ | giữ "đơn vị điều khiển" | đơn vị kiểm soát | 0,4 | p000320, p000322 |

Ghi chú: p000322 đáp lại bằng chuyện không thể đưa máy bay vào, gợi rằng "control unit" ở p000320 có thể là đơn vị thuộc không quân/kiểm soát không phận. Đây là phỏng đoán lore, **không** dùng làm căn cứ dịch; chỉ nên thêm đoạn vào mục `vol02-ch02-b11-control-unit`. Lưu ý thêm: ledger đang lệch "phía Đông" (Eastern) với "phương Bắc" (Northern); bản dịch b12 theo "phương", nên coordinator chốt một dạng cho cả ba cụm tập đoàn quân.

## Rủi ro
- Không có serious. Không hard stop; không cần hỏi người dùng.
- MOD-2 (p000310) là điểm duy nhất có thể ảnh hưởng hiểu nghĩa cốt truyện nhẹ (trạng thái chiến sự ở Dacia); nếu chọn sai không chặn các batch sau.
- Đại từ "cô ta"/"cô ấy" cho Tanya và "hắn" cho Named phản ánh hiểu lầm của người quan sát; không suy diễn danh tính.
- Batch chưa đạt hoàn tất theo `completion` cho tới khi áp dụng MOD-1..3 và các minor nên sửa.

## Đề xuất bước tiếp theo
Người giữ quyền sửa áp dụng MOD-1..3 và các minor nên sửa (m1, m5, m9, m11, m13 ưu tiên), coordinator cập nhật ledger theo bảng trên, chạy lại validator/diff-check, rồi Claude ký xác nhận sau sửa trước khi commit. Validator/diff_check: not_run; commit: null.
