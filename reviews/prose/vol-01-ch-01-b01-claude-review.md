# Phản biện b01 — vol-01 Chapter 1 (19 đoạn)

Người phản biện: Claude. Task: `vol-01-ch-01-b01-review`. Mã đoạn viết tắt: `A/pNNNNNN` = `YS-LN01/Text/chapter003.xhtml/pNNNNNN`; `B/pNNNNNN` = `YS-LN01/Text/chapter003b.xhtml/pNNNNNN`. Báo cáo không chép câu nguồn; chỉ dùng mã đoạn và thuật ngữ nguyên gốc ngắn để nhận diện.

Đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, `handoffs/vol-01/review-ch-01-b01.yml`, `handoffs/vol-01/ch-01-b01.yml`, gói nguồn b01 (đọc tại chỗ), `translations/vol-01/ch-01-b01.jsonl`, `work/run-state/pending-terms.yml`, `reviews/prose/vol-01-ch-00-pending-decisions-claude.md`, `canon/*` (glossary/characters rỗng; decisions chỉ có DEC-P01-001/002; glossary-pending chỉ có mục ngữ cảnh ch-00).

**Tính chất:** mọi lựa chọn dưới đây là phương án tạm theo quy tắc ủy quyền trong AGENTS.md, không phải canon và không phải duyệt của người dùng. Không sửa bản dịch, canon, handoff hay sổ pending. Không có hard stop; không có quyết định ảnh hưởng cốt truyện. Validator/diff_check: not_run; commit: null.

## 1. Kiểm tra cấu trúc

- 19/19 đoạn có bản dịch, đúng thứ tự, `source_sha256` và `glossary_version` khớp handoff; `status: draft`.
- Nhấn mạnh (DEC-P01-002): nguồn có hai chỗ in nghiêng (A/p000002 cả câu; B/p000001 một từ). Bản dịch đánh dấu `*...*` đúng hai chỗ, không đánh thừa. Riêng phạm vi ở B/p000001 xem mục 2.
- Đại từ (DEC-P01-001): nội tâm tự quy chiếu dùng "mình" nhất quán; ngoại lệ ở B/p000009 (mục 2).
- Không có câu nguồn bị bỏ sót hay trùng; đơn vị "feet" giữ nguyên theo nguồn là chấp nhận được.

## 2. Phát hiện theo mã đoạn

Mức: nghiêm trọng 0, vừa 6, nhẹ 12.

### Vừa

1. **A/p000006 — tốc độ.** "Duy trì tốc độ bay ngang ổn định" sai hai chỗ: nguồn nói *ground speed* (tốc độ so với mặt đất) và sắc thái "thoải mái/vừa phải", không phải "ổn định"; "bay ngang" là thêm. **Đề xuất:** "tốc độ mặt đất vừa phải/thong thả". Tin cậy 0,75.
2. **A/p000008 — "spotter magician" + "vigilant".** Bản dịch "pháp sư trinh sát cảnh giới … tỉnh táo" dùng hai từ cho một tính từ và dịch *spotter* thành "trinh sát" (reconnaissance), lệch khỏi "quan sát viên pháo binh" ở A/p000006 cùng vai trò quan sát hiệu chỉnh pháo. **Đề xuất (tạm):** "pháp sư quan sát" + "cảnh giác" (một lần); thay thế: "pháp sư trinh sát". Tin cậy 0,6.
3. **B/p000001 — "đầy đặn".** Tính từ chỉ thể chất trời phú của cơ thể đời trước bị dịch thành "đầy đặn", gợi dáng nở nang/đẫy đà, đổi đặc điểm nhân vật. **Đề xuất:** "thể chất trời phú/được trời ưu ái", không tự suy ra cao lớn hay vạm vỡ. Tin cậy 0,75.
4. **B/p000003 — lệnh điều phối.** Nguồn yêu cầu tiến hành nhiệm vụ được giao; bản dịch thêm "khu vực" và hướng di chuyển ("tiến đến khu vực…"), mâu thuẫn với B/p000002 (đã tới vùng trời nhiệm vụ). **Đề xuất:** "Tiến hành nhiệm vụ được giao." Tin cậy 0,8.
5. **B/p000005 — "all clear".** "Thông thoáng" không phải cách báo cáo tình trạng khu vực; dễ đọc thành "không bị che chắn". Cũng cần phân biệt với B/p000010 (xác nhận bộ binh địch tiến), nên "an toàn" tuyệt đối có thể mâu thuẫn; nguồn không nêu rõ phạm vi (không phận hay mặt đất). **Đề xuất (tạm):** "Khu vực an toàn/không phát hiện địch", giữ nguyên lặp lại "xin nhắc lại"; thay thế: "khu vực thông suốt". Tin cậy 0,55; **không** tự thu hẹp thành "không phận".
6. **B/p000009 — "em ấy".** Đại từ thân mật gán quan hệ không có trong nguồn, lệch DEC-P01-001 (không suy ra quan hệ thân thuộc; tự quy chiếu là "mình"/trần thuật Tanya là "nó"). Đối tượng ở đây là bé gái nói chung. **Đề xuất:** "nếu còn dùng được thì … bé gái ấy" hoặc "đứa bé ấy"; tránh "em ấy". Tin cậy 0,75.

