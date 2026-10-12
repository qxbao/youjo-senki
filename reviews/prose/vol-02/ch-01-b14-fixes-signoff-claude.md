# Ký duyệt sửa lỗi — vol-02-ch-01-b14-fixes-signoff

- Người phản biện: Claude (chỉ đọc; không sửa bản dịch, handoff, ledger hay canon).
- Phạm vi: `p000003`–`p000018` của `YS-LN02/Text/part0012.xhtml` (mã viết tắt `pNNNNNN`). Đối chiếu: báo cáo gốc `ch-01-b14-claude.md`, handoff b14, `translations/vol-02/ch-01-b14.jsonl` hiện tại, gói nguồn b14 đã chuẩn bị. Không đọc nguồn hay batch khác. Không trích văn bản nguồn.
- Mọi thuật ngữ dưới đây vẫn là đề xuất tạm, không phải canon.

## 1. Kiểm tra cơ học

| Hạng mục | Kết quả |
|---|---|
| Hash gói nguồn | `af9b1c44…d7332` khớp handoff |
| Hash 5 tệp canon | Khớp handoff |
| Số đoạn / thứ tự | 18/18, p000001→p000018, khớp 1–1 |
| `*…*` nhấn mạnh | Không có; nguồn cũng không có nhấn mạnh in nghiêng (DEC-P01-002) |

## 2. Xác nhận M1–M5

| Mã | Đoạn | Kết quả | Nhận xét |
|---|---|---|---|
| M1 | p000003, p000005 | **Đạt** | p000003 lặp tên "Tanya", p000005 dùng "Tanya" ở vế đầu và "nó" ở "của nó". Khớp DEC-P01-001 và phương án trong handoff (nó / Tanya / lược chủ ngữ). Không còn "cô". Danh tính Tanya vẫn suy từ mạch b13 (nguồn b14 chỉ dùng đại từ), mức chắc chắn trung bình-cao. |
| M2 | p000012 | **Đạt** | "Nuốt trôi" bằng cà phê giả đã đúng quan hệ phương tiện–mục đích. "Thực phẩm giống bánh mì", "đồ thay thế", "cà phê giả" khớp ledger. "Chỉ có chiếc tách Meissen trong tay mới đáng gọi là hàng thật" đưa phạm vi "chỉ" về đúng chiếc tách, đúng quan hệ tách–các món thay thế. Nhận biết qua cảm giác và độ bóng được giữ. |
| M3 | p000015 | **Đạt** | "Phụ trách tác chiến, chủ yếu là tác chiến cơ động" nhất quán với p000014 về "tác chiến" và không còn vế treo. Xem R1 về chữ "học thuyết" ở p000014. |
| M4 | p000018 | **Đạt** | Lời trích là "Tôi cho ông thời gian, nên hậu cần ông lo đi?", khớp lựa chọn tạm của handoff. Không còn "câu giờ" lẫn "nhé". Dấu hỏi vẫn nằm trong ngoặc, giữ sắc thái mỉa mai/mệnh lệnh. |
| M5 | p000018 | **Đạt** | "Vật tư quân sự" thay "quân nhu", không thu hẹp về lương thực/quân trang. |

**fixes_pass: true cho M1–M5.** Không thấy thay đổi nghĩa hay nhấn mạnh ngoài ý muốn trong các chỗ đã sửa. Chi tiết nhỏ: p000012 thêm "khi chạm" cụ thể hóa "feel", và nguồn lặp "chỉ… và chỉ cái đó" còn bản dịch nói một lần. Cả hai đều rất nhẹ.

## 3. Thuật ngữ (đề xuất tạm)

