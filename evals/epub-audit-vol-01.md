# Kiểm tra EPUB — LN 01

Ngày kiểm tra: 2026-10-12. Chế độ: chỉ đọc tại chỗ.

## Phạm vi và bảo toàn nguồn

Đã đọc `project.local.yml` và dùng `source_dir` để xác định thư mục nguồn
(thư mục anh em `../youjo-senki-source/`). Không lưu đường dẫn tuyệt đối cục bộ
vào báo cáo. Kiểm kê tên/kích thước 14 EPUB; chỉ phân tích cấu trúc LN 01.
Không mở PDF.

EPUB được mở bằng `zipfile.ZipFile(..., 'r')`; XML/CSS được đọc trong bộ nhớ,
không giải nén ra đĩa. Không sửa, sao chép, đổi tên, đưa EPUB vào Git hoặc tải
lên nơi khác. Không tạo công cụ tách EPUB, bản dịch hoặc tệp chứa văn bản truyện.
Báo cáo chỉ lưu tên tệp, nhãn tiêu đề/mục lục và số liệu cấu trúc.

Kích thước và mtime của cả 14 EPUB không đổi trước/sau lượt kiểm tra tạo báo cáo.
SHA-256 LN 01 cũng không đổi trong lượt này:

`7698e1b80fc5d560020b8934f6243b3b7be1be9c911668455a069f857f3da528`

Fingerprint này nhận diện bản nguồn đã kiểm tra, không xác nhận nguồn trùng bản
phát hành khác. Việc đọc có thể ảnh hưởng atime tùy hệ thống tệp.

## Kiểm kê

Có đúng **14 EPUB** trực tiếp trong `source_dir`: đủ **LN 01–LN 14**, mỗi tập
một tệp, không thiếu hoặc trùng số tập. Xác định tập từ tên tệp; chưa xác minh
nội dung hoặc tính hợp lệ của LN 02–LN 14.

| Tập | Tên tệp | Kích thước (byte) |
| --- | --- | ---: |
| LN 01 | `The Saga of Tanya the Evil - LN 01.epub` | 13,279,309 |
| LN 02 | `The Saga of Tanya the Evil - LN 02.epub` | 29,089,547 |
| LN 03 | `The Saga of Tanya the Evil - LN 03.epub` | 14,870,094 |
| LN 04 | `The Saga of Tanya the Evil - LN 04.epub` | 10,274,778 |
| LN 05 | `The Saga of Tanya the Evil - LN 05.epub` | 7,350,325 |
| LN 06 | `The Saga of Tanya the Evil - LN 06.epub` | 7,955,788 |
| LN 07 | `The Saga of Tanya the Evil - LN 07.epub` | 16,549,207 |
| LN 08 | `The Saga of Tanya the Evil - LN 08.epub` | 19,760,771 |
| LN 09 | `The Saga of Tanya the Evil - LN 09.epub` | 21,277,826 |
| LN 10 | `The Saga of Tanya the Evil - LN 10.epub` | 21,789,575 |
| LN 11 | `The Saga of Tanya the Evil - LN 11.epub` | 22,063,088 |
| LN 12 | `The Saga of Tanya the Evil - LN 12.epub` | 21,767,596 |
| LN 13 | `The Saga of Tanya the Evil - LN 13.epub` | 26,960,966 |
| LN 14 | `The Saga of Tanya the Evil - LN 14.epub` | 25,216,284 |

## Tổng quan LN 01

