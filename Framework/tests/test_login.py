import json
import logging
import os

from Framework.common.generate_screenshot import save_screenshot
from Framework.pages.login_page import LoginPage
from Framework.common.configure_config import load_config


# Load configuration data from config.json file
config = load_config()


def test_valid_login(setup_driver):
    driver = setup_driver
    logging.info("Test Start...")

    driver.get(config['login_page'])
    logging.info("Test URL Open...")

    login_page = LoginPage(driver)

    login_page.enter_email("mail123@gmail.com")
    logging.info("Enter Email...")

    login_page.enter_password("123456")
    logging.info("Enter Password...")

    login_page.click_login()
    logging.info("Click Login button...")

    # Verification Login Success
    expected_title = "My Account"

    actual_title = driver.title

    if expected_title == actual_title:
        with open(os.path.join(os.getcwd(), 'Framework', 'Report', 'TN_test_result.txt'), 'a') as file:
            file.write("\nTest Case Passed. Login Success.\n")
            logging.info("Test Case Passed. Login Success")
    else:
        with open(os.path.join(os.getcwd(), 'Framework', 'Report', 'TN_test_result.txt'), 'a') as file:
            file.write(
                f"\nTest Case failed !!\n"
                f"Getting Actual Result: {actual_title}\n"
                f"Expected Result: {expected_title}\n"
            )
            logging.info("Test Case Failed !!\n")

        save_screenshot(driver, 'login_failed.png')
        logging.info("Capture Screenshot...")

    logging.info("Test Complete...")
