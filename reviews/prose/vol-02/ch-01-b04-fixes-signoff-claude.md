role: reviewer
task_id: vol-02-ch-01-b04-fixes-signoff
state: done
review_of: reviews/prose/vol-02/ch-01-b04-claude.md
scope: {first: YS-LN02/Text/part0010.xhtml/p000060, last: YS-LN02/Text/part0010.xhtml/p000087, units: 28}
inputs_read:
  - handoffs/vol-02/ch-01-b04.yml  # review_coordination hiện còn là thay đổi chưa commit trong working tree
  - reviews/prose/vol-02/ch-01-b04-claude.md
  - translations/vol-02/ch-01-b04.jsonl
  - work/vol-02/batches/ch-01-b04-source.jsonl  # bị Git bỏ qua, đọc tại chỗ
  - note: không đọc batch khác; không sửa tệp hiện có; không commit; không chạy worker
integrity:
  segment_ids_match_source_in_order: true   # 28/28
  source_package_sha256_matches_handoff: true
  per_unit_source_sha256_matches: true
  glossary_version_matches_canon: true
  status_all: draft
counts:
  unresolved_serious: 0
  unresolved_moderate: 0
  new_serious: 0
  new_moderate: 0
  unresolved_minor_carried_over: 11   # m1 và m2 đã xử lý; m3–m13 chưa/chưa hoàn toàn xử lý, không chặn
verdict: pass_moderate_fixes_verified   # ứng viên vẫn là draft; chỉ coordinator được nâng cấp
moderate_findings:
  - id: M1
    segment_ids: [YS-LN02/Text/part0010.xhtml/p000060, YS-LN02/Text/part0010.xhtml/p000082, YS-LN02/Text/part0010.xhtml/p000087]
    status: resolved
    evidence: Cả ba đoạn nay dùng "Thiếu úy" (p000087 là "Thiếu úy Serebryakov"). Nguồn p000087 có cả họ lẫn cấp bậc; chọn ánh xạ này khớp phương án tạm đã ghi, không xuất hiện "Trung úy" nào trong batch.
  - id: M2
    segment_ids: [YS-LN02/Text/part0010.xhtml/p000084]
    status: resolved
    evidence: Lời phụ tá nay xưng "Tôi", không còn đại từ nội tâm "Mình"; khớp giọng xưng "Tôi… ngài" ở p000086 và quan hệ cấp dưới–cấp trên.
  - id: M3
    segment_ids: [YS-LN02/Text/part0010.xhtml/p000086]
    status: resolved
    evidence: Chỉ cụm "ba sư đoàn" được bọc `*...*`, đúng phạm vi nhấn của nguồn; câu còn lại không có dấu thừa.
  - id: M4
    segment_ids: [YS-LN02/Text/part0010.xhtml/p000067, YS-LN02/Text/part0010.xhtml/p000068, YS-LN02/Text/part0010.xhtml/p000072, YS-LN02/Text/part0010.xhtml/p000073]
    status: resolved
    evidence: Mọi "nó" chỉ Tanya đã thay bằng tên "Tanya" (p000067 hai chỗ, p000068, p000072, p000073). Tìm toàn batch chỉ còn một "nó" ở p000060, và đó là chỉ cuộc chiến, không phải Tanya.
  - id: M5
    segment_ids: [YS-LN02/Text/part0010.xhtml/p000069]
    status: resolved
    evidence: "các cô cậu" đã đổi thành "mọi người"; không còn chỗ nào trong batch dùng "cô cậu". "Các quý ông" ở cuối đoạn là lời gọi theo nguồn, không còn mâu thuẫn.
  - id: M6
    segment_ids: [YS-LN02/Text/part0010.xhtml/p000075]
    status: resolved
    evidence: Hai nguồn khác nhau liền kề nay có hai từ Việt khác nhau, "nhân lực" (núi bị lãng phí) và "vốn con người" (không biết tận dụng); khớp lựa chọn tạm trong handoff.
  - id: M7
    segment_ids: [YS-LN02/Text/part0010.xhtml/p000078]
    status: resolved
    evidence: "pháp sư không quân" thay cho "không chiến"; ngữ cảnh đối đầu lực lượng mặt đất nay đúng nghĩa. Nhất quán với "pháp sư" ở p000081.
emphasis_parity:
  source_emphasized: 3
  translation_marked: 3
  rows:
    - {segment_id: YS-LN02/Text/part0010.xhtml/p000067, source_scope: toàn tiếng hô ngắn, translation_scope: toàn tiếng hô ngắn, result: match}
    - {segment_id: YS-LN02/Text/part0010.xhtml/p000077, source_scope: một từ đơn, translation_scope: "*chiến tranh*", result: match}
    - {segment_id: YS-LN02/Text/part0010.xhtml/p000086, source_scope: cụm số lượng, translation_scope: "*ba sư đoàn*", result: match}
  extra_marks_elsewhere: 0   # chỉ ba đoạn trên chứa `*`
