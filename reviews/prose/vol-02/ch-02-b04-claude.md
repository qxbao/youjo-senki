# Báo cáo phản biện văn phong và ngữ nghĩa — vol-02-ch-02-b04 (batch chẵn, có cờ new_pending_terms)

- **Người phản biện:** Claude (reviewer; chỉ ghi báo cáo này, không sửa bản dịch, handoff, canon, ledger hay run-state). Báo cáo không trích văn bản nguồn.
- **Phạm vi:** 21 đoạn p000072–p000092 (`YS-LN02/Text/part0014.xhtml/…`, viết tắt `pNNNNNN`). Đã đọc: `agents/shared.md`, `agents/coordinator.md`, `config/translation-pipeline.yml`, handoff b04, gói nguồn b04, bản dịch b04, `canon/*`, các mục liên quan trong `work/run-state/pending-terms.yml` (mục `chapter2_b04_translation_proposals`, quân hàm/xưng hô b08 ch01, sĩ quan phụ tá, tập đoàn quân/cụm tập đoàn quân, Tổ quốc, Tanya narration, Weiss). Không đọc bản dịch của batch khác. (Ghi chú minh bạch: có một lần đếm số dòng chứa một cụm từ trên toàn bộ `translations/vol-02/`; chỉ lấy số đếm, không đọc nội dung.)

## 1. Kết luận

- **Kết luận:** `pass_with_fixes`.
- **Mức nghiêm trọng:** serious = 0; moderate = 6 (M1–M6); minor = 9 (m1–m9).
- **next_action:** người giữ quyền sửa xử lý M1–M6 và cân nhắc minor, chạy lại validator + `git diff --check`, rồi commit. Cần reviewer xác nhận nhanh p000072, p000073, p000075, p000080, p000084, p000090, p000091, p000092 sau khi sửa.

## 2. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự ID | Đạt: 21 đoạn p000072–p000092, đúng thứ tự, khớp 1:1 với gói nguồn. |
| Hash gói nguồn | Đạt: `0085352774…27b0d659` khớp handoff. |
| `source_sha256` mỗi record | Đạt: khớp gói nguồn và handoff. |
| `glossary_version` | Đạt: khớp handoff (`d5f19d64…`). |
| Validator | Đạt (`validate_translation.py`: 21 hàng khớp thứ tự và metadata; gói nguồn bị Git bỏ qua). |
| `status` / `notes` | `draft` toàn bộ; `notes` rỗng; không có ghi chú làm việc lọt vào translation. |
| Nhấn mạnh (DEC-P01-002) | Đạt: nguồn không có thẻ nhấn mạnh/nghiêng ở đoạn nào; bản dịch không có `*…*`. Không đánh dấu thừa. |
| Định dạng thoại | Đạt: dấu ngoặc kép giữ đúng ở p000074, p000075, p000080, p000082, p000088, p000090; p000083 giữ nguyên chuỗi ngoặc lồng bốn lớp như nguồn. Các đoạn không ngoặc (p000091, p000092) là nội tâm/tường thuật, bản dịch giữ không ngoặc — đúng. |
| Phủ định / logic | Không phát hiện đảo nghĩa hay mất phủ định. |

## 3. Phát hiện

### Moderate

- **M1 — p000072: đổi điểm nhìn ngôi thứ nhất sang ngôi thứ ba.**
  Đoạn nguồn là nội tâm ngôi thứ nhất của Tanya (nhìn bằng mắt “tôi”, “tôi hiểu”). Bản dịch viết “Tanya hiểu vì sao…”, trong khi các đoạn nội tâm ngôi thứ nhất khác của batch (p000077–p000079, p000085–p000087, p000089) dùng “mình” đúng DEC-P01-001. Hậu quả: cùng một mạch nội tâm bị đổi giọng, và người đọc thấy một người kể bên ngoài thay vì Tanya.
  Đề xuất: “Đưa mắt nhìn khắp hàng ngũ từ trên bục, mình hiểu vì sao người ta có thể thấy họ là một đơn vị kỷ luật, tràn đầy tự tin.” Độ tin cậy 0.85.

