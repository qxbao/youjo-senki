# Báo cáo tự kiểm (Self-Check): `vol-06-ch-05-b12`

## 1. Thông tin chung
- **Task ID**: `vol-06-ch-05-b12` (`vol-06-ch-05-b12-translator-signoff`)
- **Translator**: `argon-low`
- **Phạm vi đoạn**: `YS-LN06/Text/part0023.html/p000402` → `YS-LN06/Text/part0023.html/p000440` (39 đoạn)
- **Tệp bản dịch**: `translations/vol-06/ch-05-b12.jsonl`
- **Trạng thái dòng**: Tất cả 39 dòng đã được cập nhật sang `status: "reviewed"` sau khi đối chiếu với `reviews/prose/vol-06/ch-05-b12-argon-review.yml` (0 findings, khớp toàn bộ `pending_term_recommendations` và `locked_choices`).

## 2. Kiểm tra tính đầy đủ và siêu dữ liệu
- **Số dòng và thứ tự**: Đủ 39 dòng, khớp chính xác thứ tự `segment_id` với gói nguồn `work/vol-06/batches/ch-05-b12-source.jsonl`.
- **Trường bắt buộc**: Đầy đủ `segment_id`, `translation`, `status`, `translator`, `glossary_version`, `source_sha256`, `notes` trên mọi dòng.
- **Nhấn mạnh (`*...*`) theo `DEC-P01-002`**:
  - Chỉ duy nhất đoạn `YS-LN06/Text/part0023.html/p000423` có thẻ nhấn mạnh trong nguồn và đã được dịch là `*tuy nhiên…*`.
  - Toàn bộ 38 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và hoàn toàn không sử dụng dấu `*...*`.

## 3. Kiểm tra đại từ và quy chuẩn xưng hô (`DEC-P01-001`)
- **Trần thuật ngôi thứ ba**:
  - Tanya: dùng `nó` nhất quán xuyên suốt các câu trần thuật (`p000403`, `p000412`, `p000422`, `p000436`).
  - Trung tá Uger: dùng `anh` / `anh ta` (`p000403`, `p000405`, `p000412`, `p000413`, `p000418`, `p000428`, `p000434`).
  - Trung úy Serebryakov: dùng `cô` trong `p000403` (tiếp nối ngữ cảnh Serebryakov vừa báo tin ở cuối batch trước `p000401`).
- **Độc thoại nội tâm của Tanya**:
  - Ngôi thứ nhất số ít: dùng `mình` (`p000409`, `p000438`).
  - Ngôi thứ nhất số nhiều (chỉ phía Đế quốc / Lục quân Đế quốc): dùng `chúng ta` (`p000419`).
- **Đối thoại giữa Tanya và Trung tá Uger**:
  - Hai người có cùng cấp bậc Trung tá và là chỗ quen biết thân thiết từ Trường Đại học Quân sự, bàn bạc công việc trên tinh thần đồng cấp chuyên nghiệp.
  - Tanya xưng `tôi` (hoặc `chúng tôi` khi nói thay mặt đơn vị Kampfgruppe), gọi Uger là `anh` (`p000407`, `p000411`, `p000415`, `p000417`, `p000423`, `p000429`, `p000433`, `p000435`, `p000439`).
  - Uger xưng `tôi` (hoặc `chúng ta` khi nói chung về phía quân đội Đế quốc), gọi Tanya là `cô`, `Trung tá` hoặc `Trung tá von Degurechaff` (`p000406`, `p000408`, `p000414`, `p000416`, `p000418`, `p000426`, `p000428`, `p000434`, `p000436`).

## 4. Kiểm tra ngữ nghĩa, logic và thuật ngữ
- **Ngữ nghĩa và mạch lập luận**:
  - Giữ nguyên logic trao đổi về nút thắt cổ chai trên tuyến đường biển Norden, hệ thống tiếp vận vốn thiết kế cho tác chiến vùng núi cao, năng lực hạn chế của các tuyến đường sắt trước chiến tranh mới khôi phục một phần ở phía bắc Norden, và bài học xương máu khi tiếp tế cho quân thiết giáp ở đó (`p000406`–`p000416`).
  - Bảo toàn sự đối lập giữa việc pháo binh có thể dùng thiết bị dự trữ sẵn tại chỗ và nỗi lo ngại chiến lược khi dồn quân vào mà khó rút ra như vết xe đổ hồi chiến dịch Liên minh Hiệp ước bị Cộng hòa đánh vào sườn (`p000417`–`p000421`).
  - Giữ đúng lập luận của Tanya về bản chất đơn vị binh chủng hợp thành, sự vô lý nếu tách kíp lái xe tăng khỏi xe tăng để biến họ thành bộ binh nghiệp dư, cùng đề xuất thay thế bằng quân mô tô sử dụng xe chiến lợi phẩm thu từ Quân đội Cộng hòa do Cục Đường sắt nắm giữ với số lượng đủ đồng bộ cho một đại đội (`p000422`–`p000440`).
- **Thuật ngữ đã đối chiếu (`canon/glossary.yml`, `canon/glossary-pending.yml`, `work/run-state/pending-terms-index.yml`)**:
  - `Trung tá Uger` (`p000402`) — theo `pending-terms-index.yml`.
  - `Bộ Tổng tham mưu` (`p000404`, `p000409`) / `Bộ Tổng tham mưu Lục quân Đế quốc` (`p000420`) — theo `canon/glossary.yml`.
  - `quân du kích` (`p000407`, `p000428`) — theo `pending-terms-index.yml`.
  - `Norden` / `tuyến đường biển Norden` (`p000408`, `p000412`, `p000413`, `p000415`, `p000419`) — theo `canon/glossary.yml` và `pending-terms-index.yml`.
  - `Liên minh Hiệp ước` (`p000419`) — theo `canon/glossary.yml`.
  - `Cộng hòa` / `Quân đội Cộng hòa` (`p000419`, `p000430`) — theo `canon/glossary.yml` và `pending-terms-index.yml`.
  - `Đế quốc` (`p000420`) — theo `canon/glossary.yml`.
  - `Kampfgruppe` (`p000420`) — giữ nguyên theo `canon/glossary.yml`.
  - `đơn vị binh chủng hợp thành` (`p000424`) — theo `pending-terms-index.yml`.
  - `quân mô tô` (`p000426`, `p000427`) — diễn đạt sát nghĩa cho lực lượng cơ động bằng mô tô.
  - `các pháp sư Liên bang` (`p000428`) — theo `canon/glossary.yml` và `pending-terms-index.yml`.
  - `Cục Đường sắt` (`p000430`) — theo `pending-terms-index.yml`.
  - `Trung tá von Degurechaff` (`p000436`) — theo `pending-terms-index.yml`.
  - `chuyên gia hậu cần` (`p000437`, `p000439`) — theo `pending-terms-index.yml`.
  - `hậu phương` (`p000438`) — theo `pending-terms-index.yml`.
  - `vốn xã hội` (`p000438`) — theo `pending-terms-index.yml`.
