import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options


def firefox_options_demo():
    start_time = time.time()

    # launch browser
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--start-maximized")
    firefox_options.add_argument("--disable-search-engine-choice-screen")
    firefox_options.add_argument("--disable-features=OptimizationGuideModelDownloading,OptimizationHintsFetching,"
                                 "OptimizationTargetPrediction,OptimizationHints")

    driver = webdriver.Chrome(options=firefox_options)

    # step 1: Go to Application page
    driver.get("https://google.com")

    print(driver.title)

    driver.close()

    # Execution End Time
    end_time = time.time()
    # Calculate total time taken
    execution_time = end_time - start_time
    print(execution_time)  # 3.606043577194214


firefox_options_demo()
