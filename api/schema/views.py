import django_filters
from rest_framework import viewsets, filters

from core.models import Schema

from .serializers import SchemaSerializer


class SchemaViewSet(viewsets.ModelViewSet):
    queryset = Schema.objects.all().order_by('-id')
    serializer_class = SchemaSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author__id', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

