# Lab 02 – Câu hỏi thảo luận

## 1. Vì sao phải đồng bộ `master` trước khi tạo/gửi PR?
Nhánh tính năng có thể được tạo từ một phiên bản `master` cũ. Trong lúc phát triển, `master` có thể nhận thay đổi mới từ PR khác. Đồng bộ bằng `fetch` rồi `merge origin/master` (hoặc rebase khi nhánh riêng và phù hợp) giúp phát hiện xung đột sớm, kiểm thử trên trạng thái tích hợp gần nhất và giảm nguy cơ PR gây lỗi khi merge. Bài thực hành minh họa Dev 2 phải lấy thay đổi `print_cart` đã được merge trước khi gửi PR tìm kiếm.

## 2. Khi nào không được rebase?
Không rebase nhánh đã được push/chia sẻ và người khác đang dựa vào, trừ khi cả nhóm thống nhất phối hợp vì rebase viết lại SHA/lịch sử commit và có thể làm lệch lịch sử của người khác. Không dùng rebase để viết lại lịch sử chung của `master` hoặc `release/*`. Rebase phù hợp nhất với nhánh cá nhân chưa chia sẻ; nếu nhánh đã chia sẻ, ưu tiên merge để giữ lịch sử an toàn.

## 3. `feature/*` khác `topic/*` ra sao?
Trong tài liệu, `feature/*` biểu diễn một tính năng sản phẩm có hành vi người dùng, ví dụ `feature/cart-print`, `feature/search-by-title`. `topic/*` là nhánh cho một chủ đề/công việc hỗ trợ hoặc thay đổi có phạm vi cụ thể, ví dụ `topic/pr-template`, `topic/use-case-diagram`. Cả hai đều được tạo từ `master`, có mục đích riêng và tích hợp qua PR; khác nhau chủ yếu ở ý nghĩa/tên gọi và phạm vi công việc.

## So sánh 3 kiểu merge
- **Merge commit**: giữ các commit chi tiết và tạo commit merge; lịch sử thể hiện nhánh phân kỳ/hội tụ, có thể revert cả merge bằng `git revert -m 1 <sha>`.
- **Squash and merge**: gom toàn bộ thay đổi PR thành một commit trên nhánh đích; lịch sử gọn, nhưng không giữ từng commit riêng lẻ của nhánh.
- **Rebase and merge**: đặt các commit của nhánh lên đầu nhánh đích, tạo SHA mới và lịch sử tuyến tính; cần tránh áp dụng với nhánh đã chia sẻ nếu việc viết lại lịch sử gây ảnh hưởng cộng tác viên.
