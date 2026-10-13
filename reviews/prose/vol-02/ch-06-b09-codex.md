# Review b09 — vol-02, chương 6

```yaml
role: reviewer
task_id: vol-02-ch-06-b09-review
state: done
review_path: reviews/prose/vol-02/ch-06-b09-codex.md
files_written: [reviews/prose/vol-02/ch-06-b09-codex.md]
scope:
  start: YS-LN02/Text/part0030.xhtml/p000257
  end: YS-LN02/Text/part0030.xhtml/p000284
  assigned: 28
  assessed: 28
source_package_sha256: b8e33087650cb9bb665a018e7adf731ed974f773356be5e7b132bb5d1561fe71
source_package_hash: pass
canon_reference_hashes: pass
counts: {serious: 0, moderate: 6, minor: 5}
unresolved_findings: [B09-F01, B09-F02, B09-F03, B09-F04, B09-F05, B09-F06, B09-F07, B09-F08, B09-F09, B09-F10, B09-F11]
term_recommendations:
  status: provisional_non_canon
  assigned_clusters: 8
  details: "Bảng đề xuất bên dưới; không nâng thành canon."
validator: not_run
diff_check: not_run
risks:
  - Self-check bỏ sót các thẻ em trong XHTML của năm ID.
  - Hai nhãn thuật ngữ b09 trong ledger khác từ thực tế ở gói nguồn.
  - Đại từ trần thuật cần sửa theo quy ước được handoff viện dẫn; đại từ trong thoại và nội tâm vị tư lệnh được xét riêng.
  - Lập luận pháp lý là cách diễn giải của nhân vật, không phải kết luận pháp luật do reviewer xác nhận.
commit: null
next_action: coordinator_accept_provisional_choices_then_translator_fix_and_recheck
```

