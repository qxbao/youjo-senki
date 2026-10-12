# Báo cáo phản biện tiếp theo — vol-01-ch-01-b06

- Task: `vol-01-ch-01-b06-review-fixes-followup` (reviewer: Claude).
- Phạm vi: 25 đoạn `YS-LN01/Text/chapter003b.xhtml/p000076`–`p000100` (viết tắt `pNNNNNN`).
- Đã đối chiếu: source package cục bộ, `translations/vol-01/ch-01-b06.jsonl` sau sửa, báo cáo phản biện trước, handoff sửa, `work/run-state/pending-terms.yml`, canon, agents, config.
- Toàn vẹn: 25/25 đoạn, đúng thứ tự mã đoạn; `source_sha256` mỗi đoạn khớp package; `status: draft`; `glossary_version` và `translator` giữ nguyên. Không chép câu nguồn; mọi thuật ngữ chỉ là đề xuất, không canon.
- Validator/diff_check: not_run. Commit: null.

## 1. Kết luận

Ba trong bốn lỗi mức vừa đã được xử lý (M1, M2, M4). **M3 chưa được xử lý ở văn bản**: p000089 vẫn dịch "dominion" thành "chủ quyền", trong khi ghi chú đoạn và ledger đều khẳng định đã dùng "quyền cai trị". Đây là lỗi mức vừa còn lại duy nhất; không có lỗi nghiêm trọng mới. Không có quyết định canon ảnh hưởng cốt truyện cần hỏi người dùng.

| Mức | Số lượng |
|---|---|
| Nghiêm trọng | 0 |
| Vừa | 1 (M3 còn mở) |
| Nhẹ | 7 |

## 2. Kiểm tra bốn lỗi mức vừa trước đó

- **M1 — p000076: ĐÃ XỬ LÝ.** Dòng tiêu đề giữ đúng dạng "Nordland" như nguồn, không thay bằng "Norden", không khẳng định tương đương. Ghi chú đoạn và mục `b06-nordland` trong ledger khớp (pending, tin cậy 0,7, nêu rõ chưa đồng nhất với Norden).
- **M2 — p000084: ĐÃ XỬ LÝ.** "đường ranh giả" đã đổi thành "một dạng biên giới không chính thức"; cụm "thực chất" thêm vào đã bỏ; giữ hạt nhân "biên giới". Đọc với p000089 ("trên thực tế là biên giới quốc gia") thì "không chính thức" ≈ de facto, không còn mâu thuẫn bề mặt. Dấu chú thích ⁶ và chữ nghiêng "binh sĩ" được giữ. Ghi chú đoạn (tin cậy 0,5) khớp mục ledger mới.
- **M3 — p000089: CHƯA XỬ LÝ (vừa, còn mở).** Câu cuối đoạn vẫn dùng "yêu sách về chủ quyền" cho "claim of dominion", nên p000089 và p000091 (sovereignty) vẫn cùng là "chủ quyền", làm mất phân biệt hai khái niệm và vẫn khiến người đọc hiểu hiệp ước nể trọng yêu sách chủ quyền. Ghi chú đoạn nói "dominion → quyền cai trị", ledger `b06-dominion` và `coordinator_decisions` cũng ghi vậy — tức metadata nói đã áp dụng nhưng văn bản chưa. Các sửa nhẹ khác ở p000089 (vì nể, giữ mơ hồ chủ thể) đã áp dụng.
  - Đề xuất: thay "yêu sách về chủ quyền" bằng "yêu sách về quyền cai trị" (hoặc "quyền cai quản" nếu muốn tránh trùng "quyền quản lý" ở câu trước); giữ "chủ quyền" ở p000091. Tin cậy 0,6. Sau đó đọc lại cả câu cho tự nhiên.
- **M4 — p000094: ĐÃ XỬ LÝ.** Đã bỏ "hành quân"; dùng "cuộc đi bộ đường dài có tổ chức chặt chẽ trong điều kiện áp lực", nhất quán với "đi bộ đường dài trong điều kiện áp lực" ở p000090 và p000092. Ghi chú đoạn và ledger khớp. "Exercise" không được dịch riêng — chấp nhận được, ghi ở mục nhẹ.

## 3. Kiểm tra các sửa nhẹ trước đó

Đã áp dụng và đúng hướng: p000077 ("hỏi trời cao", "sạm nắng vì tuyết", "bộ binh không giáp"); p000078 (khôi phục ý "được báo sai"); p000084 ("cứ thản nhiên bước qua", "vốn luôn cần mẫn", "lẽ ra họ phải lường trước"); p000086 ("khoảng cách giữa các tầng lớp"); p000088 ("sai lầm", "chửi rủa"); p000091 ("hão huyền", "cay cú", "thèm coi trọng"); p000094 ("kẻ ăn hại lương", "thiếu suy nghĩ đến mức kinh người"); p000097 ("vượt qua biên giới"); p000098 ("bộ phận kiểm soát không phận" chữ thường, "Trung tâm Điều hành Tác chiến"); p000099 ("kênh liên lạc"); p000100 (không còn "cựu binh"). "Quân đội Đế quốc" nhất quán ở p000077/p000084/p000097.

## 4. Phát hiện mức nhẹ (mới hoặc còn lại)

