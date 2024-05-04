import factory
from core.tests import faker

from users.models import CustomUser


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.LazyAttribute(lambda _: faker.user_name())
    email = factory.LazyAttribute(lambda _: faker.email())

    class Params:
        with_first_name = factory.Trait(first_name=faker.first_name())
        with_last_name = factory.Trait(last_name=faker.last_name())
        with_speciality = factory.Trait(speciality=faker.sentence()[:50])
        with_skills = factory.Trait(skills=faker.words(nb=10))
        with_description = factory.Trait(description=" ".join(faker.sentences(nb=5)))
        with_country = factory.Trait(country=faker.country())
        with_city = factory.Trait(city=faker.city())
        with_phone = factory.Trait(phone=faker.phone_number())
