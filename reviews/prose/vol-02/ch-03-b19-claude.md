# Báo cáo phản biện — vol-02-ch-03-b19

- Người phản biện: Claude (reviewer). Phạm vi: 23 đoạn p000335–p000357 của `YS-LN02/Text/part0018.xhtml`.
- checkpoint_generation theo yêu cầu: 641. Lưu ý: `handoffs/vol-02/ch-03-b19.yml` còn ghi 640, coordinator nên đối chiếu với checkpoint thực.
- Đầu vào đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b19, `canon/style-guide.md`, `canon/decisions.md`, `canon/glossary*.yml`, các mục liên quan trong `work/run-state/pending-terms.yml`, gói nguồn b19 (hash khớp handoff: `ebdd7e80…1182f4`), và `translations/vol-02/ch-03-b19.jsonl`. Không mở EPUB/PDF, gói khác hay bản dịch lô khác.
- Mã đoạn dưới đây viết tắt `pNNNNNN`, thuộc `YS-LN02/Text/part0018.xhtml/`.

## Tổng quan

Bản dịch bám sát nghĩa, đủ 23 đoạn, không thấy bỏ sót hay thêm ý lớn. Phủ định, số lượng (7 chọi 7 → 10 chọi 7), thứ tự thời gian và các mệnh đề giả định ở p000350 đều đúng. Đại từ "họ" nhất quán, không suy diễn quan hệ. In nghiêng ở p000352 và p000355 đúng phạm vi nguồn (DEC-P01-002). Văn phong trôi chảy, hợp giọng quân sự.

Vấn đề đáng sửa gồm 3 lỗi mức vừa (một thuật ngữ lệch sổ pending, một giả định quá khứ bị mất thì, một chỗ lệch nghĩa ở đoạn cuối) và một số lỗi nhẹ.

## Đếm theo mức

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 3 |
| Nhẹ | 11 |

## Lỗi mức vừa

### V1 — p000342: "pháp sư hải quân" lệch với đề xuất đã ghi trong sổ pending
- **Vấn đề:** bản dịch dùng "pháp sư hải quân", trong khi mục `vol02-ch03-b19-marine-mages` ghi `proposed_vi` là "pháp sư thủy quân lục chiến" (theo gốc đã dùng ở b15). Văn bản và sổ không khớp. Từ "hải quân" còn trùng với "Hải quân Đế quốc" ở p000356, nên dễ nhập nhằng giữa lực lượng thủy binh và hải quân.
- **Căn cứ:** b14 từng đề xuất "pháp sư hải quân" (độ tin cậy 0,5), b15 chuyển sang gốc "thủy quân lục chiến" để tách khỏi hải quân. Ngữ cảnh b19 chưa đủ để lật lại lựa chọn đó: các pháp sư này xuất kích cùng hạm đội, và p000351 xin pháp sư lục quân chi viện, tức là pháp sư thuộc một quân chủng khác. Cách đọc "pháp sư thuộc hạm đội" cũng hợp lý, nên độ bất định còn cao.
- **Đề xuất sửa:** đổi p000342 thành "pháp sư thủy quân lục chiến" để thống nhất với b15 và sổ pending. Giữ "pháp sư hải quân" làm phương án thay thế. Chỉ là đề xuất tạm, không thành canon; ghi độ tin cậy khoảng 0,5.

### V2 — p000348: mất thì và tính phản thực tế của giả định quá khứ
- **Vấn đề:** nguồn là giả định phản thực tế ở quá khứ, về việc Đế quốc đã không chọn Hạm đội Eo biển làm đối thủ. Bản dịch "Nếu Đế quốc chọn họ làm đối thủ…, có lẽ họ vẫn cản trở được" đọc như khả năng ở hiện tại hoặc tương lai, vi phạm quy tắc giữ thời gian của giả định trong `style-guide.md`. Ngoài ra "cut" nên được hiểu là bị hạ gục/xé nát, còn "đánh tan" hơi lệch về hướng bị đánh bại, ít hàm ý bị tiêu diệt.
- **Đề xuất sửa:** "Nếu trong tình thế ấy Đế quốc đã chọn họ làm đối thủ, thì dù rốt cuộc họ có bị hạ gục, có lẽ họ cũng đã làm hỏng được mục tiêu của Đế quốc."
- **Phương án thay thế:** "…thì dù cuối cùng có bị xé nát, họ vẫn có thể đã cản được mục tiêu của Đế quốc."

