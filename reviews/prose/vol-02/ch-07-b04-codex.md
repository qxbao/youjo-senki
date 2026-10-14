# Phản biện b04 — vol-02, chương 7

Đã đối chiếu độc lập 28/28 dòng p000076–p000103 về nghĩa, văn phong, điểm nhìn, đại từ, cấp bậc, nhấn mạnh và toàn bộ 11 nhóm pending trong mục `chapter7_b04_translator_proposals`. Không sửa bản dịch; các sửa đổi dưới đây chưa được áp dụng.

Gói nguồn đúng SHA-256 `bbe4ad2e636962ef2d554ae815a8bbbed9f026b02a5ab93c3d6c14bc38729d46`. Hai JSONL đều có 28 dòng, mã đoạn khớp theo thứ tự và không trùng. Hash của cả năm tài liệu canon khớp primary handoff. Chỉ đối chiếu package b04, translation, self-check, hai handoff được giao, năm tài liệu canon được nêu và phần ledger b04; không dùng EPUB/PDF, package khác hay lore ngoài phạm vi. Không chép câu nguồn vào báo cáo.

Trong báo cáo, mã rút gọn pNNNNNN luôn có tiền tố `YS-LN02/Text/part0032.xhtml/`.

```yaml
role: reviewer
task_id: vol-02-ch-07-b04-review
state: done
review_path: reviews/prose/vol-02/ch-07-b04-codex.md
files_written:
  - reviews/prose/vol-02/ch-07-b04-codex.md
coverage:
  checked_rows: 28
  total_rows: 28
  pending_groups_reviewed: 11
  source_package_hash: pass
  segment_alignment: pass
  canon_reference_hashes: pass
counts:
  serious: 0
  moderate: 5
  minor: 3
  total: 8
unresolved_findings: [B04-C01, B04-C02, B04-C03, B04-C04, B04-C05, B04-C06, B04-C07, B04-C08]
validator: not_run
diff_check: not_run
commit: null
next_action: translator_revision_then_required_checks
findings:
  - id: B04-C01
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000076
    issue: Biến việc quan tâm cấp dưới thành việc chỉ tỏ ra quan tâm.
    resolution: Đề xuất bỏ phần diễn đạt về sự giả vờ; chưa áp dụng.
  - id: B04-C02
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000081
    related_segment_ids: [YS-LN02/Text/part0032.xhtml/p000082, YS-LN02/Text/part0032.xhtml/p000088]
    issue: Tự xác định Đại tướng từ danh xưng cấp tướng chung, gây lệch với cấp hàm cụ thể ở p000088.
    resolution: Tạm dùng tướng ở p000081–p000082; giữ thiếu tướng ở p000088, chưa canon.
  - id: B04-C03
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000082
    issue: Cụm làm đội đoạn hậu không tự nhiên khi chủ thể tự quy chiếu là một cá nhân.
    resolution: Đề xuất đảm nhiệm việc đoạn hậu ở đây; chưa áp dụng.
  - id: B04-C04
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000085
    issue: Câu về nói giảm nói tránh làm mờ người ép và người bị ép im miệng.
    resolution: Đề xuất diễn đạt rõ ông ta dùng lời lẽ để ép người khác im miệng; chưa áp dụng.
  - id: B04-C05
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000092
    issue: Tuyến gọi từ 01 tới 06 và 09 bị biểu diễn như dải số 01 đến 06.
    resolution: Đề xuất 01 gọi 06 và 09 và làm rõ màn chắn không giữ được lâu; chưa áp dụng.
  - id: B04-C06
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000098
    issue: Đổi lời chửi tục thành lời nguyền chết, làm lệch kiểu xúc phạm.
    resolution: Đề xuất lời chửi có hình ảnh tục tương ứng, giữ chữ nghiêng; chưa áp dụng.
  - id: B04-C07
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000101
    issue: Rời đội hình có thể được hiểu là đổi vị trí chiến thuật thay vì không còn tham chiến.
    resolution: Tạm diễn đạt một nửa đã phải ngừng tham chiến, không khẳng định tử vong hay nguyên nhân cụ thể.
  - id: B04-C08
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000103
    issue: Mệnh đề kết quả của giả định thiếu dấu hiệu giả định và câu về nhãn sai còn cứng.
    resolution: Giữ nếu cùng thì coi như mình đã và dùng ghi nhãn sai; chưa áp dụng.
pending_terms: [] # Các khuyến nghị đầy đủ được ghi trong bảng bên dưới; không sửa ledger.
term_recommendations:
  count_existing_groups: 11
  additional_choices: [General, dialogue_address, radio_route, profanity, mislabeling]
  status: proposed
  canon: false
risks:
  - Chưa đủ căn cứ từ b04 để xác lập hệ thống quân hàm hoặc quan hệ nhân vật cho các chương khác.
  - Cơ chế công thức và quan hệ giữa hai lớp bảo vệ chưa được giải thích đủ để bổ sung lore.
  - Chỉ tiêu tại p000101 không được định danh; không tự diễn giải thành số mục tiêu hay số người.
  - Còn năm findings mức vừa cần translator sửa trước khi coi lô đạt.
```

