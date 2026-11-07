# Báo cáo tự kiểm (Self-Check): `vol-08-ch-05-b09`

- **Task ID**: `vol-08-ch-05-b09`
- **Phạm vi**: `YS-LN08/Text/chapter018.xhtml/p000288` – `YS-LN08/Text/chapter018.xhtml/p000329` (42 đoạn)
- **Người dịch**: `argon-low`
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`
- **Source SHA256**: `b5e55889614fa6fbd3f59c099ac5b761978d880d2feea29cd7355a432a65d2a4`

## 1. Kiểm tra tính toàn vẹn & định dạng
- Đã dịch đầy đủ 42/42 đoạn theo đúng thứ tự từ `p000288` đến `p000329`, không gộp dòng, không tách dòng, không bỏ sót bất kỳ mệnh đề hay câu văn nào.
- Tất cả các dòng đều có `"status": "reviewed"`, `"translator": "argon-low"`, đầy đủ `glossary_version` và `source_sha256` khớp với `handoffs/vol-08/ch-05-b09.yml`.
- Bảo toàn chính xác đánh dấu nhấn mạnh (`*...*`) theo đúng quy định `DEC-P01-002`: chỉ hai đoạn `p000291` và `p000300` có thẻ nhấn mạnh trong XHTML gốc được bọc dấu sao `*...*`; 40 đoạn còn lại hoàn toàn không tự ý thêm in nghiêng hay in đậm.
- **Cập nhật Sign-off (`vol-08-ch-05-b09-translator-signoff`)**:
  - Đã tiếp nhận toàn bộ 2 findings mức `minor` từ `reviews/prose/vol-08/ch-05-b09-argon-review.yml`:
    - `p000298`–`p000299`: Chỉnh thành `Nhưng ông đã xoay xở phá nhỏ được nó ra.` và `Việc đập vụn nó thành đống đá vụn không còn chỉ là một giấc mơ nữa.` để giữ trọn mạch ẩn dụ ngọn núi việc từ `p000297`.
    - `p000306` & `p000318`: Lược bỏ các từ giải thích thêm (`sự ngang bướng`, `xương máu`, `thay thế`) để bám sát phong cách trần thuật trực tiếp của bản gốc.
  - Đã đối chiếu tuân thủ đầy đủ toàn bộ `pending_term_recommendations` và `locked_choices` cho cả 42 đoạn (`p000288`–`p000329`), đồng thời chuyển `status` toàn bộ 42 dòng từ `draft` sang `reviewed`.

## 2. Xưng hô & giọng nhân vật (`DEC-P01-001`)
- **Trần thuật ngôi thứ ba theo góc nhìn Zettour**: Gọi Zettour là `Zettour` / `ông`, Cramm là `Chỉ huy Cramm` / `anh ta`, Grantz là `một trung úy` / `Grantz` / `vị trung úy`, Schulz là `Chuẩn tướng Schulz` / `Phó chỉ huy Schulz`.
- **Đối thoại giữa Chỉ huy Cramm và Trung tướng von Zettour (`p000288`–`p000294`)**:
  - Cramm nói với Zettour (`p000288`, `p000293`): Xưng `tôi` / `chúng tôi`, gọi `ngài` / `thưa Tướng quân`, giữ thái độ vừa nghiêm chỉnh quân lệnh vừa hào sảng trước giờ xung trận cảm tử. Ở `p000293`, chi tiết nói đùa về việc cùng xông vào điện Valhalla sau khi tử trận và được truy phong một cấp hàm được dịch là `với tư cách nguyên soái và đại tướng` (Zettour từ trung tướng lên đại tướng/thượng tướng hoặc nguyên soái, Cramm là tư lệnh sư đoàn lên cấp đại tướng).
  - Zettour nói với Cramm (`p000292`, `p000294`): Xưng `ta`, gọi `anh`, chúng ta (`hai chúng ta`).
- **Độc thoại nội tâm và lời tự nhủ của Zettour (`p000291`, `p000296`, `p000300`, `p000301`)**:
  - Giữ giọng điềm tĩnh, già dặn và pha chút tự trào của một vị tướng lão luyện (`ta` / `mình`).
- **Đối thoại giữa Trung tướng von Zettour và Trung úy Grantz (`p000303`–`p000316`, `p000324`–`p000327`)**:
  - Grantz nói với Zettour (`p000303`, `p000305`, `p000310`, `p000312`, `p000315`, `p000324`, `p000326`): Xưng `tôi` / `chúng tôi`, gọi `ngài` / `thưa Tướng quân`, thể hiện sự khẩn thiết của sĩ quan hộ tống được Trung tá von Degurechaff giao nhiệm vụ bảo vệ tướng quân.
  - Zettour nói với Grantz (`p000304`, `p000309`, `p000311`, `p000313`, `p000316`, `p000325`, `p000327`): Xưng `ta` / `chúng ta`, gọi `cậu` / `Trung úy` / `Trung úy Grantz`, giữ giọng bề trên quyết đoán, nghiêm nghị trên chiến trường.

## 3. Thuật ngữ Canon & Pending đã áp dụng nhất quán
- `Lục quân Đế quốc`, `Đế quốc`, `mặt trận Rhine`, `mặt trận phía đông`, `miền đông`, `tiền tuyến`, `hậu phương`
- `hệ thống chỉ huy` (`p000290`)
- `Valhalla`, `nguyên soái và đại tướng` (`p000293`)
- `Trung úy Grantz`, `Trung tá von Degurechaff`, `Chỉ huy Cramm`, `Chuẩn tướng Schulz`, `Phó chỉ huy Schulz`, `Trung tướng von Rudersdorf`, `Trung tá Uger`
- `tuyến đầu tiên`, `súng máy hạng nhẹ` (`p000317`, `p000318`)
- `mạng lưới tiếp vận` (`p000318`)
- `tuyến giao thông liên lạc`, `trận đánh cơ động` (`p000320`, `p000321`)
- `Andromeda`, `cuộc tổng tấn công` (`p000321`)
- `Cụm B`, `những bậc thầy lập biểu đồ chạy tàu` (`p000322`)
- `trung đoàn trưởng` (`p000326`)
- `lịch trình chạy tàu đường sắt` (`p000328`)
