# Báo cáo review — vol-02-ch-04-b09 (Claude reviewer)

- Task: `vol-02-ch-04-b09`, checkpoint_generation 761.
- Phạm vi: 25 đoạn `YS-LN02/Text/part0022.xhtml/p000192`–`p000216` (nguồn 800 từ). Dưới đây viết tắt mã đoạn là `p000NNN`, cùng tiền tố `YS-LN02/Text/part0022.xhtml/`.
- Đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b09, `canon/` (style-guide, decisions DEC-P01-001/002, glossary và characters còn trống, glossary-pending), ledger `work/run-state/pending-terms.yml` (mục `chapter4_b09_translation_proposals` và các mục Tanya narration/interior, aerial/marine mage, địa chỉ "các anh" liên quan), gói nguồn b09 và `translations/vol-02/ch-04-b09.jsonl`.
- Không mở EPUB/PDF, không đọc gói hay bản dịch của lô khác. Mọi lựa chọn dưới đây là **đề xuất tạm, không phải canon**.
- Báo cáo không chép câu nguồn.

## Tóm tắt

Bản dịch bám sát nghĩa và cấu trúc: đủ 25 đoạn, không thấy bỏ sót hay thêm ý lớn, phủ định và điều kiện giả định (p000194, p000201, p000216) được giữ. Chữ nghiêng/nhấn mạnh khớp nguồn ở cả năm vị trí (p000192, p000193, p000194, p000213, p000214), theo DEC-P01-002. Chuỗi trích dẫn lồng nhau ở p000209 được giữ nguyên.

Có **hai lỗi xưng hô mức vừa** (chưa theo DEC-P01-001 và ledger LN02) và **một lỗi nghĩa mức vừa** ở p000199. Các lỗi này nên được sửa trước khi lô được tính là hoàn tất. Còn lại là các điểm nhẹ về chọn từ và văn phong.

## Số lượng theo mức

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 3 |
| Nhẹ | 12 |

## Lỗi mức vừa

### M1 — Đại từ trần thuật về Tanya dùng "cô" (p000193, p000194, p000197, p000199, p000201)

- **Vấn đề:** Trần thuật ngôi ba về Tanya dùng "cô" ở 5 đoạn, ví dụ "cô khó lòng tin nổi", "Nhiệm vụ của cô", "khiến cô sợ hãi", "cô không quá lo", "cô quyết định", "Cô nhanh chóng tính toán".
- **Căn cứ:** DEC-P01-001 chốt trần thuật về Tanya dùng "nó" và không tự mở rộng suy luận về giới tính hay thân thuộc. Ledger LN02 cũng ghi cùng hướng: `vol02-ch04-b07-tanya-narration` đề xuất "nó / lặp tên Tanya / lược chủ ngữ", và ghi "cô" chỉ là phương án thay thế cần quyết định canon cấp dự án; `vol02-ch01-b09-tanya-narration` ghi "avoid cô". Lô b09 lệch với các lô ledger gần nhất.
- **Đề xuất sửa tạm:** Thay "cô" bằng "nó" ở các chỗ cần chủ ngữ, lặp "Tanya" hoặc lược chủ ngữ khi câu vẫn rõ. Ví dụ p000193: "Nhiệm vụ của nó là tìm địch"; p000199: "Nó quyết định rằng…"; p000201: "Tanya nhanh chóng tính toán rồi quyết định điều chỉnh vài thứ".
- **Phương án thay thế:** Giữ "cô" chỉ khi coordinator ghi quyết định cấp dự án đổi quy ước cho LN02; khi đó phải đổi đồng loạt cho mọi lô LN02, không riêng b09.
- **Độ chắc:** cao (khoảng 0.8) về việc lệch ledger. Chưa kiểm tra việc dùng "cô" ở các lô khác của chương 4, nên coordinator cần đối chiếu trước khi sửa hàng loạt.

### M2 — Tự quy chiếu nội tâm/độc thoại đổi từ "mình" sang "tôi" (p000211, p000213, p000214, p000216)

