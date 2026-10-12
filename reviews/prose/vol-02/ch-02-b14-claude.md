# Review b14 — vol-02-ch-02-b14-review

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích câu nguồn.
- **Phạm vi:** 38 đoạn `YS-LN02/Text/part0014.xhtml/p000354`–`p000391` (viết tắt `pNNNNNN`). Đã đọc: handoff b14, gói nguồn đã chuẩn bị, `translations/vol-02/ch-02-b14.jsonl`, `canon/` (glossary, characters, style-guide, decisions, glossary-pending), `agents/reviewer.md`, `agents/shared.md` và `work/run-state/pending-terms.yml` (mục `chapter2_b14_translation_proposals` cùng các mục liên quan: đại từ Tanya/Named, cấp bậc Serebryakov, thuật thức, control unit, Combat Direction Center). Không đọc batch dịch khác.
- **Kiểm tra cơ học:** 38/38 đoạn; thứ tự p000354→p000391 liên tục, không dư/thiếu; `segment_id`, `source_sha256`, `glossary_version` khớp; `notes` rỗng; status `draft`. Dấu ngoặc thoại cân. Không thấy ghi chú làm việc lẫn trong bản dịch.

## Kết luận: `needs_fixes` (serious 0, moderate 5, minor 11)

Nghĩa, phủ định và logic nhìn chung chắc (đặc biệt p000358–p000362 chuỗi phản đối/chấp nhận, p000363 giọng mỉa, p000384 điều kiện "trừ khi… hoặc ít nhất"). Năm lỗi moderate đều sửa nhanh, không có hard stop, không ảnh hưởng cốt truyện.

## Moderate

### MOD-1 — p000374, p000385, p000391: mất toàn bộ nhấn mạnh/chữ nghiêng (DEC-P01-002)
- **Vấn đề:** nguồn có chữ nghiêng ở ba chỗ: p000374 (toàn bộ đoạn là suy nghĩ nội tâm in nghiêng), p000385 (toàn bộ câu hỏi nội tâm), p000391 (chỉ một từ "hỗn loạn" được nhấn). Bản dịch không có `*...*` nào.
- **Đề xuất:** p000374 và p000385 bọc cả đoạn trong `*...*`; p000391 chỉ bọc đúng cụm "hỗn loạn" (không bọc cả câu). Không thêm nhấn mạnh ở đoạn khác (p000378 là lời cầu nguyện, nguồn không in nghiêng).
- **Độ tin cậy:** 0,9.

### MOD-2 — p000381, p000382, p000386, p000388, p000389, p000391: đại từ Tanya không theo DEC-P01-001/ledger
- **Vấn đề:** trần thuật về Tanya dùng "cô" xuyên suốt, trong khi DEC-P01-001 (đã duyệt) và ledger chương 2 chọn "nó" hoặc lặp tên Tanya/lược chủ ngữ; "cô" chỉ là phương án thay thế chưa chốt. Hệ quả cụ thể:
  - p000381: "cô" xuất hiện cho cả Tanya ("của cô") lẫn Serebryakov ("cô nói thêm") trong cùng đoạn, người đọc khó phân biệt người nói.
  - p000382–p000389: "cô" lặp dày, lại trùng với "cô ta" dành cho Named ở p000373/p000375 nên người đọc dễ lẫn hai chủ thể (cùng một người nhưng nhìn từ hai phía).
  - p000391: nội tâm tự quy chiếu dùng "Tôi" thay vì "mình" theo DEC-P01-001 (giữ "mình"; hoặc lược chủ ngữ).
  - p000387: lời Serebryakov hỏi/nhận xét dùng "cô" để gọi Tanya, không nhất quán với "Thiếu tá" ở p000381 và với ledger (gọi theo cấp bậc, tránh "cô/anh").
- **Đề xuất:** p000381 "người quan sát của nó" hoặc "người quan sát của Tanya", và đổi "cô nói thêm" thành "Serebryakov nói thêm" (lặp tên); p000382, p000386, p000388, p000389 dùng "nó" hoặc lược chủ ngữ/lặp "Tanya" ở chỗ cần rõ; p000391 "Mình sẽ kiên quyết từ chối"; p000387 "Chắc hẳn Thiếu tá đã đánh trúng…". Giữ "cô ta" cho Named (p000373, p000375) như ledger b13.
- **Phương án thay thế:** nếu coordinator chọn "cô" làm chuẩn cho giai đoạn này thì phải cập nhật DEC/ledger trước, rồi dùng nhất quán và vẫn lặp tên ở p000381.
- **Độ tin cậy:** 0,75. Ghi vào pending (xem pending_term_choices).

