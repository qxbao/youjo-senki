# Pilot-01 — đánh giá mù Candidate A/B

- `task_id`: `pilot-01-blind-evaluation`.
- Ngày đánh giá: 2026-10-12.
- Phạm vi: tám đoạn liên tiếp, `YS-LN01/Text/chapter001.xhtml/p000008` đến `YS-LN01/Text/chapter001.xhtml/p000015`.
- Chỉ đọc chín tệp được chỉ định; không đọc bản dịch gốc, báo cáo thuật ngữ, lịch sử Git hoặc tên nhánh; không truy tìm danh tính ứng viên. Không sửa bản dịch hoặc canon.
- Nguồn đối chiếu: gói JSONL cục bộ được giao; không mở EPUB/PDF hoặc dùng dịch vụ ngoài để tra cứu.

## 1. Căn cứ và bảng điểm

Phiên bản được nhận diện bằng SHA-256 của chính các tệp được phép đọc:

| Tệp trong gói mù | SHA-256 |
| --- | --- |
| `source.jsonl` | `4094834d8395d7e23f7375646d2eeebf090791904b5cbd6cf38f2add8a9fa4cb` |
| `candidate-a.jsonl` | `b45f3c8a32dde00a818310d428147a8ee755491e6f98d9b91731948f013e7d12` |
| `candidate-b.jsonl` | `cda3a353ce6567962c445bad5e4ec5b70a93ded3375b5d38613b0c2180e34cef` |

SHA nguồn ghi trong cả tám bản ghi: `7698e1b80fc5d560020b8934f6243b3b7be1be9c911668455a069f857f3da528`. Đây là metadata của gói, không phải kết quả kiểm tra lại tệp nguồn gốc.

Chấm riêng từng ứng viên đối chiếu nguồn trước khi chọn theo đoạn. Các mã ngắn bên dưới đều có tiền tố `YS-LN01/Text/chapter001.xhtml/`. Năm dòng đầu đáp ứng các tiêu chí người giao việc yêu cầu; dòng cuối bổ sung tiêu chí bắt buộc về độ đầy đủ trong rubric và protocol. Độ sạch kỹ thuật không thay thế tiêu chí này.

| Tiêu chí | Candidate A | Căn cứ cho A | Candidate B | Căn cứ cho B |
| --- | ---: | --- | ---: | --- |
| Đúng nghĩa và logic | 4/5 | Giữ câu hỏi về tình trạng ở p000009, giả thuyết bệnh viện ở p000011 và điều kiện dè dặt ở p000012. p000009 có cách diễn đạt trạng thái tỉnh táo chưa rõ; p000013 hơi cứng nhưng giữ yêu cầu phát âm. | 3/5 | p000009 chuyển câu hỏi về tình trạng thành câu hỏi vị trí; p000013 đổi yêu cầu phát âm thành yêu cầu há miệng. Các suy luận ở p000010–p000012 vẫn đúng hướng. |
| Giọng kể / giọng nhân vật | 4/5 | p000010–p000011 giữ lối tự lý giải có khoảng cách; p000009 và p000014 dùng nội tâm “mình” ổn định. Một số kết hợp từ nặng làm nhịp kể kém linh hoạt. | 4/5 | p000010–p000014 giữ giọng quan sát và suy luận; p000013/p000015 có lời gọi mềm, hợp cảnh chăm trẻ. Nội tâm p000009 bị thu hẹp trọng tâm; chưa có đủ thoại để đánh giá giọng riêng lâu dài. |
| Văn xuôi tiếng Việt tự nhiên | 3/5 | p000008 có cấu trúc bị động vụng; p000009 dùng “giữ được tỉnh thức”; p000012 có “ánh sáng nghèo nàn”, “nguồn sáng thiếu thốn”, “lạc thời”. Đọc hiểu được nhưng cần biên tập lặp lại ở nhiều đoạn. | 4/5 | p000010, p000012 và p000014 rõ, nhịp câu thuận; p000013 tự nhiên trong cảnh chăm trẻ. p000008 còn cụm thời gian cứng; p000011 có kết hợp “thị lực mờ” chưa thuận. |
| Nhất quán đại từ, xưng hô và quy ước | 4/5 | “Nó” trong trần thuật, “mình” trong nội tâm; cách gọi Tanya thống nhất tại p000013/p000015. Các phương án tạm được ghi là đề xuất trong báo cáo này; chưa có căn cứ coi là canon đã duyệt. | 4/5 | Cùng hệ đại từ ở p000009/p000014; cách gọi Tanya nhất quán tại p000013/p000015. Tên và thuật ngữ không có biến thể tùy tiện trong tám đoạn; phương án vẫn cần duyệt. |
| Độ sạch kỹ thuật | 4/5 | Đủ tám mã p000008–p000015, đúng thứ tự, JSONL hợp lệ, trường dịch có nội dung, không có ghi chú làm việc. Gói văn bản phẳng chưa thể hiện chữ nghiêng của nguồn tại p000008/p000009/p000014. | 4/5 | Cùng kết quả về số lượng, mã đoạn, thứ tự, JSONL và trường dịch; cũng chưa thể hiện chữ nghiêng tại p000008/p000009/p000014. |
| Không bỏ sót hoặc thêm ý — tiêu chí bổ sung theo rubric | 4/5 | Không bỏ đơn vị nguồn; p000009 giữ đối tượng thân xác, p000013 giữ chi tiết phát âm. Những cách gọi ở p000013/p000015 là lựa chọn xưng hô cần duyệt, không chứng minh quan hệ thân thuộc. | 3/5 | Không bỏ đơn vị nguồn, nhưng p000013 mất chi tiết phát âm và thay bằng hành động; p000009 làm mất độ mở của câu hỏi đầu. p000010 dùng phạm vi tuổi rộng hơn, ảnh hưởng nhẹ vì ngữ cảnh vẫn rõ. |