provisional_choices_check:   # tất cả vẫn là đề xuất, không phải canon
  - {term_id: vol02-ch01-b04-turkey-shoot, segment_ids: [YS-LN02/Text/part0010.xhtml/p000065], applied: cuộc bắn gà tây, result: consistent, note: "p000065 còn cụm 'thoải mái tàn sát' là minor m1 phần còn lại, không phải lỗi chọn thuật ngữ"}
  - {term_id: vol02-ch01-b04-manhunt, segment_ids: [YS-LN02/Text/part0010.xhtml/p000070], applied: cuộc săn người, result: consistent}
  - {term_id: vol02-ch01-b04-aerial-mage, segment_ids: [YS-LN02/Text/part0010.xhtml/p000078], applied: pháp sư không quân, result: consistent}
  - {term_id: vol02-ch01-b04-human-resources, segment_ids: [YS-LN02/Text/part0010.xhtml/p000075], applied: nhân lực, result: consistent, note: handoff chọn "nhân lực" thay vì "nguồn nhân lực" ghi trong sổ pending; coordinator cần đồng bộ sổ}
  - {term_id: vol02-ch01-b04-human-capital, segment_ids: [YS-LN02/Text/part0010.xhtml/p000075], applied: vốn con người, result: consistent}
  - {term_id: vol02-ch01-b04-aconitum-01, segment_ids: [YS-LN02/Text/part0010.xhtml/p000077], applied: giữ nguyên "Aconitum 01", result: consistent}
  - term_id: vol02-ch01-b04-address-to-unit
    segment_ids: [YS-LN02/Text/part0010.xhtml/p000069, YS-LN02/Text/part0010.xhtml/p000079]
    applied: mọi người
    result: consistent_with_residual_uncertainty
    note: p000069 đúng phạm vi (nguồn gọi chung cả nhóm). p000079 giữ lời gọi "Các đại đội trưởng" rồi mới "mọi người", nên phạm vi người nghe vẫn rõ; chỉ còn lệch nhẹ (m10), không phải lỗi vừa.
  - {term_id: vol02-ch01-b04-serebryakov-address, segment_ids: [YS-LN02/Text/part0010.xhtml/p000060, YS-LN02/Text/part0010.xhtml/p000082, YS-LN02/Text/part0010.xhtml/p000085, YS-LN02/Text/part0010.xhtml/p000087], applied: Thiếu úy, result: consistent, note: "p000085 đã bỏ 'Cô'; không còn đại từ suy giới tính"}
new_issues_from_fixes:
  serious: []
  moderate: []
  minor: []
  note: Không thấy lỗi mới do các sửa đổi. Cấu trúc câu, phủ định, thời gian và quy mô (ba trong bốn đại đội, ba sư đoàn) giữ nguyên sau sửa.
carried_over_minor:   # không chặn; translator xử lý khi tiện, đề xuất ở báo cáo gốc
  - {ref: m3, segment_ids: [YS-LN02/Text/part0010.xhtml/p000071], status: open}
  - {ref: m4, segment_ids: [YS-LN02/Text/part0010.xhtml/p000069], status: open, detail: "'sẽ bắn trả', 'tiếp tục diễn tập', 'trò chơi bắt đầu' chưa chỉnh"}
  - {ref: m5, segment_ids: [YS-LN02/Text/part0010.xhtml/p000068], status: open}
  - {ref: m6, segment_ids: [YS-LN02/Text/part0010.xhtml/p000072], status: open, detail: "ba điểm (a)(b)(c) vẫn còn"}
  - {ref: m7, segment_ids: [YS-LN02/Text/part0010.xhtml/p000073], status: open}
  - {ref: m8, segment_ids: [YS-LN02/Text/part0010.xhtml/p000076], status: open}
  - {ref: m9, segment_ids: [YS-LN02/Text/part0010.xhtml/p000078], status: open}
  - {ref: m10, segment_ids: [YS-LN02/Text/part0010.xhtml/p000079], status: open}
  - {ref: m11, segment_ids: [YS-LN02/Text/part0010.xhtml/p000081], status: open}
  - {ref: m12, segment_ids: [YS-LN02/Text/part0010.xhtml/p000085], status: partially_resolved, detail: "'Cô' đã bỏ; 'hành quân' vẫn thu hẹp nghĩa"}
  - {ref: m13, segment_ids: [YS-LN02/Text/part0010.xhtml/p000061], status: open}
  - {ref: m1, segment_ids: [YS-LN02/Text/part0010.xhtml/p000065], status: partially_resolved, detail: "'thảm sát' đã đổi; 'thoải mái tàn sát' vẫn còn sắc thái thái độ"}
  - {ref: m2, segment_ids: [YS-LN02/Text/part0010.xhtml/p000070], status: resolved}
coordinator_notes:
  - Đồng bộ sổ pending với lựa chọn "nhân lực" cho human resources (khác mục "nguồn nhân lực" cũ).
  - Chưa chốt giữa "Thiếu úy" và "Trung úy" cho Serebryakov ở cấp toàn chương; batch này đã nhất quán, nhưng cần đồng bộ với các batch khác (chưa đọc theo phạm vi nhiệm vụ).
  - Mọi lựa chọn thuật ngữ và xưng hô ở trên vẫn là đề xuất, không tự nâng thành canon.
validator: not_run
diff_check: not_run
files_written: [reviews/prose/vol-02/ch-01-b04-fixes-signoff-claude.md]
commit: null
next_action: coordinator_may_promote_candidate_after_optional_minor_polish
