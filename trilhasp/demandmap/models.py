#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.gis.db import models

#
###############################################################################
##                     Geolocation history data Classes                      ##
###############################################################################


class GEOLastPosition(models.Model):
    """This class stores the last location of each user
    It's used to show the users on the map. As it just stores one occurrence per
    user, it improves the performance of the map """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True)
    geolocation = models.PointField(default='POINT(-23.5475, -46.63611)')  # São Paulo geolocation
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)


class GEOHistoryPosition(models.Model):
    """This class stores all positions of each user. It will be used to generate
    statistics from the system and from the demand."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='positions')
    geolocation = models.PointField(default='POINT(-23.5475, -46.63611)')  # São Paulo geolocation
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        unique_together = ('user', 'timestamp')
