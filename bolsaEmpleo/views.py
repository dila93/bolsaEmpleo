# -*- coding: cp1252 -*-
from django.shortcuts import render_to_response, redirect,render,get_object_or_404

from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login as auth_login , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from empleoApp.forms import *
import json
from django.core.mail import send_mail
import string
from pprint import pprint

def iniciar_sesion(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		clave = request.POST.get('password')
		print clave
		acceso = authenticate(username = username, password = clave)
		print acceso
		if acceso is not None:
			if acceso.is_active:
				auth_login(request,acceso)
			#request.session.set_expiry(60)	# 1 min
			login(request, acceso)
			#message="bien hecho tio"
			#return render_to_response('usuarios/login.html' ,{'message':message} , context_instance=RequestContext(request))
			return HttpResponseRedirect("/principal")
		else:
			#return HttpResponseRedirect('/index')
			return render_to_response('usuario/index.html',{'message':'no eres usuario'},context_instance=RequestContext(request))
	else:
		return render_to_response('usuario/index.html',{'formulario':formulario},context_instance=RequestContext(request))



def inicio(request):
	formulario = AuthenticationForm()
	return render_to_response('usuario/index.html',context_instance=RequestContext(request))

def Registro(request):	                                # pagina de inicio
        if request.method == 'POST':			# comprobamos si es una peticion post
                formulario = UserCreationForm(request.POST)

                response_data = {}
                if formulario.is_valid():
                        informacion = formulario.save(commit=False)
                        informacion.is_active=0
			informacion.save()
                        usuario = get_object_or_404(User, id=informacion.id)
                        form = RegistroForm(request.POST)
                        print 'usuario:'
                        if form.is_valid():					# guardo datos personales
                                print 'llega'
                                informacion = form.save(commit=False)
                                informacion.usuario = usuario
                                informacion.save()
                                form.save()


                                response_data['message'] = 1	# Datos guardados satisfactoriamente
                                return HttpResponse(json.dumps(response_data), content_type="application/json")
                        else:
                                print form.errors
                                response_data['message'] = form.errors		# formulario invalido, envio el error
                                return HttpResponse(json.dumps(response_data), content_type="application/json")
                else:
                        print formulario.errors
                        response_data['message'] = form.errors		# formulario invalido, envio el error
                        return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
                formulario = UserCreationForm()
                return render_to_response('usuario/registro.html',{'formulario':formulario}, context_instance=RequestContext(request))#[template_directory]/pregrep/index.html



def Recuperar_contrasena(request):	                # Envia el correo al usuario que perdio la contrasena
        if request.method == 'POST':			# comprobamos si es una peticion post
                correo=request.POST['username']
                usuarios = User.objects.all().filter(username=correo)
                print usuarios
                if usuarios:
                        for usuario in usuarios:
                                contrasena=usuario.password
                                id=usuario.id
                        link= 'http://127.0.0.1:8000/cambiar_pass/?usr='+str(id)+'&ps='+contrasena
                        send_mail('Recuperacion de password en bolsaEmpleo.com','Por Favor siga el siguiente enlace: '+link, 'bolsaempleo28gmail.com', [correo], fail_silently=False)
                        return render_to_response('usuario/recuperarContra1.html', context_instance=RequestContext(request))
                else:
                        print 'no accedi'
                        return render_to_response('usuario/RecuperarContra2.html', context_instance=RequestContext(request))
        else:
                return render_to_response('usuario/recuperarContrasena.html',context_instance=RequestContext(request))

def Cambiar_pass(request):
        if request.method == 'POST':			# comprobamos si es una peticion post
                print 'entre por post'
                usuario = get_object_or_404(User, username=request.POST.get('username'))
                usuario.set_password(request.POST.get('password1'))
                usuario.is_active=1
                usuario.save()
                response_data = {}
                response_data['message'] = 1	# Datos guardados satisfactoriamente
                return HttpResponse(json.dumps(response_data), content_type="application/json")

	else:
                idUsuario = request.GET.getlist('usr')
                ps = request.GET.getlist('ps')
                usuario = get_object_or_404(User, id=idUsuario[0])
                #print 'encontrado'
                #print len(ps[0])
                print usuario.password
                print 'otro'
                #print len(usuario.password)
                valido = True
                auxps = str(ps[0])

                newps=string.replace(auxps,' ','+')
                print newps
                if usuario.password == newps:
                        print 'las contrasenas coinciden'
                        return render_to_response('usuario/nuevoPassword.html',{'correo': usuario.username}, context_instance=RequestContext(request))
                else:
                        return render_to_response('usuario/nuevoPasswordFail.html', context_instance=RequestContext(request))

                return HttpResponse('hecho')


def cerrar_sesion(request):
	logout(request)
	print request
	return redirect('inicio')
