# Review vol-02-ch-05-b02 — p000025–p000048

Phạm vi: đúng 24 đoạn `YS-LN02/Text/part0026.xhtml/p000025` đến `YS-LN02/Text/part0026.xhtml/p000048`. Đã đọc shared/reviewer, config, handoff, năm canon references, riêng mục `chapter5_b02_translation_proposals`, package và bản dịch được giao. Không đọc batch, nguồn, bản dịch hay review khác. Báo cáo không trích câu nguồn; phần căn cứ diễn giải nội dung package tại mã đoạn tương ứng. Các câu tiếng Việt dưới đây là đề xuất sửa, chưa được áp dụng.

Package SHA-256 khớp handoff: `0a326d0ddade5bed1a23ded2fb4e650439d3778f085a906b88548d625a6bcd70`. Năm hash canon references đều khớp; ID, thứ tự và source hash của cả 24 dòng nguồn/bản dịch khớp phạm vi. Đây là đối chiếu đầu vào, không phải chạy validator hay diff-check của pipeline.

Kết luận: cần sửa trước khi đóng review. Không thấy mất cả đoạn hoặc lỗi nghiêm trọng. Có sáu finding mức vừa về nghĩa/logic và chín finding mức nhẹ về chi tiết, giọng và diễn đạt. Chuỗi cứu thương → yểm trợ → địch chuyển mục tiêu → pháo kích mạnh hơn → hoài nghi tiếp viện nhìn chung được giữ. Các phạm vi nhấn mạnh ở p000032, p000035, p000040 và hai âm thanh ở p000042 tương ứng với markup nguồn, phù hợp DEC-P01-002. Không đủ căn cứ nhận người kể là Tanya; không áp dụng quy ước đại từ của Tanya cho người kể này.

## Findings

### B02-F01 — vừa — YS-LN02/Text/part0026.xhtml/p000025

- **Vấn đề:** “lấy ... ra mà thề” đổi hình ảnh đặt cược để khẳng định sự chắc chắn thành một lời yêu cầu thề.
- **Căn cứ:** Người nói dùng vật đặt cược để nhấn mạnh rằng lời hứa chắc chắn là lời hứa suông; không yêu cầu người nghe tuyên thệ. Giọng là khẩu ngữ của lính.
- **Đề xuất:** “Tôi đã bảo rồi còn gì? Cậu có thể đem cả con gà tây Lễ Phục Sinh ra cá: đó chỉ là lời hứa suông.” Giữ hình ảnh gà tây và dịp lễ; không tự sửa chi tiết văn hóa của nguồn.

### B02-F02 — nhẹ — YS-LN02/Text/part0026.xhtml/p000025

- **Vấn đề:** Mất dấu bao lời thoại, trong khi các đoạn thoại khác trong batch đều có.
- **Căn cứ:** Package đánh dấu cả đoạn là lời nói trực tiếp; bản dịch hiện có thể bị đọc như trần thuật ngôi thứ nhất.
- **Đề xuất:** Thêm cặp dấu “...” quanh đoạn, theo cách bản dịch đang dùng ở các đoạn thoại còn lại. Đây là khôi phục tín hiệu thoại của đoạn, không đề nghị một quyết định định dạng EPUB mới.

### B02-F03 — vừa — YS-LN02/Text/part0026.xhtml/p000026

- **Vấn đề:** “ngay từ đầu tôi đã không nghĩ” chuyển thời điểm và phạm vi nhận định.
- **Căn cứ:** Người kể hiện nhìn lại và cho rằng tập thể vốn đã không kỳ vọng nhiều ngay từ đầu; bản dịch đặt việc suy nghĩ của cá nhân vào thời điểm ban đầu. Cần giữ mức dè dặt của nhận định hồi tưởng.
- **Đề xuất:** “Vì vậy, tôi nghĩ ngay từ đầu chúng tôi cũng chẳng kỳ vọng gì nhiều.” Phương án gần cấu trúc phủ định hơn: “Vì vậy, tôi không nghĩ ngay từ đầu chúng tôi đã kỳ vọng gì nhiều.” Chọn phương án đầu cho độ tự nhiên, giữ “tôi nghĩ” để không biến suy xét thành xác quyết.

### B02-F04 — vừa — YS-LN02/Text/part0026.xhtml/p000026

