# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from materiaprima.models import *

class tipo(models.Model):
	nombre=models.CharField('Tipo',max_length=30,blank=True,null=True)
	def __unicode__(self):
		return '%s' % (self.nombre)




class producto(models.Model):
	imagen = models.ImageField(upload_to='producto/', blank=True)
	nombre=models.CharField('Producto',max_length=30,blank=True,null=True)
	tipo=models.ForeignKey(tipo,max_length=30,blank=True,null=True)
	pcosto=models.CharField('Precio de Costo',max_length=30,blank=True,null=True)
	pventa=models.CharField('Precio de Venta',max_length=30,blank=True,null=True)
	fecha= models.DateTimeField('Fecha de Registro',auto_now=False, blank=True, null=True)
	actualizacion= models.DateTimeField('Actualizado',auto_now=True)
	observacion=models.TextField('Observacion',max_length=30,blank=True,null=True)
	activo = models.BooleanField('Activo', max_length=256, blank=True)

	def __unicode__(self):
		return '%s' % (self.nombre)


class ficha(models.Model):
	producto = models.ForeignKey(producto, related_name="productos")
	mprima = models.ForeignKey(mprima, related_name="MateriaPrima")
	norma=models.CharField('Norma',max_length=30,blank=True,null=True)
	pcosto=models.CharField('Precio de Costo',max_length=30,blank=True,null=True)
	pventa=models.CharField('Precio de Venta',max_length=30,blank=True,null=True)
	actualizacion= models.DateTimeField('Actualizado',auto_now=True)
	def __unicode__(self):
		return '%s' % (self.producto.nombre)
