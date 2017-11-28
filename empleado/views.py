# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from empleado.models import *
from empleado.forms import *

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


def inicio(request):

	context = {
	}
	return render(request, 'inicio.html', context)


def empleado_content(request):
	m = Trabajador.objects.all()
	print "hola"

	context = {	'empleado':m, 
	}
	return render(request, 'empleado-content.html', context)


def empleado_form(request):
	if request.method=='POST':
		form_empleado = formulario_empleado(request.POST, request.FILES)
		if form_empleado.is_valid():
			form = form_empleado.save(commit=False)
			form.save()
			return HttpResponseRedirect('/empleado_content')
	else:
		form_empleado = formulario_empleado()

	context = {
	'form_empleado':form_empleado, 

	}
	return render(request, 'empleado-form.html', context)



def empleado_delete(request):
	if request.method=='GET':
		var = request.GET.get('id')
		d=Trabajador.objects.get(id=var)
		d.delete()
		return HttpResponseRedirect('/empleado_content')
	else:
		return HttpResponseRedirect('/empleado_content')


def empleado_edit(request):
	var = request.GET.get('id')
	d=Trabajador.objects.get(id=var)
	if request.method=='POST':
		form_empleado = formulario_empleado(request.POST, request.FILES, instance=d)
		if form_empleado.is_valid():
			form = form_empleado.save(commit=False)
			form.save()
			return HttpResponseRedirect('/empleado_content')
	else:
		form_empleado = formulario_empleado(instance=d)
	context = {
	'd':d, 
	'form_empleado':form_empleado, 
	}
	return render(request, 'empleado-form.html', context)

