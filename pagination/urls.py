from django.conf.urls import url
from .views import *

# Pagination URLs
urlpatterns = [
    url(
        regex='^configurar/$',
        view=pagination_config,
        name='pagination-config'
    ),
    url(
        regex='^configurar/(?P<pk>[0-9]+)$',
        view=pagination_update,
        name='pagination-modify'
    ),
    
    url(
        regex='^eliminar/$',
        view=pagination_delete,
        name='pagination-delete'
    ),
]