- **Vấn đề:** “vừa bị thúc ép huấn luyện xong” làm lệch đặc điểm của tân binh.
- **Căn cứ:** Nguồn nêu việc huấn luyện bị tiến hành gấp/rút ngắn cho tân binh; không xác lập rằng họ bị ép phải huấn luyện. Điều này giải thích sự khác biệt trải nghiệm giữa lính mới và lính cũ.
- **Đề xuất:** “Dù những tân binh được huấn luyện gấp rút cảm thấy thế nào...” Hoặc “đám tân binh trải qua khóa huấn luyện cấp tốc”; ưu tiên phương án đầu vì không thêm cấu trúc khóa học chưa được nêu.

### B02-F05 — vừa — YS-LN02/Text/part0026.xhtml/p000031

- **Vấn đề:** “át cả tiếng ầm vang” gán độ lớn lấn át chiến trường cho tiếng người ngã và đồng đội hoảng hốt.
- **Căn cứ:** Điều bất thường là người kể vẫn nghe được những âm thanh ấy giữa tiếng gầm của chiến trường; không có khẳng định chúng lớn hơn. Chuỗi suy luận về tay bắn tỉa sau đó vẫn được giữ, không cần tự sửa logic của người kể.
- **Đề xuất:** “... cùng tiếng đồng đội họ hoảng hốt, ngay giữa tiếng ầm vang của chiến trường.” Hoặc “... dù chiến trường vẫn gầm vang.”

### B02-F06 — nhẹ — YS-LN02/Text/part0026.xhtml/p000032

- **Vấn đề:** “bắn quấy rối” giữ mục đích nhưng mất sắc thái bắn rải và “mọi chỗ có vẻ hắn có thể” nặng cấu trúc.
- **Căn cứ:** Hành động phản ứng là cúi thấp rồi rải đạn vào các nơi nghi có tay bắn tỉa, không phải một loạt bắn nhắm chắc vào vị trí xác định.
- **Đề xuất:** “Chúng tôi vội cúi thấp hơn, bắn rải để quấy rối mọi chỗ nghi hắn đang ẩn nấp.” Giữ nguyên phạm vi chữ nghiêng của câu cuối. Không thêm pháo binh hoặc đổi thành tiêu diệt mục tiêu.

### B02-F07 — nhẹ — YS-LN02/Text/part0026.xhtml/p000035

- **Vấn đề:** “yểm trợ cẩn mật” nghiêng sang kín đáo/bí mật, không diễn đạt việc đồng đội tích cực duy trì che chở.
- **Căn cứ:** Bốn người khiêng cáng lao ra dưới sự yểm trợ tận lực; p000040 cho thấy nhiều thành phần cùng dựng màn hỏa lực và khói.
- **Đề xuất:** “... lao ra dưới sự yểm trợ tận lực của đồng đội, cố đưa người đồng đội bị thương về phía sau.” “Người anh em” hiện có vẫn có thể giữ như sắc thái tình đồng đội, không coi là quan hệ huyết thống.

### B02-F08 — nhẹ — YS-LN02/Text/part0026.xhtml/p000035

- **Vấn đề:** “chúng tôi được bảo đảm vẫn còn chút nhân tính” dễ thành nhận định về phần nhân tính còn lại trong chính người kể và đồng đội; văn cũng mang giọng hành chính.
- **Căn cứ:** Quân y đem lại chút đối xử có tình người trong thế giới chiến tranh địa ngục. Đoạn không bàn về việc tập thể mất hay giữ phẩm chất đạo đức của mình.
- **Đề xuất:** “Có những người quân y được gọi là *Sanis* ở bên, chúng tôi ít ra vẫn được hưởng chút tình người trong thế giới địa ngục ấy.” Phương án trung tính hơn: “... sự hiện diện của họ bảo đảm vẫn còn chút tình người trong thế giới địa ngục ấy.” Chọn phương án đầu để giữ người thụ hưởng và giọng hồi tưởng.

### B02-F09 — nhẹ — YS-LN02/Text/part0026.xhtml/p000037

- **Vấn đề:** “kính trọng, sâu sắc nhất” thêm so sánh cực cấp và kết hợp từ gượng.
- **Căn cứ:** Nguồn nhấn mạnh lòng kính trọng chân thành, sâu sắc cùng tính duy nhất của đối tượng; không nêu một thang so sánh mức kính trọng.
- **Đề xuất:** “Họ là những người duy nhất tôi thật lòng và vô cùng kính trọng.” Giữ hai lần lặp “những người duy nhất” trong đoạn để giữ nhịp khẳng định.

### B02-F10 — nhẹ — YS-LN02/Text/part0026.xhtml/p000038

