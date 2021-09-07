from rest_framework import viewsets

from core.models import Schema

from .serializers import SchemaSerializer


class SchemaViewSet(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer

