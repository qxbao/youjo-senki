# Báo cáo review — vol-01-ch-01-b05 (Claude)

- Task: `vol-01-ch-01-b05-review`; vai trò reviewer.
- Phạm vi: 21 đoạn `YS-LN01/Text/chapter003b.xhtml/p000055`–`p000075` (bên dưới viết tắt `pNNNNNN`).
- Đầu vào đã đọc: source package, `translations/vol-01/ch-01-b05.jsonl`, `canon/*`, `work/run-state/pending-terms.yml`, handoff review.
- Kiểm tra cơ học: sha256 source package khớp handoff (`b09c90b4…`); 21/21 đoạn, thứ tự và `segment_id` khớp giữa source và bản dịch. Validator/diff_check: `not_run`.
- Không có quyết định canon nào bị tự đặt; mọi lựa chọn thuật ngữ dưới đây là đề xuất tạm, chưa phải canon.

## Kết luận chung

Không có lỗi nghiêm trọng. Nghĩa, phủ định, mức chắc chắn và logic điều kiện/giả định được giữ tốt trên cả 21 đoạn. Còn **2 lỗi mức vừa** (đều là nhất quán thuật ngữ/sổ pending) và **một số lỗi nhẹ** về từ vựng, sắc thái. Không có mục nào ảnh hưởng cốt truyện cần hỏi người dùng. Có thể hoàn tất lô sau khi translator xử lý hai mục mức vừa.

## Kết quả theo các cờ rủi ro

| Cờ rủi ro | Kết quả |
|---|---|
| Nghĩa p000066 | Đạt, kèm nhắc nhẹ về sắc thái (F-05). Phần hedge "tôi cho rằng", phân biệt chế áp/vô hiệu hóa và quan hệ địch–bộ binh tan hàng được giữ. |
| Nghĩa p000070 | Đạt. Phủ định về thời tiết và nhiễu, nguyên nhân từ mỏ khoáng sản, mục đích nhắm tàn quân đều đúng. Có vài chỗ nên tinh chỉnh từ (F-07, F-08). Logic "nên… đâu phải…" ở mệnh đề thời tiết bám nguồn; xem mục 4 dưới đây. |
| Chú thích ⁵ | Đạt. Nguồn chỉ có **một** dấu chú thích trong lô, ở p000056 (sau tên sự kiện). Bản dịch có đúng một ⁵, ở p000056, đặt sau tên sự kiện. Các đoạn p000057–p000070 không có dấu chú thích trong nguồn và không bị thêm dấu thừa. Việc đánh số ⁵ tiếp nối ⁴ ở lô b02 (theo sổ pending). Nội dung chú thích không thuộc đầu vào được giao nên không đối chiếu được (xem F-01). |
| Nhấn mạnh (DEC-P01-002) | Đạt. Nguồn có đúng hai vùng in nghiêng: câu nội tâm cuối p000055 và câu nội tâm trong p000070. Bản dịch dùng `*…*` đúng hai chỗ, đúng phạm vi. Các câu nội tâm không nhấn mạnh (p000056, 061, 062, 071) không bị đánh dấu thêm. |
| Thuật ngữ mới | Xem F-01, F-02, F-03, F-04, F-10 và bảng đề xuất. |
| Đại từ (DEC-P01-001) | Nhìn chung đúng: trần thuật dùng "nó", nội tâm dùng "mình". Một chỗ cần xem lại: F-06. |

## Phát hiện

### Mức vừa

**F-01 · p000058 — "Hỏa lực đạt hiệu quả tốt trên mục tiêu" lệch thuật ngữ đã chọn ở b02.**
- Vấn đề: b02 (review Claude, `b02-fire-for-effect`) đã chọn "bắn hiệu lực" và thay thế rõ ràng "bắn hiệu quả". Báo cáo "good effect" là phần báo kết quả của chính loạt bắn hiệu lực đó, nên nên dùng cùng gốc "hiệu lực". Bản dịch quay lại "hiệu quả".
- Căn cứ: `pending-terms.yml` mục `b02-fire-for-effect` và `b02-fire-for-effect-terminology`; p000058 là phần "good effect" lặp hai lần trong báo cáo kết quả bắn (p000057 đã yêu cầu "kết quả bắn").
- Đề xuất: "Hiệu lực tốt trên mục tiêu. Tôi nhắc lại, hiệu lực tốt." Không cần thêm "Hỏa lực"; nếu giữ thì vẫn nên là "hiệu lực". Giữ nguyên ý: đánh giá hiệu quả, không suy ra tiêu diệt hoàn toàn (translator đã ghi đúng điều này).
- Độ tin cậy: 0,6 (thuật ngữ pháo binh Việt thường dùng "hiệu lực" cho "effect" trong "bắn hiệu lực"; phương án "hiệu quả" vẫn hiểu được).
- Ghi sổ: mục này chưa có trong `pending-terms.yml` (xem F-10).

