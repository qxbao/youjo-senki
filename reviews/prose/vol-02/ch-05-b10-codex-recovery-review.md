# Codex recovery review — vol-02-ch-05-b10

## Phạm vi, chứng cứ và kết luận

Rà soát hồi cứu giới hạn ở 26 đoạn `YS-LN02/Text/part0026.xhtml/p000227`–`YS-LN02/Text/part0026.xhtml/p000252`. Đã đọc agents/shared.md, agents/reviewer.md, config/translation-pipeline.yml, handoff b10, prepared package b10, bản dịch b10, self-check b10 và hai báo cáo Claude b10 được giao. SHA-256 package thực tế khớp giá trị mong đợi `c7a3a6292282d3a23258cfced6053fe94d7de1ce4eb0730d03d07b760c517e82`. Hai JSONL có đủ 26 dòng, mã đoạn tương ứng đúng thứ tự; đây là quan sát đầu vào, không phải chạy validator.

Đối chiếu trực tiếp văn bản và markup nguồn trong package, không dựa riêng vào disposition của translator. Không mở EPUB/PDF, batch khác, canon hoặc run-state. Canon chỉ được tham chiếu qua metadata/checkpoints và lựa chọn tạm trong handoff; không xác nhận độc lập nội dung các quyết định canon. Chỉ ghi báo cáo này; không sửa translation, handoff, self-check, canon hay run-state; không chạy validator/diff-check và không commit. Báo cáo không chép câu nguồn; các nhãn nguồn ngắn chỉ dùng nhận diện.

**Codex signoff: pass.** Counts hiện tại: **serious 0 / moderate 0 / minor 3**. F01–F06 cũ được đóng sau đối chiếu nguồn độc lập. Ba khuyến nghị nhẹ R01–R03 bên dưới không chặn signoff; `unresolved_findings: []` ghi nhận không còn finding bắt buộc xử lý để đạt signoff theo điều kiện serious/moderate của nhiệm vụ. Không coi các điểm nhẹ là đã được translator sửa. Signoff này không thay thế validator, diff-check hoặc commit của pipeline.

## Findings nhẹ và sửa đề xuất

### R01 — minor — YS-LN02/Text/part0026.xhtml/p000231

- **Chứng cứ:** Nhãn nguồn `red slips` chứa chi tiết màu; bản dịch chỉ ghi “giấy gọi nhập ngũ”. Self-check đã thừa nhận lược màu, và signoff Claude để chi tiết này trong giới hạn pending.
- **Đánh giá:** Chức năng giấy gọi và logic chi phí huấn luyện/trang bị/nuôi quân được giữ; màu sắc bị lược là mất chi tiết nhỏ có căn cứ trực tiếp, không phải lỗi nghiêm trọng về cơ chế nhập ngũ.
- **Sửa đề xuất:** “giấy gọi nhập ngũ màu đỏ”. Đây là đề xuất provisional/non-canon; không suy diễn loại biểu mẫu hoặc giá trị hành chính đặc biệt. Phương án khác: “giấy triệu tập nhập ngũ màu đỏ”.
- **Disposition:** Khuyến nghị không chặn signoff; chưa sửa trong review này.

### R02 — minor — YS-LN02/Text/part0026.xhtml/p000243

- **Chứng cứ:** Nguồn dùng mức so sánh cao nhất cho hiệu quả chi phí quản lý; bản hiện tại là “điều hành tiểu đoàn sao cho hiệu quả về chi phí”, giữ tiêu chí nhưng mất mức tối đa. Self-check F06 xác nhận đúng đối tượng quản lý, chưa ghi nhận sắc thái này.
- **Đánh giá:** F06 về cú pháp và đối tượng đã xử lý. Phần còn thiếu là cường độ mục tiêu trong giọng tính toán của Tanya, không làm đổi kết luận về thương vong hay tân binh.
- **Sửa đề xuất:** “Tanya định điều hành tiểu đoàn sao cho đạt hiệu quả cao nhất về chi phí ở mặt trận Rhine điên loạn này”. Giữ đây là ý định, không biến thành kết quả đã đạt hoặc mục tiêu giảm thương vong.
- **Disposition:** Khuyến nghị không chặn signoff; chưa sửa trong review này.

### R03 — minor — YS-LN02/Text/part0026.xhtml/p000251

