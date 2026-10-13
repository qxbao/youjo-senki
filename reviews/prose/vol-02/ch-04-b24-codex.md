# Review vol-02-ch-04-b24

Đã đối chiếu 32 đoạn từ `YS-LN02/Text/part0024.xhtml/p000381` đến `YS-LN02/Text/part0024.xhtml/p000412`. Chỉ dùng các đầu vào được giao; phần ledger được xét duy nhất là `chapter4_b24_translation_proposals`. Hash gói nguồn và năm tài liệu canon khớp handoff. Không mở nguồn sách, lô khác hoặc báo cáo khác; không chạy worker. Bằng chứng dưới đây diễn giải nghĩa và cấu trúc nguồn, không trích văn bản nguồn.

Chưa thấy thiếu cả đoạn hay đảo phủ định/quan hệ nhân quả lớn. Mạch tự biện hộ, lo bị xem là cấp dưới tự tiện, rồi chuyển sang nhiệm vụ hải quân nhìn chung còn rõ. Các vấn đề nghĩa, giọng và định dạng cần xử lý được ghi riêng dưới đây. Đề xuất thuật ngữ không phải quyết định canon.

## Findings

### B24-R01 — moderate — Đại từ trần thuật

- **Segment ID:** `YS-LN02/Text/part0024.xhtml/p000388`, `YS-LN02/Text/part0024.xhtml/p000399`, `YS-LN02/Text/part0024.xhtml/p000411`, `YS-LN02/Text/part0024.xhtml/p000412`.
- **Bằng chứng:** Bản dịch dùng “cô” ở lời kể về Tanya, trong khi DEC-P01-001 và checkpoint của handoff yêu cầu phân biệt “nó” trong trần thuật với “mình” trong nội tâm. p000388 có chuyển từ lời kể sang nội tâm ngay trong cùng đoạn; p000412 cũng xen hai lớp này.
- **Đề nghị:** Đổi các đại từ trần thuật về Tanya thành “nó”; giữ “mình” ở phần tự quy chiếu nội tâm. Có thể lược đại từ khi câu vẫn rõ chủ thể, nhưng không đổi đại từ tập thể trong hai câu nội tâm p000412.
- **Trạng thái:** unresolved; áp dụng quyết định đã duyệt, không tạo quy ước mới.

### B24-R02 — moderate — Mất phạm vi nhấn mạnh

- **Segment ID:** `YS-LN02/Text/part0024.xhtml/p000403`.
- **Bằng chứng:** XHTML đánh dấu nhấn mạnh liên tục cho câu hỏi than thở và lời tự trả lời quy nguyên nhân về Being X. Bản dịch để toàn bộ phần này ở dạng thường. Lời kể “Tanya than thở” nằm ngoài phạm vi nhấn mạnh của nguồn.
- **Đề nghị:** Bọc bằng `*...*` từ “Tại sao chuyện này lại xảy ra cơ chứ?” đến hết “Being X”; để “Tanya than thở” và câu suy xét Tsuji ngoài dấu nhấn mạnh. p000387 và hai phạm vi nhấn mạnh ở p000412 đã tương ứng với nguồn.
- **Trạng thái:** unresolved; theo DEC-P01-002.

### B24-R03 — moderate — Tự thu hẹp địa danh thành con sông

- **Segment ID:** `YS-LN02/Text/part0024.xhtml/p000397`, `YS-LN02/Text/part0024.xhtml/p000400`.
- **Bằng chứng:** Nguồn dùng Rhine như đích điều chuyển, rồi nói đến việc quét chiến trường ở p000401; không xác định nhiệm vụ trên một con sông. Bản dịch thêm “sông” vào cả lời thông báo lẫn lời nhắc lại, làm đích quân sự bị hiểu hẹp đi.
- **Lựa chọn tạm tốt nhất:** Giữ “Rhine” ở cả hai đoạn, kể cả lần nhấn lại trong p000397.
- **Thay thế và lý do:** “Mặt trận Rhine” phù hợp mạch chiến trường nhưng thêm phân loại chưa được nêu trực tiếp; “khu vực Rhine” trung tính hơn nhưng vẫn thêm danh từ. Giữ tên trần là phương án ít suy diễn nhất trong phạm vi này.
- **Trạng thái:** unresolved; chưa chốt loại địa danh thành canon.

### B24-R04 — moderate — Mờ đối lập lục quân/hải quân

