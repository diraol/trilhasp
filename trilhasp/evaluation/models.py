#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.gis.db import models
import datetime

# Create your models here.

###############################################################################
##                     Classes for the buses                                 ##
###############################################################################


class BusCompanies(models.Model):
    company_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.company_name


class BusLine(models.Model):
    """ This class contains all bus lines and their informations """
    bus_line_code = models.CharField(max_length=10)
    going_bus_name = models.CharField(max_length=200)
    return_bus_name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
     #Name of the company responsible for this bus line
    company_name = models.ForeignKey('BusCompanies')

    def __unicode__(self):
        return self.bus_line_code


class Buses(models.Model):
    """ Class that represents each 'car' from the fleet """
    bus_unique_number = models.IntegerField(unique=True)
    bus_line_code = models.ForeignKey('BusLine')
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.bus_unique_number) + "(" + self.bus_line_code + ")"


###############################################################################
##                     Classes from Evaluation module                        ##
###############################################################################


class EVALAnswerModel(models.Model):
    """ Model of possible answers for a question. Used to build the
        evaluation form
    """
    answer = models.CharField(max_length=200)
    lower_limit_text = models.CharField(max_length=30, default="Péssimo")
    upper_limit_text = models.CharField(max_length=30, default="Ótimo")
    middle_text = models.CharField(max_length=30, default="Regular")
    lower_limit_value = models.IntegerField(default=-5)
    upper_limit_value = models.IntegerField(default=5)
    middle_value = models.IntegerField(default=0)

    def __unicode__(self):
        return self.answer


class EVALQuestion(models.Model):
    """ Questions created on the system (could be or not enabled) """
    question = models.CharField(max_length=200)
    answer = models.ForeignKey('EVALAnswerModel')
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.question


class EVALAnswer(models.Model):
    """ Save the Evaluation made by the users """
    question = models.ForeignKey('EVALQuestion')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    bus_id = models.ForeignKey('Buses')  # unique ID of the bus
    answer_value = models.IntegerField(default=0)
    answer_text = models.TextField(blank=True)
    geolocation = models.PointField(default='POINT(-23.5475, -46.63611)')  # São Paulo geolocation

    def __unicode__(self):
        return self.user.name + " - " + self.question.question + " - " + str(self.timestamp)

    @staticmethod
    def _already_evaluated(self):
        evaluated_list = EVALAnswer.objects.filter(user=self.user, bus_id=self.bus_id, question=self.question)
        if evaluated_list:
            for evaluated in evaluated_list:
                #TODO: Período mínimo entre avaliações hardcoded
                if (self.timestamp - evaluated.timestamp) < datetime.timedelta(hours=1):
                    return True
                else:
                    return False
        else:
            return False

    @staticmethod
    def add_evaluation(self):
        """Adds the evaluation checking the uniquiness of user, bus_id, question and timestamp"""
        evaluated = self._already_evaluated(self)
        if evaluated:
            return False

