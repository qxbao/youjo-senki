# Codex signoff sau sửa — vol-02-ch-05-b11

```yaml
role: reviewer
task_id: vol-02-ch-05-b11-fixes-signoff
state: done
review_path: reviews/prose/vol-02/ch-05-b11-fixes-signoff-codex.md
files_written:
  - reviews/prose/vol-02/ch-05-b11-fixes-signoff-codex.md
scope:
  batch: vol-02-ch-05-b11
  segment_id_start: YS-LN02/Text/part0026.xhtml/p000253
  segment_id_end: YS-LN02/Text/part0026.xhtml/p000283
  unit_count: 31
  assessment: Văn phong tiếng Việt, nhất quán nội bộ và mức khớp với disposition trong self-check của translator.
  inputs_read:
    - agents/shared.md
    - agents/reviewer.md
    - config/translation-pipeline.yml
    - handoffs/vol-02/ch-05-b11.yml
    - reviews/prose/vol-02/ch-05-b11-codex.md
    - reviews/semantic/vol-02/ch-05-b11-self-check.md
    - translations/vol-02/ch-05-b11.jsonl
  source_access: none
  limitation: >-
    Không mở source package, EPUB/PDF, canon hoặc batch/bản dịch khác.
    Disposition kiểm tra nguồn được tiếp nhận từ self-check, không phải kiểm chứng nguồn độc lập.
validator: not_run
diff_check: not_run
commit: null
counts:
  serious: 0
  moderate: 1
  minor: 0
  closed: 4
  unresolved: 1
  safely_deferred_findings: 0
  basis: Các mức nghiêm trọng đếm finding còn mở sau follow-up; thuật ngữ pending không tính là lỗi đã chứng minh.
closed_findings:
  - id: B11-P02
    original_severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000254
    resolution: >-
      Đã dùng “tân binh đang ngã xuống nhanh đến mức nào”; kết hợp từ tự nhiên hơn,
      khớp self-check, giữ hình ảnh thương vong và không tự chuyển thành tỷ lệ tử trận.
  - id: B11-P03
    original_severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000261
    resolution: >-
      Đã bỏ “rồi”; “ai cũng từng là tân binh” tự nhiên và nhất quán với p000262.
  - id: B11-P04
    original_severity: minor
    segment_id: YS-LN02/Text/part0026.xhtml/p000272
    resolution: >-
      “Không chịu nổi cảnh bị pháo kích áp chế” giải quyết kết hợp từ gượng.
      “Hôm nào … gây náo loạn … hẳn cô sẽ muốn” vẫn đọc được như tình huống dự liệu,
      không kể sự việc đã xảy ra; phù hợp disposition giữ thời gian/điều kiện của translator.
      Không cần buộc thay bằng “Nếu”; giữ chuyển điểm nhìn và thuật ngữ tạm.
  - id: B11-P05
    original_severity: minor
    segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000279
      - YS-LN02/Text/part0026.xhtml/p000280
    resolution: >-
      “Tanya đoán thử một điều đơn giản và lập tức được xác nhận” loại bỏ cụm
      “câu phỏng đoán”; cuộc gọi/hỏi ở p000278 cung cấp ngữ cảnh cho hành vi xác minh.
      “Tanya khá chắc rằng” loại bỏ cách chồng mức độ chắc chắn và giữ nhận định về đơn vị
      ở mức chưa tuyệt đối, đúng disposition của self-check. Không coi mọi suy đoán là đã xác nhận.
unresolved_findings:
  - id: B11-P01
    severity: moderate
    segment_id: YS-LN02/Text/part0026.xhtml/p000270
    related_segment_ids:
      - YS-LN02/Text/part0026.xhtml/p000275
      - YS-LN02/Text/part0026.xhtml/p000276
      - YS-LN02/Text/part0026.xhtml/p000279
    issue: Phân biệt thái độ nhận nghĩa vụ với tình trạng ban lệnh vẫn chưa rõ trong bản dịch.
    translator_disposition: >-
      Self-check giải thích p000270 là Tanya miễn cưỡng nhận nhiệm vụ như một mệnh lệnh;
      p000275 là lệnh cụ thể chưa được ban chính thức; p000276 vẫn là tin đồn;
      p000279 mới có xác nhận. Translator chủ trương giữ cả thái độ chấp nhận và bước xác minh.
    evidence: >-
      Bản hiện tại đổi thành “Dù sao thì rốt cuộc đây cũng là mệnh lệnh” nhưng vẫn giữ
      “cô phải ép mình nhận nhiệm vụ”. “Rốt cuộc” chưa đánh dấu đây là thái độ/dự liệu của Tanya,
      nên câu vẫn khẳng định tình trạng mệnh lệnh. p000275 tiếp tục nói “lệnh này còn chưa được
      ban xuống”; p000276 tiếp tục gọi là “tin đồn”. “Chuẩn bị tinh thần” giúp diễn đạt tâm lý
      nhưng chưa làm rõ sự khác biệt giữa nghĩa vụ dự kiến và việc ban lệnh chính thức.
    assessment: >-
      Bản sửa khớp các chữ và trạng thái mà self-check nói đã giữ, nhưng chưa chuyển được
      sự phân biệt do self-check giải thích vào văn bản cho người đọc. Chưa đủ căn cứ đóng
      finding moderate chỉ vì handoff ghi resolved. Đây là vấn đề diễn đạt/nhất quán nội bộ,
      không phải kết luận nguồn tự mâu thuẫn hoặc translator kiểm tra nguồn sai.
    required_translator_action: >-
      Translator đối chiếu lại đúng b11 và làm rõ ngay trong p000270 hoặc p000275 rằng
      Tanya đang chấp nhận nghĩa vụ dự kiến, còn lệnh cụ thể chưa được ban chính thức,
      nếu đúng disposition đã báo. Cân nhắc cách diễn đạt thái độ như “Tanya đành coi đó
      là nhiệm vụ phải chấp hành” chỉ nếu nguồn cho phép; đây không phải câu sửa bắt buộc.
      Không tự đổi thành mệnh đề điều kiện, xóa tin đồn, hoặc đưa xác nhận sớm hơn p000279.
      Nếu nguồn buộc giữ câu khẳng định hiện tại, self-check cần giải thích chính xác đối tượng
      của “mệnh lệnh” và điều chưa được ban/xác nhận, rồi chọn cách làm rõ ít suy diễn nhất.
      Trả bản sửa và self-check cho lượt signoff tiếp theo.
safely_deferred_findings: []
source_check_risks:
  disposition_received: [B11-U01, B11-U02, B11-U03, B11-U04, B11-U05, B11-U06]
  assessment: >-
    Bản hiện tại phù hợp các xử lý được báo: giữ chuyển ngôi, dùng “người bạn” ở p000253,
    dùng “khiến mọi người im lặng bằng xẻng” và giữ mốc 18 ở p000273,
    giữ hài đen ở dạng khả năng, giữ vùng in nghiêng p000283 và nghĩa mong muốn ở p000276.
    Cấp bậc nhất quán nội bộ tại các vị trí đã nêu. Không phát hiện thêm lỗi serious/moderate
    có căn cứ từ các đầu vào này; không tuyên bố U01–U06 đã được reviewer xác minh với nguồn.
term_recommendations:
  - source_term: instructor unit
    proposed_vi: đơn vị huấn luyện
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000255]
    status: provisional_non_canon
    recommendation: Giữ tạm theo handoff/self-check; không suy ra loại đơn vị cụ thể hơn.
  - source_term: suppressive shellfire
    proposed_vi: pháo kích áp chế
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000272]
    status: provisional_non_canon
    recommendation: Giữ tạm; câu đã đọc tự nhiên sau sửa, không cần đổi thuật ngữ ở lượt này.
  - source_term: firing line
    proposed_vi: tuyến hỏa lực
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000281]
    status: provisional_non_canon
    recommendation: Giữ pending theo self-check; chưa đủ căn cứ chọn tuyến bắn hoặc đồng nhất với tiền tuyến.
  - source_term: break the newbies in
    proposed_vi: giúp lính mới làm quen với công việc
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000280]
    status: provisional_non_canon
    recommendation: Giữ tạm; câu sau đã làm rõ liên hệ huấn luyện, không suy thêm hình thức huấn luyện.
  - category: cấp bậc và xưng hô trong B11-U02/B11-U05
    status: provisional_non_canon
    recommendation: Giữ các lựa chọn tạm theo disposition; không nâng thành canon qua signoff này.
signoff_status: withheld
signoff_reason: B11-P01 còn moderate; P02–P05 đã đóng, không có finding serious còn mở.
next_action: translator_follow_up_then_codex_signoff
```