- **Chứng cứ:** Nguồn mô tả người bạn học hiện thuộc/được biệt phái về Bộ chỉ huy với vai trò quan sát viên, rồi nêu cô ấy ở khu vực khác. “Đang được điều đến Bộ chỉ huy” trong bản dịch có thể khiến độc giả hiểu việc điều chuyển đang diễn ra, thay vì trạng thái công tác hiện hữu.
- **Đánh giá:** Vai trò quan sát viên, địa bàn Rhine, khu vực khác, giới nữ và thư riêng đều giữ đúng. Đây là nguy cơ lệch sắc thái thời gian cục bộ, không có căn cứ kết luận toàn mạch tin đồn bị đổi.
- **Sửa đề xuất:** “một bạn cùng khóa ở Trường Sĩ quan hiện làm quan sát viên ở Rhine, thuộc Bộ chỉ huy”. Phương án khác: “hiện được biệt phái về Bộ chỉ huy làm quan sát viên ở Rhine”; nhãn “biệt phái” chỉ là đề xuất, không chốt cơ chế tổ chức từ package này.
- **Disposition:** Khuyến nghị không chặn signoff; chưa sửa trong review này.

## Đánh giá lại F01–F06 và translator follow-up

| Finding cũ | Segment ID | Đối chiếu độc lập và disposition |
| --- | --- | --- |
| F01, moderate | YS-LN02/Text/part0026.xhtml/p000241 | Closed, addressed. Nguồn đặt Tanya trong dòng suy nghĩ rồi Serebryakov mang thông báo hành chính đến ngắt ngang; bản hiện tại dùng “cắt ngang dòng suy nghĩ ấy”, không còn gợi đang nói thành tiếng. |
| F02, moderate | YS-LN02/Text/part0026.xhtml/p000245 | Closed, source-preserving ambiguity; no confirmed defect. Nguồn kết luận loại trừ Bộ chỉ huy bằng đại từ nhưng để tỉnh lược vai trò/hành động bị loại trừ. Bản Việt giữ “họ” quy chiếu Bộ chỉ huy và không tự thêm hành động. Có thể suy đoán lỗi điều động từ ngữ cảnh, nhưng nguồn không viết tường minh; không bắt translator chọn một diễn giải. Độ chắc chắn được giữ. |
| F03, minor | YS-LN02/Text/part0026.xhtml/p000228 | Closed, addressed. Giữ làm việc vất vả hơn khi quay lại; nguồn không định lượng mức tăng tương ứng với thời gian nghỉ. Bỏ “bấy nhiêu” có căn cứ. |
| F04, minor | YS-LN02/Text/part0026.xhtml/p000235 | Closed, addressed. “Được hàng nghìn binh sĩ sử dụng” sửa cú pháp và giữ quan hệ người sử dụng; không thêm yêu cầu số người vận hành. |
| F05, minor | YS-LN02/Text/part0026.xhtml/p000240 | Closed, addressed. Nguồn liên kết việc có tiền, bắn đạn hào phóng và giá mỗi quả; “ném tiền vào việc bắn đạn pháo … như nước lã” giữ ý chi tiêu và lượng bắn qua cách diễn đạt tự nhiên. Toàn đoạn vẫn nhấn mạnh đúng markup. |
| F06, minor | YS-LN02/Text/part0026.xhtml/p000243 | Closed, addressed về cú pháp/đối tượng. Tiểu đoàn là đối tượng quản lý có căn cứ ngữ cảnh. R02 là khuyến nghị riêng về mức so sánh cao nhất, không mở lại lỗi cú pháp đã sửa. |

## Sổ đối chiếu đủ 26 đoạn và các checkpoint

Các mã rút gọn trong bảng có tiền tố cố định `YS-LN02/Text/part0026.xhtml/`. “Đạt” nghĩa không thấy finding serious/moderate hoặc vấn đề nhẹ riêng cần báo thêm từ nguồn được giao; không phê duyệt canon.

