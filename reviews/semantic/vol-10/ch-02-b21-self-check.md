# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-02-b21`

- **Task ID**: `vol-10-ch-02-b21`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter010.xhtml/p000363` đến `YS-LN10/Text/chapter010.xhtml/p000403` (41 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc
- Đã dịch đầy đủ 41/41 đoạn theo đúng thứ tự nguồn từ `p000363` đến `p000403`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn.
- Trường `status` của toàn bộ 41 dòng đã được cập nhật từ `draft` sang `reviewed` sau khi xử lý Argon review.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter010.xhtml/p000374`: 1 cụm độc thoại nội tâm in nghiêng ở đầu đoạn (`*À, chết tiệt thật. Mình sẽ không gục ngã mà không đánh trả đâu.*`).
  - `YS-LN10/Text/chapter010.xhtml/p000380`: 1 cụm in nghiêng ở cuối câu thứ hai (`*sôi máu vì giận*`).
- Tất cả các đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.

## 2. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Nửa đầu lô (`p000363` – `p000379`) — Góc nhìn ngôi thứ ba của Trung tá Drake**:
  - Trần thuật gọi `Trung tá Drake`, `Drake`, đại từ `anh` (nhất quán với `ch-02-b19` và `ch-02-b20`).
  - Độc thoại nội tâm của Drake tại `p000374` tự xưng `mình`.
  - Lời thoại của pháp sư Đế quốc (Tanya) nói bằng tiếng Khối Thịnh vượng chung với kẻ địch vừa bị hạ (`p000369`, `p000371`): xưng `ta`, gọi đối phương là `đồ khốn`, `tên người Anh` — giữ đúng giọng điệu lạnh lùng, áp đảo trên chiến trường.
  - Tiếng hét tuyệt vọng cuối cùng của Drake trước khi ngất đi (`p000370`, `p000379`): giữ nguyên nhịp ngắt quãng và sắc thái chửi thề khi dồn toàn lực phản kích.
- **Nửa sau lô (`p000380` – `p000403`) — Góc nhìn ngôi thứ nhất của Tanya**:
  - Độc thoại nội tâm và lời tự lẩm bẩm một mình trên không trung (`p000390`, `p000401`): tự xưng `mình` (hoặc `chúng ta` khi bao hàm phe Đế quốc / con người nói chung tại `p000389`, `p000394`), tự quy chiếu tên `Tanya` ở `p000380` theo đúng bản gốc.
  - Gọi viên sĩ quan địch vừa giao chiến là `tên sĩ quan đó` / `hắn` (`p000386`), gọi chung lực lượng địch là `bọn chúng` / `chúng` / `đám người này` / `các người` (khi hướng lời trách móc giả định tới đối phương ở `p000389`).
  - Giọng văn duy lý, thực dụng, pha lẫn sự phẫn nộ và mỉa mai đặc trưng của Tanya khi đánh giá hành vi cảm tử phi lý của đối phương dưới góc nhìn chiến tranh hiện đại.

## 3. Kiểm tra các cấu trúc ngữ pháp dễ lệch nghĩa
- **Giả định, thời gian và tính chất chưa xảy ra (`p000366`, `p000367`, `p000386`, `p000394`)**:
  - `YS-LN10/Text/chapter010.xhtml/p000366`: Bảo toàn sắc thái giả định quá khứ về lưỡi kiếm vốn dĩ sẽ đâm xuyên vai (`lưỡi kiếm lẽ ra đã xuyên thủng vai anh`).
  - `YS-LN10/Text/chapter010.xhtml/p000367`: Bảo toàn mốc thời gian sát nút trước khi thuật thức kích hoạt (`khiến nỗ lực liều mạng cuối cùng thất bại chỉ vài mili giây trước khi kịp phát nổ`).
  - `YS-LN10/Text/chapter010.xhtml/p000386`: Bảo toàn chuỗi hai hành động liên tiếp của viên sĩ quan địch và hệ quả tất yếu (`đã định dùng một ảo ảnh quang học ở cự ly cực gần—một hành vi vốn dĩ đã có thể coi là tự sát—rồi lại quyết định bồi thêm một thuật thức phát nổ toàn lực, cầm chắc việc chính hắn cũng sẽ bị cuốn vào vụ nổ`).
  - `YS-LN10/Text/chapter010.xhtml/p000394`: Bảo toàn cấu trúc loại trừ / bổ sung bình diện (`Đó là còn chưa kể tới đại đa số những tên chỉ biết bay tán loạn về những hướng ngẫu nhiên`).
