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
