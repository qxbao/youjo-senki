# Báo cáo phản biện — vol-02-ch-01-b16

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, sổ pending hay canon).
- Phạm vi: `p000036`–`p000064` (29 đoạn) của `YS-LN02/Text/part0012.xhtml`; gồm handoff b16, gói nguồn cục bộ b16, `translations/vol-02/ch-01-b16.jsonl`, canon và sổ pending.
- Kích hoạt: `even_batch`, `new_pending_terms`.
- Báo cáo không trích câu nguồn. Thuật ngữ gốc ngắn và mã đoạn chỉ dùng để nhận diện. Mọi lựa chọn dưới đây là đề xuất tạm, không phải canon, không nâng lên canon.
- Mã đoạn viết tắt `pNNNNNN` = `YS-LN02/Text/part0012.xhtml/pNNNNNN`.

## 1. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Số đoạn / thứ tự | 29/29, liên tục p000036→p000064, khớp 1–1 và cùng thứ tự giữa nguồn và bản dịch |
| Hash | Gói nguồn `d8059c15…a77a23` khớp `source_package_sha256`; `source_sha256` mọi đoạn khớp `3ac53161…`; `glossary-pending.yml` khớp `65458cca…` |
| Trường bản dịch | `status: draft`, `glossary_version` khớp, `notes` rỗng ở cả 29 đoạn. Lưu ý nhỏ: `translator` ghi `codex-personal`, handoff ghi `translation_editor: codex-coordinator` (không ảnh hưởng nội dung) |
| Nhấn mạnh (DEC-P01-002) | Nguồn không có thẻ in nghiêng/nhấn mạnh ở đoạn nào; bản dịch không có `*…*`. Đúng. |
| Đại từ Tanya (DEC-P01-001) | Tanya không xuất hiện bằng tên; chỉ có một lần chỉ "chỉ huy đơn vị 203" ở p000056 qua điểm nhìn Rudersdorf (xem m6). |
| Phủ định / điều kiện | p38 (điều kiện kép "nếu không… và nếu…"), p39 (không có trở ngại), p46 ("nếu không thành"), p54/p55 giữ đúng; không đảo phủ định. |
| Người nói | Suy từ nội dung (nguồn không đánh dấu): Rudersdorf (Tác chiến) = p36, p41, p44, p47, p49, p52, p55, p58?, p62?; Zettour (hậu cần) = p37, p40, p42, p46, p48, p51, p53, p57, p60?, p63?. p36, p40, p41 và cụm p58–p63 là suy luận (độ chắc chắn trung bình). Bản dịch không dùng đại từ gán người nói nên không có gán sai; "tôi/ông" đối xứng, nhất quán với b15. |
| Ranh giới đoạn | Giữ nguyên, không gộp/tách. |

Nhìn chung bản dịch bám nghĩa tốt, mạch bàn kế hoạch (tìm điểm đánh → thuyết phục → xin lực lượng → nâng ly) rõ và giọng hai tướng nhất quán. Không có lỗi nghĩa nghiêm trọng.

## 2. Phát hiện

Đếm: **nghiêm trọng 0 · vừa 2 · nhẹ 9**.

### Mức vừa

**M1 — p54: "Xưởng kỹ thuật" lệch với dạng đã dùng trước đó.**
- Sổ pending đã có mục `b02-technical-arsenal` với dạng ưu tiên "Xưởng Vũ khí Kỹ thuật" (phương án bị thay: "Kho Vũ khí Kỹ thuật"). b16 tự rút gọn thành "Xưởng kỹ thuật" và bỏ yếu tố "Vũ khí", đồng thời mục b16 mới không nhắc tới mục cũ.
- Hệ quả: cùng một thuật ngữ gốc có hai nhãn ở hai lô; "Xưởng kỹ thuật" còn dễ đọc như xưởng cơ khí chung chung. Ngữ cảnh p54 (trang bị tối tân cho đơn vị chiến đấu) khớp với cơ quan chế tạo/thử nghiệm vũ khí, hỗ trợ dạng đầy đủ.
- Đề xuất: dùng lại dạng của b02 (xem mục 3, T8).

