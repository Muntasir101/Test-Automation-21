from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators for login requests
        self.search_input = (By.CSS_SELECTOR, "div#search > input[name='search']")
        self.search_button = (By.CSS_SELECTOR, ".btn-default")

    def search(self, keyword):
        search_field = self.wait.until((EC.visibility_of_element_located(self.search_input)))
        search_field.send_keys(keyword)

    def click_search_button(self):
        search_btn = self.wait.until((EC.visibility_of_element_located(self.search_button)))
        search_btn.click()
