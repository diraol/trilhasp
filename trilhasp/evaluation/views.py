#-*- coding: utf-8 -*-

#from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .permissions import IsStaffOrTargetUser


# Create your views here.
class BusCompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Bus Companies to be viewed or edited.
    """
    queryset = BusCompanies.objects.all()
    serializer_class = BusCompaniesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BusLineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Bus Lines to be viewed or edited.
    """
    queryset = BusLine.objects.all()
    serializer_class = BusLineSerializer
    lookup_field = 'bus_line_code'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BusesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Buses to be viewed or edited.
    """
    queryset = Buses.objects.all()
    serializer_class = BusesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EVALAnswerModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows answer models to be viewed or edited
    """
    queryset = EVALAnswerModel.objects.all()
    serializer_class = EVALAnswerModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EVALQuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = EVALQuestion.objects.all()
    serializer_class = EVALQuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EVALAnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users answers to be viewed or edited.
    """
    queryset = EVALAnswer.objects.all()
    serializer_class = EVALAnswerSerializer


###############################################################################
##                     Classes for the Users                                 ##
###############################################################################


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    lookup_field = 'username'
    permission_classes = (IsStaffOrTargetUser,)

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),


