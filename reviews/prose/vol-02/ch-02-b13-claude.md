# Review b13 — vol-02-ch-02-b13-review

- **Người phản biện:** Claude (chỉ ghi báo cáo này; không sửa bản dịch, handoff, canon, ledger hay run-state). Không trích câu nguồn.
- **Phạm vi:** 25 đoạn `YS-LN02/Text/part0014.xhtml/p000329`–`p000353` (viết tắt `pNNNNNN`). Đã đọc: handoff b13, gói nguồn đã chuẩn bị, `translations/vol-02/ch-02-b13.jsonl`, `canon/` (glossary, characters, style-guide, decisions, glossary-pending) và `work/run-state/pending-terms.yml` (mục `chapter2_b13_translation_proposals` cùng các mục liên quan: Named, Commonwealth, Entente, augmented battalion, đại từ). Không đọc batch dịch khác.
- **Kiểm tra cơ học:** 25/25 đoạn; thứ tự p000329→p000353 liên tục; `segment_id`, `source_sha256`, `glossary_version` khớp; `notes` rỗng; status `draft`. Chữ nghiêng (DEC-P01-002): nguồn chỉ nhấn mạnh ở p000345 (cụm "một trận đánh cam go"); bản dịch có `*...*` đúng chỗ và đúng phạm vi. Dấu ngoặc thoại đóng/mở cân. Không thấy bản dịch xuất bản bị lẫn ghi chú làm việc.

## Kết luận: `needs_fixes` (serious 0, moderate 4, minor 12)

Nghĩa, phủ định và logic nhìn chung được giữ tốt (đặc biệt p000334, p000339, p000342 giữ đúng tính giả định/phản thực tế; p000345 giữ đúng phạm vi nhấn mạnh). Bốn lỗi moderate đều sửa nhanh, không có hard stop và không ảnh hưởng cốt truyện.

## Moderate

### MOD-1 — p000335, p000341, p000342: đại từ/cách gọi Named không nhất quán, thêm sắc thái miệt thị
- **Vấn đề:** cùng một chủ thể (Named, nguồn dùng đại từ nữ) được gọi "nó" (p000335), "con Named đó" (p000341) rồi "cô ta" (p000342). Ba cách gọi cho ba sắc thái khác nhau. "con" trước Named và "nó" mang sắc thái coi thường/vật hóa mà nguồn không có (chỉ có chữ chửi "bastard" ở p000341, đã dịch "tên khốn"). DEC-P01-001 chỉ duyệt "nó" cho trần thuật về Tanya và dặn không mở rộng sang chủ thể khác; đoạn này là điểm nhìn phía Thịnh vượng chung, chưa nêu danh tính.
- **Đề xuất:** thống nhất một cách. Phương án khuyến nghị: "Named đó/này" làm danh từ, và đại từ "cô ta" (hoặc "cô ấy") khi nguồn dùng đại từ; bỏ "con" và bỏ "nó". Không suy diễn danh tính Tanya. Phương án thay thế: lặp "Named đó" thay đại từ ở p000335 ("nhưng Named ấy có thật").
- **Độ tin cậy:** 0,6.

### MOD-2 — p000330: mất quan hệ nhân quả "vì… nên…"
- **Vấn đề:** nguồn là mệnh đề nguyên nhân ("vì Khối Thịnh vượng chung mong họ tích lũy kinh nghiệm… nên, xét từ góc độ quốc phòng, nó đối đãi chu đáo và trang bị tốt cho nhân sự"). Bản dịch ngắt bằng dấu chấm phẩy và thêm "quả thật", làm quan hệ nguyên nhân–hệ quả thành hai nhận định song song. Style guide: không đổi quan hệ nguyên nhân–hệ quả.
- **Đề xuất:** "Vì Khối Thịnh vượng chung mong họ tích lũy đủ loại kinh nghiệm và học hỏi được nhiều trong chiến đấu, nên xét từ góc độ quốc phòng, nước này rất chu đáo với nhân sự của mình và đã trang bị cho họ đầy đủ."
- **Độ tin cậy:** 0,65.

### MOD-3 — p000338: lời thoại bị thu hẹp thành một diễn giải ("chỉ một nửa là đúng")
- **Vấn đề:** nguồn là "nên chuẩn bị cho khoảng một nửa những gì đã nghe", mơ hồ giữa (a) chấp nhận khoảng một nửa là thật và (b) chuẩn bị đối mặt với mức độ bằng khoảng một nửa. Bản dịch chọn (a) và thêm "chỉ", biến thành nhận định về độ xác thực. Ngữ cảnh p000340 ("dù mọi lời đồn có bị phóng đại") nghiêng về (a), nhưng nguồn không nói "đúng/sai".
- **Đề xuất:** giữ trung lập: "…Có lẽ chúng ta nên chuẩn bị tinh thần cho khoảng một nửa những gì đã nghe." Nếu coordinator chọn (a) thì bỏ "chỉ": "…nên chuẩn bị tinh thần rằng khoảng một nửa những gì nghe được là đúng."
- **Độ tin cậy:** 0,5. Ghi vào pending (không chắc).

