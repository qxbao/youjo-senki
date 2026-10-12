# Báo cáo review vol-02-ch-01-b02 (Claude, văn phong/nghĩa/thuật ngữ)

- Task: `vol-02-ch-01-b02-review`; lô gồm 25 đoạn, từ `YS-LN02/Text/part0010.xhtml/p000001` đến `p000025`.
- Đầu vào đã dùng: handoff `handoffs/vol-02/ch-01-b02.yml`, source package cục bộ (SHA-256 khớp `80d9766c…d7d938`), `canon/` và `work/run-state/pending-terms.yml`, bản dịch `translations/vol-02/ch-01-b02.jsonl` (25/25 đoạn, trạng thái `draft`).
- Không sửa bản dịch, canon, handoff, package hay checkpoint. Mọi thuật ngữ dưới đây chỉ là đề xuất, không phải canon. Mã đoạn viết tắt `pNNNNNN` thuộc `YS-LN02/Text/part0010.xhtml/`.
- Phạm vi kiểm: nghĩa, chủ thể, phủ định, trình tự thời gian, thuật ngữ quân sự, văn phong, nhấn mạnh.

## Kết luận tổng quát

Bản dịch bám sát nghĩa, đủ 25 đoạn, không sót hay thêm ý lớn. Phủ định, câu hỏi tu từ, quan hệ "không chỉ… mà còn" (p000019) và chuỗi diễn biến báo động → hủy diễn tập → lệnh cầm chân → quyền tùy nghi đều đúng thứ tự. Nguồn không có nhấn mạnh in nghiêng nên việc không dùng `*...*` là đúng theo DEC-P01-002. Còn 3 lỗi mức vừa cần sửa trước khi nâng chuẩn và một số lỗi nhẹ.

Kiểm tra riêng:
- Phủ định/hạn định: p000012, p000017, p000019, p000022 đúng.
- Thời gian: p000010 và p000018 có chỗ giả định/quá khứ cần chỉnh (xem F4); các đoạn còn lại ổn.
- Nhấn mạnh: nguồn không có thẻ nhấn mạnh; bản dịch không thêm. Đạt.
- Ký hiệu chú thích ở p000024: xem F14.

## Phát hiện

### Mức vừa

**F1 — p000006 — đổi đối tượng của thông tin.**
- Căn cứ: nguồn nói nhân viên chỉ huy muốn lấy thông tin *về* một đồn khác; bản dịch viết "hỏi tin tức *từ* đồn khác", chuyển đồn thành nguồn cung cấp tin.
- Đề xuất: sửa thành "hỏi tin tức về đồn khác" (hoặc "hỏi tình hình của đồn khác").

**F2 — p000025 — thu hẹp phạm vi "mọi đánh giá" thành "mọi người".**
- Căn cứ: nguồn nói đó là chuẩn của mọi lần đánh giá (chuẩn tối thiểu của chỉ huy và thước đo chung); bản dịch viết "tiêu chuẩn để đánh giá mọi người", đổi đối tượng thành con người.
- Đề xuất: "…đồng thời là tiêu chuẩn cho mọi đánh giá" (hoặc "mọi lần đánh giá").

**F3 — p000010, p000016, p000018, p000025 (và p000012 ở lời thoại) — đại từ chỉ Tanya/Lergen lệch khỏi quy ước hiện hành.**
- Căn cứ: DEC-P01-001 dùng "nó" cho trần thuật về Tanya và cấm suy ra tuổi/giới/quan hệ từ một đoạn; đề xuất reviewer vol-02-b01 (ledger, chưa canon) là lặp tên "Tanya"/bỏ chủ ngữ và tránh "cô"; với Lergen là lặp tên hoặc bỏ chủ ngữ, tránh suy tuổi. Bản dịch dùng "cô" ở p000010 (3 lần), p000016, p000018 ("cô đã điều tra", "tiểu đoàn cô"), p000025 ("cô được toàn quyền", "hồ sơ của cô"), và "Ông" cho Lergen ở p000010. Ngoài ra p000012 dùng "Cô" gọi trực tiếp Tanya sau khi vừa gọi "Thiếu tá", chưa có canon xưng hô.
- Đề xuất: thay bằng "Tanya"/"Lergen" hoặc bỏ chủ ngữ khi không mơ hồ; "tiểu đoàn cô" → "tiểu đoàn của Tanya"; p000012 lặp "Thiếu tá" hoặc dùng cách gọi trung tính. Nếu coordinator chốt dùng "cô" cho LN02 thì áp dụng nhất quán cả lô; hiện chưa có quyết định.