| Đoạn | Chứng cứ/điểm kiểm và kết quả |
| --- | --- |
| p000227 | Đạt: chiến hào, mưa/đạn pháo, bắn tỉa và hỏa lực quấy nhiễu; khả năng nghỉ do pháp sư khan hiếm vẫn là phỏng đoán. Nguồn không có địa điểm hậu phương ở đoạn này. |
| p000228 | Đạt: nghỉ nhanh/tắm rửa tại hậu phương và làm việc vất vả hơn khi trở lại; F03 đóng. |
| p000229 | Đạt: ngày nắng/tầm nhìn tốt, máu đòi máu, một sư đoàn/một nghìn tấn mỗi ngày, khẩu quyết chỉ đúng một nửa và không tiến được. Markup nhấn mạnh đúng khẩu quyết; không thêm nhấn mạnh cho phần còn lại. |
| p000230 | Đạt: khí tài/người bị coi rẻ, sự lãng phí và chăm lo nhân lực. Chuyển Tanya/cô sang tôi có trong nguồn, không phải nhầm ngôi dịch. |
| p000231 | R01: chức năng giấy gọi và ẩn dụ mua số lượng lớn/họp cổ đông giữ đúng, lược chi tiết màu đỏ. |
| p000232 | Đạt: bắn phá phung phí, muốn chất vấn về lại quả, Grupper giữ đúng dạng package; không xác định thêm danh tính. |
| p000233 | Đạt: không phủ nhận màn hỏa lực và hiểu độc lập với quan điểm cấp trên. “Đáng kính” giữ khả năng mỉa mai, không bắt buộc thêm giọng mỉa. “Yểm trợ” vẫn là lựa chọn tạm; phương án ít diễn giải hơn là “màn hỏa lực”. |
| p000234 | Đạt: đã khuyên giảm chi phí; hậu phương rối và bảy/tám tiêu chuẩn riêng cho pháo đường sắt, không đồng nhất tiêu chuẩn với chủng loại. |
| p000235 | Đạt: 20 cm/80 cm, hàng nghìn người sử dụng, nhiều loại pháo và nghi ngờ kỹ sư làm theo ý thích; nghi ngờ chưa thành sự thật. F04 đóng. |
| p000236 | Đạt: câu hỏi đòi ít nhất chút quan tâm đến sản xuất hàng loạt. |
| p000237 | Đạt: từ cảnh tiêu hao suy ra tổ hợp công nghiệp quân sự chuộng chiến tranh; không thêm tổ chức cụ thể. |
| p000238 | Đạt: Nhật Bản/Thế chiến thứ nhất, phép liên hệ với mua sắm đặc biệt/Chiến tranh Triều Tiên. Không bổ sung giải thích lịch sử ngoài package. |
| p000239 | Đạt: tốc độ tiêu thụ, doanh số tất tăng, cung/cầu và gần như muốn mở công ty quân sự tư nhân; giữ mức chưa thành quyết định. |
| p000240 | Đạt: điều kiện bị phí phạm, đề nghị tăng lương/phúc lợi, tiền và đạn hướng về Cộng hòa, mong hơn kẹo bánh. Toàn đoạn nhấn mạnh có căn cứ nguồn; F05 đóng. |
| p000241 | Đạt: trần thuật/ngắt dòng suy nghĩ bằng thông báo hành chính; F01 đóng. Cấp bậc tiếng Việt giữ tạm theo handoff. |
| p000242 | Đạt: pháp sư mới đã đến bộ chỉ huy cụm; lời đề nghị Tanya ghé qua xem họ. Cách gọi chức danh/bà không xác lập tuổi hay quan hệ. |
| p000243 | R02: giả định bổ sung quân số, chưa mất ai/không thương vong, hai khả năng điều nhầm/gửi nhầm vẫn đúng; cần phục hồi mức hiệu quả cao nhất. F06 về cú pháp đã đóng. |
| p000244 | Đạt: sự dè dặt, ngập ngừng, đã tự kiểm tra và phủ định nhầm lẫn. “Thưa bà” là lựa chọn xưng hô tạm. |
| p000245 | Đạt: không yêu cầu bổ sung, Serebryakov xác nhận không nghe nhầm/hiểu nhầm, phụ tá hiểu không cần người thay thế khi không thương vong. F02 đóng do phép tỉnh lược có trong nguồn. |
| p000246 | Đạt: tiểu đoàn vốn tăng cường, gần tối đa dưới quyền thiếu tá, khó hình dung thăng chức/nhận thêm quân đột ngột trong tình cảnh này; không chuyển giả định thành sự kiện. |
| p000247 | Đạt: kết luận duy nhất là sắp gặp rắc rối; ngôi chúng tôi và thời gian sắp tới được giữ. |
| p000248 | Đạt: tự nhận tốt bụng/tiết kiệm/tuân thủ, giả định Số phận tồn tại, đại từ nữ và lời miệt thị có căn cứ. Quan hệ với Being X vẫn là suy đoán qua “có lẽ”. |
| p000249 | Đạt: chưa chắc/chỉ tin đồn/có thể muốn; vai trò đơn vị huấn luyện không thành mệnh lệnh xác nhận. |
| p000250 | Đạt: phản ứng ngạc nhiên và hỏi nguồn nghe tin; không đổi chủ thể người nghe. |
| p000251 | R03: nữ bạn học, quan sát viên Rhine/khu vực khác và thư cá nhân giữ đúng; cách diễn đạt trạng thái điều động nên rõ hơn. Cadet Corps/Trường Sĩ quan tiếp tục tạm. |
| p000252 | Đạt: tin đồn hợp lý/có vẻ đáng tin qua quan hệ cá nhân tình cờ và Tanya hỏi làm rõ, không biến tin đồn thành sự thật. |

