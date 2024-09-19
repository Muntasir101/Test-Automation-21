import json
import logging
import os

import pytest
from selenium import webdriver

from Framework.pages.login_page import LoginPage
from Framework.common.configure_config import load_config
import pandas as pd

# Load configuration data from config.json file
config = load_config()


# load test data from excel
def load_test_data(file_path):
    return pd.read_excel(file_path)


@pytest.fixture(params=['chrome', 'firefox', 'edge'])
def setup_driver(request):
    browser = request.param
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.quit()


@pytest.mark.usefixtures("setup_driver")
class TestLogin:
    def test_login_dd_tn(self):
        data_file = os.path.join(os.getcwd(), 'Framework', 'Data', "login_data.xlsx")
        test_data = load_test_data(data_file)

        for index, row in test_data.iterrows():
            email = row['Email']
            password = row['Password']

            self.driver.get(config['login_page'])

            login_page = LoginPage(self.driver)

            login_page.enter_email(email)

            login_page.enter_password(password)

            login_page.click_login()
