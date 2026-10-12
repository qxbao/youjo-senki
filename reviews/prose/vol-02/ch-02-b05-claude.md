# Báo cáo phản biện văn phong và ngữ nghĩa — vol-02-ch-02-b05-review (batch lẻ, có cờ risk_flags + new_pending_terms)

- **Người phản biện:** Claude (reviewer; chỉ ghi báo cáo này, không sửa bản dịch, handoff, canon, ledger hay run-state). Báo cáo không trích văn bản nguồn.
- **Phạm vi:** 25 đoạn p000093–p000117 (`YS-LN02/Text/part0014.xhtml/…`, viết tắt `pNNNNNN`). Đã đọc: `agents/reviewer.md`, `agents/shared.md`, `config/translation-pipeline.yml`, handoff b05, gói nguồn b05, bản dịch b05, `canon/*`, các mục liên quan trong `work/run-state/pending-terms.yml` (mục `chapter2_b05_translation_proposals` và các mục tiền lệ: Central/Northern Command, army group, quân hàm Serebryakov/Weiss, phó chỉ huy, xưng hô Tanya, General Staff). Không đọc bản dịch của batch khác.

## 1. Kết luận

- **Kết luận:** `pass_with_fixes`.
- **Mức nghiêm trọng:** serious = 0; moderate = 7 (M1–M7); minor = 11 (m1–m11).
- **next_action:** người giữ quyền sửa xử lý M1–M7, cân nhắc minor, chạy lại validator + `git diff --check`, rồi commit. Cần reviewer xác nhận nhanh p000093, p000096, p000100, p000101, p000108, p000109, p000112, p000117 sau khi sửa.

## 2. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự ID | Đạt: 25 đoạn p000093–p000117, đúng thứ tự, khớp 1:1 với gói nguồn. |
| Hash gói nguồn | Đạt: `1c6b416e…cf392` khớp handoff. |
| `source_sha256` mỗi record | Đạt: khớp handoff. |
| `glossary_version` | Đạt: khớp handoff (`d5f19d64…`). |
| `status` / `notes` | `draft` toàn bộ; `notes` rỗng; không có ghi chú làm việc lọt vào translation. |
| Nhấn mạnh (DEC-P01-002) | Đạt: nguồn có nhấn mạnh ở p000108 (1 cụm) và p000116 (2 cụm); bản dịch có đúng 1 và 2 cụm `*…*`, đúng phạm vi. Không đánh dấu thừa ở đoạn khác. |
| Định dạng thoại | Đạt: số dấu ngoặc kép khớp nguồn ở mọi đoạn; p000097 giữ cấu trúc ngoặc lặp ba lớp như nguồn; cụm trích dẫn nội tâm ở p000108 giữ ngoặc kép. |
| Phủ định / logic | Không phát hiện đảo nghĩa hay mất phủ định. |
| Người nói | Đạt: các lời thoại p000093, p000095, p000102, p000104, p000107, p000109, p000112 đều là lời Weiss/Tanya đúng như nguồn; không lẫn chủ thể giữa thoại và nội tâm. |

## 3. Phát hiện moderate

**M1 — p000093: “tuyến nội bộ” làm sai thuật ngữ quân sự (đề xuất 1).**
- Vấn đề: “interior lines” là khái niệm chiến lược (lực lượng nằm bên trong vòng cung của địch, cơ động nhanh giữa các hướng). “Tuyến nội bộ” đọc như “tuyến đường nội bộ/ nội bộ đơn vị”, mất nghĩa và không tìm được cách dùng tương ứng trong văn quân sự tiếng Việt. Cụm “cơ động qua lại” thì tốt.
- Đề xuất: “liên tục cơ động qua lại theo nội tuyến” (thuật ngữ “nội tuyến”/“tác chiến theo nội tuyến” có trong văn quân sự). Nếu muốn dễ hiểu hơn: “theo các tuyến nội tuyến” (ít tự nhiên, không khuyến nghị).

