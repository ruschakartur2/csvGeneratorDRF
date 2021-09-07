from rest_framework import viewsets

from api.data_type.serializers import DataTypeSerializer
from core.models import DataType


class DataTypeViewSet(viewsets.ModelViewSet):
    queryset = DataType.objects.all()
    serializer_class = DataTypeSerializer

