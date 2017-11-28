# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from cliente.models import *
from cliente.forms import *

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


def cliente_content(request):
	m = Cliente.objects.all()

	context = {	'cliente':m, 
	}
	return render(request, 'cliente-content.html', context)


def cliente_form(request):
	if request.method=='POST':
		form_cliente = formulario_cliente(request.POST, request.FILES)
		if form_cliente.is_valid():
			form = form_cliente.save(commit=False)
			form.save()
			return HttpResponseRedirect('/cliente_content')
	else:
		form_cliente = formulario_cliente()
	context = {'form_cliente':form_cliente,}
	return render(request, 'cliente-form.html', context)


def cliente_delete(request):
	if request.method=='GET':
		var = request.GET.get('id')
		d=Cliente.objects.get(id=var)
		d.delete()
		return HttpResponseRedirect('/cliente_content')
	else:
		return HttpResponseRedirect('/cliente_content')





def cliente_edit(request):
	var = request.GET.get('id')
	d=Cliente.objects.get(id=var)
	if request.method=='POST':
		form_cliente = formulario_cliente(request.POST, request.FILES, instance=d)
		if form_cliente.is_valid():
			form = form_cliente.save(commit=False)
			form.save()
			return HttpResponseRedirect('/cliente_content')
	else:
		form_cliente = formulario_cliente(instance=d)
	context = {
	'd':d, 
	'form_cliente':form_cliente, 
	}
	return render(request, 'cliente-form.html', context)

