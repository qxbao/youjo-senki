# Báo cáo tự kiểm dịch thuật — `vol-09-ch-05-b19`

- **Task ID**: `vol-09-ch-05-b19`
- **Phạm vi**: `YS-LN09/Text/chapter020.xhtml/p000645` đến `YS-LN09/Text/chapter020.xhtml/p000695` (51 đoạn)
- **Tác tử**: `argon-low`
- **Bản dịch**: `translations/vol-09/ch-05-b19.jsonl`
- **Trạng thái**: `reviewed` (Sign-off sau review của Argon)

## 0. Xử lý findings trong `ch-05-b19-argon-review.yml`
- **`YS-LN09/Text/chapter020.xhtml/p000658` (`minor`, `emphasis_style`)**: Đổi `Tất *nhiên*` thành `Lẽ *dĩ nhiên*` để giữ đúng cụm nhấn mạnh Markdown mà không cắt rời từ ghép hai âm tiết tiếng Việt.
- **`YS-LN09/Text/chapter020.xhtml/p000661` (`minor`, `meaning_nuance`)**: Đổi `bị kìm chân` ở vế đầu thành `bị cản lại` để diễn đạt chuẩn xác việc bị ngăn không cho nổ súng (do quân mình ở lẫn bên dưới), phân biệt rõ với vế hai.
- **`YS-LN09/Text/chapter020.xhtml/p000691` (`minor`, `terminology`)**: Lược bỏ danh từ phân loại `trận` tự thêm ngoài nguồn, giữ nguyên định danh `Soldim 528`.
- **Trạng thái dòng (`status`)**: Đã cập nhật toàn bộ 51 dòng trong `translations/vol-09/ch-05-b19.jsonl` từ `draft` sang `reviewed` và tuân thủ đầy đủ mọi `locked_choices` cùng `pending_term_recommendations`.

## 1. Kiểm tra nghĩa, phủ định, đối tượng và logic (`meaning`)
- **`p000645`–`p000651`**: Giữ nguyên chuỗi tiếng la hét hỗn loạn trên kênh liên lạc của lực lượng đồn trú tại cảng khi quân biệt kích có thêm viện binh, hỏa lực bắn nhầm vào quân mình, đám cháy bùng phát và các mệnh lệnh mâu thuẫn nhau vang lên, phản ánh trạng thái hỗn loạn cận kề vỡ trận.
- **`p000652`–`p000667`**: Bảo toàn mạch liên lạc trực tiếp giữa Đại úy Meybert và Trung úy Tospan: Tospan báo không thể kịp tiếp ứng vì đang bị chính một chốt quân mình bắn nhầm. Giữ đúng nhận định của Meybert về việc binh lính, hạ sĩ quan và sĩ quan tại cảng đều thiếu kinh nghiệm thực chiến nên hoảng loạn nhìn bóng nào cũng tưởng là địch; anh không thể nã đạn khói hay đạn xuyên giáp để chế áp vì quân mình cũng đang ở dưới đó, đành lệnh cho Tospan ưu tiên làm chốt quân mình ngừng bắn trước.
- **`p000668`–`p000678`**: Tospan báo cáo cả cờ hiệu lẫn đèn tín hiệu đều không ăn thua và phát hiện thêm quân tiếp viện địch đổ bộ lên cầu cảng, khiến việc ghìm chân toán biệt kích ngay tại đầu cầu đổ bộ trở nên bất khả thi. Giữ nguyên sự đối lập giữa cảnh hỗn loạn của phía Đế quốc với tác phong tác chiến sắc bén của bộ binh địch (tự ra quyết định ngay ở cấp tiểu đội mà không cần sĩ quan thúc giục), cùng lập luận trấn an của Meybert rằng phía Đế quốc vẫn nắm ưu thế tuyệt đối về quân số vì địch tối đa chỉ có khoảng một tiểu đoàn.
- **`p000679`–`p000695`**: Bảo toàn chuỗi suy luận chiến thuật của Meybert: từ phán đoán đây là một đội tập kích đi phá hoại và rút lui bằng xuồng (nên việc phá hủy tàu dọc cầu cảng sẽ hợp lý hơn là cố chiếm tàu, vì địch chẳng ngu xuẩn đến mức để lại khóa giải mã mật mã trên xuồng) đến sự nghi ngờ trước canh bạc quá liều lĩnh nếu chỉ dùng bộ binh đơn thuần. Từ đó Meybert sực nhớ tới chiến thuật ở cao điểm Soldim 528 trên mặt trận phía đông—dùng một bộ phận pháp sư bay trên mặt nước làm mồi nhử thu hút sự chú ý, còn thực chất đã trà trộn thêm pháp sư vào toán biệt kích để đánh thốc vào sườn—và lập tức hét gọi Tospan quay đầu rút lui ngay trước khi bị một báo cáo cắt ngang.