- Tệp: `The Saga of Tanya the Evil - LN 01.epub`.
- Container: `META-INF/container.xml`; package: `OEBPS/content.opf`.
- Package khai báo EPUB **3.0**, ngôn ngữ `en`; spine khai báo `page-progression-direction="ltr"`, `toc="ncx"`.
- Manifest có **38 XHTML**, không có tài liệu `text/html`; cả 38 đều có trong spine.
- **37** tài liệu `linear="yes"`; bìa ở đầu spine nhưng `linear="no"`.
- **3.192 thẻ p** trong body toàn bộ spine; tất cả có văn bản không trắng, không có p chứa ảnh. Đây là số nút đoạn, không phải số câu/dòng hiển thị hay số đơn vị dịch cuối cùng.
- Phần truyện Chapter 0–V: **3.119 p**. Còn lại: copyright 36, afterword 14, footnote 20, newsletter 3.
- **22 tài nguyên JPEG** trong manifest và ZIP, **47 lần dùng img** trong body; không có SVG image. Tất cả 22 ảnh được tham chiếu.
- `Images/Art_image1.jpg` dùng **26 lần**; 21 ảnh khác dùng một lần mỗi ảnh. Không xem 47 lần dùng là 47 minh họa độc lập.
- Có một stylesheet: `OEBPS/Styles/stylesheet.css`.

## Tài liệu theo thứ tự đọc

Thứ tự lấy từ **spine**, không theo tên tệp hoặc thứ tự ZIP. Đường dẫn đầy đủ
là `OEBPS/Text/` cộng tên trong bảng. Liệt kê cả bìa không tuyến tính để đủ spine.

Tiêu đề lấy từ h1 hoặc mục lục. Nhãn “tiếp”/“trang ảnh” là phân loại suy ra từ
vị trí spine và markup, không phải kết quả OCR. Nhãn chương kế thừa mục trước
cho các phần tiếp nối/trang ảnh xen. Không đọc chữ nằm trong ảnh.

| # | XHTML | linear | Tiêu đề / vai trò | p | img |
| ---: | --- | --- | --- | ---: | ---: |
| 01 | `cover.xhtml` | no | Cover (ảnh) | 0 | 1 |
| 02 | `insert001.xhtml` | yes | Insert — trang ảnh | 0 | 1 |
| 03 | `insert002.xhtml` | yes | Insert — trang ảnh | 0 | 1 |
| 04 | `insert003.xhtml` | yes | Insert — trang ảnh | 0 | 1 |
| 05 | `titlepage.xhtml` | yes | Title Page (ảnh) | 0 | 1 |
| 06 | `copyright.xhtml` | yes | Copyright | 36 | 0 |
| 07 | `toc.xhtml` | yes | Contents / Navigation | 0 | 0 |
| 08 | `Prologue.xhtml` | yes | Chapter 0: Prologue — trang ảnh | 0 | 1 |
| 09 | `chapter001.xhtml` | yes | [chapter] 0 Prologue | 154 | 3 |
| 10 | `chapter002.xhtml` | yes | Chapter I: The Sky over Norden — trang ảnh | 0 | 1 |
| 11 | `chapter003.xhtml` | yes | [chapter] I The Sky over Norden | 8 | 1 |
| 12 | `chapter003a.xhtml` | yes | Chapter I: The Sky over Norden — trang ảnh | 0 | 1 |
| 13 | `chapter003b.xhtml` | yes | Chapter I: The Sky over Norden (tiếp) | 293 | 2 |
| 14 | `chapter003c.xhtml` | yes | Chapter I: The Sky over Norden — trang ảnh | 0 | 1 |
| 15 | `chapter003d.xhtml` | yes | Chapter I: The Sky over Norden (tiếp) | 63 | 1 |
| 16 | `chapter004.xhtml` | yes | Chapter II: The Elinium Type 95 Computation Orb — trang ảnh | 0 | 1 |
| 17 | `chapter005.xhtml` | yes | [chapter] II The Elinium Type 95 Computation Orb | 127 | 1 |
| 18 | `chapter005a.xhtml` | yes | Chapter II: The Elinium Type 95 Computation Orb — trang ảnh | 0 | 1 |
| 19 | `chapter005b.xhtml` | yes | Chapter II: The Elinium Type 95 Computation Orb (tiếp) | 309 | 2 |
| 20 | `chapter006.xhtml` | yes | Chapter III: The Watch/Guard on the Rhine — trang ảnh | 0 | 1 |
| 21 | `chapter007.xhtml` | yes | [chapter] III The Watch/Guard on the Rhine | 498 | 4 |
| 22 | `chapter007a.xhtml` | yes | Chapter III: The Watch/Guard on the Rhine — trang ảnh | 0 | 1 |
| 23 | `chapter007b.xhtml` | yes | Chapter III: The Watch/Guard on the Rhine (tiếp) | 315 | 1 |
| 24 | `chapter008.xhtml` | yes | Chapter IV: War College — trang ảnh | 0 | 1 |
| 25 | `chapter009.xhtml` | yes | [chpater] IV War College | 249 | 1 |
| 26 | `chapter009a.xhtml` | yes | Chapter IV: War College — trang ảnh | 0 | 1 |
| 27 | `chapter009b.xhtml` | yes | Chapter IV: War College (tiếp) | 275 | 1 |
| 28 | `chapter010.xhtml` | yes | Chapter V: The Primeval Battalion — trang ảnh | 0 | 1 |
| 29 | `chapter011.xhtml` | yes | [chapter] V The Primeval Battalion | 646 | 8 |
| 30 | `chapter011a.xhtml` | yes | Chapter V: The Primeval Battalion — trang ảnh | 0 | 1 |
| 31 | `chapter011b.xhtml` | yes | Chapter V: The Primeval Battalion (tiếp) | 182 | 1 |
| 32 | `appendixes.xhtml` | yes | Appendixes: Interior & Exterior Line Strategy / Mapped Outline of History | 0 | 1 |
| 33 | `appendixa.xhtml` | yes | Appendixes: Interior & Exterior Line Strategy / Mapped Outline of History — trang ảnh | 0 | 1 |
| 34 | `appendixb.xhtml` | yes | Appendixes: Interior & Exterior Line Strategy / Mapped Outline of History — trang ảnh | 0 | 1 |
| 35 | `appendixc.xhtml` | yes | Appendixes: Interior & Exterior Line Strategy / Mapped Outline of History — trang ảnh | 0 | 1 |
| 36 | `afterword.xhtml` | yes | Afterword | 14 | 0 |
| 37 | `footnote.xhtml` | yes | Chú thích cuối sách | 20 | 0 |
| 38 | `newsletterSignup.xhtml` | yes | Trang đăng ký bản tin | 3 | 0 |
| **Tổng** | **38 tài liệu** | **37 yes / 1 no** | | **3192** | **47** |

