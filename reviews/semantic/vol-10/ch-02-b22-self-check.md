# Báo cáo tự kiểm (Translator Self-Check & Sign-off) — `vol-10-ch-02-b22`

- **Task ID**: `vol-10-ch-02-b22-translator-signoff` (parent: `vol-10-ch-02-b22`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter010.xhtml/p000404` đến `YS-LN10/Text/chapter010.xhtml/p000442` (39 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc
- Đã dịch và rà soát đầy đủ 39/39 đoạn theo đúng thứ tự nguồn từ `p000404` đến `p000442`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn.
- Trường `status` của toàn bộ 39 dòng đã được cập nhật từ `draft` sang `reviewed` sau khi xử lý đầy đủ báo cáo review của Argon.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter010.xhtml/p000412`: 2 cụm in nghiêng ở câu thứ hai (`*Trật tự*` và `*hỗn loạn*`).
  - `YS-LN10/Text/chapter010.xhtml/p000421`: 1 câu hỏi nội tâm in nghiêng ở đầu đoạn (`*Cô có hạ được mục tiêu không?*`).
- Tất cả các đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.

## 2. Xử lý các findings từ `ch-02-b22-argon-review.yml` và tuân thủ `locked_choices`
- **`YS-LN10/Text/chapter010.xhtml/p000406` (minor — modality)**: Đã cập nhật câu thứ hai thành `Có lẽ mình đã nên chú tâm hơn đến những mảnh chân lý mà tổ tiên để lại mới phải.`, khôi phục trạng từ tình thái phỏng đoán dè dặt ở đầu câu và giữ đúng các thành phần đã khóa.
- **`YS-LN10/Text/chapter010.xhtml/p000432` (minor — pronouns_register)**: Đã chỉnh `quanh hai đứa` thành `quanh hai chúng mình` để thống nhất sắc thái đại từ nội tâm của Tanya (chỉ Tanya và Visha) với các đoạn kế cận (`p000423`, `p000436`–`p000438`).
- **`YS-LN10/Text/chapter010.xhtml/p000434` (minor — meaning_modality)**: Đã chỉnh `ở nơi quân địch đang đóng…` thành `ở nơi lẽ ra là vị trí của quân địch…`, giữ đúng sắc thái tình thái ước lượng vị trí trên không và loại bỏ nét nghĩa đóng quân cố định trên mặt đất.
- Toàn bộ 39/39 mục trong `locked_choices` và 14/14 mục trong `pending_term_recommendations` của `ch-02-b22-argon-review.yml` đều được bảo toàn tuyệt đối.

## 3. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Góc nhìn ngôi thứ nhất của Tanya xuyên suốt toàn bộ lô (`p000404` – `p000442`)**:
  - Độc thoại nội tâm tự xưng `mình` (hoặc `chúng ta` khi bao hàm phe Đế quốc / hai người cùng bay ở `p000412`, `p000428`, `p000429`, `p000431`, `p000442`; `cả hai chúng mình` / `hai chúng mình` / `chúng mình` khi chỉ riêng Tanya và Visha đang rút lui cùng nhau ở `p000423`, `p000432`, `p000436`, `p000437`, `p000438`).
  - Tự quy chiếu ngôi thứ ba bằng tên `Tanya` và đại từ `cô ấy` tại các đoạn tách biệt cái tôi nội tâm khỏi vỏ bọc bên ngoài (`p000413`, `p000414`, `p000416`, `p000417`, `p000421`, `p000426`, `p000431`, `p000436`), giữ đúng đặc trưng phong cách tâm lý của nhân vật.
  - Gọi Visha (Trung úy Serebryakov) trong nội tâm là `sĩ quan phụ tá của Tanya` (`p000421`), `người cộng sự của Tanya` (`p000426`), `Visha` (`p000436`), `Trung úy Serebryakov` (`p000442`), đại từ `cô ấy`.
  - Gọi kẻ địch ngoan cố đang truy kích từ xa (Mary Sue) bằng các định danh miệt thị trong nội tâm: `con lợn rừng ban nãy`, `cái thứ quái thai phản tự nhiên ấy`, đại từ `ả` (`p000441`).
- **Thoại vô tuyến giữa Tanya (`01`) và Visha (`02`) (`p000419` – `p000430`)**:
  - Visha (`02`) báo cáo cho Tanya (`01`): xưng `tôi`, gọi `ngài`, dùng từ kính ngữ `ạ` ở cuối câu (`p000419`, `p000422`, `p000425`), giữ đúng kỷ luật quân đội giữa sĩ quan phụ tá và chỉ huy tiểu đoàn.
  - Tanya (`01`) đáp lời Visha (`02`): xưng `tôi` (`p000427`), gọi mã hiệu `02` (`p000420`) hoặc dùng ngôi gộp `chúng ta` (`p000425`), giọng điệu điềm tĩnh, pha chút mỉa mai tự trào (`một pháp sư biết điều như tôi`).

## 4. Kiểm tra các cấu trúc ngữ pháp dễ lệch nghĩa
- **Mệnh đề khuyên răn cổ phong và quan hệ đối lập (`p000405`, `p000406`, `p000407`)**:
  - `YS-LN10/Text/chapter010.xhtml/p000405`: Bảo toàn cấu trúc phủ định khuyên răn ở vế đầu (`Chớ bắt chước kẻ ác, kẻo chính mình cũng hóa ra kẻ ác`) và cấu trúc điều kiện tương phản ở vế sau (`bất kỳ con ngựa nào cũng có thể trở thành tuấn mã chỉ cần nó học theo tuấn mã, và bất kỳ ai cũng có thể trở thành bậc hiền triết, miễn là người đó noi theo hành động của bậc hiền triết`).
  - `YS-LN10/Text/chapter010.xhtml/p000406`: Giữ đúng sắc thái tình thái phỏng đoán kết hợp giả định nuối tiếc trong quá khứ (`Có lẽ mình đã nên chú tâm hơn...`).
  - `YS-LN10/Text/chapter010.xhtml/p000407`: Giữ đúng cấu trúc nhượng bộ (`Dẫu chỉ là về hình thức, bắt chước bậc hiền triết vẫn là điều khôn ngoan`).
- **Câu hỏi tu từ, giả định và phủ định mức độ (`p000409`, `p000417`, `p000425`, `p000429`, `p000434`, `p000438`, `p000442`)**:
  - `YS-LN10/Text/chapter010.xhtml/p000409`: Bảo toàn câu hỏi tu từ phủ định (`Chẳng phải chính vì thế mà chiến trường mới trở nên hỗn loạn đến vậy sao?`) và kết luận điều kiện tiếp nối.
  - `YS-LN10/Text/chapter010.xhtml/p000417`: Giữ đúng phủ định khả năng bắn trúng của địch (`Đó chẳng thực sự là những phát đạn mà quân địch có khả năng bắn trúng; đại khái chỉ là những viên đạn bắn bừa tình cờ bay đúng hướng mà thôi`).
  - `YS-LN10/Text/chapter010.xhtml/p000425`: Giữ đúng sắc thái giả định quá khứ trong câu hỏi của Visha (`Đó có phải là kẻ mà lẽ ra chúng ta nên khử ngay khi còn cơ hội không ạ?`).
  - `YS-LN10/Text/chapter010.xhtml/p000429`: Bảo toàn cấu trúc gác lại nghi vấn ở đầu câu, sự thừa nhận khách quan ở giữa và sự đối lập với thực tế bất khả thi ở mặt trận phía đông ở cuối đoạn.
  - `YS-LN10/Text/chapter010.xhtml/p000434`: Giữ đúng sắc thái giả định của vị trí quân địch phía sau (`ở nơi lẽ ra là vị trí của quân địch`) và phép so sánh cảm giác ớn lạnh (`như thể có kẻ vừa dí súng vào đầu mình vậy`).
  - `YS-LN10/Text/chapter010.xhtml/p000438`: Bảo toàn sắc thái giới hạn sát nút bổ sung cho đoạn trước (`Phải lưu ý thêm là chỉ vừa vặn làm được mà thôi`).
  - `YS-LN10/Text/chapter010.xhtml/p000442`: Bảo toàn chuỗi câu hỏi nội tâm xác minh số lượng đòn bắn và sự tương phản về thông số kỹ thuật của quả cầu tính toán.

## 5. Thuật ngữ đã áp dụng và đề xuất (`pending_terms`)
- Các thuật ngữ kế thừa nhất quán từ `canon/`, `work/run-state/pending-terms-index.yml` và `pending_term_recommendations`:
  - `mặt trận phía đông` (`p000404`, `p000429`)
  - `chiến tranh tổng lực` (`p000412`)
  - `hỏa lực quấy rối` (`p000417`)
  - `01 / 02` (`p000419`, `p000420`)
  - `sĩ quan phụ tá` (`p000421`)
  - `sĩ quan chỉ huy` (`p000422`)
  - `đòn tập kích chặt đầu chỉ huy` (`p000427`)
  - `lớp vỏ phòng thủ` (`p000434`)
  - `Trung úy Serebryakov / Visha` (`p000436`, `p000442`)
  - `các pha cơ động né tránh` (`p000436`)
  - `lõi kép / quả cầu tính toán Type 97 / quả cầu tính toán` (`p000437`, `p000442`)
  - `thuật thức quang học tầm xa quy mô lớn / thuật thức quan sát quang học` (`p000439`)
  - `tín hiệu ma lực` (`p000440`)
  - `quân tình nguyện đa quốc gia` (`p000442`)
