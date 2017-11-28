# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from empleado.models import *
from asistencia.models import *
from asistencia.forms import *

from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, HttpRequest
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models import Count
import datetime



def asistencia_content(request):
	d = calendario.objects.all()
	context = {'d':d,
	}
	return render(request, 'components-calendar.html', context)


def asistencia_form(request):
	t = Trabajador.objects.all()

	if request.method=='POST':
		form_asistencia = formulario_asistencia(request.POST, request.FILES)
		if form_asistencia.is_valid():
			form = form_asistencia.save(commit=False)
			form.save()
			return HttpResponseRedirect('/asistencia_content')
	else:
		form_asistencia = formulario_asistencia()

	context = {
	't':t, 
	'form_asistencia':form_asistencia, 

	}
	return render(request, 'asistencia_form.html', context)
