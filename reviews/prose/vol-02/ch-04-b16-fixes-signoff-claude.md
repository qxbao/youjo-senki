# Báo cáo signoff sau sửa vol-02-ch-04-b16 (Claude)

- Phạm vi: 32 đoạn `YS-LN02/Text/part0024.xhtml/p000141`–`p000172`. Mã đoạn viết tắt `pNNNNNN`.
- Đã đọc: shared.md, reviewer.md, config, handoff b16, package nguồn b16 (sha256 khớp handoff `835da13a…27c7ed`), canon tham chiếu, `chapter4_b16_translation_proposals`, báo cáo review gốc và `translations/vol-02/ch-04-b16.jsonl`. Không mở EPUB/PDF hay lô khác. Chỉ ghi báo cáo này. Mọi thuật ngữ là đề xuất tạm, không canon.
- Toàn vẹn: 32 dòng, đúng thứ tự mã đoạn p000141…p000172, không thiếu/thừa.

## Kết luận

V2, V3, V4 đã xử lý. V1 xử lý một phần: chủ thể Đế quốc/Khối Thịnh vượng chung đã tách rõ, nhưng cụm “đáng lẽ phải biết” vẫn còn, trái điều kiện nghiệm thu của coordinator. Còn 1 lỗi mức vừa (dư lượng V1) nên chưa signoff.

Đếm: nghiêm trọng 0, vừa 1, nhẹ 12 (N1–N12 cũ, không bắt buộc sửa).

## Kiểm tra V1–V4

| Mã | Đoạn | Kết quả | Căn cứ |
|---|---|---|---|
| V1 | p000162 | **Chưa đạt hoàn toàn** | Đã tách “Phía Đế quốc” (có mặt tại điểm hẹn) khỏi “Phía Khối Thịnh vượng chung” (vừa kịp chuyển giao), khớp p000163/p000165. Nhưng vế “chỉ một số ít người đáng lẽ phải biết” vẫn giữ “đáng lẽ phải biết”; trong tiếng Việt cụm này mang sắc thái phản thực tế (lẽ ra phải biết mà không biết/nên đã biết), dễ lệch khỏi ý “chỉ số ít người được biết”. |
| V2 | p000158 | Đạt | Thuyền trưởng nay là “Ông” ở cả ba chỗ, thống nhất với p000159–p000171; hết sắc thái “hắn”. |
| V3 | p000158 | Đạt | “những người hoạt động ngầm” khớp đề xuất pending (độ chắc thấp, không canon); hết “đám”. Chơi chữ mole/subterranean vẫn bị làm phẳng nhưng đã ghi nhận là rủi ro, không chặn. |
| V4 | p000157, p000158 | Đạt | `*Syrtis*` và `*Có một gián điệp cài trong cơ quan tình báo.*` đã khôi phục, khớp nguồn và DEC-P01-002; p000165 vẫn `*Lytol*`. |

## Phát hiện còn lại

- Vừa (V1-dư, p000162): bỏ “đáng lẽ phải biết”. Đề xuất giữ cấu trúc hiện tại, sửa vế sau: “Phía Đế quốc đã có mặt tại điểm hẹn mà chỉ một số ít người được biết.” (hoặc “…điểm hẹn vốn chỉ một số ít người biết”). Độ chắc ~0,7. Không ảnh hưởng cốt truyện.
- Nhẹ: N1–N12 như báo cáo gốc vẫn còn (p000142, 143, 144, 146, 150, 152, 154, 158 dấu chú thích 16, 160, 167, 171, 172). Không có lỗi nhẹ mới. Không phát hiện lỗi nghiêm trọng hoặc vừa mới do đợt sửa gây ra; p000158 liền mạch, p000162–p000163 chủ thể rõ.

## Đề xuất thuật ngữ (tạm, chưa canon)

- the subterranean = những người hoạt động ngầm; thay thế: người hoạt động bí mật; độ chắc ~0,45 (chỉ ngữ chưa rõ).
- Commonwealth = Khối Thịnh vượng chung; tàu ngầm lớp S; quả cầu tính toán; thuật thức nổ mạnh: giữ như ledger.
- Thuật ngữ mới gợi ý ghi pending (độ chắc thấp): Bộ Hải quân (Office of the Admiralty), tàu phụ trợ, bảng thông số khai hỏa, nhật ký đơn vị, sĩ quan hàng hải (cân nhắc “sĩ quan dẫn đường”).
- Không có mục ảnh hưởng cốt truyện cần hỏi người dùng.

## YAML cho coordinator

```yaml
role: reviewer
task_id: vol-02-ch-04-b16-review-signoff
state: done
review_path: reviews/prose/vol-02/ch-04-b16-fixes-signoff-claude.md
segment_ids:
  - YS-LN02/Text/part0024.xhtml/p000141..p000172 (32)
counts:
  serious: 0
  moderate: 1
  minor: 12
v_status:
  V1: partial_unresolved   # p000162 tách chủ thể được, nhưng còn "đáng lẽ phải biết"
  V2: resolved
  V3: resolved
  V4: resolved
files_written:
  - reviews/prose/vol-02/ch-04-b16-fixes-signoff-claude.md
validator: not_run
diff_check: not_run
findings:
  - {severity: moderate, segment_id: p000162, issue: "còn 'đáng lẽ phải biết' (sắc thái phản thực tế) dù đã tách chủ thể", resolution: "đổi thành 'được biết'/'biết' như đề xuất"}
unresolved_findings: [V1-residual p000162]
term_recommendations:
  - {source_term: the subterranean, proposed_vi: những người hoạt động ngầm, alternatives: [người hoạt động bí mật], segment_ids: [p000158], status: pending, confidence: 0.45}
risks:
  - "Chơi chữ mole/subterranean bị làm phẳng; chú thích 16 chưa giữ (chưa có quyết định về chú thích)"
commit: null
next_action: translator_fix_v1_residual_then_resignoff
```
