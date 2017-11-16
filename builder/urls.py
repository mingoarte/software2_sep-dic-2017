from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from builder.views import *
from . import views

urlpatterns = [

    # List of URL's related to orders
    url(r'^build/(?P<templateID>[0-9]+)$', editarTemplate.as_view(), name='editar'),
    url(r'^build/$', buildTemplate.as_view(), name='build'),
    url(r'^poll-config/$', views.pollConfig, name='pollConfig'),
    url(r'^faq-config/$', views.faqConfig, name='faqConfig'),
    url(r'^new-template/$', views.newTemplate, name='newTemplate'),
    url(r'^erase-question/$', views.eraseQuestion, name='eraseQuestion'),
    url(r'^create-poll/$', views.createPoll, name='createPoll'),



]