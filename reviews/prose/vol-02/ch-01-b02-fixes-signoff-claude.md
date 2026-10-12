task_id: vol-02-ch-01-b02-fixes-signoff
reviewer: claude
report_type: fixes_signoff
reviews: reviews/prose/vol-02/ch-01-b02-claude.md
volume: vol-02
chapter: 1
batch: b02
segment_range: [YS-LN02/Text/part0010.xhtml/p000001, YS-LN02/Text/part0010.xhtml/p000025]
segment_prefix: "YS-LN02/Text/part0010.xhtml/"
inputs_read:
  - handoffs/vol-02/ch-01-b02.yml
  - reviews/prose/vol-02/ch-01-b02-claude.md
  - translations/vol-02/ch-01-b02.jsonl
  - work/vol-02/batches/ch-01-b02-source.jsonl
  - work/run-state/pending-terms.yml (chapter2_b02_translator_terms, chapter2_b02_review_proposals)
source_package_sha256_check: match  # 80d9766c...d7d938
files_edited: none
status_of_choices: provisional_non_canon
verdict: pass_for_f1_f3
counts:
  segments_checked: 25
  serious_new: 0
  moderate_new: 0
  moderate_prior_total: 3
  moderate_resolved: 3
  moderate_unresolved: 0
  serious_unresolved: 0
  minor_unresolved: 11   # F4, F5, F6, F7, F10, F11, F12, F13, F14 (decision only), F16, F17a
  minor_resolved: 3      # F8, F9, F15 (F17b "cái gọi là" cũng đã sửa)
unresolved_serious_moderate: []

findings:
  - id: F1
    segment_id: p000006
    status: resolved
    evidence: >-
      Bản dịch hiện tách rõ hai vế: yêu cầu nối máy đến một đồn, và hỏi tình hình về
      đồn khác. Đồn khác không còn là nguồn cung cấp tin; khớp cấu trúc nguồn
      (nối đến một nơi / lấy thông tin về nơi khác).
  - id: F2
    segment_id: p000025
    status: resolved
    evidence: >-
      "mọi lần đánh giá" thay cho "mọi người"; đối tượng là các lần đánh giá, khớp nguồn.
      Ý "yêu cầu tối thiểu của chỉ huy" giữ nguyên.
  - id: F3
    segment_ids: [p000010, p000012, p000016, p000018, p000025]
    status: resolved
    evidence: >-
      Không còn "cô", "Ông", "anh" trong bất kỳ đoạn nào của lô. Trần thuật về Tanya
      và Lergen dùng tên lặp hoặc bỏ chủ ngữ (p000010, p000016, p000018, p000025).
      p000012 lặp "Thiếu tá" khi Lergen gọi Tanya, không dùng đại từ. "tiểu đoàn của
      Tanya" ở p000018 đã đổi. Nhất quán với ledger vol02-ch01-b02-tanya-narration và
      vol02-ch01-b02-lergen-narration. Hệ quả: tên Tanya lặp dày ở p000016 và p000025;
      đọc hơi nặng nhưng đúng chính sách tạm, không phải lỗi nghĩa.

provisional_choice_checks:
  - term_id: vol02-ch01-b02-command-personnel
    segment_id: p000006
    rendering: nhân sự của Bộ chỉ huy
    result: ok
    note: >-
      Khớp ledger. Khác "Bộ chỉ huy Biên phòng" ở p000005 nên chưa gộp thực thể.
      Rủi ro nhẹ: người đọc có thể xem "Bộ chỉ huy" là cùng đơn vị; ghi theo dõi, không chặn.
  - term_id: vol02-ch01-b02-seventh-air-fleet
    segment_id: p000008
    rendering: Hạm đội Không quân 7
    result: ok_provisional
    note: >-
      Khớp ledger (confidence 0.4). Số hiệu đã bỏ "số", thống nhất với "Tiểu đoàn 203"
      (F8 phần số hiệu đã giải quyết). Sắc thái hải quân vẫn là rủi ro đã ghi; không ảnh hưởng cốt truyện.
  - term_id: vol02-ch01-b02-general-staff-office
    segment_id: p000013
    rendering: Văn phòng Bộ Tổng tham mưu (cùng đoạn dùng "Bộ Tổng tham mưu" cho General Staff)
    result: ok_provisional
    note: >-
      Không ám chỉ cục cụ thể, khớp ledger (0.45). Hai cách gọi cùng đoạn phân biệt Office/General Staff, nhất quán nguồn.
  - term_id: vol02-ch01-b02-tanya-lergen-narration
    segment_ids: [p000010, p000012, p000016, p000018, p000025]
    result: ok
    note: Xem F3.

new_issues_from_fixes:
  serious: []
  moderate: []
  minor:
    - segment_id: p000016
      note: >-
        Lặp "Tanya" ba lần trong hai câu liền; có thể bỏ chủ ngữ ở vế giữa. Chỉ văn phong.

unresolved_minor_nonblocking:
  - {id: F4, segment_ids: [p000010], note: "giả định quá khứ còn phẳng; 'cho nổ tung' gượng; 'rồi hơi cau mày' nối tiếp"}
  - {id: F5, segment_ids: [p000001], note: "'dịp thuận tiện', 'đề phòng Dacia' còn lệch sắc thái"}
  - {id: F6, segment_ids: [p000003], note: "'Quân Dacia', 'gần như chờ sẵn', 'không biết phải làm sao' còn lệch nhẹ"}
  - {id: F7, segment_ids: [p000002], note: "'phô trương sức mạnh' so với thói ỷ thế"}
  - {id: F10, segment_ids: [p000011], note: "'bất ngờ' mất hình ảnh bolt from the blue"}
  - {id: F11, segment_ids: [p000013], note: "'đồn' cho garrison trùng với p000006; 'trực thuộc quyền chỉ huy trực tiếp' thừa"}
  - {id: F12, segment_ids: [p000016], note: "'đâu dễ bị xem thường' là nhận xét, không phải ý chí"}
  - {id: F13, segment_ids: [p000019], note: "'Tôi nghĩ' yếu hơn 'I'm sure'"}
  - {id: F14, segment_ids: [p000024], note: "ký hiệu chú thích cần coordinator ghi decisions.md; không sửa bản dịch"}
  - {id: F16, segment_ids: [p000025], note: "vẫn mất sắc thái 'rough' của nhóm dã ngoại"}
  - {id: F17a, segment_ids: [p000018, p000019, p000022], note: "'chúng' chỉ quân Dacia chưa có canon"}

recommendation: >-
  F1–F3 đã xử lý đủ; không còn lỗi nghiêm trọng hay mức vừa chưa giải quyết. Lô có thể
  được coordinator cân nhắc nâng chuẩn sau khi chạy validator và diff-check (chưa chạy trong task này).
  Các lỗi nhẹ còn lại không chặn. Mọi lựa chọn thuật ngữ/xưng hô vẫn là đề xuất tạm, chưa canon.
notes:
  - Không sửa bản dịch hay file có sẵn; không commit; không khởi chạy worker.
  - Không sao chép câu nguồn vào báo cáo.
