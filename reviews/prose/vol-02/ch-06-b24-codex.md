# Independent review — vol-02-ch-06-b24

## Phạm vi và kết luận

Đã đối chiếu độc lập đủ 36 hàng p000752–p000787 với package được giao, bao gồm XHTML nhấn mạnh trong package. SHA-256 package khớp `a1106140d11c8aac7c59fdb12f94336a45379acca67c25b56006d1d93ee6da6a`; bản dịch có đủ 36 ID, đúng thứ tự, không trùng ID. Đã đọc shared/reviewer, config, primary handoff, review handoff, self-check, năm tài liệu canon được primary handoff chỉ định và riêng mục ledger `chapter6_b24_translator_proposals`. Hash của cả năm tài liệu canon khớp primary handoff.

Không mở EPUB/PDF, chú thích ngoài package hoặc package khác; không tra cứu ngoài. Báo cáo không trích câu nguồn. Chỉ ghi tệp báo cáo này; không sửa translation/canon/ledger/handoff. Không chạy validator hay diff-check pipeline. Kiểm đếm ID và hash ở trên chỉ là kiểm tra đầu vào.

Kết luận: cần sửa 5 finding mức vừa và 1 finding mức nhẹ. Không phát hiện lỗi nghiêm trọng. Sáu nhóm pending có thể tiếp tục bằng lựa chọn tạm dưới đây, không cần dừng để duyệt canon. Không xác lập danh tính ngoài truyện hoặc chi tiết chiến thuật ngoài những gì package cung cấp.

## Findings chưa xử lý

### B24-C01 — Vừa — Đại từ tự quy chiếu nội tâm không nhất quán

- **Segment IDs:** `YS-LN02/Text/part0030.xhtml/p000754`, `p000755`, `p000756`, `p000757`, `p000760`, `p000761`, `p000762`, `p000763`, `p000767`, `p000769`, `p000782` (mọi mã rút gọn trong báo cáo có cùng tiền tố `YS-LN02/Text/part0030.xhtml/`).
- **Vấn đề:** nhiều câu suy nghĩ của Tanya vẫn tự xưng “tôi”, xen với “mình” ngay trong cùng mạch hoặc cùng đoạn. Đây là độc thoại ngôi thứ nhất, không phải lời kể ngôi thứ ba hay thoại trực tiếp. Self-check khẳng định đã dùng “mình” nhưng bản dịch chưa thực hiện nhất quán.
- **Căn cứ:** DEC-P01-001 quy định nội tâm tự quy chiếu dùng “mình”; p000754–p000757 tiếp nối suy nghĩ về học viện và hy sinh cấp dưới, p000760–p000764 là suy nghĩ về Uger và đường sống, p000767–p000770 và p000781–p000784 tiếp tục cùng điểm nhìn.
- **Đề xuất:** đổi các đại từ đơn số tự quy chiếu nêu trên thành “mình” hoặc lược khi tự nhiên. Không thay đại từ của người khác hay tự động đổi mọi đại từ số nhiều. Giữ “tôi” trong thoại trực tiếp khi phù hợp; lời tưởng tượng hướng tới Uger ở p000760 có thể giữ cách gọi lễ phép, nhưng phần dẫn nội tâm phải theo canon.

### B24-C02 — Vừa — p000755 mất quan hệ đối lập và sai phạm vi nhấn mạnh

- **Segment ID:** `YS-LN02/Text/part0030.xhtml/p000755`.
- **Vấn đề:** bản dịch tách khả năng làm được và ý không chịu làm thành hai ý phối hợp ngang hàng, rồi cùng đối lập với việc thử. Nguồn đối chiếu hai thái độ: thừa nhận làm được nhưng từ chối thực hiện, và chủ động thử. Ba vùng nghiêng ở bản dịch thay cho hai vùng của nguồn; quan hệ nhượng bộ bên trong thái độ thứ nhất bị mất.
- **Căn cứ:** cấu trúc nghĩa và hai phần tử nhấn mạnh trong XHTML package; DEC-P01-002 yêu cầu giữ phạm vi nhấn mạnh tương ứng.
- **Đề xuất:** “*Có thể làm được, nhưng mình sẽ không làm* và *Cứ thử xem sao* là hai chuyện rất khác nhau.” Giữ cả mệnh đề khả năng và từ chối trong một vùng nghiêng.

