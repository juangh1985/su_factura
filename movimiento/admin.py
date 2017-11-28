# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from movimiento.models import *

class tipo_Admin(admin.ModelAdmin):
	pass
admin.site.register(tipo,tipo_Admin)



class movimiento_Admin(admin.ModelAdmin):
	pass
admin.site.register(movimiento,movimiento_Admin)
