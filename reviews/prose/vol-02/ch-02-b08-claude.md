# Review b08 — vol-02-ch-02-b08-review

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích câu nguồn.
- **Phạm vi:** 22 đoạn `YS-LN02/Text/part0014.xhtml/p000168`–`p000189` (dưới đây viết tắt `pNNNNNN`). Đã đọc: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b08, gói nguồn đã chuẩn bị, `translations/vol-02/ch-02-b08.jsonl`, `canon/` (glossary, characters, style-guide, decisions, glossary-pending) và mục `chapter2_b08_translation_proposals` trong ledger. Không đọc batch dịch khác.
- **Kiểm tra cơ học:** 22/22 đoạn, thứ tự và `segment_id` khớp gói nguồn. Chữ nghiêng (DEC-P01-002) khớp nguồn: p000177 (một cụm), p000182, p000184 (hai cụm, gồm câu hỏi ngắn cuối đoạn), p000185, p000187 (hai câu đầu, câu cuối ngoài nhấn mạnh). Không có nhấn mạnh thừa hay thiếu.

## Kết luận: `needs_fixes` (serious 0, moderate 1, minor 14)

## Moderate

### MOD-1 — p000172: sai hình ảnh/sự kiện chính
- **Vấn đề:** cụm miêu tả chỉ huy "bung đỏ" khi che đạn cho cấp dưới bị dịch thành "đỏ lựng". Trong tiếng Việt "đỏ lựng" gợi đỏ mặt/nóng bừng, không phải trúng đòn và chảy máu. Nguồn là hình ảnh máu bung ra khi bị bắn trúng. p000173 mới cho biết là vết thương nên người đọc phải đoán ngược lại.
- **Đề xuất:** thay bằng hình ảnh máu/trúng đòn, giữ ẩn dụ "nở/bung đỏ", ví dụ "Máu anh bung đỏ khi che chắn cho…" hoặc "Anh nở một đóa máu đỏ khi che chắn cho…". Giữ nguyên phần còn lại của câu (cấp dưới bất cẩn cơ động vào làn đạn).
- **Độ tin cậy:** cao (0,9) rằng "đỏ lựng" sai nghĩa. Không ảnh hưởng cốt truyện nên xếp moderate, nhưng phải sửa trước khi nâng batch.

## Minor (không chặn, nên sửa cùng lượt nếu tiện)

