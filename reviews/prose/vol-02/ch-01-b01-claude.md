# Báo cáo review — vol-02-ch-01-b01

- Task: `vol-02-ch-01-b01-review`; phạm vi `YS-LN02/Text/part0008.xhtml/p000001`–`p000020` (20 đoạn).
- Đầu vào đã dùng: handoff `handoffs/vol-02/ch-01-b01.yml`, source package cục bộ (sha256 khớp `5a32b413…8239`), `canon/` (decisions, style-guide, glossary-pending), `work/run-state/pending-terms.yml`, `translations/vol-02/ch-01-b01.jsonl`.
- Không sửa bản dịch/canon/handoff/package/checkpoint; không đọc batch khác. Mọi lựa chọn dưới đây là đề xuất tạm, **không phải canon**.
- Báo cáo không chép câu nguồn; chỉ dùng mã đoạn, thuật ngữ ngắn và đoạn tiếng Việt của bản dịch để nhận diện.

## Kết luận chung

Bản dịch nhìn chung bám sát nghĩa, đúng chủ thể, phủ định và trình tự thời gian ở hầu hết đoạn. Không có lỗi nghiêm trọng. Có 6 lỗi mức vừa cần sửa trước khi nâng lên bản chuẩn, và 11 điểm nhẹ.

Đã kiểm tra nhấn mạnh (DEC-P01-002): nguồn chỉ có `<em>` ở p000006 và p000008; phạm vi `*...*` trong bản dịch khớp ở cả hai đoạn, không có đoạn nào bị thêm hoặc thiếu nhấn mạnh. **Không có lỗi về nhấn mạnh.**

## Đánh giá đề xuất FAC (p000003)

- **Chọn tạm:** giữ nguyên **FAC** trong văn bản (như bản dịch hiện tại: «FAC Dacia»); trong sổ pending ghi khai triển tạm là **«kiểm soát không quân tiền phương»**, bỏ chữ «viên».
- **Căn cứ:** trong cả lô chỉ xuất hiện một lần, trong ngữ cảnh Bộ chỉ huy đang theo dõi kênh liên lạc của FAC phía Dacia khi hỏi về tình hình trên không. Ngữ cảnh khớp với vai trò điều phối/liên lạc không – địa, nên cách khai triển «kiểm soát không quân tiền phương» là hợp lý.
- **Vì sao bỏ «viên»:** nguồn trong lô không cho biết FAC là một người hay một đài/đơn vị; «kiểm soát viên» khẳng định đó là người, tức là suy diễn. Dạng không có «viên» ít suy diễn hơn. Cách giữ nguyên viết tắt cũng không ép giải nghĩa vào văn bản dịch (hợp style-guide: không chèn giải thích).
- **Phương án thay thế:** «kiểm soát viên không quân tiền phương» (đề xuất của translator, nếu sau này xác nhận là người); «tiền sát viên không quân»; «dẫn đường không quân tiền phương».
- **Độ bất định:** vừa (confidence ≈ 0.55). Lô này không có khai triển viết tắt trong nguồn; cần đối chiếu khi viết tắt xuất hiện lại. Không ảnh hưởng cốt truyện, không cần hỏi người dùng.
- **Hành động:** không phải sửa bản dịch p000003; chỉ coordinator cập nhật `proposed_vi` trong ledger.

## Lỗi và đề xuất sửa

### Mức vừa

**F1 — p000014 — đảo sắc thái «chỉ… trên giấy tờ»**
- Căn cứ: nguồn nói ngày 24/9 chỉ là sinh nhật trên giấy tờ (không phải sinh nhật thật). Bản dịch dùng «…trên giấy tờ mới là sinh nhật cô», trong đó «mới là» nhấn rằng ngày trên giấy tờ *chính là* sinh nhật thật, ngược với ý nguồn. Đoạn sau (p000015) còn dựa vào ý «sinh nhật chỉ trên giấy» để nói về món quà sinh nhật đầu tiên.
- Sửa: «Ngày 24 tháng Chín chỉ là sinh nhật của cô trên giấy tờ.»

**F2 — p000015 — mất góc nhìn nội tâm và đổi mức độ của câu thứ hai**
- Căn cứ: câu thứ hai của đoạn là tiếng nội tâm ngôi thứ nhất của Tanya xen vào lời kể (có «tôi/mình»), nhưng bản dịch chuyển thành trần thuật «cô sắp nhảy chân sáo». Ngoài ra nguồn nói *có thể sẽ* làm vậy (khả năng, mức độ ít chắc chắn hơn), còn «sắp» nghĩa là sắp xảy ra thật. Vi phạm quy tắc giữ điểm nhìn, mức chắc chắn (style-guide).
- Sửa (gợi ý): giữ nội tâm, dùng «mình» (DEC-P01-001), mức khả năng — ví dụ «Hôm nay hẳn sẽ là một ngày tuyệt vời đến mức mình có thể nhảy chân sáo như một đứa trẻ hí hửng mất.»

