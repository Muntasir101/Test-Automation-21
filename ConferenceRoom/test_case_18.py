import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def testCase_18():
    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    driver.get("https://muntasir101.github.io/Conference-Room-Booking/")
    time.sleep(3)

    # step 2:Select Room Type
    room_type = driver.find_element(By.ID, "room-type")
    room_type_options = Select(room_type)
    room_type_options.select_by_value("small")

    # Step 3: Select Start Date
    start_date = driver.find_element(By.ID, "check-in-date")

    current_date = datetime.now()
    formatted_date_current_date = current_date.strftime('%Y-%m-%d')
    start_date.send_keys(formatted_date_current_date)

    # Step 4: Select Start Time
    start_time = driver.find_element(By.ID, "check-in-time")
    start_time.send_keys("10:00")

    # Step 5: Select End Date
    end_date = driver.find_element(By.ID, "check-out-date")

    future_date = current_date + timedelta(days=3)
    formated_future_date = future_date.strftime('%Y-%m-%d')
    end_date.send_keys(formated_future_date)

    # Step 6: Select End Time
    end_time = driver.find_element(By.ID, "check-out-time")
    end_time.send_keys("11:00")

    # Step 7: Click "Calculate" button
    calculate_button = driver.find_element(By.CSS_SELECTOR, "#booking-form > button")
    calculate_button.click()

    time.sleep(3)

    # Verify Actual Cost with Expected Cost
    expected_result = "ESTIMATED BOOKING COSTS: $2500.00 (0 Weeks, 3 Days, 1 Hours)"

    actual_result = driver.find_element(By.ID, "result").text

    if expected_result == actual_result:
        with open("test_result.txt", 'a') as file:
            file.write("\nTest Case 18 Passed.\n")
    else:
        with open("test_result.txt", 'a') as file:
            file.write(
                f"\nTest Case 18 failed !!\n"
                f"Getting Actual Result: {actual_result}\n"
                f"Expected Result: {expected_result}\n"
            )

    driver.close()


testCase_18()
