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

    def test_tc6_login_success_without_remember_me(self):
        page = LoginPage(self.driver)
        page.open()
        page.login("huongngt", "123456@utc", remember_me=False)
        page.wait_for_url_changes(page.URL)
        assert "dashboard" in page.get_current_url() or "home" in page.get_current_url()

    def test_tc7_login_with_utc_email(self):
        page = LoginPage(self.driver)
        page.open()
        page.click_login_with_email_utc()
        page.wait_for_url_changes(page.URL)
        url = page.get_current_url()
        assert "sso" in url or page.URL not in url

    def test_tc8_forgot_password(self):
        page = LoginPage(self.driver)
        page.open()
        page.click_forgot_password()
        page.wait_for_url_changes(page.URL)
        url = page.get_current_url()
        assert "forgot" in url or "recover" in url

    def test_tc9_sql_injection(self):
        page = LoginPage(self.driver)
        page.open()
        page.login("' OR '1'='1", "any_password")
        assert "Tài khoản không đúng" in page.get_error_message()

    def test_tc10_password_is_masked(self):
        page = LoginPage(self.driver)
        page.open()
        assert page.is_password_masked()

    def test_tc11_case_sensitive_password(self):
        page = LoginPage(self.driver)
        page.open()
        page.login("huongngt", "123456@UTC")
        assert "Tài khoản không đúng" in page.get_error_message()

    def test_tc12_brute_force_protection(self):
        page = LoginPage(self.driver)
        page.open()
        for i in range(5):
            page.login("huongngt", f"wrong_pass_{i}")
            time.sleep(1)
        assert len(page.get_error_message()) > 0

    def test_tc13_mobile_responsive(self):
        self.driver.set_window_size(375, 812)
        page = LoginPage(self.driver)
        page.open()
        assert page.get_username_element().is_displayed()
        self.driver.maximize_window()

    def test_tc14_help_center_link(self):
        page = LoginPage(self.driver)
        page.open()
        page.click_help_center()
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        page.wait_for_url_changes(page.URL)
        assert page.get_current_url() != page.URL

    def test_tc15_feedback_link(self):
        page = LoginPage(self.driver)
        page.open()
        page.click_feedback()
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        page.wait_for_url_changes(page.URL)
        assert page.get_current_url() != page.URL