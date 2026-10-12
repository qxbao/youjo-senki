# Báo cáo phản biện — vol-02-ch-01-b15

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon).
- Phạm vi: `p000019`–`p000035` (17 đoạn) của `YS-LN02/Text/part0012.xhtml`; gồm handoff b15, gói nguồn cục bộ b15, `translations/vol-02/ch-01-b15.jsonl`, canon và sổ pending.
- Kích hoạt: `new_pending_terms`.
- Báo cáo không trích câu nguồn. Thuật ngữ gốc ngắn và mã đoạn chỉ dùng để nhận diện. Mọi lựa chọn dưới đây là đề xuất tạm, không phải canon, không nâng lên canon.
- Mã đoạn viết tắt `pNNNNNN` = `YS-LN02/Text/part0012.xhtml/pNNNNNN`.

## 1. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự | 17/17, liên tục p000019→p000035, khớp 1–1 giữa nguồn và bản dịch |
| Hash gói nguồn | `f340547f…c28a` khớp `source_package_sha256`; `source_sha256` mọi đoạn khớp `3ac53161…` |
| Hash canon (5 tệp) | Khớp handoff (glossary, style-guide, characters, decisions, glossary-pending) |
| Trường bản dịch | `status: draft`, `glossary_version` khớp, `notes` rỗng ở cả 17 đoạn |
| Nhấn mạnh (DEC-P01-002) | Nguồn không có thẻ in nghiêng/nhấn mạnh ở đoạn nào; bản dịch không có `*…*`. Đúng. |
| Đại từ Tanya (DEC-P01-001) | Lô này không có trần thuật về Tanya; không áp dụng. |
| Phủ định / điều kiện | p19, p25, p28, p31, p35 giữ đúng (điều kiện "nếu… thì", "chỉ có giá trị với giả định", "không còn lựa chọn nào ngoài…", "dù không… vẫn…"). Không đảo phủ định. |
| Người nói | Suy ra từ nội dung: p19, p22, p24, p29, p33 = Rudersdorf (Tác chiến); p21, p23, p25, p32, p35 = Zettour (hậu cần); p20, p26–p28, p30–p31, p34 = trần thuật. Bản dịch xưng hô đối đáp đúng chiều ở p21/p22. p32 và p33 không có dấu hiệu người nói trong nguồn nên đây là suy luận (độ chắc chắn trung bình-cao); bản dịch không gán sai. |
| Ranh giới đoạn | Giữ nguyên, không gộp/tách. |

Nhìn chung bản dịch bám nghĩa tốt, mạch lập luận (hậu cần ↔ đổ bộ đường biển ↔ rủi ro hải quân ↔ bất đồng Tác chiến/Hậu cần) rõ. Không có lỗi nghĩa nghiêm trọng.

## 2. Phát hiện

Đếm: **nghiêm trọng 0 · vừa 1 · nhẹ 8**.

### Mức vừa

**M1 — p21, p34: cấp bậc tổ chức của hai tên gọi không tương xứng ("Binh đoàn Hậu cần" ↔ "Bộ Tác chiến").**
- Bằng chứng ngữ cảnh: p34 đặt hai cơ quan song song như hai bên của một bất đồng nội bộ; Zettour nói bằng lập trường hậu cần (p21, p23, p35), Rudersdorf bằng lập trường tác chiến. Cả hai là bộ phận tham mưu ngang cấp, không phải đơn vị dã chiến. "Binh đoàn" gợi đơn vị chiến đấu, lệch cấp so với "Bộ Tác chiến".
- Ngoài ra "Bộ" của Tác chiến dễ đọc như ngang với "Bộ Tổng tham mưu" (đang tạm dùng ở b14), trong khi nguồn không có dấu hiệu một cơ quan lớn hơn cơ quan mẹ.
- Lệch nhất quán: b07 p000177 đang tạm dùng "Quân đoàn Công vụ" cho cùng thuật ngữ gốc; b15 chuyển sang "Binh đoàn Hậu cần". Hai nhãn khác nhau cho một thuật ngữ trong cùng tập.
- Đề xuất tạm (không canon): xem mục 3.

### Mức nhẹ

**m1 — p23: Zettour tự xưng "ta" khi nguồn là "tôi".** Câu "ta có thể điều một con tàu…" là ngôi thứ nhất số ít, nhưng cùng người nói dùng "tôi" ở p21, p25, p35. "ta" ở "các tuyến… của ta" (ngôi gộp "chúng ta") chấp nhận được; chỉ nên đổi "ta có thể điều" thành "tôi có thể điều" để giữ giọng một nhân vật. Chắc chắn trung bình-cao.

