# Báo cáo signoff sửa lỗi — vol-02-ch-03-b11 (Claude)

- Task: `vol-02-ch-03-b11-final-signoff`, checkpoint_generation 563.
- Phạm vi: 28 đoạn `YS-LN02/Text/part0018.xhtml/p000088`–`p000115`.
- Đã đọc: `agents/shared.md`, `agents/reviewer.md`, config, handoff b11 (gồm `translator_followup`), package b11, bản dịch hiện tại, báo cáo đầu `ch-03-b11-claude.md`, mục `chapter3_b11_translation_proposals`, DEC-P01-001. Không mở batch khác.
- Package: sha256 tính lại là `d89528f4…2464`, khớp handoff. Bản dịch đủ 28 dòng, mã đoạn đúng thứ tự, `status: draft`.
- Không quote câu nguồn. Mọi lựa chọn dưới đây là tạm thời, không nâng canon.

## Kết quả kiểm tra M1–M3

### M1 — nhất quán đại từ trần thuật về Tanya: CHƯA ĐẠT HOÀN TOÀN
- p000095: đã đổi sang "nó" (trần thuật). Đạt. "cô" còn lại nằm trong lời thoại của Weiss, hợp lệ.
- p000098: đã đổi hết sang "nó". Đạt.
- p000099: đã đổi hết sang "nó". Đạt.
- **p000092: vẫn còn "Cô ấy"** ở câu cuối, sau câu có tên "Tanya". Chưa đổi và không nằm trong `changed_segments` của `translator_followup`, dù p000092 có trong `translator_followup_segments`. Mục ledger `vol02-ch03-b11-tanya-third-person-reference` ghi phương án tạm là "Tanya in p000092" (lặp tên). Bản dịch hiện tại lệch cả DEC-P01-001 (trần thuật dùng "nó") lẫn ledger. Câu không gây nhầm người, nhưng M1 gồm cả p000092 và handoff báo "resolved" là chưa đúng.
- Đề xuất sửa tối thiểu: "Tanya sẽ không mắc đi mắc lại cùng một sai lầm đâu" (lặp tên, theo ledger) hoặc "Nó sẽ không mắc…". Độ chắc về việc cần sửa: cao; về lựa chọn lặp tên hay "nó": trung bình.

### M2 — đại từ nội tâm "mình" và "chúng ta": ĐẠT
- p000102, p000108, p000111, p000112 đều dùng "mình" cho nội tâm tự quy chiếu, khớp DEC-P01-001 và ledger `vol02-ch03-b11-tanya-interior-pronoun`.
- Lời thoại thành tiếng (p000091, 094, 095, 097, 101, 104, 109, 110, 113, 114) vẫn dùng "tôi", đúng quy ước.
- p000111 và p000112 giờ đều dùng "chúng ta". Hết lệch "chúng ta"/"chúng tôi".
- Lưu ý nhẹ (mới): ở p000111, "không thuộc thẩm quyền của mình" có thể bị hiểu là "mình" của Tanya thay vì của Ban Ngân sách, nên cân nhắc đổi thành "không thuộc thẩm quyền của họ". Không phải lỗi vừa.

### M3 — p000110, đối tượng của "rủi ro": ĐẠT
- Bản dịch hiện tại dùng "Khi… nêu rủi ro của cuộc tấn công, … bị điều đi…". Rủi ro gắn với cuộc tấn công mà phía Đế quốc định mở, không còn đọc thành mối đe dọa từ phía khác. Cấu trúc "Khi…" thay "Sau khi" đúng đề xuất, hết nhấn thứ tự thời gian quá chặt. Đạt.

## Các mục kiểm tra khác

