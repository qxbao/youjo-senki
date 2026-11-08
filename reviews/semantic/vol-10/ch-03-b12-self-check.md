# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-03-b12`

- **Task ID**: `vol-10-ch-03-b12`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter018.xhtml/p000260` đến `YS-LN10/Text/chapter018.xhtml/p000306` (47 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc
- Đã dịch đầy đủ 47/47 đoạn theo đúng thứ tự nguồn từ `p000260` đến `p000306`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 47 dòng đã được cập nhật từ `draft` sang `reviewed` sau khi xử lý toàn bộ findings và đối chiếu `locked_choices` từ Argon review.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter018.xhtml/p000265`: `*Anh hiểu ý tôi mà*`.
  - `YS-LN10/Text/chapter018.xhtml/p000305`: `*sương mù chiến tranh*`.
- Tất cả 45 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.

## 2. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Trần thuật ngôi thứ ba từ góc nhìn xoay quanh Trung tá Drake và Tướng Habergram**:
  - Trần thuật gọi `Trung tá Drake` / `Drake` là `anh` hoặc `vị trung tá`; gọi `Tướng Habergram` / `Habergram` là `ông`, `vị tướng`, hoặc `cấp trên của anh`.
  - Trong đối thoại giữa Tướng Habergram và Trung tá Drake:
    - Tướng Habergram xưng `tôi`, gọi Drake là `anh` hoặc `Trung tá` (`p000263`, `p000290` — bao gồm cả cách gọi rút gọn trong quân đội đối với cấp bậc trung tá).
    - Trung tá Drake xưng `tôi` (và `chúng tôi` / `bên ta` khi nói về đơn vị của mình), gọi Tướng Habergram là `ngài` / `thưa ngài`, giữ thái độ lịch sự, đúng mực của một sĩ quan cấp dưới đang báo cáo với người đứng đầu ngành tình báo dù trong lòng đầy bức xúc và hoài nghi.
  - Khi đề cập đến Tanya (`Ác quỷ sông Rhine` / `Pháp sư Định danh`), dùng đại từ `cô ta` hoặc danh xưng `con ác quỷ đó` theo đúng góc nhìn của phe Khối Thịnh vượng chung.
  - Trong lời chỉ dẫn của người dẫn đường tại `p000301`, giữ câu thoại lịch sự `“Mời đi lối này, thưa ngài”`.

## 3. Kiểm tra các cấu trúc ngữ pháp và sắc thái dễ lệch nghĩa
- **`p000262` – `p000268`**: Bảo toàn rõ sự lệch pha trong giao tiếp giữa một sĩ quan tác chiến thực địa hiếm khi ngồi bàn giấy như Drake và Tướng Habergram. Ban đầu Drake báo cáo về tâm lý bị kích động của các pháp sư cựu Liên minh Hiệp ước và Hợp chúng quốc khi thấy đối phương, nhưng Habergram ngắt lời vì muốn đi thẳng vào chi tiết cuộc chạm trán thực tế để kiểm chứng xem có nhầm lẫn nhận dạng hay không.
- **`p000273` – `p000280`**: Giữ nguyên số liệu thiệt hại (hai pháp sư địch tiến hành trinh sát chiến đấu đã bắn hạ sáu người, nếu tính cả số bị thương nặng thì tổng tổn thất lên tới cả một đại đội) và nhận định của hai người rằng `Trung tướng Zettour` (`bậc thầy mánh khóe`) đã bắt tay với `Ác quỷ sông Rhine` để xoay họ như chong chóng.
- **`p000284` – `p000294`**: Phản ánh chính xác sự mâu thuẫn giữa xác nhận bằng mắt thường (cùng trải nghiệm đánh giáp lá cà trực diện dẫn đến bị thương của Drake ở `p000289`) với báo cáo tình báo mới nhất phía Habergram rằng cả Tanya lẫn tiểu đoàn trứ danh kia đang ở mặt trận phía tây, dẫn đến kết luận áp đặt của Habergram rằng thứ Drake thấy chỉ là `ảo ảnh hoặc ảo giác`.
- **`p000298` – `p000306`**: Giữ nguyên chỉ thị bàn giao báo cáo miệng cho `ông Johnson`, cùng lời mỉa mai chua chát của Drake ở cuối đoạn khi vết thương trên vai nhức nhối giữa hành lang (`Đây có phải là *sương mù chiến tranh* trứ danh mà ai nấy vẫn thường nhắc tới không?`, `Biết đâu đây cũng chỉ là một ảo giác mà thôi`).

## 4. Thuật ngữ đã áp dụng và đề xuất (`pending_terms`)
- Kế thừa nhất quán các phương án từ `work/run-state/pending-terms-index.yml`:
  - `Ác quỷ sông Rhine` (`p000260`, `p000268`, `p000284`, `p000289`)
  - `Liên bang` (`p000260`)
  - `Pháp sư Định danh` (`p000262`)
  - `Liên minh Hiệp ước` (`p000262`)
  - `các pháp sư trên không` (`p000262`)
  - `Hợp chúng quốc` (`p000262`)
  - `Trung tá Drake` / `Drake` / `Trung tá` / `vị trung tá` (`p000263`, `p000265`, `p000266`, `p000275`, `p000287`, `p000289`, `p000290`, `p000291`, `p000297`, `p000301`, `p000304`)
  - `Tướng Habergram` / `Habergram` (`p000266`, `p000297`, `p000304`)
  - `trinh sát chiến đấu` (`p000273`)
  - `Trung tướng Zettour` (`p000276`)
  - `bậc thầy mánh khóe` (`p000279`)
  - `mặt trận phía đông` (`p000284`, `p000298`)
  - `ông Johnson` (`p000298`, `p000299`)
  - `sương mù chiến tranh` (`p000305`)
