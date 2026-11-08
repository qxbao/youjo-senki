# Báo cáo tự kiểm dịch thuật — `vol-11-ch-01-b11` (Sign-off)

- **Task ID:** `vol-11-ch-01-b11-translator-signoff` (Parent: `vol-11-ch-01-b11`)
- **Phạm vi đoạn:** `YS-LN11/Text/chapter002.xhtml/p000304` .. `YS-LN11/Text/chapter002.xhtml/p000342` (39 đoạn)
- **Tác tử thực hiện:** `argon-low` (`translator_luna`)

## 1. Xử lý phản biện Argon (`reviews/prose/vol-11/ch-01-b11-argon-review.yml`)
- **Trạng thái:** Đã xử lý đầy đủ 6/6 findings (3 moderate, 3 minor) và cập nhật `status: "reviewed"` cho toàn bộ 39/39 dòng:
  - `YS-LN11/Text/chapter002.xhtml/p000311` (moderate): Đổi `vị cục phó` thành `vị phó tổng tham mưu trưởng` và đổi đại từ `ông ta` thành `ông ấy` để nhất quán với quy chiếu Rudersdorf ở `p000316`–`p000317` và `pending-terms-index.yml`.
  - `YS-LN11/Text/chapter002.xhtml/p000314` (moderate): Sửa `Hai chúng tôi cùng bật cười sảng khoái.` thành `Cả hai cùng bật cười sảng khoái.` để tránh trượt sang đại từ đối thoại `tôi` trong trần thuật của Tanya theo `DEC-P01-001`.
  - `YS-LN11/Text/chapter002.xhtml/p000317` (moderate): Sửa `Sau khi chúng tôi nhìn ông ấy...` thành `Sau khi cả hai nhìn ông ấy...` để giữ ngôi kể trần thuật nhất quán.
  - `YS-LN11/Text/chapter002.xhtml/p000305` (minor): Sửa `nghiêm nghị một cách ngượng ngập đến mức trông như đang làm quá lên` thành `nghiêm nghị đến mức gây khó chịu và trông như đang làm quá lên`.
  - `YS-LN11/Text/chapter002.xhtml/p000309` (minor): Lược bỏ trợ từ thời quá khứ `đã` trước `hào hứng` (`cô hào hứng đến mức nào khi phải đi theo làm cận vệ cho ông ta`) để phản ánh đúng nghĩa vụ hiện hành/khái quát.
  - `YS-LN11/Text/chapter002.xhtml/p000324` (minor): Đổi hô ngữ `thưa Tướng quân` thành `thưa ngài` (`“Vì ngài thì việc gì cũng được ạ, thưa ngài.”`) để thống nhất với `p000330` và `p000334`.

## 2. Kiểm tra nghĩa và mạch tự sự (`meaning`)
- **Trạng thái:** `pass`
- **Chi tiết:**
  - Bảo toàn đầy đủ 39/39 đoạn văn từ đầu đến cuối batch, giữ nguyên mã đoạn ổn định và không gộp hoặc tách dòng.
  - Phản ánh chính xác diễn biến cảnh tại văn phòng bộ chỉ huy mặt trận phía đông: cuộc đối thoại châm biếm giữa Tướng Rudersdorf và Tướng Zettour về đội hộ vệ mới trước khi Rudersdorf đi họp với Hội đồng Tự trị (`p000304`–`p000307`), màn trò chuyện xã giao nhắc tới Trung úy Grantz và bia của Đế quốc (`p000308`–`p000314`), sự nhẹ nhõm ngắn ngủi của Tanya khi Rudersdorf rời phòng và hy vọng được nghỉ phép (`p000315`–`p000325`), rồi bước ngoặt bất ngờ khi Tướng Zettour thản nhiên giao cho Tanya nhiệm vụ chuẩn bị ám sát người bạn thân của ông trong tương lai gần khiến Tanya bàng hoàng hỏi lại ý định (`p000326`–`p000342`).
  - Các mệnh đề điều kiện, phủ định, lối nói ẩn dụ đen tối của Zettour (`p000326`, `p000335`) và phản ứng nội tâm thực dụng của Tanya (`p000322`, `p000329`, `p000341`) đều được truyền tải sát nghĩa, tuân thủ toàn bộ `locked_choices`.

