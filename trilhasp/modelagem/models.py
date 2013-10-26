# coding=utf8
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

class Avaliacoes(models.Model):
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
    CB = "C/B"
    BC = "B/C"
    SENTIDOS = (
        (CB, "Centro-Bairro"),
        (BC, "Bairro-Centro"),
    )
    usuario = models.ForeignKey('Usuario')
    linha = models.ForeignKey('Onibus')
    sentido = models.CharField(max_length=60, choices=SENTIDOS, blank=False)
    pergunta = models.ForeignKey('Pergunta')
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    lat = models.DecimalFiedl(max_digits=9, decimal_places=6, blank=False)
    long = models.DecimalFiedl(max_digits=9, decimal_places=6, blank=False)
    resposta = models.CharField(max_length=255)

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




class Usuario(models.Model):
    """Usuários do sistema
        Atributos:
            nome -- string
            email -- email do usuário -> e login dele no facebook
        Métodos:
    """
    username = models.CharField(max_length=254, blank=False, unique=True)
    nome = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=250, blank=False, unique=True)
    facebook_flag = models.BooleanField(default=False)
    twitter_flag = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'username']
    USERNAME_FIELD = 'username'

class TiposMoedas(models.Model):
    """Tipos de moedas do sistema de remuneração de usuários
        Atributos:
            nome --  string
            valor -- int -- peso relativo da moeda - quantas vezes ela é mais valiosa que a unidade
            habilitada -- bool -- moeda disponível ou indisponível
        Métodos:
    """
    nome = models.CharField(max_length=120, blank=False, unique=True)
    valor = models.PositiveIntegerField(blank=False)
    habilitada = models.BooleanField(default=True)

class Financas(models.Model):
    """Classe que armazena as informações financeiras do usuário
        Atributos:
            usuario -- id do usuário (fk)
            moeda -- id da moeda (fk)
            quantidade -- int - quantidade de moedas que o usuário possui
        Métodos:
    """
    usuario = models.ForeignKey("Usuario")
    moeda = models.ForeignKey("TiposMoeda")
    quantidade = models.PositiveIntegerField(blank=False)

class Onibus(models.Model):
    """Classe que conterá as linhas de ônibus da cidade de São Paulo
        Atributos:
            linha -- string -- linha do ônibus em questão
            concessionaria -- string -- choice vindo da linha da concessionária

        Métodos:
    """
    CONCESSIONARIAS = (
        ("VS", "Via Sul"),
    )
    linha = models.CharField(max_length=15)
    concessionaria = models.CharField(max_length=150, choices=CONCESSIONARIAS)

class TiposOnibusPessoal(models.Model):
    """Classe com os tipos de ônibus que cada usuário pode comprar para sua própria frota
        Atributos:
            nome -- string -- nome do tipo de ônibus
            tipo (?) -- string -- choice dentro dos tipos de ônibus existentes
            modelo -- string -- choice do modelo de ônibus
            marca -- string -- choice da marca do ônibus
            quantidade_disponivel -- int -- quantidade de ônibus daquele modelo disponíveis para serem compradas
            rendimento -- int -- quantidade de moedas produzidas por esse modelo por unidade de tempo
            preco -- int -- preço de uma unidade desse modelo de ônibus.
        Métodos:
    """
    MERCEDES = "Merc"
    CAIO = "Caio"
    MARCAS = (
        (MERCEDES = "Mercedes Benz"),
        (CAIO = "CAIO"),
    )

    MODELOS = (
        ("1","CONVENCIONAL"),
        ("2","ALONGADO I"),
        ("3","ALONGADO II"),
        ("4","PADRON"),
        ("6","CONVENCIONAL"),
        ("7","BI-ARTICULADO"),
        ("8","ALONGADO I"),
        ("9","ONIBUS LEVE"),
        ("A","MONOBLOCO"),
        ("B","CONVENCIONAL"),
        ("C","ALONGADO I"),
        ("D","ALONGADO I"),
        ("E","ALONGADO II"),
        ("F","ALONGADO II"),
        ("G","PADRON"),
        ("H","PADRON"),
        ("I","ARTICULADO"),
        ("J","ESPECIAL"),
        ("K","PADRON III"),
        ("L","ONIBUS LEVE-VOL"),
        ("M","BI-ARTIC/MARTAO"),
        ("P","ONIBUS LEVE-VOL"),
        ("X","CONVENCIONAL"),
        ("Z","ALONGADO I"),
    )
    nome = models.CharField(max_length=30)
    #tipo = models.CharField(max_length=150, choices=TIPOS_DE_ONIBUS, blank=False)
    modelo = models.CharField(max_length=150, choices=MODELOS_DE_ONIBUS, blank=False)
    marca = models.CharField(max_length=150, choices=MARCAS_DE_ONIBUS, blank=False)
    quantidade_disponivel = models.PositiveIntegerField(blank=False)
    rendimento = models.PositiveIntegerField(blank=False)
    preco = models.PositiveIntegerField(blank=False)

class FrotaPessoal(models.Model):
    """Classe com informações da frota pessoal de cada usuário
        Atributos:
            usuario -- id do usuário (fk)
            onibus -- tipo do ônibus pessoal (fk)
            quantidade -- int -- número de ônibus que o usuário possui daquele modelo
            tempo para produzir -- tempo para a produção da próxima moeda
        Métodos:
    """
    usuario = models.ForeignKey("Usuario")
    onibus = models.ForeignKey("TiposOnibusPessoal")
    quantidade = models.PositiveIntegerField(blank=False)
    tempo_producao = models.PositiveIntegerField()

