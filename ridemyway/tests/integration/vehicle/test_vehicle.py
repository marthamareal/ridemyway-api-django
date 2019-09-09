from ridemyway.tests.base_test_case import VehicleBaseTestCase
from ridemyway.tests.test_data import (vehicle_data,
                                       invalid_vehicle_category_choice,
                                       empty_vehicle_data,
                                       vehicle_data_no_number_plate,
                                       vehicle_data_invalid_plate,)


class TestVehicle(VehicleBaseTestCase):
    def test_create_vehicle(self):
        admin_login = {
            "email":  self.admin_user.email,
            "password": "password123"
        }

        self.set_authorization_header(self.login_uri, admin_login)

        response = self.client.post(self.vehicle_uri, vehicle_data, format="json")
        self.assertEqual(
            response.status_code,
            201,
            "Expected Response Code 201, received {0} instead.".format(
                response.status_code
            )
        )
        self.assertIn("Vehicle successfully created", str(response.data))
    
    def test_create_vehicle_with_empty_data(self):
        admin_login = {
            "email":  self.admin_user.email,
            "password": "password123"
        }

        self.set_authorization_header(self.login_uri, admin_login)

        response = self.client.post(self.vehicle_uri, empty_vehicle_data, format="json")
        self.assertEqual(
            response.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(
                response.status_code
            )
        )
        self.assertIn("This field is required.", str(response.data))

    def test_create_vehicle_with_invalid_number_plate(self):
        admin_login = {
            "email":  self.admin_user.email,
            "password": "password123"
        }

        self.set_authorization_header(self.login_uri, admin_login)

        response = self.client.post(self.vehicle_uri, vehicle_data_invalid_plate, format="json")
        self.assertEqual(
            response.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(
                response.status_code
            )
        )
        self.assertIn("Invalid number plate format", str(response.data))
    
    def test_create_vehicle_with_missing_number_plate(self):
        admin_login = {
            "email":  self.admin_user.email,
            "password": "password123"
        }

        self.set_authorization_header(self.login_uri, admin_login)

        response = self.client.post(self.vehicle_uri, vehicle_data_no_number_plate, format="json")
        self.assertEqual(
            response.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(
                response.status_code
            )
        )
        self.assertIn("This field may not be blank.", str(response.data))
    
    def test_create_vehicle_with_invalid_category_choice(self):
        admin_login = {
            "email":  self.admin_user.email,
            "password": "password123"
        }

        self.set_authorization_header(self.login_uri, admin_login)

        response = self.client.post(self.vehicle_uri, invalid_vehicle_category_choice, format="json")
        self.assertEqual(
            response.status_code,
            400,
            "Expected Response Code 400, received {0} instead.".format(
                response.status_code
            )
        )
        self.assertIn(f'"{invalid_vehicle_category_choice["category"]}" is not a valid choice.',
                      str(response.data))
    
    def test_get_vehicle_list(self):
        user_login = {
            "email":  self.test_user.email,
            "password": "password123"
        }

        self.set_authorization_header(self.login_uri, user_login)

        response = self.client.get(self.vehicle_uri, format="json")
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )
