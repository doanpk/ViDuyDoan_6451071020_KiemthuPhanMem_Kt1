import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- CẤU HÌNH ---
BASE_URL = "http://vanphongdientu.utc.edu.vn"

# Các bộ chọn (Selectors) - BẠN CẦN CẬP NHẬT LẠI CHO ĐÚNG VỚI HTML THỰC TẾ CỦA TRANG
USERNAME_INPUT = (By.ID, "username") # Hoặc By.NAME, "username"
PASSWORD_INPUT = (By.ID, "password") 
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Đăng nhập') or contains(@class, 'btn-login')]")
REMEMBER_ME_CHECKBOX = (By.ID, "rememberMe")
ERROR_MESSAGE = (By.CLASS_NAME, "error-message") # Class của thẻ hiển thị lỗi
LOGIN_EMAIL_UTC_BUTTON = (By.XPATH, "//button[contains(text(), 'Đăng nhập bằng e-mail UTC')]")
FORGOT_PASSWORD_LINK = (By.PARTIAL_LINK_TEXT, "quên mật khẩu")
HELP_CENTER_LINK = (By.PARTIAL_LINK_TEXT, "Trung tâm trợ giúp")
FEEDBACK_LINK = (By.PARTIAL_LINK_TEXT, "Ý kiến phản hồi")

@pytest.fixture
def driver():
    # Khởi tạo Chrome WebDriver
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Bỏ comment dòng này để chạy ngầm không mở giao diện
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    # Đóng trình duyệt sau khi test xong
    driver.quit()

def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

def test_tc1_empty_username_or_password(driver):
    """TC1: Để trống user hoặc password"""
    driver.get(BASE_URL)
    
    # Nhập pass, để trống user
    driver.find_element(*PASSWORD_INPUT).send_keys("1256")
    driver.find_element(*LOGIN_BUTTON).click()
    
    # Kiểm tra thông báo lỗi
    error_el = wait_for_element(driver, ERROR_MESSAGE)
    assert "Bạn chưa nhập tên đăng nhập" in error_el.text

def test_tc2_empty_password(driver):
    """TC2: Để trống mật khẩu"""
    driver.get(BASE_URL)
    
    driver.find_element(*USERNAME_INPUT).send_keys("huongngt")
    driver.find_element(*LOGIN_BUTTON).click()
    
    error_el = wait_for_element(driver, ERROR_MESSAGE)
    assert "Bạn chưa nhập mật khẩu" in error_el.text

def test_tc3_correct_user_wrong_pass(driver):
    """TC3: Đúng tên sai mật khẩu"""
    driver.get(BASE_URL)
    
    driver.find_element(*USERNAME_INPUT).send_keys("huongngt")
    driver.find_element(*PASSWORD_INPUT).send_keys("utc@235")
    driver.find_element(*LOGIN_BUTTON).click()
    
    error_el = wait_for_element(driver, ERROR_MESSAGE)
    assert "Tài khoản không đúng" in error_el.text

def test_tc4_wrong_user_correct_pass(driver):
    """TC4: Sai tên, đúng mật khẩu"""
    driver.get(BASE_URL)
    
    driver.find_element(*USERNAME_INPUT).send_keys("lihuongthunguyen")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456@utc")
    driver.find_element(*LOGIN_BUTTON).click()
    
    error_el = wait_for_element(driver, ERROR_MESSAGE)
    assert "Tài khoản không đúng" in error_el.text

def test_tc5_login_success_with_remember_me(driver):
    """TC5: Đăng nhập thành công và chọn Giữ tôi luôn đăng nhập"""
    driver.get(BASE_URL)
    
    driver.find_element(*USERNAME_INPUT).send_keys("huongngt")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456@utc")
    
    # Tích chọn "Giữ tôi luôn đăng nhập"
    remember_checkbox = driver.find_element(*REMEMBER_ME_CHECKBOX)
    if not remember_checkbox.is_selected():
        remember_checkbox.click()
        
    driver.find_element(*LOGIN_BUTTON).click()
    
    # Kiểm tra xem có chuyển hướng vào trang chủ không (Ví dụ: URL thay đổi)
    WebDriverWait(driver, 10).until(
        EC.url_changes(BASE_URL)
    )
    assert "dashboard" in driver.current_url or "home" in driver.current_url
    
    # Bước kiểm tra tắt trình duyệt và mở lại có thể thực hiện bằng cách lấy cookies
    cookies = driver.get_cookies()
    assert len(cookies) > 0 # Chắc chắn rằng cookie phiên/remember token đã được lưu

