# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from producto.models import *
from movimiento.models import *
from almacen.models import *
from movimiento.forms import *

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
from producto.models import *
from producto.forms import *
# Create your views here.


def producto_content(request):
	m = producto.objects.all()

	context = {	'producto':m, 
	}
	return render(request, 'producto-content.html', context)


def producto_form(request):
	if request.method=='POST':
		t = tipo.objects.filter(id=2)
		form_producto = formulario_producto(request.POST, request.FILES)
		if form_producto.is_valid():
			form = form_producto.save(commit=False)
			form.save()
			return HttpResponseRedirect('/producto_content')
	else:
		form_producto = formulario_producto()

	context = {
	'form_producto':form_producto, 

	}
	return render(request, 'producto-form.html', context)




def producto_delete(request):
	if request.method=='GET':
		var = request.GET.get('id')
		d=producto.objects.get(id=var)
		d.delete()
		return HttpResponseRedirect('/producto_content')
	else:
		return HttpResponseRedirect('/producto_content')




def producto_edit(request):
	var = request.GET.get('id')
	d=producto.objects.get(id=var)
	if request.method=='POST':
		form_producto = formulario_producto(request.POST, request.FILES, instance=d)
		if form_producto.is_valid():
			form = form_producto.save(commit=False)
			form.save()
			return HttpResponseRedirect('/producto_content')
	else:
		form_producto = formulario_producto(instance=d)
	context = {
	'd':d, 
	'form_producto':form_producto, 
	}
	return render(request, 'producto-form.html', context)

