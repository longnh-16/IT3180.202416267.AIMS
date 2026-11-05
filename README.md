# IT3180 – AIMS-mini (bộ bài thực hành Git & GitHub)

Bộ dự án này chuẩn bị các tệp mã nguồn và tài liệu cần thiết cho chuỗi Lab 01–05 trong tài liệu **IT3180_0504_C5.4-Thuc-hanh-Git-GitHub.pdf**.

## Yêu cầu
- Windows 10/11
- Git for Windows (Git Bash), Git >= 2.40
- Python >= 3.10 (khuyến nghị 3.12)
- Tài khoản GitHub

## Chạy chương trình
Mở **Git Bash** hoặc PowerShell tại thư mục chứa `main.py`:

```bash
python main.py
python -m unittest discover -s tests -v
```

Nếu Windows không nhận lệnh `python`, thử:

```powershell
py main.py
py -m unittest discover -s tests -v
```

Kết quả chính cần thấy:

```text
AIMS-mini v1.1.0
Total cost: 63.89 $
Search 'lion': The Lion King
```

## Cấu trúc
```text
it3180-<MSSV>-aims/
├── .github/
│   ├── pull_request_template.md
│   └── workflows/ci.yml
├── aims/
│   ├── __init__.py
│   ├── cart.py
│   ├── dvd.py
│   └── search.py
├── docs/
│   ├── use-case.md
│   ├── answers-lab01.md ... answers-lab05.md
│   └── WINDOWS_GITHUB_GUIDE.md
├── tests/
│   ├── test_cart.py
│   └── test_search.py
├── scripts/check_project.ps1
├── .gitattributes
├── .gitignore
├── CHANGELOG.md
└── main.py
```

## Lưu ý quan trọng về bài thực hành
ZIP chứa snapshot mã nguồn/tài liệu đã hoàn thiện và kiểm thử. GitHub Issue, lịch sử nhánh, PR, review/approval, branch protection, tag và GitHub Release là trạng thái trên repository từ xa; bạn cần tạo chúng theo `docs/WINDOWS_GITHUB_GUIDE.md`. Không nên nộp ZIP như thể các PR/Issue đã được tạo.

## Câu hỏi thảo luận
Câu trả lời đã được soạn trong `docs/answers-lab01.md` đến `docs/answers-lab05.md`. Khi làm từng Lab, đưa file tương ứng vào PR của Lab đó theo hướng dẫn.
