from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
import datetime


class AddTaskTestCase(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.user = User.objects.create_user('pika', 'pika@snow.com', '1')

    def test_add_task(self):
        # test permission (user not admin cant create task)
        data = {"date": "2021-01-01", "start_time": "12:12 AM", "end_time": "12:13 AM", "person_id": "1"}
        self.client.login(username='pika', password='1')
        response = self.client.post('http://127.0.0.1:8000/training/api/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # test permission (admin can create task)
        self.client.login(username='john', password='johnpassword')
        response = self.client.post('http://127.0.0.1:8000/training/api/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # date in the past
        data = {"date": f"{(datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')}",
                "start_time": f"{(datetime.datetime.now()).time().strftime('%H:%M %p')}",
                "end_time": f"{(datetime.datetime.now() + datetime.timedelta(minutes=30)).time().strftime('%H:%M %p')}",
                "person_id": "1"}
        response = self.client.post('http://127.0.0.1:8000/training/api/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['non_field_errors'], ['The date cannot be in the past!'])

        # today but time in the past
        data = {"date": f"{datetime.datetime.today().strftime('%Y-%m-%d')}",
                "start_time": f"{(datetime.datetime.now() - datetime.timedelta(hours=1)).time().strftime('%H:%M %p')}",
                "end_time": f"{(datetime.datetime.now() - datetime.timedelta(minutes=30)).time().strftime('%H:%M %p')}",
                "person_id": "1"}
        response = self.client.post('http://127.0.0.1:8000/training/api/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['non_field_errors'], ["The time cannot be in the past!"])

        # start_time > end_time
        data = {"date": f"{datetime.datetime.today().strftime('%Y-%m-%d')}",
                "start_time": f"{(datetime.datetime.now()).time().strftime('%H:%M %p')}",
                "end_time": f"{(datetime.datetime.now() - datetime.timedelta(minutes=30)).time().strftime('%H:%M %p')}",
                "person_id": "1"}
        response = self.client.post('http://127.0.0.1:8000/training/api/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['non_field_errors'], ["The end_time cannot be before start_time!"])