**F3 — p000015 — lời cầu nguyện: thêm quan hệ «Người/con» và chọn «Chúa» lệch ledger**
- Căn cứ: nguồn chỉ gọi God và cảm ơn; không có quan hệ cha–con hay xưng «con». Bản dịch thêm «Người… con», biến lời thốt ra thành lời cầu nguyện thân phận con–Đấng; DEC-P01-001 cấm suy ra quan hệ từ ngữ cảnh mỏng. Hơn nữa ledger vol-01 đang tạm dùng «Thượng đế (ơi)» cho God, «lạy Chúa» chỉ là phương án thay thế; «Chúa» dành cho «the Lord». Đoạn p000016 nhấn rằng Tanya bình thường sẽ không nói ra lời này, nên bình diện Being X/God dễ ảnh hưởng cốt truyện — nên chọn dạng trung tính.
- Sửa (tạm, trung tính): «Thượng đế ơi, cảm ơn vì cơ hội một phần triệu này.» (hoặc «Lạy Thượng đế, cảm ơn vì…»). Bỏ «Người» và «con». Việc có chọn «Chúa» hay không là quyết định coordinator ghi vào ledger; không nâng canon.

**F4 — p000005 — giả định phản thực tế ở quá khứ bị đổi thành tương lai/khả năng hiện tại**
- Căn cứ: nguồn nói nếu Lergen *đã* thấy vẻ mặt ấy thì có lẽ *đã* cười như vậy (sự kiện không xảy ra ở quá khứ; đoạn p000018 xác nhận Lergen chỉ thấy cảnh Tanya chạy đi, không phải nụ cười). Bản dịch «nếu… trông thấy… sẽ mỉm cười» đọc như giả định tương lai. Style-guide: giữ thời gian của giả định.
- Sửa: «…nếu Lergen đã trông thấy vẻ mặt đó, có lẽ anh cũng đã mỉm cười y hệt.»

**F5 — p000011 / p000012 — tự xưng nội tâm không nhất quán («tôi» ↔ «mình» ↔ «tôi»)**
- Căn cứ: hai đoạn liền nhau cùng là độc thoại của Tanya; p000011 dùng «tôi», câu đầu p000012 dùng «mình», câu cuối p000012 lại «tôi». DEC-P01-001: nội tâm tự quy chiếu của Tanya dùng «mình».
- Sửa: dùng «mình» thống nhất ở p000011 và câu cuối p000012. Lưu ý độ bất định: DEC-P01-001 giới hạn «ở giai đoạn này», chưa chắc áp dụng cho LN02; nếu coordinator quyết định khác thì vẫn phải thống nhất một cách trong cả hai đoạn.

**F6 — các đoạn p000002, p000003, p000006, p000015, p000016, p000017, p000019 — trần thuật về Tanya dùng «cô»**
- Căn cứ: checkpoint pronouns của handoff chỉ dẫn theo DEC-P01-001 (trần thuật «nó», nội tâm «mình»); ledger vol-01 còn ghi lựa chọn trung hòa «lặp tên hoặc lược chủ ngữ, tránh “cô”». Bản dịch dùng «cô» xuyên suốt. DEC-P01-001 giới hạn theo giai đoạn và cấm suy ra quan hệ/giới tính chỉ từ một đoạn; nên «cô» là lựa chọn mới, chưa có căn cứ trong canon/ledger cho LN02.
- Đề xuất (tạm): chọn cách ít suy diễn nhất — lặp «Tanya» hoặc lược chủ ngữ; coordinator quyết định có kéo dài «nó» sang LN02 không. Nếu muốn giữ «cô», phải ghi rõ là lựa chọn mới trong ledger (không ảnh hưởng cốt truyện nhưng cần nhất quán toàn volume).

### Mức nhẹ

