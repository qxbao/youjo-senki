# Báo cáo signoff cuối vol-02-ch-04-b16 (Claude)

- Phạm vi: 32 đoạn `YS-LN02/Text/part0024.xhtml/p000141`–`p000172`. Mã đoạn viết tắt `pNNNNNN`.
- Đã đọc: shared.md, reviewer.md, config, handoff b16, package nguồn b16 (sha256 khớp handoff `835da13a…27c7ed`), canon tham chiếu (DEC-P01-001/002), `chapter4_b16_translation_proposals`, báo cáo review gốc, báo cáo signoff trước và `translations/vol-02/ch-04-b16.jsonl`. Không mở EPUB/PDF hay lô khác. Chỉ ghi báo cáo này. Mọi thuật ngữ là đề xuất tạm, không canon.
- Toàn vẹn: 32 dòng, đúng thứ tự p000141…p000172, không thiếu/thừa; status `draft`.

## Kết luận

V1–V4 đều đã xử lý. Không còn lỗi nghiêm trọng hay vừa. Đủ điều kiện signoff.

Đếm: nghiêm trọng 0, vừa 0, nhẹ 12 (N1–N12 cũ, không bắt buộc sửa, không chặn).

## Kiểm tra V1–V4

| Mã | Đoạn | Kết quả | Căn cứ |
|---|---|---|---|
| V1 | p000162 | Đạt | Cụm “đáng lẽ phải biết” đã bỏ; nay là “Phía Đế quốc đã có mặt tại điểm hẹn vốn chỉ một số ít người biết đến”. Vẫn tách rõ “Phía Đế quốc” (có mặt tại điểm hẹn) khỏi “Phía Khối Thịnh vượng chung” (vừa kịp chuyển giao), khớp p000163/p000165. |
| V2 | p000158 | Đạt | Thuyền trưởng là “Ông” nhất quán, thống nhất với p000159–p000171. |
| V3 | p000158 | Đạt | “những người hoạt động ngầm” khớp đề xuất pending (độ chắc 0,4, không canon). Chơi chữ mole/subterranean còn bị làm phẳng nhưng đã ghi nhận là rủi ro. |
| V4 | p000157, p000158 | Đạt | `*Syrtis*` và `*Có một gián điệp cài trong cơ quan tình báo.*` đã khôi phục theo DEC-P01-002; p000165 vẫn `*Lytol*`. |

## Phát hiện còn lại

- Nhẹ: N1–N12 như báo cáo gốc (p000142, 143, 144, 146, 150, 152, 154, 158 dấu chú thích 16, 160, 167, 171, 172). Không có lỗi nhẹ mới. Không thấy lỗi nghiêm trọng/vừa mới do các đợt sửa gây ra.

## Đề xuất thuật ngữ (tạm, chưa canon)

- the subterranean = những người hoạt động ngầm; thay thế: người hoạt động bí mật, những kẻ hoạt động dưới lòng đất; độ chắc ~0,4.
- Commonwealth = Khối Thịnh vượng chung; tàu ngầm lớp S; quả cầu tính toán; thuật thức nổ mạnh: giữ như ledger.
- Thuật ngữ gợi ý ghi pending (độ chắc thấp): Bộ Hải quân, tàu phụ trợ, bảng thông số khai hỏa, nhật ký đơn vị, sĩ quan hàng hải (cân nhắc “sĩ quan dẫn đường”).
- Không có mục ảnh hưởng cốt truyện cần hỏi người dùng.

## YAML cho coordinator

```yaml
role: reviewer
task_id: vol-02-ch-04-b16-final-signoff
state: done
review_path: reviews/prose/vol-02/ch-04-b16-final-signoff-claude.md
segment_ids:
  - YS-LN02/Text/part0024.xhtml/p000141..p000172 (32)
counts:
  serious: 0
  moderate: 0
  minor: 12
v_status:
  V1: resolved
  V2: resolved
  V3: resolved
  V4: resolved
files_written:
  - reviews/prose/vol-02/ch-04-b16-final-signoff-claude.md
validator: not_run
diff_check: not_run
findings: []
unresolved_findings: []
term_recommendations:
  - {source_term: the subterranean, proposed_vi: những người hoạt động ngầm, alternatives: [người hoạt động bí mật, những kẻ hoạt động dưới lòng đất], segment_ids: [p000158], status: pending, confidence: 0.4}
risks:
  - "Chơi chữ mole/subterranean bị làm phẳng; chú thích 16 chưa giữ (chưa có quyết định về chú thích)"
commit: null
next_action: signoff
```
