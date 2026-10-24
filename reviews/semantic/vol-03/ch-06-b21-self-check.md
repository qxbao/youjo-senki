# Báo cáo tự kiểm tra ngữ nghĩa — Batch `vol-03-ch-06-b21`

- **Phạm vi**: `YS-LN03/Text/chapter006_002.xhtml/p000668` – `YS-LN03/Text/chapter006_002.xhtml/p000699` (32 đoạn)
- **Người dịch**: `argon-low`
- **Trạng thái bản dịch**: `draft`

## 1. Kiểm tra tính toàn vẹn và đối chiếu với nguồn
- Toàn bộ 32 đoạn từ `p000668` đến `p000699` được dịch đầy đủ, giữ nguyên thứ tự, mã đoạn (`id`) và `source_sha256` (`74f557a5f02ccc0308519579028d46fc0a89698a81e15219feb3add22ffc96a4`).
- Không làm rò rỉ câu văn tiếng Anh từ nguồn vào báo cáo hoặc ghi chú.

## 2. Xưng hô, đại từ và giọng văn (`DEC-P01-001`)
- **Trần thuật và độc thoại nội tâm của Tanya (`p000668`–`p000698`)**:
  - Ngôi kể khách quan dùng `nó` cho Thiếu tá Tanya von Degurechaff (`p000668`, `p000669`, `p000672`, `p000690`, `p000697`, `p000698`) và độc thoại nội tâm tự quy chiếu dùng `mình` (`p000668`–`p000670`, `p000672`, `p000676`, `p000681`–`p000685`, `p000690`, `p000692`, `p000694`, `p000695`) theo đúng quy ước `DEC-P01-001`.
  - Khi quy chiếu chung về đơn vị/tiểu đoàn trong nội tâm và thoại, dùng `chúng ta` (`p000676`, `p000678`–`p000681`, `p000684`, `p000686`, `p000687`, `p000691`–`p000695`).
- **Hội thoại giữa Tanya và thuộc cấp**:
  - Các đoạn thoại giữa Tanya và cấp dưới (`p000671`, `p000673`, `p000675`, `p000686`, `p000687`, `p000689`, `p000693`, `p000696`, `p000699`) giữ đúng sắc thái chỉ huy – thuộc cấp nối tiếp từ `ch-06-b20`: thuộc cấp đáp lễ phép (`Vâng, thiếu tá nói phải` ở `p000687`), Tanya gọi chung toàn đơn vị là `Các vị` (`p000693`) và gọi hai đại đội trưởng (`02` và `05`) là `Các anh` (`p000699`).

## 3. Bảo toàn nhấn mạnh (`DEC-P01-002`)
- Chỉ 5 đoạn có thẻ nhấn mạnh trong XHTML gốc và đã được bảo toàn chính xác bằng dấu `*...*` đúng phạm vi nhấn mạnh của nguồn:
  - `p000684`: `*Cô muốn khoe khoang con số đi săn của mình đến* mức đó *sao?*` (bảo toàn việc từ ở giữa không in nghiêng trong XHTML gốc).
  - `p000685`: `*Khát khao thành tích bắn hạ đến mức nào rồi chứ?*`
  - `p000690`: `*Mình không muốn làm hỏng hồ sơ thành tích của mình đâu*`
  - `p000693`: `*tsurinobuse*`
  - `p000695`: `Chúng *mới là kẻ đang truy đuổi* chúng ta*. Mình thà chọn phương thức văn minh là trò chuyện hòa bình hơn nhiều*` (bảo toàn chính xác ranh giới hai cụm nhấn mạnh trong XHTML gốc).
- Toàn bộ 27 đoạn còn lại không có thẻ nhấn mạnh trong nguồn và không phát sinh dấu `*...*` ngoài nguồn.

## 4. Thuật ngữ và tính nhất quán nội bộ
- **Thuật ngữ đã khóa / tiếp nối từ các batch trước và sổ pending**:
  - `Type 95`, `Type 97`, `Elinium Type 97`, `Elinium Arms` (`p000668`, `p000673`, `p000674`) — khớp với `ch-06-b20` và `ch-01-b10`.
  - `Thượng đế` (`p000672`), `mặt trận Rhine` (`p000684`), `Thế chiến thứ hai` (`p000688`).
  - `đòn đánh chống mục tiêu mặt đất` (`p000679`, `p000681`) — khớp với `vol02-ch01-b07-anti-surface-strikes` trong `work/run-state/pending-terms.yml`.
  - `cuộc bắn gà tây` (`p000686`) — khớp với `vol02-ch01-b04-turkey-shoot` trong `work/run-state/pending-terms.yml`; đối sánh tự nhiên với `cuộc săn vịt` ở `p000675`.
  - `Fairy 01 gọi 02 và 05` (`p000699`) — giữ nguyên định danh hô hiệu theo quy ước xuyên suốt của dự án.
- **Thuật ngữ mới đề xuất (pending)**:
  - `Lục quân Đế quốc Nhật Bản` (`p000680`).
  - `*tsurinobuse*` (`p000693`) và `chế độ Shimazu giả tạo` (`p000694`) — giữ nguyên thuật ngữ chiến thuật tiếng Nhật được in nghiêng và tên gia tộc `Shimazu` nối tiếp từ `ch-06-b14` (`p000430`–`p000431`).