### B24-C03 — Vừa — p000762 thêm chiến thuật đánh lừa

- **Segment ID:** `YS-LN02/Text/part0030.xhtml/p000762`.
- **Vấn đề:** “nghi binh trì hoãn” đưa thêm hoạt động đánh lừa đối phương. Package chỉ nêu nhiệm vụ trì hoãn ở cuối đội quân khi rút lui, không nói đến nghi binh.
- **Căn cứ:** p000752–p000753 xác lập phòng ngự trì hoãn; p000762 nêu vị trí cuối đội quân; p000767 xác lập lực lượng đoạn hậu. Các đoạn này không cung cấp căn cứ về mưu đánh lừa.
- **Đề xuất:** “Nói cách khác, khi rút lui, mình sẽ phải ở cuối đội quân để đánh trì hoãn ư?” Có thể dùng “thực hiện nhiệm vụ trì hoãn” nếu muốn trung tính hơn. Giữ câu hỏi và giọng mỉa mai về bị đẩy đi chết.

### B24-C04 — Vừa — p000764 đổi xin phép sử dụng thành đăng ký quyền sở hữu

- **Segment ID:** `YS-LN02/Text/part0030.xhtml/p000764`.
- **Vấn đề:** “đăng ký bản quyền nó” khiến Tanya định đăng ký quyền sở hữu đối với tuyệt chiêu nhà Shimahdzu. Mạch nguồn đùa về việc xin giấy phép dùng chiêu của người khác và tuân thủ quy định; không xác lập chuyện nhận quyền sở hữu.
- **Căn cứ:** câu trước gắn chiêu với nhà Shimahdzu, câu sau nhấn việc luôn theo quy định. Cách diễn đạt hiện tại làm đổi hành động trong lời đùa.
- **Đề xuất:** “Có lẽ mình nên xin giấy phép sử dụng nó.” Phương án ngắn hơn: “Có lẽ mình nên xin phép dùng nó.” Không bổ sung học thuyết pháp lý hoặc giải thích lịch sử. Đây là lựa chọn tạm dựa trên mạch đoạn, không phải khẳng định một cơ chế cấp phép trong thế giới truyện.

### B24-C05 — Vừa — p000776 đổi thời gian của nguy cơ giả định

- **Segment ID:** `YS-LN02/Text/part0030.xhtml/p000776`.
- **Vấn đề:** “vẫn chưa bao giờ hoàn toàn biến mất” diễn đạt một lịch sử kéo dài đến hiện tại. Nguồn nói nguy cơ sẽ còn tồn tại ngay cả nếu lời xin thu hồi mệnh lệnh không bị từ chối.
- **Căn cứ:** p000774 đặt việc xin thu hồi mệnh lệnh ở sau đó; p000775–p000776 xét hai khả thể của yêu cầu chưa thực hiện. Style guide yêu cầu giữ thời gian và tính giả định.
- **Đề xuất:** “Không, ngay cả khi ông ấy không từ chối lời đề nghị của mình, nguy cơ chúng ta bị thủ tiêu cũng sẽ chẳng bao giờ hoàn toàn biến mất.” Giữ cả nhượng bộ, phủ định và chủ thể tập thể; không biến nguy cơ thành sự kiện đã được chứng thực.

### B24-C06 — Nhẹ — p000783 thu hẹp lời chơi về danh tiếng thành đánh giá tiêu cực

- **Segment ID:** `YS-LN02/Text/part0030.xhtml/p000783`.
- **Vấn đề:** “khá tai tiếng” áp sẵn nghĩa xấu cho nhận xét về pháo đài. Nguồn giữ cách nói mở về danh tiếng theo nhiều nghĩa rồi đưa ví dụ; giọng mỉa mai không đòi hỏi bổ sung một phán xét rõ hơn.
- **Căn cứ:** cách nối nhà máy điện, pháo đài và ví dụ Maginot trong chính đoạn; style guide hạn chế tự thêm sắc thái phán xét.
- **Đề xuất:** “Mà những pháo đài họ thực sự xây cũng khá nổi tiếng—hiểu theo nhiều nghĩa—chẳng hạn như phòng tuyến Maginot.” Giữ mỉa mai qua ngữ cảnh, không định danh “đám ốc sên” thành một quốc gia.

