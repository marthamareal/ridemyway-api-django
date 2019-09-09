from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from ridemyway.tests.factories.user_factory import UserFactory

from ridemyway.api.vehicle.models import Vehicle


class BaseTestCase(APITestCase):
    """A base test class that is used to setup test and admin user
    and authorization headers. This class is reusable to other test
    classes.
    """
    def setUp(self):
        self.client = APIClient()
        self.test_user = self.setup_user()
        self.admin_user = self.setup_admin_user()
        self.login_uri = reverse('user_login')

    def setup_user(self):
        user = UserFactory()
        user.is_active = True
        user.save()
        return user
    
    def setup_admin_user(self):
        admin_user = UserFactory()
        admin_user.is_active = True
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

        return admin_user
    
    def login_client(self, uri, params):
        response = self.client.post(uri, params, format="json")
        return response
    
    def set_authorization_header(self, uri, params):
        self.token = self.login_client(uri, params).data["token"]
        self.client.credentials(HTTP_AUTHORIZATION=self.token)


class VehicleBaseTestCase(BaseTestCase):
    """A base test class to setup vehicle reusable for integration testing
    with vehicle endpoints.
    """
    def setUp(self):
        super().setUp()
        self.vehicle = self.setup_vehicle()
        self.vehicle_uri = reverse("vehicle:create_list_vehicles")
    
    def setup_vehicle(self):
        vehicle = Vehicle.objects.create(
            number_plate="TEST 490S",
            category="CR",
            color="Black",
            make="TEST-BMW",
            model="2018",
            user_id=self.admin_user
        )

        return vehicle
