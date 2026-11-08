# Báo cáo tự kiểm (Translator Self-Check) — `vol-10-ch-02-b23`

- **Task ID**: `vol-10-ch-02-b23`
- **Translator**: `argon-low`
- **Phạm vi**: `YS-LN10/Text/chapter010.xhtml/p000443` đến `YS-LN10/Text/chapter010.xhtml/p000470` (28 đoạn)
- **Glossary version**: `sha256:d5f19d64d8d734e1a21400978b70a7c10daf776ba7f77eb58f01a39ac78f5a41`

## 1. Kiểm tra độ đầy đủ và bảo toàn cấu trúc
- Đã dịch đầy đủ 28/28 đoạn theo đúng thứ tự nguồn từ `p000443` đến `p000470`.
- Giữ nguyên toàn bộ `segment_id` và `source_sha256` khớp chính xác với tệp nguồn.
- Trường `status` của toàn bộ 28 dòng là `reviewed`.
- Không tách hoặc gộp đoạn.
- Bảo toàn chính xác định dạng in nghiêng (`*...*`) theo đúng thẻ nhấn mạnh trong `xhtml` gốc (`DEC-P01-002`):
  - `YS-LN10/Text/chapter010.xhtml/p000461`: 1 từ tượng thanh in nghiêng ở câu đầu (`*vù*`).
  - `YS-LN10/Text/chapter010.xhtml/p000470`: 1 cụm giới từ chỉ vị trí in nghiêng ở câu cuối (`*ở phía sau*`).
- Tất cả 26 đoạn còn lại không có thẻ nhấn mạnh trong `xhtml` đều không sử dụng dấu `*...*`.

## 2. Xưng hô, giọng điệu và tính nhất quán nội bộ (`DEC-P01-001`)
- **Góc nhìn ngôi thứ nhất của Tanya xuyên suốt toàn bộ lô (`p000443` – `p000470`)**:
  - Độc thoại nội tâm tự xưng `mình`; khi nói đến cả hai người (Tanya và Visha) đang cùng rút lui và cơ động trên không thì dùng `chúng mình` (`p000453`, `p000454`, `p000456`, `p000463`, `p000466`, `p000469`) hoặc `bọn này` trong câu lẩm bẩm phẫn nộ (`p000458`), hoàn toàn thống nhất với `ch-02-b22`.
  - Tự quy chiếu ngôi thứ ba bằng tên `Tanya` tại các đoạn nhìn nhận khách quan về năng lực bẩm sinh và kinh nghiệm chiến trường (`p000445`, `p000447`), giữ đúng đặc trưng phong cách tâm lý nhân vật.
  - Gọi Visha trong nội tâm là `Trung úy Serebryakov` (`p000447`, `p000459`) và `sĩ quan phụ tá` (`p000469`).
  - Gọi pháp sư địch đang truy kích điên cuồng từ xa (Mary Sue) bằng các định danh miệt thị nhất quán với `ch-02-b22`: `đồ quái vật khốn kiếp` (`p000443`), `con lợn rừng kia` / `con lợn rừng này` (`p000444`, `p000450`, `p000465`), `con ngốc này` (`p000445`), `con quái vật này` (`p000446`, `p000464`), `tên pháp sư địch` / `tên pháp sư này` / `tên pháp sư tình nguyện này` (`p000453`, `p000466`, `p000467`, `p000469`, `p000470`), kết hợp đại từ `ả` (`p000453`, `p000465`, `p000466`, `p000468`) và gọi thẳng `ngươi` khi lẩm bẩm chất vấn từ xa (`p000462`).
  - Giữ nguyên danh xưng `Being X` (`p000446`, `p000464`, `p000465`) theo đúng quy chuẩn canon.

## 3. Kiểm tra các cấu trúc ngữ pháp dễ lệch nghĩa
- **Phủ định nhấn mạnh và đối lập nguyên nhân (`p000444`, `p000445`, `p000446`)**:
  - `YS-LN10/Text/chapter010.xhtml/p000444`: Bảo toàn cấu trúc phủ định nguyên nhân kỹ thuật/công nghệ ở câu đầu và khẳng định nguyên nhân duy nhất là sức mạnh thuần túy ở câu sau (`chẳng phải một kỹ thuật đặc biệt hay công nghệ tiên tiến nào đã làm nên điều này. Đơn giản chỉ là sức mạnh thuần túy của con lợn rừng kia mà thôi`).
  - `YS-LN10/Text/chapter010.xhtml/p000445`: Giữ đúng sự đối lập gay gắt giữa việc Tanya phải chắt chiu từng chút ma lực trong `Type 95` với việc đối phương phung phí ma lực không cần suy nghĩ, cùng câu hỏi tu từ cảm thán ở cuối đoạn.
  - `YS-LN10/Text/chapter010.xhtml/p000446`: Bảo toàn cấu trúc tăng tiến (`vốn đã bất chấp mọi quy luật logic... thế mà lại còn thực sự đem thứ sức mạnh ấy trút vào một thuật thức cải biến cả thế giới theo đúng nghĩa đen`) và phép liên tưởng tới `Being X`.
- **Mệnh đề nhượng bộ, điều kiện và giả định (`p000448`, `p000450`, `p000452`, `p000453`, `p000465`, `p000467`, `p000470`)**:
  - `YS-LN10/Text/chapter010.xhtml/p000448`: Bảo toàn ẩn dụ về học phí đắt đỏ của kinh nghiệm và mệnh đề điều kiện thời gian (`một khi bạn đã trả đủ cái giá phải trả, kinh nghiệm sẽ trở thành đồng minh vĩnh viễn của bạn`).
  - `YS-LN10/Text/chapter010.xhtml/p000450`: Giữ đúng chuỗi lập luận chiến thuật phân tích điểm yếu của thuật thức tấn công tầm xa (hữu dụng trong việc chống tiếp cận khu vực nhưng kém hiệu quả khi tấn công trực diện ở cự ly xa, dễ bị né tránh ngay cả khi là đòn tập kích bất ngờ không phát lộ bức xạ).
  - `YS-LN10/Text/chapter010.xhtml/p000452`: Bảo toàn mệnh đề điều kiện phủ định (`có bao nhiêu ma lực trên đời đi nữa mà không bắn trúng đích thì cũng vô giá trị thôi`).
  - `YS-LN10/Text/chapter010.xhtml/p000453`: Giữ đúng câu giả định quá khứ bỏ lửng ở đầu đoạn (`lẽ ra cũng đã có thể tung thêm một đòn tấn công nữa rồi, nếu không phải vì cái điểm nhỏ nhặt đó…`) và dự đoán mối đe dọa tiếp diễn cho tới khi thoát hẳn khỏi tầm bắn.
  - `YS-LN10/Text/chapter010.xhtml/p000465` & `p000466`: Bảo toàn phép suy luận đảo chiều của Tanya (từ việc ví đối phương với `Being X` suy ra đối phương cũng đần độn và thiếu kiềm chế, không đánh giá thấp năng lực nhưng cũng không đánh giá quá cao trí thông minh).
  - `YS-LN10/Text/chapter010.xhtml/p000467` & `p000468`: Giữ đúng mức độ hoài nghi của Tanya về khả năng có kế hoạch phối hợp và tận dụng việc đối phương nổi giận quên mất tỷ lệ phát nổ sai lệch cao của thuật thức phát nổ.
  - `YS-LN10/Text/chapter010.xhtml/p000469` & `p000470`: Bảo toàn chuỗi hành động tính toán tọa độ, hạ độ cao để đưa đồng minh mặt đất của địch vào đường bắn, và nguyên tắc an toàn hỏa lực cơ bản ở câu kết (`luôn ghi nhớ trong đầu thứ gì đang nằm *ở phía sau* mục tiêu mà mình nhắm bắn`).

## 4. Thuật ngữ đã áp dụng và đề xuất (`pending_terms`)
- Thuật ngữ chuẩn theo `canon/glossary.yml` và `canon/characters.yml`:
  - `Type 95`: `Type 95` (`p000445`)
  - `Being X`: `Being X` (`p000446`, `p000464`, `p000465`)
  - `First Lieutenant Serebryakov`: `Trung úy Serebryakov` (`p000447`, `p000459`)
  - `adjutant`: `sĩ quan phụ tá` (`p000469`)
- Thuật ngữ kế thừa từ `work/run-state/pending-terms-index.yml` và các lô trước:
  - `ace aerial mage`: `pháp sư trên không át chủ bài` (`p000447`)
  - `Rhine campaign`: `chiến dịch Rhine` (`p000447`)
  - `long-range attack formula`: `thuật thức tấn công tầm xa` (`p000450`)
  - `area denial`: `chống tiếp cận khu vực` (`p000450`)
  - `frontal assaults`: `các đòn tấn công trực diện` (`p000450`)
  - `sneak attack`: `đòn tập kích bất ngờ` (`p000450`)
  - `exfiltration path`: `đường rút lui` (`p000454`)
  - `pre-radiation`: `bức xạ tiền phát` (`p000456`)
  - `explosion formula(s)`: `thuật thức phát nổ` (`p000457`, `p000468`)
  - `predesignated fire`: `bắn vào tọa độ định sẵn` (`p000458`)
  - `evasive maneuvers`: `các pha cơ động né tránh` (`p000459`)
  - `maneuver warfare`: `tác chiến cơ động` (`p000462`)
  - `volunteer mage`: `pháp sư tình nguyện` (`p000467`)
  - `line of fire`: `đường bắn` (`p000469`)
