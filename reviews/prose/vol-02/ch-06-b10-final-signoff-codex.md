# Final-signoff b10 — Codex

```yaml
role: reviewer
task_id: vol-02-ch-06-b10-final-signoff
state: done
review_result: changes_requested
review_path: reviews/prose/vol-02/ch-06-b10-final-signoff-codex.md
coverage: 46/46
segment_id_start: YS-LN02/Text/part0030.xhtml/p000285
segment_id_end: YS-LN02/Text/part0030.xhtml/p000330
source_package: work/vol-02/batches/ch-06-b10-source.jsonl
source_package_sha256: 2aa9e83e70ceb04bd458066e5a6621374f1ff1c60bdaa2682b8a5bc56ac5199c
hash_verified: true
counts:
  serious: 0
  moderate: 0
  minor: 1
  total: 1
count_unit: unresolved_finding_record
resolved_counts:
  serious: 0
  moderate: 23
  minor: 7
  total: 30
unresolved_findings: [L04]
pending_terms_count: 8
terms_status: pending_non_canon
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_assign_L04_fix_and_followup
```

Đã hoàn tất kiểm tra, nhưng chưa cấp signoff toàn bộ F01–F23 và L01–L08: L04 còn một phần chưa sửa. Không còn finding nghiêm trọng/vừa trong phạm vi được giao. Trạng thái `done` là hoàn tất nhiệm vụ reviewer, không phải hoàn tất batch hay cho phép commit.