- **p000060 (ngoài phạm vi):** không có trong package b11 và không có trong bản dịch b11. `git status` chỉ thấy file b11 (handoff, báo cáo đầu, bản dịch) thay đổi hoặc chưa theo dõi. Không có file dịch đã commit nào bị sửa, nên p000060 không bị đụng tới. Đạt.
- **Cấu trúc:** 28 dòng JSONL, `segment_id` liên tục p000088–p000115, đủ `translation`, `source_sha256`, `glossary_version`, `status`, `translator`, `notes`. Không thấy bất thường (tôi không chạy validator).
- **Nhấn mạnh (DEC-P01-002):** `*...*` chỉ có ở p000112 (hai câu cuối) và p000115 (câu đầu), khớp báo cáo đầu. Không có nhấn mạnh thừa ở đoạn khác. Đạt.
- **Nội dung ngoài M1–M3:** không thấy đoạn mất nghĩa hay thêm ý mới nghiêm trọng trong các đoạn đã sửa.
- **Lỗi nhẹ từ báo cáo đầu:** không thuộc yêu cầu signoff nên không đánh giá lại hết. Quan sát thấy một số vẫn còn nguyên: m1 (p000088 "cuộc thăm dò"), m4 (p000098 "phong thư lệnh"), m9 (p000112 "bồi thường"), m10 (p000113 "Cô lập dự toán"), m11 (p000115 "quá chén"). Đây là lỗi nhẹ, không chặn signoff.

## Kết luận

Không có lỗi nghiêm trọng. M2 và M3 đã giải quyết. **Còn 1 lỗi vừa chưa giải quyết (phần p000092 của M1)**, nên chưa thể signoff hoàn tất. Việc cần làm là một sửa nhỏ ở p000092 rồi kiểm lại nhanh p000092. Không cần hỏi người dùng, không ảnh hưởng cốt truyện.

## Thuật ngữ tạm thời (không nâng canon)

- Tanya trong trần thuật: "nó"; p000092 lặp tên "Tanya" (theo ledger). Thay thế: "nó".
- Tanya nội tâm: "mình" (p000102/108/111/112, đã áp dụng). Thay thế: "tôi" nếu có ngoại lệ ledger được duyệt.
- `Central Army`: "Quân Trung ương". Thay thế: "Lục quân Trung ương". Độ bất định trung bình.
- `Budget section`: "Ban Ngân sách". Thay thế: "Phòng Ngân sách". Độ bất định thấp–trung bình.
- `Northern Army Group`: "Cụm tập đoàn quân phương Bắc". Giữ nhất quán.
- `Vitamin P`: giữ nhãn tiếng Anh, độ bất định cao (khoảng 0,5).
- p000110: dùng "Khi… nêu rủi ro của cuộc tấn công…".

```yaml
role: reviewer
task_id: vol-02-ch-03-b11-final-signoff
state: done
segment_ids: [p000092, p000095, p000098, p000099, p000102, p000108, p000110, p000111, p000112]
files_written:
  - reviews/prose/vol-02/ch-03-b11-fixes-signoff-claude.md
review_path: reviews/prose/vol-02/ch-03-b11-fixes-signoff-claude.md
validator: not_run
diff_check: not_run
counts:
  serious: 0
  moderate: 1
  minor: 6
unresolved_findings:
  - severity: moderate
    segment_id: YS-LN02/Text/part0018.xhtml/p000092
    issue: "M1 chưa xử lý hết: còn 'Cô ấy' trong trần thuật về Tanya, lệch DEC-P01-001 và ledger (phương án tạm là lặp tên Tanya)."
    resolution: "Sửa p000092 (lặp 'Tanya' hoặc dùng 'nó'), rồi kiểm lại nhanh."
  - severity: minor
    segment_id: YS-LN02/Text/part0018.xhtml/p000111
    issue: "'thẩm quyền của mình' có thể bị hiểu là của Tanya thay vì Ban Ngân sách."
    resolution: "Cân nhắc 'thẩm quyền của họ'."
  - severity: minor
    segment_id: p000088, p000098, p000112, p000113, p000115
    issue: "Các lỗi nhẹ m1/m4/m9/m10/m11 từ báo cáo đầu vẫn còn."
    resolution: "Không chặn signoff; sửa nếu thuận tiện."
term_recommendations:
  tanya_narration: "nó; p000092 lặp tên Tanya"
  tanya_internal: "mình (p000102/108/111/112, đã áp dụng)"
  central_army: "Quân Trung ương (pending)"
  budget_section: "Ban Ngân sách (pending)"
  northern_army_group: "Cụm tập đoàn quân phương Bắc (pending)"
  Vitamin_P: "giữ nhãn tiếng Anh (pending, độ bất định cao)"
  p000110: "Khi… nêu rủi ro của cuộc tấn công… (đã áp dụng)"
  out_of_scope_p000060: "không có trong b11; không bị sửa"
risks: []
commit: null
next_action: "translator sửa p000092 rồi signoff lại"
```
