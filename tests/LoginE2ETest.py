import pytest
import time
import allure
from base.BaseTest import BaseTest
from pages.LoginPage import LoginPage

@allure.epic("UTC Web Application")
@allure.feature("Login Feature")
class LoginE2ETest(BaseTest):

    def test_tc1_empty_username_or_password(self):
        page = LoginPage(self.driver)
        page.open()
        page.login("", "1256")
        assert "Bạn chưa nhập tên đăng nhập" in page.get_error_message()

    def test_tc2_empty_password(self):
        page = LoginPage(self.driver)
        page.open()
        page.login("huongngt", "")
        assert "Bạn chưa nhập mật khẩu" in page.get_error_message()

    def test_tc3_correct_user_wrong_pass(self):
        page = LoginPage(self.driver)
        page.open()
        page.login("huongngt", "utc@235")
        assert "Tài khoản không đúng" in page.get_error_message()

    def test_tc4_wrong_user_correct_pass(self):
        page = LoginPage(self.driver)
        page.open()
        page.login("lihuongthunguyen", "123456@utc")
        assert "Tài khoản không đúng" in page.get_error_message()

    def test_tc5_login_success_with_remember_me(self):
        page = LoginPage(self.driver)
        page.open()
        page.login("huongngt", "123456@utc", remember_me=True)
        page.wait_for_url_changes(page.URL)
        assert "dashboard" in page.get_current_url() or "home" in page.get_current_url()