## 2. Kiểm tra xưng hô và giọng điệu (`pronouns`)
- **Trần thuật và nội tâm**: Điểm nhìn ngôi thứ ba theo sát Đại úy Meybert. Trong trần thuật dùng `Meybert` / `anh`, với Trung úy Tospan dùng `Tospan` / `viên trung úy` / `anh ta`. Trong nội tâm trực tiếp của Meybert (`p000663`, `p000683`, `p000685`, `p000692`), dùng `mình` / `chúng ta` nhất quán với quy ước của chương.
- **Đối thoại**: Meybert gọi Tospan là `Trung úy Tospan` / `Trung úy` / `cậu`, tự xưng `tôi` / `chúng ta`. Tospan gọi Meybert là `Đại úy` (`p000654`, `p000674`), tự xưng `chúng tôi` và có tiểu từ lễ phép phù hợp với cấp trên trực tiếp trong cùng Kampfgruppe. Khi nhắc tới Trung tá Tanya von Degurechaff (`p000694`), dùng `Trung tá` nhất quán với các lô trước của Tập 9.

## 3. Kiểm tra nhấn mạnh (`emphasis`)
- Tuân thủ nghiêm ngặt `DEC-P01-002`: chỉ sử dụng `*...*` ở đúng các đoạn có thẻ nhấn mạnh trong `xhtml` nguồn và khớp chính xác số cụm nhấn mạnh trên từng dòng:
  - `p000652`: 1 cụm (`*Đúng lúc lắm.*`).
  - `p000655`: 1 cụm (`*Sao các cậu lại không tới kịp được cơ chứ?*`).
  - `p000658`: 2 cụm (`*dĩ nhiên*`, `*chỉ*`).
  - `p000663`: 1 cụm (`*Mấy gã bù nhìn khốn kiếp này hoàn toàn chẳng biết mình phải làm gì cả!*`).
  - `p000664`: 1 cụm (`*Rốt cuộc họ nghĩ chiến tranh là cái gì chứ? Phải bổ sung thêm một phụ lục vào quy chế mới được. Ừ, xem chừng cuốn sổ tay hướng dẫn cần phải quy định rõ rằng phải coi trọng chuyện chiến tranh một cách nghiêm túc.*`).
  - `p000667`: 1 cụm (`*Lũ ngu xuẩn này!*`).
  - `p000683`: 1 cụm (`*Thay vì cố tìm cách chiếm lấy những con tàu dọc cầu cảng, chẳng phải cứ phá hủy quách chúng đi sẽ tốt hơn sao? Đằng nào thì kẻ địch của chúng ta cũng đâu phải hạng ngu xuẩn đến mức bỏ lại khóa giải mã mật mã của chúng trên xuồng.*`).
  - `p000685`: 1 cụm (`*Chỉ mang mỗi bộ binh mà dám xông vào đây thì cũng gan thật đấy. Hẳn chúng phải cực kỳ tự tin vào kế hoạch của mình, bao gồm cả phương án rút quân nào đó mà chúng có; bằng không thì hành động này chỉ tổ liều mạng mà thôi.*`).
  - `p000692`: 1 cụm (`*Dùng một bộ phận pháp sư làm mồi nhử để thu hút sự chú ý của địch. Khiến chúng tưởng rằng đó là toàn bộ số pháp sư mà mình có, kéo sự cảnh giác của chúng sang một hướng khác, rồi chờ đúng thời cơ giáng một đòn trời giáng từ bên sườn vào lũ ngốc đang mất cảnh giác.*`).
  - `p000695`: 1 cụm (`*trà trộn các pháp sư vào đó*`).
- Các thẻ neo trang ở `p000657`, `p000674`, `p000691` không sinh dấu nhấn mạnh. Toàn bộ 41 đoạn còn lại không chứa dấu `*`.

## 4. Kiểm tra thuật ngữ và mục chờ duyệt (`pending_terms`)
- Đã tra cứu và áp dụng nhất quán các thuật ngữ đã có trong `work/run-state/pending-terms-index.yml`:
  - Nhân vật và cấp bậc: `Đại úy` / `Meybert` / `Trung úy` / `Trung úy Tospan` / `Tospan` (`p000652`–`p000655`, `p000665`, `p000671`, `p000673`–`p000674`, `p000679`–`p000680`, `p000686`, `p000689`), `Trung tá` (`p000694`).
  - Thuật ngữ quân sự: `biệt kích` (`p000645`, `p000671`, `p000694`), `mặt trận phía đông` (`p000661`, `p000681`, `p000694`), `đội tập kích` (`p000679`), `đánh chặn` (`p000687`).
- Ghi nhận một số cụm thuật ngữ/địa danh quân sự trong lô để đồng bộ nếu gặp lại tại `p000668` (`cờ hiệu` / `đèn tín hiệu`), `p000671` (`đầu cầu đổ bộ`) và `p000691` (`Soldim 528`).
