import factory
from core.tests import faker

from users.models import CustomUser


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.LazyAttribute(lambda _: faker.user_name())
    email = factory.LazyAttribute(lambda _: faker.email())
    first_name = factory.LazyAttribute(lambda _: faker.first_name())
    last_name = factory.LazyAttribute(lambda _: faker.last_name())
    # TODO: use traits for nullable fields
    speciality = factory.LazyAttribute(lambda _: faker.sentence()[:50])
    description = factory.LazyAttribute(lambda _: " ".join(faker.sentences(nb=5)))
    # TODO: skills?
    country = factory.LazyAttribute(lambda _: faker.country())
    city = factory.LazyAttribute(lambda _: faker.city())
    phone = factory.LazyAttribute(lambda _: faker.phone_number())