### Nhẹ

7. **A/p000001 — tiêu đề.** "Chiến khu" gợi căn cứ du kích trong tiếng Việt; *theater* là mặt trận/chiến trường. **Đề xuất:** "mặt trận Norden" hoặc "chiến trường Norden". "Niên hiệu Thống nhất" gợi niên hiệu vua chúa; tạm có thể "Năm Thống nhất 1923". Cả hai chưa vào sổ pending.
8. **A/p000002 — "bản ngã tỉnh táo … mang danh tính".** *Conscious self* gần "ý thức/bản thân có ý thức" hơn "bản ngã tỉnh táo" (khái niệm triết học khác); "mang danh tính" làm mất sắc thái *được gán cho*. **Đề xuất:** "ý thức của mình, được gán danh tính …". Giữ "thiếu úy ma pháp" (xem mục 3).
9. **A/p000005 — "công thức".** *Formulas* là hiện tượng siêu nhiên, không phải công thức toán; "công thức" dễ nhầm. **Đề xuất:** "thuật thức" (alt: "công thức"). Chọn tạm để nhất quán với "công thức bay" ở A/p000008. Tin cậy 0,5 (chưa có canon lore). Ngoài ra: (a) cụm nói về thân phận oái oăm bị làm nhẹ ("Trớ trêu thay" mất sắc thái bệnh hoạn/ác ý); (b) "khối cầu" và "quả cầu" đổi qua lại cho một vật, nên thống nhất "quả cầu".
10. **A/p000007 — "cô".** Xưng "cô" của đài kiểm soát giả định giới tính và lời gọi; DEC-P01-001 yêu cầu xét riêng. **Đề xuất:** lược đại từ ("Nghe rõ Fairy 08… theo dõi không gặp vấn đề") hoặc dùng "cô" như phương án tạm có ghi sổ. Không ảnh hưởng cốt truyện.
11. **B/p000001 — phạm vi nhấn mạnh.** "*thì*" làm chức năng đối chiếu chủ đề, trong khi nguồn nhấn mạnh sự khẳng định. **Đề xuất:** "mình *đúng là* bé xíu". "Kiếp trước" mang sắc thái luân hồi dân gian (ch-00 đã đổi "đầu thai" → "tái sinh" vì lý do tương tự); phương án tạm trung tính hơn: "đời trước" (alt: "kiếp trước"). Tin cậy 0,6.
12. **B/p000004 — "khác thường" / "kết luận hợp lý nhất".** Nghĩa đúng nhưng làm nhạt sắc thái mỉa mai khâm phục và "đến cùng logic". **Đề xuất:** "đúng là không ai bằng" / "đẩy đến tận cùng logic". "Người giám hộ" chấp nhận được.
13. **B/p000006 — "mật danh", "bình định".** *Call sign* là hô hiệu liên lạc, không phải mã bí mật; "mật danh" tạm chấp nhận nhưng phải dùng nhất quán (A/B p000008 cũng dùng). *Pacified* → "bình định" mang sắc thái chiến dịch lịch sử; tạm chấp nhận, alt: "dẹp yên/ổn định". Cả hai chưa có ở sổ pending (xem mục 3).
14. **B/p000006 vs B/p000008 — nguồn tự mâu thuẫn.** Đoạn 6 gọi Goliath 07 là tiểu đoàn bộ binh; đoạn 8 tự xưng là tiểu đoàn pháo binh của Quân đoàn Lâm thời. Bản dịch trung thực với từng đoạn; **không hòa giải**. Ghi vào sổ như rủi ro nguồn; đối chiếu bản gốc/các đoạn sau, không tự sửa.
15. **B/p000007 — "bóc lột".** *Exploit* ở đây là khai thác nhân lực; "bóc lột" nặng sắc thái ý thức hệ/lao động, thêm phán xét (style-guide). **Đề xuất:** "khai thác/vắt kiệt nhân lực". Giữ "Bộ Tổng Tham mưu" (chữ hoa nhất quán; alt: "Bộ Tổng tham mưu").
16. **B/p000010 — "âm điệu tỉnh bơ".** Gần sắc thái thờ ơ, trong khi nguồn là giọng báo cáo thực tế, đều đều. **Đề xuất:** "giọng điệu công vụ/khô khan". Câu "xác nhận bộ binh địch đang tiến lên" thêm tính tiến hành; chấp nhận được.
17. **Ghi chú `notes` lệch một đoạn (B/p000003 → B/p000010).** Ghi chú thuật ngữ của p000004, p000006, p000007, p000008, p000010 bị gắn vào đoạn trước; B/p000004 (artillery observer, guardian) và B/p000010 (matter-of-fact register) thiếu ghi chú đúng chỗ. Chỉ ảnh hưởng đối chiếu, không ảnh hưởng văn bản dịch.
18. **Chưa vào sổ pending.** Xem mục 3.

