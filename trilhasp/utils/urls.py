#-*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from .views import *
from evaluation.views import *
from demandmap.views import *

router = routers.DefaultRouter()
router.register(r'user', UserView)
router.register(r'evaluation/bus/company', BusCompanyViewSet)
router.register(r'evaluation/bus/line', BusLineViewSet)
router.register(r'evaluation/bus', BusesViewSet)
router.register(r'evaluation/answer/model', EVALAnswerModelViewSet)
router.register(r'evaluation/question', EVALQuestionViewSet)
router.register(r'evaluation/answer', EVALAnswerViewSet)
router.register(r'position/last', GEOLastPositionViewSet)
router.register(r'position/history', GEOHistoryPositionViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^evaluation/bus/line/(?P<bus_line_code>[0-9A-Za-z--]+)/', BusLineViewSet.as_view(), name='bus-line'),
    url(r'^position/last/user/(?P<user>[^/.]+)/$', LastUserPosition.as_view(), name='lastlocation-detail'),
    url(r'^position/last/users/(?P<lon>(-?\d+\.\d+))_(?P<lat>(-?\d+\.\d+))/$', LastUsersAtPosition.as_view(), name='lastuserslocation-detail'),
]
