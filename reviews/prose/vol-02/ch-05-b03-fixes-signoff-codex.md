# Sign-off sửa lỗi vol-02-ch-05-b03

Chấp nhận các sửa B03-F01–B03-F09 trong bản dịch hiện tại. Không phát hiện lỗi nghiêm trọng hoặc vừa mới trong bảy đoạn bị sửa: p000053, p000062, p000066–p000069, p000074. Bảy lựa chọn thuật ngữ trong `chapter5_b03_translation_proposals` đều được áp dụng đúng; chúng vẫn là đề xuất pending, không phải canon.

Đã đọc shared/reviewer, config, handoff, năm canon references, riêng mục pending được giao, package b03, bản dịch b03 và review b03 ban đầu. Đối chiếu 27 đoạn p000049–p000075 để kiểm tra ngữ cảnh của các sửa; không đọc batch/source/translation/review khác, không mở EPUB/PDF, không gọi worker. Chỉ ghi báo cáo này.

Hash package và cả năm canon references khớp handoff. Hai danh sách mã đoạn đủ 27 đoạn, đúng thứ tự/phạm vi; trường định danh hash nguồn khớp handoff. Hash bản dịch được xét: `63d87d4128207d847d95d39dea60b1a4743509ab1d54e60025998ec79f197a69`. Đây là kiểm tra đầu vào cục bộ, không thay thế validator/diff-check và không tái xác minh sách gốc. Chỉ p000062 có nhấn mạnh; phạm vi nhấn mạnh của bản dịch khớp package. Không thêm nhấn mạnh vào nội tâm.

| ID | Mã đoạn (YS-LN02/Text/part0026.xhtml/) | Kết quả và căn cứ |
| --- | --- | --- |
| B03-F01 | p000066, p000069 | Resolved. Trần thuật dùng “nó” cho Tanya; câu sau ở p000069 dùng “mình”, nối đúng nội tâm p000070–p000071 theo DEC-P01-001. |
| B03-F02 | p000067 | Resolved. Giữ cả cấp vùng nhận dạng phòng không và phân khu D-5; cấu trúc địa chỉ không còn gắn D-5 với toàn vùng. |
| B03-F03 | p000068 | Resolved. Tên tiểu đoàn giữ hoạt động trên không và số 203, không gán đơn vị cho Không quân; phù hợp căn cứ Lục quân tại p000064. |
| B03-F04 | p000074 | Resolved. Dùng “công thức đánh lừa quang học”, giữ chức năng rộng, không tự xác lập cơ chế che giấu. |
| B03-F05 | p000062, p000067 | Resolved. Giữ Rhine chưa phân loại trong lời xướng và tên vùng; không bổ sung sông/mặt trận. Các vế lặp và nhấn mạnh ở p000062 được giữ. |
| B03-F06 | p000068 | Resolved. “Hô hiệu Pixie” biểu thị chức năng định danh vô tuyến, giữ nguyên tên; xác nhận mã và thời gian 160 giây vẫn đúng. |
| B03-F07 | p000066 | Resolved. “Giới chỉ huy cấp cao của Lục quân Đế quốc” giữ tầng chỉ huy, không thêm sắc thái miệt thị; hình ảnh thần chết vẫn được giữ. |
| B03-F08 | p000053 | Resolved. “Bị sốc vì pháo kích” là phương án thay thế được review ban đầu và handoff cho phép; giữ đây là suy đoán của người lính, không khẳng định chấn thương thể chất hay chẩn đoán cụ thể. |
| B03-F09 | p000066 | Resolved. Giữ đồng thời tiểu đoàn dành cho những kẻ cuồng chiến tranh và do chính họ lập nên, cùng sự lặp có chủ ý và việc đã tới chiến trường. |

Kiểm tra lại các đoạn bị sửa không thấy đảo phủ định, đổi chủ thể, mất số hiệu/thời gian, chuyển sai điểm nhìn hoặc phát sinh lỗi nghĩa mức nghiêm trọng/vừa. Ở p000074, danh sách chuẩn bị, quyền tùy nghi đối phó và hành động cầm thiết bị vẫn được giữ. Các nhận xét dưới đây chỉ xác nhận lựa chọn tạm trong phạm vi b03, không suy ra lore hoặc tính nhất quán toàn bộ sách.

