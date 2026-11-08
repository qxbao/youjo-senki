# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-02-b24`

- **Task ID**: `vol-10-ch-02-b24`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter010.xhtml/p000471` đến `YS-LN10/Text/chapter010.xhtml/p000498` (28 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc
- Đã dịch đầy đủ 28/28 đoạn theo đúng thứ tự nguồn từ `p000471` đến `p000498`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn.
- Trường `status` của toàn bộ 28 dòng là `reviewed` (sau khi hoàn tất sign-off theo `ch-02-b24-argon-review.yml`).
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter010.xhtml/p000476`: 1 cụm từ in nghiêng ở câu cuối (`*thân thiện với eco*`).
- Tất cả 27 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.

## 2. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Phần 1 (`p000471` – `p000478`): Góc nhìn của Tanya và đối thoại với Trung úy Serebryakov**:
  - Độc thoại nội tâm của Tanya tự xưng `mình` (`p000478`), khi nói chung cả hai người trên không trung dùng `chúng mình` (`p000471`), hoàn toàn nối tiếp mạch văn từ `ch-02-b23`.
  - Câu trần thuật khách quan mô tả biểu cảm của Tanya (`p000473`) giữ đúng danh xưng `Tanya` và gọi Visha là `sĩ quan phụ tá của mình`.
  - Trong lời thoại trực tiếp: Tanya gọi cấp dưới là `Trung úy Serebryakov`, xưng `chúng ta` (`p000472`, `p000474`) và gọi `cô` (`p000474`); Serebryakov gọi Tanya là `ngài` kèm tiểu từ kính ngữ `ạ` (`p000475`, `p000477`).
  - Giữ lối chơi chữ xoay quanh tiền tố `eco` trong chuỗi thoại và độc thoại `p000476`–`p000478` (giữa ý nghĩa sinh thái/môi trường và ý nghĩa kinh tế/tiết kiệm mà Serebryakov hỏi lại).
- **Phần 2 (`p000479` – `p000498`): Tiêu đề chuyển cảnh và trần thuật ngôi thứ ba từ góc nhìn phía Quân đội Liên bang**:
  - `YS-LN10/Text/chapter010.xhtml/p000479`: Dịch tiêu đề chuyển cảnh viết hoa toàn bộ (`CÙNG NGÀY HÔM ĐÓ, DOANH TRẠI QUÂN ĐỘI LIÊN BANG TRÊN MẶT TRẬN PHÍA ĐÔNG`).
  - Trần thuật khách quan về các tướng lĩnh và chuyên viên phân tích của Quân đội Liên bang dùng đại từ `họ`.
  - Khi đề cập đến `Trung tướng Zettour` / `Tướng Zettour` (`p000488` – `p000498`), dùng nhất quán đại từ `ông` xuyên suốt toàn bộ các đoạn phân tích tình báo quân sự, giữ đúng giọng văn nghiêm túc, thực dụng và sắc lạnh.

## 3. Kiểm tra các cấu trúc ngữ pháp dễ lệch nghĩa
- **Lối nói mỉa mai, chơi chữ và nhượng bộ trong nội tâm Tanya (`p000471` – `p000478`)**:
  - `YS-LN10/Text/chapter010.xhtml/p000471` & `p000472`: Giữ đúng suy luận nhân quả của Tanya từ việc pháp sư địch vẫn cố nhắm bắn bất chấp vị trí bay ngay phía trên đội hình Quân đội Liên bang.
  - `YS-LN10/Text/chapter010.xhtml/p000474` & `p000475`: Bảo toàn ẩn dụ mỉa mai (`chia sẻ màn pháo hoa này với những người bạn của chúng ta ở dưới mặt đất`) và phản ứng nhận diện ý đồ dụ địch bắn nhầm quân mình của Serebryakov.
  - `YS-LN10/Text/chapter010.xhtml/p000478`: Giữ đúng cấu trúc kết hợp hai khía cạnh (`vừa thuộc về sinh thái lại vừa có tính kinh tế. Thế nên nó thân thiện với eco gấp đôi`) và sự chấp nhận thực tế nghề nghiệp ở cuối đoạn.
