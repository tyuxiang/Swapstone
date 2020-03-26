from django.test import TestCase, Client
from .load_csv_data import load_csv_data
# Create your tests here.


class UploadTest(TestCase):
    def test_upload_correct(self):
        client = Client()
        client.post('/')
        self.assertTrue(client.login(username = 'crystal', password = 'yeohje00'))
