# Báo cáo tự kiểm dịch thuật — `vol-06-ch-01-b04`

- **Nhiệm vụ:** `vol-06-ch-01-b04`
- **Tập / Chương:** `vol-06`, chương `1`
- **Phạm vi đoạn:** `YS-LN06/Text/part0008.html/p000116` → `YS-LN06/Text/part0008.html/p000162` (47 đoạn)
- **Tác tử dịch:** `argon-low`
- **Trạng thái sign-off:** Đã tiếp thu đầy đủ các finding từ `reviews/prose/vol-06/ch-01-b04-argon-review.yml`, đối chiếu toàn bộ `locked_choices` và `pending_term_recommendations`, cập nhật `status` của cả 47 dòng từ `draft` sang `reviewed`.

## 1. Kiểm tra nghĩa, logic và mạch trần thuật
- Đảm bảo truyền tải đầy đủ tất cả các chi tiết trong 47 đoạn từ `p000116` đến `p000162`, không lược bỏ ý hoặc tự ý thêm thắt giải thích.
- Giữ nguyên cấu trúc tương phản, điều kiện, giả định và nhân quả:
  - Ở `p000116`–`p000123`: Cuộc trao đổi giữa Serebryakov và Tanya về việc binh lính cần vận động làm ấm cơ thể vào mùa đông và dự báo tình hình sẽ trở nên nguy ngập vào tháng Một, tháng Hai khi trời rét đậm.
  - Ở `p000124`–`p000134`: Nhận định của Tanya về sai lầm khi không lường trước việc tác chiến mùa đông trên lãnh thổ Liên bang; sự lệch pha giữa nhận thức của quê nhà/sở chỉ huy với thực tế hiện trường khiến trang bị chống rét do Cục Quân vụ của Tướng von Zettour gửi tới chỉ ở mức tối thiểu (áo khoác mỏng, tất và đồ lót không đủ chống cái lạnh thấu xương), dù hệ thống đường sắt và tuyến tiếp tế đã nỗ lực hết sức.
  - Ở `p000135`–`p000145`: Bàn về việc dùng quỹ mật phí để tự thu mua quân trang Liên bang bị đánh cắp thông qua Hội đồng Tự trị; sự khan hiếm nguồn cung tại chỗ do xung đột thời chiến khiến dù có tiền cũng không có hàng để mua, làm nỗi bực bội của Tanya tăng lên theo cái lạnh.
  - Ở `p000146`–`p000162`: Suy ngẫm của Tanya về Tướng Mùa Đông và lời nhắc của Serebryakov về Tướng Bùn Lầy khi tuyết tan vào mùa xuân; sự đối lập giữa góc nhìn lịch sử chiến trường Đức – Xô của Tanya (lo ngại việc sống sót qua mùa đông hơn) và sự kiên quyết hiếm thấy của Serebryakov (cho rằng Tướng Bùn Lầy là mối đe dọa lớn hơn đối với Đế quốc), dẫn tới việc Tanya muốn lắng nghe quan điểm của viên sĩ quan phụ tá am tường về Liên bang.

## 2. Kiểm tra đại từ và xưng hô (`DEC-P01-001`)
- **Trần thuật ngôi thứ ba về Tanya:** Dùng nhất quán đại từ `nó` (`p000124`, `p000150`, `p000153`, `p000157`, `p000162`).
- **Nội tâm tự quy chiếu của Tanya:** Dùng `mình` cho ngôi thứ nhất số ít (`p000127`, `p000130`, `p000143`, `p000145`, `p000158`); dùng `chúng ta` khi nói chung về đơn vị/quân mình (`p000121`, `p000134`, `p000143`, `p000158`).
- **Đối thoại giữa Tanya và Trung úy Serebryakov:** Tanya xưng `tôi` – gọi `Trung úy Serebryakov` / `cô`, dùng `chúng ta` khi nói về đơn vị; Serebryakov xưng `tôi` / `chúng tôi` – gọi `thưa Trung tá` (có đệm `ạ` lịch sự đúng mực cấp dưới với cấp trên ở `p000116`, `p000118`, `p000123`, `p000136`, `p000138`, `p000156`, `p000160`).
- **Trần thuật/nội tâm về Serebryakov:** Dùng `cô ấy` trong câu nội tâm trực tiếp (`p000119`) và `cô` trong trần thuật (`p000139`, `p000150`, `p000162`).