**F-02 · p000066, p000068 — "chế áp" lệch sổ pending ("áp chế").**
- Vấn đề: sổ pending (`b05-suppressive-fire`, độ tin cậy 0,8) chọn "hỏa lực áp chế", "hỏa lực chế áp" chỉ là phương án khác. Bản dịch và ghi chú dùng "chế áp" làm phương án chính ("hỏa lực chế áp", "dẫn bắn chế áp"). Hai bên đang đảo vai trò nên không truy vết được và translator không áp dụng phương án tạm hiện hành.
- Căn cứ: `chapter1_b05_translator_terms`, mục `b05-suppressive-fire`; ghi chú p000066 của translator.
- Đề xuất: thống nhất một phương án. Đề xuất của reviewer: **"hỏa lực áp chế"** (p000066) và **"dẫn bắn áp chế"** (p000068), vì "áp chế" là cách nói quen thuộc hơn trong văn bản quân sự tiếng Việt và khớp sổ. Nếu coordinator muốn giữ "chế áp" thì phải sửa sổ pending cho khớp. Chọn một, dùng nhất quán ở cả hai đoạn.
- Độ tin cậy: 0,7.

### Mức nhẹ

**F-03 · p000056 — tên sự kiện Fuji và chú thích ⁵.**
- Giữ dấu ⁵ ngay sau tên sự kiện là đúng. Tên "buổi trình diễn hỏa lực Fuji" là dịch sát, chấp nhận được.
- Lưu ý: "Review" trong nguồn có thể hướng về "thao diễn/duyệt" hơn là "trình diễn"; nội dung chú thích (`footnote.xhtml`, mục fn0005) không thuộc đầu vào được giao nên chưa thể chốt. Giữ phương án hiện tại và đối chiếu chú thích khi có quyền đọc. Không suy diễn sự kiện thật. Độ tin cậy: 0,6. Phương án khác: "cuộc thao diễn hỏa lực Fuji".
- "lời thì thầm chỉ nghĩ đến bản thân của nó" hơi nặng nề; có thể gọn hơn là "lời thì thầm toàn nghĩ cho bản thân" (không đổi nghĩa; tùy chọn).

**F-04 · p000059, p000067 — "khẩu đội" có thể sai quy mô cho "batteries".**
- Trong tiếng Việt, "khẩu đội" thường là tổ phục vụ một khẩu pháo (cấp rất nhỏ), còn "battery" thường tương ứng "pháo đội" hoặc "đơn vị pháo". Bản dịch p000067 còn nói "các khẩu đội… xuất sắc… loạt pháo kích", dễ gây hiểu quy mô nhỏ hơn nguồn.
- Đề xuất: **"pháo đội"** (độ tin cậy 0,6); phương án trung tính hơn: "các đơn vị pháo binh" (0,55). "khẩu đội" nên hạ xuống phương án khác (0,4). Đồng bộ p000059 và p000067.
- Không thuộc lớp quyết định cốt truyện.

**F-05 · p000066 — sắc thái "chúng" trong báo cáo vô tuyến; "tan đội hình".**
- "Tôi cho rằng chúng ta đã vô hiệu hóa chúng" dùng đại từ "chúng" cho địch trong một báo cáo công vụ, nghe suồng sã hơn nguồn; "địch" đã được dùng ở các câu bên cạnh và hợp giọng công vụ hơn (xem `P01-matter-of-fact-register`). Đề xuất: "…đã vô hiệu hóa địch" hoặc "…đã vô hiệu hóa lực lượng đó".
- "tan đội hình" tự nhiên hơn là "tan hàng" hoặc "vỡ đội hình" (tùy chọn).
- Về cờ nghĩa p000066: các điểm cốt lõi đều đúng, không có lỗi nghĩa. Giữ "vô hiệu hóa" (độ tin cậy 0,7; phương án khác "làm mất khả năng chiến đấu", 0,6).
- Ngoài ra, "chúng" xuất hiện cho binh sĩ địch ở p000065 và p000067 trong trần thuật; chấp nhận được theo DEC-P01-001 mở rộng cho số nhiều, nhưng nếu muốn tránh sắc thái miệt thị thì lược chủ ngữ hoặc dùng "đám bộ binh đó". Mức nhẹ, không bắt buộc.

