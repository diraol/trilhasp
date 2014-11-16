#-*- coding: utf-8 -*-
__author__ = 'diraol'

from django.shortcuts import render
from models import *
from rest_framework import viewsets
from serializers import *

# Create your views here.
class BusCompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Bus Companies to be viewed or edited.
    """
    queryset = BusCompanies.objects.all()
    serializer_class = BusCompaniesSerializer


class BusLineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Bus Lines to be viewed or edited.
    """
    queryset = BusLine.objects.all()
    serializer_class = BusLineSerializer
    lookup_field = 'bus_line_code'


class BusesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Buses to be viewed or edited.
    """
    queryset = Buses.objects.all()
    serializer_class = BusesSerializer
