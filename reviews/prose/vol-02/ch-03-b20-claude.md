# Báo cáo phản biện — vol-02-ch-03-b20

- Người phản biện: Claude (reviewer). Phạm vi: 22 đoạn p000358–p000379 của `YS-LN02/Text/part0018.xhtml`.
- checkpoint_generation theo yêu cầu: 651. Lưu ý: `handoffs/vol-02/ch-03-b20.yml` còn ghi 650; coordinator nên đối chiếu với checkpoint thực.
- Đầu vào đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b20, `canon/style-guide.md`, `canon/decisions.md`, `canon/glossary.yml`, `canon/characters.yml`, `canon/glossary-pending.yml` (không có mục liên quan), các mục liên quan trong `work/run-state/pending-terms.yml` (khối `chapter3_b20_translation_proposals` và các mục councilor, radio operator, Major General, General address, Commonwealth, Entente Alliance, Dacia), gói nguồn b20 (sha256 tính lại khớp `source_package_sha256` trong handoff: `3cab7e43…1371ba2aa`) và `translations/vol-02/ch-03-b20.jsonl`. Không mở EPUB/PDF, gói khác hay bản dịch lô khác. Một ít dòng sổ pending lô khác chỉ được đọc để đối chiếu thuật ngữ.
- Mã đoạn dưới đây viết tắt `pNNNNNN`, thuộc `YS-LN02/Text/part0018.xhtml/`.

## Tổng quan

Bản dịch bám sát nghĩa, đủ 22 đoạn, không thấy bỏ sót hay thêm ý lớn. Phủ định ("không phải tin xấu", "không phải gọi riêng tàu của cơ quan tình báo") đúng. Italic tên tàu *Lytol* ở p000360 và p000373 đúng phạm vi nguồn (DEC-P01-002); không có nhấn mạnh thừa. Văn phong trôi chảy, hợp giọng quân sự. Cả 22 đoạn đều có `translation`, `status`, hash và glossary_version khớp handoff.

Có 3 lỗi mức vừa (chủ thể bị mờ ở p000367, cấp bậc cụ thể hóa ở p000369, mức chắc chắn bị nâng ở p000371) và một số lỗi nhẹ. Hai thuật ngữ lệch sổ pending đã có trước (councilor, radio operator) cũng cần đồng bộ.

## Đếm theo mức

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 3 |
| Nhẹ | 12 |

## Lỗi mức vừa

### V1 — p000367: "người nhận điện" gây nhầm chủ thể
- Vấn đề: nguồn nói theo điểm nhìn của người được báo cáo (vị sĩ quan cấp trên), không phải người đã giải mã điện. Trong bản dịch, "người nhận điện" ngay sau các đoạn nói về người điện báo (p000362–p000363, người nhận và giải mã điện từ tàu) dễ bị hiểu là chính người điện báo. Đoạn p000369 sau đó mới nói rõ người điện báo hiểu sự nghi ngờ của cấp trên, nên p000367 nên đọc là suy nghĩ của cấp trên.
- Căn cứ: ngữ cảnh p000366 (lời hỏi về Bộ Ngoại giao) và p000369 (nêu "cấp trên"/tên tướng). Không suy diễn quan hệ khác (DEC-P01-001, giới hạn suy luận).
- Sửa tạm tốt nhất: đổi thành "người nghe báo cáo" hoặc "người được báo cáo". Ví dụ: "Nhưng với người đang nghe báo cáo, việc này dường như nằm ngoài thẩm quyền của họ."
- Phương án thay thế nếu coordinator muốn bám sát hơn: "người tiếp nhận thông điệp" (kém tự nhiên hơn).

