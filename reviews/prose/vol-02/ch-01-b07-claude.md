# Báo cáo phản biện — vol-02-ch-01-b07 (Claude)

- Phạm vi: `YS-LN02/Text/part0010.xhtml/p000153` → `p000178`, **26 đoạn**. Đã đối chiếu 26/26; tập và thứ tự segment_id của bản dịch khớp source package. Dưới đây viết tắt `pNNNNNN`.
- Đầu vào: handoff b07, source package cục bộ (có XHTML để kiểm tra nhấn mạnh), `canon/` (`decisions.md`, `style-guide.md`, `glossary-pending.yml`), `work/run-state/pending-terms.yml`, `translations/vol-02/ch-01-b07.jsonl`. Không đọc bản dịch batch khác; chỉ dùng mục sổ pending và báo cáo review b05 để lấy quyết định đã áp dụng. Không sửa tệp nào ngoài báo cáo này.
- Metadata JSONL: 26/26 dòng có `source_sha256` khớp handoff, `glossary_version` khớp, `status: draft`. Không chép câu nguồn; mọi thuật ngữ là **đề xuất tạm, không phải canon**.
- Hạn chế: handoff chỉ ghi `review_flags` và số pending, không có văn bản bốn "risk findings" của translator. Tôi đánh giá bốn đoạn p000153, p000155, p000160, p000159 theo đoạn, không theo lời translator.

## 1. Kết luận chung

Bản dịch bám sát nghĩa, phủ định, logic và giọng ra lệnh/mỉa mai của Tanya. Không có lỗi nghiêm trọng. Có 3 lỗi vừa (một lỗi nghĩa ở p000160, một đại từ mơ hồ ở p000165, một lệch thuật ngữ so với b05 ở p000159/p000157) và 9 lỗi nhẹ.

**Nhấn mạnh (DEC-P01-002):** nguồn có đúng hai chỗ in nghiêng là p000156 (cả câu nội tâm) và p000157 (một từ chỉ vào đội hình địch). Bản dịch đánh `*...*` đúng hai chỗ, đúng phạm vi. Không thừa, không thiếu. Dấu chú thích ² ở p000173 và ³ ở p000174 được giữ.

**Chủ thể/người nói:**
- p000154 là Tanya ra lệnh (cậu/tôi đúng).
- p000155 là Weiss đáp, dùng "tôi" và "Vâng".
- p000157 là Tanya, gọi Weiss là Trung úy, khớp sổ cấp bậc tạm "Weiss: Trung úy".
- p000158 là Weiss ngắt lời, gọi "Thiếu tá" đúng.
- p000159 là Tanya.
- p000163 là Weiss.
- p000164 là Tanya.
- p000167 và p000170 là Tanya.
- p000169 và p000171 là Weiss.
- p000172 là Tanya nói thành lời.

Nội tâm Tanya dùng "mình" (p000153, p000174, p000175, p000177), đúng DEC-P01-001. Trần thuật dùng "nó" (p000156, p000173), cũng đúng.

**Phủ định/logic:** p000153 (khuyến cáo tránh), p000160 (câu "có phải… đâu" tương ứng nguồn dạng phủ định), p000161, p000168 (mệnh đề nhượng bộ "dù có thể phòng thủ hay không") đều giữ đúng. Không tìm thấy đảo nghĩa.

## 2. Phát hiện

### Vừa

