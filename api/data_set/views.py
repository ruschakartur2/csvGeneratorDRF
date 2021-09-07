import datetime

from rest_framework import viewsets, status
from rest_framework.response import Response

from api.data_set.serializers import DataSetSerializer
from core.tasks import generate
from core.models import DataSet


class DataSetViewSet(viewsets.ModelViewSet):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        if serializer.is_valid():
            data = serializer.data
            filename = str(data['schema']['name']) + '_' + str(datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'
            rows = data['rows']
            schema = data['schema']['id']
            data_set = generate.delay(rows, schema, filename)

        return Response({'data_set_id': data_set.id}, status=status.HTTP_201_CREATED)
