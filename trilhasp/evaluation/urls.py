#-*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'bus/company', views.BusCompanyViewSet)
router.register(r'bus/line', views.BusLineViewSet)
router.register(r'bus/bus', views.BusesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^bus/line/(?P<bus_line_code>[0-9A-Za-z--]+)/', views.BusLineViewSet, name='bus-line')
]