- **Phủ định và tương phản mức độ (`p000387`, `p000389`, `p000401`, `p000402`, `p000403`)**:
  - `YS-LN10/Text/chapter010.xhtml/p000387`: Phân biệt rõ việc xem binh lính như vũ khí (phương tiện) với việc tự nguyện biến bản thân thành vũ khí cảm tử.
  - `YS-LN10/Text/chapter010.xhtml/p000389`: Giữ rõ sự nhượng bộ về bản chất bẩn thỉu của chiến tranh và yêu cầu tối thiểu về việc giữ gìn nhân tính.
  - `YS-LN10/Text/chapter010.xhtml/p000401`: Giữ đúng phủ định bản chất và so sánh khoảng cách trình độ/độ gan lì (`đám này chẳng phải binh lính của Khối Thịnh vượng chung. Chúng còn lâu mới gan góc và lì đòn được như những người mà mình từng giao chiến trong Trận Không chiến Phương Tây`).
  - `YS-LN10/Text/chapter010.xhtml/p000402`: Bảo toàn phủ định toàn phần ở cả hai chiến trường đối chiếu (`mặt trận Rhine` và `bầu trời chính quốc Khối Thịnh vượng chung`).
  - `YS-LN10/Text/chapter010.xhtml/p000403`: Bảo toàn hai vế phỏng đoán nối tiếp cùng sắc thái nghi vấn của Tanya.

## 4. Thuật ngữ đã áp dụng và đề xuất (`pending_terms`)
- Các thuật ngữ kế thừa nhất quán từ `canon/` và `work/run-state/pending-terms-index.yml`:
  - `thuật thức bắn tỉa quang học` (`p000363`)
  - `Khối Thịnh vượng chung` (`p000368`, `p000401`, `p000402`)
  - `Trung tá Drake` / `Drake` (`p000363`, `p000364`, `p000366`, `p000368`, `p000372`, `p000373`, `p000377`)
  - `khẩu tiểu liên` (`p000373`)
  - `thuật thức phát nổ` (`p000374`, `p000386`, `p000392`)
  - `Lục quân Đế quốc` (`p000383`)
  - `mồi nhử quang học` / `mồi nhử` (`p000394`)
  - `ưu thế trên không` (`p000397`)
  - `lớp vỏ phòng thủ` / `màn chắn bảo hộ` (`p000397`)
  - `Đội quân đa quốc gia` (`p000399`)
  - `mặt trận Rhine` (`p000402`)
  - `pháp sư trên không` (`p000402`)
  - `cận chiến quần vòng` (`p000402`)
- Thuật ngữ đề xuất ghi nhận mới (`pending_terms`):
  - `Trận Không chiến Phương Tây` (`YS-LN10/Text/chapter010.xhtml/p000401`): dịch tương ứng theo cấu trúc của `Trận chiến Phương Tây` và `Trận Không chiến Đài Loan` đã có trong sổ pending.
  - `chính quốc Khối Thịnh vượng chung` (`YS-LN10/Text/chapter010.xhtml/p000402`): kết hợp nhất quán `Khối Thịnh vượng chung` và `chính quốc` đã dùng ở `vol-10`.

## 5. Xử lý Argon Review Sign-off (`vol-10-ch-02-b21-translator-signoff`)
- `YS-LN10/Text/chapter010.xhtml/p000392` (`minor` — `pronouns_viewpoint`): Đã chỉnh cụm `"ngay sau phòng tuyến của mình"` thành `"ngay sau phòng tuyến của chúng"` để khử lưỡng nghĩa với đại từ tự xưng `"Mình"` (Tanya) ở câu trước.
- `YS-LN10/Text/chapter010.xhtml/p000403` (`minor` — `terminology_nuance`): Đã chỉnh `"lương tri"` thành `"lẽ thường"` để phản ánh chính xác bình diện năng lực phán đoán tỉnh táo thông thường mà Tanya đang phê phán.
- Đã kiểm tra và tuân thủ đầy đủ toàn bộ `pending_term_recommendations` và `locked_choices` trong `reviews/prose/vol-10/ch-02-b21-argon-review.yml`.
- Đã cập nhật `status` của toàn bộ 41 dòng trong `translations/vol-10/ch-02-b21.jsonl` từ `draft` sang `reviewed`.
