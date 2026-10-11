# Đề xuất thuật ngữ — pilot-01 (bản dịch mù, claude-sonnet)

Phạm vi: `YS-LN01/Text/chapter001.xhtml/p000008` đến `p000015` (8 đơn vị).
Tất cả mục dưới đây chỉ là **đề xuất**, chưa được chốt; không ghi vào `canon/`.
Canon hiện trống (`glossary.yml`, `characters.yml`, `decisions.md`), nên các lựa chọn dưới đây là phương án tạm để bản dịch đọc liền mạch.

| Mã đề xuất | Loại | Phương án tạm | Phương án khác | Đoạn | Lý do / nghi vấn |
| --- | --- | --- | --- | --- | --- |
| TERM-P01 | xưng hô (đại từ trần thuật) | “nó” | “thực thể ấy”, lược chủ ngữ, “hắn/cô” (cần biết giới tính được dùng sau này) | p000008–p000012, p000014 | Nguồn dùng đại từ vô giới tính cho chủ thể chưa định danh. “Nó” giữ khoảng cách lạnh và phù hợp việc chưa rõ thân phận; có thể đổi khi các đoạn sau xác lập danh tính. |
| TERM-P02 | thuật ngữ | “thân xác” | “cái vỏ”, “cơ thể” | p000009 | Từ nguồn mang sắc thái vật chứa, khách thể hóa. “Thân xác” giữ được sự xa cách mà vẫn tự nhiên; cần xem cách dùng ở các chương sau. |
| TERM-P03 | thuật ngữ | “bảo mẫu” | “vú nuôi”, “người trông trẻ” | p000011 | Nữ tu “có vẻ là” bảo mẫu — mức độ suy đoán được giữ bằng “có vẻ là”. “Vú nuôi” mang sắc thái cổ hơn. |
| TERM-P04 | tên riêng / địa danh | giữ “Yamanote”, “tuyến Yamanote” | “tuyến vòng Yamanote” | p000011 | Chưa có quy tắc phiên âm địa danh Nhật; giữ nguyên dạng La-tinh, thêm “tuyến” cho rõ loại. |
| TERM-P05 | thuật ngữ | “đèn khí” | “đèn ga”, “đèn hơi đốt” | p000012 | Chưa có quy ước; “đèn khí” ngắn gọn và quen thuộc trong văn dịch lịch sử. |
| TERM-P06 | xưng hô / tên nhân vật | “Tanya”; người lớn xưng “con” hoặc gọi “con yêu” | “bé Tanya”, “con gái”, “cục cưng” | p000013, p000015 | Người nói là nữ tu nói với trẻ sơ sinh; “con yêu” giữ độ thân mật. Chưa rõ quan hệ xưng hô giữa nữ tu và Tanya (có thể nên dùng “sơ”/“con”). Dạng phiên Việt của tên (Tanya / Tania / Tanja…) cần quyết định. |
| TERM-P07 | tên riêng | giữ “Mennonite”, “Amish” | “người Mennonite”, “người Amish” | p000014 | Tên các nhóm tôn giáo; giữ nguyên dạng La-tinh. Chưa quyết định có thêm “người” hay không. |

## Vấn đề trình bày (chưa có quyết định)

- Dấu thoại: tạm dùng “ ” cho thoại và ‘ ’ cho phần trích lồng trong thoại (p000013). Cần ghi vào `decisions.md` trước khi áp dụng thống nhất.
- Nội tâm (p000009, p000014): không dùng dấu ngoặc hay nghiêng; chuyển ngôi “mình” trong câu hỏi nội tâm. Nguồn là đoạn trần thuật thường, không có dấu hiệu định dạng riêng trong văn bản tách; cần đối chiếu `xhtml` cục bộ nếu muốn giữ chữ nghiêng.
- p000010 nằm trong dải 008–015 nhưng không được liệt kê trong `coverage` của `handoffs/pilot-01.yml`; đã dịch đủ theo phạm vi giao.
- Dấu chấm lửng ở p000012 và p000014 giữ nguyên vị trí và hình thức “…”.
- `handoffs/pilot-01.yml` ghi `translation_editor: null`; theo `AGENTS.md`, người giữ quyền sửa cần được ghi trước khi sửa `translations/`. Theo chỉ dẫn nhiệm vụ, tôi không sửa tệp bàn giao; cần người điều phối xác nhận.

## Siêu dữ liệu

- `glossary_version` dùng trong JSONL: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41` (theo bàn giao).
- `source_sha256`: lấy theo từng đơn vị trong gói nguồn cục bộ.
