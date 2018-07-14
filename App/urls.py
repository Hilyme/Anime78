#!/usr/bin/python3
# Author : Hily
# file: urls
# @Time: 18-7-14 下午3:30
from django.conf.urls import url

from App import views

urlpatterns = {
    url(r'^index/', views.index, name='index'),
    url(r'^register/', views.Register.as_view(), name='register'),
    url(r'^login/', views.Login.as_view(), name='login'),
}
