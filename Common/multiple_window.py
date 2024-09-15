import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def switch_window():
    start_time = time.time()

    # launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get("https://the-internet.herokuapp.com/windows")
    wait = WebDriverWait(driver, 10)

    # store the ID of the parent window
    original_window = driver.current_window_handle
    # print(original_window)

    # Check we don't have other window open already
    assert len(driver.window_handles) == 1

    click_here = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Click Here")))
    click_here.click()

    # wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for child_window in driver.window_handles:
        if child_window != original_window:
            driver.switch_to.window(child_window)
            print("Switch to new window Done.")
            print("Child Window Title: " + driver.title)
            # break
        if child_window != original_window:
            driver.switch_to.window(original_window)
            print("Switch to Original window Done.")
            print("Original Window Title: " + driver.title)
            # break
        if child_window != original_window:
            driver.switch_to.window(child_window)
            print("Switch to Child window Done.")
            print("Child Window Title: " + driver.title)
            # break

    # Execution End Time
    end_time = time.time()

    # Calculate total time taken
    execution_time = end_time - start_time
    print(execution_time)


switch_window()
