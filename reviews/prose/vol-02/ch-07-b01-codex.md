# Review — vol-02-ch-07-b01

```yaml
role: reviewer
task_id: vol-02-ch-07-b01-review
state: done
review_path: reviews/prose/vol-02/ch-07-b01-codex.md
files_written:
  - reviews/prose/vol-02/ch-07-b01-codex.md
scope:
  batch: vol-02-ch-07-b01
  segment_id_start: YS-LN02/Text/part0032.xhtml/p000001
  segment_id_end: YS-LN02/Text/part0032.xhtml/p000025
  reviewed_rows: 25
  source_package: work/vol-02/batches/ch-07-b01-source.jsonl
  source_package_sha256: 7b3f19c518f9496b9c62ccbe804df972be23924be7f4be43f4356f9d09cf061c
  checksum_match: true
  translation: translations/vol-02/ch-07-b01.jsonl
  self_check: reviews/semantic/vol-02/ch-07-b01-self-check.md
  primary_handoff: handoffs/vol-02/ch-07-b01.yml
  review_handoff: handoffs/vol-02/ch-07-b01-review.yml
  canon_read:
    - canon/glossary.yml
    - canon/style-guide.md
    - canon/characters.yml
    - canon/decisions.md
    - canon/glossary-pending.yml
  ledger_section_read: chapter7_b01_translator_proposals
  other_source_packages_read: false
  epub_pdf_read: false
  source_quotations: false
validator: not_run
diff_check: not_run
commit: null
counts:
  serious: 0
  moderate: 3
  minor: 3
  total: 6
  unresolved_findings: 6
checks:
  stable_ids: '25 mã duy nhất; đúng thứ tự và đối ứng 1:1 với gói nguồn; không thiếu, lặp hay gộp đoạn.'
  emphasis: 'Đúng phạm vi câu đầu p000008 và p000009; không thêm nhấn mạnh cho nội tâm ở p000010 hoặc p000024.'
  viewpoint: 'Trần thuật về Tanya dùng nó, tự quy chiếu dùng mình; phù hợp DEC-P01-001. Không xác lập thêm quan hệ nhân vật.'
  numbers: 'Giữ 01, 04, 10, 11, 13, 203, 95; tám nghìn feet; khoảng một mét; 12,7/40/88/120 mm. Không đổi đơn vị.'
  tactical_logic: 'p000015 giữ khó gây sát thương, không đảo thành khó bị sát thương. p000020 giữ bão hòa làm suy yếu rồi xuyên chắn và điều kiện tập trung phòng thủ. p000021–p000024 giữ choáng, mất khả năng né, xung lực xuyên qua bảo vệ, và giới hạn lý thuyết của thiết bị; cần sửa trình tự p000023.'
  remaining_rows: 'p000001–p000002, p000005–p000010, p000012–p000015, p000017–p000018, p000020–p000022, p000024–p000025 không có lỗi nghĩa vừa/nghiêm trọng được xác lập từ gói này. Hình ảnh định giá sinh mạng ở p000012 được giữ.'
findings:
  - id: B01-R01
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000003
    issue: 'Tách ra! chốt một động tác chia/tách đội hình khi gói chưa xác định đối tượng của khẩu lệnh.'
    evidence: 'p000002 có xung phong; p000004–p000007 là liên lạc gấp, báo trúng đạn và đưa thương binh về sau; p000010 và p000014 có hỏa lực dày đặc và bị bao vây. Các chi tiết này chứng minh tình thế khẩn cấp nhưng không mô tả động tác ngay sau khẩu lệnh, người phát lệnh hay quy ước vô tuyến.'
    resolution: 'Tạm giữ thuật ngữ Break! hai lần, giữ dấu thoại và dấu chấm than; ghi pending. Đây là phương án ít suy diễn nhất, chưa phải bản Việt hóa cuối cùng. Không thêm đối tượng, hướng chuyển động hoặc ý định phá vây.'
    alternatives:
      - 'Tách ra! nếu có bằng chứng về tách đội hình; hiện chỉ là một cách đọc có thể.'
      - 'Ngoặt gấp! hoặc Né gấp! nếu có bằng chứng về động tác tránh đạn; không chọn từ gói hiện tại.'
      - 'Ngắt! nếu có bằng chứng về ngắt lượt liên lạc; chuỗi thoại gấp chỉ hỗ trợ khả năng, chưa xác nhận.'
      - 'Phá vây! nếu có lệnh thoát vòng vây; p000014 chưa đủ nối ý định này với p000003.'
    uncertainty: high
    status: open
  - id: B01-R02
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000004
    issue: 'Thêm gọi biến Fox Three thành người/đơn vị nhận liên lạc.'
    evidence: 'Cấu trúc đoạn này không chỉ rõ quan hệ người gọi–người nhận. Khác với p000006 và p000014, quan hệ đó không được nêu tường minh. Gói cũng chưa xác định Fox Three là biệt danh hay mã báo hành động.'
    resolution: 'Bỏ gọi; giữ 04 rồi cụm Fox Three lặp hai lần, không khai triển nghĩa. Sửa mô tả pending từ biệt danh thành tín hiệu/định danh vô tuyến chưa rõ chức năng.'
    alternatives:
      - 'Giữ gọi chỉ khi có căn cứ xác nhận Fox Three là người nhận; gói này không cung cấp.'
      - 'Không tự đổi thành thông báo phóng tên lửa hoặc gắn loại vũ khí.'
    status: open
  - id: B01-R03
    severity: moderate
    segment_id: YS-LN02/Text/part0032.xhtml/p000023
    issue: 'Bị nghiền nát ngay tại chỗ làm mờ hậu quả tiếp diễn sau khi rơi xuống, dễ hiểu thành bị nghiền ngay lúc trúng đạn trên không.'
    evidence: 'Đoạn phân biệt chấn động nội tạng làm mất khả năng hành động, trường hợp may chỉ bất tỉnh nhưng vẫn rơi, rồi khả năng phần lớn bị xé nát ở nơi họ nằm. Bản dịch giữ độ bất định nhưng bỏ dấu hiệu về vị trí sau khi rơi.'
    resolution: 'Giữ trình tự; đề xuất câu cuối: Và có lẽ phần lớn sẽ bị xé nát ngay nơi họ nằm. Không bổ sung tác nhân hay khẳng định chính cú rơi gây cái chết.'
    alternatives:
      - 'Và có lẽ phần lớn sẽ bị băm nát tại chỗ họ nằm.'
    status: open
  - id: B01-R04
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000011
    issue: 'Bên bờ Rhine thêm vị trí ven sông, trái với phương án ledger giữ địa danh chưa phân loại.'
    evidence: 'p000011 định vị địa ngục tại Rhine; p000013 gọi Rhine là nghĩa địa pháp sư. Không có chi tiết xác nhận bờ sông trong b01.'
    resolution: 'Đổi bên bờ Rhine thành ở Rhine; không tự thêm sông hoặc mặt trận.'
    alternatives:
      - 'Tại Rhine.'
    status: open
  - id: B01-R05
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000016
    issue: 'Thuốc nổ mạnh bắn vào máy bay nghe như bắn vật liệu nổ thô, làm mờ loại đạn/hỏa lực.'
    evidence: 'Đoạn nói vật nổ được bắn nhằm vào máy bay, đặt song song với màn đạn phòng không; không nêu thành phần hóa học hoặc loại pháo cụ thể.'
    resolution: 'Tạm dùng đạn nổ mạnh bắn vào những máy bay này, không thêm cỡ đạn, ngòi nổ hoặc cơ chế nổ.'
    alternatives:
      - 'Đạn có sức nổ mạnh.'
    status: open
  - id: B01-R06
    severity: minor
    segment_id: YS-LN02/Text/part0032.xhtml/p000019
    issue: 'Cỡ đạn đơn thông thường là kết hợp từ khó hiểu, có thể che mất giới hạn chịu một phát riêng lẻ.'
    evidence: 'p000019 nêu mức 12,7 mm cho một phát trúng trực tiếp; p000020 đối chiếu với nhiều phát trong tấn công bão hòa.'
    resolution: 'Diễn đạt rõ một phát: Với một phát đạn thông thường trúng trực tiếp, cỡ đạn lớn nhất màn chắn bảo hộ có thể đỡ là 12,7 mm.'
    alternatives:
      - 'Màn chắn bảo hộ có thể đỡ một phát đạn thông thường trúng trực tiếp với cỡ tối đa 12,7 mm.'
    status: open
unresolved_findings: [B01-R01, B01-R02, B01-R03, B01-R04, B01-R05, B01-R06]
term_recommendations:
  - source_term: Magic Major / field major
    proposed_vi: 'Thiếu tá Pháp sư / thiếu tá tác chiến'
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000001, YS-LN02/Text/part0032.xhtml/p000002]
    rationale: 'Tạm giữ cấp thiếu tá và vai trò pháp sư/tác chiến, không suy ra bảng quân hàm hay xem cách gọi thứ hai là cấp bậc khác.'
    alternatives_vi: ['Thiếu tá ma pháp / thiếu tá ngoài chiến trường']
    status: pending
  - source_term: 203rd Aerial Mage Battalion
    proposed_vi: Tiểu đoàn Pháp sư Trên không số 203
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000007]
    rationale: 'Giữ cấp đơn vị, số hiệu và hoạt động trên không; không tự gán quân chủng.'
    alternatives_vi: [Tiểu đoàn Pháp sư Không chiến số 203]
    status: pending
  - source_term: Being X
    proposed_vi: Being X
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000008]
    rationale: 'Kế thừa đề xuất glossary-pending; không khẳng định bản thể hay đồng nhất với danh xưng ở đoạn sau.'
    alternatives_vi: [Thực thể X]
    status: pending
  - source_term: God
    proposed_vi: 'Thượng đế; ngài'
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000009]
    rationale: 'Giữ lựa chọn ledger và giả định tồn tại; ngài chỉ là cách quy chiếu tạm, không chứng minh Tanya tôn kính. Nếu cần giảm sắc thái kính trọng, lặp danh xưng thay vì tự thêm đại từ miệt thị.'
    alternatives_vi: ['Thượng đế; lặp danh xưng', Chúa]
    status: pending
  - source_term: Rhine
    proposed_vi: Rhine
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000011, YS-LN02/Text/part0032.xhtml/p000013]
    rationale: 'Giữ địa danh không phân loại; sửa bổ nghĩa bên bờ tại p000011.'
    alternatives_vi: ['Sông Rhine hoặc mặt trận Rhine chỉ khi có căn cứ thích hợp']
    status: pending
  - source_term: protective film / defensive shell
    proposed_vi: màn chắn bảo hộ / lớp vỏ phòng thủ
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000017, YS-LN02/Text/part0032.xhtml/p000018, YS-LN02/Text/part0032.xhtml/p000019, YS-LN02/Text/part0032.xhtml/p000020, YS-LN02/Text/part0032.xhtml/p000021, YS-LN02/Text/part0032.xhtml/p000022, YS-LN02/Text/part0032.xhtml/p000023, YS-LN02/Text/part0032.xhtml/p000024]
    rationale: 'Phân biệt chắn ngoài cách khoảng một mét và giáp áp sát thịt; p000017 có thể dùng màn chắn bảo hộ để nối rõ tên tạm với p000019. Không gộp hai lớp hoặc suy ra cơ chế kỹ thuật.'
    alternatives_vi: [màng bảo hộ / lớp vỏ phòng ngự]
    status: pending
  - source_term: Elinium Type 95 / orb
    proposed_vi: Elinium Type 95 / quả cầu
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000024]
    rationale: 'Giữ tên thiết bị và danh từ trung tính; không thêm cấu tạo. 88 mm thuộc màn chắn; 120 mm thuộc lớp vỏ và chỉ là năng lực lý thuyết, không bảo đảm cơ thể sống sót.'
    alternatives_vi: [Elinium loại 95 / cầu thể]
    status: pending
  - source_term: Break!
    proposed_vi: Break!
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000003]
    rationale: 'Giữ thuật ngữ ngắn tạm thời vì các cách Việt hóa đều chọn một chức năng chưa được xác nhận; xem B01-R01.'
    alternatives_vi: [Tách ra!, Ngoặt gấp!, Né gấp!, Ngắt!, Phá vây!]
    uncertainty: high
    status: pending
  - source_term: Fox Three / Fairy 01 / CP
    proposed_vi: Fox Three / Fairy 01 / CP
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000004, YS-LN02/Text/part0032.xhtml/p000014]
    rationale: 'Giữ tín hiệu/định danh và chữ viết tắt. p000014 có quan hệ gọi rõ, p000004 không có; không coi cả ba đều là biệt danh hoặc tự khai triển CP.'
    alternatives_vi: ['Khai triển hoặc Việt hóa khi có bằng chứng về chức năng']
    status: pending
  - source_term: high explosives
    proposed_vi: đạn nổ mạnh
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000016]
    rationale: 'Được bắn vào máy bay trong chuỗi hỏa lực; thuật ngữ tạm không suy ra loại vũ khí.'
    alternatives_vi: [đạn có sức nổ mạnh]
    status: pending
  - source_term: saturation attack
    proposed_vi: tấn công bão hòa
    segment_ids: [YS-LN02/Text/part0032.xhtml/p000020]
    rationale: 'Giữ đối lập giữa một phát riêng lẻ và hỏa lực dồn dập làm suy yếu chắn; không thêm số lượng hoặc đội hình.'
    alternatives_vi: [tấn công bằng hỏa lực dồn dập]
    status: pending
pending_terms_policy: 'Tất cả 11 mục trên là đề xuất tạm, không canon. Coordinator cập nhật ledger/handoff; reviewer không sửa các tệp đó. Không cần dừng xin quyết định cho các lựa chọn tạm này.'
risks:
  - 'Break! vẫn chưa xác định được nghĩa chuyên biệt từ b01; giữ nguyên là giải pháp tạm, cần rà lại khi có thêm ngữ cảnh được giao.'
  - 'Fox Three chưa rõ chức năng; nhận xét dựa vào cấu trúc của gói, không dựa vào quy ước quân sự hoặc lore bên ngoài.'
  - 'Self-check chưa nhận diện suy diễn người nhận ở p000004, địa hình ở p000011 và vị trí sau khi rơi ở p000023.'
  - 'Báo cáo hoàn tất nhưng bản dịch còn ba finding mức vừa; không coi batch đã đạt điều kiện hoàn tất pipeline.'
  - 'Đối chiếu ID/nhấn mạnh là kiểm tra cục bộ, không thay thế validator hoặc diff-check; cả hai chưa chạy.'
next_action: 'Coordinator tiếp nhận đề xuất; người giữ quyền sửa translations xử lý findings, cập nhật self-check và chạy các kiểm tra bắt buộc.'
```
