# Semantic self-check — vol-02-ch-05-b12 review fixes

- Đã đối chiếu gói nguồn cục bộ với handoff: SHA-256 khớp `cb717af0caf5d3b156dbdd48c71741359a4cdf815be6138462682897ed579509`.
- Đã rà đủ 29 mã đoạn của batch; giữ nguyên thứ tự, mã đoạn và siêu dữ liệu. Sửa các câu thuộc F01–F08 theo căn cứ và khuyến nghị được hỗ trợ trong báo cáo prose.
- F01 (`p000296`, serious): khôi phục biến động nhân sự đã xảy ra gồm truy thăng sau khi chết hoặc điều chuyển/đưa về hậu phương; bỏ cách diễn đạt thành các sĩ quan đang lo chuyện đó.
- F02 (`p000286`, `p000288`, `p000289`, `p000294`, moderate): dùng “mình” cho tự quy chiếu nội tâm; ở trần thuật dùng Tanya hoặc lược chủ ngữ khi tự nhiên. Không áp dụng quy ước này cho lời thoại.
- F03 (`p000292`, moderate): đổi Tech Research thành “bộ phận nghiên cứu kỹ thuật”, không suy ra cấp tổ chức.
- F04 (`p000290`, minor): dùng hình ảnh nguyên liệu cho cối xay thịt; giữ đúng phạm vi chữ nghiêng của lời hô.
- F05 (`p000294`, minor): khôi phục kết luận nhân quả dạng khẳng định, bỏ câu hỏi tu từ.
- F06 (`p000293`, minor): giữ dấu hiệu ví von cho hình ảnh nghĩa địa.
- F07 (`p000310`, minor): tách chi phí chế tạo cực thấp khỏi kết luận thích hợp sản xuất hàng loạt.
- F08 (`p000312`, minor): diễn đạt hạ sát lén lút, không thêm ý che giấu dấu vết sau hành động; giữ chữ nghiêng cho tiếng động.
- Không từ chối khuyến nghị nào. Các lựa chọn tạm dưới đây đều non-canon.

## Pending terms

- `Tech Research` → “bộ phận nghiên cứu kỹ thuật” (`p000292`); chưa xác định cấp tổ chức.
- `Central` → giữ nguyên `Central` (`p000292`); chưa xác định loại địa danh/nhãn cơ quan.
- `Elinium Type 95` → giữ nguyên `Elinium Type 95` (`p000292`); chưa xác định bản chất tên mẫu.
- Tanya: “mình” trong nội tâm; ở trần thuật dùng “nó”, lặp Tanya hoặc lược chủ ngữ tùy câu (`p000286`, `p000288`, `p000289`, `p000294`). Đây là đề xuất LN02, không tự mở rộng canon.
- `Magic Major` / `major` → “Thiếu tá Pháp sư” / “Thiếu tá” (`p000291`, `p000296`, `p000297`); cấu trúc danh xưng và cấp bậc vẫn pending.
- `Lieutenant Weiss` → “Trung úy Weiss” (`p000289`); ánh xạ tạm, chưa canon.
- `instructor unit` → “đơn vị huấn luyện” (`p000292`); không xác định cấp hoặc biên chế.
- `magic scanning` → “dò quét ma thuật” (`p000312`); giữ là lựa chọn tạm.

## Risk flags

- `meaning`: đã sửa sai lệch nhân sự nghiêm trọng ở `p000296` và các sai lệch nghĩa F04–F08.
- `new_pending_terms`: các mục thuật ngữ và giọng LN02 nêu trên vẫn cần coordinator ghi nhận/xử lý theo quy trình; không mục nào được nâng thành canon.
- `emphasis`: giữ chữ nghiêng ở `p000290` và `p000312` theo nguồn.
- Validator và `git diff --check` được chạy sau khi cập nhật bản dịch.
