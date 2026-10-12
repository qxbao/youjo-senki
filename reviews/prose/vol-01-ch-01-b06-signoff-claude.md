# Sign-off review ch-01-b06 (Claude)

Task: vol-01-ch-01-b06-signoff-review. Phạm vi: M3 và các note đã cập nhật. Không chép câu nguồn; mọi thuật ngữ vẫn là đề xuất, chưa phải canon.

## Xác nhận M3

- p000089: bản dịch dùng “quyền cai trị” cho dominion; không còn “chủ quyền” trong đoạn. Đã kiểm tra trực tiếp trong `translations/vol-01/ch-01-b06.jsonl`. **Đạt.**
- p000091: giữ “chủ quyền” cho sovereignty. **Đạt.**
- Ledger `work/run-state/pending-terms.yml`: `b06-dominion` đề xuất “quyền cai trị” (phương án khác có “quyền cai quản”); `b06-sovereignty` là “chủ quyền”; ghi chú giữ tách biệt. Khớp với văn bản và note. **Đạt.**
- Hai thuật ngữ vẫn pending; không có promotion canon.

## Kiểm tra note đã cập nhật

Diff chưa commit chỉ chạm note/văn bản của p000078, p000088, p000089, p000091, p000099.

| segment_id | Kết quả |
|---|---|
| p000078 | Note mô tả đúng ý bản dịch (thông tin nhận được không khớp thực tế, không hàm ý hoàn toàn không được báo). Đạt. |
| p000088 | Note đúng: hai ý phê phán tách biệt; tham chiếu `b06-sue-cunningham-address` là đề xuất tạm, ghi rõ chưa canon. Đạt. |
| p000089 | Note khớp văn bản và ledger (`b06-dominion`, `b06-sovereignty`, `b06-demilitarized-zone`). Văn bản dùng nhất quán tên khu vực; lặp từ “bảo đảm” đã được giảm (còn một lần). Đạt. |
| p000091 | Note khớp văn bản và ledger `b06-sovereignty`; giữ tách biệt với dominion. Đạt. |
| p000099 | Note khớp bản dịch (nhiễu/rối liên lạc và chưa được phân đúng tần số thành hai ý). Đạt. |

p000100 không nằm trong diff chưa commit; văn bản hiện dùng “lão luyện” nên không còn lặp “kỳ cựu”. Note giữ nguyên, vẫn đúng.

## Phát hiện

- Nghiêm trọng: 0
- Vừa: 0
- Nhẹ: 0
- Unresolved: không có.

## Khuyến nghị thuật ngữ (đề xuất, không canon)

- dominion → quyền cai trị (p000089); phương án khác: quyền cai quản. Độ tin cậy trong ledger 0,55.
- sovereignty → chủ quyền (p000091).

## Ghi chú giới hạn

Validator và diff_check chưa chạy (not_run). Không commit.
