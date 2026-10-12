# Sign-off sửa lỗi b08 — vol-02-ch-02-b08-final-signoff

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch hay tệp dự án khác). Không trích câu nguồn.
- **Phạm vi:** 3 đoạn do translator sửa: `p000172`, `p000178`, `p000180` (`YS-LN02/Text/part0014.xhtml/…`). Đã đối chiếu: báo cáo review b08 trước, handoff b08, gói nguồn đã chuẩn bị (sha256 khớp handoff: `53359fe9…`), `translations/vol-02/ch-02-b08.jsonl`, mục `chapter2_b08_translation_proposals` trong `work/run-state/pending-terms.yml`. Chỉ đọc thêm p000173, p000179, p000181 trong cùng batch để kiểm ngữ cảnh. Không đọc batch khác.

## Kết luận: `approved` (serious 0, moderate 0)

## Kiểm tra từng mục

### MOD-1 — p000172: đã giải quyết
- Bản dịch hiện dùng hình ảnh máu bung đỏ khi che chắn cho cấp dưới, đúng với hình ảnh "nở đỏ" khi trúng đòn trong nguồn; không còn "đỏ lựng" (không còn xuất hiện ở bất kỳ đoạn nào trong batch).
- Phần còn lại của câu (cấp dưới bất cẩn cơ động vào làn đạn địch) giữ đúng nghĩa, không thêm/bớt. Liền mạch với p000173 (vết thương).

### Dấu chú thích — p000178: đã khôi phục
- Nguồn có dấu chú thích số 7 (superscript, liên kết tới phần chú thích) gắn với "CP". Bản dịch giữ ký tự superscript ⁷ ngay sau "Sở chỉ huy" → neo chú thích được bảo toàn.
- Đúng với lựa chọn tạm trong ledger (`vol02-ch02-b08-footnote-marker`: giữ ⁷ inline, chờ quy ước toàn volume) và handoff (`provisional_choices.footnote`). Vị trí đặt dấu trước dấu phẩy thay vì sau chỉ là khác biệt dấu câu, không ảnh hưởng nghĩa.
- Phần còn lại của đoạn đúng: "do you read me" → "nghe rõ không", người nói 01, chuyển giao quyền chỉ huy tiểu đoàn Viper khớp nguồn.

### Thuật ngữ combat ineffective — p000180: đã thống nhất
- Bản dịch dùng "mất sức chiến đấu", khớp khuyến nghị tạm của reviewer và ledger (`vol02-ch02-b08-combat-ineffective`) và `provisional_choices` trong handoff.
- Toàn đoạn được đối chiếu lại: số lượng/chủ thể (đại đội được cử đi trước, pháo thủ phòng không bị né, trận địa pháo tạm thời là tuyến cuối, đánh chặn đôi chút nhưng không chống nổi đợt tấn công lớn) và phủ định/khả năng đều khớp nguồn.

## Minor còn lại (không chặn, không thuộc yêu cầu sửa)
- **p000180:** "chúng" (trận địa pháo) vẫn có thể bị nhầm với "chúng" chỉ địch ở p000183/p000184 (m10 trước đó). Tùy chọn: "các trận địa ấy".
- Các minor khác (m1–m7, m9, m11–m14) không thuộc phạm vi 3 đoạn sửa; không đánh giá lại ở lượt này.

## Rủi ro
1. Quy ước chú thích vẫn là tạm thời và không phải canon; cần coordinator chốt toàn volume trước khi dựng EPUB.
2. "mất sức chiến đấu" vẫn là đề xuất (độ tin cậy 0,6), chỉ xuất hiện một lần ở p000180; đổi sau chỉ cần thay tại đó.
3. Reviewer không chạy validator/diff-check; kết quả `pass` lấy từ handoff, chưa tự kiểm. Không commit.

## YAML

```yaml
task_id: vol-02-ch-02-b08-final-signoff
state: done
reviewed_segments: 3
serious: 0
moderate: 0
minor: 1
findings:
  - {id: m10, severity: minor, segment_ids: [p000180], issue: "'chúng' (trận địa pháo) còn có thể nhầm với 'chúng' chỉ địch ở p000183/p000184", suggestion: "tùy chọn: 'các trận địa ấy'"}
risks:
  - "quy ước chú thích (⁷) vẫn tạm thời, chưa phải canon"
  - "'mất sức chiến đấu' vẫn là đề xuất, chưa phải canon"
  - "validator/diff-check chưa được reviewer tự chạy"
next_action: "coordinator ghi nhận MOD-1, dấu chú thích p000178 và thuật ngữ combat-ineffective đã giải quyết; có thể nâng b08 theo quy trình; chốt quy ước chú thích cho cả volume"
```