Đã đọc `AGENTS.md`, `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff final-signoff, package b10 được chỉ định, bản dịch hiện tại, self-check, báo cáo review b10 và handoff sửa review. SHA-256 package khớp giá trị được giao. Package và bản dịch đều có 46 ID duy nhất, cùng thứ tự p000285–p000330. Đã đối chiếu nội dung và XHTML của package; không mở EPUB/PDF, package khác hoặc đầu vào ngoài phạm vi. Chỉ ghi báo cáo này; không sửa bản dịch, self-check, handoff, ledger, canon hay checkpoint. Không chạy validator/diff-check; trạng thái pass trong fix handoff là kết quả do translator báo, không phải kiểm chứng lại của reviewer này.

Các ID rút gọn dưới đây đều thuộc `YS-LN02/Text/part0030.xhtml/`.

| Finding | ID | Kết quả đối chiếu hiện tại |
| --- | --- | --- |
| F01 | p000287 | Đã xử lý: điều kiện giữ trong câu chính; không thêm lại câu điều kiện ở cuối. |
| F02 | p000294 | Đã xử lý: phương án không đốt thành phố chỉ xuất hiện một lần. |
| F03 | p000295 | Đã xử lý: một câu hỏi nghiêng, rồi trần thuật về điều kiện ý chí chiến đấu. |
| F04 | p000300 | Đã xử lý: nội tâm xuất hiện một lần. |
| F05 | p000306 | Đã xử lý: không còn mảnh cuối và bản nội tâm lặp; giữ hai vùng nhấn mạnh, trần thuật Rhine theo sau. |
| F06 | p000308 | Đã xử lý: thuật ngữ nhấn mạnh nằm trong câu chính, không có mảnh thừa cuối đoạn. |
| F07 | p000312 | Đã xử lý: một câu nội tâm. |
| F08 | p000313 | Đã xử lý: giữ trần thuật đầu và một câu hỏi nội tâm. |
| F09 | p000314 | Đã xử lý: hai câu nội tâm chỉ xuất hiện một lần. |
| F10 | p000316 | Đã xử lý: chuỗi lời đồn nằm một lần trong nội tâm, rồi đến đánh giá thường. |
| F11 | p000320 | Đã xử lý: ba câu nội tâm xuất hiện một lần. |
| F12 | p000321 | Đã xử lý: ba câu nội tâm xuất hiện một lần. |
| F13 | p000323 | Đã xử lý: một câu hỏi nghiêng. |
| F14 | p000324 | Đã xử lý: chuỗi hình ảnh nanh/ma cà rồng xuất hiện một lần trong nội tâm. |
| F15 | p000330 | Đã xử lý: một câu hỏi nghiêng, giữ phần kể về muốn hỏi rồi kìm lại. |
| F16 | p000289 | Đã xử lý: hai tham chiếu Tanya trong trần thuật đều dùng “nó”. |
| F17 | p000299 | Đã xử lý: trần thuật dùng “nó”, giữ giới hạn cường điệu của đánh giá. |
| F18 | p000306 | Đã xử lý: “nó” chỉ ở trần thuật; câu hỏi nghiêng vẫn là nội tâm người tư lệnh. |
| F19 | p000308 | Đã xử lý: người tư lệnh là “ông”, Tanya là “nó”. |
| F20 | p000316 | Đã xử lý: nội tâm giữ “cô ta”; đánh giá thường dùng “nó”. |
| F21 | p000295 | Đã xử lý: cảnh báo đầu hàng để tạo cớ biện minh vẫn là câu hỏi suy đoán. |
| F22 | p000320 | Đã xử lý: người lính được so sánh với cỗ máy chiến tranh, không thuộc về một cỗ máy/hệ thống. |
| F23 | p000330 | Đã xử lý: câu hỏi nêu đối tượng cần lo; giữ mong muốn hỏi, tự kiềm chế và không muốn biết. |
| L01 | p000287 | Đã xử lý: chỉ phần “không còn cách nào khác” được nghiêng, không bao “nếu”. |
| L02 | p000294 | Đã xử lý về phạm vi nhấn mạnh: chỉ phần đánh giá “thì tốt hơn” được nghiêng, không bao phương án không đốt thành phố. |
| L03 | p000297 | Đã xử lý: “bị thương hoặc thiệt mạng” giữ độ mở của thương vong. |
| L04 | p000303 | Chưa xử lý hết: giữ nghe đồn và trò đối đáp thính giác, nhưng vẫn dùng hình ảnh số nhiều “chim chóc”. |
| L05 | p000309 | Đã xử lý yêu cầu trong fix handoff: “có dịp trổ sức”, giữ mỉa mai, câu giờ và nguy cơ quân số áp đảo. |
| L06 | p000312 | Đã xử lý: riêng nội tâm người tư lệnh dùng “mình” nhất quán. |
| L07 | p000326 | Đã xử lý: “giật nảy người” giữ phản ứng cơ thể nhỏ; người tư lệnh sợ Tanya. |
| L08 | p000327 | Đã xử lý: “nguyên các khu phố” giữ số nhiều, không mở rộng đối tượng tàn phá thành toàn thành phố. |

Không phát hiện đoạn bị lặp thêm trong toàn bộ 46 ID. Các vùng nghiêng không bị chép lại thành bản thường; không có dòng dịch trùng hoàn toàn. Số vùng nhấn mạnh ở từng ID khớp XHTML; đã kiểm tra riêng phạm vi L01/L02 và hai vùng ở p000306. Những lần nhắc khái niệm trong đối thoại và trần thuật có chức năng riêng vẫn được giữ.

Phạm vi đại từ đúng với chỉ dẫn sửa: năm vị trí trần thuật F16–F20 dùng “nó”; lời thoại, nội tâm/lời đồn của người tư lệnh và lời gọi hướng tới Tanya vẫn giữ “cô/cô ta”. Nội tâm của tư lệnh dùng “mình”, không chuyển thành tự quy chiếu của Tanya. Các tham chiếu p000326/p000330 không bị đổi máy móc theo quy tắc năm vị trí trên. Ba sửa nghĩa F21–F23 đều giữ được đối tượng, điều kiện và điểm nhìn; p000295 không xác lập động cơ thật, p000316 vẫn là lời đồn/suy đoán và p000324 không xác lập lore ma cà rồng.

L04 còn mở ở mức nhẹ, độ chắc chắn cao về số lượng hình ảnh: package dùng hình ảnh một chú chim; bản hiện tại vẫn là “tôi nghe chim chóc đồn về chuyện du kích…”. Sửa phần đó thành “tôi nghe một chú chim mách nhỏ chuyện du kích…”; phương án khác là “tôi nghe một chú chim líu lo chuyện du kích…”. Giữ cách ám chỉ tin nghe được và câu đáp về thính giác tại p000304. Self-check chỉ ghi giữ hình ảnh chim và nghe đồn, nên chưa phản ánh phần số ít chưa sửa; handoff khai L04 resolved cần được coordinator đối chiếu với kết luận này. Reviewer không sửa các tệp đó.

Tám lựa chọn vẫn là đề xuất pending/non-canon theo tài liệu b10 được phép đọc:

| Mục | Lựa chọn hiện hành và phạm vi |
| --- | --- |
| T01 | “giới chỉ huy cấp cao” p000286/p000319; “cấp trên” p000294. Hai cách gọi phù hợp ngữ cảnh, không chốt tên cơ quan/quân hàm. |
| T02 | “Tiểu đoàn Pháp sư Trên không số 203” p000293/p000295, nhất quán. |
| T03 | “trường quân sự cao cấp” p000298/p000315, nhất quán; chưa xác lập tên/cơ cấu chính thức. |
| T04 | “cớ biện minh” p000295; không xác lập ý đồ cốt truyện. |
| T05 | “tư lệnh quân đoàn”, trần thuật “ông”, p000285/p000326; không suy tên riêng hay quân hàm. |
| T06 | “nó” tại đúng năm vị trí F16–F20; không nâng thành quy tắc canon chung cho LN02. |
| T07 | “mình” cho nội tâm người tư lệnh tại p000300–p000302/p000312/p000316/p000320/p000326; không phải quy tắc Tanya. |
| T08 | “Huy hiệu Đột kích Cánh bạc”: đề xuất cho Silver Wings Assault Badge; không xuất hiện trong package b10, giữ loại vật phẩm huy hiệu, không kiểm tra hoặc sửa batch khác. |

Đây là xác nhận trạng thái thể hiện trong self-check, review và fix handoff của b10; không phải kiểm toán ledger/canon ngoài phạm vi. Không có lựa chọn nào được báo cáo này nâng thành canon. Rủi ro còn lại là L04 chưa sửa hết dù handoff khai đã xử lý, cùng việc không được mở rộng các lựa chọn đại từ/thuật ngữ tạm ra ngoài phạm vi. Self-check còn nhắc p000265 ngoài b10; không dùng lời nhắc đó làm bằng chứng đã kiểm tra đoạn ngoài nhiệm vụ. Coordinator cần giao sửa L04 và cập nhật self-check trong quyền của mình trước khi xin signoff đầy đủ; reviewer không tự mở task tiếp theo.
