import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def chrome_demo():
    start_time = time.time()

    # launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get("https://google.com")

    print(driver.title)

    driver.close()

    # Execution End Time
    end_time = time.time()
    # Calculate total time taken
    execution_time = end_time - start_time
    print(execution_time) # 10.498687505722046


chrome_demo()
