# Semantic self-check — vol-02-ch-06-b24

## Phạm vi

Đã rà lại 36 unit p000752–p000787 theo package được giao và báo cáo `reviews/prose/vol-02/ch-06-b24-argon-review.yml`. Các điểm kiểm gồm logic tác chiến, giả định và thời gian, chủ thể tập thể, độc thoại nội tâm, lời thoại và phạm vi nhấn mạnh theo DEC-P01-002. Đã xử lý đầy đủ toàn bộ findings từ Argon review, tuân thủ mọi `locked_choices` và cập nhật trạng thái toàn bộ 36 dòng sang `reviewed`.

## Kết quả xử lý review trước (Semantic)

- **B24-C01 — p000754–p000757, p000760–p000763, p000767, p000769, p000782:** thống nhất đại từ tự quy chiếu nội tâm thành “mình” hoặc lược tự nhiên. Đại từ số nhiều “chúng tôi/chúng ta” giữ theo chủ thể tập thể; câu được hình dung như lời nói trực tiếp ở p000760 vẫn giữ “tôi”. Lời thoại trực tiếp khác không bị đổi theo quy tắc nội tâm.
- **B24-C02 — p000755:** khôi phục quan hệ nhượng bộ giữa khả năng làm được và ý từ chối; hai thái độ đối lập với việc chủ động thử được nhấn mạnh thành đúng hai vùng.
- **B24-C03 — p000762:** bỏ ý nghi binh không có căn cứ; giữ câu hỏi về việc ở cuối đội quân để đánh trì hoãn khi rút lui.
- **B24-C04 — p000764:** diễn đạt rõ sắc thái nộp đơn xin cấp phép sử dụng tuyệt chiêu. Câu hiện dùng “lối vừa đánh vừa rút lui kiểu *sutegamari*”; nhấn mạnh ở thuật ngữ được giữ nguyên.
- **B24-C05 — p000776:** khôi phục nguy cơ đối với “chúng ta” sẽ còn tồn tại trong giả định ngay cả khi lời đề nghị không bị từ chối; giữ nhượng bộ và phủ định.
- **B24-C06 — p000783:** thay đánh giá tiêu cực bằng cách nói mở về danh tiếng, không định danh biệt danh “đám ốc sên”.

## Kết quả xử lý Argon review (Sign-off)

- **p000752, p000765 (moderate — pronouns_and_register):** Đổi đại từ Thiếu tá Uger gọi Tanya từ “các cậu” / “cậu” thành “cô” để đồng bộ với ch-06-b22 và ch-06-b23.
- **p000759, p000760, p000766, p000786 (moderate — pronouns_and_register):** Thống nhất cách Tanya xưng hô với Thiếu tá Uger là “tôi - ông”: ở p000759 đổi “Ừ,” thành “Đúng vậy,”; ở p000760 đổi “*Ngài đùa tôi đấy à?*” thành “*Ông đùa tôi đấy à?*”; ở p000766 đổi “cậu biết đấy” thành “ông biết đấy”; ở p000786 đổi “nhưng nếu cậu thấy được” thành “nhưng nếu ông không chê”.
- **p000763 (moderate — formatting_and_completeness):** Bổ sung ký hiệu chú thích số mũ `²³` thành “nhà Shimahdzu²³”.
- **p000764 (minor — meaning_and_nuance):** Đổi “xin phép dùng nó” thành “nộp đơn xin cấp phép sử dụng nó” để giữ sắc thái thủ tục cấp phép bản quyền kết nối với câu sau.
- **p000769 (minor — logic_and_connectors):** Sửa quan hệ đẳng lập bổ sung thành “Không, mình nghĩ ông ấy nghiêm túc về chuyện dinh dưỡng, đồng thời đơn giản là một kẻ cuồng chiến trường hết thuốc chữa thôi.”
- **p000774 (minor — time_and_context):** Đổi “sau này” thành “sau đó” cho khớp ngữ cảnh đang trên đường đến gặp cấp trên.
- **p000784 (minor — meaning_and_completeness):** Sửa “trí tò mò và tâm hồn trong sáng của mình” thành “óc tò mò tri thức và sự thuần khiết của mình”.

## Lựa chọn tạm — tất cả pending, không phải canon

| Thuật ngữ / vấn đề | Phương án dùng trong lô | Phương án khác và căn cứ |
|---|---|---|
| `delaying defense / delaying action` (p000752, p000753, p000762) | “phòng ngự trì hoãn / đánh trì hoãn” | Có thể dùng “tác chiến trì hoãn”; giữ theo đề xuất của Argon review. |
| `rear guard` (p000767) | “đội đoạn hậu” | Ledger review đề xuất “lực lượng đoạn hậu”; giữ “đội đoạn hậu” theo `locked_choices`. |
| `Major / General` (p000760, p000772, p000774, p000775, p000785) | “Thiếu tá / Tướng” | Giữ mức “Tướng” vì package không xác định cấp tướng cụ thể. |
| `Shimahdzu(s)` (p000763–p000764) | “nhà Shimahdzu” (kèm `²³` ở p000763) | Có thể dùng “gia tộc Shimahdzu”; giữ theo `locked_choices`. |
| `sutegamari` (p000764) | “lối vừa đánh vừa rút lui kiểu *sutegamari*” | Có thể dùng “chiến thuật vừa đánh vừa rút *sutegamari*”. Đã giữ nhấn mạnh vốn có. |
| `practical economic agent` (p000783) | “tác nhân kinh tế thực dụng” | Có thể dùng “chủ thể kinh tế thực dụng”; giữ theo `locked_choices`. |
| `Maginot Line` (p000783) | “phòng tuyến Maginot” | Có thể viết hoa “Phòng tuyến Maginot”; giữ theo `locked_choices`. |
| `ersatz coffee` (p000786) | “cà phê thay thế” | Có thể dùng “cà phê giả” hoặc giữ “cà phê ersatz”; giữ theo `locked_choices`. |
| `escargots` (p000783) | “đám ốc sên” | Có thể giữ nguyên `escargots`; giữ theo `locked_choices`. |

## Kiểm tra nhấn mạnh

Các dấu nhấn mạnh được giữ đúng phạm vi nguồn: hai vùng ở p000755; một vùng mỗi đoạn tại p000756, p000760 và p000764. p000755 nhấn mạnh trọn mệnh đề có quan hệ nhượng bộ và riêng lời đề nghị thử; p000760 giữ nhấn mạnh ở câu hét giả định `*Ông đùa tôi đấy à?*`; p000764 giữ nhấn mạnh ở `*sutegamari*`.
