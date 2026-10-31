# Báo cáo tự kiểm (Self-Check) — `vol-05-ch-02-b07`

## 1. Thông tin chung
- **Task ID**: `vol-05-ch-02-b07`
- **Tác tử**: `argon-low` (Gemini 4 Argon Low)
- **Phạm vi**: `YS-LN05/Text/part0016.html/p000001` .. `YS-LN05/Text/part0016.html/p000029` (29 đoạn)
- **Tệp đích**: `translations/vol-05/ch-02-b07.jsonl`
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`
- **Source SHA256**: `494fbc70fbd1e8324426441839ccf91319082ac0150ba1089dc77b6c3d605004`

## 2. Kiểm tra đối chiếu nghĩa và dòng chảy tự sự
- **Bối cảnh & Điểm nhìn (POV)**:
  - Đoạn `p000001`–`p000008`: Tiếp nối trực tiếp cuộc trao đổi trong văn phòng của Trung tướng Hans von Zettour ở cuối batch `ch-02-b06` dưới góc nhìn ngôi thứ nhất của Trung tá Pháp sư Tanya von Degurechaff. Zettour thừa nhận sai lầm chiến lược và bác bỏ lời xin từ chức của Tanya; Tanya tự vấn về việc định kiến đối với những người Cộng sản đã làm lệch hướng quan sát khách quan của bản thân.
  - Đoạn `p000009`–`p000029`: Chuyển cảnh sang góc nhìn trần thuật ngôi thứ ba bám theo Trung tướng Hans von Zettour sau khi tiễn Trung tá von Degurechaff rời phòng. Zettour triệu tập khẩn cấp Trung tá von Lergen từ Cục Tác chiến, thông báo đổi lịch trình thị sát sang mặt trận phía đông và giao nhiệm vụ tìm một chuyên gia về các vấn đề sắc tộc (có liên hệ thực địa và giữ được bí mật) ngay trước đầu tuần sau (sáng thứ Hai).
- **Bảo toàn nghĩa**: Đã rà soát toàn bộ 29 đoạn; không bỏ sót mệnh đề, không thêm thắt ý ngoài văn bản, giữ nguyên nhịp điệu đối thoại quân sự và sắc thái hài hước khô khan ở cuối phân cảnh (`p000027`–`p000029`).

## 3. Kiểm tra đại từ và quy chuẩn xưng hô (`DEC-P01-001`)
- **Độc thoại nội tâm của Tanya** (`p000004`–`p000008`): Tự xưng `mình` / `chúng ta`, gọi Zettour là `ông ấy` / `Zettour`.
- **Đối thoại Tanya – Zettour** (`p000001`–`p000003`):
  - Tanya với Zettour: `tôi` – `ngài`.
  - Zettour với Tanya: `tôi` / `chúng ta` – `cô`.
- **Trần thuật ngôi thứ ba theo góc nhìn Zettour & độc thoại nội tâm của Zettour** (`p000009`–`p000029`):
  - Trong câu chuyển cảnh `p000009` nhìn từ phía Zettour, Tanya được gọi là `Trung tá von Degurechaff` và đại từ ngôi thứ ba là `cô` (đúng quy ước khi không ở trong điểm nhìn tự thuật của Tanya).
  - Zettour trong trần thuật: `Tướng von Zettour` / `Zettour` / `ông`; trong câu độc thoại nội tâm trực tiếp (`p000020`): tự xưng `mình`, gọi Rudersdorf là `Rudersdorf` / `kẻ vô trách nhiệm như vậy`, gọi Lergen là `anh ta` / `người sĩ quan cấp trung này` / `Lergen`.
  - Lergen trong trần thuật: `Trung tá von Lergen` / `Lergen` / `anh ta`.
- **Đối thoại Zettour – Lergen** (`p000011`–`p000029`):
  - Zettour với Lergen: `tôi` / `chúng ta` – `Trung tá von Lergen` / `Trung tá` / `anh`.
  - Lergen với Zettour: `tôi` / `chúng tôi` / `chúng ta` – `ngài` / `thưa Tướng quân`.

## 4. Kiểm tra định dạng nhấn mạnh (`DEC-P01-002`)
- Chỉ sử dụng dấu `*...*` tại đúng 3 đoạn có thẻ nhấn mạnh trong XHTML nguồn:
  - `YS-LN05/Text/part0016.html/p000020`: Toàn bộ đoạn độc thoại nội tâm của Zettour được bọc trong `*...*`.
  - `YS-LN05/Text/part0016.html/p000027`: Cụm suy nghĩ trực tiếp mở đầu câu (`*Anh ta nhạy bén thật*`).
  - `YS-LN05/Text/part0016.html/p000029`: Cụm tiếng lòng không thốt nên lời của Lergen (`*Nhưng hôm nay là thứ Sáu mà*`).
- Toàn bộ 26 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và hoàn toàn không dùng `*...*`.

## 5. Thuật ngữ & Đề xuất (Pending Terms)
- Đã áp dụng nhất quán các thuật ngữ trong `pending-terms-index.yml`:
  - `những người Cộng sản` (`p000004`)
  - `Trung tá von Degurechaff` (`p000009`)
  - `Tướng von Zettour` (`p000009`, `p000027`)
  - `Trung tá von Lergen` / `Trung tá` (`p000011`, `p000016`, `p000025`, `p000027`)
  - `mặt trận phía nam` (`p000012`), `lục địa phía nam` (`p000013`)
  - `Tướng von Romel` (`p000012`)
  - `Cục Tác chiến` (`p000013`, `p000015`, `p000018`, `p000022`)
  - `Tướng von Rudersdorf` (`p000018`)
  - `vùng hậu phương` (`p000021`)
  - `các hoạt động bình định` (`p000025`)
- Các cụm mới mang tính mô tả/tổ chức trong phạm vi batch:
  - `Đại hội Dân tộc` (`p000022`): Dùng cho tổ chức chính trị của các sắc tộc hợp tác với Cục Tác chiến (thống nhất mạch từ vựng với `các hội đồng dân tộc` ở `ch-02-b06`).
  - `chuyên gia về các vấn đề sắc tộc` (`p000021`) / `các vấn đề sắc tộc` (`p000024`).

## 6. Kết quả chạy Validator & Sign-off (`vol-05-ch-02-b07-translator-signoff`)
- **Xử lý Argon Review (`reviews/prose/vol-05/ch-02-b07-argon-review.yml`)**:
  - Tiếp thu finding `minor` tại `YS-LN05/Text/part0016.html/p000005`: chỉnh `"bóp nghẹt nghiêm trọng"` thành `"bóp méo nghiêm trọng"` để chuẩn xác hơn về trường nghĩa hình ảnh làm sai lệch nhận thức khách quan.
  - Bảo toàn đầy đủ toàn bộ `locked_choices` và `pending_term_recommendations` trên cả 29 đoạn.
  - Đã cập nhật trường `status` của toàn bộ 29/29 dòng trong `translations/vol-05/ch-02-b07.jsonl` từ `draft` sang `reviewed`.
- **Lệnh kiểm tra**: `python3 tools/validate_translation.py --handoff handoffs/vol-05/ch-02-b07.yml --source work/vol-05/batches/ch-02-b07-source.jsonl --translation translations/vol-05/ch-02-b07.jsonl`
- **Trạng thái**: **PASS** (29/29 dòng hợp lệ, khớp `segment_id`, `source_sha256`, `glossary_version`, `status: reviewed`).
