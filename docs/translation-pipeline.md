# Điều phối dịch bằng Herdr

Bộ này là cấu hình và hợp đồng vai trò cho coordinator chạy liên tục. `translate.sh` quản lý lifecycle và ownership; coordinator AI thực hiện vòng dịch theo persona. Script không phải daemon tự dịch và không khởi động Herdr server. Mọi lệnh thực dùng cú pháp CLI 0.9.0 đã đọc từ `herdr --help`, `herdr agent`, `herdr pane`, `herdr --skill`.

## Khởi chạy

Chạy từ pane được Herdr quản lý, trong checkout của dự án. Cần Bash, Git, jq, flock, zsh, Python/PyYAML, Herdr tương thích và `agy`; alias `codex-personal` trong `~/.zshrc` phải gọi ai-isolator profile personal. Coordinator/reviewer chạy `agy --model gemini-4-argon-medium --mode auto --dangerously-skip-permissions` và bỏ `--effort` vì mức Medium nằm trong model variant. Translator và semantic regression chạy `codex-personal --model gpt-6-luna --config model_reasoning_effort=medium --sandbox danger-full-access --ask-for-approval never`. Polisher chạy `agy --model gemini-3.8-flash-medium --effort medium --mode auto --dangerously-skip-permissions`. `agy` không có subcommand `review`: đọc persona để xác định vai trò. Doctor kiểm help và model registry bằng lệnh đọc, không gửi task. Không gọi `herdr agent start --kind codex` vì lệnh đó có thể chạy Codex gốc.

Đường dẫn nguồn chỉ đặt trong `project.local.yml` bị Git bỏ qua. `source_dir` được kiểm tra bằng metadata thư mục/tên đuôi tệp; preflight không mở sách. Git phải sạch trước bootstrap/recovery, và `work/run-state/` phải không được theo dõi.

```bash
scripts/translate.sh doctor
scripts/translate.sh up --dry-run
scripts/translate.sh up
scripts/translate.sh status
scripts/translate.sh logs
scripts/translate.sh down --dry-run
scripts/translate.sh down
scripts/translate.sh resume
```

`up` dùng workspace/tab của pane gọi, tạo một pane anh em tại đúng root của checkout, giữ focus. Workspace hiện tại có thể chứa pane của người dùng: script không nhận ownership các pane đó. `up` giữ coordinator đã đăng ký nếu còn chạy, không gửi prompt lặp. `resume` dùng recovery persona và trạng thái lưu; coordinator đang working được giữ nguyên. Không gọi các lệnh này từ ngoài Herdr hoặc dùng `down` ngay trong pane coordinator cần đóng.

Dry-run chỉ đọc kiểm tra và in kế hoạch, không tạo run-state, lock, pane, agent; không gửi prompt hoặc đóng pane. `down --dry-run` vẫn cần session file hợp lệ để xác minh quyền sở hữu.

## Vai trò và vòng lặp

| Vai trò | Quyền ghi |
| --- | --- |
| coordinator | handoff/queue metadata và work/run-state/; nâng nguyên ứng viên đã được Luna duyệt; stage/commit allowlist của lô |
| translator | translations/ của lô và reviews/semantic/ của lô |
| reviewer (Gemini 4 Argon qua agy) | reviews/prose/ của task; đề xuất locked choices để coordinator ghi snapshot |
| polisher (Gemini 3.8 Flash qua agy) | translations/ của lô: chỉ `.gemini.jsonl` và `.gemini-change-log.yml` |
| semantic_regression (Luna) | reviews/semantic/ của task; không sửa bản dịch |
| recovery | work/run-state/ trong pha phục hồi |

Mỗi agent đọc `agents/shared.md` và persona riêng. Coordinator không đọc chữ nguồn hoặc dịch; có thể gọi adapter chuẩn bị nguồn để tạo metadata/handoff/package. Translator báo thuật ngữ mới, coordinator ghi sổ pending cục bộ; không persona nào tự sửa canon. Khi người dùng chốt, một nhiệm vụ sửa canon riêng phải được giao rõ ràng.

Mỗi lần bắt đầu và sau commit, coordinator dựng lại queue từ `segments/vol-*/manifest.yml`, handoff, tên bản dịch, Git và review receipts. Dùng segment_id, ưu tiên story sớm nhất chưa hoàn tất (kể cả lô đã commit nhưng còn review mở). Bỏ copyright/newsletter/bìa/mục lục/trang ảnh/phụ lục ảnh. Lô 600–900 từ giữ nguyên segment. Không dừng chỉ vì đổi chương/tập.

