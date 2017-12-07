from django.conf.urls import url
from .views import BreadcrumbConfig

urlpatterns = [
    url(
        regex='^breadcrumb/configurar/$',
        view=BreadcrumbConfig,
        name='breadcrumb-config'
    ),
]