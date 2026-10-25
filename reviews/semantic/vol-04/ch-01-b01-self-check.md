# Báo cáo tự kiểm tra ngữ nghĩa — Batch `vol-04-ch-01-b01`

- **Phạm vi**: `YS-LN04/Text/chapter001_b.xhtml/p000001` – `YS-LN04/Text/chapter001_b.xhtml/p000023` (23 đoạn)
- **Người dịch**: `argon-low`
- **Trạng thái bản dịch**: `reviewed`

## 1. Kiểm tra tính toàn vẹn và đối chiếu với nguồn
- Toàn bộ 23 đoạn từ `chapter001_b.xhtml/p000001` đến `chapter001_b.xhtml/p000023` đã được dịch đầy đủ, giữ nguyên thứ tự, mã đoạn (`id`) và `source_sha256` (`d753e588b788516ce336d1cf80988217124eba4e9a380a1881bc8efb45e4467f`).
- Không làm rò rỉ câu văn hay trích đoạn tiếng Anh từ nguồn vào báo cáo hoặc ghi chú.

## 2. Xưng hô, đại từ và giọng văn (`DEC-P01-001`)
- **Trần thuật và độc thoại nội tâm của Tanya (`p000010`–`p000023`)**:
  - Ngôi kể khách quan dùng `nó` cho Thiếu tá Tanya von Degurechaff (`p000013`, `p000017`, `p000019`–`p000023`) và giữ nguyên cách gọi tên/chức danh (`Thiếu tá Tanya von Degurechaff`, `Chỉ huy von Degurechaff`) theo đúng quy ước `DEC-P01-001`.
  - Nội tâm tự quy chiếu của Tanya ở ngôi thứ nhất số ít dùng `mình` (`p000011`, `p000013`, `p000016`).
  - Khi Tanya tự quy chiếu tập thể Tiểu đoàn Pháp sư Trên không số 203 ở ngôi thứ nhất số nhiều (`p000014`–`p000015`), dùng `chúng tôi` nhất quán, phân biệt rõ với lời dẫn chuyển cảnh của người kể chuyện ở `p000018`.
- **Lời nói giả định của các sĩ quan Bộ Tổng tham mưu (`p000007`)**:
  - Khi các sĩ quan Bộ Tổng tham mưu ghé qua trung tâm điều hành phòng không để yêu cầu không ghi nhận báo cáo, dùng `Các anh` cho nhân viên kiểm soát radar để phù hợp ngữ cảnh quân sự.

## 3. Bảo toàn nhấn mạnh (`DEC-P01-002`)
- Chỉ 3 đoạn có thẻ nhấn mạnh trong XHTML gốc và đã được bảo toàn chính xác bằng dấu `*...*` đúng phạm vi nhấn mạnh của nguồn:
  - `chapter001_b.xhtml/p000007`: cụm câu nói giả định `*Các anh đã không nhìn thấy gì hết*`
  - `chapter001_b.xhtml/p000011`: toàn bộ câu nội tâm `*Tất cả những gì mình muốn là có ai đó đổi chỗ cho mình.*`
  - `chapter001_b.xhtml/p000016`: cụm lời than thở `*Mình không muốn chiến đấu, nhưng xem chừng lúc này khó lòng mà trốn thoát được*`
- Toàn bộ 20 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và không phát sinh dấu `*...*` ngoài nguồn.

## 4. Thuật ngữ và tính nhất quán nội bộ
- **Thuật ngữ đã khóa / tiếp nối từ các tập trước và sổ pending**:
  - `Năm Thống nhất` (`p000001`), `Lục quân Đế quốc` (`p000002`, `p000009`, `p000014`), `Bộ Tổng tham mưu` (`p000007`, `p000008`, `p000014`), `Cụm tập đoàn quân phía Đông` (`p000007`), `Tiểu đoàn Pháp sư Trên không số 203` (`p000014`), `Thiếu tá Tanya von Degurechaff` (`p000012`), `Chỉ huy von Degurechaff` (`p000015`), `thủ đô Đế quốc` (`p000017`, `p000019`), `đơn vị huấn luyện` (`p000020`), `mặt trận phía nam` (`p000023`).
  - Dòng tiêu đề thời gian – địa điểm ở mở đầu chương được viết hoa toàn bộ (`p000001`): `NGÀY 15 THÁNG 3, NĂM THỐNG NHẤT 1926, TRÊN BẦU TRỜI VÙNG BIÊN GIỚI PHÍA ĐÔNG ĐẾ QUỐC`.
- **Đề xuất thuật ngữ tạm mới (`pending_terms`)**:
  - `Đơn vị Vận tải Hàng không Lục quân Đế quốc` (`p000002`) — dịch sát nghĩa đơn vị vận tải đường không trực thuộc Lục quân Đế quốc.
  - `Trung tâm Điều hành Tác chiến Phòng không phía Đông` (`p000007`) — kế thừa cấu trúc `Trung tâm Điều hành Tác chiến` trong sổ pending và bổ sung thành tố phòng không phía Đông.
  - `đội tác chiến đặc biệt` (`p000006`, `p000009`, `p000012`) — dịch thống nhất cho cách gọi nhóm đặc nhiệm không quân/pháp sư thực hiện nhiệm vụ mật vượt biên giới.
  - `công việc bẩn thỉu` (`p000008`) — diễn đạt tự nhiên ẩn dụ ám sát/phi vụ đen tối mà Bộ Tổng tham mưu giao phó khi cấp bách.

## 5. Sign-off (`vol-04-ch-01-b01-translator-signoff`)
- **Báo cáo review**: `reviews/prose/vol-04/ch-01-b01-argon-review.yml` (`status: approved_for_polish`, `serious: 0`, `moderate: 0`, `minor: 0`, `findings: []`).
- **Xử lý findings**: Không có finding cần chỉnh sửa nội dung. Giữ nguyên toàn bộ `locked_choices` từ `p000001` đến `p000023`.
- **Cập nhật trạng thái**: Đã chuyển `status` của toàn bộ 23 dòng trong `translations/vol-04/ch-01-b01.jsonl` từ `draft` sang `reviewed`.
