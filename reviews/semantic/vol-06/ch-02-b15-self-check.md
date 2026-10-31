# Báo cáo tự kiểm dịch thuật: `vol-06-ch-02-b15`

## 1. Thông tin chung
- **Task ID**: `vol-06-ch-02-b15`
- **Phạm vi**: `YS-LN06/Text/part0013.html/p000144` đến `YS-LN06/Text/part0013.html/p000183` (40 phân đoạn)
- **Người dịch**: `argon-low`
- **Trạng thái**: `reviewed` (đã hoàn tất sign-off sau review của Argon)

## 2. Kiểm tra quy chuẩn xưng hô và giọng văn (`DEC-P01-001`)
- **Trung tá Drake**:
  - Trần thuật: dùng `ông` nhất quán nối tiếp từ `ch-02-b14`.
  - Thoại trực tiếp với Đại tá Mikel (trong vở kịch tranh cãi trước mặt các sĩ quan chính trị và thông dịch viên): xưng `tôi`, gọi `ông`.
  - Thoại trực tiếp quát Liliya (`p000181`): xưng `tôi`, gọi `cô`.
  - Độc thoại nội tâm (`p000163`, `p000166`, `p000174`, `p000175`, `p000183`): xưng `tôi` / `chúng ta`, giữ đúng sắc thái quyết đoán, châm biếm ngầm và kìm nén cơn giận đối với sĩ quan chính trị Liên bang.
- **Đại tá Mikel**:
  - Trần thuật: dùng `ông`.
  - Thoại trực tiếp với Drake: xưng `tôi`, gọi `ông`.
  - Thoại trực tiếp với Liliya (`p000170`, `p000176`): gọi `Đồng chí Trung úy Tanechka`, xưng `tôi` - `đồng chí` đúng chuẩn quân đội Liên bang.
- **Liliya Ivanova Tanechka**:
  - Trần thuật: dùng `cô ta` (phản ánh góc nhìn khó chịu của Drake đối với sĩ quan chính trị).
  - Thoại trực tiếp với Mikel (`p000171`, `p000177`, `p000182`): xưng `tôi`, gọi `Trung tá Drake` (theo quy chuẩn cấp bậc thực tế của Drake trong hồ sơ thuật ngữ) và `Trung úy Sue`.

## 3. Kiểm tra nhấn mạnh (`DEC-P01-002`)
- Chỉ sử dụng dấu `*...*` tại đúng 6 phân đoạn có thẻ nhấn mạnh trong nguyên tác:
  - `p000158`: hai cụm nhấn mạnh đối lập trong cuộc cãi vã.
  - `p000163`: toàn bộ câu khẳng định quyền chỉ huy tối cao.
  - `p000166`: toàn bộ câu cảm thán nội tâm về thời đại phi lý.
  - `p000174`: mệnh đề châm ngôn đầu đoạn.
  - `p000175`: câu suy nghĩ nội tâm về điểm đột phá.
  - `p000183`: câu quát tháo mà Drake cố kìm nén ở cuối đoạn.
- Các phân đoạn còn lại hoàn toàn không thêm dấu nhấn mạnh ngoài nguồn.

## 4. Thuật ngữ, tính nhất quán và xử lý review (`ch-02-b15-argon-review`)
- Đã tiếp nhận finding minor tại `p000167`: đồng bộ `Quân đội Khối Thịnh vượng chung` thành `Lục quân Khối Thịnh vượng chung` để khớp nhất quán với sổ pending các tập trước và Tập 6.
- Duy trì nhất quán với `canon/glossary.yml`, `work/run-state/pending-terms-index.yml`, `locked_choices` trong `ch-02-b15-argon-review.yml` và `ch-02-b14`:
  - `Khối Thịnh vượng chung`, `Lục quân Khối Thịnh vượng chung`, `Liên bang`, `Đảng`.
  - `nhiệm vụ trinh sát chiến đấu` (`p000146`), `chiến hữu vào sinh ra tử` (`p000147`), `quyền giam giữ tù binh` (`p000153`), `phương ngữ Nữ hoàng` (`p000155`), `sĩ quan chính trị` / `chính ủy` (`p000155`, `p000162`, `p000164`, `p000167`, `p000168`, `p000176`, `p000182`), `hệ thống chỉ huy` (`p000176`).
  - Cấp bậc và danh xưng: `Trung tá Drake`, `Đồng chí Trung úy Tanechka`, `Trung úy Sue`.
- Đảm bảo bảo toàn trọn vẹn nghĩa, phủ định, đối tượng chất vấn, toàn bộ `locked_choices` và đã chuyển trạng thái toàn bộ 40 phân đoạn sang `reviewed`.