### V2 — p000369: "Thiếu tướng Habergram" cụ thể hóa cấp bậc
- Vấn đề: nguồn chỉ gọi vị này bằng cấp bậc chung "General", không có "Major". Bản dịch chọn "Thiếu tướng" (Major General) mà nguồn không nêu. Sổ pending có mục Major General → Thiếu tướng (vol02 ch01 b14/b16) và mục address "General" → "Tướng" (ch03 b01); không mục nào gán Habergram với cấp Major General. Trong bản b20, đây là cấp bậc suy từ một mục khác chứ không từ nguồn.
- Sửa tạm tốt nhất: "Tướng Habergram" (hình thức trung tính, khớp mục address "General" → "Tướng" và nguyên tắc "không ngụ ý cấp bậc khác"). Không đưa vào canon.
- Phương án thay thế: "tướng Habergram" (viết thường) nếu coordinator muốn coi đây là chức danh chung. Nếu coordinator có căn cứ khác (ví dụ lô trước đã xác định Habergram là Thiếu tướng), nên ghi rõ vào sổ và giữ nhất quán; khi đó đây chỉ còn là lỗi nhẹ. Độ tin cậy lựa chọn: 0,5. Không ảnh hưởng cốt truyện.

### V3 — p000371: nâng mức chắc chắn của suy đoán
- Vấn đề: nguồn là suy luận có giới hạn ("tôi chỉ có thể nghĩ là…"). Bản dịch viết "chắc chắn ở đâu đó đã có một lỗ hổng", nâng suy đoán thành khẳng định và đổi "đang có" thành "đã có". Theo style guide, phải giữ mức chắc chắn.
- Sửa tạm tốt nhất: "Nếu vậy thì tôi chỉ nghĩ được rằng ở đâu đó chúng ta đang có một lỗ hổng an ninh nghiêm trọng." Gọn hơn: "Nếu vậy thì chỉ có thể là ở đâu đó đang có một lỗ hổng an ninh nghiêm trọng."
- Phương án thay thế: "Nếu vậy thì hẳn là…" (nhẹ hơn "chắc chắn", vẫn là suy đoán), nhưng ít sát hơn.

## Lỗi mức nhẹ

- **N1 — p000359:** "Đã bao nhiêu ngày rồi anh mới gần như chạy đi báo tin…" làm lệch trục thời gian: nguồn hỏi đã bao lâu kể từ lần trước, bản dịch đọc như "bao lâu thì mới có lần này". Gợi ý: "Đã bao nhiêu ngày kể từ lần anh phải gần như chạy đi báo cấp trên thế này? Kể từ khi Dacia thất thủ ư?" Ngoài ra "sở thích cá nhân" cho thích/ghét dễ hiểu thành sở thích; đề xuất "chuyện thích hay ghét".
- **N2 — p000358:** "mất chức" làm nhẹ hình ảnh "đầu sẽ rơi"; gợi ý "sẽ có người bị trừng phạt ngay" hoặc "có người sẽ mất đầu". Chọn nghĩa nào cũng được; không đổi cốt truyện.
- **N3 — p000362:** "tàu buôn vũ trang" bỏ "tuần dương"; đề xuất "tàu tuần dương thương mại vũ trang" nếu coordinator muốn đầy đủ, và ghi vào sổ. "mật mã dùng một lần" là cách diễn đạt chấp nhận được cho tạm thời; xem phần thuật ngữ.
- **N4 — p000363:** "anh không chắc có gì đáng mừng lắm" chuyển đối tượng nghi ngờ từ "nó có đáng mừng không" sang "có gì đáng mừng không". Gợi ý: "anh không chắc đó có phải điều đáng mừng lắm hay không, nhưng thôi."
- **N5 — p000364, p000365:** "đưa … đi nơi khác" thêm điểm đến/hành động mà nguồn không nêu (nguồn chỉ nói vận chuyển). Gợi ý: "vận chuyển một nhân vật quan trọng" hoặc "đưa đón một nhân vật quan trọng" (cả hai đoạn, giữ nhất quán).
- **N6 — p000365:** "Hội đồng Nhà nước" viết hoa như một cơ quan cụ thể; nguồn là chức danh councilor of state. Sổ pending (ch02 b02) dùng "Nghị viên" cho councilor; hai mục này nên đồng bộ. Đề xuất tạm: "mười nghị viên nhà nước" (ngụ ý theo mục councilor), thay thế: "mười ủy viên nhà nước". Không suy diễn lore về cơ quan.
- **N7 — p000365:** "Như vậy vẫn tốt hơn" bỏ "nhiều". Gợi ý: "Như vậy còn tốt hơn nhiều so với để đất nước ngoan ngoãn đầu hàng Đế quốc."
- **N8 — p000368:** "một phòng ban thuộc cục tình báo" bỏ chi tiết "chiến lược" (nguồn là một phòng của bộ phận chiến lược thuộc cơ quan tình báo) và "cục" khác với "cơ quan tình báo" ở p000373. Gợi ý: "một phòng thuộc ban chiến lược của cơ quan tình báo", thống nhất "cơ quan tình báo".
- **N9 — p000374:** "kết quả tất yếu" mạnh hơn "kết quả tự nhiên". Gợi ý: "kết quả hiển nhiên/dễ hiểu".
- **N10 — p000377:** "sớm muộn gì" thay "bằng cách nào đó"; nguồn nhấn mạnh chắc chắn sẽ lọt ra mà không rõ đường nào. Gợi ý: "thế nào cũng có tin lọt ra ngoài". "Nhưng có lẽ" ở cuối nên đổi thành "Mà thôi, có lẽ…" để giữ giọng nhún vai.
- **N11 — p000379:** "tổng tấn công" mạnh hơn "tấn công quy mô lớn"; "các tuyến phòng thủ" thêm "phòng thủ"; "có thể phải đối mặt" làm yếu "đang chờ đợi/dự đoán". Gợi ý: "vì họ dự đoán Đế quốc có thể mở một cuộc tấn công quy mô lớn trên các tuyến phía bắc bất cứ lúc nào". Câu cuối "thì vẫn còn hy vọng" nâng "có thể có cơ hội"; gợi ý: "thì có lẽ vẫn còn cơ hội".
- **N12 — p000373, p000376, p000378, p000369:** các chi tiết nhỏ. p000376 "phà chở khách" thêm "chở khách"; gợi ý "phà thông thường". p000378 "bỏ trốn" thêm sắc thái chê; gợi ý "rời đi/tháo chạy". p000369 trộn "anh ta"/"anh" cho cùng một người điện báo; nên thống nhất một cách (theo sổ: "anh ta"). p000373 giữ "con tàu ấy" tạm được.

