from django.conf.urls.static import static
from django.urls import path, include

from core.views import toCsv

urlpatterns = [
    path(r'schema/', include('api.schema.urls'), name='schemas'),
    path(r'data_types/', include('api.data_type.urls'), name='data_types'),
    path(r'data_sets/', include('api.data_set.urls'), name='data_sets'),
    path(r'column/', include('api.column.urls')),
    path(r'transform/', toCsv, name='tocvs')
]