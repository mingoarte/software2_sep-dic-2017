from django.conf.urls import url
from .views import CarouselContentListView, CarouselContentCreateView, CarouselContentUpdateView

# Carousel URLs
urlpatterns = [
    url(
        regex='^carousel/index/$',
        view=CarouselContentListView.as_view(),
        name='carousel-list'
    ),
    url(
        regex='^carousel/create/$',
        view=CarouselContentCreateView.as_view(),
        name='carousel-create',
    ),
    url(
        regex='^carousel/(?P<pk>\d+)/update/$',
        view=CarouselContentUpdateView.as_view(),
        name='carousel-update'
    ),
]
