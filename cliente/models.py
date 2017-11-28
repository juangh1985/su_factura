# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Cliente(models.Model):

	cliente = models.CharField('Cliente', max_length = 256, blank=False, null=True)
	correo = models.CharField('Correo', max_length = 256, blank=False, null=True)
	telefono = models.CharField('Telefono de Contacto', max_length = 256, blank=False, null=True)
	direccion = models.CharField('Direccion', max_length = 256, blank=False, null=True)
	imagen = models.ImageField(upload_to='cliente/', blank=True)
	registro = models.DateTimeField('Registrado', auto_now=True)
	estado = models.BooleanField('Activo', max_length = 256, blank=True)
	empresa = models.BooleanField('Empresa', max_length = 256, blank=True)
	
	def __unicode__(self):
		return '%s' % (self.cliente)
