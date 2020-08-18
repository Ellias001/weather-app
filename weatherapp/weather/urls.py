from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_city, name='delete_city'),
]