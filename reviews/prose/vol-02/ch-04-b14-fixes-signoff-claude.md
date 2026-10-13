# Báo cáo signoff sau sửa — vol-02-ch-04-b14 (Claude)

- Phạm vi: p000079–p000110 (32 đoạn), `translations/vol-02/ch-04-b14.jsonl`.
- Đã đọc: shared.md, reviewer.md, config, handoff b14, source package b14 (sha256 khớp handoff: 9ed89f95…), canon tham chiếu, `chapter4_b14_translation_proposals`, báo cáo review gốc, bản dịch. Không đọc lô khác.
- Kết luận: M1, M2, M3 đã xử lý đúng. Không còn lỗi nghiêm trọng hay vừa.

Mã đoạn viết tắt bằng số p; tiền tố đầy đủ là `YS-LN02/Text/part0024.xhtml/`.

## Trạng thái M1–M3

| Mục | Đoạn | Kết quả | Ghi chú |
|---|---|---|---|
| M1 | p000088 | Đã sửa | "Hô gọi nó đi." Dùng "nó" số ít cho một tàu, khớp nguồn "challenge it". |
| M1 | p000096 | Đã sửa | "Đã hô gọi rồi thì giờ không thể làm ngơ được." Không còn "dừng lại"; lệnh dừng/tắt động cơ chỉ xuất hiện ở p000100, 104. |
| M2 | p000107 | Đã sửa | "Rõ, thưa chỉ huy." Trung tính, nhất quán với "Chỉ huy!" ở p000082. |
| M3 | p000106 | Đã sửa | "Trung úy Weiss, đại đội của trung úy sẽ lên tàu." Không còn đại từ giới tính; "board" dịch "lên tàu". |

## Đại từ Tanya (tạm thời, không phải canon)

- "nó" cho Tanya ở p000084, 086, 089, 092, 093, 109: đã áp dụng đủ sáu đoạn, khớp DEC-P01-001 và b10–b13. Nội tâm dùng "mình" (p000080, 099).
- Lưu ý nhẹ: p000092 và p000093 đứng ngay sau p000091 (tàu *Lytol*), nên "nó" có thể bị đọc nhầm là con tàu, nhất là p000093 ("nó có thể cứ thế bỏ qua"). Không đổi nghĩa chính nên không tính lỗi vừa. Nếu muốn rõ hơn thì lặp "Tanya" ở p000093; nên tính trong lượt rà soát văn phong sau, không chặn signoff.
- Cô Serebryakov ở p000110 dùng "cô" theo "she" trong nguồn: hợp lệ, khác chủ thể.

## Dạng trung tính

- p000095 "Chỉ huy chắc chứ?": đạt.
- p000100 và p000104 "các vị": đạt, không còn "các anh".

## Lỗi còn lại

- Nghiêm trọng: 0. Vừa: 0.
- Nhẹ còn mở (chỉ ghi nhận, không chặn): F5 p000087 ("ai đó", "kiệt quệ"); F6 p000079 ("liên tục", "rồi thoát đi"); F7 p000086 ("phụ cấp" thay cho tiền làm thêm giờ, "hơi khâm phục… khó chịu"); F9 p000098 ("quyền khám xét" cho "board"); F10 p000109 ("đôi co pháp lý"); F11 "thuyền" ở p000082, 085, 089, 097; F12 p000100 "yêu cầu" yếu hơn "order"; thêm nhận xét nhẹ ở trên về p000092–093. Không đổi cốt truyện, không đổi nghĩa chính.

## Khuyến nghị thuật ngữ (đề xuất, không phải canon)

- Giữ tạm: Liên minh Entente; Khối Thịnh vượng chung; Trung úy; tàu chở hàng kiêm chở khách.
- Nên đồng loạt xét "boat/ship" → "tàu" thay cho "thuyền" khi rà soát thuật ngữ (F11).
- "Tiểu đoàn Pháp sư Không quân": giữ tạm, xét đồng loạt toàn dự án, không đổi riêng lô này.
- "nó" cho Tanya trong trần thuật: giữ tạm; vẫn pending, không nâng thành canon.
- Không có mục nào ảnh hưởng cốt truyện cần hỏi người dùng.

## Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-04-b14
state: done
segment_ids: [YS-LN02/Text/part0024.xhtml/p000079..p000110]
files_written: [reviews/prose/vol-02/ch-04-b14-fixes-signoff-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 0, minor: 8}
m_status: {M1: resolved, M2: resolved, M3: resolved}
unresolved_findings: []
term_recommendations:
  - keep_provisional: [Liên minh Entente, Khối Thịnh vượng chung, Trung úy, tàu chở hàng kiêm chở khách, nó (Tanya, trần thuật)]
  - review_project_wide: [Tiểu đoàn Pháp sư Không quân, boat/ship -> tàu]
review_path: reviews/prose/vol-02/ch-04-b14-fixes-signoff-claude.md
commit: null
next_action: signoff
```
