from django.test import TestCase, Client
from .load_csv_data import load_csv_data
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from django.contrib.auth.models import User
import time

class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        cls.selenium.get('%s%s' % (cls.live_server_url, '/'))
        username_input = cls.selenium.find_element_by_xpath("/html/body/div/form/div[4]/a").click()
        username_input = cls.selenium.find_element_by_name("username")
        username_input.send_keys('crystal')
        password_input = cls.selenium.find_element_by_name("first_password")
        password_input.send_keys('yeohje00')
        second_password_input = cls.selenium.find_element_by_name("password")
        second_password_input.send_keys('yeohje00')
        username_input = cls.selenium.find_element_by_xpath("/html/body/div/form/div[1]/button").click()
        cls.selenium.get('%s%s' % (cls.live_server_url, '/accounts/login/'))
        username_input = cls.selenium.find_element_by_name("username")
        username_input.send_keys('crystal')
        password_input = cls.selenium.find_element_by_name("password")
        password_input.send_keys('yeohje00')
        cls.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
        time.sleep(1)
        cls.selenium.refresh()
        
    # def wrong_username(self):

    #     self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        # username_input = self.selenium.find_element_by_name("username")
        # username_input.send_keys('crystal')
        # password_input = self.selenium.find_element_by_name("password")
        # password_input.send_keys('yeohje00')
        # self.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
        # time.sleep(3)
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
        
        

    

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        
        username_input = self.selenium.find_element_by_xpath("/html/body/div/form/div[4]/a").click()
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('crystal')
        password_input = self.selenium.find_element_by_name("first_password")
        password_input.send_keys('yeohje00')
        second_password_input = self.selenium.find_element_by_name("password")
        second_password_input.send_keys('yeohje00')
        username_input = self.selenium.find_element_by_xpath("/html/body/div/form/div[1]/button").click()
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('crystal')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('yeohje00')
        self.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
        time.sleep(1)
        self.selenium.refresh()

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

    def test_drag(self):
        booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        initial_x_offset = booth_test.get_attribute('x')
        initial_y_offset = booth_test.get_attribute('y')
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
        self.assertNotEqual(initial_x_offset, final_x_offset)
        self.assertNotEqual(initial_y_offset, final_y_offset)
        self.assertEqual(final_x_offset, '400')
        self.assertEqual(final_y_offset, '400')

    def test_x_input(self):
        booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        x_input = self.selenium.find_element_by_name('input-x')
        x_input.send_keys('600')
        x_offset = booth_test.get_attribute('x')
        self.assertEqual(x_offset, '600')

    def test_y_input(self):
        booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        y_input = self.selenium.find_element_by_name('input-y')
        y_input.send_keys('600')
        y_offset = booth_test.get_attribute('y')
        self.assertEqual(y_offset, '600')


    def test_length_input(self):
        booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        length_input = self.selenium.find_element_by_name('input-length')
        length_input.send_keys('3')
        length_offset = booth_test.get_attribute('height')
        self.assertEqual(length_offset, '40.191')

    def test_width_input(self):
        booth_test = self.selenium.find_element_by_xpath('//*[@id="booth-id-1"]')
        width_input = self.selenium.find_element_by_name('input-width')
        width_input.send_keys('4')
        width_offset = booth_test.get_attribute('width')
        self.assertEqual(width_offset, '53.588')
