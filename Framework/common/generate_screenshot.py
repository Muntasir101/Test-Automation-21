import os


def save_screenshot(driver, filename):
    driver.save_screenshot(
        os.path.join(os.getcwd(), 'Framework', 'Screenshots', filename))
