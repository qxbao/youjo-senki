# Final signoff — vol-02-ch-06-b04-final-signoff

Vai trò: reviewer (Codex). **Signoff đạt trong phạm vi b04:** S01, M01–M04 và L01–L04 đã được xử lý. Số finding chưa xử lý chính xác: serious 0, moderate 0, minor 0; tổng 0. Không phát hiện finding tồn dư hoặc lỗi phát sinh từ các sửa được giao.

## Đầu vào và phạm vi

- Đã đọc `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff final-signoff, handoff review-fixes, review gốc, bản dịch hiện tại và self-check tương ứng. Đã đối chiếu các lựa chọn `chapter6_b04_coordinator_choices` và quy tắc canon về nhấn mạnh, giới hạn suy luận.
- Chỉ dùng nguồn từ `work/vol-02/batches/ch-06-b04-source.jsonl`. SHA-256 thực tế khớp handoff: `f667b42079f2a4e86e9c9461ac282ffbba00b3399f95fbf2f69e5bc798dd9308`.
- Package và bản dịch có cùng 38 ID, đúng thứ tự, từ `YS-LN02/Text/part0030.xhtml/p000094` đến `YS-LN02/Text/part0030.xhtml/p000131`. Đối chiếu các ID sửa với text/XHTML trong package và ngữ cảnh liền kề trong cùng gói.
- Không mở EPUB/PDF hoặc package khác. Không chép câu nguồn. Chỉ ghi báo cáo này; không sửa bản dịch, self-check, canon, ledger, handoff hay checkpoint. Không chạy graphify hoặc tạo dữ liệu graph vì nhiệm vụ chỉ cho phép ghi một báo cáo và đọc nguồn được giao.

## Kết quả theo stable ID

| Finding | Mức gốc | Segment ID | Kết quả đối chiếu bản hiện tại |
| --- | --- | --- | --- |
| S01 | serious | YS-LN02/Text/part0030.xhtml/p000129 | Đã xử lý. Điều kiện hợp lệ vẫn gắn với việc loại trừ sự hiện diện của người không tham chiến; phần kết tiếp tục phủ định đúng nhóm này. Không còn khẳng định không còn bất kỳ ai. Giữ ý lừa dối và nhận định của chuyên gia pháp lý, không thêm cơ chế sơ tán/tái phân loại hay thủ tục. |
| M01 | moderate | YS-LN02/Text/part0030.xhtml/p000094 | Đã xử lý. Dùng cách diễn đạt cô lập địch phía bắc, không gán riêng đường lui hoặc đường tiếp tế. |
| M02 | moderate | YS-LN02/Text/part0030.xhtml/p000097 | Đã xử lý. Chỉ câu rủa thầm về ngủ trưa được bọc Markdown chữ nghiêng; lời kể trước và hành động sau nằm ngoài phạm vi nhấn mạnh, khớp XHTML. |
| M03 | moderate | YS-LN02/Text/part0030.xhtml/p000103 | Đã xử lý. Dùng “Bộ phận Tác chiến”, bỏ cấp Cục suy diễn. Viết hoa hiện tại không xác lập cấp tổ chức hoặc tên canon. |
| M04 | moderate | YS-LN02/Text/part0030.xhtml/p000123 | Đã xử lý. Dùng “người không tham chiến”, giữ đây là giả định từ góc nhìn quân sự, với lực lượng địch vẫn hiện diện. Nhất quán với p000129. |
| L01 | minor | YS-LN02/Text/part0030.xhtml/p000101 | Đã xử lý. Dùng “dịch chuyển mặt trận”, giữ độ mở về hướng di chuyển, câu hỏi nội tâm và phạm vi chữ nghiêng. |
| L02 | minor | YS-LN02/Text/part0030.xhtml/p000104 | Đã xử lý. “Có thể giúp” giữ mức khả năng, không khẳng định chắc chắn hiệu quả của kế hoạch chuẩn bị trước. |
| L03 | minor | YS-LN02/Text/part0030.xhtml/p000121 | Đã xử lý. Diễn đạt việc không thể phí thêm thời gian tự nhiên; giữ toàn đoạn chữ nghiêng và dạng nội tâm, không biến thành lời nói. |
| L04 | minor | YS-LN02/Text/part0030.xhtml/p000126 | Đã xử lý. Cư dân là chủ thể; giữ thường dân khác dân quân và việc xác nhận dân cư khi chiếm Arene. |

Ở p000123–p000131, mạch lập luận vẫn phân biệt giả định pháp lý với thực tế dân cư. p000130 vẫn là câu hỏi phản ứng về hậu quả giết tất cả, không bị p000129 khẳng định trước thành kết quả tuyệt đối. Không suy diễn cách tạo điều kiện pháp lý hoặc quy định ngoài đời.

## Thuật ngữ: ba lựa chọn có nguồn vẫn pending/non-canon

| Source term | Segment ID | Giữ đề xuất tạm | Phương án khác và giới hạn |
| --- | --- | --- | --- |
| Worms Convention | YS-LN02/Text/part0030.xhtml/p000117 | Công ước Worms — pending, không canon | Hiệp ước Worms. Tên đầy đủ hiện diện trong package, đủ căn cứ cho cách dịch tại chỗ; không đồng nhất với hiệp ước ngoài đời hoặc WTN. |
| Feldgendarmerie | YS-LN02/Text/part0030.xhtml/p000095; YS-LN02/Text/part0030.xhtml/p000097 | Giữ Feldgendarmerie — pending, không canon | Hiến binh dã chiến. Cách giữ nguyên nhất quán, tránh gán cơ cấu chưa được giải thích; mức Việt hóa còn bất định. |
| war college | YS-LN02/Text/part0030.xhtml/p000113; YS-LN02/Text/part0030.xhtml/p000114 | Học viện Quân sự — pending, không canon | Học viện chiến tranh. Cách dùng hiện tại nhất quán, không thêm cấp học hoặc đối tượng đào tạo; tên chính thức và viết hoa chưa được chốt. |

Đã kiểm tra toàn bộ text và XHTML của 38 bản ghi: **WTN không xuất hiện**. Không xác nhận quan hệ đồng nghĩa hoặc khai triển giữa WTN và Worms Convention. Dùng tên đầy đủ ở p000117 không phải bằng chứng cho quan hệ viết tắt. Bất định này vẫn mở, không phải finding dịch chưa xử lý và không cần dừng signoff.

Coordinator/self-check còn nhắc Waldstätte Confederacy như một lựa chọn pending/non-canon. Không có căn cứ trong package b04 để thẩm định mục đó; không mở nguồn khác hoặc xác nhận cách dùng ngoài 38 ID. Ba lựa chọn có nguồn nêu trên và ghi chú WTN được đánh giá riêng, không coi con số pending_terms_count: 4 trong fix handoff là bốn lỗi tồn dư.

## Kết quả bàn giao

- Resolved: S01, M01, M02, M03, M04, L01, L02, L03, L04.
- Unresolved findings: `[]`.
- Unresolved counts: `{serious: 0, moderate: 0, minor: 0}`.
- Rủi ro còn mở: thuật ngữ vẫn là đề xuất; quan hệ WTN chưa đủ chứng cứ; mục Waldstätte ngoài package không được thẩm định. Không có hard stop được phát hiện trong phạm vi review này.
- Self-check/fix handoff ghi validator và diff-check pass của lượt sửa. Reviewer không chạy lại và không coi đó là kiểm tra do mình thực hiện: `validator: not_run`, `diff_check: not_run`, `commit: null`.
- Signoff này hoàn tất review được giao; không xác nhận bước commit hoặc nâng bản chuẩn của coordinator đã hoàn tất.
