# Báo cáo tự kiểm ngữ nghĩa — `vol-10-ch-05-b17`

- **Task ID**: `vol-10-ch-05-b17-translator-signoff` (parent: `vol-10-ch-05-b17`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter024.xhtml/p000602` → `YS-LN10/Text/chapter024.xhtml/p000653` (52 đoạn)
- **Tập tin bản dịch**: `translations/vol-10/ch-05-b17.jsonl`

## 1. Kiểm tra tính đầy đủ, cấu trúc và xử lý Argon Review

- Đã dịch và rà soát đầy đủ 52/52 đoạn từ `p000602` đến `p000653`, khớp hoàn toàn thứ tự và mã định danh.
- Toàn bộ 52 dòng đã được cập nhật `status: "reviewed"`, giữ `translator: "argon-low"`, `source_sha256` và `glossary_version` khớp với `handoffs/vol-10/ch-05-b17.yml`.
- Xử lý đầy đủ 2 findings (`minor`) trong `reviews/prose/vol-10/ch-05-b17-argon-review.yml`:
  - `p000618`: Đổi `cho chúng biết mình đang phải đối đầu với ai` thành `cho chúng biết chúng đang phải đối đầu với ai` để quy chiếu chủ thể rõ nghĩa tức thì.
  - `p000619`: Đổi `khi bản thân lỡ lời` thành `khi bản thân trót phạm phải` để giữ trọn độ mở về việc nhận ra sai lầm của Tanya trong độc thoại nội tâm.
- Tuân thủ đầy đủ toàn bộ `pending_term_recommendations` và `locked_choices` từ `p000602` đến `p000653`.
- Không bỏ sót câu, mệnh đề, phủ định, giả định hay quan hệ nhân quả nào trong toàn bộ lô.

## 2. Xưng hô, điểm nhìn và giọng văn

- **Độc thoại nội tâm của Tanya** (`p000602`–`p000604`, `p000607`–`p000609`, `p000611`, `p000613`, `p000615`, `p000619`–`p000621`): Giữ nhất quán đại từ tự xưng `mình`, gọi chung đơn vị là `chúng ta`, giữ đúng sự lệch pha hài hước đen giữa góc nhìn tự cho mình là người duy nhất tỉnh táo của Tanya với thực tế chiến trường.
- **Đối thoại giữa Tanya và Trung úy Serebryakov (Visha)** (`p000605`–`p000607`, `p000612`, `p000614`, `p000616`–`p000618`):
  - Tanya gọi Visha là `Trung úy`, xưng `tôi` – `cô`, gọi chung đơn vị là `chúng ta`.
  - Visha gọi Tanya là `thưa Trung tá`, thêm tiểu từ lễ phép `ạ` (`p000606`, `p000616`, `p000618`), giữ đúng giọng điệu hào hứng đẫm máu đối lập với vẻ ngoài hiền lành.
- **Lời hô hào trên kênh liên lạc mở của Trung tá Drake** (`p000610`): Giữ nguyên hoàn toàn câu dịch đã khóa ở `p000535` (lô `b15`) để đảm bảo tính nhất quán tuyệt đối khi Tanya nghe lại đúng lời hô của Drake trên sóng vô tuyến.
- **Trần thuật góc nhìn Trung tá Drake và toàn cảnh chiến trường** (`p000622`–`p000653`):
  - Dùng đại từ `anh` cho `Trung tá Drake`, phân biệt rõ lời dẫn với câu cảm thán nội tâm của Drake ở `p000630`.
  - Đối thoại giữa Drake và sĩ quan phụ tá (`p000626`, `p000628`, `p000631`, `p000632`, `p000634`, `p000635`): cấp dưới xưng `chúng tôi` / `chúng ta`, gọi `thưa Trung tá`; Drake giữ giọng điệu quyết liệt, phong trần của lính hải quân đánh bộ.
  - Khắc họa nhịp độ dồn dập, cân sức của cuộc đọ hỏa lực trực diện giữa hai tiểu đoàn tinh nhuệ ở độ cao lớn (`p000636`–`p000653`).

## 3. Thuật ngữ và tính nhất quán với Canon / Pending Terms

- `thuật thức bắn tỉa quang học` (`p000603`)
- `thuật thức nghi binh` / `các thuật thức mồi nhử và nghi binh` (`p000603`, `p000648`)
- `các pháp sư Khối Thịnh vượng chung` / `tiếng Khối Thịnh vượng chung` / `quân đội Khối Thịnh vượng chung` / `Đơn vị dự bị của Khối Thịnh vượng chung` (`p000603`, `p000608`, `p000614`, `p000619`, `p000630`, `p000653`)
- `bản thổ` (`p000614`)
- `viên sĩ quan phụ tá` (`p000615`, `p000633`)
- `Trung tá Drake` (`p000623`, `p000627`)
- `Trung úy Sue` (`p000624`)
- `Chỉ huy` / `Trung tướng Ballmer` (`p000625`)
- `pháp sư Đế quốc` (`p000629`)
- `lớp vỏ phòng thủ` (`p000641`)
- `thuật thức phát nổ` (`p000648`, `p000649`)
- `lưỡi kiếm ma pháp` (`p000649`)

## 4. Kiểm tra định dạng nhấn mạnh (`DEC-P01-002`) và dấu câu đặc biệt

- Chỉ sử dụng dấu `*...*` tại đúng 3 đoạn có nhấn mạnh (`<html:em>`) trong nguồn:
  - `p000602`: `*rõ*`
  - `p000625`: `*Trung tướng Ballmer*`
  - `p000630`: `*Lũ chó Đế quốc đó bị cái quái gì thế không biết?*`
- 49 đoạn còn lại hoàn toàn không chứa ký tự `*`.
- Bảo toàn dấu ngoặc kép đôi `““...””` tại `p000637` và `p000643` để biểu thị lời hô đồng thanh của hai vị chỉ huy ở hai đầu chiến tuyến theo đúng bản gốc.
