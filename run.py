import os
import pytest

if __name__ == "__main__":
    # Tự động di chuyển (cd) vào thư mục selenium_project chứa file run.py này
    # Bất kể bạn đang đứng ở thư mục lớn (Test Case Login) hay nhỏ, nó đều xử lý được.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)

    print("🚀 Bắt đầu chạy test...")
    # Chạy toàn bộ test bằng pytest (sẽ tự động đọc cấu hình từ pytest.ini)
    exit_code = pytest.main()
    
    print(f"✅ Đã chạy xong test (Mã thoát: {exit_code}). Đang mở Allure Report...")
    # Tự động mở báo cáo Allure sau khi test xong
    os.system("allure serve allure-results")
