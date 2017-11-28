# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from almacen.models import *






class existencia_Admin(admin.ModelAdmin):
	pass
admin.site.register(existencia,existencia_Admin)




class tipo_Admin(admin.ModelAdmin):
	pass
admin.site.register(tipo,tipo_Admin)




class movimiento_Admin(admin.ModelAdmin):
	pass
admin.site.register(movimiento,movimiento_Admin)
