# Báo cáo signoff sửa lỗi vol-02-ch-03-b05 (Claude)

- task_id: `vol-02-ch-03-b05-final-signoff`; checkpoint_generation: 489; vai trò: Claude reviewer.
- Phạm vi: 20 đoạn `YS-LN02/Text/part0016.xhtml/p000100`–`p000119`. Không mở lô khác, EPUB/PDF; không sửa tệp nào ngoài báo cáo này.
- Đầu vào: `agents/shared.md`, `agents/reviewer.md`, `config/translation-pipeline.yml`, handoff b05 (gồm metadata `translator_followup`), source package b05, bản dịch hiện tại, báo cáo review đầu `ch-03-b05-claude.md`, mục ledger `chapter3_b05_translation_proposals`.
- Hash source package `d2c7aac1…14bd9d3` khớp handoff (sha256sum).
- Báo cáo không chép câu nguồn; chỉ dùng thuật ngữ ngắn và mã đoạn.

## Kết luận

**Đạt signoff.** Cả 5 lỗi mức vừa F01–F05 đã được sửa đúng hướng đề xuất, không phát sinh lỗi mới nghiêm trọng hoặc vừa. Còn lại **0 nghiêm trọng, 0 vừa**; 11 lỗi nhẹ cũ chưa sửa (không chặn hoàn tất lô).

## Xác minh F01–F05

| Mã | Đoạn | Trạng thái | Kiểm tra |
|---|---|---|---|
| F01 | p000102 | Đã sửa | Dịch “thu hẹp tuyến”, không còn gắn “phòng thủ”; giữ độ mở giữa chiến tuyến và tuyến tiếp tế, không lệch p000101/p000108. |
| F02 | p000111, p000118 | Đã sửa | p000111 dùng “các sĩ quan Trung ương” (không còn “Bộ Chỉ huy”); p000118 dùng “Quân Trung ương”. Hai đoạn nhất quán với nhau và với ledger (`vol02-ch03-b05-central-army`). |
| F03 | p000112 | Đã sửa | Mở đầu lời thoại là “Cô nói cũng có lý”; người nghe được gọi “cô” xuyên suốt, hết xung đột “anh”/“cô”. Người nói vẫn chưa nêu tên trong đoạn (bất định đã ghi, không chặn). |
| F04 | p000118 | Đã sửa | Giữ giọng giả định phản thực (“hẳn đã … nếu cô không phải …”), bỏ “cô ta”, dùng “cô” như phần còn lại của lô. |
| F05 | p000119 | Đã sửa | Dịch “bị bào mòn bởi nỗ lực của các đồng đội chúng ta”: giữ thể bị động, bỏ “chính”, không chốt chủ thể bị bào mòn. Độ bất định về chủ thể vẫn còn do thiếu ngữ cảnh ngoài lô, đã được xử lý bằng cách diễn đạt trung tính nên không phải lỗi vừa. |

## Căn chỉnh thuật ngữ liên quan (đối chiếu ledger, đều là đề xuất tạm, không phải canon)

- **Phía Tác chiến / Hậu cần / Tình báo** (p000100, p000102, p000104, p000107, p000116): nhất quán “phía …”; p000104 dùng “nhân viên phía Hậu cần”, p000102 “các sĩ quan phía Tác chiến” — hợp ledger.
- **“cô” cho Tanya theo điểm nhìn ngoài** (p000100, p000102, p000104, p000107, p000116, p000118): nhất quán, đúng phạm vi hẹp ledger đã ghi; không lan sang nội tâm Tanya (xem F06 đã xử lý).
- **cụm tập đoàn quân / Cụm tập đoàn quân phương Bắc** (p000107, p000117): khớp ledger; viết hoa chỉ ở đầu câu/tên riêng (F12 đã xử lý).
- **đường sắt nhẹ** (p000108 “tuyến đường sắt nhẹ”, p000111 “đặt thêm đường sắt nhẹ”): nhất quán với khuyến nghị.
- **pháp sư biệt kích** (p000110), **công binh dã chiến** (p000111), **nhiên liệu thông dụng** (p000107), **đại đội tăng cường** (p000119): khớp ledger.
- Không thấy chỗ lệch thuật ngữ nào trong 11 đoạn nêu trên.

