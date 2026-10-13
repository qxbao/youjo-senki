# Review — vol-02-ch-06-b19-review

Reviewer: Codex; runtime reviewer được cấu hình trong `config/translation-pipeline.yml`: `codex-personal`, `gpt-6.1-sol`, effort `medium`. Không gọi worker khác, không sửa bản dịch hoặc ledger.

## Phạm vi và kiểm tra đầu vào

- Chỉ đối chiếu package b19, hai handoff b19, bản dịch b19, self-check b19, mục ledger `chapter6_b19_translator_proposals` và năm tài liệu canon được handoff b19 nêu tên. Không mở EPUB/PDF hoặc package khác.
- SHA-256 package: `723e1690b28ab3388f722f722362dcf76c7f2498ed788d89d6cb911f1f7151ea`, khớp yêu cầu.
- Package và bản dịch đều có đúng 26 ID, đúng thứ tự theo handoff: `YS-LN02/Text/part0030.xhtml/p000584` đến `YS-LN02/Text/part0030.xhtml/p000609`. Hash cả năm tài liệu canon khớp handoff.
- Cả 26 đoạn XHTML không có dấu nhấn mạnh tương ứng cần biểu diễn bằng Markdown; bản dịch không tự thêm chữ nghiêng. Dấu ngắt và nhịp câu vẫn được xét riêng.
- Không chạy validator hoặc diff-check của pipeline; đây là review, không phải xác nhận lô đã đạt điều kiện hoàn tất.

## Findings cần xử lý

### Vừa

**B19-M01 — YS-LN02/Text/part0030.xhtml/p000587 — Đổi bình diện đánh giá.**

“Xét trên thực tế” biến một nhận định ở bình diện khái niệm thành khẳng định về thực tế. Đây là thay đổi đáng kể trong lập luận về ý định chiến đấu của dân thường, dù câu tiếp theo có đưa bằng chứng. Đề xuất thay bằng “xét về mặt khái niệm”; phương án tự nhiên hơn là “xét về ý nghĩa của hành động ấy”, nhưng có thêm diễn giải. Tin cậy: cao. Không suy từ ý định chiến đấu thành tư cách pháp lý của người tham chiến.

**B19-M02 — YS-LN02/Text/part0030.xhtml/p000587 — Thu hẹp đối tượng và chốt phạm vi thu hồi quá mạnh.**

Bản dịch chỉ còn “những thi thể”, đồng thời thêm hai nhóm “binh sĩ và nhân viên quân đội”. Package phân biệt thân thể với thi thể của nhóm nhân viên quân đội; không đủ căn cứ để thêm nhóm binh sĩ hoặc coi toàn bộ đối tượng là người chết. Về cú pháp, `recovered` trực tiếp bổ nghĩa nhóm nhân viên quân đội, không trực tiếp bổ nghĩa riêng thi thể. Tuy vậy, cụm nguồn vụng và ngữ cảnh giải cứu chưa đủ để kết luận tất cả đều sống, đã chết, được giải cứu hay chỉ được tìm lại.

Đề xuất tạm cho riêng cụm này: “thân thể và thi thể của những nhân viên quân đội được tìm lại”. Giữ hai danh từ và đối tượng nhân viên quân đội, dùng “được tìm lại” để tránh chốt sống/chết hoặc quy trình thu hồi. Không thêm thương tích, tra tấn, quân tịch, quốc tịch hay quy chế tù binh. Phương án khác: “những nhân viên quân đội được tìm lại, qua thân thể và thi thể của họ, cho thấy…”; dễ đọc hơn nhưng đổi cấu trúc chứng cứ và vẫn hơi gượng. Không khuyến nghị “các nhân viên quân đội được giải cứu” vì có thể loại các thi thể ra khỏi phạm vi, cũng không khuyến nghị chỉ “các thi thể được thu hồi” vì bỏ thân thể.

