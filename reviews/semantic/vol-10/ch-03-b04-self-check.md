# Báo cáo tự kiểm (Semantic Self-Check) — `vol-10-ch-03-b04`

- **Task ID:** `vol-10-ch-03-b04` (Sign-off: `vol-10-ch-03-b04-translator-signoff`)
- **Translator:** `argon-low`
- **Phạm vi:** `YS-LN10/Text/chapter018.xhtml/p000001` .. `YS-LN10/Text/chapter018.xhtml/p000029` (29 đoạn)
- **Tệp đích:** `translations/vol-10/ch-03-b04.jsonl`
- **Glossary Version:** `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra tính đầy đủ và cấu trúc dữ liệu
- **Số lượng đoạn:** Đầy đủ 29/29 đoạn từ `p000001` đến `p000029`, khớp 1:1 với tệp nguồn.
- **Trạng thái & siêu dữ liệu:** Toàn bộ 29 dòng đã được cập nhật sang `status: "reviewed"`, giữ `translator: "argon-low"`, `source_sha256` và `glossary_version` khớp với handoff.
- **Nhấn mạnh (`DEC-P01-002`):** Đã kiểm tra và bảo toàn chính xác đánh dấu `*...*` ở đúng 5 đoạn có thẻ nhấn mạnh trong nguồn:
  - `p000009`: `*lẽ ra cô phải biết điều này rồi chứ*`
  - `p000012`: `*lúc nào*`
  - `p000024`: `*phòng ngự*`
  - `p000025`: `*chờ*`
  - `p000027`: `*phòng ngự*`
  - Các đoạn còn lại không tự ý thêm dấu `*...*`.

## 2. Xưng hô, điểm nhìn và giọng điệu (`DEC-P01-001` & `style-guide.md`)
- **Độc thoại nội tâm & trần thuật của Tanya:** Giữ nhất quán đại từ ngôi thứ nhất `mình` (`p000002`, `p000004`, `p000009`, `p000014`, `p000015`, `p000016`, `p000023`), đại từ giả định chung `bạn` (`p000004`, `p000024`) và lối tự quy chiếu tách ngôi bằng tên riêng `Tanya` / `cô` (`p000001`, `p000015`, `p000019`), đồng bộ với lô `ch-03-b03` ngay trước đó.
- **Thoại quân sự giữa Tướng Romel và Trung tá Tanya von Degurechaff:**
  - Tướng Romel gọi Tanya là `Trung tá Degurechaff` / `cô`, tự xưng `Ta` (hoặc `chúng ta` khi nói chung về phe mình ở `p000013`, `p000021`), giọng quyết đoán, áp đặt (`p000006`, `p000008`, `p000013`, `p000018`, `p000021`).
  - Tanya gọi Tướng Romel là `thưa Tướng quân` / `ngài`, tự xưng `tôi`, kèm `ạ` giữ lễ tiết quân sự nhưng vẫn tranh luận sắc bén (`p000003`, `p000005`, `p000007`, `p000017`, `p000020`, `p000029`).

## 3. Thuật ngữ và phương án Pending
- Các thuật ngữ đã có trong sổ pending được áp dụng nhất quán:
  - `General Romel` -> `Tướng Romel` (`p000009`, `p000016`)
  - `Lieutenant Colonel Degurechaff` -> `Trung tá Degurechaff` (`p000013`)
  - `White Silver` -> `Bạch Ngân` (`p000013`)
  - `General Zettour` -> `Tướng Zettour` (`p000029`)
  - `maneuver warfare` -> `tác chiến cơ động` (`p000029`)
- Các đề xuất thuật ngữ/tên riêng mới (ghi nhận ở trạng thái `pending`):
  - `Oda Nobunaga / Oda clan` -> `Oda Nobunaga / gia tộc Oda` (`p000022`, `p000023`, `p000025`, `p000027`, `p000028`)
  - `Battle of Okehazama / Dengakuhazama` -> `Trận Okehazama / Dengakuhazama` (`p000023`)
  - `Imagawa Yoshimoto / Owari Province` -> `Imagawa Yoshimoto / xứ Owari` (`p000025`, `p000027`)
  - `decapitation strikes` -> `các đòn tập kích chặt đầu chỉ huy` (`p000029`, đối chiếu `decapitation tactics` = `chiến thuật chặt đầu chỉ huy` trong sổ pending)

## 4. Kiểm tra ngữ nghĩa, phủ định và giả định
- `p000012`: Bảo toàn phủ định bộ phận có nhấn mạnh (`không phải *lúc nào* cũng xấu`).
- `p000013`: Bảo toàn cấu trúc phủ định kép trong lời Tướng Romel (`Ta không định để cô không hiểu thấu bản kế hoạch này.`).
- `p000020`: Bảo toàn cấu trúc phủ định kép trong lời Tanya (`ý tôi không phải là không cần một mức độ tiến công nhất định để tổ chức phòng ngự hiệu quả`).
- `p000028`: Bảo toàn thời gian và tính giả định trái thực tế trong quá khứ về Nobunaga (`chuyện gì hẳn đã xảy ra nếu...`, `hẳn đã khép lại...`, `hẳn đã bị đẩy xuống...`).

## 5. Xử lý Argon Review & Translator Sign-off (`vol-10-ch-03-b04-translator-signoff`)
- **`p000005` (minor):** Đã chỉnh từ `"các điều khoản của nhiệm vụ"` thành `"khuôn khổ của nhiệm vụ"` theo khuyến nghị của Argon review để tự nhiên hơn trong ngữ cảnh báo cáo quân sự trực tiếp với Tướng Romel, đồng thời giữ nguyên toàn bộ `locked_choices` của đoạn.
- **`p000028` (minor):** Đã chỉnh từ `"Và chuyện gì sẽ xảy ra nếu tướng quân Nobunaga chỉ ngồi không trong thành..."` thành `"Và chuyện gì hẳn đã xảy ra nếu tướng quân Nobunaga chỉ ngồi không trong thành..."` theo khuyến nghị của Argon review để đồng bộ thời gian giả định quá khứ trái thực tế với câu tiếp theo.
- **`pending_term_recommendations` & `locked_choices`:** Đã kiểm tra và bảo đảm tuân thủ đầy đủ toàn bộ 9 mục `pending_term_recommendations` và 29 mục `locked_choices` trong `reviews/prose/vol-10/ch-03-b04-argon-review.yml`.
- **Trạng thái dòng (`status`):** Đã chuyển toàn bộ 29/29 dòng trong `translations/vol-10/ch-03-b04.jsonl` từ `draft` sang `reviewed`.