### Mức nhẹ

**F4 — p000010 — giả định quá khứ bị làm phẳng.** Nguồn là mong muốn trái thực tế (lẽ ra đã muốn có cơ hội làm tùy viên/sĩ quan liên lạc nhưng không có); "cô đã muốn có cơ hội" đọc như nguyện vọng có thật trong quá khứ. Đề xuất: "lẽ ra cô đã muốn/đã mong có cơ hội…" (đổi chủ ngữ theo F3). Cùng đoạn: "hình dung rõ hơn cần cho nổ tung những gì" gượng, đề xuất "hình dung rõ hơn những thứ cần cho nổ tung"; "rồi hơi cau mày" biến hai việc đồng thời thành nối tiếp, cân nhắc "vừa… vừa…".

**F5 — p000001 — "useful expedient" thành "dịp thuận tiện".** Nguồn là biện pháp/phương tiện tạm thời hữu ích, không phải cơ hội; đề xuất "biện pháp tiện dụng" (hoặc "cách tạm thời hữu ích"). "đề phòng Dacia" cũng nặng hơn "để mắt tới/lưu ý Dacia" (chưa có ý phòng thủ).

**F6 — p000003 — ba chỗ lệch nhỏ.** (a) "The Dacians" bị thu hẹp thành "Quân Dacia"; nguồn chỉ người Dacia/quốc gia nói chung, đề xuất "người Dacia" hoặc "phía Dacia". (b) "half expects" → "gần như chờ sẵn" mạnh hơn nguồn (chỉ nửa mong đợi); đề xuất "đoán chừng sẽ nhận…". (c) "hoàn toàn không biết phải làm sao" chệch sang bí; nguồn là hoang mang, không hiểu nổi; đề xuất "hoàn toàn không hiểu nổi/bối rối". Đồng thời "combat maneuvers" mất "chiến đấu"; có thể giữ "diễn tập chiến đấu".

**F7 — p000002 — "freely throwing its weight around" thành "phô trương sức mạnh".** Nguồn nói về thói lấn lướt, ỷ thế; "phô trương" nghiêng về khoe khoang. Đề xuất "thói ỷ thế lấn lướt".

**F8 — p000008, p000005 — thuật ngữ đơn vị và định dạng số.** "Hạm đội Không quân" mang sắc thái hải quân trong tiếng Việt (xem mục thuật ngữ); số hiệu viết "số 7" ở đây nhưng "203" không có "số" ở p000005; nên thống nhất. "báo cáo chiến trường" chấp nhận được; "theater" có thể là mặt trận/khu vực tác chiến.

**F9 — p000012 — thêm nội dung.** "làm nhiệm vụ cầm chân địch" thêm "nhiệm vụ" và "địch"; nguồn chỉ nói sẽ cầm chân (kẻ địch được hiểu ngầm) cho phía mình. Đề xuất "Cô sẽ cầm chân chúng cho chúng tôi" (đại từ theo F3).

**F10 — p000011 — "bolt from the blue" bị làm phẳng.** "bất ngờ" mất độ đột ngột và giọng mỉa của Tanya (Lergen đáp lại bằng "mỉa mai"); đề xuất giữ hình ảnh như "sét đánh giữa trời quang".

