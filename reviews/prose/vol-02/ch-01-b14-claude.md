# Báo cáo phản biện — vol-02-ch-01-b14

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon).
- Phạm vi: `p000001`–`p000018` (18 đoạn) của `YS-LN02/Text/part0012.xhtml`; gồm handoff b14, gói nguồn cục bộ, `translations/vol-02/ch-01-b14.jsonl`, canon và sổ pending.
- Kích hoạt: `new_pending_terms`.
- Báo cáo không trích câu nguồn. Thuật ngữ nguyên gốc ngắn và mã đoạn chỉ dùng để nhận diện. Mọi lựa chọn dưới đây là đề xuất tạm, không phải canon, không nâng lên canon.
- Mã đoạn viết tắt `pNNNNNN` = `YS-LN02/Text/part0012.xhtml/pNNNNNN`.

## 1. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự | 18/18, liên tục p000001→p000018, khớp 1–1 giữa nguồn và bản dịch |
| Hash gói nguồn | `af9b1c44…d7332` khớp `source_package_sha256`; `source_sha256` mọi đoạn khớp `3ac53161…` |
| Hash canon (5 tệp) | Khớp handoff (glossary, style-guide, characters, decisions, glossary-pending) |
| Trường bản dịch | `status: draft`, `glossary_version` khớp, `notes` rỗng ở cả 18 đoạn |
| Nhấn mạnh (DEC-P01-002) | Nguồn không có in nghiêng/nhấn mạnh ở đoạn nào; bản dịch không có `*…*`. Đúng. |
| Chú thích | Không có ở nguồn lẫn bản dịch |
| Đại từ Tanya (DEC-P01-001) | Trần thuật dùng "cô" ở p000003, p000005. Xem M1. |
| Phủ định / logic | Các cấu trúc phủ định ở p000002, 009, 012, 013 giữ đúng ("không hẳn… cũng chẳng hẳn", "không thể phủ nhận", "Đừng bận tâm"). |
| Ranh giới đoạn / người nói | Lời thoại p000013 → trần thuật p000014 ("đáp lời") nối đúng; p000017, p000018 luân phiên Rudersdorf/Zettour, bản dịch không gán sai người nói. |

Nhìn chung bản dịch bám nghĩa tốt, giọng mỉa mai (p000004, p000008–009) được giữ; không có lỗi nghiêm trọng. Có 5 lỗi mức vừa cần sửa trước khi chốt lô và 10 lỗi nhẹ.

## 2. Phát hiện

Đếm: **nghiêm trọng 0 · vừa 5 · nhẹ 10**.

### Mức vừa

**M1 — p000003, p000005: đại từ trần thuật "cô" lệch DEC-P01-001 và lệch sổ pending.**
- DEC-P01-001 (đã duyệt): trần thuật về Tanya ở giai đoạn này dùng "nó". Sổ pending vol-02 (b01, b02) tạm dùng cách lặp tên Tanya hoặc lược chủ ngữ, tránh đại từ có giới tính. Cả hai đều không cho "cô".
- Căn cứ danh tính: b14 không nêu tên người này (nguồn chỉ dùng đại từ nữ), nên việc xác định là Tanya dựa vào mạch từ b13 và việc nhân vật gọi "binh sĩ" ở p000006; mức chắc chắn trung bình-cao, không tuyệt đối.
- Hệ quả: p000003 và p000005 là hai đoạn duy nhất trong lô dùng đại từ này; b13 cũng từng bị nhận xét tương tự (xem báo cáo b13, M2). Nếu giữ "cô", đoạn b14 sẽ lệch b11/b12.
- Đề xuất: p000003 lược chủ ngữ ("Quay lại, ngắm nhìn khung cảnh…") hoặc lặp "Tanya". p000005 dùng "nó" theo DEC-P01-001 ("Nó cười khanh khách…", "mừng… của nó") hoặc lặp tên. Nếu coordinator xác nhận người này không phải Tanya, giữ "cô" và bỏ phát hiện này.

**M2 — p000012: phạm vi "chỉ" bị lệch và hướng hành động "nuốt trôi" bị mất.**
- Câu cuối: nguồn nhấn "duy nhất chiếc tách Meissen mới là hàng thật" (phạm vi của "only" là chiếc tách) và Rudersdorf nhận ra điều đó qua cảm giác/độ bóng. Bản dịch viết "chỉ bằng cảm giác… và ánh lên… ông nhận ra duy nhất nó…", gán "chỉ" cho phương tiện nhận biết (như thể chỉ dựa vào hai yếu tố này) rồi lặp "duy nhất" ở vế sau. "Ánh lên" là cụm động từ lửng, thiếu danh từ ("độ bóng/ánh men").
- Câu trước: nguồn là dùng cà phê giả để nuốt trôi món giống bánh mì; bản dịch "để nuốt xuống cùng cà phê giả" đổi thành ăn kèm, mất quan hệ phương tiện–mục đích.
- Đề xuất: "…ông dùng cà phê giả nuốt trôi thứ thực phẩm giống bánh mì." và "Giữa bao món đồ thay thế trên bàn, ông nhận ra qua cảm giác khi chạm và độ bóng rằng chỉ có chiếc tách Meissen trong tay mới đáng gọi là hàng thật." Cũng nên đổi "trông như bánh mì" thành "giống bánh mì" (bản dịch hiện chỉ giới hạn ở vẻ ngoài).

