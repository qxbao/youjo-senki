# Báo cáo review tiếp theo — vol-01-ch-01-b05 (Claude)

- Task: `vol-01-ch-01-b05-review-fixes-followup`; vai trò reviewer.
- Phạm vi: 21 đoạn `YS-LN01/Text/chapter003b.xhtml/p000055`–`p000075` (viết tắt `pNNNNNN`).
- Đã đọc: source package, `translations/vol-01/ch-01-b05.jsonl`, báo cáo review trước, handoff, `work/run-state/pending-terms.yml`, bản dịch b01–b04 để đối chiếu thuật ngữ.
- Kiểm tra cơ học: sha256 source package `b09c90b4…` khớp handoff; 21/21 đoạn, thứ tự và `segment_id` khớp nguồn và handoff; `source_sha256` từng dòng khớp; mọi dòng có đủ trường (`status: draft`, `translator`, `glossary_version`, `source_sha256`, `notes`), không có trường lạ. Validator/diff_check: `not_run`.
- Mọi lựa chọn thuật ngữ dưới đây là đề xuất tạm, chưa phải canon.

## Kết luận

Hai lỗi mức vừa của báo cáo trước (F-01, F-02) **đã xử lý xong**. Không có lỗi nghiêm trọng hoặc vừa mới. Còn một số lỗi nhẹ cũ và hai điểm nhẹ mới (N-01, N-02). Không có mục nào ảnh hưởng cốt truyện hoặc cần hỏi người dùng. Lô đủ điều kiện về mặt review để chuyển sang validator/diff_check và commit.

## Xác nhận hai lỗi mức vừa

**F-01 · p000058 — ĐÃ XỬ LÝ.**
- Bản dịch dùng "hiệu lực tốt" ở cả hai lần lặp, bỏ "hiệu quả"; ghi chú nêu `b05-good-effect` với phương án khác "hiệu quả tốt", độ tin cậy 0,60, pending.
- Khớp b02: p000014 dùng "bắn hiệu lực", không còn "hiệu quả" trong b01–b04 theo nghĩa này (hai chỗ "hiệu quả" ở b03 và p000065 là nghĩa thường, không liên quan). Khớp sổ: `b02-fire-for-effect` (ưu tiên "bắn hiệu lực", loại "bắn hiệu quả") và `b05-good-effect`. Ghi chú vẫn giữ "không suy ra tiêu diệt hoàn toàn".

**F-02 · p000066, p000068 — ĐÃ XỬ LÝ.**
- p000066 dùng "hỏa lực áp chế", p000068 dùng "dẫn bắn áp chế"; không còn "chế áp" làm phương án chính ở đâu trong b01–b05 (chỉ còn trong ghi chú với vai trò phương án khác).
- Khớp sổ `b05-suppressive-fire` (đề xuất "hỏa lực áp chế", phương án khác "hỏa lực chế áp", 0,7). Ghi chú p000066 và p000068 trỏ chéo đúng.

## Các điểm nhẹ đã sửa (xác nhận)

| Mục | Kết quả |
|---|---|
| F-04 "pháo đội" p000059, p000067 | Đã sửa, đồng bộ; khớp `b05-batteries` |
| F-06 p000059 | Đã bỏ "mình" trong trần thuật, dùng "nó" |
| F-07 p000060 | Đã thành "không chỉ là giấc mơ viển vông" |
| F-05 p000066 | "địch" thay "chúng"; "tan đội hình" |
| F-08 p000070 | "Norden Control" thay "bộ phận kiểm soát"; mã ghi chú `b05-airman-radio-set`, `b05-control-of-the-air` khớp sổ |

## Kiểm tra theo yêu cầu