**M2 — p000096: “cô ấy” trong nội tâm tự quy chiếu.**
- Vấn đề: đoạn là suy nghĩ của Tanya (chủ ngữ “mình”), nhưng vế cuối dùng “binh lính của cô ấy”, đọc như một người thứ ba và đồng thời gán giới tính/xưng hô mà ledger `vol02-ch01-b05-tanya-narration` yêu cầu tránh. Nguồn dùng ngôi thứ ba ở chỗ này nhưng trong nội tâm nên không cần phơi bày đại từ.
- Đề xuất: “binh lính dưới quyền mình” hoặc “binh lính của Tanya”; không dùng “cô ấy”.

**M3 — p000101: “cô” cho Tanya trong trần thuật (hai lần).**
- Vấn đề: DEC-P01-001 dùng “nó” cho trần thuật về Tanya ở giai đoạn pilot và cấm mở rộng sang giai đoạn khác; ledger Vol 2 (`vol02-ch01-b05-tanya-narration`) chọn “lặp tên Tanya hoặc lược chủ ngữ”, thay thế “nó/cô” chỉ ở mức đề xuất. Bản dịch dùng “nhìn cô”, “Cô cho anh biết” trái lựa chọn tạm đó, trong khi các đoạn khác của batch (p000094, p000113) lặp tên/lược chủ ngữ.
- Đề xuất: “…ra hiệu với Weiss, người đang nhìn Tanya đầy thắc mắc. Tanya cho Weiss biết không có gì đáng lo và bảo anh nói tiếp.” (hoặc lược chủ ngữ: “Báo cho anh biết…”). Coordinator nên kiểm tra tính nhất quán với các batch khác; reviewer không đọc batch khác.

**M4 — p000108: “cô” trong lời tưởng tượng gọi Tanya.**
- Vấn đề: lời tưởng tượng của “họ” gọi Tanya bằng “cô”, tức một xưng hô giới tính hóa do người dịch thêm vào, trái ghi chú ledger (“không dùng kính ngữ gắn giới tính”, phương án trung tính “thưa Thiếu tá”). Nguồn không có đại từ ở vế này.
- Đề xuất: lược đại từ: “Chúng tôi đang hỗ trợ rồi đấy, vậy bắt tay vào làm đi!”; phương án thay thế: “…hỗ trợ Thiếu tá…”. Giữ nguyên phạm vi `*…*`.

**M5 — p000100: “lương hưu công chức và sĩ quan được ủy nhiệm” (đề xuất 2).**
- Vấn đề: (a) nguồn nói hai khoản lương hưu (số nhiều), bản dịch gộp thành một cụm “lương hưu công chức và sĩ quan…” dễ hiểu là một khoản lương hưu cho nhóm hai đối tượng; (b) “sĩ quan được ủy nhiệm” là calque “commissioned officer”, trong tiếng Việt “sĩ quan” đã là cấp có quân hàm được phong; “được ủy nhiệm” gợi nghĩa “được giao/ủy quyền”. Phương án thay thế của translator (“sĩ quan chuyên nghiệp”) đổi nghĩa (chuyên nghiệp ≠ commissioned) nên không khuyến nghị.
- Đề xuất: “lương hưu công chức lẫn lương hưu sĩ quan” (có thể thêm “có quân hàm” nếu cần phân biệt với hạ sĩ quan, không bắt buộc).

**M6 — p000109, p000112: tên Bộ Chỉ huy miền Bắc / miền Trung (đề xuất 3).**
- Vấn đề: (a) “Central” trong nguồn đứng một mình (“dispatched from Central”), bản dịch tự thêm “Bộ Chỉ huy” và thành “miền Trung”, suy ra một bộ chỉ huy vùng; nhưng ngữ cảnh p000114 nhấn mạnh đơn vị thuộc Bộ Tổng tham mưu, nên “Central” nhiều khả năng là trung ương, không chắc là một bộ chỉ huy ngang hàng với Northern; (b) “miền Bắc/miền Trung” có sắc thái địa lý Việt Nam và không khớp “phía Đông/phía Nam” trong cùng câu; (c) lệch tiền lệ ledger (`vol02-ch01-b16-northern-command`: “Bộ chỉ huy phương Bắc”; `b05-central-command`: giữ “Central”).
- Đề xuất (xem mục 4): “Bộ Chỉ huy phương Bắc” và “do Trung ương điều đi”; p000112 đổi “ở miền Bắc” thành “ở phía Bắc”.

