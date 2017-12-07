from django.conf.urls import url
from .views import *

# Cards URLs
urlpatterns = [
    url(
        regex = '^configurar/$',
        view = formattedContentConfig,
        name = 'formattedcontent-config'
    ),
    url(
        regex = '^configurar/(?P<pk>[0-9]+)$',
        view = formattedContentUpdate,
        name = 'formattedcontent-modify'
    ),
    url(
        regex = '^eliminar/$',
        view = formattedContentDelete,
        name = 'formattedcontent-delete'
    ),
]
