# Final sign-off — vol-02-ch-06-b11

```yaml
role: reviewer
task_id: vol-02-ch-06-b11-final-signoff
state: done
review_result: signoff_with_minor_documentation_finding
review_path: reviews/prose/vol-02/ch-06-b11-final-signoff-codex.md
files_written:
- reviews/prose/vol-02/ch-06-b11-final-signoff-codex.md
source_package: work/vol-02/batches/ch-06-b11-source.jsonl
source_package_sha256: c1dfda6756f791aad672a6f89a87de0017104fd7be57d0cc8a123f631b5d0831
hash_verification: pass
coverage: 28/28
segment_id_start: YS-LN02/Text/part0030.xhtml/p000331
segment_id_end: YS-LN02/Text/part0030.xhtml/p000358
resolved_findings: [F01, F02, F03, F04, F05, F06, F07]
counts:
  serious: 0
  moderate: 0
  minor: 1
counting_method: Đếm phát hiện còn mở, không đếm số đoạn; F08 chỉ thuộc self-check.
unresolved_findings:
- id: F08
  severity: minor
  segment_ids:
  - YS-LN02/Text/part0030.xhtml/p000332
  - YS-LN02/Text/part0030.xhtml/p000333
  issue: Danh sách đề xuất trong self-check còn ghi lựa chọn trước khi sửa F02, chưa đánh dấu đã thay thế.
pending_terms_status: provisional_non_canon
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_receive_signoff_and_assign_self_check_cleanup
```

## Phạm vi và căn cứ

Đã đọc persona reviewer/shared, `AGENTS.md`, `config/translation-pipeline.yml`, handoff final-signoff, review và handoff sửa b11, bản dịch hiện tại, self-check hiện tại và duy nhất package nguồn b11. Tham chiếu handoff gốc/review b11, các tệp canon được handoff dẫn và các mục ledger b11 để xác nhận trạng thái lựa chọn. Không mở EPUB/PDF, package khác hoặc nội dung chú thích ngoài package; không tra cứu dịch vụ ngoài. Không dùng graphify để quét/tạo dữ liệu vì phạm vi task chỉ cho phép đọc đầu vào được giao và ghi một báo cáo.

SHA-256 package tính trực tiếp khớp giá trị trong handoff. Package và bản dịch có đủ 28 ID tương ứng, đúng thứ tự p000331–p000358. Đã đối chiếu text/XHTML với bản dịch về nghĩa, tầng phát ngôn, điểm nhìn và phạm vi nhấn mạnh. Đây là sign-off nội dung trong phạm vi b11, không xác nhận hoàn tất điều kiện commit/validator của pipeline.

## Kết quả F01–F07

| Finding | Mức cũ | Segment ID | Kết quả kiểm tra bản hiện tại |
|---|---|---|---|
| F01 | moderate | YS-LN02/Text/part0030.xhtml/p000331 | Resolved: đã khôi phục cặp ngoặc thoại; không thêm người nói. Self-check ghi đúng sửa đổi. |
| F02 | moderate | YS-LN02/Text/part0030.xhtml/p000332; YS-LN02/Text/part0030.xhtml/p000333 | Resolved trong bản dịch: giữ hình ảnh xúc xắc ở cả hai đoạn, chỉ p000332 nghiêng; p000333 còn mức phỏng đoán và cảm giác buồn nôn. Ghi chú xử lý F02 trong self-check đúng; danh sách đề xuất cũ còn lệch, xem F08. |
| F03 | moderate | YS-LN02/Text/part0030.xhtml/p000350 | Resolved: cách gọi oanh kích bao quát, không giới hạn vào thả bom; giữ câu hỏi, khả năng và tính ám chỉ. Self-check khớp. |
| F04 | moderate | YS-LN02/Text/part0030.xhtml/p000355 | Resolved: dùng lên án/quy là, không khẳng định kết án chính thức; giữ đối lập bên thắng/bên thua và nỗi lo tự bảo toàn. Self-check ghi đúng giới hạn suy luận. |
| F05 | minor | YS-LN02/Text/part0030.xhtml/p000341 | Resolved: thêm sắc thái quen thuộc cho thành ngữ ở nhà giữa địa ngục; giữ hai mức phỏng đoán, lời hướng đến Tanya và nghiêng toàn đoạn. |
| F06 | minor | YS-LN02/Text/part0030.xhtml/p000342 | Resolved: hầm nơi chờ lệnh ở tuyến trước cùng, hầm chỉ huy an toàn phía sau; không còn gán lực lượng dự bị hoặc thêm so sánh an toàn hơn. Nhiệm vụ và ưu tiên mệnh lệnh được giữ. |
| F07 | minor | YS-LN02/Text/part0030.xhtml/p000354 | Resolved: lời tự trấn an tự nhiên hơn, nhấn hẹp đúng chức năng; giữ thảm sát và việc thay ném bom rải thảm bằng pháo binh, không biến thông thường thành hợp pháp. |