- **Segment ID:** `YS-LN02/Text/part0024.xhtml/p000407`.
- **Bằng chứng:** Đoạn so sánh hai lực lượng về suất ăn, chi tiêu và phúc lợi. Bản dịch đối chiếu “hải quân” với “quân đội”, khiến một quân chủng bị so với toàn bộ tổ chức bao gồm chính nó; chuỗi bên phê bình/bên bị phê bình vì thế thiếu chính xác.
- **Lựa chọn tạm tốt nhất:** Dùng “lục quân” cho phía đối chiếu với hải quân xuyên suốt p000407.
- **Thay thế và lý do:** “Bên lục quân” tự nhiên ở giọng kể khẩu ngữ; “quân đội” chỉ phù hợp nghĩa chung ở nơi khác. Không cần thay hàng loạt các lần dùng “quân đội” trong lô khi chúng nói về thiết chế quân sự nói chung.
- **Trạng thái:** unresolved; lựa chọn theo ngữ cảnh, không bổ sung canon.

### B24-R05 — moderate — Đội hình đánh chiếm tàu bị chuyển sang đổ bộ

- **Segment ID:** `YS-LN02/Text/part0024.xhtml/p000411`.
- **Bằng chứng:** Nhãn đội hình gắn với hành động lên tàu để tấn công; phần triển khai mô tả bay sát mặt nước, giữ tốc độ và lao vào mục tiêu, trong bối cảnh hỗ trợ hạm đội ở p000409. “Đội hình đột kích đổ bộ” dễ khiến người đọc hình dung đổ quân lên bờ và không giữ được nét nghĩa lên tàu.
- **Lựa chọn tạm tốt nhất:** “Đội hình đột kích lên tàu”.
- **Thay thế và lý do:** “Đội hình tấn công lên tàu” sát nghĩa, ít sắc thái hơn; “đội hình đánh chiếm tàu” rõ mục đích nhưng diễn giải thêm kết quả mong muốn. Hai phương án ledger cùng dùng “đổ bộ” đều chưa giải quyết nét nghĩa bị mất. Chưa đủ căn cứ để xác định quy trình kỹ thuật hay loại tàu; không thêm những chi tiết ấy.
- **Trạng thái:** unresolved; đồng thời là khuyến nghị cho pending `vol02-ch04-b24-boarding-assault-formation`, không tính hai lỗi riêng.

### B24-R06 — moderate — Câu hỏi về việc khai hỏa dễ thành câu hỏi về đạn thật

- **Segment ID:** `YS-LN02/Text/part0024.xhtml/p000412`.
- **Bằng chứng:** Tanya kinh ngạc vì hỏa lực đánh chặn quá yếu so với điều được báo trước. Câu hỏi nhằm xác nhận phía kia có đang bắn hay không. “Họ đang bắn thật đấy à?” trong ngữ cảnh diễn tập dễ được hiểu là ngạc nhiên vì họ dùng đạn thật hoặc thực sự bắn, trái hướng với nỗi lo thiếu đánh chặn.
- **Lựa chọn tạm tốt nhất:** “Họ có đang bắn không vậy?”; giữ chữ nghiêng như hiện tại.
- **Thay thế và lý do:** “Họ có bắn không đấy?” tự nhiên và giữ hướng nghi vấn nhưng kém rõ thời đang diễn ra. Không thêm “đạn thật”. Câu kỳ vọng kế tiếp có thể giữ, vì nguồn cũng thể hiện sự tin chắc rằng đối phương sẽ khai hỏa dù đang diễn tập.
- **Trạng thái:** unresolved.

### B24-R07 — minor — Làm nhạt ẩn dụ công cụ bạo lực

- **Segment ID:** `YS-LN02/Text/part0024.xhtml/p000389`, `YS-LN02/Text/part0024.xhtml/p000390`.
- **Bằng chứng:** Nguồn dùng hình ảnh con vật canh giữ để nói về quân đội chịu sự kiểm soát của nhà nước, rồi nối sang lũ chuột và việc truy đuổi ở p000392. “Người canh giữ” giữ chức năng bảo vệ nhưng thay hình ảnh và làm nhẹ giọng tự mô tả lạnh lùng của Tanya; “người canh giữ của họ” cũng khiến đại từ chỉ Đế quốc hơi gượng.
- **Lựa chọn tạm tốt nhất:** “Chó canh” ở cả hai đoạn; p000389 có thể dùng “con chó canh của Đế quốc”.
- **Thay thế và lý do:** “Chó giữ nhà” tự nhiên nhưng thêm sắc thái gia đình; “lực lượng canh giữ” trung tính song tiếp tục mất ẩn dụ. Chỉ dùng hình ảnh này đúng hai chỗ tương ứng, không thêm miệt thị vào chỗ khác.
- **Trạng thái:** unresolved; đề xuất về giọng và hình ảnh, không chốt thuật ngữ.

### B24-R08 — minor — Biểu cảm bị đổi và tốc độ được thêm

