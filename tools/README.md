# Chuẩn bị EPUB volume

Chạy từ gốc kho, với `source_dir` trong `project.local.yml` trỏ đến thư mục
EPUB ngoài kho. Dùng môi trường và phụ thuộc hiện có trong `pyproject.toml`.

```sh
uv run python tools/extract_epub.py vol-02 --dry-run
uv run python tools/extract_epub.py vol-02
uv run python tools/validate_segments.py vol-02
```

Dry-run đọc và kiểm tra nhưng không tạo thư mục/tệp dữ liệu. Chạy thật tạo:

- `segments/vol-NN/manifest.yml`: metadata, locator, markup dạng cấu trúc không
  chứa chữ nguồn, vị trí ảnh/pagebreak/space-break và liên kết chú thích; lưu Git.
- `work/vol-NN/source.jsonl`: chữ và XHTML của từng p, chỉ cục bộ, Git bỏ qua.
  Không thêm bằng `git add -f`, sao chép sang thư mục được theo dõi hoặc tải lên.

Vol 1 giữ profile audit và mã đoạn cũ. Vol 2–14 dùng TOC EPUB 3 hoặc NCX để
nhận diện chương theo spine; metadata `epub:type` và đường dẫn loại trang bìa,
mục lục, bản quyền, phụ lục và ghi chú. Nếu TOC trỏ tới fragment, adapter ánh xạ
anchor tới đoạn văn chứa nó hoặc đoạn tiếp theo. Một p là một đơn vị, kể cả p rỗng
khi đếm ordinal; mã p có sáu chữ số. Adapter không ghi nhãn chương hay chữ nguồn
vào manifest. Nếu không xác định được ranh giới chương an toàn, công cụ từ chối.
Không sao chép ảnh, OCR hoặc sửa EPUB.

SHA-256 nguồn được lưu trong manifest. Nếu bản nguồn đổi, lệnh từ chối ghi đè;
sau khi tự đối chiếu bản nguồn và tác động tới mã đoạn, có thể dùng:

```sh
uv run python tools/extract_epub.py vol-02 --force
```

`--force` chỉ bỏ chặn thay SHA; kiểm tra phạm vi/số đoạn vẫn bắt buộc. Cùng SHA
thì có thể chạy lại để tái tạo tệp. Nếu chạy bị gián đoạn giữa hai lần ghi tệp,
chạy lại rồi kiểm tra trước khi sử dụng dữ liệu. Adapter dùng chung cho LN 01–14;
vẫn cần dry-run và validator trước khi dùng một volume mới.

Công cụ dựng EPUB vẫn cần triển khai sau này; sản phẩm xuất sẽ nằm ở `output/`.

## Lập lô theo chương

Sau khi tách nguồn và kiểm tra danh mục, chạy:

```sh
uv run python tools/plan_batches.py vol-02 chapter-01 --dry-run
uv run python tools/plan_batches.py vol-02 chapter-01
uv run python tools/plan_batches.py vol-02 chapter-01 --check
```

Nếu dùng môi trường Python đã có PyYAML, có thể thay `uv run python` bằng
`python3`. Công cụ hỗ trợ volume và chapter có trong manifest; chỉ chạy chương
thuộc phạm vi nhiệm vụ.

Lệnh lập toàn bộ các lô của chương được chọn theo thứ tự nguồn, chỉ lấy đơn vị
`story`, giữ nguyên mã và không chia nhỏ một đơn vị. Từ được đếm theo regex
`[A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*`, cùng quy ước pilot: có tính số và
đơn vị ngày/địa điểm; từ có dấu nối hoặc dấu nháy bên trong được tính một lần.

Mỗi lô tạo hai tệp, đánh số từ `b01`:

- `handoffs/vol-NN/ch-NN-b01.yml`: metadata để lưu Git, gồm dải mã, số đoạn,
  số từ, SHA EPUB ghi trong manifest, phiên bản canon bằng SHA-256, đường dẫn
  và SHA gói nguồn, người giữ quyền sửa kế thừa từ handoff pilot, trạng thái
  `ready` và bốn điểm kiểm tra. Không có câu nguồn hoặc bản dịch.