## Findings và sửa đổi đề xuất

**B04-C01 — vừa — p000076.** Nguồn đặt cái cớ ở việc điều người làm mồi nhử để hỗ trợ lính rút lui; vế tiếp theo nói lợi ích riêng đồng thời đi cùng sự quan tâm tới cấp dưới. “Tỏ ra quan tâm” đưa thêm kết luận rằng sự quan tâm chỉ là giả tạo. Câu sau còn nêu khả năng cứu người tăng lên, nên không cần thêm suy diễn này để giữ giọng tư lợi. Đề xuất: “nếu mình điều người làm mồi nhử với cớ yểm trợ cho một người lính đang rút lui, mình vừa có thể mưu cầu lợi ích riêng, vừa quan tâm đến cấp dưới”. Cách này cũng sửa kết hợp từ thiếu tự nhiên “điều nghi binh đi”. Có thể dùng “điều đội nghi binh” nếu muốn nhất quán với p000093; không thêm quân số.

**B04-C02 — vừa — p000081–p000082; đối chiếu p000088.** Danh xưng `General` trong hai đoạn đầu không đủ để chốt “Đại tướng”. Ngay trong gói, p000088 dùng cấp hàm cụ thể `major generals` khi nói hai vị cấp trên. Không có canon cấp bậc đã duyệt. Đề xuất tạm “tướng von Zettour”, “tướng von Rudersdorf” tại p000081 và p000082; giữ “hai vị thiếu tướng” tại p000088. Đây là cách bảo toàn mức cụ thể từng lần gọi, không suy diễn thăng/giáng cấp hoặc sửa lore. Phương án khác “Thiếu tướng” ở mọi lần gọi có căn cứ ngữ cảnh nhưng cụ thể hóa hai đoạn đầu hơn cần thiết; không ưu tiên.

**B04-C03 — nhẹ — p000082.** “Mình … làm đội đoạn hậu” khiến cá nhân thành cả một đội. Vai trò bảo vệ phía sau vẫn đúng, nhưng nên viết “đảm nhiệm việc đoạn hậu ở đây” hoặc “làm nhiệm vụ đoạn hậu ở đây”. Không cần đổi thuật ngữ trong mọi ngữ cảnh tập thể.

**B04-C04 — nhẹ — p000085.** “Ông ta … nói giảm nói tránh chuyện bị ép phải im miệng” dễ khiến người đọc hiểu ông ta là người bị ép hoặc chỉ đang nói về một sự việc thụ động. Mạch p000083–p000085 là Tanya nghi ngờ lời động viên của cấp trên dùng để bịt phản đối của mình. Đề xuất câu đầu: “Chắc chẳng ai giỏi dùng lời lẽ nói giảm nói tránh để ép người khác im miệng như ông ta đâu.” Giữ nguyên vế khả năng hiểu lầm và lời khuyên chuẩn bị cho điều xấu nhất; không biến nghi ngờ thành sự thật đã xác nhận.

**B04-C05 — vừa — p000092.** Cấu trúc liên lạc cùng kiểu với p000100–p000101 cho thấy 01 là bên gọi, 06 và 09 là bên nhận. “01 đến 06 và 09” dễ bị đọc là toàn bộ số từ 01 tới 06 cộng 09, làm thay đổi người nhận lệnh. Đề xuất: “01 gọi 06 và 09. Mau di chuyển đi. Màn chắn không giữ được lâu đâu.” Chủ thể ở câu cuối được hỗ trợ bởi màn chắn p000089–p000091 và sự phân biệt với sức chịu đựng của người nghi binh p000093. Phương án ít bổ nghĩa hơn: “Nó không giữ được lâu đâu.” Không thêm CP/Fairy vào đoạn này khi nguồn không có.

