# Báo cáo tự kiểm (Self-Check): `vol-06-ch-02-b10`

- **Task ID**: `vol-06-ch-02-b10-translator-signoff` (parent: `vol-06-ch-02-b10`)
- **Phạm vi**: `YS-LN06/Text/part0011.html/p000404` .. `YS-LN06/Text/part0011.html/p000466` (63 đoạn)
- **Tác tử**: `argon-low`
- **Trạng thái dòng dịch**: `reviewed`

## 1. Kiểm tra tính đầy đủ & bảo toàn nghĩa
- Toàn bộ 63 đoạn từ `p000404` đến `p000466` đã được dịch và rà soát đầy đủ, giữ nguyên phân tách đoạn 1-1 theo đúng mã đoạn (`segment_id`), cập nhật trạng thái sang `reviewed` và khớp `source_sha256`.
- Đã tiếp nhận và xử lý đầy đủ 4 findings trong báo cáo Argon Review (`reviews/prose/vol-06/ch-02-b10-argon-review.yml`):
  - `p000404` (moderate): Đổi `đại đội ma đạo` -> `đại đội pháp sư`, `đơn vị ma đạo` -> `đơn vị pháp sư` để thống nhất hệ thống thuật ngữ trong sổ pending tập 1–6.
  - `p000407` (minor): Đổi `về cố hương` -> `về chính quốc` để khớp ngữ cảnh đưa tù binh Liên bang về lãnh thổ Khối Thịnh vượng chung của Drake (đồng bộ với `ch-02-b09`).
  - `p000436` (moderate): Đổi `ma đạo sĩ` -> `pháp sư`.
  - `p000442` (moderate): Đổi `ma đạo sĩ` -> `các pháp sư`.
- Tuân thủ toàn bộ `locked_choices` từ `p000404` đến `p000466`.

## 2. Xưng hô, giọng điệu & điểm nhìn (`DEC-P01-001`)
- **Nửa đầu (`p000404`–`p000435`, góc nhìn ngôi thứ ba theo Trung tá Drake)**:
  - Trần thuật gọi Drake là `ông`, độc thoại nội tâm tự xưng `mình`.
  - Đối thoại giữa Drake và Trung úy Mary Sue (`p000405`–`p000407`, `p000431`): Drake gọi `Trung úy Sue` / `Trung úy` / `cô`, xưng `tôi` / `chúng ta`; Mary Sue đáp lễ phép `thưa Trung tá`.
  - Đối thoại giữa Drake và nữ sĩ quan chính trị Liên bang (`p000415`–`p000429`, `p000433`–`p000434`): giữ khoảng cách ngoại giao - quân sự (`tôi` / `chúng tôi` – `ngài` / `các ngài` / `thưa Trung tá`); khi nhắc tới Trung tá Mikel ở `p000415`–`p000416`, giữ nhất quán với các batch trước là `Trung tá Mikel` và `Đồng chí Trung tá`.
- **Nửa sau (`p000436`–`p000466`, góc nhìn ngôi thứ ba theo Mary Sue)**:
  - Trần thuật gọi Mary là `cô`.
  - Trong lời độc thoại tự nhủ và dòng suy nghĩ nội tâm (`p000447`, `p000452`–`p000461`, `p000463`), Mary tự xưng `mình` (và `chúng ta` khi nói về tập thể đồng đội/quê hương ở `p000452`, `p000459`, `p000460`), thể hiện đúng tâm lý tự vấn và quyết tâm dồn nén của nhân vật.

## 3. Bảo toàn nhấn mạnh (`DEC-P01-002`)
- Đối chiếu chính xác với thẻ nhấn mạnh trong trường `xhtml` của nguồn:
  - Chỉ sử dụng dấu `*...*` tại đúng 13 đoạn có thẻ nhấn mạnh trong nguồn: `p000405`, `p000407`, `p000418`, `p000428`, `p000432`, `p000453`, `p000454`, `p000455`, `p000456`, `p000458`, `p000459`, `p000460`, `p000463`.
  - Toàn bộ 50 đoạn còn lại hoàn toàn không có dấu `*`.

## 4. Thuật ngữ & tính nhất quán với Canon / Pending Index
- ` đại đội pháp sư` / `đơn vị pháp sư` / `pháp sư` / `các pháp sư` (`p000404`, `p000436`, `p000442`).
- `Trung úy Sue` / `Trung úy` (`p000405`, `p000431`).
- `tàu RMS *Queen of Anjou*` / `chính quốc` (`p000407`).
- `Bộ binh Liên bang` (`p000412`).
- `viên sĩ quan chính trị` / `sĩ quan chính trị` (`p000414`, `p000418`, `p000426`).
- `Trung tá Mikel` / `Đồng chí Trung tá` (`p000415`, `p000416`).
- `Đảng Cộng sản` (`p000425`).
- `tòa án quân sự` / `xử bắn` (`p000429`).
- `vừa đánh vừa rút lui` (`p000434`).
- `đơn vị chặn hậu` / `đội phản ứng nhanh` (`p000441`, `p000442`).
- `Lục quân Đế quốc` / `Ác quỷ sông Rhine` (`p000446`).
