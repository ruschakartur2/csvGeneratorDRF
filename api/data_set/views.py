import datetime
from os.path import join

import django_filters.rest_framework
from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from api.data_set.serializers import DataSetSerializer
from core.tasks import generate
from core.models import DataSet
from testTaskCelery import settings


class DataSetViewSet(viewsets.ModelViewSet):
    queryset = DataSet.objects.all().order_by('-id')
    serializer_class = DataSetSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['schema__id', ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        if serializer.is_valid():
            data = serializer.data
            id = data['id']
            res_filename = str(data['schema']['name'].replace(' ', '_')) + '_' + str(
                datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'
            path = join(settings.MEDIA_ROOT, 'files', res_filename)
            rows = data['rows']
            schema = data['schema']['id']
            data_set = generate.delay(id, rows, schema, path, res_filename)

        return Response({'data_set_id': data_set.id, 'id': id, 'schema_id': schema},
                        status=status.HTTP_201_CREATED)