- **Vấn đề:** Từ p000201 đến p000208, nội tâm Tanya dùng "mình". Từ p000211 trở đi, cùng giọng ngôi nhất (không có chuyển điểm nhìn trong nguồn) lại dùng "tôi", ví dụ "đại đội tôi", "đâu phải tôi muốn phơi mình", "Dĩ nhiên tôi muốn", "giả định tôi đang lao tới", "an toàn cho tôi". Cùng ý "không muốn phơi mình trước hỏa lực" được dịch bằng "mình" ở p000203 và "tôi" ở p000213.
- **Căn cứ:** DEC-P01-001 (nội tâm tự quy chiếu dùng "mình"). Ledger `vol02-ch03-b11-tanya-interior-pronoun` ghi "mình" cho độc thoại nội tâm, còn "tôi" chỉ dành cho thoại nói. Các câu trên là trần thuật/độc thoại, không phải thoại. Lưu ý p000212 là thoại nói nên "tôi" không đặt ra vấn đề.
- **Đề xuất sửa tạm:** Đổi "tôi" thành "mình" trong p000211, p000213, p000214, p000216 (không đổi thoại). Có thể lược chủ ngữ khi tự nhiên, ví dụ p000211: "Người trong đại đội mình phấn khích xung phong, nhưng mình không thể làm theo đề nghị đó."
- **Phương án thay thế:** Dùng "tôi" cho các đoạn giải thích ngôi nhất nếu coordinator duyệt ngoại lệ trong ledger. Khi đó cần thống nhất cả p000201, p000203, p000205, p000208. Không nên để hai đại từ cùng tồn tại trong một cảnh.
- **Độ chắc:** khoảng 0.75.

### M3 — "Discipline" bị đổi thành "đội hình" (p000199)

- **Vấn đề:** Câu cuối ("Phải khôi phục lại phần nào đội hình rồi thoát khỏi đây!") dịch khái niệm kỷ luật/trật tự chỉ huy thành "đội hình" (formation). "Đội hình" là danh từ khác nghĩa, đồng thời làm đứt liên hệ từ vựng với "disciplined fire" ở p000195 và "organized interception" ngay trong p000199. Ngữ cảnh ngay trước là chia đại đội tự hoạt động vì không điều khiển nổi cả tiểu đoàn, nên cái cần khôi phục là trật tự/khả năng kiểm soát, không nhất thiết là cách bố trí hình học.
- **Căn cứ:** DEC/style-guide (không thay chi tiết bằng chi tiết suy ra); so sánh ngữ cảnh p000195, p000199.
- **Đề xuất sửa tạm:** "Phải lấy lại phần nào trật tự rồi thoát khỏi đây!" hoặc "…khôi phục phần nào kỷ cương…".
- **Phương án thay thế:** "kỷ luật" (sát nghĩa nhất, hơi cứng); "khả năng kiểm soát".
- **Độ chắc:** khoảng 0.65. Không có căn cứ ngoài ngữ cảnh để biết chính xác hàm ý quân sự, nên đây là đề xuất tạm.

## Lỗi mức nhẹ

| # | Đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| m1 | p000192 | "Đừng mải tập trung vào bên nào quá": nguồn là bị phân tâm/sa đà vào một bên, còn "tập trung" nghe như khen | "Đừng quá sa đà vào riêng bên nào!" |
| m2 | p000194 | "cô đã có thể nhận ra nó": thêm tân ngữ "nó" mà nguồn không có | "…cô đã có thể nhận ra mà vẫn ổn." (đồng thời "bình an vô sự" hơi nặng hơn "fine") |
| m3 | p000196 | "bắt được tín hiệu pháp sư": thêm "tín hiệu" không có trong nguồn | "Tôi phát hiện pháp sư!" |
| m4 | p000198 | "tùy tình hình mà giao chiến" làm nhẹ nghĩa "tự do/tự quyết giao chiến"; "Làm theo chỉ huy" gần với phục tùng, trong khi nguồn nói theo sự dẫn dắt của chỉ huy đại đội | "Tất cả, tự do giao chiến! Theo sự dẫn dắt của chỉ huy đại đội các anh!" |
| m5 | p000200 | "Không khí nặng" mơ hồ (có thể hiểu là oi nặng, ngột ngạt); nguồn nói mật độ/độ đặc | Xem phần thuật ngữ dense air |
| m6 | p000203 | Mất nhấn mạnh "even" trong câu về đa số thuộc cấp; "hiếu chiến" nhẹ hơn "war-crazy" | "Có lẽ ngay cả phần lớn đám thuộc cấp cuồng chiến của mình cũng vậy." |
| m7 | p000204 | "bảo vệ hậu phương" thiên về nghĩa chiến lược/hậu cứ; "đấu pháo" ám chỉ pháo binh trong khi nguồn nói giao tranh/đấu hỏa lực với tàu | "Đại đội Bốn, đoạn hậu." hoặc "bảo vệ phía sau"; "Không được giao hỏa với các tàu chiến." |
| m8 | p000207 | "quấy phá" nghe như phá rối; p000208 dùng "quấy rối", là thuật ngữ quân sự đúng cho harass | Đổi thành "quấy rối" ở p000207 |
| m9 | p000214 | Phủ định bị đổi thành "muốn tránh làm việc đó" nên nhấn mạnh *muốn* nay thuộc vế khẳng định, lệch phạm vi nhấn mạnh so với nguồn (nhấn vào "want" trong phủ định, theo DEC-P01-002) | "Dĩ nhiên tôi/mình chẳng *muốn* làm vậy" |
| m10 | p000214, p000216 | "kẻ nghiệp dư", "mới là kẻ lao thẳng": "kẻ" thêm sắc thái miệt thị mà nguồn không có | "cách tính của người nghiệp dư"; "…chính những người theo sau mới lao thẳng vào đó" |
| m11 | p000215 | Trật tự từ "sẽ rốt cuộc trúng" vụng | "rốt cuộc sẽ trúng" |
| m12 | p000202 | "đám pháp sư đó": "đám" thêm chút khinh miệt đối với địch | "những pháp sư đó" hoặc giữ nếu coordinator chấp nhận giọng khẩu ngữ của chỉ huy (nhẹ) |

Ghi chú địa chỉ "các anh" (p000198, p000202): hiện chưa có canon. Đây là cách xưng hô ngôi thứ hai số nhiều với đại đội, chưa đủ căn cứ để suy ra giới tính của toàn bộ người nghe (DEC-P01-001). Giữ tạm cho nhất quán với ledger (đã có "Các anh" làm phương án thay thế ở lô khác); nếu coordinator muốn trung tính hơn thì dùng "các cậu" hoặc lược. Không tính là lỗi.

## Đánh giá năm thuật ngữ pending (ledger `chapter4_b09_translation_proposals`)

Tất cả vẫn là `pending`, không canon.