## 3. Kiểm tra nhấn mạnh / chữ nghiêng (`DEC-P01-002`)
- Đối chiếu chính xác thẻ `<html:em>` từ dữ liệu nguồn:
  - `p000119`: `*Cô ấy nói đúng*`
  - `p000141`: `*Đáng lẽ…?*`
- Không tự ý thêm `*...*` vào các đoạn nội tâm hoặc cảm thán khác không có thẻ nhấn mạnh trong nguồn.

## 4. Thuật ngữ và mục chờ xét (`pending_terms`)
- Áp dụng nhất quán các phương án tạm đã có trong sổ pending:
  - `ma’am` / `Colonel` (khi gọi Trung tá Tanya): thưa Trung tá (`p000116`, `p000150`)
  - `cold-weather gear`: trang bị chống rét (`p000120`, `p000124`, `p000126`, `p000135`, `p000140`)
  - `Lieutenant Serebryakov` / `Serebryakov` / `adjutant`: Trung úy Serebryakov / Serebryakov / sĩ quan phụ tá (`p000122`, `p000124`, `p000138`, `p000150`, `p000158`, `p000162`)
  - `Federation` / `Federation territory`: Liên bang / lãnh thổ Liên bang (`p000124`, `p000126`, `p000136`, `p000140`, `p000144`, `p000162`)
  - `Service Corps`: Cục Quân vụ (`p000124`, `p000129`)
  - `General von Zettour`: Tướng von Zettour (`p000124`)
  - `headquarters`: sở chỉ huy (`p000125`)
  - `home country`: quê nhà (`p000126`, `p000144`)
  - `classified funds`: quỹ mật phí (`p000136`)
  - `General Winter`: Tướng Mùa Đông (`p000146`, `p000156`)
  - `Lieutenant Colonel Tanya von Degurechaff`: Trung tá Tanya von Degurechaff (`p000148`)
  - `the Empire`: Đế quốc (`p000156`)
- Ghi nhận 3 thuật ngữ đề xuất mới vào mục `pending_terms` của báo cáo:
  - `Council for Self-Government` -> `Hội đồng Tự trị` (`p000136`, `p000140`)
  - `General Mud` -> `Tướng Bùn Lầy` (`p000150`, `p000152`, `p000156`)
  - `German-Soviet lines` -> `chiến tuyến Đức – Xô` (`p000157`)

## 5. Xử lý phản biện Argon (`ch-01-b04-argon-review.yml`)
- `YS-LN06/Text/part0008.html/p000136` (`moderate` / `meaning_logic`): Đưa cụm chỉ nguồn bán `từ Hội đồng Tự trị` lên ngay sau động từ `mua lại` (`Chủ yếu chúng tôi mua lại từ Hội đồng Tự trị số quân trang Liên bang bị đánh cắp...`) để làm rõ Hội đồng Tự trị là bên bán lại số quân trang bị đánh cắp, loại bỏ sự nhập nhằng cú pháp.
- `YS-LN06/Text/part0008.html/p000142` (`minor` / `pronouns_pov`): Lược bỏ đại từ `mình` trong mệnh đề phụ (`lời họ nói rằng không có nguồn dự trữ đáng kể...`) để tránh giao thoa với đại từ độc thoại nội tâm tự quy chiếu `Mình` của Tanya theo `DEC-P01-001`.
- Đảm bảo tuân thủ toàn bộ 47 mục `locked_choices` và 12 mục `pending_term_recommendations` trong báo cáo review; cập nhật trường `status` của toàn bộ 47 dòng từ `draft` sang `reviewed`.
