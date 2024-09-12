import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def hrm_login():
    start_time = time.time()

    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    username = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    username.clear()
    username.send_keys("Admin")
    time.sleep(2)

    password = driver.find_element(By.CSS_SELECTOR, "[type='password']")
    password.clear()
    password.send_keys("admin123")

    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    login_button.click()
    time.sleep(2)

    driver.close()

    # Execution End Time
    end_time = time.time()

    # Calculate total time taken
    execution_time = end_time - start_time
    print(execution_time)  # 25.4701726436615


hrm_login()
