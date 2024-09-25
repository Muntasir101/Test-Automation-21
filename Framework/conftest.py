import logging
import os

import pytest
from selenium import webdriver

logging.basicConfig(
    filename=os.path.join(os.getcwd(), 'Framework', 'Log', 'test_log.log'),
    # Change path if needed, e.g., 'logs/test_log.log'
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'  # Append to log file instead of overwriting
)


@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
