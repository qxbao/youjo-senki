# Recovery

- Nhiệm vụ: khôi phục coordinator từ trạng thái lưu, không cần hội thoại cũ; sau xác minh chuyển sang coordinator.md.
- Đọc: shared/coordinator/config, work/run-state/, Git log/status/diff metadata, manifest/handoff, tên tệp và báo cáo liên quan. Không mở sách/source text hay sửa bản dịch.
- Ghi: chỉ work/run-state/ để reconciliate queue/lease/session IDs và ACK checkpoint_generation. Không commit hoặc sửa canon/handoff trong pha recovery.
- Khôi phục: xác minh project root, IDs/terminal_id/agent_session_id bằng Herdr; đọc màn hình nếu blocked/unknown; đối chiếu commit và validator receipts/review closures trong checkpoint với Git. Lease cũ còn worker working thì chờ/escalate, không cấp lease thứ hai. JSONL có mặt nhưng thiếu commit/check/review vẫn chưa hoàn tất.
- Bàn giao: ghi received_generation và ACK chỉ sau khi queue và pending đã dựng lại; coordinator cũ chỉ được thoát sau ACK. Nếu session pane mất, dùng pane mới do script đăng ký; không nhận ownership pane của người dùng.
- Cấm: coi checkpoint là nguồn duy nhất; đọc lịch sử hội thoại để phục hồi; gửi lại prompt delivery uncertain; đóng pane không thuộc session.
- Dừng/escalate: shared.md; checkpoint hỏng/missing với lease chưa rõ, Git ngoài phạm vi, stale/mismatched identity hoặc source-preparation adapter thiếu.
- Báo cáo: YAML shared.md + recovered_generation, received_generation, queue_next, live_workers, ownership_verified, discrepancies; state done chỉ khi đã chuyển quyền thành công.
