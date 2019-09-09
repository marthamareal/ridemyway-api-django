import factory
from faker import Factory

from .user_factory import UserFactory
from ridemyway.api.vehicle.models import Vehicle

faker = Factory.create()

class VehicleFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Vehicle
    
    number_plate = factory.LazyAttribute(lambda _: faker.text(10))
    category = 'CR'
    color = factory.LazyAttribute(lambda _: faker.text(10))
    make = factory.LazyAttribute(lambda _: faker.text(10))
    model = factory.LazyAttribute(lambda _: faker.text(10))
    user_id = factory.SubFactory(UserFactory)
