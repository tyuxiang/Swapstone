from django.test import TestCase, Client
from .load_csv_data import load_csv_data
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import sys, os

username = "crystal"
password = "yeohje00"

class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting Up...")
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        cls.selenium.get('%s%s' % (cls.live_server_url, '/'))
        
        # username_input = cls.selenium.find_element_by_xpath("/html/body/div/form/div[4]/a").click()
        cls.selenium.find_element_by_xpath("/html/body/div/form/div[4]/a").click()
        
        # username_input = cls.selenium.find_element_by_name("username")
        # username_input.send_keys('crystal')
        cls.selenium.find_element_by_name("username").send_keys(username)

        # password_input = cls.selenium.find_element_by_name("first_password")
        # password_input.send_keys('yeohje00')
        cls.selenium.find_element_by_name("first_password").send_keys(password)
        
        # password_input = cls.selenium.find_element_by_name("password")
        # password_input.send_keys('yeohje00')
        cls.selenium.find_element_by_name("password").send_keys(password)
        # username_input = cls.selenium.find_element_by_xpath("/html/body/div/form/div[1]/button").click()
        cls.selenium.find_element_by_xpath("/html/body/div/form/div[1]/button").click()

        # cls.selenium.get('%s%s' % (cls.live_server_url, '/accounts/login/'))
        print("Setting Up Done...")
        # username_input = cls.selenium.find_element_by_name("username")
        # username_input.send_keys('crystal')
        # password_input = cls.selenium.find_element_by_name("password")
        # password_input.send_keys('yeohje00')
        # cls.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
        # time.sleep(1)
        # cls.selenium.refresh()
        
    def test_1wrong_username(self):
        print("Testing wrong_username...")
        # username_input = cls.selenium.find_element_by_name("username")
        # username_input.send_keys('crystal')
        # password_input = cls.selenium.find_element_by_name("password")
        # password_input.send_keys('yeohje00')
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        self.selenium.find_element_by_name("username").send_keys("wrong" + username)
        # self.selenium.find_element_by_name("username").send_keys(username)
        self.selenium.find_element_by_name("password").send_keys("wrong" + password)
        # self.selenium.find_element_by_name("password").send_keys(password)

        self.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
        time.sleep(3)

        if (self.selenium.find_element_by_xpath('/html/body/div/form/p')):
            found = True
        else :
            found = False

        self.assertEqual(found, True)

        # time.sleep(100)
        # map_layout = self.selenium.find_element_by_name("map-layout")
        # actions = ActionChains(self.selenium)
        # actions.move_to_element(map_layout)
        # actions.double_click()
        # actions.perform()
        # self.assertEqual(response.status_code, 200)
        # password_input = self.selenium.find_element_by_name("password")
        # password_input.send_keys('secret')
        # self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()# Create your tests here.
        # self.selenium.find_element_by_xpath('/html/body/nav/a').click()

        print("Wrong_username test done!...")
        
        
    # tests both login and loading the csv file
    def test_2login(self):
        print("Testing test_login...")
        self.setUpClass()
        # self.selenium.get('%s%s' % (self.live_server_url, '/'))
        
        # username_input = self.selenium.find_element_by_xpath("/html/body/div/form/div[4]/a").click()
        # username_input = self.selenium.find_element_by_name("username")
        # username_input.send_keys('crystal')

        # password_input = self.selenium.find_element_by_name("first_password")
        # password_input.send_keys('yeohje00')

        # second_password_input = self.selenium.find_element_by_name("password")
        # second_password_input.send_keys('yeohje00')
        # username_input = self.selenium.find_element_by_xpath("/html/body/div/form/div[1]/button").click()
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        time.sleep(2)
        # username_input = self.selenium.find_element_by_name("username")
        # username_input.send_keys('crystal')
        self.selenium.find_element_by_name("username").send_keys(username)
        print("done this : " + username)
        # password_input = self.selenium.find_element_by_name("password")
        # password_input.send_keys('yeohje00')
        self.selenium.find_element_by_name("password").send_keys(password)
        print("done this : " + password)

        self.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
        time.sleep(1)
        self.selenium.refresh()

        if (self.selenium.current_url.find("login") == -1):
            login = True
        else:
            login = False

        self.assertEqual(login, True)

        time.sleep(3)
        self.selenium.find_element_by_xpath('/html/body/div/div/nav[1]/div/ul[1]/li[2]/a').click()
        time.sleep(3)
        # self.selenium.find_element_by_xpath('/html/body/div/div/main/div/div/form/input[2]').click()
        self.selenium.find_element_by_name('input').send_keys("C:\\Users\\HansingJ\\Desktop\\Swapstone\\data.xlsx")
        time.sleep(2)    
        self.selenium.find_element_by_xpath('/html/body/div/div/main/div/div/form/button').click()
        time.sleep(2)    
        self.selenium.find_element_by_xpath('/html/body/div/div/nav[2]/div/form/button').click()
        time.sleep(10)
        # self.selenium.

        print("test_login test done!")


    # def test_3uploadcsv(self):
        
    #     self.selenium.find_element_by_xpath('/html/body/div/div/nav[1]/div/ul[1]/li[2]/a').click()
    #     self.selenium.find_element_by_xpath('/html/body/div/div/main/div/div/form/input[2]').click()
    #     self.selenium.send_keys('data.xlsx')
    #     self.selenium.find_element_by_name('input').send_keys("C:\\Users\\HansingJ\\Desktop\\Swapstone\\data.xlsx")
    #     time.sleep(2)    
    #     self.selenium.find_element_by_xpath('/html/body/div/div/main/div/div/form/button').click()
    #     time.sleep(2)    
    #     self.selenium.find_element_by_xpath('/html/body/div/div/nav[2]/div/form/button').click()

    #     print("test_uploadcsv test done!...")

class FunctionalityTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting Up...")
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)


        cls.selenium.execute_script("document.body.style.zoom='20%'")
        # Create Account
        cls.selenium.get('%s%s' % (cls.live_server_url, '/'))
        cls.selenium.find_element_by_xpath("/html/body/div/form/div[4]/a").click()
        cls.selenium.find_element_by_name("username").send_keys(username)
        cls.selenium.find_element_by_name("first_password").send_keys(password)
        cls.selenium.find_element_by_name("password").send_keys(password)
        cls.selenium.find_element_by_xpath("/html/body/div/form/div[1]/button").click()

        # Log in
        cls.selenium.get('%s%s' % (cls.live_server_url, '/accounts/login/'))
        time.sleep(2)
        cls.selenium.find_element_by_name("username").send_keys(username)
        cls.selenium.find_element_by_name("password").send_keys(password)
        cls.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
        time.sleep(1)
        cls.selenium.refresh()
        
        # Upload CSV
        cls.selenium.find_element_by_xpath('/html/body/div/div/nav[1]/div/ul[1]/li[2]/a').click()
        time.sleep(2)
        cls.selenium.find_element_by_name('input').send_keys("C:\\Users\\HansingJ\\Desktop\\Swapstone\\data.xlsx")
        time.sleep(2)    
        cls.selenium.find_element_by_xpath('/html/body/div/div/main/div/div/form/button').click()
        time.sleep(2)    
        cls.selenium.find_element_by_xpath('/html/body/div/div/nav[2]/div/form/button').click()
        time.sleep(10)

        print("Setting Up Done...")

    def test_drag(self):
        print("Testing drag...")
        # booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        booth_test = self.selenium.find_element_by_id('booth-id-30')
        booth_test.click()
        initial_x_offset = booth_test.get_attribute('x')
        initial_y_offset = booth_test.get_attribute('y')
        print(initial_x_offset, initial_y_offset)
        actions = ActionChains(self.selenium)
        # actions.click_and_hold(booth_test)
        # actions.move_by_offset(100, 100)
        # actions.release()
        actions.drag_and_drop_by_offset(booth_test, 20, 415)
        actions.perform()
        final_x_offset = booth_test.get_attribute('x')
        final_y_offset = booth_test.get_attribute('y')
        self.assertEqual(initial_x_offset, final_x_offset)
        self.assertEqual(initial_y_offset, final_y_offset)
        self.selenium.find_element_by_xpath('//*[@id="dragbooth-button"]').click()
        actions = ActionChains(self.selenium)
        actions.drag_and_drop_by_offset(booth_test, 20, 415)
        # actions.click_and_hold(booth_test)
        # actions.move_by_offset(100, 100)
        # actions.release()
        actions.perform()
        final_x_offset = booth_test.get_attribute('x')
        final_y_offset = booth_test.get_attribute('y')
        print(final_x_offset, final_y_offset)
        self.assertNotEqual(initial_x_offset, final_x_offset)
        self.assertNotEqual(initial_y_offset, final_y_offset)
        self.assertEqual(float(final_x_offset), float(initial_x_offset) + 20)
        self.assertEqual(float(final_y_offset), float(initial_y_offset) + 415)

    def test_x_input(self):

        print("Testing x_input...")
        # booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        booth_test = self.selenium.find_element_by_id('booth-id-30')
        booth_test.click()
        x_input = self.selenium.find_element_by_id('input-x')
        x_input.clear()
        x_input.send_keys('440')
        time.sleep(1)
        x_offset = booth_test.get_attribute('x')
        self.assertEqual(x_offset, '440')

    def test_y_input(self):
        print("Testing y_input...")
        # booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        booth_test = self.selenium.find_element_by_id('booth-id-30')
        booth_test.click()
        y_input = self.selenium.find_element_by_id('input-y')
        y_input.clear()
        y_input.send_keys('1020')
        time.sleep(1)
        y_offset = booth_test.get_attribute('y')
        self.assertEqual(y_offset, '1020')


    def test_length_input(self):
        print("Testing length_input...")
        # booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        booth_test = self.selenium.find_element_by_id('booth-id-30')
        booth_test.click()
        length_input = self.selenium.find_element_by_id('input-length')
        length_input.clear()
        length_input.send_keys('3')
        time.sleep(1)
        length_offset = booth_test.get_attribute('height')
        self.assertEqual(length_offset, '40.191')

    def test_width_input(self):
        print("Testing width_input...")
        # booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        booth_test = self.selenium.find_element_by_id('booth-id-30')
        booth_test.click()
        width_input = self.selenium.find_element_by_id('input-width')
        width_input.clear()
        width_input.send_keys('4')
        time.sleep(1)
        width_offset = booth_test.get_attribute('width')
        self.assertEqual(width_offset, '53.588')

    def test_x_NaNinput(self):
        print("Testing x_NaNinput...")
        booth_test = self.selenium.find_element_by_id('booth-id-30')
        booth_test.click()
        x = booth_test.get_attribute('x')
        x_input = self.selenium.find_element_by_id('input-x')
        x_input.clear()
        x_input.send_keys('NaN')
        time.sleep(1)
        alert = False

        try:
            WebDriverWait(self.selenium, 3).until(EC.alert_is_present(), 'Timed out waiting for PA creation confirmation popup to appear.')
            alert = self.selenium.switch_to.alert
            alert.accept()
            alert = True
        except TimeoutException:
            alert = False

        self.assertEqual(alert, True, "NaN input")

        x_input.clear()
        time.sleep(1)
        x_input.send_keys(x)

    def test_zoom(self):
        map_layout = self.selenium.find_element_by_xpath('//*[@id="map-layout"]')
        actions = ActionChains(self.selenium)
        actions.move_to_element(map_layout)
        actions.double_click()
        actions.perform()
        scale = map_layout.get_attribute("transform").split(' ')[1][6:-1]
        self.assertEqual(scale, '1')
        self.selenium.find_element_by_xpath('//*[@id="zoom-button"]').click()
        actions.move_to_element(map_layout)
        actions.double_click()
        actions.perform()
        scale = map_layout.get_attribute("transform").split(' ')[1][6:-1]
        self.assertNotEqual(scale, '1')
        
        print("test_zoom test done!")

