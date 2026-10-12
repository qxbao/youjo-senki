# Signoff cuối — vol-02-ch-01-b08 (Claude)

- Phạm vi: chỉ p000210 và p000216 (`YS-LN02/Text/part0010.xhtml/…`). Đầu vào: báo cáo phản biện gốc, báo cáo signoff sửa lỗi, handoff b08, `translations/vol-02/ch-01-b08.jsonl`, source package b08 (kể cả XHTML để kiểm tra nhấn mạnh). Không đọc lô/nguồn khác. Không sửa bản dịch, handoff, sổ, canon. Không chép câu nguồn.
- Mọi thuật ngữ vẫn là đề xuất tạm (provisional), không phải canon.

## Kết quả: PASS (2/2)

| Đoạn | Mục kiểm | Kết quả |
|---|---|---|
| p000210 | Phạm vi nhấn mạnh | Nguồn có đúng một cụm in nghiêng ngắn (nghĩa “tốt hơn cả”), “dự tính” nằm ngoài thẻ nhấn mạnh. Bản dịch hiện là `*tốt hơn cả*` rồi “dự tính” nằm ngoài `*...*`. Khớp phạm vi nguồn, DEC-P01-002 và handoff. **Đạt.** |
| p000210 | Ngữ pháp / nghĩa | Cấu trúc “tiến triển *tốt hơn cả* dự tính” đúng ngữ pháp, tự nhiên. Vế “không phải bàn”, vế chiến tranh (không theo kế hoạch là chuyện thường, đúng mức khẳng định của nguồn), vế “chưa từng mơ” đều giữ nguyên. Chỉ có một cặp `*...*`, cân đối. **Đạt.** |
| p000216 | Mơ hồ đại từ | “lá cờ của nó” đã đổi thành “lá cờ của sở chỉ huy ấy”; trong câu không còn “nó” nào có thể bị đọc là Tanya. Tanya xuất hiện bằng tên ở mệnh đề sau. **Đạt.** |
| p000216 | Bảo toàn nghĩa | Còn nguyên: lý do “vì vậy”, hành động hạ xuống chiếm tổng hành dinh dã chiến, lá cờ phấp phới nổi bật bất chấp nguy hiểm, Tanya bối rối và buông thêm một câu đùa hiếm hoi. Ngôi “chúng tôi” giữ. **Đạt.** |

## Còn tồn đọng
- Nghiêm trọng: 0
- Vừa: 0
- Nhẹ: 0 (L-a và L-b của signoff trước đã được giải quyết)

## Ghi chú nhẹ / rủi ro
- p000216: “sở chỉ huy ấy” quay lại chỉ “tổng hành dinh dã chiến”, nên về mặt từ vựng hơi lặp “sở chỉ huy” với “tổng hành dinh”; người đọc vẫn hiểu là cùng một nơi. Đây là rủi ro đã biết: nguồn không nói rõ tổng hành dinh ở p000186/p000211 và field HQ ở p000216 có phải cùng một địa điểm hay không. Không chặn commit; giữ ở trạng thái provisional_non_canon trong `work/run-state/pending-terms.yml`.
- Sở chỉ huy (command post cấp sư/lữ) và “sở chỉ huy ấy” ở p000216 dùng chung từ “sở chỉ huy”; chấp nhận được vì ngữ cảnh khác nhau.

```yaml
task: vol-02-ch-01-b08-final-signoff
segments: [p000210, p000216]
result: pass
p000210: {emphasis_span_ok: true, dutinh_outside_markup: true, grammar_ok: true, meaning_preserved: true}
p000216: {pronoun_ambiguity_resolved: true, meaning_preserved: true}
remaining: {serious: 0, moderate: 0, minor: 0}
risks:
  - "p000216: cùng địa điểm hay không giữa tổng hành dinh và field HQ — nguồn không nói rõ; provisional."
next_action: "Có thể commit b08. Coordinator giữ các thuật ngữ trong pending-terms.yml ở trạng thái provisional_non_canon."
```
