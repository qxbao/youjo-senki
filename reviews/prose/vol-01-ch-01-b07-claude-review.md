# Báo cáo review vol-01-ch-01-b07 (Claude, reviewer)

- Task: `vol-01-ch-01-b07-review`; lô `vol-01-ch-01-b07`; 28 đoạn `YS-LN01/Text/chapter003b.xhtml/p000101`–`p000128`. Dưới đây viết tắt mã đoạn là `pNNNNNN`.
- Đầu vào đã đọc: source package cục bộ (sha256 khớp `source_package_sha256` trong handoff: 7dfde0dc…d1c8), `translations/vol-01/ch-01-b07.jsonl`, canon (glossary và characters còn rỗng; `decisions.md` có DEC-P01-001/002), `canon/glossary-pending.yml`, `work/run-state/pending-terms.yml`.
- Đối chiếu cấu trúc: đủ 28/28 đoạn, đúng thứ tự, `source_sha256` mỗi dòng khớp handoff. Không phát hiện đoạn thiếu, thừa hay gộp.
- Không đọc `footnote.xhtml` vì nằm ngoài phạm vi được giao; ảnh hưởng tới p000122 ghi ở mục 2.

## Kết luận

Không có lỗi nghiêm trọng. Bản dịch bám sát nghĩa, giọng và quan hệ nhân quả. Có **2 lỗi vừa** (p000119, p000108) và **9 lỗi nhẹ**. Hai điểm rủi ro nghĩa translator nêu (p000116, p000122) đều chấp nhận được, chỉ cần chỉnh nhẹ. Nhấn mạnh ở p000128 đúng DEC-P01-002. Bốn thuật ngữ mới dùng được làm phương án tạm, kèm khuyến nghị bên dưới.

## 1. Phát hiện

### Vừa

**M1 — p000119: "tín hiệu số" gây hiểu sai nghĩa.**
- Vấn đề: nguồn nói đối phương đang phát các dãy số (mã số liên lạc của quan sát viên pháo binh, có thể là nội dung mã hóa hoặc chuỗi số điều chỉnh pháo). Trong tiếng Việt "tín hiệu số" là *digital signal*, thuộc thuật ngữ kỹ thuật khác hẳn.
- Căn cứ: p000120 giải thích đây là các thông điệp mã hóa gửi đều đặn trên bước sóng riêng của trinh sát pháo binh, không phải đặc tính điều chế số.
- Đề xuất: "Chúng đang phát các dãy số!" hoặc "…đang phát số liệu!". Đồng thời đổi "Họ" thành "Chúng" (xem m6) để người đọc không nhầm với Sư đoàn Sáu ở p000116–p000118.
- Độ tin cậy: 0.8.

**M2 — p000108: "sĩ quan điều phối tiền phương" thêm cấp bậc/chức vụ nguồn không nêu.**
- Vấn đề: nguồn chỉ nói về người/đơn vị điều phối tiền phương được chỉ định. Bản dịch tự gắn "sĩ quan", nên thành thông tin về cấp bậc. AGENTS.md và shared.md cấm tự chốt cấp bậc.
- Căn cứ: sổ pending không có mục cho thuật ngữ này; đây là lần đầu xuất hiện trong lô. Translator cũng không ghi nó vào `notes`.
- Đề xuất: "người điều phối tiền phương được chỉ định" (hoặc "đầu mối điều phối tiền phương"). Nếu giữ chức danh thì thêm vào ledger như pending mới.
- Độ tin cậy: 0.7.

### Nhẹ

**m1 — p000101 (và p000102): "diễn trò ngoại giao" và "chơi trò nguy hiểm" thêm sắc thái miệt thị.**
- Nguồn dùng động từ trung tính ("thực hành/vận dụng" một chiến thuật ngoại giao). Phát ngôn viên đang giải thích, không chế nhạo. "Diễn trò" kéo giọng sang châm biếm.
- Đề xuất: "chỉ đang thực hiện chiến thuật ngoại giao bên miệng hố chiến tranh" (hoặc "chỉ đang đi nước ngoại giao…"). "Chơi trò nguy hiểm" giữ được vì nguồn có "game".
- Độ tin cậy: 0.6.