- `work/vol-NN/batches/ch-NN-b01-source.jsonl`: các bản ghi nguồn nguyên đơn vị,
  gồm chữ và XHTML để đối chiếu nhấn mạnh; chỉ cục bộ, Git bỏ qua.

Ưu tiên mọi lô đạt 600–900 từ, sau đó ưu tiên điểm ngắt cấu trúc, rồi chọn
phương án gần 750 từ hơn. Pagebreak ở đầu đơn vị và ranh giới tài liệu được ưu tiên
hơn space-break; ngắt giữa hai đơn vị thường là phương án sau cùng. Pagebreak
nằm giữa một đơn vị không được dùng để chia đơn vị. Space-break được hiểu là
điểm trước đơn vị mang dấu đó; dấu ở p rỗng được ánh xạ tới p theo sau.
Có thể bổ sung ranh giới cảnh đã xác định bằng
`--scene-start SEGMENT_ID` (lặp lại nếu cần); công cụ không đoán cảnh từ chữ nguồn.

Lô đầu bắt đầu từ đơn vị truyện đầu tiên. Trong dải pilot Vol 1 lấy từ
`handoffs/pilot-01.yml`, chỉ cho phép ngắt ở pagebreak hoặc ranh giới cảnh/tài
liệu, tránh tách câu hỏi hay chỉ dẫn khỏi mạch ngữ cảnh vì đủ số từ. Quy tắc
này cho phép hai phần pilot nằm ở hai lô nếu giữa chúng có chuyển cảnh.

Nếu không thể đạt ngưỡng cho toàn chương, công cụ giữ đơn vị nguyên vẹn,
ưu tiên ranh giới cấu trúc/kết thúc chương và ghi lý do trong
`planning.word_count_exception`. `planning.boundary_after` cho biết loại điểm
ngắt; các ranh giới thường không được tự gọi là ranh giới cảnh.

`--dry-run` chỉ đọc và kiểm tra, không ghi tệp. `--check` kiểm tra tệp đã tạo
khớp kế hoạch và đầu vào hiện tại, gồm số từ, dải mã, nguồn và phiên bản canon.
Chạy lại cùng đầu vào không thay nội dung. Nếu tệp đã có khác nội dung dự kiến
(kể cả chủ sở hữu, trạng thái hoặc canon đã đổi), công cụ từ chối ghi đè;
cần điều phối viên xét việc bàn giao/lập lại kế hoạch trước khi thay tệp.

Không tự thêm tệp vào Git. Chỉ đưa handoff metadata vào Git, không dùng
`git add -f` với gói nguồn. Công cụ kiểm tra quy tắc bỏ qua và từ chối khi
`work/` có tệp được Git theo dõi hoặc đường dẫn đầu ra là liên kết tượng trưng.
Lập lô không dịch, không tạo bản nháp và không sửa canon hay EPUB.

## Kiểm tra JSONL bản dịch

Chạy validator từ gốc kho sau khi có JSONL cần kiểm tra:

```sh
uv run python tools/validate_translation.py \
  --handoff handoffs/vol-01/ch-00-b01.yml \
  --source work/vol-01/batches/ch-00-b01-source.jsonl \
  --translation translations/vol-01/ch-00-b01.jsonl
```

Công cụ kiểm tra JSONL, mã và thứ tự đoạn, trường bắt buộc, trạng thái, SHA
nguồn và phiên bản glossary theo handoff, trường/văn bản nguồn bị chép lại, cú
pháp nhấn mạnh Markdown và quy tắc Git bỏ qua gói nguồn. Thiếu nhấn mạnh trong
bản dịch khi nguồn có nhấn mạnh được báo cảnh báo. Có thể chạy kiểm tra tối thiểu
chỉ dùng dữ liệu giả bằng `uv run python tools/test_validate_translation.py`.

## Nâng bản đã chuốt bằng Gemini

