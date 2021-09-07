from django.urls import path

from .views import DataTypeViewSet

data_type_list = DataTypeViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)
data_type_detail = DataTypeViewSet.as_view(
    {
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
    }
)

urlpatterns = [
    path('', data_type_list),
    path('<int:pk>', data_type_detail)
]