**M3 — p000015: "war operations—mainly mobile" dịch lệch thuật ngữ so với p000014 và dở dang.**
- p000014 dùng "tác chiến" cho operations/operational; p000015 đổi sang "các chiến dịch quân sự" (campaigns) rồi để "chủ yếu là cơ động" treo không danh từ. Ledger gom hai đoạn vào một nhóm thuật ngữ nhưng bản dịch không nhất quán trong nhóm đó.
- Đề xuất: "phụ trách tác chiến, chủ yếu là tác chiến cơ động". Giữ nguyên các vế còn lại của câu.

**M4 — p000018: "câu giờ" sai nghĩa lời nói được trích.**
- Nguồn nói về việc cho đối phương thời gian để lo hậu cần; "câu giờ" nghĩa là kéo dài/trì hoãn, thay đổi nội dung đề nghị và còn mang sắc thái chủ động trì hoãn mà nguồn không có. Đuôi "nhé" biến mệnh lệnh mỉa mai thành lời nhờ thân mật, không có trong nguồn (xem thêm N10).
- Đề xuất: "‘Tôi cho ông thời gian, nên hậu cần ông lo đi?’" (giữ dấu hỏi nằm trong ngoặc như nguồn).

**M5 — p000018: "quân nhu" thu hẹp nghĩa của "matériel".**
- Trong tiếng Việt quân sự, "quân nhu" thường chỉ lương thực, quân trang (không gồm vũ khí, đạn dược, nhiên liệu). Câu đang nói gánh nặng vận chuyển cho một cuộc tấn công mùa đông, nơi đạn dược/trang bị là phần chính. Xem mục 3 (thuật ngữ 12).

### Mức nhẹ

- **N1 — p000003:** "bâng quơ" làm câu nói mất tính chủ ý lảng chuyện của nguồn (lái sang cảnh đẹp). Đề xuất "một câu nói lảng sang cảnh tượng kỳ vĩ ấy".
- **N2 — p000004:** "giúp chúng ta tổ chức diễn tập" thêm vai "tổ chức" mà nguồn không nói; nguồn là giúp/hỗ trợ trong buổi diễn tập. Đề xuất "giúp chúng ta diễn tập bắn đạn thật".
- **N3 — p000005:** "mừng cô hoàn thành nhiệm vụ" diễn giải "her service"; bản gốc là vinh danh sự phục vụ/cống hiến, không nói hoàn thành nhiệm vụ. Mức chắc chắn thấp vì b14 không nêu rõ phạm vi "service"; đề xuất "mừng công lao phục vụ của nó" hoặc cách trung tính tương đương.
- **N4 — p000006:** "…thôi" làm mệnh lệnh của người chỉ huy mềm đi thành lời rủ; cân nhắc "Quay về căn cứ." hoặc "Chúng ta quay về căn cứ." Giữ "các binh sĩ" (xem mục 3).
- **N5 — p000007:** (a) "Nghe… bảo" thêm sắc thái nghe lại, trùng với "Nghe nói" ở p000008; nguồn p000007 là lời khẳng định trực tiếp, chỉ p000008 mới là tin đồn. (b) "ở đây" chốt trước đối tượng của "it" khi p000007 chưa có ngữ cảnh; p000008 mới cho biết là nhà ăn. Đề xuất "Vị đại úy ấy quả có nói là…, có thể trải nghiệm khẩu phần thời chiến ở đó đấy" hoặc giữ chỉ định trung tính ("nơi này").
- **N6 — p000010:** "theo điều Thiếu tướng von Zettour biết" gượng; đề xuất "theo như Thiếu tướng von Zettour biết". "Căng tin" khác "nhà ăn" ở p000008–009, 011 dù cùng một nơi; nên thống nhất một từ (đề xuất "nhà ăn").
- **N7 — p000011:** "cùng nhau" đứng cuối câu như từ rơi; đề xuất "tận dụng hết mức mọi thứ có thể, và cùng nhau làm vậy" hoặc đặt "cùng" trước động từ.
- **N8 — p000016:** (a) "Còn ở Dacia" đảo thành tương phản, nguồn là nối tiếp. (b) "làm gương hoàn hảo" nghiêng nghĩa nêu gương đạo đức; nguồn là ví dụ mẫu mực; đề xuất "đưa ra mẫu mực hoàn hảo". (c) "đơn vị tiên phong" (vanguard) chưa chắc đúng với advance unit (đơn vị đi trước/tiền phương); chưa ghi vào sổ pending.
- **N9 — p000017:** "tiêu diệt kẻ địch yếu nhất" nặng hơn "knock out" (đánh gục/loại khỏi cuộc). Đề xuất "hạ gục" hoặc "đánh bại".
- **N10 — p000018:** "nhé" (xem M4) và "quá tải" mạnh hơn "đã ở mức giới hạn"; đề xuất "đã chạm giới hạn".

