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


def movimiento_content(request):
	m = movimiento.objects.all()

	context = {	'movimiento':m, 
	}
	return render(request, 'movimiento-content.html', context)


def movimiento_form(request):
	
	c = Cliente.objects.filter(estado=True)

	
	if request.method=='POST':
		t = tipo.objects.filter(id=2)
		form_movimiento = formulario_movimiento(request.POST, request.FILES)
		if form_movimiento.is_valid():
			form = form_movimiento.save(commit=False)
			form.tipo = t[0]
			form.confirmado = False
			form.importe = float(form.producto.pventa) * float(form.cantidad)
			form.pcosto = float(form.producto.pcosto) * float(form.cantidad)
			
			form.save()
			return HttpResponseRedirect('/movimiento_content')
	else:
		form_movimiento = formulario_movimiento()

	context = {
	'c':c, 
	'form_movimiento':form_movimiento, 

	}
	return render(request, 'movimiento-form.html', context)


def movimiento_delete(request):
	if request.method=='GET':
		var = request.GET.get('id')
		d=movimiento.objects.get(id=var)
		d.delete()
		return HttpResponseRedirect('/movimiento_content')
	else:
		return HttpResponseRedirect('/movimiento_content')


def movimiento_confirmar(request):
	if request.method=='GET':
		var = request.GET.get('id')
		d=movimiento.objects.get(id=var)
		d.confirmado = True
		d.save()
		return HttpResponseRedirect('/movimiento_content')
	else:
		return HttpResponseRedirect('/movimiento_content')



def movimiento_edit(request):
	var = request.GET.get('id')
	d=movimiento.objects.get(id=var)
	cl = Cliente.objects.get(id=d.cliente.id)
	if request.method=='POST':
		form_movimiento = formulario_movimiento(request.POST, request.FILES, instance=d)
		if form_movimiento.is_valid():
			form = form_movimiento.save(commit=False)
			form.importe = float(form.producto.pventa) * float(form.cantidad)
			form.pcosto = float(form.producto.pcosto) * float(form.cantidad)
			form.save()
			return HttpResponseRedirect('/movimiento_content')
	else:
		form_movimiento = formulario_movimiento(instance=d)
	context = {
	'cl':cl, 
	'd':d, 
	'form_movimiento':form_movimiento, 
	}
	return render(request, 'movimiento-form.html', context)









#~ def inicio(request):
	#~ t = tipo.objects.all()

	#~ m = movimiento.objects.all()


	#~ today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	#~ today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

	#~ m = movimiento.objects.filter(actualizacion__range=(today_min, today_max))


	#~ conteoi = tipo.objects.annotate(imp=Sum('movimiento__importe'))
	#~ conteoc = tipo.objects.annotate(cos=Sum('movimiento__pcosto'))


	#~ i=[]
	#~ for e in conteoi:
		#~ i= e.imp

	#~ c=[]
	#~ for e in conteoc:
		#~ c= e.cos



	#~ alma = existencia.objects.all()

	#~ return render_to_response('movimiento/inicio.html',{
	#~ 'movimiento':m,
	#~ 'conteoi':conteoi,
	#~ 'conteoc':conteoc,
	#~ 'tipo':t,
	#~ 'i':i,
	#~ 'c':c,
	#~ 'almacen':alma,
	#~ }, context_instance=RequestContext(request))



#~ def carta(request):
	#~ productos = producto.objects.filter(activo=True).order_by('-tipo')
	#~ if request.method=='POST':

		#~ id = request.POST.get('id_producto')
		#~ pro = producto.objects.get(id=id)

		#~ t = tipo.objects.filter(id=2)
		#~ form_movimiento = formulario_movimiento(request.POST, request.FILES)
		#~ if form_movimiento.is_valid():

			#~ form = form_movimiento.save(commit=False)
			#~ form.tipo = t[0]

			#~ form.producto = pro
			#~ form.importe = float(pro.pventa) * float(form.cantidad)
			#~ form.pcosto = float(pro.pcosto) * float(form.cantidad)
			
			#~ form.save()
			#~ return HttpResponseRedirect('/carta')
	#~ else:
		#~ form_movimiento = formulario_movimiento()
	#~ return render_to_response('movimiento/carta.html',{
	#~ 'form_movimiento':form_movimiento,
	#~ 'productos':productos,
	#~ } , context_instance=RequestContext(request))






#~ def listar(request):

	#~ import datetime
	#~ start_date = datetime.date(2016, 9, 5)
	#~ end_date = datetime.date(2016, 9, 6)

	#~ informe = movimiento.objects.filter(actualizacion__range=(start_date, end_date))
	#~ informe = movimiento.objects.all()




	#~ informe = movimiento.objects.all()
	#~ return render_to_response('movimiento/listar.html',{
	#~ 'informe':informe,
	#~ }, context_instance=RequestContext(request))




#~ def eliminar(request):
	#~ id = request.GET.get('id_movimiento')
	#~ auto = movimiento.objects.get(id=id)
	#~ auto.delete()
	#~ return HttpResponseRedirect('/listamovimiento')




#~ def agregar(request):
	#~ if request.method=='POST':
		#~ t = tipo.objects.filter(id=2)
		#~ form_movimiento = formulario_movimiento(request.POST, request.FILES)
		#~ if form_movimiento.is_valid():
			#~ form = form_movimiento.save(commit=False)
			#~ form.tipo = t[0]
			#~ form.importe = float(form.producto.pventa) * float(form.cantidad)
			#~ form.pcosto = float(form.producto.pcosto) * float(form.cantidad)
			
			#~ form.save()
			#~ return HttpResponseRedirect('/listamovimiento')
	#~ else:
		#~ form_movimiento = formulario_movimiento()
	#~ return render_to_response('movimiento/agregar.html',{'form_movimiento':form_movimiento} , context_instance=RequestContext(request))

