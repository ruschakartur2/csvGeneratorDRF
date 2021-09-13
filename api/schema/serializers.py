import datetime

from rest_framework import serializers

from api.column.serializers import SchemaColumnSerializer
from core.models import Schema, SchemaColumn


class SchemaSerializer(serializers.ModelSerializer):
    columns = SchemaColumnSerializer(many=True)

    class Meta:
        model = Schema
        fields = ['id', 'name', 'author', 'modified', 'column_separator', 'string_character', 'columns']

    def create(self, validated_data):
        columns_data = validated_data.pop('columns')
        schema = Schema.objects.create(**validated_data)

        for column_data in columns_data:
            SchemaColumn.objects.create(schema=schema, **column_data)
        return schema

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.column_separator = validated_data.get('column_separator', instance.column_separator)
        instance.string_character = validated_data.get('string_character', instance.string_character)
        instance.modified = datetime.datetime.now()
        instance.save()

        columns_data = validated_data.pop('columns')

        for column_data in columns_data:
            column_id = column_data.get('id', None)
            if column_id:
                column = SchemaColumn.objects.get(id=column_id, schema=instance)
                column.name = column_data.get('name', column.name)
                column.data_type = column_data.get('data_type', column.data_type)
                column.save()
            else:
                SchemaColumn.objects.get_or_create(schema=instance, **column_data)
        return instance
