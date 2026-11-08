# Báo cáo tự kiểm (Self-Check) — `vol-10-ch-05-b12`

- **Task ID:** `vol-10-ch-05-b12-translator-signoff` (parent: `vol-10-ch-05-b12`)
- **Phạm vi:** `YS-LN10/Text/chapter024.xhtml/p000405` → `YS-LN10/Text/chapter024.xhtml/p000450` (46 đoạn)
- **Model:** `argon-low`
- **Trạng thái dòng (`status`):** `reviewed` (46/46 dòng)

## 1. Xử lý Argon Review (`reviews/prose/vol-10/ch-05-b12-argon-review.yml`)
- **Findings (`serious: 0`, `moderate: 0`, `minor: 3`):**
  - `p000423` (`minor` — diễn đạt / chuốt câu): Giản lược từ `và` thành `bắt đầu bay vào thực hiện các đợt lao vào công kích` để nhịp câu gọn hơn đồng thời giữ nguyên cụm thuật ngữ đề xuất `các đợt lao vào công kích`.
  - `p000425` (`minor` — diễn đạt / chuốt câu): Chỉnh cụm mở đầu thành `Khi đợt tấn công của họ đi được nửa chặng` theo đúng gợi ý trong review để câu văn tự nhiên hơn.
  - `p000429` (`minor` — diễn đạt / chuốt câu): Lược bớt từ `tuổi` thứ hai thành `Một quý ông lớn tuổi đơn độc giữa bầu trời đầy những pháp sư trẻ.` để tránh lặp từ trong câu ngắn.
- **Pending term recommendations & Locked choices:**
  - Đối chiếu toàn bộ 46 đoạn với `pending_term_recommendations` và `locked_choices` trong Argon review: tuân thủ đầy đủ các lựa chọn đã khóa về tên gọi, cấp bậc, đại từ/điểm nhìn, logic tình thái và nhấn mạnh `*...*`.
  - Cập nhật trường `status` của toàn bộ 46 dòng trong `translations/vol-10/ch-05-b12.jsonl` từ `draft` sang `reviewed`.

## 2. Kiểm tra nghĩa, phủ định, giả định và logic (`meaning`)
- **p000405–p000419:** Giữ đúng diễn biến Tanya quan sát lính của mình thực hiện đợt xung phong tiếp theo, nhận thấy không cần phải bao vây địch giúp đám lính mới nữa và bảo Thiếu tá Weiss để lính mới tự xử lý phần còn lại. Giữ đúng nhận định về tình trạng thiếu hụt nhân sự kinh niên của Tiểu đoàn 203 buộc họ phải liên tục cơ động, sự khác biệt của Tiểu đoàn 203 ở khả năng cơ động ba chiều và kiểm soát đơn vị di chuyển đồng bộ giữa cuộc cận chiến quần vòng, cùng mệnh lệnh tiến thẳng vào trung tâm đội hình địch.
- **p000420–p000436:** Giữ đúng sự chuyển dịch điểm nhìn trần thuật và nội tâm khi binh lính hiểu ý Tanya chỉ qua cử chỉ nắm tay: nhắm thẳng vào vị chỉ huy địch và tiêu diệt ông ta trước khi ông ta kịp hiểu chuyện gì đang diễn ra. Giữ đúng diễn biến vị phó chỉ huy và quân lính mở đợt công kích bằng biển lửa thuật thức phát nổ, việc pháo thủ trên tàu chiến của Khối Thịnh vượng chung sợ bắn nhầm quân nhà nên hỏa lực phòng không chi viện đều bắn lệch vào khoảng không vô hại, và cảnh hai đại đội át chủ bài của Tiểu đoàn 203 xuyên thủng đội hình thưa thớt của lữ đoàn địch để lao tới vị chỉ huy lớn tuổi đang phản ứng chậm chạp, tự bật lớp vỏ phòng thủ nghênh chiến thay vì lấy cấp dưới làm lá chắn.
- **p000437–p000450:** Giữ đúng tiêu đề chuyển cảnh sang phía bên kia chiến tuyến trong cùng ngày hôm đó và điểm nhìn của Trung tá Drake. Giữ đúng nỗi uất ức, bất lực của Drake khi đại đội của anh đang bị giữ làm lực lượng dự bị chiến thuật nên không thể tự ý rời vị trí lao ra ứng cứu những người lính trẻ của đất nước đang bị tiêu diệt. Giữ đúng lập luận về vai trò của lực lượng dự bị (giữ lại quân để truy kích và tấn công tàu địch, đồng thời ứng cứu các điểm nóng như một quân bài tẩy của Chỉ huy Ballmer) và sự bàng hoàng không thể tin nổi của Drake khi thấy cả một lữ đoàn quy mô lớn bị đánh tan rã quá đỗi dễ dàng.