## 3. Kiểm tra xưng hô và giọng nhân vật (`pronouns`)
- **Trạng thái:** `pass`
- **Chi tiết:**
  - **Độc thoại nội tâm của Tanya:** Duy trì nhất quán ngôi thứ nhất `mình` (`p000308`, `p000311`, `p000315`, `p000319`, `p000322`, `p000325`, `p000327`, `p000329`, `p000331`–`p000333`, `p000337`, `p000341`), kết hợp góc nhìn ngôi thứ ba `Tanya` tại các câu tự sự đặc trưng của tác phẩm (`p000308`, `p000319`). Trong câu dẫn chung (`p000314`, `p000317`), dùng `Cả hai` / `cả hai` theo `DEC-P01-001`.
  - **Rudersdorf ↔ Zettour (`p000304`–`p000307`):** Hai vị tướng đồng cấp, bạn cũ lâu năm đối thoại bằng cặp đại từ `tôi` – `anh` tự nhiên, vừa thể hiện sự thân tình vừa giữ khí chất sĩ quan cao cấp.
  - **Zettour → Tanya (`p000309`, `p000312`, `p000321`, `p000323`, `p000326`, `p000335`, `p000339`, `p000342`):** Xưng `tôi`, gọi `cô` / `Trung tá`, giữ giọng điềm tĩnh, sắc lạnh và tỉnh táo.
  - **Tanya → Rudersdorf (`p000310`, `p000313`) và Tanya → Zettour (`p000320`, `p000324`, `p000328`, `p000330`, `p000334`, `p000338`, `p000340`):** Xưng `tôi`, gọi `ngài` / `thưa ngài`, giữ thái độ chuẩn mực quân kỷ ngoài mặt.
  - **Nhắc tới Trung úy Grantz (`p000310`, `p000312`, `p000313`):** Tanya gọi là `cậu ấy`, Rudersdorf gọi là `cậu ta`, đúng vị thế cấp trên nói về sĩ quan cấp dưới.

## 4. Kiểm tra bảo toàn nhấn mạnh (`emphasis`)
- **Trạng thái:** `pass`
- **Chi tiết:**
  - Tuân thủ nghiêm ngặt quy định `DEC-P01-002`: chỉ dùng dấu `*...*` tại đúng 4 đoạn có thẻ nhấn mạnh trong `xhtml` gốc:
    - `YS-LN11/Text/chapter002.xhtml/p000325`: `*nghỉ phép*`
    - `YS-LN11/Text/chapter002.xhtml/p000327`: `*chuyện này*`
    - `YS-LN11/Text/chapter002.xhtml/p000331`: `*Sao thế?*`
    - `YS-LN11/Text/chapter002.xhtml/p000341`: `*sĩ quan chỉ huy nghiêm túc*`
  - Toàn bộ 35 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` gốc và hoàn toàn không phát sinh dấu `*` nào trong bản dịch.

## 5. Thuật ngữ và mục chờ duyệt (`pending_terms`)
- **Trạng thái:** `pass`
- **Chi tiết:**
  - Áp dụng nhất quán các thuật ngữ theo `canon/` và `pending_term_recommendations` trong `ch-01-b11-argon-review.yml`:
    - `người phụ trách mặt trận phía đông` (`p000305`)
    - `Trung úy Grantz` (`p000310`)
    - `vị phó tổng tham mưu trưởng` (`p000311`)
    - `đại đội` (`p000312`)
    - `Đế quốc` (`p000313`)
    - `Tướng Rudersdorf` (`p000315`, `p000322`, `p000325`, `p000337`)
    - `Hội đồng Tự trị` (`p000315`)
    - `Văn phòng Bộ Tổng tham mưu` (`p000316`)
    - `Tướng Zettour` (`p000317`, `p000319`, `p000322`, `p000341`)
    - `Trung tá` (`p000323`, dùng khi gọi tắt cấp bậc Trung tá của Tanya theo quy ước canon/pending)
    - `nhà chiến lược` (`p000342`)
