# Review b17 — đối chiếu 44 đoạn

Báo cáo dưới dạng YAML (JSON là tập con của YAML); chỉ chứa diễn giải và thuật ngữ ngắn, không trích câu nguồn.

```yaml
{
  "role": "reviewer",
  "task_id": "vol-02-ch-06-b17-review",
  "state": "done",
  "review_path": "reviews/prose/vol-02/ch-06-b17-codex.md",
  "files_written": [
    "reviews/prose/vol-02/ch-06-b17-codex.md"
  ],
  "runtime_config": {
    "launcher_alias": "codex-personal",
    "via": "ai-isolator",
    "model": "gpt-6.1-sol",
    "effort": "medium",
    "note": "Ghi cấu hình reviewer từ config; không khởi chạy thêm worker."
  },
  "source_verification": {
    "path": "work/vol-02/batches/ch-06-b17-source.jsonl",
    "expected_sha256": "3d43967ca2b146408635d3eac527634fc11cb8f20212f5baf6c97505141df8ed",
    "actual_sha256": "3d43967ca2b146408635d3eac527634fc11cb8f20212f5baf6c97505141df8ed",
    "hash_match": true,
    "source_units": 44,
    "translation_units": 44,
    "ordered_ids_match": true
  },
  "counts": {
    "reviewed": 44,
    "nghiem_trong": 0,
    "vua": 7,
    "nhe": 6,
    "total_findings": 13,
    "pending_term_groups": 7,
    "local_recommendations": 5
  },
  "validator": "not_run",
  "diff_check": "not_run",
  "commit": null,
  "findings": [
    {
      "id": "F01",
      "severity": "vừa",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000510"
      ],
      "issue": "Thu hẹp omission thành hành vi không tố giác; luật hiện hành cũng dễ bị hiểu là luật của thế giới hiện tại.",
      "evidence": "Nguồn đang xét trách nhiệm do không thực hiện hành động, rồi mới đặt vấn đề nghĩa vụ báo cáo; không xác lập tên tội hoặc hệ thống luật.",
      "resolution": "Dùng Theo pháp luật hiện đại, đó là hành vi không hành động; giữ câu sau về nghĩa vụ báo cáo.",
      "confidence": 0.94,
      "status": "open"
    },
    {
      "id": "F02",
      "severity": "vừa",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000510",
        "YS-LN02/Text/part0030.xhtml/p000515",
        "YS-LN02/Text/part0030.xhtml/p000516",
        "YS-LN02/Text/part0030.xhtml/p000521",
        "YS-LN02/Text/part0030.xhtml/p000543",
        "YS-LN02/Text/part0030.xhtml/p000551"
      ],
      "issue": "Giọng nội tâm luân phiên tôi/mình, trái lựa chọn tạm được self-check nêu.",
      "evidence": "Các đoạn này là tự suy nghĩ của Tanya, cùng tuyến với p000512/p000517/p000536/p000550/p000553; ngôi ba tại p000518/p000528/p000535 là tuyến khác.",
      "resolution": "Thống nhất tự quy chiếu nội tâm là mình; không thay tôi trong lời thoại xin lỗi p000514. Chọn chúng ta cho suy nghĩ về nhiệm vụ chung, giữ họ/chúng cho đối phương.",
      "confidence": 0.95,
      "status": "open"
    },
    {
      "id": "F03",
      "severity": "vừa",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000516"
      ],
      "issue": "Mất nhấn mạnh kiểu chữ; self-check kết luận không có nhấn mạnh là sai.",
      "evidence": "XHTML trong package có đúng một thẻ em, ở tiếng hô yee-haw; bản dịch chỉ đặt ngoặc kép.",
      "resolution": "Giữ nhấn mạnh cho tiếng hô trong biểu diễn bản dịch mà pipeline hỗ trợ; nếu dùng Markdown thì *yee-haw*. Ngoặc kép không thay cho nhấn mạnh. Coordinator giao translator cập nhật self-check cùng bản dịch.",
      "confidence": 1,
      "status": "open"
    },
    {
      "id": "F04",
      "severity": "nhẹ",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000519"
      ],
      "issue": "Cậu tạo mức thân mật chưa có căn cứ, đồng thời vốn là vậy mà làm mờ ý không thể làm khác bản tính.",
      "evidence": "Package cho thấy chỉ huy đang trấn an rồi phân công; không đủ căn cứ xác nhận quan hệ thân mật hoặc người được trấn an.",
      "resolution": "Dùng Không sao. Bản tính như vậy thì cũng khó làm khác được. Được rồi, Trung úy König, tiếp nhận quyền chỉ huy của Trung úy Weiss.",
      "confidence": 0.87,
      "status": "open"
    },
    {
      "id": "F05",
      "severity": "nhẹ",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000521"
      ],
      "issue": "Tự ý dễ gợi làm trái quyền hạn.",
      "evidence": "Người nói điều chỉnh chỉ huy theo quyền tùy nghi của mình; nguồn không nói vi phạm mệnh lệnh.",
      "resolution": "Dùng mình quyết định sắp xếp lại hệ thống chỉ huy, tránh gợi hành động không được phép.",
      "confidence": 0.9,
      "status": "open"
    },
    {
      "id": "F06",
      "severity": "nhẹ",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000528",
        "YS-LN02/Text/part0030.xhtml/p000529"
      ],
      "issue": "Họ/đưa được pháp sư làm mờ bên thực hiện và tính chất đẩy lùi đối phương.",
      "evidence": "p000527–p000529 nói nhiệm vụ lực lượng Tanya và mục đích ngăn địch tiếp cận máy bay/pháo binh.",
      "resolution": "p000528 dùng lực lượng của Tanya đẩy được các pháp sư địch ra khỏi những khu vực có thể tấn công ở rìa thành phố; p000529 dùng lực lượng ấy thay họ nếu cần. Không diễn giải thành tiêu diệt hoặc giải cứu.",
      "confidence": 0.86,
      "status": "open"
    },
    {
      "id": "F07",
      "severity": "vừa",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000532"
      ],
      "issue": "Cô trong câu chất vấn làm lệch sắc thái quân sự khi cấp dưới nói với chỉ huy.",
      "evidence": "p000530 gọi chức vụ, p000531 là chỉ thị và p000533 xác nhận sự do dự của thành viên đại đội; không có dấu hiệu chuyển sang quan hệ ngang hàng.",
      "resolution": "Dùng …Chắc chứ ạ? để giữ do dự và quan hệ cấp dưới mà không gán giới/tuổi; thay thế: …Chỉ huy chắc chứ ạ?",
      "confidence": 0.94,
      "status": "open"
    },
    {
      "id": "F08",
      "severity": "vừa",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000533"
      ],
      "issue": "Dọn sạch chiến trường dễ thành thu dọn vật chất, che mất nghĩa tác chiến của mopping up.",
      "evidence": "Câu nói rõ sự ngần ngại tấn công ở giai đoạn tiếp theo; đây là hoạt động chiến đấu, không phải thu dọn chiến trường.",
      "resolution": "Dùng giai đoạn truy quét; không thêm tàn quân vì nguồn chưa xác định trạng thái lực lượng địch.",
      "confidence": 0.96,
      "status": "open"
    },
    {
      "id": "F09",
      "severity": "nhẹ",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000539"
      ],
      "issue": "Nuốt lời vào trong có thể gợi nuốt lời hứa và kém tự nhiên.",
      "evidence": "Đối tượng bị kìm lại là điều họ muốn nói, không phải lời hứa.",
      "resolution": "Dùng tất cả đều đủ chín chắn để giữ những lời ấy trong lòng; có thể sửa dù tốt hay xấu thành dù điều đó tốt hay xấu.",
      "confidence": 0.94,
      "status": "open"
    },
    {
      "id": "F10",
      "severity": "vừa",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000542"
      ],
      "issue": "Pháo kích thu hẹp bombardment về riêng pháo binh.",
      "evidence": "p000541 vừa giao liên lạc cả pháo binh lẫn đơn vị máy bay ném bom; package không chỉ rõ riêng bên nào thực hiện đợt đánh tiếp theo.",
      "resolution": "Dùng đợt oanh kích sẽ kết thúc mọi chuyện, hoặc đợt bắn phá; giữ điều kiện đầu hàng/không đầu hàng.",
      "confidence": 0.9,
      "status": "open"
    },
    {
      "id": "F11",
      "severity": "nhẹ",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000546"
      ],
      "issue": "Các anh thêm giới tính cho cả đơn vị; trực tiếp yểm trợ kém rõ như tên nhiệm vụ.",
      "evidence": "Nguồn giao Đại đội 2 vai trò direct support, không xác định giới tính người nhận lệnh hoặc đối tượng được yểm trợ.",
      "resolution": "Dùng Đại đội 2, đảm nhiệm yểm trợ trực tiếp. Không tự thêm bảo vệ ai hoặc nhiệm vụ hộ tống.",
      "confidence": 0.94,
      "status": "open"
    },
    {
      "id": "F12",
      "severity": "nhẹ",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000547"
      ],
      "issue": "Xác suất lớn hơn không rằng là cấu trúc gượng; biết suy nghĩ mang thêm sắc thái chê trí tuệ.",
      "evidence": "Nguồn giữ điều kiện hành xử hợp lý và khả năng đầu hàng nhỏ nhưng khác không.",
      "resolution": "Dùng Nếu họ hành xử hợp lý thì vẫn có chút khả năng họ sẽ chọn đầu hàng. Giữ giả định nếu có phiên tòa và mục đích biện hộ.",
      "confidence": 0.92,
      "status": "open"
    },
    {
      "id": "F13",
      "severity": "vừa",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000551"
      ],
      "issue": "Dự phòng khả năng đó không rõ đang dự phòng đầu hàng hay đánh tiêu diệt.",
      "evidence": "Lập luận vừa nêu gánh nặng nếu nhiều người đầu hàng, vừa nói cấp trên mặc định phải đánh; lời tự suy nghĩ đề nghị chừa phương án cho bất định.",
      "resolution": "Dùng Mình nghĩ vẫn nên chừa phương án cho cả khả năng họ đầu hàng; giữ cân nhắc giảm chi phí. Không thêm kế hoạch giam giữ hoặc trách nhiệm pháp lý.",
      "confidence": 0.86,
      "status": "open"
    }
  ],
  "unresolved_findings": [
    "F01",
    "F02",
    "F03",
    "F04",
    "F05",
    "F06",
    "F07",
    "F08",
    "F09",
    "F10",
    "F11",
    "F12",
    "F13"
  ],
  "term_recommendations": [
    {
      "id": "B17-T01",
      "source_term": "omission",
      "proposed_vi": "hành vi không hành động",
      "alternatives_vi": [
        "sự không hành động",
        "việc không thực hiện nghĩa vụ hành động"
      ],
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000510"
      ],
      "rationale": "Giữ khái niệm rộng; việc báo cáo là bước xét nghĩa vụ tiếp theo. Không dùng tên tội không tố giác hoặc khẳng định luật nào áp dụng.",
      "confidence": 0.94,
      "status": "pending",
      "canon": false
    },
    {
      "id": "B17-T02",
      "source_term": "sortie",
      "proposed_vi": "xuất kích",
      "alternatives_vi": [
        "ra giao chiến",
        "đưa lực lượng ra chặn đánh"
      ],
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000511",
        "YS-LN02/Text/part0030.xhtml/p000525"
      ],
      "rationale": "p000511 nói hoạt động chiến đấu trên không; p000525 là địch ra đánh chặn. Xuất kích phù hợp cả hai mà không suy cơ cấu binh chủng.",
      "confidence": 0.98,
      "status": "pending",
      "canon": false
    },
    {
      "id": "B17-T03",
      "source_term": "Ma’am / Lieutenant / Commander",
      "proposed_vi": "Thưa thiếu tá / Trung úy / chỉ huy",
      "alternatives_vi": [
        "Thưa chỉ huy cho Ma’am nếu thiếu căn cứ cấp bậc",
        "giữ Lieutenant như nhãn cấp bậc nếu có xung đột được cung cấp"
      ],
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000514",
        "YS-LN02/Text/part0030.xhtml/p000519",
        "YS-LN02/Text/part0030.xhtml/p000524",
        "YS-LN02/Text/part0030.xhtml/p000530"
      ],
      "rationale": "Giữ thiếu tá dựa riêng lựa chọn tạm kế thừa được self-check xác nhận, không suy Ma’am tự nó nghĩa là thiếu tá. Trung úy theo ánh xạ tạm đã giao, không suy tiểu cấp từ lore. Commander là chức vụ/lời gọi, không quy thành quân hàm.",
      "confidence": 0.84,
      "status": "pending",
      "canon": false
    },
    {
      "id": "B17-T04",
      "source_term": "Second Company",
      "proposed_vi": "Đại đội 2",
      "alternatives_vi": [
        "Đại đội thứ hai",
        "Đại đội Hai"
      ],
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000546"
      ],
      "rationale": "Số thứ tự đơn vị được nguồn nêu; dạng chữ số gọn trong khẩu lệnh. Không thêm phiên hiệu tiểu đoàn hoặc đối tượng yểm trợ.",
      "confidence": 0.99,
      "status": "pending",
      "canon": false
    },
    {
      "id": "B17-T05",
      "source_term": "the brass",
      "proposed_vi": "giới chỉ huy cấp cao",
      "alternatives_vi": [
        "cấp trên",
        "các cấp chỉ huy"
      ],
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000551"
      ],
      "rationale": "Cụm khẩu ngữ hướng tới tầng chỉ huy cao, không chỉ mọi cấp chỉ huy. Giữ tầng quyền lực, tránh giới tướng lĩnh vì chưa biết cấp hàm.",
      "confidence": 0.93,
      "status": "pending",
      "canon": false
    },
    {
      "id": "B17-T06",
      "source_term": "urban warfare",
      "proposed_vi": "tác chiến đô thị",
      "alternatives_vi": [
        "chiến đấu trong đô thị"
      ],
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000534"
      ],
      "rationale": "Nguồn giới hạn loại hoạt động nằm ngoài nhiệm vụ chống pháp sư, không nói đơn vị miễn mọi hoạt động tại thành phố.",
      "confidence": 0.99,
      "status": "pending",
      "canon": false
    },
    {
      "id": "B17-T07",
      "source_term": "mopping up",
      "proposed_vi": "truy quét",
      "alternatives_vi": [
        "quét sạch lực lượng địch còn lại",
        "truy quét tàn quân nếu nguồn sau xác nhận"
      ],
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000533"
      ],
      "rationale": "Giữ nghĩa tác chiến và tránh nghĩa vệ sinh/thu dọn; chưa đủ căn cứ gọi lực lượng địch là tàn quân.",
      "confidence": 0.96,
      "status": "pending",
      "canon": false
    }
  ],
  "local_recommendations": [
    {
      "id": "B17-L01",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000519"
      ],
      "proposed_vi": "Bỏ đại từ ở câu trấn an, giữ tên/cấp bậc tại câu phân công",
      "alternatives_vi": [
        "cậu nếu có căn cứ quan hệ thân mật được giao"
      ],
      "confidence": 0.87,
      "rationale": "Chức năng trấn an có căn cứ; mức thân mật chưa được xác lập.",
      "status": "pending",
      "canon": false
    },
    {
      "id": "B17-L02",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000532"
      ],
      "proposed_vi": "…Chắc chứ ạ?",
      "alternatives_vi": [
        "…Chỉ huy chắc chứ ạ?"
      ],
      "confidence": 0.94,
      "rationale": "Giữ lời hỏi do dự của cấp dưới; không gán giới tính cho cách gọi.",
      "status": "pending",
      "canon": false
    },
    {
      "id": "B17-L03",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000544"
      ],
      "proposed_vi": "Nói cách khác, chúng ta sẽ lấy họ làm cái cớ biện minh cho mình.",
      "alternatives_vi": [
        "Giữ bản dịch hiện tại"
      ],
      "confidence": 0.94,
      "rationale": "Mạch p000543–p000547 hướng tới dùng phản ứng đối phương và việc cảnh báo để tự biện hộ; họ là địch. Không thay bằng đơn vị ném bom/pháo binh và không diễn giải thành chính nghĩa được xác nhận.",
      "status": "pending",
      "canon": false
    },
    {
      "id": "B17-L04",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000546"
      ],
      "proposed_vi": "Đại đội 2, đảm nhiệm yểm trợ trực tiếp.",
      "alternatives_vi": [
        "Đại đội 2, làm nhiệm vụ yểm trợ trực tiếp."
      ],
      "confidence": 0.94,
      "rationale": "Lược đại từ chưa đủ căn cứ giới tính; direct support là vai trò, chưa xác định bên nhận.",
      "status": "pending",
      "canon": false
    },
    {
      "id": "B17-L05",
      "segment_ids": [
        "YS-LN02/Text/part0030.xhtml/p000551"
      ],
      "proposed_vi": "Giới chỉ huy cấp cao; chừa phương án cho cả khả năng địch đầu hàng",
      "alternatives_vi": [
        "Cấp trên; tính đến cả khả năng đầu hàng"
      ],
      "confidence": 0.86,
      "rationale": "Tách chủ thể cấp trên khỏi Tanya; hedge giữ cửa cho khả năng trái giả định đánh tiêu diệt, không tự dựng phương án hậu cần.",
      "status": "pending",
      "canon": false
    }
  ],
  "emphasis_audit": {
    "segments_with_em": [
      "YS-LN02/Text/part0030.xhtml/p000516"
    ],
    "other_assigned_segments": "Không có thẻ nhấn mạnh trong XHTML package.",
    "self_check_correction": "Kết luận không có nhấn mạnh cần sửa; bản dịch cần bảo toàn tiếng hô được nhấn."
  },
  "coverage": [
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000510",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F01",
        "F02"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000511",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Ý so sánh Rudel và xuất kích giữ được; không kiểm chứng lịch sử ngoài package."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000512",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ giả định làm bổn phận cá nhân, giọng mình."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000513",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ lời cảm thán và mỉa mai về luật."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000514",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ xin lỗi; thiếu tá chỉ là lựa chọn tạm kế thừa, không nghĩa từ vựng của kính ngữ."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000515",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F02"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000516",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F02",
        "F03"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000517",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ chất vấn nội tâm về chiến dịch phi lý."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000518",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ chuyển ngôi ba và nó; chưa khao khát cái chết là lối cường điệu, không gán ý định tự sát."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000519",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F04"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000520",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Rõ phù hợp đáp khẩu lệnh."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000521",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F02",
        "F05"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000522",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Khỏe mạnh chấp nhận được; còn đủ sức chiến đấu là lựa chọn làm rõ tùy ý."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000523",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ cảnh báo phục kích và hậu quả coi thường; có thể dùng lao xuống áp sát để rõ chuyển động swoop."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000524",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ lời báo rút lui/cố thủ; chỉ huy là chức vụ."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000525",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ giả định địch xuất kích đánh chặn và quan hệ đối lập."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000526",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ hủy xung phong và tiếp tục gây sức ép."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000527",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ giới hạn nhiệm vụ ven thành phố."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000528",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F06"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000529",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F06"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000530",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ câu hỏi gọi chức vụ."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000531",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ thứ tự đẩy địch ra xa rồi cảnh báo đầu hàng."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000532",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F07"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000533",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F08"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000534",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Tác chiến đô thị phù hợp; chúng ta bao gồm đơn vị Tanya, không phải đối phương."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000535",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ ngôi ba nó, hình ảnh vấy bẩn và ưu tiên rút khỏi nơi đó sau cảnh báo."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000536",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ tự quy chiếu mình và lập luận không trực tiếp giết."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000537",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ câu nội tâm bỏ lửng."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000538",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ đáp chấp nhận sau do dự."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000539",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F09"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000540",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ so sánh công việc/nhẫn nhịn và mệnh lệnh làm cái cớ; không đảo quan hệ điều kiện."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000541",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ hai bên nhận thông báo và cảnh báo đầu hàng, không chuyển thành lệnh bắn ngay."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000542",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F10"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000543",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F02"
      ],
      "note": "Giữ dự đoán gần chắc chắn, dù chẳng đời nào hơi mạnh; sửa đại từ theo F02."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000544",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Không bắt buộc sửa nghĩa; chọn tạm họ là địch, cái cớ biện minh theo B17-L03."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000545",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ hỏi nhu cầu bảo vệ bằng chủ thể lược bỏ; không tự gán người nói/người nhận."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000546",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F11"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000547",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F12"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000548",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ đề nghị liên lạc; không có căn cứ bắt buộc đổi mệnh lệnh sang lời rủ."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000549",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ nghịch lý chi phí và chủ nghĩa tư bản."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000550",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ mong đầu hàng vì lợi ích riêng, giá trị thời gian/đạn dược; muốn là cách diễn đạt chấp nhận được."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000551",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [
        "F02",
        "F13"
      ],
      "note": "Đã đối chiếu; xử lý cụ thể tại findings được dẫn."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000552",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ giới hạn tầm suy nghĩ khi đang trực tiếp tham chiến."
    },
    {
      "segment_id": "YS-LN02/Text/part0030.xhtml/p000553",
      "reviewed_dimensions": [
        "meaning",
        "prose",
        "viewpoint_pronouns",
        "emphasis",
        "rank_terminology"
      ],
      "findings": [],
      "note": "Giữ mình và chuyển sang hành động."
    }
  ],
  "risks": [
    "Các lựa chọn đều pending/non-canon. Không có quyết định canon ảnh hưởng cốt truyện cần hỏi người dùng; reviewer không tự sửa ledger hoặc canon.",
    "Ma’am không tự xác định cấp hàm; thiếu tá được giữ chỉ theo lựa chọn kế thừa mà self-check cung cấp. Không mở b16 để xác nhận thêm.",
    "Chủ thể ở p000545 và bên nhận yểm trợ tại p000546 chưa đủ căn cứ; giữ lược bỏ/trung tính.",
    "Một lệnh tìm chuỗi b17 trong ledger đã trả thêm phần của các chương khác ngoài phạm vi; sau đó đọc lại đúng chapter6_b17_translator_proposals. Không dùng các mục ngoài phạm vi làm căn cứ. Đây là sai lệch phạm vi đọc của lượt review.",
    "Chưa có sửa dịch hoặc xác minh sau sửa; done chỉ nghĩa là báo cáo hoàn tất, không phải lô đã được duyệt."
  ],
  "next_action": "Coordinator ghi đề xuất pending vào ledger/handoff; giao translator đang giữ lease sửa F01–F13 và self-check nhấn mạnh, rồi chạy validator/diff-check và đối chiếu lại các findings. Không mở rộng batch."
}
```