**F11 — p000013 — hai chỗ.** (a) "garrison" dịch "đồn", trùng với "post" ở p000006; đề xuất "doanh trại/đơn vị đồn trú". (b) "trực thuộc quyền chỉ huy trực tiếp" thừa; đề xuất "chịu quyền chỉ huy trực tiếp của…". Xem thêm thuật ngữ General Staff Office.

**F12 — p000016 — "isn't about to be underestimated".** Nguồn là Tanya không định để mình bị coi thường (ý chí); "đâu dễ bị xem thường" là nhận xét về mức dễ. Đề xuất "Tanya không định để bị xem thường".

**F13 — p000019 — "I'm sure" thành "Tôi nghĩ".** Nguồn tự tin hơn; đề xuất "Tôi chắc rằng". Mức độ chắc chắn là một phần của giọng Tanya.

**F14 — p000024 — ký hiệu chú thích.** Nguồn có dấu chú thích số 1 (liên kết note cuối sách); bản dịch giữ "¹", hợp lý để đối chiếu, nhưng style-guide yêu cầu ghi vào `decisions.md` mọi lựa chọn về chú thích trước khi áp dụng thống nhất. Đề xuất: coordinator ghi quyết định định dạng; chưa cần sửa bản dịch. Nội dung chú thích nằm ngoài lô nên không đánh giá.

**F15 — p000022 — "national guard reserves".** "lực lượng dự bị vệ binh quốc gia" đọc vướng, thứ tự yếu tố đảo. Đề xuất "lực lượng vệ binh quốc gia dự bị" hoặc "dự bị của vệ binh quốc gia".

**F16 — p000025 — mất "rough".** "rough gathering of picnickers" bị bỏ sắc thái tạp nham; đề xuất "một đám người tụ tập đi dã ngoại lộn xộn". "Đạo quân trang bị đầy đủ" vẫn ổn.

**F17 — p000018, p000019, p000022 — đại từ "chúng" chỉ quân Dacia.** Nguồn trung tính ("them"); "chúng" thêm sắc thái miệt thị. Hợp giọng Tanya nhưng chưa có canon; nếu muốn an toàn dùng "họ"/"quân Dacia" ở lời kể, giữ "chúng" ở nội tâm nếu coordinator chấp nhận. Đồng thời p000018 "so-called minor nation" → "được xem là" làm mất sắc thái "cái gọi là"; đề xuất "cái gọi là nước nhỏ" hoặc "kiểu nước nhỏ".

## Đề xuất thuật ngữ tạm (không canon)

Mục "mới" là thuật ngữ ledger chưa có. Độ tin cậy là ước lượng.

