# Báo cáo phản biện — vol-02-ch-04-b20

- Phạm vi: p000250–p000277 (28 đoạn), `translations/vol-02/ch-04-b20.jsonl`.
- Đã đọc: shared/reviewer, config, handoff b20, source package b20, canon được tham chiếu, mục `chapter4_b20_translation_proposals` (cùng các mục formula/Service Corps/Northern Sea Fleet/Commonwealth/Habergram có sẵn trong sổ pending để đối chiếu gốc từ “formula”), bản dịch b20. Không đọc bản dịch của lô khác.
- Không sửa bản dịch/canon/handoff/ledger/checkpoint. Validator/diff_check: not_run. Commit: null.
- Tổng quan: bản dịch đủ câu, không thiếu/thừa đoạn; phần lớn sát nghĩa. Ba chỗ in nghiêng của nguồn (p000255, p000274, p000276) được giữ bằng `*...*` đúng DEC-P01-002; không đánh dấu thừa ở đoạn nào khác. Không có lỗi nghiêm trọng. Có 3 lỗi vừa (câu rối/thuật ngữ “bridge”), còn lại là nhẹ.

## Phát hiện

### Vừa

**M1 — p000257: câu mở đầu rối cấu trúc.**
Câu dịch gộp “tin xấu”, “đánh thức ông dậy”, “đủ làm ông suýt bóp nát tẩu” thành một chuỗi “khiến… phải… đủ làm…” khó đọc, đối tượng bị đánh thức/đối tượng bóp tẩu bị đẩy xa nhau. Nghĩa nguồn: tin xấu mà người ta phải đánh thức ông dậy để báo đủ làm ông suýt bóp nát tẩu.
Đề xuất: “Đối với Tướng Habergram, tin xấu khiến ông bị đánh thức dậy ấy đủ làm ông suýt bóp nát chiếc tẩu trong tay.” (hoặc tách hai câu).

**M2 — p000258: “cây cầu chỉ huy”.**
“Bridge” ở đây là đài chỉ huy của tàu (đối lập với khu sinh hoạt); “cây cầu” dễ bị đọc thành cây cầu vật lý.
Đề xuất: “đài chỉ huy” (hoặc “cầu tàu”). Đây là đề xuất thuật ngữ, không canon.

**M3 — p000261: câu hỏi tu từ về xác suất bị méo cú pháp.**
“Xác suất thiên văn nào khiến kẻ địch… lại đụng phải…” đọc như “xác suất nào khiến…”, mất ý nguồn là xác suất để sự trùng hợp ấy xảy ra nhỏ đến mức thiên văn. Ngoài ra “auxiliary ship” dịch “tàu tiếp tế” thu hẹp nghĩa (xem L3).
Đề xuất: “Nhưng xác suất để một kẻ địch đã kiên trì chờ đợi, chỉ đánh một đòn rồi vội vã bỏ đi, sau đó lại ‘trên đường về’ đụng phải tàu hỗ trợ và tàu ngầm của Khối Thịnh vượng chung — sự trùng hợp ấy nhỏ đến mức nào chứ?”

### Nhẹ

**L1 — p000273: “họ đã thoát mất”.**
Chủ thể bị trốn thoát là các tàu/hạm đội Entente; p000271 dùng “chúng” cho họ, p000274 lại dùng “Họ” cho phía hải quân (“Họ để cho chúng thoát mất sao?”). “Họ” ở p000273 dễ đọc nhập nhằng với “họ” p000274.
Đề xuất: p000273 “Vâng, có vẻ chúng đã thoát mất.” cho đồng bộ.

**L2 — p000277: “chạm trán được với họ”.**
“Made contact” (tiếp xúc/phát hiện trong tìm kiếm) không phải giao chiến; “chạm trán” hàm ý đụng độ. Đề xuất: “Đến chuyện hai lần bắt được tiếp xúc với họ cũng đã là ăn may rồi.”

**L3 — p000261: “tàu tiếp tế”.**
“Auxiliary ship” là tàu phụ trợ/hỗ trợ; “tiếp tế” suy ra chức năng không có trong nguồn. Đề xuất “tàu phụ trợ” hoặc “tàu hỗ trợ” (gộp với M3).

**L4 — p000262: “Chẳng cần nghĩ ngợi gì cũng thấy.”**
“Thấy” thêm một động từ cảm nhận; nguồn là “không cần cũng chẳng phải suy nghĩ”. Đề xuất: “Thậm chí chẳng cần phải suy nghĩ.”

**L5 — p000257: “Tướng quân Habergram”.**
Sổ pending đã dùng “Tướng Habergram”; “Tướng quân” mang sắc thái cổ/võ hiệp và lệch với cách gọi đã dùng. Đề xuất “Tướng Habergram”.

