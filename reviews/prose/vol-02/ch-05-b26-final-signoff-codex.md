# Final signoff — vol-02-ch-05-b26-final-signoff

## Kết quả

Đã đối chiếu bản dịch và self-check hiện tại với đúng package b26, báo cáo review và handoff sửa. **Còn mở: 0 serious, 0 moderate, 1 minor.** M01–M04 và L01–L04, L06 đã được xử lý; L05 mới xử lý một phần. Không xác nhận tuyên bố cả mười finding đã đóng trong handoff/self-check. Bốn khuyến nghị thuật ngữ vẫn là đề xuất pending/non-canon, không tính thành finding bổ sung.

Đếm theo finding độc lập, không theo số đoạn hoặc số chỗ sửa. Review này hoàn tất; không xác nhận batch đã commit hay đạt toàn bộ điều kiện hoàn tất pipeline.

## Đầu vào và phạm vi

- Đã đọc `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml` và `handoffs/vol-02/ch-05-b26-final-signoff.yml`.
- Đã đọc `work/vol-02/batches/ch-05-b26-source.jsonl`, `translations/vol-02/ch-05-b26.jsonl`, `reviews/semantic/vol-02/ch-05-b26-self-check.md`, `reviews/prose/vol-02/ch-05-b26-codex.md`, `handoffs/vol-02/ch-05-b26-review-fixes.yml` và các mục ledger `chapter5_b26_translation_proposals`, `chapter5_b26_reviewer_recommendations`, `chapter5_b26_coordinator_choices`.
- SHA-256 package thực tế: `c29cd1ba4c44371ee2a0103097f9e2ecd6697fc4b3e4761b16516b0e7ffc0110`; khớp cả hai handoff.
- Package và bản dịch đều có 37 đoạn, ID và thứ tự khớp, từ `YS-LN02/Text/part0028.xhtml/p000040` đến `YS-LN02/Text/part0028.xhtml/p000076`.
- Không mở EPUB/PDF hay package khác; không tra cứu ngoài, không tạo graph hoặc dữ liệu phụ. Chỉ ghi báo cáo này. Không chép câu nguồn.
- Validator: `not_run`; diff_check: `not_run`; commit: `null`.

## Kiểm chứng từng finding

Tiền tố ID trong bảng: `YS-LN02/Text/part0028.xhtml/`.

| Finding | Mức | Đoạn | Kết quả trong tệp hiện tại |
| --- | --- | --- | --- |
| M01 | moderate | p000048, p000055, p000056, p000058 | Đã xử lý. Các tự quy chiếu nội tâm dùng “mình”, thống nhất với điểm nhìn Tanya sau chuyển cảnh. Ngôi thứ nhất trước chuyển cảnh và trong thoại được giữ. Self-check mô tả đúng. |
| M02 | moderate | p000050, p000051, p000061, p000072 | Đã xử lý. Đúng bốn phạm vi nhấn mạnh tương ứng XHTML package: nội tâm ở p000050, câu dự báo ở p000051, cụm “không hài lòng” ở p000061, riêng “và” ở p000072. Lời dẫn và trần thuật ngoài phạm vi không bị nhấn thêm. |
| M03 | moderate | p000049 | Đã xử lý. Quy tắc hành chính được diễn đạt thành theo tiền lệ và tránh gây xáo trộn; giữ so sánh với hiện tượng tự nhiên, không thêm động cơ. |
| M04 | moderate | p000072 | Đã xử lý. Hai nhánh hoặc/or rõ ràng; nhánh sau cộng hai tính chất và chỉ nhấn liên từ. Không đếm lại dấu nhấn thành finding riêng. |
| L01 | minor | p000043 | Đã xử lý. “Đã xem tôi cứng cáp hơn…” đọc được tự nhiên trong ngữ cảnh; vẫn giữ chim non và mức tiến bộ một chút. |
| L02 | minor | p000051 | Đã xử lý. “Chuẩn bị tinh thần” diễn đạt sẵn sàng đương đầu rắc rối; giữ thuật ngữ mức hai tạm thời. |
| L03 | minor | p000056 | Đã xử lý. “Tác động… có lẽ…” bỏ sắc thái thúc đẩy của cách gọi cũ, giữ bất định, việc về hậu phương và hệ quả ngộ độc giả định. Câu còn dài nhưng không đủ căn cứ giữ finding văn phong này mở. |
| L04 | minor | p000067, p000071 | Đã xử lý. “Bản tin mã hóa ngắn” được dùng nhất quán; p000067 dùng “ống đựng thông điệp”. Không thêm kỹ thuật mã hóa hay dạng vật lý. |
| L05 | minor | p000070 | Còn mở một phần. Đã làm rõ không ai được đọc trước chỉ huy, nhưng vẫn dùng “điện báo viên”; chưa xử lý phân biệt chức năng vô tuyến mà review gốc nêu. |
| L06 | minor | p000075 | Đã xử lý. Cảm thán giữ sự ngao ngán, không thêm thời lượng ngày. |

