import time

from selenium import webdriver


def go_to_application_page():
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get("https://muntasir101.github.io/Conference-Room-Booking/")
    time.sleep(5)

    driver.close()


go_to_application_page()
