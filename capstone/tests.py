from django.test import TestCase, Client
from .load_csv_data import load_csv_data
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from django.contrib.auth.models import User
import time
# Create your tests here.


class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
    
    
    # def test_account_creation(self):


    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        
        username_input = self.selenium.find_element_by_xpath("/html/body/div/form/div[4]/a").click()
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('crystal')
        password_input = self.selenium.find_element_by_name("first_password")
        password_input.send_keys('yeohje00')
        second_password_input = self.selenium.find_element_by_name("password")
        second_password_input.send_keys('yeohje00')
        url = self.selenium.get(self.live_server_url)
        print(url)
        username_input = self.selenium.find_element_by_xpath("/html/body/div/form/div[1]/button").click()
        print("hi")
    

        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('crystal')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('yeohje00')
        self.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
        #self.selenium.find_element_by_xpath('/html/body/nav/a')
        url = self.selenium.get(self.live_server_url)
        print(url)

    def wrong_username(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('crystal')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('yeohje00')
        self.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
        message = self.selenium.find_element_by_xpath('/html/body/div/form/p')
        assert message.text =="Your username and password didn't match. Please try again."

    