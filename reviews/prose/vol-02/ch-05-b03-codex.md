# Phản biện vol-02-ch-05-b03

Đối chiếu 27 đoạn p000049–p000075 trong package được giao với bản dịch hiện tại. Chỉ đọc đầu vào của task và các canon references trong handoff; từ pending ledger chỉ lấy `chapter5_b03_translation_proposals`. Không mở sách gốc, batch khác hoặc báo cáo khác. Không sửa đầu vào và không chạy worker.

Hash package và năm canon references khớp handoff; hai danh sách mã đoạn khớp đủ phạm vi, các trường source_sha256 khớp định danh trong handoff. Đây là kiểm tra đầu vào cục bộ, không thay thế validator hoặc diff-check của pipeline.

Mạch mong tiếp viện → nghi ngờ → xác nhận bạn/địch → yểm trợ được giữ. Không thấy mất nguyên đoạn, đảo phủ định hoặc đổi con số 160 giây. Lời mật khẩu ở p000055/p000060 được lặp nhất quán; tính dùng một lần ở p000061 được giữ. Chỉ p000062 có nhấn mạnh trong package và bản dịch giữ đúng toàn bộ phạm vi ấy; không thêm chữ nghiêng vào nội tâm. Cảnh báo bắn nhầm quân mình ở p000075 được giữ, không cần tự bổ sung lời giải thích ai sẽ bắn trả.

Các đề xuất dưới đây chỉ áp dụng cho phạm vi này. Không xác lập lore, binh chủng, địa danh hoặc canon từ suy đoán. Đề xuất tên đơn vị vẫn là pending dù một lỗi nghĩa trong cách gọi hiện tại cần sửa.