**B04-C06 — vừa — p000098.** Phần chữ nghiêng được giữ đúng, nhưng “đi chết đi” chuyển lời chửi có hình ảnh tục sang lời nguyền chết. Đề xuất tạm “A… ăn cứt đi.” để giữ kiểu xúc phạm và cường độ; phương án “A… khốn kiếp” tự nhiên hơn nhưng làm mất hình ảnh tục cụ thể. Không xác định thêm người nghe hay biến thành lời thoại phát ra; đây vẫn là nội tâm. Khuyến nghị chọn phương án đầu cho lần sửa này, chưa lập quy ước tục ngữ chung.

**B04-C07 — nhẹ — p000101.** “Rời đội hình” có thể chỉ thao tác bay hoặc di chuyển. Báo cáo thương vong ở p000100 và nhận xét chưa ai chết nhưng nhiều người khó trở lại chiến tuyến ở p000102 hỗ trợ cách hiểu không thể tiếp tục tham chiến. Đề xuất tạm “Một nửa bọn tôi đã phải ngừng tham chiến.” Phương án “Một nửa bọn tôi đã phải rời cuộc chiến” cũng được nhưng rộng hơn. Không đổi thành “một nửa đã chết”, không gán thương tích cụ thể, không giải thích chỉ tiêu còn mơ hồ ở câu sau. “Bọn tôi”/“chúng tôi” cùng đoạn nên thống nhất thành “chúng tôi” trong báo cáo vô tuyến; đây là chỉnh văn phong tùy chọn.

**B04-C08 — vừa — p000103.** “Nếu bị buộc tội … mình đã phản bội” để kết quả mang hình thức sự kiện thực tế, trong khi đoạn đang xét điều kiện giả định và hệ quả hoàn thành. Đề xuất “Nếu bị buộc tội quảng cáo sai sự thật, thì coi như mình đã phản bội nguyên tắc đầu tiên …”. Không đổi thành lời xác nhận rằng Tanya đã bị buộc tội. “Hô hào ‘dán nhãn sai’” nên đổi thành “hô hào về chuyện ‘ghi nhãn sai’” để rõ đó là cách gọi/biện bạch, không phải mệnh lệnh dán nhãn. Tạm chọn “ghi nhãn sai”; phương án “gắn nhãn sai” vẫn dùng được. Giữ liên hệ quảng cáo–nhãn–lòng tin, không tự thêm bối cảnh vụ bê bối hoặc cố ý gian lận.

## Toàn bộ lựa chọn pending

Mọi lựa chọn trong bảng là **đề xuất tạm, không canon**. Bảng xét đủ 11 nhóm của ledger b04; các nhắc tới đề xuất trước trong self-check chỉ được coi là thông tin bàn giao, không phải chứng cứ đã đọc các lô trước.

