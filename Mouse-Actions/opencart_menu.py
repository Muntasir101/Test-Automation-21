import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


def main_menu():
    start_time = time.time()

    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get("https://demo.opencart.com/")

    menu_desktops = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Desktops")))

    actions = ActionChains(driver)
    actions.move_to_element(menu_desktops)
    actions.perform()

    submenu_mac = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Mac (1)")))
    submenu_mac.click()

    # Execution End Time
    end_time = time.time()
    # Calculate total time taken
    execution_time = end_time - start_time
    print(execution_time)


main_menu()