Vòng: lease + allowlist → `translator_luna` → validator/self-check → `terminology_review_argon` mỗi batch → translator sửa/signoff → snapshot locked choices → `prose_polish_gemini` bằng 3.8 Flash → `semantic_regression_luna` → coordinator nâng ứng viên → validator/diff-check → commit riêng lô → checkpoint → lô tiếp. `terminology_review_argon` thay stage Claude theo lựa chọn mới của người dùng. Risk flags vẫn là thông tin review; không cho phép bỏ qua bước khóa trước polish.

Task theo pipeline mới chỉ hoàn tất khi có commit, validator đạt, mọi phản biện bắt buộc đã xử lý, không còn lỗi nghiêm trọng/vừa và ứng viên đã có receipt Luna hợp lệ rồi được nâng. Các lô có review tồn đọng phải giải quyết trước bước polish. Task chỉ đổi config/persona không chạy dịch hoặc tự lập hàng đợi mới; phần đã dịch xong chỉ được chuốt khi nằm trong phạm vi nhiệm vụ cụ thể. Receipt/commit lịch sử vẫn được giữ để audit, không tự diễn giải thành đã qua bốn stage mới.

## Chuốt văn và nâng ứng viên

Flash đọc `agents/gemini-polisher.md`, source package cục bộ đúng batch, bản đã được Argon signoff, canon và snapshot `handoffs/vol-NN/ch-NN-bNN-locked-choices.yml`. Snapshot ghi `task_id`, `baseline_sha256`, `source_sha256`, `glossary_version`, `choices: [{segment_id, kind, value}]` và locked terms nếu cần. Các lựa chọn tạm khóa cho batch vẫn không phải canon.

Flash có thể chỉnh cú pháp, nhịp, kết hợp từ và dấu câu trong một segment; giữ nguyên hệ quy chiếu, điểm nhìn nội tâm “mình”, tên/xưng hô/thuật ngữ, chủ thể, phủ định, tình thái, thời gian, quan hệ nhân quả và thông tin. Không thêm hình ảnh, cảm xúc, mức độ, chi tiết vật lý, chú thích hoặc sắc thái phán xét. Chỉ đổi trường `translation`, giữ mọi metadata và thứ tự/mã đoạn.

Ứng viên `translations/vol-NN/ch-NN-bNN.gemini.jsonl` tách khỏi baseline `ch-NN-bNN.jsonl`. Log `ch-NN-bNN.gemini-change-log.yml` chỉ gồm task_id và entries `{segment_id, types: [syntax|rhythm|diction|punctuation], escalate: false}`; chỗ đòi đổi locked choice giữ nguyên baseline, ghi `types: [], escalate: true`. Argon/coordinator xử lý bằng phương án tạm có căn cứ hoặc giữ baseline literal/trung tính, không chờ quyết định pending thường và không nâng canon.

Luna đọc `agents/semantic-regression-checker.md` và kiểm toàn bộ source/baseline/candidate/locked choices. Receipt YAML trong `reviews/semantic/` ghi `reviewer_model: gpt-6-luna`, `decision`, checked_segment_ids đầy đủ, findings và SHA-256 raw bytes của source_package/baseline/candidate/locked choices/change_log. `critical` và `locked_choice_violation` làm reject; `style_only` được báo nhưng không chặn. Nếu sắc thái làm đổi nghĩa/tình thái/mức độ/điểm nhìn thì phải xếp critical. Khi reject, chỉ sửa các vị trí bị báo, sau đó Luna kiểm lại batch trên các hash mới.

Coordinator dùng `tools/promote_polished_translation.py` để kiểm receipt và artifact trước khi nâng; mặc định công cụ chỉ đọc. `--apply --coordinator <holder>` chỉ dành cho coordinator đã được ghi quyền sửa đúng bản chuẩn trong handoff/checkpoint, sau khi worker nhả lease. Công cụ kiểm hash, metadata/segment order, acceptance và validator, rồi thay nguyên ứng viên vào baseline bằng atomic replace. Coordinator không được tự sửa câu dịch. Mọi sửa đầu vào đều làm receipt cũ mất hiệu lực. Chi tiết tham số và handoff promotion xem `tools/README.md`.

