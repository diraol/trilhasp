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
    # Examples:
    url(r'^$', 'trilhasp.views.index', name='index'),
    url(r'^login$', 'trilhasp.views.loginpage', name='loginpage'),
    url(r'^logoutpage$', 'trilhasp.views.logoutpage', name='logoutpage'),
    url(r'^cadastro$', 'trilhasp.views.cadastro', name='cadastro'),
    url(r'^avaliar$', 'trilhasp.views.avaliar', name='avaliar'),
    url(r'^avaliar/especificas$', 'trilhasp.views.especificas', name='especificas'),
    url(r'^perfil$', 'trilhasp.views.perfil', name='perfil'),
    url(r'^explicacao$', 'trilhasp.views.explicacao', name='explicacao'),
    url(r'^fimavaliacao$', 'trilhasp.views.fimavaliacao', name='fimavaliacao'),
    url(r'^primeiraavaliacao$', 'trilhasp.views.primavali', name='primavali'),
    # url(r'^trilhasp/', include('trilhasp.foo.urls')),
    url(r'', include('modelagem.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
