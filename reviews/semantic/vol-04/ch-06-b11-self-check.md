# Báo cáo tự kiểm (Self-Check): `vol-04-ch-06-b11` (Sign-off)

- **Task ID**: `vol-04-ch-06-b11-translator-signoff` (Parent: `vol-04-ch-06-b11`)
- **Translator**: `argon-low`
- **Handoff**: `handoffs/vol-04/ch-06-b11.yml`, `handoffs/vol-04/ch-06-b11-translator-signoff.yml`
- **Review Report**: `reviews/prose/vol-04/ch-06-b11-argon-review.yml`
- **Tệp dịch**: `translations/vol-04/ch-06-b11.jsonl`
- **Phạm vi**: `YS-LN04/Text/chapter001_v.xhtml/p000321` → `YS-LN04/Text/chapter001_v.xhtml/p000356` (36 đoạn)
- **Trạng thái mỗi dòng**: `reviewed`

## 1. Xử lý các Findings trong Argon Review (`ch-06-b11-argon-review.yml`)
- **`YS-LN04/Text/chapter001_v.xhtml/p000332` (và `p000327`)** (`minor` - `modality_precision`):
  - **Vấn đề**: Động từ tình thái chỉ kỳ vọng hợp lý dựa trên điều kiện giả định bị đẩy thành khẳng định tuyệt đối (`chắc chắn`).
  - **Xử lý**: Đổi `chắc chắn yêu cầu này sẽ được thông qua` thành `hẳn là yêu cầu này sẽ được thông qua` tại `p000332`, và đồng bộ đổi `chắc chắn là làm được thôi` thành `hẳn là làm được thôi` tại `p000327`.
- **`YS-LN04/Text/chapter001_v.xhtml/p000338`** (`minor` - `meaning_precision`):
  - **Vấn đề**: Cụm chỉ vị trí quy chiếu về Xưởng Kỹ thuật dịch thành `ở dưới đó` làm phát sinh sắc thái không gian/cấp bậc không có trong nguồn.
  - **Xử lý**: Đổi `ở dưới đó` thành `ở bên đó`.
- **`YS-LN04/Text/chapter001_v.xhtml/p000356`** (`minor` - `terminology_consistency`):
  - **Vấn đề**: Dịch cụm chỉ phương thức tác chiến hiệp đồng thành `vận hành thành công theo lối hiệp đồng tích hợp` gây cảm giác lặp từ so với đề xuất `tác chiến hiệp đồng` trong sổ pending tập 4.
  - **Xử lý**: Đổi `để vận hành thành công theo lối hiệp đồng tích hợp` thành `để tác chiến hiệp đồng thành công`.

