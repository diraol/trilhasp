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
    url(r'^login$', 'trilhasp.views.login', name='login'),
    url(r'^cadastro$', 'trilhasp.views.cadastro', name='cadastro'),
    url(r'^escolhaLinha$', 'trilhasp.views.escolhelinha', name='escolhelinha'),
    url(r'^avaliacao/espec$', 'trilhasp.views.avaliaespec', name='avaliaespec'),
    url(r'^perfil$', 'trilhasp.views.perfil', name='perfil'),
    # url(r'^trilhasp/', include('trilhasp.foo.urls')),
    #url(r'^modelagem', include('modelagem.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
