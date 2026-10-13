# Review — vol-02-ch-06-b02-review

- Vai trò: reviewer (Codex). Phạm vi: 32 ID từ `YS-LN02/Text/part0030.xhtml/p000036` đến `YS-LN02/Text/part0030.xhtml/p000067`.
- Đã đọc agents/shared.md, agents/reviewer.md, config/translation-pipeline.yml, handoff review và handoff gốc b02, bản dịch, self-check, đúng năm tệp canon được handoff gốc dẫn, cùng mục chapter6_b02_translation_proposals trong ledger.
- SHA-256 gói nguồn: `257ce85587df6c83d5c436d6bef806e1e8141f11a0e6f8e4489f0eda6e168a18`, khớp handoff. Hash cả năm tệp canon cũng khớp handoff gốc. Gói nguồn và bản dịch đều có đủ 32 ID, đúng thứ tự.
- Chỉ dùng gói nguồn được giao, gồm text và markup tại chỗ; không đọc EPUB/PDF hay gói nguồn khác. Báo cáo không chép câu nguồn.
- Kết quả: **0 nghiêm trọng, 5 vừa, 2 nhẹ**, tất cả chưa xử lý trong bản dịch. Số còn mở nghiêm trọng/vừa: **0/5**. Review đã hoàn tất; batch cần translator sửa trước khi được thông qua. Validator và diff-check: not_run; commit: null.

## Findings theo mức độ và ID ổn định

### Vừa

| Finding | Segment ID | Vấn đề và căn cứ | Đề xuất xử lý |
| --- | --- | --- | --- |
| B02-M01 | YS-LN02/Text/part0030.xhtml/p000040 | Toàn bộ lời cảnh cáo nằm trong thẻ em của gói nguồn, nhưng bản dịch không có Markdown chữ nghiêng. Đây là thiếu dấu nhấn theo DEC-P01-002; self-check chưa phát hiện. | Bao toàn bộ lời thoại, kể cả dấu ngoặc kép, bằng `*...*`; không thêm nhấn vào đoạn dẫn khác. |
| B02-M02 | YS-LN02/Text/part0030.xhtml/p000043 | “Họ từng bày tỏ…” sau chủ ngữ “các học giả” dễ quy ý định phái cứu viện cho học giả. Ngữ cảnh tuyên truyền từ Cộng hòa và binh sĩ Cộng hòa ở p000044 hỗ trợ chủ thể là phía Cộng hòa. Mệnh đề khả năng ở câu trước được giữ đúng. | Thay “Họ” bằng “Phía Cộng hòa”; không tự chỉ định một cơ quan hoặc người phát ngôn. Đây là lựa chọn tạm có căn cứ ngữ cảnh mạnh, không phải quyết định canon. |
| B02-M03 | YS-LN02/Text/part0030.xhtml/p000049 | “Không có tù binh” thu hẹp lời phủ nhận người bị giam thành phủ nhận tù binh quân sự. Trong p000040 và p000048, lời yêu cầu liên quan cả dân thường/thần dân đang bị giữ; danh từ ở lời đáp không tự giới hạn vào người bị bắt trong chiến đấu. Sự thu hẹp làm yếu mắt xích dẫn sang p000050. | Dùng “Không có ai bị giam giữ cả” hoặc “Không có người bị giam nào cả”. p000038 vẫn có thể dùng “quyền được đối xử như tù binh” trong lập luận về tư cách người tham chiến; không thay đồng loạt mọi lần xuất hiện. p000050 nên đồng bộ thành “không có người bị giam giữ” để bảo toàn liên hệ với lời phủ nhận, không diễn giải thêm tính hợp pháp của lập luận. |
| B02-M04 | YS-LN02/Text/part0030.xhtml/p000057 | “Tập đoàn quân” gán cấp tổ chức cụ thể mà gói nguồn và canon chưa xác lập. Self-check đã nhận đúng rủi ro nhưng bản dịch vẫn chọn phương án suy diễn. Căn cứ được giao chỉ bảo đảm tên gọi lực lượng theo khu vực phía Tây và chiến tuyến của lực lượng ấy. | Tạm dùng “Quân đội Khu vực phía Tây” theo phương án thay thế trong ledger; giữ đây là đề xuất. Không tự chuyển thành quân đoàn, tập đoàn quân hoặc bộ tư lệnh quân khu. |
| B02-M05 | YS-LN02/Text/part0030.xhtml/p000060 | “Cắt đứt liên lạc” chỉ rõ một loại kết nối, trong khi đoạn nguồn diễn tả hậu phương bị chia cắt khỏi tiền tuyến. p000061–p000063 còn triển khai nguy cơ quân bị ghìm chân và đường sắt tiếp tế; bản dịch hiện tại dễ khiến người đọc hiểu vấn đề chỉ là truyền tin. | Dùng “cuộc nổi dậy đã chia cắt các khu vực hậu phương của Lục quân Đế quốc ở phía tây khỏi tiền tuyến”. Giữ điều kiện dẫn nhập là xét một tình thế, không biến việc chia cắt thành phỏng đoán; không thêm kết luận tuyến tiếp tế đã bị phá hủy. |

