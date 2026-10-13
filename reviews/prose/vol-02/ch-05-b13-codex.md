# Review — vol-02-ch-05-b13

Đã đối chiếu cả 20 đoạn p000313–p000332 với gói nguồn được giao, bản dịch, self-check, canon và các lựa chọn pending liên quan. SHA-256 khớp handoff; đủ mã đoạn và đúng thứ tự. Báo cáo không chứa câu nguồn. Các lựa chọn thuật ngữ dưới đây chỉ là đề xuất tạm, không phải canon.

```yaml
role: reviewer
task_id: vol-02-ch-05-b13-review
state: done
review_path: reviews/prose/vol-02/ch-05-b13-codex.md
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000313
  - YS-LN02/Text/part0026.xhtml/p000314
  - YS-LN02/Text/part0026.xhtml/p000315
  - YS-LN02/Text/part0026.xhtml/p000316
  - YS-LN02/Text/part0026.xhtml/p000317
  - YS-LN02/Text/part0026.xhtml/p000318
  - YS-LN02/Text/part0026.xhtml/p000319
  - YS-LN02/Text/part0026.xhtml/p000320
  - YS-LN02/Text/part0026.xhtml/p000321
  - YS-LN02/Text/part0026.xhtml/p000322
  - YS-LN02/Text/part0026.xhtml/p000323
  - YS-LN02/Text/part0026.xhtml/p000324
  - YS-LN02/Text/part0026.xhtml/p000325
  - YS-LN02/Text/part0026.xhtml/p000326
  - YS-LN02/Text/part0026.xhtml/p000327
  - YS-LN02/Text/part0026.xhtml/p000328
  - YS-LN02/Text/part0026.xhtml/p000329
  - YS-LN02/Text/part0026.xhtml/p000330
  - YS-LN02/Text/part0026.xhtml/p000331
  - YS-LN02/Text/part0026.xhtml/p000332
files_written:
  - reviews/prose/vol-02/ch-05-b13-codex.md
source_package_hash: 2e7afecd8ca26f1cf031857ef3ac5d7bb0894db160111f9524e8bdd651b272a3
source_package_hash_verified: true
counts:
  reviewed_segments: 20
  serious: 0
  moderate: 2
  minor: 4
  total: 6
unresolved_findings: [R01, R02, R03, R04, R05, R06]
findings:
  - id: R01
    segment_id: YS-LN02/Text/part0026.xhtml/p000324
    severity: moderate
    issue: Quân hàm Serebryakov lệch lựa chọn tạm gần nhất trong chương.
    evidence: >-
      Bản dịch và self-check dùng Thiếu úy, nhưng các mục chapter5_b09_translation_proposals,
      chapter5_b10_review_proposals và chapter5_b10_signoff_recommendations trong ledger
      đều chọn Trung úy Serebryakov. Package tại đây chỉ ghi Lieutenant, không xác nhận
      một lần đổi cấp hay cho phép quay lại ánh xạ cũ. Self-check gọi Thiếu úy là ánh xạ
      gần nhất không phù hợp với ledger hiện có.
    resolution: >-
      Dùng Trung úy Serebryakov theo lựa chọn tạm gần nhất của chương. Giữ pending;
      không khẳng định đây là quân hàm canon hay suy ra nhân vật đã được thăng cấp.
  - id: R02
    segment_id: YS-LN02/Text/part0026.xhtml/p000326
    severity: moderate
    issue: Cụm “tiền tuyến có vị thế nào” gây đọc nhầm sang địa vị và làm mờ ý giải thích điều kiện sống.
    evidence: >-
      Đoạn này nối câu hỏi về cà phê với thực trạng ngoài tiền tuyến. Tanya dùng chất lượng
      cà phê để ngầm cho khách thấy điều kiện ở đó; nguồn không nói về vị thế của tiền tuyến.
      “Vốn phải như thế” cũng dễ thành nhận định về điều bắt buộc thay vì tình trạng thực tế.
    resolution: >-
      Có thể sửa thành “Dẫu vậy, nó ngầm cho ông thấy điều kiện ở tiền tuyến,
      hàm ý rằng cà phê ở đây vốn có vị như thế.” Giữ hàm ý, không thêm lời thoại giải thích.
  - id: R03
    segment_id: YS-LN02/Text/part0026.xhtml/p000324
    severity: minor
    issue: Cách diễn đạt về đun nước thêm cơ chế lắng cặn và dùng kết hợp từ khó đọc.
    evidence: >-
      Ngữ cảnh thiếu nhiên liệu, chất lượng nước và vị cà phê hỗ trợ cách hiểu đun nước để
      loại cặn vôi; không cần coi đây là thành ngữ bóng gió. Tuy nhiên, package không xác định
      thao tác lắng cặn. “Cặn phấn vôi” chồng các danh từ khiến người đọc khó hình dung.
      Cụm cuối “vị cà phê nhiễm bẩn nặng” cũng gượng, vì đang mô tả cảm nhận vị giác.
    resolution: >-
      Giữ cách đọc literal nhưng ít suy diễn hơn: “nhưng có lẽ không đủ nhiên liệu để đun
      nước loại cặn vôi”. Cụm cuối có thể đổi thành “nhưng cà phê có vị tạp chất rất khó chịu”.
      Không thêm quy trình lọc, kết tủa, thời gian đun hay kết luận về độ an toàn của nước.
  - id: R04
    segment_id: YS-LN02/Text/part0026.xhtml/p000324
    severity: minor
    issue: “Vị đại tá quan trọng kia” là lối dịch máy móc, không thể hiện tự nhiên vị thế của khách.
    evidence: >-
      Từ bổ nghĩa nhấn mạnh người khách có tầm quan trọng, giải thích việc Tanya căng thẳng
      khi tiếp đãi. “Quan trọng” đặt trực tiếp sau “đại tá” gây cảm giác xếp loại con người
      và chưa thuận giọng kể. Nguồn không xác định thêm chức vụ hoặc quyền lực cụ thể.
    resolution: >-
      Tạm chọn “vị đại tá có vai vế ấy”. Không đổi thành đại tá cao cấp, người quyền lực nhất,
      hay gán chức vụ khác; giữ nguyên quân hàm đại tá.
  - id: R05
    segment_id: YS-LN02/Text/part0026.xhtml/p000315
    severity: minor
    issue: “Vùng đất không người” thiếu rõ ràng về vị trí giữa hai chiến tuyến.
    evidence: >-
      Package đặt hành động bò tiến trong vùng trống giữa hai bên, dưới nguy cơ bắn tỉa.
      Cách dịch hiện tại dễ bị hiểu là vùng không có cư dân nói chung, làm nhạt tính chất
      nguy hiểm trực tiếp của đường tiến quân.
    resolution: Dùng “vùng đất giữa hai chiến tuyến” hoặc “vùng đất trống giữa hai chiến tuyến”.
  - id: R06
    segment_id: YS-LN02/Text/part0026.xhtml/p000328
    severity: minor
    issue: “Tuyến hỏa lực” chưa diễn đạt rõ vị trí tiền tuyến trong lời giải thích về nước uống.
    evidence: >-
      Lời thoại đối chiếu điều kiện ở trung ương với nơi đang trực tiếp chiến đấu, nối với
      tuyến đầu ở p000324 và đời sống chiến hào. “Tuyến hỏa lực” dễ gợi một tuyến bố trí
      hoặc sử dụng hỏa lực hơn là nơi đóng quân sát địch. Cách hiện tại có nhất quán với
      đề xuất b11, nhưng sự lặp lại chưa đủ để xác lập tương đương nghĩa.
    resolution: >-
      Tạm chọn “Đây là tuyến đầu” trong lời thoại. Coordinator ghi đề xuất cho lần xuất hiện
      này và đối chiếu p000281 ở b11 trước khi thống nhất; reviewer không sửa lô khác.
term_recommendations:
  - source_term: circulating notice
    proposed_vi: thông báo lưu hành
    alternatives_vi: [công văn lưu chuyển]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000320, YS-LN02/Text/part0026.xhtml/p000321]
    status: pending
    rationale: >-
      Giữ ý một văn bản thông báo được chuyển tới các nơi liên quan, ít xác định loại công văn
      hơn lựa chọn hiện tại. “Công văn lưu chuyển” hiểu được nhưng nặng giọng hành chính.
      Nếu áp dụng, đổi danh từ hồi chỉ ở p000321 cho nhất quán.
  - source_term: gray camouflage of the trench dress code
    proposed_vi: lớp ngụy trang màu xám theo quy định trang phục trong chiến hào
    alternatives_vi: [trang phục ngụy trang màu xám theo quy định trong chiến hào]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000315]
    status: pending
    rationale: >-
      Màu xám bổ nghĩa cho ngụy trang, còn quy định liên quan đến trang phục.
      Giữ lớp ngụy trang để không xác định thêm loại quân phục. Không chọn phương án
      “quy định trang phục chiến hào màu xám”, vì dễ gắn màu xám vào quy định hoặc chiến hào.
  - source_term: 3D labor
    proposed_vi: lao động 3D (bẩn thỉu, nguy hiểm và hạ thấp phẩm giá)
    alternatives_vi: [công việc 3D (bẩn thỉu, nguy hiểm và làm mất phẩm giá)]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000316]
    status: pending
    rationale: >-
      Giữ chữ 3D và đủ ba nét nghĩa đã được package giải thích; hợp giọng nội tâm coi chiến
      tranh là lao động của Tanya. Không dùng phương án thay nét hạ thấp phẩm giá bằng
      nặng nhọc trong ledger, vì hai ý không tương đương. Bản dịch hiện tại giữ đủ nghĩa.
  - source_term: firing line
    proposed_vi: tuyến đầu
    alternatives_vi: [tuyến hỏa lực, tuyến bắn]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000328]
    status: pending
    rationale: >-
      Ưu tiên nghĩa vị trí trực tiếp chiến đấu trong đoạn bàn về điều kiện sinh hoạt.
      Tuyến hỏa lực là lựa chọn cũ b11 nên cần coordinator đối chiếu khi thống nhất;
      tuyến bắn cũng dễ gợi bố trí tác chiến. Không tuyên bố các cách dịch này sai trong mọi ngữ cảnh.
  - source_term: Lieutenant Serebryakov
    proposed_vi: Trung úy Serebryakov
    alternatives_vi: [Sĩ quan cấp úy Serebryakov, Thiếu úy Serebryakov]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000324]
    status: pending
    rationale: >-
      Theo ánh xạ tạm gần nhất b09–b10 trong cùng chương; package hiện tại không phân biệt
      thêm cấp úy. Phương án trung tính khả dụng nếu coordinator thống nhất lại; Thiếu úy
      là ánh xạ cũ, thiếu căn cứ mới để ưu tiên ở lô này. Độ chắc chắn về cấp bậc thực tế còn hạn chế.
  - source_term: chalk
    proposed_vi: cặn vôi
    alternatives_vi: [chất vôi trong nước]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000324]
    status: pending
    rationale: >-
      Chọn theo ngữ cảnh nước pha cà phê cần đun xử lý, tránh gợi phấn viết được cho vào nước.
      Chất vôi trong nước ít xác định trạng thái hơn; package không đủ để mô tả hóa học hay
      cơ chế loại bỏ. Giữ giải pháp diễn đạt ít suy diễn ở R03.
  - source_term: important colonel
    proposed_vi: vị đại tá có vai vế ấy
    alternatives_vi: [vị khách quan trọng mang quân hàm đại tá]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000324]
    status: pending
    rationale: >-
      Diễn đạt tầm quan trọng của khách tự nhiên hơn, không gán chức vụ cụ thể.
      Phương án thay thế literal hơn nhưng dài; không tự thêm sắc thái đáng kính hay quyền uy tuyệt đối.
  - source_term: no-man’s-land
    proposed_vi: vùng đất giữa hai chiến tuyến
    alternatives_vi: [vùng đất trống giữa hai chiến tuyến]
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000315]
    status: pending
    rationale: Giữ rõ vị trí quân sự trong cảnh bò tiến dưới nguy cơ bắn tỉa, không chỉ nói nơi vắng người.
risks:
  - Hai lỗi vừa R01–R02 còn mở; báo cáo hoàn tất không đồng nghĩa bản dịch được duyệt.
  - Các lựa chọn quân hàm và thuật ngữ vẫn pending; không có quyết định canon mới.
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_assign_translation_revision
```

Các đoạn p000313, p000314, p000316–p000323, p000325, p000327 và p000329–p000332 không có lỗi cần sửa được xác định trong lượt này. Giọng mỉa mai về xẻng và lính bắn tỉa, sự miễn cưỡng chấp hành mệnh lệnh, chuyển cảnh hồi tưởng, lập luận về huấn luyện tân binh và quan hệ “không chỉ… mà còn…” đều được giữ. Các đoạn có phát hiện vẫn giữ được phần lớn nội dung; đề nghị sửa đúng phạm vi từng mục.

Ở p000316, bản dịch giữ đúng một cụm nhấn mạnh tương ứng với thẻ em của nguồn, không tự đánh dấu cả độc thoại. “Nó” trong trần thuật và “mình” trong nội tâm nhất quán với đề xuất LN02 ở ledger b12; không tự mở rộng phạm vi quyết định canon của pilot. Cách xưng hô “tôi/cô”, “ngài…ạ” phù hợp lượt thoại cấp trên–cấp dưới trong gói này, không cần suy thêm quan hệ cá nhân. Tên Tanya, Serebryakov, Rhine và các lựa chọn Đế quốc, Bộ chỉ huy, Bộ Tổng tham mưu nhìn chung nhất quán với các đề xuất liên quan.
