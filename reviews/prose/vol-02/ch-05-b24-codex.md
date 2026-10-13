# Review — vol-02-ch-05-b24-review

- Vai trò: reviewer; phạm vi: đủ 45 stable ID từ `YS-LN02/Text/part0026.xhtml/p000619` đến `YS-LN02/Text/part0026.xhtml/p000663`.
- Đã đọc shared/reviewer, config, review handoff, base handoff để xác định đúng canon, package được giao, bản dịch, self-check và nhóm `chapter5_b24_translation_proposals` trong pending ledger.
- SHA-256 package: `c5224e7578fcd60814af26eaf861a74580b9c326af58950ce74c741c54461a6a`, khớp review handoff. Package và bản dịch cùng 45 ID, đúng thứ tự. Hash của cả năm canon được base handoff tham chiếu đều khớp: glossary, style-guide, characters, decisions, glossary-pending.
- Chỉ đối chiếu nguồn trong package được giao; không mở EPUB/PDF hoặc package khác. Không sửa đầu vào. Các mô tả căn cứ dưới đây là diễn giải, không trích câu nguồn.
- Kết quả: **serious 0, moderate 2, minor 8**; tất cả 10 findings còn mở vì reviewer không sửa bản dịch. **Unresolved serious 0; unresolved moderate 2.** Chưa đủ điều kiện đóng review của bản dịch cho tới khi xử lý hai lỗi vừa.
- Validator: `not_run`; diff_check: `not_run`; commit: `null`.

## Findings có thể hành động

### Moderate

1. **F01 — YS-LN02/Text/part0026.xhtml/p000626 — mức chắc chắn của giả định quá khứ.** “Có lẽ tôi đã” làm hậu quả nếu Weiss không cứu trở thành phỏng đoán. Nguồn diễn đạt hậu quả xác định trong điều kiện trái thực tế, không thêm mức bất định này. Đề xuất bỏ “có lẽ”, dùng “nếu anh ấy không cứu tôi, tôi đã bị nghiền nát…”; giữ cả điều kiện và thời quá khứ. Không biến thành khẳng định Grantz thực sự đã chết.
2. **F02 — YS-LN02/Text/part0026.xhtml/p000663 — sai hành động của cần vụ.** “Đứng chờ tôi” hiểu thành chờ đợi, trong khi ngữ cảnh và động từ của nguồn nói cần vụ phục vụ Grantz khi thức ăn được đưa ra. Đề xuất “Người cần vụ của tôi phục vụ tôi, thức ăn cũng được mang ra…” hoặc cấu trúc tương đương giữ hai sự việc. Không cần xác định cần vụ có trực tiếp mang thức ăn hay không.

### Minor

