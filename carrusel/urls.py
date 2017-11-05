from django.conf.urls import url
from .views import CarouselListView, CarouselCreateView, CarouselUpdateView

# Carousel URLs
urlpatterns = [
    url(
        regex='^$',
        view=CarouselListView.as_view(),
        name='carousel-list'
    ),
    url(
        regex='^create/$',
        view=CarouselCreateView.as_view(),
        name='carousel-create',
    ),
    url(
        regex='^(?P<pk>\d+)/update/$',
        view=CarouselUpdateView.as_view(),
        name='carousel-update'
    ),
]
