from django.conf.urls.static import static
from django.urls import path, include

from core.views import toCsv

urlpatterns = [
    path(r'schemas/', include('api.schema.urls')),
    path(r'data_types/', include('api.data_type.urls')),
    path(r'data_sets/', include('api.data_set.urls')),
    path(r'columns/', include('api.column.urls')),
    path(r'accounts/', include('api.users.urls'))
]