Tin cậy: cao về việc bản dịch hiện tại thêm nhóm và gộp đối tượng; vừa về cách gắn cú pháp của `recovered`; vừa-thấp về nghĩa sự kiện cụ thể. Đây là cách xử lý pending ít suy diễn, không phải quyết định lore/canon. Coordinator ghi bất định và lựa chọn tạm vào ledger/handoff; translator áp dụng rồi tiếp tục.

**B19-M03 — YS-LN02/Text/part0030.xhtml/p000604 — Thêm động cơ lo ngại.**

“Vẫn chưa thể yên lòng” diễn giải các cấp chỉ huy đang bất an hoặc lo cho an toàn. Package chỉ nói họ chưa thỏa mãn, sau đó mô tả việc vẫn dốc toàn lực khi những người kia còn trước mắt và không chấp nhận cách khác. Đề xuất “vẫn chưa thể hài lòng” hoặc “vẫn chưa thỏa mãn”. Tin cậy: cao. Không bổ sung lý do vì sao họ chưa hài lòng; giữ chủ thể “họ” là các cấp chỉ huy, “những người ấy” là người dân Arene.

### Nhẹ

**B19-L01 — YS-LN02/Text/part0030.xhtml/p000585 — Đại từ mang sắc thái và không nhất quán cục bộ.**

“Cô ta” dễ mang khoảng cách hoặc thái độ bất thiện mạnh hơn đại từ nguồn; các đoạn trần thuật sau lại dùng “cô”. Đề xuất gọi “Tanya” tại đây để giữ chủ thể rõ mà không tự chốt xưng hô. Có thể dùng “cô” nếu coordinator tiếp tục lựa chọn pending của riêng b19. Tin cậy: vừa-cao. Không tự áp dụng “nó” từ pilot LN01 sang LN02, vì DEC-P01-001 giới hạn giai đoạn áp dụng và cấm mở rộng khi thiếu căn cứ.

**B19-L02 — YS-LN02/Text/part0030.xhtml/p000602 — Thêm định dạng thông tin mục tiêu.**

“Xin tọa độ mục tiêu” thu hẹp yêu cầu mục tiêu thành yêu cầu tọa độ, trong khi package không nêu loại thông tin này. Đề xuất “Xin chỉ định mục tiêu” hoặc “Xin thông tin mục tiêu”. Tin cậy: cao. Giữ “Pixie 01” và “rõ”; không thêm giao thức vô tuyến ngoài package.

**B19-L03 — YS-LN02/Text/part0030.xhtml/p000600 — Cụm chức vụ và quân hàm khó đọc.**

“Thiếu tá chỉ huy tiểu đoàn von Degurechaff” khiến chức vụ chen giữa quân hàm và tên. Đề xuất “Thiếu tá von Degurechaff, chỉ huy tiểu đoàn” rồi điều chỉnh cấu trúc sở hữu của lời cảnh báo; phương án khác là “chỉ huy tiểu đoàn, Thiếu tá von Degurechaff”. Tin cậy: cao. Giữ cả quân hàm và chức vụ, không dùng riêng chức vụ để thay quân hàm.

## Tám nhóm đề xuất tạm — tất cả pending, không phải canon

