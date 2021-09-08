import datetime

from celery import shared_task
from celery_progress.backend import ProgressRecorder
import csv

from core.models import Schema, SchemaColumn, DataSet
from faker import Faker

fake = Faker('en_US')
fake1 = Faker('en_GB')


@shared_task(bind=True)
def generate(self, ds_id, rows, schema, filename,res_filename, parameters=None):
    headers = []
    progress_recorder = ProgressRecorder(self)
    result = 0
    parameters = []
    columns = SchemaColumn.objects.filter(schema=schema)
    int_params = [0,100]
    for column in columns:
        headers.append(column.data_type.name)
        if column.data_type.parameters:
            for parameter in column.data_type.parameters.all():
                parameters.append(parameter)

    for param in parameters:
        int_params.append(int(param.value))

    with open(filename, 'w') as csvFile:
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
                "Integer": fake.random_int(min=int_params[0], max=int_params[1]),
            }

            filtered_dict = {}
            for (k, v) in gen_dict.items():
                if k in headers:
                    filtered_dict[k] = v
                    result += i
                    progress_recorder.set_progress(i + 1, rows)

            writer.writerow(filtered_dict)
    dataset = DataSet.objects.get(id=ds_id)
    dataset.status = 'READY'
    dataset.filepath = res_filename
    dataset.save()
    return result
