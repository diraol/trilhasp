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
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^cadastrar/$', 'modelagem.views.cadastrar', name='cadastrar'),
    url(r'^dologin$', 'modelagem.views.dologin', name='dologin'),
)
