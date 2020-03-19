from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        # registration new user
        data = {'username': 'test_user', 'email': 'asdf@test.com', 'password': 'qwerty1234'}
        response = self.client.post('http://127.0.0.1:8000/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # try register exiting user
        response = self.client.post('http://127.0.0.1:8000/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)