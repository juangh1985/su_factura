# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from empleado.models import *



class Nom_Cargo_Trabajador_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Cargo_Trabajador,Nom_Cargo_Trabajador_Admin)


class Nom_Titulo_Trabajador_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Titulo_Trabajador,Nom_Titulo_Trabajador_Admin)



class Nom_Habilidad_Trabajador_Admin(admin.ModelAdmin):
	pass
admin.site.register(Nom_Habilidad_Trabajador,Nom_Habilidad_Trabajador_Admin)



class Trabajador_Admin(admin.ModelAdmin):
	pass
admin.site.register(Trabajador,Trabajador_Admin)



class Perfil_Admin(admin.ModelAdmin):
	pass
admin.site.register(Perfil,Perfil_Admin)



class Userlog_Admin(admin.ModelAdmin):
	pass
admin.site.register(Userlog,Userlog_Admin)
