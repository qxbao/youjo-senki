# Báo cáo tự kiểm (Semantic Self-Check) — `vol-08-ch-05-b02`

## 1. Thông tin chung
- **Task ID**: `vol-08-ch-05-b02`
- **Tác tử dịch**: `argon-low`
- **Phạm vi**: `YS-LN08/Text/chapter018.xhtml/p000028` – `YS-LN08/Text/chapter018.xhtml/p000054` (27 đoạn)
- **Tệp đích**: `translations/vol-08/ch-05-b02.jsonl`

## 2. Kiểm tra đối chiếu quy chuẩn & thuật ngữ
- **Ngôi kể và điểm nhìn (`DEC-P01-001`)**:
  - Trần thuật ngôi thứ ba bám theo điểm nhìn của Trung tướng von Zettour xuyên suốt các đoạn `p000028`–`p000054`: Zettour và Cramm được quy chiếu bằng đại từ `ông`.
  - Lời lẩm bẩm thành tiếng của Zettour (`p000028`, `p000033`, `p000035`, `p000045`, `p000047`, `p000054`): dùng đại từ `chúng ta` khi nói về phía Đế quốc/quân đội Đế quốc, giữ giọng suy tư trầm tĩnh của một tướng lĩnh tham mưu.
- **Bảo toàn nghĩa, phủ định, câu hỏi và giả định (`style-guide.md`)**:
  - Giữ đúng câu hỏi tu từ ở `p000029`, `p000031`, `p000054`.
  - Giữ đúng thời gian và tính chất giả định trái thực tế ở `p000031`, `p000038`, `p000042`, và giả định hướng tới khả năng ở `p000049`, `p000053`, `p000054`.
  - Giữ đúng quan hệ nhân quả và đối lập giữa góc nhìn hậu phương/bản quốc với thực tế chiến trường ở `p000040`–`p000041` và `p000049`–`p000051`.
- **Bảo toàn nhấn mạnh (`DEC-P01-002`)**:
  - Toàn bộ 27 đoạn từ `p000028` đến `p000054` không có thẻ nhấn mạnh trong nguồn và bản dịch không tự thêm dấu `*...*`.
- **Thuật ngữ và tên riêng (`pending_terms` & `glossary`)**:
  - Áp dụng nhất quán các phương án đã có trong sổ pending: `Zettour`, `tư lệnh sư đoàn` (`p000028`), `mặt trận phía đông` (`p000029`, `p000036`, `p000041`), `Lục quân Đế quốc` (`p000030`, `p000031`, `p000037`, `p000040`, `p000049`), `các sĩ quan tham mưu Cụm B` (`p000031`), `sư đoàn thiết giáp` (`p000032`), `miền đông` (`p000034`), `tuyến đầu tiên` (`p000036`, `p000051`), `sĩ quan chiến trường` / `Degurechaff` / `Cramm` (`p000037`), `tiền tuyến` (`p000037`, `p000039`), `hạ sĩ quan` (`p000038`), `Đế quốc` (`p000039`, `p000043`, `p000049`), `bản quốc` (`p000041`), `Heimat` (`p000043`), `Chiến dịch Andromeda` (`p000049`), `hậu phương` (`p000050`), `cuộc tiến công` (`p000051`), `Hội đồng Tự trị` (`p000054`).
  - Các cách diễn đạt tạm cần lưu ý cho sổ pending: `nhân sự cấp sư đoàn` / `nhân sự cấp trung đoàn` (`p000031`), `đội ngũ sĩ quan` (`p000038`), `vùng tài nguyên` / `nền kinh tế thời chiến` (`p000049`), `tầng đất đen` (`p000053`).

## 3. Xử lý phản biện Argon & Sign-off (`vol-08-ch-05-b02-translator-signoff`)
- **Báo cáo phản biện**: `reviews/prose/vol-08/ch-05-b02-argon-review.yml` ghi nhận `0` findings (`serious: 0`, `moderate: 0`, `minor: 0`).
- **Đối chiếu `locked_choices` & `pending_term_recommendations`**: Toàn bộ 27/27 đoạn (`p000028`–`p000054`) đã tuân thủ đầy đủ các lựa chọn khóa và khuyến nghị thuật ngữ của Argon (`tư lệnh sư đoàn`, `sư đoàn thiết giáp`, `mặt trận phía đông`, `tuyến đầu tiên`, `tiền tuyến`, `hậu phương`, `Lục quân Đế quốc`, `nhân sự cấp sư đoàn`, `nhân sự cấp trung đoàn`, `các sĩ quan tham mưu Cụm B`, `những sĩ quan chiến trường`, `hàng ngũ hạ sĩ quan`, `nguồn hạ sĩ quan`, `đội ngũ sĩ quan`, `bản quốc`, `Heimat`, `vùng biên viễn`, `Chiến dịch Andromeda`, `nền kinh tế thời chiến`, `vùng tài nguyên`, `Hội đồng Tự trị`).
- **Cập nhật trạng thái**: Đã chuyển trường `status` của toàn bộ 27 dòng trong `translations/vol-08/ch-05-b02.jsonl` từ `"draft"` sang `"reviewed"`.

## 4. Tự kiểm tra kỹ thuật
- Đủ 27/27 dòng JSONL, khớp thứ tự `segment_id` từ `p000028` đến `p000054`.
- Trường `status` của mọi dòng đều là `"reviewed"`, `translator` là `"argon-low"`, khớp `source_sha256` và `glossary_version` trong handoff.
- Không chép câu nguồn tiếng Anh vào báo cáo tự kiểm.
