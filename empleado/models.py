# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

perfil = (
	('Visualizador', 'Visualizador'),
	('Editor', 'Editor'),
	
	)

directorio_fotografias = '%s/%s'

class Nom_Cargo_Trabajador(models.Model):

	cargo = models.CharField('Funciones', max_length = 256, blank=True, null=True)
	resposabilidad = models.TextField('Responsabilidad', max_length = 256, blank=True, null=True)
	
	def __unicode__(self):
		return '%s' % (self.cargo)

class Nom_Titulo_Trabajador(models.Model):

	titulo = models.CharField('Categoria Profecional', max_length = 256, blank=True, null=True)
	especialidad = models.TextField('Especialidad', max_length = 256, blank=True, null=True)
	
	def __unicode__(self):
		return '%s' % (self.titulo)

class Nom_Habilidad_Trabajador(models.Model):

	habilidad = models.CharField('Habilidad', max_length = 256, blank=True, null=True)
	descripcion = models.TextField('Descripcion', max_length = 256, blank=True, null=True)
	
	def __unicode__(self):
		return '%s' % (self.habilidad)


class Trabajador(models.Model):

	nombre = models.CharField('Nombre', max_length = 256, blank=False, null=True)
	imagen = models.ImageField(upload_to='empleado/', default="Empleado", blank=True, verbose_name="imagen")
	carne = models.CharField('Carne de Identidad', max_length = 256, blank=True, null=True)
	correo = models.EmailField('Correo electronico', max_length = 256, blank=False, null=True)
	direccion = models.CharField('Direccion', max_length = 256, blank=True, null=True)
	titulo = models.ForeignKey(Nom_Titulo_Trabajador, max_length = 256, blank=True, null=True)
	graduado = models.CharField('Graduado de ', max_length = 256, blank=True, null=True)
	telefono = models.CharField('Telefono', max_length = 256, blank=True, null=True)
	cargo = models.ManyToManyField(Nom_Cargo_Trabajador , blank=True)
	registro = models.DateTimeField('Registrado', auto_now=True)
	estado = models.BooleanField('Estado', max_length = 256, blank=True)
	
	def __unicode__(self):
		return '%s' % (self.nombre)

class Perfil(models.Model):
	user = models.OneToOneField(User, unique=True)
	trabajador = models.ForeignKey(Trabajador, max_length = 256, blank=True, related_name='perfil')

	def __unicode__(self):
		return '%s' % (self.user.id)

class Userlog(models.Model):
	usuario =  models.CharField(max_length=250, blank=True)
	unidad =  models.CharField(max_length=250, blank=True)
	departamento =  models.CharField(max_length=250, blank=True)
	trabajador =  models.CharField(max_length=250, blank=True)
	accion = models.CharField(max_length=250, blank=True)
	numaccion = models.IntegerField(blank=True)
	ip= models.CharField( max_length=250,blank=True)
	fecha= models.DateTimeField('Registrado el: ', auto_now=True)
	def __unicode__(self):
		return 'log del usuario %s el %s' % (self.user, self.fecha)
