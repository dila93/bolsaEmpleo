from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

class Usuario(models.Model):

	usuario = models.ForeignKey(User)
	tipo_user = models.CharField(max_length=50)
	numero_user = models.CharField(max_length=50, unique=True)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=20, null=True, blank=True)
	fecha_nacimiento = models.CharField(max_length=20, null=True, blank=True)

	estado= models.CharField(max_length=30, default='En espera')
	perfil= models.CharField(max_length=30, default='Indefinido')
	activo = models.BooleanField(default=True)		#activo o inactivo
	fecha_registro = models.DateTimeField(auto_now=True)	#fecha de registro

	def __unicode__(self):
		return self.numero