### Nhẹ

| Finding | Segment ID | Vấn đề và căn cứ | Đề xuất xử lý |
| --- | --- | --- | --- |
| B02-L01 | YS-LN02/Text/part0030.xhtml/p000054 | “Hôm nay cùng chúng ta có…” thiếu tự nhiên trong lời giới thiệu khách mời; “hôm nay” cũng là chi tiết không được nêu trực tiếp. Vai trò người dẫn và câu hỏi vẫn đúng. | “Cùng chúng ta có Giáo sư Walter Halbom thuộc Đại học Londinium.” hoặc “Khách mời của chúng ta là…”. Giữ tên và học hàm, không thêm thông tin nhân vật. |
| B02-L02 | YS-LN02/Text/part0030.xhtml/p000056 | “Theo lối chiến lược các thứ” ghép từ gượng. Nguồn có sắc thái nói miệng, nên không cần xóa toàn bộ nét khẩu ngữ của giáo sư. | Có thể dùng “Nói cách khác, họ nhìn mọi việc dưới góc độ chiến lược và những chuyện đại loại thế.” Giữ chữ nghiêng và dấu mở thoại liên đoạn. |

## Kiểm tra đủ 32 ID

Mỗi dòng đã xét nghĩa, văn phong, điểm nhìn/chủ thể, nhấn mạnh và thuật ngữ. “Đạt” nghĩa là không thấy lỗi cần sửa có căn cứ trong phạm vi được giao, không phải phê duyệt canon. Tiền tố đầy đủ của các ID dưới đây là `YS-LN02/Text/part0030.xhtml/`.