| Mã ledger | Đoạn | Phương án dịch giả | Đánh giá | Đề xuất tạm (độ chắc) |
|---|---|---|---|---|
| `vol02-ch04-b09-anti-mage-counterattack` | p000195 | phản công chống pháp sư | Chấp nhận được, sát nghĩa, hiểu được trong thoại chiến thuật | Giữ "phản công chống pháp sư"; thay thế "phản kích chống pháp sư" (0.55) |
| `vol02-ch04-b09-disciplined-fire` | p000195 | hỏa lực phòng không có tổ chức | Nghĩa gần đúng (bắn có kiểm soát, không loạn xạ). Điểm cần để ý là cùng cụm "có tổ chức" cũng dịch "organized interception" ở p000199, dễ làm hai khái niệm nhập một | Giữ "có tổ chức" nếu coordinator ưu tiên đơn giản; thay thế "có kiểm soát" hoặc "phối hợp". Nên đi kèm sửa M3 để "discipline" không còn là "đội hình" (0.5) |
| `vol02-ch04-b09-depth-perception` | p000200 | khả năng ước lượng khoảng cách | Hơi thu hẹp: depth perception là cảm nhận chiều sâu/vị trí trong không gian, rất liên quan khi bay trên mặt biển lúc tối (độ cao so với mặt nước), không chỉ ước lượng khoảng cách. Quy tắc style-guide: không thu hẹp phạm vi nghĩa | Nghiêng về "cảm nhận chiều sâu" (alt của dịch giả); giữ phương án dịch giả nếu coordinator ưu tiên dễ đọc (0.55) |
| `vol02-ch04-b09-dense-air` | p000200 | không khí nặng | "Nặng" dễ gợi cảm giác oi/ngột, không rõ là độ đặc. Phù hợp hơn với lập luận về độ ẩm ngay sau đó là "dày/đặc" | Nghiêng về "không khí đặc" hoặc "không khí dày"; "dày đặc" (alt của dịch giả) dễ đọc thành "mật độ dày kín" nên kém hơn (0.45) |
| `vol02-ch04-b09-deflection-shooting` | p000216 | bắn đón | Đúng thuật ngữ xạ kích ("bắn đón" dùng cho mục tiêu chuyển động); logic tốc độ 250/300 được diễn đạt đúng. "Bắn chặn đầu" là cách gọi khác về nghĩa (chặn ở phía trước), không nên dùng thay | Giữ "bắn đón"; không nhận "bắn chặn đầu" (0.65) |

Các mục khác trong khối `chapter4_b09_translation_proposals` (Wiengenberg, naval guns, fleet, marine mage, task force…) thuộc lô trước, nằm ngoài phạm vi b09; không đánh giá lại. Coordinator nên tách hoặc ghi chú đúng lô khi cập nhật ledger.

Về các thuật ngữ b09 dùng lại từ ledger, không phát sinh mục mới: "pháp sư không quân" (aerial mage, p000203) và "pháp sư thủy quân lục chiến" (marine mage, p000196, p000203) khớp phương án tạm hiện có (xem `vol02-ch04-b07-marine-mage`, ledger aerial mage); "tiểu đoàn/đại đội/Đại đội Một…Bốn" nhất quán.

## Ghi chú dịch giả (translator notes)

- Trường `notes` của cả 25 dòng JSONL đều rỗng. Handoff ghi "3 terminology notes" trong `translation_report.findings`; các ghi chú đó không nằm trong JSONL và không đối chiếu được trong phạm vi được đọc. Không ảnh hưởng chất lượng bản dịch; coordinator cần xác nhận chúng đã vào ledger.
- Handoff ghi `pending_term_count: 5`, khớp với năm mục ở trên.

## Điểm tốt cần giữ

- Câu hỏi/ý giả định ngược (p000194: nếu không nhận ra thì sẽ bị ủy ban chất vấn; nếu ở xa hơn thì đã nhận ra) giữ đúng thể điều kiện và thời gian.
- Nhấn mạnh p000192 (*lẫn*), p000193, p000194, p000213, p000214 đúng phạm vi nguồn.
- Thông tin số liệu p000216 (hai trăm năm mươi, ba trăm) và logic "người sau mới trúng đạn" giữ đúng.
- Phân biệt đại đội theo số, quan hệ vị trí trên/dưới (p000201), vai trò đoạn hậu và mồi nhử (p000204–p000206) nhất quán.

## Báo cáo coordinator (YAML)

