# Báo cáo tự kiểm (Self-Check): `vol-06-ch-05-b15`

## 1. Thông tin chung
- **Task ID**: `vol-06-ch-05-b15` (Sign-off: `vol-06-ch-05-b15-translator-signoff`)
- **Translator**: `argon-low`
- **Phạm vi đoạn**: `YS-LN06/Text/part0025.html/p000050` → `YS-LN06/Text/part0025.html/p000097` (48 đoạn)
- **Tệp bản dịch**: `translations/vol-06/ch-05-b15.jsonl`
- **Trạng thái dòng**: Toàn bộ 48 dòng đã được cập nhật sang `status: "reviewed"` sau khi xử lý Argon review.

## 2. Kiểm tra tính đầy đủ và siêu dữ liệu
- **Số dòng và thứ tự**: Đủ 48 dòng, khớp chính xác thứ tự `segment_id` với gói nguồn `work/vol-06/batches/ch-05-b15-source.jsonl`.
- **Trường bắt buộc**: Đầy đủ `segment_id`, `translation`, `status`, `translator`, `glossary_version`, `source_sha256`, `notes` trên mọi dòng.
- **Nhấn mạnh (`*...*`) theo `DEC-P01-002`**:
  - Các đoạn có thẻ nhấn mạnh trong nguồn và đã được đánh dấu `*...*` đúng phạm vi:
    - `YS-LN06/Text/part0025.html/p000060`: `*Tại sao ông ấy lại thụ động đến thế?*`
    - `YS-LN06/Text/part0025.html/p000061`: `*cuộc chiến giả vờ*`
    - `YS-LN06/Text/part0025.html/p000062`: `*Nói thế là có ý gì?*`
    - `YS-LN06/Text/part0025.html/p000063`: `*không*`
    - `YS-LN06/Text/part0025.html/p000064`: `*Không thể nào có chuyện đó được*`
    - `YS-LN06/Text/part0025.html/p000076`: `*Đến nước này mà vẫn chưa hiểu ra thì Trung úy Sue đúng là một kẻ nghiệp dư quá mức!*`
    - `YS-LN06/Text/part0025.html/p000077`: `*Cô ta đã được đào tạo sĩ quan ở đâu thế không biết?*`
    - `YS-LN06/Text/part0025.html/p000078`: `*Có thể vì chiến tranh nên đang thiếu hụt sĩ quan thật, nhưng không ngờ chúng ta lại phải trao quân hàm trung úy cho một kẻ thậm chí còn chẳng đủ tư cách thế này!*`
    - `YS-LN06/Text/part0025.html/p000079`: `*Mình cứ tưởng đã hiểu rõ cô ta có thể liều lĩnh đến mức nào rồi. Nhưng mình chưa từng ngờ rằng cô ta lại không thể hiểu nổi những người du kích trên chính đất nước của cô ta!*`
    - `YS-LN06/Text/part0025.html/p000091`: `*Chẳng lẽ cô ta thực sự không hiểu sao?*`
    - `YS-LN06/Text/part0025.html/p000096`: `*Tôi đâu có cố ý làm thế*`
  - Toàn bộ 37 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và hoàn toàn không sử dụng dấu `*...*`.

## 3. Kiểm tra đại từ và quy chuẩn xưng hô (`DEC-P01-001`)
- **Điểm nhìn và trần thuật**:
  - Nửa đầu lô (`p000050`–`p000065`): bám điểm nhìn của Mary Sue. Trần thuật gọi Mary là `cô` / `Mary`, nội tâm tự quy chiếu của Mary dùng `mình` (trong câu hỏi nội tâm ở `p000060`, `p000062`, `p000064`), gọi Mikel trong nội tâm/trần thuật từ góc nhìn Mary là `ông` / `ông ấy` (`p000060`, `p000063`).
  - Nửa sau lô (`p000066`–`p000097`): chuyển sang điểm nhìn của Trung tá Drake. Trần thuật gọi Drake là `ông` / `Drake` / `Trung tá Drake` (thống nhất với các lô trước như `ch-05-b06`–`b09`, `b14`), gọi Mary là `cô` / `viên trung úy trẻ tuổi` / `Mary Sue`. Nội tâm tự quy chiếu của Drake dùng `mình` / `chúng ta`, và trong suy nghĩ bực dọc về cấp dưới dùng `cô ta` (`p000077`–`p000079`, `p000091`).