**m2 — p000102: "phô trương" mạnh hơn "show signs".**
- Nguồn chỉ nói để lộ dấu hiệu hoạt động quân sự tăng cường để dò phản ứng. "Phô trương" ngụ ý khoe lực lượng có chủ đích.
- Đề xuất: "chỉ nên dừng ở việc để lộ dấu hiệu hoạt động quân sự gia tăng…".
- Độ tin cậy: 0.55.

**m3 — p000106: "một ổ lũ bất tài" gượng và nhẹ hơn nguồn.**
- "Ổ lũ" ghép sai; nguồn là cụm chửi mạnh (ổ/bãi toàn kẻ ngu), đồng bộ với "ngu xuẩn" ở câu trước. "Bất tài" yếu hơn nghĩa "imbeciles".
- Đề xuất: "một ổ toàn lũ ngu" hoặc "một ổ lũ ngu xuẩn" (đổi từ ở câu trước nếu thấy lặp).
- Độ tin cậy: 0.65.

**m4 — p000115: "phá hoại hỏa lực gián tiếp".**
- Nguồn là cản trở/gây nhiễu hỏa lực gián tiếp của địch bằng cách diệt quan sát viên. "Phá hoại" hợp nghĩa *sabotage*, không đúng ở đây.
- Đề xuất: "cản trở hỏa lực gián tiếp của địch bằng cách loại bỏ những quan sát viên của chúng".
- Độ tin cậy: 0.6.

**m5 — p000116 (rủi ro nghĩa do translator nêu): chấp nhận được, chỉnh cách viết.**
- Đánh giá: "Ground" trong tên đơn vị rất có thể chỉ lục quân, khớp cách dịch "lục quân" ở p000108; cách dịch này nhất quán. Điểm cần lưu ý là tuyên bố trong ledger ("không gán binh chủng") không khớp với bản dịch: "thuộc lục quân" vẫn gán binh chủng, chỉ là gán có căn cứ ngữ cảnh. Nên sửa lời giải thích cho đúng thay vì sửa bản dịch.
- Về hình thức, "Sư đoàn số Sáu" lai giữa "Sư đoàn 6" và "Sư đoàn Sáu"; tên đơn vị thường viết "Sư đoàn 6". Cách nói "Tin mới từ…" ổn.
- Chưa đủ căn cứ để biết đây là tên riêng (đặt theo kiểu tên đơn vị) hay mô tả. Giữ nhãn pending.
- Đề xuất: "Sư đoàn 6 lục quân" hoặc "Sư đoàn Lục quân số 6"; sửa lại rationale trong ledger.
- Độ tin cậy: 0.6.

**m6 — p000117/p000119/p000121/p000122: đại từ và mức yêu cầu.**
- p000117: "Bảo họ tìm" biến yêu cầu thăm dò ("xem họ có tìm được không") thành mệnh lệnh. Đề xuất: "Hỏi xem họ có tìm ra… không".
- p000119 và p000122: "họ" dùng cho địch trong khi cùng lô "họ" cũng chỉ Sư đoàn Sáu; p000121 và p000125–p000126 dùng "chúng" cho địch. Đề xuất thống nhất "chúng" cho địch (p000119; cân nhắc p000122, vì người nói là lính Entente).
- Độ tin cậy: 0.5.

**m7 — p000120: thuật ngữ quan sát/trinh sát chưa nhất quán và ghi chú lệch bản dịch.**
- Một nhóm nguồn gồm *observers* (p000115), *spotters* (p000117, p000120) và *observer mages* (p000120) được dịch lần lượt "người quan sát", "trinh sát pháo binh", "pháp sư quan sát". Ghi chú p000120 nói đã dùng "quan sát viên pháo binh", nhưng văn bản dùng "trinh sát pháo binh".
- "Trinh sát" nghĩa gần reconnaissance, khác "quan sát viên pháo binh" trong ledger (đã có ở b03/b05). Cần đồng bộ để người đọc nhận ra cùng một vai trò.
- Đề xuất: p000117, p000120 dùng "quan sát viên pháo binh" như ledger; sửa ghi chú. Liên hệ thêm mục `spotter magician → pháp sư trinh sát cảnh giới` đã có trong ledger (xem mục 2).
- Độ tin cậy: 0.6.