### MOD-3 — p000381: cấp bậc Serebryakov lệch ledger ("Trung úy" thay vì "Thiếu úy")
- **Vấn đề:** ledger các batch trước chốt tạm Serebryakov = Thiếu úy (Weiss = Trung úy); bản dịch viết "Trung úy Serebryakov". Nguồn chỉ ghi "Lieutenant" không rõ bậc, nên dễ trượt, nhưng đây là cùng một nhân vật đã có cách gọi tạm.
- **Đề xuất:** "Thiếu úy Serebryakov" cho nhất quán. Nếu coordinator muốn đổi, phải đổi ở ledger cho toàn bộ.
- **Độ tin cậy:** 0,7.

### MOD-4 — p000357: "đang ném bom" biến kế hoạch thành hành động đang diễn ra
- **Vấn đề:** ngữ cảnh là thảo luận phương án (p000355–p000356, p000358–p000363), các câu sau mang tính điều kiện ("chỉ cần… thành công", "còn nếu thất bại"). "Họ đang ném bom một kho nhiên liệu" nghe như sự kiện đang xảy ra, mâu thuẫn với việc sau đó họ còn đang bàn nên làm gì.
- **Đề xuất:** "Mục tiêu ném bom là một kho nhiên liệu." hoặc "Họ định ném bom một kho nhiên liệu." Phần còn lại giữ nguyên.
- **Độ tin cậy:** 0,55.

### MOD-5 — p000354: mất chủ thể "cô ấy/nó có lực lượng dự phòng" và nghĩa "backup"
- **Vấn đề:** nguồn nói lúc đối phương (một nhân vật nữ) có đơn vị Quân đội Đế quốc yểm trợ thì phía Thịnh vượng chung bắt đầu phải tính đến rút lui. Bản dịch bỏ chủ thể ("Khi có một đơn vị… làm lực lượng dự bị"), nên không rõ ai có lực lượng, và "dự bị" (reserve) lệch với "yểm trợ/hậu thuẫn" (backup).
- **Đề xuất:** "Khi phía Named có thêm một đơn vị Quân đội Đế quốc làm lực lượng hậu thuẫn, họ đã đến lúc phải tính chuyện rút lui. Nhưng họ không thể làm ngơ trước…". Nếu không chắc "she" là Named, chọn trung tính "khi đối phương có…". Không suy diễn danh tính.
- **Độ tin cậy:** 0,5. Ghi vào pending nếu coordinator xác nhận chủ thể.

## Minor

- **m1 — p000358:** "quá lớn để có thể bỏ qua" cho ý "gánh chịu nổi/gạt đi được"; đề xuất "tổn thất vượt quá mức chúng ta có thể chịu đựng". Độ tin cậy 0,4.
- **m2 — p000362:** "Làm vậy thì chúng ta được lợi rất nhiều" có thể đọc thành đồng tình tích cực; nguồn là lời nhận xét chấp nhận miễn cưỡng ("có nhiều thứ để được/mất", rồi "chẳng còn lựa chọn"). Đề xuất "Làm vậy chúng ta cũng thu được khá nhiều." Độ tin cậy 0,3.
- **m3 — p000363:** "chậm như rùa bò" là thành ngữ địa phương hóa thay cho cách nói của nguồn; chấp nhận được vì cùng sắc thái mỉa, chỉ nên nhất quán với phong cách các batch khác. Không cần sửa. Độ tin cậy 0,2.
- **m4 — p000365:** "thô thiển" cho "boorish" hơi nặng và lệch (boorish = thô lỗ, vụng về); đề xuất "một niềm hy vọng thô thiển" → "một niềm hy vọng quá đỗi thô lỗ/ích kỷ". Độ tin cậy 0,3.
- **m5 — p000367:** "điều phối lực lượng" thêm "lực lượng" so với "giving direction" (chỉ dẫn/điều hướng). Đề xuất "chỉ dẫn/điều phối". Cũng cân nhắc ghi rõ "hơn hai mươi cây số" là khoảng cách tới tiền tuyến theo đúng cấu trúc câu (đã đúng nghĩa, chỉ nhắc kiểm tra). Độ tin cậy 0,3.
- **m6 — p000370:** "lập tức" thêm vào "Đề nghị tìm chỗ trú ẩn". Bỏ "lập tức" cho sát nguồn. Độ tin cậy 0,3.
- **m7 — p000371/p000374:** "lần ra vị trí" suy rộng từ "bị dò/bị lần theo" (traced); chấp nhận, nhưng nếu muốn trung tính hơn dùng "bị dò ra". Độ tin cậy 0,25.
- **m8 — p000373 và p000388:** "controller(s)" dịch thành "Người điều khiển" ở p000373 nhưng "kiểm soát viên" ở p000388, trong khi p000369 dùng "phụ trách điều khiển" và ledger có "đơn vị điều khiển". Đề xuất thống nhất "nhân viên/người điều khiển". Độ tin cậy 0,5.
- **m9 — p000381:** "sóng trinh sát bị triệt tiêu" làm đổi nghĩa "collapse" (sụp đổ/ngừng đột ngột) sang "triệt tiêu" (hủy lẫn nhau như giao thoa). Đề xuất "đã xác nhận sóng giám sát bị mất/ngắt hẳn" (xem thuật ngữ 1). Độ tin cậy 0,55.
- **m10 — p000383:** "đợt sóng" gợi xung/đợt rời rạc trong khi nguồn là phát sóng mạnh liên tục (đối lập với "tiếp nhận thụ động"). Đề xuất bỏ "đợt": "phát ra sóng giám sát mạnh liên tục". Độ tin cậy 0,5 (xem thuật ngữ 1).
- **m11 — p000391:** "mô tả dè dặt" khó hiểu; đề xuất "nói giảm nói tránh nhất cũng là hỗn loạn" hoặc "nói nhẹ nhất thì đó cũng là hỗn loạn". Độ tin cậy 0,4. Ngoài ra p000378 (lời cầu nguyện) dùng "Ngài giáng sinh" và "Chúa": khớp ledger "Chúa", chỉ cần giữ cùng cách ở các lần lặp lại sau. Không cần sửa.

