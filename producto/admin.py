# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from producto.models import *

class tipo_Admin(admin.ModelAdmin):
	pass
admin.site.register(tipo,tipo_Admin)


class ficha_Admin(admin.ModelAdmin):
	pass
admin.site.register(ficha,ficha_Admin)


class producto_Admin(admin.ModelAdmin):
	pass
admin.site.register(producto,producto_Admin)
