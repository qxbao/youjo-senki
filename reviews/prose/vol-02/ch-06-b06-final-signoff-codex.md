# Final signoff — vol-02-ch-06-b06

- Task: `vol-02-ch-06-b06-final-signoff`; vai trò reviewer.
- Đã đọc `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff final-signoff, handoff review-fixes, review b06, self-check và bản dịch hiện tại. Đã đối chiếu đủ 26 ID từ `YS-LN02/Text/part0030.xhtml/p000168` đến `p000193` với đúng package b06 được giao; không mở EPUB/PDF hoặc package khác.
- Package: `work/vol-02/batches/ch-06-b06-source.jsonl`; SHA-256 thực tế `1afb88d6570143a47f3950b1138107fe431183d677eceaecab40da5279606ede`, khớp cả hai handoff.
- Kết luận: F01–F09 đã được xử lý trong bản dịch hiện tại. Không phát hiện lỗi dịch nghiêm trọng/vừa/nhẹ còn mở trong phạm vi lô này. Chấp thuận signoff về nghĩa/văn phong/nhấn mạnh; không nâng thuật ngữ thành canon.

## Đối chiếu từng finding

Các mã đoạn dưới đây có tiền tố `YS-LN02/Text/part0030.xhtml/`.

| Finding | Mức ban đầu | ID | Kết quả kiểm tra bản hiện tại |
|---|---|---|---|
| F01 | minor | p000174 | Resolved: lệnh sẵn sàng chờ lệnh và cơ động ngay khi có lệnh được diễn đạt rõ; không thêm người ra lệnh. |
| F02 | moderate | p000176 | Resolved: chỉ xác nhận dấu hiệu về cuộc tiến công; không thêm quy mô tổng tấn công hoặc xác nhận tiến công đã xảy ra. |
| F03 | minor | p000178 | Resolved: tăng viện hội quân với du kích; không còn hàm ý gia nhập một phe. |
| F04 | moderate | p000179 | Resolved: đưa quân xuống bằng đường không, không phải tiếp tế vật tư; dùng lựa chọn tạm “chiến dịch đột kích đường không”, không suy thêm dù; giữ mức bất định của việc hội quân. |
| F05 | minor | p000180 | Resolved: giữ dạng ngắn Control; không đồng nhất với Bộ chỉ huy hoặc tự thêm tên/cấp cơ quan. |
| F06 | moderate | p000181 | Resolved: giữ giả định phản thực không có pháp sư và khả thể quá khứ của cảnh sát/bộ binh; không biến thành kết quả đã xảy ra. |
| F07 | minor | p000182 | Resolved: nhận định gián tiếp bằng “người ta cho rằng”; không thêm sắc thái tin đồn hay xác quyết của người kể. |
| F08 | moderate | p000184 | Resolved: khả năng đã đủ sức trấn áp trong quá khứ, kể cả phải đổ máu; không báo cáo một cuộc trấn áp đã hoàn tất. |
| F09 | moderate | p000190 | Resolved: có đúng hai phạm vi Markdown `*Chỉ vì lý do ấy thôi*` và `*chính vì thế?*`, tương ứng hai phạm vi XHTML trong package; “chăng?” và “Hay” ở ngoài, dấu hỏi thứ hai ở trong. Self-check phần xử lý F09 khớp bản dịch. |

Các ID còn lại đã được rà lại; không phát hiện lỗi mới cần sửa. Số lỗi dịch còn mở: serious 0, moderate 0, minor 0; `unresolved_findings: []`.

## Thuật ngữ và giới hạn

- `Feldgendarmerie`, p000171: tiếp tục đề xuất giữ nguyên; alternative “hiến binh dã chiến”. Bản dịch và self-check đều giữ lựa chọn này ở trạng thái tạm. Mục `chapter6_b06_coordinator_choices` trong `work/run-state/pending-terms.yml` có `status: provisional_non_canon`, riêng lựa chọn có `status: pending`; không có mục tương ứng trong glossary/decisions canon được tra cứu. Package chỉ hỗ trợ chức năng quân cảnh, chưa xác lập cơ cấu hoặc cách Việt hóa chính thức. Độ bất định thấp về việc giữ định danh, vừa về phương án Việt hóa.
- `Control`, p000180: tiếp tục giữ nguyên dạng ngắn; alternative “bộ phận kiểm soát”; pending/non-canon, chưa đủ căn cứ khai triển tên đầy đủ hoặc cấp cơ quan.
- Hoạt động đường không, p000179: tiếp tục “đưa quân xuống bằng đường không / chiến dịch đột kích đường không”; alternative “đổ quân đường không / chiến dịch đổ bộ đường không”; pending/non-canon. Không xác định cơ chế dùng dù.
- Self-check còn ghi chú cũ “tiếp tế đường không”, “đổ bộ đường không” và lặp mục pending/rủi ro. Đây là ghi chú tồn dư; phần xử lý F04 và bản dịch hiện tại đã dùng cách diễn đạt sửa đúng. Không dùng các ghi chú cũ làm căn cứ mô tả bản dịch hoặc mở lại F04. Ghi nhận giới hạn tài liệu, không phải lỗi dịch còn mở.

## Trạng thái bàn giao

- Chỉ viết báo cáo này; không sửa translation, self-check, handoff, canon hoặc ledger.
- Validator và diff_check của reviewer: `not_run`; handoff review-fixes báo `pass` cho cả hai, không thay thế bằng kết quả kiểm tra mới.
- Không commit; `commit: null`. Coordinator tiếp nhận signoff và giữ các lựa chọn thuật ngữ ở trạng thái pending/non-canon.
