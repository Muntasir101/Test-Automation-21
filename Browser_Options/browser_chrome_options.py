import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def chrome_options_demo():
    start_time = time.time()

    # launch browser
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_options.add_argument("--disable-features=OptimizationGuideModelDownloading,OptimizationHintsFetching,"
                                "OptimizationTargetPrediction,OptimizationHints")

    driver = webdriver.Chrome(options=chrome_options)

    # step 1: Go to Application page
    driver.get("https://google.com")

    print(driver.title)

    driver.close()

    # Execution End Time
    end_time = time.time()
    # Calculate total time taken
    execution_time = end_time - start_time
    print(execution_time) # 3.606043577194214


chrome_options_demo()