Canon hiện chưa chốt thuật ngữ, nhân vật hoặc định dạng. Điểm nhất quán đánh giá phương án tạm trong gói; không suy luận rằng các báo cáo ngoài phạm vi đọc có hay không có đề xuất. Chưa đủ căn cứ cho mức 5 về hệ thống đề xuất và xưng hô toàn tác phẩm. Quân hàm: **không xuất hiện** ở cả hai ứng viên.

Phần chữ nghiêng là giới hạn của biểu diễn trong gói mù, cần xác nhận ở quy trình dựng bản xuất bản; chưa coi đây là lỗi vi phạm một quy ước đã duyệt. Điểm kỹ thuật không chứng nhận chất lượng EPUB.

**Lỗi loại trực tiếp:** không phát hiện ở cả hai ứng viên. Không có đảo phủ định, nhầm chủ thể, sai quan hệ được nguồn xác lập hoặc bỏ nguyên đơn vị nguồn. Các sai lệch của B ở p000009/p000013 là lỗi vừa, không được nâng thành lỗi loại trực tiếp. **Cả hai chưa đạt điều kiện duyệt của rubric:** A còn tiêu chí văn xuôi dưới 4; B còn tiêu chí nghĩa và độ đầy đủ dưới 4. Không dùng tổng điểm để bù các điểm này.

## 2. Nhận xét theo segment_id

“Lỗi vừa” là sai lệch nghĩa hoặc trở ngại diễn đạt cần sửa trước khi dùng; chỗ chỉ cần tinh chỉnh được ghi rõ là nhẹ. Nhận xét chỉ nhắc cụm cần thiết, không chép câu nguồn hay toàn bộ câu dịch.