**L6 — p000267: “ban Hậu cần”, “ban Tình báo”, “ban Tác chiến”.**
Sổ pending đã thiên về “Cục Hậu cần / phía Tác chiến” cho Service Corps/Operations; ở đây dùng “ban”. Đề xuất đồng bộ theo ledger (ví dụ “Cục Hậu cần”, “ban Tình báo”, “ban Tác chiến”) hoặc ghi rõ “ban” là cách gọi staff. Ledger tự nó còn chưa thống nhất (có mục “Quân đoàn Công vụ”); chỉ ghi nhận.

**L7 — p000263: “tàu của ta”.**
“Boat” trong nguồn là cách gọi tàu nhỏ/tàu ngầm; “tàu” chung chung làm mất khác biệt với “ship” ở các đoạn khác. Độ chắc thấp; có thể giữ. Nếu sửa: “chiếc tàu của ta” hoặc “tàu ngầm của ta” (chỉ khi coordinator xác nhận đó là tàu ngầm; tôi không tự suy).

**L8 — p000274: “Hạm đội không phải hoàn hảo”.**
Nên “không hoàn hảo”. Đề xuất: “Hạm đội không hoàn hảo, nhưng họ đã tập hợp được…”.

**L9 — p000276: “phải hứng chịu… buộc phải đưa tài liệu”.**
Lặp “phải… buộc phải”. Đề xuất bỏ một: “Các sĩ quan hải quân bối rối, phải hứng chịu sức ép ấy, đành đưa tài liệu ra và cố giải thích.”

**L10 — p000250: “hẳn sẽ có không ít người”.**
“Hẳn” thêm độ chắc chắn nhẹ. Nguồn chỉ nói việc nhiều người bắt đầu nghĩ vậy là chuyện sớm muộn. Đề xuất: “Chỉ còn là chuyện sớm muộn trước khi không ít người bắt đầu nghĩ như vậy.” Có thể giữ.

## Kiểm tra nhanh theo hạng mục

- Nghĩa/thiếu-thừa: không thiếu câu; không thấy đảo phủ định/logic. Thừa/lệch nhỏ ở L4, L10.
- Đại từ: không có “nó/mình”; không gán giới tính cho người đối thoại; “chúng/họ/ông” nhìn chung nhất quán. Điểm nhập nhằng duy nhất là L1. Lời thoại p000253, p000269, p000272 “chúng ta” và p000263 “của ta” là nhóm nói, không phải điểm nhìn Tanya.
- Nhấn mạnh: đúng (p000255, p000274, p000276 là italic nguồn); không có nhấn mạnh bị bỏ sót hay thêm.
- Văn phong: mượt ở p000253–p000254, p000264–p000270; điểm thô: M1, M3, L9.
- Nhất quán với sổ pending: “Liên minh Entente”, “Hạm đội Biển Bắc”, “Khối Thịnh vượng chung” khớp ledger. “Tướng quân” và “ban Hậu cần” xem L5, L6.

## Thuật ngữ tạm — đề xuất (không canon)

Gốc “formula” = “thuật thức” (ledger P01-formulas và các mục b13–b17 trở đi); “phép thức” là phương án thay thế đã được cân nhắc nhiều lần, không có lý do đổi.

| Mã | Nguồn | Hiện dịch | Khuyến nghị | Độ tin cậy | Ghi chú |
|---|---|---|---|---|---|
| vol02-ch04-b20-heavy-explosion-formula (p000257) | heavy explosion formula | thuật thức nổ mạnh | Giữ | 0.65 | Khớp mục b15/b16 “thuật thức nổ mạnh”; số ít, đúng nguồn. |
| vol02-ch04-b20-gravity-formula (p000257) | gravity formula | thuật thức trọng lực | Giữ | 0.6 | Khớp gốc “thuật thức”; “trọng lực” là cách gọi thường dùng. Chưa có mục cũ để đối chiếu. |
| vol02-ch04-b20-anti-personnel-explosion-formulas (p000258) | anti-personnel explosion formulas | thuật thức nổ chống nhân lực | Giữ “thuật thức nổ chống nhân lực”; không dùng “diệt bộ binh” | 0.55 | Mục tiêu là thủy thủ/người ở khu sinh hoạt, không phải bộ binh nên “diệt bộ binh” sai đối tượng. Cân nhắc thay thế “thuật thức nổ sát thương sinh lực” nếu ledger muốn dùng từ quân sự VN, nhưng “chống nhân lực” sát nguồn hơn. |

Thuật ngữ phụ ghi nhận (chưa có trong ledger b20): “bridge” → “đài chỉ huy” (M2, p000258); “auxiliary ship” → “tàu phụ trợ/hỗ trợ” (L3, p000261). Cả hai là đề xuất.

Không có điểm ảnh hưởng cốt truyện cần hỏi người dùng. Chưa suy luận danh tính nhân vật ngoài văn bản.