- **M1 — p000160, "súng ngắn" cho "sidearms":** "súng ngắn" nghĩa hẹp là pistol, không hợp ngữ cảnh. Ngữ cảnh là sức sát thương của vũ khí do phía Tanya mang theo (pháp sư) làm đội hình vuông vô dụng. Nên dùng cách trung tính như "vũ khí cá nhân" hoặc "vũ khí mang theo bên mình". Không đủ căn cứ để chốt một loại vũ khí cụ thể nên giữ nghĩa chung. Độ chắc 0.6.
- **M2 — p000159 (và p000157, vì cùng khái niệm "defensive shell"):** "kết giới phòng ngự". Mục sổ ghi lý do "tái dùng thuật ngữ ma pháp tạm có sẵn", nhưng tôi không tìm thấy mục "kết giới" nào trong sổ ngoài chính b07. Hơn nữa review b05 đã áp dụng "lớp vỏ phòng ngự" cho khái niệm này. "Kết giới" còn kéo theo sắc thái "barrier" kiểu huyền ảo mà nguồn không dùng. Nên đổi sang "lớp vỏ phòng ngự" để nhất quán b05 và sát nghĩa đen. Độ chắc 0.6.
- **M3 — p000165, "điều khiển nó lượn xuống":** "nó" ở đây bị đọc thành đối tượng của "điều khiển" (khẩu súng hoặc viên đạn), trong khi nguồn nói về việc Tanya tự cơ động. Với quy ước "nó" = Tanya ở trần thuật, câu thành "điều khiển [Tanya/nó]", gây mơ hồ chủ thể. Nên bỏ "điều khiển nó" và viết Tanya "lượn xuống gọn ghẽ". Độ chắc 0.7.

### Nhẹ

- **L1 — p000159, biệt danh "ngài Lẽ Thường Tình":** giữ được ý mỉa mai và phép "ngài" đối lập "cậu". Nhưng "lẽ thường tình" là thành ngữ khác nghĩa ("lẽ tự nhiên"). Gần nghĩa hơn là "ngài Lẽ Thường" hoặc "ngài Thường Thức". Mỉa mai và đúng một lần giải thích vẫn giữ. Còn lại ổn: "súng trường bộ binh khóa nòng", "rìa tầm bắn hiệu quả", "xuyên thủng".
- **L2 — p000155, "tư thế bắn":** "tư thế" thường chỉ dáng người (quỳ, nằm), còn nguồn là một vị trí/thế bắn theo đội hình. Xem T3. Chủ thể (Weiss) và "ra lệnh cho đại đội tránh" đúng.
- **L3 — p000160:** "bị ném vào đội hình tercio" lệch nhẹ: nguồn là kỵ binh bị đâm vào rồi tan. "Đâm sầm vào / vỡ nát trước" sát hơn. "khốc liệt đến nực cười" khuếch đại; nguồn là sắc thái mỉa mai "đáng cười mà tệ hại", không phải mức độ. Đoạn này là nội tâm Tanya, không có ngoặc kép, nên "cậu" hướng về Weiss trong đầu là chấp nhận được. Xem T5.
- **L4 — p000168, "chúng" chỉ quân địch:** thêm sắc thái khinh miệt mà nguồn không có. Dùng "họ" hoặc "quân địch". Câu "bị nổ tung" ổn.
- **L5 — p000173:** thêm "vừa" ("tin vừa truyền qua vô tuyến") suy diễn thời điểm. Có thể bỏ. "Trên cao, Tanya" thêm tên ở chỗ nguồn dùng đại từ, nhưng phù hợp quy ước lặp tên/lược chủ ngữ.
- **L6 — p000177:** "Tướng quân von Zettour" lệch phong cách "Tướng Lee" của sổ; nên "Tướng von Zettour". "Bộ Tổng tham mưu" cho "General Staff Office" lệch mục sổ "Văn phòng Bộ Tổng tham mưu" (b-khác); cần đồng bộ hoặc ghi đây là biến thể.
- **L7 — p000162, "gỡ tội":** hàm ý tội danh nặng hơn "clear your name"; "rửa sạch tiếng xấu / gỡ lại danh dự" sát hơn.
- **L8 — p000178:** "điên rồ đến mức phóng túng" và "niềm vui ăn mừng không sao thành hình" hơi nặng chữ so với nguồn; không sai nghĩa. Có thể gọn lại.
- **L9 — p000172, p000166:** p000172 thêm "đơn vị" trước "ở rìa" (nguồn chỉ nói về rìa của Quân đội). p000166 lược chủ ngữ nên không xác định ai nói; chấp nhận được như phương án trung tính, ghi là rủi ro người nói.

## 3. Đánh giá bốn đoạn translator đánh dấu rủi ro

