from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        # registration new user
        data = {'username': 'pika', 'email': 'asdf@test.com', 'password': '1'}
        response = self.client.post('http://127.0.0.1:8000/users/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # try register exiting user
        response = self.client.post('http://127.0.0.1:8000/users/users/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PermissionTestCase(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.user = User.objects.create_user('pika', 'pika@snow.com', '1')

    def test_unauthorized(self):
        response = self.client.get('http://127.0.0.1:8000/users/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_forbiden(self):
        self.client.login(username='pika', password='1')
        response = self.client.get('http://127.0.0.1:8000/users/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_permission(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('http://127.0.0.1:8000/users/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