| Nhóm | ID đầy đủ | Khuyến nghị tạm | Căn cứ, phương án khác, độ tin cậy |
|---|---|---|---|
| cleanup | YS-LN02/Text/part0030.xhtml/p000589 | Giữ “truy quét” | Chuỗi p000586–p000593 mô tả xử lý kháng cự còn lại bằng hỏa lực; “truy quét” phù hợp hoạt động tác chiến. Có thể dùng “dọn dẹp” để giữ cách gọi lạnh lùng/uyển ngữ, nhưng dễ gợi công việc hậu chiến. “Truy quét” làm sắc thái tác chiến rõ hơn nguồn; lưu tradeoff này. Tin cậy: vừa. Không viện chứng cứ từ package b18. |
| God / đại từ | YS-LN02/Text/part0030.xhtml/p000594 | Giữ “Thượng đế”; có thể giữ “ngài” viết thường | Danh xưng phổ quát và mệnh đề điều kiện tồn tại đều được giữ; “ngài” có thể là lối gọi mỉa mai trong suy nghĩ Tanya, không tự chứng minh lòng tôn kính. Phương án khác: “Chúa”, hoặc lặp “Thượng đế” để tránh sắc thái đại từ. Không đồng nhất danh xưng này với Being X. Tin cậy: vừa. |
| Being X | YS-LN02/Text/part0030.xhtml/p000595 | Giữ “Being X” | Khớp đề xuất pending P05-being-x trong canon được phép đọc; chưa có quyết định Việt hóa. Phương án khác: “Thực thể X”, cần ghi đề xuất riêng nếu đổi. Tin cậy: cao về lựa chọn tạm, không xác nhận canon. |
| Major / Battalion Commander | YS-LN02/Text/part0030.xhtml/p000600; YS-LN02/Text/part0030.xhtml/p000603; YS-LN02/Text/part0030.xhtml/p000609 | “Thiếu tá” / “chỉ huy tiểu đoàn” | Nguồn tách quân hàm khỏi chức vụ; cách dịch hiện tại đúng phân biệt, cần sửa vị trí cụm ở p000600 theo L03. Phương án khác: giữ “Major” khi chưa ánh xạ, nhưng kém tự nhiên; chỉ nêu chức vụ sẽ mất quân hàm nên không chọn. Tin cậy: cao. Không suy diễn lịch sử thăng cấp. |
| Imperial subjects | YS-LN02/Text/part0030.xhtml/p000601 | Giữ “thần dân Đế quốc” | Giữ quan hệ thần dân thay vì mặc định công dân. Phương án khác: “người dân Đế quốc”, trung tính hơn nhưng mất sắc thái quan hệ chính thể. Tin cậy: cao. |
| Imperial prisoners / military employees | YS-LN02/Text/part0030.xhtml/p000596; YS-LN02/Text/part0030.xhtml/p000603 | “Nhân viên quân đội bị giam cầm”; ưu tiên “những người Đế quốc bị giam giữ” thay “tù nhân Đế quốc” | “Nhân viên quân đội” không tự thêm quân tịch; “người … bị giam giữ” tránh sắc thái người bị kết án mà “tù nhân” có thể gợi. “Tù nhân Đế quốc” vẫn là phương án literal chấp nhận được nếu ngữ cảnh giam giữ rõ; “tù binh Đế quốc” chỉ dùng khi đủ căn cứ quân sự, package này chưa đủ. Tin cậy: cao về tránh chốt quy chế, vừa về cách gọi tiếng Việt. Không gộp nghĩa `recovered` ở p000603 với p000587 chỉ vì cùng từ. |
| Tanya / Grantz và điểm nhìn | YS-LN02/Text/part0030.xhtml/p000585; YS-LN02/Text/part0030.xhtml/p000589; YS-LN02/Text/part0030.xhtml/p000596; YS-LN02/Text/part0030.xhtml/p000597; YS-LN02/Text/part0030.xhtml/p000598; YS-LN02/Text/part0030.xhtml/p000599; YS-LN02/Text/part0030.xhtml/p000600; YS-LN02/Text/part0030.xhtml/p000601; YS-LN02/Text/part0030.xhtml/p000608; YS-LN02/Text/part0030.xhtml/p000609 | Dùng tên Tanya ở p000585; giữ “cô” ở trần thuật còn lại như lựa chọn cục bộ; giữ “anh” cho Grantz; “mình” tự quy chiếu theo chủ thể | Các đại từ nguồn và chuyển điểm nhìn trong b19 đủ để phân biệt hai chủ thể. P000594–p000597 là nhận định Tanya; p000598–p000601 và p000608–p000609 theo Grantz. “Chúng ta” p000595 là con người nói chung, không riêng tiểu đoàn. “Cô” cuối p000608 là Tanya; có thể thay tên để tránh hiểu là một nhân vật khác. Phương án khác: lặp tên/bỏ đại từ, ít suy diễn nhất. Không mở rộng quy tắc pilot LN01 hoặc lựa chọn b19 ra volume khác. Tin cậy: cao về chủ thể, vừa về sắc thái xưng hô. |
| HQ / pursuit battle | YS-LN02/Text/part0030.xhtml/p000605; YS-LN02/Text/part0030.xhtml/p000606 | Giữ “Bộ Chỉ huy” / “lệnh truy kích” | HQ trong trao đổi thông tin chỉ đầu mối chỉ huy; không đủ căn cứ gán cấp tổ chức cụ thể. “Lệnh truy kích” diễn đạt tự nhiên mệnh lệnh tiến hành hoạt động truy kích, được ngữ cảnh rút lui p000606 hỗ trợ. Phương án khác: “sở chỉ huy” / “lệnh tiến hành trận truy kích”. Không đồng nhất HQ với Bộ Chỉ huy Lục quân Đế quốc tại p000604. Tin cậy: cao về hoạt động truy kích, vừa về danh xưng HQ. |

