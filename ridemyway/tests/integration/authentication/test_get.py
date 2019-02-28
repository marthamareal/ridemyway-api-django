# Third party libraries
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient

from ridemyway.tests.factories.user_factory import UserFactory

class TestGerUser(TestCase):
    """Class for testing the User get"""

    def setUp(self):
        self.client = APIClient()
        self.user1 = UserFactory()
        self.user2 = UserFactory()

    def test_get_user_list_succeeds(self):

        response = self.client.get(reverse('create_and_list_users'))
        self.assertEqual(len(response.data['data']), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_user_succeeds(self):

        response = self.client.get(reverse('single_user', args=(self.user1.id,)))
        self.assertEqual(response.data['data'].get('username'), self.user1.username)
        self.assertEqual(response.data['data'].get('email'), self.user1.email)
        self.assertEqual(response.data['data'].get('id_number'), self.user1.id_number)
        self.assertEqual(response.data['data'].get('phone_number'), self.user1.phone_number)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_un_existing_user_fails(self):

        response = self.client.get(reverse('single_user', args=('fake-id',)))
        self.assertEqual(response.data['message'], 'Not found')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
