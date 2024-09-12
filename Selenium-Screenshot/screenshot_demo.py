import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def hrm_login():
    start_time = time.time()

    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='username']")))
    username.clear()
    username.send_keys("Admin")
    time.sleep(2)
    driver.save_screenshot("Username_Typed.png")

    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[type='password']")))
    password.clear()
    password.send_keys("admin123")
    time.sleep(2)
    driver.save_screenshot("Password_Typed.png")

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".orangehrm-login-button")))
    login_button.click()

    driver.close()

    # Execution End Time
    end_time = time.time()

    # Calculate total time taken
    execution_time = end_time - start_time
    print(execution_time)  # 14.589903354644775


hrm_login()
