# Báo cáo tự kiểm & Sign-off (Semantic Self-Check) — `vol-10-ch-03-b03`

- **Task ID:** `vol-10-ch-03-b03-translator-signoff` (parent: `vol-10-ch-03-b03`)
- **Translator:** `argon-low`
- **Phạm vi:** `YS-LN10/Text/chapter016.xhtml/p000050` .. `YS-LN10/Text/chapter016.xhtml/p000082` (33 đoạn)
- **Tệp đích:** `translations/vol-10/ch-03-b03.jsonl`
- **Glossary Version:** `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra tính đầy đủ, trạng thái Sign-off và cấu trúc dữ liệu
- **Số lượng đoạn:** Đầy đủ 33/33 đoạn từ `p000050` đến `p000082`, khớp 1:1 với tệp nguồn.
- **Trạng thái & siêu dữ liệu:** Toàn bộ 33 dòng đã được cập nhật `status: "reviewed"`, giữ nguyên `translator: "argon-low"`, `source_sha256` và `glossary_version` khớp với handoff.
- **Nhấn mạnh (`DEC-P01-002`):** Bảo toàn chính xác đánh dấu `*...*` ở đúng 3 đoạn có thẻ nhấn mạnh trong nguồn:
  - `p000070`: `*cơ bản*`
  - `p000073`: `*tái tổ chức lưới phòng không của nó*`
  - `p000080`: `*phòng ngự*`
  - Các đoạn còn lại không tự ý thêm dấu `*...*`.

## 2. Xử lý các Findings trong `reviews/prose/vol-10/ch-03-b03-argon-review.yml`
- **`p000050` (minor):** Đã chỉnh cụm `hạm đội hải quân quân ta` thành `hạm đội hải quân của chúng ta` để tránh lặp từ, và chỉnh `đúng lúc vừa hết thời gian suy nghĩ` thành `đúng lúc mình vừa hết thời gian` để bám sát cấu trúc nguồn mà không tự thêm bổ ngữ, vẫn tuân thủ đầy đủ `locked_choices`.
- **`p000059` (minor):** Đã chỉnh câu cảm thán `Khốn thay cho Tướng Romel.` thành `Đáng hận thay Tướng Romel.` nhằm thể hiện rõ sắc thái oán thán/trách cứ của Tanya trước vị cấp trên vừa giao bản kế hoạch kinh khủng, đồng thời giữ nguyên danh xưng `Tướng Romel` theo `locked_choices`.
- **`p000064` (minor):** Đã chỉnh động từ `dung thứ` ở cuối câu thành `chấp nhận` (`Một canh bạc mà đứng trên góc độ chuyên môn, Tanya không thể nào chấp nhận.`) để tự nhiên và chuẩn xác hơn khi đánh giá nghiệp vụ đối với một kế hoạch tác chiến, giữ nguyên cấu trúc tách ngôi theo `locked_choices`.

## 3. Xưng hô, điểm nhìn và giọng điệu (`DEC-P01-001` & `locked_choices`)
- Bảo đảm tuân thủ tuyệt đối toàn bộ 33 mục `locked_choices` trong báo cáo review của Argon:
  - **Độc thoại nội tâm & trần thuật của Tanya:** Giữ nhất quán đại từ ngôi thứ nhất `mình` (hoặc `chúng ta` khi bao hàm phe Đế quốc ở `p000050`, `p000065`, `p000066`, `p000068`, `p000070`, `p000082`) và lối tự quy chiếu tách ngôi bằng tên riêng `Tanya` / `cô` (`p000050`, `p000051`, `p000056`, `p000064`, `p000072`, `p000076`).
  - **Thoại quân sự giữa Tướng Romel và Trung tá Tanya von Degurechaff:**
    - Tướng Romel gọi Tanya là `Trung tá` / `cô`, tự xưng `Ta` (`p000058`, `p000063`, `p000077`, `p000079`).
    - Tanya gọi Tướng Romel là `thưa Tướng quân` / `ngài`, tự xưng `tôi`, kèm `ạ` lịch sự quân ngũ pha nét mỉa mai chừng mực (`p000068`, `p000070`, `p000078`, `p000080`).

## 4. Thuật ngữ và phương án Pending (`pending_term_recommendations`)
- Đã kiểm tra và giữ đồng bộ toàn bộ 11 mục `pending_term_recommendations` trong `argon-review`:
  - `duty officer / adjutant` -> `sĩ quan trực ban / sĩ quan phụ tá` (`p000050`)
  - `General Romel / the general / sir` -> `Tướng Romel / vị tướng / thưa Tướng quân (ngài)` (`p000050`, `p000059`, `p000064`, `p000066`, `p000070`, `p000073`, `p000075`, `p000076`, `p000078`)
  - `mobile command center` -> `sở chỉ huy cơ động` (`p000051`, `p000054`)
  - `Colonel` -> `Trung tá` (`p000058`, `p000063`, `p000077`, `p000079`)
  - `the Commonwealth / Commonwealth homeland` -> `Khối Thịnh vượng chung / bản thổ Khối Thịnh vượng chung` (`p000060`, `p000066`, `p000068`, `p000082`)
  - `air superiority` -> `ưu thế trên không` (`p000065`)
  - `François Low Lands` -> `Vùng Trũng François` (`p000065`)
  - `Western Army Group / western front` -> `Cụm tập đoàn quân phía Tây / mặt trận phía tây` (`p000066`, `p000070`)
  - `General Staff Office` -> `Văn phòng Bộ Tổng tham mưu` (`p000070`)
  - `Being X` -> `Being X` (`p000075`)
  - `Home Fleet` -> `Hạm đội Bản thổ` (`p000082`)
