import json
import os

from Framework.common.generate_screenshot import save_screenshot
from Framework.pages.login_page import LoginPage

# Load configuration data from config.json file
with open("E:\\PnT_Online_21\\Projects\\TestAutomation21\\Framework\\Config\\framework_config.json", 'r') as file:
    config = json.load(file)


def test_valid_login(setup_driver):
    driver = setup_driver

    driver.get(config['login_page'])

    login_page = LoginPage(driver)

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    save_screenshot(driver, 'login2.png')
