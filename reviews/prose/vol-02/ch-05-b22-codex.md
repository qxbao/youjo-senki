# Review — vol-02-ch-05-b22

Đã đối chiếu đủ 22 đoạn với text và XHTML trong package được giao, bản dịch và self-check. Kết quả: 0 lỗi nghiêm trọng, 2 lỗi vừa, 6 lỗi nhẹ; cả 8 phát hiện đang mở vì reviewer không sửa bản dịch. `state: done` chỉ xác nhận hoàn tất review, không xác nhận lô đủ điều kiện nghiệm thu.

Đã đọc `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff review và batch, toàn bộ năm tệp canon, các mục ledger liên quan. Không truy cập EPUB/PDF, thư mục nguồn gốc hoặc package khác. Không chạy validator/diff-check; không commit.

## Đầu vào và tính toàn vẹn

- Package: `work/vol-02/batches/ch-05-b22-source.jsonl`.
- SHA-256 thực tế và handoff cùng là `5c946b229178eddc01eff2ddb38fe51890ea55436efb22c0f724fb313cb75f47`: khớp.
- Package và `translations/vol-02/ch-05-b22.jsonl` đều có 22 bản ghi; danh sách ID khớp hoàn toàn và đúng thứ tự p000566–p000587.
- `source_sha256` trong bản ghi là hash nguồn theo handoff batch, khác chức năng với hash của tệp package; không coi hai giá trị khác nhau này là lỗi.
- Self-check đã nhận diện ba nhóm thuật ngữ pending và nhấn mạnh p000576, nhưng bỏ sót nhấn mạnh p000571.

## Phát hiện và đề xuất xử lý

Mọi mã đoạn dưới đây có tiền tố ổn định `YS-LN02/Text/part0026.xhtml/`. Mã phát hiện giữ nguyên cho lượt sửa và tái kiểm tra.

### B22-CX-01 — nhẹ — p000566 — kết hợp từ và hình ảnh đình trệ

“Ngay cả riêng” nặng và trùng chức năng nhấn mạnh. “Đóng băng cứng” bám cấu trúc tiếng Anh, dễ khiến người đọc hiểu đường tuyến bị đông cứng theo nghĩa vật lý thay vì trạng thái mặt trận không tiến triển. Bối cảnh mùa đông hỗ trợ hình ảnh đóng băng, nhưng package chưa đủ để xác định chắc mọi tuyến mà đại từ đang chỉ tới.

Đề xuất: mở bằng “Chỉ riêng cụm tập đoàn quân tại chỗ cũng đủ…”; dùng “Có lẽ các tuyến này sẽ vẫn đóng băng cho đến mùa xuân năm sau.” Giữ đại từ trung tính, không tự xác định đó là riêng tuyến Rhine hay riêng mặt trận phía bắc. Giữ “cụm tập đoàn quân”: phù hợp đề xuất pending `vol02-ch02-b04-army-group` và `vol02-ch03-b05-northern-army-group`; không đổi cấp đơn vị chỉ để câu gọn hơn.

### B22-CX-02 — vừa — p000568 — thêm một phòng tuyến chưa được xác nhận

“Phá vỡ phòng tuyến trên eo biển” biến mục tiêu đột phá qua eo biển thành đánh vỡ một hệ thống phòng tuyến cụ thể. Nguồn không xác nhận phòng tuyến ấy; đoạn sau nói đến kiểm soát biển và phản ứng của Khối Thịnh vượng chung. Đây là bổ sung đối tượng quân sự, không chỉ là làm câu thuận hơn. Self-check cũng đang dựa vào cách hiểu phòng tuyến hải quân này.

Đề xuất: “Có vẻ hải quân nóng lòng muốn đột phá qua eo biển.” Giữ riêng bước tiêu diệt hạm đội và bước đổ bộ sau đó. Người sửa cập nhật nhận định tương ứng trong self-check; reviewer không sửa self-check.

### B22-CX-03 — nhẹ — p000569 — đại từ ở câu hỏi cuối dễ đổi chủ thể

“Họ” vừa chỉ lực lượng Đế quốc ở câu điều kiện, rồi lại dùng cho Khối Thịnh vượng chung ở câu hỏi cuối. Ngữ cảnh cho phép hiểu đúng, nhưng câu hỏi quyết định khả năng can thiệp nên cần chủ thể rõ.

Đề xuất: “Liệu Khối Thịnh vượng chung có chỉ đứng yên quan sát không?” Giữ đây là câu hỏi chưa có lời giải; không đổi thành khẳng định bên này chắc chắn sẽ can thiệp. Không thêm chữ nghiêng vì XHTML không nhấn mạnh câu này.

### B22-CX-04 — nhẹ — p000571 — mất nhấn mạnh đã được canon quy định

XHTML nhấn mạnh cụm nhận diện chiến tranh thế giới; bản dịch hiện không có Markdown tương ứng. Nội dung và khả thể ở phần còn lại vẫn đúng, nhưng mất nhịp nhấn khi nhận ra quy mô cuộc chiến, trái `DEC-P01-002`.

Đề xuất: “Phải, *chiến tranh thế giới*.” Chỉ đánh dấu cụm đó, không đánh dấu cả đoạn.

### B22-CX-05 — nhẹ — p000576 — sắc thái của lực lượng xen vào và đòn bên sườn

“Cường quốc ngoài cuộc” chỉ tình trạng chưa tham chiến, làm mờ ý một thế lực xen vào cuộc chiến. “Đánh úp” thêm sắc thái bất ngờ; căn cứ trong package xác nhận hướng đánh bên sườn nhưng không xác nhận yếu tố bất ngờ.

Đề xuất: “Họ cũng không thể chịu nổi ý nghĩ bị Khối Thịnh vượng chung hay một cường quốc khác xen vào cuộc chiến đánh từ bên sườn.” Có thể chỉnh trật tự câu cho nhẹ hơn nhưng phải giữ cả ý xen vào và hướng đánh. Câu hỏi nội tâm hiện giữ đúng đối tượng tình thế tiến thoái lưỡng nan và phạm vi chữ nghiêng; giữ nguyên phần ấy, không áp dụng quy ước đại từ Tanya cho Zettour.

### B22-CX-06 — vừa — p000578 — thêm lịch sử tái chiếm

“Giành lại” khẳng định quốc gia từng mất rồi thu hồi những vùng đất này. Nguồn chỉ xác nhận việc có được các vùng đất lịch sử, không xác nhận một chu kỳ mất–lấy lại. Tính chất “lịch sử” của vùng đất không đủ để bổ sung sự kiện tái chiếm. Trong đoạn nói về tranh chấp lãnh thổ, lựa chọn này dễ làm lệch cách hiểu lịch sử quốc gia.

Đề xuất: “Kể từ khi lập quốc, Đại Đế quốc đã có được những vùng đất lịch sử của mình, nhưng cũng luôn bị các tranh chấp lãnh thổ bủa vây…” Giữ “Đại Đế quốc” ở trạng thái pending theo khuyến nghị bên dưới; không suy ra quyền sở hữu chính đáng, biên giới cụ thể hay một quốc gia ngoài đời.

### B22-CX-07 — nhẹ — p000580 — cấu trúc bổ ngữ dịch sát gây vấp

“Đến một mức độ đáng ngạc nhiên đối với một quân nhân” đứng trước mệnh đề chính khiến mức độ niềm tin khó đọc. Ý đối lập giữa người làm quân sự và quan điểm không cần tấn công đã được giữ, không có lỗi điểm nhìn.

Đề xuất: “Zettour tin rằng họ không cần tấn công, với mức độ tin tưởng khá đáng ngạc nhiên ở một quân nhân.” Có thể viết trôi chảy hơn nhưng không biến thành ông ngạc nhiên về chính mình hoặc bỏ sắc thái mức độ. Giữ nhịp lặp “biết” và ý chỉ cần không thua ở đầu đoạn.

### B22-CX-08 — nhẹ — p000586 — thiếu danh từ trong lời thoại

“Một chuyển đổi mô thức” là kết hợp từ thiếu tự nhiên. Đây là lỗi câu tiếng Việt, không phải căn cứ đổi thuật ngữ pending đã dùng trong dự án.

Đề xuất: “Chúng ta cần một sự chuyển đổi mô thức.” Giữ “chuyển đổi mô thức” theo `P03-paradigm-shift`; không tự thêm chữ nghiêng, không diễn giải thành một học thuyết cụ thể.

## Phủ đủ 22 đoạn

| Mã đoạn | Kết quả đối chiếu nghĩa, văn phong, điểm nhìn, nhấn mạnh và nhất quán |
| --- | --- |
| p000566 | CX-01; giữ đúng ưu thế, thời tiết, khó điều quân và gánh tiếp tế; thuật ngữ đơn vị phù hợp pending. |
| p000567 | Không thấy lỗi cần sửa; giữ khác biệt lợi ích hải quân/lục quân và hỗ trợ theo yêu cầu. |
| p000568 | CX-02; trình tự hải chiến rồi đổ bộ và mục tiêu tiêu diệt vẫn được giữ. |
| p000569 | CX-03; nhận định Zettour, thương vong, an toàn đường biển và trung lập bề ngoài được giữ. |
| p000570 | Không thấy lỗi cần sửa; chủ thể Zettour–Rudersdorf rõ, khả năng can thiệp và cán cân quyền lực đúng; Thiếu tướng phù hợp ledger. Chưa suy ra hai nhan đề là tên văn kiện chính thức. |
| p000571 | CX-04; chuỗi mở rộng chiến tranh và khả thể nhiều mặt trận giống Rhine đúng. |
| p000572 | Không thấy lỗi cần sửa; đối thủ khó đối phó nhưng vẫn có cơ hội nếu chỉ đánh Cộng hòa. “Quân đội” được hiểu theo ngữ cảnh mặt trận bộ binh, không cần tự đổi tên lực lượng. |
| p000573 | Không thấy lỗi cần sửa; câu hỏi giả định và nguy cơ đảo chiều ưu thế được giữ. |
| p000574 | Không thấy lỗi cần sửa; giữ sự nghi ngờ năng lực ngăn hải quân đối phương và điều kiện tàn quân tham chiến. “Một khi” vẫn nằm trong kết cấu điều kiện, chưa khẳng định sự kiện đã xảy ra. |
| p000575 | Không thấy lỗi cần sửa; trì hoãn dẫn đến kiệt lực và mất tác dụng chiến lược của thắng lợi trước đúng. |
| p000576 | CX-05; câu hỏi nội tâm và nhấn mạnh đúng phạm vi. |
| p000577 | Không thấy lỗi cần sửa; giữ quan hệ dung chịu hiện trạng–rủi ro tiếp tế–thảm họa. |
| p000578 | CX-06; giữ tranh chấp lãnh thổ và mồi lửa chiến tranh; tên gọi còn pending. |
| p000579 | Không thấy lỗi cần sửa; giữ khổ tâm, lời giải đơn giản và những người biết kế hoạch; không tự chỉ định thêm người biết. |
| p000580 | CX-07; giữ quan điểm không cần tấn công, chỉ cần không thua của Zettour. |
| p000581 | Không thấy lỗi cần sửa; Rudersdorf đồng ý không cần công kích lớn nhưng không chấp nhận tiêu hao; giữ điều kiện kiểm soát tổn thất và thắng. |
| p000582 | Không thấy lỗi cần sửa; quyết định của cả hai và việc được phép phát biểu đúng. |
| p000583 | Không thấy lỗi cần sửa; lời đề nghị đổi cách nhìn, xưng tôi/chúng ta phù hợp ngữ cảnh. |
| p000584 | Không thấy lỗi cần sửa; giữ tự đánh giá, lo lắng, giọng hơi cứng và mức độ khó nhận ra. |
| p000585 | Không thấy lỗi cần sửa; giữ giải pháp một nhát, hậu quả đẫm máu và hình ảnh Gordian; không tự giải thích thêm điển tích hoặc đối tượng bị chém. |
| p000586 | CX-08; giữ học thuyết/giá trị hiện tại, mức phỏng đoán và yêu cầu đổi mô thức; không có nhấn mạnh nguồn. |
| p000587 | Không thấy lỗi cần sửa; giữ bất khả thi của cách thắng cũ, ngoại lệ chênh lệch quốc lực và chiến tranh đến kiệt sức. |

## Lựa chọn thuật ngữ tạm

1. **amphibious operation / landing operation**: giữ “chiến dịch đổ bộ đường biển” ở p000568 và “đổ bộ” trong cấu trúc chỉ mục đích ở p000569. “Chiến dịch đổ bộ / cuộc đổ bộ” là phương án ngắn hơn đã có trong ledger; “chiến dịch đổ bộ đường biển / chiến dịch đổ bộ” là phương án giữ danh từ chỉ hoạt động ở cả hai nơi. Đề xuất b22 làm rõ phương thức biển, tương thích với `vol02-ch03-b08-airborne-amphibious` và b14 phân biệt đột kích đường không/nhảy dù. Khác biệt hai từ nguồn trong package này chưa đủ để xác lập hai cấp tổ chức tác chiến khác nhau. Không coi phần “đường biển” là thuật ngữ mới đã chốt.
2. **Great Reich**: tạm giữ “Đại Đế quốc” như đề xuất b22, có thể thay bằng “Đế quốc Vĩ đại” hoặc giữ “Great Reich” nếu cần giữ định danh. “Đại Đế quốc” giữ yếu tố chỉ quy mô/tôn xưng và nối với “Đế quốc” đang dùng; “Đế quốc Vĩ đại” thiên về lời ca ngợi, còn giữ nguyên tiếng nước ngoài giảm diễn giải nhưng làm câu Việt kém liền mạch. Package chưa đủ xác nhận tên hiến định, sắc thái chính trị hay sự khác biệt thực thể với Empire. Độ tin cậy trung bình; tiếp tục bằng lựa chọn tạm, không cần dừng hỏi canon.
3. **paradigm shift**: giữ “chuyển đổi mô thức” theo `P03-paradigm-shift` và đề xuất b22. “Thay đổi hệ hình” là phương án đã có trong glossary-pending; “sự thay đổi mô thức” và “bước ngoặt mô hình” có trong ledger b22. Ngữ cảnh đòi thay căn bản cách nhìn, học thuyết và giá trị, nên “chuyển đổi mô thức” sát hơn một thay đổi chiến thuật đơn lẻ. Chỉ sửa ngữ pháp thành “một sự chuyển đổi mô thức”; không nâng lựa chọn thành canon.

Các ánh xạ “cụm tập đoàn quân”, “Thiếu tướng”, “Khối Thịnh vượng chung”, “chiến tranh tổng lực” đã được đối chiếu ledger và vẫn là pending. Glossary/characters chính thức chưa có mục chốt; chỉ các quy tắc trong decisions có trạng thái đã duyệt.

```yaml
role: reviewer
reviewer: codex
task_id: vol-02-ch-05-b22-review
state: done
report_path: reviews/prose/vol-02/ch-05-b22-codex.md
review_path: reviews/prose/vol-02/ch-05-b22-codex.md
files_written:
  - reviews/prose/vol-02/ch-05-b22-codex.md
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000566
  - YS-LN02/Text/part0026.xhtml/p000567
  - YS-LN02/Text/part0026.xhtml/p000568
  - YS-LN02/Text/part0026.xhtml/p000569
  - YS-LN02/Text/part0026.xhtml/p000570
  - YS-LN02/Text/part0026.xhtml/p000571
  - YS-LN02/Text/part0026.xhtml/p000572
  - YS-LN02/Text/part0026.xhtml/p000573
  - YS-LN02/Text/part0026.xhtml/p000574
  - YS-LN02/Text/part0026.xhtml/p000575
  - YS-LN02/Text/part0026.xhtml/p000576
  - YS-LN02/Text/part0026.xhtml/p000577
  - YS-LN02/Text/part0026.xhtml/p000578
  - YS-LN02/Text/part0026.xhtml/p000579
  - YS-LN02/Text/part0026.xhtml/p000580
  - YS-LN02/Text/part0026.xhtml/p000581
  - YS-LN02/Text/part0026.xhtml/p000582
  - YS-LN02/Text/part0026.xhtml/p000583
  - YS-LN02/Text/part0026.xhtml/p000584
  - YS-LN02/Text/part0026.xhtml/p000585
  - YS-LN02/Text/part0026.xhtml/p000586
  - YS-LN02/Text/part0026.xhtml/p000587