## Sáu khuyến nghị pending — tất cả là đề xuất, chưa phải canon

| Nhóm | Mã đoạn | Lựa chọn tạm đề nghị | Phương án khác và căn cứ/giới hạn |
|---|---|---|---|
| `rear guard` | p000767 | **lực lượng đoạn hậu** | “đội đoạn hậu” hiện dùng đúng chức năng và có thể giữ nếu coordinator ưu tiên tối thiểu thay đổi. “Đội hậu vệ” là phương án ledger nhưng dễ hiểu thành vị trí phía sau chung chung. “Lực lượng đoạn hậu” thể hiện nhiệm vụ bảo vệ cuộc rút lui, không áp cỡ tổ chức cụ thể. Không kết luận cách dùng ở batch trước sai vì không đọc chúng. |
| `Major / General` | p000760, p000772, p000774, p000785; p000775 liên quan quy chiếu | **Thiếu tá / Tướng** | Package trực tiếp gắn Major với Uger và von Degurechaff, General với von Zettour. Giữ cách dùng hiện tại; không suy thành Trung tướng/Đại tướng vì package không cho cấp tướng cụ thể. Phương án khác: giữ Major/General trong lúc chờ chuẩn hóa; lược quân hàm chỉ là phương án kém hơn vì mất thông tin trong lời gọi trực tiếp. p000775 chỉ có đại từ chỉ von Zettour, không có lần xuất hiện quân hàm mới. |
| `Shimahdzu(s)` | p000763–p000764 | **nhà Shimahdzu** | Package gọi một gia tộc chiến binh, nên “nhà” giữ đối tượng và một dạng tên ổn định. Có thể dùng “gia tộc Shimahdzu” ở p000763 hoặc giữ dạng Shimahdzus nếu muốn giữ hình thức nguồn; chưa có căn cứ để sửa chính tả sang tên lịch sử khác. Dấu chú thích 23 có trong package nhưng nội dung chú thích không thuộc phạm vi; không tự giải nghĩa. |
| `sutegamari` | p000764 | **lối vừa đánh vừa rút lui kiểu *sutegamari*** | Nguồn có mô tả chức năng rút lui trong chiến đấu, nên diễn nghĩa ngắn là có căn cứ. “Chiến thuật rút lui chiến đấu” hiện dùng hơi gượng; có thể thay bằng “chiến thuật rút lui có giao chiến kiểu *sutegamari*”. Không thêm chi tiết về các toán cảm tử, hiến sinh hay quy trình luân phiên vì package không nêu. Giữ chữ nghiêng chỉ quanh thuật ngữ. “Có khi mình phải dùng” giữ tính khả thể; bất định về cách chuẩn hóa ghi trong báo cáo, không chèn ghi chú vào bản dịch. |
| `ersatz coffee` | p000786 | **cà phê thay thế** | Giữ rõ đây là thứ thay cho cà phê, không cần độc giả biết từ ersatz; self-check nêu đây là đề xuất có trước, nhưng review chỉ xác nhận căn cứ tại b24. Phương án khác: “cà phê ersatz” hiện dùng, giữ màu từ ngoại ngữ nhưng khó hiểu hơn; “thứ thay cà phê” nếu cần khẩu ngữ. Không bổ sung thành phần, chất lượng hay thương hiệu. |
| `escargots` | p000783 | **đám ốc sên** | Giữ hình ảnh của tên gọi giễu và phù hợp đại từ tập thể trong đoạn. Phương án khác: giữ “escargots” để bảo toàn hình thức; “bọn ốc sên” tăng sắc thái khinh miệt nên không ưu tiên. Không thay bằng tên quốc gia hoặc nhóm người được suy từ nhà máy điện/Maginot; package chưa đủ để duyệt định danh. |

## Kiểm tra các điểm trọng tâm

