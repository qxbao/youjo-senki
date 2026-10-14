# Tự kiểm nghĩa — vol-02-ch-07-b01

Phạm vi: 25 đoạn `p000001–p000025` trong gói B01 được giao.

## Findings đã xử lý

- **B01-R01 — p000003:** Giữ token thoại `Break!` nguyên văn trong ngoặc kép và với dấu chấm than. Chức năng câu lệnh chưa được xác định; giữ nguyên là lựa chọn tạm thời, pending và không phải canon.
- **B01-R02 — p000004:** Giữ `04` rồi `Fox Three` hai lần, phân cách trung tính; không gán người nhận, biến thành lời gọi hay khai triển chức năng tín hiệu/định danh. Lựa chọn vẫn pending.
- **B01-R03 — p000023:** Giữ đúng trình tự chấn động, bất tỉnh, rơi xuống rồi hậu quả có thể xảy ra ở nơi họ nằm. Không khẳng định cú rơi là nguyên nhân.
- **B01-R04 — p000011:** Dùng “ở Rhine”, không thêm phân loại sông hay mặt trận.
- **B01-R05 — p000016:** Dùng “đạn nổ mạnh”; không thêm cỡ đạn, ngòi nổ hay cơ chế.
- **B01-R06 — p000019:** Nêu rõ giới hạn là một phát đạn thông thường trúng trực tiếp, tối đa 12,7 mm; giữ riêng đối chiếu với tấn công bão hòa ở p000020.

## Rà soát nghĩa và trình bày

- Giữ đủ 25 mã đoạn theo thứ tự. Rà lại phủ định, chủ thể, quan hệ điều kiện, trình tự sự kiện và các mức độ bất định; giữ các số liệu cùng đơn vị như trong bản dịch.
- Đại từ trần thuật và tự quy chiếu về Tanya theo `DEC-P01-001`.
- Chỉ giữ nhấn mạnh ở phần tương ứng trong p000008–p000009 theo `DEC-P01-002`; không mở rộng nhấn mạnh sang phần còn lại. Không có p000764 trong phạm vi B01.
- Các hàng còn lại không có finding bổ sung từ lần rà soát B01 này.

## Đề xuất thuật ngữ pending, không phải canon

Tất cả 11 lựa chọn dưới đây là phương án tạm theo đề xuất reviewer; chúng vẫn pending/non-canon.

1. **Magic Major / field major** — đề xuất: “Thiếu tá Pháp sư / thiếu tá tác chiến” (p000001–p000002). Lý do: giữ cấp thiếu tá và phân biệt chức năng pháp sư/tác chiến mà không suy ra bảng quân hàm. Phương án khác: “Thiếu tá ma pháp / thiếu tá ngoài chiến trường”.
2. **203rd Aerial Mage Battalion** — đề xuất: “Tiểu đoàn Pháp sư Trên không số 203” (p000007). Lý do: giữ cấp đơn vị, số hiệu và hoạt động trên không, không tự gán quân chủng. Phương án khác: “Tiểu đoàn Pháp sư Không chiến số 203”.
3. **Being X** — đề xuất: giữ “Being X” (p000008). Lý do: chưa khẳng định bản thể hoặc đồng nhất với danh xưng khác. Phương án khác: “Thực thể X”.
4. **God** — đề xuất: “Thượng đế”; cách quy chiếu tạm “ngài” (p000009). Lý do: giữ lựa chọn đang có trong ledger, không xem đại từ là bằng chứng Tanya tôn kính. Phương án khác: lặp danh xưng hoặc “Chúa”.
5. **Rhine** — đề xuất: giữ “Rhine” như địa danh chưa phân loại (p000011, p000013). Lý do: package không xác nhận sông hay mặt trận. Phương án khác: “Sông Rhine” hoặc “mặt trận Rhine” khi có căn cứ.
6. **protective film / defensive shell** — đề xuất: “màn chắn bảo hộ / lớp vỏ phòng thủ” (p000017–p000024). Lý do: phân biệt màn chắn cách cơ thể khoảng một mét với lớp vỏ áp sát; không suy diễn cơ chế. Phương án khác: “màng bảo hộ / lớp vỏ phòng ngự”.
7. **Elinium Type 95 / orb** — đề xuất: “Elinium Type 95 / quả cầu” (p000024). Lý do: giữ tên thiết bị và danh từ trung tính; 88 mm thuộc màn chắn, 120 mm là năng lực lý thuyết của lớp vỏ. Phương án khác: “Elinium loại 95 / cầu thể”.
8. **Break!** — đề xuất: giữ nguyên `Break!` (p000003). Lý do: package chưa phân biệt được chức năng khẩu lệnh; giữ nguyên ít suy diễn nhất. Phương án khác: “Tách ra!”, “Ngoặt gấp!”, “Né gấp!”, “Ngắt!” hoặc “Phá vây!”. Độ bất định cao.
9. **Fox Three / Fairy 01 / CP** — đề xuất: giữ nguyên các định danh/chữ viết tắt (p000004, p000014). Lý do: chưa đủ căn cứ khai triển; cấu trúc p000004 không xác định người nhận. Phương án khác: chỉ khai triển khi có bằng chứng về chức năng.
10. **high explosives** — đề xuất: “đạn nổ mạnh” (p000016). Lý do: phù hợp ngữ cảnh hỏa lực bắn vào máy bay mà không suy ra loại vũ khí cụ thể. Phương án khác: “đạn có sức nổ mạnh”.
11. **saturation attack** — đề xuất: “tấn công bão hòa” (p000020). Lý do: giữ đối lập giữa giới hạn một phát riêng lẻ và hỏa lực dồn dập. Phương án khác: “tấn công bằng hỏa lực dồn dập”.

## Rủi ro còn lại

- Chức năng chuyên biệt của `Break!` và `Fox Three` vẫn chưa được xác định từ package B01; các lựa chọn trên vẫn pending/non-canon.
- Các đề xuất thuật ngữ không phải quyết định canon và cần được coordinator ghi nhận theo quy trình.