Số p theo nhóm chương: Chapter 0 = 154; I = 364; II = 436; III = 813;
IV = 524; V = 828. Nhóm gồm tất cả tệp tiếp nối và trang ảnh trong khoảng
spine tương ứng. Một chương không tương ứng một tệp XHTML.

## Mục lục và điều hướng

Có cả EPUB 3 NAV (`OEBPS/Text/toc.xhtml`, manifest `properties="nav"`)
và NCX (`OEBPS/toc.ncx`, được spine tham chiếu bằng `toc="ncx"`).

NAV có **13 liên kết TOC**. Nhãn nguyên gốc và đích đã chuẩn hóa tương đối với
`OEBPS/Text/`:

| # | Nhãn | Đích |
| ---: | --- | --- |
| 1 | Cover | `cover.xhtml` |
| 2 | Insert | `insert001.xhtml` |
| 3 | Title Page | `titlepage.xhtml` |
| 4 | Copyright | `copyright.xhtml` |
| 5 | Chapter 0: Prologue | `Prologue.xhtml#Ref_72736` |
| 6 | Chapter I: The Sky over Norden | `chapter002.xhtml#Ref_72739` |
| 7 | Chapter II: The Elinium Type 95 Computation Orb | `chapter004.xhtml` |
| 8 | Chapter III: The Watch/Guard on the Rhine | `chapter006.xhtml#Ref_72745` |
| 9 | Chapter IV: War College | `chapter008.xhtml#Ref_72748` |
| 10 | Chapter V: The Primeval Battalion | `chapter010.xhtml#Ref_72751` |
| 11 | Appendixes: Interior & Exterior Line Strategy / Mapped Outline of History | `appendixes.xhtml#Ref_72742aaa` |
| 12 | Afterword | `afterword.xhtml#aftwrd001` |
| 13 | Yen Newsletter | `newsletterSignup.xhtml` |

