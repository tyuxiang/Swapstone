from django.test import TestCase, Client
from .load_csv_data import load_csv_data
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from django.contrib.auth.models import User
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

    #     print("test_uploadcsv test done!...")

    def test_drag(self):
        print("Testing drag...")
        # booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        booth_test = self.selenium.find_element_by_id('booth-id-30')
        booth_test.click()
        initial_x_offset = booth_test.get_attribute('x')
        initial_y_offset = booth_test.get_attribute('y')
        print(initial_x_offset, initial_y_offset)
        actions = ActionChains(self.selenium)
        actions.drag_and_drop_by_offset(booth_test, '400', '400')
        final_x_offset = booth_test.get_attribute('x')
        final_y_offset = booth_test.get_attribute('y')
        self.assertEqual(initial_x_offset, final_x_offset)
        self.assertEqual(initial_y_offset, final_y_offset)
        self.selenium.find_element_by_xpath('//*[@id="dragbooth-button"]').click()
        actions = ActionChains(self.selenium)
        actions.drag_and_drop_by_offset(booth_test, '400', '400')
        final_x_offset = booth_test.get_attribute('x')
        final_y_offset = booth_test.get_attribute('y')
        print(final_x_offset, final_y_offset)
        self.assertNotEqual(initial_x_offset, final_x_offset)
        self.assertNotEqual(initial_y_offset, final_y_offset)
        self.assertEqual(final_x_offset, '400')
        self.assertEqual(final_y_offset, '400')

    def test_x_input(self):
        print("Testing x_input...")
        # booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        booth_test = self.selenium.find_element_by_id('booth-id-30')
        booth_test.click()
        x_input = self.selenium.find_element_by_id('input-x')
        x_input.clear()
        x_input.send_keys('40')
        time.sleep(1)
        x_offset = booth_test.get_attribute('x')
        self.assertEqual(x_offset, '450')

    def test_y_input(self):
        print("Testing y_input...")
        # booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        booth_test = self.selenium.find_element_by_id('booth-id-30')
        booth_test.click()
        y_input = self.selenium.find_element_by_id('input-y')
        y_input.clear()
        y_input.send_keys('80')
        time.sleep(1)
        y_offset = booth_test.get_attribute('y')
        self.assertEqual(y_offset, '80')


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

    # def test_zoom(self):
    #     map_layout = self.selenium.find_element_by_xpath('//*[@id="map-layout"]')
    #     actions = ActionChains(self.selenium)
    #     actions.move_to_element(map_layout)
    #     actions.double_click()
    #     actions.perform()
    #     scale = map_layout.get_attribute("transform").split(' ')[1][6:-1]
    #     self.assertEqual(scale, '1')
    #     self.selenium.find_element_by_xpath('//*[@id="zoom-button"]').click()
    #     actions.move_to_element(map_layout)
    #     actions.double_click()
    #     actions.perform()
    #     scale = map_layout.get_attribute("transform").split(' ')[1][6:-1]
    #     self.assertNotEqual(scale, '1')
        
    #     print("test_zoom test done!")
