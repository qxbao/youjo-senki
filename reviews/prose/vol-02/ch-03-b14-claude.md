# Báo cáo review vol-02-ch-03-b14 (Claude)

- Task: `vol-02-ch-03-b14`, checkpoint_generation 591, 29 đoạn từ `YS-LN02/Text/part0018.xhtml/p000162` đến `p000190`.
- Đầu vào: source package `work/vol-02/batches/ch-03-b14-source.jsonl` có SHA-256 khớp handoff (`0e7290dc…ae4c`). Bản dịch `translations/vol-02/ch-03-b14.jsonl` có đủ 29 đoạn, mã đoạn khớp. Đã đối chiếu `canon/` (style-guide, decisions DEC-P01-001/002, glossary-pending) và `work/run-state/pending-terms.yml`.
- Không trích câu nguồn. ID đoạn viết tắt `pNNNNNN`.
- Lưu ý quy trình: để kiểm tra nhất quán thuật ngữ, reviewer có chạy một lệnh grep đếm cách dịch "Tiểu đoàn Pháp sư…" và "cầu tính toán" trên các bản dịch b10–b13, chỉ để đếm, không đọc nội dung hay đánh giá các lô đó.

## Tổng quan

Bản dịch bám sát nghĩa, đủ ý, không thấy đoạn bị bỏ hay thêm nội dung lớn. Logic giả định ở p000183–p000185 và p000188 được giữ. Giọng nội tâm "mình" và trần thuật "nó" nhìn chung theo DEC-P01-001. Dấu nhấn mạnh ở p000162 được giữ đúng hai cụm. Vấn đề chính: một lỗi xưng hô sai người nói (p000181), một cách gọi gây hiểu nhầm giới tính đơn vị (p000177), thuật ngữ lệch sổ pending (đổ bộ / đường không), thiếu một dấu nhấn mạnh (p000165) và một đại từ "mình" mơ hồ (p000189).

Số lượng: nghiêm trọng 0, vừa 6, nhẹ 14.

## Mức vừa

**V1. p000181: sai xưng hô.** Đoạn này là lời viên sĩ quan hỏi lại Tanya sau đề nghị ở p000178; Tanya trả lời ở p000182 và viên sĩ quan nói tiếp ở p000186. Bản dịch dùng "anh" gọi người đối diện, nhưng cùng người nói này gọi Tanya là "cô" ở p000171, p000177 và p000186. Căn cứ: thứ tự lượt thoại và tính nhất quán trong lô. Đề xuất: đổi thành "Ý cô là sao?" (vẫn là đề xuất xưng hô, chưa canon).

**V2. p000177: "các cô" gán giới tính cho cả đơn vị.** "You" ở đây chỉ đơn vị/đội hình của Tanya, không phải riêng một người nữ. "Các cô" làm cả tiểu đoàn thành nữ và không có căn cứ (DEC-P01-001: không suy diễn). Đề xuất: "tăng viện cho đơn vị của cô" hoặc "tăng viện cho các cô" chỉ khi coordinator chốt. Cũng ở đoạn này, "sau khi các cô đổ bộ" là cách gọi nhảy dù, xem V3.

**V3. p000162, p000163, p000166, p000177: "đổ bộ" dùng cho chiến dịch đường không.** Sổ pending (`vol02-ch03-b08-airborne-amphibious`) ghi phải phân biệt airborne với amphibious và không dùng "đổ bộ" cho cả hai. Bản dịch dịch chiến dịch đường không là "chiến dịch đổ bộ đường không" (p000162, p000166), "chiến dịch đổ bộ của chúng ta" (p000163) và "sau khi các cô đổ bộ" (p000177). Với hạm đội, hải quân và lính thủy đánh bộ trong cùng cảnh, "đổ bộ" dễ gây hiểu thành đổ bộ đường biển. Đề xuất: "chiến dịch đột kích đường không" hoặc "chiến dịch nhảy dù"; p000177 dùng "sau khi các cô nhảy dù ba mươi phút" hoặc "ba mươi phút sau khi nhảy dù". Chỉ là đề xuất tạm.

**V4. p000165: bỏ nhấn mạnh.** Nguồn có nhấn mạnh ở cụm chỉ mệnh lệnh "vào đó". Bản dịch không có `*...*`, trái DEC-P01-002 và checkpoint emphasis. Đề xuất: "Ra lệnh cho người khác *xông vào* thì dễ…".

**V5. p000189: "mình" mơ hồ.** Câu có chủ ngữ "ông ấy", rồi "những điều mình nói". Người đọc dễ hiểu "mình" là chính ông ấy, trong khi đó là lời Tanya. Đề xuất: "những điều tôi/nó đã nói" hoặc "những gì mình vừa trình bày", đặt chủ ngữ rõ hơn (ví dụ "những lời của mình" đặt trước chủ ngữ).