- **Vấn đề:** “Bắn màn khói!” dùng kết hợp từ khó hiểu: màn khói là kết quả cần tạo.
- **Căn cứ:** Mệnh lệnh yêu cầu dựng màn che; cách thực hiện bằng đạn cối khói được nói rõ ở p000040.
- **Đề xuất:** “Tạo màn khói!” Đây là phương án ít suy diễn nhất. “Bắn đạn khói!” cũng hợp diễn biến nhưng đưa phương tiện ở đoạn sau vào chính câu lệnh; không ưu tiên.

### B02-F11 — vừa — YS-LN02/Text/part0026.xhtml/p000040

- **Vấn đề:** “Nếu phải bảo vệ ai trước tiên” biến yêu cầu tuyệt đối bảo vệ quân y dù không cứu được ai khác thành thứ tự ưu tiên có điều kiện. “Có thể cứu” cũng thiên về năng lực hơn sự sẵn lòng cứu trong mạch ca ngợi này.
- **Căn cứ:** Người kể xác định quân y nhất thiết phải được bảo vệ, kể cả khi không bảo vệ được người khác; lý do là họ là những người duy nhất sẽ cứu tập thể.
- **Đề xuất:** “Dù không bảo vệ được ai khác, vẫn phải bảo vệ *Sanis*; chỉ có họ mới cứu chúng tôi.” Hoặc “Dù không bảo vệ ai khác, chúng tôi nhất định phải bảo vệ *Sanis*; họ là những người duy nhất sẽ cứu chúng tôi.” Chọn phương án đầu cho tiếng Việt tự nhiên; không biến thành một kế hoạch phân thứ tự cứu người.

### B02-F12 — nhẹ — YS-LN02/Text/part0026.xhtml/p000040

- **Vấn đề:** “khiến ai nấy mừng rỡ như trông thấy ánh sáng” thêm hình ảnh và mở cảm nhận ra toàn bộ mọi người.
- **Căn cứ:** Việc cáng xuất hiện an toàn đem lại cảm giác dễ chịu/nhẹ nhõm cho điểm nhìn tập thể người kể. Nguồn không đưa hình ảnh ánh sáng hay xác nhận phản ứng từng người.
- **Đề xuất:** “Thấy chiếc cáng xuất hiện an toàn, chúng tôi nhẹ cả người.” Giữ sự nhẹ nhõm thay vì thêm biểu tượng cứu rỗi.

### B02-F13 — nhẹ — YS-LN02/Text/part0026.xhtml/p000041

- **Vấn đề:** Câu cuối giữ sự gượng cười nhưng làm phẳng hình ảnh địch hào phóng đãi đạn và giảm sắc thái suy đoán.
- **Căn cứ:** Người kể đùa chua chát về số pháo thủ đối phương hẳn đang cùng bắn vào mình; không biết chính xác số lượng. “Láo xược” ở câu trước đã giữ được một phần giọng nhân hóa chế giễu.
- **Đề xuất:** “... chúng tôi gượng cười, nghĩ không biết bao nhiêu pháo thủ Cộng hòa hẳn đang chiêu đãi mình bằng đạn pháo.” Có thể dùng “đãi chúng tôi đạn pháo” nếu muốn khẩu ngữ hơn. Không thêm số lượng hoặc cấp đơn vị pháo binh.

### B02-F14 — vừa — YS-LN02/Text/part0026.xhtml/p000042

- **Vấn đề:** “sự yên ắng” chuyển trạng thái bình tâm thành chiến trường im tiếng; “chưa từng nghe” tuyệt đối hóa mức độ xa lạ của tiếng nổ.
- **Căn cứ:** Ngay trước đó họ đang chịu hỏa lực tập trung và gượng cười khi nằm trong hào. Sự bình thản kỳ lạ chỉ kéo dài ngắn; tiếng nổ tiếp theo là loại họ không quen, chưa đủ căn cứ nói chưa từng nghe trong đời.
- **Đề xuất:** “Nhưng sự bình thản kỳ lạ ấy chẳng kéo dài được bao lâu. Sau tiếng *vút* của thứ gì đó xé gió là một tiếng nổ *ầm* lớn, trầm nặng mà chúng tôi không quen nghe.” Giữ hai phạm vi nhấn mạnh âm thanh, không nghiêng thêm cả câu.

### B02-F15 — nhẹ — YS-LN02/Text/part0026.xhtml/p000047

- **Vấn đề:** “rốt cuộc” giữ bực bội nhưng làm sạch sắc thái chửi thề của lời lính.
- **Căn cứ:** Đây là câu hỏi trực tiếp, thô ráp về thời điểm viện trợ, nối với nỗi hoài nghi và kiệt sức của tổ súng máy. Bản dịch đã dùng “Chết tiệt” ở p000029.
- **Đề xuất:** “Chết tiệt, vậy đơn vị hỗ trợ kia bao giờ mới tới?” Không đổi câu hỏi thời điểm thành hỏi vị trí; chưa đủ căn cứ đổi loại đơn vị.

