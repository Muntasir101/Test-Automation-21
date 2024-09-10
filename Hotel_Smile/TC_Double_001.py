import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_case_1():
    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get("https://www.smilehotel.com.my/web/property/smile-hotel-cheras-cityview/")
    time.sleep(3)

    # Step 2: Select Check-in Date

    start_date = driver.find_element(By.ID, "check_in_date")
    start_date.click()
    start_date.clear()
    start_date.send_keys("2024-09-12")
    time.sleep(3)

    # Step 3: Select Check-out Date
    end_date = driver.find_element(By.ID, "check_out_date")
    end_date.click()
    end_date.clear()
    end_date.send_keys("2024-09-15")
    time.sleep(3)

    # Step 4: Click "Check Availability" button
    availability_button = driver.find_element(By.CSS_SELECTOR, "#frmIndex > div > div.col-search > div > button")
    availability_button.click()

    # Step 5:Select Double No of Room
    no_of_room = driver.find_element(By.CSS_SELECTOR,
                                     "div.roomtype-container:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1) > i:nth-child(1)")
    no_of_room.click()
    no_of_room.click()
    time.sleep(5)

    # Step 6: Click "Book" button
    book_button = driver.find_element(By.CSS_SELECTOR, "#btn_room_1600")
    book_button.click()
    time.sleep(5)

    # Step 7: Click "OK" button for Room Available
    modal = driver.find_element(By.CSS_SELECTOR, ".swal2-popup")
    ok_button = modal.find_element(By.CSS_SELECTOR, ".swal2-confirm")
    ok_button.click()

    # Step 8: Click "Next Step" button
    next_step_button = driver.find_element(By.CSS_SELECTOR, "#frmIndexCore > button")
    next_step_button.click()
    time.sleep(3)


test_case_1()