## 3. Đánh giá 12 đề xuất pending (chỉ dùng căn cứ trong b14 và sổ pending)

Quy ước: "Đề xuất" là phương án tạm tốt nhất; "độ tin" là độ chắc chắn của tôi; không phải canon.

| # | Thuật ngữ | Đoạn | Đề xuất tạm | Phương án khác | Độ tin | Ghi chú / bất định |
|---|---|---|---|---|---|---|
| 1 | live-fire exercise | p000004 | **diễn tập bắn đạn thật** (giữ) | diễn tập có bắn đạn thật | 0.8 | Nghĩa chuẩn, b14 không cho thêm ngữ cảnh. Đoạn này mang tính mỉa mai, giữ nguyên nghĩa đen. |
| 2 | troops | p000006 | **các binh sĩ** (giữ) | các quân nhân; toàn thể binh sĩ | 0.6 | "Binh sĩ" thiên về cấp thấp; đơn vị có thể gồm sĩ quan. Có xưng hô trực tiếp của người chỉ huy; không đổi sang "các cậu/các anh" vì suy ra quan hệ. p000016 "troops" nghĩa lực lượng (bản dịch "binh lực") chưa được ghi vào sổ; nên ghi riêng, không gộp với p000006. |
| 3 | war rations | p000007 | **khẩu phần thời chiến** (giữ) | khẩu phần chiến trường; khẩu phần chiến tranh | 0.65 | "Chiến tranh" thiên về sự kiện, "thời chiến" đúng nghĩa giai đoạn; "chiến trường" suy diễn thêm. Giữ. |
| 4 | Personnel | p000008 | **bộ phận Nhân sự** | Cục Nhân sự; Phòng Nhân sự | 0.55 | Nguồn chỉ có tên chung, không nêu cấp. "Cục" suy ra cấp biên chế; sổ pending vol-01 (b05-personnel) đã chọn "bộ phận nhân sự" với lý do "chưa suy ra biên chế". Đổi sang "Cục" khi có căn cứ về cấp. |
| 5 | General Staff Office / General Staff | p000008, 010, 014, 015, 016 | **Bộ Tổng tham mưu** (giữ) | sĩ quan tham mưu (cho "General Staffers/officer"); Văn phòng Bộ Tổng tham mưu | 0.65 | Hợp b03 ("Bộ Tổng Tham mưu Quân đội Đế quốc"). Nên thống nhất viết hoa ("Tổng Tham mưu" ở b03, "Tổng tham mưu" ở b14). Không dùng "Văn phòng" vì chưa có căn cứ rằng Office khác Staff trong b14. |
| 6 | Commonwealth | p000009 | **Khối Thịnh vượng chung** (giữ, khớp b03-commonwealth) | Thịnh vượng chung | 0.55 | **Bỏ "Liên bang"** khỏi phương án khác: "Liên bang" đã dùng cho Federation (b03-federation) và sẽ gây trùng. Ngữ cảnh b14 chỉ cho thấy đây là thực thể bên kia cạnh tranh về đồ ăn, không đủ phân biệt khối/nước; "Thịnh vượng chung" không có "Khối" ít suy diễn hơn nếu sau này cần đổi. |
| 7 | ersatz / pseudo-coffee / bread-like foodstuff | p000012 | ersatz → **đồ thay thế**; pseudo-coffee → **cà phê giả**; bread-like foodstuff → **thực phẩm giống bánh mì** | cà phê thay thế; hàng thay thế; thứ giống bánh mì | 0.5 | Tách ba nhãn trong sổ làm ba mục. "Giả" giữ được sắc thái bực dọc của Rudersdorf; "thay thế" trung tính hơn. "Trông như" thu hẹp vào vẻ ngoài, đổi sang "giống". Xem M2. |
| 8 | Meissen | p000012 | **Meissen** (giữ nguyên) | tách sứ Meissen | 0.75 | Tên riêng; "sứ" là suy diễn chất liệu từ độ bóng/cảm giác, chưa được nguồn nói thẳng. Giữ "tách Meissen". |
| 9 | operational theory / war operations | p000014, 015 | **lý thuyết tác chiến**; **tác chiến** | học thuyết tác chiến; chiến dịch quân sự; hoạt động quân sự | 0.6 | Nguồn dùng "theory", không phải "doctrine"; "học thuyết" thiên về doctrine. "Chiến dịch" là campaign. Dùng "tác chiến" nhất quán cho cả operations và war operations (xem M3). |
| 10 | maneuver warfare | p000016 | **chiến tranh cơ động** (giữ) | tác chiến cơ động | 0.65 | **Bỏ "chiến tranh cơ động hóa"**: "cơ giới/cơ động hóa" thêm nghĩa cơ giới hóa. "Mobile" (p000015) và "maneuver" (p000016) cùng cho "cơ động"; chấp nhận được, nhưng cần ghi nhận khác nguồn nếu sau này nguồn phân biệt. |
| 11 | Anluk E. Kahteijanen | p000018 | **Anluk E. Kahteijanen** (giữ nguyên, không thêm loại) | không có | 0.5 | Không bổ sung "tàu/tuyến/đường sắt". Căn cứ trong b14: có mạo từ "the", được xếp song song với cơ sở cảng, chịu tải khi xây dựng và vận chuyển; nên thiên về hạ tầng/phương tiện vận tải chứ ít khả năng là người, nhưng không đủ để chọn loại. Ghi bất định vào `work/run-state/pending-terms.yml` và chỉnh khi có ngữ cảnh. |
| 12 | matériel | p000018 | **vật tư quân sự** | quân nhu (hiện tại); trang bị vật tư; quân dụng | 0.6 | "Quân nhu" thu hẹp (xem M5). "Vật tư quân sự" bao cả đạn dược/trang bị cho cuộc tấn công mùa đông. |

