# Rà soát văn phong — vol-02-ch-05-b11

Chỉ rà soát 31 đoạn b11 (p000253–p000283) từ bản dịch, self-check, handoff và các đề xuất pending được giao. Không mở source package, EPUB/PDF, bản dịch hay nguồn của batch khác. Không đối chiếu trực tiếp canon; nhận định về canon chỉ giới hạn ở metadata được giao. Các trích dẫn dưới đây là tiếng Việt trong bản dịch.

```yaml
role: reviewer
task_id: vol-02-ch-05-b11
state: done
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000253
  - YS-LN02/Text/part0026.xhtml/p000254
  - YS-LN02/Text/part0026.xhtml/p000255
  - YS-LN02/Text/part0026.xhtml/p000256
  - YS-LN02/Text/part0026.xhtml/p000257
  - YS-LN02/Text/part0026.xhtml/p000258
  - YS-LN02/Text/part0026.xhtml/p000259
  - YS-LN02/Text/part0026.xhtml/p000260
  - YS-LN02/Text/part0026.xhtml/p000261
  - YS-LN02/Text/part0026.xhtml/p000262
  - YS-LN02/Text/part0026.xhtml/p000263
  - YS-LN02/Text/part0026.xhtml/p000264
  - YS-LN02/Text/part0026.xhtml/p000265
  - YS-LN02/Text/part0026.xhtml/p000266
  - YS-LN02/Text/part0026.xhtml/p000267
  - YS-LN02/Text/part0026.xhtml/p000268
  - YS-LN02/Text/part0026.xhtml/p000269
  - YS-LN02/Text/part0026.xhtml/p000270
  - YS-LN02/Text/part0026.xhtml/p000271
  - YS-LN02/Text/part0026.xhtml/p000272
  - YS-LN02/Text/part0026.xhtml/p000273
  - YS-LN02/Text/part0026.xhtml/p000274
  - YS-LN02/Text/part0026.xhtml/p000275
  - YS-LN02/Text/part0026.xhtml/p000276
  - YS-LN02/Text/part0026.xhtml/p000277
  - YS-LN02/Text/part0026.xhtml/p000278
  - YS-LN02/Text/part0026.xhtml/p000279
  - YS-LN02/Text/part0026.xhtml/p000280
  - YS-LN02/Text/part0026.xhtml/p000281
  - YS-LN02/Text/part0026.xhtml/p000282
  - YS-LN02/Text/part0026.xhtml/p000283
files_written:
  - reviews/prose/vol-02/ch-05-b11-codex.md
review_path: reviews/prose/vol-02/ch-05-b11-codex.md
validator: not_run
diff_check: not_run
commit: null
counts:
  serious: 0
  moderate: 1
  minor: 4
findings:
  - id: B11-P01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000270
    related_segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000275
      - YS-LN02/Text/part0026.xhtml/p000276
      - YS-LN02/Text/part0026.xhtml/p000279
    issue: Trạng thái mệnh lệnh thiếu nhất quán trong chính bản dịch.
    evidence: >-
      p000270 viết “Dù sao thì đây cũng là mệnh lệnh” và “cô phải ép mình nhận nhiệm vụ”,
      nhưng p000275 viết “lệnh này còn chưa được ban xuống” và yêu cầu xác nhận;
      p000276 vẫn gọi thông tin là “tin đồn”, đến p000279 mới “nhận được xác nhận”.
      Người đọc khó phân biệt chấp nhận một nhiệm vụ đã giao với chuẩn bị cho khả năng được giao.
    proposed_fix: >-
      Translator đối chiếu riêng các đoạn này để làm rõ trạng thái chắc chắn/giả định.
      Nếu p000270 vẫn là dự liệu, cân nhắc “Dù sao, nếu đó là mệnh lệnh thì cũng phải chấp hành”
      và cách diễn đạt chuẩn bị nhận nhiệm vụ; nếu đã có lệnh, cần làm rõ điều chưa được xác nhận
      ở p000275–p000276. Không áp dụng phương án nào trước khi translator kiểm tra nguồn.
    resolution: unresolved; chưa sửa bản dịch; nguyên nhân và phương án đúng theo nguồn unverifiable.
  - id: B11-P02
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000254
    issue: Cụm danh từ diễn đạt thương vong gượng.
    evidence: '“nhận ra tốc độ quân mới ngã xuống” thiếu liên kết tự nhiên giữa “tốc độ” và mệnh đề phía sau.'
    proposed_fix: >-
      Cân nhắc “nhận ra tân binh đang ngã xuống nhanh đến mức nào”, giữ hình ảnh “ngã xuống”.
      Không tự thay bằng “tỷ lệ tử trận” vì chưa xác minh mức độ cụ thể của nghĩa.
    resolution: unresolved; đề xuất văn phong.
  - id: B11-P03
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000261
    issue: Kết hợp thời gian không tự nhiên trong lời thoại.
    evidence: '“ai rồi cũng từng là tân binh” ghép “rồi” hướng tới diễn biến với “từng” chỉ trải nghiệm đã qua; p000262 diễn đạt cùng ý bằng “ai cũng từng là lính mới”.'
    proposed_fix: 'Bỏ “rồi”: “Thì, ừm, ai cũng từng là tân binh mà…”'
    resolution: unresolved; đề xuất văn phong.
  - id: B11-P04
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000272
    issue: Hai cụm diễn đạt nặng và thiếu tự nhiên.
    evidence: '“không chịu nổi nỗi khổ vì pháo kích áp chế” và “Đến ngày một lính mới… làm ầm ĩ” khiến đoạn giả định khó đọc.'
    proposed_fix: >-
      Cân nhắc “không chịu nổi cảnh bị pháo kích áp chế” và “Nếu một lính mới chưa qua huấn luyện
      làm ầm ĩ…” nếu nguồn cho phép cấu trúc giả định ấy. Giữ thuật ngữ tạm và không tự đổi chuyển ngôi cô/tôi.
    resolution: unresolved; phần sửa điều kiện/thời gian cần translator xác minh nguồn.
  - id: B11-P05
    severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000279
    related_segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000280
    issue: Cách diễn đạt hành vi hỏi và mức độ chắc chắn gượng.
    evidence: >-
      “hỏi một câu phỏng đoán đơn giản” đặt “phỏng đoán” vào loại câu hỏi thiếu tự nhiên;
      “gần như chắc chắn đoán rằng” chồng hai cách biểu đạt nhận định mà chưa làm rõ điều được xác nhận.
    proposed_fix: >-
      p000279 có thể viết “Tanya thử hỏi để kiểm tra một phỏng đoán đơn giản…” nếu đúng nghĩa.
      p000280 có thể viết “Qua cuộc điện thoại, Tanya gần như chắc rằng…” nếu giữ được mức độ chắc chắn.
      Translator cần xác minh phạm vi của “xác nhận” ở p000279 trước khi sửa p000280;
      không tự nâng phỏng đoán thành thông tin đã được xác nhận.
    resolution: unresolved; độ chắc chắn đúng theo nguồn unverifiable.
unresolved_findings:
  - B11-P01
  - B11-P02
  - B11-P03
  - B11-P04
  - B11-P05
pending_terms:
  - source_term: instructor unit
    proposed_vi: đơn vị huấn luyện
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000255]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: suppressive shellfire
    proposed_vi: pháo kích áp chế
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000272]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: firing line
    proposed_vi: tuyến hỏa lực
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000281]
    volume: vol-02
    chapter: 5
    status: pending
  - source_term: break the newbies in
    proposed_vi: giúp lính mới làm quen với công việc
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000280]
    volume: vol-02
    chapter: 5
    status: pending
term_recommendations:
  - source_term: instructor unit
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000255]
    recommendation: Tạm giữ “đơn vị huấn luyện” theo handoff; rõ và phù hợp chủ đề huấn luyện trong b11.
    status: provisional_non_canon
    limitation: Không xác minh được loại đơn vị hay đối chiếu b10/canon.
  - source_term: suppressive shellfire
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000272]
    recommendation: Tạm giữ “pháo kích áp chế”; có thể cân nhắc “hỏa lực pháo áp chế” khi chỉnh cả câu.
    status: provisional_non_canon
    limitation: Chưa xác minh được mức tương đương với nguồn; không dùng lựa chọn này để suy ra loại đạn hay nhiệm vụ pháo binh.
  - source_term: firing line
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000281]
    recommendation: Giữ “tuyến hỏa lực” như đề xuất đang pending cho đến khi translator kiểm tra nghĩa tại chỗ.
    alternatives: [tuyến bắn]
    status: provisional_non_canon
    limitation: >-
      “Quan sát tuyến hỏa lực” chưa giúp xác định đó là một vị trí, tuyến bố trí hay khu vực giao chiến.
      Không có căn cứ chọn “tuyến bắn” hoặc đồng nhất với “tiền tuyến” chỉ từ p000282.
  - source_term: break the newbies in
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000280]
    recommendation: >-
      “Giúp lính mới làm quen với công việc” đọc được nhưng khá chung;
      phương án “huấn luyện cho lính mới quen việc” làm rõ liên kết với câu sau nếu nguồn cho phép.
    status: provisional_non_canon
    limitation: Không suy thêm hình thức huấn luyện hoặc mức độ chiến đấu thực tế.
risks:
  - id: B11-U01
    status: unverifiable
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000262
      - YS-LN02/Text/part0026.xhtml/p000266
      - YS-LN02/Text/part0026.xhtml/p000270
      - YS-LN02/Text/part0026.xhtml/p000272
      - YS-LN02/Text/part0026.xhtml/p000276
      - YS-LN02/Text/part0026.xhtml/p000280
    issue: >-
      Bản dịch chuyển giữa tôi/chúng tôi và Tanya/cô. Trong tiếng Việt vẫn nhận diện được Tanya,
      nhưng không thể xác minh ranh giới trần thuật/nội tâm hoặc việc chuyển ngôi có đúng nguồn.
      Self-check khẳng định riêng p000272 giữ chuyển điểm nhìn; đó là lời khai translator, chưa phải kiểm chứng độc lập.
    action: Translator kiểm tra ranh giới điểm nhìn; reviewer không đề nghị đồng nhất toàn bộ về một ngôi.
  - id: B11-U02
    status: unverifiable
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000253
      - YS-LN02/Text/part0026.xhtml/p000265
      - YS-LN02/Text/part0026.xhtml/p000267
      - YS-LN02/Text/part0026.xhtml/p000275
    issue: >-
      “cô bạn của cô” hàm chứa quan hệ chưa kiểm chứng; “ngài” nhất quán giữa hai lượt cấp dưới nói với Thiếu tá;
      “Các anh” có thể là cách gọi tập thể nhưng chưa xác minh được phạm vi người nghe, nhất là khi Serebryakov vừa lên tiếng.
      Không đủ căn cứ kết luận sai giới tính hay xưng hô.
    action: Translator kiểm tra đối tượng lời thoại và quy tắc xưng hô đã giao; không tự thay bằng một quan hệ hoặc đại từ khác.
  - id: B11-U03
    status: unverifiable
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000273
      - YS-LN02/Text/part0026.xhtml/p000274
    issue: >-
      Bản tiếng Việt dùng “Tệ nhất thì”, “có thể” và “nếu cần” nên đọc như khả năng/ý nghĩ đe dọa,
      không như việc đã làm. Tuy nhiên mức độ đe dọa, đối tượng “chất thải” và hàm ý dùng xẻng
      chưa thể kiểm chứng với nguồn. Mốc 18 hiện diện; không xác minh vị trí/định dạng tương ứng trong nguồn.
    action: Translator xác minh; không làm nhẹ hài đen hoặc chuyển sang hành động đã xảy ra.
  - id: B11-U04
    status: unverifiable
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000283]
    issue: >-
      Bản dịch có một vùng in nghiêng “Được rồi, cần lên kế hoạch huấn luyện”.
      Self-check nói đúng vùng nhấn mạnh nguồn; không thể xác minh độc lập phạm vi ấy hay nhấn mạnh bị bỏ sót ở các đoạn còn lại.
    action: Translator xác minh theo nguồn; không tự thêm hoặc bỏ in nghiêng.
  - id: B11-U05
    status: unverifiable
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000253
      - YS-LN02/Text/part0026.xhtml/p000258
      - YS-LN02/Text/part0026.xhtml/p000262
      - YS-LN02/Text/part0026.xhtml/p000264
      - YS-LN02/Text/part0026.xhtml/p000265
      - YS-LN02/Text/part0026.xhtml/p000267
      - YS-LN02/Text/part0026.xhtml/p000268
      - YS-LN02/Text/part0026.xhtml/p000278
    issue: >-
      Trong b11, Weiss/Serebryakov được gọi Trung úy và von Degurechaff được gọi Thiếu tá,
      không thấy lệch nội bộ rõ ràng. Độ đúng của cấp bậc, cách viết tên và sự phù hợp canon chưa thể xác minh.
    action: Giữ các lựa chọn tạm theo handoff; không nâng thành canon.
  - id: B11-U06
    status: unverifiable
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000276]
    issue: >-
      “tôi sẽ biết mình có muốn nhận việc này hay không” biểu đạt mong muốn cá nhân,
      trong khi các đoạn gần đó nhấn mạnh nghĩa vụ chấp hành. Không đủ căn cứ kết luận
      câu nguồn nói về mong muốn, sự sẵn sàng hay đánh giá nhiệm vụ.
    action: Translator kiểm tra nghĩa, không tự đổi thành quyền từ chối hoặc trạng thái sẵn sàng.
signoff:
  status: withheld
  scope: Vietnamese prose and internal consistency only; no independent source verification.
  reason: B11-P01 mức moderate còn unresolved; không ký duyệt b11.
next_action: translator_follow_up
translator_follow_up: >-
  Translator xử lý B11-P01 trước, xem các đề xuất minor và kiểm tra các điểm unverifiable bằng đúng nguồn b11;
  trả bản sửa/self-check cho lượt review tiếp theo. Reviewer không sửa translations hoặc ledger.
```
