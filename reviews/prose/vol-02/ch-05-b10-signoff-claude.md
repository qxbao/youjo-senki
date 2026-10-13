# Final prose signoff — vol-02-ch-05-b10

Đã đọc agents/shared.md, agents/reviewer.md, config/translation-pipeline.yml, handoffs/vol-02/ch-05-b10.yml, work/run-state/pending-terms.yml (chính sách và các mục liên quan), review prose lần đầu, self-check follow-up và đủ 26 đoạn p000227–p000252 trong bản dịch hiện tại. Không mở/đọc prepared source package hoặc EPUB/PDF. Đánh giá nghĩa phụ thuộc nguồn dựa trên disposition của translator trong handoff/self-check, không phải đối chiếu nguồn độc lập.

Signoff prose: **pass**. Không còn finding serious/moderate/minor có căn cứ trong phạm vi đánh giá này. Signoff này xác nhận xử lý review; không thay cho các điều kiện hoàn tất pipeline về validator, diff-check và commit. Mọi thuật ngữ, tên gọi, cấp bậc và xưng hô tiếp tục provisional/non-canon.

## Đối chiếu F01–F06

| ID | Mức ban đầu | Segment ID | Disposition và căn cứ hiện tại |
| --- | --- | --- | --- |
| F01 | moderate | YS-LN02/Text/part0026.xhtml/p000241 | Closed, addressed. Thông báo hành chính “cắt ngang dòng suy nghĩ ấy”; không còn hàm ý Tanya đang nói thành tiếng. Phù hợp follow-up đã kiểm nguồn. |
| F02 | moderate | YS-LN02/Text/part0026.xhtml/p000245 | Closed, source-preserving ambiguity; no confirmed defect. Xem lý do bên dưới. |
| F03 | minor | YS-LN02/Text/part0026.xhtml/p000228 | Closed, addressed. Đã bỏ “bấy nhiêu”; giữ mức làm việc vất vả hơn mà không thêm quan hệ lượng với thời gian nghỉ. |
| F04 | minor | YS-LN02/Text/part0026.xhtml/p000235 | Closed, addressed. “Được hàng nghìn binh sĩ sử dụng” thay kết cấu “dùng bởi”; không biến số người thành yêu cầu nhân lực vận hành. |
| F05 | minor | YS-LN02/Text/part0026.xhtml/p000240 | Closed, addressed. “Ném tiền vào việc bắn đạn pháo … như nước lã” gắn hình ảnh với chi tiền; vẫn giữ nhấn mạnh toàn đoạn như self-check xác nhận. |
| F06 | minor | YS-LN02/Text/part0026.xhtml/p000243 | Closed, addressed. “Điều hành tiểu đoàn sao cho hiệu quả về chi phí” có đối tượng rõ, giữ giọng tính toán; không thêm mục tiêu giảm thương vong. |

F02 có thể đóng vì bản Việt là một phép tỉnh lược có thể bảo vệ được theo disposition đã kiểm nguồn. “Họ” quy chiếu về Bộ chỉ huy vừa được nêu; phần còn thiếu là vai trò/hành động của chủ thể ấy trong kết luận phủ định. Handoff và self-check đều ghi nguồn không xác định phần này. “Vậy chắc chắn không phải là họ” là câu tiếng Việt có thể hiểu như một kết luận loại trừ mà không buộc bổ sung hành động. Câu vẫn mơ hồ, nhưng không có căn cứ cho rằng bản dịch tạo thêm sự mơ hồ hoặc làm mất một hành động nguồn đã nêu. Độ chắc chắn cũng được giữ theo self-check. Vì vậy, yêu cầu lần đầu phải viết rõ hành động không còn là căn cứ giữ lỗi moderate. Không chọn hoặc bổ sung referent/hành động bị lược; không dùng các phương án tường minh có điều kiện của review đầu làm kết luận về nguồn. Việc thêm “là” chỉ cải thiện cú pháp; căn cứ đóng F02 là tính defensible của cách giữ tỉnh lược, không phải riêng thay đổi đó.

## Các giới hạn U và tính nhất quán

U01 đã được translator đính chính: “hậu phương” ở p000228/p000234, không quy cho p000227. U02 được self-check xác nhận phạm vi nhấn mạnh; bản hiện tại giữ khẩu quyết p000229 và toàn đoạn p000240. U03–U05 có disposition kiểm nguồn và giữ các lựa chọn tạm; riêng “giấy gọi nhập ngũ” vẫn lược yếu tố màu theo ghi chú translator, là giới hạn thuật ngữ còn pending, không đủ căn cứ nâng thành serious/moderate. Không tự xác định Grupper hoặc loại cơ sở Cadet Corps. U06 giữ giả định quân số và mức tin đồn ở p000249/p000252; phần kết luận F02 được xử lý như trên. U07 giữ “có lẽ” ở p000248, không nâng quan hệ với Being X thành lore. Các U vốn là giới hạn chứng cứ, không phải lỗi dịch đã xác nhận; chúng không được tính như findings còn mở.

