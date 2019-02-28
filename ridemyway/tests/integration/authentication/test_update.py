# Third party libraries
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.test import TestCase
from ridemyway.api.utilities.helpers.error_messages import error_messages
from ridemyway.tests.test_data import invalid_user_data, valid_update_user_data
from ridemyway.tests.factories.user_factory import UserFactory


class TestUserUpdate(TestCase):
    """Class for testing the User update"""

    def setUp(self):
        self.client = APIClient()
        self.user1 = UserFactory()
        self.user2 = UserFactory()

    def test_update_with_valid_data_succeeds(self):

        response = self.client.patch(reverse('single_user',
                                             args=(self.user1.id,)), data=valid_update_user_data)
        self.assertEqual(response.data['data'].get('email'), valid_update_user_data['email'])
        self.assertEqual(response.data['data'].get('username'), valid_update_user_data['username'])
        self.assertEqual(response.data['data'].get('phone_number'), valid_update_user_data['phone_number'])
        self.assertEqual(response.data['data'].get('image_url'), valid_update_user_data['image_url'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_with_invalid_data_fails(self):
        
        response = self.client.patch(reverse('single_user',
                                             args=(self.user1.id,)), data=invalid_user_data)
        self.assertEqual(response.data['errors'].get('username')[0], error_messages['invalid_username'])
        self.assertEqual(response.data['errors'].get('email')[0], error_messages['invalid_email'])
        self.assertEqual(response.data['errors'].get('id_number')[0], error_messages['invalid_id_number'])
        self.assertEqual(response.data['errors'].get('phone_number')[0], error_messages['invalid_phone_number'])
        self.assertEqual(response.data['errors'].get('password')[0], error_messages['invalid_password'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_with_existing_data_fails(self):

        new_user_data = {}
        new_user_data['username'] = self.user2.username
        new_user_data['email'] = self.user2.email
        new_user_data['id_number'] = self.user2.id_number

        response = self.client.patch(reverse('single_user', args=(self.user1.id,)), data=new_user_data)
        self.assertEqual(response.data['errors'].get('email')[0], 'user with this email already exists.')
        self.assertEqual(response.data['errors'].get('username')[0], 'user with this username already exists.')
        self.assertEqual(response.data['errors'].get('id_number')[0], 'user with this id number already exists.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
