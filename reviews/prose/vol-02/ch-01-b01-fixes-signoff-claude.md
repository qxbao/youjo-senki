role: reviewer
task_id: vol-02-ch-01-b01-fixes-signoff
state: done
scope: YS-LN02/Text/part0008.xhtml/p000001..p000020
inputs_used:
  - handoffs/vol-02/ch-01-b01.yml (HEAD + working-tree; review_coordination chỉ có ở working tree, chưa commit)
  - reviews/prose/vol-02/ch-01-b01-claude.md
  - translations/vol-02/ch-01-b01.jsonl (20 đoạn, status draft)
  - work/vol-02/batches/ch-01-b01-source.jsonl (sha256 khớp 5a32b413…8239)
not_read: batch khác, canon, ledger, checkpoint
modified: [] # không sửa bản dịch/báo cáo cũ/canon/ledger/handoff/checkpoint
provisional: true # mọi lựa chọn dưới đây là đề xuất tạm, không phải canon
summary: >
  F1–F6 đều đã được xử lý trong batch này, khớp nguồn và khớp lựa chọn tạm trong handoff.
  Không phát hiện lỗi nghiêm trọng hay mức vừa mới do bản sửa gây ra.
findings:
  - id: F1
    segment_id: YS-LN02/Text/part0008.xhtml/p000014
    status: resolved
    evidence: Câu hiện dùng "chỉ là sinh nhật … trên giấy tờ", đúng nghĩa "chỉ trên giấy"; không còn "mới là" đảo sắc thái. Nối mạch với p000015 (món quà sinh nhật đầu tiên).
  - id: F2
    segment_id: YS-LN02/Text/part0008.xhtml/p000015
    status: resolved
    evidence: Câu thứ hai giữ độc thoại nội tâm ngôi thứ nhất ("mình"), mức dự đoán giữ bằng "dường như sẽ" + "có thể nhảy" (không còn "sắp" nghĩa là sắp xảy ra). Chuyển lại sang trần thuật ở câu sau khớp nguồn.
  - id: F3
    segment_id: YS-LN02/Text/part0008.xhtml/p000015
    status: resolved
    evidence: Lời kêu hiện là "Thượng đế ơi" đúng provisional choice vol02-ch01-b01-god-address; không còn "Người/con", không thêm quan hệ cha–con. "một phần triệu" giữ đúng mức (cũng đóng luôn điểm nhẹ F14).
  - id: F4
    segment_id: YS-LN02/Text/part0008.xhtml/p000005
    status: resolved
    evidence: Giả định phản thực tế ở quá khứ được giữ ("nếu … đã trông thấy … có lẽ … cũng đã mỉm cười"), nhất quán với p000018 (Lergen chỉ thấy cảnh chạy đi).
  - id: F5
    segment_ids: [YS-LN02/Text/part0008.xhtml/p000011, YS-LN02/Text/part0008.xhtml/p000012]
    status: resolved
    evidence: Tự xưng nội tâm thống nhất "mình" ở p000011 và cả hai chỗ của p000012; không còn "tôi". Khớp provisional choice vol02-ch01-b01-interior-self-reference (confidence 0.8; phạm vi DEC-P01-001 vẫn là bất định đã ghi).
  - id: F6
    segment_ids:
      - YS-LN02/Text/part0008.xhtml/p000002
      - YS-LN02/Text/part0008.xhtml/p000003
      - YS-LN02/Text/part0008.xhtml/p000006
      - YS-LN02/Text/part0008.xhtml/p000015
      - YS-LN02/Text/part0008.xhtml/p000016
      - YS-LN02/Text/part0008.xhtml/p000017
      - YS-LN02/Text/part0008.xhtml/p000019
    status: resolved
    evidence: Toàn bản không còn "cô" chỉ Tanya trong trần thuật; dùng tên Tanya hoặc lược chủ ngữ (p000003, p000016 dùng "Tanya" rõ ràng, không mơ hồ chủ thể). Khớp provisional choice vol02-ch01-b01-tanya-narration. Nội tâm ở p000011/12/15 vẫn là "mình", phân biệt đúng với trần thuật.
new_issues_from_fixes:
  serious: []
  moderate: []
  minor:
    - id: N1
      segment_ids: [YS-LN02/Text/part0008.xhtml/p000002, YS-LN02/Text/part0008.xhtml/p000006, YS-LN02/Text/part0008.xhtml/p000019]
      note: Lặp tên "Tanya" dày (2 lần trong một câu ở p000002; 3 lần ở p000006; 2 lần ở p000019), hơi nặng văn. Là hệ quả chấp nhận được của lựa chọn tạm "lặp tên"; có thể lược chủ ngữ ở lần lặp gần nhau (ví dụ vế sau p000002, câu cuối p000006) mà không gây mơ hồ.
other_checks:
  - Khớp provisional_choices của handoff cho FAC (giữ "FAC Dacia", p000003), god-address, interior-self-reference, tanya-narration.
  - Nhấn mạnh *...* chỉ ở p000006 và p000008, không đổi so với báo cáo gốc.
  - Không có đoạn bị thêm/bớt; 20 mã đoạn đầy đủ, status vẫn draft.
carried_over_minor_unchanged: # không thuộc F1–F6, không chặn nâng bản chuẩn
  still_present: [F7, F8, F9, F10, F11, F12, F13, F15, F16, F17]
  resolved_incidentally: [F14]
counts:
  serious: 0
  moderate: 0
  minor: 11 # 10 nhẹ cũ còn lại + 1 mới (N1)
  f1_f6_resolved: 6
  f1_f6_unresolved: 0
unresolved_serious_moderate: []
verdict: F1–F6 đạt; không còn lỗi nghiêm trọng/vừa. Các điểm nhẹ còn lại tùy translator xử lý, không cần vòng sửa bắt buộc.
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_decide_promotion