Tên gọi/cấp bậc khi lặp, hai hướng xưng hô bà–cô, lớp nội tâm/trần thuật và các mức chắc chắn không phát sinh mâu thuẫn nội bộ serious/moderate mới. Không chỉnh bản dịch, ledger, handoff, self-check hoặc canon.

## YAML report

```yaml
role: reviewer
task_id: vol-02-ch-05-b10
state: done
review_path: reviews/prose/vol-02/ch-05-b10-signoff-claude.md
files_written:
  - reviews/prose/vol-02/ch-05-b10-signoff-claude.md
segment_scope:
  start: YS-LN02/Text/part0026.xhtml/p000227
  end: YS-LN02/Text/part0026.xhtml/p000252
  count: 26
counts: {serious: 0, moderate: 0, minor: 0}
initial_counts: {serious: 0, moderate: 2, minor: 4}
closed_findings: [F01, F02, F03, F04, F05, F06]
signoff_status: pass
signoff_scope: prose_and_followup_disposition_review
unresolved_findings: []
f02_disposition:
  status: closed
  classification: source_preserving_ambiguity
  confirmed_defect: false
  basis: Translator source-check records an unstated role/action; current Vietnamese defensibly preserves that ellipsis without selecting an interpretation.
  source_verified_independently_by_reviewer: false
term_policy: provisional_non_canon
term_recommendations:
  - source_term: red slips
    proposed_vi: giấy gọi nhập ngũ
    alternative_vi: giấy triệu tập nhập ngũ
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000231]
    status: pending
    rationale: Giữ lựa chọn chức năng hiện tại; yếu tố màu vẫn là giới hạn pending đã ghi nhận.
  - source_term: curtain of fire
    proposed_vi: màn hỏa lực yểm trợ
    alternative_vi: màn hỏa lực
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000233]
    status: pending
    rationale: Giữ nhất quán với handoff; phương án ngắn ít xác định chức năng hơn.
  - source_term: railway artillery / railway gun
    proposed_vi: pháo đường sắt
    alternative_vi: pháo đặt trên đường sắt
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000234, YS-LN02/Text/part0026.xhtml/p000235]
    status: pending
    rationale: Cách gọi gọn, nhất quán; không thêm cơ chế vận hành.
  - source_term: military-industrial complex
    proposed_vi: tổ hợp công nghiệp quân sự
    alternative_vi: tổ hợp quân sự–công nghiệp
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000237]
    status: pending
    rationale: Giữ ledger; không xác định một tổ chức cụ thể.
  - source_term: instructor unit
    proposed_vi: đơn vị huấn luyện
    alternative_vi: đơn vị phụ trách huấn luyện
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000249]
    status: pending
    rationale: Giữ chức năng tạm và mức tin đồn, không thêm biên chế.
  - source_term: Cadet Corps
    proposed_vi: Trường Sĩ quan
    alternative_vi: cơ sở đào tạo sĩ quan
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000251]
    status: pending
    rationale: Giữ handoff; loại cơ sở và tên chính thức chưa được chốt.
  - source_term: Grupper
    proposed_vi: Grupper
    alternative_vi: giữ nguyên Grupper, chờ xác minh định danh
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000232]
    status: pending
    rationale: Giữ dạng tên translator xác nhận, không suy diễn nhà sản xuất.
  - source_term: Lieutenant Serebryakov
    proposed_vi: Trung úy Serebryakov
    alternative_vi: Sĩ quan cấp úy Serebryakov
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000241, YS-LN02/Text/part0026.xhtml/p000245]
    status: pending
    rationale: Giữ lựa chọn gần nhất nhất quán; mapping cấp bậc tiếng Việt chưa canon.
  - source_term: ma’am
    proposed_vi: bà/thưa bà
    alternative_vi: Thiếu tá/thưa Thiếu tá
    segment_ids: [YS-LN02/Text/part0026.xhtml/p000242, YS-LN02/Text/part0026.xhtml/p000244]
    status: pending
    rationale: Nhất quán trong lô; không chốt tuổi hoặc quan hệ từ cách xưng hô.
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_records_signoff_and_checks_pipeline_completion
```
