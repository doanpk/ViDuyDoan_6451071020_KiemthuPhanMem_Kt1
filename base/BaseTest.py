import pytest
from selenium import webdriver

class BaseTest:
    def setup_method(self, method):
        # Khởi tạo WebDriver và các thiết lập chung
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        # Đóng trình duyệt sau khi test xong
        if self.driver:
            self.driver.quit()
