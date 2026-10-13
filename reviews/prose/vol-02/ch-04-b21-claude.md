# Báo cáo review vol-02-ch-04-b21 (Claude)

- Phạm vi: 34 đoạn, từ `YS-LN02/Text/part0024.xhtml/p000278` đến `p000311`. Mã đoạn dưới đây viết tắt `pNNNNNN`.
- Đầu vào đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b21, source package b21, canon (`style-guide.md`, `decisions.md` DEC-P01-001/002, `glossary.yml`, `characters.yml`, `glossary-pending.yml`), mục `chapter4_b21_translation_proposals` trong `pending-terms.yml`, bản dịch b21.
- Không đọc lô khác. Vì vậy chưa đối chiếu được độ nhất quán với sổ pending hay bản dịch của các lô khác.
- `glossary.yml` và `characters.yml` đang trống. Mọi thuật ngữ, xưng hô và cấp bậc dưới đây là đề xuất, không phải canon.
- Validator/diff-check: not_run. Commit: null.

## Kết luận tổng

- Không có lỗi nghiêm trọng.
- Có 4 lỗi vừa (p000288, p000294, p000295, p000298). Cả bốn đều là lỗi nghĩa hoặc logic do cách dùng từ, nên cần translator sửa trước khi lô được tính hoàn tất.
- Có 8 lỗi nhẹ, không chặn lô.
- Dấu nhấn mạnh: nguồn có đúng hai chỗ in nghiêng (p000284, p000295). Bản dịch có `*...*` ở đúng hai chỗ này, đúng phạm vi, theo DEC-P01-002. Không thêm hay thiếu.
- Không phát hiện đoạn bị bỏ sót hay thêm ý lớn. Số đoạn khớp (34/34).

## Lỗi vừa

### M1 — p000288: đảo chiều logic của câu giả định
- Vấn đề: nguồn nói lý lẽ không phải là tất cả. Nếu lý lẽ là tất cả thì thế giới đã là Utopia, và thiên đường nơi trần thế không tồn tại chứng tỏ điều ngược lại. Bản dịch viết "Nếu đúng vậy, thế giới hẳn đã thành Utopia". Câu liền trước là câu phủ định ("lý lẽ không phải điều duy nhất quan trọng"), nên "đúng vậy" trỏ về chính phủ định đó. Câu giả định bị đọc ngược: nếu lý lẽ không phải điều duy nhất thì thế giới đã là Utopia.
- Căn cứ: style-guide giữ nguyên quan hệ điều kiện và logic, và giữ tính giả định phản thực.
- Đề xuất: viết rõ vế giả định, ví dụ "Nếu chỉ cần lý lẽ là đủ, thế giới hẳn đã là Utopia, còn việc ... không tồn tại cho thấy rõ lập trường của họ."

### M2 — p000294: "để mất những con tàu" chệch nghĩa
- Vấn đề: nguồn nói mất dấu các con tàu, tức không còn theo dõi được, phù hợp với mạch tìm kiếm trên biển ở p000278–p000279. "Để mất những con tàu" dễ hiểu là mất tàu, tức bị đánh chìm hoặc mất quyền sở hữu.
- Đề xuất: "một khi đã mất dấu những con tàu đó".

### M3 — p000295: chủ thể "Họ đang cố làm nản lòng..." bị đảo
- Vấn đề: ở nguồn, người đang cố dập tắt ý chí kháng cự ở thời điểm này là phía Đế quốc. Trong bản dịch, câu liền trước có chủ ngữ "Kẻ địch có thể nói: ...", nên "Họ" tự nhiên trỏ về kẻ địch. Như vậy chủ thể bị đảo và lý do vấn đề trở thành "đau đầu" bị hiểu sai.
- Đề xuất: nêu chủ thể rõ, ví dụ "Đế quốc đang cố dập tắt ý chí kháng cự vào thời điểm này, nên..."
- Lưu ý: "họ" trong "thuyết phục họ đầu hàng" cũng có thể trỏ về đoàn tàu hoặc Liên minh Entente. Nên chọn một chủ thể cụ thể. Chứng cứ nguồn chưa đủ để chắc chắn; chọn cách ít suy diễn nhất.

