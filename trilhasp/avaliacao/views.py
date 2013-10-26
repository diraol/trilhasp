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
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from modelagem import models

import logging
from django.views.decorators.cache import cache_page

# Create your views here.

def verify_login(request):
    errors = []
    if request.method == 'POST':
    referer = request.META.get('HTTP_REFERER', 'unknown')
    host = request.get_host()
    if not referer == host + "/login/":
        errors.append('Tentativa ilegal de login')
        return HttpResponseRedirect(request,'login.html', { 'errors': errors }}
    else:
        errors.append('')
        return HttpResponseRedirect(request,'login.html', {
            'errors': errors,
        })

def recupera_linhas(request,lat, long, sentido):
    """Função que recupera as linhas de ônibus que estão próximas a uma determinada localidade no momento"""
    #Como ainda não há na API da SPTrans essa função foi utilizado um método alternativo que recupera as paradasde ônibus próximas à localidade do usuário e depois verificar quais são os ônibus estão próximos a elas.
    paradas_proximas = _recupera_pontos_por_localidade(lat,long)
    if not paradas_proximas:
        return render_to_response('insere_linha.html', {'linhas': None}, context_instance=RequestContext(request))
    else:
        linhas = _recupera_linhas_por_parada_ao_vivo(parada,sentido)
        return render_to_response('seleciona_linhas.html', {'linhas': linhas},

def _recupera_linhas_por_parada_ao_vivo(parada,sentido):
    """Função que recupera as linhas de ônibus que estão próximas a um determinado ponto de ônibus"""


def _recupera_paradas_por_localidade(lat,long,sentido):
    """Função que recupera paradas de ônibus próximas a uma determinada localidade"""
    #Recueprar via API

def avalia_linha(request

def salva_avaliacao_geral(
