# Báo cáo tự kiểm (Self-Check): `vol-11-ch-01-b07`

- **Task ID:** `vol-11-ch-01-b07-translator-signoff` (parent: `vol-11-ch-01-b07`)
- **Phạm vi đoạn:** `YS-LN11/Text/chapter002.xhtml/p000194` → `YS-LN11/Text/chapter002.xhtml/p000220` (27 đoạn)
- **Tác tử dịch:** `argon-low` (Translator)
- **Trạng thái dòng:** `reviewed`

## 1. Kiểm tra nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic và thời gian giả định
- **p000194–p000197:** Giữ đúng ý mở đầu về việc cấp trên trút gánh nặng sang cấp dưới khi mọi chuyện không như ý, cảnh Tanya phải đứng nghiêm hứng khói thuốc thụ động trước hai vị sếp đang cau mày hút thuốc liên tục, mong ước được rời đi ngay lập tức bị dập tắt khi Tướng Rudersdorf đề nghị bày hết mọi chuyện ra bàn để thảo luận thẳng thắn về Kế hoạch B và Tướng Zettour tán thành.
- **p000198–p000204:** Bảo toàn suy nghĩ tính toán của Tanya khi tìm cách xen vào bằng câu hỏi xin phép lui ra với giọng điệu khiêm nhường và chân thành (`p000200`), câu trả lời giả định mà cô mong nhận được trong đầu (`p000201`), phản ứng mỉm cười của Zettour và cái vỗ lưng của Rudersdorf (`p000202`–`p000203`), cùng lời tuyên bố của Rudersdorf rằng tiểu đoàn của cô sẽ là trọng tâm của chiến dịch (`p000204`).
- **p000205–p000211:** Giữ nguyên phản ứng nội tâm kinh hãi và bất mãn của Tanya trước việc trở thành trọng tâm của Kế hoạch B, câu đáp ngoại giao đầy dè dặt (`p000207`), và nỗ lực vắt óc tìm cớ thoái thác (ví tình thế như tấm ván của Carneades, thậm chí giả định cực đoan rằng sẵn sàng thề trung thành với phe Cộng sản ở bề ngoài nếu cần để khỏi ký vào bản án tử) nhưng rốt cuộc chẳng có gì cả (`p000211`).
- **p000212–p000220:** Bảo toàn câu hỏi truy vấn của Rudersdorf khi thấy Tanya kiệm lời (`p000212`), sự giằng xé nội tâm của Tanya giữa bản năng tự bảo toàn và thực tế không thể trốn chạy của một động vật chính trị (vì thử trốn tránh là tự sát về mặt xã hội lẫn hành chính), cơn rủa thầm Being X, màn đỡ lời như pháo hạng nặng chi viện từ bên sườn của Zettour (`p000215`–`p000217`), và thái độ kiên quyết không nhượng bộ của Rudersdorf khi buộc Tanya phải tự mình trả lời (`p000218`–`p000220`).

## 2. Xử lý Findings & Locked Choices từ Argon Review (`reviews/prose/vol-11/ch-01-b07-argon-review.yml`)
- **Finding 1 (`p000211`, minor):** Tiếp nhận khuyến nghị từ Argon review, chỉnh `"Nhưng than ôi, chẳng có cái cớ nào cả."` thành `"Nhưng than ôi, chẳng có gì cả."` để sát bề mặt đại từ bất định phủ định trong câu nguồn, không tự thêm danh từ giải thích ngoài câu nguồn, đồng thời giữ nguyên mệnh đề phủ định và đại từ tự quy chiếu `Mình` ở câu sau theo `locked_choices`.
- **Finding 2 (`p000212`, minor):** Tiếp nhận khuyến nghị từ Argon review, chỉnh `"cô có vẻ trầm ngâm nhỉ"` thành `"cô có vẻ kiệm lời nhỉ"` để phản ánh trực tiếp trạng thái ít nói của Tanya sau câu đáp ngắn ở `p000207`–`p000208`, bảo toàn đầy đủ `locked_choices` (`Trung tá`, cặp `Tôi` – `cô`, câu hỏi phủ định và ý định giao nhiệm vụ vinh dự bậc nhất).
- **Locked Choices & Pending Term Recommendations:** Toàn bộ 27 đoạn (`p000194`–`p000220`) tuân thủ tuyệt đối các `locked_choices` và `pending_term_recommendations` trong báo cáo review của Argon. Toàn bộ 27 dòng trong `translations/vol-11/ch-01-b07.jsonl` đã được cập nhật `status` từ `draft` sang `reviewed`.

