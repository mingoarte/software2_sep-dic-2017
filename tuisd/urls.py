from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^showCaptcha/$', views.showCaptcha, name='showCaptcha'),
    url(r'^showCaptchaCode/$', views.showCaptchaCode, name='showCaptchaCode'),
    url(r'^demo/$', views.demoCaptcha, name='demoCaptcha'),

]
