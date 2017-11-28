# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from empleado.models import *

# Create your models here.
class calendario(models.Model):
	trabajador = models.ForeignKey(Trabajador, max_length = 256, blank=False)
	inicio= models.DateTimeField('Inicio: ', auto_now=False)
	fin= models.DateTimeField('Fin: ', auto_now=True)
	fecha= models.DateTimeField('Registrado el: ', auto_now=True)