| segment_id | Lỗi nghiêm trọng / loại trực tiếp | Lỗi vừa | Điểm mạnh | Chọn riêng đoạn | Lý do ngắn, cụ thể |
| --- | --- | --- | --- | --- | --- |
| `YS-LN01/Text/chapter001.xhtml/p000008` | A/B: không phát hiện. | A — văn xuôi: cấu trúc “bị một nỗi… ập xuống” phối hợp bị động với hình ảnh gây vấp. B: không có lỗi vừa; cụm thời gian còn cứng, mức nhẹ. | A giữ độ mạnh của sự hoang mang; B giữ mốc gần ba năm và tiến trình bắt đầu tìm lại bản thân, câu gọn hơn. | B | Hai bản giữ ý chính; B dễ đọc hơn ở cấu trúc câu chính. |
| `YS-LN01/Text/chapter001.xhtml/p000009` | A/B: không phát hiện. | A — văn xuôi/độ rõ: “giữ được tỉnh thức” là kết hợp từ khó hiểu trong ngữ cảnh duy trì ý thức. B — nghĩa/độ đủ: “Đây là đâu?” thu hẹp câu hỏi về tình trạng đang xảy ra thành xác định địa điểm. | A giữ trọng tâm câu hỏi và sự tách biệt giữa thân xác với ý thức. B diễn đạt sự suy giảm ý thức mượt, giữ quan hệ nguyên nhân và cảm giác xấu hổ không rõ lý do. | A | Trọng tâm của câu hỏi mở đầu được giữ đúng hơn; vấn đề diễn đạt của A có thể sửa cục bộ. |
| `YS-LN01/Text/chapter001.xhtml/p000010` | A/B: không phát hiện. | Không có lỗi vừa rõ. A có nhịp nặng ở cụm chỉ sự nhẹ nhõm; B dùng “trẻ nhỏ” rộng hơn trẻ sơ sinh và “khinh ghét” hơi lệch sắc thái khinh miệt; đều mức nhẹ trong ngữ cảnh này. | Cả hai giữ mức chắc chắn khác nhau giữa người lớn và trẻ sơ sinh, quan hệ bảo vệ/cơ hội bình đẳng, cùng bước tự gạt bỏ xấu hổ. | Hòa | A sát phạm vi và sắc thái hơn; B trôi chảy hơn. Chưa có chênh lệch đủ lớn để chọn dứt khoát. |
| `YS-LN01/Text/chapter001.xhtml/p000011` | A/B: không phát hiện. | Không có lỗi vừa chắc chắn. A có “yên tâm giả định”, “giải thích bằng thương tích” hơi cứng. B gọi sự hiểu biết mơ hồ là ý thức trở lại, làm nhạt phân biệt với lúc tỉnh lại; mức nhẹ. | A giữ nét nhận thức bắt đầu hé lên. B diễn đạt cảnh chăm trẻ thuận hơn. Cả hai giữ Yamanote, điều kiện trí nhớ, vẻ phỏng đoán về nữ tu và hai giả thuyết bệnh viện/chấn thương. | Hòa | A rõ hơn về tiến trình nhận thức; B thuận tiếng Việt hơn. Các điều kiện và suy luận chủ chốt đều được giữ. |
| `YS-LN01/Text/chapter001.xhtml/p000012` | A/B: không phát hiện. | A — văn xuôi: chuỗi “ánh sáng nghèo nàn”, “nguồn sáng thiếu thốn”, “đèn khí lạc thời” gượng và khiến người đọc phải giải mã. B: không có lỗi vừa rõ. | Cả hai giữ sự nhận ra trang phục cũ và phỏng đoán có điều kiện về đèn; B dùng từ dễ hiểu hơn, giữ nhịp ngập ngừng. | B | B rõ và tự nhiên hơn mà vẫn giữ mức độ chưa chắc chắn. |
| `YS-LN01/Text/chapter001.xhtml/p000013` | A/B: không phát hiện. | B — nghĩa/độ đủ: thay yêu cầu phát ra âm bằng yêu cầu mở miệng; hành động có thể phù hợp cảnh nhưng không giữ hết chi tiết chỉ dẫn. A: không có lỗi vừa; lời nhắc phát âm hơi cứng, mức nhẹ. | A giữ chi tiết phát âm; B có lời chăm trẻ tự nhiên. Cả hai giữ tên Tanya và sắc thái thân mật. | A | Ưu tiên giữ chi tiết chỉ dẫn có trong nguồn. Cách xưng hô của cả hai vẫn là phương án tạm. |
| `YS-LN01/Text/chapter001.xhtml/p000014` | A/B: không phát hiện. | Không có lỗi vừa rõ. A có “vắng hẳn… một cách kỳ quặc” hơi nặng nhịp, mức nhẹ. | Cả hai giữ năm 2013, phân biệt đồ điện/điện tử, sự tương phản với đồ cổ và chuỗi câu hỏi nội tâm; B nối các ý thuận hơn. | B | B có nhịp quan sát rồi tự vấn tự nhiên hơn, không mất mắt xích lập luận. |
| `YS-LN01/Text/chapter001.xhtml/p000015` | A/B: không phát hiện. | Không có lỗi vừa được chứng minh. “Con yêu” và “ngoan” tạo sắc thái khác nhau; cần duyệt xưng hô, không đủ căn cứ kết luận sai quan hệ. | Cả hai giữ lời gọi thân mật, lặp tên và dấu cảm thán làm mạnh lần gọi sau; thống nhất với lựa chọn ở p000013. | Hòa | Đoạn quá ngắn, thiếu ngữ cảnh để xác lập ưu thế của một cách gọi. |