## 3. Thuật ngữ — đánh giá đề xuất của translator

| Thuật ngữ | Bản dịch | Đánh giá | Phương án tạm ưu tiên | Tin cậy |
|---|---|---|---|---|
| Magic Second Lieutenant | thiếu úy ma pháp | chấp nhận; alt "thiếu úy pháp sư" | giữ | 0,65 |
| computation orb | quả cầu tính toán | chấp nhận; alt "quả cầu diễn toán" | giữ, thống nhất "quả cầu" | 0,6 |
| formulas | công thức | cần xét | **thuật thức**; alt giữ "công thức" | 0,5 |
| magic engineering | kỹ thuật ma pháp | chấp nhận; alt "ma pháp công trình" | giữ | 0,55 |
| artillery observer | quan sát viên pháo binh | chấp nhận | giữ (cơ sở cho pháp sư quan sát) | 0,7 |
| spotter magician | pháp sư trinh sát cảnh giới | sửa (A/p000008) | **pháp sư quan sát**; alt "pháp sư trinh sát" | 0,6 |
| aerial mage | pháp sư không quân | chấp nhận | giữ | 0,7 |
| airspace control | bộ phận kiểm soát không phận | chấp nhận; alt "đài kiểm soát không phận" | giữ | 0,55 |
| General Staff | Bộ Tổng Tham mưu | chấp nhận | giữ | 0,75 |
| Provisional Corps | Quân đoàn Lâm thời | chấp nhận; alt "Quân đoàn Tạm thời" | giữ | 0,6 |
| Entente Alliance | Liên minh Entente | chấp nhận như tên riêng tạm | giữ | 0,6 |
| matter-of-fact register | âm điệu tỉnh bơ | cần xét | giọng điệu công vụ | 0,55 |
| previous life | kiếp trước | cần xét | **đời trước**; alt "kiếp trước" | 0,6 |

**Đề xuất bổ sung vào sổ pending (chưa có):** Unified Year (Niên hiệu/Năm Thống nhất), Norden theater (mặt trận Norden), Third Patrol Line (tuyến tuần tra thứ ba), Northern Military District (quân khu phía Bắc), Norden Control (giữ nguyên, alt "Đài kiểm soát Norden"), Fairy 08 / Goliath 07 (giữ nguyên), call sign (mật danh; alt "hô hiệu"), pacified (được bình định), guardian (người giám hộ), child soldier (binh sĩ trẻ em), quan hệ xưng hô đài–Tanya ("cô"), và rủi ro nguồn B/p000006–B/p000008.

Cấp bậc/tên riêng: Tanya Degurechaff giữ nguyên Latin; cấp bậc dùng "thiếu úy" nhất quán; không phát hiện tên hay cấp bậc bị đổi giữa các đoạn.

## 4. Nhất quán nội bộ b01

- "Mình" nhất quán cho nội tâm (ngoại lệ B/p000009). Người nói trong thoại vô tuyến dùng "Tôi" ở A/B p000002, p000010 — nhất quán.
- Thuật ngữ vô tuyến (rõ / nghe rõ tín hiệu / xác nhận / hết) nhất quán giữa A/p000004, p000007 và B/p000002–p000010.
- "Quân đội" cho *army* và *military* — nhất quán; "Lực lượng vũ trang" chỉ dùng ở B/p000011 cho *armed forces*.

## 5. Kết luận

Phản biện: không có lỗi nghiêm trọng; 6 lỗi vừa cần translator sửa (A/p000006, A/p000008, B/p000001, B/p000003, B/p000005, B/p000009); 12 lỗi nhẹ tùy chọn theo khuyến nghị. Các lỗi nhẹ liên quan đến thuật ngữ nên đi kèm cập nhật sổ pending do coordinator.

counts: {nghiêm_trọng: 0, vừa: 6, nhẹ: 12}
unresolved_findings: [A/p000006, A/p000008, B/p000001, B/p000003, B/p000005, B/p000009]
term_recommendations: [formulas→thuật thức, spotter magician→pháp sư quan sát, previous life→đời trước, call sign (mật danh), pacified, Norden Control, Unified Year]
