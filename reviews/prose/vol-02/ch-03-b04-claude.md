# Báo cáo phản biện — vol-02-ch-03-b04 (checkpoint_generation 477)

- Phạm vi: 20 đoạn, p000080–p000099 của `YS-LN02/Text/part0016.xhtml`.
- Source package: `work/vol-02/batches/ch-03-b04-source.jsonl`, SHA-256 `86fceedd…a4517`, khớp handoff.
- Canon đã đối chiếu: các hash canon khớp handoff (glossary, style-guide, characters, decisions, glossary-pending); sổ `work/run-state/pending-terms.yml` chỉ tra các mục liên quan.
- Kết luận: không có lỗi nghiêm trọng hay vừa. Có 7 lỗi nhẹ, không lỗi nào chặn việc hoàn tất lô. Nghĩa, phủ định, chủ thể và logic nhìn chung được giữ đúng; không phát hiện thêm hay bớt nội dung đáng kể, ngoài các điểm nêu dưới đây.

## Xác minh cờ nhấn mạnh p000093 (DEC-P01-002)

- Nguồn có đúng một đoạn nhấn mạnh, gồm một từ đơn nằm trong cụm trích dẫn nói về việc phía Bắc “vẫn còn chiến đấu”. Đoạn này không có nhấn mạnh nào khác.
- Bản dịch dùng `*vẫn*`, tức đúng một từ tương ứng, không rộng hơn hay hẹp hơn. Không có `*...*` nào ở đoạn khác trong lô và nguồn cũng không có nhấn mạnh khác. **Đạt.**
- Lỗi nhẹ đi kèm: xem F1 (mất dấu ngoặc kép của cụm trích dẫn).

## Phát hiện

| # | segment_id | Mức | Vấn đề | Căn cứ | Đề xuất |
|---|---|---|---|---|---|
| F1 | p000093 | nhẹ | Nguồn đặt cụm “still fighting up there” trong dấu ngoặc kép (lời chỉ trích được trích lại). Bản dịch bỏ dấu ngoặc nên mất sắc thái trích dẫn. | So sánh nguồn và bản dịch. Phạm vi nhấn mạnh vẫn đúng. | Viết thành “*vẫn* còn chiến đấu ở đó” trong ngoặc kép, giữ nguyên `*vẫn*`. |
| F2 | p000081 | nhẹ (cần coordinator quyết) | Nguồn có chỉ mục chú thích số 8 sau cụm “harassing attacks”. Bản dịch không giữ dấu chú thích. | Style-guide yêu cầu ghi lựa chọn về chú thích vào `decisions.md`; chưa có quyết định nào. Không thể coi là lỗi dịch nhưng là thông tin bị bỏ. | Coordinator quyết định chung cách xử lý chỉ mục chú thích cho cả quyển. Nếu chưa có quyết định, ghi lại là rủi ro. Không sửa trong lô này nếu chưa có quy ước. |
| F3 | p000089, p000090 | nhẹ | Trần thuật theo điểm nhìn Schreise gọi Tanya là “cô”, trong khi p000082 (nội tâm Tanya/trần thuật) dùng “nó” theo DEC-P01-001. Đổi theo điểm nhìn là hợp lý, nhưng đây là ranh giới áp dụng quyết định. | DEC-P01-001 chỉ quy định “nó” cho trần thuật về Tanya ở giai đoạn này và không cho mở rộng tự động. Tôi không đọc các lô khác nên không xác nhận được mức nhất quán toàn chương. | Coordinator đối chiếu với cách các lô cùng chương xử lý điểm nhìn Schreise. Nếu nhất quán thì giữ; nếu không thì chọn một cách thống nhất (đề xuất tạm: giữ “cô” cho điểm nhìn các sĩ quan Đế quốc, ghi vào ledger). |
| F4 | p000089 | nhẹ | “matter-of-fact” dịch là “khách quan”, hơi lệch: ý là giọng điệu thản nhiên, thực dụng, không phải sự vô tư. | Ngữ nghĩa nguồn. | “giọng điệu khá thản nhiên/thực tế”. |
| F5 | p000090 | nhẹ | “with obvious displeasure” được dịch thành “cơn giận”, mạnh hơn nguồn, và sắc thái “lộ rõ” mất. | Ngữ nghĩa nguồn. | “nén lại ý muốn quát át cô, vẻ bất mãn lộ rõ; nét mặt như muốn nói họ không tin vào kế hoạch này”. |
| F6 | p000083 | nhẹ | “quá lớn rủi ro” được thay bằng “canh bạc quá lớn”, thêm ẩn dụ cờ bạc không có ở nguồn. | Ngữ nghĩa nguồn. | “một rủi ro quá lớn”. |
| F7 | p000092 vs p000099 | nhẹ | “ban Hậu cần” (p000092) so với “Cục Tác chiến” (p000099) và ledger tạm dùng “Cục Hậu cần”/“Cục Tác chiến”. Ở các đoạn còn lại dùng “Hậu cần”/“Tác chiến” trần, nên cấp tổ chức lệch nhau trong cùng lô. | `vol02-ch01-b15-operations` và `vol02-ch01-b15-service-corps`/`vol02-ch03-b01-service-corps` trong ledger (tạm, chưa canon). | Dùng “bộ phận/phía Hậu cần” thay cho “ban Hậu cần”, hoặc “Cục Hậu cần” nếu cùng thực thể; giữ nhất quán với ledger. |