## 4. Thuật ngữ chưa vào sổ pending

- Cấp bậc "Thiếu tướng" (Major General, p000009, 010) và "đại úy" (captain, p000007): chưa thấy trong sổ pending; nên ghi để nhất quán cho b15+.
- Dacia, Norden, Đế quốc: bản dịch dùng đúng với b03/b04 trong sổ; không cần mục mới nhưng nên kiểm tra cách dùng.
- advance unit (p000016, "đơn vị tiên phong") và "nhà ăn/căng tin" (p000008–011): chưa có mục.

## 5. Kết luận báo cáo

```yaml
role: reviewer
task_id: vol-02-ch-01-b14
state: done
segment_ids: [p000001..p000018]   # YS-LN02/Text/part0012.xhtml/
review_path: reviews/prose/vol-02/ch-01-b14-claude.md
files_written: [reviews/prose/vol-02/ch-01-b14-claude.md]
counts: {serious: 0, moderate: 5, minor: 10}
unresolved_findings:
  - {severity: moderate, segment_id: [p000003, p000005], issue: "đại từ 'cô' lệch DEC-P01-001/sổ pending (M1)"}
  - {severity: moderate, segment_id: p000012, issue: "phạm vi 'chỉ' + 'nuốt trôi' (M2)"}
  - {severity: moderate, segment_id: p000015, issue: "thuật ngữ tác chiến không nhất quán, 'cơ động' treo (M3)"}
  - {severity: moderate, segment_id: p000018, issue: "'câu giờ' sai nghĩa (M4)"}
  - {severity: moderate, segment_id: p000018, issue: "'quân nhu' thu hẹp matériel (M5)"}
term_recommendations:
  - {term: Personnel, proposed_vi: bộ phận Nhân sự, status: pending, confidence: 0.55}
  - {term: matériel, proposed_vi: vật tư quân sự, status: pending, confidence: 0.6}
  - {term: operational theory, proposed_vi: lý thuyết tác chiến, status: pending, confidence: 0.6}
  - {term: war operations, proposed_vi: tác chiến, status: pending, confidence: 0.6}
  - {term: Anluk E. Kahteijanen, proposed_vi: giữ nguyên, status: needs_context, confidence: 0.5}
  - {term: ersatz/pseudo-coffee/bread-like, proposed_vi: "đồ thay thế / cà phê giả / thực phẩm giống bánh mì", status: pending, confidence: 0.5}
  - {term: Commonwealth, proposed_vi: Khối Thịnh vượng chung, status: pending, confidence: 0.55, note: "bỏ 'Liên bang' (trùng Federation)"}
risks:
  - "Danh tính 'she' ở p000003/p000005 suy từ mạch, b14 không nêu tên."
  - "Anluk E. Kahteijanen chưa xác định loại; nếu sau này là người hoặc vật khác, cần đối chiếu lại."
  - "Cấp bậc Major General/captain và advance unit chưa vào sổ."
validator: not_run
diff_check: not_run
commit: null
next_action: translator sửa M1–M5 (và các mục nhẹ tùy ý) rồi reviewer ký lại; coordinator ghi lựa chọn tạm vào ledger/handoff, không nâng canon.
```
