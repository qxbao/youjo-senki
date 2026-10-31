# Báo cáo tự kiểm & Sign-off (Self-Check): `vol-05-ch-01-b14`

- **Task ID**: `vol-05-ch-01-b14-translator-signoff` (Parent: `vol-05-ch-01-b14`)
- **Translator**: `argon-low`
- **Handoff**: `handoffs/vol-05/ch-01-b14.yml`, `handoffs/vol-05/ch-01-b14-translator-signoff.yml`
- **Review tiếp nhận**: `reviews/prose/vol-05/ch-01-b14-argon-review.yml`
- **Tệp dịch**: `translations/vol-05/ch-01-b14.jsonl`
- **Phạm vi**: `YS-LN05/Text/part0010.html/p000467` → `YS-LN05/Text/part0010.html/p000505` (39 đoạn)
- **Trạng thái mỗi dòng**: `reviewed`

## 1. Kiểm tra tính đầy đủ, nghĩa gốc và xử lý Argon Review
- Đã dịch và rà soát đầy đủ 39 đoạn từ `part0010.html/p000467` đến `part0010.html/p000505` sang tiếng Việt, khớp 1:1 theo thứ tự mã đoạn của gói nguồn cục bộ.
- Tiếp nhận và xử lý đầy đủ các findings và `locked_choices` trong `reviews/prose/vol-05/ch-01-b14-argon-review.yml`:
  - `YS-LN05/Text/part0010.html/p000475` (`minor` / `meaning_nuance`): Đã chỉnh mệnh đề chỉ đạo đơn vị thiết giáp thành `cứ giả định đây là lực lượng dự bị của địch` (bỏ từ hạn định `mới chỉ là`) và đồng bộ `đại đội dự bị` theo đúng khuyến nghị của Argon review.
  - `YS-LN05/Text/part0010.html/p000485` (`locked_choices`): Đã lược bỏ lượng từ `đám` trước `quân du kích` (`Hẳn quân du kích đã phát hiện ra chúng ta vào ban ngày`) để khớp hoàn toàn với `locked_choices` và `pending_term_recommendations`.
  - `YS-LN05/Text/part0010.html/p000491` & `YS-LN05/Text/part0010.html/p000498` (`minor` / `style_tone`): Đã đổi `đám lính nghĩa vụ` thành `những người lính nghĩa vụ` ở `p000491` và đổi `đám nhân sự hậu phương` thành `các nhân sự hậu phương` ở `p000498` nhằm giữ sắc thái trung tính đối với quân mình theo `canon/style-guide.md`.
