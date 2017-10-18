from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^image$', views.serveCaptchaImage),
    url(r'^audio$', views.serveCaptchaAudio),
    url(r'^generate_apikey/$', views.generate_apikey, name="generate_apikey"),
    url(r'^generate_captcha/(?P<public_key>[a-zA-Z0-9]{64})/$', views.generate_captcha, name="generate_captcha"),
    url(r'^validate_captcha/$', views.validate_captcha, name="validate_captcha"),
]