U01–U07 của review đầu nay đã được kiểm bằng package: U01 đúng phạm vi hậu phương ở p000228/p000234; U02 khớp hai vị trí nhấn mạnh; U03 còn R01 nhưng Grupper và quan hệ độc lập với cấp trên có căn cứ; U04 xác nhận số liệu/quan hệ sử dụng, không thêm lore kinh tế; U05 xác nhận các nhãn cấp bậc nguồn và bạn học nữ, mapping tiếng Việt vẫn tạm; U06 giữ phủ định, giả định và tin đồn, còn khuyến nghị nhẹ R03 về trạng thái công tác; U07 xác nhận nhân cách hóa nữ và suy đoán về Being X. Không tiếp tục gọi những điểm đã đọc trực tiếp này là bất khả kiểm chứng nguồn; phần chưa chốt là thuật ngữ/canon ngoài phạm vi được giao.

## Term recommendations — provisional/non-canon

Tất cả là đề xuất, không sửa ledger/canon và không tự nâng thành canon. Chỉ R01 đề xuất bổ sung chi tiết trực tiếp; các lựa chọn còn lại giữ theo handoff hoặc nêu phương án ít suy diễn hơn.

| Nhãn nguồn | Segment IDs (cùng tiền tố trên) | Đề xuất tạm | Căn cứ và phương án khác |
| --- | --- | --- | --- |
| red slips | p000231 | giấy gọi nhập ngũ màu đỏ | Giữ chức năng và màu nguồn; khác: giấy triệu tập nhập ngũ màu đỏ. |
| curtain of fire | p000233 | màn hỏa lực yểm trợ | Giữ handoff theo mạch pháo binh; “màn hỏa lực” ít xác định chức năng hơn. |
| railway guns | p000234, p000235 | pháo đường sắt | Giữ nhất quán; khác: pháo đặt trên đường sắt; không thêm cơ chế vận hành. |
| military-industrial complex | p000237 | tổ hợp công nghiệp quân sự | Giữ nghĩa tập hợp; khác: tổ hợp quân sự–công nghiệp. |
| instructor unit | p000249 | đơn vị huấn luyện | Giữ chức năng và mức tin đồn; khác: đơn vị phụ trách huấn luyện. |
| Cadet Corps | p000251 | Trường Sĩ quan | Giữ handoff tạm, không xác định tên chính thức/loại cơ sở; khác: cơ sở đào tạo sĩ quan. |
| Grupper | p000232 | Grupper | Đúng dạng package; giữ nguyên, chờ xác minh định danh, không thay bằng tên suy đoán. |
| Lieutenant Serebryakov | p000241, p000245 | Trung úy Serebryakov | Nhãn nguồn có căn cứ, mapping tiếng Việt chưa canon; khác: Sĩ quan cấp úy Serebryakov. |
| ma’am / lời gọi cấp trên | p000242, p000244 | bà/thưa bà | Giữ giọng hiện tại, không suy ra tuổi; khác: Thiếu tá/thưa Thiếu tá. p000242 dùng bà để dịch đại từ người nghe, nhãn ma’am xuất hiện ở p000244. |

## Trạng thái

```yaml
role: reviewer
task_id: vol-02-ch-05-b10
state: done
review_path: reviews/prose/vol-02/ch-05-b10-codex-recovery-review.md
counts: {serious: 0, moderate: 0, minor: 3}
findings:
  - {id: R01, severity: minor, segment_id: YS-LN02/Text/part0026.xhtml/p000231, issue: omitted_red_color, disposition: nonblocking_recommendation}
  - {id: R02, severity: minor, segment_id: YS-LN02/Text/part0026.xhtml/p000243, issue: omitted_cost_efficiency_superlative, disposition: nonblocking_recommendation}
  - {id: R03, severity: minor, segment_id: YS-LN02/Text/part0026.xhtml/p000251, issue: current_posting_temporally_ambiguous, disposition: nonblocking_recommendation}
closed_previous_findings: [F01, F02, F03, F04, F05, F06]
signoff_status: pass
signoff_by: Codex
unresolved_findings: []
term_recommendations:
  status: provisional_non_canon
  details: See term table; retain handoff choices except recommend restoring red color at p000231.
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_records_codex_signoff_and_nonblocking_minor_recommendations
```