### V3 — p000357: "không hề rối loạn" lệch nghĩa
- **Vấn đề:** nguồn nói bản thân văn phòng (không gian làm việc) không có gì khó chịu, mà sự khó chịu đến từ tâm trạng của vị thiếu tướng, tức cách nói "không ở trạng thái tồi tệ". "Rối loạn" gợi sự hỗn loạn, mất trật tự, là một nghĩa khác và làm mạch "không phải văn phòng… mà là tâm trạng ông chủ" kém rõ.
- **Đề xuất sửa:** "Thế nhưng bản thân văn phòng không có gì bất ổn." hoặc "…không có gì đáng phàn nàn."
- **Phương án thay thế:** "Thế nhưng bản thân văn phòng không hề ảm đạm."
- Cùng đoạn: "Tình thế ngày càng xấu đi, nỗi khổ sở vì vậy lớn đến mức…" thêm quan hệ "vì vậy" không có trong nguồn (nguồn là danh ngữ: nỗi đau của tình thế xấu đi). Nên chỉnh: "Nỗi khổ sở trước tình thế ngày càng xấu đi lớn đến mức dập tắt cả hy vọng…".

## Lỗi mức nhẹ

- **N1 — p000347:** nguồn in nghiêng tên tàu *Helgoland* (soái hạm); bản dịch để thường. Theo DEC-P01-002 nên viết `*Helgoland*`. "lớp Helgoland" giữ thường là đúng.
- **N2 — p000349:** "mọi chuyện đều vô vọng" mở rộng phạm vi: nguồn nói chính hy vọng ấy trở nên vô ích. Gợi ý: "hy vọng ấy trở nên vô ích". Thành ngữ "giao chiến trực diện" làm mất sắc thái cận chiến sống mái, có thể dùng "giáp lá cà" hoặc "đối đầu cận chiến" nếu muốn giữ hình ảnh.
- **N3 — p000352:** "Chỉ còn cách làm được thôi" khó hiểu. Nguồn là quyết tâm phải kịp. Gợi ý: "*Nhất định phải kịp.*" hoặc "*Phải kịp thôi.*" (vẫn in nghiêng, đúng phạm vi nguồn).
- **N4 — p000356:** "vịnh Osfjord" thêm "vịnh" không có trong nguồn, dư với "fjord" trong tên. Sổ b17 đề xuất giữ "Osfjord" (phương án thay thế "vịnh hẹp Os"). Đề xuất: "Osfjord".
- **N5 — p000355:** "siết chặt nắm đấm" thay cho động tác giơ nắm đấm, và "tóm được chúng" ngả sang bắt giữ, trong khi lời thề là báo thù/đánh bại. Gợi ý: "giơ nắm đấm" (hoặc "nắm chặt tay" nếu muốn tự nhiên hơn); "chúng ta sẽ hạ được chúng" hoặc "cho chúng biết tay".
- **N6 — viết hoa:** "Hạm đội Đế quốc" (p000336) so với "hạm đội Đế quốc" (p000349) cho cùng một cụm nguồn viết thường; "Khối Thịnh Vượng Chung" (p000341, p000357) khác với sổ pending "Khối Thịnh vượng chung". Nên thống nhất theo sổ.
- **N7 — p000344:** "tuyến ngăn chặn" tạm chấp nhận; "tuyến kiềm chế" sát hơn với ý ghìm chân hạm đội không cho xuất kích. Tùy chọn.
- **N8 — p000345, p000347:** tên hạm đội mới chưa có mục riêng trong sổ b19: "Hạm đội Eo biển" (Channel Fleet) và "Hạm đội Biển khơi" (High Seas Fleet). Riêng Northern Sea Fleet dùng "Hạm đội Biển Bắc", là phương án thay thế của mục b12 (`proposed_vi` là "Hạm đội Bắc Hải"); bản dịch không ghi lý do. Đề xuất tạm: giữ ba cách gọi hiện tại (đối xứng, dễ đọc, tránh trùng địa danh Bắc Hải) và coordinator ghi vào sổ, đồng thời đối chiếu với cách dùng ở b12. Không suy diễn lore.
- **N9 — p000351:** nguồn dùng "the capital ship" ở số ít, chỉ một chiếc xác định, nhưng bản dịch để danh từ không lượng từ. Gợi ý "chiếc tàu chiến chủ lực" mà không gán là tàu địch hay tàu ta.
- **N10 — p000340:** "ưu thế lục quân" nên là "ưu thế lực lượng mặt đất" (nguồn là ground forces chứ không phải quân chủng Army).
- **N11 — p000341:** "trong vòng bí mật tuyệt đối" gượng. Gợi ý: "trong tuyệt mật" hoặc "được giữ tuyệt mật".