**M2 — p53: "Ông chắc chứ?" đổi trọng tâm câu hỏi.**
- Nguồn hỏi người nghe có chấp nhận/chịu được việc dùng một đơn vị khó trị hay không (mức độ sẵn lòng, rủi ro), không hỏi mức độ chắc chắn. "Chắc chứ" chuyển thành hỏi về độ quả quyết của quyết định.
- Quy tắc style-guide "giữ đối tượng và độ mở của câu hỏi". Đề xuất: "Ông không ngại chứ?" / "Ông chịu được chứ?" (độ chắc chắn trung bình-cao ở phần nghĩa; câu trước đã gánh sắc thái cảnh báo nên sửa nhẹ là đủ).

### Mức nhẹ

**m1 — p36: "đánh chiếm nơi đó" thêm đối tượng.** Nguồn chỉ nói hạ/đánh bại một đối tượng (so với Cộng hòa); bản dịch cụ thể hóa thành "chiếm một nơi" mà đoạn không cho biết. Đề xuất trung tính: "hạ họ/đánh bại họ sẽ dễ hơn" hoặc đối chiếu đoạn trước (ngoài phạm vi b16). Độ chắc chắn thấp-trung bình.

**m2 — p39: câu rườm.** "Xét việc… trong chuyện…" lặp cấu trúc; nghĩa đúng. Gợi ý: "Vì xét về mặt tác chiến, việc kiểm soát hậu phương phía bắc không có trở ngại nào, Zettour đồng ý…".

**m3 — p47: ba chỗ nhẹ.** (a) Thiếu sắc thái của trạng từ "dramatically": nên có "xoay chuyển ngoạn mục/hẳn". (b) Nước "dirty-water" bị làm nhẹ thành "dở tệ"; có thể "nước bẩn/nhạt như nước đục". (c) "cấp tác chiến" — xem T2. Không ảnh hưởng cốt truyện.

**m4 — p50: "thẳng thừng đòi" yếu hơn "merciless".** Nguồn nhấn mạnh sự không chút nể nang khi đòi; gợi ý "chẳng chút nể nang đòi thứ mình muốn".

**m5 — p52, p54: "giấu" thừa và không nhất quán; gọi đơn vị.** p52 thêm "giấu" (ý che giấu) không có trong nguồn, trong khi p54 chỉ dùng "trong túi". Bỏ "giấu". Ngoài ra p53 nói thẳng "tiểu đoàn" nên p52/p56 có thể thống nhất "Tiểu đoàn 203" như b02 thay vì "đơn vị 203" (trong b02 chỉ ghi suy luận). Độ chắc chắn trung bình-cao.

**m6 — p56: hai điểm.** (a) "khác thường" nghiêng về nghĩa lập dị/tiêu cực hơn nghĩa "đặc trưng, có cá tính"; xem T10. (b) "cô" cho chỉ huy đơn vị: nguồn có đại từ giống cái nên không thêm giới tính; nhưng sổ pending hướng tránh "cô" khi kể về Tanya (P01-tanya-narration-ch01 và các mục vol-02). Ở đây điểm nhìn là Rudersdorf, người chưa gọi tên nhân vật, nên chấp nhận được; chỉ cần ghi nhất quán với các lô có Tanya/203 qua mắt người khác. Độ chắc chắn thấp-trung bình.

**m7 — p58, p61: sắc thái nâng ly bị nhạt.** p58 là lời chúc khi nâng ly; "Mong là chúng ta sẽ thắng" đọc như một lời hy vọng thông thường. p61 "lời chúc thứ hai" làm mất ý "lời chúc đáp lại". Gợi ý: "Cầu cho chúng ta thắng" / "Lời chúc đáp lại khiến cả hai…". p60 đã dùng "mong là", nên có thể giữ song song nhưng thêm yếu tố chúc.

**m8 — p54: "gan lì" cho "dauntless".** "gan lì" nghiêng về ương bướng; "dauntless" là không biết sợ. Gợi ý "gan dạ/bất khuất". Ngoài ra "túi Zettour" có thể "túi của Zettour" cho tự nhiên.