```yaml
role: reviewer
task_id: vol-02-ch-05-b03
state: done
review_path: reviews/prose/vol-02/ch-05-b03-codex.md
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000049
  - YS-LN02/Text/part0026.xhtml/p000050
  - YS-LN02/Text/part0026.xhtml/p000051
  - YS-LN02/Text/part0026.xhtml/p000052
  - YS-LN02/Text/part0026.xhtml/p000053
  - YS-LN02/Text/part0026.xhtml/p000054
  - YS-LN02/Text/part0026.xhtml/p000055
  - YS-LN02/Text/part0026.xhtml/p000056
  - YS-LN02/Text/part0026.xhtml/p000057
  - YS-LN02/Text/part0026.xhtml/p000058
  - YS-LN02/Text/part0026.xhtml/p000059
  - YS-LN02/Text/part0026.xhtml/p000060
  - YS-LN02/Text/part0026.xhtml/p000061
  - YS-LN02/Text/part0026.xhtml/p000062
  - YS-LN02/Text/part0026.xhtml/p000063
  - YS-LN02/Text/part0026.xhtml/p000064
  - YS-LN02/Text/part0026.xhtml/p000065
  - YS-LN02/Text/part0026.xhtml/p000066
  - YS-LN02/Text/part0026.xhtml/p000067
  - YS-LN02/Text/part0026.xhtml/p000068
  - YS-LN02/Text/part0026.xhtml/p000069
  - YS-LN02/Text/part0026.xhtml/p000070
  - YS-LN02/Text/part0026.xhtml/p000071
  - YS-LN02/Text/part0026.xhtml/p000072
  - YS-LN02/Text/part0026.xhtml/p000073
  - YS-LN02/Text/part0026.xhtml/p000074
  - YS-LN02/Text/part0026.xhtml/p000075
files_written:
  - reviews/prose/vol-02/ch-05-b03-codex.md
validator: not_run
diff_check: not_run
commit: null
counts:
  reviewed_segments: 27
  serious: 0
  moderate: 4
  minor: 5
  total_findings: 9
  unresolved_findings: 9
  provisional_groups_reviewed: 5
  pending_terms: 7
findings:
  - id: B03-F01
    severity: moderate
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000066
      - YS-LN02/Text/part0026.xhtml/p000069
    issue: Đại từ trần thuật không theo DEC-P01-001 và câu nội tâm bị chuyển thành lời kể.
    evidence: >-
      p000066 dùng cô ta cho chủ thể được xác định là Tanya ở p000067.
      p000069 dùng cô ở câu sau, trong khi package chuyển từ lời kể về Tanya
      sang tự quy chiếu ngôi thứ nhất; p000070–p000071 tiếp tục nội tâm ấy.
    resolution: >-
      Dùng nó cho Tanya ở p000066. Ở p000069, giữ câu đầu là trần thuật và
      dùng mình ở câu sau: Công việc duy nhất mình ghét hơn là phải tỏ ra
      duyên dáng để phục vụ tuyên truyền. Không thêm chữ nghiêng.
    alternatives_vi:
      - Việc duy nhất mình còn ghét hơn là phải làm ra vẻ duyên dáng để phục vụ tuyên truyền.
    status: unresolved
  - id: B03-F02
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000067
    issue: Mất cấp phân khu trong địa chỉ tác chiến.
    evidence: >-
      Package đặt D-5 ở cấp phân khu thuộc vùng nhận dạng phòng không Rhine.
      Bản dịch gắn D-5 trực tiếp với toàn khu vực, làm mất cấu trúc định vị.
    resolution: Dùng phân khu D-5 thuộc Vùng nhận dạng phòng không Rhine.
    alternatives_vi:
      - phân khu D-5 của Khu vực nhận dạng phòng không Rhine
    status: unresolved
  - id: B03-F03
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000068
    issue: Tên đơn vị tự thêm quan hệ thuộc Không quân.
    evidence: >-
      Tên trong package mô tả pháp sư hoạt động trên không, chưa xác lập
      binh chủng Không quân. p000064 còn nhận diện lực lượng tinh nhuệ của
      Lục quân Đế quốc. Cách gọi hiện tại khiến người đọc dễ hiểu sai tổ chức.
    resolution: Tạm dùng Tiểu đoàn Pháp sư Trên không số 203.
    alternatives_vi:
      - Tiểu đoàn Pháp sư Bay số 203
    status: unresolved
  - id: B03-F04
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000074
    issue: Ngụy trang quang học thu hẹp phạm vi phép đánh lừa thị giác.
    evidence: >-
      Package chỉ xác định chức năng đánh lừa bằng quang học, không giới hạn
      ở che giấu hoặc hòa vào môi trường. Bản dịch chốt một cơ chế hẹp hơn
      khi chưa có canon hay mô tả cơ chế trong batch.
    resolution: Tạm dùng công thức đánh lừa quang học trong danh sách chuẩn bị.
    alternatives_vi:
      - công thức nghi binh quang học
      - công thức ngụy trang quang học, chỉ nếu có căn cứ xác nhận cơ chế che giấu
    status: unresolved
  - id: B03-F05
    severity: minor
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000062
      - YS-LN02/Text/part0026.xhtml/p000067
    issue: Tự phân loại Rhine thành con sông trong cả lời xướng và tên vùng.
    evidence: >-
      Package giữ Rhine như địa danh trong hai định danh này, không nêu
      con sông. Thêm sông thu hẹp đối tượng được bảo vệ và vị trí của vùng.
      Không dùng kiến thức địa lý ngoài task để quyết định cách hiểu tại đây.
    resolution: >-
      p000062 dùng Những người bảo vệ Rhine; p000067 giữ Rhine trong tên
      vùng như B03-F02, bỏ diễn đạt trên sông.
    alternatives_vi:
      - Những người bảo vệ mặt trận Rhine, chỉ khi có căn cứ xác nhận mặt trận
    status: unresolved
  - id: B03-F06
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000068
    issue: Biệt hiệu chưa thể hiện chức năng định danh liên lạc của Pixie.
    evidence: Câu thoại là xác nhận mã và báo danh đơn vị qua vô tuyến, không phải giới thiệu tên gọi thân mật.
    resolution: Tạm dùng hô hiệu Pixie; giữ nguyên Pixie.
    alternatives_vi:
      - tên gọi vô tuyến Pixie
    status: unresolved
  - id: B03-F07
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000066
    issue: Đám chỉ huy cấp cao thêm sắc thái miệt thị mạnh hơn căn cứ tại chỗ.
    evidence: >-
      Cách gọi cấp chỉ huy trong package có sắc thái khẩu ngữ, nhưng chưa
      đủ để xác lập thái độ khinh miệt. Giọng châm biếm vẫn có thể giữ bằng
      hình ảnh thần chết và mô tả những kẻ cuồng chiến tranh.
    resolution: Tạm dùng giới chỉ huy cấp cao của Lục quân Đế quốc.
    alternatives_vi:
      - các chỉ huy cấp cao của Lục quân Đế quốc
      - cấp trên, nhưng cách này làm mờ tầng chỉ huy được nói tới
    status: unresolved
  - id: B03-F08
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000053
    issue: Bị choáng vì đạn pháo dễ gợi chấn động thể chất tức thời hơn trạng thái tinh thần.
    evidence: >-
      Những người lính cho rằng tin tiếp viện là dấu hiệu người lính điện đài
      không còn tỉnh táo; p000058–p000061 tiếp tục đối chiếu phát điên và
      nghe nhầm. Không có căn cứ nói anh ta vừa chịu một cú nổ gây choáng.
    resolution: Tạm dùng bị sang chấn vì pháo kích, không thêm chẩn đoán cụ thể.
    alternatives_vi:
      - bị sốc vì pháo kích
    status: unresolved
  - id: B03-F09
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000066
    issue: Mô tả thành phần tiểu đoàn làm mờ ý đơn vị được lập cho những kẻ cuồng chiến tranh.
    evidence: >-
      Package đặt song song đối tượng mà tiểu đoàn phục vụ và những người
      tạo nên nó. Gồm những kẻ cuồng chiến tranh chỉ giữ thông tin thành phần.
    resolution: >-
      Dùng một tiểu đoàn dành cho những kẻ cuồng chiến tranh, do chính những
      kẻ cuồng chiến tranh lập nên; giữ sự lặp lại có chủ ý.
    alternatives_vi:
      - một tiểu đoàn lập ra cho những kẻ cuồng chiến tranh, bởi chính những kẻ cuồng chiến tranh
    status: unresolved
unresolved_findings:
  - B03-F01
  - B03-F02
  - B03-F03
  - B03-F04
  - B03-F05
  - B03-F06
  - B03-F07
  - B03-F08
  - B03-F09
term_recommendations:
  - id: vol02-ch05-b03-guardians-of-rhine
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000062]
    proposed_vi: Những người bảo vệ Rhine
    alternatives_vi: [Những người bảo vệ sông Rhine, Những người bảo vệ mặt trận Rhine]
    rationale: Giữ địa danh chưa phân loại, không tự thêm sông hoặc mặt trận; giữ nhịp lời xướng và các vế lặp.
    uncertainty: Chưa đủ căn cứ xác định đây là tên tổ chức chính thức hay lời xưng tụng.
    status: pending
  - id: vol02-ch05-b03-air-defense-identification-zone
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000067]
    proposed_vi: Vùng nhận dạng phòng không Rhine, phân khu D-5
    alternatives_vi: [Khu vực nhận dạng phòng không Rhine, phân khu D-5]
    rationale: Giữ đầy đủ chức năng nhận dạng và cấp phân khu; Vùng gọn hơn trong tên địa bàn tác chiến.
    uncertainty: Chưa có quy ước canon về tên vùng hoặc cách viết hoa.
    status: pending
  - id: vol02-ch05-b03-203rd-aerial-mage-battalion
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000068]
    proposed_vi: Tiểu đoàn Pháp sư Trên không số 203
    alternatives_vi: [Tiểu đoàn Pháp sư Bay số 203]
    rationale: Giữ số hiệu và phương thức hoạt động, không tự gán đơn vị cho Không quân.
    uncertainty: Tên tiếng Việt chính thức chưa được duyệt; không suy ra cơ cấu tổ chức ngoài batch.
    status: pending
  - id: vol02-ch05-b03-computation-orb
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000074]
    proposed_vi: quả cầu tính toán
    alternatives_vi: [quả cầu tính toán ma thuật]
    rationale: Giữ phương án literal đang dùng; câu đã đặt thiết bị trong bối cảnh pháp sư nên không cần thêm ma thuật.
    uncertainty: Không suy ra hình dạng chi tiết hoặc nguyên lý vận hành từ tên gọi.
    status: pending
  - id: vol02-ch05-b03-brass
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000066]
    proposed_vi: giới chỉ huy cấp cao
    alternatives_vi: [các chỉ huy cấp cao, cấp trên, đám chỉ huy cấp cao]
    rationale: Giữ đúng tầng chỉ huy và hạn chế phán xét thêm; có thể dùng cùng tên cơ quan trong câu.
    uncertainty: Không kiểm chứng lựa chọn ở batch trước vì ngoài phạm vi đọc; không coi tham chiếu trong ledger là bằng chứng về giọng tại đây.
    status: pending
  - id: vol02-ch05-b03-optical-deception-formulas
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000074]
    proposed_vi: công thức đánh lừa quang học
    alternatives_vi: [công thức nghi binh quang học, công thức ngụy trang quang học]
    rationale: Chọn cách rộng và ít suy diễn nhất, giữ loại công thức nhưng không tự xác định cơ chế che giấu.
    uncertainty: Chưa rõ cơ chế cụ thể; đây là đề xuất bổ sung từ lần review này.
    status: pending
  - id: vol02-ch05-b03-pixie-call-sign
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000068]
    proposed_vi: hô hiệu Pixie
    alternatives_vi: [tên gọi vô tuyến Pixie]
    rationale: Giữ chức năng định danh vô tuyến và nguyên dạng tên riêng, không Việt hóa Pixie.
    uncertainty: Chưa có quy ước canon cho hô hiệu; đây là đề xuất bổ sung từ lần review này.
    status: pending
risks:
  - Bốn lỗi mức vừa còn mở; chưa thể coi batch đã qua review bắt buộc.
  - Tên địa bàn, đơn vị và cơ chế ma pháp vẫn tạm thời; áp dụng đề xuất trong batch không phải phê duyệt canon.
  - Không kiểm chứng tính nhất quán với batch khác theo giới hạn nhiệm vụ; coordinator cần tự xử lý các liên hệ đã có trong ledger.
  - Chỉ xác nhận hash package và định danh nguồn trong các trường dữ liệu; không tái xác minh EPUB hoặc manifest ngoài phạm vi.
pending_terms:
  - {id: vol02-ch05-b03-guardians-of-rhine, proposed_vi: Những người bảo vệ Rhine, volume: vol-02, chapter: 5, segment_ids: [YS-LN02/Text/part0026.xhtml/p000062], status: pending}
  - {id: vol02-ch05-b03-air-defense-identification-zone, proposed_vi: 'Vùng nhận dạng phòng không Rhine, phân khu D-5', volume: vol-02, chapter: 5, segment_ids: [YS-LN02/Text/part0026.xhtml/p000067], status: pending}
  - {id: vol02-ch05-b03-203rd-aerial-mage-battalion, proposed_vi: Tiểu đoàn Pháp sư Trên không số 203, volume: vol-02, chapter: 5, segment_ids: [YS-LN02/Text/part0026.xhtml/p000068], status: pending}
  - {id: vol02-ch05-b03-computation-orb, proposed_vi: quả cầu tính toán, volume: vol-02, chapter: 5, segment_ids: [YS-LN02/Text/part0026.xhtml/p000074], status: pending}
  - {id: vol02-ch05-b03-brass, proposed_vi: giới chỉ huy cấp cao, volume: vol-02, chapter: 5, segment_ids: [YS-LN02/Text/part0026.xhtml/p000066], status: pending}
  - {id: vol02-ch05-b03-optical-deception-formulas, proposed_vi: công thức đánh lừa quang học, volume: vol-02, chapter: 5, segment_ids: [YS-LN02/Text/part0026.xhtml/p000074], status: pending}
  - {id: vol02-ch05-b03-pixie-call-sign, proposed_vi: hô hiệu Pixie, volume: vol-02, chapter: 5, segment_ids: [YS-LN02/Text/part0026.xhtml/p000068], status: pending}
next_action: >-
  Coordinator tiếp nhận báo cáo, ghi các lựa chọn tạm theo quy trình của mình
  và giao người giữ quyền sửa xử lý B03-F01–B03-F09 trong đúng batch này;
  sau đó kiểm tra lại các đoạn bị sửa và chạy các kiểm tra pipeline bắt buộc.
  Reviewer không tự chạy bước tiếp theo; không cần chờ người dùng chốt các
  thuật ngữ pending và không nâng đề xuất thành canon.
```
