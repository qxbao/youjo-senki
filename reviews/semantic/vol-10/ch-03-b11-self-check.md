# Báo cáo tự kiểm (Translator Self-Check & Sign-off) — `vol-10-ch-03-b11`

- **Task ID**: `vol-10-ch-03-b11-translator-signoff` (parent: `vol-10-ch-03-b11`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter018.xhtml/p000220` đến `YS-LN10/Text/chapter018.xhtml/p000259` (40 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ, bảo toàn cấu trúc và cập nhật trạng thái Sign-off
- Đã dịch và rà soát đầy đủ 40/40 đoạn theo đúng thứ tự nguồn từ `p000220` đến `p000259`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 40 dòng đã được cập nhật từ `draft` sang `reviewed` theo đúng quy trình Sign-off.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`): toàn bộ 40 đoạn trong lô này không có thẻ nhấn mạnh trong `xhtml`, và bản dịch hoàn toàn không sử dụng dấu `*...*`.

## 2. Xử lý các findings và `locked_choices` từ `ch-03-b11-argon-review.yml`
- **`p000225` (minor)**: Chỉnh cụm `một sự đồng cảnh ngộ ngoài ý muốn` thành `một cảm giác gần gũi ngoài ý muốn` để giữ sát sắc thái bề mặt của nguyên văn khi Trung tá Drake liên tưởng bản thân với que diêm đang cháy dần, đồng thời bảo toàn mọi `locked_choices` của đoạn.
- **`p000236` (minor)**: Tiết chế cụm `tuyến đầu méo mó dị dạng ấy` thành `tuyến đầu méo mó ấy` để phản ánh đúng sắc thái mô tả hình thái chiến tuyến bị biến dạng trong nguyên văn.
- **`p000248` (minor)**: Chỉnh `đó là một con nhãi xấc xược…` thành `đó là một đứa nhóc xấc xược…` để giữ sắc thái trung tính về giới tính đồng bộ với cách gọi trung tính ở các câu lân cận và bảo toàn dấu chấm lửng ở cuối câu thoại bị ngắt lời.
- **`p000257` (minor)**: Chỉnh `ông đang nung nấu điều gì đó trong đầu` thành `ông đang bận tâm suy nghĩ điều gì đó` để giữ sắc thái trung tính đồng thời bảo toàn `locked_choices` của đoạn.
- Toàn bộ 40 mục `locked_choices` và 15 mục `pending_term_recommendations` trong `reviews/prose/vol-10/ch-03-b11-argon-review.yml` được tuân thủ nghiêm ngặt và giữ nhất quán tuyệt đối.

## 3. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Trần thuật ngôi thứ ba từ góc nhìn xoay quanh Trung tá Drake và Tướng Habergram**:
  - Trần thuật gọi `Trung tá Drake` / `Drake` là `anh`; gọi `Tướng Habergram` (`cấp trên`, `vị tướng`) là `ông`.
  - Trong đối thoại giữa Tướng Habergram và Trung tá Drake (tiếp nối trực tiếp mạch `ch-03-b10`):
    - Tướng Habergram xưng `tôi` (và `chúng ta` khi nói về phía Khối Thịnh vượng chung), gọi Drake là `anh` và `Trung tá` (`p000229`, `p000231`, `p000233` — cách gọi rút gọn trong quân đội đối với cấp bậc trung tá).
    - Trung tá Drake xưng `tôi` (và `chúng ta` / `chúng tôi`), gọi Tướng Habergram là `thưa Tướng quân` (`p000230`) hoặc `thưa ngài` (`p000238`, `p000243`), giữ thái độ lịch sự, đúng mực của một sĩ quan cấp dưới đang báo cáo nhưng vẫn thẳng thắn trình bày nhận định thực chiến.
  - Khi đề cập đến Tanya (`Ác quỷ sông Rhine`, `Bạch Ngân Rỉ Sét`, `Pháp sư Định danh`), dùng cách gọi trung tính `tên pháp sư đó` / `con ác quỷ đó` / `bóng ma chết tiệt đó` / `đứa nhóc xấc xược` phù hợp với thái độ dè chừng lẫn cay cú của Drake sau trận cận chiến.

## 4. Thuật ngữ đã áp dụng và đề xuất (`pending_terms`)
- Đồng bộ nhất quán với `pending-terms-index.yml` và `pending_term_recommendations` trong `ch-03-b11-argon-review.yml`:
  - `Liên bang` (`p000220`)
  - `Chủ nghĩa Cộng sản` / `những người Cộng sản` (`p000220`, `p000222`)
  - `chủ nghĩa dân tộc` (`p000220`)
  - `nhánh Tình báo của Lục quân Khối Thịnh vượng chung` (`p000222`)
  - `Trung tá Drake` / `Drake` / `Trung tá` (`p000221`, `p000223`, `p000225`, `p000226`, `p000229`, `p000231`, `p000233`, `p000240`, `p000244`, `p000250`, `p000252`, `p000256`, `p000257`, `p000259`)
  - `Tướng Habergram` / `vị tướng` / `thưa Tướng quân` (`p000230`, `p000235`, `p000250`, `p000257`)
  - `Trung úy Sue` (`p000230`)
  - `đơn vị đa quốc gia` (`p000234`)
  - `các pháp sư kỳ cựu của Lục quân Đế quốc` (`p000238`)
  - `Ác quỷ sông Rhine` / `con ác quỷ đó` (`p000243`, `p000246`, `p000247`, `p000249`, `p000251`, `p000253`)
  - `Pháp sư Định danh` / `tên Pháp sư Định danh đó` (`p000246`, `p000249`, `p000254`)
  - `Bạch Ngân Rỉ Sét` (`p000246`)
  - `các đòn tập kích chặt đầu chỉ huy` / `kẻ chuyên tung đòn chặt đầu chỉ huy` (`p000249`, `p000256`)
  - `xác nhận bằng mắt thường` / `chỉ số ma năng` (`p000251`)
  - `lưỡi kiếm ma pháp` / `thuật thức bắn tỉa quang học` / `thuật thức phát nổ` (`p000253`)
  - `trị liệu ma pháp` (`p000255`)
  - `tiền tuyến` / `bản thổ` (`p000259`)
