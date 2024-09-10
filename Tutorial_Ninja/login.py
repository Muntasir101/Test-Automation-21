import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import json

# Load configuration data from config.json file
with open('TN_Config.json', 'r') as file:
    config = json.load(file)


def testCase_valid_1():
    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get(config['home_page'])
    time.sleep(3)

    # My Account
    my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
    my_account.click()

    login = driver.find_element(By.LINK_TEXT, "Login")
    login.click()
    time.sleep(5)

    email = driver.find_element(By.CSS_SELECTOR, "#input-email")
    email.clear()

    registered_email = open("login_credentials.txt", "r").readline()
    email.send_keys(registered_email)

    password = driver.find_element(By.CSS_SELECTOR, "#input-password")
    password.clear()
    password.send_keys("12345678")

    login_button = driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[value='Login']")
    login_button.click()

    # Verification Login Success
    expected_title = "My Account"

    actual_title = driver.title

    if expected_title == actual_title:
        with open("TN_test_result.txt", 'a') as file:
            file.write("\nTest Case Passed. Login Success.\n")
    else:
        with open("TN_test_result.txt", 'a') as file:
            file.write(
                f"\nTest Case failed !!\n"
                f"Getting Actual Result: {actual_title}\n"
                f"Expected Result: {expected_title}\n"
            )

    driver.close()


testCase_valid_1()