## Bốn nhóm thuật ngữ tạm và ghi chú Brass

Tất cả lựa chọn sau giữ trạng thái đề xuất, chỉ dựa trên batch này và canon được giao. Không có thuật ngữ/tên gọi đã chốt trong glossary/characters. Không tra cứu lore hoặc lịch sử quân sự bên ngoài để lấp chỗ thiếu căn cứ.

| Nhóm / mã đoạn | Phương án tạm ưu tiên | Phương án khác | Lý do và giới hạn |
| --- | --- | --- | --- |
| `Sanis` — YS-LN02/Text/part0026.xhtml/p000035; YS-LN02/Text/part0026.xhtml/p000040 | Giữ *Sanis*, lần đầu gắn với “những người quân y” | “nhân viên quân y” khi diễn giải vai trò; không thay hẳn định danh | Package trực tiếp xác định đây là cách gọi quân y, không phải tên cá nhân. Vai trò trong batch rõ; xuất xứ ngôn ngữ, dạng số và cách Việt hóa chưa được xác lập. Giữ đúng chính tả package và chữ nghiêng hai lần; không suy ra bác sĩ, giới tính hay cấp bậc. |
| `harassing fire` — YS-LN02/Text/part0026.xhtml/p000032 | “bắn quấy rối”; trong câu ưu tiên “bắn rải để quấy rối” | “bắn quấy nhiễu”, “hỏa lực quấy rối” | Phản ứng của nhóm lính trước tay bắn tỉa chưa rõ vị trí hỗ trợ nghĩa bắn gây cản trở/quấy rối. Ledger gọi đây là thuật ngữ pháo binh, nhưng riêng đoạn này không xác định loại vũ khí; không áp dụng phần suy diễn ấy. Không tự đổi thành hỏa lực chế áp vốn nhấn mạnh một tác dụng chiến thuật khác. |
| `machine-gun nets` — YS-LN02/Text/part0026.xhtml/p000041 | “lưới hỏa lực súng máy” — độ tin cậy vừa, cần ghi pending | “các cụm súng máy”; “những ổ súng máy” như bản hiện tại | Nguồn có ý mạng/lưới; hỏa lực yểm trợ khiến địch chuyển sang đánh các vị trí súng máy. “Ổ súng máy” hợp hình ảnh mục tiêu vật lý nhưng làm mất ý phối trí nhiều súng. Ưu tiên cách giữ hình ảnh lưới, chẳng hạn “những lưới hỏa lực súng máy láo xược ấy”; không khẳng định chúng bắn chéo hay liên kết theo một mô hình kỹ thuật cụ thể. Không tự sửa thuật ngữ nguồn thành một từ khác vì thấy bất thường. Đây là khuyến nghị pending, không tính riêng thành lỗi nghĩa đã chứng minh. |
| `the brass` — YS-LN02/Text/part0026.xhtml/p000026 | “đám chỉ huy cấp cao” | “giới chỉ huy cấp cao”; “đám sĩ quan cấp trên” hiện có; “cấp trên” | Lính cũ khinh bạc sự đáng tin của lời hứa từ tầng chỉ huy cao. Phương án ưu tiên giữ cả cấp độ và giọng bất tín; “giới chỉ huy cấp cao” trung tính hơn, còn “cấp trên”/“sĩ quan cấp trên” mở rộng sang mọi cấp trên trực tiếp. Không gán quân hàm, cơ quan hay cá nhân cụ thể. |

**Brass note:** Mục proposal ghi “giới chỉ huy cấp cao”, nhưng p000026 thực tế dùng “đám sĩ quan cấp trên”; `notes` của dòng này rỗng. Có chênh lệch giữa phương án ghi nhận và cách áp dụng, không có chú thích nguồn trong package của batch cần dịch hoặc phục hồi. Đề xuất coordinator ghi nhận phương án tạm “đám chỉ huy cấp cao” để translator áp dụng và đồng bộ metadata theo quyền của mình; reviewer không sửa ledger/handoff và không yêu cầu thêm ghi chú làm việc vào bản dịch xuất bản. Chênh lệch này được theo dõi ở term recommendation, không cộng thêm một lỗi nội dung trùng với thảo luận thuật ngữ.