| Thuật ngữ | Trạng thái trong b14 hiện tại |
|---|---|
| Personnel → bộ phận Nhân sự (p000008) | Khớp |
| General Staff (Office) → Bộ Tổng tham mưu | Nhất quán ở p000008, 010, 014, 015, 016 |
| Commonwealth → Khối Thịnh vượng chung (p000009) | Khớp b03, không trùng "Liên bang" |
| Ersatz foods → đồ thay thế / cà phê giả / thực phẩm giống bánh mì | Khớp |
| Meissen → tách Meissen | Khớp, không suy diễn "sứ" |
| war operations → tác chiến (p000015) | Khớp |
| **operational theory (p000014)** | **Lệch**: bản dịch dùng "học thuyết tác chiến"; ledger và handoff chọn "lý thuyết tác chiến" (xem R1) |
| maneuver warfare → chiến tranh cơ động (p000016) | Khớp ledger; "cơ động" dùng cho cả mobile (p000015) lẫn maneuver, chấp nhận được |
| Anluk E. Kahteijanen | Giữ nguyên, không thêm loại; vẫn cần ngữ cảnh |
| Ranks: Thiếu tướng, đại úy | Chuẩn, nhất quán; đã có trong ledger (`major-general`, `captain`) |
| troops → các binh sĩ (p000006); binh lực (p000016) | Khớp; tách riêng, đã ghi `troops-force` |
| advance unit → đơn vị tiên phong (p000016) | Chưa đổi (xem N3) |
| canteen/dining hall → nhà ăn | Đã thống nhất "nhà ăn" ở p000008–011; không còn "căng tin" |

## 4. Còn lại

Đếm: **nghiêm trọng 0 · vừa 1 · nhẹ 8**.

### Vừa

- **R1 — p000014:** "học thuyết tác chiến" cho "operational theory". Ledger (`vol02-ch01-b14-operational-theory`) và handoff chọn "lý thuyết tác chiến"; "học thuyết" thiên về doctrine, đúng loại sai lệch mà ledger muốn tránh. Sửa một từ: "lý thuyết tác chiến". Nghĩa câu không đổi.

### Nhẹ (chưa sửa, báo cáo gốc cho phép tùy ý)

- **N1 — p000004:** "tổ chức diễn tập" thêm vai tổ chức (gốc N2).
- **N2 — p000006:** "…thôi" làm mệnh lệnh mềm thành lời rủ (gốc N4).
- **N3 — p000016:** "đơn vị tiên phong" (vanguard) chưa chắc khớp advance unit; "Còn ở Dacia" thành tương phản; "làm gương hoàn hảo" nghiêng nghĩa nêu gương (gốc N8).
- **N4 — p000007:** "ở đây" chốt trước đối tượng của "it", khi p000008 mới cho biết là nhà ăn; "Nghe… bảo" gần "Nghe nói" ở p000008 (gốc N5).
- **N5 — p000011:** "cùng nhau" lơ lửng cuối vế (gốc N7).
- **N6 — p000017:** "tiêu diệt" nặng hơn "knock out" (gốc N9).
- **N7 — p000018:** "quá tải" mạnh hơn "ở mức giới hạn" (gốc N10).
- **N8 — p000003:** "buông một câu lảng sang cảnh tượng kỳ vĩ ấy" hơi gượng nhưng đúng nghĩa.

## 5. Rủi ro

- Danh tính Tanya ở p000003/p000005 suy từ mạch; nếu coordinator xác nhận khác thì cần xem lại M1.
- Anluk E. Kahteijanen chưa rõ loại.
- Mọi thuật ngữ vẫn provisional; không tự nâng thành canon.

## 6. Kết luận

```yaml
role: reviewer
task_id: vol-02-ch-01-b14-fixes-signoff
state: done
segment_ids: [p000003..p000018]
review_path: reviews/prose/vol-02/ch-01-b14-fixes-signoff-claude.md
files_written: [reviews/prose/vol-02/ch-01-b14-fixes-signoff-claude.md]
fixes_pass: true            # M1-M5 đều đạt
signoff: pass_with_one_residual_moderate
remaining: {serious: 0, moderate: 1, minor: 8}
unresolved_findings:
  - {severity: moderate, segment_id: p000014, issue: "học thuyết tác chiến lệch ledger/handoff (lý thuyết tác chiến) - R1"}
unintended_meaning_or_emphasis_change: none_found
risks:
  - "Danh tính Tanya suy từ mạch ở p000003/p000005."
  - "Anluk E. Kahteijanen chưa xác định loại."
  - "Thuật ngữ còn provisional, chưa canon."
validator: not_run
diff_check: not_run
commit: null
next_action: "Translator (người giữ quyền sửa) đổi 'học thuyết tác chiến' thành 'lý thuyết tác chiến' ở p000014, chạy lại validator; coordinator có thể chấp nhận R1 và commit ngay nếu muốn, vì không ảnh hưởng nghĩa. Các mục nhẹ để tùy ý, không chặn commit."
```
