from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^image$', views.serveCaptchaImage),
    url(r'^audio$', views.serveCaptchaAudio),
]