**F-06 · p000059 — "kéo mình xuống" trong trần thuật.**
- "mình" được dành cho nội tâm tự quy chiếu (DEC-P01-001). Ở đây là trần thuật ngôi ba nên "mình" (đại từ phản thân) dễ bị đọc như nội tâm. Đề xuất: "nặng trĩu đè lên nó" hoặc "kéo nó xuống" (hoặc lược). Độ tin cậy: 0,7.

**F-07 · p000060 — "chẳng phải chỉ là giấc mơ viển vông." thiếu dấu hỏi / dễ hiểu sai.**
- Dạng "chẳng phải… ." không có "sao?" nghe như câu hỏi tu từ bị cụt, hoặc đọc thành phủ định lơ lửng. Nguồn là câu khẳng định phủ định.
- Đề xuất: "…không chỉ là giấc mơ viển vông." Nghĩa giữ nguyên.
- Cũng nên kiểm tra "bộ phận nhân sự" ở p000060: nguồn viết hoa như tên cơ quan; nếu các lô trước (b01–b04) đã dùng một tên cụ thể cho cơ quan này thì cần đồng bộ (không có căn cứ trong phạm vi đọc để chốt).

**F-08 · p000070 — một số điểm từ vựng.**
- "gần như trở nên lố bịch": "lố bịch" có sắc thái chê/xấu hổ mạnh hơn "ridiculous"; nên giảm nhẹ ("đến mức gần như vô lý/đáng cười"). Độ tin cậy 0,65.
- "đủ để gọi là “rõ”": nguồn chỉ nói mức nhiễu có thể gọi là mức "clear"; "đủ để" thêm ý đủ điều kiện/đạt ngưỡng. Hơn nữa "rõ" trong lô này còn là "roger" (p000066, 068, 069…), nên dấu ngoặc "rõ" dễ nhầm với lời đáp; cân nhắc "rõ nét"/"trong" (ví dụ gọi là mức “trong”). Độ tin cậy: 0,55.
- "điềm nhiên" cho "dispassionate": nghiêng về bình thản, trong khi nguồn là "khô khan/thuần công vụ". Cân nhắc "khô khan, công vụ" (tùy chọn).
- "bộ phận kiểm soát" cho "Control": đây là cách gọi rút gọn của Norden Control, nhưng b01 đã dùng "bộ phận kiểm soát không phận" cho một thực thể khác ("airspace control"), dễ gây nhầm. Đề xuất: giữ "Norden Control" ở p000070 (hoặc "đài kiểm soát" nếu coordinator chọn phương án đó). Độ tin cậy 0,6.
- "bộ vô tuyến hàng không" cho "airman radio set": hợp lệ nhưng "hàng không" gợi hàng không dân dụng; phương án khác "bộ vô tuyến dành cho không quân/phi công". Độ tin cậy 0,55; không nên suy ra kiểu thiết bị.

**F-09 · p000070 — mệnh đề thời tiết: xác nhận, không cần sửa nghĩa.**
- Phủ định "đâu phải thời tiết sẽ cản trở địch gây nhiễu" khớp nguồn, và chuỗi "bầu trời u ám… nên…" giữ đúng dạng của câu gốc (không đảo thành "thời tiết gây nhiễu"). Quan hệ nhân quả "nên" trong câu nguồn hơi lỏng, nên Vietnamese cũng lỏng; đừng "sửa cho thuận" bằng cách đổi logic. Có thể làm câu dễ đọc hơn bằng "nên cũng chẳng phải thời tiết sẽ cản trở địch gây nhiễu tín hiệu". Độ tin cậy giữ nghĩa: 0,8.
- "đến tận nơi đôi mắt xanh của nó có thể nhìn thấy" hơi gượng; tùy chọn: "tới tận chân trời trong tầm mắt xanh của nó".

