from selenium.webdriver.common.by import By
from .BasePage import BasePage

class LoginPage(BasePage):
    # --- Locators (Bộ chọn UI thực tế từ vanphongdientu.utc.edu.vn) ---
    USERNAME_INPUT = (By.NAME, "username") 
    PASSWORD_INPUT = (By.NAME, "userpwd") 
    LOGIN_BUTTON = (By.CLASS_NAME, "submit_login")
    REMEMBER_ME_CHECKBOX = (By.ID, "persistent")
    ERROR_MESSAGE = (By.XPATH, "//*[@color='red' or contains(@class, 'error') or contains(@style, 'color: red')]") # Giả định vì lỗi sinh ra sau khi submit
    
    LOGIN_EMAIL_UTC_BUTTON = (By.XPATH, "//a[contains(@href, 'accounts.google.com')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(@href, '/Login/GetPass')]")
    HELP_CENTER_LINK = (By.XPATH, "//a[contains(@href, 'hotrokythuat.utc.edu.vn')]")
    FEEDBACK_LINK = (By.XPATH, "//a[contains(@href, 'mailto:hotrokythuat@utc.edu.vn')]")

    URL = "https://vanphongdientu.utc.edu.vn/Login"

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password, remember_me=False):
        if username:
            self.input_text(self.USERNAME_INPUT, username)
        if password:
            self.input_text(self.PASSWORD_INPUT, password)
        
        checkbox = self.find_element(self.REMEMBER_ME_CHECKBOX)
        if remember_me and not checkbox.is_selected():
            checkbox.click()
        elif not remember_me and checkbox.is_selected():
            checkbox.click()
            
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def click_login_with_email_utc(self):
        self.click_element(self.LOGIN_EMAIL_UTC_BUTTON)

    def click_forgot_password(self):
        self.click_element(self.FORGOT_PASSWORD_LINK)

    def is_password_masked(self):
        element = self.find_element(self.PASSWORD_INPUT)
        return element.get_attribute("type") == "password"
        
    def click_help_center(self):
        self.click_element(self.HELP_CENTER_LINK)
        
    def click_feedback(self):
        self.click_element(self.FEEDBACK_LINK)
        
    def get_username_element(self):
        return self.find_element(self.USERNAME_INPUT)