## Finding còn mở

**L05 — minor — `YS-LN02/Text/part0028.xhtml/p000070`.** Package nhận diện người vận hành vô tuyến; bản dịch hiện tại vẫn gọi “điện báo viên”. Ngữ cảnh điện tín ở đoạn trước không đủ để đồng nhất hai chức năng. Phần quan hệ đọc trước đã được sửa, nên không nâng mức nghiêm trọng và không tạo finding mới.

Đề nghị dùng chức danh tạm “nhân viên vô tuyến” hoặc “vô tuyến viên”, giữ nguyên quy tắc chỉ huy đọc trước người khác ngoại trừ người vận hành. Không suy thêm quân hàm hay quy trình giải mã. Độ chắc chắn cao về chức năng được package nêu; cách gọi tiếng Việt vẫn có thể chọn tạm.

Self-check tuyên bố L05 đã sửa nhưng chính mô tả vẫn giữ “điện báo viên”; handoff cũng liệt kê L05 trong `findings_resolved`. Hai xác nhận đó chưa đủ để đóng toàn bộ L05. Người giữ quyền sửa cần sửa bản dịch và cập nhật self-check tương ứng; reviewer không sửa các tệp này. Sai lệch báo cáo được gắn với L05, không đếm thành lỗi thứ hai.

## Bốn khuyến nghị thuật ngữ

| Mã | Thuật ngữ nhận diện | Đề xuất tiếp tục dùng | ID đầy đủ | Phương án khác / giới hạn |
| --- | --- | --- | --- | --- |
| T01 | Commonwealth | Khối Thịnh vượng chung | YS-LN02/Text/part0028.xhtml/p000056 | Liên bang Thịnh vượng chung; giữ lựa chọn hiện tại để tránh khẳng định cấu trúc liên bang. Cấu trúc chính trị chưa rõ. |
| T02 | magical interference formulas | thuật thức gây nhiễu | YS-LN02/Text/part0028.xhtml/p000047 | công thức gây nhiễu ma thuật; chức năng được hỗ trợ tại chỗ, cơ chế/đối tượng gây nhiễu chưa rõ. |
| T03 | short cipher | bản tin mã hóa ngắn | YS-LN02/Text/part0028.xhtml/p000067; YS-LN02/Text/part0028.xhtml/p000071 | bản mật mã ngắn; “bản tin” là suy luận chức năng có căn cứ tại chỗ, chưa xác định vật mang tin hay kỹ thuật. |
| T04 | combat readiness level two | trạng thái sẵn sàng chiến đấu cấp độ hai | YS-LN02/Text/part0028.xhtml/p000051 | mức sẵn sàng chiến đấu hai; không ánh xạ cấp hai sang hệ thống quân sự ngoài đời. |

Cả ba nhóm b26 trong ledger đều có trạng thái nhóm `provisional_non_canon`; từng entry/choice đều `pending`. Reviewer recommendations và coordinator choices thống nhất cả bốn phương án với bản dịch và mục pending trong self-check. Đề xuất dịch ban đầu của T03 vẫn lưu cách gọi cũ; đây là lịch sử đề xuất, không thay thế coordinator choice hiện tại và không phải dấu hiệu nâng canon. Xác nhận provisional/non-canon dựa trên các tệp được giao, không suy rộng thành kiểm toán toàn bộ canon.

## Rủi ro và bước tiếp theo

Không còn finding serious hoặc moderate có căn cứ trong phạm vi kiểm tra này. Còn một minor L05 và sai lệch xác nhận đã đóng đi kèm. Ngữ cảnh không đủ để chốt cấu trúc Commonwealth, cơ chế gây nhiễu/mã hóa hoặc định nghĩa cấp sẵn sàng hai; tiếp tục dùng đề xuất tạm, không tự nâng canon. Tên Serebryakov được self-check nhắc từ b25 không xuất hiện trong package b26 và không được kiểm chứng bằng nguồn ngoài phạm vi.

Coordinator có thể giao sửa phần còn lại của L05 rồi xác nhận đóng; validator, diff-check và commit vẫn thuộc bước pipeline khác. Handoff sửa ghi các kiểm tra trước đó là pass, nhưng reviewer không chạy lại và không dùng chúng thay cho kết quả đối chiếu hiện tại.