```yaml
role: reviewer
task_id: vol-02-ch-04-b09
state: done
review_path: reviews/prose/vol-02/ch-04-b09-claude.md
segment_ids:
  range: [YS-LN02/Text/part0022.xhtml/p000192, YS-LN02/Text/part0022.xhtml/p000216]
  count: 25
files_written:
  - reviews/prose/vol-02/ch-04-b09-claude.md
validator: not_run
diff_check: not_run
counts:
  serious: 0
  moderate: 3
  minor: 12
findings:
  - id: M1
    severity: moderate
    segment_ids: [p000193, p000194, p000197, p000199, p000201]
    issue: Trần thuật về Tanya dùng "cô", lệch DEC-P01-001 và ledger LN02 (nó / lặp tên / lược chủ ngữ).
    resolution: Thay bằng "nó", lặp "Tanya" hoặc lược chủ ngữ; hoặc coordinator ghi quyết định cấp dự án nếu muốn đổi cho toàn LN02.
  - id: M2
    severity: moderate
    segment_ids: [p000211, p000213, p000214, p000216]
    issue: Tự quy chiếu nội tâm đổi từ "mình" sang "tôi" giữa cùng một cảnh, trái DEC-P01-001 và ledger.
    resolution: Đổi sang "mình" (hoặc lược chủ ngữ) cho các đoạn trần thuật/độc thoại; thoại p000212 giữ nguyên.
  - id: M3
    severity: moderate
    segment_ids: [p000199]
    issue: "Discipline" dịch thành "đội hình", đổi nghĩa và đứt liên hệ với p000195.
    resolution: "Lấy lại phần nào trật tự/kỷ cương rồi thoát khỏi đây"; thay thế "kỷ luật".
  - id: m1-m12
    severity: minor
    segment_ids: [p000192, p000194, p000196, p000198, p000200, p000202, p000203, p000204, p000207, p000214, p000215, p000216]
    issue: Lệch nhẹ từ vựng/sắc thái/phạm vi nhấn mạnh (xem bảng mức nhẹ).
    resolution: Sửa theo bảng nếu thuận tiện; không chặn hoàn tất lô.
unresolved_findings: 3   # M1, M2, M3 chưa sửa; sau khi translator sửa cần kiểm tra lại
pending_terms:
  - {source_term: anti-mage counterattack, proposed_vi: phản công chống pháp sư, segment_ids: [YS-LN02/Text/part0022.xhtml/p000195], volume: vol-02, chapter: 4, status: pending}
  - {source_term: disciplined fire, proposed_vi: hỏa lực phòng không có tổ chức, segment_ids: [YS-LN02/Text/part0022.xhtml/p000195], volume: vol-02, chapter: 4, status: pending}
  - {source_term: depth perception, proposed_vi: cảm nhận chiều sâu, segment_ids: [YS-LN02/Text/part0022.xhtml/p000200], volume: vol-02, chapter: 4, status: pending}
  - {source_term: dense air, proposed_vi: không khí đặc, segment_ids: [YS-LN02/Text/part0022.xhtml/p000200], volume: vol-02, chapter: 4, status: pending}
  - {source_term: deflection shooting, proposed_vi: bắn đón, segment_ids: [YS-LN02/Text/part0022.xhtml/p000216], volume: vol-02, chapter: 4, status: pending}
term_recommendations:
  - {term: anti-mage counterattack, keep: phản công chống pháp sư, alt: phản kích chống pháp sư, confidence: 0.55, canon: false}
  - {term: disciplined fire, keep: hỏa lực phòng không có tổ chức, alt: [có kiểm soát, phối hợp], confidence: 0.5, canon: false}
  - {term: depth perception, prefer: cảm nhận chiều sâu, alt: khả năng ước lượng khoảng cách, confidence: 0.55, canon: false}
  - {term: dense air, prefer: không khí đặc, alt: [không khí dày, không khí nặng], confidence: 0.45, canon: false}
  - {term: deflection shooting, keep: bắn đón, reject: bắn chặn đầu, confidence: 0.65, canon: false}
risks:
  - Chưa kiểm tra việc dùng "cô"/"tôi" ở các lô khác của chương 4; cần coordinator đối chiếu trước khi sửa hàng loạt.
  - Ghi chú dịch giả (3 terminology notes) không nằm trong JSONL; cần xác nhận đã có trong ledger.
  - Khối ledger chapter4_b09 chứa cả mục của b06/b08; cần ghi đúng lô khi cập nhật.
commit: null
next_action: translator_revise_then_recheck   # sửa M1–M3 (mức nhẹ tùy chọn), sau đó review nhanh các đoạn đã đổi
```
