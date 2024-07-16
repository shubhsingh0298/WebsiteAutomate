from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.common.exceptions import NoSuchElementException

def take_screenshot(driver, file_name):
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    file_path = os.path.join(screenshot_dir, file_name)
    driver.save_screenshot(file_path)
    print(f"Screenshot saved to {file_path}")

driver = webdriver.Chrome()
url = 'https://www.raptorsupplies.com/login'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

try:
    driver.find_element(By.ID, 'email').send_keys('shubham@raptorsupplies.co.uk')
    driver.find_element(By.ID, 'pass').send_keys('Shubham@123')
    driver.find_element(By.ID, 'send2').click()
    take_screenshot(driver, 'login_page.png')
except NoSuchElementException as e:
    print(f"Error occurred: {e}")
    take_screenshot(driver, 'error.png')
finally:
    driver.quit()
