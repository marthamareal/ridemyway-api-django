import factory
from faker import Factory

from ridemyway.api.authentication.models import User

faker = Factory.create()

class UserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = User
    
    email = factory.LazyAttribute(lambda _: faker.email())
    username = factory.LazyAttribute(lambda _: faker.profile().get('username'))
    phone_number = factory.LazyAttribute(lambda _: faker.text(20))
    id_number = factory.LazyAttribute(lambda _: faker.text(50))
    image_url = factory.LazyAttribute(lambda _: faker.text(255))
    password = factory.PostGenerationMethodCall('set_password', 'password123')
    is_active = factory.LazyAttribute(lambda _: False)