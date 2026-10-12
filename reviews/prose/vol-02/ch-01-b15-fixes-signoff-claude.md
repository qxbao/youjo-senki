# Ký duyệt sửa lỗi — vol-02-ch-01-b15-fixes

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon).
- Phạm vi: chỉ `p000021`, `p000023`, `p000034` của `YS-LN02/Text/part0012.xhtml`. Đối chiếu với báo cáo gốc `reviews/prose/vol-02/ch-01-b15-claude.md`, handoff b15, `translations/vol-02/ch-01-b15.jsonl` hiện tại và gói nguồn cục bộ b15. Không đọc bản dịch/nguồn của lô khác.
- Không trích câu nguồn. Mọi lựa chọn thuật ngữ vẫn là đề xuất tạm (pending), không phải canon.
- Mã đoạn viết tắt `pNNNNNN` = `YS-LN02/Text/part0012.xhtml/pNNNNNN`.

## Kết luận

**fixes_pass: false** — còn 1 lỗi mức vừa (sót một chỗ chưa đồng bộ ở p000034). Sửa đúng một cụm từ là đạt.

Đếm còn lại: **nghiêm trọng 0 · vừa 1 · nhẹ 0**.

## 1. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Hash gói nguồn b15 | `f340547f…c28a`, khớp `source_sha256`/handoff |
| `source_sha256` p21/p23/p34 | Khớp `3ac53161…` |
| Mã đoạn, `status`, `glossary_version` | Giữ nguyên, `status: draft`, `notes` rỗng |
| Handoff | Có `provisional_review_choices`: Cục Hậu cần / Cục Tác chiến, `pending_status: provisional_non_canon`; khớp hướng đề xuất của báo cáo gốc |

## 2. Kiểm tra từng mục

### M1 — tên hai cơ quan song song: **chưa đóng hoàn toàn**
- p21: dùng "Cục Hậu cần". Đạt.
- p34, câu đầu: "Cục Tác chiến và Cục Hậu cần" — song song, cùng cấp. Đạt.
- **p34, câu cuối: vẫn còn "Bộ Tác chiến"** (theo quan điểm của …). Cùng đoạn, cùng cơ quan, nhưng hai nhãn khác nhau ("Cục" rồi "Bộ"). Đây là chỗ sót khi sửa; hậu quả: trong chính p34 độc giả thấy hai cơ quan khác nhau, và "Bộ" lại gợi ngang cấp "Bộ Tổng tham mưu" — đúng điều M1 muốn tránh.
- Yêu cầu sửa (mức vừa, một cụm): đổi "Bộ Tác chiến" ở câu cuối p34 thành "Cục Tác chiến". Không cần sửa gì khác trong đoạn.
- Đã rà toàn bộ bản dịch b15 hiện tại cho các nhãn liên quan: ngoài chỗ trên không còn "Binh đoàn" hay "Bộ Hậu cần"; nhãn "Cục Hậu cần" xuất hiện ở p21 và p34.
- Ghi nhận theo yêu cầu: b07 p000177 giữ cách dịch tạm khác đã commit trước đó. Đây là việc nhất quán xuyên lô để xử lý sau; **không** yêu cầu và không đề nghị sửa b07 ở đợt này. Coordinator nên ghi nhận trong sổ pending rằng hai đoạn cùng thuật ngữ gốc, nhãn tạm khác nhau.

### p000023 — ngôi thứ nhất "tôi": **đạt**
- Câu của Zettour "nếu cần, tôi có thể điều…" nay dùng "tôi", đồng nhất với p21/p25/p35. Không đổi nghĩa: vẫn là cam kết của người nói, điều kiện "nếu cần", đối tượng (tàu gần ba trăm nghìn tấn, cơ sở cảng phía bắc, mục đích đổ bộ) giữ nguyên.
- "của ta" / "mà ta có thể trưng dụng" ở các câu trước là ngôi gộp của phía Đế quốc, hợp lý và khớp nghĩa nguồn; không cần đổi. Số liệu, thời điểm ("từ khi chiến tranh nổ ra") và hàm ý "kế hoạch đã cân nhắc nhiều lần" không đổi.

### p000021 — cách dịch đầu máy toa xe: **đạt**
- "những người phụ trách đầu máy toa xe thuộc Cục Hậu cần": giữ đủ hai thành tố (đầu máy + toa xe), vai trò phụ trách/quản lý, và nguồn tin là người trong ngành (Zettour nghe từ họ). Không thêm/bớt nghĩa, không biến thành chức danh chính thức hay người điều hành cả đội phương tiện.
- Câu xin lỗi, đối đáp "Tướng von Rudersdorf" và nhận định hậu cần ở Norden "sẽ chẳng sớm được cải thiện" giữ đúng phủ định và thời gian. Lưu ý nhỏ, không phải lỗi: "Tướng" vẫn là cách trung tính vì cấp chưa chốt (ghi nhận từ báo cáo gốc 3.4).

## 3. Rủi ro còn lại

1. Nếu commit mà không sửa chỗ sót ở p34, ledger/handoff ghi "Cục Tác chiến" nhưng bản dịch có cả "Bộ Tác chiến" → lệch nội bộ đoạn và lệch với `provisional_review_choices`.
2. Lệch nhãn với b07 p000177 (đã ghi nhận ở trên); nên xử lý ở đợt nhất quán thuật ngữ, vẫn trong diện đề xuất tạm.
3. Các lỗi nhẹ m2–m7 của báo cáo gốc ngoài phạm vi ký duyệt này (không thuộc p21/p23/p34 trừ m2 ở p34); m2 ("lời qua tiếng lại" ở p34) vẫn nguyên trong bản hiện tại — nhẹ, không chặn.

## 4. next_action

1. Người giữ quyền sửa đổi một cụm ở p34 (câu cuối): "Bộ Tác chiến" → "Cục Tác chiến".
2. Coordinator chạy lại validator/diff cho p34, rồi cho reviewer xác nhận nhanh (hoặc ghi nhận ký duyệt có điều kiện) trước khi commit.
3. Ghi vào sổ pending: cặp Cục Hậu cần/Cục Tác chiến là đề xuất tạm không canon; b07 p000177 cần đối chiếu sau.
