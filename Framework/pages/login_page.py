from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators for login requests
        self.email_input = (By.CSS_SELECTOR, "#input-email")
        self.password_input = (By.CSS_SELECTOR, "#input-password")
        self.login_button = (By.CSS_SELECTOR, "form[method='post'] > input[value='Login']")

    def enter_username(self, username):
        username_field = self.wait.until((EC.visibility_of_element_located(self.email_input)))
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until((EC.visibility_of_element_located(self.password_input)))
        password_field.send_keys(password)

    def click_login(self):
        login_btn = self.wait.until((EC.visibility_of_element_located(self.login_button)))
        login_btn.click()
