import datetime

from celery import shared_task
from celery_progress.backend import ProgressRecorder
import csv

from core.models import Schema, SchemaColumn, DataSet
from faker import Faker

fake = Faker('en_US')
fake1 = Faker('en_GB')


@shared_task(bind=True)
def generate(self, rows, schema, filename, parameters=None):
    headers = []
    progress_recorder = ProgressRecorder(self)
    result = 0

    columns = SchemaColumn.objects.filter(schema=schema)

    for column in columns:
        headers.append(column.data_type.name)


    with open('test/'+filename, 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()

        for i in range(rows):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname + "." + Lname + domain_name

            gen_dict = {
                "Email": userId,
                "Full name": fake.name(),
                "Date": fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)),
                'Job': fake.job(),
                'Company name': fake.company(),
                "Phone number": fake1.phone_number(),
                "Address": fake.address(),
                "Integer": fake.random_int(),
            }

            filtered_dict = {}
            for (k, v) in gen_dict.items():
                if k in headers:
                    filtered_dict[k] = v
                    result += i
                    progress_recorder.set_progress(i + 1, rows)

            writer.writerow(filtered_dict)
    return result