3. **F03 — YS-LN02/Text/part0026.xhtml/p000619 — thiếu nhấn mạnh toàn câu.** XHTML nhấn mạnh toàn bộ lời hướng tới Thượng đế; trường translation hiện không có `*...*`. Bọc toàn câu bằng Markdown theo DEC-P01-002. Self-check nói đã giữ nhấn mạnh ở đây nhưng bản được giao chưa giữ.
4. **F04 — YS-LN02/Text/part0026.xhtml/p000620 — thêm tư thế và thu hẹp nơi ở.** Nguồn chỉ đặt Grantz ở góc nơi ở của anh, không xác định anh đứng hay đó là phòng trọ thuê. Đề xuất “Thiếu úy Pháp sư Warren Grantz than trời trách đất ở một góc chỗ ở của mình”; không thêm tư thế. “Bữa tối hôm trước” chấp nhận được trong ngữ cảnh đêm trước, không cần phát sinh finding riêng.
5. **F05 — YS-LN02/Text/part0026.xhtml/p000626 — thiếu một phạm vi nhấn mạnh.** Nguồn có hai phạm vi: ý nghĩ sợ bị bỏ lại và lời Weiss mắng. Bản dịch chỉ đánh dấu phạm vi thứ hai. Đề xuất `*Không muốn bị bỏ lại*` cho phần ý nghĩ đầu; có thể bỏ ngoặc kép đang dùng thay dấu nhấn. Giữ nguyên phần lời mắng đã đánh dấu đúng.
6. **F06 — YS-LN02/Text/part0026.xhtml/p000626 — mất chi tiết cùng thời điểm đến mặt trận.** “Những người cùng ra mặt trận với tôi” có thể gợi đi cùng nhau, còn nguồn xác định hai người kia đến mặt trận cùng thời điểm với Grantz. Đề xuất “hai gã kia, những người đến mặt trận cùng lúc với tôi”. Không suy ra họ cùng chuyến đi hoặc quan hệ thân thiết.
7. **F07 — YS-LN02/Text/part0026.xhtml/p000631 — thêm kết quả tổn thương.** “Đập vỡ đầu” thêm kết quả đầu bị vỡ; nguồn ở đây hồi tưởng cảm giác đánh mạnh vào đầu người khác. Đề xuất “cảm giác nện vào đầu ai đó lại ùa về trong đôi tay tôi”. Giữ cơn buồn nôn và việc mọi tân binh có cùng cảm giác.
8. **F08 — YS-LN02/Text/part0026.xhtml/p000633 — chưa rõ ai bị nỗi lo giày vò.** “Mặc cho nỗi lo đang giày vò” không nêu đối tượng, dễ đọc thành nỗi lo của các sĩ quan cấp cao. Nguồn đặt nỗi lo ở nhóm người kể; cảnh thẩm vấn diễn ra ngay cạnh họ. Đề xuất “Ngay cạnh chúng tôi, những người đang bị nỗi lo giày vò, các sĩ quan cấp cao lạnh lùng bắt đầu thẩm vấn tù binh.” Có thể viết tự nhiên hơn bằng “Trong lúc chúng tôi còn bị nỗi lo giày vò, ngay bên cạnh, …”. Không cần thêm động cơ phớt lờ của sĩ quan.
9. **F09 — YS-LN02/Text/part0026.xhtml/p000658 — chuyển khó khăn sang thời điểm.** “Chỉ vừa kịp ghìm” làm nổi bật kịp thời; nguồn nhấn vào việc Grantz chật vật mới ghìm được cơn buồn nôn. Đề xuất “Tựa vào bồn rửa, tôi chật vật ghìm cơn buồn nôn đang dâng lên, rồi ngước nhìn trời.” Không thêm hành động nôn ở đoạn này.
10. **F10 — YS-LN02/Text/part0026.xhtml/p000662 — kết hợp từ nhượng bộ gượng.** “Dù những chuyện vừa xảy ra” chưa tự nhiên vì “dù” đứng trước cụm danh từ không thành mệnh đề. Đề xuất “Bất chấp những chuyện vừa xảy ra, tôi vẫn nghe thấy cả tiếng cười” hoặc “Dù vừa trải qua những chuyện ấy, họ vẫn cười…”, ưu tiên phương án đầu để giữ chính xác người nghe và không thay cấu trúc sự việc. Phần tương phản và ghê tởm phía sau giữ đúng nghĩa.

## Đánh giá ba minor findings trong self-check

| Stable ID | Đánh giá | Hành động |
| --- | --- | --- |
| YS-LN02/Text/part0026.xhtml/p000629 | “Hai người” giữ đúng số lượng và trung tính. Package có cách gọi hai người ở p000626 nhưng không buộc phải thêm giới tính/chức vụ vào đây. Quan hệ phản ứng chậm–mất mạng được giữ. | Không còn vấn đề có thể hành động từ finding này; giữ bản hiện tại. |
| YS-LN02/Text/part0026.xhtml/p000633 | Cách chọn trung tính chưa làm rõ nỗi lo thuộc nhóm Grantz, và thêm quan hệ nhượng bộ thay cho sự đặt cạnh nhau. | Xử lý F08; không coi lựa chọn hiện tại đã giải quyết hoàn toàn. |
| YS-LN02/Text/part0026.xhtml/p000663 | “Cần vụ” phù hợp tạm thời; “riêng” không cần thiết nhưng không đủ căn cứ để coi là sai độc lập. Vấn đề có căn cứ là hành động phục vụ bị đổi thành đứng chờ. | Xử lý F02; ưu tiên “người cần vụ của tôi”. Finding về thuật ngữ tự nó không cần chờ canon. |

## Tám khuyến nghị thuật ngữ tạm thời

Mọi lựa chọn dưới đây có trạng thái **provisional_non_canon**. Glossary và characters chưa chốt mục nào; các quyết định đã duyệt chỉ chi phối giới hạn suy luận và dấu nhấn. Không viện dẫn lịch sử lô trước ngoài thông tin ledger được giao, không đồng nhất tên thần/quỷ với nhân vật lore.

