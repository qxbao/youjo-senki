# Signoff sửa lỗi vol-02-ch-04-b21 (Claude)

- Phạm vi: 34 đoạn, `YS-LN02/Text/part0024.xhtml/p000278` đến `p000311`. Mã đoạn viết tắt `pNNNNNN`.
- Đầu vào đã đọc: handoff b21, source package b21 (sha256 khớp handoff: 97e2ffe3…), canon được tham chiếu (`style-guide.md`, `decisions.md`, `glossary.yml`, `characters.yml`, `glossary-pending.yml`; sha256 khớp handoff), mục `chapter4_b21_translation_proposals` trong `pending-terms.yml`, báo cáo review gốc, bản dịch hiện tại. Không đọc lô khác.
- Đề xuất gốc ở p000221 nằm ngoài phạm vi b21 và không bị thay đổi; không kiểm tra.
- Bản dịch hiện có 34 dòng, khớp 34 đoạn.

## Kiểm tra M1–M4

| ID | Đoạn | Nguồn | Bản dịch hiện tại | Kết quả |
|---|---|---|---|---|
| M1 | p000288 | "If that were the case, the world would already be Utopia" | "Nếu chỉ cần lý lẽ là đủ, thế giới hẳn đã là Utopia; việc thiên đường nơi trần thế không tồn tại đã cho thấy rõ lập trường của họ." | Đã sửa. Vế giả định phản thực đúng chiều; "Utopia" giữ theo đề xuất tạm. |
| M2 | p000294 | "once they'd lost them" (mất dấu/không còn theo dõi) | "một khi đã mất dấu những con tàu đó" | Đã sửa. Khớp mạch tìm kiếm trên biển. |
| M3 | p000295 | "They were trying to discourage further resistance" (Đế quốc) | "Đế quốc đang cố dập tắt ý chí kháng cự vào thời điểm này, nên vấn đề ấy có thể trở thành một cơn đau đầu." | Đã sửa. Chủ thể nêu rõ là Đế quốc; không còn "họ" mơ hồ. Dấu `*...*` ở lời kẻ địch được giữ đúng phạm vi (DEC-P01-002). |
| M4 | p000298 | "Missing a ship or two was one thing, but they had let them get away" | "Để sót một hai con tàu thì còn đành, đằng này họ đã để chúng trốn thoát." | Đã sửa. Không còn nghĩa "mất tàu của mình". |

## Kết luận

- Serious còn lại: 0.
- Moderate còn lại: 0 (M1–M4 đều đã giải quyết).
- Minor L1–L8 và ghi nhận xưng hô/cấp bậc (p000306 "Đại tá", p000310 "cô") không chặn lô; không thuộc phạm vi signoff này và vẫn là đề xuất pending, không phải canon.
- Ghi chú không chặn: handoff ghi `pending_term_count: 4` nhưng mục ledger `chapter4_b21_translation_proposals` hiện có 6 mục (thêm cách gọi "Đại tá" p000306 và "cô" p000310). Coordinator nên đồng bộ số đếm.
- Validator/diff-check: không chạy lại trong signoff này (handoff ghi pass).

next_action: signoff
