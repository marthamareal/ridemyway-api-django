# Third party libraries

from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse

from ridemyway.api.authentication.models import User
from ridemyway.tests.factories.user_factory import UserFactory


class TestLogin(TestCase):
    """Class for testing the User login"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()

        self.login_data = {
            'email': self.user.email,
            'password': 'password123'
        }

    def test_login_with_valid_data_succeeds(self):
        # activate account before login
        self.user.is_active = True
        self.user.save()

        response = self.client.post(reverse('user_login'), data=self.login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_with_inactive_account_fails(self):

        response = self.client.post(reverse('user_login'), data=self.login_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_wrong_password_data_fails(self):
        # activate account before login
        self.user.is_active =True
        self.user.save()

        self.login_data['password'] = 'wrong password'
        response = self.client.post(reverse('user_login'), data=self.login_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_activate_account_succeeds(self):
        response = self.client.get(reverse('user_activate', args=(self.user.token,)))
        self.assertIn('Your account has been activated,', response.data['message'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
