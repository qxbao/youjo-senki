# Báo cáo tự kiểm (Semantic Self-Check) — vol-06-ch-01-b13

- **Task ID**: `vol-06-ch-01-b13`
- **Translator**: `argon-low`
- **Source Batch**: `work/vol-06/batches/ch-01-b13-source.jsonl` (`p000484`–`p000519`, 36 đoạn)
- **Output Translation**: `translations/vol-06/ch-01-b13.jsonl`

## 1. Kiểm tra tính đầy đủ và nghĩa
- Đã dịch đầy đủ toàn bộ 36 đoạn từ `YS-LN06/Text/part0008.html/p000484` đến `YS-LN06/Text/part0008.html/p000519`, giữ nguyên thứ tự và mã đoạn.
- Bảo toàn chính xác mạch nghĩa ở cả hai phân cảnh:
  - Phân cảnh 1 (`p000484`–`p000500`): Tanya giải thích mục tiêu chiến tranh tâm lý của chiến dịch bình định/trưng thu cho Thiếu tá Weiss (làm suy yếu tuyên truyền của Liên bang và tạo ấn tượng tốt với Hội đồng Tự trị), trao quyền áp dụng các biện pháp lâm thời nếu phát hiện quân nhà vi phạm quân luật, suy ngẫm nội tâm về nguyên tắc tự bảo toàn để giữ luật pháp đứng về phía mình sau chiến tranh, và hứa cấp mệnh lệnh bằng văn bản trước khi xuất kích.
  - Phân cảnh 2 (`p000501`–`p000519`): Chuyển cảnh sang phòng họp ngầm đặc biệt tại thủ đô Moskva của Liên bang. Ủy viên Dân ủy Nội vụ Loria quan sát bầu không khí u ám và thói quen bóp méo thực tế trong nội bộ Đảng Cộng sản, lắng nghe báo cáo của trưởng Ủy ban Kháng chiến tại các Vùng lãnh thổ bị Chiếm đóng về khó khăn của quân Đế quốc trước Tướng Mùa Đông, rồi chất vấn thẳng về sức chiến đấu thực tế mà Lục quân Đế quốc có thể huy động.
- Không bỏ sót vế câu, phủ định, điều kiện hay trạng thái nhận định nào.

## 2. Kiểm tra đại từ và xưng hô (`DEC-P01-001`)
- **Tanya von Degurechaff**:
  - Tự sự ngôi thứ ba: gọi là `Tanya` hoặc `nó` (`p000495`, `p000500`).
  - Độc thoại nội tâm: tự xưng `mình` / `chúng ta`, đại từ khái quát ngôi thứ hai dịch là `bạn` (`p000486`, `p000493`–`p000495`).
  - Thoại trực tiếp với cấp dưới (Thiếu tá Weiss): tự xưng `tôi` / `chúng ta`, gọi Weiss và nhóm của anh là `anh` / `các anh` (`p000485`, `p000487`, `p000489`, `p000491`, `p000496`, `p000498`).
- **Johann Weiss**:
  - Tự sự ngôi thứ ba: gọi là `Weiss` / `anh` (`p000488`, `p000500`).
  - Thoại trực tiếp với cấp trên (Tanya): tự xưng `tôi` / `chúng tôi`, gọi Tanya là `Trung tá` / `thưa Trung tá`, dùng kính ngữ quân sự chuẩn mực (`p000484`, `p000488`, `p000490`, `p000492`, `p000497`, `p000499`).
- **Loria và các cán bộ Liên bang**:
  - Tự sự ngôi thứ ba: gọi là `Ủy viên Dân ủy Nội vụ Loria` / `Loria` / `gã`; gọi trưởng Ủy ban Kháng chiến tại các Vùng lãnh thổ bị Chiếm đóng là `người đàn ông này` / `người đàn ông kia` / `ông ta`.
  - Độc thoại nội tâm trực tiếp của Loria (`p000503`): tự xưng `mình` / `chúng ta`, gọi các ủy viên khác là `các đồng chí`.
  - Thoại trong cuộc họp (`p000508`, `p000511`, `p000512`, `p000514`, `p000518`): tự xưng `tôi` / `chúng ta`, gọi nhau là `đồng chí` / `các đồng chí`, gọi quân Đế quốc là `quân Đế quốc` / `Lục quân Đế quốc` / `chúng` / `quân địch`.

## 3. Kiểm tra nhấn mạnh (`DEC-P01-002`)
- Chỉ sử dụng dấu `*...*` ở đúng 3 đoạn có thẻ nhấn mạnh trong nguồn XHTML:
  - `YS-LN06/Text/part0008.html/p000489`: `*làm lợi cho kẻ địch*`
  - `YS-LN06/Text/part0008.html/p000503`: `*Các đồng chí của mình trông ủ dột có lẽ là vì việc đọc báo cáo với gương mặt đưa đám đã trở thành căn bệnh kinh niên trong hàng ngũ chúng ta mất rồi*`
  - `YS-LN06/Text/part0008.html/p000517`: `*hiểu được*` và `*tôn trọng*`
- Toàn bộ 33 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và hoàn toàn không dùng dấu `*...*`.

## 4. Thuật ngữ và mục đề xuất (Pending Terms)
- Đã tuân thủ nhất quán thuật ngữ canon và pending terms: `Liên bang`, `Lục quân Đế quốc`, `Bộ Tổng tham mưu`, `Moskva`, `Ủy viên Dân ủy Nội vụ Loria`, `Đảng Cộng sản`, `Tướng Mùa Đông`.
- Các mục đề xuất / tạm dùng nhất quán theo báo cáo review Argon (`ch-01-b13-argon-review.yml`):
  - `Hội đồng Tự trị` (`YS-LN06/Text/part0008.html/p000487`, đã cập nhật từ `Hội đồng Tự quản` theo finding và locked_choices trong argon-review).
  - `chiến dịch giám sát và bình định đặc biệt` (`YS-LN06/Text/part0008.html/p000498`).
  - `Ủy ban Kháng chiến tại các Vùng lãnh thổ bị Chiếm đóng` (`YS-LN06/Text/part0008.html/p000506`, `p000519`).

## 5. Xử lý Argon Review Sign-off (`vol-06-ch-01-b13-translator-signoff`)
- **Finding xử lý**:
  - `YS-LN06/Text/part0008.html/p000487` (`moderate`, `terminology_consistency`): Đổi `Hội đồng Tự quản` thành `Hội đồng Tự trị` theo đúng `recommendation` và `locked_choices`.
- **Trạng thái (`status`)**: Đã cập nhật toàn bộ 36 dòng trong `translations/vol-06/ch-01-b13.jsonl` từ `draft` sang `reviewed`.
