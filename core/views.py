import csv
from django.shortcuts import redirect
from django.http import HttpResponse
from faker import Faker

from .models import Schema, SchemaColumn
from .tasks import generate
from faker import Faker

fake = Faker()


def toCsv(request):
    print(request)
    if generate.delay():
        response = redirect('/')

        return response
