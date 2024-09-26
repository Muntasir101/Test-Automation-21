import json
import logging
import os

from Framework.common.generate_screenshot import save_screenshot
from Framework.pages.home_page import HomePage
from Framework.common.configure_config import load_config

# Load configuration data from config.json file
config = load_config()


def test_valid_search(setup_driver):
    driver = setup_driver
    logging.info("Test Start...")

    driver.get(config['home_page'])
    logging.info("Test URL Open...")

    home_page = HomePage(driver)

    home_page.search("macbook")
    logging.info("Enter Search Keyword...")

    home_page.click_search_button()
    logging.info("Click Search Button...")

    logging.info("Test Complete...")