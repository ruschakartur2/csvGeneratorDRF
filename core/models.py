from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class DataType(models.Model):
    TYPES = (
        ('EMAIL', 'Email'),
        ('FullName', 'FullName'),
        ('JOB', 'Job'),
        ('PhoneNumber', 'PhoneNumber'),
        ('CompanyName', 'CompanyName'),
        ('TEXT', 'Text'),
        ('INTEGER', 'Integer'),
        ('ADDRESS', 'Address'),
        ('DATE', 'Date')
    )
    name = models.CharField(max_length=225)
    data_type = models.CharField(max_length=11, choices=TYPES)

    def __str__(self):
        return "Type:{0}".format(self.name)


class DataTypeParameter(models.Model):
    name = models.CharField(max_length=255)
    data_type = models.ForeignKey(
        DataType, on_delete=models.CASCADE, related_name="parameters")
    value = models.CharField(max_length=255)  # сериализированное значение параметра

    def __str__(self):
        return self.name


class Schema(models.Model):
    name = models.CharField(max_length=255)
    column_separator = models.CharField(max_length=25)
    string_character = models.CharField(max_length=25)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SchemaColumn(models.Model):
    name = models.CharField(max_length=255)
    data_type = models.ForeignKey(DataType,
                                  related_name='column',
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=True)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='columns')
    order = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name


class DataSet(models.Model):
    STATUS = (
        ('PROCESSING', 'Processing'),
        ('READY', 'Ready'),
    )
    schema = models.ForeignKey(Schema,
                               related_name='schema',
                               on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS, default='PROCESSING')
    rows = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    filepath = models.CharField(max_length=255, blank=True, null=True)