## 2. Kiểm tra tính đầy đủ, nghĩa gốc và tuân thủ `locked_choices`
- Toàn bộ 36 đoạn từ `chapter001_v.xhtml/p000321` đến `chapter001_v.xhtml/p000356` đã được rà soát đối chiếu với `locked_choices` và `pending_term_recommendations` trong `reviews/prose/vol-04/ch-06-b11-argon-review.yml`, khớp 1:1 theo thứ tự mã đoạn của gói nguồn cục bộ.
- Giữ đúng mạch nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic nhân quả và thời gian của giả định:
  - **Tanya đòi thêm xe thiết giáp chiến lợi phẩm từ Cộng hòa để cải tiến pháo lỗi thời thành pháo tự hành (`chapter001_v/p000321`–`p000346`)**: Sau khi ép viên thiếu tá Ban Trang bị về khoản xe tăng mẫu G, Tanya chợt nảy ra ý nghĩ rằng đằng nào mình cũng chẳng bao giờ hòa hợp được với gã này nên cứ coi đây là một trò chơi có tổng bằng không để vắt kiệt từ hắn càng nhiều càng tốt (`p000321`–`p000322`); vì mở miệng hỏi xin cũng đâu mất gì, nó liền hỏi tới số chiến lợi phẩm thu giữ được từ Cộng hòa trong đợt tổng tiến công ở phía Tây, xác nhận có xe tăng và xe thiết giáp dự trữ chưa đưa vào sử dụng chính thức rồi ngỏ ý muốn lấy luôn số xe đó vì hẳn là làm được thôi (`p000323`–`p000327`); khi viên thiếu tá lắp bắp từ chối với lý do đơn vị của Tanya đã có bộ binh và đơn vị thiết giáp rồi nên không thể phá lệ cấp thêm xe thiết giáp, Tanya—vốn nắm rõ từng chi tiết quy định—thấy tội cho gã đang tuyên bố không làm được với vẻ đắc thắng như vừa chém bay đầu quỷ dữ (`p000328`–`p000329`); Tanya lập tức viện dẫn quy định cho phép sửa chữa vũ khí tại chỗ theo thẩm quyền của người chỉ huy, giải thích rằng số xe thiết giáp thu giữ từ Cộng hòa không phải dành cho bộ binh mà dùng để gắn pháo lên nhằm cải tiến đám pháo cũ kỹ thành pháo tự hành, đồng thời tính toán rằng vì số xe này đang nằm kho không có chỗ dùng nên trừ phi Bộ Tổng tham mưu có lý do hợp lý để bác bỏ thì hẳn là yêu cầu sẽ được thông qua, và phần nhiên liệu phát sinh ở chiến trường phòng ngự phía đông sẽ có thể mượn từ Cụm tập đoàn quân phía Đông nhờ các mỏ dầu Esti nên không phải lo thiếu hụt như lực lượng ở lục địa phía nam (`p000330`–`p000334`); trước sự phản đối của viên thiếu tá rằng yêu cầu đó thật vô lý, Tanya nhận ra đòi Ban Trang bị trực tiếp sửa chữa là hơi quá đáng vì chức trách của họ là quản lý chứ không phải tân trang nên lùi một bước, chỉ yêu cầu xuất kho xe thiết giáp còn phần cải tiến sẽ nhờ các mối quen biết ở bên Xưởng Kỹ thuật (kể cả Schugel) làm gấp và cậy nhờ đơn vị huấn luyện chi trả kinh phí dưới danh nghĩa thử nghiệm pháo tự hành (`p000335`–`p000339`); thấy viên thiếu tá vẫn bướng bỉnh lặp đi lặp lại rằng mình không thể làm được dù Tanya đã ăn nói khiêm nhường, nó khẽ gật đầu rồi hỏi thẳng bằng hai từ tiếng Đức in nghiêng để ép hắn chốt câu trả lời có hay không (`p000340`–`p000346`).
  - **Tanya và Trung úy Serebryakov trình diện Trung tướng von Zettour tại Văn phòng Phó Cục trưởng Cục Quân vụ để xin bổ sung thêm một đại đội pháp sư (`chapter001_v/p000347`–`p000356`)**: Bối cảnh chuyển sang ngày 28 tháng 6 năm Thống nhất 1926 tại văn phòng Phó Cục trưởng Cục Quân vụ thuộc Bộ Tổng tham mưu (`p000347`); dù chuyện cấp dưới chạy đến khóc lóc kêu thiếu quân ngay sau khi có lệnh vốn rất quen thuộc với bất kỳ sĩ quan nào ở Bộ Tổng tham mưu, lần này ngay cả Trung tướng von Zettour cũng sững sờ trước lời thỉnh cầu trơ tráo vượt quá sức tưởng tượng từ vị khách của mình (`p000348`–`p000350`); nhìn tờ biểu mẫu được soạn thảo và trình bày hoàn hảo không một lỗi nhỏ, Zettour lẩm bẩm đọc lại yêu cầu xin một đại đội pháp sư bổ sung rồi ngẩng đầu nhìn Trung tá von Degurechaff cùng vị trung úy đi kèm mà ông nhận ra là sĩ quan phụ tá của cô—Trung úy Serebryakov (`p000351`–`p000353`); không kìm được, Zettour hỏi thẳng phải chăng đây là một trò đùa vì Kampfgruppe Salamander vốn đang được thành lập với Tiểu đoàn Pháp sư Trên không số 203 làm đơn vị chủ chốt, nhưng Tanya nghiêm túc đáp lại rằng đó không phải trò đùa và khẳng định một đại đội pháp sư là yếu tố tối quan trọng để tác chiến hiệp đồng thành công (`p000354`–`p000356`).
- Tuyệt đối không sao chép câu hoặc cụm từ tiếng Anh từ nguồn vào báo cáo.

