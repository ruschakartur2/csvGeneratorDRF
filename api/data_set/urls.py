from django.urls import path

from .views import DataSetViewSet

ds_list = DataSetViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)
ds_detail = DataSetViewSet.as_view(
    {
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
    }
)

urlpatterns = [
    path('', ds_list),
    path('<int:pk>/', ds_detail)
]