**m8 — p000122 (rủi ro nghĩa do translator nêu): chấp nhận được, kèm điều kiện.**
- Đánh giá: p000123 xác nhận người nói chỉ ra mạng lưới phòng thủ/đánh chặn trên không bảo vệ các quan sát viên, nên "tuyến cảnh giới" tạm ổn và "lớn" tạm hiểu là "đồ sộ". Phỏng đoán lore: có thể đây là *tuyến cảnh báo sớm* hoặc *tuyến tiền gác*; đây chỉ là phỏng đoán, không dùng làm căn cứ.
- Cần xem chú thích ⁷ (nằm ngoài phạm vi được giao) trước khi chốt: nếu chú thích giải thích chính cụm này thì thuật ngữ nên theo đó. Dấu ⁷ đã giữ đúng vị trí như b02/b05/b06.
- "Lớn" yếu hơn "massive"; b05 dùng "đồ sộ" cho một tuyến tương tự. Đề xuất: "một tuyến cảnh giới đồ sộ". Ở p000123 "tuyến phòng không" khác "tuyến cảnh giới"; có thể là cùng một tuyến, cần xác nhận khi có chú thích.
- Độ tin cậy: 0.5.

**m9 — p000125: "chiến tranh có phải lúc nào cũng dễ thế này không".**
- Nguồn dùng "supposed to be" (vốn dĩ phải thế nào), không phải "luôn luôn". Đề xuất: "chiến tranh vốn dĩ dễ thế này sao".
- Độ tin cậy: 0.5.

**m10 — Ghi chép ledger không khớp bản dịch.**
- `b07-brinkmanship-diplomacy`: `proposed_vi` ghi "ngoại giao bên miệng hố chiến" (thiếu "tranh"), bản dịch dùng "…chiến tranh". Cần sửa ledger.
- Độ tin cậy: 0.9.

### Không có vấn đề (đã đối chiếu)
- p000103, p000104, p000107, p000109–p000114, p000118, p000121, p000123, p000124, p000126, p000127: giữ nghĩa, giọng và cấu trúc. Lưu ý p000111: dấu hai chấm tách "trả giá" khỏi "mất kiểm soát" hơi mạnh nhưng quan hệ nhân quả vẫn còn; p000105 "đụng độ lẻ tẻ" làm nhẹ "irregular" (không chính quy) nhưng chấp nhận được.
- p000128: nguồn nhấn mạnh bằng thẻ `<em>` bao toàn đoạn. Bản dịch bọc toàn đoạn bằng `*…*`, đúng phạm vi theo DEC-P01-002; cú pháp Markdown hợp lệ (dấu mở đầu dòng, dấu đóng ngay sau "?"). Không có nhấn mạnh thừa ở đoạn khác (đã kiểm tra tất cả thẻ trong gói nguồn). Dùng "Chúa" ở p000127–p000128 hợp lý và nhất quán trong lô; nên theo dõi ở các lô sau vì có thể liên quan đến chủ đề Being X.

## 2. Khuyến nghị thuật ngữ (chỉ là đề xuất, không phải quyết định canon)

| Mục ledger | Hiện tại | Khuyến nghị | Độ tin cậy | Ghi chú |
|---|---|---|---|---|
| b07-brinkmanship-diplomacy (p000101, p000102) | ngoại giao bên miệng hố chiến(tranh) | Giữ tạm; phương án khác "ngoại giao đẩy sát bờ vực chiến tranh". Sửa ledger cho đủ chữ "tranh". Bỏ chữ "diễn trò" khi dùng (m1). | 0.65 | "Ngoại giao cưỡng ép" nên tránh vì lệch sang *coercive diplomacy*. Không ảnh hưởng cốt truyện. |
| b07-warning-line (p000122) | tuyến cảnh giới | Giữ tạm; đối chiếu chú thích ⁷ rồi chọn. Phương án khác: "tuyến cảnh báo sớm". Nếu cùng tuyến với p000123 thì thống nhất. | 0.5 | Chưa đủ căn cứ để quyết định; trung tính literal là đủ. Không phải điều kiện dừng. |
| b07-ground-division-six (p000116) | Sư đoàn số Sáu thuộc lục quân | Dùng "Sư đoàn 6 lục quân" làm tạm; sửa lại rationale (m5). Phương án khác: "Sư đoàn Lục quân số 6". | 0.6 | Chưa rõ tên riêng hay mô tả; nếu về sau có thêm các sư đoàn đánh số thì thống nhất công thức. |
| b07-observer-mage (p000120) | pháp sư quan sát | Giữ tạm; đối chiếu với `spotter magician → pháp sư trinh sát cảnh giới` đã có (chapter003 p000008) vì hai thuật ngữ có thể cùng chỉ một vai trò. Bỏ phương án "pháp sư trinh sát quan sát" (gượng). Thống nhất với "quan sát viên pháo binh" (m7). | 0.55 | Nếu hai nhãn nguồn thực sự khác nhau thì giữ khác; chưa đủ căn cứ để hợp nhất. |
| (mới, đề xuất thêm) forward controller (p000108) | sĩ quan điều phối tiền phương | Đổi thành "người điều phối tiền phương", ghi vào ledger là pending; không gán cấp bậc (M2). | 0.6 | Cấp bậc là điểm cần ghi nhận, không tự chốt. |

