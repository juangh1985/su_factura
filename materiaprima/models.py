# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

directorio_fotografias = '%s/%s'


class tipo(models.Model):
	nombre=models.CharField('Tipo',max_length=30,blank=True,null=True)
	def __unicode__(self):
		return '%s' % (self.nombre)


class umedida(models.Model):
	nombre=models.CharField('Unidad de Medida',max_length=30,blank=True,null=True)
	def __unicode__(self):
		return '%s' % (self.nombre)

class mprima(models.Model):
	imagen = models.ImageField(upload_to='mprima/', default="Materias Primas", blank=True, verbose_name="imagen")
	nombre=models.CharField('Producto',max_length=30,blank=True,null=True)
	tipo=models.ForeignKey(tipo,max_length=30,blank=True,null=True)
	umedida=models.ForeignKey(umedida,max_length=30,blank=True,null=True)
	pcosto=models.FloatField('Precio de Costo',max_length=30,blank=True,null=True)
	fecha= models.DateTimeField('Fecha de Registro',auto_now=False, blank=True, null=True)
	actualizacion= models.DateTimeField('Actualizado',auto_now=True)
	observacion=models.TextField('Observacion',max_length=30,blank=True,null=True)
	activo = models.BooleanField('Activo', max_length=256, blank=True)

	def __unicode__(self):
		return '%s' % (self.nombre)