| ID | Kết quả |
| --- | --- |
| p000036 | Đạt: giữ tranh cãi hiện tại, chỉ trích và đối lập luật/lẽ thường. |
| p000037 | Đạt: ý kiến được quy cho học giả luật; lời hướng đến khán giả giữ đúng. |
| p000038 | Đạt: không quân phục, tư cách phi chính quy và phủ định bảo đảm quyền được giữ; thuật ngữ tạm T01. |
| p000039 | Đạt: giữ “có lẽ” và hành động cảnh cáo. |
| p000040 | B02-M01; điều 26, khoản 3 và đối tượng dân thường được giữ; thuật ngữ tạm T02. |
| p000041 | Đạt: một số ít người tìm cách trốn, bị bắn trước mắt quân đội; không biến cố gắng thành trốn thành công. |
| p000042 | Đạt: giữ câu hỏi nguyên nhân của người dẫn. |
| p000043 | B02-M02; giữ tính khả thể của nhận định về tuyên truyền. |
| p000044 | Đạt: một số binh sĩ, không nâng thành toàn thể quân đội. |
| p000045 | Đạt: giữ quy thuộc sử gia và ý kiến về ảnh hưởng của pháp sư; chưa biến thành nguyên nhân chắc chắn. |
| p000046 | Đạt: tâm lý cầm cự được quy cho lời kể người sống sót. |
| p000047 | Đạt: lời cảnh cáo cuối cùng và thứ tự sự kiện. |
| p000048 | Đạt: yêu cầu gặp đại diện để thảo luận, thần dân đang bị giam; đúng phạm vi chữ nghiêng; T01/T02. |
| p000049 | B02-M03; phần chữ nghiêng chỉ bao lời đáp, đúng markup. |
| p000050 | Liên quan B02-M03: đồng bộ phạm vi người bị giam; giữ cấu trúc lập luận được người dẫn trình bày, không bổ sung phán quyết pháp lý. |
| p000051 | Đạt: giữ mục đích tránh trách nhiệm xác nhận bằng mắt và dự định gây cháy bằng pháo kích, không khẳng định kết quả. |
| p000052 | Đạt: giữ bằng chứng từ một phần hồ sơ và mục tiêu thử nghiệm; “bão lửa” là tạm T05. |
| p000053 | Đạt: giữ đánh giá tàn bạo/khét tiếng và tên Thảm sát Arene. |
| p000054 | B02-L01; câu hỏi giữ đối tượng, mức quyết liệt và không do dự. |
| p000055 | Đạt: cờ translator về paradigm được xét tại T03; “mô thức tư duy” dùng được, không cần sửa chỉ vì pending. |
| p000056 | B02-L02; không có lệch nghĩa đáng kể. |
| p000057 | B02-M04 và T04; giữ quan hệ bạo loạn ở phía sau chiến tuyến và lối nghĩ của binh sĩ. |
| p000058 | Đạt: giữ mầm mống kháng chiến và giả thuyết có người kích động, không coi giả thuyết là sự thật. |
| p000059 | Đạt: nhận định của giáo sư và không thể bác bỏ hoàn toàn được giữ. |
| p000060 | B02-M05; mở đầu xét tình thế được giữ. |
| p000061 | Đạt: ưu tiên nỗi lo, trước khi tập hợp lực lượng, và mất khu công nghiệp là nguy cơ trong điều kiện được nêu; không phải sự kiện đã xảy ra. |
| p000062 | Đạt: phương án nổi dậy bị giới hạn trong vùng và vai trò đường sắt tiếp tế được giữ; vẫn là nhận định giáo sư. |
| p000063 | Đạt: điều kiện áp lực lên tiếp tế và giới hạn sức chiến đấu được giữ. |
| p000064 | Đạt: nguy cơ kịch bản tồi tệ nhất cùng dè dặt về cách suy luận phía Đế quốc. |
| p000065 | Đạt: mức chấn động lớn và bình diện chiến lược. |
| p000066 | Không kết luận lỗi: giữ trải nghiệm quân ngũ và chỉ ý nghĩ cũng gây kinh hãi. “Các tuyến liên lạc” còn có thể mang nghĩa rộng về đường kết nối quân sự; nếu sửa đồng bộ với p000060, ưu tiên “các tuyến kết nối với hậu phương”, không tự thu hẹp thành chỉ thông tin hoặc chỉ tiếp tế. |
| p000067 | Đạt: giữ “tôi nghĩ”, điều kiện can thiệp, yêu cầu khẩn trương và nguy cơ pháp sư tăng cường kháng chiến. “Gây sức ép” là lựa chọn trung tính phù hợp khi cách can thiệp chưa rõ. |

Nhấn mạnh: p000040 bị thiếu; p000048, phần lời đáp p000049 và toàn bộ p000055–p000067 khớp phạm vi em. Các đoạn khác không bị thêm chữ nghiêng. Dấu mở thoại ở mỗi đoạn p000055–p000067 nhưng chưa đóng là cấu trúc lời nói kéo dài có trong gói được giao, không phải lỗi cần tự bổ sung dấu đóng ở cuối batch. DEC-P01-001 về Tanya không áp sang người dẫn hoặc giáo sư; bản dịch không có dấu hiệu áp sai quy ước ấy.

## Năm lựa chọn tạm, không phải canon