### M4 — p000298: "Mất một hai con tàu" sai nghĩa
- Vấn đề: "missing" ở nguồn là bắn hụt hoặc để sót, tức không đánh chìm được. Bản dịch viết "Mất một hai con tàu thì còn đành". "Mất" dễ bị hiểu là phía Đế quốc mất tàu của mình.
- Đề xuất: "Để sót một hai con tàu thì còn chấp nhận được, đằng này họ đã để chúng trốn thoát."

## Lỗi nhẹ

- **L1 — p000280, p000287: "các anh" / "anh"**. Nguồn dùng "you" trung tính. Bản dịch chọn "các anh" (số nhiều, nam) ở p000280 và "anh" ở p000287. Theo DEC-P01-001, không suy ra giới tính hay quan hệ từ ngữ cảnh mỏng. Đề xuất tạm giữ vì đây là cách xưng hô quân đội thông dụng. Ghi pending về xưng hô cho hai đoạn này, nếu cần dùng "các vị"/"ông".
- **L2 — p000290: hai "họ" liên tiếp có chỉ tố khác nhau**. Câu đầu "họ" là các con tàu, câu sau "họ" là Khối Thịnh vượng chung. Đề xuất thay câu sau bằng "nước này" hoặc nêu tên.
- **L3 — p000304: "nung nấu"**. Nguồn là "festered", nghĩa là âm ỉ thối rữa, tiêu cực. "Nung nấu" thường mang sắc thái quyết tâm hoặc ấp ủ, lệch sắc thái. Đề xuất "âm ỉ ủ men" hoặc "âm ỉ thối rữa".
- **L4 — p000304 / p000309: "cơn điên" và "sự điên loạn"**. Cùng khái niệm "madness" nhưng hai cách dịch khác nhau, trong khi p000305 dùng "điên loạn". Đề xuất thống nhất "sự điên loạn".
- **L5 — p000305: "tất cả những gì bạn có thể làm là cố cưỡng lại"**. Nguồn nhấn rằng cưỡng lại đã là hết sức. Bản dịch nghe như chỉ còn mỗi việc cố gắng. Ngoài ra "bạn" khá lạc giọng trong văn kể. Đề xuất "chỉ riêng việc cưỡng lại ánh nhìn mê hoặc ấy cũng đã là hết sức" hoặc dùng chủ ngữ chung "người ta". "Gieo mầm" cũng thêm ẩn dụ thực vật không có trong nguồn; có thể dùng "đưa/kéo điên loạn vào".
- **L6 — p000282, p000283, p000284: văn phong**.
  - p000282: "chấm dứt ... bèn lên tiếng để kết thúc" lặp ý.
  - p000283: "sắp hết kiên nhẫn" hơi lệch so với "gần cạn sức chịu đựng" của hải quân đang bị dồn ép.
  - p000284: "Cậu nhóc trẻ thật" thừa "trẻ"; nên "Còn nhóc quá" hoặc "Trẻ quá". "Chuyển sang chuyện khác" có thể thiên về đổi chủ đề, trong khi nguồn là đổi tâm thế; đề xuất "chuyển sang tâm thế khác".
- **L7 — p000291: "mất rồi"** thêm sắc thái tiếc nuối; nguồn là dự đoán trung tính. Đề xuất bỏ "mất".
- **L8 — p000311: "soạn thảo"** bỏ vế "lên kế hoạch" của "planned and drafted". Đề xuất "được hoạch định và soạn thảo".

## Cấp bậc và xưng hô cần ghi nhận (không chặn lô)

