#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trilhasp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^v1/evaluation/', include('evaluation.urls')),
    #url(r'^v1/user', include('utils.urls')),
    url(r'^v1/', include('utils.urls')),
    url(r'^$', 'evaluation.views.home', name='home'),  # to test social AUTH
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)