- Giữ nguyên nghĩa, phủ định, đối tượng câu hỏi, chỉ dẫn, logic nhân quả và thời gian của giả định:
  - **Sự hoài nghi của Tanya trước đòn tiến công bằng hai tiểu đoàn và quyết định giữ lại lực lượng pháp sư (`p000467`–`p000481`)**: Khi Thiếu tá Weiss ngập ngừng định thắc mắc (`p000467`), Tanya tự nhủ rằng nếu là một cuộc chạm trán bất ngờ hoặc chỉ huy địch quyết định cho quân ập vào ngay thì còn có thể hiểu và châm chước được, nhưng một kẻ địch đã nắm khá rõ sức chiến đấu của quân mình qua nhiều cuộc giao tranh nhỏ thì đời nào lại tung ra một đòn tấn công vụng về đến thế (`p000468`–`p000471`); Tanya khẳng định việc cố cưỡng bức đột nhập chỉ với hai tiểu đoàn là vô lý (`p000472`); với người muốn tránh rủi ro, nỗi tiếc nuối vì quá thận trọng vẫn đáng chọn hơn cảm giác thỏa mãn khi tưởng mình đã nhìn thấu kế hoạch của địch—dù trong tiến công người ta có thể không thích sự dè dặt, nhưng đây là nhiệm vụ phòng ngự nhằm giữ mức tiêu hao ở ngưỡng tối thiểu (`p000473`–`p000474`); vì vậy, Tanya ra lệnh báo cho đơn vị thiết giáp cứ giả định đây là lực lượng dự bị của địch, giữ lại đơn vị pháp sư để ứng cứu các điểm nóng, đồng thời cho đại đội dự bị xuất kích khẩn cấp không phải để chủ động giao chiến mà để làm tai mắt trên chiến trường (`p000475`); nhìn Weiss chào chuẩn mực rồi vội vã quay về đơn vị, Tanya cười chua chát và tin rằng anh sẽ làm việc chăm chỉ cho xứng với chỗ cà phê đã uống (`p000476`–`p000477`); nó tự giải thích cách nói đó xuất phát từ ý thức về chi phí—bằng chứng cho thấy mình đã lấy lại cảm quan lành mạnh về nguyên lý thị trường và vẫn giữ được sức khỏe tinh thần lẫn thể chất ngay nơi tiền tuyến dễ làm mất nhân tính, điều vô cùng dễ chịu với một cá nhân tự do, hiện đại, dù chiến trường chẳng cho phép đắm mình trong niềm vui giản dị ấy (`p000478`–`p000481`).
  - **Cuộc đột kích bất ngờ nhắm thẳng vào sở chỉ huy và đặc thù tác chiến không chiến hào ở mặt trận phía Đông (`p000482`–`p000496`)**: Tiếng báo động khẩn cấp vang lên báo tin quân địch đang tấn công ngay tại sở chỉ huy cùng mệnh lệnh đánh chặn (`p000482`–`p000483`); Tanya vừa thấy đúng như dự liệu vừa kinh ngạc vì địch đánh thẳng vào sở chỉ huy, nhận định nếu ở dưới chiến hào thì chuyện này đã không xảy ra và hẳn quân du kích đã phát hiện ra vị trí của họ vào ban ngày (`p000484`–`p000485`); do cần nhiều hơn vài ngày mới nắm rõ địa hình ngôi làng đang đồn trú, lại thêm khu vực phòng thủ rộng hơn dự kiến trong khi thiếu nhân lực bao quát địa bàn dù đã cử đội tuần tra, tuyến cảnh giới xuất hiện lỗ hổng và dẫn tới đòn tập kích không lường trước này (`p000486`–`p000488`); binh lính vừa chửi thề vừa vớ súng trường trước việc địch nhắm thẳng vào sở chỉ huy, nhưng nhân sự hậu phương của Kampfgruppe chỉ là vài nhân viên tham mưu—tuy là lính nên biết bắn súng nhưng bắn có trúng hay không lại là chuyện khác (`p000489`–`p000490`); lực lượng đáng cậy nhờ lúc này là những người lính nghĩa vụ bảo vệ sở chỉ huy, song do thiếu quân nên đã phải rút bớt từ đơn vị cảnh vệ ra chi viện tiền tuyến, khiến thế bất lợi trầm trọng về quân số là không thể tránh khỏi (`p000491`); giữa tiếng than thở rằng tác chiến ở mặt trận phía Đông khác hẳn chiến tranh chiến hào, Tanya phân tích rằng miền Đông không có chiến hào vì chiến tuyến quá dài, không đủ quân để đào công sự và trấn giữ toàn tuyến, dẫn tới việc không thể phân biệt tuyến một với tuyến hai, lính hậu phương cũng có thể phải chiến đấu và chỉ một thoáng lơ là cũng biến thành xác chết trước dao găm, lưỡi lê hay xẻng—nên việc yêu cầu nhân viên sở chỉ huy qua huấn luyện tối thiểu là hoàn toàn đúng đắn (`p000492`–`p000496`).
  - **Tung Tiểu đoàn Pháp sư Trên không số 203 phản kích từ trung tâm và xoay chuyển cục diện (`p000497`–`p000505`)**: Khi cấp dưới hoảng hốt báo tin đã bị bao vây hoàn toàn, Tanya vừa mỉm cười vừa gầm lên trấn an các nhân sự hậu phương rằng họ chỉ đang làm theo đúng kế hoạch ban đầu là cố thủ phòng ngự tại chỗ và chính địch mới đang lúng túng chưa biết tấn công thế nào (`p000497`–`p000498`); nó nhận định địch khôn ngoan không có nghĩa là phải cuốn theo kế hoạch của chúng, muốn đánh tan tác chúng thì chỉ cần thổi bay từ phần lõi (`p000499`); nhận thấy chủ lực địch đã tập trung gần như toàn bộ tại đây, Tanya lập tức hạ lệnh cho Thiếu tá Weiss đánh tan quân địch, và Weiss hô toàn tiểu đoàn xuất kích đánh chặn ngay lập tức kèm lời nhắc không nhận nhầm quân mình (`p000500`–`p000501`); Tanya tung ra đơn vị dự bị cưng mà mình quyết giữ lại dù phải giảm lính gác sở chỉ huy—Tiểu đoàn Pháp sư Trên không số 203, một cỗ máy bạo lực hoàn hảo từng dày dạn kinh nghiệm ở Dacia, Norden và mặt trận Rhine nay tiếp tục phát huy hiệu quả kỳ diệu trên vùng đất phương Đông mênh mông (`p000502`–`p000503`); các tiểu đoàn bộ binh Liên bang vốn định bao vây bào mòn quân Đế quốc liền bị giáng một loạt thuật thức phát nổ trực diện, bị chiếm lĩnh bầu trời ngay trên đầu trong lúc hoảng loạn rồi nhận lời khuyên đầu hàng (`p000504`); cục diện nhanh chóng ngã ngũ theo hướng có lợi cho Đế quốc, khẳng định giá trị của một tiểu đoàn pháp sư dự bị như quân bài tẩy lợi hại mà không ai có thể ung dung đấu súng trừ phi trận địa dày đặc pháo phòng không như tổ ong (`p000505`).
- Tuyệt đối không sao chép câu hoặc cụm từ nguồn tiếng Anh vào báo cáo.