NCX có **14 navPoint**, playOrder 1–14: cùng các mục trên, thêm “Table of
Contents” trỏ `Text/toc.xhtml` sau Copyright. Các mục khác có cùng nhãn và đích
sau khi chuẩn hóa. Không liệt kê riêng phần tiếp nối, ảnh xen hoặc footnote.

NAV còn có landmarks: “Begin Reading” đến `insert001.xhtml`, “Table of
Contents” đến `toc.xhtml`. Khối landmarks dùng `hidden-tag` và bị ẩn bằng CSS.
Không có NAV page-list. OPF còn có guide kiểu cũ gồm copyright,
other.ms-firstpage, text, toc, cover; guide type=text trỏ TOC trong khi landmark
Begin Reading trỏ insert001. Dùng spine làm chuẩn thứ tự, NAV/NCX để nhóm chương.

Kiểm tra đích nội bộ của a/img trong 38 XHTML và đích NCX không phát hiện thiếu
tệp hoặc thiếu fragment ID. Không kiểm tra liên kết web.

## Kiểu đánh dấu cấu trúc

- XHTML namespace: `http://www.w3.org/1999/xhtml`; namespace epub:type:
  `http://www.idpf.org/2007/ops`.
- Khung thường dùng body → section → div.galley-rw. Có 38 section; class phổ
  biến là `body-rw Chapter-rw`, cùng các class frontmatter/backmatter.
  epub:type gồm cover, frontmatter titlepage, bodymatter chapter, backmatter
  chapter, backmatter appendix, toc, landmarks, list. Nhãn chương còn được gán
  cho copyright/trang ảnh, nên không đủ để tự quyết định phạm vi dịch.
- Body có **11 h1**: 8 chapter-title (Chapter 0–V, Appendixes, Afterword),
  một copyright-title, hai tiêu đề Contents/Navigation. Có một h3 ở newsletter;
  không có h2/h4–h6 đang dùng. Phần lớn title lặp lại nhan đề tập; title của TOC
  là `a`. Không dùng title làm khóa chương.
- Văn bản dùng p/span, với em/strong/sup và a nội tuyến. Giữ markup và liên kết
  khi dịch; không tách theo span. Trong body không có br/hr/blockquote/table.
- Các class đoạn: noindent (27 p), center5 (26 p), space-break (1),
  space-break1 (67), space-break1a (1), space-break2 (1). CSS space-break điều
  chỉnh khoảng cách đầu đoạn, có thể là dấu chuyển cảnh; cần xét ngữ cảnh.
- chapter001 có hai ol.textindent, gồm 3 và 10 li; mỗi li chứa một p.
  Class nl_f/nl_m/nl_l đánh dấu đầu/giữa/cuối danh sách. Không đếm li và p hai lần.
- Ảnh đặt trong image_full, cover_image, width-90/pc, width-60/pc1. CSS có quy
  tắc ngắt/giữ trang. Có **20 span epub:type=pagebreak** có ID; số trang in
  không phải ranh giới đoạn văn.
- **20 liên kết gọi chú thích** có ID fn0001–fn0020, trỏ đến 20 p.footnote
  có ID fn0001fn–fn0020fn trong footnote.xhtml; mỗi chú thích có liên kết ngược.
  Không thấy epub:type=noteref hoặc footnote; nhận diện bằng href, ID và class.

### Điểm cần lưu ý khi chia đoạn

- Phần lớn p không có ID: chỉ 20 p chú thích và một p newsletter có ID.
- Không có ID trùng trong cùng XHTML. Section ID `chapter003b` lặp giữa
  chapter003a.xhtml và chapter003b.xhtml; ID chỉ có phạm vi tài liệu.
- chapter005b.xhtml có section ID `chapter005c`; footnote.xhtml có section ID
  `Afterword`. Không dùng section ID đơn lẻ để suy ra vai trò/tên tệp.
