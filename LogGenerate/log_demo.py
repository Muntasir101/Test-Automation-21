import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# setup logging
logging.basicConfig(filename='test_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def google_search():
    logging.info("Google Search Test Started...")
    start_time = time.time()

    # launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    logging.info("Browser launched...")

    # step 1: Go to Application page
    driver.get("https://google.com")
    logging.info("Google opened...")
    wait = WebDriverWait(driver, 10)

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#APjFqb")))
    logging.info("Search Box located...")

    search_box.send_keys("Selenium")
    logging.info("Selenium Typed...")

    # Press Enter
    search_box.send_keys(Keys.RETURN)
    logging.info("Press Enter...")

    driver.close()
    logging.info("Test Execution Completed...")

    # Execution End Time
    end_time = time.time()

    # Calculate total time taken
    execution_time = end_time - start_time
    logging.info("Execution Time: " + str(execution_time))


google_search()
