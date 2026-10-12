# Điều phối dịch bằng Herdr

Bộ này là cấu hình và hợp đồng vai trò cho coordinator chạy liên tục. `translate.sh` quản lý lifecycle và ownership; coordinator AI thực hiện vòng dịch theo persona. Script không phải daemon tự dịch và không khởi động Herdr server. Mọi lệnh thực dùng cú pháp CLI 0.9.0 đã đọc từ `herdr --help`, `herdr agent`, `herdr pane`, `herdr --skill`.

## Khởi chạy

Chạy từ pane được Herdr quản lý, trong checkout của dự án. Cần Bash, Git, jq, flock, zsh, Python/PyYAML, Herdr tương thích và Claude CLI; alias `codex-personal` trong `~/.zshrc` phải gọi ai-isolator profile personal. Script nạp rc và khởi chạy alias với `gpt-6-luna`, effort `medium`, `--sandbox danger-full-access --ask-for-approval never`. Không gọi `herdr agent start --kind codex` vì lệnh đó có thể chạy Codex gốc.

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
| coordinator | handoff/queue metadata và work/run-state/; stage/commit allowlist của lô |
| translator | translations/ của lô và reviews/semantic/ của lô |
| reviewer (Claude) | reviews/prose/ của task |
| recovery | work/run-state/ trong pha phục hồi |

Mỗi agent đọc `agents/shared.md` và persona riêng. Coordinator không đọc chữ nguồn hoặc dịch; có thể gọi adapter chuẩn bị nguồn để tạo metadata/handoff/package. Translator báo thuật ngữ mới, coordinator ghi sổ pending cục bộ; không persona nào tự sửa canon. Khi người dùng chốt, một nhiệm vụ sửa canon riêng phải được giao rõ ràng.

Mỗi lần bắt đầu và sau commit, coordinator dựng lại queue từ `segments/vol-*/manifest.yml`, handoff, tên bản dịch, Git và review receipts. Dùng segment_id, ưu tiên story sớm nhất chưa hoàn tất (kể cả lô đã commit nhưng còn review mở). Bỏ copyright/newsletter/bìa/mục lục/trang ảnh/phụ lục ảnh. Lô 600–900 từ giữ nguyên segment. Không dừng chỉ vì đổi chương/tập.

Vòng: lease + allowlist → translator → validator/self-check → Claude mỗi lô chẵn hoặc cờ meaning/new_pending_terms/emphasis/validator_warning → translator sửa → validator/diff-check → coordinator commit riêng lô → checkpoint → lô tiếp. Cấu hình mới này dùng review mỗi lô chẵn và risk flags, thay lịch gom 20 term/10 batch của lượt chạy trước.

Chỉ coi hoàn tất khi có commit, validator đạt, mọi phản biện bắt buộc đã xử lý và không còn lỗi nghiêm trọng/vừa. Các lô b03–b05 trong repo hiện có báo cáo review tồn đọng: recovery phải xét báo cáo ấy trước khi chọn b06, không coi sự tồn tại JSONL là hoàn tất.

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

Test dựng Git fixture trong mktemp và mock toàn bộ Herdr/zsh/Claude. Nó kiểm tra đối số sai, down thiếu session, dry-run không thay filesystem/Herdr, ownership sai, shutdown thiếu ACK, vòng up/down giả lập và không gọi backend bị cấm. Không có agent hoặc server thật được khởi chạy. `logs` chỉ in control events; không ghi dump màn hình có thể chứa nguồn.
