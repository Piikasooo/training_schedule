from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        # registration new user
        data = {'username': 'pika', 'email': 'asdf@test.com', 'password': '1'}
        response = self.client.post('http://127.0.0.1:8000/users/api/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # try register exiting user
        response = self.client.post('http://127.0.0.1:8000/users/api/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TokenAuthorizationTestCase(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('admin_pika', 'admin_pika@test.com', '1')
        self.user = User.objects.create_user('pika', 'pika@test.com', '1')
        self.client = APIClient()

        data = {'username': 'admin_pika', 'password': '1'}
        response = self.client.post('http://127.0.0.1:8000/api-token-auth/', data)
        self.admin_access_token = response.json()['token']

        data = {'username': 'pika', 'password': '1'}
        response = self.client.post('http://127.0.0.1:8000/api-token-auth/', data)
        self.user_access_token = response.json()['token']

    def test_admin_login(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_access_token)
        response = self.client.get('http://127.0.0.1:8000/users/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_access_token)
        response = self.client.get('http://127.0.0.1:8000/users/api/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PermissionTestCase(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.user = User.objects.create_user('pika', 'pika@snow.com', '1')

    def test_unauthorized(self):
        response = self.client.get('http://127.0.0.1:8000/users/api/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_forbidden(self):
        self.client.login(username='pika', password='1')
        response = self.client.get('http://127.0.0.1:8000/users/api/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_permission(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('http://127.0.0.1:8000/users/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

