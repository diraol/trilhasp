#-*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoModelSerializer
from models import *
from utils.util import IsStaffOrTargetUser
from django.contrib.auth.models import User


class GameCoinModelSerializaer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GameCoinModel
        fields = (
            'name',
            'value',
            'enabled',
        )


class GameBusBrandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GameBusBrand
        fields = (
            'label',
            'name',
            'logo',
            'enabled'
        )


class GameBusModelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GameBusModel
        fields = (
            'name',
            'bus_brand',
            'efficiency',
            'price',
        )


class GameBusAvailabilitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GameBusAvailability
        fields = (
            'bus_model',
            'available_buses',
        )


class GameFinanceSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field='username'
    )

    class Meta:
        model = GameFinance
        fields = (
            'user',
            'coin_model',
            'amount',
        )


class GamePersonalBusFleetSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field='username'
    )

    class Meta:
        model = GamePersonalBusFleet
        fields = (
            'user',
            'bus_model',
            'amount',
            'last_payment'
        )
