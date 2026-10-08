import os
import re
import subprocess
import time

repo_dir = r"d:\KiemThu\Test Case Login"
file_path = os.path.join(repo_dir, "tests", "LoginE2ETest.py")

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Tách phần đầu (import và khai báo class)
header_match = re.search(r'(.*?class LoginE2ETest\(BaseTest\):)', content, re.DOTALL)
header = header_match.group(1)

# Tìm tất cả các hàm test (bắt đầu bằng '    def test_')
test_cases = re.findall(r'(\n    def test_tc\d+.*?)(?=\n    def test_tc|$)', content, re.DOTALL)

# Khởi tạo git
subprocess.run(["git", "init"], cwd=repo_dir)

# Bước 1: Trống file LoginE2ETest.py (chỉ để lại header)
with open(file_path, "w", encoding="utf-8") as f:
    f.write(header + "\n")

# Commit các file nền tảng (cấu trúc thư mục, gitignore, BaseTest, LoginPage...)
subprocess.run(["git", "add", "."], cwd=repo_dir)
subprocess.run(["git", "commit", "-m", "Initial commit: Setup OOP project structure (BaseTest, POM)"], cwd=repo_dir)

# Bước 2: Thêm dần từng test case và commit
current_content = header + "\n"
for i, tc in enumerate(test_cases, 1):
    current_content += tc
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(current_content)
    
    # Tìm tên test case để ghi log commit
    tc_name_match = re.search(r'def (test_tc\d+[^(\s]*)', tc)
    tc_name = tc_name_match.group(1) if tc_name_match else f"test_tc{i}"
    
    # Add và commit
    subprocess.run(["git", "add", r"tests\LoginE2ETest.py"], cwd=repo_dir)
    commit_msg = f"Add test case {i}: {tc_name}"
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_dir)
    print(f"Da commit: {commit_msg}")

print("Da chia va commit xong tat ca cac test case voi cau truc moi!")
