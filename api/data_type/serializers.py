from rest_framework import serializers

from core.models import DataType, DataTypeParameter


class DataTypeParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTypeParameter
        fields = '__all__'


class DataTypeSerializer(serializers.ModelSerializer):
    parameters = DataTypeParameterSerializer(many=True)

    class Meta:
        model = DataType
        fields = ['id', 'name', 'data_type', 'parameters']

    def create(self, validated_data):
        parameters_data = validated_data.pop('parameters')
        data_type = DataType.objects.create(**validated_data)
        for parameter_data in parameters_data:
            DataTypeParameter.objects.create(data_type=data_type, **parameter_data)
        return data_type

    def update(self, instance, validated_data):
        parameters_data = validated_data.pop('parameters')
        parameters = instance.parameters.all()
        parameters = list(parameters)

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        for parameter_data in parameters_data:
            parameter = parameters.pop(0)
            parameter.name = parameter_data.get('name', parameter.name)
            parameter.data_type = parameter_data.get('data_type', parameter.data_type)
            parameter.save()

        return instance
