# Báo cáo ký duyệt sau sửa — vol-02-ch-02-b18-final-signoff (Claude)

- **Task:** vol-02-ch-02-b18-final-signoff; checkpoint_generation 431.
- **Phạm vi:** 33 đoạn b18 (`p000480`–`p000512`); trọng tâm xác minh M1–M3 và thuật ngữ liên quan.
- **Đầu vào đã đọc:** `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b18 (gồm `translator_followup`), source package b18, `translations/vol-02/ch-02-b18.jsonl`, báo cáo đầu `ch-02-b18-claude.md`, các lựa chọn ledger b18 trong `work/run-state/pending-terms.yml` (chỉ đọc mục `chapter2_b18_translation_proposals`).
- **Package:** SHA-256 của package b18 là `8e0a34a6…415576f`, khớp `source_package_sha256` trong handoff. Có 33 đoạn nguồn và 33 dòng dịch, mã đoạn khớp một–một và đúng thứ tự.
- **Không** mở batch khác, EPUB/PDF; không sửa bản dịch, handoff, ledger, canon, run-state. Báo cáo không trích câu nguồn.

## Kết luận

Không còn lỗi nghiêm trọng hay vừa. M1, M2, M3 đã xử lý đạt. Các mục thuật ngữ liên quan đã nhất quán với ledger. Có thể ký duyệt, với điều kiện validator/diff-check do coordinator chạy.

## 1. Xác minh M1–M3

| Mã | Đoạn | Kết quả | Căn cứ |
|---|---|---|---|
| M1 | p000509 | Đạt | Nguồn có đúng một thẻ nhấn mạnh quanh câu một từ đầu lời “tuyệt vời”. Bản dịch bọc đúng câu ngắn đó bằng `*...*`, không nhấn mạnh thêm chỗ nào khác trong đoạn. |
| M2 | p000498 | Đạt | “xưng hô” đã bỏ; dùng “lời trình bày chỉn chu ấy”, khớp ledger `vol02-ch02-b18-well-made-address`, không thu hẹp đối tượng nhận định. |
| M3 | p000498, p000500, p000501, p000505 | Đạt | Không còn “cô” làm đại từ trần thuật về Tanya: p000498 và p000500 lặp “Tanya”; p000501 dùng “Tanya may mắn hơn dự tính” (đúng đề xuất trung tính, hết “mình” ở trần thuật ngôi ba); p000505 lặp “Tanya”. Khớp p000504 và p000512 vốn đã dùng “Tanya”. |

## 2. Nhất quán thuật ngữ liên quan

- **p000497 (rear guard):** “đơn vị hậu vệ” — khớp ledger `vol02-ch02-b18-rear-guard`.
- **Reinforcements (p000498, 504, 508, 512):** thống nhất “quân tiếp viện”, khớp ledger `vol02-ch02-b18-reinforcements`; không còn “quân chi viện/đơn vị tiếp viện” ở các đoạn đã kiểm. (p000510 nằm ngoài danh sách task; quét toàn tệp b18 không thấy biến thể lệch.)
- **p000506, p000511 (xưng hô với đơn vị):** cùng dùng “mọi người”, khớp ledger `vol02-ch02-b18-address-to-unit`.
- **p000509 (radio operator):** “báo vụ viên”, khớp ledger `vol02-ch02-b18-radio-operator`.
- **p000508:** “Một số quân tiếp viện” — đã bỏ chữ “đơn vị” thêm; “Vui lên nào” vẫn giữ (nhẹ, xem mục 4).
- **p000504:** “mình” nội tâm, “Tanya” trần thuật — đúng DEC-P01-001 / ledger tạm.

## 3. Cấu trúc dòng và nhấn mạnh

- Mọi dòng có đủ trường `segment_id`, `translation`, `status` (đều `draft`), `translator`, `glossary_version`, `source_sha256`, `notes`; `source_sha256` từng dòng khớp package; `notes` rỗng.
- Nhấn mạnh: nguồn có thẻ nhấn mạnh ở đúng hai đoạn p000509 và p000512; bản dịch có `*...*` ở đúng hai đoạn này, dấu `*` chẵn/cân bằng, không thêm nhấn mạnh nơi nguồn không có. p000512: hai chỗ (câu nội tâm và tên tựa game) đều giữ.
- Quét toàn b18: không còn “cô” trần thuật, “điện báo viên”, “hậu quân”, “quân chi viện”, “đơn vị tiếp viện”.

## 4. Còn lại (nhẹ, không chặn)

- p000497: “Ta điều họ…” còn sắc thái người trên (góp ý L1 cũ, nhẹ; chấp nhận được, chưa có chứng cứ về cấp bậc người nói).
- p000508: “Vui lên nào” nghiêng “cheer up” hơn “rejoice” (L8 cũ, nhẹ).
- Các góp ý nhẹ L2–L6, L10, L11 của báo cáo đầu không được yêu cầu sửa; không ảnh hưởng nghĩa nên không chặn hoàn tất.

## 5. Khuyến nghị thuật ngữ (tạm, không nâng canon)

Giữ nguyên các lựa chọn ledger b18: đơn vị hậu vệ; Định luật Heinrich; báo vụ viên; quân tiếp viện; lời trình bày chỉn chu; “mọi người” cho đối tượng số nhiều là đơn vị; trần thuật Tanya = lặp tên hoặc bỏ chủ ngữ. Không có mục nào ảnh hưởng cốt truyện; không cần hỏi người dùng.

```yaml
role: reviewer
task_id: vol-02-ch-02-b18-final-signoff
state: done
segment_ids: [YS-LN02/Text/part0014.xhtml/p000480..p000512]
files_written: [reviews/prose/vol-02/ch-02-b18-fixes-signoff-claude.md]
validator: not_run
diff_check: not_run
review_path: reviews/prose/vol-02/ch-02-b18-fixes-signoff-claude.md
counts: {serious: 0, moderate: 0, minor: 2}
unresolved_findings: []
term_recommendations: [rear_guard=đơn vị hậu vệ, heinrichs_law=Định luật Heinrich, radio_operator=báo vụ viên, reinforcements=quân tiếp viện, well_made_address=lời trình bày chỉn chu, address_to_unit=mọi người, tanya_narration=lặp Tanya/bỏ chủ ngữ]
pending_terms: []
risks: []
commit: null
next_action: coordinator_validate_and_commit
```
