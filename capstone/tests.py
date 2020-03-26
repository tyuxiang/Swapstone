from django.test import TestCase, Client
from .load_csv_data import load_csv_data
from django.contrib.auth.models import User
# Create your tests here.


class UploadTest(TestCase):
    def test_upload_correct(self):
        client = Client()
        client.post('/')
        User.objects.create_user('crystal',password='yeohje00')
        self.assertTrue(client.login(username = 'crystal', password = 'yeohje00'))

    def load_csv(self):
        c = Client()
        User.objects.create_user('crystal',password='yeohje00')
        c.login(username = 'crystal', password = 'yeohje00')
        with open('../../somedata.xlsx') as fp:
            c.post('/load_csv', {'input': fp})
