# coding=utf8
################################################################################
#                              Copyright (C) 2013                              #
#         Diego Rabatone Oliveira - <diraol(at)diraol(dot)eng(dot)br>          #
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
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Pergunta(models.Model):
    """Classe que definirá as perguntas e os tipos de resposta de cada pergunta.
        Atributos:
            pergunta -- string;
            extremo_negativo -- string
            centro -- string
            extremo_positivo -- string
            habilitado -- booleano que define se a pergunta está ativa ou não no sistema
    """
    pergunta = models.CharField(max_length=255, blank=False, unique=True)
    extremo_negativo = models.CharField(max_length=50, blank=False)
    centro = models.CharField(max_length=50, blank=False)
    extremo_positivo = models.CharField(max_length=50, blank=False)
    habilitado = models.BooleanField(default=False)
    orgem = models.IntegerField(unique=True)

class Avaliacao(models.Model):
    """Classe de avaliação propriamente dita, que vai armazenar as avaliações feitas pelos usuários
        Atributos:
            user -- id do usuário que fez a avaliação (fk)
            linha -- id da linha de ônibus
            prefixo -- Prefixo do ônibus (identificador único do carro)
            sentido -- sentido da linha (centro/bairro - bairro/centro)
            pergunta -- id da pergunta sendo respondida (fk)
            timestamp -- datetime.datetime -- dia da avaliação
            long -- float -- longitude do usuário no momento da avaliação
            lat -- float -- latitude do usuário no momento da avaliação
            resposta -- string(?) -- resposta dada à pergunta
    """
    SENTIDOS = (
    ("TPTS", "Term. Primário -> Term. Secundário"),
    ("TSTP", "Term. Secundário -> Term. Primário"),
    )
    user = models.ForeignKey(User)
    linha = models.CharField(max_length=30, blank=False)
    prefixo = models.CharField(max_length=30)
    sentido = models.IntegerField()
    pergunta = models.ForeignKey('Pergunta')
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=False)
    long = models.DecimalField(max_digits=9, decimal_places=6, blank=False)
    resposta = models.IntegerField(blank=False)

    class Meta:
        unique_together=('user','linha','timestamp')

    @staticmethod
    def _ja_avaliado(self,user,linha,pergunta,timestamp):
        lista_avaliacoes = Avaliacoes.objects.filter(user=user,linha=linha,data=data,pergunta=pergunta)
        if lista_avaliacoes:
            for avaliacao in lista_avaliacoes:
                #TODO: Período mínimo entre avaliações hardcoded
                if (timestamp - avaliacao.timestamp) < datetime.timedelta(hour=1):
                    return True
                else:
                    return False
        else:
            return False

    @staticmethod
    def adiciona_avaliacao(self,user,linha,sentido,pergunta,lat,long,resposta):
        """Adiciona a avaliação verificando a unicidade de user-linha-pergunta-timestamp"""
        timestamp = datetime.datetime.now()
        #ja_avaliada = _ja_avaliada(user,linha,pergunta,timestamp)
        #if ja_avaliada:
        #    return False


class Onibus(models.Model):

    route_id = models.CharField(max_length=30)
    trip_id = models.CharField(max_length=30, unique=True)
    trip_headsign = models.CharField(max_length=250)
    direction_id = models.BooleanField() #0 = TPTS ; 1 = TSTP

