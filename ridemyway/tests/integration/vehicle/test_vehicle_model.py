from django.test import TestCase

from ridemyway.api.vehicle.models import Vehicle
from ridemyway.tests.factories.vehicle_factory import VehicleFactory


class VehicleTestCase(TestCase):
    def setUp(self):
        self.vehicle = VehicleFactory()
    
    def test_vehicle(self):
        self.assertEqual(Vehicle.objects.count(), 1)
    
    def test_string_representation(self):
        self.assertEqual(str(self.vehicle), self.vehicle.number_plate)