counts:
  serious: 0
  moderate: 2
  minor: 6
findings:
  - id: B22-CX-01
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000566
    issue: Cấu trúc nhấn mạnh nặng và hình ảnh đóng băng dịch sát.
    resolution: Dùng chỉ riêng và vẫn đóng băng; giữ đại từ trung tính và thuật ngữ đơn vị pending.
  - id: B22-CX-02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000568
    issue: Thêm phòng tuyến cụ thể không được package xác nhận.
    resolution: Dùng đột phá qua eo biển; người sửa điều chỉnh self-check tương ứng.
  - id: B22-CX-03
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000569
    issue: Đại từ câu hỏi cuối dễ lẫn chủ thể.
    resolution: Gọi rõ Khối Thịnh vượng chung; giữ câu hỏi chưa có lời giải.
  - id: B22-CX-04
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000571
    issue: Mất nhấn mạnh cụm chiến tranh thế giới theo DEC-P01-002.
    resolution: Đặt Markdown chữ nghiêng đúng riêng cụm chiến tranh thế giới.
  - id: B22-CX-05
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000576
    issue: Mờ ý thế lực xen vào và thêm sắc thái đánh bất ngờ.
    resolution: Dùng cường quốc khác xen vào cuộc chiến và đánh từ bên sườn; giữ câu hỏi nghiêng.
  - id: B22-CX-06
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000578
    issue: Giành lại thêm lịch sử mất đất rồi tái chiếm.
    resolution: Dùng có được những vùng đất lịch sử; giữ Đại Đế quốc pending.
  - id: B22-CX-07
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000580
    issue: Bổ ngữ mức độ đặt đầu câu gây vấp.
    resolution: Đưa mức độ tin tưởng sau mệnh đề niềm tin; giữ đối lập với tư cách quân nhân.
  - id: B22-CX-08
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000586
    issue: Một chuyển đổi mô thức thiếu tự nhiên trong lời thoại.
    resolution: Dùng một sự chuyển đổi mô thức; giữ thuật ngữ pending và không thêm chữ nghiêng.
