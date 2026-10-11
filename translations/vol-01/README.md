# Định dạng bản dịch LN 01

Chưa tạo bản dịch. Tệp dự kiến cho gói thử là `pilot-01.jsonl`; chỉ tạo khi có
nhiệm vụ dịch cụ thể và một tác tử được giao quyền sửa trong bàn giao.

JSONL dùng UTF-8: mỗi dòng là một object JSON hoàn chỉnh cho **một đơn vị
nguồn**, theo đúng thứ tự gói nguồn. Không có dòng tiêu đề, dòng trắng hay
object nhiều dòng; xuống đoạn trong translation dùng ký tự JSON `\n`.

| Trường | Kiểu | Quy định |
| --- | --- | --- |
| `segment_id` | string | Giữ đúng ID từ manifest; không tự đánh lại, gộp hay bỏ mã |
| `translation` | string | Chỉ bản dịch tiếng Việt của đơn vị; không chép văn bản tiếng Anh để đối chiếu |
| `status` | string | Chỉ `draft`, `reviewed` hoặc `approved` |
| `translator` | string | ID ổn định của người/tác tử chịu trách nhiệm dịch; không để trống |
| `glossary_version` | string | Dạng `sha256:<64 ký tự hex>` của canon/glossary.yml đã dùng, tham chiếu snapshot trong handoff |
| `source_sha256` | string | SHA-256 EPUB, 64 ký tự hex, phải khớp manifest và handoff |
| `notes` | array of strings | Ghi chú tiếng Việt, mã đề xuất hoặc locator; không chép câu hay cụm nguồn để minh họa; dùng `[]` khi không có |

Không thêm trường chứa nguồn như source_text, original hoặc source_xhtml.
Không đặt lại hay sao chép tiếng Anh vào bất kỳ tệp nào trong `translations/`,
kể cả notes, README hoặc tệp nháp. Nguồn đối chiếu chỉ ở gói cục bộ trong work/.
Giữ thông tin nhấn mạnh và liên kết cần thiết bằng ghi chú locator/mã; cách
trình bày xuất bản phải theo quyết định được duyệt, không tự chọn cú pháp mới.

Một mã chỉ có một dòng. Sau khi giao đủ gói, tập mã và thứ tự phải khớp nguồn,
không được bỏ đơn vị ngày/địa điểm hoặc đơn vị ngắn. Nếu bản dịch của một đơn vị
cần nhiều đoạn, dùng \n trong cùng translation, giữ nguyên segment_id.

Trạng thái đi từ draft (đang dịch/sửa), reviewed (đã có phản biện nghĩa và văn
phong, đã xử lý báo cáo), đến approved (người duyệt chấp nhận, đủ kiểm tra và
đạt rubric). Khi sửa nội dung reviewed/approved, đưa về draft và phản biện lại
phần bị ảnh hưởng. Người phản biện chỉ viết báo cáo, không tự sửa dòng JSONL.

Tra canon/style-guide.md, canon/characters.yml, canon/glossary.yml và
canon/decisions.md. Đề xuất mới ghi vào canon/glossary-pending.yml; không coi
đề xuất là thuật ngữ đã chốt. Thay canon cần ghi phiên bản mới và đối chiếu
các dòng bị ảnh hưởng trước khi cập nhật glossary_version.