class CSV_Tests(StaticLiveServerTestCase):

    path = "C:\\Users\\Tan Yu Xiang\\Desktop\\SUTD\\Year 2\\Term 5\\Elements of Software Construction\\ESC Project\\Swapstone\\Excel Testing\\BlackBoard Testing\\"

    @classmethod
    def setUpClass(cls):
        print("Setting Up...")
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        cls.selenium.get('%s%s' % (cls.live_server_url, '/'))

        time.sleep(1)

        print("Setting Up Done...")

    def create_user(self):
        # Click on the create account button
        self.selenium.find_element_by_xpath("/html/body/div/form/div[4]/a").click()
        
        # Key in username, first password and key in the password agn
        self.selenium.find_element_by_name("username").send_keys(username)
        self.selenium.find_element_by_name("first_password").send_keys(password)
        self.selenium.find_element_by_name("password").send_keys(password)

        # Click on the create account button and go back to login page
        self.selenium.find_element_by_xpath("/html/body/div/form/div[1]/button").click()
        self.selenium.find_element_by_xpath("/html/body/div/form/div[2]/a").click()
        print("Created account")
        time.sleep(1)

    def login(self):
        # Login
        self.selenium.find_element_by_name("username").send_keys(username)
        self.selenium.find_element_by_name("password").send_keys(password)
        self.selenium.find_element_by_xpath("/html/body/div/form/div[2]/button").click()
        print("Logged in")
        time.sleep(1)

    def upload_csv(self, file):
        # self.selenium.find_element_by_xpath("/html/body/div/div/nav[1]/div/ul[1]/li[2]/a").click()
        self.selenium.find_element_by_id("load_csv").click()
        time.sleep(1)
        self.selenium.find_element_by_name('input').send_keys(self.path + file)
        time.sleep(1)    
        self.selenium.find_element_by_xpath('/html/body/div/div/main/div/div/form/button').click()
        print("Uploaded excel file")
        time.sleep(2)

    def test_normal_csv(self):
        time.sleep(2)
        print("Testing uploading of normal csv")
        file = "2by2.xlsx"
        self.selenium.refresh()
        self.create_user()
        self.login()
        self.upload_csv(file)
        try: self.selenium.find_element_by_id("map-item-2by2.xlsx")
        except NoSuchElementException: self.fail("normal map could not be found")

    def test_empty_csv(self):
        print("Testing uploading of empty csv")
        file = "Empty.xlsx"
        self.selenium.refresh()
        self.create_user()
        self.login()
        self.upload_csv(file)
        try:
            WebDriverWait(self.selenium, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
            self.selenium.switch_to.alert.accept()
        except TimeoutException:
            self.fail("Alert did not show even though excel file is empty")

    def test_1booth_csv(self):
        time.sleep(2)
        print("Testing uploading of correct csv with 1 booth")
        file = "2by2_1.xlsx"
        self.selenium.refresh()
        self.create_user()
        self.login()
        self.upload_csv(file)
        allBooths = self.selenium.find_elements_by_class_name("booth-link")
        numOfBooths = len(allBooths)
        self.assertEqual(numOfBooths,1)

    # def test_oversized_csv(self):
    #     print("Testing uploading of oversized csv")
    #     file = "Oversized.xlsx"
    #     self.selenium.refresh()
    #     self.create_user()
    #     self.login()
    #     self.upload_csv(file)
    #     try: self.selenium.find_element_by_id("map-item-Oversized.xlsx")
    #     except NoSuchElementException: self.fail("uploaded map cannot be found")

    def test_999booth_csv(self):
        time.sleep(2)
        print("Testing uploading of correct csv with 1 booth")
        file = "2by2_999.xlsx"
        self.selenium.refresh()
        self.create_user()
        self.login()
        self.upload_csv(file)
        allBooths = self.selenium.find_elements_by_class_name("booth-link")
        numOfBooths = len(allBooths)
        self.assertEqual(numOfBooths,999)

    def test_1booth_missingName_csv(self):
        time.sleep(2)
        print("Testing uploading of correct csv with 1 booth")
        file = "2by2_1_missingName.xlsx"
        self.selenium.refresh()
        self.create_user()
        self.login()
        self.upload_csv(file)
        try:
            WebDriverWait(self.selenium, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
            self.selenium.switch_to.alert.accept()
        except TimeoutException:
            self.fail("Alert did not show even though excel file has a missing name")

    def test_1booth_missingSize_csv(self):
        time.sleep(2)
        print("Testing uploading of correct csv with 1 booth")
        file = "2by2_1_emptyLength.xlsx"
        self.selenium.refresh()
        self.create_user()
        self.login()
        self.upload_csv(file)
        try:
            WebDriverWait(self.selenium, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
            self.selenium.switch_to.alert.accept()
        except TimeoutException:
            self.fail("Alert did not show even though excel file has a missing size")

    def test_1booth_missingIndustry_csv(self):
        time.sleep(2)
        print("Testing uploading of correct csv with 1 booth")
        file = "2by2_1_emptyIndustry.xlsx"
        self.selenium.refresh()
        self.create_user()
        self.login()
        self.upload_csv(file)
        try:
            WebDriverWait(self.selenium, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
            self.selenium.switch_to.alert.accept()
        except TimeoutException:
            self.fail("Alert did not show even though excel file has a missing industry")

    # @classmethod
    # def tearDownClass(cls):
    #     cls.selenium.quit()
    #     super().tearDownClass()
