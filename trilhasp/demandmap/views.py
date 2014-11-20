#-*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from django.contrib.gis.geos import Point
from .serializers import *
from utils.util import IsStaffOrTargetUser
import pdb

class GEOLastPositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GeoLastPosition to be viewed or edited.
    """
    queryset = GEOLastPosition.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return GEOLastPositionSerializer
        else:
            return GEOLastAnonPositionSerializer


class LastUserPosition(generics.RetrieveAPIView):
    """
    API endpoint that shows the last position of a specific user
    """
    queryset = GEOLastPosition.objects.all()
    serializer_class = GEOLastPositionSerializer
    lookup_field = 'user'
    permission_classes = (IsStaffOrTargetUser,)

    def get_queryset(self):
        username = self.kwargs['user']
        if username is not None:
            try:
                user = User.objects.get(username=username)
                self.kwargs['user']=user.pk
                return GEOLastPosition.objects.filter(user_id=user.pk)
            except:
                return None
        else:
            return None


class LastUsersAtPosition(generics.ListAPIView):
    serializer_class = GEOLastAnonPositionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        lat = self.kwargs['lat']
        lon = self.kwargs['lon']
        if lat is not None or lon is not None:
            point = Point((float(lon), float(lat)))
            self.kwargs['geolocation'] = point.wkt
            self.queryset = GEOLastPosition.objects.all().extra(
                where=["ST_Distance(geolocation, ST_PointFromText(%s,4326)) <= 0.07000 AND now()::date - timestamp  < interval '1h'"],
                params=[point.wkt]
            )
            return self.queryset
        else:
            return GEOLastPosition.objects.all()


class GEOHistoryPositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GEOHistoryPosition to be viewed or edited.
    """
    queryset = GEOHistoryPosition.objects.all()
    serializer_class = GEOHistoryPositionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsStaffOrTargetUser,)

