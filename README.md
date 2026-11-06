# IT3180 – AIMS-mini (bộ bài thực hành Git & GitHub)

## Phần trả lời các câu hỏi của các bài thực hành ở trong thư mục docs

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

Kết quả chính cần thấy:

```text
AIMS-mini v1.1.0
Total cost: 63.89 $
Search 'lion': The Lion King
```

## Cấu trúc
```text
it3180-202416267-aims/
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

## Câu hỏi thảo luận
Câu trả lời đã được soạn trong `docs/answers-lab01.md` đến `docs/answers-lab05.md`
