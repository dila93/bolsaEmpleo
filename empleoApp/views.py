# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
#importar modelos en caso de necestiar
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from Appi.forms import RegistroForm
from Appi.models import Usuario
from django.core.mail import send_mail
from django.contrib.auth.models import User
import smtplib



@login_required
def principal(request):	#pagina de inicio
        if request.user.is_staff:
                return render_to_response('usuario/principal.html' ,context_instance=RequestContext(request))#[template_directory]/pregrep/index.html
        else:
                usuarios = get_object_or_404(Usuario, usuario=request.user.id)
                return render_to_response('usuario/principal.html',{'usuarios': usuarios} ,context_instance=RequestContext(request))#[template_directory]/pregrep/index.html


@login_required
def listarSolicitudes(request):
        if request.user.is_staff:
                user=User.objects.all().filter(is_active=True)
                usuarios = Usuario.objects.all().filter(usuario=user)
                return render_to_response('usuario/listarUsuarios.html',{'usuarios': usuarios}, context_instance=RequestContext(request))#[template_directory]/pregrep/index.html

@login_required
def cambiarEstadoUsuario(request):
        if request.user.is_staff:
                print 'entre'
                estado= request.POST['estado']
                numero= request.POST['usuario']
                perfil = request.POST['perfil']
                print perfil
                response_data = {}
                cliente = get_object_or_404(Usuario, numero=numero)
                #mensaje='Reciba un caluroso saludo de nuestra parte; permítanos informarle que su cuenta de usuario en bolsaEmpleo.com se encuentra'
                if estado == 'Aprobado':
                        cliente.estado='Aprobado'
                        cliente.perfil=perfil
                        cliente.usuario.is_active=True
                        cliente.usuario.save()
                        cliente.save()
                        
                        response_data['message'] = 1    # Datos guardados satisfactoriamente
                        #aqui se debe enviar el correo electronico
                elif estado == 'Rechazado':
                        cliente.estado='Rechazado'
                        cliente.perfil=perfil
                        
                        print cliente.usuario.is_active
                        cliente.usuario.is_active =False
                        cliente.usuario.save()
                        cliente.save()
                        
                        response_data['message'] = 1    # Datos guardados satisfactoriamente
                        #aqui se debe enviar el correo electronico

                elif estado == 'En espera':
                        cliente.estado='En espera'
                        cliente.perfil=perfil
                        cliente.usuario.is_active=False
                        cliente.usuario.save()
                        cliente.save()

                        response_data['message'] = 1    # Datos guardados satisfactoriamente
                        #aqui se debe enviar el correo electronico

                print 'por aca llego la baina'
                print cliente.usuario.username
                send_mail('Estado de su cuenta en bolsaEmpleo.com','actualmente su cuenta se encuentra en estado: '+estado, 'bolsaempleo28gmail.com', [cliente.usuario.username], fail_silently=False)                       
                return HttpResponse(json.dumps(response_data), content_type="application/json")
                       

@login_required
def listarUsuarios(request):
        if request.user.is_staff:
                usuarios = Usuario.objects.filter(estado="Aprobado")
                return render_to_response('usuario/listaEditar.html',{'usuarios': usuarios}, context_instance=RequestContext(request))
         
@login_required
def editarUsuario(request,Id):
        persona = get_object_or_404(Usuario, id=Id)     # toma datos por GET, y saca el correspondiente en el modelo

        if request.method == 'POST': 
                form = RegistroForm(request.POST, instance=persona)
                response_data = {}
                if form.is_valid():

                        informacion = form.save(commit=False)
                        informacion.usuario.username = request.POST.get('usuario')
                        informacion.usuario.save()
                        informacion.save()
                
                response_data['message'] = 1    # Datos guardados satisfactoriamente
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
                return render_to_response('usuario/Editar_Usuario.html',{'persona': persona },context_instance=RequestContext(request))

@login_required
def borrarUsuario(request,Id):
        persona = get_object_or_404(Usuario, id=Id)     # toma datos por GET, y saca el correspondiente en el modelo

        if request.method == 'POST': 
                form = RegistroForm(request.POST, instance=persona)
                response_data = {}
                if form.is_valid():
                        print "paseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
                        informacion = form.save(commit=False)
                        informacion.usuario.is_active =False
                        informacion.usuario.save()
                        informacion.save()
                
                response_data['message'] = 1    # Datos guardados satisfactoriamente
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
                return render_to_response('usuario/Editar_Usuario.html',{'persona': persona },context_instance=RequestContext(request))


