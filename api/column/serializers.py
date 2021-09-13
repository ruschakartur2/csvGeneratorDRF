from rest_framework import serializers

from api.data_type.serializers import DataTypeSerializer
from core.models import SchemaColumn


class SchemaColumnSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = SchemaColumn
        fields = ['id', 'name', 'data_type']