`promote_polished_translation.py` chỉ nâng nguyên ứng viên `.gemini.jsonl`
sau khi Luna chấp nhận; không tự sửa văn bản. Chạy từ gốc kho:

```sh
uv run python tools/promote_polished_translation.py \
  --handoff handoffs/vol-02/ch-01-b01.yml \
  --source work/vol-02/batches/ch-01-b01-source.jsonl \
  --baseline translations/vol-02/ch-01-b01.jsonl \
  --candidate polish-candidates/vol-02/ch-01-b01.gemini.jsonl \
  --locked-choices handoffs/vol-02/ch-01-b01-locked-choices.yml \
  --change-log polish-candidates/vol-02/ch-01-b01.gemini-change-log.yml \
  --receipt reviews/semantic/vol-02/ch-01-b01-gemini-regression.yml
```

Mặc định chỉ đọc, trả `result: ready` nếu đạt. Chỉ coordinator thêm
`--apply --coordinator <identity>` sau khi được bàn giao quyền sửa bản chuẩn;
công cụ thay atomically bằng đúng bytes của ứng viên, giữ nguyên ứng viên và
in receipt promotion JSON để coordinator ghi checkpoint/handoff.

Handoff batch và checkpoint `work/run-state/translation-coordinator.yml`
(có thể chỉ định bằng `--checkpoint`) đều phải ghi lease:

```yaml
lease:
  holder: ys-coord-example # trùng --coordinator
  task_id: vol-02-ch-01-b01 # task_id handoff batch, không phải task review
  state: active
  allowlist:
    - translations/vol-02/ch-01-b01.jsonl
```

Checkpoint còn phải có `coordinator` và `active_translation_editor` trùng
holder, `active_worker: null`. Flash candidate/log nằm trong
`polish-candidates/`, tách khỏi bản chuẩn để có thể chạy đồng thời với
translator của batch khác. Chỉ một writer được sửa bản chuẩn trong
`translations/` tại một thời điểm; coordinator nhả lease và ghi promotion
receipt sau khi nâng.

Baseline phải `reviewed`/`approved`; ứng viên chỉ khác `translation`, giữ mọi
metadata và mã/thứ tự đoạn. Snapshot locked choices trong handoffs ghi
`task_id`, `baseline_sha256`, `source_sha256`, `glossary_version` và
`choices: [{segment_id, kind, value}]`, khớp baseline/handoff. Có thể khai báo
`choices: []` nếu không có lựa chọn cần khóa. Log dưới `polish-candidates/` gồm
`task_id`, `change_log` đầy đủ theo thứ tự đoạn; mỗi entry chỉ có `segment_id`,
`types: [syntax|rhythm|diction|punctuation]` và boolean `escalate`. Escalate
giữ baseline nguyên văn với `types: []`; không cần chặn pending thường.

Receipt kiểm hồi quy theo `agents/semantic-regression-checker.md`: `schema_version: 1`,
task_id, `reviewer_model: gemini-4-argon-low` (hoặc `gpt-6-luna` cho receipt lịch sử), `decision: accept`, checked_segment_ids
đầy đủ, findings và các SHA-256 raw bytes của baseline/candidate/snapshot/log/
source package. Receipt không có `critical` hoặc `locked_choice_violation`;
`style_only` được ghi nhưng không chặn. `source_sha256` của handoff là SHA
EPUB; `source_package_sha256` là SHA raw bytes JSONL, không được lẫn hai loại.

Công cụ kiểm validator, receipt, hash, scope và lease trước atomic replace;
đọc lại tất cả đầu vào ngay trước khi thay. Input đổi thì phải review lại,
không dùng receipt cũ. Gói nguồn chỉ được đọc dưới work đã Git bỏ qua và chưa
được theo dõi. Công cụ không tự chứng minh nghĩa hoặc xác thực provider:
Luna chịu trách nhiệm xét nghĩa; coordinator chịu trách nhiệm tạo receipt
đúng worker và giữ quyền sửa.

Kiểm thử dùng dữ liệu giả, không đọc hoặc nâng batch thật:

```sh
uv run python tools/test_promote_polished_translation.py
```