| Mã | Thuật ngữ / ID đầy đủ | Đề xuất tạm | Phương án khác và lý do lựa chọn | Độ bất định |
| --- | --- | --- | --- | --- |
| T01 | irregular combatants — YS-LN02/Text/part0030.xhtml/p000038, YS-LN02/Text/part0030.xhtml/p000048, YS-LN02/Text/part0030.xhtml/p000050 | chiến binh phi chính quy | “Người tham chiến phi chính quy” trung tính hơn về cá nhân; “chiến binh bất quy tắc” bám từ nhưng kém tự nhiên. Giữ đề xuất ledger vì hợp đối lập với quân phục và quân chính quy; không tự gọi họ là khủng bố hoặc gán danh mục pháp lý ngoài lời kể. | Thấp về nghĩa trong lô; vừa về thuật ngữ pháp lý chính thức chưa chốt. |
| T02 | Rules of War on Land — YS-LN02/Text/part0030.xhtml/p000040, YS-LN02/Text/part0030.xhtml/p000048, YS-LN02/Text/part0030.xhtml/p000050 | Quy tắc Chiến tranh trên bộ | “Quy tắc chiến tranh trên đất liền” literal nhưng dài; “Quy tắc chiến tranh trên bộ” là lựa chọn viết hoa tiết chế. Giữ cách hiện có để nhất quán trong lô; không tự đồng nhất với một công ước ngoài đời hoặc đổi số điều/khoản. | Thấp về nghĩa; vừa về tên chính thức và viết hoa. |
| T03 | paradigm — YS-LN02/Text/part0030.xhtml/p000055 | mô thức tư duy | “Mô hình tư duy” dễ đọc; “khuôn khổ tư duy” diễn đạt khá tự nhiên; “hệ hình” chuyên môn hơn mức cần thiết. Canon pending đã có đề xuất liên quan mô thức ở một mục khác, nhưng chưa duyệt. Trong lời giáo sư, ý chính là lối tư duy thiên về quân sự và áp dụng logic ấy rộng khắp; cách hiện có giữ nghĩa và mức dè dặt. Không đổi thành “tư tưởng quân phiệt” vì thêm phán xét. | Thấp về nghĩa ngữ cảnh; vừa về lựa chọn văn phong. Cờ translator được giải quyết bằng khuyến nghị giữ tạm, không nâng canon. |
| T04 | Western District Army — YS-LN02/Text/part0030.xhtml/p000057 | Quân đội Khu vực phía Tây | “Lực lượng quân đội khu vực phía Tây” trung tính, dài hơn; “Quân đội quân khu phía Tây” hàm ý mô hình quân khu chưa chắc chắn; “Tập đoàn quân Khu vực phía Tây” hàm ý cấp tổ chức chưa được chứng minh. Chọn phương án có sẵn trong ledger để giữ tên vùng và quân đội mà tránh xác lập cấp. p000061 có thể tiếp tục dùng cách gọi mô tả “quân đội phía tây”. | Cao về cấp tổ chức; vừa về dạng tên Việt. Cờ translator có cơ sở và cần sửa B02-M04. Không cần chờ quyết định thông thường để áp dụng phương án trung tính. |
| T05 | firestorm — YS-LN02/Text/part0030.xhtml/p000052 | bão lửa | “Cơn bão lửa” hoặc “trận bão lửa” phù hợp khi thêm lượng từ; “đám cháy dữ dội” làm mất khái niệm cụ thể. Mục tiêu lan lửa và thử nghiệm hỗ trợ cách gọi hiện có; không thêm cơ chế vật lý, vũ khí hoặc kết quả thực nghiệm. | Thấp về cách gọi trong đoạn; cơ chế và kết quả chưa được gói xác lập. |

## Giới hạn và bàn giao

- Translator sửa B02-M01–M05, đồng bộ p000050 với B02-M03, rồi xử lý hai lỗi nhẹ. Không tính hai đoạn liên quan của cùng một finding thành hai lỗi vừa riêng.
- Chưa thấy lỗi nghiêm trọng hoặc quyết định canon ảnh hưởng cốt truyện cần dừng. Còn năm findings vừa nên báo cáo này không thông qua bản dịch hiện tại.
- Nhận định về chiến tranh và tư cách pháp lý ở đây chỉ đối chiếu lời kể hư cấu trong gói, không kiểm chứng luật ngoài đời. Không suy lore để xác lập cấp tổ chức.
- Độ rộng của các tuyến liên lạc tại p000066 chưa đủ để chốt nghĩa chuyên biệt; dùng cách diễn đạt rộng nếu chỉnh. Không yêu cầu mở nguồn ngoài phạm vi để tiếp tục sửa.
- Chỉ ghi báo cáo này; không sửa bản dịch, self-check, handoff, ledger, canon hoặc checkpoint; không chạy validator/diff-check và không commit.