## 3. Kiểm tra đại từ, xưng hô và giọng văn (`DEC-P01-001`)
- Tuân thủ nghiêm ngặt `DEC-P01-001`, `canon/style-guide.md` và mọi mục `pronouns_and_address` trong `locked_choices`:
  - **Trong trần thuật ngôi thứ ba theo điểm nhìn của Tanya (`p000321`–`p000346`)**: quy chiếu `Tanya` nhất quán bằng tên riêng và đại từ `nó` kết hợp phản thân `mình` (`p000321`, `p000332`–`p000334`, `p000337`–`p000339`, `p000344`, `p000345`).
  - **Trong độc thoại nội tâm và bình luận trực tiếp của Tanya (`p000322`, `p000329`, `p000334`, `p000338`)**: tự quy chiếu ngôi thứ nhất số ít bằng `mình` (`p000322`, `p000329`, `p000334`, `p000338`) và số nhiều đại diện đơn vị bằng `chúng ta` (`p000338`).
  - **Trong trần thuật ngôi thứ ba theo điểm nhìn của Trung tướng von Zettour (`p000348`–`p000355`)**: quy chiếu Zettour bằng `ông`, quy chiếu Tanya bằng chức danh `Trung tá von Degurechaff` và đại từ `cô` / `cô ta` (`p000353`, `p000355`).
  - **Trong lời thoại trực tiếp**:
    - Tanya (`Trung tá Tanya von Degurechaff`) xưng `tôi` / `chúng tôi` / `chúng ta`, gọi viên thiếu tá Ban Trang bị là `Thiếu tá` / `anh` / `các anh` (`p000325`, `p000327`, `p000330`, `p000336`, `p000341`, `p000346`); khi đối thoại với Trung tướng von Zettour (`p000356`), Tanya xưng `tôi` và gọi Zettour là `ngài` / `thưa Tướng von Zettour`.
    - Viên thiếu tá Ban Trang bị xưng `tôi`, gọi Tanya là `ngài` / `thưa Trung tá von Degurechaff` / `thưa Trung tá` (`p000328`, `p000335`, `p000342`, `p000344`).
    - Trung tướng von Zettour gọi Tanya là `Trung tá von Degurechaff` (`p000354`).
  - **Quy chiếu các nhân vật khác trong trần thuật**: quy chiếu viên thiếu tá Ban Trang bị bằng `hắn` / `gã này` (`p000322`, `p000329`, `p000343`, `p000344`), quy chiếu Schugel bằng `lão ta` / `lão` (`p000338`).

## 4. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002`)
- Kiểm tra toàn bộ 5 đoạn có thẻ `<html:em>` trong XHTML nguồn và bảo toàn chính xác bằng cặp dấu `*...*` đúng phạm vi nhấn mạnh:
  - `chapter001_v/p000322`: bọc toàn bộ đoạn độc thoại nội tâm của Tanya (`*Đằng nào mình cũng chẳng bao giờ hòa hợp được với gã này. Nếu đã vậy, có lẽ cứ coi đây là một trò chơi có tổng bằng không rồi vắt kiệt từ hắn càng nhiều càng tốt mới là hợp lý.*`).
  - `chapter001_v/p000337`: chỉ bọc mệnh đề suy nghĩ ở câu đầu (`*Có lẽ yêu cầu Ban Trang bị thực hiện việc “sửa chữa” là hơi quá đáng,*`), phần trần thuật còn lại nằm ngoài dấu `*`.
  - `chapter001_v/p000338`: chỉ bọc mệnh đề quyết định ở đầu câu thứ nhất (`*Chắc mình sẽ phải làm phiền Xưởng Kỹ thuật làm gấp cho chúng ta vụ này vậy*`), phần dẫn và các câu sau nằm ngoài dấu `*`.
  - `chapter001_v/p000346`: bọc đúng hai từ ngoại ngữ in nghiêng trong câu thoại (`*ja*` và `*nein*`).
  - `chapter001_v/p000353`: chỉ bọc câu suy nghĩ nội tâm của Zettour ở cuối đoạn (`*Trung tá von Degurechaff đã dẫn người kia đi cùng, nên chắc hẳn đó là… ờ, đúng rồi, sĩ quan phụ tá của cô ta, Trung úy Serebryakov.*`).
- Toàn bộ 31 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và không phát sinh dấu `*` ngoài nguồn.

## 5. Kiểm tra thuật ngữ và tính nhất quán (`canon/` & `pending_term_recommendations`)
- Các thuật ngữ đã khóa và đề xuất trong `argon-review` được áp dụng đầy đủ, nhất quán:
  - `trò chơi có tổng bằng không` (`p000322`)
  - `pháo tự hành` (`p000330`, `p000331`) / `cuộc thử nghiệm pháo tự hành` (`p000339`)
  - `các mỏ dầu Esti` / `Cụm tập đoàn quân phía Đông` (`p000333`)
  - `Xưởng Kỹ thuật` (`p000338`)
  - `BỘ TỔNG THAM MƯU, VĂN PHÒNG PHÓ CỤC TRƯỞNG CỤC QUÂN VỤ` (`p000347`)
  - `đại đội pháp sư bổ sung` (`p000351`)
  - `Kampfgruppe Salamander` / `Tiểu đoàn Pháp sư Trên không số 203` (`p000355`)
  - `tác chiến hiệp đồng` (`p000356`).

## 6. Kiểm tra định dạng và công cụ xác thực
- Đã kiểm tra cấu trúc JSONL tại `translations/vol-04/ch-06-b11.jsonl`: 36 dòng hợp lệ, đầy đủ các trường bắt buộc (`segment_id`, `translation`, `status`, `translator`, `glossary_version`, `source_sha256`, `notes`), trường `status` của toàn bộ 36 dòng đã được cập nhật từ `draft` sang `reviewed`.
- Chạy `python3 tools/validate_translation.py --handoff handoffs/vol-04/ch-06-b11.yml --source work/vol-04/batches/ch-06-b11-source.jsonl --translation translations/vol-04/ch-06-b11.jsonl` để xác nhận kết quả `PASS`.
