from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bolaEmpleo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^be/', include(admin.site.urls)),
    url(r'^$', 'bolsaEmpleo.views.inicio', name='inicio'),
    url(r'^login/$', 'bolsaEmpleo.views.iniciar_sesion', name='iniciar_sesion'),
    url(r'^registro/$', 'bolsaEmpleo.views.Registro', name='Registro'),
    url(r'^logout/$', 'bolsaEmpleo.views.cerrar_sesion', name='cerrar_sesion'),
    url(r'^recuperar_contrasena/$', 'bolsaEmpleo.views.Recuperar_contrasena', name='Recuperar_contrasena'),
    url(r'^cambiar_pass/$', 'bolsaEmpleo.views.Cambiar_pass', name='Cambiar_pass'),

    url(r'^principal/$', 'empleoApp.views.Principal', name='Principal'),
    url(r'^listar_solicitudes/$', 'empleoApp.views.Listar_solicitudes', name='Listar_solicitudes'),
    url(r'^cambiar_estado_usuario/$', 'empleoApp.views.Cambiar_estado_usuario', name='Cambiar_estado_usuario'),

     #--------------------------------------------------------------------------------------------------------------------------------
    url(r'^Listar_Usuarios/$', 'empleoApp.views.Listar_Usuarios', name='Listar_Usuarios'),
    url(r'^Editar_Usuario/(?P<Id>\d+)/$','empleoApp.views.Editar_Usuario', name='Editar_Usuario'),
    url(r'^Borrar_Usuario/(?P<Id>\d+)/$','empleoApp.views.Borrar_Usuario', name='Borrar_Usuario'),


) #+ static(settings.MEDIA_URL) + static(document_root=settings.MEDIA_ROOT)
