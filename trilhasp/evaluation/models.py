#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.gis.db import models
import datetime, os


# Create your models here.

###############################################################################
##                     Classes for the buses                                 ##
###############################################################################

def get_company_logo_path(instance, filename):
    return os.path.join('images', 'buscompanies', filename)


class BusCompanies(models.Model):
    company_name = models.CharField(max_length=200, unique=True)
    logo = models.ImageField(upload_to=get_company_logo_path, blank=True, null=True)

    def __unicode__(self):
        return self.company_name


class BusLine(models.Model):
    """ This class contains all bus lines and their informations """
    bus_line_code = models.CharField(max_length=10)
    going_bus_name = models.CharField(max_length=200)
    return_bus_name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
     #Name of the company responsible for this bus line
    company_name = models.ForeignKey('BusCompanies', related_name='bus_lines')

    def __unicode__(self):
        return self.bus_line_code + " (" + self.going_bus_name + " / " + self.return_bus_name + ")"

    class Meta:
        unique_together = ('bus_line_code', 'active')


class Buses(models.Model):
    """ Class that represents each 'car' from the fleet """
    bus_unique_number = models.IntegerField(
        unique=True,
        primary_key=True,
        help_text='Número único do "carro" (ônibus), pintado na lateral do mesmo.',
        verbose_name='Bus Number'
    )
    bus_line_code = models.ForeignKey('BusLine', related_name='buses', limit_choices_to={'active':True})
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.bus_unique_number) + " (" + self.bus_line_code.bus_line_code + ")"

    class Meta:
        unique_together = ('bus_unique_number', 'active')

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
    answer = models.ForeignKey('EVALAnswerModel', related_name='questions')
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.question


class EVALAnswer(models.Model):
    """ Save the Evaluation made by the users """
    question = models.ForeignKey('EVALQuestion', related_name='evaluations', limit_choices_to={'enabled':True})
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='evaluations')
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    answer_value = models.IntegerField(default=0)
    answer_text = models.TextField(blank=True)
    bus_unique_number = models.ForeignKey(
        'Buses',
        related_name='evaluations',
        limit_choices_to={'active':True},
        to_field='bus_unique_number',
        help_text='Número único do "carro" (ônibus), pintado na lateral do mesmo.',
        verbose_name='Bus Number'
    )  # unique ID of the bus
    geolocation = models.PointField(default='POINT(-23.5475, -46.63611)')  # São Paulo geolocation

    def __unicode__(self):
        return self.user.username + " - " + self.question.question + " - " + str(self.timestamp)

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