**m2 — p34: "lời qua tiếng lại" nặng hơn nguồn.** Nguồn chỉ là bất đồng nhẹ bắt đầu lộ ra trong lời lẽ; "lời qua tiếng lại" gợi cãi vã. Đề xuất: "…trong lời lẽ của hai bên bắt đầu thoáng chút bất đồng."

**m3 — p19: "đừng hòng thuyết phục tôi" gắt hơn nguồn.** Nguồn là phủ định khả năng ("ông sẽ không thuyết phục được tôi"), giọng tin cậy giữa bạn cũ chứ không đe nẹt (xem p20). Đề xuất: "…ông không thuyết phục nổi tôi rằng ông không có kế hoạch thay thế." Độ chắc chắn thấp-trung bình; cách hiện tại vẫn nằm trong khoảng chấp nhận được.

**m4 — p24: "Vậy là quyết định thế nhé?" nghiêng sang đề nghị.** Nguồn là câu xác nhận ("vậy là đã quyết rồi sao?"), và "just" (cứ nói thẳng) bị lược ở vế sau. Đề xuất: "Vậy là chốt rồi nhỉ? Giá mà ông cứ nói thế ngay từ đầu."

**m5 — p26: "lo về… khả năng chiến dịch thành công" dễ hiểu sai.** "Lo về khả năng thành công" nghe như lo thành công. Nguồn so mức bận tâm giữa tổn thất và thành quả. Đề xuất: "…để tâm đến tổn thất có thể xảy ra hơn là thành quả tiềm năng của chiến dịch."

**m6 — p27 (câu cuối): "họ" mơ hồ.** Sau chủ ngữ "Hải quân Đế quốc", "Đó là rủi ro họ phải đối mặt" có thể đọc là rủi ro của riêng Hải quân; nguồn nói về phía Đế quốc nói chung. Đề xuất: "Đó là rủi ro mà Đế quốc phải đối mặt." (hoặc "phía Đế quốc").

**m7 — p29: "trên giấy" và "chỉ cần… là đủ" thêm sắc thái.** "supposed losses" là tổn thất được cho là/giả định; "trên giấy" là thành ngữ thêm hàm ý lý thuyết suông. "chỉ cần… là đủ" thêm ý "đủ" mà nguồn chỉ nói "sẽ đánh gục". Đề xuất: "Ông lo quá nhiều về những tổn thất được cho là sẽ xảy ra. Dù có hơi mạo hiểm, luồn ra sau phòng tuyến Liên minh Entente và cắt đứt liên lạc của họ cũng sẽ đánh gục họ." Độ chắc chắn trung bình.

**m8 — p21, p34: hai lỗi nhẹ mà translator ghi `minor_findings: 2` (handoff không nêu chi tiết).** Handoff chỉ ghi số lượng; không nêu nội dung, nên tôi không khẳng định đó là m nào. Các ứng viên trong phạm vi p21/p34 là: p21 — "Tướng" (nguồn là "General") và "quản lý đầu máy toa xe" (xem mục 3); p34 — "lời qua tiếng lại" (m2). Coordinator nên đối chiếu với ghi chú của translator.

## 3. Đánh giá đề xuất thuật ngữ (tạm, không canon)

Ledger: `chapter2_b15_translator_terms` trong `work/run-state/pending-terms.yml`, trạng thái `provisional_non_canon`.

### 3.1 Service Corps — p21, p34 (ledger: "Binh đoàn Hậu cần", 0.45)
- Bằng chứng chức năng: hậu cần/tiếp tế (p21, p34, p35), đối trọng nội bộ với Tác chiến (p34). Nguồn không cho biết tên đầy đủ, cấp, hay vị trí trong Bộ Tổng tham mưu.
- **Đề xuất tạm: "Cục Hậu cần"** — độ tin cậy ~0.5. Lý do: ngang cấp với "Cục Tác chiến" (xem 3.2), khớp thực tế mã "cục" của bộ phận trong bộ tham mưu, và đã thể hiện chức năng bằng "Hậu cần" như phần còn lại của đoạn (p34, p35).
- Phương án thay thế: (a) "Binh đoàn Hậu cần" — giữ nếu coordinator ưu tiên ổn định với b15 hiện tại, nhưng lệch cấp (xem M1); (b) "Bộ Hậu cần"; (c) "ngành hậu cần/Quân vụ" nếu muốn trung tính, tránh chốt cấp; (d) "Quân đoàn Công vụ" (b07 p000177) — chỉ phù hợp nếu b07 là đơn vị khác; hiện không có bằng chứng như vậy.
- Điểm bất định: ánh xạ "Service"→"Hậu cần" dựa trên chức năng suy ra từ ngữ cảnh, không dựa trên nghĩa từ vựng của "Service Corps"; cấp tổ chức chưa rõ. Ledger cần ghi b07 p000177 là cùng thuật ngữ gốc để tránh hai nhãn song song.

