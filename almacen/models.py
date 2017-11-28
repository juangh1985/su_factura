# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#!/usr/bin/python
# -*- coding: utf-8 -*-

from materiaprima.models import *


class existencia(models.Model):

	materia=models.ForeignKey(mprima,max_length=30,blank=True,null=True)
	existencia=models.CharField('Existencia',max_length=30,blank=True,null=True)
	actualizacion= models.DateTimeField('Actualizado',auto_now=True)

	def __unicode__(self):
		return '%s' % (self.materia)


class tipo(models.Model):
	nombre=models.CharField('Tipo',max_length=30,blank=True,null=True)
	def __unicode__(self):
		return '%s' % (self.nombre)


class movimiento(models.Model):

	tipo=models.ForeignKey(tipo,max_length=30,blank=True,null=True)
	materia=models.ForeignKey(mprima,max_length=30,blank=True,null=True)
	cantidad=models.CharField('Cantidad',max_length=30,blank=True,null=True)
	importe=models.CharField('Importe',max_length=30,blank=True,null=True)
	pcosto=models.CharField('Precio de Costo',max_length=30,blank=True,null=True)
	actualizacion= models.DateTimeField('Actualizado',auto_now=True)

	def __unicode__(self):
		return '%s' % (self.materia)