### MOD-4 — p000329 (thuật ngữ mới 1): "cựu binh" xung đột với "chưa có kinh nghiệm chiến đấu" ở p000333/p000336
- **Vấn đề:** "cựu binh" nghĩa gốc là lính đã giải ngũ/từng chiến đấu; còn "dày dạn" là thêm. Nguồn chỉ là nhóm lão luyện trong công tác thu thập tình báo. Hai đoạn sau nhấn mạnh họ thiếu kinh nghiệm chiến đấu, nên "cựu binh" gây mâu thuẫn nghĩa.
- **Đề xuất:** xem phần pending_term_choices.
- **Độ tin cậy:** 0,55.

## Minor

- **m1 — p000329:** "với mục tiêu chuẩn bị cho…" hơi nặng hơn "với tầm nhìn tới/hướng tới trận chiến sau này"; đề xuất "hướng đến cuộc chiến sắp tới với Đế quốc". Độ tin cậy 0,4.
- **m2 — p000331/p000332:** "nhỉ", "đấy" thêm giọng thân mật; chấp nhận được vì thoại miệng, không suy ra quan hệ giữa người nói (DEC-P01-001). Không cần sửa.
- **m3 — p000335:** "trật lất" quá khẩu ngữ so với giọng trần thuật; đề xuất "đã chệch hướng/trượt mục tiêu". Độ tin cậy 0,4.
- **m4 — p000336:** "đáng lo ngại" cho "vexing" (gây phiền/bực), trong khi câu sau dùng "bực bội". Đề xuất "đáng bực" hoặc "đáng phiền". Độ tin cậy 0,4.
- **m5 — p000337:** "trực giác thiết yếu" hơi thu hẹp "sense" (cảm quan/độ nhạy); đề xuất "cảm quan thiết yếu ấy". Độ tin cậy 0,35.
- **m6 — p000340:** "nhận ra" cho "sensed" khẳng định hơn "cảm nhận được"; "lời đồn" cho các câu chuyện nghe lại hơi nghiêng về tin đồn, trong khi p000338 là "những gì nghe được". Đề xuất "cảm nhận được" và "những lời kể/thông tin nghe lại". Độ tin cậy 0,4.
- **m7 — p000341:** "Thì sao nếu…" đọc thành "nếu như thì sao" (lo ngại), trong khi nguồn là nhượng bộ giả định mang giọng bác bỏ. Đề xuất "Cứ cho là con Named đó có thể thổi bay nguyên một đại đội trong chớp mắt đi, thì nó cũng đâu thể xử nổi hai tiểu đoàn, đúng không?" (kết hợp MOD-1). Độ tin cậy 0,5.
- **m8 — p000345:** nên cân nhắc đổi "khiến … phải chật vật giao chiến" cho gọn; ý đúng. Chỉ nhắc kiểm tra tính liền mạch của câu "ngược lại" (ý: kịch bản xấu nhất cũng chỉ là trận đánh cam go). Hiện đúng nghĩa, không cần sửa. Độ tin cậy 0,3.
- **m9 — p000348:** hai cặp gạch ngang lồng nhau ("Cộng hòa — … — cùng Khối Thịnh vượng chung — … —") khó đọc; "nơi Liên minh Entente từng phải van nài" làm "Cộng hòa" thành nơi chốn và thêm "phải". Đề xuất dùng ngoặc hoặc tách câu: "Cộng hòa (bên mà Liên minh Entente từng cầu cứu, nay chính họ lại đang xin giúp đỡ) và Khối Thịnh vượng chung (vốn thu thập tình báo với tâm thế hướng đến cuộc chiến với Đế quốc) đã trở nên rất lệch nhịp." Độ tin cậy 0,55.
- **m10 — p000351:** "sẽ nói xấu" thành thì tương lai; nguồn là thói quen quá khứ. Đề xuất "thường nói xấu". "Lời chê bai" cho "insults" nhẹ hơn; cân nhắc "lời xúc phạm". Độ tin cậy 0,45.
- **m11 — p000353:** "chưa lúc nào muốn" yếu hơn "không một khoảnh khắc nào muốn"; đề xuất "chẳng giây phút nào muốn". Độ tin cậy 0,35.
- **m12 — p000342/p000347/p000353:** "Named" giữ nguyên, nhất quán với ledger ("Named (retain provisionally)"); "Khối Thịnh vượng chung", "Liên minh Entente", "tiểu đoàn tăng cường" khớp ledger. Không có vấn đề. "tình báo họ không thể chia sẻ" ở p000347 hơi cụt; đề xuất "thông tin tình báo mà họ không thể chia sẻ". Độ tin cậy 0,3.

## Kiểm tra theo hạng mục
- **Phủ định:** p000333, p000337, p000343, p000353 đúng. Không đảo nghĩa.
- **Người nói/đại từ:** thoại p000331, p000332, p000338, p000341, p000343, p000344, p000346, p000349, p000352 là các sĩ quan Thịnh vượng chung (hoặc liên quân), không rõ từng người nói; bản dịch dùng "tôi/chúng ta" trung tính, không suy ra cấp bậc. Chấp nhận. Riêng cách gọi Named xem MOD-1.
- **Nhấn mạnh:** chỉ p000345; khớp.
- **Thứ tự và định dạng:** đúng; không dư/thiếu đoạn.

## Pending term (đề xuất, không phải canon)

Xem YAML trả về: `pending_term_choices`.
