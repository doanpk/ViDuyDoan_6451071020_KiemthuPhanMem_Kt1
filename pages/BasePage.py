from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        
    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )
        
    def click_element(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator):
        return self.find_element(locator).text
        
    def get_current_url(self):
        return self.driver.current_url
        
    def wait_for_url_changes(self, old_url):
        WebDriverWait(self.driver, self.timeout).until(
            EC.url_changes(old_url)
        )