| Thuật ngữ | Stable ID | Khuyến nghị tạm | Phương án thay thế | Lý do và độ bất định |
| --- | --- | --- | --- | --- |
| God | YS-LN02/Text/part0026.xhtml/p000619; YS-LN02/Text/part0026.xhtml/p000628 | Thượng đế | Chúa | Một lời than và một lời cảm tạ hướng tới thần linh; “Thượng đế” giữ nhất quán và không tự xác định giáo phái. “Đấng Tạo Hóa” trong ledger thêm vai trò sáng tạo chưa được package chứng minh, nên không ưu tiên. Bất định: danh xưng tôn giáo/lore chưa canon; không cần quyết định lore để dịch hai đoạn. |
| devil | YS-LN02/Text/part0026.xhtml/p000625 | quỷ dữ | quỷ | Cách nói đối chiếu số phận với tác động của quỷ trong hồi tưởng hoảng loạn; “quỷ dữ” giữ sắc thái bất lợi, không gán tên riêng. Bất định: chưa đủ căn cứ xác định một thực thể cụ thể, nên giữ chữ thường và nghĩa chung. |
| Magic Second Lieutenant | YS-LN02/Text/part0026.xhtml/p000620 | Thiếu úy Pháp sư | Thiếu úy ma pháp | Giữ cấp thiếu úy và đặc tính quân nhân sử dụng ma pháp; package có hành động dùng ma lực và bay hỗ trợ cách hiểu này. Không biến thành trung úy hoặc chức vụ chỉ huy. Bất định: tên chính thức của binh chủng chưa chốt; giữ dạng hiện tại tạm thời, không coi là chuẩn quân hàm toàn truyện. |
| computation orb | YS-LN02/Text/part0026.xhtml/p000622; YS-LN02/Text/part0026.xhtml/p000628 | quả cầu tính toán | cầu tính toán | Giữ thành tố hình dạng và chức năng của tên thiết bị, dùng cùng một dạng ở chỗ truyền ma lực và chỗ xem cảnh ghi lại. Bất định: cấu tạo/cơ chế chưa được package giải thích; không đổi sang thiết bị tính toán hoặc thêm mô tả kỹ thuật. |
| protective film | YS-LN02/Text/part0026.xhtml/p000624 | màn bảo hộ | màng bảo hộ | Hai lớp phòng vệ được liệt kê riêng; “màn bảo hộ” phân biệt với “lớp vỏ phòng ngự” và giữ lựa chọn ledger. “Màng bảo hộ” sát nét lớp mỏng hơn nếu ngữ cảnh được phép sau này xác nhận. Bất định: độ mỏng và hình dạng chưa đủ căn cứ để buộc đổi; đây là lựa chọn tạm, không xác nhận tính nhất quán với package khác. |
| battalion commander | YS-LN02/Text/part0026.xhtml/p000625; YS-LN02/Text/part0026.xhtml/p000626; YS-LN02/Text/part0026.xhtml/p000661 | tiểu đoàn trưởng | chỉ huy tiểu đoàn | Diễn đạt chức vụ, không gán quân hàm cá nhân. Trong p000626 và p000661 nguồn dùng dạng chỉ huy rút gọn; bản dịch “chỉ huy” được phép giữ vì quy chiếu trong package đã rõ. Bất định thấp về chức vụ, còn tên và quân hàm không được xác lập. Đại từ “cô ấy” ở hồi tưởng Grantz có căn cứ tại p000625; không tự mở rộng quy ước đại từ Tanya của pilot sang mọi chủ thể/giai đoạn. |
| officers’ mess | YS-LN02/Text/part0026.xhtml/p000652; YS-LN02/Text/part0026.xhtml/p000653; YS-LN02/Text/part0026.xhtml/p000660 | nhà ăn sĩ quan | phòng ăn sĩ quan | Package trực tiếp mô tả bữa sáng, quyền dùng địa điểm và chuyện trò khi ăn; “nhà ăn sĩ quan” phù hợp chức năng, giữ nhất quán. Giữ “tạm thời” ở p000652. Bất định: không xác định quy mô tòa nhà hay chức năng ngoài ăn uống; không tự dịch thành câu lạc bộ. |
| batman | YS-LN02/Text/part0026.xhtml/p000652; YS-LN02/Text/part0026.xhtml/p000663 | cần vụ | người hầu cận quân đội | Ngữ cảnh là người phục vụ sĩ quan, báo bữa sáng và phục vụ Grantz; “cần vụ” gọn, không gán cấp bậc. p000652 dùng số nhiều “các cần vụ”; p000663 dùng “người cần vụ của tôi”. Bất định: chưa rõ tổ chức phân công hoặc tính độc quyền; tránh thêm “riêng”, và phải sửa động tác theo F02. |

