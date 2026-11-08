# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-03-b14`

- **Task ID**: `vol-10-ch-03-b14`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter018.xhtml/p000341` đến `YS-LN10/Text/chapter018.xhtml/p000371` (31 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc
- Đã dịch đầy đủ 31/31 đoạn theo đúng thứ tự nguồn từ `p000341` đến `p000371`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn và handoff.
- Trường `status` của toàn bộ 31 dòng đã được cập nhật từ `draft` sang `reviewed` sau khi xử lý Argon review.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter018.xhtml/p000348`: `*nhìn thấy con ác quỷ đó ở phía đông*`.
- Tất cả 30 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.
- **Xử lý findings từ Argon review (`vol-10-ch-03-b14-argon-review`)**:
  - `YS-LN10/Text/chapter018.xhtml/p000361` (minor): Đã chỉnh `rượu mạnh` thành `rượu brandy` để giữ rõ loại rượu cụ thể theo nguyên tác.
  - `YS-LN10/Text/chapter018.xhtml/p000371` (minor): Đã chỉnh `vị trí đóng quân của từng chiếc tàu ngầm địch` thành `vị trí bố trí của từng chiếc tàu ngầm địch` để phù hợp với lực lượng tàu ngầm hoạt động trên biển.
  - Đã kiểm tra và tuân thủ đầy đủ toàn bộ `pending_term_recommendations` và `locked_choices`.

## 2. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Điểm nhìn trần thuật và độc thoại nội tâm của Tướng Habergram (`p000341` – `p000371`)**:
  - Trần thuật ngôi thứ ba gọi `Tướng Habergram` / `Habergram` là `ông` (kế thừa nhất quán từ `vol-10-ch-03-b12` và `vol-10-ch-03-b13`).
  - Trong các câu tự nhủ/lẩm bẩm một mình của Habergram tại văn phòng (`p000343`, `p000349`, `p000355`, `p000357`, `p000359`, `p000363`, `p000365`, `p000367`), ông tự xưng `mình` hoặc `chúng ta` (khi nói chung về phía cơ quan tình báo Khối Thịnh vượng chung), giữ giọng điệu căng thẳng, nặng nề và hoài nghi của một người đứng đầu ngành tình báo đang đứng trước hai nguồn tin mâu thuẫn gay gắt.
  - Khi đề cập đến `Trung tá Drake`, Habergram gọi là `anh ta` (`p000348`, `p000349`).
  - Khi đề cập đến Tanya (`Ác quỷ sông Rhine`), dùng danh xưng trung tính `con ác quỷ đó` / `con ác quỷ ấy` (`p000341`, `p000345`, `p000348`, `p000349`), không suy diễn giới tính khi phía Habergram chỉ nắm được thông tin qua mật điện và lời kể.
  - Khi đề cập đến phía Đế quốc, tiểu đoàn pháp sư hay cặp đôi Romel – Ác quỷ sông Rhine, dùng `chúng` / `hai kẻ đó` / `hai kẻ này` đúng góc nhìn đối địch của Habergram.