**m9 — p62, p64: vài chỗ giọng.** p62 "mất" thêm sắc thái tiếc nuối/ngao ngán không có; bỏ "mất" hoặc giữ nếu muốn giọng đùa chua chát (tùy dịch giả). p64 kết thúc "…ở nơi khác hơn" hơi vụng; gợi ý "muốn ăn ở nơi khác hơn" hoặc "thà ăn ở nơi khác".

(Các đoạn không có phát hiện: p37, p38, p40, p41, p42, p43, p44, p45, p48, p49, p51, p55, p57, p59, p60, p63. Ghi chú: p44 "hiểm" ổn, có thể "hiểm độc" nếu muốn mạnh hơn; p45 "chết như chó" giữ nguyên độ thô của nguồn.)

## 3. Thuật ngữ pending (đề xuất tạm, không canon)

Tất cả 10 nhóm khớp mục `chapter2_b16_translator_terms` trong `work/run-state/pending-terms.yml`.

| # | Thuật ngữ | Mã đoạn | Đề xuất tạm | Phương án khác | Độ chắc | Bất định |
|---|---|---|---|---|---|---|
| T1 | state warfare | p38 | chiến tranh giữa các quốc gia (giữ) | chiến tranh giữa các nhà nước; "chiến tranh quốc gia" (kém tự nhiên) | 0.55 | "Giữa các quốc gia" đọc như chiến tranh liên quốc gia; nếu nguồn muốn nói chiến tranh do nhà nước tiến hành (đối lập với du kích/khủng bố), "nhà nước" sát hơn. Không ảnh hưởng cốt truyện. |
| T2 | operational terms / level | p39, p47 | p39 giữ "về tác chiến"; p47 đề xuất "cấp chiến dịch" (thay "cấp tác chiến") | cấp tác chiến; tầm tác chiến | 0.55 | Chuỗi học thuyết quen thuộc: chiến lược – chiến dịch – chiến thuật; p38 đã dịch "operation" là "chiến dịch" nên "cấp chiến dịch" khớp. Nhưng đã có "Cục Tác chiến" (b15) và "lý thuyết tác chiến" (b14) nên giữ "tác chiến" cũng nhất quán; chưa rõ nguồn muốn học thuyết hay nghĩa thường. |
| T3 | Osfjord / Os | p40, p41, p42, p44 | giữ nguyên Osfjord (vịnh/cửa vịnh) và Os (thành phố) như tên riêng | "vịnh Osfjord" khi cần nhắc rõ | 0.7 | Không nên dùng phương án "Vịnh Os" trong sổ: p41–p42 phân biệt rõ fjord/bay (nơi có pháo bờ biển) với thành phố Os (đầu mối đường sắt) nên "Vịnh Os" làm hòa nhập hai đối tượng. Bản dịch hiện giữ đúng sự phân biệt. |
| T4 | Northern Command | p45 | Bộ chỉ huy phương Bắc (giữ) | Bộ Tư lệnh phương Bắc; Bộ chỉ huy phía Bắc | 0.5 | Vol-02 đã dùng "Bộ chỉ huy" cho Command (b-nhiều lô), còn "Bộ Tư lệnh Hậu cần/Trung ương" dùng "Bộ Tư lệnh" — chưa thống nhất. Ngữ cảnh: có thể là bộ phận chỉ huy phía Bắc của Đế quốc hoặc cách nói chung về những người đang lên kế hoạch; chưa đủ để xác định. Không viết "Bắc" hoa ở chỗ này nhưng "phía bắc" thường ở p39 — nhất quán với tên cơ quan/vùng địa lý. |
| T5 | General Staff officer | p47 | sĩ quan Bộ Tổng tham mưu (giữ) | sĩ quan tham mưu | 0.7 | Khớp "Bộ Tổng tham mưu" dùng 6 lần ở vol-02. "Sĩ quan tham mưu" rộng hơn, mất liên hệ với tổ chức. |
| T6 | mage unit | p49, p51 | đơn vị pháp sư (giữ) | đơn vị pháp sư chiến đấu; đơn vị ma pháp | 0.6 | p53 xác nhận thực thể được hỏi là tiểu đoàn; "đơn vị" là nhãn trung tính phù hợp ở p49/p51. |
| T7 | augmented unit | p54 | đơn vị tăng cường (giữ, nhất quán b13) | đơn vị được cường hóa/nâng cấp; đơn vị trang bị bổ sung | 0.5 | Câu liền nhau nói đến trang bị tối tân, nghiêng sang nghĩa "được nâng cường năng lực/trang bị" hơn là "được bổ sung quân số"; "tăng cường" trong tiếng Việt quân sự thường chỉ biệt phái thêm lực lượng, dễ lệch. Chưa đủ căn cứ để đổi; giữ b13–b16 đồng bộ. |
| T8 | Technical Arsenal | p54 | Xưởng Vũ khí Kỹ thuật (theo `b02-technical-arsenal`) | Kho Vũ khí Kỹ thuật (đã bị thay ở b02) | 0.6 | Xem M1. Loại "Kho kỹ thuật" khỏi danh sách: ngữ cảnh chế tạo/trang bị mới hợp với "xưởng". Viết hoa như tên cơ quan. |
| T9 | Lieutenant Colonel | p54 | Trung tá (giữ) | — (bỏ "Thượng tá") | 0.9 | Thứ tự bậc Việt: Thiếu tá < Trung tá < Thượng tá < Đại tá; Lt Col tương ứng Trung tá, và b01/b06 đã dùng "Trung tá". "Thượng tá" là cấp bậc cao hơn một bậc. Nên bỏ phương án thay thế để tránh nhầm. |
| T10 | distinctive personality | p56 | cá tính đặc biệt (thay "tính cách khác thường") | tính cách khác thường; cá tính riêng; tính cách có nét riêng | 0.5 | Bản gốc không mang phán xét đạo đức, chỉ nói đặc điểm riêng; "khác thường" thêm sắc thái lạ/kỳ quặc. Theo P01-personality: không đồng nhất với phẩm chất đạo đức. Chỉ ảnh hưởng giọng, không ảnh hưởng cốt truyện. |

