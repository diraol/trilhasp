#-*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from utils.util import IsStaffOrTargetUser
import pdb

class GameCoinModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GameCoinModel to be viewed or edited.
    """
    queryset = GameCoinModel.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = GameCoinModelSerializaer


class GameBusBrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GameBusBrand to be viewed or edited.
    """
    queryset = GameBusBrand.objects.all()
    permission_classes = (IsStaffOrTargetUser,)
    serializer_class = GameBusBrandSerializer


class GameBusModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GameBusModel to be viewed or edited.
    """
    queryset = GameBusModel.objects.all()
    permission_classes = (IsStaffOrTargetUser,)
    serializer_class = GameBusModelSerializer


class GameBusAvailabilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GameBusAvailability to be viewed or edited.
    """
    queryset = GameBusAvailability.objects.all()
    #permission_classes = (IsStaffOrTargetUser,)
    serializer_class = GameBusAvailabilitySerializer




class GamePersonalBusFleetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GamePersonalBusFleet to be viewed or edited.
    """
    queryset = GamePersonalBusFleet.objects.all()
    lookup_field = 'bus_model'
    serializer_class = GamePersonalBusFleetSerializer

    def filter_queryset(self, queryset):
        return GamePersonalBusFleet.objects.filter(user_id=self.request.user.pk)

    def list(self, request):
        queryset = GamePersonalBusFleet.objects.filter(user_id=self.request.user.pk)
        serializer = GamePersonalBusFleetSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class GameFinanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GameFinance to be viewed or edited.
    """
    queryset = GameFinance.objects.all()
    lookup_field = 'coin_model'
    serializer_class = GameFinanceSerializer

    def filter_queryset(self, queryset):
        return GameFinance.objects.filter(user_id=self.request.user.pk)

    def list(self, request):
       queryset = GameFinance.objects.filter(user_id=self.request.user.pk)
       serializer = GameFinanceSerializer(queryset, many=True, context={'request': request})
       return Response(serializer.data)
