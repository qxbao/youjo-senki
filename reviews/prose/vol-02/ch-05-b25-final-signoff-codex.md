# Final signoff — vol-02-ch-05-b25-final-signoff

Đã đối chiếu bản dịch hiện tại với đúng package cục bộ được giao, đủ 39 mã đoạn từ `YS-LN02/Text/part0028.xhtml/p000001` đến `YS-LN02/Text/part0028.xhtml/p000039`. Đã đọc shared/reviewer, config, handoff final-signoff, self-check, báo cáo review, handoff sửa và các mục b25 trong pending ledger. Không mở EPUB/PDF hoặc package khác. Không chép câu nguồn vào báo cáo.

SHA-256 package xác minh tại chỗ: `b019ace402b28641702238268c6f0b7ff142cac508aca8efb0c070d43f91fdcc`; khớp handoff final-signoff và handoff sửa.

Kết quả: **M01, M02, m01–m05 đều đã xử lý**. Số lỗi còn mở chính xác: **serious: 0; moderate: 0; minor: 0**. Không phát hiện lỗi mới cần hành động trong phạm vi b25.

| Mã | Mức ban đầu | Stable segment ID | Xác minh bản hiện tại |
|---|---|---|---|
| M01 | moderate | YS-LN02/Text/part0028.xhtml/p000030 | Điều kiện giả định ở học viện đã rõ qua “Nếu ở học viện”; giữ đối chiếu với tiền tuyến và phạm vi chữ nghiêng của lời quở trách. |
| M02 | moderate | YS-LN02/Text/part0028.xhtml/p000036 | Lời gọi đã dùng “thưa Trung úy”, nhất quán với Serebryakov tại p000033/p000037; không nhập với cấp bậc Grantz tại p000012. |
| m01 | minor | YS-LN02/Text/part0028.xhtml/p000004 | Việc tuân lệnh là chủ thể thành thói quen; cấu trúc tự nhiên và giữ quan hệ với rèn luyện lặp lại. |
| m02 | minor | YS-LN02/Text/part0028.xhtml/p000025 | “Cứ như người mất hồn” giữ trạng thái nhận biết mơ hồ, phù hợp ký ức ở p000026, không thêm chẩn đoán. |
| m03 | minor | YS-LN02/Text/part0028.xhtml/p000032 | “Cũng tạm ổn” khôi phục mức độ tương đối trong lời trấn an mang giọng đùa. |
| m04 | minor | YS-LN02/Text/part0028.xhtml/p000038 | “Những người lính dày dạn” giữ ý từng trải của nhóm sĩ quan, không thêm hàm ý giải ngũ; giữ cường độ làm việc và mốc hôm nọ. |
| m05 | minor | YS-LN02/Text/part0028.xhtml/p000039 | Giữ cảm giác có thể thở phào, cùng sự bình tâm chỉ mới trở lại đôi chút. |

Qua đối chiếu cả lô, điểm nhìn ngôi thứ nhất vẫn rõ; “anh ấy” tại p000019 chỉ Weiss. Chữ nghiêng tại p000002, p000007, p000015 và p000030 giữ đúng phần tương ứng trong package. Self-check và handoff sửa phù hợp với các sửa hiện có.

Các lựa chọn sau tiếp tục là **pending, provisional/non-canon**:

| Mục | Lựa chọn tạm được xác nhận | Lựa chọn thay thế | ID trọng tâm và căn cứ |
|---|---|---|---|
| Grantz viewpoint pronouns | tôi trong lời kể ngôi thứ nhất và khi tự xưng với cấp trên; mình trong tự nhủ trực tiếp khi rõ chủ thể | tôi xuyên suốt; lược chủ ngữ khi rõ | p000001/p000007/p000015: đúng điểm nhìn và lựa chọn cục bộ của coordinator. “Tôi” trong hồi tưởng tự nhủ p000002 đã được review trước chấp nhận; không phải lỗi còn mở. |
| Lieutenant Serebryakov | Trung úy | Thiếu úy | p000033/p000036/p000037: nhất quán cục bộ theo mục `chapter5_b25_rank_recommendation`; chưa chốt ánh xạ quân hàm chung. |
| Magic Second Lieutenant | Thiếu úy Pháp sư | Thiếu úy ma pháp | p000012: giữ cả quân hàm và chuyên môn; cách gọi chuyên môn còn bất định. |
| old stagers | những người lính dày dạn | những người dày dạn kinh nghiệm | p000038: giữ kinh nghiệm quân nhân theo ngữ cảnh, không suy tình trạng giải ngũ. |

Các hậu tố pNNNNNN trong bảng lựa chọn đều thuộc `YS-LN02/Text/part0028.xhtml/`. Ledger lưu đề xuất translator cũ về “anh” và “cựu binh”, nhưng mục reviewer/coordinator b25 cùng self-check hiện tại đã xác định phương án áp dụng; không coi các đề xuất lịch sử ấy là canon hoặc chỉ dẫn thay thế lựa chọn hiện hành. Mọi mục b25 liên quan trong ledger vẫn mang trạng thái pending/provisional_non_canon.

Rủi ro còn lại: lựa chọn đại từ, tên chuyên môn và ánh xạ quân hàm chỉ có giá trị tạm trong phạm vi được giao; không dùng signoff này để nâng thành canon hoặc suy thay đổi cấp bậc ngoài b25. Signoff xác nhận xử lý review, không xác nhận hoàn tất toàn bộ pipeline. Handoff sửa ghi validator/diff-check pass của translator; reviewer không chạy lại và báo `validator: not_run`, `diff_check: not_run`, `commit: null`.

Chỉ ghi báo cáo này; không sửa bản dịch, self-check, handoff, ledger, canon hoặc checkpoint.
