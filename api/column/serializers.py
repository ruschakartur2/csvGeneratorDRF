from rest_framework import serializers

from api.data_type.serializers import DataTypeSerializer
from core.models import SchemaColumn


class SchemaColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchemaColumn
        fields = ['id', 'name', 'data_type']

    def create(self, validated_data):
        data_type = validated_data.pop('data_type')
        column = SchemaColumn.objects.create(**validated_data)
        return column

    def to_representation(self, instance):
        self.fields['data_type'] = DataTypeSerializer(read_only=True)
        return super(SchemaColumnSerializer, self).to_representation(instance)