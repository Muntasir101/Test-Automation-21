import json
import logging
import os

from Framework.common.generate_screenshot import save_screenshot
from Framework.pages.login_page import LoginPage
from Framework.common.configure_config import load_config
from Framework.common.log_config import setup_logging

# Load configuration data from config.json file
config = load_config()

# Load logging configuration
logging.basicConfig(filename=os.path.join(os.getcwd(), 'Framework', 'Log', 'test_log.log'), level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def test_valid_login(setup_driver):
    driver = setup_driver
    logging.info("Test Start...")

    driver.get(config['login_page'])
    logging.info("Test URL Open...")

    login_page = LoginPage(driver)

    login_page.enter_username("Admin")
    logging.info("Enter Username...")

    login_page.enter_password("admin123")
    logging.info("Enter Password...")

    login_page.click_login()
    logging.info("Click Login button...")

    save_screenshot(driver, 'login2.png')
    logging.info("Capture Screenshot...")

    logging.info("Test Complete...")
