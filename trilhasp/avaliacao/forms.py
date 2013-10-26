# -*- coding: utf-8 -*-
################################################################################
#                              Copyright (C) 2013                              #
#          Diego Rabatone Oliveira - <diraol(at)diraol(dot)eng(dot)br>         #
#                                                                              #
#    This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU Affero General Public License as published by  #
#      the Free Software Foundation, either version 3 of the License, or       #
#                     (at your option) any later version.                      #
#                                                                              #
#       This program is distributed in the hope that it will be useful,        #
#       but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#             GNU Affero General Public License for more details.              #
#                                                                              #
#  You should have received a copy of the GNU Affero General Public License    #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
################################################################################

from __future__ import unicode_literals
from django import forms
from datetime import datetime

CB = "C/B"
BC = "B/C"
SENTIDOS = (
    (CB, "Centro-Bairro"),
    (BC, "Bairro-Centro"),
)
class SelectSentido(forms.Form):
    long = forms.DecimalField(max_digits=9, decimal_places=6)
    lat = forms.DecimalField(max_digits=9, decimal_places=6)
    time = datetime.now()
    sentido = forms.ChoiceField(choices=SENTIDOS)


class SelecionaLinha(forms.Form):

