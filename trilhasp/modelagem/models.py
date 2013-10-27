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
import datetime

# Create your models here.
class Pergunta(models.Model):
    """Classe que definirá as perguntas e os tipos de resposta de cada pergunta.
        Atributos:
            pergunta -- string;
            tipo_resposta -- item da lista de tipos pré-definida
            habilitado -- booleano que define se a pergunta está ativa ou não no sistema
    """

    BINARIA="Bin"
    ESCALANUM="Quant"
    ESCALAQUALI="Quali"
    TIPOS_RESPOSTA = (
        (BINARIA, "Binária"),
        (ESCALANUM, "Escala Numérica"),
        (ESCALAQUALI, "Escala Qualitativa"),
    )

    pergunta = models.CharField(max_length=255, blank=False, unique=True)
    tipo_resposta = models.CharField(max_length=255, choices=TIPOS_RESPOSTA, blank=False, default=ESCALANUM)
    habilitado = models.BooleanField(default=False)

class Avaliacao(models.Model):
    """Classe de avaliação propriamente dita, que vai armazenar as avaliações feitas pelos usuários
        Atributos:
            usuario -- id do usuário que fez a avaliação (fk)
            linha -- id da linha de ônibus avaliada (fk)
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
    usuario = models.ForeignKey('Usuario')
    linha = models.ForeignKey('Onibus')
    sentido = models.CharField(max_length=60, choices=SENTIDOS, blank=False)
    pergunta = models.ForeignKey('Pergunta')
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    lat = models.DecimalFiedl(max_digits=9, decimal_places=6, blank=False)
    long = models.DecimalFiedl(max_digits=9, decimal_places=6, blank=False)
    resposta = models.IntegerField(blank=False)

    class Meta:
        unique_together=('usuario','linha','timestamp')

    @staticmethod
    def _ja_avaliado(self,usuario,linha,pergunta,timestamp)
        lista_avaliacoes = Avaliacoes.objects.filter(usuario=usuario,linha=linha,data=data,pergunta=pergunta)
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
    def adiciona_avaliacao(self,usuario,linha,sentido,pergunta,lat,long,resposta):
        """Adiciona a avaliação verificando a unicidade de usuario-linha-pergunta-timestamp"""
        timestamp = datetime.datetime.now()
        ja_avaliada = _ja_avaliada(usuario,linha,pergunta,timestamp)
        if ja_avaliada:
            return False