## 3. Kiểm tra các cấu trúc ngữ pháp và sắc thái dễ lệch nghĩa
- **`p000341` – `p000342`**: Giữ đúng mạch lập luận nối tiếp từ cuối `b13`: giả sử chỉ huy đơn vị có di chuyển độc lập vì mục đích liên lạc hay nghỉ phép, thì cũng không có lý do gì lại bỏ lại tiểu đoàn ở phía tây để trực tiếp tham chiến ở phía đông—đây là một sự mâu thuẫn hoàn toàn trong mắt Habergram.
- **`p000345` – `p000347`**: Bảo toàn chi tiết mật điện giải mã từ `Ultra` cho biết `Ác quỷ sông Rhine` cùng tiểu đoàn pháp sư đang đóng quân ở phía tây thuộc `Kampfgruppe Lergen`, chịu sự chỉ huy trực tiếp của `Trung tướng Romel`, và chuẩn bị mở cuộc tập kích biệt kích vào `bản thổ Khối Thịnh vượng chung` với các pháp sư trên không làm mũi nhọn mở màn.
- **`p000348`**: Giữ nguyên cấu trúc phủ định kép (không có lý do gì để không tin vào điều đó cho đến khi một người lính được tín nhiệm ngang ngửa `Ultra` báo cáo đã `*nhìn thấy con ác quỷ đó ở phía đông*`).
- **`p000351` – `p000354`**: Phản ánh chính xác thế tiến thoái lưỡng nan trong phân tích phản gián của Habergram: ông lo ngại kịch bản tồi tệ nhất là Đế quốc đã phát hiện mật mã vô tuyến bị bẻ khóa và đang tung tin phản gián; nhưng thực tế mọi tin chặn thu từ `SIGINT` và lực lượng kháng chiến (như việc tàu bè Đế quốc bí mật tập kết tại một điểm) đều được xác minh là thật, cộng thêm xu hướng quá tự tin vào hệ thống mã hóa của Đế quốc và việc nhiều pháp sư quân ta bị bắn hạ gần đây trên vùng eo biển khiến giới tình báo buộc phải cảnh giác.
- **`p000365` – `p000367`**: Giữ rõ sự giằng xé giữa lý trí phân tích (nếu Đế quốc nghi ngờ mật mã bị lộ hoặc muốn dùng `Ultra` để gài bẫy thì luồng thông tin `SIGINT` của `Lục quân Đế quốc` không thể giữ nguyên như cũ mà không có động thái bảo mật nào) và nỗi ám ảnh nghề nghiệp của người làm tình báo (lo sợ đây là một phần trong một âm mưu lớn hơn).
- **`p000370` – `p000371`**: Bảo toàn mối liên hệ nhân quả về quá khứ của Habergram: ông rủa thầm tuyến giao thương đường biển từng khiến mình bị giáng cấp bẽ bàng, dù thực tế ông đã lập công lớn khi dùng tin từ `Ultra` nắm vị trí từng chiếc tàu ngầm địch và tổ chức các tàu buôn thành những đoàn tàu có hộ tống vũ trang để bảo vệ hoạt động vận tải qua eo biển trước đội tàu ngầm `U-boat` của Đế quốc.

## 4. Thuật ngữ đã áp dụng và đề xuất (`pending_terms`)
- Kế thừa nhất quán các phương án từ `work/run-state/pending-terms-index.yml`:
  - `Ultra` / `tin tình báo của Ultra` (`p000344`, `p000348`, `p000358`, `p000359`, `p000365`, `p000366`, `p000371`)
  - `Lục quân Đế quốc` (`p000344`, `p000366`)
  - `Ác quỷ sông Rhine` (`p000345`, `p000347`, `p000349`)
  - `Kampfgruppe Lergen` (`p000345`)
  - `Trung tướng Romel` (`p000345`)
  - `bản thổ Khối Thịnh vượng chung` (`p000347`)
  - `Trung tá Drake` (`p000349`)
  - `SIGINT` (`p000352`, `p000366`)
  - `giới tình báo Khối Thịnh vượng chung` (`p000354`)
  - `Tướng Habergram` / `Habergram` (`p000341`, `p000348`, `p000356`, `p000361`, `p000370`)
  - `PTSD` (`p000369`)
  - `đoàn tàu có hộ tống vũ trang` (`p000371`)
  - `U-boat` (`p000371`)
- Ghi nhận các thuật ngữ/cụm từ đề xuất mới trong lô (`status: pending`):
  - `commando strike` -> `cuộc tập kích biệt kích` (`p000347`)
  - `PTSD` -> `chứng PTSD` (`p000369`)
  - `armed convoys` -> `những đoàn tàu có hộ tống vũ trang` (`p000371`)
