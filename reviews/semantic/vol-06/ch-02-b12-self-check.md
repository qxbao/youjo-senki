# Báo cáo tự kiểm (Self-Check): `vol-06-ch-02-b12`

- **Task ID**: `vol-06-ch-02-b12-translator-signoff` (parent: `vol-06-ch-02-b12`)
- **Phạm vi**: `YS-LN06/Text/part0013.html/p000036` .. `YS-LN06/Text/part0013.html/p000061` (26 đoạn)
- **Tác tử**: `argon-low`
- **Trạng thái dòng dịch**: `reviewed` (26/26 dòng)

## 1. Kiểm tra tính đầy đủ, bảo toàn nghĩa & xử lý Argon Review
- Đã dịch và rà soát đầy đủ toàn bộ 26 đoạn từ `p000036` đến `p000061`, giữ nguyên ranh giới đoạn 1-1 theo đúng mã đoạn (`segment_id`), giữ nguyên `source_sha256` và `glossary_version`, nâng `status` của toàn bộ 26/26 dòng từ `draft` lên `reviewed`.
- Đã xử lý đầy đủ 2 findings (`minor`) trong `reviews/prose/vol-06/ch-02-b12-argon-review.yml`:
  - `p000036`: Đổi `lời hứa trao trả độc lập của Đế quốc` thành `lời hứa trao độc lập của Đế quốc` để tránh sắc thái hiểu nhầm rằng Đế quốc từng tước đoạt rồi nay hoàn trả độc lập.
  - `p000044`: Đổi `các quan sát viên cài cắm tại chỗ` thành `các quan sát viên đi cùng đơn vị` để sát ngữ cảnh quân sự hơn (các quan sát viên/sĩ quan chính trị đi kèm các đơn vị Quân đội Liên bang).
- Bảo toàn chặt chẽ nghĩa, sắc thái, quan hệ nhân quả, phủ định, câu hỏi tu từ và tuân thủ toàn bộ `locked_choices`:
  - `p000036`–`p000042`: Loria chỉ ra vấn đề chính trị cốt lõi là lời hứa trao độc lập và giấc mộng tự quyết dân tộc của Đế quốc đã trở thành độc dược cực mạnh đối với Liên bang; phản ứng trái chiều trong phòng họp giữa những người hiểu chuyện và đám khờ khạo nhếch mép cười nhạo.
  - `p000043`–`p000049`: Báo cáo từ các quan sát viên đi cùng đơn vị về sự kháng cự quyết liệt của các nhóm vũ trang địa phương, thái độ thù địch đối với Quân đội Liên bang, và tin chấn động rằng Lục quân Đế quốc tin tưởng giao cả nhiệm vụ giữ gìn trật tự tại các vùng lãnh thổ bị chiếm đóng cho các nhóm sắc tộc thiểu số ly khai, giúp Đế quốc rảnh tay tiến hành lối tác chiến cơ động sở trường mà không sợ quân du kích quấy rối.
  - `p000050`–`p000055`: Loria tiết lộ thông tin khiến cả phòng họp lạnh toát về việc Lục quân Đế quốc và đám ly khai địa phương thiết lập mặt trận thống nhất kề vai sát cánh chiến đấu trên chiến trường, chứng tỏ niềm tin sâu sắc giữa hai bên và việc không thể trông cậy vào các đồng chí tại vùng bị chiếm đóng.
  - `p000056`–`p000061`: Một cán bộ đặt câu hỏi mang tính giáo điều về việc nhổ tận gốc đám ly khai từ trong bóng tối; Loria thầm ngán ngẩm trước câu trả lời sách vở xa rời thực tại chiến trường nhưng ngoài mặt vẫn bình tĩnh tán đồng rồi khéo léo dùng lời đe dọa ngầm cử chính người đó ra hiện trường kèm nụ cười hiền hậu.

## 2. Xưng hô, giọng điệu & điểm nhìn (`DEC-P01-001`)
- **Điểm nhìn Loria tại phòng họp ở Moskva (`p000036`–`p000061`)**:
  - Trần thuật gọi Loria là `gã`, tự quy chiếu là `mình` (`p000038`, `p000042`, `p000058`, `p000061`), nhất quán với `ch-02-b11` và các lô trước có Loria (`ch-01-b13`..`b16`).
  - Trong lời phát biểu và đối đáp chính thức tại cuộc họp (`p000036`, `p000041`, `p000045`, `p000050`, `p000055`, `p000056`, `p000059`, `p000060`, `p000061`), Loria và người chất vấn dùng `tôi` – `đồng chí` / `các đồng chí` và `chúng ta` / `chúng tôi` đúng văn phong chính trị Liên bang.
  - Trong câu độc thoại nội tâm mỉa mai đám cán bộ khờ khạo (`p000040`), Loria gọi họ là `các người` để giữ đúng sắc thái khinh miệt ngầm.

## 3. Bảo toàn nhấn mạnh (`DEC-P01-002`)
- Đối chiếu chính xác với thẻ nhấn mạnh trong trường `xhtml` của nguồn:
  - Chỉ sử dụng dấu `*...*` tại đúng 3 đoạn có thẻ nhấn mạnh trong nguồn:
    - `p000040`: `*Ààà, trình độ trí tuệ của các người quả thực hiện rõ mồn một trên mặt đấy…*`
    - `p000057`: `*Xét về mặt tuân thủ đường lối của Đảng thì đó là một đề xuất rất hay*`
    - `p000058`: `*Khốn nỗi, kiểu câu trả lời rập khuôn theo sách vở đó chẳng có chút ý nghĩa nào khi đem đặt trước thực tại chiến trường.*`
  - Toàn bộ 23 đoạn còn lại hoàn toàn không có dấu `*`.

## 4. Thuật ngữ & tính nhất quán với Canon / Pending Index
- Đã tra cứu và áp dụng nhất quán các thuật ngữ từ `canon/`, `work/run-state/pending-terms-index.yml` và `pending_term_recommendations` trong Argon review:
  - `Đế quốc` / `Lục quân Đế quốc` / `quân Đế quốc` (`p000036`, `p000041`, `p000045`, `p000047`, `p000048`, `p000050`).
  - `Liên bang` / `Quân đội Liên bang` / `Đảng Cộng sản Liên bang` / `Đảng` / `đường lối của Đảng` (`p000036`, `p000043`, `p000044`, `p000047`, `p000048`, `p000056`, `p000057`, `p000059`).
  - `đám ly khai` / `các nhóm sắc tộc thiểu số ly khai` / `đám ly khai địa phương` (`p000041`, `p000046`, `p000047`, `p000050`, `p000056`).
  - `các vùng lãnh thổ bị chiếm đóng` (`p000046`, `p000055`).
  - `quân du kích` (`p000048`).
  - `các sĩ quan chính trị` (`p000050`).
  - Các cụm thuật ngữ trong lô (trạng thái `pending`):
    - `quyền tự quyết dân tộc` (`p000041`)
    - `các quan sát viên đi cùng đơn vị` (`p000044`)
    - `tác chiến cơ động` (`p000048`)
    - `mặt trận thống nhất` (`p000050`, `p000051`, `p000054`)
