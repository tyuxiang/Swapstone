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
<<<<<<< HEAD
    
    
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
    

=======
        # User.objects.create_user("crystal",password="yeohje00")
    
    def test_login(self):
>>>>>>> 4d12d3c63e77b1843cc10606719c5d832993a101
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('crystal')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('yeohje00')
        self.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
<<<<<<< HEAD
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

    
=======
        message = self.selenium.find_element_by_xpath('/html/body/div/form/p').text
        print(message)
        assert message =="Your username and password didn't match. Please try again."
        # self.selenium.find_element_by_xpath('/html/body/nav/a').click()
        
        


    # def wrong_username(self):
    #     self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
    #     username_input = self.selenium.find_element_by_name("username")
    #     username_input.send_keys('crystal')
    #     password_input = self.selenium.find_element_by_name("password")
    #     password_input.send_keys('yeohje11')
    #     self.selenium.find_element_by_xpath('/html/body/div/form/div[2]/button').click()
    #     message = self.selenium.find_element_by_xpath('/html/body/div/form/p')
    #     assert message =="Your username and password didn't match. Please try again."

    # def load_csv(self):
    #     c = Client()
    #     User.objects.create_user('crystal',password='yeohje00')
    #     c.login(username = 'crystal', password = 'yeohje00')
    #     with open('../../somedata.xlsx') as fp:
    #         c.post('/load_csv', {'input': fp})
>>>>>>> 4d12d3c63e77b1843cc10606719c5d832993a101