Các thuật ngữ còn lại trong phạm vi đọc — quân y, hầm trú, chiến hào, tổ súng cối, đạn khói, hỏa lực yểm trợ/tập trung, pháo dã chiến, tiểu đoàn trưởng, quân bổ sung và quân tiếp viện — nhìn chung phù hợp vai trò tại chỗ. p000043 giữ đúng phủ định và hai cỡ 128/180 mm. p000045 giữ phân biệt quân bổ sung với tiếp viện ở p000044/p000048; không cần đồng nhất hai loại này. Không thấy vấn đề cần thêm finding ở p000027–p000030, p000033–p000034, p000036, p000039, p000043–p000046 hoặc p000048.

## Trạng thái bàn giao

```yaml
role: reviewer
task_id: vol-02-ch-05-b02
state: done
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000025
  - YS-LN02/Text/part0026.xhtml/p000026
  - YS-LN02/Text/part0026.xhtml/p000027
  - YS-LN02/Text/part0026.xhtml/p000028
  - YS-LN02/Text/part0026.xhtml/p000029
  - YS-LN02/Text/part0026.xhtml/p000030
  - YS-LN02/Text/part0026.xhtml/p000031
  - YS-LN02/Text/part0026.xhtml/p000032
  - YS-LN02/Text/part0026.xhtml/p000033
  - YS-LN02/Text/part0026.xhtml/p000034
  - YS-LN02/Text/part0026.xhtml/p000035
  - YS-LN02/Text/part0026.xhtml/p000036
  - YS-LN02/Text/part0026.xhtml/p000037
  - YS-LN02/Text/part0026.xhtml/p000038
  - YS-LN02/Text/part0026.xhtml/p000039
  - YS-LN02/Text/part0026.xhtml/p000040
  - YS-LN02/Text/part0026.xhtml/p000041
  - YS-LN02/Text/part0026.xhtml/p000042
  - YS-LN02/Text/part0026.xhtml/p000043
  - YS-LN02/Text/part0026.xhtml/p000044
  - YS-LN02/Text/part0026.xhtml/p000045
  - YS-LN02/Text/part0026.xhtml/p000046
  - YS-LN02/Text/part0026.xhtml/p000047
  - YS-LN02/Text/part0026.xhtml/p000048
files_written:
  - reviews/prose/vol-02/ch-05-b02-codex.md
review_path: reviews/prose/vol-02/ch-05-b02-codex.md
validator: not_run
diff_check: not_run
commit: null
counts:
  reviewed_segments: 24
  serious: 0
  moderate: 6
  minor: 9
  total_findings: 15
  pending_term_groups: 4
unresolved_findings:
  - B02-F01
  - B02-F02
  - B02-F03
  - B02-F04
  - B02-F05
  - B02-F06
  - B02-F07
  - B02-F08
  - B02-F09
  - B02-F10
  - B02-F11
  - B02-F12
  - B02-F13
  - B02-F14
  - B02-F15
risks:
  - Sáu finding mức vừa còn mở; batch chưa đủ điều kiện đóng review.
  - machine-gun nets còn bất định giữa lưới hỏa lực và các vị trí súng máy; không suy diễn bố trí kỹ thuật.
  - Sanis rõ vai trò quân y tại chỗ nhưng chưa có canon về Việt hóa hoặc xuất xứ tên gọi.
  - Phương án Brass được ghi nhận và bản dịch đang dùng chưa khớp nhau.
  - Review giới hạn trong batch; không xác minh danh tính người kể hoặc cách dùng xuyên batch.
term_recommendations:
  - id: vol02-ch05-b02-sanis
    proposed_vi: Sanis
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000035, YS-LN02/Text/part0026.xhtml/p000040]
    status: pending
  - id: vol02-ch05-b02-harassing-fire
    proposed_vi: bắn quấy rối
    in_sentence: bắn rải để quấy rối
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000032]
    status: pending
  - id: vol02-ch05-b02-machine-gun-nets
    proposed_vi: lưới hỏa lực súng máy
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000041]
    status: pending
  - id: vol02-ch05-b02-brass
    proposed_vi: đám chỉ huy cấp cao
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000026]
    status: pending
pending_recommendations:
  - Coordinator ghi nhận bốn lựa chọn tạm cùng phương án khác và giới hạn nêu trong bảng; không nâng canon.
  - Translator có lease sửa sáu finding mức vừa và xử lý chín finding mức nhẹ trong đúng batch.
  - Sau sửa, đối chiếu lại nghĩa ở các ID có finding và giữ đúng phạm vi nhấn mạnh hiện có.
next_action: coordinator_record_provisional_choices_then_assign_batch_translation_revision
```
