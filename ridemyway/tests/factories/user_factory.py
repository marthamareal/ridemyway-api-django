import factory
from faker import Factory

from ridemyway.api.authentication.models import User

faker = Factory.create()

class UserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = User
    
    email = factory.LazyAttribute(lambda _: faker.email())
    username = factory.LazyAttribute(lambda _: faker.text(50))
    phone_number = factory.LazyAttribute(lambda _: faker.text(20))
    id_number = factory.LazyAttribute(lambda _: faker.text(50))
    status = factory.LazyAttribute(lambda _: faker.word(['active', 'deactive']))
    image_url = factory.LazyAttribute(lambda _: faker.text(255))
    password = factory.LazyAttribute(lambda _: faker.text(20))