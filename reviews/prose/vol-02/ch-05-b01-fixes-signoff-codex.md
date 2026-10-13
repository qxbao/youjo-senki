# Sign-off các sửa đổi vol-02-ch-05-b01

Chấp nhận tám sửa đổi được giao: **B01-F01–B01-F08 đã xử lý**, không còn finding được giao chưa xử lý. Không phát hiện lỗi mới mức nghiêm trọng hoặc vừa trong các đoạn chịu ảnh hưởng. Đây là sign-off review cục bộ, không xác nhận toàn bộ điều kiện hoàn tất của pipeline và không duyệt canon.

## Phạm vi và đầu vào

Phạm vi duy nhất là `YS-LN02/Text/part0026.xhtml/p000001`–`YS-LN02/Text/part0026.xhtml/p000024`. Đọc `agents/shared.md`, `agents/reviewer.md`, config, handoff, năm tài liệu canon được handoff liệt kê, riêng mục `chapter5_b01_translation_proposals`, prepared package, bản dịch hiện tại và báo cáo `ch-05-b01-codex.md`. Các đoạn còn lại trong batch chỉ cung cấp ngữ cảnh cho tám sửa đổi và lựa chọn tạm; không mở lại một vòng review toàn batch. Không đọc batch/source/translation/review khác, không mở EPUB/PDF, không chạy worker. Báo cáo này không trích câu nguồn.

Tên B01-F01–B01-F08 trong nhiệm vụ tương ứng F01–F08 của báo cáo gốc và handoff. Mã đoạn giữ nguyên.

Kiểm tra đầu vào tại chỗ: hash package khớp handoff (`8557f906f5d531213cb5fe652563921bc5f648de32e9ce2d9ed0a04bf4bbbaa2`); năm hash canon đều khớp. Package và bản dịch đều có đúng 24 mã đoạn theo thứ tự, metadata hash nguồn khớp handoff. SHA-256 bản dịch được sign-off: `ff180dcb116b3638dce1b6a88dfedae17512b80277172f8fac8245be75277897`. Các đối chiếu này không phải validator hoặc diff_check của pipeline; kết quả pass được ghi trong handoff là kết quả của lượt sửa trước, không phải lần chạy của reviewer này.

## Xác minh tám finding

Mọi mã đoạn trong bảng có tiền tố `YS-LN02/Text/part0026.xhtml/`.

| ID | Mức ban đầu | Mã đoạn | Căn cứ chấp nhận sửa đổi | Kết quả |
| --- | --- | --- | --- | --- |
| B01-F01 | Vừa | p000015 | “in hằn trước mắt tôi” phục hồi dấu in thị giác; “mang một vẻ thiêng liêng” giữ sắc thái tôn kính, bỏ đánh giá đẹp. Sự kính trọng kéo dài đến hiện tại vẫn còn. | resolved |
| B01-F02 | Vừa | p000020 | “những viên đạn sống” giữ ẩn dụ người lính bị dùng để phá tuyến; mạch Đại đội H hứng đạn và phê phán giới chỉ huy làm rõ đối tượng. Không còn gợi vật liệu chế tạo đạn từ thân người. Giữ mức chắc chắn của nhận định về giới chỉ huy. | resolved |
| B01-F03 | Vừa | p000021 | “Họ nghĩ…” giữ ngôi thứ ba, nối về giới chỉ huy ở đoạn trước; câu hỏi vẫn cân đo đất với mạng người. Dấu `?!` và chữ nghiêng toàn câu được giữ. | resolved |
| B01-F04 | Nhẹ | p000002 | Câu đặt ông lão làm chủ thể của việc từng phục vụ, rồi đặt ký ức làm đối tượng khắc sâu vào tâm trí ông. Không còn cấu trúc gán tư cách người lính cho “mọi thứ”; thông tin Đại chiến và giấc mơ lặp lại vẫn còn. | resolved |
| B01-F05 | Nhẹ | p000007 | “tôi” nối nhất quán với lời hồi tưởng ngôi thứ nhất của người lính già. Giữ “Có lẽ”, ý không quên và phạm vi nghiêng của nội tâm; không áp quy ước riêng của Tanya cho ông lão. | resolved |
| B01-F06 | Nhẹ | p000022 | “mấy khẩu pháo địch” xác định đối tượng cần áp chế theo mạch pháo kích p000010–p000012. Giữ yêu cầu yểm trợ đường không và tính khẩn thiết; không thêm loại pháo hoặc cơ chế yểm trợ. | resolved |
| B01-F07 | Nhẹ | p000023 | “đẩy tuyến chiến đấu lên” làm rõ mục tiêu đẩy tuyến về phía trước. Giữ kế hoạch dự kiến qua “Lẽ ra”, giới hạn ưu thế trên không cục bộ và lời giải thích cách chiến dịch vốn phải vận hành. | resolved |
| B01-F08 | Nhẹ | p000024 | Phạm vi nghiêng là `*đầy đủ*` và `*hoàn toàn không có*`, phù hợp DEC-P01-002. Giữ đối lập lời hứa/thực tế và ý muốn hét lên, không biến thành lời đã nói. | resolved |

Không thấy sửa đổi làm mất nội dung, đảo phủ định, đổi chủ thể, tăng mức chắc chắn hoặc tạo lỗi nghiêm trọng/vừa mới ở tám đoạn trên. Các lựa chọn Rhine được kiểm tra thêm tại p000001 và p000006.