- **Segment ID:** `YS-LN02/Text/part0024.xhtml/p000411`.
- **Bằng chứng:** Nguồn mô tả biểu cảm cau có trước nước bắn; “nheo mắt” chuyển thành phản ứng thị giác. Câu cuối xác định các đại đội đều vào đội hình hỗ trợ nhau, không nêu tốc độ “nhanh chóng”.
- **Đề nghị:** Dùng “Cau mày trước những đợt nước bắn…” và bỏ “nhanh chóng”; có thể dùng “các đại đội đều vào đội hình hỗ trợ lẫn nhau” để giữ phạm vi toàn thể.
- **Trạng thái:** unresolved; không ảnh hưởng cấu trúc chiến thuật bằng R05.

### B24-R09 — minor — Lời tuyên bố bớt sắc thái bất chấp

- **Segment ID:** `YS-LN02/Text/part0024.xhtml/p000382`.
- **Bằng chứng:** Nguồn mở lời bằng thái độ không bận tâm nơi đến có khắc nghiệt đến đâu, rồi khẳng định sẽ đi và chinh phục. “Dù nơi đó có là luyện ngục…” giữ điều kiện nhưng giảm nét bất chấp trực tiếp của người chỉ huy.
- **Đề nghị:** Có thể mở bằng “Ta chẳng quan tâm nơi đó có là luyện ngục…” rồi giữ phần tuyên bố tập thể hiện tại. Nếu tránh chuyển đại từ thoại khi chưa đủ căn cứ, “Có là luyện ngục cũng chẳng sao…” là phương án tự nhiên, ít suy diễn hơn.
- **Lựa chọn tạm tốt nhất:** “Có là luyện ngục cũng chẳng sao…”, giữ cách xưng tập thể “chúng ta” trong phần tiếp theo.
- **Trạng thái:** unresolved; mức nhẹ, không phải đảo nghĩa.

## Ba mục pending

1. **`vol02-ch04-b24-heinrichs-law` — `YS-LN02/Text/part0024.xhtml/p000383`:** Giữ tạm **“Định luật Heinrich”**. Đoạn dùng tên nguyên tắc như lời cảnh báo không để lỗi nhỏ tích tụ; không có canon phủ định phương án ledger. **“Quy luật Heinrich”** là lựa chọn thay thế nếu về sau dự án thống nhất cách gọi các nguyên tắc kinh nghiệm. Độ tin cậy vừa; không suy ra công thức, tỷ lệ hoặc cơ chế ngoài đoạn. Cách diễn giải hậu quả lớn trong bản dịch nhìn chung phù hợp ý cảnh báo, nhưng có thể rút sát hơn thành “cảnh báo không nên để những sai sót nhỏ tích tụ”. Không tính thành lỗi độc lập.
2. **`vol02-ch04-b24-marine-mages` — `YS-LN02/Text/part0024.xhtml/p000406`:** Giữ tạm **“pháp sư hải quân”**. Các đoạn p000406–p000409 liên tục gắn hoạt động với hải quân, suất ăn và hạm đội, nên đây là phương án có căn cứ tại chỗ tốt nhất. **“Pháp sư tác chiến trên biển”** là phương án trung tính nếu cần tránh khẳng định biên chế; **“pháp sư thủy quân lục chiến”** chỉ phù hợp khi có bằng chứng về một lực lượng riêng, hiện chưa có trong đầu vào được phép. Độ tin cậy thấp đến vừa: b24 không đủ xác nhận tổ chức hay so sánh với lô trước, và lời dẫn ledger về sự nhất quán trước đó chưa được kiểm chứng ở lần review này. Chưa xác lập đây là tên quân chủng.
3. **`vol02-ch04-b24-boarding-assault-formation` — `YS-LN02/Text/part0024.xhtml/p000411`:** Đề xuất thay bằng **“đội hình đột kích lên tàu”** theo R05; thay thế **“đội hình tấn công lên tàu”**, **“đội hình đánh chiếm tàu”**. Độ tin cậy vừa đến cao cho nét nghĩa lên tàu, vừa cho tên đội hình tiếng Việt. Không xem lựa chọn ledger là canon và không tự sửa ledger.

## Tổng kết bàn giao

