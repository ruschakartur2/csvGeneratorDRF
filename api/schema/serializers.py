from rest_framework import serializers

from api.column.serializers import SchemaColumnSerializer
from core.models import Schema, SchemaColumn


class SchemaSerializer(serializers.ModelSerializer):
    columns = SchemaColumnSerializer(many=True)

    class Meta:
        model = Schema
        fields = ['id', 'name', 'column_separator', 'string_character', 'columns']

    def create(self, validated_data):
        columns_data = validated_data.pop('columns')
        schema = Schema.objects.create(**validated_data)
        for column_data in columns_data:
            SchemaColumn.objects.create(schema=schema, **column_data)
        return schema

    def update(self, instance, validated_data):
        columns_data = validated_data.pop('columns')
        columns = instance.columns.all()
        columns = list(columns)

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        for column_data in columns_data:
            column = columns.pop(0)
            column.name = column_data.get('name', column.name)
            column.data_type = column_data.get('data_type', column.data_type)
            column.save()

        return instance