## 3. Kết luận và đề xuất

**Ưu tiên Candidate A cho bản dịch nháp hàng loạt, có điều kiện phải qua biên tập văn xuôi và kiểm tra nghĩa.** A giữ tốt hơn trọng tâm câu hỏi ở p000009 và chi tiết chỉ dẫn ở p000013. Văn xuôi của A thường cứng nhưng các vấn đề được thấy trong mẫu chủ yếu nằm ở cách diễn đạt. Lựa chọn này là ưu tiên thử nghiệm cho bản nháp, không phải phê duyệt chất lượng hoặc cho phép bỏ bước phản biện.

**Candidate B phù hợp hơn với vai trò tạo phương án diễn đạt tiếng Việt hoặc hỗ trợ biên tập văn xuôi.** B cho câu thuận hơn tại p000008, p000012 và p000014. Khi dùng phương án của B, người giữ quyền sửa phải đối chiếu nguồn để tránh việc diễn đạt tự nhiên làm thu hẹp câu hỏi hoặc thay chi tiết cụ thể bằng hành động suy ra. Đây là đề xuất phân vai, không phải kết quả kiểm chứng năng lực biên tập bằng một nhiệm vụ riêng.

Theo từng đoạn: A được chọn ở 2 đoạn, B ở 3 đoạn, hòa ở 3 đoạn. Quyết định ưu tiên A dựa trên tầm quan trọng của các chi tiết nghĩa, không lấy số đoạn thắng hoặc điểm trung bình thay cho đánh giá lỗi.

Tối đa năm quy tắc đề xuất dưới đây **chưa được duyệt**; chỉ ghi tại báo cáo, không sửa style-guide, glossary hoặc canon:

| Mã đề xuất | Nơi cân nhắc bổ sung | Quy tắc và căn cứ |
| --- | --- | --- |
| BL-P01 | Style-guide | Giữ đối tượng và độ mở của câu hỏi nội tâm; không tự chuyển câu hỏi về tình trạng thành câu hỏi địa điểm. Căn cứ: p000009. |
| BL-P02 | Style-guide | Với chỉ dẫn ngắn, giữ chi tiết phát âm nếu có; không thay bằng hành động suy ra từ cảnh. Căn cứ: p000013. |
| BL-P03 | Glossary-pending / hồ sơ xưng hô | Ghi phương án tạm phân biệt ý thức, thân xác và nhận thức; ghi riêng “nó” ở trần thuật, “mình” ở nội tâm và cách nữ tu gọi Tanya. Chưa xác lập quan hệ thân thuộc hoặc giới tính từ đại từ. Căn cứ: p000008–p000011, p000013–p000015. |
| BL-P04 | Style-guide | Dùng kết hợp từ tự nhiên cho trạng thái ý thức, ánh sáng và suy luận; sau khi sửa phải giữ nguyên mức chắc chắn, điều kiện và quan hệ nhân quả. Căn cứ: p000009, p000011–p000012. |
| BL-P05 | Style-guide / decisions | Xác lập cách ghi hoặc ánh xạ chữ nghiêng cho nội tâm và đại từ được nhấn mạnh khi đi từ JSONL sang bản xuất bản; không để văn bản phẳng làm mất dấu hiệu cấu trúc. Căn cứ: p000008–p000012, p000014. |

**Mức tin cậy: vừa đối với ưu tiên A trong đúng mẫu này; thấp khi suy rộng sang dịch hàng loạt.** Tám đoạn liền nhau gồm sáu đoạn kể/nội tâm và hai lời gọi rất ngắn. Mẫu không có quân hàm, hội thoại dài, hành động chiến đấu hoặc hệ thuật ngữ chuyên môn phong phú; cũng không cho phép kiểm tra nhất quán giữa chương. Không có ngữ cảnh trước p000008 hoặc sau p000015. Cần thêm mẫu thuộc các dạng này trước khi giao khối lượng lớn hoặc xác lập xưng hô lâu dài.

**Xác nhận phạm vi:** đã chấm đủ 8/8 `segment_id`, p000008, p000009, p000010, p000011, p000012, p000013, p000014 và p000015 cho cả Candidate A và Candidate B. Kiểm tra cục bộ cho thấy mỗi tệp có tám mã duy nhất; mã và thứ tự của hai ứng viên khớp nguồn, mọi trường dịch đều không rỗng.
