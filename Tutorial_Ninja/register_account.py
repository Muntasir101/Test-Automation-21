import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import json
from faker import Faker

fake = Faker()

# Load configuration data from config.json file
with open('TN_Config.json', 'r') as file:
    config = json.load(file)


def register_testCase_valid():
    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get(config['home_page'])
    time.sleep(3)

    # My Account
    my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
    my_account.click()

    register = driver.find_element(By.LINK_TEXT, "Register")
    register.click()
    time.sleep(5)

    first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    first_name.clear()
    first_name.send_keys("Test First Name")

    last_name = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    last_name.clear()
    last_name.send_keys("Test Last Name")

    unique_email = fake.email()
    with open("login_credentials.txt", 'w') as file:
        file.write(unique_email)

    email = driver.find_element(By.CSS_SELECTOR, "#input-email")
    email.clear()
    email.send_keys(unique_email)

    telephone = driver.find_element(By.CSS_SELECTOR, "#input-telephone")
    telephone.clear()
    telephone.send_keys("12345678")

    password = driver.find_element(By.CSS_SELECTOR, "#input-password")
    password.clear()
    password.send_keys("12345678")

    confirm_password = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    confirm_password.clear()
    confirm_password.send_keys("12345678")

    newsletter_yes = driver.find_element(By.CSS_SELECTOR, "label:nth-of-type(1) > input[name='newsletter']")
    newsletter_yes.click()

    privacy_agree = driver.find_element(By.CSS_SELECTOR, "input[name='agree']")
    privacy_agree.click()

    continue_button = driver.find_element(By.CSS_SELECTOR, "input[value='Continue']")
    continue_button.click()

    # Verification account creation
    expected_result = "Your Account Has Been Created!"

    actual_result = driver.find_element(By.CSS_SELECTOR, "#content > h1:nth-child(1)").text

    if expected_result == actual_result:
        with open("TN_test_result.txt", 'a') as file:
            file.write("\nTest Case Passed.Account Creation Success.\n")
    else:
        with open("TN_test_result.txt", 'a') as file:
            file.write(
                f"\nTest Case failed !!\n"
                f"Getting Actual Result: {actual_result}\n"
                f"Expected Result: {expected_result}\n"
            )

    driver.close()


def register_testCase_firstName():
    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get(config['home_page'])
    time.sleep(3)

    # My Account
    my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
    my_account.click()

    register = driver.find_element(By.LINK_TEXT, "Register")
    register.click()
    time.sleep(5)

    first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    first_name.clear()
    first_name.send_keys("")

    last_name = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    last_name.clear()
    last_name.send_keys("Test Last Name")

    unique_email = fake.email()
    with open("login_credentials.txt", 'w') as file:
        file.write(unique_email)

    email = driver.find_element(By.CSS_SELECTOR, "#input-email")
    email.clear()
    email.send_keys(unique_email)

    telephone = driver.find_element(By.CSS_SELECTOR, "#input-telephone")
    telephone.clear()
    telephone.send_keys("12345678")

    password = driver.find_element(By.CSS_SELECTOR, "#input-password")
    password.clear()
    password.send_keys("12345678")

    confirm_password = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    confirm_password.clear()
    confirm_password.send_keys("12345678")

    newsletter_yes = driver.find_element(By.CSS_SELECTOR, "label:nth-of-type(1) > input[name='newsletter']")
    newsletter_yes.click()

    privacy_agree = driver.find_element(By.CSS_SELECTOR, "input[name='agree']")
    privacy_agree.click()

    continue_button = driver.find_element(By.CSS_SELECTOR, "input[value='Continue']")
    continue_button.click()

    # Verification error message for first name
    expected_result = "First Name must be between 1 and 32 characters!"

    actual_result = driver.find_element(By.CSS_SELECTOR, "#account .text-danger").text

    if expected_result == actual_result:
        with open("TN_test_result.txt", 'a') as file:
            file.write("\nError Message for First name display.Test Passed.\n")
    else:
        with open("TN_test_result.txt", 'a') as file:
            file.write(
                f"\nError Message for First name failed !!\n"
                f"Getting Actual Result: {actual_result}\n"
                f"Expected Result: {expected_result}\n"
            )

    driver.close()


def register_testCase_lastName():
    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get(config['home_page'])
    time.sleep(3)

    # My Account
    my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
    my_account.click()

    register = driver.find_element(By.LINK_TEXT, "Register")
    register.click()
    time.sleep(5)

    first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    first_name.clear()
    first_name.send_keys("Test Name")

    last_name = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    last_name.clear()
    last_name.send_keys("")

    unique_email = fake.email()
    with open("login_credentials.txt", 'w') as file:
        file.write(unique_email)

    email = driver.find_element(By.CSS_SELECTOR, "#input-email")
    email.clear()
    email.send_keys(unique_email)

    telephone = driver.find_element(By.CSS_SELECTOR, "#input-telephone")
    telephone.clear()
    telephone.send_keys("12345678")

    password = driver.find_element(By.CSS_SELECTOR, "#input-password")
    password.clear()
    password.send_keys("12345678")

    confirm_password = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    confirm_password.clear()
    confirm_password.send_keys("12345678")

    newsletter_yes = driver.find_element(By.CSS_SELECTOR, "label:nth-of-type(1) > input[name='newsletter']")
    newsletter_yes.click()

    privacy_agree = driver.find_element(By.CSS_SELECTOR, "input[name='agree']")
    privacy_agree.click()

    continue_button = driver.find_element(By.CSS_SELECTOR, "input[value='Continue']")
    continue_button.click()

    # Verification error message for last name
    expected_result = "Last Name must be between 1 and 32 characters!"

    actual_result = driver.find_element(By.CSS_SELECTOR, "#account .text-danger").text

    if expected_result == actual_result:
        with open("TN_test_result.txt", 'a') as file:
            file.write("\nError Message for Last name display.Test Passed.\n")
    else:
        with open("TN_test_result.txt", 'a') as file:
            file.write(
                f"\nError Message for Last name failed !!\n"
                f"Getting Actual Result: {actual_result}\n"
                f"Expected Result: {expected_result}\n"
            )

    driver.close()


"""
register_testCase_valid()
register_testCase_firstName()
register_testCase_lastName()
"""