**F-10 · Sổ pending thiếu mục cho các đề xuất mà translator đã nêu.**
- Có trong ghi chú bản dịch nhưng **không** có trong `chapter1_b05_translator_terms`: `b05-fuji` (p000056), `b05-good-effect` (p000058), `b05-batteries` (p000059, p000067), `b05-central-command` (p000059), `b05-rear-echelon` (p000060). Ngoài ra mã `b05-airman-radio`/`b05-control-air` trong ghi chú khác với `b05-airman-radio-set`/`b05-control-of-the-air` trong sổ. Coordinator nên bổ sung/đồng bộ mã.

**F-11 · p000074 — "Hết" cho "Over".**
- "Hết" đúng cho "Over" trong quy trình vô tuyến nhưng dễ bị hiểu thành "Out/kết thúc". Translator đã ghi không suy thành kết thúc liên lạc. Chấp nhận; kiểm tra lại cách dùng ở b01–b04 để đồng bộ. Độ tin cậy: 0,5.

## Những điểm đã kiểm tra và đạt

- p000055, 057, 063, 064, 069, 072, 073, 075: nghĩa, hô hiệu, thể thức vô tuyến đúng; "Nghe to và rõ", "điểm đạn rơi" giữ đúng phạm vi.
- p000061–062: giọng nội tâm "mình" đúng; không thêm in nghiêng; ý thư cảm ơn kèm tình hình mới nhất và mục đích xây dựng quan hệ giữ đúng.
- p000065, 067: điều kiện "một khi pháo binh đã triển khai", mức tăng tiến "càng… nếu địa thế…", chuyển từ ngay ngắn sang tán loạn, "chỉ phí đạn" giữ đúng; "lựu pháo", "dữ liệu đạn đạo" ổn.
- p000071: giả định ngược về việc đã chọn bắn quét, phép so sánh chim dodo/gà tây giữ nguyên hình ảnh, không giải thích thêm; "quyền chọn trước", "làm chủ bầu trời" không thêm mức tuyệt đối.
- Nhân vật/xưng hô: không có nhân vật mới cần canon; không có tên nhân vật mới ngoài hô hiệu.

## Đề xuất thuật ngữ (đều pending, không phải canon)

| source_term | đề xuất VI | khác | độ tin cậy | segment |
|---|---|---|---|---|
| Fuji Firepower Review | buổi trình diễn hỏa lực Fuji⁵ | cuộc thao diễn hỏa lực Fuji | 0,6 | p000056 |
| good effect | hiệu lực tốt (trên mục tiêu) | hiệu quả tốt | 0,6 | p000058 |
| suppressive fire | hỏa lực áp chế | hỏa lực chế áp | 0,7 | p000066, p000068 |
| neutralized | vô hiệu hóa | làm mất khả năng chiến đấu | 0,7 | p000066 |
| batteries | pháo đội | các đơn vị pháo binh; khẩu đội (0,4) | 0,6 | p000059, p000067 |
| Central Command | Bộ Tư lệnh Central | Bộ Tư lệnh Trung ương | 0,5 | p000059 |
| rear echelon | hậu phương | tuyến sau | 0,55 | p000060 |
| Personnel | bộ phận nhân sự | cơ quan nhân sự | 0,6 | p000060 |
| howitzers | lựu pháo | pháo lựu | 0,85 | p000067 |
| ballistics data | dữ liệu đạn đạo | số liệu đạn đạo | 0,85 | p000067 |
| primary infantry | lực lượng bộ binh chủ lực | bộ binh chính | 0,6 | p000068 |
| airman radio set | bộ vô tuyến hàng không | bộ vô tuyến dành cho không quân/phi công | 0,55 | p000070 |
| Control (rút gọn) | Norden Control | đài kiểm soát Norden | 0,6 | p000070 |
| dodoes | chim dodo | chim đô đô | 0,7 | p000071 |
| strafe | bắn quét | bắn càn từ trên không | 0,75 | p000071 |
| control of the air | làm chủ bầu trời | kiểm soát không phận | 0,75 | p000071 |
| Over (vô tuyến) | Hết | — | 0,5 | p000074 |

Không có mục nào ảnh hưởng cốt truyện hoặc cần hỏi người dùng.

## Trạng thái

- Lỗi nghiêm trọng: 0. Lỗi vừa: 2 (F-01, F-02). Lỗi nhẹ: 9 (F-03–F-11).
- Điều kiện hoàn tất lô: translator xử lý F-01 và F-02 (hoặc coordinator đồng bộ sổ pending cho F-02), sau đó validator/diff_check.