- **Nhấn mạnh:** nguồn có bốn đoạn mang nhấn mạnh: p000755 (hai vùng), p000756, p000760 và p000764 (mỗi đoạn một vùng). p000756/p000760/p000764 giữ đúng phạm vi tương ứng; p000755 cần sửa C02. Self-check bỏ sót p000764 trong danh sách nhấn mạnh, nhưng bản dịch thực tế đã giữ `*sutegamari*`; đây là thiếu sót mô tả, không phải mất nhấn mạnh ở hàng đó. Không thấy thêm dấu nghiêng ở hàng khác.
- **Xưng hô thoại:** “cậu/các cậu”, “ông”, “ngài” thể hiện cách nói trực tiếp/giả định trong cảnh sĩ quan; chưa có căn cứ để nâng thành quy ước canon hay suy thân thuộc. p000752 có thể hiểu người nghe cùng đơn vị, p000765 trực tiếp hướng tới Tanya; chưa đủ căn cứ để coi số nhiều ở p000752 là lỗi. p000766 và p000786 có thể lược “cậu” để giảm giả định khi chỉnh văn, nhưng không bắt buộc và không tính thành finding. Việc dùng “tôi” trong thoại không cùng vấn đề với C01.
- **Tác chiến:** giữ được phòng ngự trì hoãn, thế bị bao vây chưa hoàn toàn, tổn thất một nửa quân số không đủ câu giờ, khả năng đơn vị bị tiêu diệt và yêu cầu đoạn hậu cảnh giác cao. Không đổi “một nửa” thành tổn thất đã xảy ra. C03 là chỗ duy nhất thêm loại hoạt động quân sự không có căn cứ.
- **Giả định và chủ thể:** p000774–p000778 vẫn là tính toán sinh tồn của Tanya; không coi ý bị bịt miệng/thủ tiêu là âm mưu đã xác nhận. p000777 giữ ý tàu bị đánh chìm vô tình, thử cân nhắc đầu hàng rồi nhận ra rủi ro, và bước chuyển từ khả thể xấu nhất sang sự chắc chắn trong suy nghĩ nhân vật. C05 cần sửa thời gian, không sửa thành kết luận khách quan.
- **Liên tưởng:** Rudel và Maginot được giữ đúng dạng package, không xác lập lore/danh tính ngoài văn bản. p000781 giữ 5,7 mét và câu hỏi hậu quả; không bổ sung tên thảm họa. p000784/p000787 giữ cách tự giễu và sự không rõ nguyên nhân. Nội dung chú thích 23 chưa được kiểm tra theo giới hạn đầu vào, không tự tạo chú thích mới.

## Nhật ký kiểm đủ 36 hàng

“Đạt” ở đây chỉ có nghĩa không thấy lỗi cần ghi finding trong hàng, không thay kết quả validator. Pending được đánh giá riêng, không mặc nhiên là lỗi.