- **M2 — p000084: đại từ “cô” cho Tanya trong trần thuật.**
  DEC-P01-001 (đã duyệt) dùng “nó” trong trần thuật về Tanya; ledger `vol02-ch01-b01-tanya-narration` và các batch sau chọn lặp tên/lược chủ ngữ và tránh “cô”. Bản dịch dùng “cô” ở p000084, trong khi p000072–p000092 còn lại dùng tên “Tanya” (p000073, p000074, p000081). Đề xuất: “Tiếng đáp vang dội khiến Tanya tạm hài lòng.” Độ tin cậy 0.9.

- **M3 — p000090: người nghe và người nói bị lẫn (đoạn Weiss báo cáo).**
  Câu mở đầu của Weiss là đáp lời gọi của Tanya; phần sau nói với toàn đơn vị, nhắc lại điều “chỉ huy của chúng ta” đã nói. Bản dịch “Thưa chỉ huy. Như chỉ huy đã nghe…” biến người nghe thành chính Tanya và làm mất vế “từ chỉ huy của chúng ta”, thành ra Weiss bảo Tanya rằng chính Tanya đã nghe điều Tanya nói — vô nghĩa. Đây là lỗi người nghe/đại từ ngôi hai, không phải thuật ngữ.
  Đề xuất: “Thưa chỉ huy. Như các vị đã nghe từ chỉ huy của chúng ta, đơn vị này sẽ hoạt động với tư cách một tiểu đoàn cơ động.” (“các vị” theo ledger plural-address; xem M5). Độ tin cậy 0.75; nếu coordinator muốn tránh chọn ngôi hai, có thể dùng “Như đã được chỉ huy thông báo, đơn vị này…”.

- **M4 — p000091, p000092: “army group” bị dịch thành “tập đoàn quân”.**
  Ledger: Army = “Tập đoàn quân” (ví dụ Seventeenth Army → Tập đoàn quân số 17), regional army group = “Cụm tập đoàn quân khu vực”, Eastern Army Group = “Cụm tập đoàn quân phía Đông”. Bản dịch dùng “tập đoàn quân” cho army group ở cả hai đoạn, làm lẫn hai cấp tổ chức. Đề xuất: “trực thuộc một cụm tập đoàn quân” (p000091) và “phối hợp nhiều trước với một cụm tập đoàn quân” (p000092). Độ tin cậy 0.8.

- **M5 — p000075, p000080: “Các anh” lệch ledger “Các vị” và suy ra giới tính/thân phận.**
  Ledger `vol02-ch01-b08-ranks-and-address` (Gentlemen = “Các vị”) và mục plural-address chương 0 (“các vị” trung tính) đều chọn “các vị”. “Các anh” (a) giả định toàn bộ người nghe là nam, (b) mang sắc thái thân mật/ngang hàng, trái nguyên tắc DEC-P01-001 là không suy ra quan hệ khi thiếu ngữ cảnh. Đề xuất: “Các vị, hãy tự hào…” (p000075) và “Các vị, Dacia chẳng qua…” (p000080). Độ tin cậy 0.7; thay thế “các cậu” không khuyến nghị.

- **M6 — p000073: lệch mức chắc chắn và đối tượng của vế đầu.**
  Nguồn nói đơn vị “chưa sẵn sàng như Bộ Tổng tham mưu *có thể muốn tin*” (niềm tin, mức không chắc). Bản dịch “như Bộ Tổng tham mưu hẳn mong muốn” đổi “tin” thành “mong muốn” và thêm “hẳn” (chắc chắn), làm lệch cả đối tượng (điều họ tin ≠ điều họ muốn) lẫn độ chắc chắn. Đề xuất: “chưa sẵn sàng như Bộ Tổng tham mưu có thể muốn tin.” Độ tin cậy 0.8.

### Minor

