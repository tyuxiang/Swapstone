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
        # time.sleep(5)
        # self.selenium.find_element_by_xpath('/html/body/div/div/nav[1]/div/ul[1]/li[2]/a').click()
        # time.sleep(1)
        # self.selenium.find_element_by_xpath('/html/body/div/div/main/div/div/form/button').click()
        # self.selenium.find_element_by_name('input').click()
        #url = self.browser.current_url
        map_layout = self.selenium.find_element_by_xpath('//*[@id="map-layout"]')
        actions = ActionChains(self.selenium)
        actions.move_to_element(map_layout)
        actions.double_click()
        actions.perform()
        # scale = map_layout.get_attribute("transform")
        # if (scale != '2'):
        #     print("Zoom Test Case 1 - Before Clicking Zoom and Pan Button: TRUE")
        # else:
        #     print("Zoom Test Case 1 - before Clicking Zoom and Pan Button: FALSE")
    
        self.selenium.find_element_by_xpath('//*[@id="zoom-button"]').click()
        actions.move_to_element(map_layout)
        actions.double_click()
        actions.perform()
        scale = map_layout.get_attribute("transform").split(' ')[1][6:-1]
        if (scale == '2'):
            print("Zoom Test Case 2 - After Clicking Zoom and Pan Button: TRUE")
        else:
            print("Zoom Test Case 2 - After Clicking Zoom and Pan Button: FALSE")
        