| Segment | Kết quả kiểm nghĩa/văn/điểm trọng tâm |
|---|---|
| p000752 | Đạt: nhiệm vụ trì hoãn, khó khăn và phỏng đoán lý do triệu tập. |
| p000753 | Đạt: bao vây chưa hoàn toàn, mất nửa quân số vẫn không câu được thời gian. |
| p000754 | C01; mạch hồi tưởng học viện và bất ngờ trước tình huống giữ được. |
| p000755 | C01, C02; cần khôi phục cấu trúc hai thái độ và hai vùng nghiêng. |
| p000756 | C01; lá chắn/cấp dưới và yêu cầu kỷ luật giữ được, vùng nghiêng đúng. |
| p000757 | C01; giữ việc tự nhận là sĩ quan trẻ và đòi hỏi quá sức. |
| p000758 | Đạt: phản ứng trước nửa quân số và khả năng gần như bị xóa sổ. |
| p000759 | Đạt: xác nhận nguy cơ, tình huống thi vấn đáp phải thực hiện thật. |
| p000760 | C01; quân hàm Uger tạm hợp lý, vùng nghiêng đúng, ý muốn phản đối vô ích giữ được. |
| p000761 | C01; nhận xét dè dặt về tính cách Uger giữ được. |
| p000762 | C01, C03; giữ giả định tin Uger và mỉa mai nhưng phải bỏ nghi binh. |
| p000763 | C01; tên gia tộc pending, kiềm chế bỏ chạy và chuyển sang tìm cách sống sót giữ được. |
| p000764 | C04; tên và thuật ngữ pending, khả thể dùng chiêu và vùng nghiêng giữ được. |
| p000765 | Đạt: trấn an nhiệm vụ ngắn, chủ yếu canh chừng, có câu hỏi. |
| p000766 | Đạt: chuẩn bị cho điều tệ nhất, không thích tính khí của bản thân; “chiến trường triền miên” hơi cứng nhưng hiểu được. |
| p000767 | C01; hy vọng không phải bảo đảm, không đặt mạng vào cơ may, chức năng đoạn hậu giữ được. |
| p000768 | Đạt: hối tiếc ăn bò hầm, muốn nôn, câu hỏi phỏng đoán về Rudel. |
| p000769 | C01; phủ nhận phỏng đoán trước và nhận xét về dinh dưỡng/nghiện chiến trường giữ được. |
| p000770 | Đạt: có thể học theo việc uống sữa và để sau cân nhắc. |
| p000771 | Đạt: lời hứa cố gắng và rút ngắn thời gian, không thành bảo đảm tuyệt đối. |
| p000772 | Đạt: cảm ơn Uger, quân hàm pending giữ đúng người. |
| p000773 | Đạt: lời bực bội ngắn. |
| p000774 | Đạt: khả thể xin von Zettour thu hồi lệnh về sau, cấp tướng không tự cụ thể hóa. |
| p000775 | Đạt: điều kiện bịt miệng và chắc chắn sẽ không thu hồi trong điều kiện ấy; đại từ nối đúng Zettour. |
| p000776 | C05; nhượng bộ giữ được nhưng thời gian nguy cơ cần sửa. |
| p000777 | Đạt: cân nhắc đầu hàng, tự bác vì rủi ro, tai nạn tàu, bị hy sinh vì quan hệ hai bên. |
| p000778 | Đạt: điều kiện và ưu tiên thoát tình thế hiện tại. |
| p000779 | Đạt: nghĩa vụ người lính và câu hỏi xác nhận. |
| p000780 | Đạt: giả vờ không biết để sống sót, mong tất cả chỉ là hiểu lầm. |
| p000781 | Đạt: đối lập bi quan/lạc quan, chi phí, 5,7 mét và câu hỏi hậu quả. |
| p000782 | C01; chi phí, so sánh quốc gia/doanh nghiệp, ủng hộ hòa bình và can thiệp vì lợi ích giới hạn giữ được. |
| p000783 | C06; biệt danh pending, đối chiếu nhà máy/pháo đài và ví dụ Maginot giữ được. |
| p000784 | Đạt: tự giễu việc đầu óc lan man. |
| p000785 | Đạt: quân hàm đúng von Degurechaff, gặp lại và đề nghị nâng ly. |
| p000786 | Đạt nghĩa: chỉ có đồ thay cà phê và sẵn lòng nếu người nghe chấp nhận; thuật ngữ pending nên chuẩn hóa tạm. |
| p000787 | Đạt: lần sau chuẩn bị sữa, Đế quốc nổi tiếng về sữa nhưng không rõ vì sao. |

## Rủi ro và bước tiếp theo

Năm finding vừa chưa được xử lý nên chưa thể coi batch đã hoàn tất review. Self-check chưa nhận diện các lỗi logic/đại từ/thời gian trên và mô tả thiếu một đoạn nhấn mạnh. Lựa chọn về giấy phép ở p000764 là cách hiểu có căn cứ tại chỗ; không dùng nó để xác lập luật bản quyền trong lore. Các phương án tên/thuật ngữ và xưng hô vẫn tạm thời; không tự đồng nhất tên với lịch sử hoặc biệt danh với quốc gia. Không có yêu cầu quyết định canon ảnh hưởng cốt truyện phát sinh từ review này.

Coordinator tiếp nhận C01–C06, ghi sáu lựa chọn tạm vào ledger/handoff; translator giữ lease mới sửa bản dịch. Sau sửa, cần đối chiếu lại các hàng liên quan và chạy validator/diff-check theo pipeline. Reviewer không tự sửa hoặc commit.

```yaml
role: reviewer
task_id: vol-02-ch-06-b24-review
state: done
review_path: reviews/prose/vol-02/ch-06-b24-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b24-codex.md
counts:
  rows_reviewed: 36
  serious: 0
  moderate: 5
  minor: 1
  total: 6
  pending_groups: 6
unresolved_findings: [B24-C01, B24-C02, B24-C03, B24-C04, B24-C05, B24-C06]
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_assign_translation_revision
```