| ID | Đoạn | Vấn đề | Đề xuất |
|---|---|---|---|
| m1 | p000168 | "vẫn phải vượt trội" đọc như mệnh lệnh/bổn phận, mất sắc thái dự tính hóa ra sai ("lẽ ra… nên"). Style guide yêu cầu giữ mức chắc chắn và thời gian của giả định. | "lẽ ra pháp sư Đế quốc vẫn phải vượt trội…" hoặc "theo tính toán thì vẫn phải vượt trội". |
| m2 | p000169 | Thêm "chỉ cần" (biến điều kiện thành điều kiện đủ); thêm "bộ phận" cho tên đơn vị Airspace Control. | Bỏ "chỉ cần"; cân nhắc giữ tên như đơn vị ("Kiểm soát không phận"), thống nhất với p000170 nơi "Tình báo" được viết hoa như tên đơn vị. |
| m3 | p000170 | "những kẻ" thêm sắc thái miệt thị; "bảo sao họ không muốn…" thêm lời biện minh không có trong nguồn (nguồn chỉ nêu hệ quả tâm lý). "sai lệch" mạnh hơn "khác nhau". Style guide cấm thêm sắc thái phán xét. | "những người/bên chịu trách nhiệm"; "…khiến họ muốn buông lời cay nghiệt"; "dựa trên một thông tin khác". |
| m4 | p000173 | "hẳn anh đã không bất tỉnh" mất ý "xoay xở để không ngất". | "hẳn anh đã gắng không ngất". |
| m5 | p000174 | (a) "duy trì đội hình" dịch "coordination" (phối hợp), không phải formation. (b) "hỏa lực" cho "output" (cường độ/công suất phép thuật) trùng với "hỏa lực có kỷ luật" ở p000168. (c) "linh cảm đáng ngại" lệch khỏi "nghi ngờ". (d) "phép thuật" cho "formulas": nguồn nói công thức/thuật thức được thi triển. | (a) "duy trì sự phối hợp"; (b) "công suất/uy lực"; (c) "mối nghi ngờ đáng ngại"; (d) ghi vào ledger nếu muốn thống nhất (đề xuất "thuật thức"), chưa phải canon. |
| m6 | p000175 | Lời chỉ huy gọi 02 là "cậu": xưng hô cấp trên–cấp dưới suy từ một đoạn, DEC-P01-001 yêu cầu không suy quan hệ khi thiếu ngữ cảnh. Chấp nhận được làm tạm. | Giữ "Tôi/cậu" như lựa chọn tạm, ghi vào ledger xưng hô; hoặc dùng trung tính "Phần còn lại nhờ 02". |
| m7 | p000177 | "chuyển sang tính toán tình hình" thêm "tính toán"; nguồn chỉ nói chuyển trạng thái tư duy. | "nhanh chóng chuyển sang trạng thái/lối nghĩ chỉ huy" (đề xuất nhẹ). |
| m8 | p000178 | Dấu chú thích đi kèm "CP" (số 7, liên kết tới part0039_split_006) bị bỏ trong bản dịch. Validator không kiểm tra chú thích, và `decisions.md` chưa có quy ước về chú thích. | Coordinator chốt quy ước (giữ dấu hay ghi chú ngoài bản dịch); không tự quyết ở mức batch. Xem Rủi ro. |
| m9 | p000179 | "nghe rõ" lặp lại cho cả "roger" (đã nhận/hiểu) lẫn "do you read me" (có nghe rõ không), làm mất khác biệt. | "Sở chỉ huy đã nhận. Viper 02, nghe rõ không?" |
| m10 | p000180 | "chúng" (các trận địa pháo phòng không) trùng với "chúng" chỉ địch ở p000183 và p000184, dễ nhầm chủ thể. | "các trận địa ấy". |
| m11 | p000182 | (a) "Khốn thật" thêm từ "khốn" gần với "khốn nạn" cuối đoạn; nguồn là thán từ bực bội. (b) "bình tĩnh" thêm ý. (c) "Chúa" cho "God": nhất quán với các lần khác chưa kiểm được. (d) Nội tâm dùng "Mình" cho Viper 02: DEC-P01-001 chỉ chốt "mình" cho Tanya và cấm mở rộng sang chủ thể khác. | (a) "Chết tiệt/Trời ạ"; (b) bỏ "bình tĩnh"; (c) ghi theo dõi "God" trong ledger; (d) giữ "mình" làm lựa chọn tạm cho nội tâm Viper 02, ghi rõ không phải canon. |
| m12 | p000184 | (a) "hơn cả một đại đội" mất "way more" (số lượng lớn hơn nhiều). (b) "ta" trong nội tâm, còn p000185/p000187 dùng "chúng ta" cho cùng chủ thể và cùng kiểu nội tâm: không nhất quán. | (a) "hạ hơn một đại đội rất nhiều"; (b) thống nhất "chúng ta" hoặc "ta" trong cả ba đoạn. |
| m13 | p000187 | "chuyển sang cố thủ" mạnh hơn "commit to defensive battle" (dốc sức vào trận phòng thủ). | "dồn sức vào trận phòng thủ" / "chuyển sang chiến đấu phòng thủ". |
| m14 | p000189 | "Kho có thể sẽ bị hư hại nhiều hơn" đổi "khả năng bị hư hại tăng" thành "mức độ hư hại tăng". | "khả năng kho bị hư hại sẽ tăng". |

## Đã đối chiếu, không có lỗi

