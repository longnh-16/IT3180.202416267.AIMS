# Lab 03 – Câu hỏi thảo luận

## 1. Merge base là gì?
Merge base là commit tổ tiên chung tốt nhất mà Git dùng làm điểm xuất phát khi so sánh/tích hợp hai nhánh. Khi merge, Git so sánh thay đổi từ merge base đến từng đầu nhánh để xác định phần nào được thêm/sửa ở mỗi phía. Nếu hai nhánh sửa cùng một vùng không thể tự kết hợp, Git yêu cầu giải quyết conflict.

## 2. Vì sao `master`/`release/*` phải dùng `revert`?
Đây là các nhánh dùng chung hoặc đã đại diện cho baseline được chia sẻ. `reset` di chuyển con trỏ nhánh và có thể viết lại/làm mất commit khỏi lịch sử công khai; điều đó gây lệch lịch sử ở các bản clone khác. `revert` tạo commit mới đảo ngược thay đổi, giữ nguyên lịch sử đã chia sẻ và có thể review qua PR. `reset` chỉ nên dùng cho commit chưa push/chưa chia sẻ, trên nhánh nháp cá nhân.

## Ghi nhớ thao tác
- `git reset --soft HEAD~1`: bỏ commit nhưng giữ thay đổi trong staging.
- `git reset --mixed HEAD~1`: bỏ commit, giữ thay đổi trong working directory (mặc định).
- `git reset --hard HEAD~1`: bỏ commit và xóa thay đổi khỏi working tree; rất dễ mất dữ liệu.
- `git reflog`: tra lại các vị trí HEAD/nhánh trước đó để cứu commit.
- Revert một merge commit cần chỉ định mainline, thường là `git revert -m 1 <merge-sha>`.
