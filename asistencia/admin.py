# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from asistencia.models import *

class calendario_Admin(admin.ModelAdmin):
	pass
admin.site.register(calendario,calendario_Admin)
