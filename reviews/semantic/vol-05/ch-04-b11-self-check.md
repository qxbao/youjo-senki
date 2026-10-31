# Báo cáo tự kiểm (Self-Check): `vol-05-ch-04-b11` (Translator Sign-off)

## 1. Thông tin chung
- **Task ID**: `vol-05-ch-04-b11-translator-signoff` (Parent: `vol-05-ch-04-b11`)
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN05/Text/part0022.html/p000384` .. `YS-LN05/Text/part0022.html/p000426` (43 đoạn)
- **Tệp đích**: `translations/vol-05/ch-04-b11.jsonl`
- **Trạng thái dòng**: Đã cập nhật toàn bộ 43/43 dòng từ `draft` sang `reviewed`
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`
- **Source SHA256**: `494fbc70fbd1e8324426441839ccf91319082ac0150ba1089dc77b6c3d605004`

## 2. Xử lý các Findings từ Argon Review (`reviews/prose/vol-05/ch-04-b11-argon-review.yml`)
1. **`YS-LN05/Text/part0022.html/p000391` (minor)**:
   - **Vấn đề**: Tiêu đề chuyển cảnh dịch là `ĐƠN VỊ TÀU NGẦM CỦA LỤC QUÂN ĐẾ QUỐC`, dễ gây mâu thuẫn quân chủng với các đoạn `p000403`, `p000408` và `p000419` xác định tàu `U-152` thuộc Hải quân Đế quốc.
   - **Giải quyết**: Đã tiếp nhận đề xuất của Reviewer, đổi thành `ĐƠN VỊ TÀU NGẦM CỦA QUÂN ĐỘI ĐẾ QUỐC ĐƯỢC PHÁI TỚI BIỂN BẮC` để vừa sát nghĩa toàn quân vừa thống nhất ngữ cảnh.
2. **`YS-LN05/Text/part0022.html/p000407` & `p000415` (minor)**:
   - **Vấn đề**: Cụm `chiếc bục gỗ` làm giảm sắc thái vật dụng kê chân tạm bợ khiến Tanya tự ái ở `p000415`.
   - **Giải quyết**: Đã đổi `chiếc bục gỗ` thành `chiếc hộp gỗ` ở cả `p000407` và `p000415`.
3. **`YS-LN05/Text/part0022.html/p000414` (minor)**:
   - **Vấn đề**: Đại từ `nó` được dùng ở hai câu liên tiếp cho hai chủ thể khác nhau (câu thứ hai chỉ chiếc kính tiềm vọng, câu thứ ba chỉ Tanya).
   - **Giải quyết**: Đã đổi `nó` ở câu thứ hai thành `thiết bị này` (`Chỉ là những gì thiết bị này có thể làm được có một giới hạn căn bản mà thôi.`), giữ nguyên đại từ `nó` cho Tanya ở câu thứ ba theo `DEC-P01-001`.

## 3. Kiểm tra quy chuẩn xưng hô, ngôi kể và `locked_choices`
- Tuân thủ đầy đủ toàn bộ `locked_choices` và `pending_term_recommendations` trong `ch-04-b11-argon-review.yml`:
  - **Đoạn kết cảnh căn cứ hải quân Liên bang (`p000384` – `p000390`)**: Đại tá Mikel tự xưng `Tôi` với `viên chính ủy` (`p000384`), tự sự ngôi thứ ba gọi Mikel là `ông` (`p000386`); trước tiểu đoàn gọi `Các đồng chí` và xưng `chúng ta` (`p000389`); tiếng đáp đồng thanh giữ nguyên ba lớp ngoặc kép `“““Rõ!”””` (`p000390`).
  - **Cảnh bên trong tàu ngầm soái hạm `U-152` (`p000391` – `p000426`)**:
    - **Trung tá Tanya von Degurechaff**: Tự sự ngôi thứ ba dùng đại từ `nó` theo `DEC-P01-001`; độc thoại nội tâm dùng `mình`; khi hướng lời mỉa mai thầm tới thủy thủ đoàn tàu `U-152` gọi `các anh` (`p000407`).
    - **Thuyền trưởng von Schraft (`Thuyền trưởng von Schraft` / `Thuyền trưởng`)**: Trong đối thoại công vụ với Tanya, hai bên xưng `tôi`, gọi nhau là `Trung tá von Degurechaff` / `thưa Trung tá` – `Thuyền trưởng von Schraft` / `thưa Thuyền trưởng`, kết hợp đại từ `anh` – `cô`. Tự sự và độc thoại của Tanya gọi von Schraft là `anh ta`. Ở `p000422`, phân biệt rõ `chúng ta` (hai bên trên tàu hiện tại) và `Lính tàu ngầm chúng tôi` / `chúng tôi` (giới lính tàu ngầm).

## 4. Kiểm tra thuật ngữ và định dạng nhấn mạnh (`DEC-P01-002`)
- **Thuật ngữ đã áp dụng nhất quán**: `Moskva`, `viên chính ủy`, `Liên bang`, `Đảng`, `Đồng chí Tổng Bí thư Josef`, `Đại tá Mikel`, `Biển Bắc`, `soái hạm U-152` / `tàu U-152` / `chiếc U-152`, `Trung tá von Degurechaff` / `Trung tá Tanya von Degurechaff` / `Trung tá`, `Thuyền trưởng von Schraft` / `Thuyền trưởng`, `Bộ Tư lệnh Tối cao`, `Bộ Tổng tham mưu`, `nàng công chúa của biển cả`, `Hải quân Đế quốc`, `không hạm đội`, `cơ quan tình báo liên hợp của Bộ Tư lệnh Lục quân và Hải quân`, `Trân Châu Cảng⁵`, `Scapa Flow⁶`.
- **Bảo toàn nhấn mạnh (`DEC-P01-002`)**:
  - Chỉ sử dụng dấu `*...*` ở đúng 4 đoạn có thẻ `<html:em>` trong `xhtml` nguồn (`p000399`, `p000405`, `p000407`, `p000418`). Toàn bộ 39 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không chứa dấu `*`.
