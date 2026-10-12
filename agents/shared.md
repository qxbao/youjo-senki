# Quy tắc chung

- Nhiệm vụ: thực hiện đúng vai trò và một task_id/segment_id được coordinator giao.
- Đọc: persona của mình, config/translation-pipeline.yml và đúng đầu vào ghi trong task.
- Ghi: chỉ các đường dẫn được persona cho phép; dùng apply_patch, giữ thay đổi ngoài task.
- Cấm: Orca, worktree mới, Codex gốc, ghi nguồn vào Git, sao chép sách, truyền nguồn cho công cụ/dịch vụ ngoài luồng đã giao; tự sửa canon hoặc đổi tên/cấp bậc/xưng hô đã chốt.
- Chạy tuần tự: chỉ một worker hoạt động; translator giữ lease trong checkpoint trước khi sửa translations/. Reviewer hoàn tất rồi mới gọi translator sửa.
- Pending: dùng phương án tạm nhất quán từ canon/glossary-pending.yml và work/run-state/pending-terms.yml. Báo thuật ngữ mới; không tự gọi là canon. Coordinator giữ sổ pending, translator không sửa canon.
- Hoàn tất: lô có commit, validator đạt, mọi review bắt buộc đã xử lý, không còn lỗi nghiêm trọng/vừa. Pilot và JSONL chưa đạt không được tính.
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
