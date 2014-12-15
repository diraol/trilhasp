# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import *
from django.contrib.auth.models import User

###############################################################################
##                     Classes for the buses                                 ##
###############################################################################


class BusCompaniesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusCompanies
        fields = ('company_name', 'logo')


class BusLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusLine
        fields = ('bus_line_code', 'going_bus_name', 'return_bus_name', 'active', 'company_name')


class BusesSerializer(serializers.HyperlinkedModelSerializer):
    #bus_line_code = serializers.HyperlinkedRelatedField(
    #    view_name='bus-line',
    #    lookup_field='bus_line_code'
    #)

    class Meta:
        model = Buses
        fields = ('bus_unique_number', 'bus_line_code', 'active')


###############################################################################
##                     Classes from Evaluation module                        ##
###############################################################################


class EVALAnswerModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EVALAnswerModel
        fields = (
            'answer',
            'lower_limit_text',
            'upper_limit_text',
            'middle_text',
            'lower_limit_value',
            'upper_limit_value',
            'middle_value'
        )


class EVALQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EVALQuestion
        fields = ('id','question', 'answer', 'enabled')


class EVALAnswerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name = 'user-detail',
        lookup_field = 'username'
    )
    class Meta:
        model = EVALAnswer
        fields = (
            'question',
            'user',
            'timestamp',
            'bus_unique_number',
            'answer_value',
            'answer_text',
            'geolocation'
        )
