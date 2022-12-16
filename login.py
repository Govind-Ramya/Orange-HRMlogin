from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest

class TestLogTest(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    @classmethod
    def test_setUpClass(self):
        self.driver.maximize_window()

    def test_01_right_login(self):
        #open_url
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        #enter_login_credential
        self.driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
        self.driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        #click_logout
        self.driver.find_element(By.XPATH,'//span/img[@alt="profile picture"]').click()
        self.driver.find_element(By.XPATH,'//a[text()="Logout"]').click()

    def test_02_wrong_login(self):
        # open_url
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # enter_login_credential
        self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Invalid password")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        pop_up = self.driver.find_element(By.XPATH, '//div/p[text()="Invalid credentials"]')
        msg = pop_up.text
        if msg == "Invalid credentials":
            print("Invalid login credential message appears")


    @classmethod
    def test_tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("test sucessfuly completed")
if __name__ == '__main__':
    unittest.main()


