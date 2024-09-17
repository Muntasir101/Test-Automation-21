import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import json

# Load configuration data from config.json file
with open('config.json', 'r') as file:
    config = json.load(file)


def testCase_1():
    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step 1: Go to Application page
    # driver.get("https://muntasir101.github.io/Conference-Room-Booking/")
    driver.get(config['test_url'])
    time.sleep(3)

    # step 2:Select Room Type
    room_type = driver.find_element(By.ID, "room-type")
    room_type_options = Select(room_type)
    room_type_options.select_by_value("small")

    # Step 3: Select Start Date
    start_date = driver.find_element(By.ID, "check-in-date")
    start_date.send_keys("2024-09-06")

    # Step 4: Select Start Time
    start_time = driver.find_element(By.ID, "check-in-time")
    start_time.send_keys("10:00")

    # Step 5: Select End Date
    end_date = driver.find_element(By.ID, "check-out-date")
    end_date.send_keys("2024-09-06")

    # Step 6: Select End Time
    end_time = driver.find_element(By.ID, "check-out-time")
    end_time.send_keys("11:00")

    # Step 7: Click "Calculate" button
    calculate_button = driver.find_element(By.CSS_SELECTOR, "#booking-form > button")
    calculate_button.click()

    time.sleep(3)

    # Verify Actual Cost with Expected Cost
    expected_result = "ESTIMATED BOOKING COSTS: $100.00 (0 Weeks, 0 Days, 1 Hours)"

    actual_result = driver.find_element(By.ID, "result").text

    if expected_result == actual_result:
        print("\nTest Case Passed")
        with open("test_result.txt", 'a') as file:
            file.write("\nTest Case 1 Passed.\n")
    else:
        print("\nTest Case Failed !!"
              "\n" "Getting Actual Result: " + actual_result,
              "\n" "But Expected Result: " + expected_result)

        with open("test_result.txt", 'a') as file:
            file.write(
                f"\nTest Case 1 failed !!\n"
                f"Getting Actual Result: {actual_result}\n"
                f"Expected Result: {expected_result}\n"
            )

    driver.close()


testCase_1()
