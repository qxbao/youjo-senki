# Báo cáo tự kiểm (Self-Check): `vol-09-ch-05-b02`

- **Phạm vi**: `YS-LN09/Text/chapter018.xhtml/p000034` – `YS-LN09/Text/chapter018.xhtml/p000066` (33 đoạn)
- **Người dịch**: `argon-low`
- **Trạng thái các dòng**: `reviewed`

## 1. Kiểm tra nghĩa, logic và dòng thời gian giả định
- Đảm bảo truyền tải đầy đủ đối lập giữa quân cảng Đế quốc (những hộp đen quân sự bí mật tuyệt đối, có boong-ke U-boat bằng bê tông) và cảng Ildoa (bầu không khí thoải mái tự nhiên, cập cầu tàu lộ thiên dưới bầu trời xanh thẫm, máy bay tiêm kích do Khối Thịnh vượng chung chế tạo nghiêng cánh chào, quân phục hồ phẳng phiu).
- Giữ đúng chuỗi suy luận của Tanya trên toa ăn thuộc Tuyến đường sắt Xuyên Ildoa (`p000049`–`p000066`): cảm giác bất thường khó tả từ lúc rời ga -> phỏng đoán khoảng cách giữa tiền tuyến và hậu phương -> chú ý tới chiếc bình nước bằng thủy tinh đặt trên bàn không cần cố định -> nhận ra tàu chạy rất êm và ít rung lắc -> kết luận công tác bảo trì đường sắt của Ildoa tốt hơn hẳn các tuyến đường sắt ra mặt trận phía đông của Lục quân Đế quốc.
- Giữ nguyên cấu trúc giả định ở `p000058` (nếu để nguyên như vậy mà toa tàu rung lắc thì sẽ vỡ) và `p000064` (nếu Trung tá Uger bên Cục Đường sắt có mặt thì hẳn sẽ giảng giải tường tận).

## 2. Kiểm tra đại từ và xưng hô (`DEC-P01-001`)
- Trong độc thoại nội tâm của Tanya: tự xưng `mình`, số nhiều bao gộp đơn vị dùng `chúng ta`.
- Trong các câu trần thuật ngôi thứ ba (`p000047`, `p000051`, `p000052`, `p000064`): dùng `Tanya` và đại từ `cô` nhất quán với các lô trước của Tập 9.
- Trong câu cảm thán mang sắc thái quảng cáo mỉa mai ở `p000048`: dùng `bạn` cho ngôi thứ hai khái quát và `chúng ta` cho chuyến đi của đơn vị.

## 3. Kiểm tra nhấn mạnh (`DEC-P01-002`)
- `p000035`: Đánh dấu nhấn mạnh `*thanh bình*` tương ứng với thẻ `<html:em>` trong nguồn.
- `p000050`: Đánh dấu nhấn mạnh toàn bộ câu tượng thanh `*Xình xịch, xình xịch. Xình xịch, xình xịch.*` tương ứng với thẻ `<html:em>`.
- `p000059`: Đánh dấu nhấn mạnh cụm từ tượng thanh `*xình xịch, xình xịch*` tương ứng với thẻ `<html:em>`.
- Các đoạn còn lại không có thẻ nhấn mạnh trong nguồn và không tự ý thêm dấu `*...*`.

## 4. Thuật ngữ và mục chờ xét (Pending Terms)
- Dùng nhất quán các phương án tạm đã có trong sổ pending:
  - `Ildoa` -> `Ildoa`
  - `the Empire` / `Imperial Army` -> `Đế quốc` / `Lục quân Đế quốc`
  - `U-boat` -> `U-boat` (`boong-ke U-boat` / `U-boat` / phân biệt với `tàu ngầm`)
  - `Commonwealth` -> `Khối Thịnh vượng chung`
  - `Colonel Calandro` -> `Đại tá Calandro`
  - `203rd Aerial Mage Battalion` -> `Tiểu đoàn Pháp sư Trên không số 203`
  - `submariners` -> `lính tàu ngầm`
  - `General Staff` -> `Bộ Tổng tham mưu`
  - `Lieutenant Colonel Uger` -> `Trung tá Uger`
  - `Railroad Department` -> `Cục Đường sắt`
  - `eastern front` -> `mặt trận phía đông`
- Thuật ngữ/địa danh mới ghi nhận tạm:
  - `Cross-Ildoa Railway` (`p000049`) -> `Tuyến đường sắt Xuyên Ildoa` (status: `pending`).
  - `U-boat bunkers` (`p000037`) -> `boong-ke U-boat` (status: `pending`).

## 5. Xử lý Argon Review Sign-off (`vol-09-ch-05-b02-argon-review`)
- `p000037`, `p000038`: Đổi `boong-ke tàu ngầm U-boat` thành `boong-ke U-boat` và `bằng tàu ngầm U-boat` thành `bằng U-boat` để bỏ từ giải thích ngoài nguồn và phân biệt rõ bề mặt từ vựng với `tàu ngầm` ở câu thứ hai của `p000038`.
- `p000041`, `p000044`: Đổi `đám người mà mình đoán là phái đoàn đón tiếp bên quân đội` thành `những người mà mình đoán là phái đoàn đón tiếp bên quân đội` và `đám quân nhân Ildoa` thành `các quân nhân Ildoa` để giữ sắc thái trung tính.
- `p000051`: Đổi `một cảm giác lạc lõng khó tả` thành `một cảm giác bất thường khó tả` để giữ đúng mạch nhận thức về sự bất thường của ngoại cảnh từ `p000051` đến `p000064`.
- Cập nhật `status` của toàn bộ 33 dòng trong `translations/vol-09/ch-05-b02.jsonl` từ `draft` sang `reviewed` và tuân thủ đầy đủ mọi `locked_choices`.