Không có mục nào cần hỏi người dùng theo hướng ảnh hưởng cốt truyện. Theo AGENTS.md, các lựa chọn trên là phương án tạm để coordinator ghi vào ledger và handoff.

## 3. Rủi ro còn lại

1. Chú thích ⁷ chưa được đối chiếu (ngoài phạm vi); có thể làm thay đổi cách dịch "warning line" (m8).
2. Nhóm thuật ngữ quan sát/trinh sát/spotter trải trên nhiều lô; nếu không đồng bộ sớm sẽ lan sang các lô sau (m7).
3. Cách xưng hô "cậu" (Darton, p000107) và "các anh" (trung đội, p000109) chưa có canon; hiện nhất quán và hợp ngữ cảnh. Không đổi, theo dõi ở các lô sau.
4. Dịch "God" thành "Chúa" nên giữ ổn định về sau (liên quan Being X).

## 4. Báo cáo YAML

```yaml
role: reviewer
task_id: vol-01-ch-01-b07-review
state: done
segment_ids: [p000101..p000128, 28 đoạn theo handoff]
files_written:
  - reviews/prose/vol-01-ch-01-b07-claude-review.md
review_path: reviews/prose/vol-01-ch-01-b07-claude-review.md
validator: not_run
diff_check: not_run
counts:
  serious: 0
  moderate: 2
  minor: 10
unresolved_findings:
  - {severity: moderate, segment_id: p000119, issue: '"tín hiệu số" đọc thành digital signal', suggested: 'phát các dãy số; đổi "Họ" thành "Chúng"'}
  - {severity: moderate, segment_id: p000108, issue: 'thêm "sĩ quan" cho người điều phối tiền phương, nguồn không nêu cấp bậc', suggested: 'người điều phối tiền phương được chỉ định'}
  - {severity: minor, segment_ids: [p000101, p000102, p000106, p000115, p000116, p000117, p000120, p000122, p000125], issue: 'sắc thái, từ ngữ, nhất quán thuật ngữ như mục 1 (m1–m9)'}
  - {severity: minor, segment_id: p000101, issue: 'ledger b07-brinkmanship-diplomacy thiếu chữ "tranh" so với bản dịch (m10)'}
term_recommendations:
  - {id: b07-brinkmanship-diplomacy, keep_provisional: true, note: 'sửa ledger; bỏ "diễn trò" khi dùng'}
  - {id: b07-warning-line, keep_provisional: true, note: 'đối chiếu chú thích ⁷; thống nhất với p000123'}
  - {id: b07-ground-division-six, keep_provisional: true, proposed_vi: 'Sư đoàn 6 lục quân', note: 'sửa rationale'}
  - {id: b07-observer-mage, keep_provisional: true, note: 'đối chiếu spotter magician; đồng bộ với quan sát viên pháo binh'}
  - {id: forward-controller, add_pending: true, proposed_vi: 'người điều phối tiền phương', note: 'không gán cấp bậc'}
risks:
  - 'Chú thích ⁷ chưa đối chiếu (ngoài phạm vi)'
  - 'Thuật ngữ quan sát/trinh sát/spotter chưa đồng bộ giữa các lô'
  - 'Xưng hô Darton/trung đội chưa có canon'
  - '"Chúa" cần giữ ổn định (liên quan Being X)'
commit: null
next_action: translator sửa M1, M2 và các lỗi nhẹ được chấp nhận; coordinator cập nhật ledger
```
