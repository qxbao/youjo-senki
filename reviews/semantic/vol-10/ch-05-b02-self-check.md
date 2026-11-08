# Báo cáo tự kiểm (Self-Check): `vol-10-ch-05-b02`

- **Task ID:** `vol-10-ch-05-b02-translator-signoff` (parent: `vol-10-ch-05-b02`)
- **Phạm vi đoạn:** `YS-LN10/Text/chapter024.xhtml/p000032` đến `YS-LN10/Text/chapter024.xhtml/p000065` (34 đoạn)
- **Tệp bản dịch:** `translations/vol-10/ch-05-b02.jsonl`
- **Trạng thái dòng:** `reviewed` (đã cập nhật toàn bộ 34 dòng từ `draft` sang `reviewed`)

## 1. Xử lý Findings từ Argon Review (`reviews/prose/vol-10/ch-05-b02-argon-review.yml`)
- **`YS-LN10/Text/chapter024.xhtml/p000053` (minor):** Đã tiếp nhận đề xuất chỉnh câu thoại của ông Johnson sang thành ngữ `"Có con chim nhỏ ở Đế quốc mách với tôi rằng..."` để bảo toàn sắc thái dí dỏm, nửa đùa nửa thật của nhân vật tình báo và tuân thủ đầy đủ `locked_choices`.
- **`YS-LN10/Text/chapter024.xhtml/p000058` (minor):** Đã tiếp nhận đề xuất quy chiếu đại từ sở hữu ở câu đầu về ông lão (`"ẩn sâu trong từng lời của ông là một cơn giận thực sự"`) và lược bỏ phụ từ `"cũng"` ở câu thứ hai (`"Ông lão dường như đang có tâm trạng rất tồi tệ."`), giúp liên từ `"Tuy nhiên"` ở câu thứ ba tạo thế đối lập mạch lạc hơn.

## 2. Kiểm tra nghĩa, logic và giả định (`locked_choices`)
- Đã đối chiếu đầy đủ 34 đoạn từ `p000032` đến `p000065`, bảo đảm tuân thủ toàn bộ `locked_choices` trong `ch-05-b02-argon-review.yml`.
- Giữ nguyên câu hỏi tu từ giả định ở `p000037` về việc cánh tay đã bình phục để tận hưởng quê nhà, cũng như câu nói xã giao mỉa mai về hương vị món ăn/đồ uống.
- Bảo toàn ẩn dụ về trò chơi trừ tà bắt ma thời thơ ấu (`p000042`–`p000048`) dẫn dắt sang nhiệm vụ đối phó với Ác quỷ sông Rhine (`p000049`–`p000056`).
- Giữ đúng sắc thái hoài nghi xen lẫn phẫn nộ khi nghe tin quân Đế quốc tấn công vùng eo biển và việc bàn chuyện cơ mật ở sảnh khách sạn (`p000057`–`p000059`), cùng lời giải thích ngầm của ông Johnson rằng khu vực khách sạn này thuộc quyền kiểm soát của cơ quan tình báo và đã được dọn sạch (`p000060`–`p000065`).

## 3. Điểm nhìn và quy chuẩn xưng hô
- Trần thuật ngôi thứ ba theo điểm nhìn của Trung tá Drake: quy chiếu Drake bằng `anh`, quy chiếu ông Johnson bằng `ông lão` / `ông Johnson` / `ông ta` / `ông` tùy sắc thái câu.
- Trong hội thoại giữa Drake và ông Johnson (`p000035`–`p000064`), nhất quán với `vol-08` và `vol-10`:
  - Ông Johnson gọi Drake là `Trung tá Drake` / `Trung tá` / `anh`, tự xưng `tôi` (hoặc `chúng tôi` / `chúng ta` khi đại diện cho phía cơ quan tình báo và đất nước Khối Thịnh vượng chung).
  - Drake gọi ông Johnson là `ông Johnson` / `ông`, tự xưng `tôi`.

## 4. Nhấn mạnh và định dạng (`DEC-P01-002`)
- Chỉ sử dụng dấu nhấn mạnh `*...*` tại đúng 1 vị trí có nhấn mạnh trong nguồn:
  - `YS-LN10/Text/chapter024.xhtml/p000060`: nhấn mạnh từ `*chúng ta*`.
- Giữ nguyên dấu ngoặc kép quanh cụm từ được đánh dấu trong nguồn ở `p000065` (`“dọn sạch”`). Không tự ý thêm chữ nghiêng ở các đoạn khác.

## 5. Thuật ngữ và mục chờ xét (`pending_term_recommendations`)
- Đã kiểm tra và tuân thủ đầy đủ 7 mục `pending_term_recommendations` trong `ch-05-b02-argon-review.yml`:
  - `Ông Johnson` / `ông Johnson` (`p000035`, `p000038`, `p000054`, `p000063`)
  - `Trung tá Drake` / `Trung tá` / `Drake` (`p000034`, `p000036`, `p000038`, `p000040`, `p000046`, `p000050`, `p000058`, `p000065`)
  - `mặt trận phía đông` (`p000038`, `p000053`)
  - `Ác quỷ sông Rhine` (`p000049`, `p000055`)
  - `Đế quốc` / `vùng eo biển` / `Bên Tình báo` / `Khối Thịnh vượng chung` / `Liên bang` (`p000053`, `p000055`, `p000056`, `p000059`, `p000062`)
  - `bọn Kraut` (`p000056`), `lũ Kraut` (`p000059`), `đám Cộng sản` (`p000062`)
  - `tinh thần John Bull` (`p000063`)