## Thuật ngữ

| Thuật ngữ | Đoạn | Bản dịch hiện tại | Lựa chọn tạm đề xuất | Thay thế | Ghi chú |
|---|---|---|---|---|---|
| radio operator | p000358, 362, 369 | người điện báo | báo vụ viên | nhân viên vô tuyến; điện báo viên | Sổ ch02 b18 đã đề xuất "báo vụ viên"; đồng bộ để giữ nhất quán. Độ tin cậy ~0,5. |
| General (Habergram) | p000369 | Thiếu tướng | Tướng Habergram | Thiếu tướng nếu có căn cứ ở lô khác | Xem V2; chưa canon. |
| councilor of state | p000365 | ủy viên Hội đồng Nhà nước | nghị viên nhà nước | ủy viên nhà nước; cố vấn nhà nước | Đồng bộ mục councilor ch02 b02; xem N6. Độ tin cậy ~0,45. |
| one-time pad | p000362 | mật mã dùng một lần | mật mã dùng một lần | khóa dùng một lần; sổ mã dùng một lần | Chấp nhận tạm; thực chất là khóa/sổ mã, nhưng "mật mã" ổn trong ngữ cảnh. Độ tin cậy ~0,5. |
| Foreign Strategy Division | p000367 | Ban Chiến lược Đối ngoại | giữ nguyên | Cục Chiến lược Đối ngoại | Chấp nhận. Lưu ý p000368 để "cục tình báo" gây lệch (N8). |
| auxiliary ship | p000360, 373 | tàu phụ trợ | giữ nguyên | tàu hỗ trợ | Chấp nhận. |
| Entente Alliance | nhiều đoạn | Liên minh Entente | giữ nguyên | Liên minh Hiệp ước Entente | Khớp sổ; chấp nhận. |
| Commonwealth | p000365, 373 | Khối Thịnh vượng chung | giữ nguyên | Liên bang | Khớp sổ; viết hoa nhất quán. |
| Foreign Office | p000366, 368 | Bộ Ngoại giao | giữ nguyên | Bộ Ngoại vụ | Chưa có mục sổ; đề xuất ghi mới, không canon. |
| armed merchant cruiser | p000362 | tàu buôn vũ trang | giữ nguyên | tàu tuần dương thương mại vũ trang | Xem N3. |
| Dacia | p000359 | Dacia | giữ nguyên | — | Khớp sổ. |