Đã đọc `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, hai handoff b09, bản dịch, self-check, năm tài liệu canon được viện dẫn và các mục pending liên quan b09/b07 trong `work/run-state/pending-terms.yml`. Hash gói khớp chính xác; cả nguồn lẫn bản dịch có đủ 28 ID, cùng thứ tự và ranh giới. Hash cả năm tài liệu canon khớp handoff. Không mở EPUB/PDF, gói khác hoặc chú thích ngoài gói; không sửa đầu vào. Không tra cứu luật ngoài phạm vi: review chỉ đánh giá độ trung thành với lập luận trong tác phẩm.

Số lỗi tính theo finding độc lập, không theo số ID bị ảnh hưởng. Hoàn tất review không có nghĩa bản dịch đã đạt: còn 6 finding vừa cần người giữ quyền sửa xử lý. Các đề xuất thông thường đã được chọn tạm, không cần chờ người dùng và không hình thành quyết định canon.

## Findings

### B09-F01 — vừa — mất nhấn mạnh có trong gói nguồn

- ID: `YS-LN02/Text/part0030.xhtml/p000265`, `YS-LN02/Text/part0030.xhtml/p000276`, `YS-LN02/Text/part0030.xhtml/p000279`, `YS-LN02/Text/part0030.xhtml/p000281`, `YS-LN02/Text/part0030.xhtml/p000282`.
- Căn cứ: XHTML chứa lần lượt 1, 2, 3, 1, 1 thẻ `em`. Bản dịch không biểu diễn các vùng đó. Nhận xét self-check rằng gói không có nhấn mạnh là sai. Áp dụng DEC-P01-002.
- Đề xuất: p000265 đặt nghiêng toàn bộ suy luận giả định từ điều kiện ai cũng là binh lính đến kết luận về tội ác chiến tranh, không nghiêng phần lời kể bao quanh; p000276 đánh dấu phần tương ứng “bất kỳ ai” và liên từ lựa chọn “hay”; p000279 đánh dấu riêng câu hỏi về lính trẻ em, cụm cỗ máy chiến đấu, và nội dung lời đồn về người nhận huy hiệu; p000281 đánh dấu câu đánh giá cuối; p000282 đánh dấu toàn đoạn. Giữ phạm vi tương ứng sau khi sửa câu, không tự nghiêng các đoạn nội tâm khác.
- Bất định: thấp; cấu trúc XHTML trực tiếp xác nhận. Đây là một finding định dạng có tác động tới điểm nhìn/nhấn mạnh, không đếm thành năm lỗi riêng.

### B09-F02 — vừa — mệnh đề diễn giải bị đổi từ giả định sang phát biểu

- ID: `YS-LN02/Text/part0030.xhtml/p000264`.
- Vấn đề: nguồn đặt cả lời tuyên bố lẫn cách ta diễn giải vào điều kiện. Bản dịch bỏ dấu hiệu điều kiện ở câu bắt đầu “Ta diễn giải”, khiến cách phân loại thường dân thành dân quân nghe như bước đã được quyết định.
- Đề xuất: giữ cấu trúc “Nếu họ tuyên bố… Nếu ta diễn giải điều đó là… thì…”. Có thể nối hai điều kiện thành một câu rõ hơn nhưng giữ nguyên ranh giới đoạn. Không sửa lý lẽ của nhân vật theo quan niệm pháp luật bên ngoài.
- Bất định: thấp; điều kiện thứ hai được ghi trực tiếp trong nguồn.

### B09-F03 — vừa — tự xác định phương tiện sát thương

- ID: `YS-LN02/Text/part0030.xhtml/p000265`.
- Vấn đề: “ném bom” xác định cách tấn công mà động từ nguồn chỉ nói đến việc làm nổ tung các đối tượng. Tính giả định và kết luận về tội ác chiến tranh được giữ, nhưng phương tiện được thêm vào.
- Đề xuất tạm: “cho nổ tung tất cả bọn họ” trong mệnh đề giả định. Phương án khác: “dùng chất nổ giết hết họ”, nhưng cách này giải thích cơ chế nhiều hơn. Ưu tiên phương án đầu; không biến giả định thành hành động đã xảy ra.
- Bất định: thấp về việc không có chỉ định ném bom; vừa về sắc thái khẩu ngữ tiếng Việt. Không cần chờ xác minh lịch sử Nam Tư để sửa lỗi dịch này.

### B09-F04 — vừa — đổi loại phần thưởng

- ID: `YS-LN02/Text/part0030.xhtml/p000279`.
- Vấn đề: gói dùng thuật ngữ ngắn `Silver Wings Assault Badge`; ledger b09 ghi `Silver Wings Assault Medal`. “Huân chương” trong bản dịch đi theo nhãn ledger, nhưng chưa có canon hay căn cứ trong gói để đổi loại vật phẩm.
- Đề xuất tạm: “Huy hiệu Đột kích Cánh bạc”. Giữ đủ yếu tố nhận diện; không rút còn “Cánh bạc”. Coordinator cần ghi lại sự lệch nhãn khi tiếp nhận, reviewer không sửa ledger.
- Bất định: thấp về từ `Badge` trong gói; vừa về tên tiếng Việt chính thức và viết hoa. Không suy đoán loại phần thưởng từ lore ngoài gói.

### B09-F05 — vừa — sai trọng tâm của cách gọi lính trẻ em

- ID: `YS-LN02/Text/part0030.xhtml/p000279`.
- Vấn đề: “một đứa trẻ trong truyền thuyết tham gia quân ngũ” đặt tính truyền thuyết vào đứa trẻ và diễn đạt việc nhập ngũ. Nguồn đặt trọng tâm vào kiểu lính trẻ em được đồn kể; câu kế tiếp đối chiếu hình dung đó với cỗ máy chiến đấu.
- Đề xuất tạm: “Vậy là một lính trẻ em như trong truyền thuyết à?”. Phương án khác: “Vậy là lính trẻ em trong lời đồn à?”, tự nhiên hơn nhưng giảm sắc thái huyền thoại. Ưu tiên phương án đầu và khôi phục chữ nghiêng theo F01.
- Bất định: vừa về sắc thái lời đùa; thấp về việc cần giữ khái niệm lính trẻ em, không biến thành lai lịch huyền thoại của một cá nhân.

### B09-F06 — vừa — đại từ trần thuật lệch quy ước được bàn giao

- ID: `YS-LN02/Text/part0030.xhtml/p000274`, `YS-LN02/Text/part0030.xhtml/p000276`, `YS-LN02/Text/part0030.xhtml/p000278`, `YS-LN02/Text/part0030.xhtml/p000279`, `YS-LN02/Text/part0030.xhtml/p000281`.
- Vấn đề: các đoạn trần thuật gọi Tanya là “cô”. Handoff b09 viện dẫn DEC-P01-001; quyết định này dùng “nó” trong trần thuật ở giai đoạn được áp dụng. Không thấy đầu vào b09 cho phép một quy ước giai đoạn khác. Điểm nhìn gần vị tư lệnh không tự tạo ngoại lệ cho lời người kể.
- Đề xuất: dùng “nó” cho tựa chỉ Tanya ở phần trần thuật của các ID trên; có thể dùng chức danh khi câu cần tránh lặp. Riêng cách gọi bên trong lời đồn tại p000279 cần xét như lời được dẫn, không thay máy móc. Giữ “cô” trong lời thoại p000277 và xét riêng p000282 là nội tâm của vị tư lệnh. Không đổi nội tâm tự quy chiếu của Tanya tại p000268 thành “nó”.
- Bất định: vừa về giới hạn giai đoạn của DEC-P01-001; bằng chứng mạnh nhất trong phạm vi là chính handoff yêu cầu áp dụng. Nếu coordinator có ngoại lệ giai đoạn đã được duyệt, cần dẫn quyết định ấy khi xử lý; reviewer không tự tạo ngoại lệ hoặc quy ước canon mới.

### B09-F07 — nhẹ — đôi mắt bị quy thành không có cảm xúc

- ID: `YS-LN02/Text/part0030.xhtml/p000276`.
- Vấn đề: “vô cảm” nói về trạng thái cảm xúc, trong khi tính từ nguồn gợi sự vô cơ/phi nhân tính. Câu cuối lại nói cảm xúc trong đôi mắt ấy bộc lộ tất cả, khiến lựa chọn hiện tại tạo mâu thuẫn không cần thiết.
- Đề xuất tạm: “Đôi mắt lạnh như vật vô tri của nó…”. Phương án khác: “Đôi mắt như vô cơ…”, gần literal hơn nhưng gượng tiếng Việt. Không thêm màu sắc hay chẩn đoán tâm lý.
- Bất định: vừa; đây là hình ảnh văn chương, nên chọn cách giữ cảm giác phi nhân tính mà không xóa cảm xúc hiện diện ở câu cuối.

### B09-F08 — nhẹ — giảm mức độ xa lạ

- ID: `YS-LN02/Text/part0030.xhtml/p000274`.
- Vấn đề: “quả thực có phần xa lạ” vẫn nghiêng về mức độ nhẹ. Nguồn phủ nhận mức độ chỉ hơi xa lạ, chuẩn bị cho sự bất lực của cảm xúc ở p000275.
- Đề xuất: “pháp sư quả thực rất xa lạ” hoặc “pháp sư xa lạ hơn nhiều so với ông tưởng”. Ưu tiên phương án đầu vì phương án sau thêm đối chiếu với kỳ vọng.
- Bất định: thấp về mức độ, vừa về lựa chọn từ tự nhiên.

### B09-F09 — nhẹ — mất sắc thái chênh lệch cấp bậc

- ID: `YS-LN02/Text/part0030.xhtml/p000270`.
- Vấn đề: “một thiếu tá” bỏ sắc thái chỉ là một thiếu tá so với tư lệnh quân đoàn. “Đến gặp mình” ở đây quy chiếu tư lệnh, không phải Tanya, và không phải lỗi tự quy chiếu.
- Đề xuất: “triệu một sĩ quan chỉ mang hàm thiếu tá” hoặc “triệu một thiếu tá cấp dưới”. Ưu tiên phương án đầu để không thêm mô tả quan hệ biên chế.
- Bất định: thấp; không cần thay thuật ngữ tư lệnh quân đoàn.

### B09-F10 — nhẹ — diễn đạt giới hạn khả năng chưa rõ

- ID: `YS-LN02/Text/part0030.xhtml/p000271`.
- Vấn đề: “chỉ có thể xảy ra thôi” dễ nghe như nói về khả năng xảy ra nói chung; nguồn nhấn mạnh đây mới chỉ là một khả năng, chưa chắc sẽ xảy ra.
- Đề xuất: “Dù có bảo ông rằng đó mới chỉ là một khả năng, ông cũng chẳng thấy khá hơn.” Giữ lời trần thuật giả định, không biến thành lời đã nói với ông.
- Bất định: thấp.

### B09-F11 — nhẹ — tự quy chiếu nội tâm chưa nhất quán

- ID: `YS-LN02/Text/part0030.xhtml/p000258`.
- Vấn đề: gói không đặt đoạn này trong dấu thoại; lời tự quyết tiếp tục sau câu hỏi ở p000257 có căn cứ mạnh để đọc như nội tâm của người đang giải thích, phù hợp Tanya tại p000267–p000268. “Tôi” chưa nhất quán với “mình” được handoff áp dụng cho nội tâm Tanya.
- Đề xuất tạm: “Được phép nói tiếp thì mình cứ tiếp tục vậy.” Phương án ít suy diễn hơn: “Được phép nói tiếp thì cứ tiếp tục vậy”, lược chủ thể nhưng vẫn giữ quyết định chủ động. Ưu tiên “mình” theo mạch b09; không thêm dấu thoại.
- Bất định: vừa vì gói bắt đầu giữa cuộc trao đổi, không có nhãn người nói. Đây là đề xuất có giới hạn, không kết luận mọi câu ngôi thứ nhất đều phải đổi sang “mình”.

## Tám cụm pending được giao

Tất cả lựa chọn trong bảng là `pending/provisional_non_canon`. Không dùng cách dịch như chứng cứ rằng lập luận của Tanya hợp pháp trong thế giới thực.

| Cụm / ID trong b09 | Khuyến nghị tạm | Phương án khác | Căn cứ và bất định |
|---|---|---|---|
| `law of war` — p000260 | luật chiến tranh | luật về chiến tranh | Kế thừa lựa chọn b07, đúng mức khái quát của gói; không tự thay bằng tên một hệ thống điều ước hoặc lĩnh vực hẹp hơn. Bất định thấp về nghĩa, vừa về chuẩn hóa chuyên ngành. |
| `noncombatants` — p000260, p000262; quan hệ suy luận ở p000264 | người không tham chiến | người không trực tiếp tham chiến | Giữ tiêu chí tham chiến, phân biệt với “thường dân” tại p000261, p000264–p000265. p000264 không chứa thuật ngữ này trực tiếp: đây là quan hệ ngữ cảnh, không phải một lần xuất hiện. Phương án có “trực tiếp” thêm giới hạn chưa được gói nêu. Bất định thấp trong b09. |
| `sophistry` — p000259 | ngụy biện | lập luận ngụy biện | Giữ phán xét mỉa mai về kiểu tranh luận, không biến thành tên thủ tục pháp lý. “Một nửa là ngụy biện” tự nhiên trong giọng kể. Bất định thấp. |
| `militia` — p000264 | dân quân | thành viên lực lượng dân quân | Gói mô tả cách nhân vật giả định phân loại từng thường dân; dùng danh từ chỉ người như bản dịch hiện tại là phù hợp. Không tự thêm hệ thống dân quân tự vệ hay tư cách pháp lý được công nhận. Bất định vừa về tổ chức thực tế, thấp về cách dịch tại đây. |
| Ledger `Area Command`; gói `regional command` — p000277 | bộ chỉ huy khu vực | bộ tư lệnh khu vực | Ưu tiên cách gọi cơ quan chung theo từ thực tế trong gói. Không có căn cứ nhận đây là tên riêng hoặc một quân khu cụ thể. Viết thường tạm thời; “Bộ tư lệnh” có thể phù hợp nếu tổ chức được xác nhận sau. Bất định vừa về cấp tổ chức/tên riêng. |
| `army corps commander` — p000270, p000274 | tư lệnh quân đoàn | chỉ huy quân đoàn | Gói xác định quân đoàn, không phải quân đội nói chung; đây là chức vụ, không phải quân hàm. Không suy ra cấp tướng. Bất định thấp về cấp đơn vị, vừa về quy chuẩn chức danh. |
| Ledger `Silver Wings Assault Medal`; gói `Silver Wings Assault Badge` — p000279 | Huy hiệu Đột kích Cánh bạc | Huy hiệu Xung kích Cánh bạc | Theo loại vật phẩm thực tế trong gói; chưa có canon cho phép dùng “Huân chương”. “Đột kích” giữ lựa chọn đang dùng cho chức năng, “Xung kích” là phương án khác nếu hệ thống tên gọi về sau hỗ trợ. Bất định vừa về tên chính thức, thấp về việc phải phân biệt badge/medal. Liên quan F04. |
| Ledger `pacify the city`; gói `suppress` — p000283, p000284 | dẹp yên thành phố / dẹp yên Arene | bình định thành phố / bình định Arene | Gói nhấn mạnh trấn áp bất ổn để khôi phục khả năng dùng đường sắt. “Dẹp yên” tránh thêm hàm ý quản trị lâu dài, dùng được cả mệnh lệnh lẫn điều kiện hậu cần. “Bình định” hiện tại vẫn có thể chấp nhận trong ngữ cảnh quân sự, không tính thành lỗi riêng. Bất định vừa về sắc thái, không có bằng chứng để tự gọi mọi cư dân là mục tiêu. |

## Các lựa chọn liên quan self-check

- `small unit`, p000261: giữ tạm “một toán nhỏ”; phương án khác “một đơn vị nhỏ”. Không có bằng chứng về biên chế để chọn tiểu đội/trung đội. Bất định vừa về tổ chức, thấp về quy mô tương đối.
- `mage unit`, p000283: giữ tạm “đơn vị pháp sư”; phương án khác “đơn vị gồm các pháp sư”. Không thêm quy mô tiểu đoàn hay quân chủng. “Pháp sư/ma pháp” ở p000274–p000275, p000284 dùng nhất quán, vẫn là đề xuất.
- `Major`, p000270, p000272, p000276; `Lieutenant Colonel`, p000282: giữ tạm “thiếu tá” và “trung tá”, viết hoa khi gọi trực tiếp như bản dịch. Không đổi cấp bậc từ chức vụ tư lệnh. Bất định thấp về cách gọi thông thường, vừa về hệ thống quân hàm toàn tác phẩm; không nâng thành canon.
- `Foreign Office`, p000282: giữ tạm “Bộ Ngoại giao”; phương án khác “cơ quan ngoại giao”. Gói cho căn cứ cơ quan đối ngoại, chưa xác nhận mô hình tổ chức chính thức. Bất định vừa. “Loại bỏ” ở cùng đoạn giữ mở, không tự diễn giải thành ám sát.
- Tanya: giữ “mình” tại p000268; đề xuất “mình” tại p000258 theo F11. “Cô” trong thoại p000277 và nội tâm vị tư lệnh p000282 có thể giữ tạm; phương án thay thế trong nội tâm là “thiếu tá ấy”. Không áp quy tắc tự quy chiếu của Tanya cho người khác. Không đổi tên `Being X`, `von Degurechaff`, `von Lergen`, `Arene` khi chưa có canon mới.

## Đánh giá đủ 28 ID

Các nhận xét “đạt” dưới đây chỉ có nghĩa không phát hiện lỗi riêng ngoài finding được viện dẫn. Không coi thuật ngữ tạm là canon.

| Stable ID | Kết quả nghĩa / văn phong / điểm nhìn / nhấn mạnh |
|---|---|
| YS-LN02/Text/part0030.xhtml/p000257 | Đạt: giữ phản ứng nhận ra và câu hỏi yêu cầu tiếp tục. |
| YS-LN02/Text/part0030.xhtml/p000258 | F11: tự quy chiếu nội tâm cần nhất quán, chưa đủ căn cứ thêm dấu thoại. |
| YS-LN02/Text/part0030.xhtml/p000259 | Đạt: giữ hai vế mỉa mai và ảnh hưởng của cách mỗi nước diễn giải luật; “ngụy biện” phù hợp tạm. |
| YS-LN02/Text/part0030.xhtml/p000260 | Đạt: giữ nghĩa vụ của cả hai bên, kỳ vọng nỗ lực tối đa và ý định tận dụng tùy cách vận dụng. |
| YS-LN02/Text/part0030.xhtml/p000261 | Đạt: giữ giả định xâm nhập, bị bắn và tạo lý do; “cái cớ” có căn cứ trong giọng cơ hội pháp lý; không tự xác định quy mô toán. |
| YS-LN02/Text/part0030.xhtml/p000262 | Đạt: còn điều kiện ép bên kia tuyên bố không có người không tham chiến và hệ quả dỡ hạn chế; không biến thành thực trạng dân cư. |
| YS-LN02/Text/part0030.xhtml/p000263 | Đạt: giữ phản ứng ngạc nhiên ngắn. |
| YS-LN02/Text/part0030.xhtml/p000264 | F02: khôi phục điều kiện ở bước diễn giải; “dân quân”, “thường dân”, “quyền của tù binh” được phân biệt đúng, vẫn là lập luận của nhân vật. |
| YS-LN02/Text/part0030.xhtml/p000265 | F01, F03: giữ giả định và lời bình về bóp méo lý trí, sửa phương tiện sát thương và nhấn mạnh. Không xác minh hay bổ sung lịch sử ngoài gói. |
| YS-LN02/Text/part0030.xhtml/p000266 | Đạt: giữ hệ quả bóp méo công lý và công bằng. |
| YS-LN02/Text/part0030.xhtml/p000267 | Đạt: giữ sự thách thức, luật tồi vẫn là luật và mức phỏng đoán “có lẽ” về Being X. Không cần tự thêm “mình” khi không có tự quy chiếu. |
| YS-LN02/Text/part0030.xhtml/p000268 | Đạt: “mình”, người tốt và làm bổn phận giữ lời tự biện hộ của Tanya. |
| YS-LN02/Text/part0030.xhtml/p000269 | Đạt trong phạm vi: giữ Q.E.D. và dấu chú thích 19, nối lời tự chứng minh mỉa mai; không bịa nội dung chú thích. |
| YS-LN02/Text/part0030.xhtml/p000270 | F09: bổ sung sắc thái chỉ là thiếu tá; tư lệnh quân đoàn và khả năng phải triệu lại được giữ. |
| YS-LN02/Text/part0030.xhtml/p000271 | F10: làm rõ đây mới chỉ là một khả năng. |
| YS-LN02/Text/part0030.xhtml/p000272 | Chấp nhận tạm: “Chúc mừng” là chuyển lời mời vui mừng sang lời báo tin trong ngữ cảnh nhiệm vụ; “Hãy vui lên” sát lời hơn nhưng gượng. Không coi đây là việc nhận thưởng mới. |
| YS-LN02/Text/part0030.xhtml/p000273 | Đạt: lời đáp cấp dưới ngắn, không suy đoán quan hệ thân thuộc. |
| YS-LN02/Text/part0030.xhtml/p000274 | F06, F08: sửa đại từ trần thuật và mức xa lạ; giữ việc vị tư lệnh miễn cưỡng tiếp vì công việc. |
| YS-LN02/Text/part0030.xhtml/p000275 | Đạt: chủ thể là pháp sư nói chung; giữ khả năng tự bay, can thiệp bằng ma pháp và khoảng cách giữa hiểu lý trí với cảm xúc. |
| YS-LN02/Text/part0030.xhtml/p000276 | F01, F06, F07: giữ đối lập vẻ ngoài dịu dàng với bản chất bị tư lệnh nhìn nhận, sửa nhấn mạnh/đại từ/hình ảnh đôi mắt. |
| YS-LN02/Text/part0030.xhtml/p000277 | Đạt: giữ nhiệm vụ đặc biệt từ cơ quan khu vực; “cô” thuộc lời thoại được xét riêng. |
| YS-LN02/Text/part0030.xhtml/p000278 | F06 về đại từ; nghĩa được bổ nhiệm/phong hàm sĩ quan trước mười tuổi được giữ, không chỉ là nhập ngũ. |
| YS-LN02/Text/part0030.xhtml/p000279 | F01, F04, F05, F06: sửa nhấn mạnh, loại huy hiệu, cách gọi lính trẻ em và trần thuật. Cách nhìn được điều chỉnh không đồng nghĩa tư lệnh đã hiểu Tanya. |
| YS-LN02/Text/part0030.xhtml/p000280 | Đạt: giờ ban lệnh 14 giờ 22 được giữ chính xác. |
| YS-LN02/Text/part0030.xhtml/p000281 | F01, F06: giữ chuỗi huấn luyện thành tập kích ban đêm, thành tích và tỷ lệ tổn thất thấp hơn các đơn vị khác; sửa đại từ và nghiêng câu cuối. |
| YS-LN02/Text/part0030.xhtml/p000282 | F01: toàn đoạn là suy nghĩ vị tư lệnh; giữ nhận định không ai ngăn được và yếu tố pháp lý/ngoại giao với mức “có lẽ”. Không đổi “loại bỏ” thành giết. |
| YS-LN02/Text/part0030.xhtml/p000283 | Đạt về trình tự: xử lý đơn vị pháp sư địch, hội quân rồi dẹp yên thành phố; đề xuất thuật ngữ tạm như bảng. Không mở rộng mục tiêu mệnh lệnh. |
| YS-LN02/Text/part0030.xhtml/p000284 | Đạt: giữ pháp sư Cộng hòa qua mặt cảnh giới Đế quốc, bạo loạn du kích gia tăng và hai mắt xích không dẹp yên → không dùng đường sắt → hậu cần bị cắt. “Ta” không gây nhầm chủ thể trong ngữ cảnh này. |

Coordinator tiếp nhận lựa chọn tạm và giao người giữ quyền sửa xử lý các finding, sau đó kiểm tra lại đúng các ID liên quan. Reviewer không sửa bản dịch, self-check, canon, ledger hay handoff và không commit.
