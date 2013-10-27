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
from django.shortcuts import render

def index(request):
    return render(request, 'base.html', {})

