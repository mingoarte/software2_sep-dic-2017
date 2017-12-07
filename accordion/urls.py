from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^acordeon/$', accordionList, name='accordion-list'),
    url(r'^crear-acordeon/$', accordionCreate, name='accordion-create'),
    url(r'^editar/(?P<accordion_id>[\w\-]+)$', accordionEdit, name='accordion-edit'),
    url(r'^get-modal-editar-panel/$', accordionModalEdit, name='accordion-modal-edit'),
    url(r'^eliminar/(?P<accordion_id>[\w\-]+)$', accordionDelete, name='accordion-delete'),
]