- **Lập luận nhân quả, so sánh tăng tiến và cấu trúc đối lập trong phân tích tình báo Liên bang (`p000480` – `p000498`)**:
  - `YS-LN10/Text/chapter010.xhtml/p000481`: Bảo toàn sự đối lập giữa thực tế khắc nghiệt và chính trị hủy hoại con người, cùng cấu trúc so sánh tỷ lệ thuận (`Càng bị thao túng nhiều vào giai đoạn đầu của một cuộc xung đột, các sĩ quan chỉ huy cấp cao lại càng dễ hình thành một cái nhìn thực tế về thế giới`).
  - `YS-LN10/Text/chapter010.xhtml/p000485` & `p000486`: Giữ đúng phạm vi thu thập tình báo (bao hàm cả cách Đế quốc tự nhìn nhận chính mình và hồ sơ cá nhân của các tướng lĩnh) cũng như nguyên nhân khả thi nhờ sự hậu thuẫn của `Bộ Dân ủy Nội vụ`, khiến phe phản đối trong nội bộ quân đội phải nuốt sự miễn cưỡng để tuân phục nhân danh sự tất yếu.
  - `YS-LN10/Text/chapter010.xhtml/p000491` & `p000492`: Bảo toàn chính xác đặc trưng tác chiến của Zettour (ưa chuộng mánh khóe và trò nghi binh trong tác chiến cơ động, sẵn sàng đánh cược tất cả để bao vây địch bằng sức cơ động chiến lược vượt trội, ưu tiên tiêu diệt hoàn toàn đạo quân dã chiến của đối phương hơn là chiếm giữ lãnh thổ mà không vượt quá giới hạn lý thuyết của hậu cần).
  - `YS-LN10/Text/chapter010.xhtml/p000493`: Kiểm tra kỹ cấu trúc `không chỉ... mà cả...` (`Sự tàn nhẫn của ông ngang ngửa với cảnh sát mật của Đảng Cộng sản không chỉ trong mắt những người nghiên cứu kỹ lưỡng về ông mà cả trong mắt những người thân cận với ông nữa`).
  - `YS-LN10/Text/chapter010.xhtml/p000494` – `p000498`: Giữ đúng chiến thuật đặc trưng của Zettour (chủ đích rút quân tạo các mũi lồi để dụ địch vào thế bị đánh tạt sườn và cắt đứt tuyến tiếp vận) và kế hoạch tương kế tựu kế của Quân đội Liên bang (bố trí phần lớn lực lượng dự bị ngay tại phần gốc mũi lồi của họ, huy động cả tân binh cho trận phục kích quy mô lớn nhằm dùng chính mánh khóe của đối phương để quật lại).

## 4. Thuật ngữ đã áp dụng và đề xuất (`pending_terms`)
- Thuật ngữ chuẩn và kế thừa nhất quán từ `work/run-state/pending-terms-index.yml`:
  - `Federation Army`: `Quân đội Liên bang` (`p000472`, `p000479`, `p000483`, `p000490`, `p000496`, `p000497`)
  - `adjutant`: `sĩ quan phụ tá` (`p000473`)
  - `First Lieutenant Serebryakov`: `Trung úy Serebryakov` (`p000474`)
  - `friendly fire`: `bắn nhầm vào quân mình` (`p000475`)
  - `Commies`: `lũ Cộng sản` (`p000478`)
  - `eastern front`: `mặt trận phía đông` (`p000479`)
  - `Imperial Army`: `Lục quân Đế quốc` (`p000485`)
  - `the Empire`: `Đế quốc` (`p000485`, `p000498`)
  - `Commissariat for Internal Affairs`: `Bộ Dân ủy Nội vụ` (`p000486`)
  - `Lieutenant General Zettour` / `General Zettour`: `Trung tướng Zettour` / `Tướng Zettour` (`p000488`, `p000490`, `p000497`)
  - `maneuver warfare`: `tác chiến cơ động` (`p000491`)
  - `field army`: `đạo quân dã chiến` (`p000492`)
  - `logistics`: `hậu cần` (`p000492`)
  - `Communist Party’s secret police`: `cảnh sát mật của Đảng Cộng sản` (`p000493`)
  - `salient(s)`: `mũi lồi` (`p000494`, `p000497`)
  - `flanking attacks`: `các đòn tấn công tạt sườn` (`p000494`)
  - `supply lines`: `tuyến tiếp vận` (`p000494`)
  - `war academy`: `học viện quân sự` (`p000495`)
  - `reserves`: `lực lượng dự bị` (`p000497`)
  - `trickster`: `bậc thầy mánh khóe` (`p000498`)