Không phát hiện lỗi nghĩa/văn phong nghiêm trọng hoặc vừa còn lại ở 28 đoạn. F01–F07 không được tính lại vào số lỗi mở.

## Phát hiện còn lại

### F08 — minor — self-check — YS-LN02/Text/part0030.xhtml/p000332; YS-LN02/Text/part0030.xhtml/p000333

- **Vấn đề:** Mục “Pending đề xuất mới” vẫn ghi “sự đã rồi” cho p000332 mà không nêu đây là đề xuất cũ đã được thay thế. Ngay bên dưới, self-check xác nhận đã sửa F02 bằng hình ảnh xúc xắc ở p000332–p000333, đúng với bản dịch hiện tại.
- **Căn cứ:** Ba đầu vào hiện tại — bản dịch, ghi chú sửa trong self-check và handoff sửa — thống nhất giữ xúc xắc. Danh sách đề xuất chưa cập nhật khiến bản ghi lựa chọn đang áp dụng thiếu nhất quán.
- **Đề nghị:** Người được giao quyền sửa self-check cập nhật lựa chọn đang áp dụng thành “xúc xắc đã gieo / con xúc xắc”, ghi cả hai ID; nếu giữ “sự đã rồi” thì đánh dấu là phương án cũ/không áp dụng. Vẫn ghi pending, không nâng thành canon. Không cần sửa lại bản dịch vì F02 đã đạt.
- **Mức bất định:** Thấp. Đây là lỗi tài liệu nhẹ, không mở lại lỗi nghĩa F02.

## Thuật ngữ và giới hạn sign-off

Các đề xuất b11 vẫn mang trạng thái pending/provisional_non_canon trong handoff, self-check và các mục ledger được đối chiếu. Glossary chính thức và danh sách nhân vật chưa chốt mục nào. DEC-P01-001 và DEC-P01-002 là quyết định đã duyệt về đại từ/nhấn mạnh; áp dụng chúng không đồng nghĩa các lựa chọn tên gọi, quân hàm, thuật ngữ hay xưng hô địa phương đã thành canon.

| Lựa chọn đang dùng / phạm vi | Trạng thái và khuyến nghị |
|---|---|
| Xúc xắc ở p000332–p000333 | Tạm giữ để bảo toàn hình ảnh lặp; F08 yêu cầu đồng bộ self-check, không canon hóa. |
| WTO ở p000351 | Tạm giữ nguyên viết tắt; package thiếu định danh và nội dung chú thích 20. |
| Công thức gây nổ ở p000352 | Tạm giữ literal, phân biệt với thuốc nổ mạnh; không xác lập cơ chế phép thuật. “Công thức thuốc nổ” chỉ là phương án cũ kém ưu tiên. |
| Ném bom rải thảm ở p000354; oanh kích chiến lược không phân biệt mục tiêu ở p000350 | Tạm giữ nhất quán; không thêm kết luận pháp lý. |
| Tòa án Quân sự Viễn Đông ở p000358 | Tạm giữ cấu tạo tên; không bổ sung định danh lịch sử ngoài package. |
| Dân quân, tư lệnh quân đoàn, Thiếu tá Pháp sư, Mùa xuân Praha, tên riêng và xưng hô trong thoại/lời hướng đến Tanya | Tiếp tục là lựa chọn tạm; không suy thêm quan hệ, quân hàm cá nhân hoặc người nói. |
| Hầm chờ lệnh/tuyến trước cùng; lên án/quy là; hành xử nhân đạo/giả vờ tử tế | Chấp nhận cách dùng hiện tại trong ngữ cảnh, vẫn là lựa chọn ngôn ngữ tạm. |

Rủi ro còn lại: p000351 chưa truy vết được nội dung chú thích 20, và bản dịch không giữ mốc chú thích; chưa có quy ước xuất chú thích để kết luận đây là lỗi cần sửa. p000355 còn bất định trong cách hiểu cụm pháp lý, nhưng cách trung tính hiện tại không thêm kết quả tố tụng. p000350–p000358 là lập luận/suy nghĩ của Tanya, không phải xác nhận luật hoặc lịch sử. Ledger giữ đề xuất cũ cùng khuyến nghị mới; coordinator cần duy trì dấu vết lựa chọn đang áp dụng khi tiếp nhận F08.

Sign-off bản dịch b11 với một phát hiện nhẹ về self-check. Số lỗi mở chính xác: **serious 0, moderate 0, minor 1**. Không chạy validator hoặc diff-check; kết quả pass trong handoff sửa là thông tin do translator báo, không phải kiểm tra lại của lượt này. Chỉ ghi báo cáo này; không sửa bản dịch, self-check, canon, ledger hoặc handoff; không commit.
