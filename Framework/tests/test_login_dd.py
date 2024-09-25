import json
import logging
import os
from Framework.pages.login_page import LoginPage
from Framework.common.configure_config import load_config
import pandas as pd

# Load configuration data from config.json file
config = load_config()


# load test data from excel
def load_test_data(file_path):
    return pd.read_excel(file_path)


def test_login_dd_tn(setup_driver):
    driver = setup_driver
    logging.info("Test Start...")

    data_file = os.path.join(os.getcwd(), 'Framework', 'Data', "login_data.xlsx")
    test_data = load_test_data(data_file)

    for index, row in test_data.iterrows():
        email = row['Email']
        password = row['Password']

        driver.get(config['login_page'])

        login_page = LoginPage(driver)
        logging.info("Go to Login Page...")

        login_page.enter_email(email)
        logging.info(f"Enter Email: {email}")

        login_page.enter_password(password)
        logging.info(f"Enter Password: {password}")

        login_page.click_login()
        logging.info("Click Login Button...")

        logging.info("Test Completed.")
