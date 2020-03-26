from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from django.contrib.auth.models import User
import time

class MySeleniumTests(StaticLiveServerTestCase):
    # fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        User.objects.create_user(username="crystal",password="yeohje00")
        super(MySeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    

    def wrong_username(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        # username_input = self.selenium.find_element_by_name("username")
        # username_input.send_keys('crystal')
        # password_input = self.selenium.find_element_by_name("password")
        # password_input.send_keys('yeohje00')
        # self.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
        # time.sleep(3)
        time.sleep(100)
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
        print("hi")
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('crystal')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('yeohje00')
        self.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
        #self.selenium.find_element_by_xpath('/html/body/nav/a')
        url = self.browser.current_url
        
        