| Nhóm | Mã đoạn | Chọn tạm và căn cứ | Phương án khác / bất định |
| --- | --- | --- | --- |
| `rear guard` | p000082 | “đoạn hậu”; trong câu dùng “làm nhiệm vụ đoạn hậu” để giữ vai trò và chủ thể cá nhân. | “lực lượng đoạn hậu” khi thực sự gọi một tập thể; “đội hậu vệ” kém rõ sắc thái quân sự trong câu này. |
| `Major General(s)` | p000088 | “thiếu tướng”, giữ cấp hàm cụ thể được nêu trong package. | Giữ tiếng Anh ít tự nhiên; lược thành “hai vị” làm mất thông tin cấp hàm, không ưu tiên. Kết hợp cách gọi chung “tướng” ở p000081–p000082. |
| `mage(s)` | p000102 | “pháp sư”, cách gọi tạm hiện có đủ rõ cho đơn vị quân sự sử dụng phép thuật. | “thuật sĩ”; b04 chưa đủ để chọn một hệ thuật ngữ cho toàn bộ thế giới truyện. |
| `orb / computation orb` | p000089 | “quả cầu tính toán” cho thiết bị được gọi cụ thể tại đây; giữ thao tác nạp công thức từ thiết bị vào viên đạn. | “thiết bị dạng cầu” mất yếu tố tính toán. “Quả cầu” chỉ dành cho lần gọi rút gọn nếu có; không thêm lần xuất hiện trong b04. |
| `interference formula` | p000089–p000090 | Tạm giữ “công thức gây nhiễu” để nhất quán hai lần, hiểu như thuật ngữ còn mở: package cho thấy tác dụng ngăn hỏa lực và tạo vật chắn, chưa giải thích cơ chế. | “công thức can thiệp” trung tính hơn về cơ chế nhưng khá cứng. Không chọn “công thức đối kháng điện tử”: chưa có chứng cứ về điện tử hay sóng vô tuyến. Không chú giải thêm vào bản dịch. |
| `protective film / defensive shell` | p000089, p000097 | Giữ “màn chắn bảo hộ / lớp vỏ phòng thủ”, phân biệt hai cách gọi tại p000097, dùng nhất quán lớp vỏ ở p000089. | “màng bảo hộ / lớp vỏ phòng ngự” gần hình ảnh vật lý hơn nhưng chưa cần đổi. Không tự chốt đây là cùng một lớp hay hai hệ thống độc lập. |
| `Elinium Type 95` | p000097 | Giữ nguyên tên thiết bị; số 95 được bảo toàn. | “Elinium loại 95” là phương án Việt hóa, chưa có căn cứ cần thay lựa chọn đang dùng. Không thêm đặc tính thiết bị. |
| `General Staff` | p000086 | “Bộ Tổng tham mưu”, giữ sự phân biệt cơ quan với vai trò sĩ quan tham mưu trong cùng đoạn. | “cơ quan Tổng tham mưu” ít xác định tổ chức hơn; không suy diễn thẩm quyền từ tên gọi. |
| `Being X` | p000098 | Giữ “Being X”, khớp đề xuất P05-being-x của canon/glossary-pending.yml; không có quyết định duyệt Việt hóa. | “Thực thể X”; không tự đồng nhất tên này với mọi danh xưng thần linh. |
| `Lord` | p000096–p000097 | “Chúa”, hợp lời cầu chúc và lời Tanya bực vì đã thốt ra lời cầu; giữ cùng cách gọi trong hai đoạn. | “Thượng đế”; không cần quyết định giáo phái, không tự chốt quan hệ với Being X hay một mục God ngoài phạm vi. |
| `CP / Fairy` | p000100–p000101 | Giữ CP, Fairy và Fairy 01; “gọi” thể hiện đúng tuyến truyền tin. | Chỉ khai triển khi có chứng cứ. Không dịch Fairy thành tên mô tả hoặc tự đổi số hiệu. |

Các lựa chọn bổ sung cần coordinator ghi nhận, vẫn chưa canon: `General` → “tướng” (p000081–p000082); xưng hô tại p000083–p000084 nên tạm bỏ “cô” thành “tôi biết làm được” và “cấp trên đặt kỳ vọng cực kỳ cao” nếu muốn tránh giới tính hóa lời gọi khi canon nhân vật còn trống. Giữ “tôi” cho người nói ở p000083 là lựa chọn trung tính. “Các cậu” ở p000096–p000097 có thể tạm giữ do đang nói với lính dưới quyền đã được xác định trong b04; phương án trung tính là “mọi người”, không suy ra quan hệ thân mật hay giới tính toàn đơn vị. Không ghi nhận cách gọi nào thành quy tắc liên chương.

## Kiểm đủ 28 dòng

“Đạt” dưới đây có nghĩa không thấy lỗi cần sửa trong phạm vi review, không thay cho validator hoặc điều kiện hoàn tất pipeline.

