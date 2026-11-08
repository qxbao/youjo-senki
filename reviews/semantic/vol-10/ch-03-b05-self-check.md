# Báo cáo tự kiểm (Semantic Self-Check) — `vol-10-ch-03-b05`

- **Task ID:** `vol-10-ch-03-b05` (Sign-off: `vol-10-ch-03-b05-translator-signoff`)
- **Translator:** `argon-low`
- **Phạm vi:** `YS-LN10/Text/chapter018.xhtml/p000030` .. `YS-LN10/Text/chapter018.xhtml/p000063` (34 đoạn)
- **Tệp đích:** `translations/vol-10/ch-03-b05.jsonl`
- **Glossary Version:** `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra tính đầy đủ và cấu trúc dữ liệu
- **Số lượng đoạn:** Đầy đủ 34/34 đoạn từ `p000030` đến `p000063`, khớp 1:1 với tệp nguồn.
- **Trạng thái & siêu dữ liệu:** Toàn bộ 34 dòng đã được cập nhật sang `status: "reviewed"`, giữ `translator: "argon-low"`, `source_sha256` và `glossary_version` khớp với handoff.
- **Nhấn mạnh (`DEC-P01-002`):** Đã kiểm tra và bảo toàn chính xác đánh dấu `*...*` ở đúng 2 đoạn có thẻ nhấn mạnh trong nguồn:
  - `p000042`: `*diễn giải lại*`
  - `p000052`: `*ngay trên sân nhà của chúng*`
  - Các đoạn còn lại không tự ý thêm dấu `*...*`.

## 2. Xử lý Findings từ Argon Review (`reviews/prose/vol-10/ch-03-b05-argon-review.yml`)
- **`p000053` (minor):** Tiếp nhận đề xuất của reviewer để tránh trùng bề mặt với đại từ nội tâm ngôi thứ nhất `mình` của Tanya; chỉnh từ `"cũng chỉ giới hạn các hành động phòng ngự của mình trong phạm vi thế lực của bản thân"` thành `"cũng chỉ giới hạn các hành động phòng ngự trong phạm vi thế lực của ông ta"`, vừa phân tách rõ ngôi thứ ba (Shimazu) theo `DEC-P01-001`, vừa tuân thủ đầy đủ `locked_choices`.
- **`p000055` (minor):** Tiếp nhận đề xuất của reviewer để hợp văn cảnh bàn luận tình hình chiến lược quân sự; chỉnh từ `"có rất nhiều tình tiết đang tác động ở đây"` thành `"có rất nhiều hoàn cảnh đang tác động ở đây"`, giữ nguyên mọi `locked_choices` của đoạn.
- **Toàn bộ `locked_choices` (`p000030`..`p000063`):** Đã đối chiếu và bảo toàn 100%.

## 3. Xưng hô, điểm nhìn và giọng điệu (`DEC-P01-001` & `style-guide.md`)
- **Độc thoại nội tâm & trần thuật của Tanya:** Giữ nhất quán đại từ ngôi thứ nhất `mình` (`p000030`, `p000033`, `p000036`, `p000037`, `p000039`, `p000043`, `p000049`, `p000060`), lối tự quy chiếu tách ngôi bằng tên riêng `Tanya` (`p000036`), và `chúng ta` khi nói chung về phe Đế quốc (`p000045`), đồng bộ với lô `ch-03-b04` ngay trước đó.
- **Thoại quân sự giữa Tướng Romel và Trung tá Tanya von Degurechaff:**
  - Tướng Romel gọi Tanya là `Trung tá` / `Bạch Ngân` / `cô`, tự xưng `ta` (hoặc `chúng ta` khi nói chung về hai bên hay phe Đế quốc ở `p000035`, `p000047`, `p000055`), giọng tự tin, áp đặt nhưng vẫn khuyến khích tranh luận (`p000031`, `p000035`, `p000041`, `p000047`, `p000051`, `p000055`, `p000057`, `p000059`, `p000062`).
  - Tanya gọi Tướng Romel là `thưa Tướng quân` / `ngài`, tự xưng `tôi`, kèm `ạ` giữ lễ tiết quân sự nhưng phản biện sắc sảo (`p000032`, `p000034`, `p000038`, `p000040`, `p000042`, `p000044`, `p000048`, `p000050`, `p000054`, `p000056`, `p000061`, `p000063`). Trong câu hỏi tu từ nội tâm hướng tới cấp trên ở `p000052`, dùng `ngài` để giữ mạch đối chất ngầm.

## 4. Thuật ngữ và phương án Pending (`pending_term_recommendations`)
- Toàn bộ 10 mục `pending_term_recommendations` trong `ch-03-b05-argon-review.yml` đều đã được áp dụng đồng bộ và nhất quán:
  - `field officer` -> `sĩ quan thực địa` (`p000030`, `p000035`)
  - `General Romel / Colonel / sir` -> `Tướng Romel / Trung tá / thưa Tướng quân (ngài)` (`p000033`, `p000035`, `p000041`, `p000043`, `p000055`, `p000056`, `p000058`)
  - `strategic defense / defensive strategy / defensive posture` -> `phòng ngự chiến lược / chiến lược phòng ngự / thế bố trí phòng ngự` (`p000034`, `p000048`, `p000055`)
  - `Commonwealth waters / maritime superpower` -> `vùng biển của Khối Thịnh vượng chung / siêu cường hàng hải` (`p000045`)
  - `coordinated naval strike / naval infantry` -> `đòn tập kích đường biển hiệp đồng / hải quân đánh bộ` (`p000050`)
  - `western front / eastern front` -> `mặt trận phía tây / mặt trận phía đông` (`p000051`, `p000060`)
  - `Shimazu` -> `Shimazu` (`p000053`)
  - `White Silver` -> `Bạch Ngân` (`p000057`)
  - `Federation / Communism / nationalism` -> `Liên bang / Chủ nghĩa Cộng sản / chủ nghĩa dân tộc` (`p000059`, `p000061`)
  - `General Zettour` -> `Tướng Zettour` (`p000063`)

## 5. Kiểm tra ngữ nghĩa, phủ định và giả định
- `p000034`: Bảo toàn thành ngữ tương đương (`chỉ hươu bảo ngựa`) và mức độ phủ định (`khó lòng gọi đây là phòng ngự chiến lược`).
- `p000044`: Bảo toàn cấu trúc đối lập (`Không phải để đánh chặn mà là để xông thẳng vào lãnh thổ địch!`).
- `p000045`, `p000048`, `p000052`: Bảo toàn chính xác mục tiêu và sắc thái mỉa mai của các câu hỏi chất vấn về ranh giới giữa phòng ngự và tấn công.
- `p000054`: Bảo toàn quan hệ nhân quả trong lập luận của Tanya (`Gọi đây là phòng ngự thì đã xóa sổ luôn khái niệm tiến công ngay từ đầu rồi`).
