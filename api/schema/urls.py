from django.urls import path

from .views import SchemaViewSet

data_columns_list = SchemaViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)
data_columns_detail = SchemaViewSet.as_view(
    {
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
    }
)

urlpatterns = [
    path('', data_columns_list),
    path('<int:pk>/', data_columns_detail)
]