- **Phủ định/điều kiện:** p000168, p000169, p000173, p000177, p000180, p000187, p000188, p000189: phủ định, điều kiện, số lượng đơn vị (đại đội/nửa đại đội/trung đoàn/hai cụm cấp đại đội) khớp nguồn.
- **Người nói:** p000171 (cấp dưới gọi chỉ huy), p000175 (chỉ huy), p000176 và p000181 (02), p000178 (01 gọi CP), p000179/p000183 (CP) đúng chủ thể. "anh ấy" ở p000176 chỉ chỉ huy, không mơ hồ.
- **Thứ tự và định dạng:** không có đoạn bị gộp/tách/đảo; dấu thoại và dấu gạch đầu ở p000171 giữ.

## Đề xuất thuật ngữ tạm (không phải canon)

### 1. `vol02-ch02-b08-combat-ineffective` — p000180
- **Đề xuất của translator:** "mất khả năng chiến đấu" (0,55).
- **Khuyến nghị tạm của reviewer:** "mất sức chiến đấu" (độ tin cậy 0,6).
- **Lý do:** đây là thuật ngữ quân sự chỉ đơn vị bị tổn thất đến mức không còn hoàn thành nhiệm vụ, không nhất thiết bị xóa sổ. "mất khả năng chiến đấu" dễ bị đọc là toàn đại đội bị hạ/bị thương tàn, mạnh hơn nghĩa gốc. "mất sức chiến đấu" là cách nói quân sự phổ biến trong tiếng Việt và còn chừa nghĩa tổn thất một phần.
- **Phương án thay thế:** "mất khả năng chiến đấu" (chấp nhận được, không chặn, vì chỉ xuất hiện một lần); "không còn hiệu quả chiến đấu" (sát thuật ngữ gốc nhưng nặng chất dịch).
- **Ảnh hưởng cốt truyện:** không. Không cần hỏi người dùng.

### 2. `vol02-ch02-b08-surface-observer-squad` — p000183
- **Đề xuất của translator:** "đội quan sát mặt đất" (0,55).
- **Khuyến nghị tạm của reviewer:** giữ "đội quan sát mặt đất" (độ tin cậy 0,6).
- **Lý do:** "squad" trong tiếng Anh ở đây là cách gọi chung một nhóm nhỏ; "tiểu đoàn/đại đội" ở ngữ cảnh gần mới là cấp quân hiệu rõ ràng. "tiểu đội" gán quy mô cụ thể (8–12 người) mà ngữ cảnh không cho biết. "đội" trung tính và an toàn nhất. "mặt đất" khớp đối lập với trên không trong cảnh này.
- **Phương án thay thế:** "tiểu đội quan sát mặt đất" (nếu sau này có căn cứ quy mô); "tổ quan sát mặt đất" (nếu là nhóm rất nhỏ); "đội quan sát trên mặt đất".
- **Ảnh hưởng cốt truyện:** không.

## Rủi ro

1. **Chú thích (m8):** dấu chú thích ở p000178 bị bỏ; nếu EPUB cuối cần giữ liên kết chú thích về CP thì mất mốc neo. Cần coordinator quyết quy ước và áp dụng nhất quán cho cả volume.
2. **Hai thuật ngữ vẫn là đề xuất:** đều chỉ xuất hiện một lần trong batch; đổi sau này chỉ cần thay tại p000180 và p000183.
3. **Thuật ngữ chưa vào ledger nhưng nên theo dõi:** "Airspace Control", "Intelligence", "CP", "formulas", "God", cách gọi "Entente". Đề xuất coordinator ghi dưới dạng đề xuất để dịch nhất quán giữa các batch.
4. **Xưng hô/nội tâm:** "mình", "cậu", "anh ấy" cho 01/02 là lựa chọn tạm, chưa là canon (DEC-P01-001 giới hạn phạm vi). Cảnh này có câu nội tâm nhắc "God" nghe giống giọng nhân vật khác trong loạt; không coi đó là sự thật về lore, chỉ giữ chủ thể là Viper 02 theo gói nguồn.
5. Reviewer không chạy validator/diff-check (`not_run`); không commit (`commit: null`).

## YAML

