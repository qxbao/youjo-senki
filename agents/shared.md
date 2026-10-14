# Quy tắc chung

- Nhiệm vụ: thực hiện đúng vai trò và một task_id/segment_id được coordinator giao.
- Đọc: persona của mình, config/translation-pipeline.yml và đúng đầu vào ghi trong task.
- Ghi: chỉ các đường dẫn được persona cho phép; dùng apply_patch, giữ thay đổi ngoài task.
- Cấm: Orca, worktree mới, Codex gốc, ghi nguồn vào Git, sao chép sách, truyền nguồn cho công cụ/dịch vụ ngoài luồng đã giao; tự sửa canon hoặc đổi tên/cấp bậc/xưng hô đã chốt.
- Điều phối song song tối đa hai worker chỉ cho cặp translator Luna + Flash polisher khi allowlist tách biệt: translator chỉ sửa một JSONL chuẩn được giao dưới `translations/`; polisher chỉ sửa candidate và change log dưới `polish-candidates/`. Ghi riêng từng lease/task/pane/session vào checkpoint trước khi dispatch; không cấp lease có đường dẫn giao nhau. Chỉ một worker được sửa bản chuẩn trong `translations/` tại một thời điểm; reviewer và semantic checker chỉ ghi báo cáo.
- Trước khi dispatch song song, ghi đủ `worker_leases` (mỗi lease có role, task_id, pane_id, terminal_id, agent_session_id, allowlist, state) và `live_workers`; nhả từng lease riêng khi worker kết thúc. Có thể tiếp tục stream còn lại khi stream kia chờ; promotion vẫn cần coordinator lease riêng trên đúng JSONL chuẩn và không được chạy đồng thời với worker nào đang sửa `translations/`.
- Pending: dùng phương án tạm nhất quán từ canon/glossary-pending.yml và work/run-state/pending-terms.yml. Báo thuật ngữ mới; không tự gọi là canon. Coordinator giữ sổ pending, translator không sửa canon.
- Hoàn tất theo pipeline mới: lô có commit, validator đạt, Argon đã review và khóa lựa chọn, mọi review bắt buộc đã xử lý, không còn lỗi nghiêm trọng/vừa; ứng viên Flash có receipt Luna chấp nhận đúng hash và đã được coordinator nâng. Tệp Gemini/receipt cũ không tự chứng minh hoàn tất; không tự mở rộng hàng đợi sang các batch lịch sử.
- Dừng/escalate: validator/diff-check lỗi, lỗi nghiêm trọng còn lại, Git ngoài phạm vi, agent/Herdr lỗi, hoặc quyết định canon ảnh hưởng cốt truyện. Blocked: đọc màn hình trước; prompt đã gửi nhưng chưa rõ kết quả thì không gửi lại.
- Báo cáo coordinator bằng YAML, không chứa câu nguồn, token, khóa hoặc lịch sử hội thoại:

```yaml
role: translator
task_id: vol-NN-ch-NN-bNN
state: done # working | blocked | failed
segment_ids: []
files_written: [] # đường dẫn tương đối
validator: pass # fail | not_run
diff_check: pass
findings: [] # {severity, segment_id, issue, resolution}
pending_terms: [] # {source_term, proposed_vi, segment_ids, volume, chapter, status: pending}
risks: []
commit: null # worker không tự commit
next_action: review
```
