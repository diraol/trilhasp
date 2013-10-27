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
# Create your views here.
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sptrans import v0 as SPTrans

TOKEN_SPTRANS='2be24b09b40618e0bc14c361657352cb5cf94f263f4dd98ae1dd0ed166f455a1'

def do_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(request, 'selecionaLinha.html', {})

    errors = []
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect(request, 'selecionaLinha.html', {})
        else:
            errors.append("User is not activated")
    else:
        errors.append("User not found or bad password")

    return HttpResponseRedirect(request, 'login.html', {'errors': errors})

def logout(request):
    logout(request)
    HttpResponseRedirect(request, 'index.html', {})

def createUser(request):
    error = []
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    email = request.POST.get('email', None)
    if username is not None:
        if password is not None:
            if email is not None:
                user = User.objects.create_user(username, email, password)
                user.save()
                return HttpResponseredirect(request, 'lista
            else:
                error.append("Email inválido")
        else:
            error.append("Password inválido")
    else:
        error.append("Username inválido")
    request.response

def logaApiSptrans():
    cliente = SPTrans.Client()
    cliente.authenticate(TOKEN_SPTRANS)

def recuperaLinhas(request):




