| Đoạn | Kết luận | Ghi chú |
|---|---|---|
| p000153 | Chấp nhận | Nghĩa và phủ định đúng; nội tâm dùng "mình"; "nhăn mặt ghê tởm" đúng. Hai thuật ngữ (T1, T2) giữ tạm. |
| p000155 | Chấp nhận, chỉnh nhẹ | Người nói là Weiss, "họ" chỉ bộ binh địch là đủ. Chỉ nên cân nhắc "thế bắn" thay "tư thế" (L2). |
| p000160 | Sửa (M1) + chỉnh nhẹ (L3) | Tercio giữ được nhờ ngữ cảnh "giáo dài và súng hỏa mai"; sidearms sai nghĩa; tone nội tâm đúng. |
| p000159 | Sửa (M2) + chỉnh nhẹ (L1) | Giọng và logic đúng; cần chỉnh biệt danh và thuật ngữ vỏ phòng ngự. |

## 4. Sáu thuật ngữ pending

Mọi lựa chọn dưới đây là đề xuất tạm, không nâng canon. Không cần hỏi người dùng. Các thuật ngữ này không ảnh hưởng cốt truyện.

- **T1 — anti-surface strikes (p000153):** giữ "đòn đánh chống mục tiêu mặt đất". Căn cứ: b05 đã dùng "chống mục tiêu mặt đất" cho lựu đạn cùng nhóm; ngữ cảnh p000153 là chiến thuật đánh mặt đất. Thay thế: "tấn công mục tiêu mặt đất", "đòn đánh đối đất" (quá Hán Việt, ít tự nhiên). Độ chắc 0.55. Bất định: "surface" có thể gồm cả mặt nước; ngữ cảnh chiến trường đất liền khiến nghĩa này ít khả năng.
- **T2 — anti-air positions (p000153):** giữ "vị trí phòng không". Căn cứ: nguồn nói "positions" chung, và p000155 cho thấy chính thế bắn dày đặc cũng là một dạng vị trí chống không; "trận địa phòng không" đúng thuật ngữ quân sự hơn nhưng thu hẹp sang công sự cố định. Thay thế: "trận địa phòng không". Độ chắc 0.6. Bất định: chưa rõ tác giả nói công sự chuyên dụng hay mọi vị trí bắn lên không.
- **T3 — close-ranks firing position (p000155):** đề xuất "thế bắn theo đội hình khép sát". Căn cứ: p000156 ("đứng sát nhau") và p000161 ("đội hình bộ binh dày đặc") cho thấy ý nghĩa là đội hình bắn dày; "thế" trung tính giữa tư thế và vị trí. Thay thế: bản của translator "tư thế bắn theo đội hình khép chặt", "vị trí bắn đội hình sát nhau". Độ chắc 0.5. Bất định: chưa rõ có phải thuật ngữ hàng ngũ chuyên biệt.
- **T4 — defensive shell (p000157→p000159, ledger ghi p000157 nhưng cụm này xuất hiện ở p000159):** đề xuất "lớp vỏ phòng ngự" thay "kết giới phòng ngự". Căn cứ: b05 dùng "lớp vỏ phòng ngự"; nghĩa đen; tránh sắc thái barrier. Thay thế: "kết giới phòng ngự" (translator), "màn chắn phòng thủ". Độ chắc 0.6. Bất định: có thể sau này canon dùng thuật ngữ khác cho phòng ngự ma pháp (ví dụ "màng phòng ngự"). Ghi chú ledger: segment_ids của mục này nên thêm p000159.
- **T5 — tercio (p000160):** giữ "đội hình tercio" (hoặc nguyên "tercio"). Căn cứ: danh xưng lịch sử, câu đã kèm "giáo dài và súng hỏa mai" nên không cần chú giải thêm (thêm chú sẽ chèn nội dung ngoài nguồn). Thay thế: "khối tercio". Độ chắc 0.6. Bất định: chưa rõ có nên chuyển tên hay thêm chú thích ở bước xuất bản — để coordinator quyết, không phải việc của bản dịch.
- **T6 — Service Corps (p000177):** giữ tạm "Quân đoàn Công vụ"; không đổi sang "Hậu cần" vì không có căn cứ chức năng hậu cần. Căn cứ: ngữ cảnh chỉ cho thấy đây là nhóm quan chức quân đội đặt cạnh Bộ Tổng tham mưu và nói về soạn bài học, nghiêng về hành chính hơn tác chiến. Thay thế: "Quân đoàn Hậu cần" (không khuyến nghị), "ngành Quân vụ" (trung tính nhưng đổi hình thái "Corps"). Độ chắc 0.4. Bất định cao: tên tổ chức và chức năng thật chưa rõ; "Quân đoàn" dễ bị đọc là đơn vị tác chiến, trùng "Quân đoàn Lâm thời" của sổ. Ghi nhận rủi ro, không dừng pipeline.

