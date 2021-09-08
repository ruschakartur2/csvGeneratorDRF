from rest_framework import viewsets

from api.column.serializers import SchemaColumnSerializer
from core.models import SchemaColumn


class SchemaColumnViewSet(viewsets.ModelViewSet):
    queryset = SchemaColumn.objects.all()
    serializer_class = SchemaColumnSerializer