Không có mục nào ở trên ảnh hưởng cốt truyện đến mức cần hỏi người dùng. Tùy chọn T4 và T7 nên ghi bất định trong `pending-terms.yml` theo quy tắc AGENTS.md.

Ghi chú: danh sách pending b16 chưa gồm vài chỗ phát sinh khi đối chiếu — "Northern Command" ↔ "Bộ Tư lệnh" (nhất quán chung), "tiểu đoàn 203" (m5), và "Republic/Cộng hòa" ở p36 (đã có dạng "nước Cộng hòa" ở lô khác; giữ). Coordinator cân nhắc ghi thêm.

## 4. Rủi ro

- Nhãn Technical Arsenal đang lệch hai lô (M1); nếu không sửa, bản xuất bản sẽ có hai tên cho cùng cơ quan.
- Người nói p36/p40/p41 và cụm p58–p63 chỉ suy luận từ ngữ cảnh; không ảnh hưởng chữ dịch hiện tại nhưng nếu lô sau cần xưng hô khác thì phải xét lại.
- T2, T4, T7 còn bất định học thuyết/tổ chức; nên giữ đề xuất, không nâng canon.

## 5. Báo cáo coordinator (YAML)

```yaml
role: reviewer
task_id: vol-02-ch-01-b16
state: done
segment_ids: [YS-LN02/Text/part0012.xhtml/p000036 … p000064]  # 29 đoạn, đủ và đúng thứ tự
files_written: [reviews/prose/vol-02/ch-01-b16-claude.md]
review_path: reviews/prose/vol-02/ch-01-b16-claude.md
validator: not_run
diff_check: not_run
counts: {nghiêm_trọng: 0, vừa: 2, nhẹ: 9}
unresolved_findings:
  - {severity: vừa, segment_id: p000054, issue: "Technical Arsenal lệch dạng b02 (Xưởng Vũ khí Kỹ thuật)"}
  - {severity: vừa, segment_id: p000053, issue: "Câu hỏi 'chắc chứ' đổi trọng tâm so với hỏi chấp nhận/chịu được"}
  - {severity: nhẹ, segment_id: p000036, issue: "thêm đối tượng 'nơi đó'"}
  - {severity: nhẹ, segment_id: p000039, issue: "câu rườm"}
  - {severity: nhẹ, segment_id: p000047, issue: "thiếu 'dramatically'; 'dở tệ' làm nhẹ; 'cấp tác chiến'"}
  - {severity: nhẹ, segment_id: p000050, issue: "'thẳng thừng' yếu hơn 'merciless'"}
  - {severity: nhẹ, segment_id: p000052, issue: "'giấu' thừa; thống nhất Tiểu đoàn 203"}
  - {severity: nhẹ, segment_id: p000056, issue: "'khác thường' lệch sắc thái; dùng 'cô'"}
  - {severity: nhẹ, segment_id: p000058/p000061, issue: "sắc thái nâng ly / lời chúc đáp lại"}
  - {severity: nhẹ, segment_id: p000054, issue: "'gan lì' vs dauntless; 'túi Zettour'"}
  - {severity: nhẹ, segment_id: p000062/p000064, issue: "'mất' thừa sắc thái; câu kết hơi vụng"}
term_recommendations:
  - {source_term: state warfare, proposed_vi: chiến tranh giữa các quốc gia, alternatives: [chiến tranh giữa các nhà nước], segment_ids: [p000038], confidence: 0.55, status: pending}
  - {source_term: operational level, proposed_vi: cấp chiến dịch (p47); về tác chiến (p39), alternatives: [cấp tác chiến], segment_ids: [p000039, p000047], confidence: 0.55, status: pending}
  - {source_term: Osfjord / Os, proposed_vi: giữ nguyên Osfjord; giữ nguyên Os (thành phố), alternatives: [vịnh Osfjord], segment_ids: [p000040, p000041, p000042, p000044], confidence: 0.7, status: pending}
  - {source_term: Northern Command, proposed_vi: Bộ chỉ huy phương Bắc, alternatives: [Bộ Tư lệnh phương Bắc], segment_ids: [p000045], confidence: 0.5, status: pending}
  - {source_term: General Staff officer, proposed_vi: sĩ quan Bộ Tổng tham mưu, alternatives: [sĩ quan tham mưu], segment_ids: [p000047], confidence: 0.7, status: pending}
  - {source_term: mage unit, proposed_vi: đơn vị pháp sư, alternatives: [đơn vị pháp sư chiến đấu], segment_ids: [p000049, p000051], confidence: 0.6, status: pending}
  - {source_term: augmented unit, proposed_vi: đơn vị tăng cường, alternatives: [đơn vị được cường hóa], segment_ids: [p000054], confidence: 0.5, status: pending}
  - {source_term: Technical Arsenal, proposed_vi: Xưởng Vũ khí Kỹ thuật, alternatives: [Kho Vũ khí Kỹ thuật], segment_ids: [p000054], confidence: 0.6, status: pending}
  - {source_term: Lieutenant Colonel, proposed_vi: Trung tá, alternatives: [], segment_ids: [p000054], confidence: 0.9, status: pending}
  - {source_term: distinctive personality, proposed_vi: cá tính đặc biệt, alternatives: [tính cách khác thường, cá tính riêng], segment_ids: [p000056], confidence: 0.5, status: pending}
risks:
  - "Technical Arsenal lệch hai lô nếu không sửa."
  - "Người nói p36/p40/p41, p58–p63 là suy luận."
  - "T2/T4/T7 chưa đủ căn cứ học thuyết/tổ chức; không nâng canon."
commit: null
next_action: translator_fix_then_review_signoff  # sửa M1, M2 (và các mục nhẹ nên sửa), coordinator ghi T1–T10 vào ledger; không có hard stop
```
