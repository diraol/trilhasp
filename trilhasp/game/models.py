#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
import os

###############################################################################
##                           Game module Classes                             ##
###############################################################################


class GameCoinModel(models.Model):
    """Models of coins of the game payment system
        Attributes:
            name --  string
            value -- int
            enabled -- bool
        Methods:
    """
    name = models.CharField(max_length=120, blank=False, unique=True)
    value = models.PositiveIntegerField(blank=False)
    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class GameFinance(models.Model):
    """Class that holds financial information from the users.
        Attributes:
            user -- user_id (fk)
            coin_type -- coin_type_id (fk)
            amount -- int -how many coins of this type the user have
        Method:
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='finances')
    coin_model = models.ForeignKey("GameCoinModel")
    amount = models.PositiveIntegerField(blank=False)

    class Meta:
        unique_together = ('user', 'coin_model')

    def __unicode__(self):
        return self.user.name + " (" + self.coin_model.name + ")"


def get_busbrand_logo_path(instance, filename):
    return os.path.join('images', 'brandlogos', filename)


class BusBrand(models.Model):
    #MERCEDES = "Merc"
    #CAIO = "Caio"
    #BRANDS = (
    #    (MERCEDES, "Mercedes Benz"),
    #    (CAIO, "CAIO"),
    #)
    label = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=get_busbrand_logo_path, blank=True, null=True)
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.label


class GameBusModel(models.Model):
    """Class with buses models. These are the buses that the users are going to buy to build their own fleet.
        Attributes:
            name -- string -- name of bus model
            model -- string -- choice of bus model
            brand -- string -- choice of bus brand
            efficiency -- int -- quantidade de moedas produzidas por esse modelo por unidade de tempo
            price -- int -- preço de uma unidade desse modelo de ônibus.
        Métodos:
    """

    #MODELS = (
    #    ("1", "CONVENCIONAL"),
    #    ("2", "ALONGADO I"),
    #    ("3", "ALONGADO II"),
    #    ("4", "PADRON"),
    #    ("6", "CONVENCIONAL"),
    #    ("7", "BI-ARTICULADO"),
    #    ("8", "ALONGADO I"),
    #    ("9", "ONIBUS LEVE"),
    #    ("A", "MONOBLOCO"),
    #    ("B", "CONVENCIONAL"),
    #    ("C", "ALONGADO I"),
    #    ("D", "ALONGADO I"),
    #    ("E", "ALONGADO II"),
    #    ("F", "ALONGADO II"),
    #    ("G", "PADRON"),
    #    ("H", "PADRON"),
    #    ("I", "ARTICULADO"),
    #    ("J", "ESPECIAL"),
    #    ("K", "PADRON III"),
    #    ("L", "ONIBUS LEVE-VOL"),
    #    ("M", "BI-ARTIC/MARTAO"),
    #    ("P", "ONIBUS LEVE-VOL"),
    #    ("X", "CONVENCIONAL"),
    #    ("Z", "ALONGADO I"),
    #)
    name = models.CharField(max_length=30)
    bus_brand = models.ManyToManyField(BusBrand, related_name='models')
    efficiency = models.PositiveIntegerField(blank=False)  # rendimento / yield
    price = models.PositiveIntegerField(blank=False)

    def __unicode__(self):
        return self.name + " (" + self.bus_brand.name + ")"


class GameBusAvailability(models.Model):
    """ Number of available buses to be bought """
    bus_model = models.ForeignKey(GameBusModel, unique=True)
    available_buses = models.PositiveIntegerField(blank=False)

    def __unicode__(self):
        return self.bus_model

class GamePersonalBusFleet(models.Model):
    """Class with personal fleet information
        Attributes:
            user -- (fk)
            bus_model -- tipo do ônibus pessoal (fk)
            amount -- int -- número de ônibus que o usuário possui daquele modelo
            time_to_return -- remaining time for the fleet to git coins back to the owner
        Methods:
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bus_fleet')
    bus_model = models.ForeignKey("GameBusModel")
    amount = models.PositiveIntegerField(blank=False)
    last_payment = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'bus_model')

    def __unicode__(self):
        return self.user + " (" + self.bus_model.name + ")"
