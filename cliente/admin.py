# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from cliente.models import *

class cliente_Admin(admin.ModelAdmin):
	pass
admin.site.register(Cliente,cliente_Admin)