def test_tc6_login_success_without_remember_me(driver):
    """TC6: Đăng nhập thành công và không chọn Giữ tôi luôn đăng nhập"""
    driver.get(BASE_URL)
    
    driver.find_element(*USERNAME_INPUT).send_keys("huongngt")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456@utc")
    
    # Đảm bảo KHÔNG chọn "Giữ tôi luôn đăng nhập"
    remember_checkbox = driver.find_element(*REMEMBER_ME_CHECKBOX)
    if remember_checkbox.is_selected():
        remember_checkbox.click()
        
    driver.find_element(*LOGIN_BUTTON).click()
    
    # Kiểm tra chuyển vào trang chủ
    WebDriverWait(driver, 10).until(
        EC.url_changes(BASE_URL)
    )
    assert "dashboard" in driver.current_url or "home" in driver.current_url

def test_tc7_login_with_utc_email(driver):
    """TC7: Đăng nhập bằng e-mail UTC"""
    driver.get(BASE_URL)
    
    driver.find_element(*LOGIN_EMAIL_UTC_BUTTON).click()
    
    WebDriverWait(driver, 10).until(
        EC.url_changes(BASE_URL)
    )
    # SSO chuyển hướng đi nơi khác (ví dụ: Google / Microsoft của trường)
    assert "sso" in driver.current_url or BASE_URL not in driver.current_url

def test_tc8_forgot_password(driver):
    """TC8: Quên mật khẩu"""
    driver.get(BASE_URL)
    
    driver.find_element(*FORGOT_PASSWORD_LINK).click()
    
    WebDriverWait(driver, 10).until(
        EC.url_changes(BASE_URL)
    )
    assert "forgot" in driver.current_url or "recover" in driver.current_url

def test_tc9_sql_injection(driver):
    """TC9: SQL Injection vào trường đăng nhập"""
    driver.get(BASE_URL)
    
    driver.find_element(*USERNAME_INPUT).send_keys("' OR '1'='1")
    driver.find_element(*PASSWORD_INPUT).send_keys("any_password")
    driver.find_element(*LOGIN_BUTTON).click()
    
    error_el = wait_for_element(driver, ERROR_MESSAGE)
    assert "Tài khoản không đúng" in error_el.text

def test_tc10_password_is_masked(driver):
    """TC10: Mật khẩu hiển thị dạng ẩn"""
    driver.get(BASE_URL)
    
    password_input = driver.find_element(*PASSWORD_INPUT)
    assert password_input.get_attribute("type") == "password"

def test_tc11_case_sensitive_password(driver):
    """TC11: Mật khẩu phân biệt chữ hoa/thường"""
    driver.get(BASE_URL)
    
    driver.find_element(*USERNAME_INPUT).send_keys("huongngt")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456@UTC") # Viết hoa @UTC
    driver.find_element(*LOGIN_BUTTON).click()
    
    error_el = wait_for_element(driver, ERROR_MESSAGE)
    assert "Tài khoản không đúng" in error_el.text

def test_tc12_brute_force_protection(driver):
    """TC12: Đăng nhập sai nhiều lần liên tiếp"""
    driver.get(BASE_URL)
    
    for i in range(5):
        driver.find_element(*USERNAME_INPUT).clear()
        driver.find_element(*USERNAME_INPUT).send_keys("huongngt")
        driver.find_element(*PASSWORD_INPUT).clear()
        driver.find_element(*PASSWORD_INPUT).send_keys(f"wrong_pass_{i}")
        driver.find_element(*LOGIN_BUTTON).click()
        time.sleep(1) # Chờ 1 giây sau mỗi lần thử
        
    error_el = wait_for_element(driver, ERROR_MESSAGE)
    # Thông báo có thể đổi thành khóa captcha hoặc tương tự
    assert len(error_el.text) > 0 

def test_tc13_mobile_responsive(driver):
    """TC13: Giao diện hiển thị đúng trên mobile"""
    # Resize về 375x812 (kích thước iPhone X)
    driver.set_window_size(375, 812)
    driver.get(BASE_URL)
    
    form = wait_for_element(driver, USERNAME_INPUT)
    assert form.is_displayed()
    
    # Trả lại kích thước cho các TC khác
    driver.maximize_window()

def test_tc14_help_center_link(driver):
    """TC14: Link Trung tâm trợ giúp hoạt động"""
    driver.get(BASE_URL)
    
    driver.find_element(*HELP_CENTER_LINK).click()
    
    # Xử lý nếu mở tab mới
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        
    WebDriverWait(driver, 10).until(
        EC.url_changes(BASE_URL)
    )
    assert driver.current_url != BASE_URL

def test_tc15_feedback_link(driver):
    """TC15: Link Ý kiến phản hồi hoạt động"""
    driver.get(BASE_URL)
    
    driver.find_element(*FEEDBACK_LINK).click()
    
    # Xử lý nếu mở tab mới
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        
    WebDriverWait(driver, 10).until(
        EC.url_changes(BASE_URL)
    )
    assert driver.current_url != BASE_URL