## 3. Kiểm tra đại từ và xưng hô (`DEC-P01-001`)
- **Độc thoại nội tâm & trần thuật ngôi thứ nhất của Tanya (`p000194`, `p000195`, `p000198`, `p000199`, `p000201`–`p000203`, `p000205`, `p000206`, `p000208`–`p000211`, `p000213`–`p000215`, `p000217`, `p000219`):**
  - Tự quy chiếu trong nội tâm dùng `mình`; khi tự nhắc đến bản thân ở ngôi thứ ba (`p000194`, `p000195`, `p000199`, `p000213`, `p000215`) giữ nguyên tên `Tanya` và đại từ `cô` (`p000194`, `p000213`).
  - Gọi Zettour và Rudersdorf trong suy nghĩ là `ông ấy` / `họ` / `các cấp trên của mình` / `hai vị sếp của cô`, hoặc gọi hướng tới hai vị tướng trong độc thoại nội tâm ở `p000219` là `các ngài`.
- **Đối thoại giữa Tanya và hai vị tướng (`p000200`, `p000204`, `p000207`, `p000212`, `p000220`):**
  - Tanya xưng `tôi`, kèm kính ngữ `ạ`.
  - Rudersdorf xưng `tôi`, gọi Tanya là `Trung tá` / `cô`.
- **Đối thoại giữa Rudersdorf và Zettour (`p000196`, `p000197`, `p000216`, `p000218`):**
  - Xưng `tôi` / `chúng ta`, gọi nhau là `ông` hoặc tên/cấp bậc (`Tướng Rudersdorf`, `Rudersdorf`, `Zettour`), gọi Tanya ở ngôi thứ ba là `con bé` (`p000218`), nhất quán với các lô trước của chương 1.

## 4. Kiểm tra nhấn mạnh / chữ nghiêng (`DEC-P01-002`)
- Đã kiểm tra đối chiếu từng thẻ `<html:em>` trong nguồn và chỉ đánh dấu `*...*` tại đúng 4 vị trí tương ứng:
  - `p000201`: `*Không, chuyện này vượt quá cấp bậc của cô rồi, Trung tá.*`
  - `p000202`: `*Vààà ông ấy đang mỉm cười.*`
  - `p000203`: `*Cô không cần phải lo chuyện đó đâu.*`
  - `p000206`: `*Trọng tâm của Kế hoạch B ư? …Chết tiệt thật chứ.*`
- Không tự ý thêm `*...*` ở bất kỳ vị trí nào khác.

## 5. Thuật ngữ & Pending Terms
- Đã tra cứu và áp dụng nhất quán các phương án tạm từ `work/run-state/pending-terms-index.yml`, `reviews/prose/vol-11/ch-01-b07-argon-review.yml` và các lô trước:
  - `General Rudersdorf` / `General Zettour`: Tướng Rudersdorf / Tướng Zettour (`p000195`, `p000197`, `p000203`, `p000213`, `p000215`, `p000217`)
  - `Plan B`: Kế hoạch B (`p000196`, `p000206`)
  - `Lieutenant Colonel` / `Colonel` (khi gọi Trung tá Tanya von Degurechaff): Trung tá (`p000201`, `p000204`, `p000212`)
  - `General Staff` / `General Staff Office`: Bộ Tổng tham mưu / Văn phòng Bộ Tổng tham mưu (`p000202`, `p000204`)
  - `God`: Thượng đế (`p000202`)
  - `plank of Carneades`: tấm ván của Carneades (`p000210`)
  - `the Communists`: phe Cộng sản (`p000210`)
  - `political animal`: động vật chính trị (`p000213`)
  - `Being X`: Being X (`p000214`)