unresolved_findings:
  - B22-CX-01
  - B22-CX-02
  - B22-CX-03
  - B22-CX-04
  - B22-CX-05
  - B22-CX-06
  - B22-CX-07
  - B22-CX-08
term_recommendations:
  - id: B22-CX-T01
    source_term: amphibious operation / landing operation
    proposed_vi: chiến dịch đổ bộ đường biển / đổ bộ
    alternatives:
      - chiến dịch đổ bộ / cuộc đổ bộ
      - chiến dịch đổ bộ đường biển / chiến dịch đổ bộ
    rationale: Giữ đề xuất b22, tương thích pending b08 và b14 phân biệt tác chiến đường không; phương thức biển rõ trong package, chưa đủ chứng cứ chia hai cấp tác chiến.
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000568
      - YS-LN02/Text/part0026.xhtml/p000569
    status: pending
  - id: B22-CX-T02
    source_term: Great Reich
    proposed_vi: Đại Đế quốc
    alternatives:
      - Đế quốc Vĩ đại
      - Great Reich
    rationale: Giữ đề xuất b22 và liên hệ cách gọi Đế quốc; phương án Vĩ đại thiên về ca ngợi, giữ nguyên làm câu kém liền mạch; chưa xác nhận tên chính thức hoặc khác biệt thực thể.
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000578
    status: pending
  - id: B22-CX-T03
    source_term: paradigm shift
    proposed_vi: chuyển đổi mô thức
    alternatives:
      - thay đổi hệ hình
      - sự thay đổi mô thức
      - bước ngoặt mô hình
    rationale: Kế thừa P03-paradigm-shift và ledger b22; phù hợp yêu cầu thay căn bản cách nhìn cùng học thuyết và giá trị; chỉ bổ sung sự cho ngữ pháp câu.
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000586
    status: pending
risks:
  - Hai lỗi vừa còn mở; lô cần được người giữ quyền sửa xử lý trước nghiệm thu.
  - Great Reich chưa xác nhận là danh xưng chính thức; không suy luận lore hoặc quốc gia ngoài đời.
  - Tham chiếu các tuyến ở p000566 chưa hoàn toàn rõ trong package; giữ diễn đạt trung tính, không mở nguồn ngoài phạm vi.
  - Tên gọi và quân hàm trong ledger vẫn là đề xuất, không được coi là canon.
package_hash_check:
  path: work/vol-02/batches/ch-05-b22-source.jsonl
  algorithm: sha256
  expected: 5c946b229178eddc01eff2ddb38fe51890ea55436efb22c0f724fb313cb75f47
  actual: 5c946b229178eddc01eff2ddb38fe51890ea55436efb22c0f724fb313cb75f47
  status: pass
  source_unit_count: 22
  translation_unit_count: 22
  segment_ids_match: true
validator: not_run
diff_check: not_run
commit: null
next_action: Coordinator ghi khuyến nghị pending vào ledger và handoff; giao người giữ quyền sửa xử lý CX-01 đến CX-08, cập nhật self-check rồi tái kiểm tra và chạy các kiểm tra bắt buộc.
```
