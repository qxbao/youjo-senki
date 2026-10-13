# Báo cáo phản biện — vol-02-ch-04-b16 (Claude)

Phạm vi: 32 đoạn `YS-LN02/Text/part0024.xhtml/p000141`–`p000172`. Người phản biện không sửa bản dịch, canon, handoff, ledger hay checkpoint. Mọi lựa chọn bên dưới là đề xuất, không phải canon. Mã đoạn dưới đây viết tắt `pNNNNNN` = `YS-LN02/Text/part0024.xhtml/pNNNNNN`.

## 1. Kiểm tra phạm vi và schema

- Package nguồn `work/vol-02/batches/ch-04-b16-source.jsonl`: SHA-256 khớp handoff (`835da13a…27c7ed`); `source_sha256` mỗi đoạn khớp `3ac53161…0a`.
- `translations/vol-02/ch-04-b16.jsonl`: 32 dòng, thứ tự và `segment_id` khớp 1–1 với package (p000141…p000172), không thiếu, không thừa, không trùng. Mọi dòng có đúng bộ khóa `segment_id, translation, status, translator, glossary_version, source_sha256, notes`; `status: draft`; `glossary_version` và `source_sha256` khớp handoff. `notes` rỗng ở mọi dòng, nhất quán với `findings: []` và `pending_term_count: 4` trong handoff.
- Lần lỗi schema ban đầu đã được sửa chỉ ở metadata: schema hiện tại hợp lệ và không thấy dấu hiệu đoạn bị cắt, gộp hay lệch phạm vi. Reviewer không có bản trước sửa nên không đối chiếu được "không đổi nội dung dịch"; chỉ xác nhận trạng thái hiện tại.
- Validator/diff-check: not_run (theo vai trò).

## 2. Tóm tắt

Bản dịch nhìn chung chính xác, đủ đoạn, giọng Việt tự nhiên, không có thêm/bớt cốt truyện. Không có lỗi nghiêm trọng. Còn 4 lỗi mức vừa (một chủ thể bị đảo, đại từ/sắc thái ở p000158, nhấn mạnh bị bỏ) và 12 lỗi nhẹ. Đề nghị sửa 4 lỗi vừa trước khi tính hoàn tất.

## 3. Phát hiện mức vừa

**V1 — p000162: chủ thể "There they were…" bị đảo.**
Căn cứ: sau "However…" (p000161), "họ" xuất hiện tại điểm hẹn là phía Đế quốc (khớp p000163 "tiểu đoàn pháp sư xuất hiện đột ngột" và p000165). Bản dịch "Họ đã đến điểm hẹn…" trong cùng đoạn có "Họ vừa kịp chuyển giao" (phía Khối Thịnh vượng chung) nên người đọc hiểu hai "họ" là một và mất ý "địch đã có mặt ở nơi chỉ vài người biết". Ngoài ra "đáng lẽ phải biết" dễ hiểu thành "lẽ ra phải biết mà không biết".
Đề xuất: tách chủ thể rõ, ví dụ "Vậy mà phía Đế quốc đã có mặt tại điểm hẹn mà lẽ ra chỉ một số ít người được biết." Độ chắc chắn trung bình-cao; nếu coordinator muốn trung lập tuyệt đối thì dùng "đối phương".

**V2 — p000158: "Hắn" cho thuyền trưởng.**
Căn cứ: nguồn dùng "he" trung tính cho thuyền trưởng; p000159–p000171 bản dịch dùng "ông". "Hắn" thêm sắc thái miệt thị không có trong nguồn (style-guide: không thêm sắc thái phán xét) và lệch với phần còn lại của lô. DEC-P01-001 không bao phủ chủ thể này.
Đề xuất: "ông" (hoặc "viên thuyền trưởng") cho cả ba lần ở p000158.

**V3 — p000158: "đám người dưới lòng đất" cho "the subterranean".**
Căn cứ: "đám" thêm sắc thái khinh miệt và "người" tự gán thực thể; chỉ ngữ trong nguồn có vẻ liên quan lối chơi chữ ngầm/"mole"/lặn (thâm nhập vs lặn). Chưa đủ chứng cứ về chỉ ngữ.
Đề xuất tạm: trung lập, sát chữ, ví dụ "những kẻ hoạt động dưới lòng đất/ngầm"; ghi bất định vào ledger (dưới) và không giải thích thêm.

**V4 — p000157, p000158: bỏ nhấn mạnh có trong nguồn (DEC-P01-002).**
Căn cứ: nguồn nhấn mạnh tên tàu ở p000157 và câu "có gián điệp trong cơ quan tình báo" ở p000158; p000165 dịch đã giữ `*Lytol*`, nên p000157 `Syrtis` không có dấu là không nhất quán.
Đề xuất: `*Syrtis*` ở p000157; `*Có một gián điệp cài trong cơ quan tình báo.*` ở p000158.

## 4. Phát hiện mức nhẹ

