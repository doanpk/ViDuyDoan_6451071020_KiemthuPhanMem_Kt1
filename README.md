# Đồ Án Kiểm Thử Tự Động - Chức năng Đăng Nhập (UTC Web Application)

Đây là project kiểm thử tự động (Automation Testing) sử dụng **Selenium WebDriver**, **Pytest**, và **Allure Report** cho chức năng đăng nhập của website hệ thống UTC.

## 📂 Cấu Trúc Dự Án

```text
Test Case Login/
├── base/
│   └── BaseTest.py        # Khởi tạo WebDriver và thiết lập chung
├── pages/                 # Áp dụng mô hình Page Object Model (POM)
│   ├── BasePage.py        # Chứa các hàm cơ sở tương tác với Web
│   └── LoginPage.py       # Chứa các locator và action riêng cho trang Login
├── tests/                 
│   └── LoginE2ETest.py    # Chứa 15 kịch bản tự động (Kế thừa từ BaseTest)
├── pytest.ini             # File cấu hình mặc định (tự động tạo Allure kết quả)
├── requirements.txt       # Danh sách các thư viện Python
├── run.py                 # Script Python chạy test tự động 1 click
├── chay_test.bat          # File chạy bằng cách click đúp chuột trên Windows
├── TestCase_Login_UTC.md  # Tài liệu mô tả chi tiết các kịch bản kiểm thử
└── README.md              # File tài liệu hướng dẫn (chính là file này)
```

## 💻 Yêu Cầu Cài Đặt (Prerequisites)

1. Cài đặt **[Python](https://www.python.org/downloads/)**.
2. Máy phải được cài đặt sẵn môi trường **Allure Commandline** (và Java JDK) để sinh báo cáo.
3. Chạy lệnh sau trong thư mục `Test Case Login` để cài đặt thư viện cần thiết:
   ```powershell
   pip install -r requirements.txt
   ```

## 🚀 Hướng Dẫn Chạy Test (Execution)

Dự án này đã được tối ưu hóa. Bạn không cần phải gõ các lệnh phức tạp. Thay vào đó, hãy sử dụng 1 trong 2 cách sau:

### Cách 1: Sử dụng File Python (Khuyên dùng)
Bạn mở Terminal tại thư mục `Test Case Login` và chạy lệnh sau:
```powershell
python run.py
```
*(Script sẽ tự động chạy toàn bộ Test Cases và tự động mở Allure Report trên trình duyệt khi test hoàn thành).*

### Cách 2: Chạy bằng file Batch (.bat)
Mở thư mục `Test Case Login` trong File Explorer và **nhấp đúp chuột** vào file `chay_test.bat`. Terminal sẽ tự động hiển thị, tự chạy test và bung báo cáo Allure khi xong.

## 📋 Danh Sách Test Cases

Dự án bao gồm **15 kịch bản** kiểm thử để bao phủ toàn bộ chức năng:
- `tc1`, `tc2`: Validate khi để trống thông tin.
- `tc3`, `tc4`: Cảnh báo khi nhập sai user/password.
- `tc5`, `tc6`: Chức năng Ghi nhớ đăng nhập (Remember me).
- `tc7`: Tính năng đăng nhập bằng email UTC.
- `tc8`: Chức năng Quên mật khẩu.
- `tc9`: Kiểm tra bảo mật (SQL Injection cơ bản).
- `tc10`: Đảm bảo mật khẩu bị ẩn (Masked).
- `tc11`: Phân biệt chữ hoa chữ thường đối với mật khẩu.
- `tc12`: Kiểm tra cơ chế chống Brute-force (Nhập sai mật khẩu liên tục).
- `tc13`: Kiểm tra tính tương thích trên giao diện di động (Mobile Responsive).
- `tc14`, `tc15`: Kiểm tra các liên kết ngoài (Trung tâm trợ giúp, Phản hồi).

## 🛠️ Công Nghệ / Framework
- **Ngôn ngữ:** Python 3
- **Framework Test:** Pytest
- **Framework Web Automation:** Selenium WebDriver
- **Báo cáo (Reporting):** Allure Report
