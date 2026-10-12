# Báo cáo duyệt cuối sau sửa — vol-02-ch-03-b09 (Claude)

- Task: `vol-02-ch-03-b09-final-signoff`, checkpoint_generation 537.
- Phạm vi: 32 đoạn `p000032`–`p000063` (`YS-LN02/Text/part0018.xhtml`).
- Đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b09, source package b09 cục bộ, `translations/vol-02/ch-03-b09.jsonl`, báo cáo phản biện đầu `ch-03-b09-claude.md`, metadata `translator_followup`, mục `chapter3_b09_translation_proposals` trong ledger. Không mở lô khác, EPUB/PDF; không kiểm tra đoạn p000025 (ngoài phạm vi b09, đã được gỡ khỏi ledger theo handoff).
- Hash: SHA-256 source package `02f9f5ca…0b63`, khớp handoff.
- Báo cáo không trích câu nguồn. Mọi lựa chọn là đề xuất, không phải canon.

## Cấu trúc dòng

- 32 dòng JSONL, mã đoạn khớp 1–1 và cùng thứ tự với source package.
- Mọi dòng có đủ trường: `segment_id`, `translation`, `status`, `translator`, `glossary_version`, `source_sha256`, `notes`.
- Số cụm nhấn mạnh `*...*` bằng đúng số thẻ nhấn mạnh trong nguồn ở mọi đoạn; không còn dấu `*` lẻ. Không có nhấn mạnh tự thêm.

## Xác minh M1–M4

| Mã | Đoạn | Kết quả | Ghi chú |
|---|---|---|---|
| M1 | p000052 | **Đã giải quyết** | Chức danh nay là "Thượng tướng von Wragell", không còn "Đại tá"; khớp ledger `vol02-ch03-b09-colonel-general`. |
| M2 | p000037, p000042 | **Đã giải quyết** | p000037: chỉ nhấn từ phủ định đầu câu và câu hỏi nội tâm; phần dẫn là trần thuật không nhấn. p000042: chỉ nhấn lời thốt đầu và câu hỏi; phần trần thuật không nhấn. Khớp phạm vi nhấn mạnh nguồn (DEC-P01-002). p000042 còn giữ mức độ ("cực kỳ triển vọng"), tức đã sửa luôn l3. |
| M3 | p000051, p000052, p000053, p000057 | **Đã giải quyết** | "Cụm tập đoàn quân phương Bắc" nhất quán ở cả ba đoạn có nhắc; p000053 dùng "phía Tác chiến" và "Cục Hậu cần", khớp ledger. |
| M4 | p000061, p000062, p000063 | **Đã giải quyết** | Nội tâm tự quy chiếu của Tanya nay dùng "mình" (p000061 nhiều chỗ, p000062, p000063); "Tanya" ngôi ba ở p000061/p000063 là trần thuật, hợp lệ. "tôi" chỉ còn trong câu lời dặn in nghiêng ở p000061 (lời tưởng tượng hướng ra ngoài), đúng như đề xuất ban đầu. |

Các lỗi nhẹ cùng đoạn cũng đã được xử lý một phần (ví dụ "Họ thậm chí chẳng làm việc gì", "giữ vẻ ngoài", "bực bội", "buổi họp tham mưu", "Rhine" không kèm "sông"). Không kiểm lại toàn bộ lỗi nhẹ ngoài các đoạn M1–M4 vì không thuộc điều kiện chặn.

## Còn lại (không chặn)

- **Nhẹ — p000053:** "tránh giao chiến" vẫn rộng hơn nghĩa "tránh tấn công" của nguồn (trùng l8). Đề xuất: "cố hết sức tránh tấn công". Không ảnh hưởng logic.
- **Nhẹ — va chạm cấp bậc (thuật ngữ):** p000052 dùng "Trung tướng von Schreise" cho Lieutenant General, còn p000033/054/057 dùng "Trung tướng von Zettour" cho General theo ledger `vol02-ch03-b09-general-rank-scale` (độ chắc 0.35). Hai cấp khác nhau đang trùng tên, nên Zettour (General) nên có bậc riêng (ví dụ "Thượng tướng" nếu Colonel General chuyển sang "Đại tướng", hoặc ngược lại) để giữ thang Lieutenant General < General < Colonel General. Chưa có canon nào; coordinator chọn phương án tạm và áp dụng nhất quán. Không ảnh hưởng cốt truyện, không phải hard stop.

## Kết luận

M1–M4 đã giải quyết đầy đủ; không còn lỗi nghiêm trọng hoặc vừa trong b09. Cấu trúc dòng và nhấn mạnh đạt. Có thể duyệt, các mục nhẹ và va chạm cấp bậc ghi ở trên là đề xuất cho coordinator.

```yaml
role: reviewer
task_id: vol-02-ch-03-b09-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-03-b09-fixes-signoff-claude.md
counts: {serious: 0, moderate: 0, minor: 2}
unresolved_findings:
  - {severity: minor, segment_id: p000053, issue: "tránh giao chiến rộng hơn nghĩa tránh tấn công", resolution: "đề xuất sửa tùy chọn"}
  - {severity: minor, segment_id: "p000033/p000052/p000054/p000057", issue: "Lieutenant General và General cùng dịch Trung tướng", resolution: "coordinator chọn thang cấp tạm, ghi ledger"}
term_recommendations:
  - {source_term: General (Zettour), proposed_vi: "bậc riêng, khác Trung tướng của Lieutenant General", status: pending, confidence: 0.35}
  - {source_term: Colonel General, proposed_vi: "Thượng tướng (giữ ledger; hoán đổi với General nếu cần thang cấp)", status: pending}
validator: not_run
diff_check: not_run
commit: null
```
