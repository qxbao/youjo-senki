# Self-check — vol-02-ch-06-b23

```yaml
task_id: vol-02-ch-06-b23-translator-signoff
parent_task_id: vol-02-ch-06-b23
segment_ids: [YS-LN02/Text/part0030.xhtml/p000709-YS-LN02/Text/part0030.xhtml/p000751]
findings:
  - severity: serious
    segment_id: YS-LN02/Text/part0030.xhtml/p000719
    issue: "Cụm từ chỉ độ tuổi ở câu cuối từng bị dịch ngược nghĩa thành trẻ tuổi, trong khi người đề ra kế hoạch theo ngữ cảnh là Tướng von Zettour."
    resolution: "Sửa thành 'đã ở độ tuổi như vậy' theo argon-review và locked_choices."
  - severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000712
    issue: "Lời thoại của Tanya với Thiếu tá Uger có tiểu từ kính ngữ 'ạ', lệch quy ước đồng cấp 'tôi' - 'ông'."
    resolution: "Bỏ 'ạ', đổi thành '“Diễn kịch sao?”' theo argon-review và locked_choices."
  - severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000725
    issue: "Lời thoại của Tanya với Thiếu tá Uger dùng đại từ 'anh', lệch quy ước đồng cấp 'tôi' - 'ông'."
    resolution: "Đổi 'Ý anh là' thành 'Ý ông là' theo argon-review và locked_choices."
  - severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000730
    issue: "Đại từ ngôi thứ ba chỉ Tướng von Zettour trong lời thoại của Tanya từng dịch là 'anh ta'."
    resolution: "Đổi 'anh ta' thành 'ông ấy' theo argon-review và locked_choices."
  - severity: moderate
    segment_id: YS-LN02/Text/part0030.xhtml/p000745
    issue: "Lời thoại của Tanya nói với Uger về Tiểu đoàn 203 dùng đại từ gộp 'chúng ta', trong khi Uger không thuộc Tiểu đoàn 203."
    resolution: "Đổi 'chúng ta' thành 'chúng tôi' theo argon-review và locked_choices."
  - severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000741
    issue: "Thuật ngữ chỉ vai trò thiếu tá ngoài chiến trường chưa đồng bộ với sổ pending của vol-02."
    resolution: "Đổi 'thiếu tá dã chiến' thành 'thiếu tá tác chiến' theo argon-review và locked_choices."
  - severity: minor
    segment_id: YS-LN02/Text/part0030.xhtml/p000744
    issue: "Tên đơn vị Tiểu đoàn 203 chưa đồng bộ với phương án tạm của vol-02."
    resolution: "Đổi thành 'Tiểu đoàn Pháp sư Trên không số 203' theo argon-review và locked_choices."
pending_choices:
  - source_term: "information warfare"
    proposed_vi: "chiến tranh thông tin"
    alternatives_vi: ["tác chiến thông tin"]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000719]
    rationale: "Theo đề xuất của argon-review, chỉ hoạt động tung tin tuyên truyền và thao túng nhận thức đối phương; vẫn là pending/non-canon."
    status: pending
  - source_term: "Ems Dispatch incident"
    proposed_vi: "Vụ Điện tín Ems"
    alternatives_vi: ["Sự kiện Điện tín Ems"]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000726]
    rationale: "Theo đề xuất của argon-review cho sự kiện ngoại giao lịch sử năm 1870; vẫn là pending/non-canon."
    status: pending
  - source_term: "disinformation"
    proposed_vi: "thông tin sai lệch"
    alternatives_vi: ["tin giả có chủ đích"]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000729]
    rationale: "Theo đề xuất của argon-review, chỉ thông tin bóp méo tung ra có chủ đích; vẫn là pending/non-canon."
    status: pending
  - source_term: "night-watchman state"
    proposed_vi: "nhà nước gác đêm"
    alternatives_vi: ["nhà nước tuần đêm", "nhà nước tối thiểu"]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000737]
    rationale: "Theo đề xuất của argon-review cho khái niệm triết học chính trị; vẫn là pending/non-canon."
    status: pending
  - source_term: "field major"
    proposed_vi: "thiếu tá tác chiến"
    alternatives_vi: ["thiếu tá dã chiến"]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000741]
    rationale: "Đồng bộ với phương án tạm trong vol-02 và argon-review; vẫn là pending/non-canon."
    status: pending
  - source_term: "203rd Aerial Mage Battalion"
    proposed_vi: "Tiểu đoàn Pháp sư Trên không số 203"
    alternatives_vi: ["Tiểu đoàn Pháp sư trên không 203"]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000744]
    rationale: "Đồng bộ với phương án tạm trong vol-02 và argon-review; vẫn là pending/non-canon."
    status: pending
  - source_term: "rear guard"
    proposed_vi: "đội hậu vệ"
    alternatives_vi: ["lực lượng đoạn hậu"]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000744, YS-LN02/Text/part0030.xhtml/p000751]
    rationale: "Giữ đồng bộ giữa p000744 và p000751 theo locked_choices; vẫn là pending/non-canon."
    status: pending
  - source_term: "golden parachutes"
    proposed_vi: "các gói đãi ngộ hậu hĩnh khi rời chức"
    alternatives_vi: ["chiếc dù vàng", "dù vàng"]
    segment_ids: [YS-LN02/Text/part0030.xhtml/p000746]
    rationale: "Theo đề xuất của argon-review, diễn đạt rõ nghĩa ẩn dụ kinh tế; vẫn là pending/non-canon."
    status: pending
risks:
  - "Các đề xuất thuật ngữ và quân sự trong báo cáo đều là pending, không tự nâng thành canon."
```
