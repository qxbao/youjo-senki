# Báo cáo review — vol-02-ch-04-b14 (Claude)

- Phạm vi: p000079–p000110 (32 đoạn), `translations/vol-02/ch-04-b14.jsonl`.
- Đầu vào đã đọc: shared.md, reviewer.md, config, handoff b14, source package b14, canon (glossary, style-guide, characters, decisions, glossary-pending), `chapter4_b14_translation_proposals`.
- Kết luận chung: bản dịch đủ đoạn, không bỏ sót hay thêm ý lớn, đại từ nội tâm "mình" và nhấn mạnh `*...*` khớp nguồn (p000086, 087, 091, 100–105, 110). Không có lỗi nghiêm trọng. Có 3 lỗi vừa và 8 lỗi nhẹ cần người giữ quyền sửa xử lý.

Mã đoạn dưới đây viết tắt bằng số p; tiền tố đầy đủ là `YS-LN02/Text/part0024.xhtml/`.

## Lỗi vừa

1. **p000088 + p000096 — "challenge" bị dịch thành "gọi chúng" / "gọi họ dừng lại".**
   - Vấn đề: "challenge" ở đây là hô gọi/yêu cầu nhận dạng tàu. Bản dịch p000088 dùng "chúng" (số nhiều) cho một con tàu, nghĩa lại mơ hồ. Bản dịch p000096 thêm "dừng lại", trong khi nguồn chưa có lệnh dừng. Lệnh dừng và tắt động cơ chỉ đến ở p000100.
   - Căn cứ: nguồn p000088, p000096 và diễn tiến p000090–p000100. Quy tắc style-guide: không thay chỉ dẫn cụ thể bằng hành động suy ra.
   - Đề xuất: p000088 "Dù sao cũng không thể làm ngơ. Hô gọi nó đi." p000096 "Đã hô gọi rồi thì giờ không thể làm ngơ được." Giữ "nó" hoặc "con tàu", không dùng "chúng/họ" cho một tàu.

2. **p000107 — "ma'am" dịch thành "thưa bà".**
   - Vấn đề: "bà" gợi người lớn tuổi, không hợp quan hệ cấp trên–cấp dưới quân đội. Nó còn tự tạo quan hệ/tuổi tác mà nguồn không nêu (DEC-P01-001: không suy quan hệ).
   - Đề xuất trung tính theo quân đội: "Rõ, thưa chỉ huy." (nhất quán với "Chỉ huy!" ở p000082). Nếu sau này canon chốt cách xưng hô thì sửa theo canon.

3. **p000106 — "cô" gán giới tính cho Trung úy Weiss.**
   - Vấn đề: bản dịch viết "đại đội của cô", nhưng nguồn trong lô không nêu giới tính của Weiss và canon chưa có `characters.yml`. DEC-P01-001 cấm suy giới tính chỉ từ một đoạn.
   - Đề xuất: bỏ đại từ, ví dụ "Trung úy Weiss, đại đội của trung úy sẽ lên tàu." Việc đổi "ma'am" ở mục 2 độc lập với mục này.

## Lỗi nhẹ

4. **p000095 — "Cô chắc chứ?"**: nguồn không ghi người nói. Gán "cô" là suy diễn giới tính/quan hệ. Đề xuất "Chỉ huy chắc chứ?" (đối tượng được gọi là Chỉ huy ở p000082).
5. **p000087 — "couldn't imagine wanting to actively enter combat".** Bản dịch đổi thành "không hiểu nổi tại sao *ai đó* lại muốn…", thêm chủ thể thứ ba và đổi "không tưởng tượng nổi việc mình muốn" thành "không hiểu lý do". Đề xuất: "Tôi không tài nào tưởng tượng nổi việc muốn *chủ động* tham chiến." Câu sau, "hurting" chỉ mức thiệt hại. "Kiệt quệ" thiên về sức lực. Đề xuất "chưa bị thiệt hại nặng đến mức phải tránh giao chiến hoàn toàn".
6. **p000079 — thêm "liên tục", "rồi thoát đi".** Nguồn chỉ nói chỉ cần hai ngày dưới nước là tàu ngầm thoát được. "Liên tục" là chi tiết thêm. Đề xuất: "Chỉ cần hai ngày dưới nước và cố gắng một chút là chiếc tàu ngầm đó thoát được." Phần điều kiện sonar nên đặt cạnh vế "thả đi" để giữ logic.
7. **p000086 — "half-impressed and half-disgusted".** "Hơi khâm phục vừa thấy khó chịu" làm yếu và mất cân đối hai nửa. "Phụ cấp" nên là "tiền làm thêm giờ". Đề xuất: "nửa khâm phục, nửa ngán ngẩm… không được trả tiền làm thêm giờ".
8. **p000100 — "We order you" → "yêu cầu".** Mức độ yếu hơn "ra lệnh". Đề xuất "ra lệnh". "Các anh" (p000100, p000104) cũng gán giới tính cho thuỷ thủ đoàn; nên dùng "quý tàu" hoặc "các vị" nếu cần giữ trung tính.
9. **p000098 — "board" lúc dịch "khám xét", lúc "lên tàu".** Nguồn dùng "board" (p000094, p000098, p000106) và "inspection" tách biệt. Đề xuất giữ "lên tàu" cho board, "kiểm tra" cho inspection, để không mất cấu trúc lập luận pháp lý ("quyền lên tàu/khám xét" chỉ nên dùng nếu có lý do rõ).
10. **p000109 — "màn đôi co pháp lý".** "Đôi co" mang nghĩa cãi vặt, không phải "legal exchange". Đề xuất "màn trao đổi pháp lý".
11. **p000081, 082, 083, 089, 097 — "thuyền" so với "tàu".** Nguồn dùng "boat" cho cả con tàu Lytol (p000097). "Thuyền" gợi vật nhỏ, và bản dịch gọi cùng một con tàu là "thuyền" (p000097) rồi "con tàu" (p000098). Đề xuất dùng "tàu" xuyên suốt (ví dụ "tàu khả nghi"). Đây liên quan thuật ngữ, ghi trong term_recommendations.

