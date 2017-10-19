from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from builder.views import *
from . import views

urlpatterns = [

    # List of URL's related to orders
    url(r'^build/$', buildTemplate.as_view(), name='build'),
    url(r'^poll-config/$', views.pollConfig, name='pollConfig'),
    


]