## Rà soát theo hạng mục

- **Nghĩa/thiếu-thừa:** đạt, trừ các điểm F4–F6. Phủ định, đối tượng câu hỏi (p000088), thì giả định (p000080), “That must have meant…” (p000099) đều giữ đúng. “chỉ trong sáu tuần” (p000093) thêm “chỉ” để nhấn mạnh sự nhanh chóng; chấp nhận được vì hàm ý của nguồn.
- **Đại từ/chủ thể:** “ông ấy” ở p000081 chưa rõ chủ thể, giống nguồn nên giữ mơ hồ là đúng. Trần thuật Schreise dùng “ông”, Rudersdorf là “ông ta”, “người này”; phù hợp. Nội tâm Tanya dùng “mình” đúng DEC-P01-001; p000082 “nó” + “đơn vị mình” hơi lẫn nhưng chấp nhận được. Với p000088 (sĩ quan Hậu cần gọi Tanya là “cô”) không có căn cứ để đổi.
- **Nhấn mạnh:** chỉ một điểm, đạt (xem trên).
- **Văn phong:** liền mạch, đúng giọng. Chuyển thì hiện tại/quá khứ của nguồn được làm mượt, không lệch nghĩa.
- **Thuật ngữ:** “Cụm tập đoàn quân phương Bắc”, “Đại Quân”, “Liên minh Entente”, “Trung ương”, “bộ chỉ huy tối cao”, “Hậu cần”, “Tác chiến” nhất quán với ledger tạm. Một điểm cần ghi: p000099 dịch “high command” là “Bộ chỉ huy tối cao”, trong khi ledger tạm (`vol02-ch02-b12-high-command`) đề xuất “bộ chỉ huy cấp cao” để tránh ngụ ý Bộ Tổng tư lệnh; xem đề xuất bên dưới.

## Đề xuất thuật ngữ (tạm, chưa canon)

```yaml
- source_term: high command
  proposed_vi: bộ chỉ huy cấp cao
  alternatives_vi: [Bộ chỉ huy tối cao]
  segment_ids: [YS-LN02/Text/part0016.xhtml/p000099]
  status: pending
  rationale: Khớp mục ledger vol02-ch02-b12-high-command, tránh ngụ ý Bộ Tổng tư lệnh khi nguồn không rõ.
- source_term: Logistics / Operations (staff)
  proposed_vi: phía Hậu cần / phía Tác chiến; Cục Tác chiến khi chỉ cơ quan
  segment_ids: [p000088, p000090, p000092, p000099]
  status: pending
  rationale: Khớp ledger vol02-ch01-b15; bỏ "ban" ở p000092 để nhất quán.
- source_term: Commander Ragheno
  proposed_vi: Chỉ huy Ragheno
  segment_ids: [YS-LN02/Text/part0016.xhtml/p000099]
  status: pending
  rationale: Không đủ căn cứ về cấp bậc trong lô này; giữ chức danh trung tính, không tự suy cấp bậc.
```

Không có mục nào ảnh hưởng cốt truyện cần hỏi người dùng.