## Bao phủ từng đoạn

Mọi hàng dưới đây đã xét nghĩa, văn phong, chủ thể/đại từ, mức chắc chắn, nhấn mạnh và thuật ngữ/cấp bậc. “Đạt” chỉ có nghĩa không thấy finding cần sửa trong phạm vi package.

| Stable ID | Kết quả |
|---|---|
| YS-LN02/Text/part0030.xhtml/p000584 | Đạt: ưu tiên cứu người và quan hệ nhiệm vụ bảo vệ dân được giữ. |
| YS-LN02/Text/part0030.xhtml/p000585 | L01; giữ dè dặt, trao đổi mạng sống, cứu một số người trước oanh kích. |
| YS-LN02/Text/part0030.xhtml/p000586 | Đạt: đã phá kháng cự có tổ chức, còn các ổ kháng cự; giọng mệnh lệnh được giữ. |
| YS-LN02/Text/part0030.xhtml/p000587 | M01, M02; sửa bình diện đánh giá và cụm thân thể/thi thể, giữ bất định phạm vi. |
| YS-LN02/Text/part0030.xhtml/p000588 | Đạt: Grantz không thể vui trước cảnh tượng; không nhầm sang Tanya. |
| YS-LN02/Text/part0030.xhtml/p000589 | Đạt với đề xuất pending “truy quét”; Tanya quan sát hài lòng. |
| YS-LN02/Text/part0030.xhtml/p000590 | Đạt: trình tự phá mái, thả bom cháy, phá tòa nhà tạo gió và mục đích duy trì lửa. |
| YS-LN02/Text/part0030.xhtml/p000591 | Đạt: nhịp lặp và Arene cháy toàn bộ trong vài giờ. |
| YS-LN02/Text/part0030.xhtml/p000592 | Đạt: chướng ngại vô tác dụng; không thêm hành động của dân. |
| YS-LN02/Text/part0030.xhtml/p000593 | Đạt: giữ suy đoán về pháp sư và so sánh địa ngục; không khẳng định tất cả đã chết. |
| YS-LN02/Text/part0030.xhtml/p000594 | Đạt với pending danh xưng/đại từ; mệnh đề tồn tại có điều kiện còn nguyên. |
| YS-LN02/Text/part0030.xhtml/p000595 | Đạt: Being X, chỉ con người cứu người và điểm yếu chung; giọng hoài nghi còn rõ. |
| YS-LN02/Text/part0030.xhtml/p000596 | Đạt: Tanya, quan hệ nhân quả và nhân viên quân đội bị giam. Hình ảnh tay sạch mang nghĩa tránh trực tiếp nhúng tay vào giết chóc; giữ liên kết p000597–p000598. |
| YS-LN02/Text/part0030.xhtml/p000597 | Đạt: hành động đáp ứng ý thức tập thể và tự tạo cớ về sau, không biến thành lời khen của người kể. |
| YS-LN02/Text/part0030.xhtml/p000598 | Đạt: chuyển sang Grantz; tay sạch là lời tự biện hộ, không chứng nhận vô tội. “Người không tham chiến” không tự gán tư cách pháp lý. |
| YS-LN02/Text/part0030.xhtml/p000599 | Đạt: giữ tự dối mình và điều kiện duy trì niềm an ủi. |
| YS-LN02/Text/part0030.xhtml/p000600 | L03; lời cảnh báo đầu hàng và dân quân khước từ phá vỡ tự biện hộ của Grantz. |
| YS-LN02/Text/part0030.xhtml/p000601 | Đạt: tiên phong, phản thực quá khứ và trở lại nhiệm vụ ban đầu; tên đơn vị/cấp tiểu đoàn không bị đổi. |
| YS-LN02/Text/part0030.xhtml/p000602 | L02; hô hiệu và xác nhận được giữ, bỏ bổ sung tọa độ. |
| YS-LN02/Text/part0030.xhtml/p000603 | Đạt với pending người bị giam giữ; tiểu đoàn tập hợp, ngầm hiểu lệnh tấn công, Tanya định đích thân tham gia. Dấu ba chấm chuyển ra cuối câu nhưng từ “đích thân” vẫn giữ trọng tâm; có thể đặt ngắt sát từ này để giữ nhịp, không bắt buộc thêm chữ nghiêng. |
| YS-LN02/Text/part0030.xhtml/p000604 | M03; giữ ngờ vực khả năng sống sót/chiến đấu và đúng hai nhóm chủ thể. |
| YS-LN02/Text/part0030.xhtml/p000605 | Đạt với pending HQ/truy kích; vị chỉ huy là Tanya, giọng thường ngày và thúc giục lệnh tiếp theo. |
| YS-LN02/Text/part0030.xhtml/p000606 | Đạt: pháp sư còn lại làm hậu quân khi rút lui, câu hỏi khả năng tiêu diệt được giữ. |
| YS-LN02/Text/part0030.xhtml/p000607 | Đạt: người nói thấy mục tiêu và xác nhận đơn vị làm được; không thêm cảm xúc. |
| YS-LN02/Text/part0030.xhtml/p000608 | Đạt: Grantz nhớ việc huấn luyện/phân công, hối tiếc và phải học cách chỉ huy của Tanya. “Đại đội sở chỉ huy” phù hợp cấp đơn vị, không nhầm với HQ đầu mối liên lạc. |
| YS-LN02/Text/part0030.xhtml/p000609 | Đạt: Grantz nhìn theo Tanya; nhóm người chỉ hơi có trật tự, nhóm hậu quân chỉ trông như pháp sư Cộng hòa và đầy thương tích. Không nâng nhận diện bằng mắt thành xác minh danh tính. |

## Kết quả cho coordinator

```yaml
role: reviewer
task_id: vol-02-ch-06-b19-review
state: done
review_path: reviews/prose/vol-02/ch-06-b19-codex.md
files_written:
  - reviews/prose/vol-02/ch-06-b19-codex.md
counts:
  reviewed_ids: 26
  serious: 0
  moderate: 3
  minor: 3
  pending_groups_assessed: 8
  scope_ambiguities_assessed: 1
validator: not_run
diff_check: not_run
unresolved_findings: [B19-M01, B19-M02, B19-M03, B19-L01, B19-L02, B19-L03]
term_recommendations:
  status: pending_non_canon
  groups: 8
  details: Tám nhóm ở bảng trên; riêng p000587 theo B19-M02.
risks:
  - p000587 còn bất định về sự kiện được tìm lại; không chốt sống/chết hoặc tư cách quân sự/pháp lý.
  - Quy ước đại từ pilot LN01 không tự mở rộng sang LN02; lựa chọn cục bộ vẫn pending.
  - Review hoàn tất nhưng ba lỗi vừa chưa được translator sửa; lô chưa đủ điều kiện hoàn tất.
commit: null
next_action: coordinator_record_provisional_choices_then_translator_fix_six_findings_and_recheck_b19
```