- **Mã ghi chú ↔ sổ:** mọi mã `b05-*` trong ghi chú đều có trong sổ pending và ngược lại, không lệch (F-10 cũ đã giải quyết). Mọi mục vẫn `pending`, không có mục nào bị nâng thành canon. Ghi chú khớp nội dung dòng hiện tại (không còn nhắc "chế áp" làm lựa chọn chính, "Norden Control" đã phản ánh).
- **Nhấn mạnh (DEC-P01-002):** nguồn có đúng hai vùng in nghiêng (p000055, p000070); bản dịch có đúng hai cặp `*…*` ở hai đoạn đó, đúng phạm vi, không thêm ở đoạn khác.
- **Chú thích:** nguồn có đúng một dấu chú thích ở p000056; bản dịch có đúng một ⁵ ở p000056, đặt sau tên sự kiện; không có dấu thừa. Nội dung chú thích vẫn không thuộc đầu vào được giao nên chưa đối chiếu được.
- **Nghĩa:** p000066 (hedge "tôi cho rằng", vô hiệu hóa ≠ tiêu diệt, bộ binh địch tan hàng) và p000070 (phủ định thời tiết/nhiễu, nguyên nhân từ mỏ khoáng sản, mục đích nhắm tàn quân) giữ đúng; phần còn lại không thấy sai nghĩa sau chỉnh sửa. Đại từ "nó"/"mình" nhất quán theo DEC-P01-001.
- **Chỉ ghi vào bản dịch và báo cáo:** `git status` chỉ thấy các tệp ngoài phạm vi này là tệp chưa theo dõi của lô b05; không có tệp canon bị sửa.

## Lỗi nhẹ còn lại (không chặn)

- **N-01 · p000060** — "Một vị trí ở hậu phương không chỉ là giấc mơ viển vông" đọc ổn, nhưng "bộ phận nhân sự" vẫn chưa có căn cứ đồng bộ với các lô trước (đã ghi ở sổ, 0,65).
- **N-02 · p000071** — ví von chim dodo/gà tây giữ đúng; cân nhắc ghi thêm vào sổ nếu coordinator muốn một phương án thống nhất cho "chim dodo" ở các tập sau. Không bắt buộc.
- Còn nguyên từ báo cáo trước, tùy chọn: F-03 (tên sự kiện Fuji, "trình diễn" so với "thao diễn", đợi đối chiếu chú thích), F-08 (một số từ vựng p000070: "lố bịch", "đủ để gọi là “rõ”" dễ nhầm với "rõ" kiểu vô tuyến, "điềm nhiên", "bộ vô tuyến hàng không"), F-09 (câu chữ "đến tận nơi đôi mắt xanh…" hơi gượng), F-11 ("Hết" cho "Over", khớp b01 đang dùng "Hết", độ tin cậy 0,5).

## Đề xuất thuật ngữ (đều pending, không phải canon)

| source_term | đề xuất VI | khác | độ tin cậy | segment |
|---|---|---|---|---|
| good effect | hiệu lực tốt | hiệu quả tốt | 0,6 | p000058 |
| suppressive fire | hỏa lực áp chế / dẫn bắn áp chế | hỏa lực chế áp | 0,7 | p000066, p000068 |
| batteries | pháo đội | các đơn vị pháo binh; khẩu đội | 0,6 | p000059, p000067 |
| Control (rút gọn) | Norden Control | đài kiểm soát Norden | 0,6 | p000070 |
| Over (vô tuyến) | Hết | — | 0,5 | p000074 |

Các mục còn lại giữ như bảng của báo cáo trước.

## Rủi ro

- Nội dung chú thích ⁵ chưa được đối chiếu (ngoài đầu vào được giao); tên "buổi trình diễn hỏa lực Fuji" có thể phải đổi sau khi đọc chú thích.
- "Hết" cho "Over" ở độ tin cậy thấp; cần thống nhất toàn tập khi có đủ b01–b05.
- Validator và diff_check chưa chạy; phải đạt trước khi tính lô hoàn tất và commit.

## Trạng thái

- Lỗi nghiêm trọng: 0. Lỗi vừa: 0. Lỗi nhẹ: 7 còn lại, đều tùy chọn (F-03, F-05 phần "chúng" ở p000065/p000067, F-08, F-09, F-11, N-01, N-02); F-04/F-06/F-07 đã xử lý.
- Review: đạt; bước tiếp theo là validator/diff_check do coordinator/translator chạy.
