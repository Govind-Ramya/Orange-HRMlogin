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
         def test_03_PIM_add_personaldata(self):
        # open_url
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        # give_login_credentials
        xpath_username = "//input[@placeholder='Username']"
        self.driver.find_element(By.XPATH, xpath_username).send_keys("Admin")
        time.sleep(5)
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        time.sleep(5)

        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        time.sleep(5)
        # gotoPIM
        self.driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        # Name_detail
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("x")

        middle = "//input[@placeholder='Middle Name']"
        self.driver.find_element(By.XPATH, middle).send_keys("x")

        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("x")

        self.driver.find_element(By.XPATH,'//label[text()="Employee Id"]//following::div[1]/input').clear()
        #self.driver.find_element(By.XPATH,'//label[text()="Employee Id"]//following::div[1]/input').click()
        self.driver.find_element(By.XPATH, '//label[text()="Employee Id"]//following::div[1]/input[1]').send_keys("4735")
        save_1 = self.driver.find_element(By.XPATH, '//p[text()=" * Required"]/following::button[@type="submit"]').click()
        time.sleep(5)
        # Additional_details

        Ot_Id = self.driver.find_element(By.XPATH, '//label[text()="Other Id"]/following::div[1]/input').send_keys("002")
        time.sleep(3)
        driversliscenceno = self.driver.find_element(By.XPATH, '//label[text()="Other Id"]/following::input[2]').send_keys("LN1")
        time.sleep(3)
        driver_liscence_date = self.driver.find_element(By.XPATH,'//label[text()="License Expiry Date"]/following::div[1]//input').send_keys("2024-06-08")
        time.sleep(5)
        SSNnumber = self.driver.find_element(By.XPATH, '//label[text()="SSN Number"]/following::div[1]/input').send_keys("20")
        time.sleep(5)
        sinnumber = self.driver.find_element(By.XPATH, '//label[text()="SIN Number"]/following::div[1]/input').send_keys("2002")
        time.sleep(3)
        nationality = self.driver.find_element(By.XPATH,'//label[text()="Nationality"]/following::div[1]//div[text()="-- Select --"]').click()
        time.sleep(3)
        selectcounty = self.driver.find_element(By.XPATH, '//span[text()="Angolan"]').click()
        time.sleep(3)
        marital_status = self.driver.find_element(By.XPATH,'//label[text()="Marital Status"]/following::div[text()="-- Select --"][1]').click()
        time.sleep(5)
        click_single = self.driver.find_element(By.XPATH, '//span[text()="Single"]').click()
        time.sleep(5)
        DOB = self.driver.find_element(By.XPATH,'//label[text()="Date of Birth"]/following::div[3]/input[@placeholder="yyyy-mm-dd"]').send_keys("1990-09-19")
        time.sleep(5)
        selectgender = self.driver.find_element(By.XPATH,'//input[@value="1"]/following::span[1]').click()
        time.sleep(5)
        military = self.driver.find_element(By.XPATH,'//label[text()="Military Service"]/following::div[1]//input').send_keys("yes")
        time.sleep(5)
        Smoker = self.driver.find_element(By.XPATH, '//input[@value="1"]/following::span[3]').click()
        time.sleep(5)
        save_2 = self.driver.find_element(By.XPATH,'//div/p[text()=" * Required"]/following::button[@type="submit"][1]').click()
        time.sleep(5)
        blood = self.driver.find_element(By.XPATH, '//label[text()="Blood Type"]/following::div[4]').click()
        time.sleep(5)
        select_blood = self.driver.find_element(By.XPATH, '//span[text()="O+"]').click()
        time.sleep(5)
        save_3 = self.driver.find_element(By.XPATH,'//div/p[text()=" * Required"]/following::button[@type="submit"][2]').click()
        time.sleep(5)
        pop_msg = self.driver.find_element(By.ID,"oxd-toaster_1").text
        print(pop_msg)
        time.sleep(5)
        print("Testcase3:","Personal details added sucessfully")


    def test_04_pim_edit(self):
        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys("Admin")
        time.sleep(5)
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        time.sleep(5)
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        time.sleep(5)
        # gotoPIM
        self.driver.find_element(By.XPATH,'//span[text()="PIM"]').click()
        time.sleep(5)
        editbutton = self.driver.find_element(By.XPATH,'//div[9]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//button[1]//i[1]').click()
        time.sleep(5)
        nickname = self.driver.find_element(By.XPATH,'//label[text()="Nickname"]/following::div[1]/input').clear()
        time.sleep(3)
        nickname = self.driver.find_element(By.XPATH,'//label[text()="Nickname"]/following::div[1]/input').send_keys("zoop")
        time.sleep(3)
        edit_save = self.driver.find_element(By.XPATH,'//div/p[text()=" * Required"]/following::button[@type="submit"][1]').click()
        time.sleep(3)
        print("Testcase4:","Editing is done sucessfully")
        
    def test_05_pim_delete(self):
        # open_url
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        # give_login_credentials
        xpath_username = "//input[@placeholder='Username']"
        self.driver.find_element(By.XPATH, xpath_username).send_keys("Admin")
        time.sleep(5)
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        time.sleep(5)

        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        time.sleep(5)
        # gotoPIM
        self.driver.find_element(By.XPATH,'//span[text()="PIM"]').click()
        time.sleep(5)
        deletebutton = self.driver.find_element(By.XPATH,'//div[9]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//button[1]//i[1]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//p[text()="Are you Sure?"]//following::button[2]/i').click()
        time.sleep(3)
        print("Testcase5:","deletion is done sucessfully")


    @classmethod
    def test_tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("test sucessfuly completed")
if __name__ == '__main__':
    unittest.main()