- **Đối thoại**:
  - Giữa Đại tá Mikel và phía thủ lĩnh du kích Liên minh Hiệp ước (`p000050`–`p000061`): hai bên trao đổi lịch sự, giữ khoảng cách ngoại giao và ngầm hiểu ý nhau qua cách xưng `tôi` / `chúng tôi` và gọi đối phương là `các vị`.
  - Giữa Trung tá Drake và Đại tá Mikel (`p000073`–`p000074`): Drake gọi `Đại tá Mikel`, xưng `tôi` và gọi Mikel là `anh` (nhất quán với `ch-05-b08`, `ch-05-b09`).
  - Giữa Trung tá Drake và Trung úy Mary Sue (`p000065`, `p000067`, `p000081`, `p000085`, `p000086`, `p000090`, `p000093`–`p000095`, `p000097`): Drake gọi `Trung úy Sue` / `cô`, xưng `tôi`; Mary gọi `Trung tá Drake` (theo quy ước dịch `Colonel` khi gọi cấp hàm `Lieutenant Colonel`), xưng `tôi`.

## 4. Kiểm tra ngữ nghĩa, logic và thuật ngữ
- **Ngữ nghĩa và mạch lập luận**:
  - Giữ đúng sự đối lập giữa thái độ hòa nhã, thực dụng của Mikel với phía du kích địa phương và sự ngỡ ngàng của Mary: Mikel chấp nhận chỉ đánh ở rìa ngoài như "đám ruồi nhặng" để không làm náo động thành phố, nhắc đến việc đặc vụ Bộ Dân ủy Nội vụ đã liên hệ trước và khẳng định sẽ không cản trở "cuộc chiến giả vờ" của họ, khiến Mary cảm thấy cuộc họp tác chiến chẳng khác nào một buổi tụ họp bàn chuyện *không* đánh nhau của những kẻ đồng lõa (`p000050`–`p000065`).
  - Bảo toàn diễn biến khi Drake buộc phải cắt ngang lời Mary, xin lỗi Mikel rồi kéo người cấp dưới thiếu kiềm chế ra ngoài để chấn chỉnh riêng nhằm tránh làm trò cười vì kỷ luật yếu kém (`p000066`–`p000080`).
  - Giữ nguyên lập luận nghiêm khắc của một quân nhân chuyên nghiệp ở Drake: dù xét trên phương diện cá nhân ông hiểu nỗi khao khát trả đũa quân Đế quốc đang chiếm đóng quê hương của Mary, nhưng với tư cách người lính ông ghê tởm sự thiếu suy xét ấy; bởi lính canh Đế quốc đang đóng giữ trong thành phố lớn, nếu quân chính quy càn quét làm lớn chuyện thì chắc chắn sẽ cuốn thường dân vào làn đạn giao tranh, và lời biện hộ "không cố ý" chẳng thể bù đắp cho núi xác người — đó chính là lý do lực lượng du kích địa phương muốn các đơn vị quân chính quy tránh xa khỏi thành phố (`p000081`–`p000097`).
- **Thuật ngữ đã đối chiếu (`canon/glossary.yml`, `canon/glossary-pending.yml`, `work/run-state/pending-terms-index.yml`)**:
  - `Liên bang` (`p000056`) — theo `pending-terms-index.yml`.
  - `Bộ Dân ủy Nội vụ` (`p000057`) — theo `pending-terms-index.yml`.
  - `Trung úy Sue` / `Trung tá Drake` / `Đại tá Mikel` (`p000067`, `p000068`, `p000073`, `p000076`, `p000086`) — theo `pending-terms-index.yml`.
  - `cấp trên` (`p000069`, `p000075`) — theo `pending-terms-index.yml`.
  - `Liên minh Hiệp ước` (`p000069`, `p000071`, `p000081`) — theo `pending-terms-index.yml`.
  - `Đế quốc` (`p000087`, `p000092`) — theo `pending-terms-index.yml`.
  - `cuộc chiến giả vờ` (`p000061`) — đề xuất mới cho thuật ngữ chỉ kiểu tác chiến cầm chừng/giả vờ giao chiến.
  - `những người du kích` / `cuộc họp với lực lượng kháng chiến` (`p000073`, `p000079`, `p000097`), `lính canh của Đế quốc` (`p000092`), `quân nhân chính quy` (`p000097`) — nhất quán với `pending_term_recommendations` trong Argon review.

## 5. Xử lý Argon Review (`vol-06-ch-05-b15-argon-review`)
- **`YS-LN06/Text/part0025.html/p000063` (minor / meaning_nuance)**: Đã đổi `chẳng có lời nào ông nói là lọt tai cô cả` thành `chẳng có lời nào ông nói mà cô hiểu nổi cả` để phản ánh đúng việc Mary không nắm bắt được logic của cuộc họp.
- **`YS-LN06/Text/part0025.html/p000079` (minor / pronouns_pov)**: Đã đổi `trên chính đất nước mình` thành `trên chính đất nước của cô ta` để tách bạch chủ thể quy chiếu với đại từ `mình` của Drake ở đầu câu.
- **Locked choices & Status**: Bảo đảm tuân thủ đầy đủ `locked_choices` cho cả 48 đoạn và nâng toàn bộ `status` từ `draft` sang `reviewed`.
