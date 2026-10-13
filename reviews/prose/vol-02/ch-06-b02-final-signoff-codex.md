# Final signoff — vol-02-ch-06-b02-final-signoff

Đã đối chiếu bản dịch và self-check hiện tại với đúng gói B02, review report và fix handoff được giao; đã đọc agents/shared.md, agents/reviewer.md và config/translation-pipeline.yml. SHA-256 gói nguồn là `257ce85587df6c83d5c436d6bef806e1e8141f11a0e6f8e4489f0eda6e168a18`, khớp final-signoff handoff. Không mở EPUB/PDF hoặc gói nguồn khác; không chép câu nguồn.

Phạm vi gồm 32 mã đoạn liên tiếp từ `YS-LN02/Text/part0030.xhtml/p000036` đến `YS-LN02/Text/part0030.xhtml/p000067`. Bản dịch giữ đủ mã đoạn, đúng thứ tự. Kết quả final signoff: cả bảy finding đã giải quyết; số lỗi chưa xử lý chính xác là **serious: 0, moderate: 0, minor: 0**. Không phát hiện lỗi mới có căn cứ trong phạm vi kiểm tra.

## Xác minh các finding

| ID ổn định | Mức ban đầu | Segment ID | Kết quả đối chiếu hiện tại |
| --- | --- | --- | --- |
| B02-M01 | moderate | YS-LN02/Text/part0030.xhtml/p000040 | Resolved: toàn bộ lời cảnh cáo, gồm ngoặc kép, đã được in nghiêng, khớp phạm vi nhấn trong gói. |
| B02-M02 | moderate | YS-LN02/Text/part0030.xhtml/p000043 | Resolved: chủ thể được diễn đạt là phía Cộng hòa, phù hợp ngữ cảnh p000043–p000044; không thêm cơ quan/cá nhân. Khả năng do học giả nêu vẫn được giữ. |
| B02-M03 | moderate | YS-LN02/Text/part0030.xhtml/p000049; YS-LN02/Text/part0030.xhtml/p000050 | Resolved: lời phủ nhận và lập luận tiếp theo đều dùng phạm vi người bị giam giữ, không chỉ tù binh quân sự. Không thêm phán quyết pháp lý; p000038 vẫn giữ lập luận riêng về quyền của người tham chiến. |
| B02-M04 | moderate | YS-LN02/Text/part0030.xhtml/p000057 | Resolved: đã dùng tên tạm “Quân đội Khu vực phía Tây”, không gán cấp tập đoàn quân hoặc một cấp tổ chức khác. |
| B02-M05 | moderate | YS-LN02/Text/part0030.xhtml/p000060 | Resolved: mô tả hậu phương phía tây bị chia cắt khỏi tiền tuyến; giữ cách dẫn nhập xét tình thế. Không thu hẹp thành truyền tin, không khẳng định tuyến tiếp tế bị phá hủy. |
| B02-L01 | minor | YS-LN02/Text/part0030.xhtml/p000054 | Resolved: lời giới thiệu khách mời tự nhiên hơn, không thêm thời điểm; giữ tên, học hàm và câu hỏi. |
| B02-L02 | minor | YS-LN02/Text/part0030.xhtml/p000056 | Resolved: cụm diễn đạt gượng đã được sửa, giữ sắc thái khẩu ngữ, chữ nghiêng và dấu mở thoại tiếp diễn. |

Self-check phản ánh đúng các sửa đổi trên và thống nhất với fix handoff. Các đoạn liên quan p000048–p000050 và p000060–p000067 giữ quan hệ lập luận, điều kiện, mức dè dặt và quy thuộc phát ngôn. Chữ nghiêng ở p000048, phần lời đáp p000049 và p000055–p000067 tiếp tục đúng phạm vi; không cần tự đóng lời thoại kéo dài ở cuối batch. p000066 không tạo residual của B02-M05: cách gọi các tuyến liên lạc có căn cứ riêng tại đoạn đó, không thay thế mô tả chia cắt ở p000060.

## Năm lựa chọn tiếp tục pending/non-canon

Trạng thái dưới đây được xác nhận từ self-check hiện tại và chỉ dẫn coordinator trong fix handoff, không phải xác nhận trực tiếp ledger/canon ngoài phạm vi task. Cả năm đều dùng nhất quán trong bản dịch và chỉ là đề xuất tạm.

| Mã | Thuật ngữ | Đề xuất giữ tạm | Segment ID | Lý do, phương án khác và bất định |
| --- | --- | --- | --- | --- |
| T01 | irregular combatants | chiến binh phi chính quy | YS-LN02/Text/part0030.xhtml/p000038; YS-LN02/Text/part0030.xhtml/p000048; YS-LN02/Text/part0030.xhtml/p000050 | Phù hợp đối lập với quân phục/quân chính quy. “Người tham chiến phi chính quy” là phương án trung tính hơn; tên pháp lý chính thức chưa chốt. Status: pending, non-canon. |
| T02 | Rules of War on Land | Quy tắc Chiến tranh trên bộ | YS-LN02/Text/part0030.xhtml/p000040; YS-LN02/Text/part0030.xhtml/p000048; YS-LN02/Text/part0030.xhtml/p000050 | Giữ nhất quán tên và điều/khoản trong lô. Có thể viết hoa tiết chế hơn; tên chính thức và cách viết hoa chưa chốt, không đồng nhất với công ước ngoài đời. Status: pending, non-canon. |
| T03 | paradigm | mô thức tư duy | YS-LN02/Text/part0030.xhtml/p000055 | Giữ ý lối tư duy thiên về quân sự. “Mô hình tư duy” hoặc “khuôn khổ tư duy” có thể dễ đọc hơn; lựa chọn văn phong chưa chốt. Status: pending, non-canon. |
| T04 | Western District Army | Quân đội Khu vực phía Tây | YS-LN02/Text/part0030.xhtml/p000057 | Giữ vùng và lực lượng, tránh suy cấp tổ chức. “Lực lượng quân đội khu vực phía Tây” là phương án mô tả; độ bất định về cấp tổ chức vẫn cao. Status: pending, non-canon. |
| T05 | firestorm | bão lửa | YS-LN02/Text/part0030.xhtml/p000052 | Hợp mục tiêu thử nghiệm và lan lửa. “Cơn bão lửa” là biến thể lượng từ; không thêm cơ chế hoặc kết quả thực nghiệm. Status: pending, non-canon. |

## Giới hạn bàn giao

- Unresolved findings: không có; serious/moderate/minor = 0/0/0. Thông qua kiểm tra review fixes B02, không nâng bất kỳ thuật ngữ nào thành canon.
- Chủ thể tại p000043 là lựa chọn tạm có căn cứ ngữ cảnh; cấp tổ chức T04 và tên/viết hoa T02 vẫn chưa chốt. Đây là bất định đã ghi nhận, không phải lỗi tồn dư.
- Chỉ kiểm tra lời kể hư cấu trong gói được giao; không xác lập tính hợp pháp ngoài đời, suy lore hoặc đọc ledger/canon ngoài phạm vi.
- Fix handoff ghi validator và diff-check pass từ lượt sửa; reviewer không chạy lại hai kiểm tra này. Signoff này không xác nhận commit hoặc hoàn tất toàn bộ pipeline.
- Chỉ ghi báo cáo này. Validator: not_run. Diff-check: not_run. Commit: null.
