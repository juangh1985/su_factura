# Create your models here.
#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


from producto.models import *
from cliente.models import *


class tipo(models.Model):
	nombre=models.CharField('Tipo',max_length=30,blank=True,null=True)
	def __unicode__(self):
		return '%s' % (self.nombre)


class movimiento(models.Model):

	tipo=models.ForeignKey(tipo,max_length=30,blank=True,null=True)
	producto=models.ForeignKey(producto,max_length=30,blank=True,null=True)
	cliente=models.ForeignKey(Cliente,max_length=30,blank=True,null=True)
	cantidad=models.CharField('Cantidad',max_length=30,blank=True,null=True)
	importe=models.CharField('Importe',max_length=30,blank=True,null=True)
	pcosto=models.CharField('Precio de Costo',max_length=30,blank=True,null=True)
	actualizacion= models.DateTimeField('Actualizado',auto_now=True)
	confirmado = models.BooleanField('Confirmado', max_length = 256, blank=True)

	def __unicode__(self):
		return '%s' % (self.id)




