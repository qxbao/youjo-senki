# Báo cáo tự kiểm dịch thuật — `vol-08-ch-03-b17` (Sign-off)

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-03-b17-translator-signoff` (Parent: `vol-08-ch-03-b17`)
- **Translator**: `argon-low`
- **Phạm vi đoạn**: `YS-LN08/Text/chapter012.xhtml/p000280` đến `YS-LN08/Text/chapter012.xhtml/p000319` (40 đoạn)
- **Tệp bản dịch**: `translations/vol-08/ch-03-b17.jsonl`
- **Trạng thái dòng**: Tất cả 40 dòng đã được cập nhật từ `draft` sang `status: "reviewed"`.

## 2. Xử lý findings từ `reviews/prose/vol-08/ch-03-b17-argon-review.yml`
1. **`YS-LN08/Text/chapter012.xhtml/p000281`** (`minor`):
   - **Vấn đề**: Cụm dịch `phi công át chủ bài kỳ cựu` cụ thể hóa quá mức sang phi công lái máy bay trong khi mạch ngữ cảnh bàn về các pháp sư trên không / át chủ bài nói chung của Liên bang.
   - **Xử lý**: Đã lược bỏ chữ `phi công`, đổi thành `một số át chủ bài kỳ cựu` theo đúng khuyến nghị và `locked_choices`.
2. **`YS-LN08/Text/chapter012.xhtml/p000285`** (`minor`):
   - **Vấn đề**: Lời thoại của Tanya (Trung tá) nói với Serebryakov (Trung úy thuộc quyền) dùng cụm `Trung úy ạ;` có tiểu từ kính ngữ `ạ` lệch chuẩn tôn ti quân đội.
   - **Xử lý**: Đã lược bỏ tiểu từ `ạ`, giữ `, Trung úy;` theo đúng khuyến nghị và `locked_choices`.

## 3. Kiểm tra tính đầy đủ, nghĩa (`meaning`) và `locked_choices`
- Đã đối chiếu toàn bộ 40/40 đoạn với `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-08/ch-03-b17-argon-review.yml`: tuân thủ 100%.
- Giữ nguyên logic lập luận, sắc thái phủ định, ẩn dụ và mạch chuyển cảnh:
  - Đoạn `p000280`–`p000303`: Cuộc trao đổi giữa Tanya và Trung úy Serebryakov về khả năng Quân đội Liên bang phóng thích các át chủ bài kỳ cựu từng bị coi là kẻ thù giai cấp khỏi các trại cải tạo (*lageri*) để tung vào chiến trường, cùng dòng suy ngẫm của Tanya về chủ nghĩa thực dụng đội lốt cách mạng và sự phi lý của lòng yêu nước/tình yêu mù quáng dành cho nhà nước hiện đại.
  - Đoạn `p000304`: Tiêu đề thời gian và địa điểm ngày 16 tháng 6 năm Thống Nhất 1927 tại Sở chỉ huy Cụm B trên mặt trận phía đông, văn phòng dành cho sĩ quan cấp cao.
  - Đoạn `p000305`–`p000319`: Góc nhìn của Trung tướng von Zettour khi đi thị sát thực địa với danh nghĩa thanh tra viên. Ông nhận ra sự chênh lệch đáng sợ giữa báo cáo trên giấy tờ và thực trạng phòng tuyến rời rạc của Mặt trận B, nhớ lại lời hứa cử quân tiếp viện cho Tanya, đồng thời vừa thấy nan giải cho chiến dịch giải vây Kampfgruppe Lergen của Trung tá von Degurechaff, vừa thầm nhẹ nhõm vì địch đã cắn câu mồi nhử có độc thay vì mở đợt xung phong trực diện vào phòng tuyến mỏng manh.

## 4. Kiểm tra đại từ và giọng văn (`pronouns` — `DEC-P01-001`)
- **Đối thoại giữa Tanya và Serebryakov (`p000281`–`p000283`, `p000285`, `p000288`, `p000292`–`p000294`, `p000298`)**:
  - Tanya gọi Serebryakov là `Trung úy Serebryakov` / `Trung úy` / `cô`, tự xưng `tôi`.
  - Serebryakov tự xưng `tôi`, giữ thái độ lễ phép với cấp trên (`Xin thứ lỗi cho tôi... đấy ạ`, `…Tôi đã rõ`).
- **Trần thuật và độc thoại nội tâm của Tanya (`p000280`, `p000284`, `p000286`–`p000287`, `p000289`–`p000291`, `p000295`–`p000297`, `p000299`–`p000303`)**:
  - Trần thuật ngôi thứ ba gọi Tanya là `Tanya` / `cô`.
  - Ngôi thứ hai khái quát trong các câu bình luận/suy ngẫm (`p000287`, `p000290`, `p000302`) dịch là `bạn` nhất quán với các batch trước.
- **Trần thuật và nội tâm của Zettour (`p000305`–`p000319`)**:
  - Trần thuật ngôi thứ ba gọi Zettour là `Trung tướng von Zettour` / `Zettour` / `ông`.
  - Câu trích dẫn lời hứa của Zettour ở `p000310` dùng đại từ `Ta` (`“Ta sẽ cử quân tiếp viện. Chắc chắn là vậy.”`), khớp hoàn toàn với cách Zettour xưng hô với Tanya trong chương 2 (`ch-02-b16`).

## 5. Kiểm tra nhấn mạnh (`emphasis` — `DEC-P01-002`)
- Chỉ sử dụng dấu `*...*` ở đúng 5 đoạn có thẻ nhấn mạnh trong nguồn:
  - `p000282`: `*lageri*`
  - `p000287`: `*lageri*`
  - `p000301`: `*Tình yêu vượt lên trên logic.*`
  - `p000312`: `*Thế này thì tồi tệ quá mức rồi.*`
  - `p000319`: `*Tạ ơn Chúa và tổ quốc là Quân đội Liên bang đã không liều lĩnh phát động một đợt tổng xung phong.*`
- Các đoạn còn lại (35/40 đoạn) hoàn toàn không sử dụng dấu `*...*`.

## 6. Kiểm tra thuật ngữ (`glossary` & `pending_terms`)
- Đã tuân thủ nhất quán các thuật ngữ trong `canon/glossary.yml`, `canon/glossary-pending.yml` và `pending_term_recommendations` của Argon review:
  - `Federation` / `Federation Army`: `Liên bang` / `Quân đội Liên bang`
  - `Commie` / `Commies` / `Communists`: `Cộng sản` / `đám Cộng sản`
  - `class enemies`: `kẻ thù giai cấp`
  - `lageri`: `*lageri*`
  - `Heimat`: `Heimat`
  - `Unified Year 1927`: `năm Thống Nhất 1927`
  - `B Group Headquarters` / `B Group staffers` / `B Front`: `Sở chỉ huy Cụm B` / `các sĩ quan tham mưu Cụm B` / `Mặt trận B`
  - `eastern front` / `Rhine front`: `mặt trận phía đông` / `mặt trận Rhine`
  - `deputy chief of the Service Corps`: `Cục phó Cục Quân vụ`
  - `General Staff Office`: `Văn phòng Bộ Tổng tham mưu`
  - `mid-ranking officers`: `các sĩ quan cấp tá`
  - `Lieutenant General von Zettour`: `Trung tướng von Zettour`
  - `Lieutenant Colonel von Degurechaff’s Lergen Kampfgruppe`: `Kampfgruppe Lergen của Trung tá von Degurechaff`
