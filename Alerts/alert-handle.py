import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def normal_alert():
    start_time = time.time()

    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)

    normal_alert_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(1) > button")))
    normal_alert_button.click()

    # switch to alert
    driver.switch_to.alert.accept()

    driver.close()

    # Execution End Time
    end_time = time.time()

    # Calculate total time taken
    execution_time = end_time - start_time
    print(execution_time)


def confirm_alert():
    start_time = time.time()

    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)

    confirm_alert_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(2) > button")))
    confirm_alert_button.click()

    # switch to alert and click Cancel
    driver.switch_to.alert.dismiss()

    # driver.close()

    # Execution End Time
    end_time = time.time()

    # Calculate total time taken
    execution_time = end_time - start_time
    print(execution_time)


def prompt_alert():
    start_time = time.time()

    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)

    confirm_alert_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(3) > button")))
    confirm_alert_button.click()

    # switch to alert and type then click ok
    driver.switch_to.alert.send_keys("Test Automation")
    driver.switch_to.alert.accept()

    # driver.close()

    # Execution End Time
    end_time = time.time()

    # Calculate total time taken
    execution_time = end_time - start_time
    print(execution_time)


# normal_alert()
# confirm_alert()
prompt_alert()