- **p000306: "Đại tá"**. Nguồn dùng "Colonel" để xưng hô. Đoạn kế tiếp nhắc "Trung tá von Lergen". Người nghe nhiều khả năng là Lergen vì mạch tả ánh nhìn rồi tới phản ứng của ông. "Colonel" trong tiếng Anh thường là cách gọi lịch sự cho cả trung tá, nên "Đại tá" có thể tạo mâu thuẫn cấp bậc giữa hai đoạn. Chứng cứ chưa đủ để chắc người nghe là ai. Đề xuất tạm: giữ literal "Đại tá" nếu không có thêm ngữ cảnh, và ghi uncertainty vào `work/run-state/pending-terms.yml`. Nếu coordinator xác nhận người nghe là Lergen, chuyển thành lời xưng hô trung tính như "thưa ngài" hoặc "thưa Trung tá".
- **p000310: "cô"**. Lergen gọi Tanya là "cô". Không có đối chiếu canon ở đây (`characters.yml` trống). Đề xuất tạm giữ, ghi là lựa chọn xưng hô chưa canon.
- Các tên thực thể chưa nằm trong bốn đề xuất nhưng cần giữ nhất quán với sổ pending và các lô khác (không kiểm tra trong lần review này): "Khối Thịnh vượng chung", "Liên minh Entente", "Cộng hòa", "Bộ Ngoại giao", "tùy viên quân sự", "Hạm đội Biển Bắc".

## Bốn đề xuất thuật ngữ

| ID | Đề xuất của translator | Khuyến nghị | Lý do |
|---|---|---|---|
| vol02-ch04-b21-software-personnel-metaphor (p000281) | "phần mềm" (ẩn dụ chỉ nhân lực chất lượng cao) | **Chấp nhận tạm**, ghi `proposed_vi` là "phần mềm" đặt trong dấu ngoặc kép; bỏ phần chú giải trong ngoặc đơn khỏi mục ledger | Cặp "phần cứng"/"phần mềm" đã nhất quán giữa p000279 và p000281. Bản dịch p000281 đã giải thích bằng ngay cụm "nhân lực chất lượng cao" theo nguồn. Giữ dấu ngoặc kép của nguồn. |
| vol02-ch04-b21-witch-hunt (p000283) | cuộc săn phù thủy | **Chấp nhận tạm** | Thành ngữ quen thuộc, nghĩa khớp. Phương án "cuộc truy lùng phù thủy" không tự nhiên hơn. |
| vol02-ch04-b21-utopia (p000288) | Utopia | **Chấp nhận tạm, giữ nguyên "Utopia"** | Giữ danh từ riêng có ám chỉ văn học. "Không tưởng" là tính từ, thành "thế giới hẳn đã thành không tưởng" sai nghĩa. Cần sửa câu theo M1 nhưng không đổi thuật ngữ. |
| vol02-ch04-b21-deputy-director-operations (p000311) | Phó cục trưởng Cục Tác chiến | **Chấp nhận tạm, độ chắc chắn thấp** | "Cục Tác chiến"/"Phó cục trưởng" là cách gọi quen trong bộ máy tham mưu quân sự. "Giám đốc Ban" nghe dân sự và kém tự nhiên. Nguồn chỉ nêu "Operations" (không rõ là cục, ban hay phòng). Cần ghi uncertainty và đối chiếu với các lần xuất hiện khác của chức danh này trong sổ pending. |

Cả bốn đề xuất vẫn là pending, không tự nâng thành canon.

## Điểm đã kiểm tra và đạt

- Phủ định, đối tượng câu hỏi và thời gian giả định ở p000279, p000281, p000284–p000287, p000290, p000296–p000300 giữ đúng nghĩa.
- Con số "bốn mươi tám giờ" (p000290) và trình tự chi tiết ở p000308–p000311 khớp.
- Xưng hô trần thuật về Zettour ("ông") và Lergen ("ông") nhất quán. Đại từ nội tâm/trần thuật của Tanya theo DEC-P01-001 không bị áp sai: p000304–p000305 không dùng "nó"/"mình" cho Tanya.
- Không thêm phán xét hay ghi chú làm việc vào bản dịch. Mảng `notes` trống.