## Lựa chọn tạm và giới hạn canon

Handoff ghi `pending_non_canon`; mục ledger được phép đọc ghi `provisional_non_canon`, với từng mục liên quan có `status: pending`. Glossary chính thức và danh sách nhân vật vẫn rỗng; decisions chỉ có hai quyết định pilot, không duyệt ba lựa chọn dưới đây. Việc chấp nhận sửa đổi không nâng chúng thành canon.

| Lựa chọn | Áp dụng và căn cứ | Phương án khác / bất định | Trạng thái |
| --- | --- | --- | --- |
| Human bullets | p000020 dùng “những viên đạn sống”, hợp hình ảnh đem người lính phá phòng tuyến và giọng chua chát. | “đạn người” ngắn nhưng gượng; diễn giải bằng thân người rõ hơn nhưng mất hình ảnh viên đạn. Tin cậy khá trong batch; không xác lập tên chiến thuật hay cơ chế vũ khí. | proposed_non_canon |
| Rhine | p000001 dùng “chiến trường Rhine”; p000006 chỉ dùng Rhine, không phân loại thêm. Ngữ cảnh hồi ức chiến đấu hỗ trợ lựa chọn tạm này. | Giữ riêng Rhine ở cả hai đoạn ít giải thích hơn; “mặt trận Rhine” xác định phạm vi quân sự mạnh hơn. Chưa đủ căn cứ về địa lý, dòng sông, trận đánh hoặc chiến dịch cụ thể. | proposed_non_canon |
| Đại từ người lính già | p000007 dùng “tôi” trong nội tâm để nối với lời hồi tưởng; trần thuật vẫn dùng ông/ông lão. DEC-P01-001 không mở rộng quy ước Tanya sang chủ thể này. | “mình” có thể phân biệt độc thoại riêng tư nhưng làm giọng tách khỏi hồi tưởng. Tin cậy trung bình; không xác lập nhân thân hoặc quy ước xưng hô ngoài batch. | proposed_non_canon |

Hai lựa chọn tại p000015 về bắn theo quan sát và bệnh bàn chân chiến hào vẫn là pending. Chấp nhận F01 không chứng nhận chúng thành thuật ngữ đã chốt; chưa đủ căn cứ để thêm quy trình hiệu chỉnh, khí tài hoặc thông tin bệnh lý. Lựa chọn pháo địch ở F06 dựa trên ngữ cảnh cục bộ, không phải quyết định canon về loại súng.

## Kết quả bàn giao

```yaml
role: reviewer
task_id: vol-02-ch-05-b01
state: done
signoff: accepted_for_assigned_fixes
scope_start: YS-LN02/Text/part0026.xhtml/p000001
scope_end: YS-LN02/Text/part0026.xhtml/p000024
segment_ids:
  - YS-LN02/Text/part0026.xhtml/p000001
  - YS-LN02/Text/part0026.xhtml/p000002
  - YS-LN02/Text/part0026.xhtml/p000006
  - YS-LN02/Text/part0026.xhtml/p000007
  - YS-LN02/Text/part0026.xhtml/p000015
  - YS-LN02/Text/part0026.xhtml/p000020
  - YS-LN02/Text/part0026.xhtml/p000021
  - YS-LN02/Text/part0026.xhtml/p000022
  - YS-LN02/Text/part0026.xhtml/p000023
  - YS-LN02/Text/part0026.xhtml/p000024
files_written: [reviews/prose/vol-02/ch-05-b01-fixes-signoff-codex.md]
review_path: reviews/prose/vol-02/ch-05-b01-fixes-signoff-codex.md
translation_sha256: ff180dcb116b3638dce1b6a88dfedae17512b80277172f8fac8245be75277897
resolved_findings: [B01-F01, B01-F02, B01-F03, B01-F04, B01-F05, B01-F06, B01-F07, B01-F08]
unresolved_findings: []
counts:
  assigned_findings: 8
  resolved: 8
  unresolved: 0
  resolved_moderate: 3
  resolved_minor: 5
  fix_segments_rechecked: 8
  provisional_choice_segments_additionally_checked: 2
  new_serious: 0
  new_moderate: 0
  new_minor_reported: 0
findings: []
term_recommendations:
  - {id: vol02-ch05-b01-human-bullets, action: retain_provisionally, status: proposed_non_canon}
  - {id: vol02-ch05-b01-rhine, action: retain_provisionally_with_p000006_unclassified, status: proposed_non_canon}
  - {id: vol02-ch05-b01-old-soldier-interior-voice, action: retain_toi_provisionally, status: proposed_non_canon}
risks:
  - Rhine chưa xác định địa lý hoặc phạm vi chiến dịch; không thêm phân loại.
  - Đại từ tôi chỉ là lựa chọn tạm cho người lính già trong ngữ cảnh batch.
  - Bắn theo quan sát còn bất định về mức hiệu chỉnh; thuật ngữ bệnh cũng chưa được duyệt canon.
  - Sign-off giới hạn ở tám finding và lựa chọn tạm; không thay thế kiểm tra hoàn tất của pipeline.
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_record_signoff_and_verify_required_pipeline_checks_before_batch_completion_keep_choices_non_canon
```