## Bao phủ 45 ID: nghĩa, văn phong, điểm nhìn, nhấn mạnh, thuật ngữ

Mỗi hàng xác nhận đã đối chiếu cả năm mặt. “Không finding thêm” nghĩa là không có lỗi có căn cứ ngoài các đề xuất thuật ngữ tạm ở trên; không phải phê duyệt canon. Tiền tố đầy đủ của mọi ID là `YS-LN02/Text/part0026.xhtml/`.

| Stable ID | Kết quả |
| --- | --- |
| YS-LN02/Text/part0026.xhtml/p000619 | F03; lời hướng tới thần linh và câu hỏi giữ đúng nghĩa. |
| YS-LN02/Text/part0026.xhtml/p000620 | F04; ngôi ba giới thiệu Grantz, cấp bậc được giữ tạm. |
| YS-LN02/Text/part0026.xhtml/p000621 | Không finding thêm; hành động, mệnh lệnh và thứ tự rút quân đúng. |
| YS-LN02/Text/part0026.xhtml/p000622 | Không finding thêm; ma lực, thiết bị, nỗ lực thoát thân đúng. |
| YS-LN02/Text/part0026.xhtml/p000623 | Không finding thêm; thời điểm cất cánh và súng máy bắn đúng. |
| YS-LN02/Text/part0026.xhtml/p000624 | Không finding thêm; hai lớp phòng vệ và quên yểm trợ đúng. |
| YS-LN02/Text/part0026.xhtml/p000625 | Không finding thêm; tốc độ bay lên, thánh ca và nỗi sợ bị bỏ lại đúng. |
| YS-LN02/Text/part0026.xhtml/p000626 | F01, F05, F06; hành động Weiss cứu, mồi nhử và lời mắng còn lại đúng. |
| YS-LN02/Text/part0026.xhtml/p000627 | Không finding thêm; phạm vi ký ức mơ hồ và nguyên nhân đúng. |
| YS-LN02/Text/part0026.xhtml/p000628 | Không finding thêm; ghi cảnh trong thiết bị, cảm tạ và mưa lửa đúng. |
| YS-LN02/Text/part0026.xhtml/p000629 | Không finding thêm; số người, đơn vị, phản ứng chậm và hậu quả đúng. |
| YS-LN02/Text/part0026.xhtml/p000630 | Không finding thêm; nhịp câu ngắn giữ sức nặng hậu quả. |
| YS-LN02/Text/part0026.xhtml/p000631 | F07; cảm giác ở tay, buồn nôn và phạm vi toàn bộ tân binh giữ đúng. |
| YS-LN02/Text/part0026.xhtml/p000632 | Không finding thêm; cảm giác tội lỗi là nhận thức của Grantz. |
| YS-LN02/Text/part0026.xhtml/p000633 | F08; hoạt động thẩm vấn và sự lạnh lùng giữ đúng. |
| YS-LN02/Text/part0026.xhtml/p000634 | Không finding thêm; giữ đe dọa gián tiếp, không thêm hành động tra tấn. |
| YS-LN02/Text/part0026.xhtml/p000635 | Không finding thêm; giữ lời viện dẫn luật, điều kiện tuyên thệ và quyền lợi; không đánh giá tính hợp pháp ngoài văn bản. |
| YS-LN02/Text/part0026.xhtml/p000636 | Không finding thêm; lời tự nhận tử tế/suy xét giữ tương phản mỉa mai trong ngữ cảnh. |
| YS-LN02/Text/part0026.xhtml/p000637 | Không finding thêm; phản ứng không tin được giữ. |
| YS-LN02/Text/part0026.xhtml/p000638 | Không finding thêm; đối tượng nghi vấn là khả năng con người. |
| YS-LN02/Text/part0026.xhtml/p000639 | Không finding thêm; giữ câu mảnh về chiến trường. |
| YS-LN02/Text/part0026.xhtml/p000640 | Không finding thêm; niềm tin trước đó và quan hệ quân ngũ–bổn phận rõ trong ngữ cảnh. |
| YS-LN02/Text/part0026.xhtml/p000641 | Không finding thêm; nhấn riêng động từ suy nghĩ đúng. |
| YS-LN02/Text/part0026.xhtml/p000642 | Không finding thêm; câu hỏi nội tâm giữ độ mở. |
| YS-LN02/Text/part0026.xhtml/p000643 | Không finding thêm; nghi vấn bổn phận/bảo vệ tổ quốc đúng. |
| YS-LN02/Text/part0026.xhtml/p000644 | Không finding thêm; nhấn sở hữu “của tôi” đúng. |
| YS-LN02/Text/part0026.xhtml/p000645 | Không finding thêm; cảm giác không chịu nổi và mất bản thân đúng. |
| YS-LN02/Text/part0026.xhtml/p000646 | Không finding thêm; ngập ngừng và lần đầu tự tay giết người đúng. |
| YS-LN02/Text/part0026.xhtml/p000647 | Không finding thêm; tương phản tối–sáng và sự biến mất đúng. |
| YS-LN02/Text/part0026.xhtml/p000648 | Không finding thêm; phân biệt tôi giết và bạn bè bị giết đúng. |
| YS-LN02/Text/part0026.xhtml/p000649 | Không finding thêm; tên Rhine giữ nguyên, lặp khẳng định địa ngục đúng. |
| YS-LN02/Text/part0026.xhtml/p000650 | Không finding thêm; ý muốn bỏ chạy chỉ thoáng qua. |
| YS-LN02/Text/part0026.xhtml/p000651 | Không finding thêm; giữ nhịp chuyển bằng gạch ngang. |
| YS-LN02/Text/part0026.xhtml/p000652 | Không finding thêm; số nhiều cần vụ, căn cứ hậu phương và quyền ăn đúng. |
| YS-LN02/Text/part0026.xhtml/p000653 | Không finding thêm; chuyển quyền thành nghĩa vụ và nhấn “phải” đúng. |
| YS-LN02/Text/part0026.xhtml/p000654 | Không finding thêm; động tác, gương và tự nhận quái vật giữ đúng điểm nhìn. |
| YS-LN02/Text/part0026.xhtml/p000655 | Không finding thêm; lời nói bật ra sau trải nghiệm chiến tranh đúng. |
| YS-LN02/Text/part0026.xhtml/p000656 | Không finding thêm; âm lượng nhỏ và câu mảnh được giữ. |
| YS-LN02/Text/part0026.xhtml/p000657 | Không finding thêm; ý nghĩ tự bật thành lời đúng. |
| YS-LN02/Text/part0026.xhtml/p000658 | F09; bồn rửa, ghìm buồn nôn rồi nhìn trời đúng trình tự. |
| YS-LN02/Text/part0026.xhtml/p000659 | Không finding thêm; câu hỏi về cư xử bình thường và nhấn toàn câu đúng. |
| YS-LN02/Text/part0026.xhtml/p000660 | Không finding thêm; cảm giác tăng ngay lúc vào nhà ăn đúng. |
| YS-LN02/Text/part0026.xhtml/p000661 | Không finding thêm; sĩ quan đông, chỉ huy đã ăn và làm việc, chuyện trò thong thả đúng. |
| YS-LN02/Text/part0026.xhtml/p000662 | F10; tương phản chiến trường–nhà ăn và ghê tởm giữ đúng điểm nhìn. |
| YS-LN02/Text/part0026.xhtml/p000663 | F02; thiếu ngon miệng và thói quen ép ăn dù vậy giữ đúng. |

## Rủi ro và bàn giao

- Hai lỗi vừa còn mở: F01 (p000626), F02 (p000663). Translator xử lý; reviewer không sửa translation hoặc self-check.
- Self-check hiện đánh giá quá cao việc giữ nhấn mạnh: thiếu cả câu p000619 và ý nghĩ đầu p000626. Báo cáo này chỉ ghi chênh lệch, không sửa self-check.
- Không có quyết định canon ảnh hưởng cốt truyện cần dừng trong phạm vi package. Tám lựa chọn vẫn là đề xuất; độ bất định về lore, tên binh chủng và tổ chức cần vụ được giữ rõ, không chờ người dùng để tiếp tục xử lý bản dịch.
- Không kiểm chứng tính nhất quán với nguồn/lô khác vì ngoài phạm vi được phép. Validator và diff-check do coordinator thực hiện sau bước sửa; reviewer không chạy và không commit.