```yaml
task_id: vol-02-ch-02-b08-review
state: done
review_path: reviews/prose/vol-02/ch-02-b08-claude.md
reviewed_segments: 22
serious: 0
moderate: 1
minor: 14
findings:
  - {id: MOD-1, severity: moderate, segment_ids: [p000172], issue: "dịch sai hình ảnh 'bung đỏ' (máu/trúng đòn) thành 'đỏ lựng' (đỏ mặt/bừng)", suggestion: "dùng hình ảnh máu bung đỏ, giữ phần còn lại"}
  - {id: m1, severity: minor, segment_ids: [p000168], issue: "mất sắc thái 'lẽ ra' của dự tính", suggestion: "lẽ ra… vẫn phải vượt trội"}
  - {id: m2, severity: minor, segment_ids: [p000169], issue: "thêm 'chỉ cần' và 'bộ phận'", suggestion: "bỏ; thống nhất tên đơn vị"}
  - {id: m3, severity: minor, segment_ids: [p000170], issue: "thêm sắc thái miệt thị/biện minh ('những kẻ', 'bảo sao')", suggestion: "trung tính hóa"}
  - {id: m4, severity: minor, segment_ids: [p000173], issue: "mất ý 'xoay xở không ngất'", suggestion: "hẳn anh đã gắng không ngất"}
  - {id: m5, severity: minor, segment_ids: [p000174], issue: "coordination/output/suspicions/formulas dịch lệch", suggestion: "phối hợp; công suất; nghi ngờ; thuật thức (đề xuất)"}
  - {id: m6, severity: minor, segment_ids: [p000175], issue: "'cậu' là xưng hô suy từ một đoạn", suggestion: "ghi lựa chọn tạm vào ledger"}
  - {id: m7, severity: minor, segment_ids: [p000177], issue: "thêm 'tính toán'", suggestion: "diễn đạt trung tính hơn"}
  - {id: m8, severity: minor, segment_ids: [p000178], issue: "dấu chú thích bị bỏ; chưa có quy ước", suggestion: "coordinator quyết quy ước chú thích"}
  - {id: m9, severity: minor, segment_ids: [p000179], issue: "roger và read me cùng thành 'nghe rõ'", suggestion: "đã nhận / nghe rõ không"}
  - {id: m10, severity: minor, segment_ids: [p000180], issue: "'chúng' mơ hồ (trận địa vs địch)", suggestion: "các trận địa ấy"}
  - {id: m11, severity: minor, segment_ids: [p000182], issue: "thán từ/bình tĩnh/Chúa/mình ngoài phạm vi DEC-P01-001", suggestion: "xem bảng"}
  - {id: m12, severity: minor, segment_ids: [p000184, p000185, p000187], issue: "mất 'way more'; 'ta' vs 'chúng ta' không nhất quán", suggestion: "thống nhất đại từ nội tâm"}
  - {id: m13, severity: minor, segment_ids: [p000187], issue: "'cố thủ' mạnh hơn nguồn", suggestion: "chiến đấu phòng thủ"}
  - {id: m14, severity: minor, segment_ids: [p000189], issue: "khả năng hư hại thành mức độ hư hại", suggestion: "khả năng kho bị hư hại tăng"}
pending_term_choices:
  - {id: vol02-ch02-b08-combat-ineffective, segment_ids: [p000180], recommended: "mất sức chiến đấu", alternatives: ["mất khả năng chiến đấu", "không còn hiệu quả chiến đấu"], confidence: 0.6, plot_affecting: false}
  - {id: vol02-ch02-b08-surface-observer-squad, segment_ids: [p000183], recommended: "đội quan sát mặt đất", alternatives: ["tiểu đội quan sát mặt đất", "tổ quan sát mặt đất"], confidence: 0.6, plot_affecting: false}
risks:
  - "quy ước chú thích chưa có (p000178)"
  - "hai thuật ngữ vẫn là đề xuất, không phải canon"
  - "xưng hô/nội tâm mình-cậu-ta chưa là canon ngoài Tanya"
  - "validator/diff_check not_run; commit null"
next_action: "translator sửa MOD-1 (bắt buộc) và các minor tùy chọn; coordinator chốt quy ước chú thích và ghi lựa chọn thuật ngữ tạm vào ledger; reviewer sign-off sau sửa"
```
