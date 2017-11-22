from django.conf.urls import url
from .views import CarouselConfig, CarouselDelete

# Carousel URLs
urlpatterns = [
    url(
        regex='^carousel/configurar/$',
        view=CarouselConfig,
        name='carousel-config'
    ),
    url(
        regex='^carousel/configurar/(?P<pk>[0-9]+)$',
        view=CarouselConfig,
        name='carousel-modify'
    ),
    url(
        regex='^carousel/eliminar/$',
        view=CarouselDelete,
        name='carousel-delete'
    ),
]