Ghi chú của translator: handoff nêu 3 ghi chú thuật ngữ mức thấp và 6 mục pending; phần `notes` trong JSONL đều rỗng, nên các mục này chỉ nằm ở sổ. Không phát hiện mục thuật ngữ nào mâu thuẫn với canon (canon hiện không có thuật ngữ chốt). Không quyết định nào ảnh hưởng cốt truyện nên không cần hỏi người dùng.

## Ghi chú còn tồn đọng cho coordinator

- V1–V3 cần translator sửa trước khi đóng lô; N1, N4, N5, N8, N11 nên sửa cùng lượt; các mục còn lại là tùy chọn.
- Cập nhật sổ pending: đồng bộ radio operator (báo vụ viên) và councilor (nghị viên), ghi mục Foreign Office, armed merchant cruiser, và cấp bậc của Habergram (xem V2).
- Lệch số checkpoint_generation giữa yêu cầu (651) và handoff (650).
- Hash gói nguồn đã đối chiếu theo handoff; không phát hiện sai khác.

```yaml
role: reviewer
task_id: vol-02-ch-03-b20
state: done
segment_ids:
  - YS-LN02/Text/part0018.xhtml/p000358..p000379
review_path: reviews/prose/vol-02/ch-03-b20-claude.md
files_written:
  - reviews/prose/vol-02/ch-03-b20-claude.md
validator: not_run
diff_check: not_run
counts:
  serious: 0
  moderate: 3
  minor: 12
findings:
  - {severity: moderate, segment_id: YS-LN02/Text/part0018.xhtml/p000367, issue: "'người nhận điện' dễ nhầm với người điện báo; nguồn là người được báo cáo", resolution: "đổi thành 'người nghe báo cáo'"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0018.xhtml/p000369, issue: "'Thiếu tướng' cụ thể hóa cấp bậc khi nguồn chỉ nói General", resolution: "'Tướng Habergram' (tạm, không canon)"}
  - {severity: moderate, segment_id: YS-LN02/Text/part0018.xhtml/p000371, issue: "suy đoán bị nâng thành chắc chắn và đổi thì", resolution: "'tôi chỉ nghĩ được rằng… đang có một lỗ hổng'"}
unresolved_findings: 3
term_recommendations:
  - {source_term: radio operator, proposed_vi: "báo vụ viên", alternatives: ["nhân viên vô tuyến", "điện báo viên"], segment_ids: [p000358, p000362, p000369], status: pending, confidence: 0.5}
  - {source_term: General (Habergram), proposed_vi: "Tướng Habergram", alternatives: ["Thiếu tướng Habergram nếu có căn cứ"], segment_ids: [p000369], status: pending, confidence: 0.5}
  - {source_term: councilor of state, proposed_vi: "nghị viên nhà nước", alternatives: ["ủy viên nhà nước", "cố vấn nhà nước"], segment_ids: [p000365], status: pending, confidence: 0.45}
  - {source_term: one-time pad, proposed_vi: "mật mã dùng một lần", alternatives: ["khóa dùng một lần", "sổ mã dùng một lần"], segment_ids: [p000362], status: pending, confidence: 0.5}
  - {source_term: Foreign Office, proposed_vi: "Bộ Ngoại giao", alternatives: ["Bộ Ngoại vụ"], segment_ids: [p000366, p000368], status: pending, confidence: 0.5}
  - {source_term: armed merchant cruiser, proposed_vi: "tàu buôn vũ trang", alternatives: ["tàu tuần dương thương mại vũ trang"], segment_ids: [p000362], status: pending, confidence: 0.45}
risks:
  - "handoff ghi checkpoint_generation 650, yêu cầu review ghi 651"
  - "cấp bậc Habergram chưa có căn cứ trong sổ; cần coordinator đối chiếu"
commit: null
next_action: translator_fix_then_recheck
```