- **F7 — p000001:** «Thiếu tá chỉ huy tiểu đoàn» ghép cấp bậc (chỉ xuất hiện ở p000004) với chức vụ; nguồn ở đây chỉ nêu chức vụ. Gợi ý «Tiểu đoàn trưởng von Degurechaff»; giữ «Thiếu tá» ở p000004. Cách dịch Major → Thiếu tá là tạm, chưa canon.
- **F8 — p000002:** «đường dây liên lạc» thu hẹp đối tượng câu hỏi về liên lạc hữu tuyến, trong khi câu hỏi nói chung về hệ thống liên lạc (hữu tuyến/vô tuyến chỉ nêu ở p000003); «chẳng phát hiện máy bay nào» thu hẹp «aerial contacts» thành máy bay. Gợi ý «hệ thống liên lạc» và «tín hiệu/mục tiêu trên không nào».
- **F9 — p000006:** «khó lòng tin nổi vận may khó tin» lặp «khó»; gợi ý «vận may khó tin đến thế» hoặc «khó lòng tin nổi vận may của mình».
- **F10 — p000009:** «quyến rũ đến chết người» thêm sắc thái gây chết không có trong nguồn (chỉ mức độ cực kỳ quyến rũ). Gợi ý «quyến rũ đến mức khó cưỡng».
- **F11 — p000010:** «Dacia hoàn toàn không có lực lượng không quân địch» có thể đọc thành Dacia không có không quân của kẻ thù (chủ thể lệch); nguồn nói việc không quân địch ở Dacia vắng bóng. Gợi ý «Nhờ không quân địch ở Dacia hoàn toàn vắng bóng…». «Ưu thế tuyệt đối» cũng nên là «ưu thế tuyệt đối trên không» để giữ bình diện.
- **F12 — p000011:** «trong cả triệu năm» là calque; gợi ý «có nằm mơ cũng chẳng ngờ». «Bất tài» chỉ nói về cá nhân, nguồn nói về mức vô vọng của quân đội; gợi ý «tệ hại đến mức này».
- **F13 — p000013:** «xoay chuyển vận mệnh» mất ý «ý trời» (heaven’s will). Gợi ý «Đã bao giờ ý trời lại thuận lợi đến thế chưa?»; giữ «trời cao» ở câu sau.
- **F14 — p000015:** «cơ hội hiếm có» làm nhẹ mức «một phần triệu». Gợi ý «cơ hội ngàn năm có một» hoặc «cơ hội một phần triệu».
- **F15 — p000019:** «Bộ chỉ huy» dùng cho cả «Command» (p000002–p000004, p000016) lẫn «HQ». Ledger chỉ ghi «Bộ chỉ huy» cho Command; chưa có đề xuất cho HQ. Chấp nhận tạm, ghi vào ledger để phân biệt sau nếu cần.
- **F16 — p000020:** «sườn núi» nghĩa là mặt dốc, trong khi «ridge» là sống/gờ núi; «trải nghiệm sống còn quan trọng nhất: phép thử bằng lửa đạn» tách thành hai ý và thêm «sống còn» (không có trong nguồn). Gợi ý «đường sống núi» (hoặc «gờ núi») và «thiếu một lần thử lửa quan trọng nhất».
- **F17 — p000005, p000018, p000019:** «anh» cho Lergen là lựa chọn nội bộ, chưa có trong ledger cho nhân vật này; không suy ra tuổi/quan hệ. Nếu coordinator muốn trung hòa: lặp «Lergen» hoặc lược chủ ngữ.

## Đã kiểm tra, không có lỗi

- Phủ định, chủ thể và chuỗi thời gian ở p000002–p000004, p000007–p000008, p000012 (trừ F5), p000016–p000018 khớp nguồn.
- Số liệu «sáu trăm nghìn» và ngày 24 tháng Chín đúng; các tên Dacia, Norden, Rhine, Alpen, Lergen giữ nhất quán; «Tiểu đoàn Pháp sư Không quân 203» khớp ledger («pháp sư không quân»).
- Dấu hỏi/chấm than và giọng nội tâm ở p000007, p000008, p000013 được giữ.

## Thuật ngữ mới / đề xuất sổ pending (tạm, không canon)

| Thuật ngữ | Đề xuất tạm | Mã đoạn | Ghi chú |
|---|---|---|---|
| FAC | FAC (khai triển tạm: kiểm soát không quân tiền phương) | p000003 | xem mục FAC; confidence ≈ 0.55 |
| God (lời kêu cầu) | Thượng đế ơi / lạy Thượng đế (thay thế: lạy Chúa) | p000015 | đồng bộ ledger vol-01; không nâng canon |
| Tanya trong trần thuật | lặp tên/lược chủ ngữ (thay thế: «nó» theo DEC-P01-001; «cô») | nhiều đoạn (F6) | coordinator quyết định |
| HQ / Command | Bộ chỉ huy (cả hai, tạm) | p000019, p000002 | cần phân biệt nếu về sau xuất hiện cả hai |

## Rủi ro

- Lựa chọn đại từ cho Tanya trong LN02 (F6, F5) ảnh hưởng nhất quán toàn volume; cần coordinator chốt tạm một cách trước batch kế tiếp.
- Cách xưng hô/gọi God trong p000015 (F3) có thể liên quan đến tuyến Being X; giữ trung tính, không nâng canon.
- Khai triển FAC dựa trên một lần xuất hiện; có thể phải đổi khi xuất hiện thêm.

## YAML báo cáo

```yaml
role: reviewer
task_id: vol-02-ch-01-b01-review
state: done
segment_ids: [YS-LN02/Text/part0008.xhtml/p000001..p000020]
files_written: [reviews/prose/vol-02/ch-01-b01-claude.md]
validator: not_run
diff_check: not_run
review_path: reviews/prose/vol-02/ch-01-b01-claude.md
counts: {serious: 0, moderate: 6, minor: 11}
unresolved_findings: [F1, F2, F3, F4, F5, F6]
commit: null
next_action: translator_fix
```
