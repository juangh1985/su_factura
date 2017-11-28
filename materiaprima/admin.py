# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from materiaprima.models import *



class mprima_Admin(admin.ModelAdmin):
	pass
admin.site.register(mprima,mprima_Admin)


class tipo_Admin(admin.ModelAdmin):
	pass
admin.site.register(tipo,tipo_Admin)



class umedida_Admin(admin.ModelAdmin):
	pass
admin.site.register(umedida,umedida_Admin)
