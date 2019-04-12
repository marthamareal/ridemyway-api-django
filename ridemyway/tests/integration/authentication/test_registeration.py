# Third party libraries

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from ridemyway.api.utilities.helpers.error_messages import error_messages
from ridemyway.tests.test_data import valid_user_data, invalid_user_data, missing_field_user_data



class TestRegistration(TestCase):
    """Class for testing the User registration"""
    
    def setUp(self):
        self.client = APIClient()
        self.register_response = self.client.post(reverse('create_and_list_users'), data=valid_user_data)

    def test_registration_with_valid_data_succeeds(self):

        self.assertIn( 'Your account has been successfully created.', self.register_response.data['message'],)
        self.assertEqual(self.register_response.status_code, status.HTTP_201_CREATED)

    def test_registration_with_invalid_data_fails(self):

        response = self.client.post(reverse('create_and_list_users'), data=invalid_user_data)
        self.assertEqual(response.data['errors'].get('username')[0], error_messages['invalid_username'])
        self.assertEqual(response.data['errors'].get('email')[0], error_messages['invalid_email'])
        self.assertEqual(response.data['errors'].get('id_number')[0], error_messages['invalid_id_number'])
        self.assertEqual(response.data['errors'].get('phone_number')[0], error_messages['invalid_phone_number'])
        self.assertEqual(response.data['errors'].get('password')[0], error_messages['invalid_password'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_missing_field_data_fails(self):

        response = self.client.post(reverse('create_and_list_users'), data=missing_field_user_data)
        self.assertEqual(response.data['errors'].get('username')[0], error_messages['field_required'])
        self.assertEqual(response.data['errors'].get('phone_number')[0],  error_messages['field_required'])
        self.assertEqual(response.data['errors'].get('id_number')[0], error_messages['field_required'])
        self.assertEqual(response.data['errors'].get('password')[0], error_messages['field_required'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_existing_data_fails(self):

        response = self.client.post(reverse('create_and_list_users'), data=valid_user_data)
        self.assertEqual(response.data['errors'].get('email')[0], 'user with this email already exists.')
        self.assertEqual(response.data['errors'].get('username')[0], 'user with this username already exists.')
        self.assertEqual(response.data['errors'].get('id_number')[0],'user with this id number already exists.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