## Cấu trúc và nhấn mạnh

- Cấu trúc: 20/20 đoạn, thứ tự và `segment_id` khớp source package; `source_sha256` và `glossary_version` khớp handoff; mọi đoạn `status: draft`; không có xuống dòng thừa hay khoảng trắng đầu/cuối; không có đoạn bị bỏ hay thêm.
- Nhấn mạnh (DEC-P01-002): nguồn chỉ có một nhấn mạnh (p000105); bản dịch chỉ có đúng một `*có sẵn*` ở p000105, không có dấu `*` nào khác.

## Lỗi nhẹ còn tồn đọng (không chặn; ghi nhận cho người giữ quyền sửa nếu còn lượt)

F07 (p000101 “mọi việc”), F08 (p000102 “chẳng buồn lắng nghe”), F09 (p000103 “các anh”), F10 (p000104 “cau có nhìn chằm chằm”), F11 (p000106 “dư sức đảm đương/thu gom”), F13 (p000108 “đầy ẩn ý”), F14 (p000110/p000117 “ngoan cố”), F15 (p000111 “giữ vững quan điểm / vướng chân”), F16 (p000113 thiếu liên từ giải thích), F17 (p000114 “thuyết phục”), F18 (p000117 “bờ bên kia”). F06 và F12 đã được xử lý. Không mục nào làm đổi nghĩa trọng yếu, đại từ hay chủ thể.

## Rủi ro

- Không có hard stop, không có quyết định ảnh hưởng cốt truyện.
- Bất định còn lại (đều đã dùng cách diễn đạt trung tính, theo dõi khi có ngữ cảnh p000120 trở đi): chủ thể “bị bào mòn” ở p000119, người nói ở p000112, echelon “Quân Trung ương”.

```yaml
role: reviewer
task_id: vol-02-ch-03-b05-final-signoff
state: done
segment_ids: [p000100, p000101, p000102, p000103, p000104, p000105, p000106, p000107, p000108, p000109, p000110, p000111, p000112, p000113, p000114, p000115, p000116, p000117, p000118, p000119]
files_written: [reviews/prose/vol-02/ch-03-b05-fixes-signoff-claude.md]
review_path: reviews/prose/vol-02/ch-03-b05-fixes-signoff-claude.md
finding_counts: {serious: 0, moderate: 0, minor: 11}
verified_resolved: [F01, F02, F03, F04, F05, F06, F12]
unresolved_findings:
  serious: []
  moderate: []
  minor: [F07, F08, F09, F10, F11, F13, F14, F15, F16, F17, F18]
term_recommendations:
  - {source_term: light-rail, proposed_vi: đường sắt nhẹ, segment_ids: [p000108, p000111], status: pending}
  - {source_term: Central officers / Central Army, proposed_vi: các sĩ quan Trung ương / Quân Trung ương, segment_ids: [p000111, p000118], status: pending}
  - {source_term: Operations / Logistics / Intelligence, proposed_vi: phía Tác chiến / phía Hậu cần / phía Tình báo, segment_ids: [p000100, p000102, p000104, p000107, p000116], status: pending}
  - {source_term: Northern Army Group, proposed_vi: Cụm tập đoàn quân phương Bắc, segment_ids: [p000107, p000117], status: pending}
  - {source_term: Tanya (external POV), proposed_vi: cô, segment_ids: [p000100, p000102, p000104, p000107, p000116, p000118], status: pending}
  - {source_term: field engineers / mage commandos / general-purpose fuel / augmented company, proposed_vi: công binh dã chiến / pháp sư biệt kích / nhiên liệu thông dụng / đại đội tăng cường, segment_ids: [p000107, p000110, p000111, p000119], status: pending}
validator: not_run
diff_check: not_run
commit: null
next_action: coordinator_may_mark_b05_complete
```