**M7 — p000117: “kẻ gia trưởng” thêm sắc thái miệt thị.**
- Vấn đề: style-guide cấm thêm sắc thái phán xét/miệt thị. “Kẻ” khiến cụm đậm tính chửi rủa hơn nguồn; “gia trưởng” trong tiếng Việt thường gắn với gia trưởng/độc đoán kiểu gia đình, thu hẹp nghĩa “paternalism” (can thiệp “vì lợi ích của bạn”).
- Đề xuất: “sự thương hại của những người theo chủ nghĩa gia trưởng…” hoặc “…của những kẻ bề trên thích bao bọc”. Khuyến nghị bản đầu (trung tính, bám nghĩa). Đây là thuật ngữ mới ngoài năm đề xuất; ghi vào ledger với confidence thấp (0.5).

## 4. Đánh giá năm đề xuất của translator (lựa chọn tạm, không nâng canon)

| # | Cụm nguồn | Lựa chọn tạm | Thay thế | Lý do | Độ tin cậy | Đoạn |
|---|---|---|---|---|---|---|
| 1 | interior lines | **nội tuyến** (“theo nội tuyến”) | tuyến nội bộ (đề xuất gốc, bác bỏ); đường nội tuyến | Thuật ngữ quân sự đúng; “nội bộ” làm lệch nghĩa. Giữ chỗ cho dị bản nếu về sau có thuật ngữ chuẩn hơn. | 0.6 | p000093 |
| 2 | civil servant and commissioned officer pensions | **lương hưu công chức lẫn lương hưu sĩ quan** | lương hưu công chức và lương hưu sĩ quan có quân hàm; (bác “sĩ quan chuyên nghiệp”) | Giữ số nhiều (hai khoản), bỏ calque “được ủy nhiệm”. | 0.6 | p000100 |
| 3 | Northern Command / Central Command | **Bộ Chỉ huy phương Bắc**; “Central” → **Trung ương** (không thêm “Bộ Chỉ huy”) | Bộ Chỉ huy phía Bắc (nếu muốn khớp “phía Đông/phía Nam”, cần cập nhật ledger b16); Bộ Tư lệnh Trung ương (tiền lệ b05 Vol 1) | Khớp ledger b16; tránh “miền” (gợi địa danh) và tránh phát minh tên bộ chỉ huy vùng. Nếu cốt truyện sau xác nhận Central là bộ chỉ huy riêng, đổi thành “Bộ Chỉ huy Trung ương”. Viết hoa “Chỉ huy” cần thống nhất với ledger b16 (thường). | 0.5 | p000109, p000112 |
| 4 | political dignity | **phẩm giá chính trị** (giữ) | thể diện chính trị | Giữ lặp từ với “phẩm giá con người” ở p000108 (cùng gốc “dignity”) và đối trọng “danh dự” ở p000111. “Thể diện” nghe tự nhiên hơn nhưng nghiêng về nghĩa “giữ mặt”, chưa chắc có trong nguồn. | 0.5 | p000110 |
| 5 | animal protection groups | **hội bảo vệ động vật** (giữ) | các tổ chức bảo vệ động vật | Câu tiếp theo dùng “tổ chức” khi quy chiếu lại (p000116), tạo biến thể tự nhiên; “hội” hợp với “vô số”. | 0.6 | p000116 |

Không có đề xuất nào cần hỏi người dùng (không ảnh hưởng cốt truyện). Chưa xác nhận được nghĩa của “Central” từ nguồn đoạn này; nếu chưa rõ, giữ “Trung ương” trung tính (nghĩa rộng nhất, ít suy diễn nhất).

## 5. Phát hiện minor

