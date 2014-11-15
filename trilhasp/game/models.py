#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

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


class GameFinances(models.Model):
    """Class that holds financial information from the users.
        Attributes:
            user -- user_id (fk)
            coin_type -- coin_type_id (fk)
            amount -- int -how many coins of this type the user have
        Method:
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    coin_model = models.ForeignKey("GameCoinModel")
    amount = models.PositiveIntegerField(blank=False)


class GameBusModel(models.Model):
    """Class with buses models. These are the buses that the users are going to buy to build their own fleet.
        Attributes:
            name -- string -- name of bus model
            model -- string -- choice of bus model
            brand -- string -- choice of bus brand
            available_buses -- int -- quantidade de ônibus daquele modelo disponíveis para serem compradas
            efficiency -- int -- quantidade de moedas produzidas por esse modelo por unidade de tempo
            price -- int -- preço de uma unidade desse modelo de ônibus.
        Métodos:
    """
    MERCEDES = "Merc"
    CAIO = "Caio"
    BRANDS = (
        (MERCEDES, "Mercedes Benz"),
        (CAIO, "CAIO"),
    )

    MODELS = (
        ("1", "CONVENCIONAL"),
        ("2", "ALONGADO I"),
        ("3", "ALONGADO II"),
        ("4", "PADRON"),
        ("6", "CONVENCIONAL"),
        ("7", "BI-ARTICULADO"),
        ("8", "ALONGADO I"),
        ("9", "ONIBUS LEVE"),
        ("A", "MONOBLOCO"),
        ("B", "CONVENCIONAL"),
        ("C", "ALONGADO I"),
        ("D", "ALONGADO I"),
        ("E", "ALONGADO II"),
        ("F", "ALONGADO II"),
        ("G", "PADRON"),
        ("H", "PADRON"),
        ("I", "ARTICULADO"),
        ("J", "ESPECIAL"),
        ("K", "PADRON III"),
        ("L", "ONIBUS LEVE-VOL"),
        ("M", "BI-ARTIC/MARTAO"),
        ("P", "ONIBUS LEVE-VOL"),
        ("X", "CONVENCIONAL"),
        ("Z", "ALONGADO I"),
    )
    name = models.CharField(max_length=30)
    bus_model = models.CharField(max_length=150, choices=MODELS, blank=False)
    bus_brand = models.CharField(max_length=150, choices=BRANDS, blank=False)
    available_buses = models.PositiveIntegerField(blank=False)
    efficiency = models.PositiveIntegerField(blank=False)  # rendimento / yield
    price = models.PositiveIntegerField(blank=False)


class GamePersonalFleet(models.Model):
    """Class with personal fleet information
        Attributes:
            user -- (fk)
            bus_model -- tipo do ônibus pessoal (fk)
            amount -- int -- número de ônibus que o usuário possui daquele modelo
            time_to_return -- remaining time for the fleet to git coins back to the owner
        Methods:
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    bus_model = models.ForeignKey("GameBusModel")
    amount = models.PositiveIntegerField(blank=False)
    time_to_return = models.PositiveIntegerField()