- **m1 — p000073:** “sau lần đầu ra trận” làm mất ẩn dụ “rửa tội bằng lửa”, trong khi ngay sau đó là hình ảnh tôn giáo (Paul, ban phước, đúng đường); chuỗi ẩn dụ này là mạch của đoạn. Đề xuất: “sau khi được rửa tội bằng lửa” hoặc “sau trận thử lửa đầu tiên”; nên chọn “rửa tội bằng lửa” để giữ mạch với p000073 vế Paul.
- **m2 — p000073:** “báo rằng họ đã đi đúng đường” lược “cho mọi người”; nguồn nói thông báo cho tất cả. Đề xuất: “báo cho tất cả rằng họ đã đi đúng đường”.
- **m3 — p000074:** “nhưng nó gượng gạo đến lạ” — “nó” dễ bị hiểu là Tanya (đại từ DEC-P01-001) thay vì nụ cười; “đến lạ” thêm sắc thái không có. Đề xuất: “nhưng nụ cười ấy trông gượng gạo quá.”
- **m4 — p000074:** “hèn nhát” (nguồn: bị khuất phục/co rúm) thêm phán xét đạo đức; “những kẻ tinh hoa” thêm sắc thái miệt thị với “kẻ”. Style guide cấm thêm sắc thái phán xét. Đề xuất: “bầy chó lai cụp đuôi chỉ sau một lần thất bại” và “lớp tinh hoa thuần chủng” (xem mục 4.3). Cấu trúc “Không ai đối mặt nghịch cảnh yếu đuối hơn…” có thể gọn hơn: “Không ai yếu đuối trước nghịch cảnh hơn lớp tinh hoa thuần chủng, và Tanya cũng vậy.”
- **m5 — p000076:** (a) “Không quân đội nào” đầu câu dễ đọc nhầm là “Không quân” (lực lượng); đề xuất “Chẳng đội quân nào có thể thắng mãi.” (b) “vùng Vịnh” nên viết “Vùng Vịnh” theo ledger `Gulf War` → Chiến tranh Vùng Vịnh. (c) “huênh hoang” mạnh hơn “khoe khoang/tuyên bố”; cân nhắc “rêu rao”/“khoe khoang”.
- **m6 — p000082:** “Hoàng đế Bệ hạ” — thứ tự và viết hoa lạ; đề xuất “Bệ hạ Hoàng đế” hoặc “Hoàng đế bệ hạ”. Giữ “Tổ quốc” (đúng ledger fatherland).
- **m7 — p000083, p000090:** “thưa chỉ huy” khác ledger b08 (“ma’am = thưa Thiếu tá”). Chấp nhận được vì đoạn không nêu cấp bậc và “chỉ huy” trung tính; không sửa văn bản, đề nghị coordinator ghi biến thể này vào ledger (không promote canon).
- **m8 — p000086:** “cao quý” thay cho “beautiful” (nguồn nêu “đẹp”, không phải “cao quý”). Đề xuất: “có vẻ vừa đẹp đẽ vừa đáng kính” (hoặc “cao đẹp”); độ tin cậy 0.6.
- **m9 — p000072:** “troops” → “hàng ngũ” (nguồn nói về binh sĩ, không phải hàng); “Quân trang” (đồng phục) khác “field gear” (trang bị dã chiến). Đề xuất: “Đưa mắt nhìn khắp đám binh sĩ từ trên bục…” và “Trang bị dã chiến được đánh bóng hoàn hảo”.

## 4. Thuật ngữ đề xuất của translator (không promote canon)

### 4.1 Copernican-level revolution (p000073)
- **Dịch đề xuất:** “cuộc cách mạng kiểu Copernicus”.
- **Đánh giá:** “kiểu” chuyển nghĩa từ *tầm vóc* (cấp độ) sang *loại hình*, làm yếu phép so sánh về quy mô. “Cách mạng Copernicus” là cách nói quen thuộc trong tiếng Việt.
- **Tạm dùng:** “cuộc cách mạng tầm Copernicus”. Thay thế: “cuộc cách mạng Copernicus”; “cuộc cách mạng kiểu Copernicus” (phương án của translator, chấp nhận được nhưng yếu hơn). Độ tin cậy 0.65.