- **m1 — p000099:** “who might be even slightly useful” → “chỉ cần có chút hữu dụng” mất sắc thái “có thể” và biến thành điều kiện. Đề xuất: “có thể hữu dụng dù chỉ chút ít”.
- **m2 — p000099:** “phần nhiều cũng vì lý do tương tự” (nguồn: gần như cùng lý do) làm yếu thành “một phần lớn”, lại lặp “cũng”. Đề xuất: “cũng vì lý do gần như tương tự”.
- **m3 — p000103:** “quát” mang nghĩa mắng; nguồn là hô khẩu lệnh. Đề xuất: “hô”.
- **m4 — p000106:** “anh ta” trong nội tâm lệch với “anh” ở p000105 (cùng người, cùng mạch). Đề xuất thống nhất “anh”.
- **m5 — p000108:** “thuần hóa” thay cho từ trích dẫn trong nguồn (nghĩa gốc là “được vun/nuôi dưỡng”) đưa vào khung “thuần hóa động vật” không có trong nguồn. Đề xuất: “được ‘nuôi dưỡng’” hoặc “được ‘bồi dưỡng’”; độ chắc thấp vì chưa đối chiếu gốc tiếng Nhật.
- **m6 — p000109:** viết hoa “Cụm Tập đoàn quân phía Đông/Nam” lệch ledger (`Cụm tập đoàn quân phía Đông`) và lệch cách viết thường ở p000114. Đề xuất viết thường “tập đoàn quân” nếu tên không phải riêng, hoặc thống nhất một kiểu.
- **m7 — p000110:** “đã phơi bày” khẳng định quá mức so với “Perhaps … show”; “hợp lý” hơi lệch “logic”. Đề xuất: “có lẽ cho thấy rõ giới hạn của nó” / “một cách logic”.
- **m8 — p000110, p000116:** “loài vật chính trị” có thể đổi thành “động vật chính trị” (cách dịch quen thuộc của câu Aristotle) để giữ trò chơi chữ với “động vật” ở p000116. Cả hai chỗ phải đồng bộ.
- **m9 — p000111:** “không biết danh dự” khiến câu sau (chưa xác nhận động vật có hiểu khái niệm hay không) dư/vòng. Đề xuất: “không có danh dự”.
- **m10 — p000114:** “các đạo quân khu vực” lệch ledger (army = tập đoàn quân). Đề xuất: “các tập đoàn quân khu vực”.
- **m11 — p000116:** (a) ký hiệu chú thích “⁵” là ký tự Unicode; chưa có quyết định trong `decisions.md` về cách biểu diễn chú thích (style-guide yêu cầu ghi trước khi áp dụng thống nhất), cần coordinator xác nhận quy ước chung; (b) “của các người” gắt hơn nguồn; đề xuất “của các bạn” hoặc “của các người” chỉ nếu giọng khẩu hiệu giận dữ được xác nhận.

## 6. Điểm tốt đáng giữ

- Phép ẩn dụ ngựa/cà rốt nhất quán (ngựa kéo → ngựa đua → ngựa cày → ngựa giống → ngựa thồ) ở p000095–p000108; giữ đúng độ mỉa mai.
- Đại từ thoại Weiss/Tanya và thứ bậc Trung úy Weiss, “phó chỉ huy” khớp ledger.
- Phạm vi nhấn mạnh `*…*` đúng DEC-P01-002.

## 7. Rủi ro

- Nhiều lựa chọn thuật ngữ (nội tuyến, Trung ương, lương hưu) độ tin cậy 0.5–0.6; có thể đổi khi canon chốt, cần đồng bộ mọi chỗ xuất hiện.
- Xưng hô Tanya (“nó/cô/lược”) chưa nhất quán xuyên batch; chưa kiểm tra batch khác theo phạm vi.
- Quy ước chú thích “⁵” chưa có quyết định chuẩn.
- Chưa đối chiếu nguồn gốc tiếng Nhật; một số nghi vấn (m5, “Central”) dựa vào ngữ cảnh.

## 8. Kết quả theo mẫu reviewer

- `validator`: not_run; `diff_check`: not_run; `commit`: null.