## Kiểm tra theo hạng mục
- **Phủ định:** p000358, p000360, p000375, p000384, p000385 đúng, không đảo nghĩa.
- **Người nói/đại từ:** thoại p000355–p000364 là sĩ quan Thịnh vượng chung (không rõ từng người), bản dịch dùng "tôi/chúng ta" trung tính, không suy cấp bậc. Thoại p000368–p000376 là phía Entente. Cách gọi Tanya/Serebryakov/Named xem MOD-2, MOD-3.
- **Nhấn mạnh:** nguồn nhấn p000374, p000385, p000391; bản dịch chưa có (MOD-1).
- **Thứ tự và định dạng:** đúng; không dư/thiếu đoạn.

## Pending term (đề xuất, không phải canon)

Xem YAML trả về: `pending_term_choices`.

1. **surveillance waves** (p000381, p000383, p000384): "waves" là sóng phát chủ động kiểu dò tìm (đối lập với bên chỉ thu thụ động), không phải "đợt/lượt". Khuyến nghị tạm **sóng giám sát**, vì "surveillance" gần "giám sát/quan sát" hơn "trinh sát" (reconnaissance), và đồng bộ với thuật ngữ thứ ba. Thay thế: sóng trinh sát (bản dịch hiện tại, chấp nhận được nếu coordinator ưu tiên thuật ngữ quân sự ngắn), làn sóng giám sát. Độ tin cậy 0,5. Tránh "đợt/làn" làm đơn vị đếm.
2. **magic bombardment formula** (p000373, p000379, p000380): giữ **thuật thức oanh kích ma pháp**; "thuật thức" khớp ledger (formula → thuật thức), "oanh kích ma pháp" giữ nhất quán với p000380. Thay thế: công thức oanh kích ma pháp, thuật thức pháo kích ma pháp. Độ tin cậy 0,6. Nên dùng cùng một cách ở mọi lần xuất hiện.
3. **surface surveillance train** (p000384): giữ nguyên "đoàn tàu", chuyển "trinh sát" thành **đoàn tàu giám sát mặt đất** để đồng bộ với thuật ngữ 1. Bối cảnh (nơi dễ rút lui, di động) gợi tàu hỏa hoặc đơn vị di động; nếu ngữ cảnh sau cho thấy là một biên đội/đơn vị thì đổi sang "đơn vị/đoàn giám sát mặt đất". Thay thế: đoàn tàu trinh sát mặt đất. Độ tin cậy 0,45. Độ bất định thấp ảnh hưởng cốt truyện; không cần hỏi người dùng.
4. **Đại từ Tanya (trần thuật/nội tâm)** (p000381–p000391): "nó" hoặc lặp tên/lược chủ ngữ cho trần thuật; "mình" cho nội tâm (theo DEC-P01-001). Thay thế: "cô" nếu coordinator đổi quyết định. Độ tin cậy 0,75.
5. **Cấp bậc Serebryakov** (p000381): Thiếu úy theo ledger. Thay thế: Trung úy (nếu ledger đổi). Độ tin cậy 0,7.

## Rủi ro
- Nếu sửa MOD-2 theo "nó" thì cần đồng bộ lại các batch chương 2 trước/sau (ledger đã ghi "rà đồng bộ"); báo coordinator, không sửa batch khác trong task này.
- Thuật ngữ 1 và 3 phụ thuộc cách hiểu "surveillance"/"train" chưa có canon; nếu đổi phải đổi đồng bộ cả ba đoạn.