### 4.2 Paul’s conversion (p000073)
- **Dịch đề xuất:** “cuộc cải đạo của Thánh Paul”.
- **Đánh giá:** “cải đạo” trong tiếng Việt thường chỉ việc đổi từ tôn giáo này sang tôn giáo khác (trường hợp Paul là hoán cải/hồi tâm trên đường Damascus), nên hơi lệch; “Thánh Paul” là dạng lai (Latin + “Thánh”) nhưng nhất quán với việc dự án giữ tên Latin (Copernicus, Weiss). Dạng Công giáo là “Phaolô”.
- **Tạm dùng:** “sự hoán cải của Thánh Paul”. Thay thế: “cuộc cải đạo của Thánh Paul”; “sự hoán cải của Thánh Phaolô”. Độ tin cậy 0.5. Giữ nhất quán một dạng tên cho cả chương.

### 4.3 Game dogs / purebred elites (p000074)
- **Dịch đề xuất:** “chó chọi / giới tinh hoa thuần chủng”.
- **Đánh giá:** “chó chọi” đúng nghĩa chó đấu và song song được với “chó lai” (tương phản thuần chủng–lai) nên giữ. Hai rủi ro: (a) “kẻ” thêm miệt thị; (b) “thuần chủng” áp cho người có thể gợi thuyết thuần chủng chủng tộc trong bối cảnh Đế quốc kiểu Đức; tuy ẩn dụ giống nòi là chủ ý, cần giữ nó ở bình diện chọn giống, không chạm vào chủng tộc.
- **Tạm dùng:** “chó chọi” / “lớp tinh hoa thuần chủng”. Thay thế: “chó đấu”; “tầng lớp tinh hoa được tuyển chọn” (mất ẩn dụ giống nòi nên không khuyến nghị). Độ tin cậy 0.55.

### 4.4 War fever (p000081)
- **Dịch đề xuất:** “cơn sốt chiến tranh”.
- **Đánh giá:** “cơn sốt” trong tiếng Việt thường mang nghĩa cơn sốt (đầu cơ, trào lưu); ở đây hiểu được là “hăng máu chiến tranh”, hợp ngữ cảnh ngay sau đó (không tốt trong bình thường, tốt khi sắp ra trận). “Cuồng chiến” gần nghĩa “cuồng nhiệt chiến đấu” nhưng nghiêng bệnh lý/miệt thị hơn.
- **Tạm dùng:** giữ “cơn sốt chiến tranh”. Thay thế: “cơn cuồng chiến”; “máu hiếu chiến”. Độ tin cậy 0.55. Giữ nhất quán với “mê chiến đấu” (p000087).

### 4.5 Mobile battalion (p000090, p000091)
- **Dịch đề xuất:** “tiểu đoàn cơ động”.
- **Đánh giá:** “cơ động” là thuật ngữ quân sự Việt cho đơn vị di chuyển nhanh, không gắn vào một đại đơn vị; “lưu động” gợi chuyển từ nơi này sang nơi khác (đội lưu động), kém hợp.
- **Tạm dùng:** “tiểu đoàn cơ động”. Thay thế: “tiểu đoàn lưu động”. Độ tin cậy 0.7.

## 5. Các điểm đã kiểm tra, không có vấn đề

- Tên đơn vị “Tiểu đoàn Pháp sư Không quân 203” (p000073, p000091) khớp ledger b06/b10.
- “Trung úy Weiss” (p000073, p000088) khớp ledger cấp bậc; “phó chỉ huy”/“sĩ quan phụ tá” (p000089) khớp ledger.
- “Bộ Tổng tham mưu” nhất quán (p000073, p000074, p000091, p000092).
- “Tổ quốc” = fatherland (p000082, p000086) khớp ledger.
- p000076–p000079: tham chiếu lịch sử, quan hệ “nhân quả” (mất nhuệ khí → hỗn loạn) và lập luận lương–bổn phận đều giữ đúng nghĩa.
- p000078: phép nhượng bộ “dù có công nghệ ma pháp…” và phần “nhà khoa học điên” không đảo nghĩa.
- p000085, p000087: ngữ khí nội tâm “mình”, “Dĩ nhiên…” khớp DEC-P01-001.