## 3. Kiểm tra đại từ và xưng hô (`pronouns`)
- **p000405–p000436 (Phía Tanya & Tiểu đoàn 203):**
  - Nội tâm / tự thuật ngôi thứ nhất của Tanya: dùng `mình` (và `chúng ta` khi bao gồm đơn vị); dùng `bạn` nếu mang tính khái quát, ở `p000413` diễn đạt tự nhiên theo danh ngữ để giữ mạch khách quan.
  - Trần thuật ngôi thứ ba về Tanya (`p000420`, `p000423`, `p000424`, `p000430`): dùng `Tanya` / `cô` nhất quán với các lô trước của tập 10.
  - Thoại giữa Tanya và Thiếu tá Weiss (`p000406`, `p000407`, `p000410`, `p000415`, `p000416`, `p000418`, `p000419`): Tanya gọi `Thiếu tá Weiss` / `Thiếu tá`, dùng `chúng ta` cho hành động chung; Weiss đáp lễ phép (`Rõ`, `...ạ`).
- **p000438–p000450 (Phía Trung tá Drake):**
  - Trần thuật ngôi thứ ba về Drake: dùng `Trung tá Drake` / `Drake` / `anh`; đối với Chỉ huy Ballmer dùng `Chỉ huy Ballmer` / `ông`.
  - Nội tâm và lời độc thoại tự nhủ của Drake (`p000438`, `p000439`, `p000442`): dùng `chúng ta` (khi nói chung đơn vị mình) và `mình` (khi tự vấn bản thân).

## 4. Kiểm tra nhấn mạnh / chữ nghiêng (`emphasis`)
- Áp dụng nghiêm ngặt `DEC-P01-002`:
  - `p000421`: Toàn bộ câu được bọc trong `<html:em>...</html:em>` → giữ nguyên phạm vi nhấn mạnh `*Nhắm vào chỉ huy của chúng và giết ông ta trước khi ông ta kịp nhận ra chuyện gì đang xảy ra.*`
  - `p000438`: Toàn bộ câu hỏi nội tâm được bọc trong `<html:em>...</html:em>` → giữ nguyên phạm vi nhấn mạnh `*Tại sao chúng ta lại chỉ ngồi ngoài cuộc, khoanh tay đứng nhìn trong khi các chàng trai của chúng ta đang bị giết hại ngoài kia chứ?*`
  - `p000439`: Câu cuối được bọc trong `<html:em>...</html:em>` → giữ nguyên phạm vi nhấn mạnh `*Sao mình lại bất lực chẳng thể làm được gì thế này?*`
  - Các đoạn còn lại (bao gồm `p000411`, `p000428`, `p000444` chỉ có thẻ neo trang `<html:a id="page-..." />`) không có nhấn mạnh trong nguồn nên không thêm dấu `*...*`.

## 5. Thuật ngữ và mục đề xuất (`pending_terms`)
- Áp dụng nhất quán các thuật ngữ đã có trong sổ pending của tập 10 và các tập trước:
  - `Thiếu tá Weiss` / `vị phó chỉ huy` (`p000406`, `p000410`, `p000411`, `p000423`)
  - `Tiểu đoàn 203` (`p000409`, `p000412`, `p000422`, `p000434`)
  - `cuộc cận chiến quần vòng` (`p000413`)
  - `các thuật thức phát nổ` (`p000424`)
  - `Khối Thịnh vượng chung` (`p000424`, `p000425`, `p000430`)
  - `hai đại đội át chủ bài` (`p000432`)
  - `hệ thống chỉ huy` / `sĩ quan chỉ huy` (`p000433`, `p000434`)
  - `lớp vỏ phòng thủ` (`p000435`)
  - `Trung tá Drake` / `Drake` (`p000439`, `p000446`, `p000450`)
  - `Chỉ huy Ballmer` (`p000446`)
- Các cụm thuật ngữ ghi nhận đề xuất (`pending`):
  - `khả năng cơ động ba chiều` (`p000413`)
  - `các đợt lao vào công kích` (`p000423`)
  - `hỏa lực phòng không chi viện` (`p000425`)
  - `đạn pháo phòng không và đạn vạch đường` (`p000425`)
  - `lực lượng dự bị chiến thuật` / `các đơn vị dự bị` / `lực lượng dự bị` (`p000441`, `p000446`)