## 2. Kiểm tra đại từ, xưng hô và giọng văn (`DEC-P01-001`)
- Phân biệt rõ điểm nhìn và quy ước đại từ theo `DEC-P01-001` cùng `canon/style-guide.md`:
  - **Trong trần thuật ngôi thứ ba (`p000477`, `p000498`)**: giữ tên `Tanya` trong câu trần thuật mô tả hành động bên ngoài (`Tanya nở nụ cười chua chát`, `Tanya vừa mỉm cười`).
  - **Trong độc thoại nội tâm / tự quy chiếu của Tanya (`p000468`, `p000469`, `p000473`, `p000477`–`p000480`, `p000484`–`p000488`, `p000491`, `p000493`, `p000496`, `p000502`–`p000504`)**: dùng `mình` khi tự quy chiếu cá nhân và `chúng ta` khi quy chiếu tập thể đơn vị/quân mình; dùng `bạn` cho chủ thể giả định khái quát ở `p000499`, `p000505`.
  - **Trong lời thoại trực tiếp (`p000467`, `p000472`, `p000475`, `p000476`, `p000482`, `p000483`, `p000489`, `p000492`, `p000497`, `p000498`, `p000500`, `p000501`)**:
    - Tanya (`Trung tá`) xưng `tôi` / `chúng ta`, gọi Thiếu tá Weiss là `Thiếu tá Weiss`, ra lệnh dứt khoát và uy quyền.
    - Thiếu tá Weiss (`p000467`, `p000476`, `p000501`) gọi Tanya là `Trung tá` (`thưa Trung tá`), khi hạ lệnh cho thuộc cấp thì hô dứt khoát (`Toàn tiểu đoàn, xuất kích!`).
    - Binh lính và nhân sự tại sở chỉ huy (`p000482`, `p000489`, `p000492`, `p000497`) dùng khẩu ngữ chiến trường khẩn trương, gọi Tanya là `Trung tá` kèm `ạ` khi báo cáo trực tiếp.

## 3. Kiểm tra bảo toàn nhấn mạnh (`DEC-P01-002`)
- Đối chiếu toàn bộ 39 đoạn với thẻ `<html:em>` trong XHTML nguồn:
  - `part0010.html/p000477`: bảo toàn nhấn mạnh đúng câu nội tâm cuối đoạn bằng `*Mình tin chắc anh ta sẽ làm việc chăm chỉ cho xứng với chỗ cà phê đã uống.*`, phần trần thuật phía trước để ngoài dấu `*`.
  - `part0010.html/p000481`: bảo toàn nhấn mạnh từ cảm thán mở đầu bằng `*Thật tình*`, phần còn lại của đoạn để ngoài dấu `*`.
- Toàn bộ 37 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và không tự ý thêm dấu `*...*`.

## 4. Kiểm tra thuật ngữ và tính nhất quán (`canon/` & `pending_term_recommendations`)
- Tuân thủ đầy đủ toàn bộ 13 mục `pending_term_recommendations` và `locked_choices` trong `reviews/prose/vol-05/ch-01-b14-argon-review.yml`:
  - `ý thức về chi phí` (`p000478`)
  - `sở chỉ huy` (`p000482`, `p000484`, `p000489`, `p000490`, `p000491`, `p000496`, `p000502`)
  - `đánh chặn` (`p000483`, `p000501`)
  - `quân du kích` (`p000485`)
  - `tuyến cảnh giới` (`p000488`)
  - `nhân sự hậu phương` (`p000490`, `p000498`)
  - `Kampfgruppe` (`p000490`)
  - `mặt trận phía Đông` (`p000492`) / `mặt trận phía Tây` (`p000493`)
  - `Trung tá` (`p000467`, `p000476`, `p000497`)
  - `Thiếu tá Weiss` (`p000500`)
  - `Tiểu đoàn Pháp sư Trên không số 203` (`p000502`)
  - `Dacia` / `Norden` / `mặt trận Rhine` (`p000503`)
  - `Liên bang` (`p000504`)
  - `thuật thức phát nổ` (`p000504`)
  - `Đế quốc` (`p000505`).
- Các cụm từ/thuật ngữ quân sự khác trong lô đã đồng bộ theo `locked_choices`:
  - `đơn vị thiết giáp` / `lực lượng dự bị của địch` / `đại đội dự bị` (`p000475`)
  - `nguyên lý thị trường` (`p000479`)
  - `pháo phòng không` (`p000505`).

## 5. Kiểm tra định dạng và công cụ xác thực
- Tệp `translations/vol-05/ch-01-b14.jsonl` gồm đúng 39 dòng JSONL hợp lệ, đầy đủ các trường bắt buộc (`segment_id`, `translation`, `status: "reviewed"`, `translator: "argon-low"`, `glossary_version`, `source_sha256`, `notes: []`).
- Chạy `python3 tools/validate_translation.py --handoff handoffs/vol-05/ch-01-b14.yml --source work/vol-05/batches/ch-01-b14-source.jsonl --translation translations/vol-05/ch-01-b14.jsonl` đạt kết quả `PASS`.