## 5. Rủi ro

- **R1:** M2/T4 phụ thuộc cách b05 áp dụng sổ ("lớp vỏ phòng ngự"); coordinator cần đồng bộ toàn chương.
- **R2:** L6 (Tướng/Zettour, Bộ Tổng tham mưu) cần đồng bộ chéo với các batch khác; tôi không đọc chúng.
- **R3:** Người nói ở p000166 không xác định rõ; phương án lược chủ ngữ an toàn nhưng nếu các batch khác đã xác định thì cần khớp.
- **R4:** Bốn "risk findings" của translator không có văn bản trong đầu vào nên chưa thể đối chiếu từng ý.

## 6. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-02-ch-01-b07
state: done
segment_ids: [p000153..p000178]  # 26/26, YS-LN02/Text/part0010.xhtml/
review_path: reviews/prose/vol-02/ch-01-b07-claude.md
files_written: [reviews/prose/vol-02/ch-01-b07-claude.md]
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 3, minor: 9}
unresolved_findings:
  - {severity: moderate, segment_id: p000160, issue: "sidearms dịch thành súng ngắn, thu hẹp nghĩa", resolution: "vũ khí cá nhân / mang theo bên mình"}
  - {severity: moderate, segment_id: p000159, issue: "kết giới phòng ngự lệch b05 và không có căn cứ sổ", resolution: "lớp vỏ phòng ngự"}
  - {severity: moderate, segment_id: p000165, issue: "'điều khiển nó' mơ hồ đối tượng", resolution: "bỏ 'điều khiển nó', Tanya lượn xuống gọn ghẽ"}
  - {severity: minor, segment_id: "p000159,p000155,p000160,p000168,p000173,p000177,p000162,p000178,p000172", issue: "L1–L9", resolution: "xem mục 2"}
term_recommendations:
  - {source_term: anti-surface strikes, proposed_vi: "đòn đánh chống mục tiêu mặt đất", alternatives: ["tấn công mục tiêu mặt đất", "đòn đánh đối đất"], segment_ids: [p000153], confidence: 0.55, status: pending}
  - {source_term: anti-air positions, proposed_vi: "vị trí phòng không", alternatives: ["trận địa phòng không"], segment_ids: [p000153], confidence: 0.6, status: pending}
  - {source_term: close-ranks firing position, proposed_vi: "thế bắn theo đội hình khép sát", alternatives: ["tư thế bắn theo đội hình khép chặt", "vị trí bắn đội hình sát nhau"], segment_ids: [p000155], confidence: 0.5, status: pending}
  - {source_term: defensive shell, proposed_vi: "lớp vỏ phòng ngự", alternatives: ["kết giới phòng ngự", "màn chắn phòng thủ"], segment_ids: [p000159, p000157], confidence: 0.6, status: pending}
  - {source_term: tercio, proposed_vi: "đội hình tercio", alternatives: ["khối tercio", "tercio"], segment_ids: [p000160], confidence: 0.6, status: pending}
  - {source_term: Service Corps, proposed_vi: "Quân đoàn Công vụ", alternatives: ["ngành Quân vụ", "Quân đoàn Hậu cần"], segment_ids: [p000177], confidence: 0.4, status: pending}
risks: [R1, R2, R3, R4]
commit: null
next_action: translator_fix_moderate_then_resign_off  # coordinator giao người giữ quyền sửa áp dụng M1–M3 và các sửa nhẹ tùy chọn
```