| Thuật ngữ nguồn | Đề xuất tạm | Đoạn | Tin cậy | Ghi chú / phương án khác |
|---|---|---|---|---|
| Border Command | Bộ chỉ huy Biên phòng (giữ) | p000005 | 0.5 | "Biên phòng" gợi lực lượng bộ đội biên phòng; thay thế "Bộ chỉ huy Biên giới". Nhất quán với đề xuất vol-01 `b02-border-army` (quân đội biên phòng). p000006 "Command personnel" là cơ quan chỉ huy tại chỗ, nên dịch khác Border Command để khỏi nhầm. |
| Seventh Air Fleet | Hạm đội Không quân 7 (giữ nghĩa đen, bỏ "số" cho khớp "Tiểu đoàn 203") | p000008 | 0.4 | Thiếu chứng cứ về cấp tổ chức. Phương án khác: Tập đoàn quân Không quân 7; Binh đoàn Không quân 7. Không ảnh hưởng cốt truyện. |
| Command Post | Sở chỉ huy (giữ) | p000008 | 0.7 | Dùng "Bộ chỉ huy" cho Command/HQ (ledger b01), "Sở chỉ huy" cho Command Post; giữ phân biệt. Khác: Trạm chỉ huy. |
| General Staff Office | Văn phòng Bộ Tổng tham mưu (đổi) | p000013 | 0.45 | "Cục" gợi một cục chức năng cụ thể, nguồn không có; "Office" dịch nghĩa đen là văn phòng. Khác: Cục Bộ Tổng tham mưu (đề xuất hiện tại); "Bộ Tổng tham mưu" nếu cùng thực thể với General Staff trong cùng đoạn. Viết hoa thống nhất theo ledger (Bộ Tổng Tham mưu hay Tổng tham mưu cần chọn một). |
| regional army group | Cụm tập đoàn quân khu vực (giữ) | p000019 | 0.5 | "Cụm tập đoàn quân" là đối ứng quen thuộc của army group. Khác: Cụm quân khu vực. |
| Korean People's Army | Quân đội Nhân dân Triều Tiên (giữ) | p000022 | 0.65 | Tên riêng thực tế, ít mơ hồ. |
| Principality (mới) | Công quốc | p000017, p000018 | 0.7 | Chỉ Dacia (p000018). Khác: không có phương án thay thế được hỗ trợ. |
| Boy Scouts / Boy Scout troop (mới) | Hướng đạo sinh / toán Hướng đạo sinh | p000016, p000018, p000021 | 0.7 | Mất "Boy"; không ảnh hưởng nghĩa. Khác: đội Hướng đạo. |
| Turao Field Maneuver Area (mới) | Khu thao trường Turao | p000001 | 0.5 | Khác: Bãi diễn tập dã chiến Turao. |
| Two hundred and third (mới) | Tiểu đoàn 203 | p000005 | 0.7 | Nguồn chỉ nêu số; "tiểu đoàn" suy từ p000013. Chấp nhận, ghi là suy luận từ ngữ cảnh. |
| Central (mới) | khu vực trung tâm (đổi) | p000015 | 0.4 | "miền Trung" gán sang địa lý cụ thể; nguồn có thể là vùng hoặc cấp chỉ huy trung tâm. Khác: miền Trung; Trung ương. Không ảnh hưởng cốt truyện nhưng nên theo dõi cách dùng ở LN02 sau. |
| Lieutenant (Weiss, Serebryakov) (mới) | Trung úy | p000007, p000009 | 0.6 | Cấp bậc cụ thể (thượng/trung/thiếu úy) chưa đủ chứng cứ; giữ "Trung úy" trung tính, nhất quán trong lô. |
| national guard reserves (mới) | lực lượng vệ binh quốc gia dự bị | p000022 | 0.5 | Khác: lực lượng dự bị quốc gia. |
| Tanya trong trần thuật | lặp tên "Tanya" hoặc bỏ chủ ngữ | p000010, p000016, p000018, p000025 | 0.6 | Theo đề xuất b01 và DEC-P01-001 (trần thuật "nó"); xem F3. |
| Lergen trong trần thuật | lặp "Lergen" hoặc bỏ chủ ngữ | p000010, p000018 | 0.55 | Không dùng "Ông" để khỏi suy tuổi. |

Không có thuật ngữ nào trong lô ảnh hưởng cốt truyện cần hỏi người dùng.

## Rủi ro

- Chuẩn xưng hô cho Tanya/Lergen ở LN02 chưa được chốt; mỗi lô dùng một kiểu sẽ lệch nhau.
- Bộ ba Bộ chỉ huy / Bộ chỉ huy Biên phòng / Sở chỉ huy dễ bị nhầm nếu về sau không giữ phân biệt.
- "Hạm đội Không quân" có thể bị hiểu là hải quân.
- Cách ghi chú thích chưa có quyết định canon.
- Validator và diff-check chưa chạy trong task này.

## Đề xuất bước tiếp

Chuyển báo cáo cho người giữ quyền sửa (translator) để xử lý F1–F3 bắt buộc, F4–F17 tùy mức; coordinator cập nhật ledger pending và ghi quyết định định dạng chú thích; sau sửa chạy validator và review lại các đoạn đã đổi.