- **n1 — p000089.** Câu thứ hai lặp "bảo đảm" ("vật bảo đảm để… được bảo đảm"); nên đổi một chỗ (ví dụ "được đảm bảo/được giữ vững"). Nghĩa không lệch.
- **n2 — ledger, trùng ID.** `b06-pseudo-border` xuất hiện hai lần trong `pending-terms.yml` (bản cũ "đường ranh giả", tin cậy 0,65, và bản mới "biên giới không chính thức", tin cậy 0,5). Bản cũ nên đánh dấu superseded/xóa bởi coordinator để tránh áp dụng nhầm. (Reviewer không sửa ledger.)
- **n3 — ledger lệch văn bản.** `b06-combat-direction-center` ledger vẫn đề xuất "Trung tâm Chỉ huy Tác chiến" còn văn bản và ghi chú p000098 dùng "Trung tâm Điều hành Tác chiến"; `b06-airspace-control` ledger viết hoa "Bộ phận Kiểm soát Không phận" còn văn bản chữ thường. Cần coordinator đồng bộ.
- **n4 — ghi chú đoạn.** Một số hàng đã đổi nội dung (p000078, p000088, p000091, p000099, p000085 không đổi) có `notes` rỗng dù handoff yêu cầu làm mới ghi chú cho hàng đã đổi. Không ảnh hưởng nghĩa.
- **n5 — p000084.** Cụm "vốn luôn cần mẫn" đứng sau "các vị trí của Quân đội Đế quốc" nên có thể đọc như bổ nghĩa cho "vị trí" hơn là cho quân đội; nguồn có độ mơ hồ tương tự. Chấp nhận được; nếu muốn rõ: "những vị trí vốn luôn được Quân đội Đế quốc canh giữ cần mẫn" (tin cậy thấp, 0,4).
- **n6 — p000094.** "Exercise" (diễn tập/hoạt động) không có đối ứng riêng; hai đoạn kia không có từ này nên bỏ là an toàn. Không bắt buộc.
- **n7 — p000100.** "kỳ cựu" lặp trong hai câu liền ("được coi là kỳ cựu", "một tay kỳ cựu trên không"). Có thể đổi câu sau thành "lão luyện". Còn "ông" (Sue) vẫn ngầm suy tuổi (m15 trước đó, đã vào ledger như đề xuất tạm).

## 5. Khuyến nghị thuật ngữ (đề xuất, không canon)

| Thuật ngữ | Hiện tại trong văn bản | Khuyến nghị | Tin cậy |
|---|---|---|---|
| Nordland (p000076) | Nordland | Giữ nguyên dạng nguồn; coordinator tự đối chiếu các lô trước ngoài phạm vi này | 0,7 |
| pseudo-border (p000084) | một dạng biên giới không chính thức | Giữ; xóa mục cũ trùng ID | 0,5 |
| dominion (p000089) | chủ quyền (**chưa theo ghi chú**) | Đổi thành quyền cai trị; thay thế: quyền cai quản/thống trị | 0,6 |
| sovereignty (p000091) | chủ quyền | Giữ | 0,75 |
| hiking under pressure (p000090/92/94) | đi bộ đường dài (có tổ chức chặt chẽ) trong điều kiện áp lực | Giữ thống nhất ba chỗ | 0,7 |
| Combat Direction Center (p000098) | Trung tâm Điều hành Tác chiến | Giữ; sửa ledger cho khớp | 0,5 |
| Airspace Control (p000098) | bộ phận kiểm soát không phận | Giữ chữ thường; sửa ledger | 0,6 |
| Imperial Army | Quân đội Đế quốc | Giữ tạm theo b03 | 0,6 |
| aerial mage, First Lieutenant, smoke screen, centripetal forces, exclusionism | như báo cáo trước | Không đổi | — |

## 6. Rủi ro còn lại

- M3 còn mở: ghi chú/ledger nói đã áp dụng nhưng văn bản chưa — nguy cơ bị coi là đã xử lý nếu chỉ kiểm tra metadata. Cần translator sửa một cụm ở p000089 rồi review lại đoạn này.
- Ledger có ID trùng và hai mục lệch văn bản (n2, n3), cần coordinator làm sạch.
- Nordland/Norden chưa được đối chiếu với nguồn của lô trước (ngoài phạm vi review).
- Validator và diff_check chưa chạy (not_run); commit: null.

## 7. YAML báo cáo

```yaml
role: reviewer
task_id: vol-01-ch-01-b06-review-fixes-followup
state: done
segment_ids: [p000076..p000100 của YS-LN01/Text/chapter003b.xhtml, 25 đoạn]
files_written:
  - reviews/prose/vol-01-ch-01-b06-followup-claude.md
review_path: reviews/prose/vol-01-ch-01-b06-followup-claude.md
validator: not_run
diff_check: not_run
counts: {serious: 0, moderate: 1, minor: 7}
unresolved_findings:
  - {severity: moderate, segment_id: p000089, issue: "dominion vẫn dịch 'chủ quyền', trùng sovereignty ở p000091; ghi chú/ledger nói đã dùng 'quyền cai trị'", resolution: "đổi cụm cuối đoạn sang 'quyền cai trị'"}
  - {severity: minor, segment_id: ledger, issue: "trùng ID b06-pseudo-border; combat-direction-center và airspace-control lệch văn bản", resolution: coordinator đồng bộ}
  - {severity: minor, segment_id: p000089, issue: "lặp 'bảo đảm'", resolution: tùy chọn}
  - {severity: minor, segment_id: p000100, issue: "lặp 'kỳ cựu'", resolution: tùy chọn}
  - {severity: minor, segment_id: "p000078/p000088/p000091/p000099", issue: "notes rỗng cho hàng đã đổi", resolution: tùy chọn}
  - {severity: minor, segment_id: p000084, issue: "vị trí bổ nghĩa 'vốn luôn cần mẫn' hơi mơ hồ", resolution: tùy chọn}
  - {severity: minor, segment_id: p000094, issue: "'exercise' không có đối ứng riêng", resolution: chấp nhận}
resolved_findings: [M1, M2, M4, m1..m14 phần lớn]
term_recommendations: xem mục 5
risks: xem mục 6
commit: null
next_action: translator sửa M3 rồi review lại p000089; coordinator làm sạch ledger
```
