# Lab 04 – Câu hỏi thảo luận

## 1. Vì sao `release/*` không merge ngược vào `master`?
Theo Release Flow rút gọn của học phần, `master` là dòng phát triển chính; `release/*` là baseline đóng băng để nộp và bảo trì riêng. Nếu merge release ngược vào master, các thay đổi chỉ dành cho bản phát hành cũ (ví dụ bump PATCH/CHANGELOG hoặc sửa nóng) có thể ghi đè/va chạm với phiên bản phát triển mới trên master. Khi cần đưa một sửa lỗi từ release về master, bài Lab 05 dùng `cherry-pick -x` để chỉ lan truyền commit sửa lỗi cần thiết, không kéo cả nhánh release.

## 2. So sánh với GitFlow
Release Flow của học phần đơn giản hóa GitFlow: dùng `master` làm dòng phát triển chính, `feature/*`, `topic/*`, `bugfix/*`, `refactor/*`, `release/labXX`, `hotfix/*`; release được giữ độc lập cho từng bài nộp và không merge ngược vào master. GitFlow cổ điển thường có hai nhánh dài hạn `main`/`master` và `develop`, tạo `release/*` từ develop, sau khi phát hành merge release vào cả main và develop; hotfix thường bắt đầu từ main rồi merge về main và develop. Mô hình học phần phù hợp việc có nhiều baseline bài tập cần bảo trì song song.

## 3. Vì sao lên `1.0.0` mà không phải `0.4.0`?
Theo SemVer, `0.y.z` biểu thị giai đoạn phát triển ban đầu/chưa ổn định. Sau Lab 01–03, bài thực hành xem AIMS-mini đã đạt baseline phát hành ổn định đầu tiên, có bộ chức năng và kiểm thử cần thiết, nên chuyển sang `1.0.0`. Đây là mốc sản phẩm/baseline ổn định, không phải phép đếm số buổi học. Từ đó tính năng tương thích tăng MINOR thành `1.1.0`, còn sửa lỗi tương thích tăng PATCH thành `1.0.1`.

## 4. Vì sao chuẩn bị phát hành trên `master` trước khi tạo nhánh release?
Mọi nội dung dự kiến thuộc phiên bản phát hành (version trong package, CHANGELOG, tài liệu) cần được review và merge vào dòng phát triển chính trước. Sau đó tạo `release/lab04` từ trạng thái master đã hoàn chỉnh để nhánh release đóng băng đúng baseline. Nếu chỉnh sửa trực tiếp trên release, master sẽ không có cùng trạng thái phát hành và quy trình lại cần đồng bộ ngược, trái với chính sách của tài liệu.