**Adapter chuẩn bị EPUB dùng chung:** `tools/extract_epub.py vol-NN` nhận diện EPUB theo số LN, đọc thứ tự spine và lấy ranh giới chương từ EPUB 3 TOC hoặc NCX; metadata `epub:type` và đường dẫn lọc bìa, mục lục, bản quyền, phụ lục và ghi chú. Chapter fragment được ánh xạ tới đoạn văn chứa anchor hoặc đoạn kế tiếp. Vol 1 giữ profile audit và mã đoạn hiện có. Các EPUB 2–14 đã được dry-run; adapter từ chối volume nếu không tìm được ranh giới chương an toàn. Manifest chỉ ghi metadata; chữ nguồn và XHTML nằm trong `work/` bị Git bỏ qua. `tools/plan_batches.py vol-NN chapter-NN` lập lô riêng cho chương được yêu cầu.

## Session, checkpoint và recovery

`work/run-state/herdr-session.json` chỉ lưu metadata cục bộ: schema/managed_by, root riêng, workspace/tab, owned_panes với role, pane_id, terminal_id, agent_session_id, state và prompt_delivery. Coordinator phải đăng ký mỗi pane ngay khi tạo và agent identity khi nhận diện; dùng atomic replace. Pane không ghi trong tệp không được script dừng. Những tệp này, pending ledger và logs không vào Git; không chứa nguồn, token hoặc khóa.

Checkpoint `work/run-state/translation-coordinator.yml` phải có:

```yaml
checkpoint_generation: 1
last_completed_batch: null
last_commit: null
next_handoff: null
active_translation_editor: null
active_worker: null
batch_allowlist: []
validator_receipts: []
review_closures: []
pipeline_stage: translator_luna
polish_artifacts: {} # paths/hashes của baseline, candidate, locked choices, change_log
semantic_regression_receipt: null
promotion_receipt: null
pending_terms_new: []
unresolved_issues: []
summary: "Tối đa 500 từ; không có chữ nguồn."
recovery:
  received_generation: null
shutdown:
  request_id: null
  acknowledged: false
```

Recovery kiểm tra Git/handoff/receipts, tái dựng queue và live lease. Sau 4 lô hoặc cảnh báo context, coordinator ghi checkpoint và thử `/compact`. Nếu không hỗ trợ/thất bại, tạo coordinator mới trong pane anh em, đăng ký ownership với role recovery; coordinator cũ chỉ thoát sau ACK `received_generation`. Sau ACK, atomic chuyển role mới thành coordinator, role cũ thành recovery và cập nhật coordinator_name, giữ nguyên các ID khác. Session luôn có đúng một coordinator. Script không giả định Herdr có lệnh compact riêng.

`down` gửi **một** request checkpoint mang UUID, chờ đúng ACK trong checkpoint và lease đã trả. Nếu timeout/blocked, đọc màn hình và giữ nguyên pane; không gửi lặp hoặc ép đóng. Sau ACK, xác minh lại terminal ID, cwd và agent session ID của mọi pane, yêu cầu agent idle/done hoặc shell ở foreground, rồi đóng worker trước và coordinator cuối. Không gọi pkill, Git reset, xóa work/, hoặc đóng server/workspace/pane không thuộc session. Session được giữ lại ở trạng thái stopped để audit/recovery.

`resume` không tự xử lý checkpoint hỏng, lease chưa rõ hoặc Git bẩn. Nếu coordinator đã mất, chạy resume từ một pane trong workspace/tab đã lưu; script không tạo pane phục hồi vào tab khác. Tab/workspace đã mất cần người điều phối đối chiếu session/checkpoint trước khi tạo phiên mới. Doctor nêu lỗi và bước khắc phục; giữ dữ liệu để người điều phối đối chiếu. Lỗi Herdr/agent, delivery uncertain, validator/diff-check lỗi, lỗi nghiêm trọng sau sửa, thay đổi Git ngoài lô và canon làm đổi cốt truyện đều dừng pipeline.

## Kiểm tra bộ quản lý

```bash
bash -n scripts/translate.sh scripts/test_translate.sh
bash scripts/test_translate.sh
shellcheck scripts/translate.sh scripts/test_translate.sh # nếu đã cài
git diff --check
```

Test dựng Git fixture trong mktemp và mock Herdr/zsh/agy. Nó kiểm tra model và cổng acceptance, đối số sai, down thiếu session, dry-run không thay filesystem/Herdr, ownership sai, shutdown thiếu ACK, vòng up/down giả lập gồm hai vai trò mới và không gọi backend bị cấm. Kiểm thử công cụ promotion dùng source/bản dịch giả để xét receipt thiếu/cũ, locked-choice violation và promotion hợp lệ. Không có agent hoặc server thật được khởi chạy. `logs` chỉ in control events; không ghi dump màn hình có thể chứa nguồn.
