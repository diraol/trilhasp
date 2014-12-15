#-*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoModelSerializer
from models import *
from utils.util import IsStaffOrTargetUser
from django.contrib.auth.models import User


class GEOLastPositionSerializer(GeoFeatureModelSerializer):
    id = serializers.Field()
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field='username'
    )

    class Meta:
        model = GEOLastPosition
        geo_field = "geolocation"
        fields = (
            'id',
            'user',
            'geolocation',
            'timestamp'
        )
        read_only_fields = ('timestamp',)


class GEOLastAnonPositionSerializer(GeoFeatureModelSerializer):
    id = serializers.Field()

    class Meta:
        geo_field = 'geolocation'
        model = GEOLastPosition
        fields = (
            'id',
            'geolocation',
            'timestamp'
        )
        read_only_fields = ('timestamp',)


class GEOHistoryPositionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field='username'
    )

    class Meta:
        model = GEOHistoryPosition
        geo_field = "geolocation"
        fields = (
            'user',
            'geolocation',
            'timestamp'
        )
        read_only_fields = ('timestamp',)
