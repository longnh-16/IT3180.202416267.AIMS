# Lab 01 – Câu hỏi thảo luận

## 1. Vì sao dùng `git mv`?
`git mv` thực hiện thao tác đổi vị trí/đổi tên tệp và cập nhật trạng thái trong working tree/staging. Git vẫn lưu lịch sử theo commit; khi xem bằng `git log --follow -- <file>`, Git có thể nhận diện nội dung tệp được chuyển sang đường dẫn mới. Về bản chất, Git phát hiện rename dựa trên độ tương đồng nội dung khi so sánh commit, nên `git mv` không tạo ra một loại đối tượng lịch sử đặc biệt; nó giúp thao tác rõ ràng và giảm nguy cơ quên `git add` đường dẫn mới/xóa đường dẫn cũ.

## 2. `release/lab01` có phải baseline không?
Có. Theo quy trình bài thực hành, nhánh `release/lab01` được tạo từ `master` sau khi Lab 01 hoàn tất và đại diện cho trạng thái bài nộp đã thống nhất. Nó là một baseline có thể tham chiếu/tái tạo. Trong bài này chưa cần gắn tag phiên bản chính thức; tag được thực hành ở Lab 04.

## 3. Vì sao không commit thẳng lên `master` dù làm một mình?
Vì mục tiêu là tuân thủ quy trình kiểm soát thay đổi: thay đổi đi qua nhánh có mục đích, Pull Request, kiểm tra diff và CI/review trước khi tích hợp. Làm một mình vẫn có thể tự kiểm tra PR; branch protection giúp ngăn thao tác trực tiếp và tạo lịch sử có thể kiểm toán. Điều này giữ quy trình nhất quán khi làm nhóm.

## Câu hỏi nhanh: `--global` khác `--local` ở đâu?
`--global` lưu cấu hình người dùng trong file cấu hình Git cấp tài khoản (thường là `~/.gitconfig` trên Windows tương ứng thư mục hồ sơ người dùng), áp dụng mặc định cho các repository của người dùng đó. `--local` lưu trong `.git/config` của repository hiện tại và chỉ áp dụng ở repo đó; cấu hình local có độ ưu tiên cao hơn global cho cùng một khóa.
