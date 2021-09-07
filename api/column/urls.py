from django.urls import path

from .views import SchemaColumnViewSet

column_list = SchemaColumnViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)
column_detail = SchemaColumnViewSet.as_view(
    {
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
    }
)

urlpatterns = [
    path('', column_list),
    path('<int:pk>', column_detail)
]