```yaml
role: reviewer
task_id: vol-02-ch-04-b24
state: done
segment_ids:
  - YS-LN02/Text/part0024.xhtml/p000381
  - YS-LN02/Text/part0024.xhtml/p000382
  - YS-LN02/Text/part0024.xhtml/p000383
  - YS-LN02/Text/part0024.xhtml/p000384
  - YS-LN02/Text/part0024.xhtml/p000385
  - YS-LN02/Text/part0024.xhtml/p000386
  - YS-LN02/Text/part0024.xhtml/p000387
  - YS-LN02/Text/part0024.xhtml/p000388
  - YS-LN02/Text/part0024.xhtml/p000389
  - YS-LN02/Text/part0024.xhtml/p000390
  - YS-LN02/Text/part0024.xhtml/p000391
  - YS-LN02/Text/part0024.xhtml/p000392
  - YS-LN02/Text/part0024.xhtml/p000393
  - YS-LN02/Text/part0024.xhtml/p000394
  - YS-LN02/Text/part0024.xhtml/p000395
  - YS-LN02/Text/part0024.xhtml/p000396
  - YS-LN02/Text/part0024.xhtml/p000397
  - YS-LN02/Text/part0024.xhtml/p000398
  - YS-LN02/Text/part0024.xhtml/p000399
  - YS-LN02/Text/part0024.xhtml/p000400
  - YS-LN02/Text/part0024.xhtml/p000401
  - YS-LN02/Text/part0024.xhtml/p000402
  - YS-LN02/Text/part0024.xhtml/p000403
  - YS-LN02/Text/part0024.xhtml/p000404
  - YS-LN02/Text/part0024.xhtml/p000405
  - YS-LN02/Text/part0024.xhtml/p000406
  - YS-LN02/Text/part0024.xhtml/p000407
  - YS-LN02/Text/part0024.xhtml/p000408
  - YS-LN02/Text/part0024.xhtml/p000409
  - YS-LN02/Text/part0024.xhtml/p000410
  - YS-LN02/Text/part0024.xhtml/p000411
  - YS-LN02/Text/part0024.xhtml/p000412
files_written: [reviews/prose/vol-02/ch-04-b24-codex.md]
review_path: reviews/prose/vol-02/ch-04-b24-codex.md
validator: not_run
diff_check: not_run
counts:
  segments_reviewed: 32
  serious: 0
  moderate: 6
  minor: 3
  total_findings: 9
  pending_terms_reviewed: 3
findings:
  - {id: B24-R01, severity: moderate, segment_id: YS-LN02/Text/part0024.xhtml/p000388, issue: Đại từ trần thuật không theo DEC-P01-001, resolution: proposed}
  - {id: B24-R02, severity: moderate, segment_id: YS-LN02/Text/part0024.xhtml/p000403, issue: Mất nhấn mạnh nội tâm, resolution: proposed}
  - {id: B24-R03, severity: moderate, segment_id: YS-LN02/Text/part0024.xhtml/p000397, issue: Thêm phân loại sông vào Rhine, resolution: proposed}
  - {id: B24-R04, severity: moderate, segment_id: YS-LN02/Text/part0024.xhtml/p000407, issue: Mờ đối lập lục quân và hải quân, resolution: proposed}
  - {id: B24-R05, severity: moderate, segment_id: YS-LN02/Text/part0024.xhtml/p000411, issue: Mất nét nghĩa đột kích lên tàu, resolution: proposed}
  - {id: B24-R06, severity: moderate, segment_id: YS-LN02/Text/part0024.xhtml/p000412, issue: Câu hỏi khai hỏa dễ bị hiểu thành bắn đạn thật, resolution: proposed}
  - {id: B24-R07, severity: minor, segment_id: YS-LN02/Text/part0024.xhtml/p000389, issue: Làm nhạt ẩn dụ chó canh, resolution: proposed}
  - {id: B24-R08, severity: minor, segment_id: YS-LN02/Text/part0024.xhtml/p000411, issue: Đổi biểu cảm và thêm tốc độ, resolution: proposed}
  - {id: B24-R09, severity: minor, segment_id: YS-LN02/Text/part0024.xhtml/p000382, issue: Giảm sắc thái bất chấp trong lời tuyên bố, resolution: proposed}
unresolved_findings: [B24-R01, B24-R02, B24-R03, B24-R04, B24-R05, B24-R06, B24-R07, B24-R08, B24-R09]
term_recommendations:
  - {id: vol02-ch04-b24-heinrichs-law, proposed_vi: Định luật Heinrich, status: pending, action: retain_provisional}
  - {id: vol02-ch04-b24-marine-mages, proposed_vi: pháp sư hải quân, status: pending, action: retain_provisional}
  - {id: vol02-ch04-b24-boarding-assault-formation, proposed_vi: đội hình đột kích lên tàu, status: pending, action: revise_provisional}
pending_terms: [] # Không phát sinh mục ledger mới; các lựa chọn tạm khác có lý do ở findings.
risks:
  - Còn sáu finding moderate; lô chưa đủ điều kiện hoàn tất pipeline.
  - Chưa xác nhận biên chế của nhóm pháp sư trong phạm vi b24.
  - Chỉ đánh giá nhất quán nội bộ b24 và canon được giao; chưa kiểm chứng sự nhất quán với lô khác.
  - Các phương án thuật ngữ và địa danh vẫn là đề xuất; không tự nâng thành canon.
commit: null
next_action: coordinator_receive_report_record_provisional_choices_then_assign_authorized_translation_revision_and_targeted_recheck
```
