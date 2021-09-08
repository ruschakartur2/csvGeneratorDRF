from rest_framework import serializers

from api.schema.serializers import SchemaSerializer
from core.models import DataSet


class DataSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSet
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['schema'] = SchemaSerializer(read_only=True)
        return super(DataSetSerializer, self).to_representation(instance)