- N1 p000142: "lo ngại" bị thay bằng "nghĩ… có lẽ", mất sắc thái lo lắng; có thể "Chợt tôi lo mười mét có khi không đủ".
- N2 p000143: "chúng" cho đồng đội, trong khi p000147/p000154 dùng "họ" (nên thống nhất "họ"); "thiếu tự tin" cho under-confident dễ hiểu sai thành nói về người, gợi ý "hơi dè dặt/an toàn quá mức".
- N3 p000144: "Có thể chúng ta đang ở…" đọc như không chắc về vị trí; đúng là nhượng bộ ("dù chúng ta đang ở…"). "nhanh chóng và thận trọng" hơi lệch "delicate" (nhạy cảm/tế nhị).
- N4 p000146: "Rõ" gợi người đáp lệnh cấp trên; người nói chưa rõ. Dạng trung lập: "Được. Bắn!".
- N5 p000150: (a) "should be in" là suy đoán/kỳ vọng đã ghi, bản dịch thành quy phạm "cần được ghi"; (b) "compromising myself" bị dịch thành "giảm thiểu trách nhiệm", lệch sang ý để mình bị vướng/bất lợi ít nhất; (c) "We've seen it" chỉ vật đã thấy, bản dịch "chứng kiến chuyện này" đổi tham chiếu.
- N6 p000152: "đồng loạt" là thêm nhỏ; nguồn là hỏa lực có kỷ luật/đều.
- N7 p000154: "đổ bộ" gợi đổ bộ vào bờ; gợi ý "áp sát lên tàu ngầm/lên tàu".
- N8 p000158: dấu chú thích 16 không được giữ. Chưa có quyết định về chú thích (style-guide), nên chỉ ghi nhận rủi ro; không bắt buộc sửa. Lối chơi chữ mole/subterranean cũng bị làm phẳng (xem V3).
- N9 p000160: "sĩ quan hàng hải" dễ hiểu là hàng hải dân sự; cân nhắc "sĩ quan hoa tiêu/dẫn đường".
- N10 p000167: mệnh đề điều kiện "would be permissible" thành khẳng định "cũng được phép"; nên giữ điều kiện ("sẽ được chấp nhận ở mức nào đó").
- N11 p000171: "nếu chúng lặn xuống" mơ hồ, có thể hiểu "chúng" = pháp sư; nên "nếu tàu lặn xuống".
- N12 p000172: "họ bắn trúng thân tàu" mơ hồ về tác nhân (nguồn là thân tàu của mình bị trúng); nên "nếu thân tàu bị bắn trúng".

Ghi chú không tính lỗi: p000145 thêm "mét" sau "mười lăm" là hợp lý theo ngữ cảnh; hai "tôi" tự quy chiếu nên giữ (xem rủi ro bên dưới).

## 5. Đại từ và nhấn mạnh

- Tanya tự xưng "tôi" ở p000142–p000152. DEC-P01-001 chỉ quy định "mình" cho nội tâm và "nó" cho trần thuật ở giai đoạn đã nêu, cấm tự mở rộng; nguồn ở lô này là ngôi thứ nhất nên "tôi" là lựa chọn trung lập tạm chấp nhận. Đề nghị coordinator xác nhận trong ledger, không coi là canon.
- Chuyển cảnh sang Syrtis từ p000157 là phần quan trọng nhất về chủ thể; ngoài V1, V2, N11, N12 không thấy lẫn lộn khác.
- Chỉ p000165 có `*…*`; xem V4.

## 6. Bốn thuật ngữ pending

| id | đề xuất của translator | khuyến nghị reviewer |
|---|---|---|
| vol02-ch04-b16-heavy-explosion-formulas (p000152) | thuật thức nổ mạnh | Giữ tạm. Lưu ý "heavy" là phân loại nặng; nếu chỗ khác phân biệt với "explosion formula" thường thì nên "nổ hạng nặng". Không kiểm chứng được "gốc thuật thức" ngoài phạm vi lô. |
| vol02-ch04-b16-commonwealth (p000157, p000166) | Khối Thịnh vượng chung | Giữ tạm, nhất quán cách viết hoa. Ở p000166 "trung lập" đi cùng, hợp lý. |
| vol02-ch04-b16-s-class-submarine (p000157, p000171) | tàu ngầm lớp S | Giữ tạm; "lớp" là cách gọi phổ biến cho class. |
| vol02-ch04-b16-computation-orb (p000151) | quả cầu tính toán | Giữ tạm; độ chắc chắn thấp hơn, cần đối chiếu với các lô khác. |

Thuật ngữ mới chưa vào ledger (gợi ý ghi pending, độ chắc chắn thấp, không canon): "Office of the Admiralty" → "Bộ Hải quân" (p000159, p000164); "auxiliary ship" → "tàu phụ trợ" (p000166); "firing data table" → "bảng thông số khai hỏa" (p000150); "unit logs" → "nhật ký đơn vị" (p000149); "navigation officer" → "sĩ quan hàng hải" (p000160); "the subterranean" → "đám người dưới lòng đất" (p000158, nên sửa, xem V3). Không có quyết định nào ảnh hưởng cốt truyện cần hỏi người dùng.

## 7. Kết luận

Cần sửa 4 lỗi mức vừa (V1–V4) bởi người giữ quyền sửa rồi chạy lại validator; không có hard stop. Lỗi nhẹ nên sửa trong cùng lượt nếu thuận tiện.