| Mã đoạn | Kết quả đối chiếu |
| --- | --- |
| p000076 | B04-C01; giữ lợi ích riêng, hỗ trợ người rút lui và cơ hội cứu người. |
| p000077 | Đạt; “Chỉ huy” giữ chức vụ gọi, không tự gán cấp hàm. |
| p000078 | Đạt; giữ phản đối, nguy hiểm và nguyên nhân; “mình” đúng nội tâm. |
| p000079 | Đạt; đủ ba ý không có lựa chọn, thiếu thời gian và mệnh lệnh. |
| p000080 | Đạt; giữ tự sửa đáng buồn thành đáng mừng và quan hệ cấp trên–binh lính. |
| p000081 | B04-C02; “nó” đúng trần thuật, đủ lệnh bằng văn bản và quyền chỉ huy trực tiếp. |
| p000082 | B04-C02/C03; tuyến truyền lệnh và ý buộc tuân thủ được giữ. |
| p000083 | Đạt về nghĩa và câu hỏi mỉa mai; xưng hô “cô” chỉ là lựa chọn tạm, có phương án trung tính. |
| p000084 | Đạt về kỳ vọng và câu hỏi mỉa mai; cùng khuyến nghị xưng hô p000083. |
| p000085 | B04-C04; khả năng hiểu lầm và lập luận bi quan vẫn được bảo toàn. |
| p000086 | Đạt; giữ trình tự chuẩn bị rồi lạc quan, quan hệ cùng có lợi và đánh giá danh tiếng. |
| p000087 | Đạt; hai vùng chữ nghiêng đúng phạm vi, đoạn trần thuật ở giữa dùng “nó”. |
| p000088 | Đạt; thiếu tướng là tạm, đủ mong muốn làm việc lại, điều kiện cơ hội và ưu tiên sống sót. |
| p000089 | Đạt với thuật ngữ tạm; đủ thiết bị, công thức, viên đạn, vị trí lớp vỏ và hướng hỏa lực. |
| p000090 | Đạt; giữ an toàn tạm thời, địch nhận biết vật chắn và suy ra có thứ phía sau. |
| p000091 | Đạt; giữ phần lớn hỏa lực và thời điểm hướng vào vị trí đó. |
| p000092 | B04-C05; cần sửa tuyến gọi và làm rõ thứ không giữ được lâu. |
| p000093 | Đạt; điều kiện di chuyển chậm và nhu cầu kéo chú ý khỏi Tanya còn nguyên. |
| p000094 | Đạt; ba lần thúc giục và một vùng chữ nghiêng đúng. |
| p000095 | Đạt; xác nhận lệnh và lời chúc được giữ. |
| p000096 | Đạt; lời cầu bảo vệ, dấu ngập ngừng; danh xưng và lời gọi chỉ tạm. |
| p000097 | Đạt; giữ bực vì lỡ cầu nguyện, điều kiện thiếu thiết bị và hệ quả đối với người/lớp bảo vệ. |
| p000098 | B04-C06; phép so sánh tín dụng tiêu dùng, ba ý không muốn/không nên/buộc phải vay đều đúng; chữ nghiêng đúng. |
| p000099 | Đạt; giữ tám nghìn feet, tính duy nhất của loại vũ khí và điều kiện bị trúng. |
| p000100 | Đạt; tuyến gọi, yêu cầu thương vong và tình trạng đúng. |
| p000101 | B04-C07; số một nửa được giữ cả hai lần, chỉ tiêu chưa bị cụ thể hóa, kho đạn vẫn chưa tìm thấy. |
| p000102 | Đạt; không biến tổn thất thành tử vong, giữ phỏng đoán về khả năng trở lại và trung thực khi tuyển quân. |
| p000103 | B04-C08; giữ nguyên tắc trung thực, ẩn dụ thị trường/lòng tin và lặp sắc thái sợ hãi. |

## Nhấn mạnh, self-check và bước tiếp theo

Đối chiếu XHTML trong package cho thấy chỉ p000087 (hai vùng), p000094 (một vùng) và p000098 (một vùng) có nhấn mạnh. Translation giữ đủ bốn vùng, không thêm chữ nghiêng ở các đoạn nội tâm khác. DEC-P01-001 được tuân thủ ở phần tự quy chiếu “mình” và trần thuật “nó”; lời thoại phải được xét riêng như khuyến nghị trên.

Self-check đúng về phạm vi nhấn mạnh, không suy diễn tử vong và giữ CP/Fairy. Tuy nhiên, cần bổ sung các lỗi cấp hàm, tuyến liên lạc p000092, sắc thái chửi p000098, phần giả định p000103 và việc thêm sự giả vờ p000076. Việc giữ đúng các con số tại p000092 chưa đủ nếu quan hệ người gửi–người nhận bị đổi.

Đề nghị coordinator chuyển tám findings cho người giữ quyền sửa translation; ưu tiên năm mục mức vừa, áp dụng lựa chọn tạm nhất quán và cập nhật ledger/handoff theo quyền của coordinator. Sau sửa, thực hiện validator và diff-check bắt buộc. Review này đã hoàn tất nhưng b04 chưa đạt điều kiện hoàn tất khi các findings mức vừa còn mở. Không có chứng cứ lỗi nghiêm trọng hay nhu cầu quyết định canon ảnh hưởng cốt truyện trong phạm vi b04; không cần dừng chờ chốt các pending ở trên.