**V6. p000170, p000162: "Pháp sư Đường không" lệch sổ pending.** Sổ ghi "pháp sư không quân" (`b06-aerial-mage`, `vol02-ch01-b04-aerial-mage`) và "Tiểu đoàn Pháp sư Không quân 203" hoặc "…số 203" (`vol02-ch03-b06-aerial-mage-battalion`). Bản dịch dùng "pháp sư đường không" (p000162) và "Tiểu đoàn Pháp sư Đường không số 203" (p000170), làm tên đơn vị lặp lại lệch phiên bản đang dùng. Đề xuất: "Tiểu đoàn Pháp sư Không quân số 203" và "pháp sư không quân", hoặc ghi rõ nếu muốn đổi cả chương thì cập nhật sổ pending.

## Mức nhẹ

- N1. p000162: "ra lệnh cho nó…, Tanya" đặt đại từ trước tên, dễ vấp. Đề xuất đặt tên trước hoặc đổi "cho nó" thành "cho Tanya".
- N2. p000162: "tiến sâu vào vịnh hẹp" thêm ý "sâu"; nguồn chỉ chạy dọc vịnh. Đề xuất "tiến dọc vịnh hẹp".
- N3. p000162: "hậu tuyến" so với sổ ("hậu phương", "tuyến sau"). Đề xuất "tuyến sau" cho khớp.
- N4. p000163: "cầu tàu" (bến) không khớp "gangway" (cầu thang lên xuống tàu). Đề xuất "cầu thang tàu" hoặc "ván cầu".
- N5. p000163: "cầu tính toán" lệch sổ ("quả cầu tính toán"). Đề xuất theo sổ.
- N6. p000166: "nhu cầu quân sự của nó" trong khi "nó" đang là Tanya ở trần thuật, nhưng ở đây chỉ chiến dịch. Đề xuất "nhu cầu quân sự của chiến dịch".
- N7. p000170: "Trớ trêu thay" mất sắc thái bực bội của "annoyingly". Đề xuất "Đáng bực thay".
- N8. p000172: "xin phép… được không" thừa lớp lịch sự. Đề xuất "Tôi xin phép nói đôi lời được không?".
- N9. p000176: "ngụy biện" mang sắc thái đạo đức mạnh hơn "excuse" (lời bào chữa); "chèn ép" lệch "smash" (đè bẹp). Đề xuất "lời bào chữa" và "đè bẹp".
- N10. p000179: "nó" cuối câu (chỉ yêu cầu) đứng gần "nó" chỉ Tanya; "che đậy yêu cầu" dễ hiểu thành giấu yêu cầu. Đề xuất đổi "nó sẽ" thành "yêu cầu ấy sẽ" và "khéo léo gói yêu cầu".
- N11. p000184, p000190: "ta" xen với "chúng ta" ở cùng người nói. Đề xuất thống nhất "chúng ta" hoặc "chúng tôi".
- N12. p000185: "việc mình đã đề nghị" làm mất ý "hồ sơ ghi nhận". Đề xuất "việc đề nghị ấy được ghi nhận".
- N13. p000188: "cuộc xung phong cưỡng ép" hơi lạ. Đề xuất "đợt xung phong bất chấp" hoặc "cuộc tấn công cưỡng ép".
- N14. p000187, p000189: "ông ấy" gán độ tuổi khi chưa có căn cứ về người nói. Đề xuất giữ tạm, ghi pending, xem phần đề xuất thuật ngữ.

## Kiểm tra theo checkpoint

- Meaning: các câu hỏi p000168, p000178, p000182–p000183 giữ đúng đối tượng; thời gian giả định ổn. Không thấy bỏ/thêm đoạn lớn. Chỗ mất nghĩa nhỏ: N12.
- Pronouns: V1, V2, V5 và các mục N liên quan.
- Emphasis: V4; p000162 đúng.
- Pending terms: V3, V6, N3, N5.

## Đề xuất thuật ngữ (đều là đề xuất, chưa canon)

- Aerial Mage Battalion: giữ "Tiểu đoàn Pháp sư Không quân số 203", theo sổ hiện có (p000170).
- airborne operation / drop: "chiến dịch đột kích đường không", "nhảy dù"; không dùng "đổ bộ" (p000162, p000163, p000166, p000177).
- marines (lính thủy đánh bộ) và marine mages (pháp sư hải quân): đề xuất mới, chưa có mục trong sổ (p000166, p000177).
- fjord: "vịnh hẹp" (p000162, p000168), đề xuất mới.
- computation orb: "quả cầu tính toán" (p000163).
- vanguard: "đội tiên phong" (p000171), khớp sổ `vol02-ch02-b19-vanguard`.
- Commonwealth: "Khối Thịnh vượng chung" (p000190), khớp sổ. Republican: "phe Cộng hòa", chưa có mục riêng cho ngữ cảnh này.
- Xưng hô: viên sĩ quan gọi Tanya là "cô" (p000171, p000177, p000181, p000186), Tanya nói "tôi"; người nói chưa rõ danh tính, không dùng "ông ấy" ở ngoài trần thuật nội tâm cho đến khi có căn cứ. Không ảnh hưởng cốt truyện cần hỏi người dùng.

## Kết luận

Cần sửa các mục V1–V6 trước khi coi lô hoàn tất. Không có lỗi nghiêm trọng và không có quyết định ảnh hưởng cốt truyện cần hỏi người dùng.