```yaml
role: reviewer
task_id: vol-02-ch-05-b03
state: done
review_path: reviews/prose/vol-02/ch-05-b03-fixes-signoff-codex.md
signoff: accepted_with_provisional_terms
segment_id_start: YS-LN02/Text/part0026.xhtml/p000049
segment_id_end: YS-LN02/Text/part0026.xhtml/p000075
affected_segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000053
  - YS-LN02/Text/part0026.xhtml/p000062
  - YS-LN02/Text/part0026.xhtml/p000066
  - YS-LN02/Text/part0026.xhtml/p000067
  - YS-LN02/Text/part0026.xhtml/p000068
  - YS-LN02/Text/part0026.xhtml/p000069
  - YS-LN02/Text/part0026.xhtml/p000074
files_written:
  - reviews/prose/vol-02/ch-05-b03-fixes-signoff-codex.md
resolved_findings: [B03-F01, B03-F02, B03-F03, B03-F04, B03-F05, B03-F06, B03-F07, B03-F08, B03-F09]
unresolved_findings: []
findings: []
term_recommendations:
  - id: vol02-ch05-b03-guardians-of-rhine
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000062]
    proposed_vi: Những người bảo vệ Rhine
    alternatives_vi: [Những người bảo vệ mặt trận Rhine, Những người bảo vệ sông Rhine]
    rationale: Giữ địa danh chưa phân loại; các phương án bổ nghĩa cần căn cứ khác.
    uncertainty: Chưa xác lập tên tổ chức chính thức hay lời xưng tụng.
    application: verified
    status: pending
  - id: vol02-ch05-b03-air-defense-identification-zone
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000067]
    proposed_vi: Vùng nhận dạng phòng không Rhine, phân khu D-5
    alternatives_vi: [Khu vực nhận dạng phòng không Rhine, phân khu D-5]
    rationale: Giữ chức năng nhận dạng và cả hai cấp định vị tác chiến.
    uncertainty: Tên tiếng Việt và cách viết hoa chưa được duyệt.
    application: verified
    status: pending
  - id: vol02-ch05-b03-203rd-aerial-mage-battalion
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000068]
    proposed_vi: Tiểu đoàn Pháp sư Trên không số 203
    alternatives_vi: [Tiểu đoàn Pháp sư Bay số 203]
    rationale: Giữ phương thức hoạt động và số hiệu; phương án Không quân trong ledger thiếu căn cứ tại chỗ nên không chọn.
    uncertainty: Tên chính thức và cơ cấu tổ chức chưa được xác lập trong phạm vi này.
    application: verified
    status: pending
  - id: vol02-ch05-b03-computation-orb
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000074]
    proposed_vi: quả cầu tính toán
    alternatives_vi: [quả cầu tính toán ma thuật]
    rationale: Phương án literal phù hợp bối cảnh thiết bị pháp sư; không cần thêm ma thuật.
    uncertainty: Không xác lập nguyên lý vận hành hoặc hình dạng chi tiết.
    application: verified
    status: pending
  - id: vol02-ch05-b03-brass
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000066]
    proposed_vi: giới chỉ huy cấp cao
    alternatives_vi: [các chỉ huy cấp cao, cấp trên, đám chỉ huy cấp cao]
    rationale: Giữ tầng chỉ huy và hạn chế phán xét thêm; cấp trên làm mờ tầng, đám thêm miệt thị.
    uncertainty: Chỉ xét sắc thái tại b03, không kiểm chứng lựa chọn ở batch khác.
    application: verified
    status: pending
  - id: vol02-ch05-b03-optical-deception-formulas
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000074]
    proposed_vi: công thức đánh lừa quang học
    alternatives_vi: [công thức nghi binh quang học, công thức ngụy trang quang học]
    rationale: Giữ phạm vi đánh lừa rộng; ngụy trang cần căn cứ về cơ chế che giấu.
    uncertainty: Cơ chế cụ thể chưa rõ.
    application: verified
    status: pending
  - id: vol02-ch05-b03-pixie-call-sign
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000068]
    proposed_vi: hô hiệu Pixie
    alternatives_vi: [tên gọi vô tuyến Pixie]
    rationale: Giữ chức năng định danh qua vô tuyến và nguyên dạng tên riêng.
    uncertainty: Quy ước hô hiệu chưa có canon.
    application: verified
    status: pending
counts:
  reviewed_segments: 27
  affected_segments_rechecked: 7
  fixes_verified: 9
  resolved_moderate: 4
  resolved_minor: 5
  serious: 0
  moderate: 0
  minor: 0
  new_findings: 0
  unresolved_findings: 0
  provisional_terms_verified: 7
  pending_terms: 7
risks:
  - Thuật ngữ, tên đơn vị/địa bàn, hô hiệu và cơ chế ma pháp vẫn pending; sign-off không phê duyệt canon.
  - Không kiểm chứng tính nhất quán ngoài b03 hoặc tái xác minh nguồn EPUB/manifest theo giới hạn nhiệm vụ.
  - Validator/diff-check và điều kiện commit của pipeline chưa được reviewer xác nhận độc lập; trạng thái pass trong handoff chỉ là báo cáo đầu vào.
validator: not_run
diff_check: not_run
commit: null
next_action: >-
  Coordinator tiếp nhận sign-off, cập nhật trạng thái chín finding và hoàn tất
  các kiểm tra/commit bắt buộc của pipeline cho b03 trong phạm vi được phép.
  Giữ bảy lựa chọn thuật ngữ ở trạng thái pending; không cần chờ người dùng
  quyết định và không tự nâng thành canon. Reviewer không chạy bước tiếp theo.
```
