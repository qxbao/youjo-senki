# Báo cáo tự kiểm (Semantic Self-Check) — `vol-08-ch-04-b09`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-04-b09` (Sign-off: `vol-08-ch-04-b09-translator-signoff`)
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter014.xhtml/p000293` – `YS-LN08/Text/chapter014.xhtml/p000326` (34 đoạn)
- **Tệp đích**: `translations/vol-08/ch-04-b09.jsonl`

## 2. Kiểm tra đối chiếu quy chuẩn & thuật ngữ
- **Ngôi kể và điểm nhìn (`DEC-P01-001`)**:
  - Nửa đầu lô (`p000293`–`p000304`, tại Soldim 528): Phân biệt rõ ràng giữa trần thuật ngôi thứ ba bám sát điểm nhìn của Tanya (`Tanya`, `cô`) ở các đoạn `p000293`, `p000296`, `p000299`, `p000300`, `p000303`, `p000304` và độc thoại nội tâm / nhận xét trực tiếp của Tanya (`mình`, `bạn`) ở các đoạn `p000299`–`p000301`.
  - Nửa sau lô (`p000305`–`p000326`, tại phòng tác chiến Sở chỉ huy Cụm B): Trần thuật ngôi thứ ba qua góc nhìn của Trung tướng von Zettour (`Trung tướng von Zettour`, `Zettour`, `ông`) và các sĩ quan tham mưu Cụm B (`họ`, `anh ta`), kèm câu suy nghĩ trực tiếp của Zettour ở `p000326` (`tôi`).
- **Xưng hô trong hội thoại**:
  - Giữa Tanya và hai Trung úy Tospan, Wüstemann (`p000293`, `p000295`, `p000297`–`p000298`, `p000302`): Tanya tự xưng `tôi`, gọi hai cấp dưới là `hai anh`, `Trung úy Tospan`, `Trung úy Wüstemann`, `anh`; hai trung úy đồng thanh đáp `Rõ, thưa Trung tá!`.
  - Giữa Trung tướng von Zettour và các sĩ quan tham mưu Cụm B (`p000310`, `p000312`–`p000313`, `p000316`, `p000318`, `p000320`–`p000322`, `p000324`–`p000325`): Zettour tự xưng `tôi`, gọi tập thể là `các quý ông` (`Thưa các quý ông`), `các vị`, và gọi cá nhân sĩ quan phát biểu ở `p000316` là `anh`; các sĩ quan tham mưu gọi Zettour là `Tướng quân` (`Thưa Tướng quân`), `ngài`, tự xưng `tôi` / `chúng ta`.
- **Bảo toàn nhấn mạnh (`DEC-P01-002`)**:
  - Đoạn `p000319`: bảo toàn cụm nhấn mạnh bằng `*Thật không thể tin nổi*`.
  - Đoạn `p000326`: bảo toàn câu nội tâm nhấn mạnh bằng `*Chuyện đó tôi biết thừa rồi*`.
  - Tất cả 32 đoạn còn lại không có nhấn mạnh trong nguồn và không dùng dấu `*...*`.
- **Thuật ngữ và tên riêng (`pending_terms` & `glossary`)**:
  - Tuân thủ nhất quán các phương án đã có trong tập 8 và các tập trước: `Kampfgruppe`, `Trung úy Tospan` / `Tospan`, `Trung úy Wüstemann` / `Wüstemann`, `nguồn nhân lực`, `Đế quốc`, `NGÀY 18 THÁNG 6 NĂM THỐNG NHẤT 1927, SỞ CHỈ HUY CỤM B ĐẠO QUÂN PHÍA ĐÔNG, PHÒNG TÁC CHIẾN`, `phòng tác chiến`, `Sở chỉ huy Cụm B`, `sĩ quan tham mưu`, `thanh tra viên`, `Trung tướng von Zettour` / `Zettour`, `Kampfgruppe Lergen`, `cứ điểm kiên cố`, `Soldim 528`, `Liên bang`, `lực lượng dự bị chiến lược`, `Trung tướng von Rudersdorf`, `Cục Tác chiến`, `thiết giáp`, `bộ binh cơ giới`, `bộ binh thông thường`, `Lục quân Đế quốc`, `mặt trận phía đông`.
  - Đề xuất thuật ngữ mới trong lô: `cơ sở hạ tầng nhân lực` (`p000303`), `trạm dừng đường sắt đô thị` (`p000314`).

## 3. Tự kiểm tra kỹ thuật & Sign-off
- Đủ 34/34 dòng JSONL, khớp thứ tự `segment_id` từ `p000293` đến `p000326`.
- Đã rà soát đối chiếu báo cáo `reviews/prose/vol-08/ch-04-b09-argon-review.yml`: 0 findings (`serious: 0`, `moderate: 0`, `minor: 0`), toàn bộ 8 mục `pending_term_recommendations` và 34 mục `locked_choices` từ `p000293` đến `p000326` đều đã được tuân thủ chính xác.
- Đã cập nhật trường `status` của toàn bộ 34 dòng từ `"draft"` sang `"reviewed"`, giữ nguyên `translator` là `"argon-low"`, khớp `source_sha256` và `glossary_version` trong handoff.
- Không chép văn bản nguồn tiếng Anh vào bản dịch hoặc báo cáo tự kiểm.