- h1 Chapter IV có lỗi đánh máy `[chpater]`, như thể hiện trong bảng. Không sửa
  nguồn hoặc nhận diện chương chỉ bằng tiền tố `[chapter]`.
- Trang ảnh và phụ lục ảnh có 0 p; điều này không có nghĩa là thiếu nội dung.
  Chưa OCR hoặc xác định chữ trong ảnh.

## Đề xuất chia đoạn ổn định — chưa triển khai

1. **Khóa phiên bản nguồn:** dùng số tập và SHA-256 EPUB. Danh mục đoạn gắn với
   bản nguồn cố định; thay nguồn phải đối chiếu/ánh xạ có kiểm soát, không âm
   thầm đánh lại mã.
2. **Thứ tự:** theo spine, giữ đường dẫn ZIP chuẩn hóa và phân biệt hoa/thường;
   ghi linear và nhóm chương từ NAV/NCX. Không sắp theo tên tệp, section ID hoặc
   số trang in.
3. **Đơn vị:** một p có văn bản là một đoạn cơ sở, kể cả p trong li; giữ markup
   nội tuyến và ranh giới DOM. Tiêu đề h1–h6 là đơn vị riêng. Chú thích là đơn
   vị riêng theo ID, gắn liên kết gọi/ngược, không nối vào đoạn truyện. Nếu tập
   khác có li với chữ trực tiếp ngoài p, cần đơn vị riêng cho phần đó để tránh
   bỏ sót/đếm đôi.
4. **Mã đề xuất:** `YS-LN01/Text/chapter001.xhtml/p000154`, ordinal p đếm từ 1
   theo DOM tài liệu nguồn đã khóa. Dải riêng cho h000001, img000001 và
   note:fn0001fn. ID nguồn là locator bổ sung, luôn đi kèm đường dẫn.
   Ví dụ này chỉ minh họa hình thức; chưa tạo danh mục đoạn.
5. **Giữ mã sau khi cấp:** không tính mã từ số câu/đoạn bản dịch. Sửa hoặc xuống
   nhiều đoạn trong bản dịch vẫn liên hệ cùng mã nguồn. Nếu cần chia nhỏ đơn vị
   nguồn, thêm hậu tố và nhật ký ánh xạ, không renumber phần còn lại. Ordinal
   ổn định trên bản nguồn cố định, không bảo đảm giữ nguyên khi EPUB thay đổi.
6. **Metadata trong Git:** chỉ số tập, fingerprint, đường dẫn, spine index,
   loại nút, ordinal/DOM path, ID có sẵn, class cần thiết. Không lưu văn bản gốc
   hoặc ảnh. Văn bản làm việc phải đọc tại chỗ hoặc lưu ngoài kho theo quy định
   bảo vệ nguồn.
7. **Ảnh/khoảng ngắt:** ghi vị trí DOM và đường dẫn tài nguyên cho từng lần dùng
   img, không sao chép ảnh hoặc OCR ở bước này. Giữ pagebreak/space-break làm
   metadata; không tách p theo span/pagebreak hoặc gộp p quanh trang ảnh.
8. **Phạm vi:** phân loại truyện, tiêu đề, chú thích, afterword, frontmatter,
   phụ lục ảnh, newsletter trước khi giao dịch. Không mặc định 3.192 p đều là
   truyện; duyệt phạm vi dịch trước khi tách.
9. **Kiểm tra sau này:** phủ đủ 38 tài liệu spine và các đơn vị trong phạm vi đã
   duyệt; kiểm tra mã trùng/thiếu, liên kết chú thích, đếm đôi p trong li. Dùng
   tổng trong báo cáo làm mốc cho bản nguồn này, không áp sang tập khác.

## Giới hạn

Đây là kiểm tra XML/ZIP tại chỗ, không phải EPUBCheck hoặc thử hiển thị trên
thiết bị đọc. Chưa phân tích sâu LN 02–LN 14, OCR ảnh, chốt thuật ngữ, tách nội
dung hoặc xây công cụ xử lý EPUB.