## Thuật ngữ

| Thuật ngữ | Đoạn | Bản dịch hiện tại | Lựa chọn tạm | Thay thế | Ghi chú |
|---|---|---|---|---|---|
| marine mages | p000342 | pháp sư hải quân | pháp sư thủy quân lục chiến | pháp sư hải quân | Đồng bộ b15 và sổ pending; độ tin cậy ~0,5; chưa rõ quan hệ tổ chức với hạm đội. |
| capital ships | p000347, p000351 | tàu chiến chủ lực | tàu chiến chủ lực | tàu chủ lực | Chấp nhận; "tàu chủ lực" ngắn hơn, đều tự nhiên; độ tin cậy ~0,55. |
| Channel Fleet / High Seas Fleet | p000345 | Hạm đội Eo biển / Hạm đội Biển khơi | giữ nguyên | — | Chưa có mục sổ; đề xuất ghi mới, không canon. |
| Northern Sea Fleet | p000345, p000347 | Hạm đội Biển Bắc | Hạm đội Biển Bắc | Hạm đội Bắc Hải | Cần đồng bộ với mục b12. |
| Osfjord | p000356 | vịnh Osfjord | Osfjord | vịnh hẹp Os | Theo mục b17. |

Không có quyết định nào ảnh hưởng cốt truyện nên không cần hỏi người dùng.

## Ghi chú còn tồn đọng cho coordinator

- V1–V3 cần translator sửa trước khi đóng lô; N1–N5 nên sửa cùng lượt; N6–N11 là tùy chọn.
- Cập nhật sổ pending: đồng bộ mục marine mages; thêm mục tên hạm đội (N8) và lý do chọn "Biển Bắc".
- Lệch số checkpoint_generation giữa yêu cầu (641) và handoff (640).

```yaml
role: reviewer
task_id: vol-02-ch-03-b19
state: done
segment_ids:
  - YS-LN02/Text/part0018.xhtml/p000335..p000357
review_path: reviews/prose/vol-02/ch-03-b19-claude.md
files_written:
  - reviews/prose/vol-02/ch-03-b19-claude.md
validator: not_run
diff_check: not_run
counts:
  serious: 0
  moderate: 3
  minor: 11
findings:
  - {severity: moderate, segment_id: YS-LN02/Text/part0018.xhtml/p000342, issue: "pháp sư hải quân lệch với đề xuất sổ pending và gốc b15", resolution: "đổi thành pháp sư thủy quân lục chiến (tạm)"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0018.xhtml/p000348, issue: "mất thì phản thực tế quá khứ của giả định", resolution: "dùng 'đã chọn' và 'cũng đã làm hỏng được'"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0018.xhtml/p000357, issue: "'không hề rối loạn' lệch nghĩa; thêm 'vì vậy'", resolution: "'không có gì bất ổn'; bỏ quan hệ nhân quả thêm vào"}
unresolved_findings: 3
term_recommendations:
  - {source_term: marine mages, proposed_vi: "pháp sư thủy quân lục chiến", alternatives: ["pháp sư hải quân"], segment_ids: [p000342], status: pending, confidence: 0.5}
  - {source_term: capital ships, proposed_vi: "tàu chiến chủ lực", alternatives: ["tàu chủ lực"], segment_ids: [p000347, p000351], status: pending, confidence: 0.55}
  - {source_term: Channel Fleet / High Seas Fleet, proposed_vi: "Hạm đội Eo biển / Hạm đội Biển khơi", alternatives: [], segment_ids: [p000345], status: pending, confidence: 0.5}
  - {source_term: Northern Sea Fleet, proposed_vi: "Hạm đội Biển Bắc", alternatives: ["Hạm đội Bắc Hải"], segment_ids: [p000345, p000347], status: pending, confidence: 0.5}
  - {source_term: Osfjord, proposed_vi: "Osfjord", alternatives: ["vịnh hẹp Os"], segment_ids: [p000356], status: pending, confidence: 0.45}
risks:
  - "handoff ghi checkpoint_generation 640, yêu cầu review ghi 641"
  - "tên hạm đội chưa có mục sổ b19; Northern Sea Fleet dùng phương án thay thế của b12"
commit: null
next_action: translator_fix_then_recheck
```
