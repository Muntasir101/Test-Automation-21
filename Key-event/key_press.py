import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


def google_search():
    start_time = time.time()

    # launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get("https://google.com")
    wait = WebDriverWait(driver, 10)

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#APjFqb")))
    search_box.send_keys("Selenium")

    # Press Enter
    search_box.send_keys(Keys.RETURN)

    time.sleep(10)


google_search()