### 3.2 Operations — p34 (ledger: "Bộ Tác chiến", 0.5)
- **Đề xuất tạm: "Cục Tác chiến"** — ~0.55. Lý do: bộ phận của Bộ Tổng tham mưu, nên "Cục" tránh trùng cấp với "Bộ Tổng tham mưu"; đối xứng với 3.1.
- Phương án thay thế: "Bộ Tác chiến" (giữ nếu muốn khớp bản dịch hiện tại; hợp lý nếu cặp 3.1 cũng dùng "Bộ"); "cơ quan tác chiến" (trung tính nhất khi chưa chốt cấp).
- Quy tắc kèm theo: dù chọn tên nào, cặp Tác chiến/Hậu cần phải cùng bậc đơn vị hành chính. Ở p34 cách dùng sở hữu ("theo quan điểm của …") giữ được với mọi phương án.

### 3.3 rolling stock managers — p21 (ledger: "quản lý đầu máy toa xe", 0.5)
- Bản dịch đúng nghĩa đen (đầu máy + toa xe), nhưng "quản lý đầu máy toa xe" đọc hơi cứng, gợi chức danh chuyên ngành hơn lời nói thường của tướng lĩnh.
- **Đề xuất tạm: "người phụ trách đầu máy toa xe"** — ~0.55; tự nhiên hơn, vẫn giữ đúng nghĩa và vai trò.
- Phương án thay thế: "quản lý đầu máy toa xe" (hiện tại, chấp nhận được); "người quản lý toa xe" (ledger) — mất đầu máy, hẹp nghĩa hơn; "cán bộ phụ trách phương tiện đường sắt" nếu muốn tổng quát.
- Điểm bất định: không rõ nguồn muốn nói "người điều hành đội phương tiện" hay "người quản lý kỹ thuật"; chọn phương án ít suy diễn nhất.

### 3.4 Các thuật ngữ khác trong lô (không nằm trong ledger b15)
- "Tướng" cho "General" (p21, p22): trung tính, phù hợp vì cấp chưa chốt (ledger chỉ mới có "Thiếu tướng" ở b14). Không cần đổi; ghi chú cấp "General" chưa chốt (Đại tướng/Thượng tướng là phương án chỉ dùng khi có bằng chứng).
- "Liên minh Entente", "Bộ Tổng tham mưu", "Norden", "Dacia", "nước Cộng hòa", "Hải quân/Lục quân Đế quốc": nhất quán với b14 và sổ pending hiện có. Không có xung đột.

## 4. Rủi ro

1. **Lệch nhãn xuyên lô (M1):** nếu giữ "Binh đoàn Hậu cần" ở b15 và "Quân đoàn Công vụ" ở b07, độc giả sẽ thấy hai tổ chức khác nhau; thuật ngữ này sẽ còn xuất hiện ở các batch sau.
2. **Suy luận người nói p32/p33:** ánh xạ dựa trên logic lập trường (Zettour hậu cần/ưu tiên Cộng hòa; Rudersdorf tác chiến/dọn Entente), không có dấu hiệu tường minh; nếu sai, p32–p35 đảo lập trường. Độ chắc chắn trung bình-cao; bản dịch hiện tại không bị ảnh hưởng vì không nêu tên người nói.
3. **Giọng nhân vật (m1, m3):** sửa nhỏ nhưng nên áp dụng nhất quán giữa Zettour và Rudersdorf ở các batch kế tiếp.
4. **Handoff thiếu chi tiết `minor_findings` (m8):** không truy được lỗi nhẹ translator đã tự phát hiện.

## 5. Kết luận và next_action

- Đếm mức độ: **nghiêm trọng 0 · vừa 1 · nhẹ 8**.
- Trạng thái đề xuất: `needs_minor_fixes` — không chặn commit về nghĩa; M1 nên xử lý trước khi commit hoặc ghi vào ledger như quyết định tạm.
- `next_action`:
  1. Coordinator ghi vào ledger/handoff lựa chọn tạm cho 3.1–3.3 (khuyến nghị: Cục Hậu cần / Cục Tác chiến / người phụ trách đầu máy toa xe; hoặc giữ cặp "Bộ/Binh đoàn" nhưng khi đó ghi rõ lệch cấp), và ghi chú b07 p000177 cùng thuật ngữ gốc. Không nâng canon.
  2. Người giữ quyền sửa (translator) áp dụng M1 theo lựa chọn của coordinator và các sửa m1–m7 tùy mức ưu tiên; ưu tiên m1, m2, m6.
  3. Sau khi sửa, gửi lại để reviewer ký kiểm tra sửa (fixes-signoff) trước khi commit.
