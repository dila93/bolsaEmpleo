from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bolaEmpleo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bolsaEmpleo.views.inicio', name='inicio'),
    url(r'^login/$', 'bolsaEmpleo.views.iniciarSesion', name='login'),
    url(r'^registro/$', 'bolsaEmpleo.views.registro', name='registro'),
    url(r'^logout/$', 'bolsaEmpleo.views.cerrarSesion', name='logout'),
    url(r'^recuperar_contrasena/$', 'bolsaEmpleo.views.recuperarContrasena', name='recuperarContrasena'),
    url(r'^cambiar_pass/$', 'bolsaEmpleo.views.cambiarPass', name='cambiarPassword'),

    url(r'^principal/$', 'empleoApp.views.principal', name='principal'),
    url(r'^listar_solicitudes/$', 'empleoApp.views.listarSolicitudes', name='ListarSolicitudes'),
    url(r'^cambiar_estado_usuario/$', 'empleoApp.views.cambiarEstadoUsuario', name='CambiarEstadoUsuario'),

     #--------------------------------------------------------------------------------------------------------------------------------
    url(r'^Listar_Usuarios/$', 'empleoApp.views.listarUsuarios', name='ListarUsuarios'),
    url(r'^Editar_Usuario/(?P<Id>\d+)/$','empleoApp.views.editarUsuario', name='EditUsuario'),
    url(r'^Borrar_Usuario/(?P<Id>\d+)/$','empleoApp.views.borrarUsuario', name='BorrarUsuario'),    
    

) + static(settings.MEDIA_URL) + static(document_root=settings.MEDIA_ROOT)
