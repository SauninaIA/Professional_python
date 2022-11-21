import unittest
import os
from parameterized import parameterized
import requests


YA_TOKEN = os.getenv("YA_TOKEN")
fixture = [
    ("test_folder", YA_TOKEN, 201),
    ("test_folder", YA_TOKEN, 409),
    ("/////", YA_TOKEN, 404),
    ("test_folder", '123error', 401),
]


class TestFunction(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp ===> START TEST')

    def tearDown(self) -> None:
        print('tearDown ===> STOP TEST')

    @parameterized.expand(fixture)
    def test_folder_create(self, path, token, result):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
        }
        create_url = "https://cloud-api.yandex.net/v1/disk/resources"
        create_params = {"path": {path}}
        req_code = requests.put(create_url, headers=headers, params=create_params).status_code
        expected_code = result
        self.assertEqual(req_code, expected_code)






