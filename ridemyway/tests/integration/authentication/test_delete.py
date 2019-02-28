# Third party libraries
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient

from ridemyway.api.utilities.helpers.success_messages import success_message
from ridemyway.tests.factories.user_factory import UserFactory


class TestUserUpdate(TestCase):
    """Class for testing the User update"""

    def setUp(self):
        self.client = APIClient()
        self.user1 = UserFactory()
        self.user2 = UserFactory()
        
    def test_delete_user_succeeds(self):

        response = self.client.delete(reverse('single_user', args=(self.user1.id,)))
        self.assertEqual(response.data['message'], success_message['deleted'].format('User'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_un_existing_user_fails(self):

        response = self.client.delete(reverse('single_user', args=('fake_user_id',)))
        self.assertEqual(response.data['message'], 'Not found')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