## Đại từ cho Tanya (cần coordinator lưu ý, không tính là lỗi)

DEC-P01-001 quy định "nó" trong trần thuật Tanya "ở giai đoạn này" và cấm tự mở rộng sang giai đoạn khác. Lô này dùng "cô" cho Tanya (p000084, 086, 089, 092, 093, 109). Canon chưa có quyết định cho Vol 2 nên không xem là sai, nhưng coordinator cần đảm bảo lựa chọn nhất quán với các lô khác và ghi vào ledger.

## Điểm đã kiểm tra, không có lỗi

- Nội tâm "mình" (p000080, 099) và ngôi kể "tôi/chúng tôi" xen "Tanya/cô" khớp cách chuyển điểm nhìn của nguồn.
- Nhấn mạnh: *Lytol* ở p000091, 100–105; *actively* ở p000087; *plus* ở p000110; câu nội tâm in nghiêng ở p000086. Không thừa, không thiếu.
- Giữ phủ định, điều kiện, quy trình cảnh báo hai lần ở p000100–p000104 và đoạn kết p000110.
- Nguồn p000104 gọi Lytol là "tàu chiến của quốc gia trung lập" dù là tàu chở hàng/khách. Bản dịch trung thành nguồn; không sửa, chỉ ghi lưu ý là điểm bất thường của nguồn, không phỏng đoán lore.

## Năm lựa chọn thuật ngữ pending (đề xuất, không phải canon)

| id | Đề xuất của translator | Khuyến nghị của reviewer | Độ tin cậy |
|---|---|---|---|
| vol02-ch04-b14-entente-alliance | Liên minh Entente | Giữ tạm. Phương án thay thế "Liên minh Hiệp ước Entente" dài và thừa. Giữ nhất quán với ledger. | 0.6 |
| vol02-ch04-b14-cargo-passenger-ship | tàu chở hàng kiêm chở khách | Giữ tạm. Nghĩa chuẩn xác, tự nhiên. Có thể rút gọn "tàu hàng–khách" nếu cần khi lặp nhiều. Nên đổi "thuyền" → "tàu" cho các đoạn liên quan (xem mục 11). | 0.6 |
| vol02-ch04-b14-commonwealth | Khối Thịnh vượng chung | Giữ tạm, viết hoa như ledger. Chưa có căn cứ để đổi. | 0.6 |
| vol02-ch04-b14-aerial-mage-battalion | Tiểu đoàn Pháp sư Không quân | Giữ tạm cho nhất quán, nhưng ghi rủi ro: "Không quân" gợi quân chủng riêng, trong khi cùng đoạn p000100 đơn vị thuộc Lục quân/Bộ Tổng tham mưu. "Pháp sư Trên không" an toàn hơn về logic; nên xét đồng loạt toàn bộ dự án, không đổi riêng lô này. "203" có thể giữ không kèm "thứ". | 0.55 |
| vol02-ch04-b14-lieutenant | Trung úy | Giữ "Trung úy" làm phương án tạm tốt hơn "Thiếu úy". "Lieutenant" trần, không kèm "Second", ánh xạ tự nhiên sang Trung úy. Đây là suy luận từ ngữ cảnh chung, chưa phải canon. | 0.6 |

Không có mục nào ảnh hưởng cốt truyện cần hỏi người dùng.

## Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-04-b14
state: done
segment_ids: [YS-LN02/Text/part0024.xhtml/p000079..p000110]
files_written: [reviews/prose/vol-02/ch-04-b14-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 3, minor: 8}
commit: null
next_action: translator_fix_then_resign_off
```
