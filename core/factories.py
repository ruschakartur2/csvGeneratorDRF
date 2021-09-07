import factory
from factory.django import DjangoModelFactory


from .models import Schema


class SchemaFactory(DjangoModelFactory):
    class Meta:
        model = Schema

    name = factory.Faker("Name")