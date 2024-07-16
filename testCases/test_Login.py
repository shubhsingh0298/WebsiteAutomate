import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_Login(self):
        self.driver.find_element(By.ID, 'eve_13').click()
        self.driver.find_element(By.ID, 'email').send_keys('shubham@raptorsupplies.co.uk')
        self.driver.find_element(By.ID, 'pass').send_keys('Shubham@123')
        self.driver.find_element(By.ID, 'send2').click()

if __name__ == "__main__":
    pytest.main()
