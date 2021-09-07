from django.contrib import admin

from core.models import DataType, Schema, SchemaColumn, DataTypeParameter, DataSet

admin.site.register(DataType)
admin.site.register(Schema)
admin.site.register(SchemaColumn)
admin.site.register(DataTypeParameter)
admin.site.register(DataSet)
